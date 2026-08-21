import csv
from textwrap import dedent
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, DCAT, SDO, XSD


EX = Namespace("http://example.com/")

with (open("datasets.csv") as f):
    reader = csv.DictReader(f)
    for row in reader:
        g = Graph()

        r = URIRef(row["IRI"])
        g.add((r, RDF.type, SDO.CreativeWork))

        if len(row["dcterms:issued"]) > 0:
            if len(row["dcterms:issued"]) == 4:
                g.add((r, SDO.dateCreated, Literal(row["dcterms:issued"], datatype=XSD.gYear)))
            elif len(row["dcterms:issued"]) == 10:
                g.add((r, SDO.dateCreated, Literal(row["dcterms:issued"], datatype=XSD.date)))

        if len(row["authorID"]) > 0:
            for c in row["authorID"].split(","):
                g.add((r, SDO.creator, URIRef(c.strip())))
        else:
            g.add((r, SDO.creator, Literal(row["dcterms:creator"])))

        if len(row["dcterms:type"]) > 0:
            if row["dcterms:type"].startswith("http"):
                g.add((r, SDO.additionalType, URIRef(row["dcterms:type"])))
            else:
                g.add((r, SDO.additionalType, Literal(row["dcterms:type"])))

        g.add((r, SDO.name, Literal(row["dcterms:title"])))

        g.add((r, SDO.description, Literal(row["dcterms:description"])))

        if len(row["dcat:theme"]) > 0:
            if row["dcat:theme"].startswith("http"):
                g.add((r, SDO.keywords, URIRef(row["dcat:theme"])))
            else:
                g.add((r, SDO.keywords, Literal(row["dcat:theme"])))

        if len(row["ISBN"]) > 0:
            g.add((r, SDO.identifier, Literal(row["ISBN"], datatype=EX.IBN)))

        if len(row["online"]) > 0:
            d = BNode()
            g.add((r, SDO.distribution, d))
            g.add((d, DCAT.downloadURL, Literal(row["online"], datatype=XSD.anyURI)))

        g.serialize(format="longturtle", destination="../resources/" + row["ID"] + ".ttl")
