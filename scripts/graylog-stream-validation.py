#!/usr/bin/env python3

"""
Graylog Stream Validation

Generic sanitized example for validating Graylog streams through the API.

Example usage:
    python3 graylog-stream-validation.py --url https://graylog.example.com --token TOKEN
"""

import argparse
import requests
import sys


def get_streams(base_url: str, token: str) -> dict:
    url = f"{base_url.rstrip('/')}/api/streams"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    return response.json()


def print_streams(data: dict) -> None:
    streams = data.get("streams", [])

    print("=" * 70)
    print("GRAYLOG STREAM VALIDATION")
    print("=" * 70)

    if not streams:
        print("No streams found.")
        return

    for stream in streams:
        print(f"\nStream Title : {stream.get('title', 'N/A')}")
        print(f"Description  : {stream.get('description', 'N/A')}")
        print(f"Disabled     : {stream.get('disabled', 'N/A')}")
        print(f"Matching     : {stream.get('matching_type', 'N/A')}")
        print("-" * 70)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Graylog streams.")
    parser.add_argument("--url", required=True, help="Graylog base URL.")
    parser.add_argument("--token", required=True, help="Graylog API token.")

    args = parser.parse_args()

    try:
        data = get_streams(args.url, args.token)
        print_streams(data)
    except requests.exceptions.RequestException as error:
        print(f"[ERROR] Graylog API request failed: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
