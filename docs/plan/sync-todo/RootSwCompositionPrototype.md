# Sync Queue: RootSwCompositionPrototype

Input class: `RootSwCompositionPrototype`
Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 4.1, p.186 (matches SWCT Table E.39)
Created: 2026-08-22

## Closure (confirmed)
| Class | Role | Notes |
|-------|------|-------|
| RootSwCompositionPrototype | input | Full 9-step sync. No `# Spec:`/marker. Drift: `calibrationParameterValueSet` Mult `*` (list) vs current singular; rename existing field to conform. |
| AtpPrototype | base | Exists, abstract, imported from GenericStructure/AbstractStructure.py. Out of scope (no stamping). |
| CalibrationParameterValueSet | member ref | primitive `RefType`* — no model class |
| FlatMap | member ref | primitive `RefType` |
| CompositionSwComponentType | member tref | primitive `TRefType` |

## Queue (dependency-first)
- [x] RootSwCompositionPrototype (commit `cdde9780`)