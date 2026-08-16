import argparse
from labops import system, disk, network, health


parser = argparse.ArgumentParser(
    description="LabOps Host Inspector: Displays system information."
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




def main() -> None:
    args = parser.parse_args()
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
        if args.json:
            health.show_system_health_json()   
        else:
            health.show_system_health()
    else:
        parser.print_help()



if __name__ == "__main__":
    main()

