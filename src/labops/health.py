import json
import psutil
from labops.disk import get_disk_usage

def get_status(percent: float) -> str:
    if percent < 80:
        return "OK"
    elif percent < 90:
        return "WARNING"
    else:
        return "CRITICAL"



def get_system_health() -> dict[str, str | float]:
    disk_percent = get_disk_usage()["percent"]
    memory_percent = psutil.virtual_memory().percent
    overall = max (disk_percent, memory_percent)
    system_health = {
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "memory_status": get_status(memory_percent),
        "disk_status": get_status(disk_percent),
        "overall_status": get_status(overall)
    }
    return system_health

def show_system_health(health_dict: dict) -> None:
    
    print("=== System Health Information ===")
    print(f"Memory Usage: {health_dict['memory_percent']:.2f}% - Status: {health_dict['memory_status']}")
    print(f"Disk Usage: {health_dict['disk_percent']:.2f}% - Status: {health_dict['disk_status']}")
    print(f"Overall System Health: {health_dict['overall_status']}")


def show_system_health_json(health_dict: dict) -> None:
    print(json.dumps(health_dict, indent=4))

