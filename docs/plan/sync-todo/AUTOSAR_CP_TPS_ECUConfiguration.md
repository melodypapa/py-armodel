# Sync Todo — AUTOSAR_CP_TPS_ECUConfiguration

Persistent sync queue (Rule 0016.6). Input scope: **all unstamped classes** listed under
`AUTOSAR_CP_TPS_ECUConfiguration.pdf` in `docs/examples/method_deviation_by_class_v2.md`
(14 inputs) plus their unstamped base/member closure (10 members), confirmed by the end
user. Queue is dependency-first (Rule 0016.5): a class is synced before its dependents.

- Closure confirmed: yes (user picked "Full closure - 24 classes")
- Missing classes: none (every class located in `autosar/markdown/*_TPS_*.md`)
- Skip / XSD-only decisions: none required
- Note: the deviation tracker attributes several of these rows to
  `AUTOSAR_CP_TPS_ECUConfiguration.pdf`, but their authoritative markdown tables live in
  `AUTOSAR_CP_TPS_SystemTemplate.md` / `AUTOSAR_FO_TPS_GenericStructureTemplate.md`
  (located by table grep per Rule 0016.3).

Per-class 9-step sub-checklists are written at file creation and flipped per step
(Rules 0016.6, 0018.2). All rows `[x]` = sync finished. One class per fresh session
(Rule 0017).

---

## Queue

### [x] 1. CommConnectorPort — base (commit 8e6654e)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py:769`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.1
- Role: base of IPduPort
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [x] 2. IPduPort — member (commit 738043f)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py:824`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.3
- Role: ref target of PduTriggering.iPduPort; extends CommConnectorPort
- Note: synced in dedicated queue docs/plan/sync-todo/IPduPort.md (user chose "Only IPduPort"); marker stamped in commit 738043f.
- Steps: (same 9-step checklist as row 1)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 3. ISignalTriggering — member
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1683`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.16
- Role: ref target of PduTriggering.iSignalTriggering
- Tracker deviation: type (spec many vs py single)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 4. PduToFrameMapping — member
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:38`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.29
- Role: aggr member of Frame.pduToFrameMapping
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 5. Frame — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:93`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.78
- Base: FibexElement (stamped ✓); depends on PduToFrameMapping (row 4)
- Tracker deviation: missing pduToFrameMapping aggr
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 6. NmPdu — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:972`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.20
- Base: Pdu (stamped ✓)
- Tracker deviation: missing iSignalToIPduMapping aggr (ISignalToIPduMapping stamped ✓)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 7. NPdu — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1033`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.21
- Base: IPdu (stamped ✓)
- Tracker deviation: "-" (no own attrs beyond framework)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 8. PduTriggering — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1481`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.31
- Depends on: IPduPort (row 2), ISignalTriggering (row 3)
- Tracker deviations: ipduportrefs / isignaltriggeringrefs type (spec many vs py single)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 9. FrameTriggering — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1547`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.79
- Depends on: PduTriggering (row 8)
- Tracker deviation: pdutriggeringrefs type (spec many vs py single)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 10. AtpFeature — member
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py:157`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 5.2
- Role: ref target of AnyInstanceRef.contextElement
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 11. AtpInstanceRef — base
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py:13`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 5.3
- Role: base of AnyInstanceRef
- Tracker deviation (as input elsewhere): missing atpContextElement(ordered) ref
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 12. DocRevision — member
- Source: `src/armodel/models/M2/MSR/AsamHdo/AdminData.py:45`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 4.17
- Role: aggr member of AdminData.docRevision
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 13. AdminData — input
- Source: `src/armodel/models/M2/MSR/AsamHdo/AdminData.py:137`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 4.16
- Depends on: DocRevision (row 12)
- Tracker deviation: missing docRevision(ordered) aggr
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 14. SwSystemconstantValueSet — member
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py:275`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 7.25
- Role: ref target of PredefinedVariant.swSystemconstantValueSet
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 15. PredefinedVariant — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py:153`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 7.24
- Depends on: SwSystemconstantValueSet (row 14)
- Tracker deviations: includedvariantrefs / swsystemconstantvaluesetrefs type (spec many vs py single)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 16. AnyInstanceRef — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/AnyInstanceRef.py:11`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 9.57
- Depends on: AtpFeature (row 10), AtpInstanceRef (row 11)
- Tracker deviation: missing contextElement(ordered) ref
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 17. EcucParameterDef — base/member
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:856`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.14
- Role: base of EcucEnumerationParamDef/EcucAddInfoParamDef; aggr member of EcucParamConfContainerDef.parameter
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 18. EcucEnumerationLiteralDef — member
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1421`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.24
- Role: aggr member of EcucEnumerationParamDef.literal
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 19. EcucParamConfContainerDef — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1596`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.4
- Depends on: EcucParameterDef (row 17); bases EcucContainerDef stamped ✓
- Tracker deviations: missing parameter/reference/subContainer aggrs
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 20. EcucChoiceContainerDef — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1569`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.5
- Depends on: EcucParamConfContainerDef (row 19); base EcucContainerDef stamped ✓
- Tracker deviation: missing choice aggr
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 21. EcucEnumerationParamDef — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1471`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.23
- Depends on: EcucParameterDef (row 17), EcucEnumerationLiteralDef (row 18)
- Tracker deviation: missing literal aggr
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 22. EcucAddInfoParamDef — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1878`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.25
- Depends on: EcucParameterDef (row 17)
- Tracker deviation: "-" (no own attrs beyond framework)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 23. EcucValueConfigurationClass — input
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:616`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.10
- Base: EcucAbstractConfigurationClass (stamped ✓)
- Tracker deviation: "-" (no own attrs beyond framework)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

### [ ] 24. EcucModuleDef — input (last)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:2349`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.2, p.32
- Bases/members: EcucDefinitionElement, EcucContainerDef, EcucConfigurationVariantEnum all stamped ✓
- Tracker deviations: naming (containers, refinedModuleDefRef, supportedConfigVariants)
- Steps:
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write the model class unit test (Red)
  - [ ] Step 3 — Implement the model class (Green)
  - [ ] Step 4 — Wipe & rewrite docstrings from spec Note
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser (reader) & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec + rows)
  - [ ] Step 8 — Deviations ⇒ no stamp decision record
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write stamp

---

## Progress log

| Class | Commit | Date |
|---|---|---|
| CommConnectorPort | 8e6654e | 2026-08-23 |
