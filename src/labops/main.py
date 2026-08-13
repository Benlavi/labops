import argparse
import socket
import platform
import time
import psutil 
from datetime import timedelta 

parser = argparse.ArgumentParser(description="LabOps Host Inspector: Displays system information.")
subparsers = parser.add_subparsers(dest="command")

parser_info = subparsers.add_parser("info" , help="Display system information.")

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



def main() -> None:
    args = parser.parse_args()
    if args.command == "info":
        show_system_info()
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
