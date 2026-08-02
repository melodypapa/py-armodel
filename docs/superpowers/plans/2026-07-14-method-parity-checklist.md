# Method Parity Checklist Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an auto-generated "method parity checklist" comment block at the top of every class body under `src/armodel/models/`, tracking impl / docstring / test status per method. Idempotent — re-running refreshes statuses.

**Architecture:** A single stdlib-only Python script (`scripts/generate_method_parity_checklist.py`) parses every `.py` file with `ast`, walks `tests/test_armodel/` once to build a class→test-method index, then inserts/replaces a comment block after each class docstring. Bottom-to-top line rewriting keeps indices valid. Also emits a Markdown coverage report.

**Tech Stack:** Python 3.8+ stdlib (`ast`, `argparse`, `re`, `pathlib`). No new dependencies.

## Global Constraints

- Target dir: `D:\workspace\py-armodel\src\armodel\models\` (≈246 `.py` files, ≈927 classes including enums/ABCs/nested).
- Test dir: `D:\workspace\py-armodel\tests\test_armodel\`.
- Line length cap: 127 chars (CI warns). Checklist lines are ~70 chars max.
- Encoding: utf-8 in/out. Line endings detected per-file and preserved.
- AGENTS.md line 39 normally forbids comments — this task is the explicit user override for these machine-generated blocks only.
- Two commits total: (1) the script + report, (2) the generated sweep across all model files.

## Output Format

Insertion point: immediately after the closing `"""` of the class docstring (or immediately after the `class X:` header line if no docstring). Indentation matches class body indent.

```python
class SwcBswMapping(AtpStructureElement):
    """
    Represents SWC-BSW mapping in AUTOSAR models.
    ...
    """
    # SwcBswMapping method parity checklist:
    # [x] __init__                [x] impl  [x] docstring  [x] test
    # [x] getBswBehaviorRef       [x] impl  [x] docstring  [x] test
    # [ ] addFoo                  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        ...
```

Formatting rules:
- Header: `# <ClassName> method parity checklist:`
- One row per declared method in **source order** (NOT alphabetical).
- Row leading mark: `[x]` if all three columns pass, else `[ ]`.
- Method-name column: 28 chars left-justified, overflow allowed (no truncation).
- Columns: `[x] impl  [x] docstring  [x] test`.
- Class with zero declared methods: emit `# (no methods)` after the header.

## Status Detection Rules

- **Methods collected:** Direct child `FunctionDef`/`AsyncFunctionDef` of the class body only — no inherited methods, no nested-class methods. Includes `__init__`, dunder methods, `@property`, `@staticmethod`/`@classmethod`, private (`_foo`).
- **impl = True** iff the body has any statement that is not a lone docstring and not a lone `pass`.
- **docstring = True** iff `ast.get_docstring(func, clean=False)` returns non-empty.
- **test = True** iff there exists a `Test<ClassName>` class anywhere under `tests/test_armodel/` containing a `test_*` function whose normalized name matches the source method's normalized name.
  - Normalization for both sides: strip `test_` prefix, lowercase, remove all underscores.
  - Example: source `getBswBehaviorRef` → `getbswbehaviorref`; test `test_get_bsw_behavior_ref` → `getbswbehaviorref`. Match.
  - Multiple `TestFoo` classes across files: union their tokens.
  - Special case for `__init__`: also accept tokens `init`, `initialization`, `constructor` (covers `test_initialization`).
  - Class with no matching `TestFoo`: every method is `[ ] test`.

---

## File Structure

Only ONE file is created by the engineer. Everything else is auto-modified by running it.

**Create:** `D:\workspace\py-armodel\scripts\generate_method_parity_checklist.py`

**Auto-created:** `D:\workspace\py-armodel\reports\method_parity_review.md` (on each run)

**Auto-modified:** ~199 files under `D:\workspace\py-armodel\src\armodel\models\` (only files containing ≥1 class definition). `__init__.py` files are scanned too (uniform rule).

### Script function inventory

| Function | Purpose |
|----------|---------|
| `normalize_token(name)` | Strip `test_`, lowercase, remove underscores. |
| `normalize_class_name(name)` | Lowercase + remove underscores. |
| `build_test_index(test_root)` | Walk `tests/test_armodel/` once; return `{normalized_class_name: set(normalized_method_tokens)}`. |
| `get_direct_methods(class_node)` | Direct child FunctionDef/AsyncFunctionDef in source order. |
| `has_real_body(func_node)` | True if body has any non-docstring, non-`pass` statement. |
| `has_docstring(func_node)` | `bool(ast.get_docstring(func_node, clean=False))`. |
| `is_tested(method_name, class_name, test_index)` | Token lookup with `__init__` special case. |
| `get_class_docstring_span(class_node, lines)` | Returns `(start_line, end_line)` 1-based, or `None`. |
| `format_checklist_block(class_name, methods, test_index, indent)` | Returns list of comment lines (no trailing newline). |
| `find_existing_block_span(lines, search_start, search_end, class_name, indent)` | Regex-match header; return inclusive (start_idx, end_idx) 0-based, or `None`. |
| `compute_insertion_point(class_node, lines, docstring_span)` | 0-based line index for fresh insert. |
| `collect_class_nodes_with_indent(tree, lines)` | `[(ClassDef, indent_string), ...]` via `ast.walk`. |
| `apply_edits_to_file(filepath, test_index, dry_run, verbose)` | Per-file orchestrator; returns `(changed, stats)`. |
| `generate_markdown_report(all_stats)` | Markdown string grouped by second-level dir under `models/`. |
| `parse_args()` | `--dry-run`, `--module <substr>`, `--verbose`. |
| `main()` | Resolve paths, build index, walk tree, dispatch, write report. |

---

## Task 1: Build the generator script

**Files:**
- Create: `D:\workspace\py-armodel\scripts\generate_method_parity_checklist.py`

**Interfaces:**
- Consumes: reads `src/armodel/models/**/*.py` and `tests/test_armodel/**/*.py`.
- Produces: modifies the source files in place; writes `reports/method_parity_review.md`.

- [ ] **Step 1: Write the script**

  Implement `scripts/generate_method_parity_checklist.py` per the function inventory above and the algorithm below. Reference `scripts/generate_docstring_report.py` for the AST-walk + scan-directory + Markdown-report pattern.

  Key algorithm — per-file orchestrator `apply_edits_to_file`:

  1. Read file bytes; detect line ending (`\r\n` / `\r` / `\n`) by byte scan; decode utf-8; split into `lines` (newline-normalized internally).
  2. `tree = ast.parse(text)` — on `SyntaxError`, warn to stderr and skip the file.
  3. `classes = collect_class_nodes_with_indent(tree, lines)` — `ast.walk` yields nested ClassDefs too; for each, capture indent from the source line.
  4. For each class (in any order — edits are collected first, applied after):
     - Compute `docstring_span = get_class_docstring_span(...)`.
     - Call `find_existing_block_span(...)` searching the window `[first_body_line, min(first_body_line + 50, class_node.end_lineno)]`. Header regex: `^${indent}# ${class_name} method parity checklist:\s*$`. If matched, extend through subsequent consecutive `^${indent}#.*$` lines.
     - `methods = get_direct_methods(class_node)`.
     - `block = format_checklist_block(class_node.name, methods, test_index, indent)` — appends a trailing blank line for visual separation.
     - If existing span found: edit = `(start_idx, end_idx_inclusive + 1, block)`. Else: edit = `(insertion_point, insertion_point, block)` where `insertion_point = docstring_span[1]` (0-based line after closing `"""`), or `class_node.body[0].lineno - 1` when no docstring.
  5. Sort edits by `start_idx` **descending**. Apply each as `lines[start:end] = block`. Bottom-to-top keeps earlier indices valid (works for nested classes too — their edits are disjoint from outer-class edits).
  6. `new_text = newline.join(lines)`; restore original line ending. Compare to `text`; write back only if changed (skip write when `--dry-run`).

  `build_test_index` walks `tests/test_armodel/` once: for each `ClassDef` whose name starts with `Test`, strip the `Test` prefix, normalize the remainder, and union all `test_*` method tokens (normalized) into the index.

  `format_checklist_block` line template (f-string):
  ```
  f"{indent}# {row_mark} {name:<28} {impl_mark} impl  {doc_mark} docstring  {test_mark} test"
  ```
  where each `*_mark` is `[x]` or `[ ]`, and `row_mark = [x]` iff all three pass.

  CLI: argparse with `--dry-run`, `--module` (substring match against path relative to `src/armodel/models/`, forward-slash normalized — handles both `--module CommonStructure` and `--module SwcBswMapping`), `--verbose` (per-class logging). Default scan: all of `src/armodel/models/`.

  Resolve paths via `Path(__file__).parent.parent / "src" / "armodel" / "models"` and `Path(__file__).parent.parent / "tests" / "test_armodel"` — runnable from any cwd.

- [ ] **Step 2: Smoke-run the script in dry-run**

  Run: `python scripts/generate_method_parity_checklist.py --dry-run --verbose`
  Expected: prints per-file summary lines, writes nothing. Reports overall impl/docstring/test counts. Exits 0.

- [ ] **Step 3: Commit the script**

  ```bash
  git add scripts/generate_method_parity_checklist.py
  git commit -m "feat: add method parity checklist generator script"
  ```

---

## Task 2: Pilot on one file and verify idempotency

**Files:**
- Modify (auto): `D:\workspace\py-armodel\src\armodel\models\M2\AUTOSARTemplates\CommonStructure\SwcBswMapping.py`

**Interfaces:**
- Consumes: Task 1's script.
- Produces: validated proof that the generator works correctly on one file before the full sweep.

- [ ] **Step 1: Run the generator on the pilot file**

  Run: `python scripts/generate_method_parity_checklist.py --module SwcBswMapping --verbose`
  Expected: logs 4 classes (`SwcBswMapping`, `SwcBswRunnableMapping`, `SwcBswSynchronizedModeGroupPrototype`, `SwcBswSynchronizedTrigger`). Modifies exactly one source file.

- [ ] **Step 2: Verify the diff manually**

  Open `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py`. Confirm:
  - Each of the 4 classes has a checklist block right after its docstring.
  - `SwcBswMapping` and `SwcBswRunnableMapping` rows show `[x] test` (because `tests/.../test_SwcBswMapping.py` defines `TestSwcBswMapping` and `TestSwcBswRunnableMapping` with matching test methods).
  - `SwcBswSynchronizedModeGroupPrototype` and `SwcBswSynchronizedTrigger` rows show `[ ] test` (no corresponding `Test*` class).
  - `__init__` rows show `[x] test` (matches `test_initialization`).
  - Method-name columns align at 28 chars.

- [ ] **Step 3: Verify idempotency**

  Run: `python scripts/generate_method_parity_checklist.py --module SwcBswMapping --dry-run --verbose`
  Expected: prints "0 files changed". Confirms re-running makes zero diff.

- [ ] **Step 4: Verify enum/no-methods edge case**

  Run: `python scripts/generate_method_parity_checklist.py --module RptAccessEnum --verbose`
  Expected: the enum class block contains `# (no methods)` because the class body has only field assignments, no FunctionDefs.

---

## Task 3: Full sweep and verification

**Files:**
- Auto-modify: ~199 files under `D:\workspace\py-armodel\src\armodel\models\`
- Auto-create: `D:\workspace\py-armodel\reports\method_parity_review.md`

**Interfaces:**
- Consumes: validated script from Task 1, validated format from Task 2.
- Produces: the complete generated sweep ready for the second commit.

- [ ] **Step 1: Run the generator across all models**

  Run: `python scripts/generate_method_parity_checklist.py`
  Expected output (approximate shape):
  ```
  Scanning <N> .py files under src/armodel/models/...
  Processed <N> files; modified <M> files.
  Report written to reports/method_parity_review.md
  Overall: <a>/<b> impl (P%), <c>/<d> docstring (Q%), <e>/<f> test (R%)
  ```

- [ ] **Step 2: Unit tests still pass**

  Run: `python scripts/run_tests.py --unit`
  Expected: all unit tests pass. Injected comments cannot change Python semantics; this is a sanity check.

- [ ] **Step 3: Lint clean**

  Run: `npm run flake8`
  Expected: no new errors. Spot-check that no generated line exceeds 127 chars.

- [ ] **Step 4: Re-verify idempotency on the full tree**

  Run: `python scripts/generate_method_parity_checklist.py --dry-run`
  Expected: "0 files changed". If any file would change, the generator is not idempotent — investigate before committing.

- [ ] **Step 5: Spot-check 3 random files**

  Manually open and verify:
  1. `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py` — a method marked `[x] test` has a real corresponding test in `tests/.../test_SwcBswMapping.py`.
  2. An enum file (e.g. `RptAccessEnum.py`) — block shows `# (no methods)`.
  3. A large class (e.g. `ARPackage.py`) — block lists all declared methods without duplicates; inherited methods from base classes are NOT listed.

- [ ] **Step 6: Inspect the Markdown report**

  Open `reports/method_parity_review.md`. Verify:
  - Overall totals line at the top.
  - Per-module sections (grouped by second-level dir: `M2/AUTOSARTemplates`, `M2/MSR`, etc.).
  - Per-class rows with `impl/docstring/test` counts.
  - Counts match what the spot-checks showed.

- [ ] **Step 7: Commit the sweep**

  Stage all model-file changes plus the report:
  ```bash
  git add src/armodel/models/ reports/method_parity_review.md
  git commit -m "feat: add method parity checklists to all model classes

  Auto-generated by scripts/generate_method_parity_checklist.py.
  Re-run the script to refresh; do not edit the blocks by hand."
  ```

---

## Verification (end-to-end summary)

After all three tasks:
- `python scripts/generate_method_parity_checklist.py --dry-run` → reports 0 files changed (idempotent).
- `python scripts/run_tests.py --unit` → all unit tests pass.
- `npm run flake8` → no new errors.
- `git log --oneline -2` → shows exactly two commits: one for the script, one for the sweep.
- `reports/method_parity_review.md` exists with overall + per-module coverage stats.
- Spot-checked model files have correctly-formatted checklist blocks reflecting actual impl/docstring/test status.

## Edge Cases Handled (reference, not separate tasks)

- File fails to parse → skip with stderr warning, do not crash.
- Class with zero methods (empty enum, marker class) → `# (no methods)`.
- `__init__` test detection → accept tokens `init`, `initialization`, `constructor`.
- Nested classes → receive their own checklists at correct indentation.
- Multi-line class headers → `body[0].lineno` is used, robust to header length.
- `@dataclass`/`@property`/`@staticmethod`/`@classmethod` → all treated as regular FunctionDefs.
- Multiple `TestFoo` classes across files → tokens unioned.
- Windows `\r\n` line endings → detected per-file, preserved on write.

## Risks

- **Noisy diff:** ~199 files in one commit. Mitigation: PR description calls this out; the generator script is committed first so reviewers can read it before the sweep.
- **Hand-edited blocks get overwritten:** by design — the block is machine-owned. The report header notes "do not edit by hand."
- **Test-name normalization mismatches:** snake_case ↔ camelCase normalization is heuristic. A method like `get` (single word) might collide with unrelated test methods like `test_get_something`. Acceptable for a tracking aid; if false positives appear, refine `is_tested` later.
