# Full API Docstring Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Google-style docstrings to every public class and method across the py-armodel codebase, achieving 100% docstring coverage.

**Architecture:** Batch-per-module processing via Claude Code. Each module batch: read files, add Google-style docstrings to undocumented classes/methods, run tests, human review. Follow reference pattern from `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`.

**Tech Stack:** Python 3.8+, Sphinx + Napoleon (already configured), Google-style docstrings

**Reference Materials:** AUTOSAR spec markdown files in `autosar/markdown/` contain authoritative class descriptions and attributes:
- `autosar/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md` — SwcInternalBehavior, Ports, Events, etc.
- `autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` — System signals, Fibex, ECU mapping, etc.
- `autosar/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md` — BswModuleDescription, BswBehavior, etc.
- `autosar/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md` — DiagnosticExtract classes.

When writing docstrings, consult the relevant spec file for:
- Official class purpose/description (Section 1.4.* in spec)
- Attribute names and descriptions (class tables with Attribute/Kind/Note columns)
- Inheritance relationships

**Task note:** When implementing each task, consult the spec file listed in the File Structure section for that module. Use the class table to get accurate attribute descriptions. Cross-reference the Python class attributes with the spec attributes to ensure completeness.

---

## File Structure

### Phase 0: Report Generation
- **Create:** `scripts/generate_docstring_report.py` — scans all Python files, extracts class names and docstrings
- **Output:** `reports/docstring_review.md` — markdown report grouped by module

### Phase 1: Models (262 classes, ~100 files)
**CommonStructure** (27 files, ~220 classes):
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Filter.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py` (3 undocumented)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py` (reference)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclarationExtra.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py` (93 classes, all documented)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/TriggerDeclaration.py`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/` (15 files)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/` (4 files)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/` (11 files)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/` (5 files)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/` (4 files)

**SystemTemplate** (24 files, ~211 classes):
- **Spec reference:** `autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` — Section 1.4 (System), class tables with attributes
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DiagnosticConnection.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/ECUResourceMapping.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/` (16 files)
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/RteEventToOsTaskMapping.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SWmapping.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py`
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

**SWComponentTemplate** (23 files, 100 classes, 94 undocumented):
- **Spec reference:** `autosar/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md` — Section 1.4 (Software Components), class tables with attributes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py` (27 classes, 21 undocumented)
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType.py`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/` (11 files)
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/` (2 files)
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SoftwareComponentDocumentation.py`

**BswModuleTemplate** (16 files, 51 classes, already documented):
- **Spec reference:** `autosar/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md` — BswModuleDescription, BswBehavior, BswImplementation classes
- `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`
- `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`
- `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswImplementation.py`
- `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/` (10 files)
- `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces/` (3 files)
- `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/` (3 files)

**GenericStructure** (11 files, 60 classes):
- `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`
- `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/` (7 files, PrimitiveTypes.py has 17 undocumented)
- `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py` (1 undocumented)
- `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/RolesAndRights/`

**MSR/** (14 files, ~57 classes):
- `src/armodel/models/M2/MSR/AsamHdo/` (6 files, all documented)
- `src/armodel/models/M2/MSR/DataDictionary/` (6 files, 17 undocumented)
- `src/armodel/models/M2/MSR/Documentation/` (6 files, 22 undocumented)
- `src/armodel/models/M2/MSR/CalibrationData/` (1 file, 2 undocumented)

**Remaining modules:**
- **Spec reference:** `autosar/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md` — DiagnosticExtract classes
- `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure.py`
- `src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/` (2 files)
- `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/` (3 files)
- `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py` (13 undocumented)
- `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py` (13 undocumented)
- **Spec reference:** `autosar/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md` — ECUC classes
- `src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform/` (2 files)
- `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/` (9 files)

### Phase 2: Parser & Writer (8 files)
- `src/armodel/parser/arxml_parser.py` (0 documented)
- `src/armodel/parser/abstract_arxml_parser.py`
- `src/armodel/parser/connector_xlsx_parser.py`
- `src/armodel/parser/excel_parser.py`
- `src/armodel/parser/file_parser.py`
- `src/armodel/writer/arxml_writer.py` (0 documented)
- `src/armodel/writer/abstract_arxml_writer.py`

### Phase 3: CLI & Lib (14 files)
- `src/armodel/cli/arxml_dump_cli.py`
- `src/armodel/cli/arxml_format_cli.py`
- `src/armodel/cli/connector2xlsx_cli.py`
- `src/armodel/cli/connector_update_cli.py`
- `src/armodel/cli/file_list_cli.py`
- `src/armodel/cli/format_xml_cli.py`
- `src/armodel/cli/memory_section_cli.py`
- `src/armodel/cli/swc_list_cli.py`
- `src/armodel/cli/system_signal_cli.py`
- `src/armodel/cli/uuid_checker_cli.py`
- `src/armodel/lib/cli_args_parser.py`
- `src/armodel/lib/sw_component.py`
- `src/armodel/lib/system_signal.py`

---

## Tasks

### Task 1: Generate Docstring Review Report

**Files:**
- Create: `scripts/generate_docstring_report.py`
- Output: `reports/docstring_review.md`

- [ ] **Step 1: Create the report generation script**

```python
"""Generate a docstring coverage report for the py-armodel codebase."""

import ast
import os
from pathlib import Path


def get_class_info(filepath):
    """Extract class names and their docstrings from a Python file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=filepath)
    except (SyntaxError, UnicodeDecodeError):
        return []

    results = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            docstring = ast.get_docstring(node)
            results.append({
                "name": node.name,
                "docstring": docstring,
                "line": node.lineno,
            })
    return results


def scan_directory(base_dir):
    """Scan all Python files and return results grouped by module."""
    modules = {}

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", "build", ".git")]

        for fname in sorted(files):
            if not fname.endswith(".py"):
                continue
            if fname == "__init__.py":
                continue

            filepath = os.path.join(root, fname)
            rel_path = os.path.relpath(filepath, base_dir)
            module = os.path.dirname(rel_path)

            classes = get_class_info(filepath)
            if classes:
                if module not in modules:
                    modules[module] = []
                modules[module].append({
                    "file": rel_path,
                    "classes": classes,
                })

    return modules


def format_docstring_summary(docstring):
    """Get first line of docstring, truncated."""
    if not docstring:
        return None
    first_line = docstring.strip().split("\n")[0]
    if len(first_line) > 120:
        return first_line[:117] + "..."
    return first_line


def generate_report(modules):
    """Generate markdown report."""
    lines = []
    lines.append("# Docstring Coverage Report")
    lines.append("")
    lines.append("Generated for manual review. Flag any inaccurate docstrings for correction.")
    lines.append("")

    total_documented = 0
    total_undocumented = 0

    for module in sorted(modules.keys()):
        files = modules[module]
        module_doc = 0
        module_undoc = 0

        lines.append(f"## {module}")
        lines.append("")

        for file_info in files:
            lines.append(f"### {file_info['file']}")
            lines.append("")

            for cls in file_info["classes"]:
                if cls["docstring"]:
                    total_documented += 1
                    module_doc += 1
                    summary = format_docstring_summary(cls["docstring"])
                    lines.append(f"- **{cls['name']}** (L{cls['line']}): {summary}")
                else:
                    total_undocumented += 1
                    module_undoc += 1
                    lines.append(f"- ~~{cls['name']}~~ (L{cls['line']}): *missing*")

            lines.append("")

        coverage = module_doc / (module_doc + module_undoc) * 100 if (module_doc + module_undoc) > 0 else 0
        lines.append(f"> Coverage: {module_doc}/{module_doc + module_undoc} ({coverage:.1f}%)")
        lines.append("")

    total = total_documented + total_undocumented
    overall = total_documented / total * 100 if total > 0 else 0
    lines.insert(3, f"**Overall: {total_documented}/{total} documented ({overall:.1f}%), {total_undocumented} missing**")
    lines.insert(4, "")

    return "\n".join(lines)


if __name__ == "__main__":
    base = Path(__file__).parent.parent / "src" / "armodel"
    modules = scan_directory(str(base))
    report = generate_report(modules)

    output = Path(__file__).parent.parent / "reports" / "docstring_review.md"
    output.write_text(report, encoding="utf-8")
    print(f"Report written to {output}")
    print(f"Modules: {len(modules)}")
```

- [ ] **Step 2: Run the report script**

```bash
python scripts/generate_docstring_report.py
```

Expected: Report written to `reports/docstring_review.md` with ~923 classes listed.

- [ ] **Step 3: Verify report output**

```bash
head -50 reports/docstring_review.md
```

Expected: Markdown with class names, line numbers, docstring summaries.

- [ ] **Step 4: Commit**

```bash
git add scripts/generate_docstring_report.py reports/docstring_review.md
git commit -m "feat: add docstring coverage report generation"
```

---

### Task 2: Add Docstrings to CommonStructure/ServiceNeeds.py

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

*Note: ServiceNeeds.py has 93 classes, all documented. Verify accuracy, fix if needed.*

- [ ] **Step 1: Read file and verify docstring accuracy**

Read `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`. Check 3-5 class docstrings against actual class behavior.

- [ ] **Step 2: Fix any inaccurate docstrings**

Edit file to correct any docstrings that don't match actual behavior.

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
git commit -m "fix: correct ServiceNeeds docstrings if needed"
```

---

### Task 3: Add Docstrings to CommonStructure/PrimitiveTypes.py

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py` (33 classes, 17 undocumented)

- [ ] **Step 1: Read the file**

Read `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`. Identify the 17 undocumented classes.

- [ ] **Step 2: Add Google-style docstrings to undocumented classes**

For each undocumented class, add docstring following ModeDeclaration.py pattern:
```python
class ClassName(ParentClass):
    """
    Brief description of the class.

    Extended description if non-obvious.
    """
```

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py
git commit -m "docs: add docstrings to PrimitiveTypes (17 classes)"
```

---

### Task 4: Add Docstrings to CommonStructure/MeasurementCalibrationSupport/

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/*.py` (11 files)

- [ ] **Step 1: Check which files have undocumented classes**

All 11 files have 1 class each, all documented. Verify accuracy.

- [ ] **Step 2: Fix any inaccurate docstrings**

Edit files to correct any docstrings that don't match actual behavior.

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/
git commit -m "docs: verify MeasurementCalibrationSupport docstrings"
```

---

### Task 5: Add Docstrings to CommonStructure/Timing/

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/**/*.py` (15 files)

*Note: ExecutionOrderConstraint.py has 2 undocumented classes.*

- [ ] **Step 1: Read files with undocumented classes**

Read `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`.

- [ ] **Step 2: Add docstrings to undocumented classes**

Add Google-style docstrings to the 2 undocumented classes in ExecutionOrderConstraint.py.

- [ ] **Step 3: Verify other Timing files are accurate**

Spot-check 3-4 other files in Timing/ directory.

- [ ] **Step 4: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 5: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/
git commit -m "docs: add docstrings to Timing module (2 classes)"
```

---

### Task 6: Add Docstrings to CommonStructure Remaining Files

**Files:**
- Modify: All remaining CommonStructure files (Filter.py, FlatMap.py, Implementation.py, etc.)

*Note: Most already documented. Check for accuracy, fix gaps.*

- [ ] **Step 1: Check ImplementationDataTypes.py for 3 undocumented classes**

Read `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`. Add docstrings to 3 undocumented classes.

- [ ] **Step 2: Spot-check 5-10 other files for accuracy**

Read files, verify docstrings match actual class behavior.

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/CommonStructure/
git commit -m "docs: complete CommonStructure docstring coverage"
```

---

### Task 7: Add Docstrings to SystemTemplate/Fibex/ (16 files)

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/**/*.py` (16 files)

- [ ] **Step 1: Read all Fibex files, identify undocumented classes**

Scan all 16 files. List classes missing docstrings.

- [ ] **Step 2: Add docstrings to undocumented classes**

For each undocumented class, add Google-style docstring.

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/
git commit -m "docs: add docstrings to Fibex module"
```

---

### Task 8: Add Docstrings to SystemTemplate Remaining (8 files)

**Files:**
- Modify: All non-Fibex SystemTemplate files

- [ ] **Step 1: Read all remaining SystemTemplate files**

Identify undocumented classes.

- [ ] **Step 2: Add docstrings to undocumented classes**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/
git commit -m "docs: complete SystemTemplate docstring coverage"
```

---

### Task 9: Add Docstrings to SWComponentTemplate/Communication.py

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py` (27 classes, 21 undocumented)

- [ ] **Step 1: Read Communication.py**

Read full file. Understand class hierarchy and relationships.

- [ ] **Step 2: Add docstrings to all 21 undocumented classes**

Follow ModeDeclaration.py pattern. Include class summary, Args for `__init__`, Returns for getters.

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
git commit -m "docs: add docstrings to Communication module (21 classes)"
```

---

### Task 10: Add Docstrings to SWComponentTemplate/SwcInternalBehavior/

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/*.py` (11 files)

- [ ] **Step 1: Read all SwcInternalBehavior files**

Identify undocumented classes across all 11 files.

- [ ] **Step 2: Add docstrings to undocumented classes**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/
git commit -m "docs: add docstrings to SwcInternalBehavior module"
```

---

### Task 11: Add Docstrings to SWComponentTemplate Remaining

**Files:**
- Modify: Remaining SWComponentTemplate files (SwComponentType.py, SwcImplementation.py, Datatype/, etc.)

- [ ] **Step 1: Read all remaining files**

Identify undocumented classes.

- [ ] **Step 2: Add docstrings to undocumented classes**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/
git commit -m "docs: complete SWComponentTemplate docstring coverage"
```

---

### Task 12: Add Docstrings to BswModuleTemplate (if any gaps)

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/**/*.py` (16 files)

*Note: All 51 classes documented. Verify accuracy only.*

- [ ] **Step 1: Spot-check 5-10 classes across different files**

Verify docstrings match actual behavior.

- [ ] **Step 2: Fix any inaccurate docstrings**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/
git commit -m "docs: verify BswModuleTemplate docstring accuracy"
```

---

### Task 13: Add Docstrings to GenericStructure/

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/**/*.py` (11 files)

*Note: LifeCycles.py has 1 undocumented, PrimitiveTypes.py handled in Task 3.*

- [ ] **Step 1: Read LifeCycles.py, add docstring to undocumented class**

- [ ] **Step 2: Verify other GenericStructure files**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/
git commit -m "docs: complete GenericStructure docstring coverage"
```

---

### Task 14: Add Docstrings to MSR/DataDictionary/ (17 undocumented)

**Files:**
- Modify: `src/armodel/models/M2/MSR/DataDictionary/*.py` (6 files)

- [ ] **Step 1: Read all DataDictionary files**

Identify all 17 undocumented classes.

- [ ] **Step 2: Add docstrings to undocumented classes**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/MSR/DataDictionary/
git commit -m "docs: add docstrings to DataDictionary module"
```

---

### Task 15: Add Docstrings to MSR/Documentation/ (22 undocumented)

**Files:**
- Modify: `src/armodel/models/M2/MSR/Documentation/**/*.py` (6 files)

- [ ] **Step 1: Read all Documentation files**

Identify all 22 undocumented classes.

- [ ] **Step 2: Add docstrings to undocumented classes**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/MSR/Documentation/
git commit -m "docs: add docstrings to Documentation module"
```

---

### Task 16: Add Docstrings to MSR/CalibrationData/ (2 undocumented)

**Files:**
- Modify: `src/armodel/models/M2/MSR/CalibrationData/CalibrationValue.py`

- [ ] **Step 1: Add docstrings to 2 undocumented classes**

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 3: Commit**

```bash
git add src/armodel/models/M2/MSR/CalibrationData/
git commit -m "docs: add docstrings to CalibrationData module"
```

---

### Task 17: Add Docstrings to Remaining Model Modules

**Files:**
- Modify: AutosarTopLevelStructure.py, DiagnosticExtract/, EcuResourceTemplate/, ECUCDescriptionTemplate.py, ECUCParameterDefTemplate.py, AbstractPlatform/, AdaptivePlatform/

- [ ] **Step 1: Read all remaining model files**

Identify undocumented classes.

- [ ] **Step 2: Add docstrings to undocumented classes**

ECUCDescriptionTemplate.py: 13 classes, all undocumented.
ECUCParameterDefTemplate.py: 13 classes undocumented.

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/
git commit -m "docs: complete remaining model docstring coverage"
```

---

### Task 18: Add Docstrings to Parser Module (5 files)

**Files:**
- Modify: `src/armodel/parser/*.py` (5 files)

*Note: arxml_parser.py has 0 documented classes.*

- [ ] **Step 1: Read all parser files**

Identify undocumented classes and methods.

- [ ] **Step 2: Add docstrings to ARXMLParser class and methods**

Follow ModeDeclaration.py pattern.

- [ ] **Step 3: Add docstrings to other parser files**

- [ ] **Step 4: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 5: Commit**

```bash
git add src/armodel/parser/
git commit -m "docs: add docstrings to parser module"
```

---

### Task 19: Add Docstrings to Writer Module (3 files)

**Files:**
- Modify: `src/armodel/writer/*.py` (3 files)

- [ ] **Step 1: Read all writer files**

Identify undocumented classes and methods.

- [ ] **Step 2: Add docstrings to ARXMLWriter class and methods**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/writer/
git commit -m "docs: add docstrings to writer module"
```

---

### Task 20: Add Docstrings to CLI Module (10 files)

**Files:**
- Modify: `src/armodel/cli/*.py` (10 files)

- [ ] **Step 1: Read all CLI files**

Identify undocumented classes and methods.

- [ ] **Step 2: Add docstrings to all CLI classes**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/cli/
git commit -m "docs: add docstrings to CLI module"
```

---

### Task 21: Add Docstrings to Lib Module (3 files)

**Files:**
- Modify: `src/armodel/lib/*.py` (3 files)

- [ ] **Step 1: Read all lib files**

Identify undocumented classes and methods.

- [ ] **Step 2: Add docstrings to all lib classes**

- [ ] **Step 3: Run tests**

```bash
python scripts/run_tests.py
```

- [ ] **Step 4: Commit**

```bash
git add src/armodel/lib/
git commit -m "docs: add docstrings to lib module"
```

---

### Task 22: Final Verification

**Files:**
- Modify: None (verification only)

- [ ] **Step 1: Run docstring coverage report**

```bash
python scripts/generate_docstring_report.py
```

Expected: 923/923 documented (100% coverage).

- [ ] **Step 2: Run full test suite**

```bash
python scripts/run_tests.py --coverage
```

Expected: All tests pass, no regressions.

- [ ] **Step 3: Build Sphinx docs, check for warnings**

```bash
cd docs && make clean && make html 2>&1 | grep -i warning
```

Expected: No new warnings related to docstrings.

- [ ] **Step 4: Final commit (if any fixes needed)**

```bash
git add -A
git commit -m "docs: final docstring coverage fixes"
```

---

## Reference Pattern

File: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`

```python
class ModeDeclaration(AtpStructureElement):
    """
    Represents a mode declaration in AUTOSAR models.
    Mode declarations define specific operational states that components can be in, with associated values.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ModeDeclaration with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this mode declaration
            short_name: The unique short name of this mode declaration
        """
```

---

## Rules

- Don't touch files/classes that already have adequate docstrings
- Don't change code logic — only add docstrings
- Follow ModeDeclaration.py patterns exactly
- AUTOSAR terminology preserved exactly
- Skip `__init__` docstring if it only calls `super().__init__()` with no custom logic
- Skip trivial getter/setter pairs where method name is self-explanatory
