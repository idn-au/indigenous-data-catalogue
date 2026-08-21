# Set up an Indigenous data catalogue

**A practical guide to planning, establishing, publishing and operating a catalogue**

| Document information | Value |
| --- | --- |
| Status | Draft for governance, policy, user and technical review |
| Intended users | Indigenous organisations, Indigenous Data Network nodes, project teams, data custodians, data stewards and technical implementers |
| Possible uses | Internal planning guide, implementation workbook, training resource or public web guidance |
| Maintainer | To be assigned by the publishing organisation |
| Review cycle | At least annually, and when governance arrangements, the IDN Catalogue Profile or major platform components change |

> **About this draft**
>
> This guide is designed to be useful before a publishing format has been chosen. It can be kept as Markdown, published as a set of web pages, or converted into a document. Organisation-specific information should be recorded in the [local implementation supplement](#appendix-b-local-implementation-supplement-template), which may be kept internal even if the main guide is published.

## Contents

1. [What this guide is for](#1-what-this-guide-is-for)
2. [Start with purpose, not software](#2-start-with-purpose-not-software)
3. [Decide what kind of catalogue arrangement you need](#3-decide-what-kind-of-catalogue-arrangement-you-need)
4. [Identify the people, organisations and roles](#4-identify-the-people-organisations-and-roles)
5. [Establish governance before publication](#5-establish-governance-before-publication)
6. [Define the catalogue's scope](#6-define-the-catalogues-scope)
7. [Choose a delivery and support model](#7-choose-a-delivery-and-support-model)
8. [Design the metadata workflow](#8-design-the-metadata-workflow)
9. [Prepare metadata for publication](#9-prepare-metadata-for-publication)
10. [Understand the technical architecture](#10-understand-the-technical-architecture)
11. [Plan and implement the platform](#11-plan-and-implement-the-platform)
12. [Load and test the first catalogue records](#12-load-and-test-the-first-catalogue-records)
13. [Approve and launch the catalogue](#13-approve-and-launch-the-catalogue)
14. [Operate and improve the catalogue](#14-operate-and-improve-the-catalogue)
15. [Know when to seek specialist assistance](#15-know-when-to-seek-specialist-assistance)
16. [End-to-end readiness checklist](#16-end-to-end-readiness-checklist)
17. [Further information](#17-further-information)
18. [Appendix A: responsibility matrix](#appendix-a-responsibility-matrix)
19. [Appendix B: local implementation supplement](#appendix-b-local-implementation-supplement-template)
20. [Appendix C: record review worksheet](#appendix-c-record-review-worksheet)

## 1. What this guide is for

An Indigenous data catalogue helps people discover and understand data, collections, projects, services and other resources. It can make resources more visible while communicating who is connected to them, who should be contacted, what access conditions apply and what responsibilities must be respected.

A catalogue is not simply a website or a piece of software. It is an ongoing service that combines:

- purpose and community benefit;
- authority and governance;
- relationships with the people and communities represented in data;
- metadata and controlled vocabularies;
- review and publication workflows;
- technical infrastructure;
- support, maintenance and resourcing.

This guide helps an organisation understand and coordinate that complete service. It is intended to help readers make informed decisions, allocate responsibilities and recognise when specialist support is required. It does not assume that one person should be able to perform every task.

### 1.1 What “catalogue” means in this guide

The word **catalogue** can refer to several levels at once. A catalogue can describe individual resources, but it can also describe or aggregate smaller catalogues. Before planning any implementation, state which level is being discussed.

| Level | Meaning | Typical responsibility | Example outcome |
| --- | --- | --- | --- |
| **Network or IDN-level catalogue** | A discovery layer across multiple IDN nodes, organisations or contributing catalogues—a catalogue of catalogues, and potentially of their records | IDN-level governance and service operators, working with contributing nodes | Users can discover participating catalogues and search or navigate resources across them |
| **Node or organisational catalogue** | A catalogue governed by an IDN node, organisation or organisational unit | The node or organisation, such as ISU, and the relevant resource custodians and rights holders | Users can discover the organisation's collections, projects, datasets and other resources |
| **Project or collection catalogue** | A bounded catalogue maintained for a particular project, program, archive or collection | The project or collection governance group and its responsible organisation | Users can discover resources within that project or collection |
| **Catalogued resource or item** | A dataset, project, collection, creative work or other thing described by a catalogue | The parties connected to that resource | A resource with identifier, description, Indigenous characterisation, roles, rights, access information |

These levels are **logical and governance levels**, not necessarily separate websites or software installations. For example:

- a project may maintain records that are published within its organisation's catalogue;
- an organisational catalogue may be listed in an IDN-level catalogue of catalogues;
- selected organisational records may also be aggregated into an IDN-wide discovery view;
- one Prez deployment may serve several catalogues;
- a catalogue at one level may itself be a catalogued resource at the level above it.

Use qualified language throughout planning and documentation:

- “IDN-level catalogue” or “network discovery service”;
- “ISU organisational catalogue” or “node catalogue”;
- “the **[name]** project catalogue”;
- “collection record” or “catalogued resource.”

Avoid saying only “the catalogue” unless the level is already unambiguous.

#### A project or collection is not automatically a catalogue

A project or collection can be represented in two different ways:

1. as a **single catalogued resource** in a node or organisational catalogue; or
2. as a **catalogue in its own right** when it aggregates and describes multiple resources that need their own records.

Likewise, a collection-level record can describe a collection as one resource without exposing or cataloguing every item within it. Choose the level of description deliberately according to purpose, authority, sensitivity, user need and capacity to maintain the records.

### 1.2 What the guide covers

The guide covers the path from an initial idea to an operating catalogue:

1. determine why the catalogue is needed;
2. decide whether to join an existing catalogue or establish another one;
3. identify rights, interests, responsibilities and decision-makers;
4. define the catalogue's scope and governance;
5. select a delivery and support model;
6. prepare, review and validate metadata;
7. implement and test the technical platform;
8. approve and publish catalogue records;
9. maintain, correct, review and, when necessary, withdraw them.

### 1.3 What the guide does not cover

This guide does not:

- replace engagement with Aboriginal and Torres Strait Islander peoples or other Indigenous peoples represented in the catalogue;
- confer authority to publish information;
- constitute legal advice;
- make restricted or sensitive data safe to publish;
- require publication of the data described by a catalogue record;
- reproduce the full installation manuals for Prez, Prez UI or an RDF database;
- prescribe a single governance model for all organisations or communities.

### 1.4 Metadata is not automatically harmless

Publishing metadata is different from publishing the data itself, but metadata can still reveal sensitive information. A title, description, place, person, community, subject, access note or relationship may disclose information that should not be public.

Treat catalogue metadata as published information. Apply appropriate authority, cultural review, privacy, security and rights processes before publication.

## 2. Start with purpose, not software

Before choosing software, write a short catalogue purpose statement. It should be understandable to someone outside the project.

Answer the following questions:

- Who is the catalogue intended to benefit?
- What problem will it solve?
- Who has asked for it?
- What resources will it help people discover?
- What should a user be able to do after finding a record?
- Will the catalogue describe resources, provide access to them, or both?
- How will Indigenous peoples and communities participate in decisions?
- What information must not be made public?
- Who will remain accountable after the implementation project ends?
- How will the organisation know whether the catalogue is useful?

### 2.1 Purpose statement template

> The **[catalogue name]** helps **[intended users and beneficiaries]** to discover and understand **[types of resources]** so that **[intended benefit]**. The catalogue is governed by **[authority or group]**, operated by **[organisation or team]**, and reviewed with **[relevant peoples, communities or representatives]**. It publishes **[metadata and/or data]** subject to **[key rights, access and cultural governance arrangements]**.

### 2.2 Minimum evidence of readiness

Do not move directly to implementation merely because software or funding is available. Before technical work begins, the organisation should have at least:

- an agreed purpose;
- an accountable organisational sponsor;
- a preliminary scope;
- a way to identify relevant owners, rights holders, custodians and representatives;
- a decision-making and escalation pathway;
- staff time or service funding for ongoing operation;
- an initial view of what will and will not be public.

If these are absent, the next step is governance and service design, not platform deployment.

## 3. Decide what kind of catalogue arrangement you need

“Setting up a catalogue” can mean establishing a new catalogue at one level, contributing a collection to a catalogue at another level, or adding a catalogue to a catalogue of catalogues. Clarify both the **catalogue level** and the **technical arrangement** early.

### 3.1 First choose the level of responsibility

#### IDN or network level

At the IDN level, the primary task is not to take over the detailed governance of every contributed resource. It is to provide trusted cross-network discovery and interoperability while preserving the responsibilities and context of contributing nodes.

IDN-level decisions include:

- which node or organisational catalogues may participate;
- minimum metadata and conformance expectations;
- how catalogues and records are identified across the network;
- whether records are harvested, copied, queried, linked or manually contributed;
- how source provenance and the authoritative record are shown;
- which network-wide vocabularies, profiles and shared reference data are used;
- how duplicate or overlapping records are handled;
- what IDN-level search, navigation and branding imply;
- how corrections are routed to the authoritative node or custodian;
- when the network service may temporarily suppress a harmful or invalid record;
- what happens when a node leaves or its service is unavailable.

An IDN-level catalogue should make clear that inclusion does not transfer ownership, custodianship or rights to IDN unless a separate agreement says so.

#### Node or organisational level

At the node level, the organisation determines which of its projects, collections and resources are described and how they are governed and maintained.

Node-level decisions include:

- the organisation's catalogue purpose and scope;
- which projects and collections may contribute;
- record approval and publication authority;
- relationships with owners, rights holders, custodians, subject agents and representatives;
- metadata stewardship and quality;
- local correction, dispute and takedown processes;
- how metadata is supplied to an IDN-level service;
- whether smaller collection catalogues remain distinct or are represented as collections within the node catalogue.

The Indigenous Studies Unit catalogue is an example of this organisational or node level. It may contain records for projects, collections and individual resources while also being discoverable as a catalogue within the wider IDN service.

#### Project or collection level

At the project or collection level, work is closer to the source resources and relevant relationships. The first question is whether a separate catalogue is needed at all.

Project- or collection-level decisions include:

- whether to create one collection or project record, or many item-level records;
- who has authority and relevant interests in the resources;
- which information is held by the project but should not be published;
- how source identifiers, descriptions and provenance are maintained;
- who reviews and approves records;
- how changes are supplied to the node catalogue;
- what happens when the project ends;
- who becomes the continuing custodian and point of contact.

A temporary project should not create a permanent catalogue service without an agreed destination, custodian and maintenance plan.

### 3.2 Then choose the technical arrangement

After selecting the level, decide how it will be delivered. A logical catalogue does not automatically require a separate Prez deployment.

#### Contribute records to an existing catalogue

Choose this path when an existing catalogue has suitable governance, scope and services, and the responsible parties agree to contribute records to it.

Questions to ask:

- Does the existing catalogue accept these kinds of resources?
- Who retains responsibility for each record?
- Who can approve, update or withdraw a record?
- What metadata profile and identifiers are required?
- How are sensitive or disputed records handled?
- What support and service levels are provided?
- Can records be exported or migrated later?

This path can reduce technical overhead, but it does not remove governance, metadata or maintenance responsibilities.

#### Establish a collection or catalogue within a shared service

Choose this path when the organisation needs a distinct identity or collection but can share infrastructure with other catalogues.

Agree on:

- collection ownership and branding;
- infrastructure ownership;
- administrative access;
- separation of data and permissions;
- release and upgrade arrangements;
- support responsibilities;
- exit and migration arrangements.

#### Establish a separate catalogue instance

Choose this path only when a separate instance is justified by governance, control, security, branding, integration, performance or service requirements.

A separate instance normally requires ongoing responsibility for:

- hosting and domain names;
- security updates and dependency management;
- the RDF database;
- Prez and Prez UI configuration;
- monitoring, logs and incident response;
- backups and restoration testing;
- deployments and upgrades;
- user support;
- metadata loading and validation.

### 3.3 Decide how levels connect

For each connection between a project, node and IDN-level service, document:

| Question | Decision to record |
| --- | --- |
| Authoritative source | Which system or catalogue owns the authoritative version of the metadata? |
| Aggregation method | Link, harvest, query, copy, file transfer or manual contribution? |
| Identifier behaviour | Will the same resource IRI be retained at every level? |
| Record selection | Are all records shared, or only an approved subset? |
| Update frequency | How quickly do additions, corrections and withdrawals propagate? |
| Provenance | How does a user see the source catalogue and responsible node? |
| Validation | Which checks occur at project, node and network levels? |
| Corrections | Where does a user report a concern, and who owns the response? |
| Emergency action | Who can temporarily suppress a record at each level? |
| Exit | What happens to records and identifiers if a project, node or service ends? |

Do not create a disconnected copy at each level without a synchronisation, correction and withdrawal process.

### 3.4 Decision record

Record the decision, not only the result.

| Question | Decision |
| --- | --- |
| Catalogue level | IDN/network / node/organisation / project/collection |
| Description resolution | Catalogue of catalogues / catalogue of resources / collection-level record / item-level records |
| Technical arrangement selected | Existing catalogue / shared service / separate instance |
| Parent catalogue or discovery service |  |
| Child catalogues or contributing collections |  |
| Authoritative metadata source |  |
| Aggregation or synchronisation method |  |
| Reasons |  |
| Governance advantages |  |
| Technical and operational consequences |  |
| Estimated establishment cost |  |
| Estimated annual operating effort or cost |  |
| Responsible decision-maker |  |
| Review date |  |

## 4. Identify the people, organisations and roles

Catalogue work involves two related kinds of role:

1. **Data-resource roles** describe how a person or organisation relates to a catalogued resource.
2. **Operational roles** describe work performed to establish and run the catalogue service.

Do not treat these as interchangeable. A system administrator may operate the platform without having authority to decide whether a resource should be published.

### 4.1 Data-resource roles

Use terms from the [IDN Role Codes vocabulary](https://data.idnau.org/pid/glossary/dataRoles-vocabulary) when recording how agents relate to resources. Relevant roles include:

| Role | Practical meaning for catalogue work |
| --- | --- |
| Owner | The party that owns the resource. Ownership does not necessarily settle all cultural, ethical, privacy or publication questions. |
| Rights holder | The party that owns or manages rights over the resource. |
| Custodian | The party that accepts accountability and responsibility for the resource and ensures its appropriate care and maintenance. |
| Subject agent | A party about whom the resource contains information. |
| Subject agent representative | A party who can be contacted and best represents the interests of a subject agent. |
| Stakeholder | A party with an interest in the resource or its use. |
| Resource provider | The party that supplies the resource. |
| Originator | The party that created the resource. |
| Processor | The party that has processed or modified the data. |
| Publisher | The party that publishes the resource. |
| Point of contact | The party who can be contacted for knowledge about or acquisition of the resource. |
| User | A party who uses the resource. |

Other vocabulary roles may apply. Select roles according to the actual relationship, not merely a person's job title.

### 4.2 Operational roles

The following labels are useful for organising the work, but are not substitutes for the data-resource vocabulary:

| Operational role | Typical responsibilities |
| --- | --- |
| Organisational sponsor | Secures authority, resources and organisational support; resolves major escalations. |
| Governance authority or group | Makes or oversees decisions about scope, publication, cultural governance, risk and disputes. |
| Catalogue service owner | Accountable for the catalogue as an ongoing organisational service. |
| Data steward | Coordinates record preparation, quality, review, publication, correction and periodic maintenance. |
| Metadata specialist | Maps source information to the catalogue profile and controlled vocabularies. |
| System administrator | Deploys, secures, monitors, backs up and upgrades the technical platform. |
| Developer or integration specialist | Builds repeatable transformations, integrations or user-interface changes. |
| Support contact | Receives enquiries, correction requests and incident reports and routes them appropriately. |
| Records contributor | Supplies information for one or more catalogue records. |
| Reviewer | Performs cultural, rights, privacy, metadata, accessibility or technical review. |

One person may hold several operational roles in a small organisation, but responsibilities and conflicts should still be explicit. Avoid making publication dependent on one person's undocumented knowledge.

### 4.3 Assign roles for both the service and each record

The catalogue service needs named responsibilities, and individual records need their relevant parties identified. For example:

- the catalogue service owner may be an organisational unit;
- the system administrator may be an internal IT team or provider;
- the custodian may vary between records;
- the owner and rights holder may not be the same party;
- the appropriate subject agent representative may depend on the resource;
- the publisher may operate the catalogue without owning the resources it describes.

Use the [responsibility matrix](#appendix-a-responsibility-matrix) to document service-level responsibilities.

## 5. Establish governance before publication

Governance is the continuing system by which decisions are made, recorded, reviewed and challenged. It should cover the catalogue service and individual records.

### 5.1 Governance questions

Agree on:

- who may propose a record;
- who identifies relevant owners, rights holders, subjects, communities and representatives;
- who decides whether engagement or further authority is required;
- who reviews descriptions, names, places, subjects and relationships;
- who determines access and rights statements;
- who approves publication;
- who can require correction, restriction or withdrawal;
- how disagreements are handled;
- what evidence of decisions is retained;
- how urgent concerns are escalated;
- how governance arrangements are reviewed.

### 5.2 Indigenous governance and participation

A catalogue about Indigenous data should not rely solely on institutional ownership or possession as a basis for publication. The appropriate process will depend on the resources, peoples, communities and context involved.

The organisation should determine, with appropriate Indigenous leadership and participation:

- whose interests and authority are relevant;
- how those parties will participate in decisions;
- whether existing relationships or agreements cover catalogue publication;
- how collective interests are recognised;
- how culturally sensitive information is identified;
- how contested names, descriptions or relationships are represented;
- how restrictions, notices or contextual information are communicated;
- how people can request correction or removal;
- how benefits and possible harms will be assessed.

Do not use a generic checklist as a substitute for relationships, dialogue or authority.

### 5.3 Publication decision record

For each record, retain an appropriate decision record. Depending on risk and organisational policy, it might include:

- resource identifier and title;
- proposed public metadata;
- relevant parties and their roles;
- engagement undertaken;
- source of authority or approval;
- rights and access decisions;
- identified risks and mitigations;
- conditions or review date;
- approver and date;
- links to supporting records held in an appropriate system.

Do not place confidential evidence or personal information in a public code repository merely because the public metadata is maintained there.

### 5.4 Correction, dispute and takedown pathway

Publish a clear contact route. Internally, define how the organisation will:

1. acknowledge a concern;
2. assess whether urgent restriction or temporary withdrawal is required;
3. notify the custodian and relevant decision-makers;
4. engage with affected parties;
5. decide and document an outcome;
6. correct, annotate, restrict or withdraw the record;
7. notify the person who raised the concern, where appropriate;
8. retain an appropriate audit history without republishing harmful information.

Set response targets appropriate to risk. A potentially harmful disclosure should not wait for an ordinary editorial meeting.

## 6. Define the catalogue's scope

Scope prevents a catalogue from becoming an unbounded promise.

### 6.1 Scope statement

Document:

- included resource types;
- excluded resource types;
- geographic, community, organisational, subject or time boundaries;
- whether records describe data, projects, services, collections, publications or other resources;
- whether the underlying resources are public, restricted or mixed;
- the minimum information required for a record;
- who may contribute records;
- relationships to other catalogues;
- expected review frequency;
- conditions for withdrawal or archiving.

### 6.2 Start with a bounded collection

For an initial release, prefer a collection that:

- has a clear custodian;
- has a manageable number of records;
- has reasonably consistent source information;
- has identifiable owners, rights holders and contacts;
- can be meaningfully reviewed;
- represents real user needs;
- includes enough variation to test the workflow.

Avoid using only artificially simple records. The pilot should expose questions about incomplete, restricted, sensitive or contested information before full-scale publication.

### 6.3 Define success

Possible measures include:

- records published and reviewed, not merely imported;
- proportion with current custodians and points of contact;
- time taken to correct a record;
- successful resolution of identifier links;
- metadata validation results;
- search and navigation usability;
- use by intended communities and organisations;
- qualitative feedback about usefulness, context, safety and trust;
- sustainability of the operating workload.

Page views alone do not demonstrate community benefit.

## 7. Choose a delivery and support model

Technical confidence should influence the support model, not determine who has decision-making authority.

### 7.1 Self-managed

The organisation deploys and operates the platform.

Suitable when it has continuing capability for:

- RDF and metadata processing;
- containerised or application hosting;
- an RDF database and SPARQL;
- DNS and TLS certificates;
- security and dependency updates;
- monitoring and incident response;
- backups and restoration;
- Prez and Prez UI upgrades;
- user and contributor support.

The organisation may still obtain specialist assistance for initial design or unusual problems.

### 7.2 Assisted implementation

The organisation retains service ownership and governance while a partner helps with implementation or selected operations.

Document:

- what the organisation performs;
- what the partner performs;
- handover expectations;
- documentation and training requirements;
- response times;
- ownership of configuration, code and identifiers;
- access to backups and exports;
- upgrade and support arrangements.

### 7.3 Managed service

A provider operates some or all of the platform under an agreement.

The agreement should cover:

- service scope and availability;
- security responsibilities;
- locations and handling of data and metadata;
- access control;
- backups and restoration;
- incident notification;
- software upgrades;
- record loading and correction processes;
- export and portability;
- termination and transition assistance;
- ownership of domain names, identifiers, configuration and content.

Outsourcing the platform does not outsource the organisation's governance responsibilities.

### 7.4 Support-model checklist

- [ ] The ongoing service owner is named.
- [ ] Governance responsibility remains explicit.
- [ ] Metadata stewardship is resourced.
- [ ] Technical responsibilities are assigned.
- [ ] Support and escalation arrangements are documented.
- [ ] Costs beyond the initial project are understood.
- [ ] The organisation can export its metadata.
- [ ] Exit and migration arrangements are documented.
- [ ] No critical process depends on one person's private knowledge or account.

## 8. Design the metadata workflow

A catalogue record should move through an agreed lifecycle rather than being uploaded directly from a spreadsheet to production.

### 8.1 Recommended lifecycle

```text
Propose a resource
  -> identify relevant parties and authority
  -> gather source information
  -> prepare draft metadata
  -> conduct cultural, rights, privacy and content review
  -> validate identifiers, terms and profile conformance
  -> approve publication
  -> publish to staging
  -> test
  -> publish to production
  -> monitor, correct and periodically review
  -> withdraw or archive when required
```

### 8.2 Workflow stages

| Stage | Main question | Typical participants | Evidence or output |
| --- | --- | --- | --- |
| Proposal | Is the resource in scope and worth describing? | Contributor, data steward, custodian | Accepted proposal |
| Authority assessment | Who has relevant rights, responsibilities and interests? | Owner, rights holder, custodian, subject agent representative, governance authority | Parties and engagement pathway |
| Metadata preparation | What can be accurately and appropriately said? | Data steward, metadata specialist, processor, point of contact | Draft record and source notes |
| Review | Is the proposed metadata accurate, authorised and safe to publish? | Relevant parties and reviewers | Review outcomes and changes |
| Validation | Does the record meet technical and profile requirements? | Metadata specialist, system administrator | Validation report |
| Approval | May this version be published? | Assigned approver or governance authority | Dated approval |
| Staging and testing | Does the record behave correctly in the catalogue? | Data steward, system administrator, user testers | Test results |
| Publication | Is the approved record available and discoverable? | Publisher, system administrator | Published record and release record |
| Maintenance | Is it still correct, current and appropriate? | Custodian, point of contact, data steward | Review, correction or withdrawal |

### 8.3 Separate source, working and published information

Maintain a clear distinction between:

- **source information** received from systems or contributors;
- **working information** used during mapping and review;
- **approved public metadata** loaded into the catalogue;
- **decision and audit information** held in appropriate organisational systems.

This supports traceability without publishing internal notes or sensitive evidence.

### 8.4 Batch imports still require record governance

Automation can transform and validate thousands of records, but it cannot assume that each record is authorised or culturally appropriate to publish. For batch work:

- define which decisions can be made for the collection as a whole;
- identify records requiring individual review;
- record source and transformation provenance;
- produce exception reports;
- sample and inspect transformed records;
- prevent failed or unapproved records from reaching production.

## 9. Prepare metadata for publication

### 9.1 Use the IDN Catalogue Profile

The [IDN Catalogue Profile](https://data.idnau.org/pid/cp) defines the project guidance for describing catalogue resources for IDN and Prez-style publication. Use its current specification, examples and validation resources rather than copying requirements into a local, unmaintained specification.

Because profiles evolve, record which version or revision was used for a release and reassess conformance when the profile changes.

### 9.2 Use stable identifiers

Assign HTTP or HTTPS persistent identifier IRIs to resources intended for publication wherever possible.

Good identifiers should:

- remain stable when labels, hosting or internal systems change;
- resolve through an organisation-controlled or trusted identifier service;
- identify the resource, not merely the current web page;
- avoid exposing confidential source keys;
- have documented ownership and maintenance arrangements.

Do not duplicate an HTTP/HTTPS PID IRI as a separate `schema:PropertyValue` identifier node. If a non-HTTP catalogue identifier must be recorded, use the pattern required by the current IDN Catalogue Profile; project guidance uses `schema:identifier` with an `xsd:token` value for such identifiers.

### 9.3 Preserve source meaning and provenance

During migration or transformation:

- preserve source identifiers where appropriate;
- keep controlled-list values as vocabulary concepts where suitable;
- retain qualifiers, provenance and uncertainty;
- do not silently replace ambiguous values with more certain claims;
- keep a repeatable mapping from source fields to RDF properties;
- record transformations and known limitations;
- represent source relationships explicitly when their identity or qualifiers matter.

Uncertainty should be visible to reviewers. It can be expressed in notes, provenance or review records rather than hidden by normalisation.

### 9.4 Use published vocabularies where they fit

Prefer stable, published terms from vocabularies such as Schema.org, DCTERMS, SKOS, ODRL and IDN vocabularies where they accurately express the source meaning. Preserve project-specific terms when they are needed for source semantics, qualifiers, provenance or uncertainty.

For roles, use concepts from the [IDN Role Codes vocabulary](https://data.idnau.org/pid/glossary/dataRoles-vocabulary). Do not invent slightly different local spellings when an appropriate published concept exists.

### 9.5 Describe access carefully

A catalogue record should distinguish discovery from access. A public metadata record does not imply that the described data is public.

For a genuinely public sample or resource, current project guidance uses:

```turtle
schema:conditionsOfAccess "Public"@en ;
```

Use a more specific, approved access statement when required. Do not use `schema:permissions` as a generic indication that data is public. If access is conditional, identify the process and point of contact without exposing restricted information.

### 9.6 Minimum quality questions

For each record, ask:

- Does the identifier resolve and identify the intended resource?
- Is the title understandable and appropriate?
- Is the description accurate, contextualised and safe to publish?
- Are relevant peoples, organisations and communities represented appropriately?
- Are roles assigned to the correct parties?
- Are rights and access statements clear?
- Is there a current point of contact?
- Are locations, dates, subjects and relationships accurate?
- Are controlled terms used consistently?
- Is provenance sufficient to trace the record to its source?
- Are uncertainty and limitations visible?
- Has the record passed the required governance and technical reviews?

## 10. Understand the technical architecture

An IDN-style web catalogue normally involves several components. Exact arrangements may vary.

```text
Source systems, spreadsheets or RDF files
              |
              v
Mapping, transformation and validation
              |
              v
       RDF database / SPARQL endpoint
              |
              v
            Prez API
              |
              v
            Prez UI
              |
              v
      Catalogue users and clients
```

Supporting services may include persistent identifier resolution, DNS, TLS, monitoring, logging, backups, deployment automation and source control.

### 10.1 A multi-level catalogue architecture

A network implementation may add aggregation above the component view:

```text
Project or collection sources
     |              |
     v              v
Project records or project catalogue
              |
              v
Node / organisational catalogue (for example, ISU)
              |
              v
IDN-level catalogue of catalogues and/or aggregated discovery
              |
              v
Users discover the source catalogue and its resources
```

The arrows do not require copying. They may represent links, harvesting, shared storage, queries or controlled publication pipelines. The chosen method should preserve:

- stable resource identifiers;
- the authoritative source;
- provenance;
- responsible parties and contacts;
- withdrawal and correction signals;
- the governance context needed to understand the record.

The IDN-level service, node catalogue and project catalogue may share infrastructure. Conversely, they may use separate infrastructure while participating in one discovery network. Governance boundaries and software boundaries should be documented separately.

### 10.2 RDF data and database

Catalogue metadata is represented as RDF. It may be maintained as version-controlled RDF files, generated from other sources, loaded directly into an RDF database, or managed through a combination of these methods.

The RDF database provides a SPARQL endpoint from which Prez reads. Treat database selection and operation as a production service decision: consider support, backup, access control, performance, upgrades and restoration.

### 10.3 Prez API

[Prez](https://github.com/RDFLib/prez) is a data-configurable Linked Data API framework. It reads from the configured RDF repository and provides catalogue, collection, item, search, profile and related endpoints.

Prez is not, by itself, the public graphical website. Its maintained repository provides current installation, configuration, container and validation information. Link to that documentation rather than reproducing changing commands in this guide.

### 10.4 Prez UI

[Prez UI](https://github.com/RDFLib/prez-ui) is the user-interface application that renders information obtained from Prez. It requires separate deployment and configuration decisions, including branding, public API location and user-facing behaviour.

### 10.5 IDN Catalogue Profile and reference data

The catalogue profile describes expected resource structures and semantics. Prez also needs relevant labels, prefixes, profiles and other reference data so that IRIs can be presented meaningfully.

Plan how profile and vocabulary changes will be introduced, tested and promoted. Do not make uncontrolled changes directly in production.

### 10.6 Metadata entry is a separate capability

Prez publishes and presents RDF; it is not automatically a metadata-entry and governance workflow tool. An organisation may prepare records using:

- controlled spreadsheets and repeatable transformations;
- RDF files in a reviewed source-control workflow;
- forms or a purpose-built metadata application;
- integrations with existing collection, research or records systems;
- a managed contribution process.

Choose an authoring approach based on users, volume, review needs and support capability. Do not assume that non-technical contributors should edit Turtle or use GitHub.

## 11. Plan and implement the platform

This section identifies the implementation work. Use the maintained component documentation for exact commands and configuration.

### 11.1 Environments

Use separate environments appropriate to the service's risk and scale:

- **development** for implementation work;
- **staging or test** for approved pre-publication testing;
- **production** for the public service.

Do not use the public production catalogue as the only place to test transformations, upgrades or new profiles.

### 11.2 Infrastructure decisions

Document:

- hosting organisation and region;
- production and non-production environments;
- domain names and DNS ownership;
- TLS certificate management;
- RDF database product and version;
- Prez and Prez UI versions;
- container or application runtime;
- network access and firewall rules;
- administrative authentication;
- secrets management;
- backup locations and retention;
- monitoring and alerting;
- log access and retention;
- deployment and rollback process;
- responsible teams and support contacts.

### 11.3 Security baseline

At minimum:

- restrict administrative and database access;
- do not expose update-capable SPARQL endpoints publicly unless explicitly required and secured;
- store secrets outside source files and repositories;
- use supported component versions;
- apply security updates through a tested process;
- collect enough logs to investigate incidents without unnecessarily collecting sensitive information;
- back up configuration and metadata;
- test restoration;
- document incident contacts and actions;
- review third-party access when staff or providers change.

### 11.4 Persistent identifier service

Decide:

- which domain or PID service issues identifiers;
- who controls it;
- how mappings are stored;
- how identifiers resolve to catalogue pages or API resources;
- how resolution will continue if the platform changes;
- how redirects and retired resources are managed.

Persistent identifiers should outlive a particular deployment.

### 11.5 Version and release record

For each production release, record:

- date and release owner;
- catalogue-data revision;
- profile revision;
- Prez version;
- Prez UI version;
- RDF database version;
- configuration revision;
- validation results;
- backup or rollback point;
- known issues.

## 12. Load and test the first catalogue records

### 12.1 Prepare a representative pilot

Include records that test:

- ordinary public descriptions;
- conditional or restricted access;
- several agent roles;
- multiple resource types;
- incomplete source information;
- a record requiring extra review;
- a correction or withdrawal scenario.

### 12.2 Validate before loading

Use layered validation:

1. **Source checks** — required source fields, identifiers and values are present.
2. **RDF syntax checks** — RDF files parse correctly.
3. **Profile validation** — records conform to applicable SHACL shapes and IDN profile requirements.
4. **Semantic review** — the chosen properties, roles and vocabulary concepts express the intended meaning.
5. **Governance review** — the metadata is authorised and appropriate to publish.
6. **Application testing** — the API and UI display and link the record correctly.

Kurra can be used for local RDF querying, formatting and SHACL validation. `riot` or `rapper` can provide quick RDF syntax checks. Use the tools already adopted by the project and keep validation repeatable.

### 12.3 Staging tests

- [ ] Catalogue, collections and items load successfully.
- [ ] Public identifiers resolve correctly.
- [ ] Titles and descriptions display as expected.
- [ ] Agent and vocabulary IRIs have readable labels.
- [ ] Search returns appropriate records.
- [ ] Filters and navigation behave as intended.
- [ ] Access and rights information is visible and understandable.
- [ ] Contact pathways work.
- [ ] Restricted information is not present in pages, APIs, downloads, logs or source repositories.
- [ ] API responses are valid in the supported formats.
- [ ] Broken links and missing labels are reported.
- [ ] Accessibility and common device sizes have been checked.
- [ ] Non-technical users have tested realistic tasks.
- [ ] Correction and withdrawal procedures have been rehearsed.
- [ ] Backup and restoration have been tested.

### 12.4 User acceptance tasks

Ask representative users to attempt tasks such as:

- find resources about a subject or place;
- understand what a record describes;
- identify who owns, holds rights over or maintains a resource;
- understand whether and how access may be requested;
- find the correct contact;
- report an error or concern;
- distinguish catalogue metadata from access to the underlying data.

Record where users hesitate or misinterpret information. Technical correctness does not guarantee understandable guidance.

## 13. Approve and launch the catalogue

### 13.1 Launch approval

Before launch, confirm:

- the governance authority or assigned approver has approved publication;
- record-level reviews and approvals are complete;
- the production support owner accepts the service;
- security and restoration checks have passed;
- public contact and correction pathways are active;
- legal, privacy, accessibility and organisational reviews required by local policy are complete;
- users can understand the catalogue's purpose and limitations;
- known issues and residual risks are accepted and recorded.

### 13.2 Public information

The catalogue should clearly state:

- its purpose and scope;
- who operates it;
- how its governance works at an appropriate level;
- what a catalogue record does and does not imply;
- how to ask about a resource;
- how to request correction, contextualisation or withdrawal;
- applicable rights and reuse information for the catalogue metadata;
- accessibility and privacy information;
- the date or process by which records are reviewed.

### 13.3 Controlled release

Consider an initial limited release before broad promotion. Use it to verify support workload, record quality, navigation and governance processes. A smaller, well-supported catalogue is preferable to a large catalogue that cannot be corrected or maintained.

## 14. Operate and improve the catalogue

Launch is the beginning of the operating service.

### 14.1 Routine activities

| Frequency | Example activities |
| --- | --- |
| Continuous | Monitor availability and errors; receive enquiries and concerns; correct urgent issues. |
| Weekly or as needed | Review proposed and changed records; triage validation failures; publish approved changes. |
| Monthly | Check broken links, failed jobs, storage, backups, certificates and support trends. |
| Quarterly | Review contacts, unresolved requests, software updates, access arrangements and selected records. |
| Annually | Review catalogue purpose, governance, scope, support model, profile conformance, all critical contacts and continuity arrangements. |
| On major change | Reassess privacy, cultural governance, security, accessibility, integrations, identifiers and migration risks. |

Adjust frequencies to risk, scale and organisational policy.

### 14.2 Record review

Review records when:

- the scheduled review date arrives;
- a custodian, owner, rights holder or contact changes;
- access conditions change;
- a resource moves or is withdrawn;
- new cultural, privacy or rights concerns emerge;
- a correction or dispute is received;
- the catalogue profile changes materially;
- automated link or validation checks fail.

### 14.3 Change management

For metadata changes:

- retain source and review traceability;
- validate the changed record;
- obtain approval proportionate to the change;
- test in staging when presentation or behaviour may change;
- publish through a controlled process;
- preserve an appropriate history.

For platform changes:

- review release notes and compatibility;
- test against representative catalogue data;
- back up before deployment;
- define rollback criteria;
- verify the API, UI, identifiers and monitoring after deployment;
- record the released versions.

### 14.4 Withdrawal and archiving

When a record or resource is withdrawn:

- determine whether the identifier should resolve to a withdrawal notice, a successor or a minimal tombstone;
- remove harmful metadata promptly where required;
- avoid breaking persistent identifiers without explanation;
- retain internal evidence according to authorised records-management processes;
- update indexes, downloads and caches;
- notify relevant parties where appropriate;
- document the decision and outcome.

Withdrawal does not always mean erasing all history, but public persistence must not be prioritised over safety, authority or applicable obligations.

### 14.5 Continuity and handover

At least two authorised people or teams should understand each critical operating area. Maintain:

- current architecture and deployment documentation;
- administrative-account ownership;
- repository and domain ownership;
- service-provider contacts and agreements;
- backup and restoration instructions;
- metadata mappings and transformation code;
- governance contacts and decision pathways;
- open risks and known issues;
- a handover checklist for staff or provider changes.

## 15. Know when to seek specialist assistance

Seek Indigenous governance, community engagement, legal, privacy, records, security, metadata or technical assistance when the organisation does not have the necessary authority or capability.

Examples include:

- uncertainty about who can authorise publication;
- potentially sensitive cultural, community, personal or location information;
- competing claims or disputed descriptions;
- complex ownership, licensing or contractual rights;
- security-sensitive metadata or systems;
- large or inconsistent legacy-data migrations;
- custom RDF modelling or profile extensions;
- production infrastructure without internal operational support;
- an incident, harmful disclosure or urgent takedown request;
- changes that may break persistent identifiers;
- inability to test backup restoration or platform upgrades.

The correct outcome of a readiness assessment may be to pause, narrow the scope, join an existing service or fund additional support.

## 16. End-to-end readiness checklist

### Purpose and scope

- [ ] The catalogue's purpose and intended benefit are documented.
- [ ] Its level is explicit: IDN/network, node/organisation, or project/collection.
- [ ] It is clear whether a project or collection is one catalogued resource or a catalogue containing multiple records.
- [ ] Parent catalogues, child catalogues and contributing collections are identified.
- [ ] Intended users and beneficiaries have been identified.
- [ ] Included and excluded resources are defined.
- [ ] The difference between metadata publication and data access is clear.
- [ ] Success measures are agreed.

### Governance

- [ ] An accountable organisational sponsor is named.
- [ ] A catalogue service owner is named.
- [ ] Indigenous governance and participation arrangements are defined.
- [ ] Owners, rights holders, custodians, subject agents and relevant representatives can be identified.
- [ ] Publication authority is documented.
- [ ] Correction, dispute and takedown processes are documented.
- [ ] Decision and audit information has an appropriate, controlled home.

### Delivery model and resourcing

- [ ] Existing, shared and separate-instance options were considered.
- [ ] Self-managed, assisted or managed delivery has been selected deliberately.
- [ ] Ongoing metadata stewardship is funded or assigned.
- [ ] Ongoing technical operation is funded or assigned.
- [ ] Support, escalation, exit and handover arrangements are documented.

### Metadata

- [ ] The current IDN Catalogue Profile has been adopted or deviations are documented.
- [ ] Stable HTTP/HTTPS PID IRIs are planned.
- [ ] Relevant data-resource roles use the IDN Role Codes vocabulary.
- [ ] Source mappings and provenance are documented.
- [ ] The authoritative metadata source is identified across every catalogue level.
- [ ] Aggregation, correction, withdrawal and synchronisation between levels are documented.
- [ ] Cultural, rights, privacy and content reviews are part of the workflow.
- [ ] RDF syntax and SHACL/profile validation are repeatable.
- [ ] Access conditions and contacts are clear.
- [ ] Uncertainty and source limitations are preserved.

### Technology

- [ ] Development, staging and production arrangements are appropriate.
- [ ] RDF database, Prez and Prez UI responsibilities are assigned.
- [ ] Domains, TLS and PID resolution are controlled.
- [ ] Administrative access and secrets are secured.
- [ ] Monitoring and incident response are active.
- [ ] Backups and restoration have been tested.
- [ ] Upgrade, rollback and release-record processes exist.

### Launch and operation

- [ ] Representative users have completed acceptance tasks.
- [ ] Restricted information has been checked across all outputs.
- [ ] Governance and service owners have approved launch.
- [ ] Public help, contact and correction information is available.
- [ ] A controlled initial release has been considered.
- [ ] Review and maintenance schedules are assigned.
- [ ] Continuity does not depend on one individual.

## 17. Further information

Use maintained sources for current specifications and component instructions:

- [IDN Catalogue Profile specification](https://data.idnau.org/pid/cp)
- [IDN Catalogue Profile repository](https://github.com/idn-au/idn-catalogue-profile)
- [IDN Role Codes vocabulary](https://data.idnau.org/pid/glossary/dataRoles-vocabulary)
- [Prez API repository and documentation](https://github.com/RDFLib/prez)
- [Prez UI repository and documentation](https://github.com/RDFLib/prez-ui)
- [Prez manifest resource roles](https://prez.dev/ManifestResourceRoles/)
- [W3C Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-3/)
- [W3C Data Privacy Vocabulary](https://www.w3.org/TR/dpv/)
- [W3C ODRL Information Model](https://www.w3.org/TR/odrl-model/)
- [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/care)

Links to third-party sources do not imply that a source alone supplies the governance or authority required for a particular catalogue.

## Appendix A: responsibility matrix

Complete this matrix before implementation and review it when staff, providers or governance arrangements change.

Use **A** for accountable, **R** for responsible for performing the work, **C** for consulted and **I** for informed. Assign only one accountable role for each activity unless the governance model explicitly requires collective accountability.

| Activity | Sponsor | Governance authority | Service owner | Custodian or relevant parties | Data steward | Metadata specialist | System administrator | Support contact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve purpose and scope |  |  |  |  |  |  |  |  |
| Approve governance model |  |  |  |  |  |  |  |  |
| Select delivery model |  |  |  |  |  |  |  |  |
| Accept a proposed record |  |  |  |  |  |  |  |  |
| Identify relevant parties |  |  |  |  |  |  |  |  |
| Prepare metadata |  |  |  |  |  |  |  |  |
| Conduct cultural and rights review |  |  |  |  |  |  |  |  |
| Validate profile conformance |  |  |  |  |  |  |  |  |
| Approve record publication |  |  |  |  |  |  |  |  |
| Publish a release |  |  |  |  |  |  |  |  |
| Operate and secure the platform |  |  |  |  |  |  |  |  |
| Respond to enquiries |  |  |  |  |  |  |  |  |
| Respond to correction or takedown requests |  |  |  |  |  |  |  |  |
| Review records |  |  |  |  |  |  |  |  |
| Approve platform upgrades |  |  |  |  |  |  |  |  |
| Test backup restoration |  |  |  |  |  |  |  |  |
| Conduct annual service review |  |  |  |  |  |  |  |  |

## Appendix B: local implementation supplement template

> **Handling note:** This supplement may contain internal names, contacts, infrastructure details and security-sensitive information. Keep it in an access-controlled system when necessary. Do not publish secrets, passwords, tokens or recovery codes in this document.

### B.1 Organisation and service

| Item | Local information |
| --- | --- |
| Organisation |  |
| Catalogue name |  |
| Catalogue level | IDN/network / node/organisation / project/collection |
| Parent catalogue or discovery service |  |
| Child catalogues or contributing collections |  |
| Authoritative metadata source |  |
| Aggregation or synchronisation method |  |
| Catalogue purpose |  |
| Public URL |  |
| API URL |  |
| Production commencement date |  |
| Catalogue service owner |  |
| Organisational sponsor |  |
| Governance authority or group |  |
| Public support contact |  |
| Internal incident contact |  |
| Review date |  |

### B.2 Scope

| Item | Local information |
| --- | --- |
| Included resources |  |
| Excluded resources |  |
| Contributing organisations or teams |  |
| Geographic or community scope |  |
| Metadata licence |  |
| Record review frequency |  |
| Related catalogues |  |

### B.3 Governance and approval

| Decision or process | Authority, contact and location of procedure |
| --- | --- |
| Accepting proposed records |  |
| Identifying relevant parties |  |
| Cultural governance review |  |
| Rights and access review |  |
| Privacy review |  |
| Publication approval |  |
| Urgent temporary withdrawal |  |
| Correction and dispute resolution |  |
| Permanent withdrawal |  |
| Annual governance review |  |

### B.4 Metadata workflow

| Item | Local information |
| --- | --- |
| Source systems or files |  |
| Source owner |  |
| Working area |  |
| Transformation process and repository |  |
| Validation process |  |
| Approval record location |  |
| Staging publication process |  |
| Production publication process |  |
| Release frequency |  |
| Record review process |  |

### B.5 Technical inventory

| Component | Product or service | Version or plan | Responsible party | Documentation location |
| --- | --- | --- | --- | --- |
| Source repository |  |  |  |  |
| Transformation tooling |  |  |  |  |
| RDF database |  |  |  |  |
| Prez API |  |  |  |  |
| Prez UI |  |  |  |  |
| Hosting |  |  |  |  |
| Domain and DNS |  |  |  |  |
| PID resolution |  |  |  |  |
| TLS certificates |  |  |  |  |
| Monitoring and alerting |  |  |  |  |
| Logs |  |  |  |  |
| Backups |  |  |  |  |
| Deployment automation |  |  |  |  |

### B.6 Service targets

| Service measure | Target | Responsible party |
| --- | --- | --- |
| Availability |  |  |
| Ordinary support acknowledgement |  |  |
| Urgent concern acknowledgement |  |  |
| Correction publication |  |  |
| Backup frequency |  |  |
| Restoration test frequency |  |  |
| Security update assessment |  |  |
| Record review frequency |  |  |

### B.7 Continuity and exit

- Where are architecture and deployment instructions held?
- Who controls organisational repositories and service accounts?
- Who controls the domain and PID service?
- Where are backups held, and who can restore them?
- How can all catalogue metadata be exported?
- What happens if the current provider or funding arrangement ends?
- Who can authorise emergency technical work?
- When was handover last rehearsed?

## Appendix C: record review worksheet

### C.1 Record identification

| Item | Value |
| --- | --- |
| Resource IRI |  |
| Proposed title |  |
| Resource type |  |
| Source system or reference |  |
| Contributor |  |
| Proposed publication date |  |
| Scheduled review date |  |

### C.2 Relevant parties

Record applicable roles using the IDN Role Codes vocabulary.

| Party | Role | Evidence or source | Contacted or consulted? | Notes or conditions |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### C.3 Review questions

| Question | Yes / No / N/A | Reviewer and notes |
| --- | --- | --- |
| Is the resource within the catalogue's approved scope? |  |  |
| Have relevant owners, rights holders and custodians been identified? |  |  |
| Have subject agents, representatives and stakeholders been considered? |  |  |
| Is there authority to publish this metadata? |  |  |
| Is the title accurate and appropriate? |  |  |
| Is the description accurate, contextualised and safe to publish? |  |  |
| Could any field disclose sensitive information? |  |  |
| Are rights and access conditions clear? |  |  |
| Is the point of contact current and appropriate? |  |  |
| Are identifiers and links correct? |  |  |
| Are published vocabulary concepts used where appropriate? |  |  |
| Are provenance, uncertainty and limitations represented? |  |  |
| Has RDF syntax validation passed? |  |  |
| Has applicable profile or SHACL validation passed? |  |  |
| Has the record been checked in staging? |  |  |

### C.4 Decision

| Item | Value |
| --- | --- |
| Outcome | Approve / approve with conditions / return for changes / do not publish / withdraw |
| Conditions or required changes |  |
| Approver or authority |  |
| Decision date |  |
| Approval record location |  |
| Next review date |  |
