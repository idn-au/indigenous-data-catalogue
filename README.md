# IDN Keeping Place Catalogue

This is the source data of the [Indigenous Data Network](https://idnau.org/)'s Keeping Place catalogue which has been established as part of 
the IDN's Catalogue Project. This catalogue lists resource of high interest to Australian Indigenous communities that the IDN is keeping long-term archived copies of, to ensure they are not lost due to system or institutional failure.

This catalogue is online at:

- https://data.dev.idnau.org/catalogs/pid:kp-catalogue


## Catalogue Resources

Resource | Role | Description
--- | --- | ---
Catalogue Definition:<br />[`catalogue.ttl`](catalogue.ttl) | [Catalogue Data](https://prez.dev/ManifestResourceRoles/CatalogueData) | The definition of, and metadata for, the container which here is a sdo:DataCatalog object
Resource Data:<br />[`resources/*.ttl`](resources/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData) | sdo:CreativeWork objects in RDF (Turtle) files in the resources/ folder
Profile Definition:<br />[`ogc_records_profile.ttl`](https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttl) | [Catalogue & Resource Model](https://prez.dev/ManifestResourceRoles/CatalogueAndResourceModel) | The default Prez profile for Records API
Labels:<br />[`labels.ttl`](labels.ttl) | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing labels for catalogue's content, auto-extracted from KurrawongAI's Semantic Background
Manual Labels:<br />[`labels-manual.ttl`](labels-manual.ttl) | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing labels for catalogue's content, manually created