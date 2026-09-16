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
>
> **Dependency audit 2026-09-11 (LParagraph closure)** (re-run during the `LParagraph` Step 1 — the 2026-09-03
> restructure and the 2026-09-11 `Graphic` audit both missed this one):
> - `LParagraph` (9.92) has **no own attributes**; its content lives in `Base` = `ARObject , LanguageSpecific ,
>   MixedContentForParagraph`, and `MixedContentForParagraph` (Table 9.2, abstract, 13 attrs) is **NOT in src**.
> - **Added 21 dependency rows** before `LParagraph` (Rule 16.5 dependency-first), all verified NOT-in-src by AST scan:
>   `SingleLanguageLongName` (4.7), `SingleLanguageReferrable` (4.12), `Url` (XSD-only, complexType URL line 128502 —
>   16.4 decision **Derive-from-XSD**), `Br` (9.33), `Std` (9.37), `Xdoc` (9.40), `Xfile` (9.41), `XrefTarget` (9.43),
>   the 10 `Xref` enums (9.46–9.55), `Xref` (9.42), `MixedContentForParagraph` (9.2), `SlParagraph` (**Table E.71**,
>   appendix letter-numbered table — same class of miss as E.81 / Group2 D.17/D.4).
> - Already stamped, no row needed: `EmphasisText` (9.34), `IndexEntry` (9.36), `Superscript` (9.38), `Tt` (9.39),
>   `Traceable` (9.29), `Referrable` (D.54), `MixedContentForLongName` (4.9), `LanguageSpecific`.
> - Primitives not queued (leaf types, same treatment as `String`/`NameToken` in the `Graphic` row): `DateTime`,
>   `String`, `NameToken`.
> - Cycle note: `MixedContentForParagraph.ft` → `SlParagraph` → base `MixedContentForParagraph`; sync order
>   (MixedContentForParagraph first, then SlParagraph) resolves the ref direction.
>
> **Dependency audit 2026-09-11** (re-run for the `Graphic` row during its Step 1 — the 2026-09-03 restructure missed this one):
> - **Added 1 missing dependency row**: `GraphicNotationEnum` (Table 9.22, p.305) — NOT in src; member type of `Graphic.notation`.
>   Queued immediately **before** `Graphic` (Rule 16.5 dependency-first: a dependent must never precede its member type, or Step 3 would fabricate the type — Rule 0001.10).
> - `Graphic` dependency closure otherwise clear: Base `ARObject` + `EngineeringObject` both `# Spec verified: R23-11`, `GraphicFitEnum` `# Spec verified: R23-11`, `String`/`NameToken` are primitives.
> - `Graphic.notation` is the only consumer of `GraphicNotationEnum` (spec `Aggregated by` = `Graphic.notation`), so no other row shifts.

> **Dependency audit 2026-09-12** (run at the start of the `Url` row — the 2026-09-11 LParagraph closure audit queued `Url` but missed this one):
> - **Added 1 missing dependency row**: `MimeTypeString` (**Table 4.55**, `Primitive`, p.111) — NOT in src, and not previously queued anywhere.
>   Member type of `Url.mimeType` → queued immediately **before** `Url` (Rule 0016.5 dependency-first; a dependent must never precede its member type — Rule 0001.10).
> - Before this row, `Url.mimeType` had no implementable PDF type: `MimeTypeString` is a spec `Primitive` (implement as an `ARLiteral` subclass), unlike the class's value type `UriString`, which is stamped.
> - `Url.mimeType` is the only consumer of `MimeTypeString` (XSD `attributeGroup URL`, `aggregated by` `Url.mimeType`), so no other row shifts.

> **Dependency audit 2026-09-14 (`Table` closure)** (run at the start of the `Table` row — every earlier
> restructure/audit missed this cluster; Phase 0 had queued only `Table` itself):
> - `Table` (9.63) has **10 attributes** whose types form the whole **OASIS exchange-table cluster**
>   (`M2::MSR::Documentation::BlockElements::OasisExchangeTable`), **none of them in src** and **none
>   queued anywhere** (AST scan: no `class Table|Tgroup|Tbody|Row|Entry|Colspec|FrameEnum|AlignEnum|ValignEnum|TableSeparatorString`).
> - **Added 10 dependency rows** before `Table` (Rule 0016.5 dependency-first): `FrameEnum` (9.65),
>   `AlignEnum` (9.67), `ValignEnum` (9.69), `OrientEnum` (**XSD-only** — `AUTOSAR_00052.xsd:140997`;
>   no R23-11 § no R4.3.1 table), `TableSeparatorString` (**Table 9.72**, `Primitive`), `Colspec`
>   (**Table E.21** — appendix letter-numbered table, same class of miss as E.71/E.81), `Entry` (9.71),
>   `Row` (9.70), `Tbody` (9.68), `Tgroup` (9.66).
> - **Moved** `DocumentViewSelectable` (Table 9.77) ahead of `Table` + `Row` (it is a `Base` of both;
>   it was queued *after* `Table`, a dependency-order violation).
> - Already stamped, no row needed: `FloatEnum` (9.64), `PgwideEnum` (9.93); `Paginateable` ✓,
>   `Caption` ✓, `DocumentationBlock` ✓. `MlFigure.frame` (Table 9.24) is the other `FrameEnum` consumer.
> - `Table` is now blocked only on the 10 new rows above it.

> **Dependency audit 2026-09-16 (`Area` closure)** (run at the start of the `Area` row — the 2026-09-11
> missing-class audit queued `Area` but missed its two enum member types):
> - **Added 2 missing dependency rows**: `AreaEnumNohref` (Table 9.18, p.301) and `AreaEnumShape`
>   (Table 9.19, p.302) — both NOT in src (grep of src/ and tests/); member types of `Area.nohref` /
>   `Area.shape` → queued immediately **before** `Area` (Rule 0016.5 dependency-first; a dependent must
>   never precede its member type, or Step 3 would fabricate the type — Rule 0001.10).
> - Same class of miss as the 2026-09-11 `GraphicNotationEnum` audit (Graphic's member-type enum).
> - XSD cross-check: `AREA-ENUM-NOHREF--SIMPLE` (line 131467; literal NOHREF, index 0) and
>   `AREA-ENUM-SHAPE--SIMPLE` (line 131484; CIRCLE/DEFAULT/POLY/RECT, indices 0-3); `NOHREF`/`SHAPE`
>   are XML attributes on the AREA attributeGroup (lines 5873/5978).
> - `Area` itself (Table 9.17, p.301): 22 attrs (all 0..1 xml.attribute=true; String except the two
>   enums), Base `ARObject`, Package M2::MSR::Documentation::BlockElements::Figure → `Figure.py`.
> - Dependency closure of the enums otherwise clear (AREnum → ARObject base); primitives not queued.

- [x] `ChapterEnumBreak` (dependency · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.61 · enum member type of `Paginateable.chapterBreak`) — verified R23-11 (commit 20e6ee88)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as BREAK attribute on Paginateable (Spec verified)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: coverage lives in Paginateable's reader/writer, already Spec verified]
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations  [none: values match XSD, literals match spec, consumed by Spec-verified Paginateable]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker # Spec verified: R23-11 written; commit 20e6ee88]
- [x] `KeepWithPreviousEnum` (dependency · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.76 · enum member type of `Paginateable.keepWithPrevious`) — verified R23-11 (commit d447cf2a)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)  [+fix: XSD values KEEP/NO-KEEP, were keep/noKeep]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as KEEP-WITH-PREVIOUS attribute on Paginateable (Spec verified)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: coverage lives in Paginateable's reader/writer, already Spec verified]
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations  [none: pre-existing wrong values keep/noKeep corrected to XSD KEEP/NO-KEEP; class now matches spec]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker # Spec verified: R23-11 written; commit d447cf2a]
- [x] `Paginateable` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.75 (mixin) · parent of `MultiLanguageParagraph`, `MlFigure`, `MsrQueryChapter`, `MsrQueryTopic1`, `MsrQueryP1` below · attrs BREAK/KEEP-WITH-PREVIOUS) — verified R23-11 (model+docstrings/checklist/parser/writer 20e6ee88, LIST aggregator coverage a06638fb)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations  [none outstanding: spec attr `break` is a Python keyword → field `chapterBreak`, accessors keep the spec name `getBreak`/`setBreak` (precedented like DefItem.def→def_doc)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker `# Spec verified: R23-11` had been committed early in 20e6ee88; full 9b checklist re-run and confirmed in this pass; ARList aggregator coverage fixed + committed a06638fb]
- [x] `MultilanguageLongName` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.6 · member type of `GeneralAnnotation.label` below) — verified R23-11 (commit 87855dea)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [reader helper getMultilanguageLongName+readLLongName already existed & covered; added value-asserting parser test; writer round-trip added]
  - [x] Step 6 — Update parser & writer (Green)  [writer helper setMultiLongName+setLLongName already existed & covered; writer round-trip test added + namespace-wrap fix]
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations  [none: class already conformed to Table 4.6; only docstrings/checklist/tests were missing — now added]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker # Spec verified: R23-11 written; commit 87855dea]
- [x] `GraphicFitEnum` (dependency · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.21 · enum member type of `Graphic.editfit`/`fit`) — verified R23-11 (commit 5b543a21)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)  [+fix: enum had NO literals at all — `__init__(self, enum_values)` ignored its arg and registered an empty tuple; now no-arg `__init__` registering all 13 spec literals]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as EDITFIT/FIT/HTML-FIT attribute value on Graphic; graphic's editfit/fit not yet serialized by parser/writer (only FILENAME) — belongs to the Graphic row]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: see Step 5]
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations  [none: all 13 literal values + indices 0-12 match XSD GRAPHIC-FIT-ENUM--SIMPLE; class now matches spec]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker # Spec verified: R23-11 written; commit 5b543a21]
- [x] `GraphicNotationEnum` (dependency · **added 2026-09-11 Graphic dependency audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.22, p.305 · enum member type of `Graphic.notation` below · **was NOT in src — created** · 8 XSD literals BMP/EPS/GIF/JPG/PDF/PNG/SVG/TIFF, indices 0-7 · queued dependency-first per Rule 16.5) — verified R23-11 (commit f25e765d)
  - [x] Step 1 — Sync members & description from spec  [8 literals bmp/eps/gif/jpg/pdf/png/svg/tiff, indices 0-7; XSD values uppercase BMP…TIFF; Note + literal descriptions from Table 9.22; Package M2::MSR::Documentation::BlockElements::Figure; p.305 confirmed via pdf_page.py]
  - [x] Step 2 — Write model class unit test (Red)  [TestGraphicNotationEnum in test_Figure.py: init, 8 literals, set/get value, validateEnumValue; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [new GraphicNotationEnum(AREnum) in Figure.py after GraphicFitEnum, no-arg __init__ registering all 8 XSD values]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring = spec Note verbatim (diffed); 7/8 literal comments verbatim from markdown Tags rows; `svg` index 6 + description from XSD GRAPHIC-NOTATION-ENUM--SIMPLE (markdown split render dropped its Tags)]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as the NOTATION attribute value on Graphic; Graphic's reader/writer currently cover FILENAME only, so NOTATION coverage belongs to the Graphic row (queued next)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: see Step 5 — no own XML element]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.22, p.305; (no methods) row for __init__ with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: all 8 literal values + indices 0-7 match XSD GRAPHIC-NOTATION-ENUM--SIMPLE; class now matches spec]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker # Spec verified: R23-11 written; commit f25e765d]
- [x] `Graphic` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.20 · member type of `LGraphic.graphic` below · **15 spec attrs (all 0..1, all xml.attribute=true); src had only 6 — all 9 missing ones added** · Base `ARObject`+`EngineeringObject` both stamped ✓ · `GraphicFitEnum` ✓ · `GraphicNotationEnum` ✓) — verified R23-11 (commit 06b46f32)
  - [x] Step 1 — Sync members & description from spec  [audit: 15 attrs vs 6 in src; XSD GRAPHIC attributeGroup confirms EDITFIT/EDIT-HEIGHT/EDITSCALE/EDIT-WIDTH/FILENAME/FIT/GENERATOR/HEIGHT/HTML-FIT/HTML-HEIGHT/HTML-SCALE/HTML-WIDTH/NOTATION/SCALE/WIDTH]
  - [x] Step 2 — Write model class unit test (Red)  [TestGraphic: 15-attr init defaults + all 15 get/set pairs with None no-op; 10 failed = Red]
  - [x] Step 3 — Implement model class (Green)  [9 new attrs added (generator NameToken, height/htmlHeight/htmlScale/htmlWidth/scale/width String, htmlFit GraphicFitEnum, notation GraphicNotationEnum); all 15 members now PEP 526 annotated (was `# type:` comments)]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [all 15 inline comments + getter + setter docstrings diffed verbatim against Table 9.20; class docstring = spec Note verbatim; old `# type:` comments replaced by PEP 526]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [test_getGraphic_all_attributes (15 attrs) + TestSetGraphic::test_with_all_attributes; 7 failures = Red; 4 pre-existing bare-str call sites updated to typed primitives]
  - [x] Step 6 — Update parser & writer (Green)  [getGraphic/setGraphic now cover all 15 attributes with typed primitives (String/NameToken/GraphicFitEnum/GraphicNotationEnum) and matched set/get pairs]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.20, p.303; 31 rows (init + 15 getter/setter pairs) with 6 columns + release R23-11]
  - [x] Step 8 — Deviations  [none: all 15 spec attrs modeled with PDF types (10 String, 1 NameToken, 3 GraphicFitEnum, 1 GraphicNotationEnum), names verbatim, all with reader+writer coverage]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker # Spec verified: R23-11 written; commit 06b46f32]
- [x] `SingleLanguageLongName` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.7 · **NOT in src** · Package M2::MSR::Documentation::TextModel::SingleLanguageData · Base `ARObject , MixedContentForLongName` (MixedContentForLongName stamped ✓) · needed by `SingleLanguageReferrable.longName1` and `Xref.label1`) — verified R23-11 (commit 8aaa2657)
  - [x] Step 1 — Sync members & description from spec  [Class <<atpMixedString>> SingleLanguageLongName; Package M2::MSR::Documentation::TextModel::SingleLanguageData; Note = "SingleLanguageLongName" (verbatim, matches R4.3.1 Table 4.10 + XSD doc); Base ARObject , MixedContentForLongName; no own Attribute rows; p.62 via pdf_page.py; XSD SINGLE-LANGUAGE-LONG-NAME mixed="true" → mixed-string `value` field + inherited e/ie/sub/sup/tt; aggregated by SingleLanguageReferrable.longName1 (LONG-NAME-1) + Xref.label1 (LABEL-1)]
  - [x] Step 2 — Write model class unit test (Red)  [test_SingleLanguageLongName.py: initialization (value None + inherited e/ie/sub/sup/tt None) + value get/set with None no-op; ModuleNotFoundError = Red]
  - [x] Step 3 — Implement model class (Green)  [new SingleLanguageLongName(MixedContentForLongName) in SingleLanguageData.py; mixed-string `value: Optional[String]` field (XSD mixed="true"); export line added to models/__init__.py; 2 passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [brand-new file — class docstring = spec Note "SingleLanguageLongName" verbatim (confirmed against PDF p.62 extract); value comment/getter/setter use the atpMixedString "text content" convention (same as EmphasisText/IndexEntry)]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser: test_getSingleLanguageLongName_parses_value_and_inline / _parses_sup_sub / _missing_returns_None; writer: test_set_single_language_long_name + _roundtrip + _inline_roundtrip + _optional_attributes_absent; AttributeError = Red]
  - [x] Step 6 — Update parser & writer (Green)  [parser readSingleLanguageLongName + getSingleLanguageLongName, writer setSingleLanguageLongName; **Rule 0001.7/0013.1 fix**: the `<<atpMixedString>>` group (SUP/SUB attrs + E/IE/TT children of Table 4.9) is now owned by the abstract XML-bearing base `MixedContentForLongName` as reusable `readMixedContentForLongName`/`writeMixedContentForLongName(element, obj)` helpers, and BOTH concrete subclasses call them — `readLLongName`/`setLLongName` (LLongName) and `readSingleLanguageLongName`/`setSingleLanguageLongName` (SingleLanguageLongName no longer inline the group); no double `readARObject` (each child calls only its direct base helper); imports added to parser + writer; 4077 passed + 3 integration]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 4.7, p.62; 3 rows (init + get/set value) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: Table 4.7 has **no own Attribute rows** (`-`) — all content inherited from stamped `MixedContentForLongName` (Table 4.9: e/ie/sub/sup/tt); the `<<atpMixedString>>` text content is modeled as `value: Optional[String]` per the established family convention (EmphasisText Table 9.34 / IndexEntry Table 9.36) — not a fabricated attribute; no flattened/relocated members; read+write coverage for every member via `readSingleLanguageLongName`/`setSingleLanguageLongName`; no missing referenced classes (Superscript/EmphasisText/IndexEntry/Tt all stamped); consumers `SingleLanguageReferrable` + `Xref` not yet in src (queued later) — class owns & directly tests its reusable helper]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [marker `# Spec verified: R23-11` written; commit 8aaa2657]
- [x] `SingleLanguageReferrable` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.12 (abstract) · **NOT in src** · Package M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable · Base `ARObject , Referrable` (Referrable stamped ✓) · attr `longName1` SingleLanguageLongName 0..1 aggr · base of `Std`, `Xdoc`, `Xfile`, `XrefTarget`) — verified R23-11 (commit a5910c1b)
  - [x] Step 1 — Sync members & description from spec  [Class `SingleLanguageReferrable (abstract)`; Package M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable → Identifiable.py; Base `ARObject , Referrable` → most-derived `Referrable`; one attr `longName1` SingleLanguageLongName 0..1 aggr (child Base ARObject+MixedContentForLongName → non-Referrable → set/get, no create); Subclasses Std/Xdoc/Xfile/XrefTarget; p.64 via pdf_page.py; Note verified against PDF p.64 (markdown joins the XSD paragraph breaks); element LONG-NAME-1 per XSD SINGLE-LANGUAGE-REFERRABLE group; abstract → owns reusable read/writeSingleLanguageReferrable helpers (Rule 0001.7)]
  - [ ] Step 2 — Write model class unit test (Red)
  - [x] Step 2 — Write model class unit test (Red)  [TestSingleLanguageReferrable in test_Identifiable.py: abstract-guard TypeError, defaults (longName1 None + inherited shortName/parent), get/set longName1 chaining, None no-op — via a local concrete subclass; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [SingleLanguageReferrable(Referrable, ABC) added to Identifiable.py after MultilanguageReferrable; abstract guard; `longName1: Optional[SingleLanguageLongName]`; TYPE_CHECKING import of SingleLanguageLongName; exported via Identifiable wildcard; 4 passed; `armodel.SingleLanguageReferrable` resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [new code — class docstring = spec Note verbatim (markdown; PDF p.64 confirms the paragraph-joined text, includes the spec's own "Therefore they aggregate But they are not…" join); longName1 comment/getter/setter = attr Note verbatim incl. the spec typo "compatibiilty"; setter appends the None-no-op line]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser: test_readSingleLanguageReferrable_sets_longName1 / _parses_long_name1_inline / _without_long_name1; writer: test_write_single_language_referrable (SHORT-NAME + LONG-NAME-1 value round-trip) + _without_long_name1; concrete subclass defined locally (none exists in src); AttributeError = Red]
  - [x] Step 6 — Update parser & writer (Green)  [parser `readSingleLanguageReferrable` = readReferrable + setLongName1(getSingleLanguageLongName(element, "LONG-NAME-1")) — mirrors readMultilanguageReferrable leveling (Rule 0013.1); writer `writeSingleLanguageReferrable` = writeReferrable + setSingleLanguageLongName; imports added to both; 3+2 passed]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 4.12, p.64; 3 rows (init + get/set longName1) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: single spec attr `longName1` (0..1 aggr) modeled with the PDF type `Optional[SingleLanguageLongName]` (that class exists in src and is `# Spec verified: R23-11` from the previous session) and accessors `getLongName1`/`setLongName1` — name verbatim from the Attribute column (no Kind suffix; not a ref/iref/tref); child Base = ARObject+MixedContentForLongName is **not** Referrable → set/get, no `createXxx`/`addXxx` (Rule 0001.6); abstract handled with ABC + TypeError guard like MultilanguageReferrable; `readSingleLanguageReferrable`/`writeSingleLanguageReferrable` own the LONG-NAME-1 group (Rule 0001.7 abstract XML-bearing base) and reuse the previous session's `getSingleLanguageLongName`/`setSingleLanguageLongName`; no flattened/relocated members; no missing referenced classes (Referrable + SingleLanguageLongName both stamped)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 4437 tests + 3 integration round-trips pass; flake8/ruff/black-check clean (ruff I001 + black reflow applied to the widened import); checklist == methods; 9b: 14-item pre-stamp checklist user-confirmed; marker `# Spec verified: R23-11` written; commit a5910c1b]
- [x] `MimeTypeString` (dependency · **added 2026-09-12 Url closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · **Table 4.55** (`Primitive`, p.111) · **NOT in src** · **NOT queued anywhere before this audit** — missed by all earlier closure passes · Package `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes` → `PrimitiveTypes.py` (same file as `UriString`) · missing **primitive** → implement as an `ARLiteral` subclass (Rule 0001.10) · member type of `Url.mimeType` below → queued immediately before `Url` (dependency-first, Rule 0016.5)) — verified R23-11 (commit 01cc23df)
  - [x] Step 1 — Sync members & description from spec  [`Primitive MimeTypeString`; Package M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes → PrimitiveTypes.py; Note = "This primitive denotes the an Internet media type, originally called a MIME type after MIME and sometimes a Content-type after the name of a header in several protocols whose value is such a type, is a two-part identifier for file formats on the Internet." (verbatim, incl. the spec's "denotes the an" grammar slip) + Tags xml.xsd.customType=MIME-TYPE-STRING / xml.xsd.type=string; p.111 via pdf_page.py, confirmed against PDF p.111; no Attribute rows (Primitive table) → ARLiteral subclass, no fields beyond ARType's timestamp]
  - [ ] Step 2 — Write model class unit test (Red)
  - [x] Step 2 — Write model class unit test (Red)  [TestMimeTypeString in test_PrimitiveTypes.py: initialization (ARLiteral instance, _value None) + setValue round-trip/chaining/str(); ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [MimeTypeString(ARLiteral) added to PrimitiveTypes.py immediately after McdIdentifier (Table 4.54 → 4.55 spec order); exported via the module wildcard; 2 passed; `armodel.MimeTypeString` resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring = spec Note verbatim + the Tags block as an indented bullet list, per the stamped AnyServiceInstanceId precedent; diffed byte-equal against the markdown cell; PDF p.111 confirms the "denotes the an Internet media type" grammar slip is the spec's own]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone ARLiteral primitive with no own XML element — MIME-TYPE-STRING is never referenced as an element type in the XSD; it is used only as the `MIME-TYPE` attribute on the URL attributeGroup, so the value form is covered by the consuming `Url` row (queued next)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: see Step 5 — no element, no typed leaf helper needed (the URL attribute is read/written by the Url row via readElementOptionalAttrib / element.attrib)]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 4.55, p.111; 1 row (__init__) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: spec table is a `Primitive` (not `Class`/`Enumeration`) → modeled as an `ARLiteral` subclass with no own fields (Rule 0001.10 primitive path); no attributes to type; reader/writer N/A (attribute-only usage — the URL attribute belongs to the `Url` row); no missing referenced classes (Base `ARLiteral`/`ARType` in src); no fabricated/naming/type rows. Note the dependency itself was the deviation being fixed: `MimeTypeString` had been missing from src and from every queue since the 2026-09-11 audits — now queued before `Url` (Rule 0016.5)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8800 models/parser/writer tests + 3 integration round-trips pass; flake8/ruff/black-check clean; checklist == methods; 9b: 12-item pre-stamp checklist user-confirmed; marker `# Spec verified: R23-11` written; commit 01cc23df]
- [x] `Url` (dependency · **added 2026-09-11 LParagraph closure audit** · **XSD-only** (no markdown/PDF table) · AUTOSAR_00052.xsd `complexType name="URL"` line 128502 (+ `attributeGroup URL` line 128494; attr `MIME-TYPE`) · **NOT in src** · member type of `Std.url` / `Xdoc.url` / `Xfile.url` (0..1 aggr) · 16.4 decision: **Derive-from-XSD** → carries `# XSD verified: AUTOSAR_00052.xsd` · deps: `mimeType` MimeTypeString queued immediately above (added 2026-09-12) / value type `UriString` stamped ✓) — verified XSD (commit 4b96ab8d)
  - [x] Step 1 — Sync members & description from spec  [XSD-only (no R23-11/R4.3.1 table — verified both corpora); Package `M2::MSR::Documentation::BlockElements` (XSD comment line 128493) → non-leaf `BlockElements/__init__.py` (Caption precedent, same package); Base `ARObject` (XSD `attributeGroup AR-OBJECT` ref line 128510 + stereotype atpObject); 2 own members alphabetical (markdown-render convention, cf. Sd/TagWithOptionalValue): `mimeType` MimeTypeString 0..1 attr (MIME-TYPE, documentation "this denotes the mime type of the resource located by the url."), `value` UriString 0..1 text (simpleContent base `URI-STRING--SIMPLE`); class doc "This meta-class specifies an Uniform Resource Locator (URL)."; element `<URL>` (XSD usages lines 113342 Std.url / 131021 Xdoc.url / 131058 Xfile.url); not VP-capable (simpleContent, no VARIATION-POINT)]
   - [x] Step 2 — Write model class unit test (Red)  [test_Url.py: defaults and typed get/set with None no-op; ImportError = Red]
   - [x] Step 3 — Implement model class (Green)  [Url(ARObject) with mimeType: Optional[MimeTypeString] and value: Optional[UriString], typed accessors; 3 passed]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and XSD member documentation copied; PEP 526 members]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser/writer tests for text, MIME-TYPE, S/T and absent URL; AttributeError = Red]
   - [x] Step 6 — Update parser & writer (Green)  [getUrl/setUrl read/write AR-OBJECT S/T, MIME-TYPE, and URI simple content; 7 focused tests passed]
   - [x] Step 7 — Update checklist comment  [XSD-only checklist with 5 method rows and release R23-11]
   - [x] Step 8 — Deviations  [none: XSD complexType and attributeGroup fully modeled; no PDF/markdown table]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, lint, and black-check pass; full unit suite 8865 passed; integration blocked by existing GBK decoding error; 9b: user-confirmed XSD compliance; marker written]
- [x] `Br` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.33 · **NOT in src** · Package M2::MSR::Documentation::TextModel::InlineTextElements · Base `ARObject` · no own attributes · member type of `MixedContentForParagraph.br`) — verified R23-11 (Rule 0013.2 correction; commit pending)
  - [x] Step 1 — Sync members & description from spec  [Class Br; Package M2::MSR::Documentation::TextModel::InlineTextElements; Note copied verbatim; Base ARObject; no own Attribute rows; p.316 via pdf_page.py; aggregated by MixedContentForOverviewParagraph.br, MixedContentForParagraph.br, MixedContentForVerbatim.br]
  - [x] Step 2 — Write model class unit test (Red)  [test_Br.py: initialization and inherited ARObject defaults; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [Br(ARObject) added to InlineTextElements.py; 1 passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note copied verbatim; no own members or accessors]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser/writer tests for inherited S/T attributes and omitted None wrapper; AttributeError = Red]
  - [x] Step 6 — Update parser & writer (Green)  [Rule 0013.2 correction: concrete XML helper names are getBr/setBr; they cover the BR XML element and inherited ARObject S/T attributes; 4 focused tests passed]
  - [x] Step 7 — Update checklist comment  [Table 9.33 p.316; one __init__ row with six columns and R23-11; concrete helper coverage is recorded on the XML layer]
  - [x] Step 8 — Deviations  [initial readBr/writeBr names corrected to concrete-element getBr/setBr per Rule 0013.2; no remaining deviation]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8869 unit tests, lint, Black check, and focused Rule 0013.2 checks pass; 9b: user-confirmed matched concrete helper names getBr/setBr; marker already present]
- [x] `Std` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.37 · **created** · Package M2::MSR::Documentation::TextModel::InlineTextElements · Base `ARObject , Referrable , SingleLanguageReferrable` · attrs date(DateTime)/position(String)/state(String)/subtitle(String)/url(Url) all 0..1 · member type of `MixedContentForParagraph.std`) — verified R23-11 (commit c53a2408)
   - [x] Step 1 — Sync members & description from spec  [Table 9.37, p.318; base and five attributes confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [Std extends SingleLanguageReferrable; typed five members and accessors]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class and member docs copied from Table 9.37]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [missing getStd/setStd before implementation]
   - [x] Step 6 — Update parser & writer (Green)  [getStd/setStd cover inherited referrable data, five attributes, and nested URL]
   - [x] Step 7 — Update checklist comment  [11 method rows with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, full unit suite, lint, Black check, and diff check pass; 9b: user-confirmed matched base, members, docstrings, reader/writer coverage, and no deviations; marker written]
- [x] `Xdoc` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.40 · **created** · Package M2::MSR::Documentation::TextModel::InlineTextElements · Base `ARObject , Referrable , SingleLanguageReferrable` · attrs date/number/position/publisher/state/url all 0..1 · member type of `MixedContentForParagraph.xdoc`) — verified R23-11 (commit 294c8aae)
   - [x] Step 1 — Sync members & description from spec  [Table 9.40, p.319; base and six attributes confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [Xdoc extends SingleLanguageReferrable; typed six members and accessors]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class and member docs copied from Table 9.40]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [missing getXdoc/setXdoc before implementation]
   - [x] Step 6 — Update parser & writer (Green)  [getXdoc/setXdoc cover inherited referrable data, six attributes, and nested URL]
   - [x] Step 7 — Update checklist comment  [13 method rows with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8887 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched base, members, docstrings, reader/writer coverage, and no deviations; marker written]
- [x] `Xfile` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.41 · **created** · Package M2::MSR::Documentation::TextModel::InlineTextElements · Base `ARObject , Referrable , SingleLanguageReferrable` · attrs tool/toolVersion/url all 0..1 · member type of `MixedContentForParagraph.xfile`) — verified R23-11 (commit 7038ce55)
   - [x] Step 1 — Sync members & description from spec  [Table 9.41, p.320; markdown rows and XSD sequence confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [Xfile extends SingleLanguageReferrable; typed tool/toolVersion/url members and accessors]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class and member docs copied from Table 9.41]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [missing getXfile/setXfile before implementation]
   - [x] Step 6 — Update parser & writer (Green)  [getXfile/setXfile cover inherited referrable data, URL, TOOL, and TOOL-VERSION in XSD order]
   - [x] Step 7 — Update checklist comment  [7 method rows with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8893 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched base, members, XML order, docstrings, reader/writer coverage, and no deviations; marker written]
- [x] `XrefTarget` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.43 · **created** · Package M2::MSR::Documentation::TextModel::InlineTextElements · Base `ARObject , Referrable , SingleLanguageReferrable` · no own attributes · member type of `MixedContentForParagraph.xrefTarget`) — verified R23-11 (commit 8c9df663)
   - [x] Step 1 — Sync members & description from spec  [Table 9.43, p.321; no own attributes; inherited SingleLanguageReferrable XML groups confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [XrefTarget extends SingleLanguageReferrable with no own members]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring copied from Table 9.43]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [missing getXrefTarget/setXrefTarget before implementation]
   - [x] Step 6 — Update parser & writer (Green)  [concrete XREF-TARGET helpers cover inherited short-name and long-name data]
   - [x] Step 7 — Update checklist comment  [one __init__ row with six columns and R23-11 release; concrete helper coverage recorded on XML layer]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8898 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched base, no own attributes, inherited XML coverage, docstrings, and no deviations; marker written]
- [x] `ResolutionPolicyEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.46 · **created** · Package M2::MSR::Documentation::TextModel::InlineAttributeEnums · AREnum; literals noSloppy/sloppy; member type of `Xref.resolutionPolicy`) — verified R23-11 (commit f0a74608)
   - [x] Step 1 — Sync members & description from spec  [Table 9.46, p.322; two literals NO-SLOPPY/SLOPPY confirmed against XSD]
   - [x] Step 2 — Write model class unit test (Red)  [ModuleNotFoundError before implementation]
   - [x] Step 3 — Implement model class (Green)  [new ResolutionPolicyEnum(AREnum) with two XSD values]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class note and literal descriptions copied from Table 9.46/XSD]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns RESOLUTION-POLICY coverage]
   - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8899 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker written]
- [x] `ShowContentEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.47 · **created** · Package M2::MSR::Documentation::TextModel::InlineAttributeEnums · AREnum; literals noShowContent/showContent; member type of `Xref.showContent`) — verified R23-11 (commit e89003bb)
   - [x] Step 1 — Sync members & description from spec  [Table 9.47, p.323; two literals NO-SHOW-CONTENT/SHOW-CONTENT confirmed against XSD]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [ShowContentEnum(AREnum) with two XSD values]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class note and literal descriptions copied from Table 9.47/XSD]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-CONTENT coverage]
   - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8900 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker written]
- [x] `ShowResourceAliasNameEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.48 · **created** · Package M2::MSR::Documentation::TextModel::InlineAttributeEnums · AREnum; literals noShowAliasName/showAliasName; member type of `Xref.showResourceAliasName`) — verified R23-11 (commit 3a68e972)
   - [x] Step 1 — Sync members & description from spec  [Table 9.48, p.323; two literals NO-SHOW-ALIAS-NAME/SHOW-ALIAS-NAME confirmed against XSD]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [ShowResourceAliasNameEnum(AREnum) with two XSD values]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class note and literal descriptions copied from Table 9.48/XSD]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-RESOURCE-ALIAS-NAME coverage]
   - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8901 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker written]
  - [x] `ShowResourceCategoryEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.49 · **created** · Package M2::MSR::Documentation::TextModel::InlineAttributeEnums · AREnum; literals noShowCategory/showCategory; member type of `Xref.showResourceCategory`) — verified R23-11 (commit d7cd8c58)
   - [x] Step 1 — Sync members & description from spec  [Table 9.49, p.323; two literals NO-SHOW-CATEGORY/SHOW-CATEGORY confirmed against XSD]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [ShowResourceCategoryEnum(AREnum) with two XSD values]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class note and literal descriptions copied from Table 9.49/XSD]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-RESOURCE-CATEGORY coverage]
   - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8902 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker written]
 - [x] `ShowResourceLongNameEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.50 · **created** · Package M2::MSR::Documentation::TextModel::InlineAttributeEnums · AREnum; literals noShowLongName/showLongName; member type of `Xref.showResourceLongName`) — verified R23-11 (commit 835b8aa1)
   - [x] Step 1 — Sync members & description from spec  [Table 9.50, p.323; two literals NO-SHOW-LONG-NAME/SHOW-LONG-NAME confirmed against XSD]
   - [x] Step 2 — Write model class unit test (Red)  [ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [ShowResourceLongNameEnum(AREnum) with two XSD values]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class note and literal descriptions copied from Table 9.50/XSD]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-RESOURCE-LONG-NAME coverage]
   - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none outstanding]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8903 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker written]
- [x] `ShowResourceNumberEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · Table 9.51 · **created** · AREnum · member type of `Xref.showResourceNumber`) — verified R23-11 (commit 6f562513)
  - [x] Step 1 — Sync members & description from spec  [Table 9.51, p.324; note and two literal descriptions confirmed against R23-11 markdown/XSD]
  - [x] Step 2 — Write model class unit test (Red)  [extended test_InlineAttributeEnums.py with initialization, literal, validation, set/get assertions; ImportError before implementation]
  - [x] Step 3 — Implement model class (Green)  [ShowResourceNumberEnum(AREnum) added with NO-SHOW-NUMBER/SHOW-NUMBER]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and literal descriptions copied from Table 9.51]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-RESOURCE-NUMBER coverage]
  - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: literals and indices match XSD SHOW-RESOURCE-NUMBER-ENUM--SIMPLE]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, lint, Black check, and diff check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker written]
- [x] `ShowResourcePageEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · Table 9.52 · **created** · AREnum · member type of `Xref.showResourcePage`) — verified R23-11 (commit 54f4f3e5)
  - [x] Step 1 — Sync members & description from spec  [Table 9.52, p.324; Note and two literal descriptions copied verbatim from R23-11 markdown; XSD values NO-SHOW-PAGE/SHOW-PAGE with indices 0/1 confirmed]
  - [x] Step 2 — Write model class unit test (Red)  [extended test_InlineAttributeEnums.py with initialization, literal, validation, set/get assertions; import failure before implementation]
  - [x] Step 3 — Implement model class (Green)  [ShowResourcePageEnum(AREnum) added with NO-SHOW-PAGE/SHOW-PAGE]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and literal descriptions copied verbatim from Table 9.52]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-RESOURCE-PAGE coverage]
  - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: literals and indices match XSD SHOW-RESOURCE-PAGE-ENUM--SIMPLE]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, lint, and Black check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker `# Spec verified: R23-11` written]
- [x] `ShowResourceShortNameEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · Table 9.53 · **created** · AREnum · member type of `Xref.showResourceShortName`) — verified R23-11 (commit e2e2c300)
  - [x] Step 1 — Sync members & description from spec  [Table 9.53, p.324; Note and two literal descriptions copied verbatim from R23-11 markdown; XSD values NO-SHOW-SHORT-NAME/SHOW-SHORT-NAME with indices 0/1 confirmed]
  - [x] Step 2 — Write model class unit test (Red)  [extended test_InlineAttributeEnums.py with initialization, literal, validation, set/get assertions; import failure before implementation]
  - [x] Step 3 — Implement model class (Green)  [ShowResourceShortNameEnum(AREnum) added with NO-SHOW-SHORT-NAME/SHOW-SHORT-NAME]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and literal descriptions copied verbatim from Table 9.53]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-RESOURCE-SHORT-NAME coverage]
  - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: literals and indices match XSD SHOW-RESOURCE-SHORT-NAME-ENUM--SIMPLE]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, lint, and Black check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker `# Spec verified: R23-11` written]
 - [x] `ShowResourceTypeEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · Table 9.54 · **created** · AREnum · member type of `Xref.showResourceType`) — verified R23-11 (commit 447709b7)
   - [x] Step 1 — Sync members & description from spec  [Table 9.54, p.324; Note and two literal descriptions copied verbatim from R23-11 markdown; XSD values NO-SHOW-TYPE/SHOW-TYPE with indices 0/1 confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [extended test_InlineAttributeEnums.py with initialization, literal, validation, set/get assertions; import failure before implementation]
   - [x] Step 3 — Implement model class (Green)  [ShowResourceTypeEnum(AREnum) added with NO-SHOW-TYPE/SHOW-TYPE]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and literal descriptions copied verbatim from Table 9.54]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-RESOURCE-TYPE coverage]
   - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release; marker deferred to 9b]
   - [x] Step 8 — Deviations  [none: literals and indices match XSD SHOW-RESOURCE-TYPE-ENUM--SIMPLE]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, lint, and Black check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker `# Spec verified: R23-11` written]
- [x] `ShowSeeEnum` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · Table 9.55 · **created** · AREnum · member type of `Xref.showSee`) — verified R23-11 (commit 5d48c2a6)
   - [x] Step 1 — Sync members & description from spec  [Table 9.55, p.325; Note and two literal descriptions copied verbatim from R23-11 markdown; XSD values NO-SHOW-SEE/SHOW-SEE with indices 0/1 confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [extended test_InlineAttributeEnums.py with initialization, literal, validation, set/get assertions; import failure before implementation]
   - [x] Step 3 — Implement model class (Green)  [ShowSeeEnum(AREnum) added with NO-SHOW-SEE/SHOW-SEE]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and literal descriptions copied verbatim from Table 9.55]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum has no own XML element; value form belongs to Xref]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Xref row owns SHOW-SEE coverage]
   - [x] Step 7 — Update checklist comment  [AREnum no-method checklist with six columns and R23-11 release; marker deferred to 9b]
   - [x] Step 8 — Deviations  [none: literals and indices match XSD SHOW-SEE-ENUM--SIMPLE]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, lint, and Black check pass; 9b: user-confirmed matched literals, enum values, docstrings, standalone N/A XML coverage, and no deviations; marker `# Spec verified: R23-11` written]
- [x] `Xref` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.42 · **created** · Package M2::MSR::Documentation::TextModel::InlineTextElements · Base `ARObject` · 12 attrs: label1(SingleLanguageLongName aggr)/referrable(Referrable ref)/resolutionPolicy + showContent + showResourceAliasName/Category/LongName/Number/Page/ShortName/Type + showSee (enums, all 0..1) · member type of `MixedContentForParagraph.xref`) — verified R23-11 (commit db2b4fe0)
   - [x] Step 1 — Sync members & description from spec  [Table 9.42, p.321; base ARObject; 12 attributes in displayed order; XSD XREF sequence confirms LABEL-1 then REFERRABLE-REF and XREF attribute group]
   - [x] Step 2 — Write model class unit test (Red)  [extended test_InlineTextElements.py with defaults and typed get/set/None-no-op assertions; ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [Xref(ARObject) added with 12 typed optional members and accessors; Kind=ref member uses `referrableRef`/`getReferrableRef`/`setReferrableRef` per Rule 0001.5]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and all 12 attribute Notes copied from Table 9.42]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser test for AR-OBJECT, LABEL-1, REFERRABLE-REF, and enum attributes; writer test for nested members and attributes; missing getXref/setXref = Red]
   - [x] Step 6 — Update parser & writer (Green)  [getXref/setXref cover AR-OBJECT, LABEL-1, REFERRABLE-REF, all 10 enum attributes, and XML nested-member order]
   - [x] Step 7 — Update checklist comment  [25 method rows (init + 12 getter/setter pairs) with six columns and R23-11 release; marker deferred to 9b]
   - [x] Step 8 — Deviations  [initial Kind=ref naming omission (`referrable` → `referrableRef`) corrected across model/accessors/checklist/parser/writer/tests; no remaining deviation]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused tests, lint, Black check, and diff check pass; 9b: user-confirmed matched base, members, Kind=ref naming, docstrings, reader/writer coverage, member order, and no deviations; marker `# Spec verified: R23-11` written]
- [x] `MixedContentForParagraph` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.2 (abstract, <<atpMixedString>>) · **created** · Package M2::MSR::Documentation::TextModel::InlineTextModel · Base `ARObject` · 13 attrs: br(Br)/e(EmphasisText ✓)/ft(SlParagraph)/ie(IndexEntry ✓)/std(Std)/sub(Superscript ✓)/sup(Superscript ✓)/trace(Traceable ref ✓)/tt(Tt ✓)/xdoc(Xdoc)/xfile(Xfile)/xref(Xref)/xrefTarget(XrefTarget) · parent of `LParagraph` and `SlParagraph`) — verified R23-11 (commit bf9114cb)
   - [x] Step 1 — Sync members & description from spec  [Table 9.2, p.289; abstract Base ARObject; 13 attributes in displayed order; `trace` Kind=ref modeled as `traceRef`; cyclic ft→SlParagraph dependency recorded]
   - [x] Step 2 — Write model class unit test (Red)  [extended test_LanguageDataModel.py with abstract guard, defaults, typed getters/setters, and None no-op assertions; ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [MixedContentForParagraph(ARObject, ABC) added with 13 typed optional members and accessors]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and member Notes copied from Table 9.2]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser/writer helper tests for BR, TT and empty optional dispatch; missing helpers = Red]
   - [x] Step 6 — Update parser & writer (Green)  [readMixedContentForParagraph/writeMixedContentForParagraph cover all 13 members, optional dispatch, and XML sequence order]
   - [x] Step 7 — Update checklist comment  [27 method rows (init + 13 getter/setter pairs) with six columns and R23-11 release; marker deferred to 9b]
   - [x] Step 8 — Deviations  [none: all 13 PDF attrs modeled with PDF types; Kind=ref naming corrected to traceRef; abstract reusable XML helpers cover every member]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: full unit suite (8943 passed) + flake8/ruff + black-check + set-based checklist==methods + lossless integration round-trip all green; 9b: user-confirmed element kind, most-derived base, no fabrication/type-drift, naming, set shape, reader+writer coverage (incl. added missing FT reader), member order, verbatim docstrings (incl. spec "refeernce" quirk), PEP 526 form, package location, no deviations; marker `# Spec verified: R23-11` written]
- [x] `SlParagraph` (dependency · **added 2026-09-11 LParagraph closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · **Table E.71** (appendix letter-numbered table; class table has no own attributes) · **created** · Package M2::MSR::Documentation::TextModel::SingleLanguageData · Base `ARObject , MixedContentForParagraph` (cyclic with MixedContentForParagraph; resolved by syncing this class after the base) · `MixedContentForParagraph.ft` member type · XSD `SL-PARAGRAPH` defines mixed text, inherited paragraph content, and deprecated optional `L` attribute; marker deferred pending 9b) — verified R23-11 (commit b7748b3)
   - [x] Step 1 — Sync members & description from spec  [Table E.71 Note copied verbatim; Base ARObject + MixedContentForParagraph; no own markdown attributes; XSD SL-PARAGRAPH group confirms mixed text, inherited content, and optional deprecated L attribute; XSD sequence is empty]
   - [x] Step 2 — Write model class unit test (Red)  [extended test_LanguageDataModel.py with defaults, inherited mixed-content fields, L getter/setter, and None no-op; ImportError before implementation]
   - [x] Step 3 — Implement model class (Green)  [SlParagraph(MixedContentForParagraph, LanguageSpecific) added; inherited value/L and paragraph content reused; 2 focused tests passed]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note copied verbatim from Table E.71; no own attribute Notes in the markdown table]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [new parser/writer tests for text, L, TT, and empty optional content; missing readSlParagraph/writeSlParagraph caused expected failures]
   - [x] Step 6 — Update parser & writer (Green)  [readSlParagraph/writeSlParagraph cover AR-OBJECT, recursive FT, MixedContentForParagraph, mixed text, L, and empty content; shared helpers now dispatch the cyclic ft member]
   - [x] Step 7 — Update checklist comment  [one own __init__ row with six columns + release R23-11; inherited LanguageSpecific and MixedContentForParagraph members remain on their declaring classes; marker deferred to 9b]
   - [x] Step 8 — Deviations  [none blocking: appendix Table E.71 has no own attributes; the deprecated `L` is handled via inherited LanguageSpecific (readSlParagraph reads/writes the L attribute, matching the spec Note "attribute l is there only for backwards compatibility"); recursive FT dispatch confirmed via readSlParagraph→readMixedContentForParagraph→SlParagraph recursion and the symmetric writer path; PDF page E.71 located at p.465 via direct PDF search (pdf_page.py does not index appendix tables, so the # Spec line was corrected manually); no remaining deviation]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: lint + black-check + 27 unit tests (parser/writer/model) + lossless integration round-trip all green; 9b: user-confirmed element kind (no own attributes, content inherited), most-derived base (MixedContentForParagraph + LanguageSpecific for l/value, matching stamped LParagraph), no fabrication/type-drift, reader+writer coverage via shared readSlParagraph/writeSlParagraph helpers (tested), verbatim class Note from Table E.71, package location, and resolved Step 8 deviation (PDF E.71 located p.465 manually; deprecated L + recursive FT confirmed); marker `# Spec verified: R23-11` written]
- [x] `LParagraph` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.92 (p.348) · member type of `MultiLanguageParagraph.l1` below · **no own spec attributes (`-` row); content comes from `Base` = ARObject , LanguageSpecific , MixedContentForParagraph** · unblocked once `MixedContentForParagraph` stamped) — verified R23-11 (commit 7fa4a01f)
  - [x] Step 1 — Sync members & description from spec  [Table 9.92 (p.348): Class `<<atpMixedString>> LParagraph`, Package M2::MSR::Documentation::TextModel::LanguageDataModel, Note "This is the text for a paragraph in one particular language. The language is denoted in the attribute l.", Base `ARObject , LanguageSpecific , MixedContentForParagraph`, Attribute `-` (no own attributes), Aggregated by `MultiLanguageParagraph.l1`]
  - [x] Step 2 — Write model class unit test (Red)  [+3 tests in test_LanguageDataModel.py::TestLParagraph: base-chain (issubclass MixedContentForParagraph + LanguageSpecific), verbatim-docstring (inspect.cleandoc vs Table 9.92 Note), inherited mixed-content accessors (set/getTt); all 3 failed Red before the fix]
  - [x] Step 3 — Implement model class (Green)  [base `LanguageSpecific` → `(MixedContentForParagraph, LanguageSpecific)`; class relocated to follow its new base at `LanguageDataModel.py:593` (mirrors stamped SlParagraph); `__init__` unchanged (`super().__init__()`); no own members]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [docstring replaced with the verbatim Table 9.92 Note; class has no own attributes so no member docstrings]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new `tests/test_armodel/parser/test_l_paragraph.py` (3: value+lang+TT, FT footnote, empty) + `tests/test_armodel/writer/test_l_paragraph.py` (3: value+lang+TT, empty, FT footnote)]
  - [x] Step 6 — Update parser & writer (Green)  [`getLParagraphs` now readARObject + readMixedContentForParagraph + setValue + setL (was readLanguageSpecific only); `writeLParagraphs` now writeMixedContentForParagraph + getValue + getL. The mixed-content write is guarded by `isinstance(l1, MixedContentForParagraph)` because this dispatch is shared with the L-1 containers of LOverviewParagraph/LLongName (which do not inherit MixedContentForParagraph); without the guard 9 pre-existing writer tests failed]
  - [x] Step 7 — Update checklist comment  [one own __init__ row (impl/docstring/test/reader/writer/release); inherited LanguageSpecific and MixedContentForParagraph members remain on their declaring classes; marker deferred to 9b]
  - [x] Step 8 — Deviations  [PDF page 348 confirmed by direct PDF text search; base chain corrected to include MixedContentForParagraph (was LanguageSpecific-only); reader/writer DISPATCH extended beyond the model body (getLParagraphs/writeLParagraphs) so the inherited mixed content round-trips — writer guarded by isinstance to avoid regressing LOverviewParagraph/LLongName; no remaining deviation]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8952 unit + 2 integration round-trip green, flake8/ruff/black clean, set-based checklist==methods OK (`{__init__}`); 9b: user-confirmed element kind (no own attributes), most-derived base (MixedContentForParagraph + LanguageSpecific), no fabrication/type-drift, reader+writer coverage via shared helpers (tested), verbatim class Note from Table 9.92, package location; marker `# Spec verified: R23-11` written]
- [x] `FrameEnum` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.65 · Package M2::MSR::Documentation::BlockElements::OasisExchangeTable → `OasisExchangeTable.py` · AREnum; literals all/bottom/none/sides/top/topbot indices 0-5 · aggregated by `Table.frame` + `MlFigure.frame`) — already verified (# Spec verified: R23-11, OasisExchangeTable.py); only the checklist `release` column was added (Rule 0012.3 drift-pass fix) (commit 531991e0)
  - [x] Step 1 — Sync members & description from spec  [short-circuit: class already carried # Spec verified: R23-11; quick deviation check found only the missing checklist release column]
  - [x] Step 2 — Write model class unit test (Red)  [already present: TestFrameEnum in test_OasisExchangeTable.py]
  - [x] Step 3 — Implement model class (Green)  [already present: FrameEnum(AREnum) with 6 literals ALL/BOTTOM/NONE/SIDES/TOP/TOPBOT]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [already verbatim from Table 9.65]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as FRAME attribute on Table/MlFigure]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: coverage lives in Table/MlFigure rows]
  - [x] Step 7 — Update checklist comment  [added `release R23-11` column per Rule 0012.3]
  - [x] Step 8 — Deviations  [none beyond the checklist-format fix]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 7 tests pass, flake8/ruff/black-check clean; 9b: already verified — marker confirmed in source]
- [x] `AlignEnum` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.67 · **NOT in src — created** · Package OasisExchangeTable → `OasisExchangeTable.py` · AREnum; literals center/justify/left/right indices 0-3 · aggregated by `Colspec.align`, `Entry.align`, `Tgroup.align`) — verified R23-11 (commit fa74a474)
  - [x] Step 1 — Sync members & description from spec  [Table 9.67, p.335; Note + 4 literals CENTER/JUSTIFY/LEFT/RIGHT indices 0-3 confirmed against markdown + XSD ALIGN-ENUM--SIMPLE]
  - [x] Step 2 — Write model class unit test (Red)  [TestAlignEnum in test_OasisExchangeTable.py: init, 4 literals, validateEnumValue, setValue/getValue; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [AlignEnum(AREnum) added to OasisExchangeTable.py with 4 XSD literals; exported via BlockElements __init__; 10 passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note + 4 literal descriptions copied verbatim from Table 9.67/XSD (RIGHT keeps spec's own "left justified" wording)]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as ALIGN attribute on Colspec/Entry/Tgroup]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming classes own ALIGN coverage]
  - [x] Step 7 — Update checklist comment  [one __init__ row with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: literals + indices match XSD ALIGN-ENUM--SIMPLE; no own XML element]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8963 unit + test_model_imports + ruff + black-check all green; 9b: user-confirmed matched literals/indices, docstrings verbatim, N/A XML coverage, package location, no deviations; marker # Spec verified: R23-11 written]
- [x] `ValignEnum` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.69 · **NOT in src — created** · Package OasisExchangeTable → `OasisExchangeTable.py` · AREnum; literals bottom/middle/top indices 0-2 · aggregated by `Entry.valign`, `Row.valign`, `Tbody.valign`) — verified R23-11 (commit 52d3272b)
  - [x] Step 1 — Sync members & description from spec  [Table 9.69, p.336; Note + 3 literals BOTTOM/MIDDLE/TOP indices 0-2 confirmed against markdown + XSD VALIGN-ENUM--SIMPLE]
  - [x] Step 2 — Write model class unit test (Red)  [TestValignEnum in test_OasisExchangeTable.py: init, 3 literals, validateEnumValue, setValue/getValue; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [ValignEnum(AREnum) added to OasisExchangeTable.py with 3 XSD literals; exported via BlockElements __init__; 13 passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note + 3 literal descriptions copied verbatim from Table 9.69/XSD]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as VALIGN attribute on Entry/Row/Tbody]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming classes own VALIGN coverage]
  - [x] Step 7 — Update checklist comment  [one __init__ row with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: literals + indices match XSD VALIGN-ENUM--SIMPLE; no own XML element]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8967 unit + test_model_imports + ruff + black-check all green; 9b: user-confirmed matched literals/indices, docstrings verbatim, N/A XML coverage, package location, no deviations; marker # Spec verified: R23-11 written]
- [x] `OrientEnum` (dependency · **added 2026-09-14 Table closure audit** · **XSD-only** (no R23-11 § no R4.3.1 markdown/PDF table) · `AUTOSAR_00052.xsd` `simpleType name="ORIENT-ENUM--SIMPLE"` line 140997 · **NOT in src — created** · Package OasisExchangeTable → `OasisExchangeTable.py` · AREnum; literals land/port · member type of `Table.orient` · carries `# XSD verified: AUTOSAR_00052.xsd`) — verified XSD (commit 9223f504)
  - [x] Step 1 — Sync members & description from spec  [XSD-only: ORIENT-ENUM--SIMPLE line 140997; 2 literals LAND/PORT indices 0-1 confirmed; no R23-11/R4.3.1 markdown/PDF table (grep + pdf_page.py)]
  - [x] Step 2 — Write model class unit test (Red)  [TestOrientEnum in test_OasisExchangeTable.py: init, 2 literals, validateEnumValue, setValue/getValue; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [OrientEnum(AREnum) added to OasisExchangeTable.py with 2 XSD literals; exported via BlockElements __init__; 16 passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class doc + LAND/PORT descriptions copied verbatim from XSD ORIENT-ENUM--SIMPLE / ORIENT attribute]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — serialized as ORIENT attribute on Table]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming Table row owns ORIENT coverage]
  - [x] Step 7 — Update checklist comment  [XSD-only checklist with (no methods) row + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: literals + indices match XSD ORIENT-ENUM--SIMPLE; no own XML element]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8970 unit + test_model_imports + ruff + black-check all green; 9b: user-confirmed XSD-only status, matched literals/indices, docstrings verbatim, N/A XML coverage, package location, no deviations; marker # XSD verified: AUTOSAR_00052.xsd written]
- [x] `TableSeparatorString` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.72 (`Primitive`) · **NOT in src — created** · Package OasisExchangeTable → `OasisExchangeTable.py` · **primitive** → `ARLiteral` subclass (Rule 0001.10); Tags `xml.xsd.customType=TABLE-SEPARATOR-STRING` `xml.xsd.pattern=[0-1]` `xml.xsd.type=string` · member type of every `colsep`/`rowsep` in the cluster) — verified R23-11 (commit 211031ea)
  - [x] Step 1 — Sync members & description from spec  [Class `Primitive TableSeparatorString`; Package M2::MSR::Documentation::BlockElements::OasisExchangeTable → OasisExchangeTable.py; Note = "This represents the ability to denote a separator string within an OASIS exchange table. • 0 : no line is displayed • 1 : line is displayed" (verbatim) + Tags xml.xsd.customType=TABLE-SEPARATOR-STRING / xml.xsd.pattern=[0-1] / xml.xsd.type=string; p.337 via pdf_page.py, confirmed against PDF p.337; no Attribute rows (Primitive table) → ARLiteral subclass, no fields beyond ARType's timestamp — same path as verified MimeTypeString]
  - [x] Step 2 — Write model class unit test (Red)  [TestTableSeparatorString in test_OasisExchangeTable.py: initialization (ARLiteral instance, _value None) + setValue round-trip/chaining/str(); ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [TableSeparatorString(ARLiteral) added to OasisExchangeTable.py; ARLiteral import added; exported via BlockElements __init__; 2 passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring = spec Note verbatim + the Tags block as an indented bullet list, per the stamped MimeTypeString precedent; diffed byte-equal against the markdown cell; PDF p.337 confirms the "• 0 : no line is displayed • 1 : line is displayed" wording is the spec's own]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone ARLiteral primitive with no own XML element — TABLE-SEPARATOR-STRING is never referenced as an element type in the XSD; it is used only as the COLSEP/ROWSEP attribute value on Colspec/Row in the OASIS exchange-table cluster, so the value form is covered by the consuming rows (queued later)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: see Step 5 — no element, no typed leaf helper needed (the COLSEP/ROWSEP attributes belong to the consuming Colspec/Row rows)]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.72, p.337; 1 row (__init__) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: spec table is a `Primitive` (not `Class`/`Enumeration`) → modeled as an `ARLiteral` subclass with no own fields (Rule 0001.10 primitive path); no attributes to type; reader/writer N/A (attribute-only usage — the COLSEP/ROWSEP attributes belong to the consuming Colspec/Row rows); no missing referenced classes (Base `ARLiteral`/`ARType` in src); no fabricated/naming/type rows]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 18 OasisExchangeTable tests (incl. TestTableSeparatorString ×2) + ruff + black-check + import-chain resolution all green; 9b: user-confirmed matched element kind (Primitive, no attrs), most-derived base (ARLiteral), no fabrication/type-drift, docstrings verbatim from Table 9.72 (incl. the "• 0 : no line is displayed • 1 : line is displayed" wording + Tags block), package location, and no deviations; marker `# Spec verified: R23-11` written; commit 211031ea]
- [x] `NameTokens` (dependency · **discovered 2026-09-14 during `DocumentViewSelectable` Step 1 closure audit (gap missed by the 2026-09-14 Table closure audit)** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.56 (`Primitive`) · **NOT in src — created** · Package `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes` → `PrimitiveTypes.py` (same file as `NameToken`/`MimeTypeString`) · **primitive** → `ARLiteral` subclass (Rule 0001.10) · Tags `xml.xsd.customType=NMTOKENS-STRING` `xml.xsd.type=NMTOKENS` · member type of `DocumentViewSelectable.si` (Table 9.77, mult 1) · queued immediately before `DocumentViewSelectable` (Rule 0016.5)) — verified R23-11 (commit c8a3ff50)
  - [x] Step 1 — Sync members & description from spec  [Class `Primitive NameTokens`; Package M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes → PrimitiveTypes.py; Note = "This is a white-space separated list of name tokens." (verbatim) + Tags xml.xsd.customType=NMTOKENS-STRING / xml.xsd.type=NMTOKENS; p.111 via pdf_page.py, confirmed against PDF p.111; no Attribute rows (Primitive table) → ARLiteral subclass, no fields beyond ARType's timestamp — same path as verified MimeTypeString; placed after MimeTypeString (Table 4.55), continuing the 4.54→4.55→4.56 file order]
  - [x] Step 2 — Write model class unit test (Red)  [TestNameTokens in test_PrimitiveTypes.py: initialization (ARLiteral instance, _value None) + setValue round-trip/chaining/str(); ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [NameTokens(ARLiteral) added to PrimitiveTypes.py immediately after MimeTypeString (Table 4.55 → 4.56 spec order); exported via the module wildcard; 2 passed; `armodel.NameTokens` resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring = spec Note verbatim + the Tags block as an indented bullet list, per the stamped MimeTypeString precedent; diffed byte-equal against the markdown cell; PDF p.111 confirms the wording]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone ARLiteral primitive with no own XML element — NMTOKENS-STRING is never referenced as an element type in the XSD; it is used only as the SI attribute value on DocumentViewSelectable, so the value form is covered by the consuming `DocumentViewSelectable` row (queued next)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: see Step 5 — no element, no typed leaf helper needed (the SI attribute belongs to the consuming `DocumentViewSelectable` row)]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 4.56, p.111; 1 row (__init__) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: spec table is a `Primitive` (not `Class`/`Enumeration`) → modeled as an `ARLiteral` subclass with no own fields (Rule 0001.10 primitive path); no attributes to type; reader/writer N/A (attribute-only usage — the SI attribute belongs to the consuming `DocumentViewSelectable` row); no missing referenced classes (Base `ARLiteral`/`ARType` in src); no fabricated/naming/type rows. Note the dependency itself was the deviation being fixed: `NameTokens`+`ViewTokens` were missing from src and from the Table 9.77 closure — now queued before `DocumentViewSelectable` (Rule 0016.5)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 107 test_PrimitiveTypes tests (incl. TestNameTokens ×2) + ruff + black-check + `armodel.NameTokens` resolution all green; 9b: user-confirmed matched element kind (Primitive, no attrs), most-derived base (ARLiteral), no fabrication/type-drift, docstrings verbatim from Table 4.56, package location, no deviations, and the closure-gap fix (NameTokens/ViewTokens queued before DocumentViewSelectable); marker `# Spec verified: R23-11` written; commit c8a3ff50]
- [x] `ViewTokens` (dependency · **discovered 2026-09-14 during `DocumentViewSelectable` Step 1 closure audit (gap missed by the 2026-09-14 Table closure audit)** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.78 (`Primitive`) · **NOT in src — created** · Package `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes` → `PrimitiveTypes.py` · **primitive** → `ARLiteral` subclass (Rule 0001.10) · Tags `xml.xsd.customType=VIEW-TOKENS` `xml.xsd.pattern=(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*` `xml.xsd.type=string` · member type of `DocumentViewSelectable.view` (Table 9.77, 0..1) · queued immediately before `DocumentViewSelectable` (Rule 0016.5)) — verified R23-11 (commit pending)
   - [x] Step 1 — Sync members & description from spec  [Table 9.78, p.340; Primitive Note and XSD tags copied from markdown; no Attribute rows → ARLiteral subclass; member type of DocumentViewSelectable.view]
   - [x] Step 2 — Write model class unit test (Red)  [TestViewTokens in test_PrimitiveTypes.py: initialization (ARLiteral instance, _value None) + setValue round-trip/chaining/str(); ImportError = Red]
   - [x] Step 3 — Implement model class (Green)  [ViewTokens(ARLiteral) added after NameTokens in PrimitiveTypes.py; exported via module wildcard]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and Tags copied verbatim from Table 9.78]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone ARLiteral primitive with no own XML element; value form belongs to DocumentViewSelectable.view]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: consuming DocumentViewSelectable row owns VIEW attribute coverage]
   - [x] Step 7 — Update checklist comment  [one __init__ row with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none: Primitive modeled as ARLiteral; note/tags match Table 9.78; no own XML element]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 109 PrimitiveTypes tests, model-import test, lint, Black check, and diff check pass; 9b: user-confirmed Primitive kind, ARLiteral base, verbatim Note/Tags, N/A standalone XML coverage, package location, and no deviations; marker `# Spec verified: R23-11` written; commit pending]
- [x] `DocumentViewSelectable` (tracker input · **moved 2026-09-14 Table closure audit ahead of `Table`/`Row`** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.77 · abstract `ARObject` mixin · **in src** (`PaginationAndView.py`) · needs 2 new attrs `si`(NameTokens 1)/`view`(ViewTokens 0..1) + reusable read/write helpers (Rule 0001.7) · **unblocked after `NameTokens` + `ViewTokens` synced** · Base of `Table`, `Row`, and `MultiLanguageParagraph`/`MlFigure`/`MsrQueryChapter`/`MsrQueryTopic1`/`MsrQueryP1`) — verified R23-11 (commit pending)
   - [x] Step 1 — Sync members & description from spec  [Table 9.77, p.340; Base ARObject; attrs si NameTokens 1 and view ViewTokens 0..1; XSD SI/VIEW attribute group confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [extended test_PaginationAndView.py with abstract/default tests, typed get/set and None no-op assertions; missing getSi = Red]
   - [x] Step 3 — Implement model class (Green)  [added si/view typed members and getSi/setSi/getView/setView to abstract DocumentViewSelectable]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and both attribute Notes copied verbatim from Table 9.77; checklist added]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser both attrs + absent VIEW; writer both attrs + absent VIEW; missing serialization = Red]
   - [x] Step 6 — Update parser & writer (Green)  [read/writeDocumentViewSelectable cover SI and VIEW; inherited Paginateable dispatch retains BREAK/KEEP coverage]
   - [x] Step 7 — Update checklist comment  [init + 4 accessors, six-column checklist with R23-11 release]
   - [x] Step 8 — Deviations  [none: both PDF attrs modeled with PDF types; abstract reusable XML helper covers every member; no fabrication or missing dependencies]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 18 model + 4 parser/writer focused tests, model imports, lint, Black check, and diff check pass; 9b: user-confirmed abstract ARObject base, member order/types, verbatim docs, SI/VIEW reader+writer coverage, package location, and no deviations; marker `# Spec verified: R23-11` written; commit pending]
- [x] `Colspec` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · **Table E.20** (appendix letter-numbered table; the markdown `Table E.21: Colspec` title is a rendering mislabel — that block is actually the `Compiler` class; Colspec located via PDF text search p.433) · Package M2::MSR::Documentation::BlockElements::OasisExchangeTable → `OasisExchangeTable.py` · Base ARObject; attrs align(AlignEnum 0..1)/colname(String 0..1)/colnum(String 0..1)/colsep(TableSeparatorString 0..1)/colwidth(String 0..1)/rowsep(TableSeparatorString 0..1) all attr · member type of `Tgroup.colspec`) — already verified (# Spec verified: R23-11, OasisExchangeTable.py); citation corrected E.21/p.434 → E.20/p.433 (Rule 0012.3 drift fix); full model+parser+writer+tests green in prior session, changes committed this pass (commit 2bd0d075)
- [x] `Entry` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.71 · **NOT in src — created** · Package OasisExchangeTable · Base `ARObject` · 12 attrs align(AlignEnum)/bgcolor(String 1)/colname/colsep(TableSeparatorString)/entryContents(DocumentationBlock 1 aggr)/morerows/nameend/namest/rotate/rowsep/spanname/valign(ValignEnum) · member type of `Row.entry`) — verified R23-11 (commit 9005f622)
  - [x] Step 1 — Sync members & description from spec  [Table 9.71, p.337 via pdf_page.py; Note "This represents one particular table cell."; Base ARObject; 12 attrs in displayed order; XSD ENTRY attributeGroup (line 55020) confirms ALIGN/BGCOLOR/COLNAME/COLSEP/MOREROWS/NAMEEND/NAMEST/ROTATE/ROWSEP/SPANNAME/VALIGN + DOCUMENTATION-BLOCK element; XSD's removed BGCOLOR element (atp.Status="removed", backwards-compat) correctly NOT modeled per Rule 0015]
  - [x] Step 2 — Write model class unit test (Red)  [TestEntry in test_OasisExchangeTable.py: initialization (12 getters None) + all 12 get/set pairs with chaining + None no-op; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [Entry(ARObject) added to OasisExchangeTable.py after Colspec; 12 typed optional members (PEP 526) + accessors; DocumentationBlock via TYPE_CHECKING import (avoids the OasisExchangeTable ↔ TextModel.BlockElements ↔ MultilanguageData cycle); exported via BlockElements __init__ import + __all__; 1 passed; `armodel.Entry` resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [brand-new class — no stale docstrings; class docstring + all 12 inline __init__ comments + getter/setter docstrings = spec Note verbatim from markdown lines 8920-8944 (incl. spec's own "bases on" typo); setters append the None-no-op sentence]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser test_entry.py (all 12 attrs + minimal w/ only DOCUMENTATION-BLOCK); writer test_entry.py (all attrs, minimal, roundtrip w/ xmlns injection for the namespace-aware parser); missing readEntry/writeEntry = Red]
  - [x] Step 6 — Update parser & writer (Green)  [readEntry = readARObject + 11 typed attributes + getDocumentationBlock("DOCUMENTATION-BLOCK"); writeEntry = writeARObject + 11 attributes + writeDocumentationBlock; attributes in XSD attributeGroup order, DOCUMENTATION-BLOCK in sequence position; Entry added to parser BlockElements import + ValignEnum to OasisExchangeTable import; Entry added to writer import; 6 focused tests passed]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.71, p.337; 25 rows (init + 12 getter/setter pairs) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: all 12 PDF attrs modeled with PDF types (6 String, 2 TableSeparatorString, 1 AlignEnum, 1 ValignEnum, 1 DocumentationBlock aggr), names verbatim from the Attribute column, member order = markdown displayed order, reader+writer coverage for every member; XSD-only removed BGCOLOR element not modeled (Rule 0015)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8989 unit + 2 integration round-trips pass, flake8/ruff/black-check clean, `armodel.Entry` resolves, set-based checklist==methods (25 rows); 9b: 11-item pre-stamp checklist user-confirmed; marker `# Spec verified: R23-11` present; commit 9005f622]
 - [x] `Row` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.70 · **NOT in src — created** · Package OasisExchangeTable · Base `ARObject , DocumentViewSelectable , Paginateable` · attrs entry(Entry 1..* aggr)/rowsep(TableSeparatorString)/valign(ValignEnum) · member type of `Tbody.row`) — verified R23-11 (commit b43b8601)
   - [x] Step 1 — Sync members & description from spec  [Table 9.70, p.336; Base ARObject + DocumentViewSelectable + Paginateable; attrs entry(Entry 1..* aggr), rowsep(TableSeparatorString 0..1 attr), valign(ValignEnum 0..1 attr); XSD ROW group confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [TestRow in test_OasisExchangeTable.py: base inheritance, defaults, typed aggregation/accessors, chaining, None no-op; ImportError = Red]
   - [x] Step 3 — Implement model class (Green)  [new Row(Paginateable) with typed entries list, rowsep, valign fields and accessors; exported via BlockElements __init__; 23 focused model tests pass]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and all three member/accessor docs copied from Table 9.70; PEP 526 members]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [test_row.py parser/writer: inherited S/T, SI, BREAK, ROWSEP, VALIGN, ordered ENTRY children, and empty ROW; missing readRow/writeRow and typed fixture setup caused expected failures]
   - [x] Step 6 — Update parser & writer (Green)  [readRow/writeRow reuse Paginateable helpers, parse/write ordered ENTRY children, ROWSEP and VALIGN; 4 focused tests pass]
   - [x] Step 7 — Update checklist comment  [7 method rows with six columns and R23-11 release; marker deferred to 9b]
   - [x] Step 8 — Deviations  [none: all three Table 9.70 members modeled with PDF types; inherited DocumentViewSelectable/Paginateable XML coverage reused; no fabrication or missing dependencies]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 8996 unit tests, focused Row tests, lint, and Black check pass; 9b: user-confirmed matched base, members, docstrings, reader/writer coverage, member order, package location, and no deviations; marker `# Spec verified: R23-11` written; commit b43b8601]
 - [x] `Tbody` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.68 · **NOT in src — created** · Package OasisExchangeTable · Base `ARObject` · attrs row(Row 1..* aggr)/valign(ValignEnum) · member type of `Tgroup.tbody`/`tfoot`/`thead`) — verified R23-11 (commit 004d3f12)
   - [x] Step 1 — Sync members & description from spec  [Table 9.68, p.335; Base ARObject; attrs row(Row 1..* aggr) and valign(ValignEnum 0..1 attr); XSD TBODY group confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [TestTbody in test_OasisExchangeTable.py: defaults, typed row aggregation, valign chaining and None no-op; ImportError = Red]
   - [x] Step 3 — Implement model class (Green)  [new Tbody(ARObject) with typed rows list and valign field/accessors; exported via BlockElements __init__; model tests pass]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and row/valign member/accessor docs copied from Table 9.68; PEP 526 members]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [test_tbody.py parser/writer: inherited S/T, VALIGN, ordered ROW children, and empty TBODY; missing readTbody/writeTbody caused expected failures]
   - [x] Step 6 — Update parser & writer (Green)  [readTbody/writeTbody reuse readRow/writeRow, preserve ordered ROW children, and serialize VALIGN; 4 focused tests pass]
   - [x] Step 7 — Update checklist comment  [5 method rows with six columns and R23-11 release; marker deferred to 9b]
   - [x] Step 8 — Deviations  [none: both Table 9.68 members modeled with PDF types; XSD sequence offset 20 preserved; no fabrication or missing dependencies]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9001 unit tests, focused Tbody tests, lint, Black check, and diff check pass; 9b: user-confirmed matched base, members, docstrings, reader/writer coverage, member order, package location, and no deviations; marker `# Spec verified: R23-11` written; commit 004d3f12]
 - [x] `Tgroup` (dependency · **added 2026-09-14 Table closure audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.66 · **NOT in src — created** · Package OasisExchangeTable · Base `ARObject` · attrs align(AlignEnum)/cols(Integer 1)/colsep(TableSeparatorString)/colspec(Colspec * aggr)/rowsep(TableSeparatorString)/tbody(Tbody 1)/tfoot(Tbody 0..1)/thead(Tbody 0..1) · member type of `Table.tgroup`) — verified R23-11 (commit 278d4674)
   - [x] Step 1 — Sync members & description from spec  [Table 9.66, p.335; Base ARObject; attrs in displayed order: align, cols, colsep, colspec, rowsep, tbody, tfoot, thead; XSD sequence COLSPEC*, THEAD, TFOOT, TBODY confirmed]
   - [x] Step 2 — Write model class unit test (Red)  [TestTgroup in test_OasisExchangeTable.py: defaults, typed aggregation, single-child accessors, typed attributes, and None no-op behavior; ImportError = Red]
   - [x] Step 3 — Implement model class (Green)  [new Tgroup(ARObject) with typed align/cols/colsep/colspecs/rowsep/tbody/tfoot/thead fields and accessors; exported via BlockElements __init__; model tests pass]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and all seven member/accessor docs copied from Table 9.66; PEP 526 members]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [test_tgroup.py parser/writer: S/T, all attributes, ordered COLSPEC/THEAD/TFOOT/TBODY children, and empty optional content; missing readTgroup/writeTgroup caused expected failures]
   - [x] Step 6 — Update parser & writer (Green)  [readTgroup/writeTgroup reuse Colspec/Tbody helpers, preserve XSD child order, parse Integer COLS, and serialize all attributes; 4 focused tests pass]
   - [x] Step 7 — Update checklist comment  [17 method rows with six columns and R23-11 release; marker deferred to 9b]
   - [x] Step 8 — Deviations  [none: all seven Table 9.66 members modeled with PDF types; XSD sequence offsets 20/40/50/60 preserved; no fabrication or missing dependencies]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9006 unit tests, focused Tgroup tests, lint, Black check, and diff check pass; 9b: user-confirmed matched member/accessor order, base, members, docstrings, reader/writer coverage, XSD XML order, package location, and no deviations; marker `# Spec verified: R23-11` written; commit 278d4674]
- [x] `Table` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.63 · member type of `TopicContent.table` + `TraceableTable.table` · **NOT in src — created** · Package OasisExchangeTable · Base `ARObject , DocumentViewSelectable , Paginateable` · 10 attrs colsep(TableSeparatorString)/float(FloatEnum ✓)/frame(FrameEnum)/helpEntry(String)/orient(OrientEnum)/pgwide(NameToken)/rowsep(TableSeparatorString)/tableCaption(Caption ✓ aggr)/tabstyle(NameToken)/tgroup(Tgroup 1..* aggr) · **unblocked once the 10 dependency rows above are synced**)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9 focused Table tests (model 4/parser 2/writer 3), lint, Black check pass; 9b: user-confirmed matched member/accessor order, base, members, docstrings, reader/writer coverage, package location, resolved quoted Caption forward-reference, and no blocking deviations (float modeled 0..1 vs spec 1, uniform optional handling); marker `# Spec verified: R23-11` written; commit e347fbbf]
- [x] `TraceableTable` (dependency · **added 2026-09-11 missing-class audit** · **XSD-only** (no R23-11 markdown 9.x/E.x table, no R4.3.1 table, no PDF table — verified 2026-09-16 via grep of all three corpora + pdf_page.py) · AUTOSAR_00052.xsd `complexType name="TRACEABLE-TABLE"` line 125345 (+ group line 125328) · member type of `TopicContent.traceableTable` · **NOT in src** — class must be created when this row is synced · 16.4 decision: Derive-from-XSD → carries `# XSD verified: AUTOSAR_00052.xsd`) — verified XSD (commit fa79c73d)
  - [x] Step 1 — Sync members & description from spec  [XSD-only: Package MSR::Documentation::BlockElements::RequirementsTracing (XSD comment line 125344) → RequirementsTracing.py after StructuredReq; doc "This meta-class represents the ability to denote a traceable table item such as requirements etc.." (verbatim, double period is the XSD's own); stereotype atpObject; Base closure from group refs AR-OBJECT/REFERRABLE/MULTILANGUAGE-REFERRABLE/IDENTIFIABLE/DOCUMENT-VIEW-SELECTABLE/PAGINATEABLE/TRACEABLE → Python bases (Traceable, Paginateable) — TraceableText precedent (Traceable, VariationPointCapable); 1 own member `table` → TABLE element (AR:TABLE), XSD element minOccurs=0 (pureMM 1) → modeled 0..1 optional per the Table.float uniform-optional precedent; doc "This represents a table with a traceable table.\nThis aggregation contains a variation point although it is not variant. Therefore, this variation point shall not exist in models. See constr_2638."; non-Referrable child (Table derives Paginateable→ARObject) → set/get, no createXxx (Rule 0001.6); no VARIATION-POINT attributeGroup on the complexType → not VP-capable; TRACEABLE--SUBTYPES-ENUM already includes TRACEABLE-TABLE (DEST values); consumer TopicContent queued next; MRO note: Referrable.__init__ calls ARObject.__init__ directly → TraceableTable.__init__ must call Paginateable.__init__(self) explicitly BEFORE super().__init__(parent, short_name) so si/view/chapterBreak/keepWithPrevious initialize and parent/short_name survive]
  - [x] Step 2 — Write model class unit test (Red)  [TestTraceableTable in test_RequirementsTracing.py: XSD-note docstring match, base chain (issubclass Traceable + Paginateable), initialization defaults (table/traceRefs/si/view/chapterBreak/keepWithPrevious/parent/short_name), get/set table with chaining + None no-op, inherited addTraceRef/getTraceRefs; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [TraceableTable(Traceable, Paginateable) added to RequirementsTracing.py after StructuredReq; Paginateable import added (runtime, no cycle); Table via TYPE_CHECKING (mirrors Entry/DocumentationBlock precedent); __init__ calls Paginateable.__init__(self) first (Referrable.__init__ bypasses the Paginateable MRO branch via direct ARObject.__init__ call), then super().__init__(parent, short_name); `table: Optional["Table"]` PEP 526 + getTable/setTable with None no-op; 24 passed; `armodel.TraceableTable` resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [brand-new class — no stale docstrings; class docstring = XSD complexType documentation verbatim (byte-diffed, incl. the "etc.." double period); table inline comment + getter docstring + setter docstring (+"A None value is a no-op...") = XSD TABLE element documentation verbatim (byte-diffed, paragraph-join whitespace only); __init__ has no docstring per Rule 0012.2.4]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_traceable_table.py (4: full attrs incl. S/T/UUID/SI/VIEW/BREAK/KEEP-WITH-PREVIOUS + TRACE-REFS + TABLE, empty optional, getTraceableTable, missing → None) + tests/test_armodel/writer/test_traceable_table.py (3: full attrs + SHORT-NAME + TRACE-REF + TABLE child, empty optional, write→read roundtrip asserting field values); 7 failed = Red (readTraceableTable/getTraceableTable/setTraceableTable missing)]
  - [x] Step 6 — Update parser & writer (Green)  [parser `readTraceableTable` = readIdentifiable + readTraceable + direct attrib reads of SI/VIEW/BREAK/KEEP-WITH-PREVIOUS (readDocumentViewSelectable/readPaginateable would re-invoke readARObject on top of readIdentifiable — Rule 0013.1) + TABLE child via readTable; `getTraceableTable(element, key, parent=None)` mirrors getTraceableText (SHORT-NAME → key fallback); writer `setTraceableTable(element, key, traceable_table)` = writeIdentifiable + direct SI/VIEW/BREAK/KEEP-WITH-PREVIOUS attrib writes (writeDocumentViewSelectable/writePaginateable would re-invoke writeARObject) + writeTraceable + TABLE subelement via writeTable; imports added to both (TraceableTable, +Table in parser); 7 focused tests passed]
  - [x] Step 7 — Update checklist comment  [XSD-only checklist: `# Spec: AUTOSAR_FO_TPS_GenericStructureTemplate (GST), class TraceableTable, AUTOSAR_00052.xsd line 125345 (XSD-only; no own table in repo corpus)`; 5 method rows (__init__, getTable, setTable + inherited getTraceRefs/addTraceRef) with 6 columns + release R23-11; `# XSD verified: AUTOSAR_00052.xsd` marker deferred to 9b]
  - [x] Step 8 — Deviations  [none blocking: 1 own spec member `table` (XSD group TRACEABLE-TABLE) modeled with type `Table` (stamped ✓), name verbatim, get/set (non-Referrable child — Rule 0001.6), full reader+writer coverage; XSD element minOccurs=0 vs pureMM.minOccurs=1 → modeled 0..1 optional, same accepted uniform-optional handling as Table.float (non-blocking); explicit Paginateable.__init__ call is an MRO implementation note (Referrable.__init__ calls ARObject.__init__ directly), not a spec deviation; no missing referenced classes (Traceable/Paginateable/DocumentViewSelectable/Table all stamped); inherited Identifiable/mixin members covered at the XML layer via readIdentifiable + direct attrib reads; # XSD verified marker to be written at 9b]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9023 unit + 2 integration round-trips pass; flake8/ruff/black-check clean; checklist == methods; 9b fix round: Table moved from TYPE_CHECKING to direct runtime import per user feedback (no quoted forward-reference; verified no import cycle), full suite re-run green; 9b: user-confirmed XSD-only kind, base (Traceable, Paginateable) from XSD group closure, verbatim docstrings, reader/writer coverage incl. inherited SI/VIEW/BREAK/KEEP + TRACE-REFS without double readARObject, member order, no deviations; marker `# XSD verified: AUTOSAR_00052.xsd` written; commit fa79c73d]
- [x] `TopicContent` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · **AUTOSAR_FO_TPS_GenericStructureTemplate Table E.81 (appendix letter-numbered table missed by numeric-regex tooling, same as Group2 D.17/D.4 cases)** · member type of `MsrQueryP1.msrQueryResultP1` below · <<atpMixed>> · `traceableTable` TraceableTable remains pending 16.4) — verified R23-11 (commit 6d7e3257)
  - [x] Step 1 — Sync members & description from spec  [partial placeholder at Chapters.py:495 (blockLevelContent only; table/traceableTable deferred until Table/TraceableTable landed — both now stamped); Table E.81 confirmed in markdown L12889 + PDF p.478 via direct search (pdf_page.py does not index appendix tables, E.71 precedent); Package M2::MSR::Documentation::Chapters → Chapters.py; Base ARObject; class Note verbatim; 3 attrs in displayed order: blockLevelContent (DocumentationBlock, 1, aggr, Note + Tags: xml.roleElement=false; non-Referrable child → set/get), table (Table, 0..1, aggr, Note + Stereotypes atpSplitable/atpVariation + Tags; Table(Paginateable) non-Referrable → set/get), traceableTable (TraceableTable, 1, aggr; TraceableTable Referrable-derived → Rule 0001.6 createTraceableTable(short_name)+getTraceableTable, NO setter; XSD choice minOccurs=0 vs pureMM 1 → uniform-optional Optional[TraceableTable]); XSD TOPIC-CONTENT complexType mixed="false" AR-OBJECT attrs only, group = choice(DOCUMENTATION-BLOCK group | TABLE | TRACEABLE-TABLE); MsrQueryP1.msrQueryResultP1 wiring stays on the MsrQueryP1 stub row]
  - [x] Step 2 — Write model class unit test (Red)  [TestTopicContent appended to test_Chapters.py: initialization (blockLevelContent/table/traceableTable None), blockLevelContent + table set/get with chaining + None no-op, createTraceableTable (instance/short-name/parent/get), create-returns-existing, create-replaces-different-short-name; 5 failed (AttributeError on missing table/traceableTable members) = Red]
  - [x] Step 3 — Implement model class (Green)  [in-place completion of the Chapters.py placeholder: runtime imports Table (OasisExchangeTable) + TraceableTable (RequirementsTracing) added (verified no import cycle); `table: Optional[Table]` + `traceableTable: Optional[TraceableTable]` PEP 526 members in spec row order; setTable/getTable (Table non-Referrable, Rule 0001.6) and createTraceableTable(short_name)/getTraceableTable (TraceableTable Referrable-derived → create+get, NO setter per Rule 0001.6; create returns existing on same short name, replaces on different); blockLevelContent annotation unquoted Optional[DocumentationBlock] (future-annotations file, TYPE_CHECKING import — Identifiable.py precedent); 19 passed; armodel import OK]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring + all 3 inline __init__ comments + getter/setter docstrings diffed byte-verbatim against the Table E.81 cells (script-verified): blockLevelContent gained the missing `Tags: xml.roleElement=false` tail (stale placeholder wording wiped, OasisExchangeTable inline-Tags precedent); table note includes Stereotypes atpSplitable/atpVariation + Tags; createTraceableTable docstring = Note verbatim + Args/Returns; __init__ has no docstring (Rule 0012.2.4)]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_topic_content.py (2: full TOPIC-CONTENT with DOCUMENTATION-BLOCK P/L-1 + TABLE FRAME/TGROUP COLS + TRACEABLE-TABLE SHORT-NAME, value-asserting; empty → all None) + tests/test_armodel/writer/test_topic_content.py (3: full write incl. XSD choice order [DOCUMENTATION-BLOCK, TABLE, TRACEABLE-TABLE], empty optional, write→read roundtrip asserting cell text/L/FRAME/COLS/short-name/SI); 3 failed = Red (TABLE/TRACEABLE-TABLE not read/written)]
  - [x] Step 6 — Update parser & writer (Green)  [parser readTopicContent extended: TABLE child → new Table() + readTable + setTable; TRACEABLE-TABLE child → SHORT-NAME resolve (fallback "TRACEABLE-TABLE") + topic_content.createTraceableTable(short_name) + readTraceableTable (reader populates via mutators, Rule 0001.7; reuses the Table/TraceableTable rows' readTable/readTraceableTable helpers — no double readARObject); writer writeTopicContent extended: writeTable via SubElement("TABLE") + setTraceableTable via SubElement("TRACEABLE-TABLE"), emitted in XSD choice order DOCUMENTATION-BLOCK → TABLE → TRACEABLE-TABLE; no import changes needed (both layers already imported Table/TraceableTable); 36 focused tests passed]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table E.81, p.478 (appendix table — page verified by direct PDF search, pdf_page.py does not index E-tables); 7 method rows (init + 3 mutator/getter pairs) with 6 columns + release R23-11; stale stub NOTE removed; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none blocking: (1) `table` PDF Mult 0..1 vs XSD maxOccurs=* (atpVariation raise, previous value 1) → PDF authoritative per Rule 0015, modeled 0..1 Optional; (2) `blockLevelContent`/`traceableTable` PDF Mult 1 vs XSD choice minOccurs=0 → uniform-optional Optional modeling (same accepted handling as Table.float / TraceableTable.table); (3) `traceableTable` Referrable-derived child → createTraceableTable(short_name)+getTraceableTable shape is the Rule 0001.6 compliance, not a deviation; (4) atpMixed stereotype with XSD mixed="false" and no text content → no value field modeled (matches spec); (5) MsrQueryP1.msrQueryResultP1 → TopicContent wiring stays deferred to the MsrQueryP1 stub row (queued below); Step-3 referenced classes all stamped: Table ✓, TraceableTable ✓, DocumentationBlock ✓ — no missing classes, no naming/type rows]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9,034 unit + integration round-trips pass; flake8/ruff/black-check clean; set-based checklist==methods exact match in order; 9b: user-confirmed element kind, base ARObject, no fabrication (3 fields ↔ 3 spec rows, PDF types), verbatim docstrings (byte-diffed incl. Tags/Stereotypes tails), Rule 0001.6 shape (set/get non-Referrable; create+get for Referrable-derived traceableTable), reader+writer coverage, member order vs markdown + XSD choice order, package location, no blocking deviations (PDF-authoritative table 0..1 vs XSD *; uniform-optional Mult-1 attrs; MsrQueryP1 wiring deferred to its stub row); marker `# Spec verified: R23-11` written]
- [x] `MultiLanguageParagraph` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.4 · after `Paginateable` (parent) + `DocumentViewSelectable` (parent, moved above) + `LParagraph` (aggr `l1`)) — verified R23-11 (commit 77074563)
  - [x] Step 1 — Sync members & description from spec  [Table 9.4 markdown L7556 + XSD complexType MULTI-LANGUAGE-PARAGRAPH (mixed="false", atpObject; sequence AR-OBJECT + DOCUMENT-VIEW-SELECTABLE + PAGINATEABLE + MULTI-LANGUAGE-PARAGRAPH groups; attributeGroups AR-OBJECT/DOCUMENT-VIEW-SELECTABLE/PAGINATEABLE — NO VARIATION-POINT attributeGroup) + group MULTI-LANGUAGE-PARAGRAPH (L-1 unbounded type L-PARAGRAPH pureMM 1..* sequenceOffset=20; generated VARIATION-POINT element atpVariation "Applicable for: DocumentationBlock.p" sequenceOffset=10000) + attribute HELP-ENTRY (STRING--SIMPLE 0..1 xml.attribute=true); Note = "This is the content model of a multilingual paragraph in a documentation."; Package M2::MSR::Documentation::TextModel::MultilanguageData → MultilanguageData.py; Aggregated by DocumentationBlock.p; Base ARObject , DocumentViewSelectable , Paginateable → most-derived Paginateable (Paginateable extends DocumentViewSelectable — same collapse as stamped Table(Paginateable), identical spec Base); **spec deviations found in src**: (1) base `(Paginateable, VariationPointCapable)` — spec Base has NO VariationPointCapable → fix to `(Paginateable)` (generated VARIATION-POINT element is Rule-0015-arbitrated: PDF Base wins, consistent with the Paginateable family — Table/Tgroup readers/writers model no VP); (2) `l1` field typed List[LLongName] — spec type is LParagraph → retype List[LParagraph] (parser getLParagraphs already builds LParagraph); (3) `helpEntry` String 0..1 attr missing → add get/set; (4) addL1 lacks the None no-op → fix; 2 attrs in displayed order: helpEntry, l1]
  - [x] Step 2 — Write model class unit test (Red)  [TestMultiLanguageParagraph rewritten spec-driven in test_MultilanguageData.py: initialization (l1 [], helpEntry/si/view/break/keepWithPrevious None), base chain (issubclass Paginateable + DocumentViewSelectable, NOT VariationPointCapable), l1 add/get with LParagraph + insertion order + None no-op, helpEntry set/get chaining + None no-op; 4 failed (helpEntry AttributeError, VP base, None-append, accessors) = Red]
  - [x] Step 3 — Implement model class (Green)  [base fixed to (Paginateable) — VariationPointCapable import retained (MultiLanguageVerbatim uses it); `helpEntry: Optional[String]` + setHelpEntry/getHelpEntry added; `l1` retyped List[LParagraph] (LLongName dropped); addL1 None no-op + chaining; LParagraph import added; 20 passed; MRO = MLP → Paginateable → DocumentViewSelectable → ARObject]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring = Table 9.4 Note verbatim; helpEntry inline comment + getter + setter = attr Note verbatim (same wording as stamped Chapter.helpEntry); l1 inline comment + addL1 + getL1s = attr Note verbatim incl. the spec typo "partiucular"; setter/adder append the None-no-op sentence; __init__ no docstring (Rule 0012.2.4); byte-diff script verified all 7 surfaces]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_multi_language_paragraph.py (2: full P with SI/VIEW/BREAK/KEEP-WITH-PREVIOUS/HELP-ENTRY attribs + L-1 value-asserting; minimal → all None/[]) + tests/test_armodel/writer/test_multi_language_paragraph.py (3: full write incl. attrib asserts, minimal absent-attribs, write→read roundtrip); 3 failed = Red (mixin attrs + HELP-ENTRY not read/written)]
  - [x] Step 6 — Update parser & writer (Green)  [parser getMultiLanguageParagraphs: readARObject → readPaginateable (single readARObject through the mixin chain; covers SI/VIEW/BREAK/KEEP-WITH-PREVIOUS — readMlFigure precedent) + HELP-ENTRY attrib → setHelpEntry; writer setMultiLanguageParagraphs: writeARObject → writePaginateable + HELP-ENTRY attrib; matched set/get pairs (Rule 0013.2); pre-existing test_writer_documentation_block.py addL1 element type corrected LOverviewParagraph → LParagraph (l1 retype hygiene); 7 focused tests passed]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.4, p.290 (verified via pdf_page.py); 5 method rows (init + 2 accessor pairs) with 6 columns + release R23-11 written at Step 3; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none remaining: all four Step-1 src deviations were FIXED during this sync and per Rule 0014 no rows are kept — (1) base VariationPointCapable removed (spec Base wins, Rule 0001.2), (2) l1 retyped LLongName → LParagraph (spec type wins), (3) missing helpEntry added, (4) addL1 None-append fixed to no-op; accepted handling notes: XSD generated VARIATION-POINT element (atpVariation, Applicable for DocumentationBlock.p) not modeled per Rule 0015 PDF-Base-wins, consistent with the stamped Paginateable family (Table/Tgroup/SlParagraph model no VP); l1 pureMM minOccurs=1 vs XSD element minOccurs=0 → list defaults [] (uniform-optional family handling); Step-3 referenced classes all stamped: LParagraph ✓ Paginateable ✓ DocumentViewSelectable ✓]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9,032 unit + integration round-trips pass; flake8/ruff/black-check clean (ruff I001 import order fixed in the new writer test); set-based checklist==methods exact match in order; 9b: user-confirmed base collapse to (Paginateable) with VariationPointCapable removal, l1 retype LLongName→LParagraph, added helpEntry with XSD HELP-ENTRY coverage, addL1 None no-op, verbatim docstrings incl. spec typo "partiucular", reader+writer mixin coverage (SI/VIEW/BREAK/KEEP/HELP-ENTRY) with single readARObject, member order, Rule 0015 VP arbitration, package location, no remaining deviations; marker `# Spec verified: R23-11` written]
> **Dependency audit 2026-09-16 (`Area` closure)** (run at the start of the `Area` row — the 2026-09-11
> missing-class audit queued `Area` but missed its two enum member types):
> - **Added 2 missing dependency rows**: `AreaEnumNohref` (Table 9.18, p.301) and `AreaEnumShape`
>   (Table 9.19, p.302) — both NOT in src (grep of src/ and tests/); member types of `Area.nohref` /
>   `Area.shape` → queued immediately **before** `Area` (Rule 0016.5 dependency-first; a dependent must
>   never precede its member type, or Step 3 would fabricate the type — Rule 0001.10).
> - Same class of miss as the 2026-09-11 `GraphicNotationEnum` audit (Graphic's member-type enum).
> - XSD cross-check: `AREA-ENUM-NOHREF--SIMPLE` (line 131467; literal NOHREF, index 0) and
>   `AREA-ENUM-SHAPE--SIMPLE` (line 131484; CIRCLE/DEFAULT/POLY/RECT, indices 0-3); `NOHREF`/`SHAPE`
>   are XML attributes on the AREA attributeGroup (lines 5873/5978).
> - `Area` itself (Table 9.17, p.301): 22 attrs (accesskey/alt/class/coords/href/nohref/onblur/onclick/
>   ondblclick/onfocus/onkeydown/onkeypress/onkeyup/onmousedown/onmousemove/onmouseout/onmouseover/
>   onmouseup/shape/style/tabindex/title, all 0..1 xml.attribute=true; String except the two enums),
>   Base `ARObject`, Package M2::MSR::Documentation::BlockElements::Figure → `Figure.py`.
> - Dependency closure of the enums otherwise clear (AREnum → ARObject base); primitives not queued.
>
- [x] `AreaEnumNohref` (dependency · **added 2026-09-16 Area dependency audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.18, p.301 · **NOT in src — created** · Package M2::MSR::Documentation::BlockElements::Figure → `Figure.py` · AREnum; literal nohref (XSD NOHREF) index 0 · aggregated by `Area.nohref` · queued dependency-first per Rule 0016.5) — verified R23-11 (commit 1d6f8c0a)
  - [x] Step 1 — Sync members & description from spec  [Table 9.18 markdown (trailing-caption render after the Area class table) + pdf_page.py p.301 confirmed; Enumeration AreaEnumNohref; Package M2::MSR::Documentation::BlockElements::Figure → Figure.py (after GraphicNotationEnum); Note = "This enumerator specifies the fact that the area has no reference."; Aggregated by Area.nohref; 1 literal: nohref = XSD NOHREF index 0, doc "This indicates that the area has no active link." + Tags atp.EnumerationLiteralIndex=0; XSD AREA-ENUM-NOHREF complexType line 131455 (simpleContent extension of --SIMPLE + AR-OBJECT attributeGroup → ARLiteral-style enum value form), --SIMPLE line 131467; serialized as the NOHREF attribute on Area — NOHREF attribute coverage belongs to the Area row]
  - [x] Step 2 — Write model class unit test (Red)  [TestAreaEnumNohref appended to test_Figure.py: initialization, 1 spec literal NOHREF with XSD value + getEnumValues, setValue/getValue round-trip, validateEnumValue accept/reject; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [AreaEnumNohref(AREnum) added to Figure.py after GraphicNotationEnum; no-arg __init__ registering (NOHREF,); literal const NOHREF = XSD value NOHREF index 0; 37 passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [brand-new class — class docstring = Table 9.18 Note verbatim ("...the area has no reference."); NOHREF literal comment = literal description verbatim + EnumerationLiteralIndex tag; byte-diff script verified both surfaces]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — no own XML element; serialized as the NOHREF attribute on Area; coverage belongs to the Area row (queued below)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: see Step 5]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.18, p.301 (pdf_page.py verified); (no methods) enum-form checklist with __init__ row, 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: 1 spec literal nohref → NOHREF index 0 matches XSD AREA-ENUM-NOHREF--SIMPLE (line 131467); AREnum modeled per Rule 0001.10 enum path — no attributes, no fabricated members; reader/writer N/A (standalone enum, serialized as the NOHREF attribute on Area — coverage belongs to the Area row); docstrings byte-verbatim from Table 9.18; no missing referenced classes (AREnum → ARObject base, both in src)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 9,036 unit + integration round-trips pass; flake8/ruff/black-check clean; checklist==methods exact; XSD cross-check NOHREF index 0; docstrings byte-verbatim; 9b: re-confirmed on main after PR #730 merge (full suite + 37 Figure tests + lint + black green), user-confirmed the 14-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `AreaEnumShape` (dependency · **added 2026-09-16 Area dependency audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.19, p.302 · **NOT in src — created** · Package M2::MSR::Documentation::BlockElements::Figure → `Figure.py` · AREnum; literals circle/default/poly/rect (XSD CIRCLE/DEFAULT/POLY/RECT) indices 0-3 · aggregated by `Area.shape` · queued dependency-first per Rule 0016.5) — verified R23-11 (commit 966320f6)
  - [x] Step 1 — Sync members & description from spec  [Table 9.19 markdown (trailing-caption render; Package/Note/Aggregated-by rows at L7855-7860, literal rows L7868-7875) + pdf_page.py p.302 confirmed; Enumeration AreaEnumShape; Package M2::MSR::Documentation::BlockElements::Figure → Figure.py (after AreaEnumNohref); Note = "This enumerator specifies the shape of the area."; Aggregated by Area.shape; 4 literals circle/default/poly/rect = XSD CIRCLE/DEFAULT/POLY/RECT indices 0-3 with verbatim descriptions; XSD AREA-ENUM-SHAPE--SIMPLE line 131489 (audit note said 131484 — corrected); serialized as the SHAPE attribute on Area — SHAPE attribute coverage belongs to the Area row]
  - [x] Step 2 — Write model class unit test (Red)  [TestAreaEnumShape appended to test_Figure.py: initialization, 4 spec literals with XSD values + getEnumValues, setValue/getValue round-trip, validateEnumValue accept/reject; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [AreaEnumShape(AREnum) added to Figure.py after AreaEnumNohref; no-arg __init__ registering all 4 XSD values; literal consts CIRCLE/DEFAULT/POLY/RECT; 41 Figure tests passed; armodel.AreaEnumShape resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [brand-new class — class docstring = Table 9.19 Note verbatim; 4 literal comments = literal descriptions verbatim + EnumerationLiteralIndex tags; byte-diff script verified all 5 surfaces]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: standalone AREnum — no own XML element; serialized as the SHAPE attribute on Area; coverage belongs to the Area row (queued below)]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: see Step 5]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.19, p.302 (pdf_page.py verified); (no methods) enum-form checklist with __init__ row, 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: 4 spec literals circle/default/poly/rect → XSD CIRCLE/DEFAULT/POLY/RECT indices 0-3 match AREA-ENUM-SHAPE--SIMPLE (line 131489); AREnum modeled per Rule 0001.10 enum path — no attributes, no fabricated members; reader/writer N/A (standalone enum, serialized as the SHAPE attribute on Area — coverage belongs to the Area row); docstrings byte-verbatim from Table 9.19; no missing referenced classes (AREnum → ARObject base, both in src)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 8991 unit + full suite incl. integration round-trips pass; flake8/ruff/black-check clean; checklist==methods exact; XSD cross-check indices 0-3; docstrings byte-verbatim; 9b: user-confirmed the pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `Area` (dependency · **added 2026-09-11 missing-class audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.17, p.301 · member type of `Map.area` · **NOT in src — created** · 22 attrs (see 2026-09-16 audit note) · Base `ARObject` · deps `AreaEnumNohref` + `AreaEnumShape` queued immediately above) — verified R23-11 (commit c9f24649)
  - [x] Step 1 — Sync members & description from spec  [Table 9.17 markdown L7797-7843 (3-page-split render) + pdf_page.py p.301 confirmed; Class Area; Package M2::MSR::Documentation::BlockElements::Figure → Figure.py; Base ARObject; Aggregated by Map.area; Note = "This element specifies a region in an image map. … For more details refer to the specification of HTML." (paragraph-joined); 22 attrs in displayed order accesskey/alt/class/coords/href/nohref/onblur/onclick/ondblclick/onfocus/onkeydown/onkeypress/onkeyup/onmousedown/onmousemove/onmouseout/onmouseover/onmouseup/shape/style/tabindex/title — 20 String + nohref AreaEnumNohref + shape AreaEnumShape, all 0..1 xml.attribute=true; XSD AREA complexType line 6006 (sequence AR-OBJECT + AREA group (empty), attributeGroups AR-OBJECT + AREA) + AREA attributeGroup line 5836 with all 22 attributes confirmed; onblur note garbled in markdown render (orphaned "away") → XSD wording "switched away from an element" used]
  - [x] Step 2 — Write model class unit test (Red)  [TestArea in test_Figure.py: initialization (22 getters None), 20 String attrs set/get chaining + None no-op via typed String().setValue(), nohref/shape enum set/get + None no-op; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [Area(ARObject) added to Figure.py between AreaEnumShape and Graphic (eager annotations require member types first; spec-row order preserved otherwise); 22 typed optional members PEP 526 in spec row order; field `class_` for the Python keyword `class` (accessors keep spec name getClass/setClass — Paginateable break precedent); 44 accessors with None no-op + chaining; 45 Figure tests passed; armodel.Area resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [brand-new class — class docstring = Table 9.17 Note verbatim (paragraph-joined); all 22 inline comments + getter docstrings + setter docstrings (incl. None-no-op sentence) byte-diffed verbatim; spec quirks kept: ondblclick Note says "The ONCLICK-Event…", onkeydown "…performed in the event." lowercase; script-verified]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_area.py (3: full 22 attrs incl. S/T, enum values NOHREF/CIRCLE, missing → None) + tests/test_armodel/writer/test_area.py (4: full 22 attribs, empty → no attribs, None no-op, write→read roundtrip asserting field values); 7 failed = Red (getArea/setArea missing)]
  - [x] Step 6 — Update parser & writer (Green)  [parser getArea = readARObject + 22 typed attribute reads in XSD attributeGroup order (Url precedent — no double read); writer setArea = writeARObject + 22 attrib writes; imports added to both (Area/AreaEnumNohref/AreaEnumShape in parser; Area only in writer — enums consumed via getValue, ruff F401 fix); 7 focused tests passed]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.17, p.301 (pdf_page.py verified); 45 rows (init + 22 getter/setter pairs) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: all 22 PDF attrs modeled with PDF types (20 String, 1 AreaEnumNohref, 1 AreaEnumShape), names verbatim (class_ = Python keyword accommodation), reader+writer coverage for every member, no missing referenced classes (both enums stamped); Map.area aggregation wiring (unbounded 1..*) stays deferred to the Map row queued next; 9a caught ruff F401 (unused enum imports in writer) — fixed before 9b]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 9,060 tests + integration round-trips pass; flake8/ruff/black-check clean (black reflowed 1 file); set-based checklist==methods (45 rows = __init__ + 44 accessors); docstrings byte-verbatim re-verified post-black; 9b: user-confirmed the 11-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `Map` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.23 · after `Area` (aggr `area`) — Area NOT in src, pending 16.4 below) — verified R23-11 (commit 43ec8ade)
  - [x] Step 1 — Sync members & description from spec  [Table 9.23 markdown TWO-PAGE-SPLIT render: fragment 1 L7968-7979 (header + area/class/name/onclick/ondblclick) ends with the caption at L7987, **fragment 2 (L7989-7999) appears AFTER the caption** with 9 more attrs onkeydown/onkeypress/onkeyup/onmousedown/onmousemove/onmouseout/onmouseover/onmouseup/title — initially missed, caught mid-sync (user flagged the multi-page fragment pattern); full displayed order = 14 attrs: area (Area 1..* aggr) + 13 attrs (class String/name NameToken/onclick/ondblclick/…/title String); pdf_page.py p.306; Base ARObject; Aggregated by LGraphic.map; Note paragraph-joined; XSD MAP attributeGroup (line 79704) confirms all 13 non-aggr attrs in order + STYLE (atp.Status="removed") → not modeled per Rule 0015; XSD MAP group = AREA unbounded (pureMM 1..*, sequenceOffset=20); MAP complexType line 79813 = sequence AR-OBJECT + MAP groups]
  - [x] Step 2 — Write model class unit test (Red)  [TestMap rewritten spec-driven in test_Figure.py: initialization (areas [] + 13 attrs None), addArea append/insertion-order/chaining, class/name/onclick/ondblclick set/get chaining + None no-op, page-split-fragment attrs (9) set/get + None no-op; 6 failed = Red]
  - [x] Step 3 — Implement model class (Green)  [stub replaced in place in Figure.py (stale docstring/checklist wiped, Rule 0012.2.3); `areas: List[Area]` typed list + addArea/getAreas (non-Referrable 1..* aggr, Rule 0001.6/0004); 13 typed attr members in spec row order; field `class_` (keyword accommodation, accessors keep getClass/setClass); 9 page-split attrs added mid-sync after the fragment-2 discovery; 50 Figure tests passed]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring = Table 9.23 Note verbatim (paragraph-joined); all 13 inline comments + getter/setter docstrings byte-diffed verbatim; spec quirks kept: Map.onclick "clicked on" (no hyphen, differs from Area.onclick "clicked-on"), ondblclick "the current Event", onkeydown lowercase "the event", name Note carries no Tags tail; area Note keeps the full roleElement/sequenceOffset Tags tail]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_map.py (3: full MAP incl. S/T + 13 attrs + 2 ordered AREA children value-asserting, empty → no areas/attrs, missing → None) + tests/test_armodel/writer/test_map.py (4: full write, empty omits, None no-op, write→read roundtrip); 7 failed = Red (getMap/setMap missing)]
  - [x] Step 6 — Update parser & writer (Green)  [parser readArea/getArea (from the Area row) refactored + readMap/getMap = readARObject + findall AREA → readArea + addArea + 13 attrib reads in XSD attributeGroup order; writer writeArea/setArea refactored + writeMap/setMap = writeARObject + ordered AREA children via writeArea + 13 attrib writes; imports added (Map in parser + writer); 64 focused tests passed (Map+Area+Figure)]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.23, p.306 (pdf_page.py verified); 29 rows (init + addArea + getAreas + 13 getter/setter pairs) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [fixed mid-sync per Rule 0014: initial extraction stopped at the `Table 9.23: Map` caption and missed the page-split fragment 2 (9 attrs) rendered AFTER the caption — user flagged the multi-fragment pattern; all 9 attrs added to model/tests/checklist/parser/writer before 9b; none remaining: 14 PDF attrs ↔ 14 fields (13 attrs + area list), XSD-only removed STYLE not modeled (Rule 0015), LGraphic.map dispatch wiring stays deferred to the LGraphic row queued next]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 9,073 tests + integration round-trips pass; flake8/ruff/black-check clean (fixed ruff I001 duplicate import + black reflow); set-based checklist==methods (29 rows = __init__ + 28 own accessors, inherited ARObject methods excluded); docstrings byte-verbatim re-verified post-black; 9b: user-confirmed the 10-item pre-stamp checklist incl. the page-split fix; marker `# Spec verified: R23-11` written]
- [x] `LGraphic` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.25 · after `Graphic` (aggr `graphic`) + `Map` (aggr `map`) · parent `LanguageSpecific` stamped ✓ · *(existing member)*) — verified R23-11 (commit e4b1acf6)
  - [x] Step 1 — Sync members & description from spec  [Table 9.25 (p.308 via pdf_page.py) is a page-split render: header fragment (Package/Note/Base/Aggregated-by + attr `graphic` seqOffset=20) BEFORE the caption, fragment 2 (`map` Map 0..1 aggr seqOffset=30) after it — same multi-fragment pattern as Map; full displayed order = 2 attrs: graphic, map; Base `ARObject , LanguageSpecific` → most-derived LanguageSpecific (current base correct); Package Figure → Figure.py; Note "This meta-class represents the figure in one particular language."; XSD L-GRAPHIC complexType line 76173 = sequence AR-OBJECT + LANGUAGE-SPECIFIC + L-GRAPHIC groups (GRAPHIC + MAP children, both minOccurs=0 → uniform-optional Optional modeling, matches current; S/T + L attributes); src deviations found: (1) graphic/map members use trailing `# type:` comments (Rule 0003) → PEP 526; (2) getMap/setMap reader/writer unwired in BOTH MlFigure (readMlFigureLGraphics/writeMlFigureLGraphics) and MlFormula (getMlFormula inline loop) paths — recorded as the Deviation row in Formula.py's checklist; (3) getter docstrings carry extra "Returns:" paraphrase (not Note-verbatim); (4) checklist stale 5-column format, no release column]
  - [x] Step 2 — Write model class unit test (Red)  [TestLGraphic rewritten spec-driven in test_Figure.py: base-chain (issubclass LanguageSpecific + ARObject), initialization (l/graphic/map None), graphic + map get/set with chaining + None no-op, docstring-verbatim test (inspect.cleandoc vs Table 9.25 Note for class docstring + both getters, Note+no-op prefix for both setters); 1 failed (getter docstrings carry extra "Returns:" paraphrase) = Red]
  - [x] Step 3 — Implement model class (Green)  [PEP 526 annotations added: `self.graphic: Optional[Graphic] = None` and `self.map: Optional[Map] = None` (were trailing `# type:` comments, Rule 0003 fix); accessors/setters already correct (None no-op + chaining, spec names verbatim); 52 Figure tests pass — the docstring-verbatim test stays Red until the Step 4 wipe+rewrite]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [getter docstrings wiped of the "Returns:" paraphrase → Note verbatim only (Map-family convention); setter docstrings = Note verbatim + None-no-op sentence + `Returns: self for method chaining`; class docstring + inline __init__ comments already byte-verbatim; 53 Figure tests pass incl. the docstring-verbatim test]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_l_graphic.py (3: L/S/T + GRAPHIC + MAP value-asserting, empty → all None, missing → None) + tests/test_armodel/writer/test_l_graphic.py (4: full write incl. L attrib + GRAPHIC-before-MAP XSD order, empty omits, None no-op, write→read roundtrip); 7 failed = Red (getLGraphic/setLGraphic missing)]
  - [x] Step 6 — Update parser & writer (Green)  [parser readLGraphic = readARObject + L attrib + GRAPHIC (getGraphic) + MAP (getMap) in XSD sequenceOffset order, getLGraphic = find → LGraphic() + readLGraphic; readMlFigureLGraphics + the getMlFormula L-GRAPHIC loop refactored to call readLGraphic (no duplicated inline logic); writer writeLGraphic = writeARObject + L attrib + setGraphic + setMap, setLGraphic = SubElement + writeLGraphic; writeMlFigureLGraphics + the setMlFormula loop refactored to call writeLGraphic/setLGraphic; LGraphic import added to writer; Formula.py Deviation row ("LGraphic.map reader/writer not wired") REMOVED — resolved by this wiring; 195 affected parser/writer tests pass]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.25, p.308 (pdf_page.py verified); 5 method rows (init + 2 getter/setter pairs) with 6 columns + release R23-11; getMap/setMap reader/writer flipped [x] (coverage now in readLGraphic/writeLGraphic); note added that the inherited L attribute is covered by the concrete helpers; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none remaining — all four Step-1 findings were FIXED this pass and per Rule 0014 no rows are kept: (1) `# type:` comments → PEP 526 annotations (Rule 0003), (2) LGraphic.map reader/writer wired in both MlFigure and MlFormula paths and the Formula.py Deviation row removed, (3) getter docstring "Returns:" paraphrase wiped → Note verbatim (Rule 0001.4), (4) checklist upgraded to 6-column format with release column; graphic Mult 1 vs XSD minOccurs=0 → uniform-optional Optional modeling, same accepted handling as Table.float/TraceableTable.table (non-blocking note)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 9,084 tests + integration round-trips pass; flake8/ruff/black-check clean; set-based checklist==methods (5 rows); 9b: user-confirmed the 10-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `MlFigure` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.24 · after `DocumentViewSelectable`+`Paginateable` (parents) + `LGraphic` (aggr `lGraphic`) · deps stamped: `figureCaption` Caption ✓ / `verbatim` MultiLanguageVerbatim ✓) — verified R23-11 (commit 9225ed15)
  - [x] Step 1 — Sync members & description from spec  [Table 9.24 markdown L8003-8017 (single fragment, all 6 attr rows BEFORE the caption) + pdf_page.py p.307; Class MlFigure; Package Figure → Figure.py; Note "This metaclass represents the ability to embed a figure." (metaclass one word); Base `ARObject , DocumentViewSelectable , Paginateable` → most-derived Paginateable (same collapse as stamped Table/MultiLanguageParagraph); Aggregated by DocumentationBlock.figure; 6 attrs displayed order: figureCaption (Caption 0..1 aggr, no Tags), frame (FrameEnum 0..1 attr), helpEntry (String 0..1 attr), lGraphic (LGraphic * aggr, Tags xml.roleWrapperElement=false xml.sequenceOffset=30), pgwide (PgwideEnum 0..1 attr, spec typo "wether"), verbatim (MultiLanguageVerbatim 0..1 aggr, seqOffset=50, XSD adds the constr_2638 VP sentence to the element doc); XSD ML-FIGURE complexType line 81642 = sequence AR-OBJECT + DOCUMENT-VIEW-SELECTABLE + PAGINATEABLE + ML-FIGURE groups; element group = FIGURE-CAPTION → choice L-GRAPHIC unbounded → VERBATIM → generated VARIATION-POINT (atpVariation, Applicable for DocumentationBlock.figure — Rule 0015 PDF-Base-wins, NOT modeled, Paginateable family precedent); attributeGroup = FRAME/HELP-ENTRY/PGWIDE; **src deviations found**: (1) base `(Paginateable, VariationPointCapable)` — spec Base has NO VariationPointCapable → fix to `(Paginateable)` (mirrors MultiLanguageParagraph row); (2) `frame` FrameEnum member missing entirely; (3) all 5 members use trailing `# type:` comments (Rule 0003) → PEP 526; (4) class docstring is a paraphrase, no member docstrings; (5) reader readMlFigure = readPaginateable + readMlFigureLGraphics only — FIGURE-CAPTION/FRAME/HELP-ENTRY/PGWIDE/VERBATIM unwired; writer same; (6) checklist stale 4-column stub without # Spec line; imports verified cycle-free: FrameEnum/PgwideEnum (OasisExchangeTable — imports only ArObject/PrimitiveTypes/PaginationAndView), MultiLanguageVerbatim (MultilanguageData — no Figure import), Caption (defined in BlockElements/__init__.py, does not import .Figure — Formula.py precedent)]
  - [x] Step 2 — Write model class unit test (Red)  [TestMlFigure rewritten spec-driven in test_Figure.py: base-chain (issubclass Paginateable + DocumentViewSelectable, NOT VariationPointCapable), initialization (figureCaption/frame/helpEntry None, lGraphics [], pgwide/verbatim None), figureCaption/frame/helpEntry/pgwide/verbatim set/get with typed primitives + chaining + None no-op, lGraphics add/get with insertion order + None no-op, docstring-verbatim test (inspect.cleandoc vs Table 9.24 Note); 5 failed (VP base assertion, missing frame AttributeError, paraphrase docstring, bare-str caption, init frame attr) = Red]
  - [x] Step 3 — Implement model class (Green)  [base fixed to `(Paginateable)` — VariationPointCapable removed (spec Base wins, Rule 0001.2; import dropped, no other user in Figure.py); `frame: Optional[FrameEnum]` + setFrame/getFrame added; all 6 members PEP 526 annotated in spec row order (figureCaption/frame/helpEntry/lGraphics/pgwide/verbatim); imports added (Caption from BlockElements __init__ — Formula.py precedent, no cycle; FrameEnum/PgwideEnum from OasisExchangeTable; MultiLanguageVerbatim from MultilanguageData); test-side fixes: DocumentViewSelectable imported from PaginationAndView, Caption needs (parent, short_name); 56 Figure tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [full-class rewrite wiped the stale paraphrase docstring + stub checklist (Rule 0012.2.3); class docstring = Table 9.24 Note verbatim ("This metaclass represents the ability to embed a figure." — metaclass one word); all 6 inline __init__ comments + getter docstrings + setter docstrings (incl. None-no-op sentence) = attr Note verbatim incl. spec typo "wether" and the "PRE in HTML ." trailing-space quirk; __init__ has no docstring (Rule 0012.2.4)]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_ml_figure.py (3: full FIGURE with S/T + SI/VIEW/BREAK/KEEP-WITH-PREVIOUS + FRAME/HELP-ENTRY/PGWIDE attribs + FIGURE-CAPTION SHORT-NAME + L-GRAPHIC + VERBATIM ALLOWBREAK/L-5 value-asserting, minimal → defaults, missing → []) + tests/test_armodel/writer/test_ml_figure.py (3: full write incl. XSD ML-FIGURE group order [FIGURE-CAPTION, L-GRAPHIC, VERBATIM] + attrib asserts, empty omits, write→read roundtrip); 3 failed = Red (FRAME/HELP-ENTRY/PGWIDE/FIGURE-CAPTION/VERBATIM unwired)]
  - [x] Step 6 — Update parser & writer (Green)  [parser readMlFigure = readPaginateable + FRAME/HELP-ENTRY/PGWIDE attrib reads (XSD attributeGroup order) + setFigureCaption(getCaption "FIGURE-CAPTION") + readMlFigureLGraphics + setVerbatim(getMultiLanguageVerbatim "VERBATIM") — reuses the stamped Caption/MultiLanguageVerbatim/LGraphic helpers, no new readers; writer writeMlFigure = writePaginateable + FRAME/HELP-ENTRY/PGWIDE attrib writes + setCaption + writeMlFigureLGraphics + setMultiLanguageVerbatim in XSD ML-FIGURE group order; all imports already present in both layers; 6 focused + 241 affected tests pass]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.24, p.307 (pdf_page.py verified); 13 method rows (init + 6 accessor pairs: get/setFigureCaption, get/setFrame, get/setHelpEntry, getLGraphics/addLGraphics, get/setPgwide, get/setVerbatim) with 6 columns + release R23-11, written during the Step 3 full-class rewrite; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none remaining — all six Step-1 findings FIXED this pass, per Rule 0014 no rows kept: (1) base VP removed, (2) frame member added, (3) PEP 526 annotations, (4) docstrings wiped/rewritten verbatim, (5) reader/writer wired for all 6 members, (6) checklist rewritten to 6-column format; accepted handling notes: XSD generated VARIATION-POINT element (atpVariation, Applicable for DocumentationBlock.figure) not modeled per Rule 0015 PDF-Base-wins, consistent with the Paginateable family (Table/MultiLanguageParagraph precedent); verbatim XSD element doc carries the constr_2638 VP sentence — PDF/markdown Note authoritative, no value field affected; lGraphic pureMM wrapperElement=false → direct L-GRAPHIC children under FIGURE (readMlFigureLGraphics, already existing), not a wrapper list; Step-3 referenced classes all stamped: Caption ✓, FrameEnum ✓, PgwideEnum ✓, MultiLanguageVerbatim ✓, LGraphic ✓]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 9,093 tests + integration round-trips pass; flake8/ruff/black-check clean (black reflowed 1 file); checklist==methods (13 rows = __init__ + 12 own accessors); docstrings byte-verbatim re-verified post-black; 9b: user-confirmed the 11-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `MsrQueryResultChapter` (dependency · **added 2026-09-11 missing-class audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.87 · member type of `MsrQueryChapter.msrQueryResultChapter` · **NOT in src** — class must be created when this row is synced) — verified R23-11 (commit fb505d35)
  - [x] Step 1 — Sync members & description from spec  [Table 9.87 (p.345 via pdf_page.py) is a page-split render: header fragment L9176-9182 (Class/Package/Note/Base/Aggregated-by/Attribute header, NO attr rows) BEFORE the caption, fragment 2 (L9194, after the caption) has the 1 attr — same multi-fragment pattern as Map/LGraphic; Class MsrQueryResultChapter; Package M2::MSR::Documentation::MsrQuery → MsrQuery.py (MsrQueryProps/MsrQueryArg already there); Note "This metaclass represents the result of an msrquery which is a set of chapters."; Base ARObject → most-derived ARObject; Aggregated by MsrQueryChapter.msrQueryResultChapter; 1 attr: chapter (ordered) — Chapter * aggr, Tags xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false; XSD MSR-QUERY-RESULT-CHAPTER group line 83479 = CHAPTER unbounded minOccurs=0 (pureMM.isOrdered=true, seqOffset=20, element doc adds the constr_2638 VP sentence), complexType line 83496 = sequence AR-OBJECT + group, attributeGroups AR-OBJECT only (S/T attrs); shape per family precedent (MsrQueryProps.addMsrQueryArg/getMsrQueryArgs, ChapterOrMsrQuery.addChapter/getChapters): `chapters: List[Chapter]` + addChapter(value) None-no-op append + getChapters() — Chapter is Referrable-derived but * aggr family uses add-append; import cycle: Chapters.py imports MsrQueryP1 from MsrQuery.py at runtime → Chapter via TYPE_CHECKING (file's existing pattern, future-annotations)]
  - [x] Step 2 — Write model class unit test (Red)  [TestMsrQueryResultChapter appended to test_MsrQuery.py: initialization (chapters []), addChapter with insertion order + None no-op (Chapter(None, name) fixtures); ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [MsrQueryResultChapter(ARObject) appended to MsrQuery.py (after MsrQueryP2; file order not spec-governed, member order is); `chapters: List[Chapter]` typed list (PEP 526) + addChapter (None-no-op append, family precedent MsrQueryProps.addMsrQueryArg/ChapterOrMsrQuery.addChapter) + getChapters; Chapter imported DIRECTLY at runtime (user-directed 9b fix round, TraceableTable precedent): the only runtime cycle edge was Chapters.py's annotation-only MsrQueryP1 import (future-annotations make its annotations lazy) → moved into Chapters.py's existing TYPE_CHECKING block, so MsrQuery.py's runtime `from Chapters import Chapter` is cycle-free in BOTH load orders — verified; no quoted forward-reference remains; exported via the module wildcard chain — `armodel.MsrQueryResultChapter` resolves]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [brand-new class — class docstring = Table 9.87 Note verbatim ("This metaclass represents the result of an msrquery which is a set of chapters." — metaclass one word); chapters inline comment + addChapter + getChapters docstrings = attr Note verbatim incl. the full roleElement/roleWrapperElement/sequenceOffset/typeElement/typeWrapperElement Tags tail; __init__ no docstring (Rule 0012.2.4)]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_msr_query_result_chapter.py (3: S/T + 2 ordered CHAPTER children value-asserting incl. HELP-ENTRY, empty → object with [], missing → None) + tests/test_armodel/writer/test_msr_query_result_chapter.py (4: full write w/ ordered CHAPTER SHORT-NAMEs, empty omits, None no-op, write→read roundtrip); 7 failed = Red (getMsrQueryResultChapter/setMsrQueryResultChapter missing)]
  - [x] Step 6 — Update parser & writer (Green)  [parser readMsrQueryResultChapter = readARObject + findall CHAPTER → readChapter(child, parent) + addChapter (ordered per pureMM.isOrdered, insertion order preserved); getMsrQueryResultChapter = find → MsrQueryResultChapter() + readMsrQueryResultChapter (result passed as both parent and target — chapters' parent is their container); writer setMsrQueryResultChapter = SubElement + writeARObject + ordered CHAPTER children via writeChapter(tag_name="CHAPTER"); MsrQueryResultChapter added to both import lines; test fixture fix: HELP-ENTRY is a CHAPTER attribute not a child; 7 focused tests pass]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.87, p.345 (pdf_page.py verified); 3 method rows (init + addChapter + getChapters) with 6 columns + release R23-11, written at Step 3; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: 1 spec attr `chapter (ordered)` (Chapter * aggr) modeled as `chapters: List[Chapter]` + addChapter/getChapters (family precedent ChapterOrMsrQuery.addChapter/getChapters, MsrQueryProps.addMsrQueryArg); XSD CHAPTER minOccurs=0 unbounded → list defaults [] (uniform-optional family handling); XSD element doc's constr_2638 VP sentence is XSD-only text — PDF/markdown Note authoritative; S/T attrs covered by readARObject/writeARObject; consumer MsrQueryChapter.msrQueryResultChapter wiring stays deferred to the MsrQueryChapter stub row (queued next); no missing referenced classes (Chapter ✓ stamped); test-side only: HELP-ENTRY attribute form fixed]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 9,102 tests + integration round-trips pass; flake8/ruff/black-check clean (black reflowed 1 file); checklist==methods (3 rows); docstrings byte-verbatim re-verified post-black; 9b fix round: user asked whether the quoted `List["Chapter"]` was necessary — analysis showed the only runtime cycle edge was Chapters.py's annotation-only MsrQueryP1 import; moved to TYPE_CHECKING (lazy annotations) and Chapter is now a direct runtime import with unquoted `List[Chapter]` (TraceableTable precedent); both import orders verified; full suite re-run green; 9b: user-confirmed the 11-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `MsrQueryChapter` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.84 · after `DocumentViewSelectable`+`Paginateable` (parents) · deps: `msrQueryProps` MsrQueryProps stamped ✓ / `msrQueryResultChapter` NOT in src — pending 16.4 below) — verified R23-11 (commit 50103018)
  - [x] Step 1 — Sync members & description from spec  [Table 9.84 markdown L9133-9143 (single fragment, both attr rows BEFORE the caption) + pdf_page.py p.343; Class MsrQueryChapter; Package M2::MSR::Documentation::MsrQuery → MsrQuery.py (existing stub); Note "This meta-class represents the ability to express a query which yields a set of chapters as a result." (meta-class two words — differs from the result classes' "metaclass"); Base `ARObject , DocumentViewSelectable , Paginateable` → most-derived Paginateable (same collapse as Table/MlFigure); Aggregated by ChapterOrMsrQuery.msrQueryChapter; 2 attrs displayed order: msrQueryProps (MsrQueryProps 1 aggr, "This is argument and properties of the chapter query. Tags: xml.sequenceOffset=20"), msrQueryResultChapter (markdown cell renders the name line-wrapped as "msrQueryResult Chapter" — render artifact, actual name msrQueryResultChapter; MsrQueryResultChapter 0..1 aggr, "This represents the result of the query. Tags: xml.sequenceOffset=30"); XSD MSR-QUERY-CHAPTER group line 83325 = MSR-QUERY-PROPS (seqOffset=20) → MSR-QUERY-RESULT-CHAPTER (seqOffset=30), complexType line 83347 = sequence AR-OBJECT + DOCUMENT-VIEW-SELECTABLE + PAGINATEABLE + MSR-QUERY-CHAPTER groups, attributeGroups AR-OBJECT/DOCUMENT-VIEW-SELECTABLE/PAGINATEABLE (S/T + SI/VIEW + BREAK/KEEP-WITH-PREVIOUS); **src deviations found (stamped-row Rule 0001.10 deferred-placeholder stub)**: (1) base `ARObject` — spec Base has the mixin chain → fix to `(Paginateable)`; (2) `msrQueryResultChapter` member deferred in the stub (MsrQueryResultChapter now stamped ✓) → add `Optional[MsrQueryResultChapter]` + get/set (MsrQueryResultChapter is ARObject-derived → non-Referrable → set/get, Rule 0001.6); (3) setter/getter docstrings are stale paraphrase blocks (standalone None-no-op paragraph + Returns on getter) → Note-verbatim rewrite; (4) checklist stale 5-column format; (5) reader readMsrQueryChapter = readARObject + MSR-QUERY-PROPS only — no PAGINATEABLE/SI/VIEW/BREAK/KEEP coverage, no MSR-QUERY-RESULT-CHAPTER; writer same. Import: Paginateable from BlockElements.PaginationAndView (no cycle — PaginationAndView imports only ArObject/PrimitiveTypes); MsrQueryResultChapter is in the same file]
  - [x] Step 2 — Write model class unit test (Red)  [TestMsrQueryChapter appended to test_MsrQuery.py: base-chain (issubclass Paginateable + DocumentViewSelectable, NOT VariationPointCapable), initialization (msrQueryProps/msrQueryResultChapter None), msrQueryProps + msrQueryResultChapter set/get with chaining + None no-op; 4 failed = Red]
  - [x] Step 3 — Implement model class (Green)  [base `ARObject` → `(Paginateable)` (spec Base wins, Rule 0001.2; Paginateable runtime import added — no cycle, both load orders verified); `msrQueryResultChapter: Optional[MsrQueryResultChapter]` + setMsrQueryResultChapter/getMsrQueryResultChapter added (stub's deferred-placeholder NOTE removed — the real class landed last session); both members PEP 526 in spec row order (msrQueryProps, msrQueryResultChapter); test-side fix: MsrQueryChapter added to the test import line; 16 MsrQuery tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [full-class rewrite wiped the stale paraphrase blocks (Rule 0012.2.3): setter docstrings = Note verbatim + None-no-op sentence appended inline + `Returns: self for method chaining`; getter docstrings = Note verbatim only (no Returns paraphrase); inline __init__ comments = attr Note verbatim incl. the `Tags: xml.sequenceOffset=20/30` tails; class docstring already byte-verbatim ("meta-class" two words); __init__ no docstring (Rule 0012.2.4)]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new tests/test_armodel/parser/test_msr_query_chapter.py (2: full MSR-QUERY-CHAPTER with S/T + SI/VIEW/BREAK/KEEP-WITH-PREVIOUS + MSR-QUERY-PROPS/MSR-QUERY-NAME + MSR-QUERY-RESULT-CHAPTER/CHAPTER value-asserting, minimal → both None) + tests/test_armodel/writer/test_msr_query_chapter.py (3: full write incl. XSD MSR-QUERY-CHAPTER group order [MSR-QUERY-PROPS, MSR-QUERY-RESULT-CHAPTER], empty omits, write→read roundtrip); test fixture fix: namespace-aware parser.find (plain element.find misses namespaced tags); 3 failed = Red (SI/VIEW/BREAK/KEEP + MSR-QUERY-RESULT-CHAPTER unwired)]
  - [x] Step 6 — Update parser & writer (Green)  [parser readMsrQueryChapter: readARObject → readPaginateable (single readARObject through the mixin chain — readMlFigure precedent; covers SI/VIEW/BREAK/KEEP-WITH-PREVIOUS) + MSR-QUERY-PROPS (unchanged) + MSR-QUERY-RESULT-CHAPTER child → new MsrQueryResultChapter + setMsrQueryResultChapter + readMsrQueryResultChapter (reuses last session's helper, no double readARObject); writer writeMsrQueryChapter: writeARObject → writePaginateable + MSR-QUERY-PROPS (unchanged) + setMsrQueryResultChapter("MSR-QUERY-RESULT-CHAPTER") in XSD group order; test fixture fix: roundtrip test switched to namespace-aware parser.find; 5 focused + 315 Documentation + 19 Chapters tests pass]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.84, p.343 (pdf_page.py verified); 5 method rows (init + 2 getter/setter pairs) with 6 columns + release R23-11, written during the Step 3 full-class rewrite (stale 5-column stub wiped); marker deferred to 9b]
  - [x] Step 8 — Deviations  [none remaining — all five Step-1 findings FIXED this pass, per Rule 0014 no rows kept: (1) base → (Paginateable), (2) msrQueryResultChapter added with the stamped MsrQueryResultChapter type (stub NOTE removed), (3) docstrings wiped/rewritten verbatim, (4) checklist rewritten to 6-column format, (5) reader/writer wired for the mixin chain + result child; accepted handling notes: msrQueryProps pureMM minOccurs=1 vs XSD element minOccurs=0 → uniform-optional Optional modeling (family precedent msrQueryResultChapter/MsrQueryP2); no missing referenced classes (MsrQueryProps ✓, MsrQueryResultChapter ✓, Paginateable ✓)]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a GREEN: 9,111 tests + integration round-trips pass; flake8/ruff/black-check clean (black reflowed 1 file); checklist==methods (5 rows); docstrings byte-verbatim re-verified post-black; 9b: user-confirmed the 11-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `MsrQueryResultTopic1` (dependency · **added 2026-09-11 missing-class audit** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.88 · member type of `MsrQueryTopic1.msrQueryResultTopic1` · **created** · one ordered `topic1` aggregation) — verified R23-11 (commit 09314bd3)
  - [x] Step 1 — Sync members & description from spec  [Table 9.88, p.345 via pdf_page.py; Class MsrQueryResultTopic1; Package M2::MSR::Documentation::MsrQuery → MsrQuery.py; Note and Base ARObject confirmed; one ordered attr `topic1` — Topic1 * aggr, Tags xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false; XSD MSR-QUERY-RESULT-TOPIC-1 group lines 83509-83524 confirms TOPIC-1 unbounded and AR-OBJECT S/T attributes]
  - [x] Step 2 — Write model class unit test (Red)  [TestMsrQueryResultTopic1 in test_MsrQuery.py: initialization, ordered addTopic1/getTopic1s, None no-op; ImportError = Red]
  - [x] Step 3 — Implement model class (Green)  [MsrQueryResultTopic1(ARObject) added to MsrQuery.py; typed `topic1: List[Topic1]` + addTopic1/getTopic1s; exported through existing wildcard chain; 2 focused tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note and topic1 member/accessor docs copied from Table 9.88; PEP 526 annotation; __init__ has no docstring]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new parser/writer tests: S/T + ordered TOPIC-1 values, empty wrapper, missing wrapper, None writer no-op, write→read roundtrip; 7 failed = helpers missing]
  - [x] Step 6 — Update parser & writer (Green)  [parser readMsrQueryResultTopic1/getMsrQueryResultTopic1 reads ordered TOPIC-1 via readTopic1; writer setMsrQueryResultTopic1 writes ordered TOPIC-1 via writeTopic1; imports added; 7 focused tests pass]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.88, p.345; 3 method rows (init + add/get) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none for this class: PDF attr and XSD group fully modeled with typed list and matched reader/writer helpers; accepted consumer deferral: MsrQueryTopic1 remains queued next and will own MSR-QUERY-RESULT-TOPIC-1 placement/coverage]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9118 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed 8-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `MsrQueryTopic1` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.83 · after `DocumentViewSelectable`+`Paginateable` (parents) · deps: `msrQueryProps` stamped ✓ / `MsrQueryResultTopic1` stamped ✓ · deferred stub completed) — verified R23-11 (commit a09f0cdf)
  - [x] Step 1 — Sync members & description from spec  [Table 9.83, p.343 via pdf_page.py; Class MsrQueryTopic1; Package M2::MSR::Documentation::MsrQuery; Note and Base ARObject + DocumentViewSelectable + Paginateable confirmed; attrs displayed order: msrQueryProps MsrQueryProps 1 aggr Tags xml.sequenceOffset=20, msrQueryResultTopic1 MsrQueryResultTopic1 0..1 aggr Tags xml.sequenceOffset=30; XSD MSR-QUERY-TOPIC-1 group confirms MSR-QUERY-PROPS then MSR-QUERY-RESULT-TOPIC-1]
  - [x] Step 2 — Write model class unit test (Red)  [TestMsrQueryTopic1 in test_MsrQuery.py: Paginateable base chain, defaults, both getter/setter pairs, chaining, None no-op; 3 failures = Red (wrong base and deferred result member/accessors)]
  - [x] Step 3 — Implement model class (Green)  [MsrQueryTopic1 now derives from Paginateable; added typed Optional[MsrQueryResultTopic1] member plus set/get accessors; existing msrQueryProps retained and typed; 4 focused tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [deferred stub checklist and placeholder note removed; class Note, both member comments, and all getter/setter docstrings synchronized to Table 9.83 notes/tags; PEP 526 members; __init__ has no docstring]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new parser/writer tests: inherited S/T + SI/VIEW/BREAK/KEEP-WITH-PREVIOUS, MSR-QUERY-PROPS, optional result TOPIC-1, empty wrapper, missing wrapper, XSD child order, write→read roundtrip; 5 failures = helpers/result wiring missing]
  - [x] Step 6 — Update parser & writer (Green)  [readMsrQueryTopic1/getMsrQueryTopic1 now use readPaginateable and parse optional MSR-QUERY-RESULT-TOPIC-1; writeMsrQueryTopic1 now uses writePaginateable and writes result after props; 6 focused tests pass]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.83, p.343; 5 method rows (init + 2 getter/setter pairs) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: all two spec attrs modeled with PDF types and matched reader/writer coverage; most-derived Paginateable base restored; XSD order respected; MsrQueryResultTopic1 dependency stamped ✓; no fabricated or flattened members]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9128 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed 9-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `MsrQueryP1` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.82 · after `DocumentViewSelectable`+`Paginateable` (parents) + `TopicContent` (aggr `msrQueryResultP1`) · `msrQueryProps` stamped ✓ · deferred stub completed) — verified R23-11 (commit 8da723c4)
  - [x] Step 1 — Sync members & description from spec  [Table 9.82, p.343 via pdf_page.py; Class MsrQueryP1; Package M2::MSR::Documentation::MsrQuery; Note and Base ARObject + DocumentViewSelectable + Paginateable confirmed; attrs displayed order: msrQueryProps MsrQueryProps 1 aggr Tags xml.sequenceOffset=20, msrQueryResultP1 TopicContent 0..1 aggr Tags xml.sequenceOffset=30; TopicContent stamped ✓]
  - [x] Step 2 — Write model class unit test (Red)  [TestMsrQueryP1 in test_MsrQuery.py: Paginateable base chain, defaults, both getter/setter pairs, chaining, None no-op; 4 failures = Red (stub base/member/accessors missing)]
  - [x] Step 3 — Implement model class (Green)  [MsrQueryP1 now derives from Paginateable; added typed Optional[MsrQueryProps] and Optional[TopicContent] members with matching accessors; 4 focused tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [deferred stub placeholder removed; class Note, member notes, getter/setter docs, and 6-column checklist synchronized to Table 9.82; PEP 526 members; __init__ has no docstring]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [new parser/writer tests: inherited S/T + SI/VIEW/BREAK/KEEP-WITH-PREVIOUS, MSR-QUERY-PROPS, optional TOPIC-CONTENT result, empty/missing cases, XSD child order, write→read roundtrip; 5 failures = helpers/result wiring missing]
  - [x] Step 6 — Update parser & writer (Green)  [readMsrQueryP1/getMsrQueryP1 use readPaginateable and parse MSR-QUERY-PROPS + TOPIC-CONTENT; writeMsrQueryP1 uses writePaginateable and writes children in props/result order; 6 focused tests pass]
  - [x] Step 7 — Update checklist comment  [# Spec: FO_TPS Table 9.82, p.343; 5 method rows (init + 2 getter/setter pairs) with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: both PDF attrs modeled with PDF types and matched reader/writer coverage; most-derived Paginateable base restored; XSD order respected; TopicContent dependency stamped ✓; no fabricated or flattened members]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 9138 unit tests, lint, Black check, and diff check pass; 9b: user-confirmed 9-item pre-stamp checklist; marker `# Spec verified: R23-11` written]
- [x] `CompuContent` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.63 (abstract) · parent of `CompuScales` below · member of `Compu.compuContent` below · existing stub completed) — verified R23-11 (commit 9f67b3e2)
  - [x] Step 1 — Sync members & description from spec  [Table 5.63, p.387 via pdf_page.py; Class CompuContent (abstract); Package M2::MSR::AsamHdo::ComputationMethod; Note supplied for the abstract meta-class; no Attribute rows (`-`); Base ARObject confirmed by existing implementation; no own XML element]
  - [x] Step 2 — Write model class unit test (Red)  [TestCompuContent in test_ComputationMethod.py: direct abstract TypeError, concrete subclass ARObject defaults, and exact supplied spec Note; initial abstract contract exposed stub coverage gap]
  - [x] Step 3 — Implement model class (Green)  [existing CompuContent(ARObject, ABC) abstract guard retained; no fields or accessors fabricated; focused test passes]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring set to the supplied Note verbatim; no own attributes/member docstrings; removed the pre-existing non-spec "Abstract base class"/Base wording; __init__ has no docstring]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: abstract type has no own XML element or attributes; concrete consumer CompuScales owns COMPU-SCALES coverage]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: no own XML helper; existing consumer dispatch remains unchanged]
  - [x] Step 7 — Update checklist comment  [# Spec: CP_TPS_SoftwareComponentTemplate.pdf, Table 5.63, p.387; one __init__ row with 6 columns + release R23-11; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: abstract class has no own attributes; ARObject base and abstract guard match the class shape; no XML coverage applicable; concrete consumers remain responsible for serialization]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused model tests, full test module, lint, and Black check pass; 9b: user-confirmed no-own-attributes abstract shape, ARObject base, supplied Note verbatim, and concrete-consumer XML coverage; marker `# Spec verified: R23-11` written]
- [x] `CompuConstContent` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.72 (abstract) · parent of `CompuConstTextContent`, `CompuConstNumericContent`, `CompuConstFormulaContent` · member type of `CompuConst.compuConstContentType`) — verified R23-11 (commit b473f524)
  - [x] Step 1 — Sync members & description from spec  [Table 5.72, p.390: abstract class, Base ARObject, no own attributes; Note copied verbatim]
  - [x] Step 2 — Write model class unit test (Red)  [added spec Note, abstract guard, and inherited ARObject default assertions; Note assertion failed before docstring sync]
  - [x] Step 3 — Implement model class (Green)  [existing CompuConstContent(ARObject, ABC) abstract guard retained; no fields or accessors fabricated; focused tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring replaced with the verbatim Table 5.72 Note; removed stale Base/Subclasses/Aggregated by wording; __init__ has no docstring]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: abstract type has no own XML element or attributes; concrete consumer CompuConst owns COMPU-CONST-CONTENT-TYPE coverage]
  - [x] Step 6 — Update parser & writer (Green)  [N/A: no own XML helper; existing consumer dispatch remains unchanged]
  - [x] Step 7 — Update checklist comment  [Table 5.72, p.390; one __init__ row with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: abstract class has no own attributes; ARObject base and abstract guard match the class shape; no XML coverage applicable]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 45 focused model tests, lint, Black check, and diff check pass; 9b: user-confirmed abstract shape, ARObject base, verbatim Note, and concrete-consumer XML coverage; marker written]
- [x] `CompuConstTextContent` (dependency · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.67 · subtype of `CompuConstContent`) — verified R23-11 (commit 4cb82851)
  - [x] Step 1 — Sync members & description from spec  [Table 5.67, p.388: Base ARObject + CompuConstContent; one optional `vt` attribute typed VerbatimString; Note and attribute Note copied verbatim]
  - [x] Step 2 — Write model class unit test (Red)  [added spec Note, VerbatimString type assertion, and None-no-op setter assertion; initial run failed on stale docstring and setter behavior]
  - [x] Step 3 — Implement model class (Green)  [`vt` changed from str to Optional[VerbatimString]; setter now ignores None; focused model tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note replaced verbatim; vt inline/getter/setter docs use the Table 5.67 attribute Note; setter includes the required None-no-op sentence]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser asserts VT produces VerbatimString; writer asserts VT value and omitted empty VT wrapper]
  - [x] Step 6 — Update parser & writer (Green)  [parser VT branch now uses getChildElementOptionalVerbatimString; writer's existing setChildElementOptionalLiteral correctly serializes VerbatimString]
  - [x] Step 7 — Update checklist comment  [Table 5.67, p.388; init/getVt/setVt rows with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: one PDF attribute modeled with its exact VerbatimString type; inherited abstract base not flattened; parser/writer coverage present]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 294 focused model/parser/writer tests, lint, Black check, and diff check pass; 9b: user-confirmed base, typed member, naming, docstrings, reader/writer coverage, and no deviations; marker written]
- [x] `CompuConstNumericContent` (dependency · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.68 · subtype of `CompuConstContent`) — verified R23-11 (commit 4b82220e)
  - [x] Step 1 — Sync members & description from spec  [Table 5.68, p.389: Base ARObject + CompuConstContent; one optional `v` attribute typed Numerical; Note and attribute Note copied verbatim]
  - [x] Step 2 — Write model class unit test (Red)  [added spec Note, ARNumerical type assertion, and None-no-op setter assertion; initial run failed on stale docstring and setter behavior]
  - [x] Step 3 — Implement model class (Green)  [`v` corrected to Optional[ARNumerical]; setter now ignores None; focused model tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note replaced verbatim; v inline/getter/setter docs use the Table 5.68 attribute Note; setter includes the required None-no-op sentence]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [existing parser V branch and writer V branch asserted with numerical field values]
  - [x] Step 6 — Update parser & writer (Green)  [existing getChildElementOptionalNumericalValue and setChildElementOptionalNumericalValue paths cover the typed v member]
  - [x] Step 7 — Update checklist comment  [Table 5.68, p.389; init/getV/setV rows with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: one PDF attribute modeled with the established ARNumerical wrapper type; inherited abstract base not flattened; parser/writer coverage present]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 295 focused model/parser/writer tests, lint, Black check, and diff check pass; 9b: user-confirmed base, typed member, naming, docstrings, reader/writer coverage, and no deviations; marker written]
- [x] `CompuConstFormulaContent` (dependency · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · **Table B.1** (appendix; stale queue citation was 5.70) · subtype of `CompuConstContent`) — verified R23-11 (commit 045d6fb5)
  - [x] Step 1 — Sync members & description from spec  [Table B.1, p.900 (appendix): Base ARObject + CompuConstContent; required `vf` attribute typed Numerical; Note and attribute Note copied verbatim from markdown/PDF]
  - [x] Step 2 — Write model class unit test (Red)  [added spec Note, ARNumerical type assertion, and None-no-op setter assertion; initial run failed on stale docstring and setter behavior]
  - [x] Step 3 — Implement model class (Green)  [`vf` corrected to Optional[ARNumerical]; setter now ignores None; focused model tests pass]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note replaced verbatim; vf inline/getter/setter docs use the full Table B.1 attribute Note including stereotypes/tags; setter includes the required None-no-op sentence]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [parser asserts VF produces ARNumerical; writer asserts numerical VF value]
  - [x] Step 6 — Update parser & writer (Green)  [VF branches now use getChildElementOptionalNumericalValue/setChildElementOptionalNumericalValue]
  - [x] Step 7 — Update checklist comment  [Table B.1, p.900 appendix; init/getVf/setVf rows with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: appendix class table is authoritative despite stale numeric queue citation; one PDF attribute modeled with ARNumerical; parser/writer coverage present]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 296 focused model/parser/writer tests, lint, Black check, and diff check pass; 9b: user-confirmed appendix table citation p.900, base, typed member, naming, docstrings, reader/writer coverage, and no deviations; marker written]
- [x] `CompuConst` (dependency · **added 2026-09-03 restructure** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.71 · member type of `Compu.compuDefaultValue` + `CompuScale.compuInverseValue` below) — verified R23-11 (commit eddddc99)
  - [x] Step 1 — Sync members & description from spec  [Table 5.71, p.390: Base ARObject; one optional aggregate `compuConstContentType` typed CompuConstContent; class and attribute Notes copied verbatim]
  - [x] Step 2 — Write model class unit test (Red)  [added class Note, typed member, chaining, and None-no-op coverage; initial run failed on stale docstring and clearing setter]
  - [x] Step 3 — Implement model class (Green)  [typed optional CompuConstContent member; setter preserves existing value on None]
  - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class Note, inline member comment, getter docstring, and setter docstring now copied from Table 5.71; XML tags retained verbatim; stale base/aggregation prose removed]
  - [x] Step 5 — Write reader/writer round-trip test (Red)  [existing focused parser/writer coverage asserts typed COMPU-CONST content values and omitted wrapper]
  - [x] Step 6 — Update parser & writer (Green)  [existing getCompuConst/setCompuConst helpers cover the member via get/set accessors]
  - [x] Step 7 — Update checklist comment  [Table 5.71, p.390; init/get/set rows with six columns and R23-11 release; marker deferred to 9b]
  - [x] Step 8 — Deviations  [none: one optional PDF aggregate modeled with exact type/name; reader and writer coverage already present]
  - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: focused model/parser/writer tests, lint, Black check, and diff check pass; 9b: user-confirmed Table 5.71 base/member/type/naming/docstrings/reader-writer coverage and no deviations; marker `# Spec verified: R23-11` written]
 - [x] `CompuScaleContents` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.66 (abstract) · parent of `CompuScaleRationalFormula` and `CompuScaleConstantContents` · member type of `CompuScale.compuScaleContents` below) — verified R23-11 (commit pending)
   - [x] Step 1 — Sync members & description from spec  [Table 5.66, p.388; abstract Base ARObject; no own attributes; Note copied verbatim; subclasses CompuScaleConstantContents and CompuScaleRationalFormula; consumer CompuScale.compuScaleContents]
   - [x] Step 2 — Write model class unit test (Red)  [abstract guard, inherited ARObject state, and verbatim Note assertion; failed before import/test-support fix]
   - [x] Step 3 — Implement model class (Green)  [existing abstract class retained; spec shape now represented by the exact Note and ARObject base]
   - [x] Step 4 — Sync docstrings (wipe + rewrite)  [class docstring replaced with the verbatim Table 5.66 Note; no own members or method docstrings]
   - [x] Step 5 — Write reader/writer round-trip test (Red)  [N/A: abstract class has no XML element or own attributes; coverage belongs to CompuScale consumer dispatch]
   - [x] Step 6 — Update parser & writer (Green)  [N/A: existing readCompuScaleContents/writeCompuScaleContents dispatch covers the CompuScaleContents subclasses]
   - [x] Step 7 — Update checklist comment  [Table 5.66, p.388; one __init__ row with six columns and R23-11 release]
   - [x] Step 8 — Deviations  [none: abstract ARObject base, no own attributes, exact Note, and consumer coverage match the spec]
   - [x] Step 9 — Verify (9a) + confirm (9b)  [9a: 300 focused model/parser/writer tests, lint, Black check, and diff check pass; 9b: user-confirmed abstract base, no own attributes, verbatim Note, consumer reader/writer coverage, package location, and no deviations; marker `# Spec verified: R23-11` written]
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
- [ ] `CompuRationalCoeffs` (dependency · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.69 · member type of `CompuScaleRationalFormula.compuRationalCoeffs`)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuScaleRationalFormula` (dependency · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.73 · subtype of `CompuScaleContents` · member type of `CompuScale.compuScaleContents`)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CompuScaleConstantContents` (dependency · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.74 · subtype of `CompuScaleContents` · member type of `CompuScale.compuScaleContents`)
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
- [ ] `SwGenericAxisParamType` (dependency · **added 2026-09-11 missing-class audit** · R23-11 markdown · ref target of `SwRecordLayoutGroup.swGenericAxisParamType` + `SwRecordLayoutV.swGenericAxisParamType` · **NOT in src** — class must be created when this row is synced)
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

- `Area` — not in `src` (NEW) · R23-11 markdown · Table 9.17 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist) → **QUEUED 2026-09-11** as a 9-step row before `Map`
- `MsrQueryResultChapter` — not in `src` (NEW) · R23-11 markdown · Table 9.87 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist) → **QUEUED 2026-09-11** as a 9-step row before `MsrQueryChapter`
- `MsrQueryResultTopic1` — not in `src` (NEW) · R23-11 markdown · Table 9.88 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist) → **QUEUED 2026-09-11** as a 9-step row before `MsrQueryTopic1`
- `SwGenericAxisParamType` — **added 2026-09-03 restructure** · not in `src` · R23-11 markdown · ref target of `SwRecordLayoutGroup.swGenericAxisParamType` + `SwRecordLayoutV.swGenericAxisParamType`; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist) → **QUEUED 2026-09-11** as a 9-step row before `SwRecordLayoutV`
- `TraceableTable` — **added 2026-09-11 dependency audit** · not in `src` · R23-11 markdown · member type of `TopicContent.traceableTable` (the TopicContent row already said "traceableTable TraceableTable remains pending 16.4", but no entry existed here); 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist) → **QUEUED 2026-09-11** as a 9-step row before `TopicContent`

## Not queued

_(none)_
