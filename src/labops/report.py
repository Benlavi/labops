import json
from labops import disk, health, network, system

def get_report() -> dict:
    report={
        'system': system.get_system_info(),
        'disk': disk.get_disk_usage(),
        'network': network.get_network_info(),
        'health': health.get_system_health(),
    }
    return report

def show_report(report_dict: dict) -> None:
    system.show_system_info(report_dict['system'])
    disk.show_disk_info(report_dict['disk'])
    network.show_network_info(report_dict['network'])
    health.show_system_health(report_dict['health'])

def show_report_json(report_dict: dict) -> None:
    print(json.dumps(report_dict, indent=4))