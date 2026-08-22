# Sync todo: DataPrototypeTransformationProps

Input class: DataPrototypeTransformationProps · Generated: 2026-08-22 · Queue order = row order
(resume = first row still `[ ]`; all rows `[x]` = sync finished)

## Phase 0 closure (confirmed by user)

Input: `DataPrototypeTransformationProps` (Table 7.17, p.787) · Base: `ARObject` · Aggregated by `TransformationISignalProps.dataPrototypeTransformationProps`
Replaces the Rule 0001.10 placeholder in `TransformationISignalProps` (commit 4ba99f8c).

Skip (exist + stamped): `SwDataDefProps` (Table 5.39); referents `DataPrototype`, `AutosarDataPrototype`,
`AbstractImplementationDataTypeElement`, `ApplicationCompositeElementDataPrototype`, `AtpInstanceRef`, `ARObject`.

| Status | Class | Role | Source | Table | Notes |
|---|---|---|---|---|---|
| [ ] | DataPrototypeReference | base/member | markdown | Table 7.18 | abstract; parent of XSD-choice subclasses; attr tagId |
| [ ] | DataPrototypeInPortInterfaceInstanceRef | base | markdown | Table B.6 | abstract; atpAbstract attrs; parent of iref classes |
| [ ] | DataPrototypeInClientServerInterfaceInstanceRef | member (iref) | markdown | Table 7.21 | iref target of DataPrototypeInPortInterfaceRef |
| [ ] | DataPrototypeInSenderReceiverInterfaceInstanceRef | member (iref) | markdown | Table 7.20 | iref target of DataPrototypeInPortInterfaceRef |
| [ ] | DataPrototypeInPortInterfaceRef | member (XSD choice) | markdown | Table 7.19 | subclass of DataPrototypeReference |
| [ ] | ImplementationDataTypeElementInPortInterfaceRef | member (XSD choice) | markdown | Table 7.22 | subclass of DataPrototypeReference |
| [ ] | TransformationProps | member (ref target) | markdown | Table 7.15 | abstract; ref target of transformationProps |
| [ ] | DataPrototypeTransformationProps | input | markdown | Table 7.17 | aggr dataPrototypeInPortInterfaceRef; aggr networkRepresentationProps (SwDataDefProps); ref transformationProps |
