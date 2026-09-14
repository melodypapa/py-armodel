# Model-Test Parity Remediation Plan

> **For agentic workers:** Use `superpowers:subagent-driven-development` or `superpowers:executing-plans`. Execute one domain batch at a time and commit each independently reviewable batch.

**Goal:** Align every model source module under `src/armodel/models/` with deliberate, behaviorally meaningful model tests while preserving valid legacy test placement.

**Architecture:** First classify structural parity results using AST and source/test references. Then normalize tests by production module and strengthen behavioral coverage in domain batches. Production code changes are permitted only when a strengthened test proves an actual implementation defect.

**Tech Stack:** Python 3.8+, `ast`, `pytest`, Ruff, Black, existing parity script.

## Global Constraints

- Keep model tests under `tests/test_armodel/models/`.
- Group classes declared in one production module into that module's test file where practical.
- Keep parser and writer tests in their dedicated folders.
- Preserve valid misplaced legacy tests until coverage is relocated.
- Do not alter production behavior solely to satisfy structural parity.
- Use TDD for production fixes.
- Run `npm run lint`, `npm run black-check`, focused tests, and `git diff --check` for each batch.

## Tasks

1. Build a reliable AST-based inventory and behavioral audit report.
2. Normalize shared-module model tests, starting with `InlineAttributeEnums.py`.
3. Strengthen enum tests with `AREnum`, exact values, `getEnumValues()`, invalid-value, and setter-chain checks.
4. Strengthen regular-class tests with defaults, accessors, `None` no-op, chaining, aggregations, and abstract guards.
5. Add or consolidate tests for the nine uncovered source modules reported by the parity script.
6. Resolve the five orphan tests by relocating valid coverage or removing obsolete tests after confirmation.
7. Resolve partial class coverage in high-impact modules, prioritizing `ServiceNeeds`, Fibex topology modules, timing events, and `PrimitiveTypes`.
8. Improve `scripts/check_model_test_parity.py` to recognize canonical multi-class tests, valid relocation allowlists, and structural vs behavioral results.
9. Run final structural/behavioral audits, lint, Black, full tests, diff checks, and review allowlists.

## Baseline

`python scripts/check_model_test_parity.py` currently reports 149 source files, 299 test files, 9 uncovered source files, 5 orphan tests, 5 files with no tested classes, 20 partial files, and 42 misplaced-test warnings. These results must be classified before broad edits.
