from fastapi import FastAPI
app = FastAPI()


@app.post("/reports")
def receive_report(report: dict):
    received={
        "status": "received",
        "hostname": report['system']['hostname'],
        "health": report['health']['overall_status']
        }
    return received
