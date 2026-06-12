from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.core.settings import settings
from app.models.incident import IncidentState
from app.services.band_client import BandClient, BandConfigurationError, BandDeliveryResult
from app.services.deterministic_agents import run_deterministic_workflow
from app.services.final_report import build_final_report
from app.services.incident_repository import DEMO_INCIDENT_ID, incident_repository


class StartIncidentRequest(BaseModel):
    reset: bool = True
    post_to_band: bool = False


class TestBandMessageRequest(BaseModel):
    content: str = "Workflow Legion test: Triage Agent online."


class WorkflowRunResponse(BaseModel):
    incident: IncidentState
    band_delivery: list[BandDeliveryResult]


app = FastAPI(
    title="Workflow Legion API",
    description="Band-native cyber incident command room backend.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "workflow-legion-api",
        "band_configured": bool(settings.band_chat_id and settings.band_triage_agent_api_key),
    }


@app.get("/api/incidents/wl-inc-001")
def get_demo_incident():
    incident = incident_repository.get(DEMO_INCIDENT_ID)
    if incident is None:
        raise HTTPException(status_code=404, detail="Demo incident not found.")
    return incident


@app.post("/api/incidents/wl-inc-001/reset")
def reset_demo_incident():
    return incident_repository.reset_demo()


@app.post("/api/incidents/wl-inc-001/start", response_model=WorkflowRunResponse)
async def start_demo_incident(request: StartIncidentRequest):
    incident = incident_repository.reset_demo() if request.reset else incident_repository.get(DEMO_INCIDENT_ID)
    if incident is None:
        raise HTTPException(status_code=404, detail="Demo incident not found.")

    incident.status = "running"
    incident_repository.upsert(incident)

    findings = run_deterministic_workflow(
        incident,
        threat_handle=settings.band_threat_intel_handle,
        forensics_handle=settings.band_forensics_handle,
        compliance_handle=settings.band_compliance_handle,
        commander_handle=settings.band_commander_handle,
    )
    report = build_final_report(incident, findings)
    completed_incident = incident_repository.replace_findings(incident.incident_id, findings, report)
    if completed_incident is None:
        raise HTTPException(status_code=404, detail="Demo incident not found.")

    band_delivery: list[BandDeliveryResult] = []
    if request.post_to_band:
        band_delivery = await _post_workflow_to_band([finding.band_message for finding in findings])

    return WorkflowRunResponse(incident=completed_incident, band_delivery=band_delivery)


@app.get("/api/incidents/wl-inc-001/report")
def get_demo_incident_report():
    incident = incident_repository.get(DEMO_INCIDENT_ID)
    if incident is None:
        raise HTTPException(status_code=404, detail="Demo incident not found.")
    if incident.final_report is None:
        raise HTTPException(status_code=404, detail="Final report has not been generated yet.")
    return incident.final_report


@app.post("/api/band/test-message", response_model=BandDeliveryResult)
async def send_band_test_message(request: TestBandMessageRequest):
    client = _build_triage_band_client()
    try:
        return await client.send_text_message(_required_band_chat_id(), request.content)
    except BandConfigurationError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc


def _build_triage_band_client() -> BandClient:
    return BandClient(
        base_url=settings.band_base_url,
        agent_api_key=settings.band_triage_agent_api_key,
    )


def _required_band_chat_id() -> str:
    if not settings.band_chat_id:
        raise BandConfigurationError("Band chat ID is not configured.")
    return settings.band_chat_id


async def _post_workflow_to_band(messages: list[str]) -> list[BandDeliveryResult]:
    client = _build_triage_band_client()
    chat_id = _required_band_chat_id()
    delivery: list[BandDeliveryResult] = []

    try:
        for message in messages:
            delivery.append(await client.send_text_message(chat_id, message))
    except BandConfigurationError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    return delivery
