import json
import psutil
import logging
from labops.disk import get_disk_usage

logger = logging.getLogger(__name__)

def get_status(percent: float) -> str:
    if percent < 80:
        return "OK"
    elif percent < 90:
        return "WARNING"
    else:
        return "CRITICAL"



def get_system_health(disk_percent: float | None = None) -> dict[str, str | float]:
    logger.debug("Collecting system data")
    if disk_percent is None:
        disk_percent = get_disk_usage()["percent"]
        
    memory_percent = psutil.virtual_memory().percent
    overall = max(disk_percent, memory_percent)
    system_health = {
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "memory_status": get_status(memory_percent),
        "disk_status": get_status(disk_percent),
        "overall_status": get_status(overall)
    }
    logger.debug("Overall status is %s",system_health["overall_status"])
    return system_health

    

def show_system_health(health_dict: dict) -> None:
    
    print("=== System Health Information ===")
    print(f"Memory Usage: {health_dict['memory_percent']:.2f}% - Status: {health_dict['memory_status']}")
    print(f"Disk Usage: {health_dict['disk_percent']:.2f}% - Status: {health_dict['disk_status']}")
    print(f"Overall System Health: {health_dict['overall_status']}")
    print()


def show_system_health_json(health_dict: dict) -> None:
    print(json.dumps(health_dict, indent=4))

