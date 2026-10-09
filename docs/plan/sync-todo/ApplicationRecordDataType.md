# Sync todo: ApplicationRecordDataType

Input class: ApplicationRecordDataType · Generated: 2026-10-10 · Queue order = row order
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished — Rule 0017.3)
> Deviation-fix pass. Group2.md:387 skipped this class (commit `0a06e0fae`) rather than
> redesign the inherited `Referrable.elements` registry, leaving the spec member `element (ordered)`
> recorded as `missing` in `docs/examples/method_deviation_by_class_v2.md:1024` and no
> `# Spec verified:` marker. Closure confirmed by the user 2026-10-10: the rename clears the conflict,
> because the `Identifiable` registry field is `referrableElements` — no `elements` collision exists.

## Queue (dependency-first)

- [x] `ApplicationRecordDataType` (input · R23-11 markdown · Table 5.12, p.261 · commit 348b98513)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py
  - Note: own Table 5.12, p.261 — concrete `Class`, one `Attribute` row: `element (ordered)` |
    `ApplicationRecordElement` | `*` | `aggr`. Most-derived base = `ApplicationCompositeDataType`
    (already correct). Fix scope = Rule 0001.5 base name verbatim (`recordElements` → `elements`,
    pluralized per Rule 0001.4 for the `*` quota, precedented by `ImplementationDataType.subElements`
    / `ClientServerInterface.operations` / `TriggerInterface.triggers`) + getter
    `getApplicationRecordElements()` → `getElements()`; `createApplicationRecordElement` is **kept**
    (type-named factory, precedented by `createImplementationDataTypeElement` / `createApplicationError`).
    Docstrings are currently absent → full Rule 0012.2.3 wipe + rewrite incl. the `Tags:`/`Stereotypes:`
    tails (Rule 0012.2.5.3) and `constr_1908`.
  - [x] Step 1 — Sync members & description from spec — Table 5.12, p.261; concrete `Class` (not Enumeration); most-derived base `ApplicationCompositeDataType` already correct; one Attribute row `element (ordered)` | `ApplicationRecordElement` | `*` | `aggr`; Noto-class text and attribute Note captured verbatim incl. `Stereotypes:`/`Tags:` tail + constr_1908
  - [x] Step 2 — Write model class unit test (Red) — `TestApplicationRecordDataType` rewritten: base shape/signature, `cleandoc` class-Note pin, `[]` defaults, `get_type_hints` List pin, create-append + duplicate-returns-existing, registry registration, getter-returns-field identity, two verbatim accessor-Note pins, legacy-name-absence. Red: 9 failed / 3 passed
  - [x] Step 3 — Implement model class (Green) — `self.recordElements` → `self.elements: List[ApplicationRecordElement] = []` (Rule 0001.5 verbatim base name, pluralized per Rule 0001.4 `*` quota); `getApplicationRecordElements()` → `getElements()`; `createApplicationRecordElement` kept (type-named factory). Red→Green: 9 failed → 3 passed (remaining 3 = the Step 4 docstring pins)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring wiped then rewritten verbatim (Note + `Tags: atp.recommendedPackage=ApplicationDataTypes` per Rule 0012.2.5.3 + constr_1908, matching the ApplicationArrayDataType sibling's constr rendering); `__init__` member comment + `createApplicationRecordElement` + `getElements` docstrings written verbatim from the Table 5.12 attribute Note incl. the `Stereotypes: atpSplitable; atpVariation Tags: ...` tail; 50 passed test_Datatypes.py
  - [x] Step 5 — Write reader/writer round-trip test (Red) — writer: field-value assertions on ELEMENTS/APPLICATION-RECORD-ELEMENT (ordered short names, TYPE-TREF DEST+value, IS-OPTIONAL present/absent), full set→save→reload→assert round-trip, plus an empty-wrapper round-trip; parser: `getElements()` ordered names + TYPE-TREF/IS-OPTIONAL field values + no-elements case. Red: 7 writer failures (`getApplicationRecordElements` gone)
  - [x] Step 6 — Update parser & writer (Green) — writer `writeApplicationRecordDataTypeElements` now reads via `getElements()`; reader already populated through the `createApplicationRecordElement` mutator and needed no change. Base-helper symmetry re-checked per Rule 0025: reader calls `readIdentifiable` exactly once, writer reaches `writeARElement` via `setApplicationDataType` → `writeAutosarDataType` on this instance. 411 passed across the two touched files
  - [x] Step 7 — Update checklist comment — 6-column block above `__init__`, 3 rows in source order, `getApplicationRecordElements` row renamed to `getElements`; bare `(R23-11)` suffix dropped from the `# Spec:` line per canonical single-corpus form; `audit_class.py` PASS (BLOCK/ROWS/SPECLINE/CITATION/SPACING/DOCTAIL/DOC clean)
  - [x] Step 8 — Deviations — the `missing` row for `element(ordered)` is **resolved and removed** (Rule 0014): field/accessors renamed to the spec base name, reader+writer coverage pinned. Tracker entry rewritten as "No deviations" with the resolution note. No `atpDerived` / `legacy` / convenience deviations remain, no Rule 0001.10 placeholder
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: `pytest tests/test_armodel/` 24796 passed / 0 failed; `tests/integration_tests/` 13 passed (lossless round-trip); `test_member_annotations.py` 3 passed; `npm run lint` (flake8+ruff+mypy) Success 279 files; `npm run black-check` 2846 unchanged; set-based checklist==methods 3/3; `audit_class.py` PASS 0 failures. 9b: 18-item rule checklist presented and user-confirmed 2026-10-10; **one 9b finding fixed before stamping** — the markdown renders `element.variation Point.shortLabel` and I had silently normalized it to `variationPoint.shortLabel`; Rule 0012.2.6 requires copying the Note as rendered (stamped precedent `AccessCountSet` AccessCount.py:163), so all three sites were corrected and re-diffed character-for-character clean. Marker written after the `# Spec:` line per Rule 0012.1 adjacency

## Not queued (16.4 / 16.5 decisions)

- `ApplicationCompositeDataType` (base) — already stamped `# Spec verified: R23-11`, Table 5.6, p.241.
- `ApplicationDataType` (base) — already stamped `# Spec verified: R23-11`, Table 5.2, p.232.
- `AutosarDataType` (base) — already stamped `# Spec verified: R23-11`, Table 5.1, p.232.
- `ApplicationRecordElement` (member, referenced by `element (ordered)`) — already stamped
  `# Spec verified: R23-11`, Table 5.13, p.262. `Referrable` sub-elements attribute `isOptional` +
  `VariationPointCapable` mixin (Rule 0020 — VARIATION-POINT is on the `APPLICATION-RECORD-ELEMENT`
  XSD group, *not* on `APPLICATION-RECORD-DATA-TYPE`) already conform.
- `ARElement`, `ARObject`, `Identifiable`, `MultilanguageReferrable`, `PackageableElement`,
  `CollectableElement`, `AtpClassifier`, `AtpType`, `AtpBlueprint`, `AtpBlueprintable` (bases) —
  already stamped `# Spec verified: R23-11`.
- `Referrable` (base) — no `# Spec verified:` marker, but foundational infrastructure and the base of
  hundreds of stamped classes; out of scope for this deviation-fix closure (user-confirmed 2026-10-10).
- 16.4 missing-class resolution: **vacuous** — every closure class was located in the R23-11 markdown
  corpus (Rule 0016.3 R4.3.1 fallback not needed).