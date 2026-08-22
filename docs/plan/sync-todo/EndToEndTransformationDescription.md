# Sync todo: EndToEndTransformationDescription

Input class: EndToEndTransformationDescription · Generated: 2026-08-21 · Queue order = row order
(resume = first row still `[ ]`; all rows `[x]` = sync finished)

| Status | Class | Role | Source | Table | Notes |
|---|---|---|---|---|---|
| [x] | IPdu | base | markdown | Table 6.18 | commit 66a76b19 |
| [x] | SystemSignalGroup | member | markdown | Table 6.13 | commit 6d986fd5 |
| [x] | IPduTiming | member | markdown | Table 6.30 | commit 6ad3cdcd |
| [x] | ISignalGroup | member | markdown | Table 6.12 | commit 60e8454c |
| [x] | ISignalToIPduMapping | member | markdown | Table 6.14 | commit 65bd7cc1 |
| [x] | ISignalIPdu | input | markdown | Table 6.19 | commit ccdfe29a |
| [x] | DataTransformation | member | markdown | Table 7.2 | commit 1dec1aff |
| [x] | TransformationISignalProps | member | markdown | Table 7.8 | commit 4ba99f8c; no stamp; placeholder dataPrototypeTransformationProps (Rule 0001.10) |
| [x] | DataPrototypeTransformationProps | member (deferred) | markdown | Table 7.17 | commit ba255a82; replaces placeholder in TransformationISignalProps; closure classes DataPrototypeReference (7.18), DataPrototypeInPortInterfaceRef (7.19), DataPrototypeInSenderReceiverInterfaceInstanceRef (7.20), DataPrototypeInClientServerInterfaceInstanceRef (7.21), ImplementationDataTypeElementInPortInterfaceRef (7.22) also synced |
| [x] | DataIdModeEnum | member enum | markdown | Table 7.24 | commit 1ea0aa9f; enum synced (p.807, Steps 5/6 N/A) |
| [ ] | EndToEndProfileBehaviorEnum | member enum | markdown | — | enum (Steps 5/6 N/A) |
| [ ] | E2EProfileCompatibilityProps | member | markdown | — | create if missing |
| [ ] | EndToEndTransformationDescription | input | markdown | Table 7.3 | |
