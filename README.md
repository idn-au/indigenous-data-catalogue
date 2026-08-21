# The Indigenous Data Catalogue


This catalogue is online at:

- https://data.idnau.org/catalogs/pid:indigenous-data-catalogue

All the resources in this catalogue are listed in the _Catalogue Resources_ section below. These resources are automatically validated and (re)loaded into the catalogue online using the [Prez Manifest](https://pypi.org/project/prezmanifest/) tool.

## Updating resources

When a resource is updated, the `dateModified` date or `version` should be updated in the resource and the catalogue as the Prez Manifest tool relies on this to determine when to update data.

If a new resource is added to the catalogue, ensure its IRI is added to `schema:hasPart` in [`catalogue.ttl`](./catalogue.ttl).

Pull requests will trigger validation of the manifest, which is required to pass before merging.

## Catalogue Resources
