# initialises the local docker environment
# run from project root directory
# requires github cli (authenticated with "gh auth login"), uv & docker installed
# requires env variables set

source .env

mkdir -p docker
mkdir -p docker/rdf docker/fuseki
cp scripts/spatial_tdb.sh docker/

fuseki_files=$(gh repo read-dir fuseki --repo idn-au/idn-infrastructure --json name,type -q '.entries.[] | select(.type == "file").name')

for file in $fuseki_files; do
  gh repo read-file fuseki/$file --repo idn-au/idn-infrastructure -o docker/$file
done

prez_files=(prez-compose.yaml prez-endpoints.trig prez-profiles.trig)

for file in "${prez_files[@]}"; do
  gh repo read-file $file --repo idn-au/idn-prez4 -o docker/$file
done

uv sync

sed "-i" "" "-e" 's|/fuseki:/fuseki|./fuseki:/fuseki|' docker/fuseki-compose.yaml
sed "-i" "" "-e" 's|/fuseki:|./fuseki:|' docker/spatial_tdb.sh
sed "-i" "" "-e" 's|/fuseki/databases:|./fuseki/databases:|' docker/spatial_tdb.sh
sed "-i" "" "-e" 's|DATASET=/fuseki|DATASET=./fuseki|' docker/spatial_tdb.sh
sed "-i" "" "-e" "s|admin = .*|admin = $ADMIN_PASSWORD|" docker/shiro.ini

docker compose --env-file .env -f docker/fuseki-compose.yaml up -d
docker compose --env-file .env -f docker/prez-compose.yaml up -d

echo "Fuseki running at http://localhost:3030"
echo "Prez API running at http://localhost:8000"
echo "Run the adjacent load.sh script to load your data"
echo "Run Prez UI pointing to Prez API at http://localhost:8000"
