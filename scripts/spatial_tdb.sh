docker run \
    -v /fuseki:/fuseki \
    -v ./rdf:/rdf \
    -v "./prez-config.ttl:/config.ttl" \
    -v "/fuseki/databases:/fuseki/databases" \
    -e DATASET=/fuseki/databases/prez4 \
    -e SPATIAL=true \
    -e TEXT=true \
    --rm \
    ghcr.io/kurrawong/tdb2-generation:master