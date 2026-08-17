import json
from pathlib import Path
from labops import disk, health, network, system

def get_report() -> dict:
    system_info = system.get_system_info()
    disk_info = disk.get_disk_usage()
    network_info = network.get_network_info()
    health_info = health.get_system_health(disk_info['percent'])
    report={
        'system': system_info,
        'disk': disk_info,
        'network': network_info,
        'health': health_info,
    }
    return report

def show_report(report_dict: dict) -> None:
    system.show_system_info(report_dict['system'])
    disk.show_disk_info(report_dict['disk'])
    network.show_network_info(report_dict['network'])
    health.show_system_health(report_dict['health'])

def show_report_json(report_dict: dict) -> None:
    print(json.dumps(report_dict, indent=4))


def save_report(report_dict: dict, output_path: str) -> None:
    path = Path(output_path)
    with path.open('w', encoding='utf-8') as file:
        json.dump(report_dict,file,indent=4)
