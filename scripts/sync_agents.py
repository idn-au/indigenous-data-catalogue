# this script reloads all agents in the https://data.idnau.org/pid/agentsdb graph as they aren't specified in the KGM manifest

import os
from pathlib import Path

from dotenv import load_dotenv
from httpx import Client
from kurra.db import gsp

AGENTS_DIR = Path(__file__).parent.parent / "resources/agents/sync"
AGENTS_GRAPH = "https://data.idnau.org/pid/agentsdb"

load_dotenv()
client = Client(auth=(os.environ.get("FUSEKI_USERNAME", ""), os.environ.get("FUSEKI_PASSWORD", "")), timeout=60)
endpoint = os.environ.get("FUSEKI_URL", "")


def main():
    gsp.upload(endpoint, AGENTS_DIR / "agentsdb.ttl", AGENTS_GRAPH, http_client=client)
    print("Agents graph content replaced")

    for file in AGENTS_DIR.glob("items/*.ttl"):
        print(f"Uploading {file.name}...")
        gsp.upload(endpoint, file, AGENTS_GRAPH, append=True, http_client=client)
        print(f"{file.name} uploaded")


if __name__ == "__main__":
    main()
