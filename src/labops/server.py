from fastapi import FastAPI
from labops.models import Report
app = FastAPI()


@app.post("/reports")
def receive_report(report: Report):
    received={
        "status": "received",
        "hostname": report.system.hostname,
        "health": report.health.overall_status
        }
    return received
