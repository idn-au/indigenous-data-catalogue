import re

from rdflib import Graph

def serialize_longtrig(g: Graph, graph_iri: str) -> str:
    """Serializes TriG with longturtle format"""
    ttl_str = g.serialize(format="longturtle")
    return re.sub(r'(PREFIX.+\n\n)', rf'\1<{graph_iri}> {{\n', ttl_str) + "\n}"
