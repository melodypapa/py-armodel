# Bundled AUTOSAR XSD Schemas

Copies of the official AUTOSAR XSDs published on autosar.org, mirrored from this
repository's `autosar/<release>/xsd/` directories so they can ship as package data.
Do not edit the copies; refresh them from the `autosar/` originals (the unit test
`tests/test_armodel/validation/test_bundled_schemas.py::test_bundled_schemas_match_repo_copies`
enforces byte equality).

| Directory | File | Source |
|---|---|---|
| R23-11 | AUTOSAR_00052.xsd | AUTOSAR R23-11 XSD (autosar.org), mirrored at `autosar/R23-11/xsd/` |
| R4.4.0 | AUTOSAR_00046.xsd | AUTOSAR R4.4.0 XSD, mirrored at `autosar/R4.4.0/xsd/` |
| R4.3.1 | AUTOSAR_00044.xsd | AUTOSAR R4.3.1 XSD, mirrored at `autosar/R4.3.1/xsd/` |
| R3.2.3 | AUTOSAR.xsd | AUTOSAR R3.2.3 XSD, mirrored at `autosar/R3.2.3/xsd/` |

`xml.xsd` is the W3C XML namespace schema imported by the R23-11/R4.4.0/R4.3.1
schemas; it is copied next to each importing schema so every directory is
self-contained.
