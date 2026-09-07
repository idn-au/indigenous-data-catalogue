# The Indigenous Data Catalogue
The IDN's catalogue of Indigenous data.

This catalogue will be online at:

- https://data.idnau.org/catalogs/pid:indigenous-data-catalogue

All the resources in this catalogue are listed in the _Catalogue Resources_ section below. These resources are automatically validated and (re)loaded into the catalogue online using the [KGM](https://pypi.org/project/kgm/) tool.

## Updating resources

When a resource is updated, the `dateModified` date or `version` should be updated in the resource and the catalogue as the KGM tool relies on this to determine when to update data.

If a new resource is added to the catalogue, ensure its IRI is added to `schema:hasPart` in [`catalogue.ttl`](./catalogue.ttl).

Pull requests will trigger validation of the manifest, which is required to pass before merging.

## Spatial Datasets
Metadata for spatial datasets & feature collections are located in [`resources/reference/datasets/metadata/`](./resources/reference/datasets/metadata) in Turtle files, and the features per feature collection are located in [`resources/reference/datasets/features/`](./resources/reference/datasets/features) in TriG files. Due to the limit of 100MiB per file on GitHub, some features files are split into parts.

A script is provided ([`scripts/split_features.py`](./scripts/split_features.py)) to split N-quads files from raw data (stored in the IDN cloud's object storage) into Turtle & TriG files to store in git.


## Catalogue Resources
Resource | Role | Description
--- | --- | ---
Catalogue Definition:<br />[`catalogue.ttl`](catalogue.ttl) | [Catalogue Data](https://prez.dev/ManifestResourceRoles/CatalogueData) | The definition of, and metadata for, the container which here is a sdo:DataCatalog object
Reference Vocabularies:<br />[`resources/reference/vocabs/sync/*.ttl`](resources/reference/vocabs/sync/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | skos:ConceptScheme objects in RDF (Turtle) files in the vocabs/sync/ folder for syncing
Reference Spatial Datasets:<br />[`resources/reference/datasets/metadata/*.ttl`](resources/reference/datasets/metadata/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | schema:Dataset objects in RDF (Turtle) files in the datasets/metadata/ folder for syncing
Reference Ontologies:<br />[`resources/reference/ontologies/*.ttl`](resources/reference/ontologies/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | owl:Ontology objects in RDF (Turtle) files in the ontologies/ folder for syncing
ISU Resource Data:<br />[`resources/isu/sync/*.ttl`](resources/isu/sync/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | sdo:CreativeWork objects in RDF (Turtle) files in the resources/ folder
ISU Archive Data:<br />[`resources/isu/sync/isu-archive.ttl`](resources/isu/sync/isu-archive.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | sdo:CreativeWork objects in RDF (Turtle) files in the resources/ folder
Keeping Place Resource Data:<br />[`resources/keeping-place/sync/*.ttl`](resources/keeping-place/sync/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | sdo:CreativeWork objects in RDF (Turtle) files in the resources/ folder
External Resource Data:<br />[`resources/external/*.ttl`](resources/external/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | schema:CreativeWork objects in RDF (Turtle) files in the resources/ folder for syncing
Demo Creative Work Resource Data:<br />[`resources/demo/sync/0811114042000269281.ttl`](resources/demo/sync/0811114042000269281.ttl)<br />[`resources/demo/sync/24750158.2024.2411643.ttl`](resources/demo/sync/24750158.2024.2411643.ttl)<br />[`resources/demo/sync/762463a4-f8b1-4eec-a335-3689c8d86e9e.ttl`](resources/demo/sync/762463a4-f8b1-4eec-a335-3689c8d86e9e.ttl)<br />[`resources/demo/sync/MPF1226_titleOnlyVariant.ttl`](resources/demo/sync/MPF1226_titleOnlyVariant.ttl)<br />[`resources/demo/sync/b494af84-a16e-4cc1-b1f1-aad2486c4656.ttl`](resources/demo/sync/b494af84-a16e-4cc1-b1f1-aad2486c4656.ttl)<br />[`resources/demo/sync/bja.2025.17.ttl`](resources/demo/sync/bja.2025.17.ttl)<br />[`resources/demo/sync/iipj.2023.14.1.10987.ttl`](resources/demo/sync/iipj.2023.14.1.10987.ttl)<br />[`resources/demo/sync/isbn0864090293.ttl`](resources/demo/sync/isbn0864090293.ttl)<br />[`resources/demo/sync/storeroom1189.ttl`](resources/demo/sync/storeroom1189.ttl)<br />[`resources/demo/sync/watch?v=tEdweyPh-N8.ttl`](resources/demo/sync/watch?v=tEdweyPh-N8.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | Creative work resource data in RDF (Turtle) files
Demo Dataset Resource Data:<br />[`resources/demo/sync/multipleIRIspatial.ttl`](resources/demo/sync/multipleIRIspatial.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | Dataset resource data in an RDF (Turtle) file
Demo ODRL Agreement Resource Data:<br />[`resources/demo/sync/policy-telstra-ngaanyatjarra-ilua.ttl`](resources/demo/sync/policy-telstra-ngaanyatjarra-ilua.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | Demonstration ODRL Agreement interpretation linked from an ATNS agreement record
Demo ATNS Agreement Record Resource Data:<br />[`resources/demo/sync/atns-24.ttl`](resources/demo/sync/atns-24.ttl)<br />[`resources/demo/sync/atns-27.ttl`](resources/demo/sync/atns-27.ttl)<br />[`resources/demo/sync/atns-30.ttl`](resources/demo/sync/atns-30.ttl)<br />[`resources/demo/sync/atns-37.ttl`](resources/demo/sync/atns-37.ttl)<br />[`resources/demo/sync/atns-1624.ttl`](resources/demo/sync/atns-1624.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | ATNS Agreement-category entity resource data in RDF (Turtle) files
Demo ATNS Entity Resource Data:<br />[`resources/demo/sync/atns-384.ttl`](resources/demo/sync/atns-384.ttl)<br />[`resources/demo/sync/atns-617.ttl`](resources/demo/sync/atns-617.ttl)<br />[`resources/demo/sync/atns-618.ttl`](resources/demo/sync/atns-618.ttl)<br />[`resources/demo/sync/atns-753.ttl`](resources/demo/sync/atns-753.ttl)<br />[`resources/demo/sync/atns-760.ttl`](resources/demo/sync/atns-760.ttl)<br />[`resources/demo/sync/atns-1845.ttl`](resources/demo/sync/atns-1845.ttl)<br />[`resources/demo/sync/atns-3160.ttl`](resources/demo/sync/atns-3160.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | Other ATNS entity resource data in RDF (Turtle) files
Demo ATNS Reference Resource Data:<br />[`resources/demo/sync/*atns-ref-*.ttl`](resources/demo/sync/*atns-ref-*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | ATNS reference resource data in RDF (Turtle) files
Demo ATNS Entity Relationship Resource Data:<br />[`resources/demo/sync/*atns-rel-*.ttl`](resources/demo/sync/*atns-rel-*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | ATNS entity relationship resource data in RDF (Turtle) files
Agents Database Resource Data:<br />[`resources/agents/sync/agentsdb.ttl`](resources/agents/sync/agentsdb.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | Database of IDN people & organisations
Profile Definition:<br />[`ogc_records_profile.ttl`](https://raw.githubusercontent.com/RDFLib/prez/refs/heads/main/prez/reference_data/profiles/ogc_records_profile.ttl) | [Catalogue & Resource Model](https://prez.dev/ManifestResourceRoles/CatalogueAndResourceModel) | The default Prez profile for Records API
Labels:<br />[`labels.ttl`](labels.ttl) | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing labels for catalogue's content, auto-extracted from KurrawongAI's Semantic Background
Manual Labels:<br />[`labels-manual.ttl`](labels-manual.ttl) | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing labels for catalogue's content, manually created