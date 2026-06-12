from copy import deepcopy
from datetime import datetime, timezone
from threading import RLock

from app.models.incident import AgentFinding, FinalReport, IncidentState


DEMO_INCIDENT_ID = "WL-INC-001"


def build_demo_incident() -> IncidentState:
    return IncidentState(
        incident_id=DEMO_INCIDENT_ID,
        title="Suspicious PowerShell Activity and Possible Data Exfiltration",
        status="ready",
        severity="pending",
        affected_host="FIN-042",
        affected_user="j.morgan",
        department="Finance",
        summary=(
            "Suspicious PowerShell execution on a finance workstation, followed by "
            "failed login attempts, outbound traffic, and sensitive file access."
        ),
        indicators={
            "process": "powershell.exe",
            "file": "invoice_update.exe",
            "destination_ip": "185.199.108.153",
            "target_file": "finance_q4_forecast.xlsx",
        },
    )


class IncidentRepository:
    def __init__(self) -> None:
        self._lock = RLock()
        self._incidents: dict[str, IncidentState] = {
            DEMO_INCIDENT_ID: build_demo_incident(),
        }

    def reset_demo(self) -> IncidentState:
        with self._lock:
            incident = build_demo_incident()
            self._incidents[DEMO_INCIDENT_ID] = incident
            return deepcopy(incident)

    def get(self, incident_id: str) -> IncidentState | None:
        with self._lock:
            incident = self._incidents.get(incident_id)
            return deepcopy(incident) if incident else None

    def upsert(self, incident: IncidentState) -> IncidentState:
        with self._lock:
            incident.updated_at = datetime.now(timezone.utc)
            self._incidents[incident.incident_id] = deepcopy(incident)
            return deepcopy(incident)

    def replace_findings(
        self,
        incident_id: str,
        findings: list[AgentFinding],
        final_report: FinalReport,
    ) -> IncidentState | None:
        with self._lock:
            incident = self._incidents.get(incident_id)
            if incident is None:
                return None

            incident.status = "complete"
            incident.severity = final_report.severity
            incident.findings = findings
            incident.final_report = final_report
            incident.updated_at = datetime.now(timezone.utc)
            self._incidents[incident_id] = deepcopy(incident)
            return deepcopy(incident)


incident_repository = IncidentRepository()

