# Full API Docstring Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Google-style docstrings to every undocumented class across py-armodel (199 classes undocumented, 75.6% current coverage).

**Architecture:** Batch-per-module processing. Each batch: read files, add docstrings to undocumented classes, run tests, commit. Follow reference pattern from `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`.

**Tech Stack:** Python 3.8+, Sphinx + Napoleon (already configured), Google-style docstrings

**Reference Materials:** AUTOSAR spec markdown files in `autosar/markdown/` for class descriptions.

**Rules:**
- Don't touch files/classes that already have adequate docstrings
- Don't change code logic — only add docstrings
- Follow ModeDeclaration.py patterns exactly
- AUTOSAR terminology preserved exactly
- Skip `__init__` docstring if it only calls `super().__init__()` with no custom logic
- Skip trivial getter/setter pairs where method name is self-explanatory

---

## File Structure

### Phase 0: Report Generation
- **Create:** `scripts/generate_docstring_report.py` — scans all Python files, extracts class names and docstrings
- **Output:** `reports/docstring_review.md` — markdown report grouped by module

### Phase 1: Models (173 undocumented classes)
**SWComponentTemplate** (95 classes undocumented):
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py` — 21 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/` (12 files) — 34 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py` — 7 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py` — 8 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py` — 7 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py` — 6 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py` — 5 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py` — 2 classes
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SoftwareComponentDocumentation.py` — 1 class
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py` — 1 class
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType.py` — 1 class
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/InstanceRefs.py` — 1 class

**SystemTemplate + Fibex** (18 classes undocumented):
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py` — 7 classes
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/Timing.py` — 7 classes
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py` — 1 class
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py` — 2 classes
- **Spec ref:** `autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md`

**MSR Modules** (39 classes undocumented):
- `src/armodel/models/M2/MSR/DataDictionary/` (6 files) — 16 classes
- `src/armodel/models/M2/MSR/Documentation/` (6 files) — 21 classes
- `src/armodel/models/M2/MSR/CalibrationData/CalibrationValue.py` — 2 classes

**ECUC Modules** (26 classes undocumented):
- `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py` — 13 classes
- `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py` — 13 classes

**Remaining Model Files** (10 classes undocumented):
- `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py` — 4 classes (FileInfoComment, AbstractAUTOSAR, AUTOSAR, AUTOSARDoc)
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py` — 3 classes
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/Traceable.py` — 1 class
- `src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticCommonElement.py` — 1 class
- **Spec ref:** `autosar/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md`
- `src/armodel/models/utils/uuid_mgr.py` — 1 class

### Phase 2: Parser, Writer, Transformer, Report (12 classes)
- `src/armodel/parser/arxml_parser.py` — 1 class
- `src/armodel/parser/abstract_arxml_parser.py` — 1 class
- `src/armodel/parser/connector_xlsx_parser.py` — 2 classes
- `src/armodel/parser/excel_parser.py` — 1 class
- `src/armodel/writer/arxml_writer.py` — 1 class
- `src/armodel/writer/abstract_arxml_writer.py` — 1 class
- `src/armodel/transformer/abstract.py` — 1 class
- `src/armodel/transformer/admin_data.py` — 1 class
- `src/armodel/report/connector_xls_report.py` — 1 class
- `src/armodel/report/excel_report.py` — 1 class

### Phase 3: Lib & Data Models (6 classes)
- `src/armodel/lib/cli_args_parser.py` — 1 class
- `src/armodel/lib/sw_component.py` — 1 class
- `src/armodel/lib/system_signal.py` — 1 class
- `src/armodel/data_models/sw_connector.py` — 3 classes

### CLI Module
- **No classes exist** in CLI files (function-based scripts). Skip class docstrings.
- If desired: add module-level docstrings only.

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

Expected: Report written to `reports/docstring_review.md`.

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

### Task 2: Add Docstrings to SWComponentTemplate Module (~95 classes)

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py` — 21 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/` (12 files) — 34 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py` — 7 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py` — 8 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py` — 7 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py` — 6 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py` — 5 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py` — 2 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SoftwareComponentDocumentation.py` — 1 class
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py` — 1 class
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType.py` — 1 class
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/InstanceRefs.py` — 1 class
- **Spec ref:** `autosar/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md`

Undocumented classes per file (list to check against):

Communication.py: HandleInvalidEnum, CompositeNetworkRepresentation, TransmissionAcknowledgementRequest, SenderComSpec, QueuedSenderComSpec, NonqueuedSenderComSpec, ClientComSpec, ModeSwitchReceiverComSpec, NvRequireComSpec, ParameterRequireComSpec, ReceiverComSpec, ModeSwitchedAckRequest, ModeSwitchSenderComSpec, ParameterProvideComSpec, TransformationComSpecProps, EndToEndTransformationComSpecProps, UserDefinedTransformationComSpecProps, ServerComSpec, NvProvideComSpec, NonqueuedReceiverComSpec, QueuedReceiverComSpec

EndToEndProtection.py: EndToEndDescription, EndToEndProtectionVariablePrototype, EndToEndProtectionISignalIPdu, EndToEndProtection, EndToEndProtectionSet

RPTScenario.py: IdentCaption, ModeAccessPointIdent

SoftwareComponentDocumentation.py: SwComponentDocumentation

SwcImplementation.py: SwcImplementation

SwComponentType.py: SwComponentType

Components/InstanceRefs.py: ModeGroupInAtomicSwcInstanceRef, PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef, RModeInAtomicSwcInstanceRef, VariableInAtomicSwcInstanceRef, RVariableInAtomicSwcInstanceRef, InnerPortGroupInCompositionInstanceRef

Composition/InstanceRefs.py: PortInCompositionTypeInstanceRef, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef, OperationInAtomicSwcInstanceRef, POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef

Datatype/DataPrototypes.py: DataPrototype, AutosarDataPrototype, VariableDataPrototype, ApplicationCompositeElementDataPrototype, ApplicationArrayElement, ApplicationRecordElement, ParameterDataPrototype

Datatype/Datatypes.py: AutosarDataType, ApplicationDataType, ApplicationPrimitiveDataType, ApplicationCompositeDataType, ApplicationArrayDataType, ApplicationRecordDataType, DataTypeMap, DataTypeMappingSet

PortInterface/InstanceRefs.py: ApplicationCompositeElementInPortInterfaceInstanceRef

SwcInternalBehavior/AccessCount.py: AbstractAccessPoint

SwcInternalBehavior/AutosarVariableRef.py: AutosarVariableRef

SwcInternalBehavior/DataElements.py: ParameterAccess, VariableAccess

SwcInternalBehavior/IncludedDataTypes.py: IncludedDataTypeSet

SwcInternalBehavior/InstanceRefsUsage.py: ArVariableInImplementationDataInstanceRef, VariableInAtomicSWCTypeInstanceRef, ParameterInAtomicSWCTypeInstanceRef, AutosarParameterRef

SwcInternalBehavior/ModeDeclarationGroup.py: ModeAccessPoint, ModeSwitchPoint, IncludedModeDeclarationGroupSet

SwcInternalBehavior/PerInstanceMemory.py: PerInstanceMemory

SwcInternalBehavior/PortAPIOptions.py: PortDefinedArgumentValue, PortAPIOption

SwcInternalBehavior/RTEEvents.py: RTEEvent, AsynchronousServerCallReturnsEvent, DataSendCompletedEvent, DataWriteCompletedEvent, DataReceivedEvent, SwcModeSwitchEvent, DataReceiveErrorEvent, OperationInvokedEvent, InitEvent, TimingEvent, InternalTriggerOccurredEvent, BackgroundEvent, ModeSwitchedAckEvent

SwcInternalBehavior/ServerCall.py: ServerCallPoint

SwcInternalBehavior/ServiceMapping.py: RoleBasedPortAssignment, SwcServiceDependency

SwcInternalBehavior/Trigger.py: InternalTriggeringPoint, ExternalTriggeringPointIdent, ExternalTriggeringPoint

- [ ] **Step 1: Read files, add docstrings to undocumented classes**

For each file, read it. For each undocumented class, add Google-style docstring:

```python
class ClassName(ParentClass):
    """
    Brief description of the class.

    Extended description if non-obvious.
    """
```

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/
git commit -m "docs: add docstrings to SWComponentTemplate module (~95 classes)"
```

---

### Task 3: Add Docstrings to SystemTemplate + Fibex Module (~18 classes)

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py` — 7 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/Timing.py` — 7 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py` — 1 class
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py` — 2 classes
- **Spec ref:** `autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md`

Undocumented classes:
- Fibex4Multiplatform.py: FrameMapping, ISignalMapping, DefaultValueElement, PduMappingDefaultValue, TargetIPduRef, IPduMapping, Gateway
- FibexCore/Timing.py: ModeDrivenTransmissionModeCondition, TransmissionModeCondition, TimeRangeType, CyclicTiming, EventControlledTiming, TransmissionModeTiming, TransmissionModeDeclaration
- FibexCore/EcuInstance.py: EcuInstance
- InstanceRefs.py: VariableDataPrototypeInSystemInstanceRef, ComponentInSystemInstanceRef

- [ ] **Step 1: Read all 4 files, add docstrings to undocumented classes**

Follow ModeDeclaration.py pattern. Reference AUTOSAR spec for class descriptions.

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/
git commit -m "docs: add docstrings to SystemTemplate + Fibex module (~18 classes)"
```

---

### Task 4: Add Docstrings to MSR Modules (~39 classes)

**Files:**
- Modify: `src/armodel/models/M2/MSR/DataDictionary/` (6 files) — 16 classes
- Modify: `src/armodel/models/M2/MSR/Documentation/` (6 files) — 21 classes
- Modify: `src/armodel/models/M2/MSR/CalibrationData/CalibrationValue.py` — 2 classes

Undocumented classes:

DataDictionary/AuxillaryObjects.py: SwAddrMethod

DataDictionary/Axis.py: SwGenericAxisParam, SwAxisGeneric, SwAxisIndividual, SwAxisGrouped

DataDictionary/CalibrationParameter.py: SwCalprmAxisTypeProps, SwCalprmAxis, SwCalprmAxisSet

DataDictionary/DataDefProperties.py: SwDataDefProps, SwPointerTargetProps, ValueList

DataDictionary/RecordLayout.py: SwRecordLayoutV, SwRecordLayoutGroupContent, SwRecordLayoutGroup, SwRecordLayout

DataDictionary/ServiceProcessTask.py: SwServiceArg

Documentation/Annotation.py: GeneralAnnotation, Annotation

Documentation/BlockElements/Figure.py: GraphicFitEnum, Graphic, Map, LGraphic, MlFigure

Documentation/TextModel/LanguageDataModel.py: LEnum, LanguageSpecific, LOverviewParagraph, LParagraph, LLongName, LPlainText

Documentation/TextModel/MultilanguageData.py: MultiLanguageParagraph, MultiLanguageOverviewParagraph, MultilanguageLongName, MultiLanguagePlainText

Documentation/TextModel/BlockElements/ListElements.py: ListEnum, Item

Documentation/TextModel/BlockElements/PaginationAndView.py: DocumentViewSelectable, Paginateable

CalibrationData/CalibrationValue.py: SwValues, SwValueCont

- [ ] **Step 1: Read all files, add docstrings to undocumented classes**

Follow ModeDeclaration.py pattern.

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add src/armodel/models/M2/MSR/
git commit -m "docs: add docstrings to MSR modules (~39 classes)"
```

---

### Task 5: Add Docstrings to ECUC Modules (26 classes)

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py` — 13 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py` — 13 classes

Undocumented classes:

ECUCDescriptionTemplate.py: EcucValueCollection, EcucIndexableValue, EcucParameterValue, EcucAddInfoParamValue, EcucTextualParamValue, EcucNumericalParamValue, EcucAbstractReferenceValue, EcucInstanceReferenceValue, EcucReferenceValue, EcucContainerValue, EcucModuleConfigurationValues, EcucConditionSpecification, EcucConfigurationVariantEnum

ECUCParameterDefTemplate.py: EcucScopeEnum, EcucConfigurationClassEnum, EcucConfigurationVariantEnum, EcucAbstractExternalReferenceDef, EcucSymbolicNameReferenceDef, EcucChoiceReferenceDef, EcucReferenceDef, EcucUriReferenceDef, EcucForeignReferenceDef, EcucInstanceReferenceDef, EcucIntegerParamDef, EcucFloatParamDef, EcucModuleDef

- [ ] **Step 1: Read both files, add docstrings to undocumented classes**

ECUCDescriptionTemplate.py is 100% undocumented (13/13). ECUCParameterDefTemplate.py has 32/45 documented, 13 missing.

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
git commit -m "docs: add docstrings to ECUC modules (26 classes)"
```

---

### Task 6: Add Docstrings to Remaining Model Files (10 classes)

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py` — 4 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py` — 3 classes
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/Traceable.py` — 1 class
- Modify: `src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticCommonElement.py` — 1 class
  - **Spec ref:** `autosar/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md`
- Modify: `src/armodel/models/utils/uuid_mgr.py` — 1 class

Undocumented classes:

AutosarTopLevelStructure/__init__.py: FileInfoComment, AbstractAUTOSAR, AUTOSAR, AUTOSARDoc

ImplementationDataTypes.py: AbstractImplementationDataTypeElement, ImplementationDataTypeElement, AbstractImplementationDataType

Traceable.py: Traceable

DiagnosticCommonElement.py: DiagnosticCommonElement

uuid_mgr.py: UUIDMgr

- [ ] **Step 1: Read all files, add docstrings to undocumented classes**

Note: AUTOSAR class in AutosarTopLevelStructure/__init__.py is the framework entry point. Docstring should describe its singleton pattern, version management, and finder methods.

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/Traceable.py src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticCommonElement.py src/armodel/models/utils/uuid_mgr.py
git commit -m "docs: add docstrings to remaining model files (10 classes)"
```

---

### Task 7: Add Docstrings to Parser / Writer / Transformer / Report (12 classes)

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py` — 1 class (ARXMLParser)
- Modify: `src/armodel/parser/abstract_arxml_parser.py` — 1 class (AbstractARXMLParser)
- Modify: `src/armodel/parser/connector_xlsx_parser.py` — 2 classes (ConnectorXls, ConnectorXlsReader)
- Modify: `src/armodel/parser/excel_parser.py` — 1 class (AbstractExcelParser)
- Modify: `src/armodel/writer/arxml_writer.py` — 1 class (ARXMLWriter)
- Modify: `src/armodel/writer/abstract_arxml_writer.py` — 1 class (AbstractARXMLWriter)
- Modify: `src/armodel/transformer/abstract.py` — 1 class (AbstractTransformer)
- Modify: `src/armodel/transformer/admin_data.py` — 1 class (AdminDataTransformer)
- Modify: `src/armodel/report/connector_xls_report.py` — 1 class (ConnectorXlsReport)
- Modify: `src/armodel/report/excel_report.py` — 1 class (ExcelReporter)

- [ ] **Step 1: Read all files, add docstrings to undocumented classes**

Key classes to document well:
- ARXMLParser: Main parser, loads ARXML files. Should document parse flow, options param (warning mode).
- AbstractARXMLParser: Base class. Document contract for subclasses.
- ARXMLWriter: Main writer, serializes model to ARXML. Should document save flow, version requirements.
- AbstractARXMLWriter: Base class. Document contract for subclasses.

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add src/armodel/parser/ src/armodel/writer/ src/armodel/transformer/ src/armodel/report/
git commit -m "docs: add docstrings to parser, writer, transformer, report (12 classes)"
```

---

### Task 8: Add Docstrings to Lib & Data Models (6 classes)

**Files:**
- Modify: `src/armodel/lib/cli_args_parser.py` — 1 class (InputFileParser)
- Modify: `src/armodel/lib/sw_component.py` — 1 class (SwComponentAnalyzer)
- Modify: `src/armodel/lib/system_signal.py` — 1 class (SystemSignalAnalyzer)
- Modify: `src/armodel/data_models/sw_connector.py` — 3 classes (SwConnectorData, DelegationSwConnectorData, AssemblySwConnectorData)

- [ ] **Step 1: Read all files, add docstrings to undocumented classes**

- [ ] **Step 2: Run tests**

```bash
python scripts/run_tests.py
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add src/armodel/lib/ src/armodel/data_models/
git commit -m "docs: add docstrings to lib and data models (6 classes)"
```

---

### Task 9: Final Verification

**Files:**
- Modify: None (verification only)

- [ ] **Step 1: Run docstring coverage report**

```bash
python scripts/generate_docstring_report.py
```

Expected: 815/815 documented (100% coverage).

- [ ] **Step 2: Run full test suite**

```bash
python scripts/run_tests.py
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

## What Changed From Original Plan

- **Removed 3 no-op tasks**: PrimitiveTypes.py (all documented), ExecutionOrderConstraint.py (all documented), LifeCycles.py (all documented)
- **Fixed AutosarTopLevelStructure path**: Was `.py` (wrong), now `AutosarTopLevelStructure/__init__.py`
- **Consolidated from 22 to 9 tasks**: Fewer agent handoffs
- **CLI files removed**: No classes exist in CLI scripts
- **Accurate counts**: Based on actual scan (199 undocumented, not 307)
- **Added exact undocumented class lists**: Each task lists every class needing a docstring
