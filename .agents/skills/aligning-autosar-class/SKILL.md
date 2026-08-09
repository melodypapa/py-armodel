---
name: aligning-autosar-class
description: "Use when aligning, implementing, or extending an AUTOSAR model class in py-armodel against its PDF spec table. Triggers: 'align <ClassName>', 'implement <ClassName> to spec', 'add reader/writer coverage for <ClassName>', 'update the class checklist', 'sync docstrings to the PDF', or working on any class under src/armodel/models/M2/AUTOSARTemplates/. py-armodel project."
author: melodypapa
repository: https://github.com/melodypapa/py-armodel
license: MIT
metadata:
  version: "1.4.0"
  keywords:
    - AUTOSAR
    - model-class
    - spec-alignment
    - TDD
    - checklist
    - reader
    - writer
    - py-armodel
---

# Aligning an AUTOSAR Model Class (TDD)

## Core Principle

The AUTOSAR PDF spec table is the source of truth. Align via a **9-step TDD workflow**:
write the failing test (Red) before the implementation (Green), **twice** — once for the
model, once for the reader/writer. Set the release before parse/write:

```python
document = AUTOSAR.getInstance()
document.setARRelease('R23-11')
```

Detailed rules live in **`rules.md`** (*Rule 0001*–*Rule 0014*); this skill is
self-contained (no external rules document). Each step below points into `rules.md` for
the detail — do not re-derive it here.

## When to use / NOT to use

**Use** when aligning, implementing, or extending a model class under
`src/armodel/models/M2/AUTOSARTemplates/` against its PDF spec table.

**Not for:** non-AUTOSAR classes; reader/writer-only refactors with no spec change;
trivial edits that don't touch the class's spec contract.

## Input

**Required:** `ClassName`. From it, locate:

| Artifact | Path |
|---|---|
| source | `src/armodel/models/M2/AUTOSARTemplates/<pkg>/<ClassName>.py` (or `<pkg>/<ClassName>/__init__.py`) |
| model test | `tests/test_armodel/models/M2/AUTOSARTemplates/<pkg>/test_<ClassName>.py` → `class Test<ClassName>` — pairs 1:1 with source `<ClassName>.py` (Step 2) |
| parser test | `tests/test_armodel/parser/test_*.py` → `class Test*` (load with `ARXMLParser`, assert model fields; Step 5) |
| writer test | `tests/test_armodel/writer/test_*.py` → `class Test*` (set → save → reload round-trip; Step 5) |
| spec PDF | `autosar/pdf/AUTOSAR_CP_TPS_*.pdf` — **PDF name, Table ID, and page (p.NN) come from the PDF file directly** |
| spec table | `grep "Table N.M: <ClassName>" autosar/markdown/AUTOSAR_CP_TPS_*.md` (table content only; the markdown carries no page numbers) |
| deviation records | the project deviation tracker (format in *Rule 0014*) |
| XSD ground truth | `autosar-pdf/examples/xsd/` |

## The 9-step workflow (TDD)

Two Red→Green pairs: **2→3** (model) and **5→6** (reader/writer). Do not write the
implementation before its failing test.

| Step | What | Rules | Phase |
|---|---|---|---|
| 1 | Sync members & description from the PDF by class name | 0001 (§§1.1–1.5, 1.11), 0007 | — |
| **2** | **Write the model class unit test** | 0006 | **Red** |
| **3** | **Implement the model class** | 0001 (§§1.6, 1.8, 1.10), 0003, 0004, 0005, 0008, 0009, 0010, 0011 | **Green** |
| 4 | Sync description (docstrings & comments) | 0012 (§§2–3) | — |
| **5** | **Write the reader/writer round-trip test** | 0006 | **Red** |
| **6** | **Update the parser (reader) & writer** | 0001 (§1.7), 0013 | **Green** |
| 7 | Update the 5-column checklist comment | 0002 | — |
| 8 | Deviations ⇒ no `# Spec verified:` stamp | 0001 (§1.9), 0012 (§1), 0014 | — |
| 9 | Verify (gate) | 0006 | — |

**Essence per step** (full detail in `rules.md`):

- **1** — Extract `Note`/`Base`/`Attribute` rows in displayed order; confirm Class vs
  Enumeration header; *Rule 0007* (Package→module location, no shadowing) is part of
  this step.
- **2** — `test_initialization` (defaults), `test_get_set_*` (round-trip + **None
  no-op**), `create*`/`add*` (append + duplicate-returns-existing). **Abstract class?**
  test `__init__` + base accessors through a concrete subclass (*Rule 0006*).
- **3** — Most-derived base from the `Base` chain; dedicated typed list fields for `*`
  `aggr` (never registry filters); `createXxx` only for `Referrable` children; collect &
  report referenced non-existent classes (do **not** block). **Enum (`AREnum`)?** produce
  literals not accessors (*Rules 0010–0011*).
- **4** — Class docstring = PDF `Note` verbatim; a guarded setter states the None-no-op
  sentence.
- **5** — **Reader/writer tests live in their own folders**, not the per-class mirror:
  parser → `tests/test_armodel/parser/`, writer → `tests/test_armodel/writer/`
  (both `class Test*`, organized by feature/handler). Assert **field values** (not just
  `len(...) == n`); add an empty-wrapper-list case.
- **6** — Reader populates via mutators (`readXxx`→`setXxx`/`createXxx`/`addXxx`), writer
  reads via getters (`writeXxx`→`getXxx`); cover wrapper lists + polymorphic five-place
  dispatch; **no chained mutator calls** (*Rule 0013*).
- **7** — One row per method, source order, all `[x]`, using the 5-column format below.
- **8** — Record deviations (*Rule 0014*); **omit `# Spec verified:`** while any
  placeholder/deviation remains; report the Step-3 referenced classes here.
- **9** — `pytest` + `flake8` + `ruff check` + `black-check` + the set-based script + a
  lossless integration round-trip (`npm run flake8` / `npm run ruff-check` /
  `npm run black-check` are the cross-platform forms). **Stop on any failure.**

**Workflow adaptations** (which steps still apply):

- **`AREnum`** — Step 2 tests member presence/values + instantiability
  (`MyEnum().setValue(MyEnum.MEMBER)`); Steps 5/6 are **N/A for a standalone enum** —
  it has no own XML element, so it is serialized as an attribute value on a *consuming*
  class and round-tripped there (*Rules 0010–0011*).
- **No own spec table (XSD-only class, e.g. a concrete `<name>InstanceRef`)** — Step 1
  derives attributes from the XSD group, not a PDF table; the checklist stays all `[ ]`
  with no `# Spec:` line and no marker (*Rule 0002*).

## The 5-column checklist (Rule 0002)

```
# ClassName method parity checklist:
# Spec: AUTOSAR_CP_TPS_<Template>.pdf, Table X.Y, p.NN
# Spec verified: R<YY>-<MM>
# Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
# [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
# [x] createFoo    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
# [x] getFoos      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
# [x] setBar       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
# [x] getBar       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
```

**Citation source:** the `# Spec:` PDF name, Table ID, and `p.NN` page come from the
PDF file directly (`autosar/pdf/AUTOSAR_CP_TPS_*.pdf`); the markdown carries no page
numbers.

`reader [x]` on the **mutator** row (reader's `readXxx` calls `setXxx`/`createXxx`/
`addXxx`); `writer [x]` on the **getter** row (writer's `writeXxx` calls `getXxx`);
`[—]` for no-XML members (`__init__`, `atpDerived`, convenience properties). An `AREnum`
class has `# (no methods)` and reader/writer coverage is the enum value form. Full
detail: *Rule 0002*.

## Common Mistakes / Red Flags — STOP

- **Implementing before the test** (model 2→3, reader/writer 5→6).
- **`getXxxs()` filtering the `elements` registry by `isinstance`** — use a dedicated
  typed list field (*Rule 0004*).
- **Stamping `# Spec verified:` while a placeholder/deviation remains** (Step 8).
- **A `[x]` checklist with `reader`/`writer` still `[ ]`** — silent round-trip drop.
- **Asserting only `len(...) == n`** in the round-trip test — assert field values.
- **Chained `set(...).set(...)`** in reader/writer source (*Rule 0013*).
- **Double `readReferrable`** — `readImplementationProps` called both, or a subclass
  re-reading `readReferrable` on top of its base helper → duplicate UUIDMgr registry
  entries (*Rule 0013.1*).
- **Recording a `naming`/`missing`/`type` deviation and leaving it** — to-fix: rename/
  retype/cover and **remove** the row (*Rule 0014*).
- **`T | None` / `list[…]` hints** — Python ≥ 3.8: `Optional[T]` / `List[T]` (*Rule 0003*).

| Rationalization | Reality |
|---|---|
| "Simple model — I'll implement then test" | A test written after mirrors the code, not the spec. Step 2 first. |
| "Reader/writer first, round-trip test after" | No failing round-trip ⇒ can't see dropped elements. Step 5 first. |
| "It's just docstrings, skip Step 4" | Drift is silent; the marker then certifies wrong wording (*Rule 0012*). |

## References

- **Rules (self-contained):** `rules.md` in this skill folder — *Rule 0001*–*Rule 0014*.
- Coding standards: `docs/development/coding_rules.md`.
- Spec PDFs (authoritative — source of the PDF name, Table ID, and page): `autosar/pdf/AUTOSAR_CP_TPS_*.pdf`.
- Spec markdown (derived table content; carries no page numbers): `autosar/markdown/AUTOSAR_CP_TPS_*.md`.
- XSD ground truth: `autosar-pdf/examples/xsd/`.
