import argparse
from labops import system, disk, network


parser = argparse.ArgumentParser(
    description="LabOps Host Inspector: Displays system information."
    )
subparsers = parser.add_subparsers(
    dest="command"
    )

subparsers.add_parser(
    "info",
    help="Display system information."
    )
disks_parser = subparsers.add_parser(
    "disk",
    help="Display disk usage information."
    )
disks_parser.add_argument(
    "--json",
    action="store_true",
    help="Output disk information in JSON format."
    )
subparsers.add_parser(
    "network",
    help="Display network information."
)






def main() -> None:
    args = parser.parse_args()
    if args.command == "info":
        system.show_system_info()
    elif args.command == "disk":
        if args.json:
            disk.show_disk_info_json()
        else:
            disk.show_disk_info()
    elif args.command == "network":
        network.show_network_info()
    else:
        parser.print_help()



if __name__ == "__main__":
    main()

