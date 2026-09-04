# The Indigenous Data Catalogue
The IDN's catalogue of Indigenous data.

This catalogue will be online at:

- https://data.idnau.org/catalogs/pid:indigenous-data-catalogue

All the resources in this catalogue are listed in the _Catalogue Resources_ section below. These resources are automatically validated and (re)loaded into the catalogue online using the [Prez Manifest](https://pypi.org/project/prezmanifest/) tool.

## Updating resources

When a resource is updated, the `dateModified` date or `version` should be updated in the resource and the catalogue as the Prez Manifest tool relies on this to determine when to update data.

If a new resource is added to the catalogue, ensure its IRI is added to `schema:hasPart` in [`catalogue.ttl`](./catalogue.ttl).

Pull requests will trigger validation of the manifest, which is required to pass before merging.

## Spatial Datasets
Metadata for spatial datasets & feature collections are located in [`datasets/metadata/`](./datasets/metadata) in Turtle files, and the features per feature collection are located in [`datasets/features/`](./datasets/features) in TriG files. Due to the limit of 100MiB per file on GitHub, some features files are split into parts.

A script is provided ([`extract_features.py`](./extract_features.py)) to split N-quads files from raw data (stored in the IDN cloud's object storage) into Turtle & TriG files to store in git.


## Catalogue Resources
| Resource                                                                                                                                                                 | Role                                                                                                                    | Description                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Catalogue Definition:<br />[`catalogue.ttl`](catalogue.ttl)                                                                                                              | [Catalogue Data](https://prez.dev/ManifestResourceRoles/CatalogueData)                                                  | The definition of, and metadata for, the container which here is a sdo:DataCatalog object                    |
| Resource Data:<br />[`resources/*.ttl`](resources/*.ttl)                                                                                                                 | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                    | sdo:CreativeWork objects in RDF (Turtle) files in the resources/ folder                                      |
| Resource Data:<br />[`resources/isu-archive.ttl`](resources/isu-archive.ttl)                                                                                             | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                    | sdo:CreativeWork objects in RDF (Turtle) files in the resources/ folder                                      |
| Profile Definition:<br />[`ogc_records_profile.ttl`](https://raw.githubusercontent.com/RDFLib/prez/refs/heads/main/prez/reference_data/profiles/ogc_records_profile.ttl) | [Catalogue & Resource Model](https://prez.dev/ManifestResourceRoles/CatalogueAndResourceModel)                          | The default Prez profile for Records API                                                                     |
| Labels:<br />[`labels.ttl`](labels.ttl)                                                                                                                                  | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing labels for catalogue's content, auto-extracted from KurrawongAI's Semantic Background |
| Manual Labels:<br />[`labels-manual.ttl`](labels-manual.ttl)                                                                                                             | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing labels for catalogue's content, manually created                                      |
