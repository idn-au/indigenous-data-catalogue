# this script clears all spatial dataset graphs to avoid geometry duplication in TBD load
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from httpx import Client
from kurra.db import gsp
from kurra.sparql import query

DATASETS_DIR = Path(__file__).parent.parent / "resources/reference/datasets/metadata"

load_dotenv()
client = Client(auth=(os.environ.get("FUSEKI_USERNAME", ""), os.environ.get("FUSEKI_PASSWORD", "")), timeout=60)
endpoint = os.environ.get("FUSEKI_URL", "")


def main():
    for file in DATASETS_DIR.glob("*.ttl"):
        print(f"Reloading {file.name}...")
        q = """PREFIX schema: <https://schema.org/>
            SELECT ?d
            WHERE {
                ?d a schema:Dataset .
            } LIMIT 1"""
        r = json.loads(query(file, q))["results"]["bindings"]
        if len(r) == 1:
            # replaces graph content with dataset metadata initially
            gsp.upload(endpoint, file, r[0]["d"]["value"], http_client=client)
            print(f"{file.name} loaded")
        else:
            print(f"{file.name} skipped, dataset query failed.")


if __name__ == "__main__":
    main()
