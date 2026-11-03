# this script adds schema:isPartOf to the agents database for any that are missing that triple

from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, SDO

AGENTS_DIR = Path(__file__).parent.parent / "resources/agents/sync"
AGENTS_GRAPH = "https://data.idnau.org/pid/agentsdb"


def main():
    for file in AGENTS_DIR.glob("items/*.ttl"):
        count = 0
        g = Graph()
        g.parse(source=file, format="turtle")
        for agent in g.subjects(RDF.type, [SDO.Person, SDO.Organization]):
            if not g.value(agent, SDO.isPartOf):
                count += 1
                g.add((agent, SDO.isPartOf, URIRef(AGENTS_GRAPH)))
        if count > 0:
            g.serialize(destination=file, format="longturtle")
            print(f"{file.name} updated {count} agents")
        else:
            print(f"{file.name} skipped")

if __name__ == "__main__":
    main()
