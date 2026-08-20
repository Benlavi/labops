from fastapi import FastAPI, HTTPException, status
from labops.models import Report, StoredReport
from datetime import datetime, UTC
from uuid import uuid4,UUID
from labops import storage
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    storage.init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/reports")
def receive_report(report: Report):
    report_store = StoredReport(
        id=uuid4(),
        stored_at=datetime.now(UTC),
        report=report
        )
    storage.save_report(report_store)
    

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
    return storage.get_reports()

@app.get("/reports/{report_id}")
def get_report_by_id(report_id: UUID):
    received_report= storage.get_report_by_uuid(report_id)
    if received_report != None:
         return received_report
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Report not found"
        )

@app.get("/hosts/{hostname}/reports")
def get_reports_by_host(hostname: str):
    received_reports= storage.get_reports_by_hostname(hostname)

    if received_reports:
        return received_reports

    raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f"Reports not found for Hostname: {hostname} "
    )