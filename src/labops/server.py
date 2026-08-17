from fastapi import FastAPI
app = FastAPI()


@app.post("/reports")
def receive_report(report: dict):
    received={"status": "received"}
    return received
