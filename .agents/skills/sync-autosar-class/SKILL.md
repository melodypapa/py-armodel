---
name: sync-autosar-class
description: "Use when syncing, aligning, implementing, or extending an AUTOSAR model class in py-armodel against its PDF spec table. Triggers: 'sync <ClassName>', 'implement <ClassName> to spec', 'add reader/writer coverage for <ClassName>', 'update the class checklist', 'sync docstrings to the PDF', 'continue/resume the class sync', or working on any class under src/armodel/models/M2/AUTOSARTemplates/. py-armodel project. Phase 0 builds the class closure and resolves missing classes interactively before the per-class 9-step TDD loop."
author: melodypapa
repository: https://github.com/melodypapa/py-armodel
license: MIT
metadata:
  version: "1.9.1"
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
  interactively (skip / derive from XSD), and write the persistent sync todo list
  (`docs/plan/sync-todo/<InputClassName>.md`) — the queue survives session death.
- **Phase 1 — 9-step TDD per class (Rules 0001–0015, 0017–0018):** consume the queue
  one class at a time, **one class per fresh session** (Rule 0017). Two Red→Green
  pairs per class: model (2→3) and reader/writer (5→6). Write the failing test before
  the implementation. The 9 steps are mirrored into the session todo list — one todo
  per step, checked off the moment its step finishes (Rule 0018) — **and into the
  todo file itself: every queued class row carries a 9-step sub-checklist written
  at file creation (Phase 0) and flipped per step, so step progress survives
  session death (Rule 0016.6)**. Each class ends
  with a rule-compliance confirmation gate (Step 9b) before it is stamped, marked
  finished in the todo list, and committed to the feature branch. All rows `[x]` in
  the todo list = the sync is finished.

Set the release before parse/write:

```python
document = AUTOSAR.getInstance()
document.setARRelease('R23-11')
```

Detailed rules live in **`rules.md`** (*Rule 0001*–*Rule 0018*); this skill is
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
   (`grep "Table N.M: K" autosar/R23-11/markdown/*_TPS_*.md`), then PDF, then mark
   `missing`.
4. **Resolve missing classes (interactive, batched)**: present one
   `AskUserQuestion` listing every class not in markdown or PDF. Per class, the
   user picks **Skip** (deviation row + placeholder) or **Derive from XSD**
   (XSD-only class, no marker). Do not proceed without an answer; do not invent a
   third option.
5. **Build the sync queue — dependency-first** (Rule 0016.5): a class that other
   queued classes reference (`Base` or `Attribute` member type) is queued
   **before** its dependents; deepest ancestors first, ties keep spec-row order,
   input class last. A dependent must never precede the class it references.
   Skip classes already stamped `# Spec verified: R<YY>-<MM>` unless extending
   or drift (Rule 0012.3).
   **"Exists" is not a stamp** — a member type that exists but is a stub (no marker,
   or fields/literals don't match its own table) is queued for the same pass like a
   missing class (Rule 0001.10 / 0016.4).
6. **Write the sync todo list file** (Rule 0016.6): persist the confirmed queue to
   `docs/plan/sync-todo/<InputClassName>.md` — one row per queued class, **each
   row carrying its 9-step sub-checklist (all `[ ]`, names per Rule 18.1, written
   now at file creation — not deferred to class start)**, plus the Skip/XSD
   resolution decisions. **The queue lives in this file, not in the
   conversation.** The Phase 0 session ends here.

**Output:** `docs/plan/sync-todo/<InputClassName>.md` — the persistent queue
(Rule 0016.6). Phase 1 consumes it one row at a time, **one class per fresh
session** (Rule 0017).

## Phase 1 — Session loop & the 9-step workflow (Rules 0017–0018)

- **Entry (every session):** the user invokes the skill (e.g. `/sync-autosar-class
  <ClassName>` or "continue the sync"). If `docs/plan/sync-todo/<ClassName>.md`
  exists, **resume — do NOT re-run Phase 0** (the closure was already confirmed;
  re-running it re-asks the interactive gates for nothing). Read the todo file,
  take the **first row still `[ ]`**, and run the 9-step workflow for that one
  class. If the file does not exist, run Phase 0 first.
- **One class per session.** Never sync two classes in one session, even when the
  context still feels fresh — the 9b verbatim-diff work degrades silently under a
  loaded context. After a class finishes (below), stop and tell the user to start
  a new session.
- **Mirror the 9 steps into the session todo list (Rule 0018).** After taking the
  `[ ]` row and before Step 1, create **9 session todos — one per workflow step**
  (`Step 1 — Sync members & description from spec` … `Step 9 — Verify (9a) +
  confirm (9b)`). Mark each `in_progress` when the step begins and `completed`
  **the moment that step finishes** — one completed step = exactly one newly
  checked todo item, **and in the same action flip the matching step checkbox in
  the todo file's per-class 9-step sub-checklist** (Rule 0016.6 — written at file
  creation; the file is the durable record, the session todos the live display).
  Never merge steps into fewer todos, never batch-check.
  N/A steps (e.g. 5/6 for a standalone `AREnum`) complete with the N/A reason.
  Step 9's todo completes only after the 9b user confirmation. All 9 completed —
  in the session todos **and** in the file's sub-checklist — is
  a precondition of the per-class commit (Rule 0017.2).
- **Finish (per class, after 9b):** once the user confirms Step 9b and the
  `# Spec verified:` marker is written — (1) commit the class's changes to the
  current feature branch (model source + mirrored test + parser/writer tests +
  parser + writer + deviation tracker + the todo file itself; message
  `feat: <ClassName> synced.`), (2) flip the todo row to `[x]` and record the
  commit hash in the same commit, (3) report and stop.
- **Termination:** after marking a row `[x]`, if **every** queue row is `[x]`, the
  sync is **finished** — report the summary (classes, commits, deviations). No
  further session needed. Any `[ ]` left → next session picks it up.

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
- **Exception — no own spec table (XSD-only class):** a class whose attributes exist
  **only** in an XSD (no PDF/markdown table) legitimately carries no `# Spec verified:
  R<YY>-<MM>` marker. When fully synced from the XSD with **no deviation**, it carries
  **`# XSD verified: <xsd-file>`** (e.g. `# XSD verified: AUTOSAR_00052.xsd`) with
  method rows `[x]` — treat it like a `Spec verified` class. Rows stay all-`[ ]` only
  if the class was **not** yet synced. `XSD verified` replaces `Spec verified` **only**
  when the class's information is XSD-exclusive; if a PDF/markdown table exists, use
  `# Spec verified: R<YY>-<MM>` (PDF authoritative, Rule 0015). It is *not*
  "unreviewed" — confirm the exception before treating a marker-less class as
  sync-from-scratch.

## Input

**Required:** `ClassName`. From it, locate:

| Artifact | Path |
|---|---|
| source | `src/armodel/models/M2/AUTOSARTemplates/<pkg>/<ClassName>.py` (leaf package → `<pkg>.py`; non-leaf package with subpackages → `<pkg>/__init__.py`. See Rule 0007) |
| model test | `tests/test_armodel/models/M2/AUTOSARTemplates/<pkg>/test_<ClassName>.py` → `class Test<ClassName>` — pairs 1:1 with source `<ClassName>.py` (Step 2) |
| parser test | `tests/test_armodel/parser/test_*.py` → `class Test*` (load with `ARXMLParser`, assert model fields; Step 5) |
| writer test | `tests/test_armodel/writer/test_*.py` → `class Test*` (set → save → reload round-trip; Step 5) |
| spec markdown | `grep "Table N.M: <ClassName>" autosar/R23-11/markdown/AUTOSAR_*_TPS_*.md` — **primary source for all text**: `Note` (→ docstrings), `Attribute`/`Base`, `Table N.M` id, table name (via filename). Covers **both** `CP_TPS` (Classic) and `FO_TPS` (Foundation) |
| spec PDF | `autosar/R23-11/pdf/AUTOSAR_*_TPS_*.pdf` — **opened only to read the page number** (`p.NN`); the markdown carries no page numbers |
| page-number script | `python .codebuddy/skills/sync-autosar-class/pdf_page.py <ClassName> [--pdf PATH] [--table <N.M>]` — finds `Table N.M: <ClassName>` across `autosar/R23-11/pdf/` and prints `p.NN` (cached per-PDF index; `--refresh` rescans). Use it in Steps 1/4 whenever the `# Spec:` line needs `p.NN` |
| deviation records | the project deviation tracker (format in *Rule 0014*) |
| XSD ground truth | `docs/requirements/xsd/` |

### The 9-step workflow (TDD, per class)

Runs once per class in the queue built by Phase 0 (Rule 0016), inside the session
loop above. Two Red→Green pairs: **2→3** (model) and **5→6** (reader/writer). Do
not write the implementation before its failing test. Each step is tracked as its
own session todo — created as a set of 9 before Step 1, checked off one at a time
as each step finishes (*Rule 0018*).

| Step | What | Rules | Phase |
|---|---|---|---|
| 1 | Sync members & description from the PDF by class name | 0001 (§§1.1–1.5, 1.11), 0007, 0015 | — |
| **2** | **Write the model class unit test** | 0006 | **Red** |
| **3** | **Implement the model class** | 0001 (§§1.6, 1.8, 1.10), 0003, 0004, 0005, 0008, 0009, 0010, 0011 | **Green** |
| 4 | Sync description — **wipe all old docstrings**, rewrite from markdown | 0012 (§§2–4) | — |
| **5** | **Write the reader/writer round-trip test** | 0006 | **Red** |
| **6** | **Update the parser (reader) & writer** | 0001 (§1.7), 0013 | **Green** |
| 7 | Update checklist comment (`# Spec:` + rows; **marker deferred to 9b**) | 0002 | — |
| 8 | Deviations ⇒ no `# Spec verified:` stamp | 0001 (§1.9), 0012 (§1), 0014 | — |
| 9 | Verify (9a) + confirm (9b) ⇒ **write `# Spec verified:`** | 0006, 0006.1 | — |

**Essence per step** (full detail in `rules.md`):

- **1** — Extract `Note`/`Base`/`Attribute` rows in displayed order; confirm Class-vs-Enumeration header. Run `python .codebuddy/skills/sync-autosar-class/pdf_page.py <ClassName>` for the `p.NN` page (the PDF is opened only for the page number). *Rule 0015* arbitrates XSD-vs-PDF/markdown attribute conflicts (the PDF/markdown table wins — model nothing the PDF lacks).
- **2** — `test_initialization` (defaults), `test_get_set_*` (round-trip + **None no-op**), `create*`/`add*` (append, duplicate returns existing). Abstract class → test `__init__` + base accessors via a concrete subclass.
- **3** — Most-derived base from the `Base` chain; dedicated typed-list fields for `*` `aggr` (never registry filters); `createXxx` only for `Referrable` children; collect referenced missing classes and report in Step 8 (don't block). Enum (`AREnum`) → literals, not accessors.
- **4** — **Wipe first, then rewrite.** Remove **all** existing docstrings — the class docstring, every method docstring (`__init__`, getters, setters, `create*`/`add*`), and every inline `__init__` member comment — so no stale wording survives a re-sync on renamed/removed/overlooked members (*Rule 0012.2.3*); keep the code, the `# Spec:` checklist block, and placeholder comments. Then copy the spec `Note` **verbatim from the markdown** into the **class docstring** (the class-level `Note` — **not** into `__init__`, which has no docstring), inline `__init__` **comments**, and getter/setter docstrings (page number via `pdf_page.py`, above); guarded setters append the None-no-op sentence. `__init__` members are declared as **PEP 526 annotated assignments** directly under their note comment — `self.foo: Optional[T] = None` / `self.foo: List[T] = []` — **never** a trailing `# type:` comment (*Rule 0003*).
- **5** — Reader/writer tests live in **their own folders** (`tests/test_armodel/parser/`, `.../writer/`, both `class Test*`), not the per-class mirror. Assert **field values**, not just `len(...) == n`; add an empty-wrapper-list case.
- **6** — Reader populates via mutators (`readXxx`→`set/create/addXxx`), writer reads via getters (`writeXxx`→`getXxx`); cover wrapper lists + polymorphic five-place dispatch; **no chained mutator calls**. All types form matched name pairs across layers — model `setX`/`getX`, structure `readX`/`writeX`, element `getX`/`setX`, leaf `getChildElementOptional<T>`/`setChildElementOptional<T>` (*Rule 0013.2*); a cross pair (`setX1` ↔ `getX2`) is incorrect.
- **7** — One row per method, source order, all `[x]`, 5-column format below. Writes the `# Spec:` line + method rows **only** — the `# Spec verified:` marker is added in Step 9b, never here.
- **8** — Record deviations; the `# Spec verified:` marker (added in 9b) is **withheld** while any placeholder/deviation remains; report the Step-3 referenced classes here.
- **9** — **(9a automated)** `pytest` + `flake8` + `ruff check` + `black-check` + the set-based script + a lossless integration round-trip (`npm run flake8` / `ruff-check` / `black-check` are the cross-platform forms). **Stop on any failure.** **(9b confirm — gate)** then present the **complete pre-stamp** rule-compliance checklist covering every check automation is blind to — element kind + every spec attr modeled (*0001.1*), most-derived base (*0001.2*), no fabrication/flattening + PDF-typed fields (*0001.3*), **Kind-suffix naming** `ref`→Ref/Refs·`tref`→TRef·`iref`→IRef/IRefs + singular `*`→plural (*0001.5*), create/set/add shape (*0001.6*), **reader+writer coverage** for every kept attr (*0001.7*), **member order** (*0011*), docstrings = spec `Note` **verbatim by diff** (*0012* **and** *0001.4* — every attribute's inline `__init__` comment + getter docstring + setter docstring must be the spec `Note` copied verbatim, not a "Gets/Sets the…" paraphrase or a truncated summary that drops the spec's full sentence), deviations resolved/removed (*0014*), stamp decision (*0012.1*) — and get explicit user confirmation; **when all pass, write the `# Spec verified:` marker in this step (9b)** — never in Step 4/7/8. Fix & re-present on any failure (*Rule 0006.1* has the full checklist). **Then finish the class per Rule 0017**: commit to the feature branch, flip the todo row to `[x]` with the commit hash, and stop the session (or, if all rows are `[x]`, report the sync complete).

**Workflow adaptations** (which steps still apply):

- **`AREnum`** — Step 2 tests member presence/values + instantiability
  (`MyEnum().setValue(MyEnum.MEMBER)`); Steps 5/6 are **N/A for a standalone enum** —
  it has no own XML element, so it is serialized as an attribute value on a *consuming*
  class and round-tripped there (*Rules 0010–0011*).
- **No own spec table (XSD-only class, e.g. a concrete `<name>InstanceRef`)** — Step 1
  derives attributes from the XSD group, not a PDF table; the checklist stays all `[ ]`
  with no `# Spec verified: R<YY>-<MM>` marker (*Rule 0002*). When fully synced from
  the XSD with no deviation, record provenance with `# XSD verified: <xsd-file>` (e.g.
  `# XSD verified: AUTOSAR_00052.xsd`) and flip method rows to `[x]`; `# XSD verified:`
  is used **instead of** `# Spec verified:` only when no PDF/markdown table exists for
  the class (*Rule 0002*).

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

**XSD-only class (no PDF/markdown table) — `# XSD verified:` variant.** Use
`# XSD verified: <xsd-file>` (e.g. `# XSD verified: AUTOSAR_00052.xsd`) **instead of**
`# Spec verified: R<YY>-<MM>`, and name the XSD in the `# Spec:` line. Apply it only
when there is no PDF/markdown table for the class; cross-check every attribute against
the XSD first, and withhold the marker if any deviation remains (Rule 0001.9):

```
# ClassName method parity checklist:
# Spec: (XSD-only - AUTOSAR_00052.xsd <GROUP> group; no own AUTOSAR table)
# XSD verified: AUTOSAR_00052.xsd
# Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
# [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
# [x] setFoo       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
# [x] getFoo       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
```

**Citation source:** the `# Spec:` table name, `Table N.M` id, and `Note` text come from
the **markdown** (`autosar/R23-11/markdown/AUTOSAR_*_TPS_*.md` — covers `CP_TPS` and `FO_TPS`);
only the `p.NN` **page** is read from the **PDF** (`autosar/R23-11/pdf/...` — look it up with
`pdf_page.py <ClassName>`) — the markdown carries no page numbers. In the `# Spec:` line,
`<Platform>` is `CP` (Classic) or `FO` (Foundation), taken from the spec markdown filename.

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
  **no docstring** (Rule 0012.2.4 / 0012.2.5.2).
- **Patching docstrings in place instead of wiping first** — a re-sync that edits only
  the docstrings it happens to re-read leaves stale old-release wording on renamed,
  removed, or overlooked members. Remove **all** docstrings (class + method + member
  comments) before writing the new ones from the markdown (*Rule 0012.2.3*).
- **Paraphrasing or truncating an attribute `Note`** — writing "Gets the X" / "Sets the
  X" in front of (or instead of) the spec `Note`, or a shortened summary ("Global
  reference to find an element…") that drops the spec's full sentence, is a *Rule 0001.4*
  violation even when the field/getter/setter/reader/writer are all correct. Tests,
  black, and ruff cannot catch it — diff every member docstring against its spec `Note`
  verbatim during 9b. This applies to **every** class in the queue, including unstamped
  member types consumed by a stamped class.
- **Trailing `# type:` comments instead of PEP 526 annotated members** — declaring a
  member as `self.foo = None  # type: Optional[T]` (or `= []  # type: List[T]`) instead of
  an annotated assignment `self.foo: Optional[T] = None` (or `self.foo: List[T] = []`)
  directly under its spec-`Note` comment is a *Rule 0003* violation even when the
  getter/setter signatures are correct; no automation catches it — check every
  `__init__` member's declaration form during 9b.
- **Keeping the queue only in the conversation** — the sync map that lives in
  conversation dies with the session, taking the Skip/XSD decisions and queue order
  with it. The queue lives in `docs/plan/sync-todo/<InputClassName>.md` (*Rule 0016.6*).
- **Re-running Phase 0 on resume** — a todo file for the class already exists ⇒ the
  closure was confirmed; read the file and take the first `[ ]` row. Re-running Phase 0
  re-asks the interactive gates for nothing (*Rule 0017.1*).
- **Re-deriving the queue from `# Spec verified:` stamps instead of reading the todo
  file** — stamps carry no queue order, no roles, no Skip/XSD decisions (*Rule 0017.4*).
- **Syncing a second class in the same session** — "context still feels fresh" is not
  evidence; the 9b verbatim diffs degrade silently under a loaded context. One class
  per session, then stop (*Rule 0017.1*).
- **Marking a todo row `[x]` before the commit exists** — the row records the commit
  hash; no commit, no `[x]`. Deferring the commit to "the end of all classes" loses a
  session's work when it dies (*Rule 0017.2*).
- **Merging the 9 steps into fewer session todos, or batch-checking them** —
  "Steps 2+3 model TDD" as one todo, or checking several step todos at once after
  the fact, hides a skipped/half-finished step until 9b or never. One step = one
  todo, checked the moment the step finishes (*Rule 0018*).
- **Writing the todo file without the per-class 9-step sub-checklist** — or
  deferring it to "when the first class starts" — recreates the original failure:
  the steps exist only in the ephemeral session and vanish on session death. The
  sub-checklist is written at file creation in Phase 0 and flipped per step
  (*Rules 0016.6, 0018.2*).

| Rationalization | Reality |
|---|---|
| "Simple model — I'll implement then test" | A test written after mirrors the code, not the spec. Step 2 first. |
| "Reader/writer first, round-trip test after" | No failing round-trip ⇒ can't see dropped elements. Step 5 first. |
| "It's just docstrings, skip Step 4" | Drift is silent; the marker then certifies wrong wording (*Rule 0012*). |
| "The docstrings mostly look right — I'll just patch the ones that changed" | In-place patching leaves stale sentences on members you didn't re-read; wipe all docstrings first, then rewrite from the markdown (*Rule 0012.2.3*). |
| "Gets/Sets the X is close enough to the spec Note" | A paraphrase or truncation is a *Rule 0001.4* violation the automation can't catch; copy the spec `Note` verbatim per member (inline comment + getter + setter) and diff it. |
| "A `# type:` comment documents the member type just fine" | Verified classes annotate members directly (PEP 526) under the spec `Note`; trailing `# type:` comments on bare assignments are a *Rule 0003* violation. |
| "The closure looks right, I'll skip the confirm gate" | Over/under-collection wastes every later step; present the set and let the user confirm (*Rule 0016.2*). |
| "Tests pass and the round-trip is clean — I can stamp and move on" | Those don't certify a class (Rule 0012.1); run Step 9b on the blind-spot rules before stamping (*Rule 0006.1*). |
| "The class already has `# Spec verified:` stamped — I'll skip 9b" | The marker is the *output* of 9b, not a substitute; on re-sync/drift re-run the full 9b checklist — a stale marker certifies nothing (*Rule 0006.1*, *Rule 0012.3*). |
| "I'll keep the queue in the conversation — writing a file is overhead" | The conversation dies with the session; the queue, order, roles, and Skip/XSD decisions are lost. The todo file is the queue (*Rule 0016.6*). |
| "Session died — I'll rebuild the queue by grepping the stamps" | Stamps carry no order/roles/Skip-XSD decisions; read `docs/plan/sync-todo/<ClassName>.md` instead (*Rule 0017.4*). |
| "Context still feels fresh — I'll sync the next class in this session" | 9b verbatim diffs degrade silently under loaded context; one class per session (*Rule 0017.1*). |
| "I'll commit everything at the end of the whole sync" | A session death then loses every finished class's work; commit per class, right after 9b (*Rule 0017.2*). |
| "One todo for the class is enough — or I'll check them all at the end" | The step todos exist to expose a skipped/half-finished step in real time; batch-checking shows progress the work doesn't have. 9 todos, one check per finished step (*Rule 0018*). |
| "9b re-verifies everything anyway — I'll check off step todos as 'done' when the class finishes" | 9b verifies the class against the rules; step todos verify the workflow was walked. Step 9's todo completes only on 9b confirmation, the others at their own finish (*Rule 0018*). |

## References

- **Rules (self-contained):** `rules.md` in this skill folder — *Rule 0001*–*Rule 0018*.
- Coding standards: `docs/development/coding_rules.md`.
- Spec markdown (primary — source of all text: `Note`, `Table N.M` id, table name): `autosar/R23-11/markdown/AUTOSAR_*_TPS_*.md` (`CP_TPS` + `FO_TPS`).
- Spec PDFs (opened only for the `p.NN` page number): `autosar/R23-11/pdf/AUTOSAR_*_TPS_*.pdf`.
- XSD ground truth: `docs/requirements/xsd/`.
