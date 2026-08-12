# sync-autosar-class Skill Evaluation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a structured, evidence-backed evaluation of the `sync-autosar-class` skill (`.claude/skills/sync-autosar-class/`) covering static quality (SKILL.md + rules.md internal consistency, codebase/spec citation accuracy), dynamic quality (running all 5 evals in `evals/evals.json` and scoring each against its `expectations`), and coverage (which of the 16 rules + 9-step workflow + Phase 0 the evals actually exercise), ending with a written report of findings + prioritized recommendations.

**Architecture:** Three evaluation tracks executed in order. **Track A — Static review** reads the skill files and verifies every internal cross-reference (Rule IDs, file paths, worked-example class names) against the actual repo state, recording pass/fail per claim. **Track B — Dynamic execution** dispatches one fresh subagent per eval case (Task tool, `subagent_type=general_purpose_task`) with the eval prompt, captures the subagent's output verbatim, then scores each `expectations` item as met / partial / not-met. **Track C — Coverage matrix** maps the 16 rules + 9 steps + Phase 0 against the 5 evals to surface untested rules. All evidence is written into a single Markdown report at `reports/sync-autosar-class-skill-evaluation.md`.

**Tech Stack:** Python 3.8+ stdlib (`ast`, `re`, `json`, `pathlib`), `grep`/`Grep` tool, `Task` tool for subagent dispatch, `pytest` only if any helper assertion script is added (none required by default). No new runtime dependencies.

---

## File Structure

**Created by this plan:**

- `reports/sync-autosar-class-skill-evaluation.md` — the final evaluation report (Markdown). Single source of truth for findings.
- `reports/skill-eval/track-a-static.md` — Track A evidence table (one row per claim: claim text, source location, repo verification, pass/fail, note).
- `reports/skill-eval/track-b-eval-<N>.md` — one file per eval case (`N` = 1..5) capturing: the prompt, the subagent's verbatim output, the per-expectation score, and a one-line verdict.
- `reports/skill-eval/track-c-coverage.md` — the Rule × Eval coverage matrix + the list of untested rules.
- `scripts/eval_skill_static_checks.py` — a small stdlib-only script that runs the mechanical Track A checks (rule-id continuity, broken file-path references, duplicate rule IDs) and prints a pass/fail table. Not required for human review but makes Track A repeatable.

**Read-only inputs (not modified):**

- `.claude/skills/sync-autosar-class/SKILL.md`
- `.claude/skills/sync-autosar-class/rules.md`
- `.claude/skills/sync-autosar-class/evals/evals.json`
- `src/armodel/models/M2/AUTOSARTemplates/**/*.py` (citation verification)
- `tests/test_armodel/models/M2/AUTOSARTemplates/**/*.py` (test-mirror citation verification)
- `autosar/markdown/AUTOSAR_*_TPS_*.md` (spec citation verification)
- `autosar/pdf/AUTOSAR_*_TPS_*.pdf` (PDF page-citation verification — opened only to confirm the file exists; the skill itself says only the page number is read from PDFs)

**Note on the three sibling copies:** the skill is duplicated across `.claude/`, `.codebuddy/`, and `.agents/` directories. Track A Task 2 confirms they are byte-identical; the evaluation treats `.claude/` as canonical and notes any drift in the other two as a finding.

---

## Global Constraints

- Repo root for all paths in this plan: `/Users/ray/Workspace/py-armodel`.
- AUTOSAR release target referenced by the skill is **R23-11**; the XSD ground truth is `docs/requirements/xsd/AUTOSAR_00052.xsd` (verify it exists in Task 5).
- All subagent dispatches in Track B must be **read-only with respect to source files** — the eval prompts explicitly say "Do NOT modify any source files." If a subagent reports it modified a file, that is itself a finding (expectation violation) and must be recorded.
- Every evidence file goes under `reports/skill-eval/` (create the directory in Task 1). Do not write into `src/`, `tests/`, or `.claude/`.
- Lint/style: the only Python file this plan creates is `scripts/eval_skill_static_checks.py`; it must pass `npm run flake8` and `npm run ruff-check` (max line length 79 per `AGENTS.md`).
- No comments in the new script unless they carry spec information (per `AGENTS.md` "Do NOT add comments unless asked").
- Type annotations: Python 3.8-compatible — `Optional[T]` / `List[T]` / `Dict[K, V]` from `typing`, never `T | None` or `list[...]`.

---

## Background facts established by investigation

These are verified facts (read during plan authoring, not assumptions) the tasks rely on:

1. The skill ships three identical-looking copies: `.claude/skills/sync-autosar-class/`, `.codebuddy/skills/sync-autosar-class/`, `.agents/skills/sync-autosar-class/`. Each has `SKILL.md`, `rules.md`, `evals/evals.json`.
2. `SKILL.md` front-matter declares `metadata.version: "1.6.0"` and `author: melodypapa`.
3. `rules.md` defines `Rule 0001` through `Rule 0016` (contiguous 4-digit IDs), plus sub-rules `0001.1`–`0001.11`, `0002` (no sub-rules), `0003`, `0004` + `0004.1`, `0005`, `0006` + `0006.1`, `0007`–`0016` with `0012.1`/`0012.2`/`0012.3` and `0013.1` and `0016.1`–`0016.6`.
4. `SKILL.md` references 16 rule IDs in its "Phase 1 — The 9-step workflow" table and inline; the cross-reference density is high enough that a mechanical ID-continuity + broken-link check is worth automating.
5. The skill cites these worked-example classes by name (must be verified to exist in the codebase during Track A): `ClientServerInterface`, `ParameterInterface`, `NvDataInterface`, `LanguageSpecific`, `LLongName`, `MixedContentForLongName`, `ObdInfoServiceNeeds`, `ObdPidServiceNeeds`, `ObdMonitorServiceNeeds`, `DiagnosticCapabilityElement`, `NmCoordinatorRoleEnum`, `NmNode`, `ExecutableEntityActivationReason`, `SymbolicNameProps`, `ImplementationProps`, `CseCodeType`, `PositiveInteger`, `AREnum`, `ARLiteral`, `ARNumerical`.
6. The skill cites these spec markdown filenames: `AUTOSAR_CP_TPS_SystemTemplate.md`, `AUTOSAR_CP_TPS_SoftwareComponentTemplate.md`, plus the glob `AUTOSAR_*_TPS_*.md` (covering `CP_TPS` + `FO_TPS`). The repo's `autosar/markdown/` contains 15 files (7 `CP_TPS`, 8 `FO_TPS`) — verified during plan authoring via `LS`.
7. The skill cites `Table 6.303` (NmNode) and `Table 6.304` (NmCoordinatorRoleEnum) in eval cases 4 and 5, and `Table 4.7` / `Table 4.9` (LLongName / MixedContentForLongName) in rules.md Rule 0001.3.
8. `evals/evals.json` contains exactly 5 eval cases with `id` 1–5; each has `prompt`, `expected_output`, and an `expectations` array (5–8 items per case). All five prompts include the sentence "Do NOT modify any source files."
9. The skill's "stamp is the review gate" section (SKILL.md lines ~91–109) makes a strong claim that **only** the `# Spec verified: R<YY>-<MM>` marker certifies a class — Track A must verify this claim is internally consistent with Rule 0012.1.
10. `AGENTS.md` mandates `python scripts/run_tests.py` for tests, `npm run flake8` for lint, max line length 79, `AUTOSAR.setARRelease('R23-11')` before parse/write — the skill repeats these; Track A checks for drift between `AGENTS.md` and the skill.

---

## Track A — Static Review

### Task 1: Set up the evaluation workspace

**Files:**
- Create: `reports/skill-eval/.gitkeep`
- Create: `reports/skill-eval/README.md`

- [ ] **Step 1: Create the reports/skill-eval directory**

Run:
```bash
mkdir -p reports/skill-eval
```

- [ ] **Step 2: Write the directory README**

Write `reports/skill-eval/README.md` with exactly:

```markdown
# sync-autosar-class Skill Evaluation Evidence

Holds the per-track evidence files for the evaluation defined in
`docs/superpowers/plans/2026-08-13-sync-autosar-class-skill-evaluation.md`.

- `track-a-static.md` — static-review evidence (one row per claim)
- `track-b-eval-<N>.md` — one file per eval case (N = 1..5)
- `track-c-coverage.md` — Rule x Eval coverage matrix

The final rollup is `reports/sync-autosar-class-skill-evaluation.md` (parent dir).
```

- [ ] **Step 3: Add a .gitkeep so the dir survives even before evidence lands**

Write `reports/skill-eval/.gitkeep` with exactly one empty line.

- [ ] **Step 4: Verify**

Run:
```bash
ls reports/skill-eval/
```
Expected output includes: `README.md`, `.gitkeep`.

- [ ] **Step 5: Commit**

```bash
git add reports/skill-eval/README.md reports/skill-eval/.gitkeep
git commit -m "chore: scaffold sync-autosar-class skill evaluation workspace"
```

---

### Task 2: Confirm the three skill copies are byte-identical

**Files:**
- Read: `.claude/skills/sync-autosar-class/SKILL.md`
- Read: `.codebuddy/skills/sync-autosar-class/SKILL.md`
- Read: `.agents/skills/sync-autosar-class/SKILL.md`
- Read: `.claude/skills/sync-autosar-class/rules.md`
- Read: `.codebuddy/skills/sync-autosar-class/rules.md`
- Read: `.agents/skills/sync-autosar-class/rules.md`
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Read: `.codebuddy/skills/sync-autosar-class/evals/evals.json`
- Read: `.agents/skills/sync-autosar-class/evals/evals.json`
- Create: `reports/skill-eval/track-a-static.md`

- [ ] **Step 1: Diff the three SKILL.md copies**

Run:
```bash
diff .claude/skills/sync-autosar-class/SKILL.md .codebuddy/skills/sync-autosar-class/SKILL.md
diff .claude/skills/sync-autosar-class/SKILL.md .agents/skills/sync-autosar-class/SKILL.md
```
Expected: no output (identical). If output appears, record the diff in `track-a-static.md` as finding `A-001`.

- [ ] **Step 2: Diff the three rules.md copies**

Run:
```bash
diff .claude/skills/sync-autosar-class/rules.md .codebuddy/skills/sync-autosar-class/rules.md
diff .claude/skills/sync-autosar-class/rules.md .agents/skills/sync-autosar-class/rules.md
```
Expected: no output. Record drift as finding `A-002`.

- [ ] **Step 3: Diff the three evals.json copies**

Run:
```bash
diff .claude/skills/sync-autosar-class/evals/evals.json .codebuddy/skills/sync-autosar-class/evals/evals.json
diff .claude/skills/sync-autosar-class/evals/evals.json .agents/skills/sync-autosar-class/evals/evals.json
```
Expected: no output. Record drift as finding `A-003`.

- [ ] **Step 4: Initialize the Track A evidence file**

Write `reports/skill-eval/track-a-static.md` with exactly:

```markdown
# Track A — Static Review Evidence

Canonical source: `.claude/skills/sync-autosar-class/`.

## A-001 — three SKILL.md copies byte-identical

| Copy pair | Result |
|---|---|
| `.claude` vs `.codebuddy` | <PASS or paste diff> |
| `.claude` vs `.agents` | <PASS or paste diff> |

## A-002 — three rules.md copies byte-identical

| Copy pair | Result |
|---|---|
| `.claude` vs `.codebuddy` | <PASS or paste diff> |
| `.claude` vs `.agents` | <PASS or paste diff> |

## A-003 — three evals.json copies byte-identical

| Copy pair | Result |
|---|---|
| `.claude` vs `.codebuddy` | <PASS or paste diff> |
| `.claude` vs `.agents` | <PASS or paste diff> |

(Further findings A-004+ appended by later Track A tasks.)
```

Fill the `<PASS or paste diff>` placeholders with the actual results from Steps 1–3.

- [ ] **Step 5: Commit**

```bash
git add reports/skill-eval/track-a-static.md
git commit -m "chore(eval): record Track A-001..A-003 skill-copy identity check"
```

---

### Task 3: Verify Rule ID continuity and cross-reference integrity

**Files:**
- Read: `.claude/skills/sync-autosar-class/rules.md`
- Read: `.claude/skills/sync-autosar-class/SKILL.md`
- Create: `scripts/eval_skill_static_checks.py`
- Modify: `reports/skill-eval/track-a-static.md`

- [ ] **Step 1: Write the static-checks script**

Write `scripts/eval_skill_static_checks.py` with exactly:

```python
"""Mechanical checks for the sync-autosar-class skill static review."""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / ".claude" / "skills" / "sync-autosar-class"
RULES_PATH = SKILL_DIR / "rules.md"
SKILL_PATH = SKILL_DIR / "SKILL.md"

RULE_HEADER_RE = re.compile(r"^##\s+Rule\s+(\d{4})", re.MULTILINE)
SUBRULE_HEADER_RE = re.compile(r"^###\s+(\d{4}\.\d+(?:\.\d+)?)\s", re.MULTILINE)
RULE_REF_RE = re.compile(r"\bRule\s+(\d{4}(?:\.\d+)?)\b")


def collect_defined_rules() -> Tuple[List[str], List[str]]:
    rules_text = RULES_PATH.read_text(encoding="utf-8")
    top_level = RULE_HEADER_RE.findall(rules_text)
    sub_level = SUBRULE_HEADER_RE.findall(rules_text)
    return top_level, sub_level


def collect_referenced_rules() -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for path in (RULES_PATH, SKILL_PATH):
        text = path.read_text(encoding="utf-8")
        for match in RULE_REF_RE.finditer(text):
            rid = match.group(1)
            counts[rid] = counts.get(rid, 0) + 1
    return counts


def check_continuity(top_level: List[str]) -> List[str]:
    findings: List[str] = []
    expected = [f"{n:04d}" for n in range(1, 17)]
    if top_level != expected:
        findings.append(
            f"top-level rule list is {top_level}, expected {expected}"
        )
    seen = set()
    duplicates = [r for r in top_level if r in seen or seen.add(r)]
    if duplicates:
        findings.append(f"duplicate top-level rule IDs: {duplicates}")
    return findings


def check_dangling_refs(defined: List[str], referenced: Dict[str, int]) -> List[str]:
    findings: List[str] = []
    defined_set = set(defined)
    for rid in referenced:
        if rid not in defined_set and not any(
            d == rid.split(".")[0] for d in defined_set
        ):
            findings.append(f"referenced Rule {rid} has no definition")
    return findings


def main() -> int:
    top_level, sub_level = collect_defined_rules()
    referenced = collect_referenced_rules()
    findings: List[str] = []
    findings.extend(check_continuity(top_level))
    findings.extend(check_dangling_refs(top_level, referenced))

    print("=== sync-autosar-class static checks ===")
    print(f"Defined top-level rules ({len(top_level)}): {top_level}")
    print(f"Defined sub-rules ({len(sub_level)}): {sub_level}")
    print(f"Referenced rule IDs ({len(referenced)}): {sorted(referenced)}")
    if findings:
        print("\nFINDINGS:")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("\nAll mechanical checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run the script and capture output**

Run:
```bash
python scripts/eval_skill_static_checks.py
```
Expected: prints the defined rules (0001–0016), the sub-rules, the referenced rule IDs, and either "All mechanical checks passed." or a FINDINGS list. Capture the full output into a temp scratch file mentally — it will be pasted into `track-a-static.md` in Step 3.

- [ ] **Step 3: Lint the new script**

Run:
```bash
npm run flake8
npm run ruff-check
```
Expected: no errors. If `ruff-check` flags an unused import or line length, fix the script (do not add comments) and re-run.

- [ ] **Step 4: Append findings A-004 and A-005 to the evidence file**

Append to `reports/skill-eval/track-a-static.md`:

```markdown

## A-004 — Rule ID continuity (0001..0016)

Defined top-level rules: <paste from script output>
Finding: <PASS or paste the script's FINDINGS block>

## A-005 — Dangling rule cross-references

Referenced rule IDs: <paste from script output>
Finding: <PASS or paste the script's FINDINGS block>
```

Fill placeholders with the script's actual output.

- [ ] **Step 5: Commit**

```bash
git add scripts/eval_skill_static_checks.py reports/skill-eval/track-a-static.md
git commit -m "chore(eval): add Rule ID continuity + dangling-ref checker (A-004, A-005)"
```

---

### Task 4: Verify every codebase citation in the skill resolves to a real artifact

**Files:**
- Read: `.claude/skills/sync-autosar-class/rules.md`
- Read: `.claude/skills/sync-autosar-class/SKILL.md`
- Modify: `reports/skill-eval/track-a-static.md`

- [ ] **Step 1: Build the citation list**

The skill cites these classes by name (verified during plan authoring). For each, locate the source file via `Glob` or `Grep`:

| # | Class | Expected location |
|---|---|---|
| 1 | `ClientServerInterface` | `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/PortInterface.py` (or sibling) |
| 2 | `ParameterInterface` | same package as #1 |
| 3 | `NvDataInterface` | same package as #1 |
| 4 | `LanguageSpecific` | somewhere under `src/armodel/models/M2/AUTOSARTemplates/` |
| 5 | `LLongName` | under `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/` |
| 6 | `MixedContentForLongName` | same area as #5 |
| 7 | `ObdInfoServiceNeeds` | under `DiagnosticExtract` or `MSR` area |
| 8 | `ObdPidServiceNeeds` | same as #7 |
| 9 | `ObdMonitorServiceNeeds` | same as #7 |
| 10 | `DiagnosticCapabilityElement` | same as #7 |
| 11 | `NmCoordinatorRoleEnum` | `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py` |
| 12 | `NmNode` | same file as #11 |
| 13 | `ExecutableEntityActivationReason` | under `CommonStructure/InternalBehavior` |
| 14 | `SymbolicNameProps` | under `CommonStructure` |
| 15 | `ImplementationProps` | `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py` |
| 16 | `CseCodeType` | under primitive-types module |
| 17 | `PositiveInteger` | `.../GeneralTemplateClasses/PrimitiveTypes.py` |
| 18 | `AREnum` | same as #17 |
| 19 | `ARLiteral` | same as #17 |
| 20 | `ARNumerical` | same as #17 |

- [ ] **Step 2: Grep each class name to confirm it exists**

Run (one `Grep` call per class, in parallel batches of ≤5):

```
Grep pattern="class ClientServerInterface\b" path="src/armodel/models"
Grep pattern="class ParameterInterface\b" path="src/armodel/models"
Grep pattern="class NvDataInterface\b" path="src/armodel/models"
Grep pattern="class LanguageSpecific\b" path="src/armodel/models"
Grep pattern="class LLongName\b" path="src/armodel/models"
```
(and so on for all 20)

Expected: at least one match per class. Record any "no matches" as a finding.

- [ ] **Step 3: Verify the two worked-example patterns the skill relies on**

The skill claims (Rule 0004): "`ClientServerInterface` is the worked example" for the dedicated-typed-list pattern; and "a fully-`[x]` sibling still in the old shape (e.g. `NvDataInterface.getNvDatas`)" is a deviation to reconcile.

Run:
```
Grep pattern="self\.operations\s*:\s*List\[ClientServerOperation\]" path="src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface"
Grep pattern="def getNvDatas\b" path="src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface"
```
Expected: first matches in `ClientServerInterface`; second matches in `NvDataInterface`. If either returns nothing, the skill's worked-example claim is inaccurate — record as finding `A-007`.

- [ ] **Step 4: Verify the LLongName / MixedContentForLongName relocation example**

The skill (Rule 0001.3) claims `LLongName` (Table 4.7) owns only `blueprintValue` and `MixedContentForLongName` (Table 4.9) owns `e/ie/sub/sup/tt`.

Run:
```
Grep pattern="class LLongName\b" path="src/armodel/models"
Grep pattern="class MixedContentForLongName\b" path="src/armodel/models"
Grep pattern="blueprintValue" path="src/armodel/models"
```
Expected: all three match. If `MixedContentForLongName` does not exist as a class, the skill's relocation example is hypothetical, not real — record as finding `A-008`.

- [ ] **Step 5: Append findings A-006..A-008 to the evidence file**

Append to `reports/skill-eval/track-a-static.md`:

```markdown

## A-006 — Cited classes exist in the codebase

| # | Class | Found at | Result |
|---|---|---|---|
| 1 | ClientServerInterface | <path or NOT FOUND> | <PASS/FAIL> |
| 2 | ParameterInterface | <...> | <...> |
| ... | ... | ... | ... |
| 20 | ARNumerical | <...> | <...> |

## A-007 — Worked-example patterns (ClientServerInterface.operations, NvDataInterface.getNvDatas)

| Claim | Grep result | Verdict |
|---|---|---|
| `ClientServerInterface.operations: List[ClientServerOperation]` | <paste> | <PASS/FAIL> |
| `NvDataInterface.getNvDatas` exists | <paste> | <PASS/FAIL> |

## A-008 — LLongName / MixedContentForLongName relocation example

| Claim | Grep result | Verdict |
|---|---|---|
| `LLongName` class exists | <paste> | <PASS/FAIL> |
| `MixedContentForLongName` class exists | <paste> | <PASS/FAIL> |
| `blueprintValue` field exists on `LLongName` | <paste> | <PASS/FAIL> |
```

Fill each row with the actual grep result and PASS/FAIL.

- [ ] **Step 6: Commit**

```bash
git add reports/skill-eval/track-a-static.md
git commit -m "chore(eval): record codebase-citation verification (A-006..A-008)"
```

---

### Task 5: Verify every spec citation in the skill resolves to a real artifact

**Files:**
- Read: `.claude/skills/sync-autosar-class/rules.md`
- Read: `.claude/skills/sync-autosar-class/SKILL.md`
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Modify: `reports/skill-eval/track-a-static.md`

- [ ] **Step 1: Verify the spec markdown glob resolves to real files**

Run:
```
LS path="/Users/ray/Workspace/py-armodel/autosar/markdown"
```
Expected: 15 files (7 `CP_TPS`, 8 `FO_TPS`). The skill claims the glob `AUTOSAR_*_TPS_*.md` "covers `CP_TPS` + `FO_TPS`" — confirm both prefixes are present.

- [ ] **Step 2: Verify the spec PDF directory exists and has matching files**

Run:
```
LS path="/Users/ray/Workspace/py-armodel/autosar/pdf"
```
Expected: PDF files mirroring the markdown set. The skill says PDFs are "opened only to read the page number" — confirm at least the PDFs referenced by the evals (`AUTOSAR_CP_TPS_SystemTemplate.pdf` for NmNode Table 6.303 and NmCoordinatorRoleEnum Table 6.304) exist.

- [ ] **Step 3: Verify the XSD ground-truth path**

Run:
```
LS path="/Users/ray/Workspace/py-armodel/docs/requirements/xsd"
```
Expected: at least one `.xsd` file. The skill references `docs/requirements/xsd/` in SKILL.md Input table and Rules 0001.3 / 0015 / 0016.4. Confirm `AUTOSAR_00052.xsd` (R23-11) is present; if not, record the actual filename as finding `A-010`.

- [ ] **Step 4: Verify the cited Table IDs exist in the markdown**

Run (one `Grep` per cited table):

```
Grep pattern="Table 6.303: NmNode" path="autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md"
Grep pattern="Table 6.304: NmCoordinatorRoleEnum" path="autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md"
Grep pattern="Table 4.7: LLongName" path="autosar/markdown"
Grep pattern="Table 4.9: MixedContentForLongName" path="autosar/markdown"
```
Expected: each returns one matching line. If a cited table cannot be found by that exact header text, the skill's citation is inaccurate — record as finding `A-011`.

- [ ] **Step 5: Verify the deviation-tracker reference**

The skill (Rule 0014) references "the project deviation tracker" but does not name a file. Run:
```
Glob pattern="**/deviation*"
Glob pattern="**/deviations*"
```
Expected: at least one Markdown file (e.g. `docs/deviation_tracker.md` or similar). If nothing is found, the skill references an artifact that does not exist in the repo — record as finding `A-012`.

- [ ] **Step 6: Verify the coding-rules reference**

The skill (References section) cites `docs/development/coding_rules.md`. Run:
```
LS path="/Users/ray/Workspace/py-armodel/docs/development"
```
Expected: `coding_rules.md` exists. If not, record as finding `A-013`.

- [ ] **Step 7: Append findings A-009..A-013 to the evidence file**

Append to `reports/skill-eval/track-a-static.md`:

```markdown

## A-009 — spec markdown glob resolves

| Check | Result |
|---|---|
| `autosar/markdown/` file count | <N> |
| `CP_TPS` files present | <list or NONE> |
| `FO_TPS` files present | <list or NONE> |

## A-010 — PDF + XSD ground-truth paths

| Artifact | Path | Exists? |
|---|---|---|
| `AUTOSAR_CP_TPS_SystemTemplate.pdf` | <path> | <YES/NO> |
| XSD (R23-11) | <path> | <YES/NO> |

## A-011 — cited Table IDs exist in the markdown

| Cited table | Markdown file | Header match? |
|---|---|---|
| Table 6.303 (NmNode) | <file> | <YES/NO> |
| Table 6.304 (NmCoordinatorRoleEnum) | <file> | <YES/NO> |
| Table 4.7 (LLongName) | <file> | <YES/NO> |
| Table 4.9 (MixedContentForLongName) | <file> | <YES/NO> |

## A-012 — deviation tracker exists

| Glob result | Verdict |
|---|---|
| <paste> | <PASS/FAIL> |

## A-013 — docs/development/coding_rules.md exists

| LS result | Verdict |
|---|---|
| <paste> | <PASS/FAIL> |
```

Fill placeholders with actual results.

- [ ] **Step 8: Commit**

```bash
git add reports/skill-eval/track-a-static.md
git commit -m "chore(eval): record spec-citation verification (A-009..A-013)"
```

---

### Task 6: Verify the "stamp is the review gate" claim is internally consistent

**Files:**
- Read: `.claude/skills/sync-autosar-class/SKILL.md` (lines ~91–109)
- Read: `.claude/skills/sync-autosar-class/rules.md` (Rule 0012.1, Rule 0006.1)
- Modify: `reports/skill-eval/track-a-static.md`

- [ ] **Step 1: Extract the three claims**

Read SKILL.md section "The stamp is the review gate" and confirm it states:
1. A class counts as reviewed/synced **only** when its source carries `# Spec verified: R<YY>-<MM>`.
2. A fully-`[x]` checklist, passing tests, or a clean round-trip do **not** by themselves certify a class.
3. The exception is XSD-only classes (no own spec table) — they legitimately carry no marker.

- [ ] **Step 2: Cross-check against Rule 0012.1**

Read Rule 0012.1 in `rules.md`. Confirm it states the same three claims (marker is the single review gate; no marker ⇒ sync from scratch; XSD-only exception).

- [ ] **Step 3: Cross-check against Rule 0006.1**

Read Rule 0006.1. Confirm Step 9b is described as a **human confirmation gate** that runs after 9a passes and before the stamp is placed, and that it lists the same automation-blind items (Rule 0001.1, 0001.2, 0001.3, 0001.5, 0001.6, 0001.7, 0011, 0012, 0014, stamp decision).

- [ ] **Step 4: Append finding A-014 to the evidence file**

Append to `reports/skill-eval/track-a-static.md`:

```markdown

## A-014 — "stamp is the review gate" internal consistency

| Claim | In SKILL.md? | In Rule 0012.1? | In Rule 0006.1? | Consistent? |
|---|---|---|---|---|
| Marker is the single review gate | <YES/NO> | <YES/NO> | <YES/NO> | <PASS/FAIL> |
| Checklist+tests+round-trip do not certify | <YES/NO> | <YES/NO> | <YES/NO> | <PASS/FAIL> |
| XSD-only exception | <YES/NO> | <YES/NO> | <YES/NO> | <PASS/FAIL> |
| 9b is a human gate before stamping | <YES/NO> | <YES/NO> | <YES/NO> | <PASS/FAIL> |

If any cell is NO where it should be YES, describe the inconsistency in a note below.
```

Fill placeholders with the actual findings.

- [ ] **Step 5: Commit**

```bash
git add reports/skill-eval/track-a-static.md
git commit -m "chore(eval): record stamp-gate consistency check (A-014)"
```

---

## Track B — Dynamic Execution

Each eval case is dispatched to a fresh `general_purpose_task` subagent. The subagent receives the exact eval `prompt` from `evals.json`, plus a short preamble telling it to use the skill files and to **not modify any source files**. The subagent's verbatim output is captured into `track-b-eval-<N>.md`, then scored against the `expectations` array.

### Task 7: Define the subagent dispatch helper and run Eval #1 (ObdInfoServiceNeeds Phase 0)

**Files:**
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Create: `reports/skill-eval/track-b-eval-1.md`

- [ ] **Step 1: Read the eval #1 prompt + expectations**

Run:
```
Read file_path="/Users/ray/Workspace/py-armodel/.claude/skills/sync-autosar-class/evals/evals.json"
```
Extract the object with `"id": 1`. Note its `prompt`, `expected_output`, and the 6 `expectations` items.

- [ ] **Step 2: Dispatch the subagent**

Call the `Task` tool with:
- `subagent_type`: `general_purpose_task`
- `description`: `Eval 1 ObdInfoServiceNeeds Phase 0`
- `query`: the exact text below (verbatim — the subagent has no other context):

```
You are evaluating the `sync-autosar-class` skill located at
/Users/ray/Workspace/py-armodel/.claude/skills/sync-autosar-class/.
Read .claude/skills/sync-autosar-class/SKILL.md and
.claude/skills/sync-autosar-class/rules.md fully before acting.

PROMPT (execute this as if a user asked it):
Run Phase 0 (Discovery & Class Closure) for the AUTOSAR class `ObdInfoServiceNeeds`
in py-armodel. Do NOT modify any source files. Produce the sync map (closure classes,
source location, queue order) and stop. The repo root is /Users/ray/Workspace/py-armodel.

CONSTRAINTS:
- Do NOT modify, create, or delete any file under src/armodel/ or tests/.
- You MAY read any file in the repo.
- When the skill says to present a closure set and ask the user to confirm (Phase 0
  step 2 / Rule 0016.2), do that — present the set and stop, exactly as the skill
  instructs. Do not invent a confirmation on the user's behalf.

Return your full final response verbatim (the same text you would show the user).
```

- [ ] **Step 3: Capture the subagent's verbatim output**

Copy the subagent's returned final message into `reports/skill-eval/track-b-eval-1.md` under a `## Subagent output` heading (use a fenced code block so the raw text is preserved).

- [ ] **Step 4: Score each expectation**

For each of the 6 expectations of eval #1, decide `MET` / `PARTIAL` / `NOT-MET` by reading the captured output. Append to `track-b-eval-1.md`:

```markdown

## Expectation scores

| # | Expectation | Score | Evidence (quote from output) |
|---|---|---|---|
| 1 | Output mentions the class ObdInfoServiceNeeds and its parent DiagnosticCapabilityElement | <MET/PARTIAL/NOT-MET> | "<quote>" |
| 2 | Output lists spec source for each closure class (markdown/pdf/missing) | <...> | "<quote>" |
| 3 | Output presents an ordered sync queue (parents first, input class last) | <...> | "<quote>" |
| 4 | No source files under src/armodel/models/ were modified | <MET/NOT-MET> | "<confirm via git status>" |
| 5 | Output cites Rule 0016 or the Phase 0 procedure | <...> | "<quote>" |
| 6 | Output presents the collected closure set and asks the user to confirm it (membership gate) before locating specs, resolving missing classes, or building the queue | <...> | "<quote>" |

## Verdict

<one-line summary, e.g. "5/6 MET, 1 PARTIAL — the membership gate was mentioned but not presented as a stop-and-ask step">
```

- [ ] **Step 5: Verify no source files were modified**

Run:
```bash
git status --short
```
Expected: only `reports/skill-eval/track-b-eval-1.md` is new; nothing under `src/` or `tests/` is modified. If anything under `src/` or `tests/` appears, set expectation #4 to `NOT-MET` and record the path.

- [ ] **Step 6: Commit**

```bash
git add reports/skill-eval/track-b-eval-1.md
git commit -m "chore(eval): capture Eval #1 (ObdInfoServiceNeeds Phase 0) output + scores"
```

---

### Task 8: Run Eval #2 (EndToEndProtection Phase 0)

**Files:**
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Create: `reports/skill-eval/track-b-eval-2.md`

- [ ] **Step 1: Read the eval #2 prompt + expectations**

Extract the object with `"id": 2` from `evals.json`. Note its 7 `expectations`.

- [ ] **Step 2: Dispatch the subagent**

Call `Task` with `subagent_type=general_purpose_task`, `description="Eval 2 EndToEndProtection Phase 0"`, and `query`:

```
You are evaluating the `sync-autosar-class` skill located at
/Users/ray/Workspace/py-armodel/.claude/skills/sync-autosar-class/.
Read .claude/skills/sync-autosar-class/SKILL.md and
.claude/skills/sync-autosar-class/rules.md fully before acting.

PROMPT (execute this as if a user asked it):
Run Phase 0 (Discovery & Class Closure) for the AUTOSAR class `EndToEndProtection`
in py-armodel. Do NOT modify any source files. Produce the sync map (closure classes,
source location, queue order) and stop. The repo root is /Users/ray/Workspace/py-armodel.

CONSTRAINTS:
- Do NOT modify, create, or delete any file under src/armodel/ or tests/.
- You MAY read any file in the repo.
- When the skill says to present a closure set and ask the user to confirm (Phase 0
  step 2 / Rule 0016.2), do that — present the set and stop, exactly as the skill
  instructs. Do not invent a confirmation on the user's behalf.

Return your full final response verbatim (the same text you would show the user).
```

- [ ] **Step 3: Capture output and score**

Write `reports/skill-eval/track-b-eval-2.md` with the same structure as Task 7 Step 3–4, but using eval #2's 7 expectations:

```markdown
# Track B — Eval #2 (EndToEndProtection Phase 0)

## Subagent output

<verbatim fenced block>

## Expectation scores

| # | Expectation | Score | Evidence |
|---|---|---|---|
| 1 | Output mentions the class EndToEndProtection | <...> | "<quote>" |
| 2 | Output lists parent class(es) by walking the Base column | <...> | "<quote>" |
| 3 | Output enumerates member types from the Attribute rows (refs, aggrs, enums) | <...> | "<quote>" |
| 4 | Output presents an ordered sync queue | <...> | "<quote>" |
| 5 | No source files under src/armodel/models/ were modified | <...> | "<git status quote>" |
| 6 | Output mentions Rule 0016 or Phase 0 procedure | <...> | "<quote>" |
| 7 | Output presents the collected closure set and asks the user to confirm it (membership gate) before locating specs, resolving missing classes, or building the queue | <...> | "<quote>" |

## Verdict

<one-line summary>
```

- [ ] **Step 4: Verify no source modifications**

Run `git status --short`; expected: only the new evidence file.

- [ ] **Step 5: Commit**

```bash
git add reports/skill-eval/track-b-eval-2.md
git commit -m "chore(eval): capture Eval #2 (EndToEndProtection Phase 0) output + scores"
```

---

### Task 9: Run Eval #3 (ObdMonitorServiceNeeds missing-class resolution)

**Files:**
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Create: `reports/skill-eval/track-b-eval-3.md`

- [ ] **Step 1: Read the eval #3 prompt + expectations**

Extract the object with `"id": 3` from `evals.json`. Note its 6 `expectations`. The key expectation is #4 ("does NOT invent a third option beyond Skip and Derive-from-XSD").

- [ ] **Step 2: Dispatch the subagent**

Call `Task` with `subagent_type=general_purpose_task`, `description="Eval 3 ObdMonitorServiceNeeds missing-class"`, and `query`:

```
You are evaluating the `sync-autosar-class` skill located at
/Users/ray/Workspace/py-armodel/.claude/skills/sync-autosar-class/.
Read .claude/skills/sync-autosar-class/SKILL.md and
.claude/skills/sync-autosar-class/rules.md fully before acting.

PROMPT (execute this as if a user asked it):
I want to sync `ObdMonitorServiceNeeds` in py-armodel but suspect some referenced types
may not exist in the markdown spec. Use the sync-autosar-class skill to run the discovery
pre-flight (Phase 0) and tell me what you find. Do NOT modify any source files. If any
closure classes are missing from both markdown and PDF, present the user-decision step.
Repo root: /Users/ray/Workspace/py-armodel.

CONSTRAINTS:
- Do NOT modify, create, or delete any file under src/armodel/ or tests/.
- You MAY read any file in the repo.
- Follow Rule 0016.2 (membership gate) first: present the closure set and ask the user
  to confirm it. Then, only for classes that turn out to be missing from markdown AND
  PDF, present the Rule 0016.4 Skip-vs-Derive-from-XSD decision. Do not invent a third
  option.

Return your full final response verbatim (the same text you would show the user).
```

- [ ] **Step 3: Capture output and score**

Write `reports/skill-eval/track-b-eval-3.md` using eval #3's 6 expectations, with special attention to:

```markdown
# Track B — Eval #3 (ObdMonitorServiceNeeds missing-class)

## Subagent output

<verbatim fenced block>

## Expectation scores

| # | Expectation | Score | Evidence |
|---|---|---|---|
| 1 | Output mentions ObdMonitorServiceNeeds and its parent DiagnosticCapabilityElement | <...> | "<quote>" |
| 2 | Output lists member types (applicationDataTypeRef, eventNeedsRef, unitAndScalingId, updateKind or their target classes) | <...> | "<quote>" |
| 3 | Output either confirms all closure classes are in markdown OR presents an AskUserQuestion-style prompt for missing ones with Skip/Derive-from-XSD options | <...> | "<quote>" |
| 4 | Output does NOT invent a third option beyond Skip and Derive-from-XSD for missing classes | <MET/NOT-MET> | "<quote — if a third option appears, paste it>" |
| 5 | No source files under src/armodel/models/ were modified | <...> | "<git status quote>" |
| 6 | Output presents the collected closure set and asks the user to confirm it (membership gate) before the missing-class Skip/Derive-from-XSD resolution | <...> | "<quote>" |

## Verdict

<one-line summary, calling out expectation #4 explicitly>
```

- [ ] **Step 4: Verify no source modifications**

Run `git status --short`.

- [ ] **Step 5: Commit**

```bash
git add reports/skill-eval/track-b-eval-3.md
git commit -m "chore(eval): capture Eval #3 (ObdMonitorServiceNeeds missing-class) output + scores"
```

---

### Task 10: Run Eval #4 (NmCoordinatorRoleEnum Step 9b)

**Files:**
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Create: `reports/skill-eval/track-b-eval-4.md`

- [ ] **Step 1: Read the eval #4 prompt + expectations**

Extract the object with `"id": 4` from `evals.json`. Note its 8 `expectations`. This eval is the enum-specialization of Step 9b.

- [ ] **Step 2: Dispatch the subagent**

Call `Task` with `subagent_type=general_purpose_task`, `description="Eval 4 NmCoordinatorRoleEnum 9b"`, and `query`:

```
You are evaluating the `sync-autosar-class` skill located at
/Users/ray/Workspace/py-armodel/.claude/skills/sync-autosar-class/.
Read .claude/skills/sync-autosar-class/SKILL.md and
.claude/skills/sync-autosar-class/rules.md fully before acting.

PROMPT (execute this as if a user asked it):
Using the sync-autosar-class skill, you have just finished implementing the sync of the
AUTOSAR enum `NmCoordinatorRoleEnum` (Table 6.304) in py-armodel: Steps 1 through 9a are
complete and all automated checks (pytest, flake8, ruff, black-check, set-based checklist
script, round-trip) pass. Now perform Step 9b: present the post-sync rule-compliance
confirmation to the end user. Do NOT modify any source files; just produce the
confirmation. Repo root: /Users/ray/Workspace/py-armodel.

CONSTRAINTS:
- Do NOT modify, create, or delete any file under src/armodel/ or tests/.
- You MAY read any file in the repo (including the current NmCoordinatorRoleEnum source
  and the spec markdown at autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md).
- Follow Rule 0006.1 precisely. The confirmation must cover every automation-blind item
  for an enum (Rule 0011 member sync, Rule 0012 docstring verbatim from markdown, member
  order, stamp decision). End by asking the user to confirm before stamping.

Return your full final response verbatim (the same text you would show the user).
```

- [ ] **Step 3: Capture output and score**

Write `reports/skill-eval/track-b-eval-4.md` using eval #4's 8 expectations:

```markdown
# Track B — Eval #4 (NmCoordinatorRoleEnum Step 9b)

## Subagent output

<verbatim fenced block>

## Expectation scores

| # | Expectation | Score | Evidence |
|---|---|---|---|
| 1 | Output presents a Step 9b rule-compliance confirmation gate (not just 'tests pass') | <...> | "<quote>" |
| 2 | Output checks field<->spec in both directions (for the enum: members vs Literal rows, no extra/missing) | <...> | "<quote>" |
| 3 | Output checks docstrings/comments copy the spec Note verbatim (verified by diff, not status) | <...> | "<quote>" |
| 4 | Output states the stamp decision: # Spec verified placed only if no unresolved deviation/placeholder remains | <...> | "<quote>" |
| 5 | Output checks member order (Rule 0011) for the enum literals | <...> | "<quote>" |
| 6 | Output states the 9b checklist is the complete pre-stamp sign-off (when all items pass, # Spec verified is warranted) | <...> | "<quote>" |
| 7 | Output asks the user to confirm before stamping the class or advancing to the next queue item | <...> | "<quote>" |
| 8 | No source files under src/armodel/models/ were modified | <...> | "<git status quote>" |

## Verdict

<one-line summary>
```

- [ ] **Step 4: Verify no source modifications**

Run `git status --short`.

- [ ] **Step 5: Commit**

```bash
git add reports/skill-eval/track-b-eval-4.md
git commit -m "chore(eval): capture Eval #4 (NmCoordinatorRoleEnum 9b) output + scores"
```

---

### Task 11: Run Eval #5 (NmNode Step 9b — the deviation-detector eval)

**Files:**
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Create: `reports/skill-eval/track-b-eval-5.md`

- [ ] **Step 1: Read the eval #5 prompt + expectations**

Extract the object with `"id": 5` from `evals.json`. Note its 6 `expectations`. This eval is the hardest — it requires the subagent to *flag* known deviations (`TxNmPduRefs` naming, type drift on `nmCoordCluster`/`nmCoordinatorRole`/`nmNodeId`) that the skill's rules predict.

- [ ] **Step 2: Dispatch the subagent**

Call `Task` with `subagent_type=general_purpose_task`, `description="Eval 5 NmNode 9b deviation detector"`, and `query`:

```
You are evaluating the `sync-autosar-class` skill located at
/Users/ray/Workspace/py-armodel/.claude/skills/sync-autosar-class/.
Read .claude/skills/sync-autosar-class/SKILL.md and
.claude/skills/sync-autosar-class/rules.md fully before acting.

PROMPT (execute this as if a user asked it):
Using the sync-autosar-class skill, you have just finished implementing the sync of the
AUTOSAR class `NmNode` (CP SystemTemplate Table 6.303, abstract, base Identifiable) in
py-armodel: Steps 1 through 9a are complete and all automated checks (pytest, flake8,
ruff, black-check, set-based checklist script, round-trip) pass. Now perform Step 9b:
present the post-sync rule-compliance confirmation for NmNode against its spec table.
The current source is src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
and the spec markdown is autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md (Table 6.303).
Do NOT modify any source files; just produce the confirmation.
Repo root: /Users/ray/Workspace/py-armodel.

CONSTRAINTS:
- Do NOT modify, create, or delete any file under src/armodel/ or tests/.
- You MAY read the source file and the spec markdown.
- Follow Rule 0006.1. Critically, perform the field<->spec cross-check in BOTH
  directions (Rule 0002) and check Rule 0001.5 (Kind-suffix naming), Rule 0001.3
  (type drift vs the PDF), Rule 0011 (member order), Rule 0001.7 (reader+writer
  coverage). If any deviation is found, state that # Spec verified may NOT be
  stamped while it remains, and ask the user to confirm.

Return your full final response verbatim (the same text you would show the user).
```

- [ ] **Step 3: Capture output and score**

Write `reports/skill-eval/track-b-eval-5.md` using eval #5's 6 expectations:

```markdown
# Track B — Eval #5 (NmNode Step 9b — deviation detector)

## Subagent output

<verbatim fenced block>

## Expectation scores

| # | Expectation | Score | Evidence |
|---|---|---|---|
| 1 | Output presents a Step 9b complete pre-stamp rule-compliance checklist (not just 'tests pass') | <...> | "<quote>" |
| 2 | Output flags the Kind-suffix/naming deviation TxNmPduRefs (should be txNmPduRefs) under Rule 0001.5 | <MET/NOT-MET> | "<quote — paste the exact wording the subagent used, or NOT-MET if absent>" |
| 3 | Output flags type drift vs the PDF (e.g. nmCoordCluster ARNumerical vs PositiveInteger, or nmCoordinatorRole ARLiteral vs NmCoordinatorRoleEnum) under Rule 0001.3 | <MET/NOT-MET> | "<quote>" |
| 4 | Output checks member order (Rule 0011) and reader/writer coverage (Rule 0001.7) | <...> | "<quote>" |
| 5 | Output concludes # Spec verified may NOT be stamped while any 9b item fails, and asks the user to confirm | <...> | "<quote>" |
| 6 | No source files under src/armodel/models/ were modified | <...> | "<git status quote>" |

## Verdict

<one-line summary — this eval is the strongest signal of whether the skill's rules
actually surface real deviations; call out explicitly whether the subagent found
the TxNmPduRefs naming bug and the type drift on its own>
```

- [ ] **Step 4: Verify no source modifications**

Run `git status --short`.

- [ ] **Step 5: Commit**

```bash
git add reports/skill-eval/track-b-eval-5.md
git commit -m "chore(eval): capture Eval #5 (NmNode 9b deviation detector) output + scores"
```

---

## Track C — Coverage Matrix

### Task 12: Build the Rule × Eval coverage matrix

**Files:**
- Read: `.claude/skills/sync-autosar-class/rules.md`
- Read: `.claude/skills/sync-autosar-class/evals/evals.json`
- Read: `reports/skill-eval/track-b-eval-1.md` through `track-b-eval-5.md`
- Create: `reports/skill-eval/track-c-coverage.md`

- [ ] **Step 1: List the 16 rules + key sub-rules + the 9 steps + Phase 0**

The rows of the matrix are:

| # | Item |
|---|---|
| 1 | Rule 0001 (Spec Sync — all of 1.1–1.11) |
| 2 | Rule 0001.3 (no fabrication / flattening / type drift) |
| 3 | Rule 0001.5 (Kind-suffix naming) |
| 4 | Rule 0001.6 (create vs set/add shape) |
| 5 | Rule 0001.7 (reader+writer coverage) |
| 6 | Rule 0001.10 (missing referenced classes) |
| 7 | Rule 0001.11 (member order) |
| 8 | Rule 0002 (5-column checklist + field-to-spec cross-check) |
| 9 | Rule 0003 (type hints, 3.8-compatible) |
| 10 | Rule 0004 / 0004.1 (getter/setter behavior, None no-op) |
| 11 | Rule 0005 (formatting, imports, black/ruff) |
| 12 | Rule 0006 / 0006.1 (tests + 9b gate) |
| 13 | Rule 0007 (package location & file shape) |
| 14 | Rule 0008 (attribute spacing) |
| 15 | Rule 0009 (method signatures) |
| 16 | Rule 0010 (enums inherit AREnum) |
| 17 | Rule 0011 (enum spec sync) |
| 18 | Rule 0012 / 0012.1–0012.3 (docstring sync + marker) |
| 19 | Rule 0013 / 0013.1 (reader/writer source style) |
| 20 | Rule 0014 (deviation tracking) |
| 21 | Rule 0015 (XSD vs PDF authority) |
| 22 | Rule 0016 / 0016.1–0016.6 (Phase 0 closure) |
| 23 | Phase 1 Step 2 (model test, Red) |
| 24 | Phase 1 Step 3 (model impl, Green) |
| 25 | Phase 1 Step 5 (reader/writer test, Red) |
| 26 | Phase 1 Step 6 (reader/writer impl, Green) |
| 27 | Phase 1 Step 9b (confirmation gate) |

- [ ] **Step 2: For each row, mark which evals exercise it**

For each (rule, eval) pair, decide `DIRECT` (the eval's prompt or expectations explicitly target this rule), `INDIRECT` (the eval would surface a failure of this rule if the subagent followed the skill faithfully), or `—` (not exercised). Read the 5 eval prompts + their `expectations` arrays from `evals.json`, and read the 5 captured subagent outputs to see what was actually touched.

- [ ] **Step 3: Write the coverage matrix file**

Write `reports/skill-eval/track-c-coverage.md` with:

```markdown
# Track C — Rule × Eval Coverage Matrix

`DIRECT` = the eval's prompt or expectations explicitly target this rule.
`INDIRECT` = a faithful execution would surface a failure of this rule.
`—` = not exercised by any eval.

| # | Rule / step | Eval 1 | Eval 2 | Eval 3 | Eval 4 | Eval 5 |
|---|---|---|---|---|---|---|
| 1 | Rule 0001 (Spec Sync) | <D/I/-> | <...> | <...> | <...> | <...> |
| 2 | Rule 0001.3 (no fabrication/flattening/type drift) | <...> | <...> | <...> | <...> | <D> |
| 3 | Rule 0001.5 (Kind-suffix naming) | <...> | <...> | <...> | <...> | <D> |
| 4 | Rule 0001.6 (create vs set/add) | <...> | <...> | <...> | <...> | <...> |
| 5 | Rule 0001.7 (reader+writer coverage) | <...> | <...> | <...> | <...> | <D> |
| 6 | Rule 0001.10 (missing referenced classes) | <...> | <...> | <D> | <...> | <...> |
| 7 | Rule 0001.11 (member order) | <...> | <...> | <...> | <D> | <D> |
| 8 | Rule 0002 (checklist + cross-check) | <...> | <...> | <...> | <D> | <D> |
| 9 | Rule 0003 (type hints) | <...> | <...> | <...> | <...> | <...> |
| 10 | Rule 0004 (getter/setter, None no-op) | <...> | <...> | <...> | <...> | <...> |
| 11 | Rule 0005 (formatting) | <...> | <...> | <...> | <...> | <...> |
| 12 | Rule 0006 / 0006.1 (tests + 9b gate) | <...> | <...> | <...> | <D> | <D> |
| 13 | Rule 0007 (package location) | <...> | <...> | <...> | <...> | <...> |
| 14 | Rule 0008 (attribute spacing) | <...> | <...> | <...> | <...> | <...> |
| 15 | Rule 0009 (method signatures) | <...> | <...> | <...> | <...> | <...> |
| 16 | Rule 0010 (enums inherit AREnum) | <...> | <...> | <...> | <D> | <...> |
| 17 | Rule 0011 (enum spec sync) | <...> | <...> | <...> | <D> | <...> |
| 18 | Rule 0012 (docstring sync + marker) | <...> | <...> | <...> | <D> | <D> |
| 19 | Rule 0013 (reader/writer source style) | <...> | <...> | <...> | <...> | <...> |
| 20 | Rule 0014 (deviation tracking) | <...> | <...> | <D> | <...> | <D> |
| 21 | Rule 0015 (XSD vs PDF authority) | <...> | <...> | <...> | <...> | <...> |
| 22 | Rule 0016 (Phase 0 closure) | <D> | <D> | <D> | <...> | <...> |
| 23 | Phase 1 Step 2 (model test, Red) | <...> | <...> | <...> | <...> | <...> |
| 24 | Phase 1 Step 3 (model impl, Green) | <...> | <...> | <...> | <...> | <...> |
| 25 | Phase 1 Step 5 (reader/writer test, Red) | <...> | <...> | <...> | <...> | <...> |
| 26 | Phase 1 Step 6 (reader/writer impl, Green) | <...> | <...> | <...> | <...> | <...> |
| 27 | Phase 1 Step 9b (confirmation gate) | <...> | <...> | <...> | <D> | <D> |

## Untested rules (no DIRECT and no INDIRECT coverage)

<list every row that is all `—`, e.g.:
- Rule 0003 (type hints) — not exercised by any eval
- Rule 0005 (formatting) — not exercised
- Rule 0007 (package location) — not exercised
- Rule 0008 (attribute spacing) — not exercised
- Rule 0009 (method signatures) — not exercised
- Rule 0013 (reader/writer source style) — not exercised
- Rule 0015 (XSD vs PDF authority) — not exercised
- Phase 1 Steps 2, 3, 5, 6 (the Red/Green TDD pairs) — not exercised; all evals are
  either Phase 0 (evals 1–3) or Step 9b (evals 4–5), so the actual implementation
  loop is never run end-to-end>

## Notes

<one or two paragraphs calling out:
- the heaviest concentration is Phase 0 (3 evals) and Step 9b (2 evals);
- the actual 9-step implementation loop (Steps 2/3/5/6 — the TDD Red/Green pairs)
  is NOT exercised by any eval, which is the largest coverage gap;
- Rule 0015 (XSD vs PDF authority), added explicitly after the Obd* sync, has no
  direct eval even though eval #3 touches ObdMonitorServiceNeeds.>
```

Fill each cell with `D`, `I`, or `-` based on your reading.

- [ ] **Step 4: Commit**

```bash
git add reports/skill-eval/track-c-coverage.md
git commit -m "chore(eval): record Rule x Eval coverage matrix (Track C)"
```

---

## Final Rollup

### Task 13: Write the final evaluation report

**Files:**
- Read: `reports/skill-eval/track-a-static.md`
- Read: `reports/skill-eval/track-b-eval-1.md` through `track-b-eval-5.md`
- Read: `reports/skill-eval/track-c-coverage.md`
- Create: `reports/sync-autosar-class-skill-evaluation.md`

- [ ] **Step 1: Aggregate the scores**

For Track B, compute per-eval pass counts: for each eval `N`, count how many of its expectations scored `MET`, how many `PARTIAL`, how many `NOT-MET`. Compute a total across all 5 evals.

- [ ] **Step 2: Write the report**

Write `reports/sync-autosar-class-skill-evaluation.md` with:

```markdown
# sync-autosar-class Skill Evaluation

**Date:** 2026-08-13
**Skill version:** 1.6.0 (per `SKILL.md` front-matter)
**Canonical source:** `.claude/skills/sync-autosar-class/`
**Plan:** `docs/superpowers/plans/2026-08-13-sync-autosar-class-skill-evaluation.md`

## 1. Executive summary

<2–4 sentences. State the overall verdict: is the skill fit for purpose?
What is the single biggest strength and the single biggest weakness?>

## 2. Track A — Static review summary

<copy the A-001..A-014 verdicts from track-a-static.md into a compact table;
call out any FAIL explicitly>

| Finding | Verdict |
|---|---|
| A-001 three SKILL.md copies identical | <PASS/FAIL> |
| A-002 three rules.md copies identical | <PASS/FAIL> |
| A-003 three evals.json copies identical | <PASS/FAIL> |
| A-004 Rule ID continuity 0001..0016 | <PASS/FAIL> |
| A-005 no dangling rule cross-refs | <PASS/FAIL> |
| A-006 cited classes exist in codebase | <PASS/FAIL> |
| A-007 worked-example patterns real | <PASS/FAIL> |
| A-008 LLongName/MixedContentForLongName relocation example real | <PASS/FAIL> |
| A-009 spec markdown glob resolves | <PASS/FAIL> |
| A-010 PDF + XSD ground-truth paths exist | <PASS/FAIL> |
| A-011 cited Table IDs exist in markdown | <PASS/FAIL> |
| A-012 deviation tracker exists | <PASS/FAIL> |
| A-013 docs/development/coding_rules.md exists | <PASS/FAIL> |
| A-014 stamp-gate claim internally consistent | <PASS/FAIL> |

## 3. Track B — Dynamic execution summary

| Eval | Class / scenario | Expectations MET | PARTIAL | NOT-MET | Verdict |
|---|---|---|---|---|---|
| 1 | ObdInfoServiceNeeds Phase 0 | <n>/6 | <n> | <n> | <one line> |
| 2 | EndToEndProtection Phase 0 | <n>/7 | <n> | <n> | <one line> |
| 3 | ObdMonitorServiceNeeds missing-class | <n>/6 | <n> | <n> | <one line, call out expectation #4> |
| 4 | NmCoordinatorRoleEnum Step 9b | <n>/8 | <n> | <n> | <one line> |
| 5 | NmNode Step 9b (deviation detector) | <n>/6 | <n> | <n> | <one line, call out whether TxNmPduRefs + type drift were found> |
| **Total** | | **<n>/33** | **<n>** | **<n>** | |

### 3.1 Notable per-eval findings

- **Eval 1:** <one or two sentences on the most important MET/NOT-MET>
- **Eval 2:** <...>
- **Eval 3:** <specifically: did the subagent invent a third option beyond Skip/Derive-from-XSD?>
- **Eval 4:** <specifically: did the subagent treat the enum's 9b correctly (members vs Literal rows, verbatim docstring)?>
- **Eval 5:** <specifically: did the subagent find TxNmPduRefs naming bug + type drift on its own? This is the strongest signal of rule effectiveness.>

## 4. Track C — Coverage summary

<copy the untested-rules list from track-c-coverage.md verbatim>

### 4.1 Largest coverage gaps

1. **Phase 1 Steps 2/3/5/6 (the TDD Red/Green pairs) are not exercised by any eval.**
   All 5 evals are either Phase 0 (evals 1–3) or Step 9b (evals 4–5). The actual
   implementation loop — write failing test, implement, run, commit — is never run
   end-to-end. <one sentence on risk>
2. **Rule 0015 (XSD vs PDF authority)** — added explicitly after the Obd* sync —
   has no direct eval, even though eval #3 touches ObdMonitorServiceNeeds.
3. **Rules 0003, 0005, 0007, 0008, 0009, 0013** (formatting / package shape /
   reader-writer source style) have no eval coverage.

## 5. Strengths

- <e.g. "Phase 0 closure + membership gate is well-specified and the 3 Phase 0
  evals give it strong coverage">
- <e.g. "Rule 0006.1 / Step 9b gate is the skill's most distinctive feature and
  the 2 Step 9b evals directly exercise it">
- <e.g. "self-contained — rules.md carries all 16 rules; no external doc drift risk">

## 6. Weaknesses / recommendations (prioritized)

1. **<highest priority>** — <e.g. "Add at least one eval that runs the full 9-step
   loop end-to-end on a small class (Steps 2/3/5/6). Today no eval proves the
   skill's central TDD workflow actually works."> Severity: HIGH.
2. **<next>** — <e.g. "Add an eval that directly exercises Rule 0015 (XSD vs PDF
   authority) — e.g. a class where the XSD has an attribute the PDF omits, and
   the eval verifies the skill says 'do not model'."> Severity: MEDIUM.
3. **<next>** — <e.g. "Add an eval that exercises Rule 0013 (no chained
   set/create/add in reader/writer) by giving the subagent a reader file with a
   chain and checking the skill flags it."> Severity: MEDIUM.
4. **<next>** — <e.g. "If the three skill copies (.claude/.codebuddy/.agents) are
   meant to stay in sync, add a CI check (or a pre-commit hook) that diffs them;
   today drift would be silent."> Severity: LOW (if A-001..A-003 passed) or HIGH
   (if they failed).
5. **<next>** — <e.g. "Rule 0014 references 'the project deviation tracker' without
   naming the file. Name it (or confirm it does not yet exist and create it).">
   Severity: <depends on A-012 result>.

## 7. Artifacts

- Static evidence: `reports/skill-eval/track-a-static.md`
- Per-eval evidence: `reports/skill-eval/track-b-eval-1.md` … `track-b-eval-5.md`
- Coverage matrix: `reports/skill-eval/track-c-coverage.md`
- Static-checks script: `scripts/eval_skill_static_checks.py`
```

Fill every placeholder (`<...>`) with the actual aggregated values from the per-track files.

- [ ] **Step 3: Sanity-check the report**

Read `reports/sync-autosar-class-skill-evaluation.md` end to end. Confirm:
- Every `<...>` placeholder is filled.
- The Track B totals row sums to 33 expectations across the 5 evals (6+7+6+8+6 = 33).
- The "Untested rules" list in section 4 matches Track C.
- Every recommendation has a severity tag.

- [ ] **Step 4: Commit**

```bash
git add reports/sync-autosar-class-skill-evaluation.md
git commit -m "docs(eval): final sync-autosar-class skill evaluation report"
```

---

## Self-Review (run after Task 13)

**1. Spec coverage.** The user asked to "eval the sync-autosar-class skill." Coverage:
- Static quality (internal consistency, citation accuracy) — Tasks 2–6. ✓
- Dynamic quality (run the 5 existing evals, score them) — Tasks 7–11. ✓
- Coverage of the skill's rules by the evals — Task 12. ✓
- Written report with findings + recommendations — Task 13. ✓

**2. Placeholder scan.** Every `<...>` in the plan is a *fill-in* marker for evidence the executor captures at runtime (grep output, subagent output, scores). These are not "TBD/TODO/implement later" placeholders — each has an exact instruction for what to fill in. The plan itself contains no TODO/TBD/placeholder prose.

**3. Type consistency.** The only Python file (`scripts/eval_skill_static_checks.py`) uses `Dict[str, int]`, `List[str]`, `Tuple[List[str], List[str]]`, `Path`, `re.Pattern` — all 3.8-compatible, all imported from `typing` where needed. Function names (`collect_defined_rules`, `collect_referenced_rules`, `check_continuity`, `check_dangling_refs`, `main`) are used consistently. The script's return type is `int` (exit code), matching `sys.exit(main())`.

**4. Cross-task consistency.** The eval IDs (1–5) and expectation counts (6, 7, 6, 8, 6 = 33) are consistent across Tasks 7–13. The finding IDs (A-001 … A-014) are contiguous and referenced consistently between Task instructions and the report template. The file paths (`reports/skill-eval/track-{a,b,c}-*.md`, `reports/sync-autosar-class-skill-evaluation.md`, `scripts/eval_skill_static_checks.py`) are consistent across all tasks.
