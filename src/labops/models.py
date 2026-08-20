from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class SystemInfo(BaseModel):

    hostname: str
    os_name: str
    kernel_version: str
    uptime_seconds: float

class HealthInfo(BaseModel):
    memory_percent: float
    disk_percent: float
    memory_status: str
    disk_status: str
    overall_status: str

class DiskInfo(BaseModel):
    total_gb: float 
    used_gb: float 
    free_gb: float 
    percent: float

class NetworkInterfaceInfo(BaseModel):
    IPv4: str | None = None
    IPv6: str |  None = None
    MAC: str |  None = None
    status: str | None = None


class Report(BaseModel):
    system: SystemInfo
    disk: DiskInfo
    network: dict[str, NetworkInterfaceInfo]
    health: HealthInfo

class StoredReport(BaseModel):
    id: UUID
    stored_at: datetime
    report: Report
    