# Rule 0007 Package-Location Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminate every confirmed Rule 0007 (*Package Location & File Shape*) violation listed in the appendix of `docs/examples/method_deviation_by_class_v2.md`: 104 mis-located classes (Section A), the `DoIp`/`DoIP` case mismatch (Section B), and the 26 synced classes missing from the top-level export chain plus 3 stale name-collision entries (Section E).

**Architecture:** Pure mechanical relocation inside `src/armodel/models/`. Each class moves to the module implied by its spec `Package` row (`M2::…::Pkg` → `…/Pkg.py` for leaf packages, `…/Pkg/__init__.py` for non-leaf). Old modules are deleted (no re-export shims at old locations), except package `__init__.py` aggregators which legitimately re-export from their submodules. Consumers (parser, writer, lib, cli, tests, `models/__init__.py`) are re-pointed to the defining module. The wildcard chain `armodel.models.__init__` keeps every public name importable as `armodel.<ClassName>`.

**Tech Stack:** Python 3.8+ (typing-compatible syntax only), pytest via `python scripts/run_tests.py`, ruff/flake8 via `npm run lint`, black via `npm run black`, git.

---

## Scope decisions (locked in — do not re-litigate during execution)

1. **Section A** (`docs/examples/method_deviation_by_class_v2.md` appendix): all rows are fixed **except** `PortPrototypeBlueprint`/`PortPrototypeBlueprintInitValue`. The spec spells the package `PortProtoypeBlueprint` (spec's own typo); the module already uses the corrected spelling at the correct depth — the report itself notes "the location is the deviation, not the spelling". We keep the corrected spelling; this row is an **accepted deviation**.
2. **Section C** (17 leaf packages hosting classes in `__init__.py`): the report lists them as "candidates, not confirmed violations" needing judgement calls. **Out of scope** — separate follow-up plan if desired.
3. **Section D** (`X/` beside `X.py` shadowing): already fixed by commit `86764353`; directories no longer exist. Verified in Task 1 only.
4. **Section E**: `ModeInBswModuleDescriptionInstanceRef` stays in `KNOWN_NAME_COLLISION_CLASSES` (its fix depends on the Section C decision for `BswOverview/InstanceRefs/`). The 3 stale `BswEntryRelationship*` entries and the 26 synced-class entries are removed.
5. Spec `Package` rows were re-verified against `autosar/R23-11/markdown/*.md` for every row touched by this plan (e.g. `RunnableEntity` → `…::SwcInternalBehavior` stays put; only `RunnableEntityArgument` moves; `EcuInstance` → `…::FibexCore::CoreTopology`). If a spec table contradicts a task below, **stop and ask** — do not improvise.

## Conventions used by every task

- Repo root is the working directory for all commands. macOS `sed -i ''` syntax is used.
- Quick test loop: `python scripts/run_tests.py -k "not integration" --no-coverage`
- Full suite (REQUIRED before every commit): `python scripts/run_tests.py`
- Lint (REQUIRED before every commit): `npm run lint`
- Format (REQUIRED before every commit): `npm run black`
- Class-block mover (created in Task 2): `python scripts/move_class_blocks.py SOURCE TARGET ClassName…` — moves top-level `class` blocks plus their directly-attached leading comment lines (the `# […] checklist` comment clusters). It does **not** touch imports; after every move you fix imports by hand and let `npm run lint` catch leftovers (F401 unused / F821 undefined).
- When a task says "split the import", it means: a line like `from X import (A, B, C)` where only `B` moved becomes two lines — `from Y import B` (new location) and `from X import (A, C)` (or `from X import A, C`). Run `npm run black` after splitting.
- Import cycles: if a move creates a circular module import, break it with a function-level import inside the method that needs it (established codebase pattern, see commit `ce4a7c9c`). Never add a re-export shim to the OLD module.
- Line numbers in `src/armodel/models/__init__.py` drift as tasks proceed; every edit below is given as **old text → new text**, matched uniquely. Use the text, not the line number.
- Commit style: `refactor(models): <what> (Rule 0007)` — one commit per task.

---

### Task 1: Baseline verification

**Files:** none (verification only)

- [ ] **Step 1: Confirm Section D is already resolved**

```bash
ls -d src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/ \
      src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ \
      src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventVfb/ 2>&1
```

Expected: three `No such file or directory` errors. If any directory exists, STOP — the plan's assumptions are stale.

- [ ] **Step 2: Run the full test suite**

Run: `python scripts/run_tests.py`
Expected: all tests PASS. Record the counts (you will compare against them after every task).

- [ ] **Step 3: Lint and format check**

Run: `npm run lint && npm run black-check`
Expected: clean exit.

---

### Task 2: Class-block mover script

**Files:**
- Create: `scripts/move_class_blocks.py`
- Test: `tests/test_scripts/test_move_class_blocks.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_scripts/test_move_class_blocks.py`:

```python
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent.parent / "scripts" / "move_class_blocks.py"


def run_mover(source, target, *classes):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(source), str(target), *classes], capture_output=True, text=True
    )


def test_moves_class_with_leading_comments(tmp_path):
    src = tmp_path / "src.py"
    src.write_text("import x\n\n\n# checklist for A\nclass A:\n    pass\n\n\n# checklist for B\nclass B:\n    pass\n")
    tgt = tmp_path / "tgt.py"
    tgt.write_text("class Z:\n    pass\n")

    result = run_mover(src, tgt, "A")

    assert result.returncode == 0, result.stderr
    assert "class A" not in src.read_text()
    assert "# checklist for A" not in src.read_text()
    assert "# checklist for B" in src.read_text()
    assert "class B" in src.read_text()
    assert "class A:" in tgt.read_text()
    assert "# checklist for A" in tgt.read_text()
    assert "class Z:" in tgt.read_text()


def test_missing_class_fails_with_message(tmp_path):
    src = tmp_path / "src.py"
    src.write_text("class A:\n    pass\n")
    tgt = tmp_path / "tgt.py"
    tgt.write_text("")

    result = run_mover(src, tgt, "Nope")

    assert result.returncode != 0
    assert "Nope" in result.stderr
    assert "class A" in src.read_text()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_scripts/test_move_class_blocks.py -v`
Expected: FAIL / ERROR (file `scripts/move_class_blocks.py` does not exist).

- [ ] **Step 3: Write the implementation**

Create `scripts/move_class_blocks.py`:

```python
#!/usr/bin/env python3
"""Move top-level class blocks from one module to another (Rule 0007 helper).

Usage:
    python scripts/move_class_blocks.py SOURCE TARGET ClassName [ClassName ...]

Removes the named top-level classes together with their directly attached
leading comment lines from SOURCE and appends them to TARGET. Import
statements are deliberately NOT touched: fix imports by hand afterwards and
let `npm run lint` report leftovers (F401 unused / F821 undefined).
"""
import argparse
import re
import sys

CLASS_RE = re.compile(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)")


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines(keepends=True)


def save(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.write("".join(lines))


def class_blocks(lines):
    starts = []
    for i, line in enumerate(lines):
        m = CLASS_RE.match(line)
        if m:
            starts.append((i, m.group(1)))
    blocks = {}
    for idx, (i, name) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        s = i
        while s > 0 and lines[s - 1].lstrip().startswith("#"):
            s -= 1
        blocks[name] = (s, end)
    return blocks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("target")
    parser.add_argument("classes", nargs="+")
    args = parser.parse_args()

    src = load(args.source)
    blocks = class_blocks(src)
    missing = [c for c in args.classes if c not in blocks]
    if missing:
        sys.exit("not found in {}: {}".format(args.source, ", ".join(missing)))

    ranges = sorted(blocks[c] for c in args.classes)
    moved = ["".join(src[s:e]).rstrip("\n") + "\n" for s, e in ranges]
    for s, e in reversed(ranges):
        del src[s:e]

    text = "".join(src)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    if text and not text.endswith("\n"):
        text += "\n"
    save(args.source, text.splitlines(keepends=True))

    tgt = load(args.target)
    if tgt and not "".join(tgt).endswith("\n"):
        tgt.append("\n")
    for block in moved:
        tgt.append("\n")
        tgt.append(block)
    save(args.target, tgt)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_scripts/test_move_class_blocks.py -v`
Expected: 2 PASS.

- [ ] **Step 5: Lint, format, commit**

```bash
npm run lint && npm run black
git add scripts/move_class_blocks.py tests/test_scripts/test_move_class_blocks.py
git commit -m "chore(scripts): add move_class_blocks helper for Rule 0007 relocations"
```

---

### Task 3: Section B — rename `DoIp.py` to `DoIP.py`

Spec writes the package `M2::AUTOSARTemplates::SystemTemplate::DoIP`; the module is `DoIp.py`. Identical on a case-insensitive filesystem, a real import break on a case-sensitive one.

**Files:**
- Rename: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py` → `DoIP.py`
- Modify: `src/armodel/models/__init__.py`, `src/armodel/parser/arxml_parser.py`, `src/armodel/writer/arxml_writer.py`, plus any test hit by the grep below
- Rename: `tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/test_DoIp.py` → `test_DoIP.py`

- [ ] **Step 1: Rename the module and its test mirror**

```bash
git mv src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIP.py
git mv tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/test_DoIp.py tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/test_DoIP.py
```

- [ ] **Step 2: Rewrite every reference to the old path**

```bash
grep -rn "SystemTemplate\.DoIp" src tests --include="*.py" | grep -v __pycache__
grep -rl "SystemTemplate\.DoIp" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/SystemTemplate\.DoIp/SystemTemplate.DoIP/g'
```

Expected: the grep lists ~4 files (`models/__init__.py`, `parser/arxml_parser.py`, `writer/arxml_writer.py`, `SystemTemplate/test_DoIp.py` before its rename). After the sed, re-running the grep must output nothing.

- [ ] **Step 3: Verify old path is dead, new path works**

```bash
grep -rn "SystemTemplate\.DoIp\b" src tests --include="*.py" | grep -v __pycache__; echo "exit=$?"
python -c "from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import AbstractDoIpLogicAddressProps, DoIpLogicTargetAddressProps, DoIpLogicTesterAddressProps; print('ok')"
```

Expected: `exit=1` (no matches) and `ok`.

- [ ] **Step 4: Full test suite, lint, black, commit**

```bash
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): rename SystemTemplate.DoIp module to DoIP per spec package (Rule 0007 B)"
```

---

### Task 4: Section E quick wins — 6 importable classes + 3 stale collision entries

`McDataAccessDetails`, `ModeErrorBehavior`, `ModeErrorReactionPolicyEnum`, `ModeTransition`, `TimingCondition`, `TimingExtensionResource` are already importable from `armodel` but still excluded. The `BswEntryRelationship*` collision entries are stale (the classes import fine; the `BswInterfaces/` directory no longer exists).

**Files:**
- Modify: `tests/test_armodel/test_model_imports.py`

- [ ] **Step 1: Remove the 9 stale entries (this makes the test stricter — it must still pass)**

In `tests/test_armodel/test_model_imports.py`:

1. In `KNOWN_NAME_COLLISION_CLASSES` delete:
```python
    # BswInterfaces/*.py files (3 classes)
    "BswEntryRelationship",
    "BswEntryRelationshipEnum",
    "BswEntryRelationshipSet",
```
2. In `INTENTIONALLY_UNEXPORTED_MODULES` delete these 6 lines:
```python
    "McDataAccessDetails",
    "ModeErrorBehavior",
    "ModeErrorReactionPolicyEnum",
    "ModeTransition",
    "TimingCondition",
    "TimingExtensionResource",
```
3. Update the module docstring's "Known limitation" paragraph to:
```python
"""
Test to verify all model classes can be imported from armodel directly.

This test ensures that all model classes defined in the codebase can be
imported from the top-level `armodel` module, confirming that wildcard imports
are properly configured throughout the package structure.

Known limitation: 1 class in a subdirectory with a name collision cannot be
directly imported and is excluded from this test:
- BswOverview/InstanceRefs/*.py files (1 class)
"""
```

- [ ] **Step 2: Run the import test**

Run: `python -m pytest tests/test_armodel/test_model_imports.py -v`
Expected: PASS. If it fails on any of the 9 names, that name is NOT actually importable — restore its entry and note it for Task 17 instead of forcing it.

- [ ] **Step 3: Full suite, lint, black, commit**

```bash
python scripts/run_tests.py && npm run lint && npm run black
git add tests/test_armodel/test_model_imports.py
git commit -m "test(models): drop 6 synced classes and 3 stale collisions from import exclusions (Rule 0007 E)"
```

---

### Task 5: MSR::Documentation family — remove the spurious `TextModel` level for BlockElements/MsrQuery

Spec packages: `M2::MSR::Documentation::BlockElements::{ListElements,Note,PaginationAndView,RequirementsTracing}` and `M2::MSR::Documentation::MsrQuery` (verified in `AUTOSAR_FO_TPS_GenericStructureTemplate.md`). `MsrQueryChapter`/`MsrQueryTopic1` (currently in `Chapters.py`) are members of `MsrQuery`.

**Files:**
- Move: `src/armodel/models/M2/MSR/Documentation/TextModel/BlockElements/{ListElements,Note,PaginationAndView,RequirementsTracing}.py` → `src/armodel/models/M2/MSR/Documentation/BlockElements/`
- Move: `src/armodel/models/M2/MSR/Documentation/TextModel/MsrQuery.py` → `src/armodel/models/M2/MSR/Documentation/MsrQuery.py`
- Modify: `Chapters.py` (loses 2 classes), `src/armodel/models/__init__.py`, consumers found by grep
- Move test mirrors: `tests/test_armodel/models/M2/MSR/Documentation/TextModel/test_MsrQuery.py` and `tests/.../TextModel/BlockElements/test_*.py` → mirrored new locations

- [ ] **Step 1: Move the four BlockElements modules and MsrQuery**

```bash
cd src/armodel/models/M2/MSR/Documentation
git mv TextModel/BlockElements/ListElements.py BlockElements/ListElements.py
git mv TextModel/BlockElements/Note.py BlockElements/Note.py
git mv TextModel/BlockElements/PaginationAndView.py BlockElements/PaginationAndView.py
git mv TextModel/BlockElements/RequirementsTracing.py BlockElements/RequirementsTracing.py
git mv TextModel/MsrQuery.py MsrQuery.py
cd -
```

- [ ] **Step 2: Fold MsrQueryChapter and MsrQueryTopic1 into MsrQuery.py**

```bash
python scripts/move_class_blocks.py \
  src/armodel/models/M2/MSR/Documentation/Chapters.py \
  src/armodel/models/M2/MSR/Documentation/MsrQuery.py \
  MsrQueryChapter MsrQueryTopic1
```

Then open `MsrQuery.py` and add whatever imports the two moved classes need (copy them from the top of `Chapters.py`); remove now-unused imports from `Chapters.py`. `npm run lint` flags both directions (F821 undefined in target, F401 unused in source).

- [ ] **Step 3: Rewrite consumers of the old paths**

```bash
grep -rl "Documentation\.TextModel\.BlockElements\.\(ListElements\|Note\|PaginationAndView\|RequirementsTracing\)" src tests --include="*.py" | grep -v __pycache__ \
  | xargs sed -i '' 's/Documentation\.TextModel\.BlockElements\./Documentation.BlockElements./g'
grep -rl "Documentation\.TextModel\.MsrQuery" src tests --include="*.py" | grep -v __pycache__ \
  | xargs sed -i '' 's/Documentation\.TextModel\.MsrQuery/Documentation.MsrQuery/g'
```

Special case — any consumer importing `MsrQueryChapter`/`MsrQueryTopic1` from `Documentation.Chapters` must be re-pointed to `Documentation.MsrQuery`:

```bash
grep -rn "Chapters import.*MsrQuery" src tests --include="*.py" | grep -v __pycache__
```

For each hit, split the import so the two `MsrQuery*` names come from `…Documentation.MsrQuery` and the rest stay on `…Documentation.Chapters`.

- [ ] **Step 4: Update `src/armodel/models/__init__.py`**

- `from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import *  # noqa: F403` → `from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import *  # noqa: F403`
- `from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import *  # noqa: F403` → `from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import *  # noqa: F403`
- Delete `from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import Traceable  # noqa: F401`
- Add (next to the ListElements line):
```python
from armodel.models.M2.MSR.Documentation.BlockElements.Note import *  # noqa: F403
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import *  # noqa: F403
from armodel.models.M2.MSR.Documentation.MsrQuery import *  # noqa: F403
```

- [ ] **Step 5: Move the test mirrors**

```bash
git mv tests/test_armodel/models/M2/MSR/Documentation/TextModel/test_MsrQuery.py tests/test_armodel/models/M2/MSR/Documentation/test_MsrQuery.py
ls tests/test_armodel/models/M2/MSR/Documentation/TextModel/BlockElements/
```

`git mv` each `test_<Module>.py` matching a moved module into `tests/test_armodel/models/M2/MSR/Documentation/BlockElements/` (create the directory if needed; it already exists with `test_Figure.py`-style files). `test___init__.py` (tests `DocumentationBlock`, which does NOT move) stays. Fix the import lines inside the moved test files with the same sed pattern from Step 3. If `MsrQueryChapter`/`MsrQueryTopic1` tests live inside `tests/.../Documentation/test_Chapters.py`, move those test classes into `test_MsrQuery.py`.

- [ ] **Step 6: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryChapter; from armodel.models.M2.MSR.Documentation.BlockElements.Note import Note; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): relocate Documentation BlockElements/MsrQuery modules out of TextModel (Rule 0007 A)"
```

---

### Task 6: FibexCore family — CoreCommunication becomes a package, Timing moves under it

Spec packages: `Timing` classes → `…::FibexCore::CoreCommunication::Timing`; `FibexElement` → `…::FibexCore` (direct member); `CommConnectorPort` and `EcuInstance` → `…::FibexCore::CoreTopology`.

**Files:**
- Convert: `FibexCore/CoreCommunication.py` → `FibexCore/CoreCommunication/__init__.py`
- Move: `FibexCore/Timing.py` → `FibexCore/CoreCommunication/Timing.py`
- Modify: `FibexCore/__init__.py` (gains `FibexElement`), `FibexCore/CoreTopology.py` (gains `CommConnectorPort`, `EcuInstance`), delete `FibexCore/EcuInstance.py`
- Modify: `src/armodel/models/__init__.py`, consumers
- Test mirrors: `tests/.../FibexCore/test_Timing.py` → `tests/.../FibexCore/CoreCommunication/`, `test_EcuInstance.py` → merge next to `test_CoreTopology.py`

- [ ] **Step 1: Convert CoreCommunication to a package and move Timing under it**

```bash
cd src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore
mkdir CoreCommunication_tmp
git mv CoreCommunication.py CoreCommunication_tmp/__init__.py
git mv CoreCommunication_tmp CoreCommunication
git mv Timing.py CoreCommunication/Timing.py
cd -
```

- [ ] **Step 2: Move FibexElement, CommConnectorPort, EcuInstance**

```bash
python scripts/move_class_blocks.py \
  src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py \
  src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/__init__.py \
  FibexElement
python scripts/move_class_blocks.py \
  src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py \
  src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py \
  CommConnectorPort
python scripts/move_class_blocks.py \
  src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py \
  src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py \
  EcuInstance
git rm src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py
```

Fix imports in the three edited files by hand (copy needed imports from the old headers; drop unused ones). `FibexCore/__init__.py` needs the imports `FibexElement` used (e.g. `PackageableElement` from `…GeneralTemplateClasses/Identifiable.py`). If `CoreTopology.py` ↔ `CoreCommunication/__init__.py` form a cycle, break it with a function-level import in the method that uses it.

- [ ] **Step 3: Rewrite consumers**

```bash
grep -rl "FibexCore\.EcuInstance" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/FibexCore\.EcuInstance/FibexCore.CoreTopology/g'
grep -rl "FibexCore\.Timing" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/FibexCore\.Timing/FibexCore.CoreCommunication.Timing/g'
```

`FibexCore.CoreCommunication` imports keep working unchanged (package `__init__`). `FibexElement`/`CommConnectorPort` consumers that imported them from `…CoreCommunication import …` must be split — find them:

```bash
grep -rn "FibexCore\.CoreCommunication import" src tests --include="*.py" | grep -v __pycache__ | grep -E "FibexElement|CommConnectorPort"
```

For each hit, split so `FibexElement` comes from `…Fibex.FibexCore` and `CommConnectorPort` from `…FibexCore.CoreTopology`.

- [ ] **Step 4: Update `src/armodel/models/__init__.py`**

- Delete `from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.EcuInstance import *  # noqa: F403`
- `from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import *  # noqa: F403` → `from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import *  # noqa: F403`
- Add next to the CoreCommunication line: `from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import *  # noqa: F403`

- [ ] **Step 5: Move test mirrors**

```bash
mkdir -p tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication
touch tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py
git mv tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/test_Timing.py \
       tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/test_Timing.py
```

`EcuInstance` test classes: move the `EcuInstance` test class(es) from `test_EcuInstance.py` into `test_CoreTopology.py` (append, fix imports), then `git rm tests/.../FibexCore/test_EcuInstance.py`. Apply the Step 3 sed patterns to the moved files too.

- [ ] **Step 6: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement; from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance, CommConnectorPort; from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import CyclicTiming; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): restructure FibexCore per spec packages - CoreCommunication pkg, Timing, FibexElement, CommConnectorPort, EcuInstance (Rule 0007 A)"
```

---

### Task 7: Fibex topology classes + Fibex4Ethernet family

Spec packages (verified in `AUTOSAR_CP_TPS_SystemTemplate.md`): `GenericTp`, `TcpTp`, `TcpUdpConfig`, `TpPort`, `TransportProtocolConfiguration`, `UdpTp` → `…::Fibex4Ethernet::EthernetTopology`; `RequestResponseDelay` → `…::Fibex4Ethernet::ServiceInstances`; `IPv6ExtHeaderFilterList` → `…::IPv6HeaderFilterList`; `TcpOptionFilterList`, `TcpOptionFilterSet` → `…::TcpOptionFilterSet`; `SoAdRoutingGroup`, `SocketConnection` → `…::ObsoleteModel`; `EthernetPhysicalChannel`, `VlanConfig` → `…::Fibex4Ethernet::EthernetTopology`; `CanClusterBusOffRecovery` → `…::Fibex4Can::CanTopology`; `FlexrayPhysicalChannel` → `…::Fibex4Flexray::FlexrayTopology`; `LinPhysicalChannel` → `…::Fibex4Lin::LinTopology`.

**Files:**
- Modify: `Fibex4Ethernet/ServiceInstances.py`, `Fibex4Ethernet/EthernetTopology.py`, `Fibex4Ethernet/EthernetCommunication.py`, `Fibex4Ethernet/ObsoleteModel.py`, `FibexCore/CoreTopology.py`, `Fibex4Can/CanTopology.py`, `Fibex4Flexray/FlexrayTopology.py`, `Fibex4Lin/LinTopology.py`
- Create: `Fibex4Ethernet/IPv6HeaderFilterList.py`, `Fibex4Ethernet/TcpOptionFilterSet.py`
- Modify: `src/armodel/models/__init__.py`, consumers

- [ ] **Step 1: Create the two new leaf modules and move classes**

```bash
MODELS=src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex
touch $MODELS/Fibex4Ethernet/IPv6HeaderFilterList.py $MODELS/Fibex4Ethernet/TcpOptionFilterSet.py
python scripts/move_class_blocks.py $MODELS/Fibex4Ethernet/EthernetCommunication.py $MODELS/Fibex4Ethernet/IPv6HeaderFilterList.py IPv6ExtHeaderFilterList
python scripts/move_class_blocks.py $MODELS/Fibex4Ethernet/EthernetCommunication.py $MODELS/Fibex4Ethernet/TcpOptionFilterSet.py TcpOptionFilterList TcpOptionFilterSet
python scripts/move_class_blocks.py $MODELS/Fibex4Ethernet/EthernetCommunication.py $MODELS/Fibex4Ethernet/ObsoleteModel.py SoAdRoutingGroup SocketConnection
python scripts/move_class_blocks.py $MODELS/Fibex4Ethernet/ServiceInstances.py $MODELS/Fibex4Ethernet/EthernetTopology.py GenericTp TcpTp TcpUdpConfig TpPort TransportProtocolConfiguration UdpTp
python scripts/move_class_blocks.py $MODELS/Fibex4Ethernet/EthernetTopology.py $MODELS/Fibex4Ethernet/ServiceInstances.py RequestResponseDelay
python scripts/move_class_blocks.py $MODELS/FibexCore/CoreTopology.py $MODELS/Fibex4Ethernet/EthernetTopology.py EthernetPhysicalChannel VlanConfig
python scripts/move_class_blocks.py $MODELS/FibexCore/CoreTopology.py $MODELS/Fibex4Can/CanTopology.py CanClusterBusOffRecovery
python scripts/move_class_blocks.py $MODELS/FibexCore/CoreTopology.py $MODELS/Fibex4Flexray/FlexrayTopology.py FlexrayPhysicalChannel
python scripts/move_class_blocks.py $MODELS/FibexCore/CoreTopology.py $MODELS/Fibex4Lin/LinTopology.py LinPhysicalChannel
```

For each edited file: move/copy the imports the classes need into the target, delete unused imports from the source. New files need a module docstring + their imports. If `EthernetTopology.py` ↔ `ServiceInstances.py` cycle appears, break with function-level imports (existing pattern in these very files, see commit `ce4a7c9c`).

- [ ] **Step 2: Rewrite consumers**

For each of the moved class names, find consumers importing it from the OLD module and re-point to the NEW module:

```bash
grep -rn "EthernetCommunication import" src tests --include="*.py" | grep -v __pycache__ | grep -E "IPv6ExtHeaderFilterList|TcpOptionFilterList|TcpOptionFilterSet|SoAdRoutingGroup|SocketConnection"
grep -rn "ServiceInstances import" src tests --include="*.py" | grep -v __pycache__ | grep -E "GenericTp|TcpTp|TcpUdpConfig|TpPort|TransportProtocolConfiguration|UdpTp"
grep -rn "EthernetTopology import" src tests --include="*.py" | grep -v __pycache__ | grep "RequestResponseDelay"
grep -rn "FibexCore\.CoreTopology import" src tests --include="*.py" | grep -v __pycache__ | grep -E "EthernetPhysicalChannel|VlanConfig|CanClusterBusOffRecovery|FlexrayPhysicalChannel|LinPhysicalChannel"
```

For every hit, split the import so the moved names come from the new module path (`…Fibex4Ethernet.IPv6HeaderFilterList`, `…Fibex4Ethernet.TcpOptionFilterSet`, `…Fibex4Ethernet.ObsoleteModel`, `…Fibex4Ethernet.EthernetTopology`, `…Fibex4Ethernet.ServiceInstances`, `…Fibex4Can.CanTopology`, `…Fibex4Flexray.FlexrayTopology`, `…Fibex4Lin.LinTopology`).

- [ ] **Step 3: Update `src/armodel/models/__init__.py`**

Add (next to the existing Fibex4Ethernet lines):
```python
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import *  # noqa: F403
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import *  # noqa: F403
```
(The `EthernetCommunication`, `EthernetTopology`, `ServiceInstances`, `ObsoleteModel`, `CanTopology`, `FlexrayTopology`, `LinTopology` wildcard lines already exist.)

- [ ] **Step 4: Move/merge test mirrors**

Move test classes for relocated classes into the test module mirroring the new defining module (e.g. the `TcpTp`/`GenericTp` test classes from `tests/.../Fibex4Ethernet/test_ServiceInstances.py` into `test_EthernetTopology.py`; `RequestResponseDelay` tests the other way). Create `tests/.../Fibex4Ethernet/test_IPv6HeaderFilterList.py` and `test_TcpOptionFilterSet.py` if tests exist for those classes. Empty test files get `git rm`.

- [ ] **Step 5: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import TcpTp, EthernetPhysicalChannel, VlanConfig; from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import RequestResponseDelay; from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanClusterBusOffRecovery; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): relocate Fibex topology/Tp/filter classes to spec Package modules (Rule 0007 A)"
```

---

### Task 8: SWComponentTemplate — Components/InstanceRefs and SwComponentType

Spec packages: `OperationInAtomicSwcInstanceRef`, `POperationInAtomicSwcInstanceRef`, `ROperationInAtomicSwcInstanceRef` → `…::SWComponentTemplate::Components::InstanceRefs`; `SwComponentType` → `…::SWComponentTemplate::Components`.

**Files:**
- Create: `SWComponentTemplate/Components/InstanceRefs.py`
- Modify: `SWComponentTemplate/Composition/InstanceRefs.py` (loses 3 classes), `SWComponentTemplate/Components/__init__.py` (gains `SwComponentType`), delete `SWComponentTemplate/SwComponentType.py`
- Modify: `src/armodel/models/__init__.py`, consumers
- Test: `tests/.../SWComponentTemplate/test_SwComponentType.py` → merge into `tests/.../SWComponentTemplate/Components/test___init__.py` (or a new `test_InstanceRefs.py` for the InstanceRefs)

- [ ] **Step 1: Create Components/InstanceRefs.py and move the three classes**

```bash
MODELS=src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate
touch $MODELS/Components/InstanceRefs.py
python scripts/move_class_blocks.py $MODELS/Composition/InstanceRefs.py $MODELS/Components/InstanceRefs.py \
  OperationInAtomicSwcInstanceRef POperationInAtomicSwcInstanceRef ROperationInAtomicSwcInstanceRef
```

Add to `Components/InstanceRefs.py` the imports the three classes need (copy from `Composition/InstanceRefs.py`'s header). Note: `ROperationInAtomicSwcInstanceRef` is imported by `SwcInternalBehavior/ServerCall.py` — update that file to `from …SWComponentTemplate.Components.InstanceRefs import ROperationInAtomicSwcInstanceRef`.

- [ ] **Step 2: Move SwComponentType into Components/__init__.py**

```bash
python scripts/move_class_blocks.py $MODELS/SwComponentType.py $MODELS/Components/__init__.py SwComponentType
git rm $MODELS/SwComponentType.py
```

Copy the imports `SwComponentType` needs into `Components/__init__.py`. If `Components/__init__.py` ↔ `Composition/…` cycles appear, break with function-level imports.

- [ ] **Step 3: Rewrite consumers**

```bash
grep -rn "Composition\.InstanceRefs import" src tests --include="*.py" | grep -v __pycache__ | grep -E "OperationInAtomicSwcInstanceRef"
grep -rn "SWComponentTemplate\.SwComponentType import" src tests --include="*.py" | grep -v __pycache__
```

For each hit of the first grep: split the import so the moved names come from `…SWComponentTemplate.Components.InstanceRefs`. For the second: re-point to `…SWComponentTemplate.Components` (`sed -i '' 's/SWComponentTemplate\.SwComponentType import/SWComponentTemplate.Components import/g'` works for single-source hits).

- [ ] **Step 4: Update `src/armodel/models/__init__.py`**

- Delete `from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import *  # noqa: F403`
- Add: `from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import *  # noqa: F403`
(The `SWComponentTemplate.Components import *` line already exists.)

- [ ] **Step 5: Move test mirrors**

Move the test classes for the three InstanceRefs from `tests/.../Composition/test_InstanceRefs.py` into a new `tests/.../Components/test_InstanceRefs.py` (create `__init__.py` if the dir lacks one); move `SwComponentType` tests from `tests/.../SWComponentTemplate/test_SwComponentType.py` into `tests/.../Components/test___init__.py`; `git rm` emptied files.

- [ ] **Step 6: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SwComponentType; from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ROperationInAtomicSwcInstanceRef; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): move SwComponentType and Operation InstanceRefs to Components package (Rule 0007 A)"
```

---

### Task 9: SwcInternalBehavior family + cross-package stragglers

Spec packages (verified): `AsynchronousServerCallPoint`, `AsynchronousServerCallResultPoint`, `SynchronousServerCallPoint` → `…::SwcInternalBehavior::ServerCall`; `RunnableEntityArgument` → `…::SwcInternalBehavior::RunnableEntity` (new leaf module; `RunnableEntity` itself stays in `__init__.py` — its spec package is `…::SwcInternalBehavior`); `AutosarVariableRef`, `AutosarParameterRef`, `ArVariableInImplementationDataInstanceRef` → `…::SwcInternalBehavior::DataElements`; `ParameterInAtomicSWCTypeInstanceRef`, `VariableInAtomicSWCTypeInstanceRef` → `…::SwcInternalBehavior::DataElements::InstanceRefsUsage`; `ExternalTriggeringPointIdent` → `…::SWComponentTemplate::RPTScenario`; `RoleBasedDataTypeAssignment` → `…::SwcInternalBehavior::ServiceMapping`; `EndToEndProtectionISignalIPdu` → `…::SystemTemplate::EndToEndProtection`.

**Files:**
- Modify: `SwcInternalBehavior/__init__.py`, `SwcInternalBehavior/ServerCall.py`, `SwcInternalBehavior/Trigger.py`, `SWComponentTemplate/RPTScenario.py`, `CommonStructure/ServiceNeeds.py`, `SwcInternalBehavior/ServiceMapping.py`, `SWComponentTemplate/EndToEndProtection.py`
- Convert: `SwcInternalBehavior/DataElements.py` → `SwcInternalBehavior/DataElements/__init__.py`; create `SwcInternalBehavior/DataElements/InstanceRefsUsage.py`; delete `SwcInternalBehavior/AutosarVariableRef.py` and `SwcInternalBehavior/InstanceRefsUsage.py`
- Create: `SwcInternalBehavior/RunnableEntity.py`, `SystemTemplate/EndToEndProtection.py`
- Modify: `src/armodel/models/__init__.py`, consumers, test mirrors

- [ ] **Step 1: Convert DataElements to a package and spread the InstanceRefs classes**

```bash
MODELS=src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior
mkdir DataElements_tmp
git mv DataElements.py DataElements_tmp/__init__.py
git mv DataElements_tmp DataElements
touch DataElements/InstanceRefsUsage.py
python scripts/move_class_blocks.py $MODELS/InstanceRefsUsage.py $MODELS/DataElements/__init__.py ArVariableInImplementationDataInstanceRef AutosarParameterRef
python scripts/move_class_blocks.py $MODELS/InstanceRefsUsage.py $MODELS/DataElements/InstanceRefsUsage.py ParameterInAtomicSWCTypeInstanceRef VariableInAtomicSWCTypeInstanceRef
python scripts/move_class_blocks.py $MODELS/AutosarVariableRef.py $MODELS/DataElements/__init__.py AutosarVariableRef
git rm $MODELS/AutosarVariableRef.py $MODELS/InstanceRefsUsage.py
```

`AutosarVariableRef.py` may hold more than the one class — run `grep -n "^class" $MODELS/AutosarVariableRef.py` FIRST; move every class it defines (they are all members of `…::DataElements`), then delete the file. Fix imports in all touched files.

- [ ] **Step 2: ServerCall classes and RunnableEntityArgument**

```bash
python scripts/move_class_blocks.py $MODELS/__init__.py $MODELS/ServerCall.py \
  AsynchronousServerCallPoint AsynchronousServerCallResultPoint SynchronousServerCallPoint
touch $MODELS/RunnableEntity.py
python scripts/move_class_blocks.py $MODELS/__init__.py $MODELS/RunnableEntity.py RunnableEntityArgument
```

In `$MODELS/__init__.py` add explicit re-imports (consumers import these from the package):
```python
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    AsynchronousServerCallPoint,
    AsynchronousServerCallResultPoint,
    SynchronousServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntity import RunnableEntityArgument
```
Copy the imports the moved classes need into `ServerCall.py` / `RunnableEntity.py` (e.g. `AbstractAccessPoint`, `ServerCallPoint`).

- [ ] **Step 3: ExternalTriggeringPointIdent, RoleBasedDataTypeAssignment, EndToEndProtectionISignalIPdu**

```bash
python scripts/move_class_blocks.py $MODELS/Trigger.py ../RPTScenario.py ExternalTriggeringPointIdent
python scripts/move_class_blocks.py ../../CommonStructure/ServiceNeeds.py $MODELS/ServiceMapping.py RoleBasedDataTypeAssignment
touch ../../SystemTemplate/EndToEndProtection.py
python scripts/move_class_blocks.py ../EndToEndProtection.py ../../SystemTemplate/EndToEndProtection.py EndToEndProtectionISignalIPdu
```

(Paths above are relative to `$MODELS`; run from repo root with full paths if preferred.) Check `SWComponentTemplate/EndToEndProtection.py` still defines classes after the move — if it is now empty, `git rm` it and drop its wildcard line from `models/__init__.py`; otherwise keep it. `RPTScenario.py` and `ServiceMapping.py` gain the imports those classes need.

- [ ] **Step 4: Rewrite consumers**

```bash
grep -rl "SwcInternalBehavior\.AutosarVariableRef" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/SwcInternalBehavior\.AutosarVariableRef/SwcInternalBehavior.DataElements/g'
grep -rl "SwcInternalBehavior\.InstanceRefsUsage" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/SwcInternalBehavior\.InstanceRefsUsage/SwcInternalBehavior.DataElements.InstanceRefsUsage/g'
```

The second sed is only correct for the two classes that go to `DataElements.InstanceRefsUsage`. Fix the other two by hand:
```bash
grep -rn "DataElements\.InstanceRefsUsage import" src tests --include="*.py" | grep -v __pycache__ | grep -E "ArVariableInImplementationDataInstanceRef|AutosarParameterRef"
```
Split each hit: those two names import from `…SwcInternalBehavior.DataElements`. Then:
```bash
grep -rn "RPTScenario\|ServiceMapping" src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py | grep import | grep -E "ExternalTriggeringPointIdent|RoleBasedDataTypeAssignment"
grep -rn "SWComponentTemplate\.EndToEndProtection import" src tests --include="*.py" | grep -v __pycache__ | grep EndToEndProtectionISignalIPdu
```
Re-point `ExternalTriggeringPointIdent` to `…SWComponentTemplate.RPTScenario`, `RoleBasedDataTypeAssignment` to `…SwcInternalBehavior.ServiceMapping`, `EndToEndProtectionISignalIPdu` to `…SystemTemplate.EndToEndProtection`.

- [ ] **Step 5: Update `src/armodel/models/__init__.py`**

- `from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import *  # noqa: F403` → `from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import *  # noqa: F403`
- Delete `from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import *  # noqa: F403`
- Add: `from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import *  # noqa: F403` and `from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import *  # noqa: F403`
- Keep the `SWComponentTemplate.EndToEndProtection import *` line if that module still defines classes.

- [ ] **Step 6: Move test mirrors**

```bash
TESTS=tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior
mkdir -p $TESTS/DataElements && touch $TESTS/DataElements/__init__.py
git mv $TESTS/test_DataElements.py $TESTS/DataElements/test___init__.py
git mv $TESTS/test_InstanceRefsUsage.py $TESTS/DataElements/test_InstanceRefsUsage.py
git mv $TESTS/test_AutosarVariableRef.py $TESTS/DataElements/test___init___autosarvariableref.py
```

(The last file tests classes now living in `DataElements/__init__.py`; alternatively merge its test classes into `test___init__.py` and `git rm` it.) Move `ExternalTriggeringPointIdent` tests into `tests/.../SWComponentTemplate/test_RPTScenario.py`, `RoleBasedDataTypeAssignment` tests into `$TESTS/test_ServiceMapping.py`, `EndToEndProtectionISignalIPdu` tests into `tests/.../SystemTemplate/test_EndToEndProtection.py` (create if missing).

- [ ] **Step 7: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import AsynchronousServerCallPoint, RunnableEntityArgument; from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef; from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef; from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): relocate SwcInternalBehavior classes to spec Package modules (Rule 0007 A)"
```

---

### Task 10: ImplicitCommunicationBehavior — `InstanceRefs.py` → `InstanceRef.py`

Spec package is `…::ImplicitCommunicationBehavior::InstanceRef` (singular).

**Files:**
- Rename: `SWComponentTemplate/ImplicitCommunicationBehavior/InstanceRefs.py` → `InstanceRef.py`
- Modify: consumers; test mirror rename

- [ ] **Step 1: Rename module and test mirror**

```bash
git mv src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ImplicitCommunicationBehavior/InstanceRefs.py \
       src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ImplicitCommunicationBehavior/InstanceRef.py
git mv tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ImplicitCommunicationBehavior/test_InstanceRefs.py \
       tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ImplicitCommunicationBehavior/test_InstanceRef.py 2>/dev/null || true
```

- [ ] **Step 2: Rewrite consumers and models/__init__.py**

```bash
grep -rl "ImplicitCommunicationBehavior\.InstanceRefs" src tests --include="*.py" | grep -v __pycache__ \
  | xargs sed -i '' 's/ImplicitCommunicationBehavior\.InstanceRefs/ImplicitCommunicationBehavior.InstanceRef/g'
```

In `src/armodel/models/__init__.py`: `…ImplicitCommunicationBehavior.InstanceRefs import *  # noqa: F403` → `…ImplicitCommunicationBehavior.InstanceRef import *  # noqa: F403`.

- [ ] **Step 3: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import RunnableEntityInCompositionInstanceRef; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): rename ImplicitCommunicationBehavior.InstanceRefs module to InstanceRef (Rule 0007 A)"
```

---

### Task 11: Transformer — extract `InstanceRef.py`

Spec package `…::SystemTemplate::Transformer::InstanceRef` for `DataPrototypeInClientServerInterfaceInstanceRef`, `DataPrototypeInSenderReceiverInterfaceInstanceRef`, `ImplementationDataTypeElementInPortInterfaceRef`.

**Files:**
- Create: `SystemTemplate/Transformer/InstanceRef.py`
- Modify: `SystemTemplate/Transformer/__init__.py` (loses 3 classes, gains explicit re-import), consumers, `src/armodel/models/__init__.py`

- [ ] **Step 1: Move the classes and re-export from the package**

```bash
MODELS=src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer
touch $MODELS/InstanceRef.py
python scripts/move_class_blocks.py $MODELS/__init__.py $MODELS/InstanceRef.py \
  DataPrototypeInClientServerInterfaceInstanceRef DataPrototypeInSenderReceiverInterfaceInstanceRef ImplementationDataTypeElementInPortInterfaceRef
```

Add to `$MODELS/__init__.py`:
```python
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef import (
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInSenderReceiverInterfaceInstanceRef,
    ImplementationDataTypeElementInPortInterfaceRef,
)
```
Copy needed imports into `InstanceRef.py`.

- [ ] **Step 2: Update models/__init__.py and verify**

Add: `from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef import *  # noqa: F403` (consumers importing from the package keep working via the re-export; new code should import from `InstanceRef`).

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef import DataPrototypeInClientServerInterfaceInstanceRef; print('ok')"
```

- [ ] **Step 3: Full suite, lint, black, commit**

```bash
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): extract Transformer.InstanceRef module per spec package (Rule 0007 A)"
```

---

### Task 12: Timing family — TimingConstraint consolidation point, SynchronizationTiming, TimingExtensions, TDEventSLLET

Spec packages (verified in `AUTOSAR_CP_TPS_TimingExtensions.md`): class `TimingConstraint` is a direct member of `…::Timing::TimingConstraint` (non-leaf package → `__init__.py`); `SynchronizationTimingConstraint`, `SynchronizationTypeEnum`, `EventOccurrenceKindEnum` → `…::TimingConstraint::SynchronizationTiming`; `SwcTiming`, `TimingExtension` → `…::Timing::TimingExtensions`; `TDEventSLLETPort` → `…::TimingDescriptionEvents::TDEventSLLET`. NOTE: the other class-named submodules under `TimingConstraint/` (`AgeConstraint.py`, `EventTriggeringConstraint.py`, …) are **spec-correct element packages — do NOT touch them**.

**Files:**
- Modify: `TimingConstraint/__init__.py` (gains class `TimingConstraint`), delete `TimingConstraint/TimingConstraint.py`
- Rename: `TimingConstraint/SynchronizationTimingConstraint.py` → `TimingConstraint/SynchronizationTiming.py`
- Move: `TimingConstraint/TimingExtensions.py` → `Timing/TimingExtensions.py`
- Modify: `TimingDescription/TimingDescriptionEvents/TDEventSLLET.py` (gains `TDEventSLLETPort`), delete `…/TDEventSLLETPort.py`
- Modify: `src/armodel/models/__init__.py`, consumers, test mirrors

- [ ] **Step 1: Do the four file operations**

```bash
TIMING=src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing
python scripts/move_class_blocks.py $TIMING/TimingConstraint/TimingConstraint.py $TIMING/TimingConstraint/__init__.py TimingConstraint
git rm $TIMING/TimingConstraint/TimingConstraint.py
git mv $TIMING/TimingConstraint/SynchronizationTimingConstraint.py $TIMING/TimingConstraint/SynchronizationTiming.py
git mv $TIMING/TimingConstraint/TimingExtensions.py $TIMING/TimingExtensions.py
python scripts/move_class_blocks.py $TIMING/TimingDescription/TimingDescriptionEvents/TDEventSLLETPort.py \
  $TIMING/TimingDescription/TimingDescriptionEvents/TDEventSLLET.py TDEventSLLETPort
git rm $TIMING/TimingDescription/TimingDescriptionEvents/TDEventSLLETPort.py
```

Check `grep -n "^class" $TIMING/TimingConstraint/SynchronizationTiming.py` — move any class there that is NOT `SynchronizationTimingConstraint`/`SynchronizationTypeEnum`/`EventOccurrenceKindEnum` back to `TimingConstraint/__init__.py` with the helper. `TimingConstraint/__init__.py` already imports and `__all__`-exports `TimingConstraint` from the old submodule — change that import to a direct definition (remove the `from …TimingConstraint.TimingConstraint import TimingConstraint` line; ensure the class's needed imports are present).

- [ ] **Step 2: Rewrite consumers**

```bash
grep -rl "TimingConstraint\.TimingConstraint" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/TimingConstraint\.TimingConstraint import/TimingConstraint import/g'
grep -rl "TimingConstraint\.SynchronizationTimingConstraint" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/TimingConstraint\.SynchronizationTimingConstraint/TimingConstraint.SynchronizationTiming/g'
grep -rl "Timing\.TimingConstraint\.TimingExtensions" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/Timing\.TimingConstraint\.TimingExtensions/Timing.TimingExtensions/g'
grep -rl "TDEventSLLETPort" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/TimingDescriptionEvents\.TDEventSLLETPort/TimingDescriptionEvents.TDEventSLLET/g'
```

After the last sed, `grep -rn "TDEventSLLETPort import\|TDEventSLLET import" src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py` — if the class name `TDEventSLLETPort` is imported alongside others from `TDEventSLLET`, no further change needed (the class keeps its name; only its home module changed).

- [ ] **Step 3: Update `src/armodel/models/__init__.py`**

- `from …Timing.TimingConstraint.TimingConstraint import *  # noqa: F403` → `from …Timing.TimingConstraint import *  # noqa: F403` (full path prefix `armodel.models.M2.AUTOSARTemplates.CommonStructure.`)
- `from …Timing.TimingConstraint.TimingExtensions import *  # noqa: F403` → `from …Timing.TimingExtensions import *  # noqa: F403`
- Add: `from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import *  # noqa: F403`

- [ ] **Step 4: Move test mirrors**

```bash
TESTS=tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing
git mv $TESTS/TimingConstraint/test_TimingConstraint.py $TESTS/TimingConstraint/test___init__.py
git mv $TESTS/TimingConstraint/test_SynchronizationTimingConstraint.py $TESTS/TimingConstraint/test_SynchronizationTiming.py
git mv $TESTS/TimingConstraint/test_TimingExtensions.py $TESTS/test_TimingExtensions.py
git mv $TESTS/TimingDescription/TimingDescriptionEvents/test_TDEventSLLETPort.py $TESTS/TimingDescription/TimingDescriptionEvents/test_TDEventSLLET_merge.py 2>/dev/null || true
```

If a `test_TDEventSLLET.py` already exists, merge the moved test classes into it and `git rm` the `_merge` file. Apply Step 2 seds to moved files.

- [ ] **Step 5: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint; from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import SynchronizationTimingConstraint; from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SwcTiming, TimingExtension; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): Timing family file shape - TimingConstraint pkg init, SynchronizationTiming, TimingExtensions, TDEventSLLET (Rule 0007 A)"
```

---

### Task 13: StandardizationTemplate

Spec packages: `AtpBlueprint`, `AtpBlueprintable`, `AtpBlueprintMapping` → `…::StandardizationTemplate::AbstractBlueprintStructure`; `BlueprintGenerator` → `…::StandardizationTemplate::BlueprintGenerator`; `BlueprintMappingSet` → `…::StandardizationTemplate::BlueprintMapping`. (`PortPrototypeBlueprint` row is an accepted deviation — see Scope decisions.)

**Files:**
- Modify: `StandardizationTemplate/AbstractBlueprintStructure/__init__.py` (gains 3 classes), delete `AbstractBlueprintStructure/AtpBlueprint.py`
- Modify: `GenericStructure/AbstractStructure.py` (loses `AtpBlueprintable`, `AtpBlueprintMapping`)
- Convert: `StandardizationTemplate/BlueprintGenerator/` dir → `BlueprintGenerator.py` file; `StandardizationTemplate/BlueprintMapping/` dir → `BlueprintMapping.py` file
- Modify: `src/armodel/models/__init__.py`, consumers, test mirrors

- [ ] **Step 1: Consolidate AbstractBlueprintStructure**

```bash
ST=src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate
python scripts/move_class_blocks.py $ST/AbstractBlueprintStructure/AtpBlueprint.py $ST/AbstractBlueprintStructure/__init__.py AtpBlueprint
git rm $ST/AbstractBlueprintStructure/AtpBlueprint.py
python scripts/move_class_blocks.py ../GenericStructure/AbstractStructure.py $ST/AbstractBlueprintStructure/__init__.py AtpBlueprintable AtpBlueprintMapping
```

(Run the second command from `$ST`, or use full paths from repo root.) Update `AbstractBlueprintStructure/__init__.py`'s import of `AtpBlueprint` from the submodule to a direct definition; move needed imports from the two sources.

- [ ] **Step 2: Flatten BlueprintGenerator and BlueprintMapping directories**

```bash
python scripts/move_class_blocks.py $ST/BlueprintGenerator/BlueprintGenerator.py $ST/BlueprintGenerator/__init__.py BlueprintGenerator
git rm $ST/BlueprintGenerator/BlueprintGenerator.py
git mv $ST/BlueprintGenerator/__init__.py $ST/BlueprintGenerator.py
python scripts/move_class_blocks.py $ST/BlueprintMapping/BlueprintMappingSet.py $ST/BlueprintMapping/__init__.py BlueprintMappingSet
git rm $ST/BlueprintMapping/BlueprintMappingSet.py
git mv $ST/BlueprintMapping/__init__.py $ST/BlueprintMapping.py
```

If the `__init__.py` files contain other classes or imports, carry them over into the flattened files. Check `grep -n "^class" $ST/BlueprintGenerator/__init__.py` BEFORE moving so nothing is lost.

- [ ] **Step 3: Rewrite consumers**

```bash
grep -rl "AbstractBlueprintStructure\.AtpBlueprint import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/AbstractBlueprintStructure\.AtpBlueprint import/AbstractBlueprintStructure import/g'
grep -rl "BlueprintGenerator\.BlueprintGenerator import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/BlueprintGenerator\.BlueprintGenerator import/BlueprintGenerator import/g'
grep -rl "BlueprintMapping\.BlueprintMappingSet import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/BlueprintMapping\.BlueprintMappingSet import/BlueprintMapping import/g'
grep -rn "GenericStructure\.AbstractStructure import" src tests --include="*.py" | grep -v __pycache__ | grep -E "AtpBlueprintable|AtpBlueprintMapping"
```

Split the last grep's hits: the two names come from `…CommonStructure.StandardizationTemplate.AbstractBlueprintStructure`.

- [ ] **Step 4: Update `src/armodel/models/__init__.py`**

- `from …StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import *  # noqa: F403` → `from …StandardizationTemplate.AbstractBlueprintStructure import *  # noqa: F403`
- Add:
```python
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import *  # noqa: F403
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import *  # noqa: F403
```

- [ ] **Step 5: Export check for the two synced classes (Section E)**

```bash
python -c "import armodel; assert hasattr(armodel,'BlueprintGenerator') and hasattr(armodel,'BlueprintMappingSet'); print('ok')"
```

In `tests/test_armodel/test_model_imports.py` delete `"BlueprintGenerator",` and `"BlueprintMappingSet",` from `INTENTIONALLY_UNEXPORTED_MODULES`, then run `python -m pytest tests/test_armodel/test_model_imports.py -v` → PASS.

- [ ] **Step 6: Move test mirrors, full suite, lint, black, commit**

Move `tests/.../StandardizationTemplate/AbstractBlueprintStructure/test_AtpBlueprint.py` → `test___init__.py`; `BlueprintGenerator/test_BlueprintGenerator.py` → `test_BlueprintGenerator.py` one level up (dir removed); same for `BlueprintMapping/test_BlueprintMappingSet.py`. `git rm` emptied files/dirs.

```bash
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): flatten StandardizationTemplate packages per spec (Rule 0007 A) and export Blueprint classes (E)"
```

---

### Task 14: DiagnosticExtract + BswServiceDependencyIdent

Spec packages: `DiagnosticCommonElement` class cluster → `…::DiagnosticExtract::CommonDiagnostics`; `BswServiceDependencyIdent` → `…::DiagnosticExtract::DiagnosticMapping::ServiceMapping`.

**Files:**
- Rename: `DiagnosticExtract/DiagnosticCommonElement.py` → `DiagnosticExtract/CommonDiagnostics.py`
- Create: `DiagnosticExtract/DiagnosticMapping/__init__.py` (empty), `DiagnosticExtract/DiagnosticMapping/ServiceMapping.py`
- Modify: `BswModuleTemplate/BswBehavior.py` (loses `BswServiceDependencyIdent`), `src/armodel/models/__init__.py`, consumers, test mirrors

- [ ] **Step 1: Rename module, create ServiceMapping, move the class**

```bash
DE=src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract
git mv $DE/DiagnosticCommonElement.py $DE/CommonDiagnostics.py
mkdir -p $DE/DiagnosticMapping
touch $DE/DiagnosticMapping/__init__.py $DE/DiagnosticMapping/ServiceMapping.py
python scripts/move_class_blocks.py ../BswModuleTemplate/BswBehavior.py $DE/DiagnosticMapping/ServiceMapping.py BswServiceDependencyIdent
```

(Third command run from `$DE`, or use full paths.) Copy the imports `BswServiceDependencyIdent` needs into `ServiceMapping.py`.

- [ ] **Step 2: Rewrite consumers and models/__init__.py**

```bash
grep -rl "DiagnosticExtract\.DiagnosticCommonElement" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/DiagnosticExtract\.DiagnosticCommonElement/DiagnosticExtract.CommonDiagnostics/g'
grep -rn "BswBehavior import" src tests --include="*.py" | grep -v __pycache__ | grep BswServiceDependencyIdent
```

Split the last hits: `BswServiceDependencyIdent` imports from `…DiagnosticExtract.DiagnosticMapping.ServiceMapping`.
In `models/__init__.py` add: `from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping import *  # noqa: F403`.

- [ ] **Step 3: Move test mirrors, verify, full suite, lint, black, commit**

```bash
git mv tests/test_armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/test_DiagnosticCommonElement.py \
       tests/test_armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/test_CommonDiagnostics.py
mkdir -p tests/test_armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticMapping
touch tests/test_armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticMapping/__init__.py
```

Move the `BswServiceDependencyIdent` tests (likely in `tests/.../BswModuleTemplate/test_BswBehavior.py`) into `…DiagnosticExtract/DiagnosticMapping/test_ServiceMapping.py`.

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement; from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping import BswServiceDependencyIdent; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): DiagnosticExtract renames and DiagnosticMapping.ServiceMapping per spec (Rule 0007 A)"
```

---

### Task 15: GenericStructure — ARPackage, ElementCollection, RolesAndRights

Spec packages: `ARElement`, `PackageableElement` → `…::GeneralTemplateClasses::ARPackage`; `CollectableElement` → `…::GeneralTemplateClasses::ElementCollection`; `AtpDefinition` → `…::GenericStructure::RolesAndRights` (leaf after consolidation → single file `RolesAndRights.py`).

**Files:**
- Modify: `GeneralTemplateClasses/ARPackage.py` (gains `ARElement`, `PackageableElement`), `GeneralTemplateClasses/Identifiable.py` (loses 3 classes)
- Create: `GeneralTemplateClasses/ElementCollection.py`
- Convert: `GenericStructure/RolesAndRights/` dir → `RolesAndRights.py` file
- Modify: `src/armodel/models/__init__.py`, consumers, test mirrors

- [ ] **Step 1: Move the three Identifiable classes**

```bash
GS=src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses
touch $GS/ElementCollection.py
python scripts/move_class_blocks.py $GS/Identifiable.py $GS/ARPackage.py ARElement PackageableElement
python scripts/move_class_blocks.py $GS/Identifiable.py $GS/ElementCollection.py CollectableElement
```

In `ARPackage.py`, change the import of `CollectableElement` (currently from `…Identifiable`) to `from …GeneralTemplateClasses.ElementCollection import CollectableElement`, and add the imports `ARElement`/`PackageableElement` need (they use `Identifiable`). Give `ElementCollection.py` the imports `CollectableElement` needs (it derives from `ARObject`). There must be NO cycle: `Identifiable.py` must not import from `ARPackage.py`/`ElementCollection.py`.

- [ ] **Step 2: Flatten RolesAndRights**

```bash
GR=src/armodel/models/M2/AUTOSARTemplates/GenericStructure
python scripts/move_class_blocks.py $GR/RolesAndRights/AtpDefinition.py $GR/RolesAndRights/__init__.py AtpDefinition
git rm $GR/RolesAndRights/AtpDefinition.py
git mv $GR/RolesAndRights/__init__.py $GR/RolesAndRights.py
```

Check `grep -n "^class" $GR/RolesAndRights/__init__.py` before the move so nothing else in it is lost.

- [ ] **Step 3: Rewrite consumers**

```bash
grep -rn "Identifiable import" src tests --include="*.py" | grep -v __pycache__ | grep -E "ARElement|PackageableElement|CollectableElement"
grep -rl "RolesAndRights\.AtpDefinition" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/RolesAndRights\.AtpDefinition import/RolesAndRights import/g'
```

Split every hit of the first grep: `ARElement`/`PackageableElement` from `…GeneralTemplateClasses.ARPackage`, `CollectableElement` from `…GeneralTemplateClasses.ElementCollection`; remaining names stay on `…Identifiable`. This is the highest-fanout rewrite of the plan (the parser/writer import `ARElement` widely) — budget time for it.

- [ ] **Step 4: Update `src/armodel/models/__init__.py`, test mirrors**

- `from …GenericStructure.RolesAndRights.AtpDefinition import *  # noqa: F403` → `from …GenericStructure.RolesAndRights import *  # noqa: F403`
- Add: `from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import *  # noqa: F403`
- The `…GeneralTemplateClasses.ARPackage import *` line already exists (now exports `ARElement`/`PackageableElement` too).

Move test classes: `CollectableElement` tests → new `tests/.../GeneralTemplateClasses/test_ElementCollection.py`; `ARElement`/`PackageableElement` tests → `test_ARPackage.py`; `AtpDefinition` tests → `tests/.../GenericStructure/test_RolesAndRights.py` (create; remove the emptied `RolesAndRights/` test dir).

- [ ] **Step 5: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, PackageableElement; from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement; from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import AtpDefinition; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): ARPackage/ElementCollection/RolesAndRights file shape per spec (Rule 0007 A)"
```

---

### Task 16: Abstract/Adaptive platforms, EcuResourceTemplate, DataDictionary

Spec packages: `ApplicationDeferredDataType`, `ApplicationInterface` → `…::AbstractPlatform`; `Field` → `…::AdaptivePlatform::ApplicationDesign::PortInterface`; `CryptoKeySlot` → `…::PlatformModuleDeployment::CryptoDeployment`; `FirewallRule`, `FirewallRuleProps`, `StateDependentFirewall` → `…::PlatformModuleDeployment::Firewall`; `IdsPlatformInstantiation`, `IdsmModuleInstantiation` → `…::PlatformModuleDeployment::IntrusionDetectionSystem`; `PlatformModuleEthernetEndpointConfiguration` → `…::PlatformModuleDeployment::AdaptiveModuleImplementation`; `HwAttributeLiteralDef`, `HwAttributeValue` → `…::EcuResourceTemplate::HwElementCategory`; `SwCalprmRefProxy`, `SwVariableRefProxy` → `…::MSR::DataDictionary::DatadictionaryProxies`.

**Files:**
- Modify: `AbstractPlatform/__init__.py`, delete `AbstractPlatform/{ApplicationDeferredDataType,ApplicationInterface}.py`
- Modify: `AdaptivePlatform/ApplicationDesign/PortInterface/__init__.py`, delete `…/Field.py`
- Modify: `AdaptivePlatform/PlatformModuleDeployment/{CryptoDeployment,Firewall,IntrusionDetectionSystem}/__init__.py`, delete the class-named submodules
- Create: `AdaptivePlatform/PlatformModuleDeployment/AdaptiveModuleImplementation.py`; delete `AdaptiveModule/PlatformModuleEthernetEndpointConfiguration.py`
- Modify: `EcuResourceTemplate/HwElementCategory.py`, delete `EcuResourceTemplate/HwAttributeValue.py`
- Create: `MSR/DataDictionary/DatadictionaryProxies.py`; modify `MSR/DataDictionary/DataDefProperties.py`
- Modify: `src/armodel/models/__init__.py`, consumers, test mirrors

- [ ] **Step 1: Consolidate the platform packages**

```bash
AP=src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform
python scripts/move_class_blocks.py $AP/ApplicationDeferredDataType.py $AP/__init__.py ApplicationDeferredDataType
python scripts/move_class_blocks.py $AP/ApplicationInterface.py $AP/__init__.py ApplicationInterface
git rm $AP/ApplicationDeferredDataType.py $AP/ApplicationInterface.py

AD=src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform
python scripts/move_class_blocks.py $AD/ApplicationDesign/PortInterface/Field.py $AD/ApplicationDesign/PortInterface/__init__.py Field
git rm $AD/ApplicationDesign/PortInterface/Field.py
PD=$AD/PlatformModuleDeployment
python scripts/move_class_blocks.py $PD/CryptoDeployment/CryptoKeySlot.py $PD/CryptoDeployment/__init__.py CryptoKeySlot
git rm $PD/CryptoDeployment/CryptoKeySlot.py
for c in FirewallRule FirewallRuleProps StateDependentFirewall; do
  python scripts/move_class_blocks.py $PD/Firewall/$c.py $PD/Firewall/__init__.py $c
  git rm $PD/Firewall/$c.py
done
for c in IdsPlatformInstantiation IdsmModuleInstantiation; do
  python scripts/move_class_blocks.py $PD/IntrusionDetectionSystem/$c.py $PD/IntrusionDetectionSystem/__init__.py $c
  git rm $PD/IntrusionDetectionSystem/$c.py
done
touch $PD/AdaptiveModuleImplementation.py
python scripts/move_class_blocks.py $PD/AdaptiveModule/PlatformModuleEthernetEndpointConfiguration.py $PD/AdaptiveModuleImplementation.py PlatformModuleEthernetEndpointConfiguration
git rm $PD/AdaptiveModule/PlatformModuleEthernetEndpointConfiguration.py
```

Before each `git rm`, run `grep -n "^class" <file>` — if a file defines additional classes, they move with the same command (add them to the class list). If `AdaptiveModule/` becomes empty of `.py` files besides `__init__.py`, leave the (now empty) package in place — out of Section A scope.

- [ ] **Step 2: EcuResourceTemplate and DataDictionary**

```bash
ER=src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate
python scripts/move_class_blocks.py $ER/HwAttributeValue.py $ER/HwElementCategory.py HwAttributeLiteralDef HwAttributeValue
git rm $ER/HwAttributeValue.py
DD=src/armodel/models/M2/MSR/DataDictionary
touch $DD/DatadictionaryProxies.py
python scripts/move_class_blocks.py $DD/DataDefProperties.py $DD/DatadictionaryProxies.py SwCalprmRefProxy SwVariableRefProxy
```

- [ ] **Step 3: Rewrite consumers**

```bash
grep -rl "AbstractPlatform\.Application\(DeferredDataType\|Interface\) import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' -E 's/AbstractPlatform\.Application(DeferredDataType|Interface) import/AbstractPlatform import/g'
grep -rl "PortInterface\.Field import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/PortInterface\.Field import/PortInterface import/g'
grep -rl "CryptoDeployment\.CryptoKeySlot import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/CryptoDeployment\.CryptoKeySlot import/CryptoDeployment import/g'
for c in FirewallRule FirewallRuleProps StateDependentFirewall; do grep -rl "Firewall\.$c import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' "s/Firewall\.$c import/Firewall import/g"; done
for c in IdsPlatformInstantiation IdsmModuleInstantiation; do grep -rl "IntrusionDetectionSystem\.$c import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' "s/IntrusionDetectionSystem\.$c import/IntrusionDetectionSystem import/g"; done
grep -rl "AdaptiveModule\.PlatformModuleEthernetEndpointConfiguration import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/AdaptiveModule\.PlatformModuleEthernetEndpointConfiguration import/AdaptiveModuleImplementation import/g'
grep -rl "EcuResourceTemplate\.HwAttributeValue import" src tests --include="*.py" | grep -v __pycache__ | xargs sed -i '' 's/EcuResourceTemplate\.HwAttributeValue import/EcuResourceTemplate.HwElementCategory import/g'
grep -rn "DataDefProperties import" src tests --include="*.py" | grep -v __pycache__ | grep -E "SwCalprmRefProxy|SwVariableRefProxy"
```

Split the last hits: the two proxy names come from `…MSR.DataDictionary.DatadictionaryProxies`.

- [ ] **Step 4: Update `src/armodel/models/__init__.py`**

- Delete `from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import *  # noqa: F403` (the `HwElementCategory` line already exists)
- Add: `from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import *  # noqa: F403`
- The Adaptive/Abstract platform classes are intentionally unexported — no new export lines for them.

- [ ] **Step 5: Move test mirrors**

Mirror each deleted module's tests onto the surviving module's test file (e.g. `tests/.../EcuResourceTemplate/test_HwAttributeValue.py` classes merge into `test_HwElementCategory.py`; `test_DataDefProperties.py` proxy tests → new `test_DatadictionaryProxies.py`; platform test files merge into the package `test___init__.py` of their package). `git rm` emptied files.

- [ ] **Step 6: Verify, full suite, lint, black, commit**

```bash
python -c "from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationInterface; from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue; from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy; print('ok')"
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "refactor(models): platform/EcuResource/DataDictionary package shapes per spec (Rule 0007 A)"
```

---

### Task 17: Section E finale — export the remaining 20 synced classes

After Tasks 12–13 the timing and blueprint classes live at their final locations; the remaining 20 of the 26 (`AgeConstraint`, `ArbitraryEventTriggering`, `BurstPatternEventTriggering`, `ConcretePatternEventTriggering`, `ConfidenceInterval`, `EventOccurrenceKindEnum`, `EventTriggeringConstraint`, `LatencyConstraintTypeEnum`, `LatencyTimingConstraint`, `ModeInBswInstanceRef`, `ModeInSwcBswInstanceRef`, `ModeInSwcInstanceRef`, `OffsetTimingConstraint`, `PeriodicEventTriggering`, `SporadicEventTriggering`, `SynchronizationTimingConstraint`, `SynchronizationTypeEnum`, `TimingConditionFormula`, `TimingModeInstance` — plus `BlueprintGenerator`/`BlueprintMappingSet` already handled in Task 13) still need top-level exports.

**Files:**
- Modify: `src/armodel/models/__init__.py`, `tests/test_armodel/test_model_imports.py`

- [ ] **Step 1: Remove the 20 names from `INTENTIONALLY_UNEXPORTED_MODULES` (red)**

Delete these lines from `tests/test_armodel/test_model_imports.py`:
```python
    "AgeConstraint",
    "ArbitraryEventTriggering",
    "BurstPatternEventTriggering",
    "ConcretePatternEventTriggering",
    "ConfidenceInterval",
    "EventOccurrenceKindEnum",
    "EventTriggeringConstraint",
    "LatencyConstraintTypeEnum",
    "LatencyTimingConstraint",
    "ModeInBswInstanceRef",
    "ModeInSwcBswInstanceRef",
    "ModeInSwcInstanceRef",
    "OffsetTimingConstraint",
    "PeriodicEventTriggering",
    "SporadicEventTriggering",
    "SynchronizationTimingConstraint",
    "SynchronizationTypeEnum",
    "TimingConditionFormula",
    "TimingModeInstance",
```

- [ ] **Step 2: Run the import test to verify it fails**

Run: `python -m pytest tests/test_armodel/test_model_imports.py -v`
Expected: FAIL listing the 19 missing names (ModeIn* / TimingCondition* / constraint classes).

- [ ] **Step 3: Add the export lines to `src/armodel/models/__init__.py` (green)**

```python
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import AgeConstraint  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    ConfidenceInterval,
    EventTriggeringConstraint,
    PeriodicEventTriggering,
    SporadicEventTriggering,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyConstraintTypeEnum,
    LatencyTimingConstraint,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import OffsetTimingConstraint  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
    EventOccurrenceKindEnum,
    SynchronizationTimingConstraint,
    SynchronizationTypeEnum,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    ModeInBswInstanceRef,
    ModeInSwcBswInstanceRef,
    ModeInSwcInstanceRef,
    TimingConditionFormula,
    TimingModeInstance,
)  # noqa: F401
```

(Adjust any path that earlier tasks changed — e.g. if `TimingCondition.py` gained/lost classes. This mirrors the explicit-export style of commit `86764353`.)

- [ ] **Step 4: Run the import test to verify it passes**

Run: `python -m pytest tests/test_armodel/test_model_imports.py -v`
Expected: PASS.

- [ ] **Step 5: Full suite, lint, black, commit**

```bash
python scripts/run_tests.py && npm run lint && npm run black
git add -A
git commit -m "feat(models): export 20 synced timing classes from armodel top level (Rule 0007 E)"
```

---

### Task 18: Update the deviation report and close out

**Files:**
- Modify: `docs/examples/method_deviation_by_class_v2.md`

- [ ] **Step 1: Update the Rule 0007 appendix**

In `docs/examples/method_deviation_by_class_v2.md`, replace the entire `## Appendix: Rule 0007 — package location & file shape deviations` section (from that heading to the end of the file) with:

```markdown
## Appendix: Rule 0007 — package location & file shape deviations

Remediated 2026-08-30 (see `docs/plan/2026-08-30-rule-0007-package-location-remediation.md`).

### Status

- **A. Module does not match the spec `Package` row** — RESOLVED for 102 of 104
  classes. Remaining accepted deviation: `PortPrototypeBlueprint` /
  `PortPrototypeBlueprintInitValue` live in `…::BlueprintDedicated::PortPrototypeBlueprint`
  (corrected spelling); the spec package is spelled `PortProtoypeBlueprint` (spec typo).
- **B. Case-only package/module mismatch** — RESOLVED (`SystemTemplate/DoIP.py`).
- **C. Leaf packages hosting classes in `__init__.py`** — OPEN (candidates only;
  judgement calls deferred to a follow-up plan).
- **D. `X/` beside `X.py`** — RESOLVED earlier (commit 86764353); verified gone.
- **E. Top-level export chain** — RESOLVED: the 26 synced classes are importable as
  `armodel.<ClassName>` and dropped from `INTENTIONALLY_UNEXPORTED_MODULES`;
  3 stale `BswEntryRelationship*` entries removed from `KNOWN_NAME_COLLISION_CLASSES`.
  Remaining real export gap: `ModeInBswModuleDescriptionInstanceRef` (depends on C).
```

- [ ] **Step 2: Final full verification**

```bash
python scripts/run_tests.py && npm run lint && npm run black-check
python -m pytest tests/test_armodel/test_model_imports.py -v
```

Expected: all green, matching or exceeding the Task 1 baseline counts.

- [ ] **Step 3: Commit**

```bash
git add docs/examples/method_deviation_by_class_v2.md
git commit -m "docs: mark Rule 0007 appendix sections A/B/D/E resolved"
```

---

## Self-review notes

- Spec coverage: every Section A row maps to Tasks 5–16 (60 package pairs); Section B → Task 3; Section E → Tasks 4, 13 (Step 5), 17; Section D → Task 1 verification. `PortProtoypeBlueprint` row and Section C documented as accepted/deferred.
- Type consistency: the mover script signature (`SOURCE TARGET ClassName…`) and the class lists are used identically in every task; export names match the `INTENTIONALLY_UNEXPORTED_MODULES` entries exactly.
- Known risks called out inline: fanout import rewrites in Tasks 8/9/15, potential cycles in Tasks 6/7/8 (function-level import escape hatch), and "check remaining classes before `git rm`" guards on every file deletion.
