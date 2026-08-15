import json
import socket
import platform
import time
import psutil
from datetime import timedelta 


def get_system_info() -> dict[str, str]:
    return{
        "hostname": socket.gethostname(),
        "os_name": platform.system(),
        "kernel_version": platform.release(),
        "uptime_seconds": (time.time() - psutil.boot_time())
    }

def show_system_info() -> None:
    print("=== LabOps Host Inspector ===")
    system_info = get_system_info()
    print(f"Hostname: {system_info['hostname']}")
    print(f"Operating System: {system_info['os_name']}")  
    print(f"Kernel Version: {system_info['kernel_version']}")  
    print(f"Uptime: {str(timedelta(seconds=system_info['uptime_seconds'])).split('.')[0]}")  # Format uptime as HH:MM:SS

def show_system_info_json() -> None:
    system_info = get_system_info()
    print(json.dumps(system_info, indent=4))