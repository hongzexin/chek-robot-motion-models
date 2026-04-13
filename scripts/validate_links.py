#!/usr/bin/env python3
"""Validate the CHEK robot motion model index files.

Checks:
1. models.json is valid JSON and contains required fields
2. models.csv is readable and has matching ids
3. URLs are syntactically valid
4. Optional HTTP check for download/homepage URLs
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


REQUIRED_FIELDS = [
    "id",
    "name",
    "source_owner",
    "source_repo_or_model",
    "platform",
    "robot_brand",
    "robot_model",
    "robot_model_normalized",
    "category_level_1",
    "action_style",
    "download_type",
    "download_url",
    "requires_login",
    "requires_accept_terms",
    "has_direct_weights",
    "is_official",
    "deployment_readiness",
    "short_description_zh",
    "short_description_en",
    "license_note",
    "risk_note",
    "last_checked_note",
    "source_confidence",
]

ALLOWED_PLATFORMS = {"GitHub", "Hugging Face", "Other"}
ALLOWED_CATEGORY_L1 = {
    "showcase",
    "motion_imitation",
    "locomotion",
    "manipulation",
    "generative_motion",
    "task_policy",
    "foundation_motion",
}
ALLOWED_ACTION_STYLE = {
    "greeting",
    "dance",
    "fight",
    "karate",
    "full_body_tracking",
    "walk",
    "run",
    "box_move",
    "pick_place",
    "table_tennis",
    "multiskill",
}
ALLOWED_DOWNLOAD_TYPES = {"direct_file", "model_page", "repo_entry", "gated"}
ALLOWED_DEPLOYMENT = {
    "index_only",
    "research_repro",
    "sim_ready",
    "real_robot_possible",
    "demo_friendly",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"[WARN] {message}")


def info(message: str) -> None:
    print(f"[INFO] {message}")


def validate_url(url: str, field_name: str, item_id: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(f"{item_id}: invalid {field_name} -> {url}")


def load_json(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        fail("models.json must contain a top-level list.")
    return data


def load_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_json_records(records: list[dict]) -> None:
    seen_ids: set[str] = set()
    for record in records:
        if not isinstance(record, dict):
            fail("models.json entries must be JSON objects.")
        item_id = record.get("id", "<missing-id>")
        for field in REQUIRED_FIELDS:
            if field not in record:
                fail(f"{item_id}: missing required field '{field}'.")
            if isinstance(record[field], str) and not record[field].strip():
                fail(f"{item_id}: required string field '{field}' is empty.")
        if item_id in seen_ids:
            fail(f"Duplicate id found in models.json: {item_id}")
        seen_ids.add(item_id)

        if record["platform"] not in ALLOWED_PLATFORMS:
            fail(f"{item_id}: unsupported platform '{record['platform']}'.")
        if record["category_level_1"] not in ALLOWED_CATEGORY_L1:
            fail(f"{item_id}: unsupported category_level_1 '{record['category_level_1']}'.")
        if record["action_style"] not in ALLOWED_ACTION_STYLE:
            fail(f"{item_id}: unsupported action_style '{record['action_style']}'.")
        if record["download_type"] not in ALLOWED_DOWNLOAD_TYPES:
            fail(f"{item_id}: unsupported download_type '{record['download_type']}'.")
        if record["deployment_readiness"] not in ALLOWED_DEPLOYMENT:
            fail(
                f"{item_id}: unsupported deployment_readiness '{record['deployment_readiness']}'."
            )
        if not isinstance(record["requires_login"], bool):
            fail(f"{item_id}: requires_login must be boolean.")
        if not isinstance(record["requires_accept_terms"], bool):
            fail(f"{item_id}: requires_accept_terms must be boolean.")
        if not isinstance(record["has_direct_weights"], bool):
            fail(f"{item_id}: has_direct_weights must be boolean.")
        if not isinstance(record["is_official"], bool):
            fail(f"{item_id}: is_official must be boolean.")

        validate_url(record["download_url"], "download_url", item_id)
        if record.get("homepage_url"):
            validate_url(record["homepage_url"], "homepage_url", item_id)


def validate_csv_records(csv_records: list[dict], json_records: list[dict]) -> None:
    if not csv_records:
        fail("models.csv is empty.")
    csv_ids = {row["id"] for row in csv_records}
    json_ids = {row["id"] for row in json_records}
    if csv_ids != json_ids:
        missing_in_csv = sorted(json_ids - csv_ids)
        missing_in_json = sorted(csv_ids - json_ids)
        fail(
            "CSV/JSON id mismatch. "
            f"Missing in CSV: {missing_in_csv}; missing in JSON: {missing_in_json}"
        )


def check_http(records: list[dict]) -> int:
    failures = 0
    headers = {"User-Agent": "chek-robot-motion-models-validator/1.0"}
    for record in records:
        item_id = record["id"]
        urls = [record["download_url"]]
        homepage_url = record.get("homepage_url", "")
        if homepage_url:
            urls.append(homepage_url)
        allow_auth_failure = bool(record.get("requires_login")) or record.get("download_type") == "gated"
        for url in urls:
            try:
                request = urllib.request.Request(url, headers=headers, method="HEAD")
                with urllib.request.urlopen(request, timeout=15) as response:
                    status = getattr(response, "status", 200)
                    info(f"{item_id}: HEAD {status} {url}")
                    if status >= 400:
                        failures += 1
            except Exception:
                fallback = urllib.request.Request(url, headers=headers, method="GET")
                try:
                    with urllib.request.urlopen(fallback, timeout=20) as response:
                        status = getattr(response, "status", 200)
                        info(f"{item_id}: GET {status} {url}")
                        if status >= 400:
                            failures += 1
                except urllib.error.HTTPError as error:
                    if allow_auth_failure and error.code in {401, 403}:
                        warn(f"{item_id}: acceptable auth-gated HTTP {error.code} {url}")
                    else:
                        warn(f"{item_id}: HTTP {error.code} {url}")
                        failures += 1
                except Exception as error:  # pragma: no cover
                    warn(f"{item_id}: request failed for {url}: {error}")
                    failures += 1
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CHEK robot motion model index files.")
    parser.add_argument(
        "--check-http",
        action="store_true",
        help="Perform live HTTP checks for download_url and homepage_url.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    json_path = repo_root / "data" / "models.json"
    csv_path = repo_root / "data" / "models.csv"

    json_records = load_json(json_path)
    csv_records = load_csv(csv_path)

    validate_json_records(json_records)
    validate_csv_records(csv_records, json_records)

    info(f"Validated {len(json_records)} JSON records and {len(csv_records)} CSV records.")

    if args.check_http:
        failures = check_http(json_records)
        if failures:
            fail(f"HTTP validation failed for {failures} URLs.")

    info("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
