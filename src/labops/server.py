from fastapi import FastAPI, HTTPException, status
from labops.models import Report, StoredReport
from datetime import datetime, UTC
from uuid import uuid4,UUID
app = FastAPI()

received_reports: list[StoredReport] = []

@app.post("/reports")
def receive_report(report: Report):
    report_store = StoredReport(
        id=uuid4(),
        stored_at=datetime.now(UTC),
        report=report
        )

    received_reports.append(report_store)

    received={
        "id": report_store.id,
        "time": report_store.stored_at,
        "status": "received",
        "hostname": report.system.hostname,
        "health": report.health.overall_status
        }

    return received

@app.get("/reports")
def get_reports() -> list[StoredReport]:
    return received_reports

@app.get("/reports/{report_id}")
def get_report_by_id(report_id: UUID):
    for report_store in received_reports:
        if report_store.id == report_id:
            return report_store

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Report not found"
        )

@app.get("/hosts/{hostname}/reports")
def get_reports_by_host(hostname: str):
    host_reports :list[StoredReport]= []
    for report in received_reports:
        if report.report.system.hostname == hostname:
            host_reports.append(report)

    if host_reports:
        return host_reports
    else: 
            raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Reports not found for Hostname: {hostname} "
        )