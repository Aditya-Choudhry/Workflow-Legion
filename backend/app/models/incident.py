from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field


AgentName = Literal[
    "triage",
    "threat_intel",
    "forensics",
    "compliance",
    "commander",
]


class EvidenceItem(BaseModel):
    evidence_id: str
    category: str
    summary: str
    source: str
    confidence: str


class TimelineEvent(BaseModel):
    order: int
    time: str
    actor: str
    action: str
    significance: str


class AgentFinding(BaseModel):
    agent: AgentName
    status: Literal["pending", "complete", "failed"] = "pending"
    summary: str
    confidence: str
    severity: str | None = None
    evidence: list[EvidenceItem] = Field(default_factory=list)
    timeline: list[TimelineEvent] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    band_message: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FinalReport(BaseModel):
    incident_id: str
    executive_summary: str
    severity: str
    commander_decision: str
    evidence_summary: list[str]
    timeline_summary: list[str]
    compliance_notes: list[str]
    recommended_actions: list[str]
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class IncidentState(BaseModel):
    incident_id: str
    title: str
    status: Literal["ready", "running", "complete", "failed"]
    severity: str
    affected_host: str
    affected_user: str
    department: str
    summary: str
    indicators: dict[str, str]
    findings: list[AgentFinding] = Field(default_factory=list)
    final_report: FinalReport | None = None
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

