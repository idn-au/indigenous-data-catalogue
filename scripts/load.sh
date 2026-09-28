# (re)loads all data and runs indexing for local environment
# run from project root directory
# requires uv, kgm & docker installed
# requires env variables set

source .env

curl -i -u $FUSEKI_USERNAME:$FUSEKI_PASSWORD -d "update=DROP SILENT GRAPH <https://prez.dev/SystemGraph>" $FUSEKI_URL/update
curl -i -u $FUSEKI_USERNAME:$FUSEKI_PASSWORD -d "update=DROP SILENT GRAPH <https://prez.dev/ProfilesGraph>" $FUSEKI_URL/update

cd docker
curl -v -u $FUSEKI_USERNAME:$FUSEKI_PASSWORD -F upload=@prez-endpoints.trig $FUSEKI_URL/data
curl -v -u $FUSEKI_USERNAME:$FUSEKI_PASSWORD -F upload=@prez-profiles.trig $FUSEKI_URL/data
cd ..

kgm validate manifest.ttl
kgm sync -u $FUSEKI_USERNAME -p $FUSEKI_PASSWORD manifest.ttl $FUSEKI_URL True False True False

uv run python scripts/sync_labels.py
uv run python scripts/sync_agents.py
uv run python scripts/clear_spatial.py

rm docker/rdf/*
cp resources/reference/datasets/features/* docker/rdf/
cd docker/
docker compose --env-file ../.env -f fuseki-compose.yaml stop -t 30 fuseki
sh spatial_tdb.sh
docker compose --env-file ../.env -f fuseki-compose.yaml start fuseki

docker compose --env-file ../.env -f prez-compose.yaml restart prez4
