import sys
import argparse
import logging
from labops import system, disk, network, health


parser = argparse.ArgumentParser(
    description="LabOps Host Inspector: Displays system information."
    )
parser.add_argument("-v",
                    "--verbose",
                    action="store_true",
                    help="Enable Debug logging"
                    )

subparsers = parser.add_subparsers(
    dest="command"
    )

info_parser = subparsers.add_parser(
    "info",
    help="Display system information."
    )
info_parser.add_argument(
    "--json",
    action="store_true",
    help="Output system information in JSON format."
    )
disk_parser = subparsers.add_parser(
    "disk",
    help="Display disk usage information."
    )
disk_parser.add_argument(
    "--json",
    action="store_true",
    help="Output disk information in JSON format."
    )
network_parser = subparsers.add_parser(
    "network",
    help="Display network information."
)
network_parser.add_argument(
    "--json",
    action="store_true",
    help="Output network information in JSON format."
)
health_parser = subparsers.add_parser(
    "health",
    help="Display system health information."
)
health_parser.add_argument(
    "--json",
    action="store_true",
    help="Output system health information in JSON format."
)


def get_exit_status(status: str | None = None) -> int:
    if status == "OK" or status is None:
        return 0
    elif status == "WARNING":
        return 1
    elif status == "CRITICAL":
        return 2
    else: # ERROR 
        return 3 

def get_log_level(verbose: bool) -> int:
    if verbose == True:
        return logging.DEBUG
    else:
        return logging.INFO

def main() -> int:
    args = parser.parse_args()

    log_level = get_log_level(args.verbose)

    logging.basicConfig(
        level=log_level,
        format="%(levelname)s: %(message)s"
    )

    status = None

    if args.command == "info":
        if args.json:
            system.show_system_info_json()
        else:
            system.show_system_info()
    elif args.command == "disk":
        if args.json:
            disk.show_disk_info_json()
        else:
            disk.show_disk_info()
    elif args.command == "network":
        if args.json:
            network.show_network_info_json()
        else:
            network.show_network_info()
    elif args.command == "health":
        health_info = health.get_system_health()
        if args.json:
           health.show_system_health_json(health_dict=health_info)
        else:
            health.show_system_health(health_dict=health_info)
        status = health_info["overall_status"]
    else:
        parser.print_help()
    return get_exit_status(status)  



if __name__ == "__main__":
    sys.exit(main())


