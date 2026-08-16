import sys
import argparse
import logging
from labops import system, disk, network, health, report


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
report_parser = subparsers.add_parser(
    "report",
    help="Display full system report"
)
report_parser.add_argument(
    "--json",
    action="store_true",
    help="Output full system report in JSON format"
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
        system_info = system.get_system_info()
        if args.json:
            system.show_system_info_json(system_info)
        else:
            system.show_system_info(system_info)
    elif args.command == "disk":
        disk_info = disk.get_disk_usage()
        if args.json:
            disk.show_disk_info_json(disk_info)
        else:
            disk.show_disk_info(disk_info)
    elif args.command == "network":
        network_info = network.get_network_info()
        if args.json:
            network.show_network_info_json(network_info)
        else:
            network.show_network_info(network_info)
    elif args.command == "health":
        try:
            health_info = health.get_system_health()
        except Exception as error:
            logging.error("Failed to collect system health: %s", error)
            return 3
        if args.json:
           health.show_system_health_json(health_dict=health_info)
        else:
            health.show_system_health(health_dict=health_info)
        status = health_info["overall_status"]
    elif args.command == "report":
        try:
            report_dict = report.get_report()
        except Exception as error:
            logging.error("Failed to collect system report: %s", error)
            return 3

        if args.json:
            report.show_report_json(report_dict)
        else:
            report.show_report(report_dict)
        status = report_dict['health']['overall_status']
    else:
        parser.print_help()
    return get_exit_status(status) 



if __name__ == "__main__":
    sys.exit(main())


