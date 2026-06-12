from app.models.incident import AgentFinding, FinalReport, IncidentState


def build_final_report(incident: IncidentState, findings: list[AgentFinding]) -> FinalReport:
    evidence_summary: list[str] = []
    timeline_summary: list[str] = []
    compliance_notes: list[str] = []
    recommended_actions: list[str] = []

    for finding in findings:
        for evidence in finding.evidence:
            evidence_summary.append(f"{evidence.evidence_id}: {evidence.summary}")
        for event in finding.timeline:
            timeline_summary.append(f"{event.time}: {event.action} - {event.significance}")
        if finding.agent == "compliance":
            compliance_notes.extend(finding.recommended_actions)
        recommended_actions.extend(finding.recommended_actions)

    deduped_actions = list(dict.fromkeys(recommended_actions))

    return FinalReport(
        incident_id=incident.incident_id,
        executive_summary=(
            "Workflow Legion agents assessed suspicious PowerShell activity on FIN-042 "
            "with follow-on login failures, sensitive finance file access, and outbound "
            "traffic. The coordinated finding is suspected endpoint compromise with "
            "possible data exposure."
        ),
        severity="high",
        commander_decision=(
            "Contain FIN-042, protect the affected identity, preserve evidence, and continue "
            "exfiltration scoping before external notification decisions."
        ),
        evidence_summary=evidence_summary,
        timeline_summary=timeline_summary,
        compliance_notes=compliance_notes,
        recommended_actions=deduped_actions,
    )

