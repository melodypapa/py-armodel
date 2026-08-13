---
name: sync-autosar-class
description: "Use when syncing, aligning, implementing, or extending an AUTOSAR model class in py-armodel against its PDF spec table. Triggers: 'sync <ClassName>', 'implement <ClassName> to spec', 'add reader/writer coverage for <ClassName>', 'update the class checklist', 'sync docstrings to the PDF', or working on any class under src/armodel/models/M2/AUTOSARTemplates/. py-armodel project. Phase 0 builds the class closure and resolves missing classes interactively before the per-class 9-step TDD loop."
author: melodypapa
repository: https://github.com/melodypapa/py-armodel
license: MIT
metadata:
  version: "1.6.0"
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

# Syncing an AUTOSAR Model Class (TDD)

## Core Principle

The AUTOSAR PDF spec table is the source of truth. Sync runs in **two phases**:

- **Phase 0 — Discovery & class closure (Rule 0016):** build the closure of related
  classes (parents + member types), confirm the collected set with the user, locate
  each one's spec source (markdown → PDF → missing), resolve missing classes
  interactively (skip / derive from XSD), and emit an ordered sync queue.
- **Phase 1 — 9-step TDD per class (Rules 0001–0015):** consume the queue
  one class at a time. Two Red→Green pairs per class: model (2→3) and reader/writer
  (5→6). Write the failing test before the implementation. Each class ends with a
  rule-compliance confirmation gate (Step 9b) before it is stamped.

Set the release before parse/write:

```python
document = AUTOSAR.getInstance()
document.setARRelease('R23-11')
```

Detailed rules live in **`rules.md`** (*Rule 0001*–*Rule 0016*); this skill is
self-contained (no external rules document). Each step below points into `rules.md` for
the detail — do not re-derive it here.

## When to use / NOT to use

**Use** when syncing, implementing, or extending a model class under
`src/armodel/models/M2/AUTOSARTemplates/` against its PDF spec table.

**Not for:** non-AUTOSAR classes; reader/writer-only refactors with no spec change;
trivial edits that don't touch the class's spec contract.

## Phase 0 — Discovery & Class Closure (Rule 0016)

Before the per-class 9-step loop, build the closure of classes that the input
class depends on, have the end user confirm the collected set, locate the spec
for each, resolve missing classes with the user, and emit an ordered sync queue.
The 9-step workflow assumes this closure exists — running it without Phase 0
risks fabricating fields when a referenced class turns out to be missing mid-sync
(Rule 0001.10).

**Procedure (full detail in Rule 0016):**

1. **Closure** = {input class} ∪ {transitive parents from `Base`} ∪ {member types
   from `Attribute` rows: refs, aggrs, enums, primitive containers}.
2. **Confirm the collected set (gate).** Present every collected class to the end
   user with its role (`input` / `base` / `member`) and, for member types, the
   referencing attribute, then ask: *is this set correct and complete?* Do **not**
   locate specs, resolve missing classes, or build the queue until the user
   confirms. If the user adds or drops a class, rebuild the closure and re-confirm.
   This membership gate is distinct from the missing-class resolution gate in
   step 4.
3. **Locate spec source** for each closure class: markdown first
   (`grep "Table N.M: K" autosar/markdown/*_TPS_*.md`), then PDF, then mark
   `missing`.
4. **Resolve missing classes (interactive, batched)**: present one
   `AskUserQuestion` listing every class not in markdown or PDF. Per class, the
   user picks **Skip** (deviation row + placeholder) or **Derive from XSD**
   (XSD-only class, no marker). Do not proceed without an answer; do not invent a
   third option.
5. **Build the sync queue**: parents first (deepest ancestor first → input class
   last), member types in spec-row order. Skip classes already stamped
   `# Spec verified: R<YY>-<MM>` unless extending or drift (Rule 0012.3).
   **"Exists" is not a stamp** — a member type that exists but is a stub (no marker,
   or fields/literals don't match its own table) is queued for the same pass like a
   missing class (Rule 0001.10 / 0016.4).

**Output:** a sync map (kept in the conversation) listing each closure class,
its source, its parent, and whether it enters the 9-step queue.

Phase 1 consumes this map one row at a time.

## The stamp is the review gate

A class counts as **reviewed/synced ONLY** when its source carries the
`# Spec verified: R<YY>-<MM>` marker (Step 8 / Rule 0012.1). That marker is the single
provenance signal — nothing else (a fully-`[x]` checklist, passing tests, or a clean
round-trip) certifies a class as reviewed.

- **Has the marker** → the class has been synced. Treat its fields, checklist,
  docstrings, and reader/writer coverage as authoritative. Re-run the workflow only when
  the spec changes (Rule 0012.3 drift) or when extending the class.
- **No marker** → the class has **not** been reviewed. Sync it **from the beginning**:
  run the full 9-step workflow starting at Step 1, with the failing model test first
  (Step 2). Do **not** trust pre-existing fields/checklist/docstrings — they may be
  fabricated or stale (Rule 0001.3 shape-3 detector; the Rule 0002 field-to-spec
  cross-check is the gate, in both directions).
- **Exception — no own spec table:** a class whose attributes are XSD-only legitimately
  carries no marker and all-`[ ]` rows. It is *not* "unreviewed" — it is excluded
  (Rule 0002). Confirm the exception before treating a marker-less class as
  sync-from-scratch.

## Input

**Required:** `ClassName`. From it, locate:

| Artifact | Path |
|---|---|
| source | `src/armodel/models/M2/AUTOSARTemplates/<pkg>/<ClassName>.py` (leaf package → `<pkg>.py`; non-leaf package with subpackages → `<pkg>/__init__.py`. See Rule 0007) |
| model test | `tests/test_armodel/models/M2/AUTOSARTemplates/<pkg>/test_<ClassName>.py` → `class Test<ClassName>` — pairs 1:1 with source `<ClassName>.py` (Step 2) |
| parser test | `tests/test_armodel/parser/test_*.py` → `class Test*` (load with `ARXMLParser`, assert model fields; Step 5) |
| writer test | `tests/test_armodel/writer/test_*.py` → `class Test*` (set → save → reload round-trip; Step 5) |
| spec markdown | `grep "Table N.M: <ClassName>" autosar/markdown/AUTOSAR_*_TPS_*.md` — **primary source for all text**: `Note` (→ docstrings), `Attribute`/`Base`, `Table N.M` id, table name (via filename). Covers **both** `CP_TPS` (Classic) and `FO_TPS` (Foundation) |
| spec PDF | `autosar/pdf/AUTOSAR_*_TPS_*.pdf` — **opened only to read the page number** (`p.NN`); the markdown carries no page numbers |
| deviation records | the project deviation tracker (format in *Rule 0014*) |
| XSD ground truth | `docs/requirements/xsd/` |

## Phase 1 — The 9-step workflow (TDD, per class)

Runs once per class in the queue built by Phase 0 (Rule 0016). Two Red→Green pairs:
**2→3** (model) and **5→6** (reader/writer). Do not write the implementation
before its failing test.

| Step | What | Rules | Phase |
|---|---|---|---|
| 1 | Sync members & description from the PDF by class name | 0001 (§§1.1–1.5, 1.11), 0007, 0015 | — |
| **2** | **Write the model class unit test** | 0006 | **Red** |
| **3** | **Implement the model class** | 0001 (§§1.6, 1.8, 1.10), 0003, 0004, 0005, 0008, 0009, 0010, 0011 | **Green** |
| 4 | Sync description (docstrings & comments) | 0012 (§§2–3) | — |
| **5** | **Write the reader/writer round-trip test** | 0006 | **Red** |
| **6** | **Update the parser (reader) & writer** | 0001 (§1.7), 0013 | **Green** |
| 7 | Update checklist comment (`# Spec:` + rows; **marker deferred to 9b**) | 0002 | — |
| 8 | Deviations ⇒ no `# Spec verified:` stamp | 0001 (§1.9), 0012 (§1), 0014 | — |
| 9 | Verify (9a) + confirm (9b) ⇒ **write `# Spec verified:`** | 0006, 0006.1 | — |

**Essence per step** (full detail in `rules.md`):

- **1** — Extract `Note`/`Base`/`Attribute` rows in displayed order; confirm Class-vs-Enumeration header. *Rule 0015* arbitrates XSD-vs-PDF/markdown attribute conflicts (the PDF/markdown table wins — model nothing the PDF lacks).
- **2** — `test_initialization` (defaults), `test_get_set_*` (round-trip + **None no-op**), `create*`/`add*` (append, duplicate returns existing). Abstract class → test `__init__` + base accessors via a concrete subclass.
- **3** — Most-derived base from the `Base` chain; dedicated typed-list fields for `*` `aggr` (never registry filters); `createXxx` only for `Referrable` children; collect referenced missing classes and report in Step 8 (don't block). Enum (`AREnum`) → literals, not accessors.
- **4** — Copy the spec `Note` **verbatim from the markdown** into the **class docstring** (the class-level `Note` — **not** into `__init__`, which has no docstring), inline `__init__` **comments**, and getter/setter docstrings (PDF opened only for the `p.NN` page); guarded setters append the None-no-op sentence.
- **5** — Reader/writer tests live in **their own folders** (`tests/test_armodel/parser/`, `.../writer/`, both `class Test*`), not the per-class mirror. Assert **field values**, not just `len(...) == n`; add an empty-wrapper-list case.
- **6** — Reader populates via mutators (`readXxx`→`set/create/addXxx`), writer reads via getters (`writeXxx`→`getXxx`); cover wrapper lists + polymorphic five-place dispatch; **no chained mutator calls**.
- **7** — One row per method, source order, all `[x]`, 5-column format below. Writes the `# Spec:` line + method rows **only** — the `# Spec verified:` marker is added in Step 9b, never here.
- **8** — Record deviations; the `# Spec verified:` marker (added in 9b) is **withheld** while any placeholder/deviation remains; report the Step-3 referenced classes here.
- **9** — **(9a automated)** `pytest` + `flake8` + `ruff check` + `black-check` + the set-based script + a lossless integration round-trip (`npm run flake8` / `ruff-check` / `black-check` are the cross-platform forms). **Stop on any failure.** **(9b confirm — gate)** then present the **complete pre-stamp** rule-compliance checklist covering every check automation is blind to — element kind + every spec attr modeled (*0001.1*), most-derived base (*0001.2*), no fabrication/flattening + PDF-typed fields (*0001.3*), **Kind-suffix naming** `ref`→Ref/Refs·`tref`→TRef·`iref`→IRef/IRefs + singular `*`→plural (*0001.5*), create/set/add shape (*0001.6*), **reader+writer coverage** for every kept attr (*0001.7*), **member order** (*0011*), docstrings = spec `Note` **verbatim by diff** (*0012*), deviations resolved/removed (*0014*), stamp decision (*0012.1*) — and get explicit user confirmation; **when all pass, write the `# Spec verified:` marker in this step (9b)** — never in Step 4/7/8. Fix & re-present on any failure (*Rule 0006.1* has the full checklist).

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
# Spec: AUTOSAR_<Platform>_TPS_<Template>.pdf, Table X.Y, p.NN
# Spec verified: R<YY>-<MM>
# Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
# [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
# [x] createFoo    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
# [x] getFoos      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
# [x] setBar       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
# [x] getBar       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
```

**Citation source:** the `# Spec:` table name, `Table N.M` id, and `Note` text come from
the **markdown** (`autosar/markdown/AUTOSAR_*_TPS_*.md` — covers `CP_TPS` and `FO_TPS`);
only the `p.NN` **page** is read from the **PDF** (`autosar/pdf/...`) — the markdown
carries no page numbers. In the `# Spec:` line, `<Platform>` is `CP` (Classic) or `FO`
(Foundation), taken from the spec markdown filename.

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
- **Flattened inherited members on a subclass** — the subclass's own spec table (`Attribute`
  column) has fewer rows than the subclass has fields; the "extra" fields live in a *separate
  base-class table* named in `Base`. Model that base class and relocate the members there;
  reduce the subclass to its own attributes (*Rule 0001.3*). A fully-`[x]` checklist + clean
  round-trip **will not** catch this — the field-to-spec cross-check is the gate.
- **Locating specs / building the queue before the user confirms the collected closure** —
  Phase 0 step 2 is a membership gate, not a nicety; over- or under-collection silently
  corrupts the whole queue (*Rule 0016.2*).
- **Stamping `# Spec verified:` (or advancing to the next class) straight after the
  automated checks pass** — Step 9b is a confirmation gate for the rules automation is
  blind to (field↔spec both directions, verbatim docstrings, no fabrication/flattening,
  reader+writer coverage, member order); present the summary and get user sign-off first
  (*Rule 0006.1*).
- **Trusting a pre-existing `# Spec verified:` stamp and skipping 9b** — the marker is
  the *output* of 9b, not a substitute for it; on any re-sync/drift pass, re-run the full
  9b checklist before re-stamping (*Rule 0006.1*, *Rule 0012.3*).
- **Class `Note` written into the `__init__` docstring** — the class-level `Note` belongs
  in the **class docstring** only; `__init__` carries inline per-attribute comments and
  **no docstring** (Rule 0012.2.3 / 0012.2.4.2).

| Rationalization | Reality |
|---|---|
| "Simple model — I'll implement then test" | A test written after mirrors the code, not the spec. Step 2 first. |
| "Reader/writer first, round-trip test after" | No failing round-trip ⇒ can't see dropped elements. Step 5 first. |
| "It's just docstrings, skip Step 4" | Drift is silent; the marker then certifies wrong wording (*Rule 0012*). |
| "The closure looks right, I'll skip the confirm gate" | Over/under-collection wastes every later step; present the set and let the user confirm (*Rule 0016.2*). |
| "Tests pass and the round-trip is clean — I can stamp and move on" | Those don't certify a class (Rule 0012.1); run Step 9b on the blind-spot rules before stamping (*Rule 0006.1*). |
| "The class already has `# Spec verified:` stamped — I'll skip 9b" | The marker is the *output* of 9b, not a substitute; on re-sync/drift re-run the full 9b checklist — a stale marker certifies nothing (*Rule 0006.1*, *Rule 0012.3*). |

## References

- **Rules (self-contained):** `rules.md` in this skill folder — *Rule 0001*–*Rule 0016*.
- Coding standards: `docs/development/coding_rules.md`.
- Spec markdown (primary — source of all text: `Note`, `Table N.M` id, table name): `autosar/markdown/AUTOSAR_*_TPS_*.md` (`CP_TPS` + `FO_TPS`).
- Spec PDFs (opened only for the `p.NN` page number): `autosar/pdf/AUTOSAR_*_TPS_*.pdf`.
- XSD ground truth: `docs/requirements/xsd/`.
