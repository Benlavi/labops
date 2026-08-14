import argparse
import socket
import platform
import time
import psutil 
from datetime import timedelta 

parser = argparse.ArgumentParser(description="LabOps Host Inspector: Displays system information.")
subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("info" , help="Display system information.")
subparsers.add_parser("disk" , help="Display disk usage information.")

################################################################################################################
#info 

def get_hostname() -> str:
    return socket.gethostname()

def get_os_name() -> str:
    return platform.system()

def get_kernel_version() -> str:
    return platform.release()

def get_uptime() -> str:
    uptime_seconds = time.time() - psutil.boot_time()
    return str(timedelta(seconds=uptime_seconds)).split('.')[0]  # Format uptime as HH:MM:SS  

def show_system_info() -> None:
    print("=== LabOps Host Inspector ===")
    print(f"Hostname: {get_hostname()}")
    print(f"Operating System: {get_os_name()}")  
    print(f"Kernel Version: {get_kernel_version()}")  
    print(f"Uptime: {get_uptime()}")

################################################################################################################
#disk
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

def main() -> None:
    args = parser.parse_args()
    if args.command == "info":
        show_system_info()
    elif args.command == "disk":
        show_disk_info()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
