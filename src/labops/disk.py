import json
import psutil


def get_disk_usage() -> dict[str, float]:
    disk_usage = psutil.disk_usage('/')
    return {
        "total_gb": disk_usage.total / (1000 ** 3),
        "used_gb": disk_usage.used / (1000 ** 3),
        "free_gb": disk_usage.free / (1000 ** 3),
        "percent": disk_usage.percent
    }
  

def show_disk_info(disk_usage_info: dict) -> None:
    
    print("=== Disk Information ===")
    print(f"Total Disk Space: {disk_usage_info['total_gb']:.2f} GB")
    print(f"Used Disk Space: {disk_usage_info['used_gb']:.2f} GB")
    print(f"Free Disk Space: {disk_usage_info['free_gb']:.2f} GB")
    print(f"Disk Usage Percentage: {disk_usage_info['percent']}%")
    print()


def show_disk_info_json(disk_usage_info: dict) -> None:
    print(json.dumps(disk_usage_info, indent=4))