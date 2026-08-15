import json
import socket
import psutil


def get_network_info() -> dict[str, dict[str, str]]:
    network_info = psutil.net_if_addrs()
    network_stats = psutil.net_if_stats()
    interfaces_info: dict[str, dict[str, str]] = {}
        
    for interface, addrs in network_info.items():
        interfaces_info[interface] = {}
        for addr in addrs:
            if addr.family == socket.AF_INET:
                interfaces_info[interface]["IPv4"] = addr.address
            elif addr.family == socket.AF_INET6:
                interfaces_info[interface]["IPv6"] = addr.address
            elif addr.family == psutil.AF_LINK:
                interfaces_info[interface]["MAC"] = addr.address
        if interface in network_stats:
            interfaces_info[interface]["status"] = "UP" if network_stats[interface].isup else "DOWN"

    return interfaces_info

def show_network_info() -> None:
    network_info = get_network_info()
    print("=== Network Information ===")
    for interface, info in network_info.items():
        print(f"Interface: {interface}")
        print(f"  Status: {info.get('status', 'N/A')}")
        print(f"  IPv4 Address: {info.get('IPv4', 'N/A')}")
        print(f"  IPv6 Address: {info.get('IPv6', 'N/A')}")
        print(f"  MAC Address: {info.get('MAC', 'N/A')}")
        print()


def show_network_info_json() -> None:
    network_info = get_network_info()
    print(json.dumps(network_info, indent=4))
