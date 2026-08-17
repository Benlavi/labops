import httpx

def send_report(report_dict: dict, server_url: str) -> httpx.Response:
    response = httpx.post(server_url, json=report_dict)
    response.raise_for_status()
    return response
