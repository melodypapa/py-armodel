# Sync todo: Group 3 — Constants, CompuMethod, DataDictionary, Documentation

Input: `Group 3 — Constants, CompuMethod, DataDictionary, Documentation` of `docs/examples/sync_class_groups.md` · Generated: 2026-08-30 · Queue order = row order
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished — Rule 0017.3)
> **Rule — already-verified short-circuit (added 2026-09-04):** before running the 9-step
> sync for a row, check whether the class already carries `# Spec verified: <RELEASE>` or
> `# XSD verified: <xsd-file>` in its own class body (verify the marker in the source — a
> row in this todo is not proof). If it does **and** a quick deviation check finds nothing
> new (base vs the spec `Base` closure, member types vs its table, verbatim docstrings,
> reader/writer coverage, checklist shape per Rules 0002/0012), **skip the 9 steps**: mark
> the row `- [x] <Class> — already verified (<marker>, <file>)` and move on. If the check
> finds a new deviation, do **not** mark it verified — keep the row queued, run the steps
> for the deviation only, and record it in Step 8 (Rule 0012.3: an existing marker is not
> proof).

## Queue (dependency-first)

> **Moved:** `StructuredReq`, `TraceableText` — wrong-heritage uuid-move blockers — moved into `Group1.md` ahead of the `Identifiable` row
> (dependency-first: the uuid move cannot run until they derive from `Identifiable`).

> **Restructured 2026-09-03** (dependency audit of all pending rows against R23-11 tables + stamp status — full class-body `Spec verified`/`XSD verified` scan):
> - **Added 12 missing dependency rows** (all verified unstamped/unverified, full class-body scan): `Paginateable` (9.75, parent mixin of the 5 GST doc classes),
>   `MultilanguageLongName` (4.6, GeneralAnnotation.label), `Graphic` (9.20, LGraphic.graphic), `LParagraph` (9.92, MultiLanguageParagraph.l1),
>   `TopicContent` (**Table E.81** — appendix letter-numbered table missed by numeric-regex tooling, same as Group2 D.17/D.4; MsrQueryP1.msrQueryResultP1),
>   `CompuConst` (5.71), `Compu` (5.62, CompuMethod.compuInternalToPhys/compuPhysToInternal), `CompuMethod` (5.61, SwAxisIndividual.compuMethod),
>   `DataConstr` (5.82, SwAxisIndividual.dataConstr), `SwRecordLayout` (5.97, SwRecordLayoutGroup.swRecordLayout),
>   `SwRecordLayoutGroupContent` (5.100, SwRecordLayoutGroup.swRecordLayoutGroupContentType), `CompuScale` (5.64, CompuScales.compuScale —
>   replaces the stale "(auto-queued, exists)" note on the CompuScales row; no dedicated row existed).
>   Already stamped (no row needed): ValueSpecification, AbstractRuleBasedValueSpecification, InternalConstrs, PhysConstrs, ValueList, SwValues, Unit,
>   SingleLanguageUnitNames, SwCalprmAxis, SwCalprmAxisTypeProps, SwAxisGeneric, SwVariableRefProxy, SwCalprmRefProxy, MultiLanguageOverviewParagraph,
>   SwBaseType, DocumentationBlock, Caption, MultiLanguageVerbatim, MsrQueryProps, Chapter, Topic1, LanguageSpecific.
> - **Corrections**: `DocumentViewSelectable` moved ahead of its five dependents (was after them); `CompositeValueSpecification` (5.110) moved ahead of
>   `RecordValueSpecification` (5.112)/`ArrayValueSpecification` (5.111) (parent-first); `DataConstr` ordered after `DataConstrRule` (aggr `dataConstrRule`);
>   `SwRecordLayoutGroup` (5.99) moved after `SwRecordLayoutV` (5.98) + `SwRecordLayout` + `SwRecordLayoutGroupContent` (all its member types);
>   Compu family ordered CompuContent → CompuConst → Compu → CompuMethod / CompuScale → CompuScales.
> - **New 16.4 entry**: `SwGenericAxisParamType` (NOT in src; ref target of SwRecordLayoutGroup/V.swGenericAxisParamType).
> - Cross-group deps: `ApplicationPrimitiveDataType` (SwAxisIndividual.inputVariableType / SwAxisGrouped.sharedAxisType) queued in Group2.

- [ ] `Paginateable` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.75 (mixin) · parent of `MultiLanguageParagraph`, `MlFigure`, `MsrQueryChapter`, `MsrQueryTopic1`, `MsrQueryP1` below · attrs BREAK/KEEP-WITH-PREVIOUS)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `MultilanguageLongName` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.6 · member type of `GeneralAnnotation.label` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Graphic` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.20 · member type of `LGraphic.graphic` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `LParagraph` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.92 · member type of `MultiLanguageParagraph.l1` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TopicContent` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · **AUTOSAR_FO_TPS_GenericStructureTemplate Table E.81 (appendix letter-numbered table missed by numeric-regex tooling, same as Group2 D.17/D.4 cases)** · member type of `MsrQueryP1.msrQueryResultP1` below · <<atpMixed>>)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DocumentViewSelectable` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.77 · **moved 2026-09-03 restructure ahead of its five dependents**: parent of `MultiLanguageParagraph`, `MlFigure`, `MsrQueryChapter`, `MsrQueryTopic1`, `MsrQueryP1` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `MultiLanguageParagraph` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.4 · after `Paginateable` (parent) + `LParagraph` (aggr `l1`))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Map` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.23 · after `Area` (aggr `area`) — Area NOT in src, pending 16.4 below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `LGraphic` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.25 · after `Graphic` (aggr `graphic`) + `Map` (aggr `map`) · parent `LanguageSpecific` stamped ✓ · *(existing member)*)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `MlFigure` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.24 · after `DocumentViewSelectable`+`Paginateable` (parents) + `LGraphic` (aggr `lGraphic`) · deps stamped: `figureCaption` Caption ✓ / `verbatim` MultiLanguageVerbatim ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `MsrQueryChapter` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.84 · after `DocumentViewSelectable`+`Paginateable` (parents) · deps: `msrQueryProps` MsrQueryProps stamped ✓ / `msrQueryResultChapter` NOT in src — pending 16.4 below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `MsrQueryTopic1` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.83 · after `DocumentViewSelectable`+`Paginateable` (parents) · deps: `msrQueryProps` stamped ✓ / `msrQueryResultTopic1` NOT in src — pending 16.4 below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `MsrQueryP1` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.82 · after `DocumentViewSelectable`+`Paginateable` (parents) + `TopicContent` (aggr `msrQueryResultP1`) · `msrQueryProps` stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuContent` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.63 (abstract) · parent of `CompuScales` below · member of `Compu.compuContent` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuConst` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.71 · member type of `Compu.compuDefaultValue` + `CompuScale.compuInverseValue` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuConstContent` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.72)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuScaleContents` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.66 · member type of `CompuScale.compuScaleContents` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuNominatorDenominator` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.75)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Compu` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.62 · member type of `CompuMethod.compuInternalToPhys`/`compuPhysToInternal` below · after `CompuContent` (aggr `compuContent`) + `CompuConst` (aggr `compuDefaultValue`))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuMethod` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.61 · ref target of `SwAxisIndividual.compuMethod` below · after `Compu` (aggr `compuInternalToPhys`/`compuPhysToInternal`) · `unit` Unit stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuScale` (dependency · **added 2026-09-03 restructure — replaces the stale '(auto-queued, exists)' note on the CompuScales row, no dedicated row existed** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.64 · member type of `CompuScales.compuScale` below · after `CompuConst` (aggr `compuInverseValue`) + `CompuScaleContents` (aggr `compuScaleContents`) · `desc` MultiLanguageOverviewParagraph stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuScales` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.65 · after `CompuScale` (aggr `compuScale`, row added 2026-09-03) + `CompuContent` (parent))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DataConstrRule` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.83 · deps stamped: `internalConstrs` InternalConstrs ✓ / `physConstrs` PhysConstrs ✓ · member type of `DataConstr.dataConstrRule` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DataConstr` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.82 · ref target of `SwAxisIndividual.dataConstr` below · after `DataConstrRule` (aggr `dataConstrRule`))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompositeValueSpecification` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.110 · **moved 2026-09-03 restructure ahead of its Record/Array subtypes** · parent `ValueSpecification` stamped ✓ · member type of `CompositeRuleBasedValueSpecification.argument` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ArrayValueSpecification` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.111 · after `CompositeValueSpecification` (parent, Table 5.110) · `element` ValueSpecification stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `RecordValueSpecification` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.112 · after `CompositeValueSpecification` (parent, Table 5.110) · `field` ValueSpecification stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompositeRuleBasedValueArgument` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.136 · member type of `CompositeRuleBasedValueSpecification.compoundPrimitiveArgument` below · base ARObject, no complex members)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompositeRuleBasedValueSpecification` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.135 · after `CompositeValueSpecification` (aggr `argument`) + `CompositeRuleBasedValueArgument` (aggr `compoundPrimitiveArgument`) · parent `AbstractRuleBasedValueSpecification` stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwValueCont` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.121 · deps stamped: `swArraysize` ValueList ✓ / `swValuesPhys` SwValues ✓ / `unit` Unit ✓ / `unitDisplayName` SingleLanguageUnitNames ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwCalprmAxisSet` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.46 · deps stamped: `swCalprmAxis` SwCalprmAxis ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwAxisIndividual` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.50 · after `CompuMethod` (ref `compuMethod`) + `DataConstr` (ref `dataConstr`) · `inputVariableType` ApplicationPrimitiveDataType queued in Group2 ✓ · deps stamped: `swAxisGeneric` SwAxisGeneric ✓ / `swVariableRef` SwVariableRefProxy ✓ / `unit` Unit ✓ / parent SwCalprmAxisTypeProps ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwAxisGrouped` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.55 · deps stamped: `swCalprmRef` SwCalprmRefProxy ✓ / `sharedAxisType` ApplicationPrimitiveDataType queued in Group2 ✓ / parent SwCalprmAxisTypeProps ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwRecordLayoutGroupContent` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.100 · member type of `SwRecordLayoutGroup.swRecordLayoutGroupContentType` below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwRecordLayoutV` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.98 · deps stamped: `baseType` SwBaseType ✓ / `desc` MultiLanguageOverviewParagraph ✓ · ref target `swGenericAxisParamType` SwGenericAxisParamType NOT in src — pending 16.4 below)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwRecordLayout` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.97 · ref target of `SwRecordLayoutGroup.swRecordLayout` below · NOTE cyclic aggregation: `swRecordLayoutGroup` → SwRecordLayoutGroup below (record layout family is mutually recursive; sync order resolves the ref direction)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwRecordLayoutGroup` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.99 · **moved 2026-09-03 restructure after `SwRecordLayoutV` (aggr `swRecordLayoutV`) + `SwRecordLayoutGroupContent` (aggr `swRecordLayoutGroupContentType`) + `SwRecordLayout` (ref `swRecordLayout`)** · self-recursive `swRecordLayoutGroup` · `swGenericAxisParamType` NOT in src — pending 16.4 below · `desc` stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `GeneralAnnotation` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.56 (multiple tables — resolve in per-class Phase 0) · after `MultilanguageLongName` (aggr `label`) · `annotationText` DocumentationBlock stamped ✓)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

## Pending 16.4 resolution (NEW — not in src)

- `Area` — not in `src` (NEW) · R23-11 markdown · Table 9.17 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist)
- `MsrQueryResultChapter` — not in `src` (NEW) · R23-11 markdown · Table 9.87 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist)
- `MsrQueryResultTopic1` — not in `src` (NEW) · R23-11 markdown · Table 9.88 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist)
- `SwGenericAxisParamType` — **added 2026-09-03 restructure** · not in `src` · R23-11 markdown · ref target of `SwRecordLayoutGroup.swGenericAxisParamType` + `SwRecordLayoutV.swGenericAxisParamType`; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist)

## Not queued

_(none)_
