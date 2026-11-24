# (re)loads all data and runs indexing for local environment
# run from project root directory
# requires uv, kgm & docker installed
# requires env variables set

source .env

kgm validate manifest.ttl
kgm sync -u $FUSEKI_USERNAME -p $FUSEKI_PASSWORD manifest.ttl $FUSEKI_URL True False True False

uv run python scripts/sync_labels.py
uv run python scripts/sync_agents.py
uv run python scripts/clear_spatial.py

rm docker/rdf/*
cp resources/spatial/features/* docker/rdf/
cd docker/
docker compose --env-file ../.env -f fuseki-compose.yaml stop -t 30 fuseki
sh spatial_tdb.sh
docker compose --env-file ../.env -f fuseki-compose.yaml start fuseki

docker compose --env-file ../.env -f prez-compose.yaml restart prez4
