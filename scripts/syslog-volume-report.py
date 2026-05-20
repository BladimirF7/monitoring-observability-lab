#!/usr/bin/env python3

"""
Syslog Volume Report

Generates a simple syslog volume summary from sanitized JSON data.

Example usage:
    python3 syslog-volume-report.py --input syslog-volume.json
"""

import argparse
import json
from pathlib import Path


def load_data(file_path: str) -> list:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of log source records.")

    return data


def print_report(records: list) -> None:
    print("=" * 80)
    print("SYSLOG VOLUME REPORT")
    print("=" * 80)

    total_events = 0

    for record in records:
        source = record.get("source", "N/A")
        device_type = record.get("device_type", "N/A")
        events = int(record.get("events_last_24h", 0))
        total_events += events

        print(f"\nSource          : {source}")
        print(f"Device Type     : {device_type}")
        print(f"Events Last 24h : {events}")
        print("-" * 80)

    print(f"\nTotal Events Last 24h: {total_events}")
    print("=" * 80)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a syslog volume report.")
    parser.add_argument("--input", required=True, help="Path to syslog volume JSON file.")

    args = parser.parse_args()

    try:
        records = load_data(args.input)
        print_report(records)
    except Exception as error:
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
