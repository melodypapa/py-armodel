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

### [x] 3. ISignalTriggering — member (commit 9d18e04)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1684`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.16
- Role: ref target of PduTriggering.iSignalTriggering
- Tracker deviation resolved: stale `isignalportrefs` type row removed (model uses `List[RefType]` for the spec `*` multiplicity) — no deviation remains
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

### [x] 4. PduToFrameMapping — member (commit 368d742, stamped 6deafb2)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:39`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.29
- Role: aggr member of Frame.pduToFrameMapping
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 5. Frame — input (commit 44410c4, stamped 6deafb2)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:94`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.78
- Base: FibexElement (stamped ✓); depends on PduToFrameMapping (row 4)
- Tracker deviation: missing pduToFrameMapping aggr — resolved (aggr present, typed list)
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 6. NmPdu — input (commit 381903a, stamped 6deafb2)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:973`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.20
- Base: Pdu (stamped ✓)
- Tracker deviation: missing iSignalToIPduMapping aggr (ISignalToIPduMapping stamped ✓) — resolved; also added missing NM-DATA-INFORMATION / NM-VOTE-INFORMATION reader+writer coverage
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 7. NPdu — input (commit f3532e0, stamped 6deafb2)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1034`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.21
- Base: IPdu (stamped ✓)
- Tracker deviation: "-" (no own attrs beyond framework) — confirmed; reader/writer coverage via readNPdu/writeNPdu + dispatch tests
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 8. PduTriggering — input (commit df03c70, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1482`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.31
- Depends on: IPduPort (row 2), ISignalTriggering (row 3)
- Tracker deviations: ipduportrefs / isignaltriggeringrefs type (spec many vs py single) — resolved (both are typed `List[RefType]`, matching spec `*` multiplicity)
- Step 8 referenced-missing class: TriggerIPduSendCondition (aggr member, spec `*`) is not in the confirmed closure and has no model class — field kept as untyped List with add/get only; reader/writer coverage deferred until the class is queued
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 9. FrameTriggering — input (commit bfa9018, stamped 6deafb2)
- Source: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:1548`
- Spec: `AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.79
- Depends on: PduTriggering (row 8)
- Tracker deviation: pdutriggeringrefs type (spec many vs py single) — resolved (typed `List[RefType]`, matching spec `*` multiplicity); reader/writer already fully covered, round-trip test added
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 10. AtpFeature — member (commit 84fc55f, stamped 6deafb2)
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py:157`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 5.2
- Role: ref target of AnyInstanceRef.contextElement
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Reader/writer N/A ([—] no own XML element)
  - [x] Step 6 — Reader/writer N/A
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 11. AtpInstanceRef — base (commit 84fc55f, stamped 6deafb2)
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py:13`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 5.3
- Role: base of AnyInstanceRef
- Tracker deviation (as input elsewhere): missing atpContextElement(ordered) ref — resolved (atpContextElementRefs typed List present); reader/writer [—] (no own XML element; serialized by concrete subclasses)
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Reader/writer N/A ([—] no own XML element)
  - [x] Step 6 — Reader/writer N/A
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 12. DocRevision — member (commit a808be0, stamp deferred)
- Source: `src/armodel/models/M2/MSR/AsamHdo/AdminData.py:46`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 4.17
- Role: aggr member of AdminData.docRevision
- Note: added missing REVISION-LABEL-P-1 / REVISION-LABEL-P-2 reader+writer coverage
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 13. AdminData — input (commit a808be0, stamp deferred)
- Source: `src/armodel/models/M2/MSR/AsamHdo/AdminData.py:241`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 4.16
- Depends on: DocRevision (row 12)
- Tracker deviation: missing docRevision(ordered) aggr — resolved (DocRevisions typed List present); sdgs typed List[Sdg]
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser (reader) & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 14. SwSystemconstantValueSet — member (commit f206bfe, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py:275`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 7.25
- Role: ref target of PredefinedVariant.swSystemconstantValueSet
- Note: base corrected Identifiable → ARElement (spec most-derived base)
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (existing coverage verified)
  - [x] Step 6 — Update parser (reader) & writer (already covered; no change needed)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 15. PredefinedVariant — input (commit f206bfe, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py:153`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 7.24
- Depends on: SwSystemconstantValueSet (row 14)
- Tracker deviations: includedvariantrefs / swsystemconstantvaluesetrefs type (spec many vs py single) — resolved (typed `List[RefType]`); base corrected Identifiable → ARElement
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (existing coverage verified)
  - [x] Step 6 — Update parser (reader) & writer (already covered; no change needed)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 16. AnyInstanceRef — input (commit 9210018, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/AnyInstanceRef.py:11`
- Spec: `AUTOSAR_FO_TPS_GenericStructureTemplate.md` Table 9.57
- Depends on: AtpFeature (row 10), AtpInstanceRef (row 11)
- Tracker deviation: missing contextElement(ordered) ref — resolved (contextElementRefs typed List present); reader/writer coverage via getAnyInstanceRef/setAnyInstanceRef
- Steps:
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write the model class unit test (Red)
  - [x] Step 3 — Implement the model class (Green)
  - [x] Step 4 — Wipe & rewrite docstrings from spec Note
  - [x] Step 5 — Write reader/writer round-trip test (existing coverage verified)
  - [x] Step 6 — Update parser (reader) & writer (already covered; no change needed)
  - [x] Step 7 — Update checklist comment (# Spec + rows)
  - [x] Step 8 — Deviations ⇒ no stamp decision record
  - [x] Step 9 — Verify (9a); stamp deferred to batch confirmation

### [x] 17. EcucParameterDef — base/member (commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:856`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.14
- Role: base of EcucEnumerationParamDef/EcucAddInfoParamDef; aggr member of EcucParamConfContainerDef.parameter
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

### [x] 18. EcucEnumerationLiteralDef — member (commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1421`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.24
- Role: aggr member of EcucEnumerationParamDef.literal
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

### [x] 19. EcucParamConfContainerDef — input (commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1596`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.4
- Depends on: EcucParameterDef (row 17); bases EcucContainerDef stamped ✓
- Tracker deviations: missing parameter/reference/subContainer aggrs — resolved (all three typed Lists present); docstrings rewritten to verbatim spec Notes
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

### [x] 20. EcucChoiceContainerDef — input (commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1569`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.5
- Depends on: EcucParamConfContainerDef (row 19); base EcucContainerDef stamped ✓
- Tracker deviation: missing choice aggr — resolved (choices typed List present)
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

### [x] 21. EcucEnumerationParamDef — input (commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1471`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.23
- Depends on: EcucParameterDef (row 17), EcucEnumerationLiteralDef (row 18)
- Tracker deviation: missing literal aggr — resolved (literals typed List present)
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

### [x] 22. EcucAddInfoParamDef — input (commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:1878`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.25
- Depends on: EcucParameterDef (row 17)
- Tracker deviation: "-" (no own attrs beyond framework)
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

### [x] 23. EcucValueConfigurationClass — input (commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:616`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.10
- Base: EcucAbstractConfigurationClass (stamped ✓)
- Tracker deviation: "-" (no own attrs beyond framework)
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

### [x] 24. EcucModuleDef — input (last; commit 8e1edfd, stamp deferred)
- Source: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py:2349`
- Spec: `AUTOSAR_CP_TPS_ECUConfiguration.md` Table 2.2, p.32
- Bases/members: EcucDefinitionElement, EcucContainerDef, EcucConfigurationVariantEnum all stamped ✓
- Tracker deviations: naming (containers, refinedModuleDefRef, supportedConfigVariants) — resolved (all match spec Kind-suffix rules); docstrings rewritten to verbatim spec Notes
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

---

## Progress log

| Class | Commit | Date |
|---|---|---|
| CommConnectorPort | 8e6654e | 2026-08-23 |
