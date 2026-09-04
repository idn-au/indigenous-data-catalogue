import os
from pathlib import Path
import httpx

TRIPLESTORE_URL = os.environ.get("TRIPLESTORE_URL", "")
TRIPLESTORE_USERNAME = os.environ.get("TRIPLESTORE_USERNAME", "")
TRIPLESTORE_PASSWORD = os.environ.get("TRIPLESTORE_PASSWORD", "")
TIMEOUT = 30.0

AGENTS_GRAPH_IRI = "https://data.idnau.org/pid/agentsdb"

data_dir = Path(__file__).parent.parent / "data" / "raw"

def upload_agents():
    """Uploads all agent files from `data/raw/` into a single named graph."""
    print("Uploading agents...")

    sparql_update_query(f"DROP GRAPH <{AGENTS_GRAPH_IRI}>")

    # upload agents in data/raw/
    for f in data_dir.glob("*.ttl"):
        upload_named_graph(f, AGENTS_GRAPH_IRI, False)
    
    print("Upload complete")

# drop & upload named graph & add to default
def upload_named_graph(file: Path, iri: str, drop_graph: bool=True):
    """Uploads a named graph from an IRI to the triplestore."""
    # drop named graph
    if drop_graph:
        sparql_update_query(f"DROP GRAPH <{iri}>")

    # upload turtle to named graph
    sparql_upload_file(file, iri)

# POST request to triplestore with credentials
# need one function for turtle data, one for SPARQL update queries
def sparql_update_query(query: str):
    """Does a SPARQL update request to the triplestore."""
    r = httpx.post(
        url=f"{TRIPLESTORE_URL}/update",
        auth=(TRIPLESTORE_USERNAME, TRIPLESTORE_PASSWORD),
        timeout=TIMEOUT,
        data=query,
        headers={
            "Content-Type": "application/sparql-update"
        },
    )

def sparql_upload_file(file: Path, named_graph: str):
    """Uploads a turtle file in a named graph to the triplestore."""
    with open(file, "rb") as f:
        content = f.read()

    r = httpx.post(
        url=f"{TRIPLESTORE_URL}/data",
        auth=(TRIPLESTORE_USERNAME, TRIPLESTORE_PASSWORD),
        timeout=TIMEOUT,
        params={"graph": named_graph},
        content=content,
        headers={
            "Content-Type": "text/turtle"
        },
    )

def main():
    upload_agents()

if __name__ == "__main__":
    main()