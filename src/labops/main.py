import argparse
from labops import system, disk, network


parser = argparse.ArgumentParser(description="LabOps Host Inspector: Displays system information.")
subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("info" , help="Display system information.")
subparsers.add_parser("disk" , help="Display disk usage information.")
subparsers.add_parser("network", help="Display network information.")






def main() -> None:
    args = parser.parse_args()
    if args.command == "info":
        system.show_system_info()
    elif args.command == "disk":
        disk.show_disk_info()
    elif args.command == "network":
        network.show_network_info()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
