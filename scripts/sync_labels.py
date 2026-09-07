# this script is required as KGM doesn't load labels on running the sync command

import os
from pathlib import Path

from dotenv import load_dotenv
from httpx import Client
from kurra.db import gsp

PROJECT_ROOT = Path(__file__).parent.parent
BACKGROUND_GRAPH = "http://background"

load_dotenv()
client = Client(auth=(os.environ.get("FUSEKI_USERNAME", ""), os.environ.get("FUSEKI_PASSWORD", "")), timeout=60)
endpoint = os.environ.get("FUSEKI_URL", "")


def main():
    gsp.upload(endpoint, PROJECT_ROOT / "labels.ttl", BACKGROUND_GRAPH, http_client=client)
    print("labels.ttl loaded")
    gsp.upload(endpoint, PROJECT_ROOT / "labels-manual.ttl", BACKGROUND_GRAPH, append=True, http_client=client)
    print("labels-manual.ttl loaded")


if __name__ == "__main__":
    main()
