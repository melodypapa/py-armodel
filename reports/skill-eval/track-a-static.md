# Track A — Static Review Evidence

Canonical source: `.claude/skills/sync-autosar-class/`.

Note: at evaluation time, `.agents/skills/sync-autosar-class/*` showed as
modified (staged) in `git status` — the staged edits bring `.agents/` into
byte-identity with `.claude/` and `.codebuddy/`. All diffs below compare the
working-tree versions, which are identical across all three locations.

## A-001 — three SKILL.md copies byte-identical

| Copy pair | Result |
|---|---|
| `.claude` vs `.codebuddy` | PASS (diff empty) |
| `.claude` vs `.agents` | PASS (diff empty) |

## A-002 — three rules.md copies byte-identical

| Copy pair | Result |
|---|---|
| `.claude` vs `.codebuddy` | PASS (diff empty) |
| `.claude` vs `.agents` | PASS (diff empty) |

## A-003 — three evals.json copies byte-identical

| Copy pair | Result |
|---|---|
| `.claude` vs `.codebuddy` | PASS (diff empty) |
| `.claude` vs `.agents` | PASS (diff empty) |

## A-004 — Rule ID continuity (0001..0016)

Script: `scripts/eval_skill_static_checks.py` (run 2026-08-13).

Defined top-level rules (16): `['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010', '0011', '0012', '0013', '0014', '0015', '0016']`

Finding: **PASS** — top-level IDs are contiguous 0001..0016, no duplicates, no gaps.

Script-limitation note: the `SUBRULE_HEADER_RE` regex (`^###\s+(\d{4}\.\d+(?:\.\d+)?)\s`) only catches 4-digit-form sub-rule headers without the `Rule` prefix. It reports 5 sub-rules (`0006.1`, `0012.1`, `0012.2`, `0012.3`, `0013.1`) but the file actually defines 22 sub-rules. The other 17 use either the short form (`### 1.1` … `### 1.11` for Rule 0001; `### 16.1` … `### 16.6` for Rule 0016) or the `Rule`-prefixed form (`### Rule 0004.1`). Verified manually via `Grep` — all 22 sub-rule headers exist. This is a script coverage gap, not a skill defect.

## A-005 — Dangling rule cross-references

Referenced rule IDs (30 distinct IDs, sorted): `['0001', '0001.1', '0001.10', '0001.2', '0001.3', '0001.5', '0001.6', '0001.7', '0002', '0003', '0004', '0004.1', '0005', '0006', '0006.1', '0007', '0008', '0009', '0010', '0011', '0012', '0012.1', '0012.2', '0012.3', '0013', '0013.1', '0014', '0015', '0016', '0016.2']`

Finding: **PASS** — every referenced rule ID resolves to a defined top-level rule (the script's `check_dangling_refs` treats a sub-rule reference as resolved if its parent top-level rule exists, which is correct given the skill's actual structure).

Manual cross-check: the two referenced sub-rule IDs that do NOT have a matching `### <id>` header in the script's output (`0004.1` and `0016.2`) were verified by direct `Grep` to exist as headers in `rules.md`:
- `### Rule 0004.1 — Abstract base + concrete subclass uniformity` (line 410; missed by the regex because of the `Rule` prefix)
- `### 16.2 Confirm the closure with the end user (gate)` (line 911; missed by the regex because of the short form)

No dangling references found.

(Further findings A-006+ appended by later Track A tasks.)
