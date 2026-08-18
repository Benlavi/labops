from fastapi import FastAPI
from labops.models import Report, StoredReport
from datetime import datetime, UTC
app = FastAPI()

received_reports: list[StoredReport] = []

@app.post("/reports")
def receive_report(report: Report):
    report_store = StoredReport(
        report=report,
        stored_at=datetime.now(UTC)
        )

    received_reports.append(report_store)

    received={
        "status": "received",
        "hostname": report.system.hostname,
        "health": report.health.overall_status
        }

    return received

@app.get("/reports")
def get_reports() -> list[StoredReport]:
    return received_reports