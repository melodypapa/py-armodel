# Group15 review — `sync-autosar-class` rule compliance

**Date:** 2026-10-03
**Subject:** `docs/plan/sync-todo/Group15.md` — all 24 class rows, every row `[x]`-stamped
**Scope:** review only. No source, queue, or tracker file was modified by this audit.
**Tree state:** audited in worktree `.g16-wt` at `982c067ce`; re-verified on `main` at `1bf2f90be` (PR #913, the merge that retired the worktree). All findings below reproduce on `main`.
**Rules enforced:** `.agents/skills/sync-autosar-class/rules.md` — Rules 0002, 0006, 0008, 0011, 0012, 0014, 0016.7, 0017.2, 0017.4, plus 0001.3/0001.4/0001.5/0001.6/0001.7/0001.11.

---

## Verdict

| Area | Result |
|---|---|
| Spec fidelity (Rule 0001, 0012) | ✅ clean — 23/23 table classes + 1 XSD-only |
| Reader/writer coverage (Rule 0001.7) | ✅ clean — 0 real drift across 24 classes |
| Checklist parity (Rule 0002) | ❌ **2 classes** |
| Queue hygiene (Rules 0014, 0016.7, 0017.2, 0017.4) | ❌ **6 findings** |
| Formatting (Rule 0008) | ❌ **1 class** |
| Gates | ✅ all green except `regen --check` (Group16-only cause) |
| Arbitration items | 3 |

**Bottom line:** the *substance* is sound — spec fidelity and reader/writer coverage, which are the hard parts, are genuinely clean. Every defect is in the *bookkeeping*: two checklists describing methods that do not exist, one wrong commit hash, one duplicated step block, two overclaimed markers, two dangling references.

---

## 1. Violations

### V1 — Rule 0002, `TransmissionModeDeclaration` — 6 bogus rows, 6 unlisted methods

`src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/Timing.py:345-350`

The checklist rows name singular `setXxx` methods that **do not exist**. The real API is the list shape:

| Checklist rows (bogus) | Actual methods (unlisted) |
|---|---|
| `getModeDrivenFalseCondition`, `setModeDrivenFalseCondition` | `getModeDrivenFalseConditions`, `addModeDrivenFalseCondition` |
| `getModeDrivenTrueCondition`, `setModeDrivenTrueCondition` | `getModeDrivenTrueConditions`, `addModeDrivenTrueCondition` |
| `getTransmissionModeCondition`, `setTransmissionModeCondition` | `getTransmissionModeConditions`, `addTransmissionModeCondition` |

The row is `[x]`-stamped, so the "checklist rows == methods" gate was never actually exercised for this class. Row at `Group15.md:321`.

### V2 — Rule 0002, `TriggerIPduSendCondition` — 1 bogus row, 1 unlisted method

`Timing.py:460` carries a row for `getModeDeclarations`, which is not a method. The real `getModeDeclarationRefs` has no row. Row at `Group15.md:246`.

### V3 — Rule 0017.2, `EventControlledTiming` cites the wrong sync commit

`Group15.md:271` records `sync commit 1649678501`.

```
1649678501 → 164967850186422c338e42389b0be7a804de97ca
             2026-08-10  feat(model): sync TextModel spec and add SignalServiceTranslation support
```

The hash *resolves* — that is the trap. It points at an unrelated commit predating this class's work by six weeks. The row's own steps-1-8 commit is `dcbc6abdb`, and its 9a run is dated 2026-09-27/28. The value looks like a Unix timestamp paste (1649678501 = 2022-04-11) that happens to prefix-match a real commit.

Blast radius beyond Group15 — the same bogus hash appears in:

- `docs/plan/sync-todo/SyncTodoIndex.md` — 3 lines (`EventControlledTiming`, `FloatEnum`, `PgwideEnum`)
- `docs/plan/sync-todo/sync-report.md` — 3 lines (same three classes)

`FloatEnum` and `PgwideEnum` are Group22 rows citing the identical "sync commit", so those two are wrong as well.

**All 27 other hashes cited by Group15 resolve correctly.**

### V4 — `TimeRangeTypeTolerance` row has a duplicated, self-contradicting step block

`Group15.md:210-231`

- **Two complete Step 1–9 sets** — block A at lines 212–220, block B at lines 223–231. Every step number appears exactly twice (`{1:2, 2:2, … 9:2}`).
- **Step 5/6 marks contradict**: `[x]` in block A vs `[—]` in block B.
- Block B's Step 9 (line 231) asserts *"row's duplicated blocks normalized into this single record"* — **self-refuting: both blocks are still present.**
- Row header (line 210) claims `stamped # Spec verified: None` — wrong marker *kind* and wrong *value*. Source carries `# XSD verified: AUTOSAR_00052.xsd` (correct for an XSD-only class; block A's Step 9 at line 220 says so correctly).

### V5 — Rule 0014, 23 of 24 classes have no deviation-tracker entry

Only `MultiplexedIPdu` has a `## \`MultiplexedIPdu\`` heading in `docs/examples/method_deviation_by_class.md`. Rule 0014 (`rules.md:1141`) is explicit:

> A class with no deviations records `No deviations — …` with a one-line summary.

So a missing entry is a gap even for a deviation-free class. See **A3** — repo-wide compliance is only 44%, so this is both a real gap and a rule-vs-practice item.

### V6 — Step 9 overclaims an `# XSD verified:` marker (2 rows)

| Row | Line | Step 9 claims | Source actually has |
|---|---|---|---|
| `CommunicationDirectionType` | 31 | `` `# Spec verified: R23-11`/`# XSD verified: AUTOSAR_00052.xsd` written in source `` | `Spec verified: R23-11` only |
| `CyclicTiming` | 269 | same | `Spec verified: R23-11` only |

Neither class carries an XSD marker, and neither should — both are spec-table classes. Only `TimeRangeTypeTolerance`, `AbsoluteTolerance`, and `RelativeTolerance` legitimately carry `# XSD verified: AUTOSAR_00052.xsd`. **The source is correct; the Step 9 record overclaims.**

### V7 — Rule 0016.7, 13 row lines exceed ~200 characters

`rules.md:1415`: *"A class-row line longer than roughly 200 characters is a signal this rule is being violated."* The write-up belongs on its own bullet directly under the row.

| Row | chars | Row | chars |
|---|---|---|---|
| `SecuredPduHeaderEnum` | 311 | `TriggerIPduSendCondition` | 207 |
| `TriggerMode` | 298 | `CommunicationDirectionType` | 207 |
| `TransmissionModeDeclaration` | 210 | `TimeRangeTypeTolerance` | 206 |
| `TransmissionModeCondition` | 208 | `TransmissionModeTiming` | 205 |
| `EventControlledTiming` | 208 | `ISignalIPduGroup` | 203 |
| `ISignalPort` | 202 | `TransferPropertyEnum` | 201 |
| | | `DynamicPart` | 201 |

Rule 0016.7 exists because long checkbox lines are hard to toggle with exact-line edits — on Group 4 (2026-09-18) six fully-synced rows stayed stuck at `[ ]` for a whole session because of this.

### V8 — Step 8 `see below` is a dangling reference (2 rows)

10 rows say `Step 8 — Deviations — see below`. Two have **no note bullet anywhere** in the block:

- `CyclicTiming` — `Group15.md:268`
- `TransmissionModeTiming` — `Group15.md:318`

The other 8 do have a note bullet — but it sits **above** Step 8 (as a `- note (Step 8):` bullet placed before Step 1), so the direction word "below" is wrong for all 10. Only for these 2 is the reference content-free.

### V9 — Rule 0008, `MultiplexedIPdu` — blank line between each comment and its member

All 7 `__init__` members have `# comment` / *blank* / `self.x = …`:

```
        # According to the value of the selector field ...

        self.dynamicPart: Optional[DynamicPart] = None
```

Repo-wide scan: **7 of 3703 annotated members**, all in this one class. Rule 0008 (`rules.md:840-846`) treats `comment + assignment` as a single block with a blank line *around* it — a blank *inside* the block detaches the comment from its field. This is also the reason a naive "member has an inline comment" checker reports all 7 members as uncommented.

It is invisible to every automated gate: Black leaves contiguous comment blocks untouched and ruff's `E303` caps the *maximum* blank count but enforces no minimum. Rule 0008 flags this as **manual-only**.

### V10 — Rule 0006 (minor), `TimeRangeTypeTolerance` has no mirror test file

There is no `test_TimeRangeTypeTolerance.py`. Coverage does exist — `tests/.../CoreCommunication/test_TimeRangeType.py` defines `class TestTimeRangeTypeToleranceChoice` (line 89) and exercises the class through concrete subclasses `AbsoluteTolerance`/`RelativeTolerance`, which is the correct abstract-class pattern under Rule 0006. Only the file-naming convention (`test_<ClassName>.py`) is unmet.

---

## 2. Verified clean

- **Spec tables** — all 23 table classes match their markdown table: member set, displayed row order, multiplicity→annotation (`Optional` / `List` / plain), ref-kind `Ref` suffixes, class docstrings verbatim (including required `constr_*` appends), enum literals exact, `Base` = most-derived, getter/setter docstrings verbatim.
- **Page-split tables** — Tables 6.5 (`ISignalPort`), 6.32 (`ISignalIPduGroup`), 6.72 (`MultiplexedIPdu`), 6.43 (`SecuredPduHeaderEnum`) have their caption **inside** the table, split across a page break. A naive caption-adjacent extraction returns phantom `EXTRA` / `NOT FOUND` errors. Reconstructing the table across image/glyph interruptions confirms a clean match in all four.
- **Reader/writer coverage** — all 24 classes consistent once `self.` parser-helper calls are excluded. The split convention (getter row `writer=x`, setter row `reader=x`) is correct throughout.
- **Rule 0001.6** (`createXxx` vs `setXxx`) — `dataFilter`, `staticPart`, `dynamicPart` all have spec `Base` = `ARObject`-derived, **not** Referrable/Identifiable, so `setXxx` is the correct shape and no `createXxx` factory is required.
- **XSD-only exception gate** — `TimeRangeTypeTolerance` correctly uses the `# Spec: XSD group TIME-RANGE-TYPE-TOLERANCE, AUTOSAR_00052.xsd line 122919 (XSD-only; …)` citation form with `# XSD verified: AUTOSAR_00052.xsd`.
- **Checklist shape** — 6-column format with release column present on all 24; every row's `reader`/`writer` cell is `[x]` or `[—]`; row order matches source method order in all 24 (including the two classes whose *names* are wrong — the count and order are right, the identifiers are not).

---

## 3. Ruled out (false positives)

Each of these looked like a violation and was checked against source before being dismissed.

1. **"Stale `[—]`" on `getSecureCommunicationProps`, `getDataFilter`, `getCyclicTiming`, `getISignalIPduRefs`, `getValue`.** The parser defines its own same-named helpers (`self.getDataFilter(child_element, "DATA-FILTER")`), so a `\.getX(` scan matches the parser, not the model. Call-site inspection confirms every receiver.
2. **Spec `EXTRA` / `NOT FOUND` for Tables 6.5, 6.32, 6.72, 6.43, 6.76.** Page-split caption trap (§2). Table 6.76 additionally reads `MultiplexedPart (abstract)` in the `Class` cell, which fails an exact-name guard.
3. **Enum literal "mismatches".** PDF wrap-spaces inside literal cells — `triggeredOnChange WithoutRepetition`, `staticOrDynamic PartTrigger`, `securedPdu Header08Bit`. De-splitting is forced (Python identifiers cannot contain spaces); squashed comparison matches. Prose and docstrings correctly retain the wrap-spaces verbatim.
4. **`MultiplexedPart` docstring ≠ spec `Note`.** It *is* the `Note` plus the `[constr_9181]` block appended verbatim, which Rule 0012.2.4 requires.
5. **`obj.__init__` / `obj.getValue` parser hits.** `def __init__(self, options=None)` is a definition, not a call; the `getValue` receiver is `SwCalibrationAccessEnum`, not `TimeRangeType`. `readTimeRangeType` only calls `setValue`.
6. **`class MultiplexedPart(ARObject, ABC)` vs spec `Base ARObject`.** The `ABC` mixin is the abstract guard, as the row note records.
7. **Enum literal `Tags:` tails (6 classes, 20 comment lines).** **Rule 0011 explicitly requires them:** *"Each member has an inline comment citing the literal's description + Tags (`atp.EnumerationLiteralIndex=N`)."* `CommunicationDirectionType`, `TransferPropertyEnum`, `TriggerMode`, `SecuredPduHeaderEnum`, `FlexrayChannelName`, `PncGatewayTypeEnum` are **compliant**, not stale.
8. **Class-docstring `Tags:` tails (7 classes).** Rule 0012 requires the class `Note` verbatim, and the markdown `Note` cells themselves contain the `Stereotypes:`/`Tags:` text — so keeping them is the verbatim behaviour. `SecuredIPdu`, `UserDefinedIPdu`, `UserDefinedPdu` fall only in this category and are clean.
9. **`regen_sync_todo.py --check` failing.** Not a Group15 issue — see §5.
10. **`TimeRangeTypeTolerance` "no mirror test"** as a coverage gap — coverage exists (see V10, which is only the file-naming convention).

---

## 4. Arbitration items (rule vs. practice)

### A1 — List accessor pair order: Rule 0001.11 vs 47% of the repo

Rule 0001.11 (`rules.md:336-343`) is explicit that within one attribute the pair order depends on accessor shape:

> scalar `getXxx`/`setXxx` → **getter first**; list/aggregated `addXxx`/`getXxxs` or `createXxx`/`getXxxs` → **mutator first**

Group15 has **9 getter-first list pairs across 5 classes** — i.e. it follows the shape the rule forbids:

| Class | Getter-first pairs |
|---|---|
| `MultiplexedPart` | `getSegmentPositions` < `addSegmentPosition` |
| `DynamicPart` | `getDynamicPartAlternatives` < `addDynamicPartAlternative` |
| `ISignalIPduGroup` | `getContainedISignalIPduGroupRefs`, `getISignalIPduRefs`, `getNmPduRefs` |
| `TriggerIPduSendCondition` | `getModeDeclarationRefs` < `addModeDeclarationRef` |
| `TransmissionModeDeclaration` | `getModeDrivenFalseConditions`, `getModeDrivenTrueConditions`, `getTransmissionModeConditions` |

Repo-wide measurement: **247 getter-first vs 279 mutator-first pairs (47% / 53%) across 150 classes.** The rule does not describe the majority convention, so this needs a decision before it can be called a violation on any single class.

### A2 — `Tags:` in `__init__` comments: Rule 0012 *verbatim* vs Rule 0012.2.5 step 5.2 *drop*

The ruleset is in tension here, and the spec text is what creates it. The markdown `Note` cells literally contain the tail:

```
| ddsQosProfile | DdsCpQosProfile | 0..1 | … | Reference to the DDS Qos profile used for this ISignal. Tags: atp.Status=candidate
| physicalProps  | SwDataDefProps  | 0..1 | … | Specification of the physical representation. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalProps
```

- **Rule 0012:** copy the `Note` **verbatim** — never summarize or rephrase.
- **Rule 0012.2.5 step 5.2** (`rules.md:985-986`): the inline `__init__` comment is the attribute's `Note` copied verbatim **(drop `Stereotypes:`/`Tags:` tail)**.

Group15 chose *keep* in **4 classes** — `ISignalPort` (1 comment), `ISignalIPduGroup` (2), `MultiplexedIPdu` (2), `SystemSignal` (1):

| Class | Queue records Tags decision? |
|---|---|
| `ISignalIPduGroup` | ✅ Step 9 `Group15.md:106`: *"9b user-confirmed 2026-10-02 — Note (incl. Tags) verbatim"*; commit bullet `:97` *"verbatim Note incl. Tags"* |
| `SystemSignal` | ✅ Step 9 `Group15.md:195`: *"9b user-confirmed 2026-10-02 — Note (incl. Tags) verbatim"* |
| `ISignalPort` | ⚠️ Step 9 says *"Note + 5 attr Notes verbatim"* — implies keep, does not call out Tags |
| `MultiplexedIPdu` | ⚠️ Step 9 says *"7 attr Notes verbatim (markdown wrap-spaces kept)"* — implies keep, does not call out Tags |

Two are explicitly user-confirmed at 9b; two are only implied by a "verbatim" claim. This is the same arbitration item surfaced in the Group16 review (where 171/172 stamped enums keep their tails) — it should be decided once, for the whole repo.

**Recommendation:** decide whether step 5.2's *drop* survives, and if it does, whether "verbatim" in Step 9 must be restated as "verbatim minus tail". Either way, `ISignalPort` and `MultiplexedIPdu` need an explicit confirmation line to match the other two.

### A3 — Rule 0014 tracker coverage: the rule vs 44% repo-wide

Group15 sits at **1/24 (4%)** tracker headings. But the rule is broadly unenforced:

| Group | Headings / stamped rows | | Group | Headings / stamped rows |
|---|---|---|---|---|
| Group4 | 28/28 | | Group22 | 17/57 |
| Group23 | 36/49 | | Group6 | 28/45 |
| Group13 | 19/23 | | Group10 | 2/32 |
| Group16 | 13/15 | | Group11 | 0/24 |
| **Group15** | **1/24** | | Group12 | 0/15 |

**Repo-wide: 320 of 721 stamped rows (44%)** have a tracker heading. So the rule text and the practice diverge sharply, and Group15 is at the bottom of the distribution. Worth fixing for Group15 specifically (its `No deviations — …` entries are cheap to write), but the rule-vs-practice gap should be settled at the same time as A1/A2.

---

## 5. Queue hygiene — notes not attributable to Group15

### Rule 0017.4 placeholder residue (6 rows — confirmation *is* present)

Lines **31, 269, 294, 307, 319, 332** carry:

```
9b deferred to batch confirmation (user instruction) — 9b user-confirmed 2026-10-02
```

All six immediately follow the placeholder with the actual confirmation, so the rule's core prohibition — writing the placeholder *instead of* capturing the confirmation — is **satisfied**. This is stale text left from a deferred batch, not an open violation. Cleanup only: rows `CommunicationDirectionType`, `CyclicTiming`, `FlexrayChannelName`, `PncGatewayTypeEnum`, `TransmissionModeTiming`, `TransmissionModeDeclaration`.

### `regen_sync_todo.py --check` fails (exit 1) — Group16 rows only

The checker reports `sync-report.md differs`; **every changed class row is Group16 (22 rows)** — e.g. `CouplingPortAbstractShaper` Deferred→Done, `IPSecConfig`, `NetworkEndpoint`, `SdServerConfig`. **Zero Group15 rows are implicated** — every Group15 row matches between the queue and the report.

Cause: the `origin/main` merge at `982c067ce` resolved `sync-report.md` (it was in `UU` conflict state) to a state stale relative to `Group16.md`. Not a Group15 defect; needs a `regen_sync_todo.py` run on the Group16 side.

---

## 6. Gate results

| Gate | Result |
|---|---|
| Unit tests `pytest tests/test_armodel/` | ✅ **17483 passed**, 0 failed |
| `ruff check` (FibexCore) | ✅ All checks passed |
| `black --check -l 200` (FibexCore) | ✅ 4 files would be left unchanged |
| `mypy` | ✅ Success: no issues found in 268 source files |
| `scripts/eval_skill_static_checks.py` | ✅ All mechanical checks passed |
| `scripts/regen_sync_todo.py --check` | ❌ exit 1 — **Group16 rows only** (§5) |

`eval_skill_static_checks.py` emits 3 stale-stamp notes — `SenderReceiverAnnotation`, `AtomicSwComponentType`, `AbstractAccessPoint` — all in `SWComponentTemplate`, none in Group15.

**Environment note:** when this review began the worktree was mid-merge (`UU sync-report.md`, `UU TcpOptionFilterSet.py`, conflict markers producing 769 test-collection errors). The concurrent session completed the merge as `982c067ce` during the audit; every finding above was re-run against post-merge content, then again on `main`. Nothing was staged, committed, or restored.

---

## 7. Method

Four scripted audits, each keyed off `docs/plan/sync-todo/Group15.md` rather than a hand-maintained class list:

1. **Structural (AST)** — checklist 6-column shape, checklist rows ↔ source methods (set, names, order), `__init__` docstring absence, blank-line adjacency, most-derived base, `Tags:` tail inventory.
2. **Spec cross-check** — reconstructs each class's markdown table (handling leading, trailing, and *page-split* captions), then compares member set/order, multiplicity→annotation, ref-kind suffixes, enum literal values, class/getter/setter docstring verbatimness, `constr_*` appends.
3. **Reader/writer coverage** — every checklist `reader`/`writer` cell against actual parser/writer call sites, excluding `self.` receivers.
4. **Queue hygiene** — row line lengths, step-block completeness/duplicates/contradictions, commit-hash resolution *and subject relevance*, `9b` placeholder text, tracker headings, marker claims vs. source.

Audit scripts live in the session temp directory and are not committed.

---

## 8. Suggested fix order

1. **V1, V2** — rewrite the two checklists to the real method names (source is correct; only the comment blocks are wrong).
2. **V3** — correct the `EventControlledTiming` commit in `Group15.md:271`, and the two Group22 rows in `SyncTodoIndex.md` / `sync-report.md`.
3. **V4** — collapse the `TimeRangeTypeTolerance` duplicate step block, fix the header marker claim to `# XSD verified: AUTOSAR_00052.xsd`.
4. **V6, V7, V8** — bookkeeping edits in `Group15.md`.
5. **V9** — remove the blank lines in `MultiplexedIPdu.__init__` (manual; no gate catches it).
6. **V5 / A3, A1, A2** — tracker entries plus the three rule-vs-practice decisions, ideally settled repo-wide rather than per-group.
7. **V10** — either add `test_TimeRangeTypeTolerance.py` or record the co-location as an accepted deviation.
