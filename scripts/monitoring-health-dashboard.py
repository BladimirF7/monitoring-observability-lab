#!/usr/bin/env python3

"""
Monitoring Health Dashboard

Generates a simple text-based operational monitoring health summary.

Example usage:
    python3 monitoring-health-dashboard.py --input monitoring-status.json
"""

import argparse
import json
from pathlib import Path


def load_status(file_path: str) -> dict:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def render_dashboard(data: dict) -> None:
    print("=" * 80)
    print("MONITORING HEALTH DASHBOARD")
    print("=" * 80)

    print(f"Environment       : {data.get('environment', 'N/A')}")
    print(f"Total Hosts       : {data.get('total_hosts', 'N/A')}")
    print(f"Healthy Hosts     : {data.get('healthy_hosts', 'N/A')}")
    print(f"Warning Hosts     : {data.get('warning_hosts', 'N/A')}")
    print(f"Critical Hosts    : {data.get('critical_hosts', 'N/A')}")
    print(f"Active Alerts     : {data.get('active_alerts', 'N/A')}")
    print(f"Last Updated      : {data.get('last_updated', 'N/A')}")

    print("\nKey Services")
    print("-" * 80)

    for service in data.get("services", []):
        print(f"{service.get('name', 'N/A'):<30} {service.get('status', 'N/A')}")

    print("=" * 80)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a simple monitoring health dashboard.")
    parser.add_argument("--input", required=True, help="Path to monitoring status JSON.")

    args = parser.parse_args()

    try:
        data = load_status(args.input)
        render_dashboard(data)
    except Exception as error:
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
