from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"status": "ok", "service": "workflow-legion-api"}


@app.get("/api/incidents/wl-inc-001")
def get_demo_incident():
    return {
        "incident_id": "WL-INC-001",
        "title": "Suspicious PowerShell Activity and Possible Data Exfiltration",
        "status": "ready",
        "severity": "pending",
        "affected_host": "FIN-042",
        "affected_user": "j.morgan",
        "band_priority": "Band must coordinate visible agent handoffs.",
    }
