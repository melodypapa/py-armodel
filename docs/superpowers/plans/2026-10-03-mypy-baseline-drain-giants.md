# Mypy Baseline Drain — Giants (3 modules, ~2703 errors) + middle-tier verification

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** (0) Verify and commit the 7-module middle-tier drain already sitting uncommitted on `feature/mypy-baseline-drain-middle`, then (1) drain the last 3 baseline modules — `ARPackage.py` (338), `arxml_writer.py` (1078), `arxml_parser.py` (1287) — keeping `uv run mypy` green after every commit, and finally (2) delete the `[[tool.mypy.overrides]]` block entirely.

**Architecture:** Same cluster-then-delete loop as the tail plan (`2026-10-03-mypy-baseline-drain-tail.md`), scaled up: fix one error family per batch, verify, commit. At this scale the mypy message itself is the per-site spec (it names the expected type), so batches are driven by a regenerated inventory, not pre-enumerated line lists. Model classes are spec-stamped — never widen/change model setter/getter signatures; the drain boundaries are the parser, the writer, and ARPackage's own lookup helpers.

**Tech Stack:** Python 3.8 typing ONLY (`typing.Optional[T]`, `typing.List[T]`, `typing.cast`, `typing.Union`, `typing.Any` — never `T | None`), mypy (uv), pytest (uv), Black 200 chars, npm lint.

---

## Evidence base (inventory captured 2026-10-03)

Config for inventory (bypasses the baseline overrides):
`printf '[mypy]\nfiles = src/armodel\nignore_missing_imports = True\nwarn_redundant_casts = True\nwarn_unused_ignores = True\n' > /tmp/mypy-giants.ini`
then `uv run mypy --config-file /tmp/mypy-giants.ini 2>&1 | grep "error:" > /tmp/giant-errors.txt`

| File | arg-type | assignment | return-value | union-attr | attr-defined | valid-type | other |
|---|---|---|---|---|---|---|---|
| ARPackage.py | 77 | — | 258 | — | — | 1 | operator 1, no-redef 1 |
| arxml_writer.py | 759 | 171 | — | 143 | 1 | 4 | — |
| arxml_parser.py | 766 | 392 | 99 | 8 | 21 | — | str-format 1 |

## Global conventions (apply to every task)

1. **Inventory loop:** regenerate `/tmp/giant-errors.txt` (command above) at the start of every batch; group that batch's sites from it. Confirm the fixed families disappear before committing.
2. **Verification per batch (in order):**
   - `uv run mypy` → `Success: no issues found in 268 source files`
   - `uv run pytest tests/test_armodel -x -q` → all pass
   - Integration roundtrip gate: `uv run pytest tests/integration_tests -q` (committed `test_files/` must pass; the 8 known failures under gitignored `custom_files/` are pre-existing and out of scope)
   - `npm run lint` → `All checks passed!`
   - `uv run black --check <files touched in this batch>` (fix with `uv run black <files>`)
3. **Commit format:** `fix(mypy): drain <family> from <file>` — one commit per batch. Never add AI attribution.
4. **Do NOT touch** spec-stamped model setter/getter signatures (Exception: Task 1 Task C adds a genuinely missing accessor — see there). Do NOT re-sort imports in `arxml_parser.py` / `arxml_writer.py` / `models/**` (I001/E402 intentionally disabled; order avoids circular imports).
5. **cast imports:** extend the file's existing `from typing import ...` line; never a second typing import.
6. **No speculative refactors.** Every edit exists to silence a specific mypy message; runtime behavior must be unchanged (roundtrip tests are the guard).

## The recipes (one per error family)

**Recipe G-A — ARPackage create/lookup return (258 `return-value`):** every `createXxx(self, short_name) -> X` ends with `return self.getReferrableElement(short_name, X)` where the helper returns `Referrable`. Non-None is a construction post-condition (element just created or exists-guarded), so wrap:

```python
return cast(X, self.getReferrableElement(short_name, X))
```

`X` = the method's declared return type = the "expected" type in the mypy message. Add `cast` to the typing import once.

**Recipe G-B — ARPackage filter-lambda (77 `arg-type`):** convert to isinstance-narrowed comprehension (established pattern from prior batches):

```python
# before
return list(filter(lambda a: isinstance(a, X), self.referrableElements))
# after
return list(a for a in self.referrableElements if isinstance(a, X))
```

**Recipe W-A — writer callee param widening (759 `arg-type`):** the errors are Optional getter results passed into writer methods whose bodies already None-guard (e.g. `setMultiLanguageOverviewParagraph` does `if paragraph is not None:`). Widen the callee's parameter to `Optional[X]` — one signature edit fixes every call site of that method (191 distinct callees). For each callee: (1) change the param annotation to `Optional[X]`; (2) confirm the body guards None — if it does not, add the guard from the existing sibling pattern; (3) do NOT change the body's logic otherwise. Works from the highest-count callees first (setChildLimitElement 14, setAutosarVariableRef 10, ... full list in `/tmp/giant-errors.txt`). Some arg-type sites are not callee-widening material (`dict.get` with `Any | None` keys, `str` locals) — route those to Recipe W-B instead.

**Recipe W-B — writer assignments / non-widening arg-types (~171 + str leftovers):** local variables assigned `Any | None` / `X | None` then used as bare types. Hoist the getter to a local and None-guard, or annotate the local honestly:

```python
# before
child_element.attrib["L"] = name.getL()          # getL() -> str | None, two calls, no narrowing
# after (W-C hoist, also fixes union-attr)
l_value = name.getL()
if l_value is not None:
    child_element.attrib["L"] = l_value
```

**Recipe W-C — writer union-attr (143):** same hoist-and-guard as W-B — the getter is called twice (once in the `if`, once in the body); hoisting to a local both narrows and removes the duplicate call. Runtime-equivalent; roundtrip verifies.

**Recipe W-D — writer `ET.SubElement` annotations (4 `valid-type`):** annotation typo — `def writeCode(self, element: ET.SubElement, ...)` uses a function as a type. Change to `ET.Element`.

**Recipe P-A — parser arg-type casts (766):** parser helpers return generic literals (`getChildElementOptionalLiteral -> Optional[ARLiteral]`) or `Optional[X]` while model setters want subclasses (`setIssuedBy(Optional[String])` — `String(ARLiteral)` confirmed). Models are spec-stamped, so cast at the call site; the expected type comes verbatim from the mypy message:

```python
# before
revision.setIssuedBy(self.getChildElementOptionalLiteral(element, "ISSUED-BY"))
# after (expected type from message)
revision.setIssuedBy(cast(String, self.getChildElementOptionalLiteral(element, "ISSUED-BY")))
```

Justification invariant: the cast documents "the XML schema says this element holds a String" — same category as the create-method post-condition casts.

**Recipe P-B — parser assignments (392):** dominant pattern is elif-chain variable reuse (`needs = BswMgrNeeds(...)` then reassigned sibling subclasses). Fix without behavior change: drop the shared variable — inline construction into the read call — or annotate the first binding with the common base type when later code reads it. Choose per site by what the surrounding code actually uses.

**Recipe P-C — parser return-value (99):** `getAdminData`-style helpers return `X | None` (element may be absent) annotated `-> X`. Prefer honesty: change to `Optional[X]` and let mypy reveal callers; callers already guard or feed Optional-tolerant APIs (verify per ripple). If a caller provably requires non-None with a guard upstream, a `cast` at that helper's return is acceptable — never both.

**Recipe P-D — parser attr-defined (21, investigate first):** parser calls setters that do not exist on the model class (e.g. `ClientServerAnnotation.setSignalFan`, `setAge`, `setTriggerRef`, ... around L7665). These are real defects, not annotation noise. For each of the 21 sites: check the model class and its spec-stamp checklist — if the member is a spec member the model is missing, that is a sync gap (fix the model per the sync-autosar-class skill conventions); if the parser is stale (method renamed/removed), fix the parser call. Document each decision in the commit message.

---

### Task 0: Verify and commit the middle-tier work already in the tree

**State:** branch `feature/mypy-baseline-drain-middle`; modified: `pyproject.toml` (7 baseline lines deleted), `cli/arxml_dump_cli.py`, `parser/abstract_arxml_parser.py`, `parser/connector_xlsx_parser.py`, `parser/ecuc_parser.py`, `parser/os_ecuc_parser.py`, `report/connector_xls_report.py`, `writer/abstract_arxml_writer.py`; `uv run mypy` already green.

- [ ] **Step 1:** Run the full verification gates (conventions step 2).
- [ ] **Step 2:** Fix anything the gates surface (scoped to the 7 touched files; recipes above apply).
- [ ] **Step 3:** Commit — `fix(mypy): drain 7 middle-tier modules from mypy baseline` (all 8 files in one commit; pyproject deletion included).
- [ ] **Step 4:** Update the tail plan's successor note if any middle module needed a fix beyond what the working tree already contains.

### Task 1: ARPackage.py — 338 errors, 3 families

**File:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py`

- [ ] **Step 1 (Task A, Recipe G-A):** cast all 258 create-method returns. Batch by file region (Diagnostic\* ~L650–L1000 is the dense block). Add `cast` to the typing import.
- [ ] **Step 2 (Task B, Recipe G-B):** convert all 77 `filter(lambda a: isinstance(a, X), self.referrableElements)` sites to comprehensions.
- [ ] **Step 3 (Task C):** fix the `InterpolationRoutineMappingSet` triple (L2571 valid-type, L2574 operator, L4455 no-redef): the delayed import at L4455 resolves to the *submodule* `...MeasurementAndCalibration.InterpolationRoutineMappingSet` (mypy error text confirms), shadowing the class re-exported by the package `__init__`. Change L4455 to import the class from its concrete module: `from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutineMappingSet import InterpolationRoutineMappingSet  # noqa: E402`. Re-run mypy; if the no-redef persists, diff the two resolutions at execution time and pick the import that satisfies all three sites.
- [ ] **Step 4: Verify** (conventions step 2, including the integration gate — ARPackage is on every roundtrip path).
- [ ] **Step 5:** `uv run mypy --config-file /tmp/mypy-giants.ini 2>&1 | grep "ARPackage.py" | wc -l` → 0, then delete the `ARPackage` line from `pyproject.toml`, re-run `uv run mypy` → green.
- [ ] **Step 6: Commit** — `fix(mypy): drain ARPackage from mypy baseline`

### Task 2: arxml_writer.py — 1078 errors, 5 families

**File:** `src/armodel/writer/arxml_writer.py`

- [ ] **Step 1 (Recipe W-A, batches by callee count):** widen Optional-receiving writer method params, highest-count callees first. Suggested commits: batch 2a = all callees with ≥4 error sites (~60 callees); batch 2b = the tail of 1–3-site callees. Each widening: param → `Optional[X]`, body guard confirmed/added, `Optional` in the typing import.
- [ ] **Step 2 (Recipes W-B/W-C):** hoist-and-guard the 143 union-attr sites and the leftover assignment sites (locals, `dict.get` args).
- [ ] **Step 3 (Recipe W-D):** fix the 4 `ET.SubElement` → `ET.Element` annotations (L6533, L8260, L10031, L15511).
- [ ] **Step 4 (Investigate):** L11084 `"EcucContainerDef" has no attribute "getReferences"` — inspect `EcucContainerDef` (defined at `ECUCParameterDefTemplate.py:499`): either the accessor exists under a different name (fix the writer call) or the model genuinely lacks it (same P-D decision tree; document the outcome).
- [ ] **Step 5: Verify** (conventions step 2 — writer is the other half of every roundtrip).
- [ ] **Step 6:** inventory grep for `arxml_writer.py` → 0, delete its baseline line, `uv run mypy` → green.
- [ ] **Step 7: Commit(s)** — `fix(mypy): drain arxml_writer callee params from baseline`, then `fix(mypy): drain arxml_writer unions/annotations from baseline` (or a single commit if landed atomically).

### Task 3: arxml_parser.py — 1287 errors, 5 families

**File:** `src/armodel/parser/arxml_parser.py`

- [ ] **Step 1 (Recipe P-A, batches by file region):** cast the 766 arg-type sites. Suggested batches: 3a = L1–L4000, 3b = L4000–L8000, 3c = L8000–end (adjust to keep batches reviewable); expected type always from the message.
- [ ] **Step 2 (Recipe P-B):** the 392 assignment sites (elif-chain variable reuse dominates — L2748ff BswM/Diagnostic needs chain is the exemplar).
- [ ] **Step 3 (Recipe P-C):** the 99 return-value sites.
- [ ] **Step 4 (Recipe P-D):** investigate all 21 attr-defined sites (L7665ff `ClientServerAnnotation` cluster first); fix models or parser per the decision tree; document per-site outcomes in the commit message.
- [ ] **Step 5:** sweep the 8 union-attr + 1 str-format leftovers (str-format at execution time; likely a `%`-format arg mismatch).
- [ ] **Step 6: Verify** (conventions step 2 — parser is the entry half of every roundtrip; run the full integration gate).
- [ ] **Step 7:** inventory grep for `arxml_parser.py` → 0, delete its baseline line, `uv run mypy` → green.
- [ ] **Step 8: Commit(s)** — one per batch: `fix(mypy): drain arxml_parser casts (L1-4000) from baseline` etc.; final `fix(mypy): drain arxml_parser defects from baseline` for P-D outcomes.

### Task 4: Final sweep — retire the baseline

- [ ] **Step 1:** Regenerate the inventory → confirm 0 errors outside the baseline, and the only remaining baseline members are the 3 giants, now fixed.
- [ ] **Step 2:** Delete the entire `[[tool.mypy.overrides]]` block from `pyproject.toml` (65 → 0). If mypy then reports the overrides' `warn_unused_ignores`/`warn_redundant_casts` deltas anywhere, fix those sites too (they were previously masked).
- [ ] **Step 3:** Full gates: `uv run pytest tests/ -q`, `npm run lint`, `npm run black-check`.
- [ ] **Step 4: Commit** — `fix(mypy): retire the mypy baseline overrides block`
- [ ] **Step 5:** Report: 3 giants drained (~2703 sites), baseline retired, commits list, any P-D model-sync gaps filed as follow-ups.

---

## Self-review

- **Coverage:** every error family in the evidence table maps to exactly one recipe and one task step: ARPackage 77+258+3 (T1), writer 759+171+143+4+1 (T2), parser 766+392+99+21+8+1 (T3), middle-tier 7 modules (T0), baseline retirement (T4). Sum = 2703 giant errors + in-tree middle work.
- **Boundary integrity:** model setter/getter signatures untouched (only P-D/W-E may add genuinely missing members, gated by investigation); parser/writer import order untouched; all annotations Python 3.8 `typing.*`.
- **Risk ordering:** T0 (already-green tree) → T1 (isolated, biggest single-file ROI) → T2 (writer, signature-level fixes fix many sites each) → T3 (parser, most per-site casts + the only true defect cluster) → T4 (retirement). Each task keeps mypy green independently; a partially completed plan leaves a valid, smaller baseline.
- **Known traps:** `getChildElementOptionalLiteral` is defined in `abstract_arxml_parser.py` (not the parser file) — its return type stays as-is; casts happen at parser call sites. The L4455 import fix must keep the `# noqa: E402` marker. Writer callees widened to Optional must not silently skip writes they previously wrote — the roundtrip gate is the check.
