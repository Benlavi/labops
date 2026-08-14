
import psutil


def get_disk_usage() -> dict[str, str]:
    disk_usage = psutil.disk_usage('/')
    return {
        "total": f"{disk_usage.total / (1000 ** 3):.2f} GB",
        "used": f"{disk_usage.used / (1000 ** 3):.2f} GB",
        "free": f"{disk_usage.free / (1000 ** 3):.2f} GB",
        "percent": f"{disk_usage.percent}%"
    }
  

def show_disk_info() -> None:
    disk_usage_info = get_disk_usage()
    print("=== Disk Information ===")
    print(f"Total Disk Space: {disk_usage_info['total']}")
    print(f"Used Disk Space: {disk_usage_info['used']}")
    print(f"Free Disk Space: {disk_usage_info['free']}")
    print(f"Disk Usage Percentage: {disk_usage_info['percent']}")
