#!/usr/bin/env python3
"""Merge a myCorp public-register grid extract into oricAgents.ttl.

The input is a JSON array containing the columns exposed by the public grid.
Existing RDF statements that are not available from that grid are preserved.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date, datetime
from pathlib import Path


ICN_RE = re.compile(r'"(\d+)"\^\^idncp:ICN')
ORG_RE = re.compile(
    r"^(oricAgents:[^\s]+) a sdo:Organization ;\n.*?(?=\n(?:oricAgents:|\Z))",
    re.MULTILINE | re.DOTALL,
)
STATE_CODES = {"NSW": "1", "VIC": "2", "QLD": "3", "SA": "4", "WA": "5", "TAS": "6", "NT": "7", "ACT": "8"}


def turtle_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "")


def iso_date(value: str) -> str:
    return datetime.strptime(value, "%d/%m/%Y").date().isoformat()


def local_name(name: str) -> str:
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    words = re.findall(r"[A-Za-z0-9]+", ascii_name)
    if not words:
        return "corporation"
    return words[0][:1].lower() + words[0][1:] + "".join(w[:1].upper() + w[1:] for w in words[1:])


def address_fields(address: str) -> tuple[str | None, str | None]:
    match = re.search(r",\s*(NSW|VIC|QLD|SA|WA|TAS|NT|ACT)\s+(\d{4})(?:,|$)", address, re.IGNORECASE)
    if not match:
        return None, None
    return STATE_CODES[match.group(1).upper()], match.group(2)


def new_block(subject: str, row: dict[str, str]) -> str:
    status = row["status"]
    predicates = [
        "    dcterms:type idni:indigenous-persons-organisation",
        f'    sdo:description "ORIC {status} Corporation"',
    ]
    if row.get("registeredOn"):
        predicates.append(f'    sdo:foundingDate "{iso_date(row["registeredOn"])}"^^xsd:date')
    if row.get("deregisteredOn"):
        predicates.append(f'    sdo:dissolutionDate "{iso_date(row["deregisteredOn"])}"^^xsd:date')
    predicates.append(f'    sdo:identifier "{row["icn"]}"^^idncp:ICN')
    state, postcode = address_fields(row.get("address", ""))
    if state:
        predicates.append(f"    sdo:location <http://asgs.linked.fsdf.org.au/dataset/asgsed3/collections/STE/items/{state}>")
    predicates.append(f'    sdo:name "{turtle_string(row["name"])}"')
    if postcode:
        predicates.append(f'    sdo:postalCode "{postcode}"')
    predicates.append(f'    sdo:url "{turtle_string(row["url"])}"^^xsd:anyURI')
    return f"{subject} a sdo:Organization ;\n" + " ;\n".join(predicates) + " .\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("extract", type=Path)
    parser.add_argument("ttl", type=Path)
    args = parser.parse_args()

    rows = json.loads(args.extract.read_text())
    by_icn = {row["icn"]: row for row in rows}
    if len(by_icn) != len(rows):
        raise ValueError("extract contains duplicate ICNs")

    original = args.ttl.read_bytes()
    newline = "\r\n" if b"\r\n" in original else "\n"
    text = original.decode().replace("\r\n", "\n")
    subjects: set[str] = set()
    seen_icns: set[str] = set()

    def update_existing(match: re.Match[str]) -> str:
        block = match.group(0)
        subject = match.group(1)
        icns = ICN_RE.findall(block)
        if not icns:
            subjects.add(subject)
            return block
        # Older name-based minting occasionally collapsed multiple ORIC records
        # with the same name onto one RDF subject. Retain the first unseen ICN
        # on that subject; the remaining ICNs are emitted as separate records.
        icn = next((value for value in icns if value not in seen_icns), None)
        if icn is None:
            return ""
        subjects.add(subject)
        seen_icns.add(icn)
        row = by_icn.get(icn)
        if not row:
            return block
        identifier_match = re.search(r"    sdo:identifier (.*?) ;\n", block, re.DOTALL)
        if identifier_match:
            values = [value.strip() for value in identifier_match.group(1).split(",")]
            values = [value for value in values if "^^idncp:ICN" not in value]
            values.append(f'"{icn}"^^idncp:ICN')
            indent = ",\n        ".join(values)
            block = block[: identifier_match.start(1)] + indent + block[identifier_match.end(1) :]
        return re.sub(
            r'    sdo:url .*?\s*\.\s*$',
            f'    sdo:url "{turtle_string(row["url"])}"^^xsd:anyURI .\n',
            block,
            flags=re.DOTALL,
        )

    text = ORG_RE.sub(update_existing, text)

    additions: list[str] = []
    for icn in sorted(by_icn.keys() - seen_icns, key=int):
        row = by_icn[icn]
        base = f"oricAgents:{local_name(row['name'])}"
        subject = base
        if subject in subjects:
            subject = f"{base}Icn{icn}"
        subjects.add(subject)
        additions.append(new_block(subject, row))

    dataset_match = re.search(r"oricAgents: a sdo:Dataset ;\n.*?\n\s+sdo:name \"ORIC Extract\" \.\n", text, re.DOTALL)
    if not dataset_match:
        raise ValueError("could not find ORIC dataset block")
    dataset = dataset_match.group(0)
    part_match = re.search(r"\n\s+sdo:hasPart (.*?) ;\n\s+sdo:name", dataset, re.DOTALL)
    existing_order = re.findall(r"oricAgents:[^\s,;]+", part_match.group(1)) if part_match else []
    dataset = re.sub(r"\n\s+sdo:hasPart .*? ;\n\s+sdo:name", "\n    sdo:name", dataset, flags=re.DOTALL)
    dataset = re.sub(r"\n\s+sdo:dateModified \"[^\"]+\"\^\^xsd:date ;", "", dataset)
    dataset = dataset.replace(
        '    sdo:dateCreated "2024-01-11"^^xsd:date ;',
        f'    sdo:dateCreated "2024-01-11"^^xsd:date ;\n    sdo:dateModified "{date.today().isoformat()}"^^xsd:date ;',
    )
    ordered = [subject for subject in existing_order if subject in subjects]
    ordered.extend(sorted(subjects - set(ordered), key=lambda value: value.casefold()))
    has_part = "    sdo:hasPart " + ",\n        ".join(ordered) + " ;\n"
    dataset = dataset.replace('    sdo:name "ORIC Extract" .', has_part + '    sdo:name "ORIC Extract" .')
    text = text[: dataset_match.start()] + dataset + text[dataset_match.end() :]
    if additions:
        text = text.rstrip() + "\n\n" + "\n".join(additions)
    args.ttl.write_bytes(text.replace("\n", newline).encode())

    print(f"updated URLs for {len(seen_icns)} existing ICNs; added {len(additions)} organisations")


if __name__ == "__main__":
    main()
