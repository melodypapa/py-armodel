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

(Further findings A-004+ appended by later Track A tasks.)
