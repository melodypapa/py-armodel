# BswM ECUC Export Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract the BswM ECUC configuration (SWS BSW Mode Manager chapter 10.2) into a `BswmModule` data model and export it as an `.xlsx` workbook with one sheet per container, `BswMAction` and `BswMActionList` first.

**Architecture:** Three new units mirroring the existing OS ECUC pipeline (`data_models/ecuc/os.py` → `parser/os_ecuc_parser.py` → `report/os_export.py` → `cli/os_config_export_cli.py`): a plain-class data model (`data_models/ecuc/bswm.py`), a tolerant markdown table parser (`parser/bswm_ecuc_parser.py`) that classifies containers/parameters per the ECUC metamodel, and an `ExcelReporter`-based exporter (`report/bswm_export.py`) wired to a `bswm-ecuc-export` console script.

**Tech Stack:** Python 3.8-compatible `typing` (mandatory in this repo), `openpyxl` via `ExcelReporter`, `pytest`, `ruff` + `mypy` (must stay green), Black at 200 chars.

**Spec:** `docs/superpowers/specs/2026-10-18-bswm-ecuc-export-design.md`

**Measured facts used by the tests:** 91 container sections, 135 `Parameter Name` rows, 92 included-container entries in the real document (`autosar/ECUC/markdown/ModeManagement/AUTOSAR_CP_SWS_BSWModeManager.md`). `BswM` includes 2 children; `BswMConfig` 1 param + 3 children; `BswMAvailableActions` 34 children; `BswMAction` 0 params + 1 child; `BswMActionList` 2 params + 1 child; `BswMGeneral` 19 params.

**Naming note:** accessors follow the field name like `os.py` does (`field containers` → `getContainers`/`addContainer`), so child accessors are `getParameters`/`addParameter`, not `addBswmParameter`.

---

## File Structure

| File | Responsibility |
|------|----------------|
| `src/armodel/data_models/ecuc/bswm.py` (new) | `BswmModule`, `BswmContainer`, `BswmParameter`, `BswmReference`, `BswmIncludedContainer`, `BswmRange`, `BswmConfigurationClass` |
| `src/armodel/data_models/ecuc/__init__.py` (modify) | re-export the BswM model classes |
| `src/armodel/parser/bswm_ecuc_parser.py` (new) | chapter extraction, row collection, ECUC classification, `BswmEcucParser` |
| `src/armodel/parser/__init__.py` (modify) | export `BswmEcucParser`, `BswmEcucParseError` |
| `src/armodel/report/bswm_export.py` (new) | `BswmConfigXlsxExporter`, `BswmConfigExporter` |
| `src/armodel/report/__init__.py` (modify) | export the two exporter classes |
| `src/armodel/cli/bswm_ecuc_export_cli.py` (new) | `main()` CLI entry point |
| `pyproject.toml` (modify) | `bswm-ecuc-export` console script |
| `tests/test_armodel/data_models/ecuc/test_bswm.py` (new) | model unit tests |
| `tests/test_armodel/parser/test_bswm_ecuc_parser.py` (new) | parser unit tests |
| `tests/test_armodel/report/test_bswm_export.py` (new) | exporter unit tests |
| `tests/test_armodel/cli/test_bswm_ecuc_export_cli.py` (new) | CLI guard test |
| `tests/test_armodel/report/test_bswm_ecuc_export.py` (new) | integration canary over the real document |

**Environment:** always run Python through uv — `uv run pytest ...`. Lint with `npm run lint` (flake8 + ruff + mypy). Format with `npm run black`.

---

### Task 1: BswM configuration data model

**Files:**
- Create: `src/armodel/data_models/ecuc/bswm.py`
- Modify: `src/armodel/data_models/ecuc/__init__.py`
- Test: `tests/test_armodel/data_models/ecuc/test_bswm.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_armodel/data_models/ecuc/test_bswm.py`:

```python
from armodel.data_models.ecuc import BswmConfigurationClass, BswmContainer, BswmIncludedContainer, BswmModule, BswmParameter, BswmRange, BswmReference


def test_bswm_parameter_setters_return_self_and_default_to_none():
    parameter = BswmParameter()

    assert parameter.getName() == ""
    assert parameter.getParameterType() is None
    assert parameter.getLowerMultiplicity() is None
    assert parameter.getUpperMultiplicityInfinite() is None
    assert parameter.getRanges() == []
    assert parameter.getDefaults() == []
    assert parameter.getMultiplicityConfigClasses() == []
    assert parameter.getValueConfigClasses() == []

    result = parameter.setName("BswMMainFunctionPeriod").setParameterType("EcucFloatParamDef").setLowerMultiplicity(0).setUpperMultiplicity(1).setScope("scope: local")

    assert result is parameter
    assert parameter.getName() == "BswMMainFunctionPeriod"
    assert parameter.getLowerMultiplicity() == 0
    assert parameter.getUpperMultiplicity() == 1
    assert parameter.getUpperMultiplicityInfinite() is None


def test_bswm_parameter_collects_ranges_defaults_and_config_classes():
    parameter = BswmParameter().setName("BswMLogicalOperator")
    literal = BswmRange().setValue("BSWM_AND").setDescription("logical and")
    multiplicity_class = BswmConfigurationClass().setConfigClass("Pre-compile time").setValue("X").setConfigVariant("VARIANT-PRE-COMPILE")
    value_class = BswmConfigurationClass().setConfigClass("Link time").setValue("-")

    parameter.addRange(literal).addDefault("BSWM_AND").setRegularExpression("[A-Z_]+").addMultiplicityConfigClass(multiplicity_class).addValueConfigClass(value_class)

    assert parameter.getRanges() == [literal]
    assert parameter.getDefaults() == ["BSWM_AND"]
    assert parameter.getRegularExpression() == "[A-Z_]+"
    assert parameter.getMultiplicityConfigClasses() == [multiplicity_class]
    assert parameter.getValueConfigClasses() == [value_class]


def test_bswm_reference_holds_targets_and_multiplicity():
    reference = BswmReference()

    result = reference.setName("BswMPartitionRef").setReferenceType("EcucReferenceDef").addTarget("EcucPartition").setLowerMultiplicity(0).setUpperMultiplicityInfinite(True).setPostBuildVariantValue(False)

    assert result is reference
    assert reference.getTargets() == ["EcucPartition"]
    assert reference.getUpperMultiplicity() is None
    assert reference.getUpperMultiplicityInfinite() is True
    assert reference.getPostBuildVariantValue() is False


def test_bswm_container_aggregates_parameters_references_and_children():
    container = BswmContainer()
    parameter = BswmParameter().setName("BswMActionListIndex")
    reference = BswmReference().setName("BswMActionRef")
    included = BswmIncludedContainer().setName("BswMAvailableActions").setMultiplicity("1").setScope("Choice container.")

    result = container.setName("BswMActionList").setContainerType("EcucParamConfContainerDef").setParent("BswMModeControl").setSwsItem("[ECUC_BswM_00811]").addParameter(parameter).addReference(reference).addIncludedContainer(included)

    assert result is container
    assert container.getParameters() == [parameter]
    assert container.getReferences() == [reference]
    assert container.getIncludedContainers() == [included]
    assert container.getSwsItem() == "[ECUC_BswM_00811]"


def test_bswm_module_holds_containers_in_insertion_order_and_looks_them_up():
    module = BswmModule()
    first = BswmContainer().setName("BswMAction")
    second = BswmContainer().setName("BswMConfig")

    result = module.setName("BswM").setPostBuildVariantSupport(True).addSupportedConfigVariant("VARIANT-PRE-COMPILE").addContainer(first).addContainer(second)

    assert result is module
    assert module.getContainers() == [first, second]
    assert module.getContainer("BswMConfig") is second
    assert module.getContainer("missing") is None
    assert module.getPostBuildVariantSupport() is True
    assert module.getSupportedConfigVariants() == ["VARIANT-PRE-COMPILE"]


def test_bswm_module_containers_are_independent_per_instance():
    first = BswmModule()
    second = BswmModule()

    first.addContainer(BswmContainer().setName("BswMAction"))

    assert first.getContainers() != []
    assert second.getContainers() == []
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_bswm.py -v`
Expected: FAIL — `ImportError: cannot import name 'BswmConfigurationClass'`

- [ ] **Step 3: Write the model**

Create `src/armodel/data_models/ecuc/bswm.py`:

```python
from typing import List, Optional


class BswmConfigurationClass:
    """One configuration class row of an ECUC definition element (AUTOSAR_CP_TPS_ECUConfiguration 2.3.4.3.2)."""

    def __init__(self) -> None:
        # The configuration class of the element: Pre-compile time, Link time or Post-build time.
        self.configClass: Optional[str] = None

        # The configuration variants the class applies to, e.g. VARIANT-PRE-COMPILE.
        self.configVariant: Optional[str] = None

        # X when the element is configurable in this class, - when it is not.
        self.value: Optional[str] = None

    def getConfigClass(self) -> Optional[str]:
        return self.configClass

    def setConfigClass(self, value: Optional[str]) -> "BswmConfigurationClass":
        self.configClass = value
        return self

    def getConfigVariant(self) -> Optional[str]:
        return self.configVariant

    def setConfigVariant(self, value: Optional[str]) -> "BswmConfigurationClass":
        self.configVariant = value
        return self

    def getValue(self) -> Optional[str]:
        return self.value

    def setValue(self, value: Optional[str]) -> "BswmConfigurationClass":
        self.value = value
        return self


class BswmRange:
    """A Range row of SWS chapter 10.2: an enumeration literal for EcucEnumerationParamDef, or a value interval for EcucIntegerParamDef/EcucFloatParamDef."""

    def __init__(self) -> None:
        # Literal name (BSWM_AND) or value interval (]0 .. INF[).
        self.value: str = ""

        # Optional description of the literal or interval.
        self.description: Optional[str] = None

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str) -> "BswmRange":
        self.value = value
        return self

    def getDescription(self) -> Optional[str]:
        return self.description

    def setDescription(self, value: Optional[str]) -> "BswmRange":
        self.description = value
        return self


class BswmParameter:
    """An ECUC scalar/enum parameter definition of SWS BswM chapter 10.2."""

    def __init__(self) -> None:
        self.name: str = ""
        self.parameterType: Optional[str] = None
        self.parent: Optional[str] = None
        self.description: Optional[str] = None
        self.swsItem: Optional[str] = None
        self.lowerMultiplicity: Optional[int] = None
        self.upperMultiplicity: Optional[int] = None
        self.upperMultiplicityInfinite: Optional[bool] = None
        self.scope: Optional[str] = None
        self.postBuildVariantMultiplicity: Optional[bool] = None
        self.postBuildVariantValue: Optional[bool] = None
        self.multiplicityConfigClasses: List[BswmConfigurationClass] = []
        self.valueConfigClasses: List[BswmConfigurationClass] = []
        self.ranges: List[BswmRange] = []
        self.defaults: List[str] = []
        self.regularExpression: Optional[str] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmParameter":
        self.name = value
        return self

    def getParameterType(self) -> Optional[str]:
        return self.parameterType

    def setParameterType(self, value: Optional[str]) -> "BswmParameter":
        self.parameterType = value
        return self

    def getParent(self) -> Optional[str]:
        return self.parent

    def setParent(self, value: Optional[str]) -> "BswmParameter":
        self.parent = value
        return self

    def getDescription(self) -> Optional[str]:
        return self.description

    def setDescription(self, value: Optional[str]) -> "BswmParameter":
        self.description = value
        return self

    def getSwsItem(self) -> Optional[str]:
        return self.swsItem

    def setSwsItem(self, value: Optional[str]) -> "BswmParameter":
        self.swsItem = value
        return self

    def getLowerMultiplicity(self) -> Optional[int]:
        return self.lowerMultiplicity

    def setLowerMultiplicity(self, value: Optional[int]) -> "BswmParameter":
        self.lowerMultiplicity = value
        return self

    def getUpperMultiplicity(self) -> Optional[int]:
        return self.upperMultiplicity

    def setUpperMultiplicity(self, value: Optional[int]) -> "BswmParameter":
        self.upperMultiplicity = value
        return self

    def getUpperMultiplicityInfinite(self) -> Optional[bool]:
        return self.upperMultiplicityInfinite

    def setUpperMultiplicityInfinite(self, value: Optional[bool]) -> "BswmParameter":
        self.upperMultiplicityInfinite = value
        return self

    def getScope(self) -> Optional[str]:
        return self.scope

    def setScope(self, value: Optional[str]) -> "BswmParameter":
        self.scope = value
        return self

    def getPostBuildVariantMultiplicity(self) -> Optional[bool]:
        return self.postBuildVariantMultiplicity

    def setPostBuildVariantMultiplicity(self, value: Optional[bool]) -> "BswmParameter":
        self.postBuildVariantMultiplicity = value
        return self

    def getPostBuildVariantValue(self) -> Optional[bool]:
        return self.postBuildVariantValue

    def setPostBuildVariantValue(self, value: Optional[bool]) -> "BswmParameter":
        self.postBuildVariantValue = value
        return self

    def getMultiplicityConfigClasses(self) -> List[BswmConfigurationClass]:
        return self.multiplicityConfigClasses

    def addMultiplicityConfigClass(self, value: BswmConfigurationClass) -> "BswmParameter":
        self.multiplicityConfigClasses.append(value)
        return self

    def getValueConfigClasses(self) -> List[BswmConfigurationClass]:
        return self.valueConfigClasses

    def addValueConfigClass(self, value: BswmConfigurationClass) -> "BswmParameter":
        self.valueConfigClasses.append(value)
        return self

    def getRanges(self) -> List[BswmRange]:
        return self.ranges

    def addRange(self, value: BswmRange) -> "BswmParameter":
        self.ranges.append(value)
        return self

    def getDefaults(self) -> List[str]:
        return self.defaults

    def addDefault(self, value: str) -> "BswmParameter":
        self.defaults.append(value)
        return self

    def getRegularExpression(self) -> Optional[str]:
        return self.regularExpression

    def setRegularExpression(self, value: Optional[str]) -> "BswmParameter":
        self.regularExpression = value
        return self


class BswmReference:
    """An ECUC reference definition of SWS BswM chapter 10.2 (EcucReferenceDef and its siblings)."""

    def __init__(self) -> None:
        self.name: str = ""
        self.referenceType: Optional[str] = None
        self.targets: List[str] = []
        self.parent: Optional[str] = None
        self.description: Optional[str] = None
        self.swsItem: Optional[str] = None
        self.lowerMultiplicity: Optional[int] = None
        self.upperMultiplicity: Optional[int] = None
        self.upperMultiplicityInfinite: Optional[bool] = None
        self.scope: Optional[str] = None
        self.postBuildVariantMultiplicity: Optional[bool] = None
        self.postBuildVariantValue: Optional[bool] = None
        self.multiplicityConfigClasses: List[BswmConfigurationClass] = []
        self.valueConfigClasses: List[BswmConfigurationClass] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmReference":
        self.name = value
        return self

    def getReferenceType(self) -> Optional[str]:
        return self.referenceType

    def setReferenceType(self, value: Optional[str]) -> "BswmReference":
        self.referenceType = value
        return self

    def getTargets(self) -> List[str]:
        return self.targets

    def addTarget(self, value: str) -> "BswmReference":
        self.targets.append(value)
        return self

    def getParent(self) -> Optional[str]:
        return self.parent

    def setParent(self, value: Optional[str]) -> "BswmReference":
        self.parent = value
        return self

    def getDescription(self) -> Optional[str]:
        return self.description

    def setDescription(self, value: Optional[str]) -> "BswmReference":
        self.description = value
        return self

    def getSwsItem(self) -> Optional[str]:
        return self.swsItem

    def setSwsItem(self, value: Optional[str]) -> "BswmReference":
        self.swsItem = value
        return self

    def getLowerMultiplicity(self) -> Optional[int]:
        return self.lowerMultiplicity

    def setLowerMultiplicity(self, value: Optional[int]) -> "BswmReference":
        self.lowerMultiplicity = value
        return self

    def getUpperMultiplicity(self) -> Optional[int]:
        return self.upperMultiplicity

    def setUpperMultiplicity(self, value: Optional[int]) -> "BswmReference":
        self.upperMultiplicity = value
        return self

    def getUpperMultiplicityInfinite(self) -> Optional[bool]:
        return self.upperMultiplicityInfinite

    def setUpperMultiplicityInfinite(self, value: Optional[bool]) -> "BswmReference":
        self.upperMultiplicityInfinite = value
        return self

    def getScope(self) -> Optional[str]:
        return self.scope

    def setScope(self, value: Optional[str]) -> "BswmReference":
        self.scope = value
        return self

    def getPostBuildVariantMultiplicity(self) -> Optional[bool]:
        return self.postBuildVariantMultiplicity

    def setPostBuildVariantMultiplicity(self, value: Optional[bool]) -> "BswmReference":
        self.postBuildVariantMultiplicity = value
        return self

    def getPostBuildVariantValue(self) -> Optional[bool]:
        return self.postBuildVariantValue

    def setPostBuildVariantValue(self, value: Optional[bool]) -> "BswmReference":
        self.postBuildVariantValue = value
        return self

    def getMultiplicityConfigClasses(self) -> List[BswmConfigurationClass]:
        return self.multiplicityConfigClasses

    def addMultiplicityConfigClass(self, value: BswmConfigurationClass) -> "BswmReference":
        self.multiplicityConfigClasses.append(value)
        return self

    def getValueConfigClasses(self) -> List[BswmConfigurationClass]:
        return self.valueConfigClasses

    def addValueConfigClass(self, value: BswmConfigurationClass) -> "BswmReference":
        self.valueConfigClasses.append(value)
        return self


class BswmIncludedContainer:
    """A child container entry of an Included Containers / Container Choices table."""

    def __init__(self) -> None:
        self.name: str = ""
        self.multiplicity: Optional[str] = None
        self.scope: Optional[str] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmIncludedContainer":
        self.name = value
        return self

    def getMultiplicity(self) -> Optional[str]:
        return self.multiplicity

    def setMultiplicity(self, value: Optional[str]) -> "BswmIncludedContainer":
        self.multiplicity = value
        return self

    def getScope(self) -> Optional[str]:
        return self.scope

    def setScope(self, value: Optional[str]) -> "BswmIncludedContainer":
        self.scope = value
        return self


class BswmContainer:
    """An ECUC container definition of SWS BswM chapter 10.2 (EcucParamConfContainerDef or EcucChoiceContainerDef)."""

    def __init__(self) -> None:
        self.name: str = ""
        self.containerType: Optional[str] = None
        self.parent: Optional[str] = None
        self.description: Optional[str] = None
        self.swsItem: Optional[str] = None
        self.lowerMultiplicity: Optional[int] = None
        self.upperMultiplicity: Optional[int] = None
        self.upperMultiplicityInfinite: Optional[bool] = None
        self.postBuildVariantMultiplicity: Optional[bool] = None
        self.multiplicityConfigClasses: List[BswmConfigurationClass] = []
        self.parameters: List[BswmParameter] = []
        self.references: List[BswmReference] = []
        self.includedContainers: List[BswmIncludedContainer] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmContainer":
        self.name = value
        return self

    def getContainerType(self) -> Optional[str]:
        return self.containerType

    def setContainerType(self, value: Optional[str]) -> "BswmContainer":
        self.containerType = value
        return self

    def getParent(self) -> Optional[str]:
        return self.parent

    def setParent(self, value: Optional[str]) -> "BswmContainer":
        self.parent = value
        return self

    def getDescription(self) -> Optional[str]:
        return self.description

    def setDescription(self, value: Optional[str]) -> "BswmContainer":
        self.description = value
        return self

    def getSwsItem(self) -> Optional[str]:
        return self.swsItem

    def setSwsItem(self, value: Optional[str]) -> "BswmContainer":
        self.swsItem = value
        return self

    def getLowerMultiplicity(self) -> Optional[int]:
        return self.lowerMultiplicity

    def setLowerMultiplicity(self, value: Optional[int]) -> "BswmContainer":
        self.lowerMultiplicity = value
        return self

    def getUpperMultiplicity(self) -> Optional[int]:
        return self.upperMultiplicity

    def setUpperMultiplicity(self, value: Optional[int]) -> "BswmContainer":
        self.upperMultiplicity = value
        return self

    def getUpperMultiplicityInfinite(self) -> Optional[bool]:
        return self.upperMultiplicityInfinite

    def setUpperMultiplicityInfinite(self, value: Optional[bool]) -> "BswmContainer":
        self.upperMultiplicityInfinite = value
        return self

    def getPostBuildVariantMultiplicity(self) -> Optional[bool]:
        return self.postBuildVariantMultiplicity

    def setPostBuildVariantMultiplicity(self, value: Optional[bool]) -> "BswmContainer":
        self.postBuildVariantMultiplicity = value
        return self

    def getMultiplicityConfigClasses(self) -> List[BswmConfigurationClass]:
        return self.multiplicityConfigClasses

    def addMultiplicityConfigClass(self, value: BswmConfigurationClass) -> "BswmContainer":
        self.multiplicityConfigClasses.append(value)
        return self

    def getParameters(self) -> List[BswmParameter]:
        return self.parameters

    def addParameter(self, value: BswmParameter) -> "BswmContainer":
        self.parameters.append(value)
        return self

    def getReferences(self) -> List[BswmReference]:
        return self.references

    def addReference(self, value: BswmReference) -> "BswmContainer":
        self.references.append(value)
        return self

    def getIncludedContainers(self) -> List[BswmIncludedContainer]:
        return self.includedContainers

    def addIncludedContainer(self, value: BswmIncludedContainer) -> "BswmContainer":
        self.includedContainers.append(value)
        return self


class BswmModule:
    """The BswM ECUC module definition extracted from SWS BSW Mode Manager chapter 10.2."""

    def __init__(self) -> None:
        self.name: str = ""
        self.postBuildVariantSupport: Optional[bool] = None
        self.supportedConfigVariants: List[str] = []
        self.containers: List[BswmContainer] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmModule":
        self.name = value
        return self

    def getPostBuildVariantSupport(self) -> Optional[bool]:
        return self.postBuildVariantSupport

    def setPostBuildVariantSupport(self, value: Optional[bool]) -> "BswmModule":
        self.postBuildVariantSupport = value
        return self

    def getSupportedConfigVariants(self) -> List[str]:
        return self.supportedConfigVariants

    def addSupportedConfigVariant(self, value: str) -> "BswmModule":
        self.supportedConfigVariants.append(value)
        return self

    def getContainers(self) -> List[BswmContainer]:
        return self.containers

    def addContainer(self, value: BswmContainer) -> "BswmModule":
        self.containers.append(value)
        return self

    def getContainer(self, name: str) -> Optional[BswmContainer]:
        for container in self.containers:
            if container.getName() == name:
                return container
        return None

    @classmethod
    def from_file(cls, path) -> "BswmModule":
        from armodel.parser import BswmEcucParser

        return BswmEcucParser().load(path)

    @classmethod
    def from_markdown(cls, text: str) -> "BswmModule":
        from armodel.parser import BswmEcucParser

        return BswmEcucParser().parse(text)
```

Update `src/armodel/data_models/ecuc/__init__.py` to:

```python
from armodel.data_models.ecuc.bswm import BswmConfigurationClass, BswmContainer, BswmIncludedContainer, BswmModule, BswmParameter, BswmRange, BswmReference
from armodel.data_models.ecuc.os import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask

__all__ = [
    "BswmConfigurationClass",
    "BswmContainer",
    "BswmIncludedContainer",
    "BswmModule",
    "BswmParameter",
    "BswmRange",
    "BswmReference",
    "OsAlarm",
    "OsApplication",
    "OsIsr",
    "OsOs",
    "OsScheduleTable",
    "OsScheduleTableExpiryPoint",
    "OsTask",
]
```

(The `from_file`/`from_markdown` imports are function-local, so this file imports cleanly before the parser exists.)

- [ ] **Step 4: Run the test to verify it passes**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_bswm.py -v`
Expected: 6 passed

- [ ] **Step 5: Commit**

```bash
git add src/armodel/data_models/ecuc/bswm.py src/armodel/data_models/ecuc/__init__.py tests/test_armodel/data_models/ecuc/test_bswm.py
git commit -m "feat: add BswM ECUC configuration data model"
```

---

### Task 2: Parser foundations — chapter extraction, section split, row collection

**Files:**
- Create: `src/armodel/parser/bswm_ecuc_parser.py`
- Test: `tests/test_armodel/parser/test_bswm_ecuc_parser.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_armodel/parser/test_bswm_ecuc_parser.py`:

```python
import pytest

from armodel.parser.bswm_ecuc_parser import BswmEcucParseError, collect_rows, extract_chapter_lines, split_section_blocks


CHAPTER = """\
## 10.1 How to read this chapter

Refer to SWS_BSWGeneral.

## 10.2 Containers and configuration parameters

Some intro text.

## 10.2.1 BswM

| SWS Item    | [ECUC_BswM_01063] |
|-------------|-------------------|
| Module Name | BswM              |

## 10.3 Published Information

Nothing here.
"""


def test_extract_chapter_lines_returns_only_the_10_2_body():
    lines = CHAPTER.splitlines()

    chapter = extract_chapter_lines(lines)

    assert chapter[0].startswith("## 10.2 Containers")
    assert chapter[-1].strip() == "| Module Name | BswM              |"
    assert not any("10.1" in line or "10.3" in line for line in chapter)


def test_extract_chapter_lines_raises_when_chapter_is_missing():
    with pytest.raises(BswmEcucParseError, match="10.2"):
        extract_chapter_lines(["## 1 Introduction", "text"])


def test_split_section_blocks_returns_one_block_per_container():
    blocks = split_section_blocks(extract_chapter_lines(CHAPTER.splitlines()))

    assert [title for title, _lines in blocks] == ["BswM"]
    assert any(line.startswith("| SWS Item") for line in blocks[0][1])


def test_collect_rows_reads_pipe_rows_and_carries_labels_over_page_breaks():
    lines = [
        "| SWS Item                         | [ECUC_BswM_00814] | [ECUC_BswM_00814] |",
        "|----------------------------------|-------------------|-------------------|",
        "| Parameter Name                   | BswMLogicalOperator | BswMLogicalOperator |",
        "glyph[triangleinv]",
        "![Image](some.png)",
        "## glyph[triangle]",
        "|                                  | Link time         | X                 |",
    ]

    rows = collect_rows(lines)

    assert rows[0][0] == "SWS Item"
    assert rows[1][0] == "Parameter Name"
    # the page-break continuation inherits the previous label
    assert rows[2][0] == "Parameter Name"
    assert rows[2][1] == "Link time"
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `uv run pytest tests/test_armodel/parser/test_bswm_ecuc_parser.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'armodel.parser.bswm_ecuc_parser'`

- [ ] **Step 3: Write the parser foundations**

Create `src/armodel/parser/bswm_ecuc_parser.py`:

```python
import re
from typing import List, Optional, Tuple

CHAPTER_HEADING = "## 10.2 Containers and configuration parameters"
SECTION_HEADING_RE = re.compile(r"^##\s+10\.2\.(\d+)\s+(.*)$")
MULTIPLICITY_RE = re.compile(r"^\d+\.\.(\d+|\*)$|^\d+$")


class BswmEcucParseError(ValueError):
    """Raised when the SWS markdown does not contain a parseable chapter 10.2."""


def extract_chapter_lines(lines: List[str]) -> List[str]:
    """Return the lines of chapter 10.2, from its heading to the next level-2 heading."""
    start: Optional[int] = None
    end = len(lines)
    for index, line in enumerate(lines):
        stripped = line.strip()
        if start is None:
            if stripped == CHAPTER_HEADING:
                start = index
        elif stripped.startswith("## 10.3 "):
            end = index
            break
    if start is None:
        raise BswmEcucParseError("Chapter 10.2 'Containers and configuration parameters' not found")
    return lines[start:end]


def split_section_blocks(lines: List[str]) -> List[Tuple[str, List[str]]]:
    """Split the chapter body into (container name, block lines) pairs, one per 10.2.N heading."""
    blocks: List[Tuple[str, List[str]]] = []
    title: Optional[str] = None
    current: List[str] = []
    for line in lines:
        match = SECTION_HEADING_RE.match(line)
        if match is not None:
            if title is not None:
                blocks.append((title, current))
            title = match.group(2).strip()
            current = []
        elif title is not None:
            current.append(line)
    if title is not None:
        blocks.append((title, current))
    return blocks


def split_cells(line: str) -> Optional[List[str]]:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def is_separator_row(row: List[str]) -> bool:
    if not any(cell for cell in row):
        return False
    for cell in row:
        if cell and set(cell) - set("-: "):
            return False
    return True


def collect_rows(lines: List[str]) -> List[List[str]]:
    """Collect markdown table rows in order; a row whose first cell is empty inherits the previous label."""
    rows: List[List[str]] = []
    last_label = ""
    for line in lines:
        cells = split_cells(line)
        if cells is None or is_separator_row(cells):
            continue
        if cells[0]:
            last_label = cells[0]
        elif last_label:
            cells = [last_label] + cells[1:]
        rows.append(cells)
    return rows


def first_value(cells: List[str]) -> Optional[str]:
    """First non-empty cell after the label; merged cells duplicate their value across columns."""
    for cell in cells:
        if cell:
            return cell
    return None


def parse_multiplicity(text: Optional[str]) -> Tuple[Optional[int], Optional[int], Optional[bool]]:
    """Parse an SWS multiplicity such as '0..1', '1' or '1..*' into (lower, upper, upper_infinite)."""
    value = (text or "").strip()
    if not value:
        return (None, None, None)
    if ".." in value:
        lower_text, upper_text = value.split("..", 1)
    else:
        lower_text, upper_text = value, value
    lower = int(lower_text) if lower_text.isdigit() else None
    if upper_text == "*":
        return (lower, None, True)
    upper = int(upper_text) if upper_text.isdigit() else None
    return (lower, upper, None)
```

(The `armodel.data_models.ecuc` import and the module logger are added in Task 4, when the
code that uses them appears — adding them now would fail `ruff` with an unused import.)

- [ ] **Step 4: Run the test to verify it passes**

Run: `uv run pytest tests/test_armodel/parser/test_bswm_ecuc_parser.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add src/armodel/parser/bswm_ecuc_parser.py tests/test_armodel/parser/test_bswm_ecuc_parser.py
git commit -m "feat: add BswM ECUC parser foundations (chapter extraction and row collection)"
```

---

### Task 3: Parser classification — ECUC parameter/reference typing

**Files:**
- Modify: `src/armodel/parser/bswm_ecuc_parser.py` (append at the end of the file)
- Test: `tests/test_armodel/parser/test_bswm_ecuc_parser.py` (append)

- [ ] **Step 1: Write the failing test**

Append to `tests/test_armodel/parser/test_bswm_ecuc_parser.py`:

```python
from armodel.parser.bswm_ecuc_parser import classify_type, parse_multiplicity  # noqa: E402


def test_parse_multiplicity_variants():
    assert parse_multiplicity("0..1") == (0, 1, None)
    assert parse_multiplicity("1") == (1, 1, None)
    assert parse_multiplicity("1..*") == (1, None, True)
    assert parse_multiplicity("0..*") == (0, None, True)
    assert parse_multiplicity("2..5") == (2, 5, None)
    assert parse_multiplicity("") == (None, None, None)
    assert parse_multiplicity(None) == (None, None, None)


def test_classify_type_maps_scalar_parameters_to_ecuc_classes():
    assert classify_type("EcucBooleanParamDef") == ("parameter", "EcucBooleanParamDef", [])
    assert classify_type("EcucEnumerationParamDef") == ("parameter", "EcucEnumerationParamDef", [])
    assert classify_type("EcucStringParamDef") == ("parameter", "EcucStringParamDef", [])
    assert classify_type("EcucIntegerParamDef") == ("parameter", "EcucIntegerParamDef", [])
    assert classify_type("EcucFloatParamDef") == ("parameter", "EcucFloatParamDef", [])
    assert classify_type("EcucIntegerParamDef (Symbolic Name generated for this parameter)") == ("parameter", "EcucIntegerParamDef", [])


def test_classify_type_maps_references_and_extracts_targets():
    assert classify_type("Reference to BswMSwitchPort") == ("reference", "EcucReferenceDef", ["BswMSwitchPort"])
    assert classify_type("Symbolic name reference to ComMChannel") == ("reference", "EcucSymbolicNameReferenceDef", ["ComMChannel"])
    assert classify_type("Choice reference to [ BswMLogicalExpression, BswMModeCondition ]") == ("reference", "EcucChoiceReferenceDef", ["BswMLogicalExpression", "BswMModeCondition"])
    assert classify_type("Foreign reference to MODE-DECLARATION") == ("reference", "EcucForeignReferenceDef", ["MODE-DECLARATION"])
    assert classify_type("Instance reference to VARIABLE-DATA-PROTOTYPE context: SW-COMPONENT-PROTOTYPE*PORT-PROTOTYPE") == ("reference", "EcucInstanceReferenceDef", ["VARIABLE-DATA-PROTOTYPE"])


def test_classify_type_keeps_unknown_types_as_raw_parameter_type():
    assert classify_type("SomeFutureDef") == ("parameter", "SomeFutureDef", [])
    assert classify_type("") == ("parameter", None, [])
    assert classify_type(None) == ("parameter", None, [])
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `uv run pytest tests/test_armodel/parser/test_bswm_ecuc_parser.py -v`
Expected: FAIL — `ImportError: cannot import name 'classify_type'`

- [ ] **Step 3: Implement the classification helpers**

Append to `src/armodel/parser/bswm_ecuc_parser.py`:

```python
PARAMETER_CLASS_NAMES = [
    "EcucBooleanParamDef",
    "EcucIntegerParamDef",
    "EcucFloatParamDef",
    "EcucStringParamDef",
    "EcucEnumerationParamDef",
    "EcucFunctionNameDef",
    "EcucLinkerSymbolDef",
    "EcucMultilineStringParamDef",
    "EcucAddInfoParamDef",
]

REFERENCE_TYPE_RE = re.compile(r"^(Reference|Symbolic name reference|Choice reference|Foreign reference|Instance reference)\s+to\s+(.+)$", re.IGNORECASE)

REFERENCE_CLASS_BY_KIND = {
    "Reference": "EcucReferenceDef",
    "Symbolic name reference": "EcucSymbolicNameReferenceDef",
    "Choice reference": "EcucChoiceReferenceDef",
    "Foreign reference": "EcucForeignReferenceDef",
    "Instance reference": "EcucInstanceReferenceDef",
}


def reference_targets(text: str) -> List[str]:
    """Extract the reference targets from the text after 'to', e.g. '[ A, B ]' or 'X context: ...'."""
    value = text.strip()
    start = value.find("[")
    if start != -1 and value.endswith("]"):
        inner = value[start + 1:value.rfind("]")]
        return [item.strip() for item in inner.split(",") if item.strip()]
    cut = value.find(" context:")
    if cut != -1:
        value = value[:cut]
    value = value.strip()
    return [value] if value else []


def classify_type(raw: Optional[str]) -> Tuple[str, Optional[str], List[str]]:
    """Classify an SWS 'Type' cell into (kind, ECUC metamodel class, targets).

    kind is 'parameter' or 'reference'; an unrecognised value stays a parameter with the raw
    type string so nothing is silently dropped.
    """
    text = (raw or "").strip()
    if not text:
        return ("parameter", None, [])
    for name in PARAMETER_CLASS_NAMES:
        if text == name or text.startswith(name + " "):
            return ("parameter", name, [])
    match = REFERENCE_TYPE_RE.match(text)
    if match is None:
        return ("parameter", text, [])
    ecuc_class = REFERENCE_CLASS_BY_KIND[match.group(1)]
    return ("reference", ecuc_class, reference_targets(match.group(2)))
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `uv run pytest tests/test_armodel/parser/test_bswm_ecuc_parser.py -v`
Expected: 8 passed

- [ ] **Step 5: Commit**

```bash
git add src/armodel/parser/bswm_ecuc_parser.py tests/test_armodel/parser/test_bswm_ecuc_parser.py
git commit -m "feat: classify BswM ECUC parameters and references per the ECUC metamodel"
```

---

### Task 4: Block parser and BswmEcucParser

**Files:**
- Modify: `src/armodel/parser/bswm_ecuc_parser.py` (replace the import block, append the block parser and the parser facade)
- Modify: `src/armodel/parser/__init__.py`
- Test: `tests/test_armodel/parser/test_bswm_ecuc_parser.py` (append)

- [ ] **Step 1: Write the failing test**

Append to `tests/test_armodel/parser/test_bswm_ecuc_parser.py`:

```python
from armodel.parser import BswmEcucParser  # noqa: E402

MODULE_BLOCK = """\
## 10.2 Containers and configuration parameters

## 10.2.1 BswM

| SWS Item                   | [ECUC_BswM_01063]                                          |
|----------------------------|------------------------------------------------------------|
| Module Name                | BswM                                                       |
| Description                | Configuration of the BswM (Basic SW Mode Manager) module.  |
| Post-Build Variant Support | true                                                       |
| Supported Config Variants  | VARIANT-LINK-TIME, VARIANT-POST-BUILD, VARIANT-PRE-COMPILE |

| Included Containers   | Included Containers   | Included Containers                     |
|-----------------------|-----------------------|-----------------------------------------|
| Container Name        | Multiplicity          | Scope / Dependency                      |
| BswMConfig            | 1..*                  | This container exists once per partition. |
| BswMGeneral           | 1                     | General configuration parameters.       |

## 10.2.2 BswMConfig

| SWS Item                 | [ECUC_BswM_00895]            |
|--------------------------|------------------------------|
| Container Name           | BswMConfig                   |
| Parent Container         | BswM                         |
| Description              | Once per partition.          |
| Configuration Parameters | Configuration Parameters     |

| SWS Item                         | [ECUC_BswM_00984]                                         | [ECUC_BswM_00984] |
|----------------------------------|-----------------------------------------------------------|-------------------|
| Parameter Name                   | BswMPartitionRef                                          | BswMPartitionRef  |
| Parent Container                 | BswMConfig                                                | BswMConfig        |
| Description                      | This references the partition the BswM shall run inside.  |                   |
| Multiplicity                     | 0..1                                                      | 0..1              |
| Type                             | Reference to EcucPartition                                |                   |
| Post-Build Variant Value         | false                                                     |                   |
| Multiplicity Configuration Class | Pre-compile time                                          | All Variants      |
| Multiplicity Configuration Class | Link time                                                 | -                 |
| Value Configuration Class        | Post-build time                                           | -                 |
| Scope / Dependency               | scope: local                                              |                   |

| Included Containers     | Included Containers   | Included Containers |
|-------------------------|-----------------------|---------------------|
| Container Name          | Multiplicity          | Scope / Dependency  |
| BswMArbitration         | 1                     | Mode arbitration.   |
| BswMDataTypeMappingSets | 0..1                  | DataTypeMappingSet. |
| BswMModeControl         | 1                     | Mode control.       |

## 10.2.3 BswMArbitration

| SWS Item         | [ECUC_BswM_00801]     |
|------------------|-----------------------|
| Container Name   | BswMArbitration       |
| Parent Container | BswMConfig            |
| Description      | Mode arbitration.     |

| SWS Item                         | [ECUC_BswM_00814]            | [ECUC_BswM_00814] | [ECUC_BswM_00814]                                        |
|----------------------------------|------------------------------|-------------------|----------------------------------------------------------|
| Parameter Name                   | BswMLogicalOperator          |                   |                                                          |
| Parent Container                 | BswMLogicalExpression        |                   |                                                          |
| Description                      | The logical operator.        |                   |                                                          |
| Multiplicity                     | 0..1                         |                   |                                                          |
| Type                             | EcucEnumerationParamDef      |                   |                                                          |
| Range                            | BSWM_AND                     | -                 |                                                          |
| Range                            | BSWM_OR                      | -                 |                                                          |
| Default value                    | BSWM_OR                      |                   |                                                          |
| Post-Build Variant Multiplicity  | false                        |                   |                                                          |
| Post-Build Variant Value         | false                        |                   |                                                          |
| Multiplicity Configuration Class | Pre-compile time             | X                 | VARIANT-PRE-COMPILE, VARIANT-LINK-TIME, VARIANT-POST-BUILD |
|                                  | Link time                    | X                 | VARIANT-LINK-TIME, VARIANT-POST-BUILD                    |
| Value Configuration Class        | Pre-compile time             | X                 | VARIANT-PRE-COMPILE                                      |
| Scope / Dependency               | scope: local                 |                   |                                                          |

## 10.2.4 BswMAction

| SWS Item                         | [ECUC_BswM_00810]   |
|----------------------------------|---------------------|
| Choice Container Name            | BswMAction          |
| Parent Container                 | BswMModeControl     |
| Description                      | Defines an action.  |
| Post-Build Variant Multiplicity  | false               |
| Multiplicity Configuration Class | Pre-compile time    | X | VARIANT-PRE-COMPILE, VARIANT-LINK-TIME, VARIANT-POST-BUILD |

| Included Containers   |    |                                                                                  |
|-----------------------|----|----------------------------------------------------------------------------------|
| BswMAvailableActions  | 1  | Choice container including the available actions.                                 |

## 10.2.5 BswMModeRequestPort

| SWS Item         | [ECUC_BswM_00835]  |
|------------------|--------------------|
| Container Name   | BswMModeRequestPort |
| Parent Container | BswMArbitration    |
| Description      | Mode requests.     |

| SWS Item          | [ECUC_BswM_00920]                        |
|-------------------|------------------------------------------|
| Parameter Name    | BswMModeSwitchInterfaceRef               |
| Parent Container  | BswMModeRequestPort                      |
| Description       | References the mode switch interface.    |
| Multiplicity      | 0..1                                     |
| Type              | Foreign reference to MODE-SWITCH-INTERFACE |
| Scope / Dependency| scope: local                             |

No Included Containers
"""

CHOICE_HEADER_DOCUMENT = """\
## 10.2 Containers and configuration parameters

## 10.2.1 BswM

| SWS Item    | [ECUC_BswM_01063] |
|-------------|-------------------|
| Module Name | BswM              |

## 10.2.2 BswMAvailableActions

| SWS Item              | [ECUC_BswM_00826]                  |
|-----------------------|------------------------------------|
| Choice Container Name | BswMAvailableActions               |
| Parent Container      | BswMAction                         |
| Description           | Choice container with the actions. |

| Container Choices Container Name     | Multiplicity   | Scope / Dependency            |
|--------------------------------------|----------------|-------------------------------|
| BswMClearEventRequest                | 0..1           | Clears an event request.      |
| BswMComMAllowCom                     | 0..1           | Allows communication.         |

| Container Choices                    | Container Choices   | Container Choices       |
|--------------------------------------|---------------------|-------------------------|
| Container Name                       | Multiplicity        | Scope / Dependency      |
| BswMComMModeLimitation               | 0..1                | Limits communication.   |
| BswMUserCallout                      | 0..1                | User callout.           |
"""


def test_parse_builds_the_module_from_the_module_block():
    module = BswmEcucParser().parse(MODULE_BLOCK)

    assert module.getName() == "BswM"
    assert module.getPostBuildVariantSupport() is True
    assert module.getSupportedConfigVariants() == ["VARIANT-LINK-TIME", "VARIANT-POST-BUILD", "VARIANT-PRE-COMPILE"]
    assert [container.getName() for container in module.getContainers()] == ["BswM", "BswMConfig", "BswMArbitration", "BswMAction", "BswMModeRequestPort"]
    assert module.getContainers()[0].getContainerType() == "EcucModuleDef"


def test_parse_reads_container_metadata_and_included_containers():
    module = BswmEcucParser().parse(MODULE_BLOCK)

    config = module.getContainer("BswMConfig")
    assert config is not None
    assert config.getContainerType() == "EcucParamConfContainerDef"
    assert config.getParent() == "BswM"
    assert config.getSwsItem() == "[ECUC_BswM_00895]"
    assert [(child.getName(), child.getMultiplicity()) for child in config.getIncludedContainers()] == [("BswMArbitration", "1"), ("BswMDataTypeMappingSets", "0..1"), ("BswMModeControl", "1")]


def test_parse_reads_parameter_fields_merged_cells_and_config_classes():
    module = BswmEcucParser().parse(MODULE_BLOCK)

    config = module.getContainer("BswMConfig")
    assert config is not None
    assert len(config.getParameters()) == 0
    assert len(config.getReferences()) == 1

    reference = config.getReferences()[0]
    assert reference.getName() == "BswMPartitionRef"
    assert reference.getSwsItem() == "[ECUC_BswM_00984]"
    assert reference.getParent() == "BswMConfig"
    assert reference.getReferenceType() == "EcucReferenceDef"
    assert reference.getTargets() == ["EcucPartition"]
    assert (reference.getLowerMultiplicity(), reference.getUpperMultiplicity(), reference.getUpperMultiplicityInfinite()) == (0, 1, None)
    assert reference.getPostBuildVariantValue() is False
    assert reference.getScope() == "scope: local"
    assert [(entry.getConfigClass(), entry.getValue(), entry.getConfigVariant()) for entry in reference.getMultiplicityConfigClasses()] == [("Pre-compile time", "All Variants", None), ("Link time", "-", None)]
    assert [(entry.getConfigClass(), entry.getValue(), entry.getConfigVariant()) for entry in reference.getValueConfigClasses()] == [("Post-build time", "-", None)]


def test_parse_reads_ranges_defaults_and_page_break_continuations():
    module = BswmEcucParser().parse(MODULE_BLOCK)

    arbitration = module.getContainer("BswMArbitration")
    assert arbitration is not None
    parameter = arbitration.getParameters()[0]
    assert parameter.getName() == "BswMLogicalOperator"
    assert parameter.getParameterType() == "EcucEnumerationParamDef"
    assert [entry.getValue() for entry in parameter.getRanges()] == ["BSWM_AND", "BSWM_OR"]
    assert parameter.getDefaults() == ["BSWM_OR"]
    assert parameter.getPostBuildVariantMultiplicity() is False
    assert [(entry.getConfigClass(), entry.getValue()) for entry in parameter.getMultiplicityConfigClasses()] == [("Pre-compile time", "X"), ("Link time", "X")]
    assert parameter.getMultiplicityConfigClasses()[0].getConfigVariant() == "VARIANT-PRE-COMPILE, VARIANT-LINK-TIME, VARIANT-POST-BUILD"
    assert parameter.getMultiplicityConfigClasses()[1].getConfigVariant() == "VARIANT-LINK-TIME, VARIANT-POST-BUILD"


def test_parse_reads_choice_containers_and_headerless_included_tables():
    module = BswmEcucParser().parse(MODULE_BLOCK)

    action = module.getContainer("BswMAction")
    assert action is not None
    assert action.getContainerType() == "EcucChoiceContainerDef"
    assert action.getPostBuildVariantMultiplicity() is False
    assert [child.getName() for child in action.getIncludedContainers()] == ["BswMAvailableActions"]


def test_parse_handles_container_choices_headers_and_no_included_containers():
    module = BswmEcucParser().parse(CHOICE_HEADER_DOCUMENT)

    available = module.getContainer("BswMAvailableActions")
    assert available is not None
    assert available.getContainerType() == "EcucChoiceContainerDef"
    assert [child.getName() for child in available.getIncludedContainers()] == ["BswMClearEventRequest", "BswMComMAllowCom", "BswMComMModeLimitation", "BswMUserCallout"]

    request_port = BswmEcucParser().parse(MODULE_BLOCK).getContainer("BswMModeRequestPort")
    assert request_port is not None
    assert request_port.getIncludedContainers() == []
    reference = request_port.getReferences()[0]
    assert reference.getReferenceType() == "EcucForeignReferenceDef"
    assert reference.getTargets() == ["MODE-SWITCH-INTERFACE"]


def test_load_reads_a_markdown_file(tmp_path):
    document = tmp_path / "bswm.md"
    document.write_text(MODULE_BLOCK, encoding="utf-8")

    module = BswmEcucParser().load(str(document))

    assert module.getName() == "BswM"


def test_module_from_file_classmethod_delegates_to_the_parser(tmp_path):
    document = tmp_path / "bswm.md"
    document.write_text(MODULE_BLOCK, encoding="utf-8")

    module = BswmModule.from_file(str(document))

    assert module.getContainer("BswMConfig") is not None
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `uv run pytest tests/test_armodel/parser/test_bswm_ecuc_parser.py -v`
Expected: FAIL — `ImportError: cannot import name 'BswmEcucParser' from 'armodel.parser'`

- [ ] **Step 3: Implement the block parser and the parser facade**

In `src/armodel/parser/bswm_ecuc_parser.py`:

Replace the import block at the top with:

```python
import logging
import re
from typing import List, Optional, Tuple, Union, cast

from armodel.data_models.ecuc import BswmConfigurationClass, BswmContainer, BswmIncludedContainer, BswmModule, BswmParameter, BswmRange, BswmReference

logger = logging.getLogger("armodel.parser.bswm_ecuc_parser")
```

(`cast` is the sanctioned bridge where mypy cannot narrow a conditionally constructed
`Union[BswmParameter, BswmReference]`; it matches the convention used in the parsers.)

Then append at the end of the file:

```python
KNOWN_LABELS = {
    "SWS Item",
    "Parameter Name",
    "Parent Container",
    "Description",
    "Multiplicity",
    "Type",
    "Range",
    "Default value",
    "Post-Build Variant Multiplicity",
    "Post-Build Variant Value",
    "Multiplicity Configuration Class",
    "Value Configuration Class",
    "Scope / Dependency",
    "Regular Expression",
    "Container Name",
    "Choice Container Name",
    "Module Name",
    "Post-Build Variant Support",
    "Supported Config Variants",
    "Configuration Parameters",
}


def to_bool(text: Optional[str]) -> Optional[bool]:
    value = (text or "").strip().lower()
    if value == "true":
        return True
    if value == "false":
        return False
    return None


def split_variants(text: Optional[str]) -> List[str]:
    value = (text or "").strip()
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


class _BlockParser:
    """Turns the table rows of one 10.2.N section into a BswmContainer."""

    def __init__(self, title: str, lines: List[str]) -> None:
        self.title = title
        self.rows = collect_rows(lines)
        self.container = BswmContainer()
        self.pending_sws_item: Optional[str] = None
        self.pending_name: Optional[str] = None
        self.current: Optional[Union[BswmParameter, BswmReference]] = None
        self.provisional = False
        self.element_context = False
        self.included_mode = False
        self.post_build_variant_support: Optional[bool] = None
        self.supported_config_variants: List[str] = []

    def parse(self) -> BswmContainer:
        for row in self.rows:
            self._handle(row)
        self._finish_current()
        return self.container

    @staticmethod
    def _is_included_header(row: List[str]) -> bool:
        if len(row) < 2 or "Multiplicity" not in row:
            return False
        return any("Container Name" in cell for cell in row)

    @staticmethod
    def _is_child_row(row: List[str]) -> bool:
        if len(row) < 2 or not row[0] or row[0] in KNOWN_LABELS:
            return False
        return MULTIPLICITY_RE.match(row[1]) is not None

    def _handle(self, row: List[str]) -> None:
        label = row[0]
        cells = row[1:]

        if label == "No Included Containers":
            self.included_mode = False
            return
        if label in ("Included Containers", "Container Choices") or self._is_included_header(row):
            self.included_mode = True
            return
        if self.included_mode:
            if label not in KNOWN_LABELS:
                if self._is_child_row(row):
                    child = BswmIncludedContainer()
                    child.setName(row[0])
                    child.setMultiplicity(row[1])
                    child.setScope(first_value(row[2:]))
                    self.container.addIncludedContainer(child)
                return
            self.included_mode = False

        if label == "Configuration Parameters":
            return
        if label == "SWS Item":
            self.pending_sws_item = first_value(cells)
            return
        if label == "Module Name":
            self.container.setName(first_value(cells) or self.title)
            self.container.setSwsItem(self.pending_sws_item)
            self.container.setContainerType("EcucModuleDef")
            return
        if label == "Container Name":
            self.container.setName(first_value(cells) or self.title)
            self.container.setSwsItem(self.pending_sws_item)
            if self.container.getContainerType() is None:
                self.container.setContainerType("EcucParamConfContainerDef")
            return
        if label == "Choice Container Name":
            self.container.setName(first_value(cells) or self.title)
            self.container.setSwsItem(self.pending_sws_item)
            self.container.setContainerType("EcucChoiceContainerDef")
            return
        if label == "Parent Container":
            value = first_value(cells)
            if self.element_context and self.current is not None:
                self.current.setParent(value)
            elif not self.element_context:
                self.container.setParent(value)
            return
        if label == "Description":
            if self.element_context and self.current is not None:
                self.current.setDescription(first_value(cells))
            elif not self.element_context:
                self.container.setDescription(first_value(cells))
            return
        if label == "Post-Build Variant Support":
            self.post_build_variant_support = to_bool(first_value(cells))
            return
        if label == "Supported Config Variants":
            self.supported_config_variants.extend(split_variants(first_value(cells)))
            return
        if label == "Parameter Name":
            sws_item = self.pending_sws_item
            self._finish_current()
            self.pending_name = first_value(cells)
            provisional = BswmParameter()
            provisional.setName(self.pending_name or "")
            provisional.setSwsItem(sws_item)
            self.current = provisional
            self.provisional = True
            self.element_context = True
            return
        if label == "Type" and self.current is not None and self.provisional:
            self._create_element(first_value(cells))
            return
        if label == "Multiplicity" and self.current is not None:
            lower, upper, upper_infinite = parse_multiplicity(first_value(cells))
            self.current.setLowerMultiplicity(lower)
            self.current.setUpperMultiplicity(upper)
            self.current.setUpperMultiplicityInfinite(upper_infinite)
            return
        if label in ("Post-Build Variant Multiplicity", "Post-Build Variant Value"):
            value = to_bool(first_value(cells))
            if self.current is not None:
                if label.endswith("Multiplicity"):
                    self.current.setPostBuildVariantMultiplicity(value)
                else:
                    self.current.setPostBuildVariantValue(value)
            elif label.endswith("Multiplicity"):
                self.container.setPostBuildVariantMultiplicity(value)
            return
        if label in ("Multiplicity Configuration Class", "Value Configuration Class"):
            entry = BswmConfigurationClass()
            entry.setConfigClass(row[1] if len(row) > 1 else None)
            entry.setValue(row[2] if len(row) > 2 else None)
            variant = row[3] if len(row) > 3 else None
            entry.setConfigVariant(variant if variant else None)
            self._add_config_class(label, entry)
            return
        if label == "Range" and self.current is not None and isinstance(self.current, BswmParameter):
            value_range = BswmRange()
            value_range.setValue(row[1] if len(row) > 1 else "")
            description = row[2] if len(row) > 2 else None
            if description in (None, "", "-"):
                description = None
            value_range.setDescription(description)
            self.current.addRange(value_range)
            return
        if label == "Default value" and self.current is not None and isinstance(self.current, BswmParameter):
            value = first_value(cells)
            if value not in (None, "", "-"):
                self.current.addDefault(value)
            return
        if label == "Regular Expression" and isinstance(self.current, BswmParameter):
            self.current.setRegularExpression(first_value(cells))
            return
        if label == "Scope / Dependency" and self.current is not None:
            self.current.setScope(first_value(cells))
            return

    def _create_element(self, raw_type: Optional[str]) -> None:
        """Replace the provisional parameter by the element the Type cell classifies.

        The SWS rows put Parent Container, Description and Multiplicity before Type, so those
        fields are collected on a provisional BswmParameter first and transferred here.
        """
        kind, ecuc_class, targets = classify_type(raw_type)
        provisional = self.current
        if kind == "reference":
            element: Union[BswmParameter, BswmReference] = BswmReference()
            cast(BswmReference, element).setReferenceType(ecuc_class)
            for target in targets:
                cast(BswmReference, element).addTarget(target)
        else:
            element = BswmParameter()
            cast(BswmParameter, element).setParameterType(ecuc_class)
        if provisional is not None:
            element.setName(provisional.getName())
            element.setSwsItem(provisional.getSwsItem())
            element.setParent(provisional.getParent())
            element.setDescription(provisional.getDescription())
            element.setLowerMultiplicity(provisional.getLowerMultiplicity())
            element.setUpperMultiplicity(provisional.getUpperMultiplicity())
            element.setUpperMultiplicityInfinite(provisional.getUpperMultiplicityInfinite())
            element.setScope(provisional.getScope())
            element.setPostBuildVariantMultiplicity(provisional.getPostBuildVariantMultiplicity())
            element.setPostBuildVariantValue(provisional.getPostBuildVariantValue())
            for entry in provisional.getMultiplicityConfigClasses():
                element.addMultiplicityConfigClass(entry)
            for entry in provisional.getValueConfigClasses():
                element.addValueConfigClass(entry)
        self.current = element
        self.provisional = False

    def _add_config_class(self, label: str, entry: BswmConfigurationClass) -> None:
        if self.current is None:
            if label == "Multiplicity Configuration Class":
                self.container.addMultiplicityConfigClass(entry)
            return
        if label == "Multiplicity Configuration Class":
            self.current.addMultiplicityConfigClass(entry)
        else:
            self.current.addValueConfigClass(entry)

    def _finish_current(self) -> None:
        if isinstance(self.current, BswmParameter):
            self.container.addParameter(self.current)
        elif isinstance(self.current, BswmReference):
            self.container.addReference(self.current)
        self.current = None
        self.pending_name = None
        self.pending_sws_item = None


class BswmEcucParser:
    """Parses the ECUC configuration specification of SWS BSW Mode Manager chapter 10.2."""

    def load(self, path: str) -> BswmModule:
        with open(path, "r", encoding="utf-8") as file:
            return self.parse(file.read())

    def parse(self, text: str) -> BswmModule:
        module = BswmModule()
        for title, block_lines in split_section_blocks(extract_chapter_lines(text.splitlines())):
            block = _BlockParser(title, block_lines)
            container = block.parse()
            if container.getContainerType() == "EcucModuleDef":
                module.setName(container.getName())
                module.setPostBuildVariantSupport(block.post_build_variant_support)
                for variant in block.supported_config_variants:
                    module.addSupportedConfigVariant(variant)
            else:
                logger.debug("Parsed container %s", container.getName())
            # the module block is kept as the root entry so the workbook gets one sheet per
            # 10.2.N section, the BswM overview included
            module.addContainer(container)
        if not module.getName():
            raise BswmEcucParseError("No EcucModuleDef found in chapter 10.2")
        return module
```

Update `src/armodel/parser/__init__.py` to:

```python
from armodel.parser.arxml_parser import ARXMLParser
from armodel.parser.bswm_ecuc_parser import BswmEcucParseError, BswmEcucParser
from armodel.parser.ecuc_parser import EcucParser
from armodel.parser.file_parser import FileListParser
from armodel.parser.os_ecuc_parser import OsEcucConversionError, OsEcucParser

__all__ = ["ARXMLParser", "BswmEcucParseError", "BswmEcucParser", "EcucParser", "FileListParser", "OsEcucConversionError", "OsEcucParser"]
```

- [ ] **Step 4: Run the parser tests to verify they pass**

Run: `uv run pytest tests/test_armodel/parser/test_bswm_ecuc_parser.py -v`
Expected: 16 passed

- [ ] **Step 5: Run the model and parser tests together (from_file wiring)**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_bswm.py tests/test_armodel/parser/test_bswm_ecuc_parser.py -v`
Expected: 22 passed

- [ ] **Step 6: Commit**

```bash
git add src/armodel/parser/bswm_ecuc_parser.py src/armodel/parser/__init__.py tests/test_armodel/parser/test_bswm_ecuc_parser.py
git commit -m "feat: parse SWS BswM chapter 10.2 into the BswmModule model"
```

---

### Task 5: XLSX exporter

**Files:**
- Create: `src/armodel/report/bswm_export.py`
- Modify: `src/armodel/report/__init__.py`
- Test: `tests/test_armodel/report/test_bswm_export.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_armodel/report/test_bswm_export.py`:

```python
from pathlib import Path

from openpyxl import load_workbook

from armodel.data_models.ecuc import BswmConfigurationClass, BswmContainer, BswmIncludedContainer, BswmModule, BswmParameter, BswmRange, BswmReference
from armodel.report import BswmConfigExporter, BswmConfigXlsxExporter


def build_module() -> BswmModule:
    module = BswmModule().setName("BswM").setPostBuildVariantSupport(True)

    action = BswmContainer().setName("BswMAction").setContainerType("EcucParamConfContainerDef").setParent("BswMModeControl").setDescription("Defines an action.")
    action.addIncludedContainer(BswmIncludedContainer().setName("BswMAvailableActions").setMultiplicity("1").setScope("Choice container."))
    module.addContainer(action)

    action_list = BswmContainer().setName("BswMActionList").setContainerType("EcucParamConfContainerDef").setParent("BswMModeControl")
    parameter = BswmParameter().setName("BswMActionListIndex").setParameterType("EcucIntegerParamDef").setParent("BswMActionList").setLowerMultiplicity(0).setUpperMultiplicity(1)
    parameter.addDefault("0")
    parameter.addMultiplicityConfigClass(BswmConfigurationClass().setConfigClass("Pre-compile time").setValue("X").setConfigVariant("VARIANT-PRE-COMPILE"))
    action_list.addParameter(parameter)
    module.addContainer(action_list)

    arbitration = BswmContainer().setName("BswMArbitration").setContainerType("EcucParamConfContainerDef").setParent("BswMConfig").setSwsItem("[ECUC_BswM_00801]")
    enum = BswmParameter().setName("BswMLogicalOperator").setParameterType("EcucEnumerationParamDef").setLowerMultiplicity(0).setUpperMultiplicity(1).setSwsItem("[ECUC_BswM_00814]")
    enum.addRange(BswmRange().setValue("BSWM_AND"))
    enum.addRange(BswmRange().setValue("BSWM_OR"))
    arbitration.addParameter(enum)
    reference = BswmReference().setName("BswMPartitionRef").setReferenceType("EcucReferenceDef").addTarget("EcucPartition").setSwsItem("[ECUC_BswM_00984]")
    arbitration.addReference(reference)
    module.addContainer(arbitration)

    return module


def test_sheet_order_puts_action_and_action_list_first(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(build_module(), output)

    workbook = load_workbook(output)
    assert workbook.sheetnames == ["BswMAction", "BswMActionList", "BswMArbitration"]


def test_container_sheet_has_metadata_block_header_and_rows(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(build_module(), output)

    sheet = load_workbook(output)["BswMArbitration"]
    assert sheet.cell(row=1, column=1).value == "Container"
    assert sheet.cell(row=1, column=2).value == "BswMArbitration"
    assert sheet.cell(row=2, column=2).value == "BswMConfig"
    assert sheet.cell(row=3, column=2).value == "[ECUC_BswM_00801]"

    headers = [sheet.cell(row=6, column=column).value for column in range(1, 14)]
    assert headers[0] == "Kind"
    assert headers[5] == "Type"
    assert headers[12] == "Description"

    assert sheet.cell(row=7, column=1).value == "Parameter"
    assert sheet.cell(row=7, column=3).value == "BswMLogicalOperator"
    assert sheet.cell(row=7, column=5).value == "0..1"
    assert sheet.cell(row=7, column=7).value == "BSWM_AND\nBSWM_OR"
    assert sheet.cell(row=8, column=1).value == "Reference"
    assert sheet.cell(row=8, column=3).value == "BswMPartitionRef"
    assert "EcucReferenceDef" in sheet.cell(row=8, column=6).value
    assert "EcucPartition" in sheet.cell(row=8, column=6).value


def test_parameter_rows_render_defaults_and_config_classes(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(build_module(), output)

    sheet = load_workbook(output)["BswMActionList"]
    headers = [sheet.cell(row=6, column=column).value for column in range(1, 14)]
    assert sheet.cell(row=7, column=3).value == "BswMActionListIndex"
    assert sheet.cell(row=7, column=5).value == "0..1"
    assert sheet.cell(row=7, column=7).value == "0"
    assert sheet.cell(row=7, column=10).value == "Pre-compile time: X VARIANT-PRE-COMPILE"


def test_long_container_names_are_sanitised_to_excel_limits(tmp_path: Path):
    module = BswmModule().setName("BswM")
    module.addContainer(BswmContainer().setName("BswMSdConsumedEventGroupCurrentState"))

    output = tmp_path / "bswm.xlsx"
    BswmConfigXlsxExporter().export(module, output)

    workbook = load_workbook(output)
    assert len(workbook.sheetnames) == 1
    assert len(workbook.sheetnames[0]) <= 31
    assert workbook.sheetnames[0].startswith("BswMSdConsumedEventGroupCurrent")


def test_exporter_rejects_unsupported_extension(tmp_path: Path):
    import pytest

    with pytest.raises(ValueError, match="Unsupported BswM configuration export format"):
        BswmConfigExporter().export(build_module(), tmp_path / "bswm.json")


def test_empty_module_still_writes_a_workbook(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(BswmModule().setName("BswM"), output)

    assert output.exists()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `uv run pytest tests/test_armodel/report/test_bswm_export.py -v`
Expected: FAIL — `ImportError: cannot import name 'BswmConfigExporter'`

- [ ] **Step 3: Implement the exporter**

Create `src/armodel/report/bswm_export.py`:

```python
import os
import re
from typing import List, Optional

from openpyxl.styles import Alignment

from armodel.data_models.ecuc import BswmConfigurationClass, BswmContainer, BswmModule, BswmParameter, BswmReference
from armodel.report.excel_report import ExcelReporter

PRIORITY_CONTAINERS = ["BswMAction", "BswMActionList"]
HEADERS = ["Kind", "SWS Item", "Name", "Parent Container", "Multiplicity", "Type", "Range / Default", "Post-Build Variant Multiplicity", "Post-Build Variant Value", "Multiplicity Config Class", "Value Config Class", "Scope / Dependency", "Description"]
METADATA_ROW_COUNT = 4
HEADER_ROW = 6
INVALID_SHEET_CHARACTERS = re.compile(r"[\\/?*\[\]:]")
MAX_SHEET_NAME_LENGTH = 31
WRAP_COLUMNS = {6, 9, 10, 12}


def format_multiplicity(lower: Optional[int], upper: Optional[int], upper_infinite: Optional[bool]) -> Optional[str]:
    if lower is None and upper is None and not upper_infinite:
        return None
    if upper_infinite:
        return "%s..*" % (lower if lower is not None else 0)
    if upper is None or upper == lower:
        return str(lower) if lower is not None else None
    return "%s..%s" % (lower, upper)


def format_bool(value: Optional[bool]) -> Optional[str]:
    if value is None:
        return None
    return "true" if value else "false"


def format_config_classes(classes: List[BswmConfigurationClass]) -> Optional[str]:
    parts = []
    for entry in classes:
        text = "%s: %s" % (entry.getConfigClass(), entry.getValue() or "")
        variant = entry.getConfigVariant()
        if variant:
            text = "%s %s" % (text, variant)
        parts.append(text.strip())
    return "; ".join(parts) if parts else None


def format_parameter_type(parameter: BswmParameter) -> Optional[str]:
    return parameter.getParameterType()


def format_reference_type(reference: BswmReference) -> Optional[str]:
    if reference.getReferenceType() is None:
        return None
    if not reference.getTargets():
        return reference.getReferenceType()
    return "%s (%s)" % (reference.getReferenceType(), ", ".join(reference.getTargets()))


def format_range_default(parameter: BswmParameter) -> Optional[str]:
    values = [entry.getValue() for entry in parameter.getRanges()]
    values.extend(parameter.getDefaults())
    values = [value for value in values if value]
    return "\n".join(values) if values else None


class BswmConfigXlsxExporter(ExcelReporter):
    """Writes one worksheet per BswM container definition, BswMAction and BswMActionList first."""

    def __init__(self, priority_containers: Optional[List[str]] = None) -> None:
        super().__init__()
        self.priority_containers = priority_containers if priority_containers is not None else PRIORITY_CONTAINERS

    def export(self, module: BswmModule, output_path) -> None:
        self.wb.remove(self.wb.active)
        for container in self.ordered_containers(module):
            self.write_container_sheet(container)
        self.save(output_path)

    def ordered_containers(self, module: BswmModule) -> List[BswmContainer]:
        containers = list(module.getContainers())
        ordered: List[BswmContainer] = []
        for name in self.priority_containers:
            for container in containers:
                if container.getName() == name:
                    ordered.append(container)
        ordered.extend(container for container in containers if container.getName() not in self.priority_containers)
        return ordered

    def sheet_name(self, name: str) -> str:
        trimmed = INVALID_SHEET_CHARACTERS.sub("", name)[:MAX_SHEET_NAME_LENGTH]
        sheet_name = trimmed
        suffix = 2
        while sheet_name in self.wb.sheetnames:
            tail = str(suffix)
            sheet_name = trimmed[:MAX_SHEET_NAME_LENGTH - len(tail)] + tail
            suffix += 1
        return sheet_name

    def write_container_sheet(self, container: BswmContainer) -> None:
        sheet = self.wb.create_sheet(self.sheet_name(container.getName()))
        metadata = [("Container", container.getName()), ("Parent Container", container.getParent()), ("SWS Item", container.getSwsItem()), ("Description", container.getDescription())]
        for row_index, (label, value) in enumerate(metadata, start=1):
            self.write_cell(sheet, row_index, 1, label)
            if value not in (None, ""):
                self.write_cell(sheet, row_index, 2, value, {"alignment": Alignment(wrap_text=True)})
        for column, header in enumerate(HEADERS):
            self.write_cell(sheet, HEADER_ROW, column + 1, header)
        row = HEADER_ROW + 1
        for included in container.getIncludedContainers():
            row = self.write_row(sheet, row, "Container", included.getName(), parent=container.getName(), multiplicity=included.getMultiplicity(), scope=included.getScope())
        for parameter in container.getParameters():
            row = self.write_row(sheet, row, "Parameter", parameter.getName(), parent=parameter.getParent(), sws_item=parameter.getSwsItem(), multiplicity=format_multiplicity(parameter.getLowerMultiplicity(), parameter.getUpperMultiplicity(), parameter.getUpperMultiplicityInfinite()), element_type=format_parameter_type(parameter), range_default=format_range_default(parameter), post_build_variant_multiplicity=format_bool(parameter.getPostBuildVariantMultiplicity()), post_build_variant_value=format_bool(parameter.getPostBuildVariantValue()), multiplicity_config_classes=format_config_classes(parameter.getMultiplicityConfigClasses()), value_config_classes=format_config_classes(parameter.getValueConfigClasses()), scope=parameter.getScope(), description=parameter.getDescription())
        for reference in container.getReferences():
            row = self.write_row(sheet, row, "Reference", reference.getName(), parent=reference.getParent(), sws_item=reference.getSwsItem(), multiplicity=format_multiplicity(reference.getLowerMultiplicity(), reference.getUpperMultiplicity(), reference.getUpperMultiplicityInfinite()), element_type=format_reference_type(reference), post_build_variant_multiplicity=format_bool(reference.getPostBuildVariantMultiplicity()), post_build_variant_value=format_bool(reference.getPostBuildVariantValue()), multiplicity_config_classes=format_config_classes(reference.getMultiplicityConfigClasses()), value_config_classes=format_config_classes(reference.getValueConfigClasses()), scope=reference.getScope(), description=reference.getDescription())
        self.auto_width(sheet)

    def write_row(self, sheet, row_index: int, kind: str, name: str, parent: Optional[str] = None, sws_item: Optional[str] = None, multiplicity: Optional[str] = None, element_type: Optional[str] = None, range_default: Optional[str] = None, post_build_variant_multiplicity: Optional[str] = None, post_build_variant_value: Optional[str] = None, multiplicity_config_classes: Optional[str] = None, value_config_classes: Optional[str] = None, scope: Optional[str] = None, description: Optional[str] = None) -> int:
        values = [kind, sws_item, name, parent, multiplicity, element_type, range_default, post_build_variant_multiplicity, post_build_variant_value, multiplicity_config_classes, value_config_classes, scope, description]
        for column, value in enumerate(values):
            if value in (None, ""):
                continue
            text = str(value)
            cell_format = None
            if "\n" in text or column in WRAP_COLUMNS:
                cell_format = {"alignment": Alignment(wrap_text=True)}
            self.write_cell(sheet, row_index, column + 1, text, cell_format)
        return row_index + 1


class BswmConfigExporter:
    """Dispatches a BswmModule export by output file extension."""

    def __init__(self) -> None:
        self.exporters = {"xlsx": BswmConfigXlsxExporter()}

    def export(self, module: BswmModule, output_path) -> None:
        extension = os.path.splitext(os.fspath(output_path))[1].lower().lstrip(".")
        exporter = self.exporters.get(extension)
        if exporter is None:
            raise ValueError("Unsupported BswM configuration export format: %s" % extension)
        exporter.export(module, output_path)
```

Update `src/armodel/report/__init__.py` to:

```python
from armodel.report.bswm_export import BswmConfigExporter, BswmConfigXlsxExporter
from armodel.report.connector_xls_report import ConnectorXlsReport
from armodel.report.os_export import OsConfigExporter, OsConfigModelMapper, OsConfigXlsxExporter, OsConfigYamlExporter

__all__ = ["BswmConfigExporter", "BswmConfigXlsxExporter", "ConnectorXlsReport", "OsConfigExporter", "OsConfigModelMapper", "OsConfigXlsxExporter", "OsConfigYamlExporter"]
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `uv run pytest tests/test_armodel/report/test_bswm_export.py -v`
Expected: 6 passed

- [ ] **Step 5: Commit**

```bash
git add src/armodel/report/bswm_export.py src/armodel/report/__init__.py tests/test_armodel/report/test_bswm_export.py
git commit -m "feat: export the BswM ECUC configuration to Excel, one sheet per container"
```

---

### Task 6: CLI and console script

**Files:**
- Create: `src/armodel/cli/bswm_ecuc_export_cli.py`
- Modify: `pyproject.toml` (the `[project.scripts]` table, after `os-ecuc-export`)
- Test: `tests/test_armodel/cli/test_bswm_ecuc_export_cli.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_armodel/cli/test_bswm_ecuc_export_cli.py`:

```python
from pathlib import Path

import pytest

from armodel.cli.bswm_ecuc_export_cli import main


def test_cli_rejects_output_equal_to_input(monkeypatch, tmp_path: Path):
    input_file = tmp_path / "input.md"
    input_file.write_text("dummy")
    monkeypatch.setattr("sys.argv", ["bswm-ecuc-export", str(input_file), str(input_file)])

    with pytest.raises(ValueError, match="must not overwrite the input file"):
        main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `uv run pytest tests/test_armodel/cli/test_bswm_ecuc_export_cli.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'armodel.cli.bswm_ecuc_export_cli'`

- [ ] **Step 3: Implement the CLI**

Create `src/armodel/cli/bswm_ecuc_export_cli.py`:

```python
import argparse
import logging
import os
import sys

from armodel import __version__
from armodel.parser import BswmEcucParser
from armodel.report import BswmConfigExporter


def main():
    version = __version__

    ap = argparse.ArgumentParser()
    ap.description = "Export the BswM ECUC configuration (SWS chapter 10.2) into an Excel workbook. <%s>" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
    ap.add_argument("INPUT", help="The path of the SWS BSW Mode Manager markdown document", nargs="+")
    ap.add_argument("OUTPUT", help="The path of the output file (.xlsx)")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter("[%(levelname)s] : %(message)s")

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, "bswm_ecuc_export.log")

    if os.path.exists(log_file):
        os.remove(log_file)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)

    else:
        stdout_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        output_path = os.path.abspath(args.OUTPUT)
        input_path = os.path.abspath(args.INPUT[0])
        if output_path == input_path:
            raise ValueError("The OUTPUT file must not overwrite the input file <%s>" % args.INPUT[0])

        module = BswmEcucParser().load(args.INPUT[0])
        containers = module.getContainers()
        elements = sum(len(container.getParameters()) + len(container.getReferences()) for container in containers)
        logger.info("Parsed %d containers and %d parameters/references from <%s>", len(containers), elements, args.INPUT[0])
        BswmConfigExporter().export(module, args.OUTPUT)
        logger.info("Wrote %d container sheets to <%s>", len(containers), args.OUTPUT)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
```

In `pyproject.toml`, add to `[project.scripts]` directly after the `os-ecuc-export` line:

```toml
bswm-ecuc-export = "armodel.cli.bswm_ecuc_export_cli:main"
```

- [ ] **Step 4: Verify the console script resolves**

Run: `uv sync --extra pytest && uv run bswm-ecuc-export --help`
Expected: usage text ending with `INPUT [INPUT ...] OUTPUT`

- [ ] **Step 5: Run the test to verify it passes**

Run: `uv run pytest tests/test_armodel/cli/test_bswm_ecuc_export_cli.py -v`
Expected: 1 passed

- [ ] **Step 6: Commit**

```bash
git add src/armodel/cli/bswm_ecuc_export_cli.py pyproject.toml tests/test_armodel/cli/test_bswm_ecuc_export_cli.py
git commit -m "feat: add bswm-ecuc-export console script"
```

---

### Task 7: Integration canary over the real document

**Files:**
- Create: `tests/test_armodel/report/test_bswm_ecuc_export.py`

- [ ] **Step 1: Write the integration test**

Create `tests/test_armodel/report/test_bswm_ecuc_export.py`:

```python
from pathlib import Path

import pytest
from openpyxl import load_workbook

from armodel.data_models.ecuc import BswmModule
from armodel.report import BswmConfigXlsxExporter

REPO_ROOT = Path(__file__).resolve().parents[3]
SWS_DOCUMENT = REPO_ROOT / "autosar" / "ECUC" / "markdown" / "ModeManagement" / "AUTOSAR_CP_SWS_BSWModeManager.md"

pytestmark = pytest.mark.skipif(not SWS_DOCUMENT.exists(), reason="SWS BSW Mode Manager markdown not available")


def load_module() -> BswmModule:
    return BswmModule.from_file(str(SWS_DOCUMENT))


def test_parses_the_full_chapter_10_2():
    module = load_module()

    containers = module.getContainers()
    assert module.getName() == "BswM"
    assert module.getPostBuildVariantSupport() is True
    assert "VARIANT-PRE-COMPILE" in module.getSupportedConfigVariants()
    assert len(containers) == 91
    assert sum(len(container.getParameters()) + len(container.getReferences()) for container in containers) == 135
    assert sum(len(container.getIncludedContainers()) for container in containers) == 92


def test_top_level_structure_matches_the_specification():
    module = load_module()

    config = module.getContainer("BswMConfig")
    assert config is not None
    assert config.getParent() == "BswM"
    assert [child.getName() for child in config.getIncludedContainers()] == ["BswMArbitration", "BswMDataTypeMappingSets", "BswMModeControl"]
    assert module.getContainer("BswMGeneral").getParameters() != []

    arbitration = module.getContainer("BswMArbitration")
    assert [child.getName() for child in arbitration.getIncludedContainers()] == ["BswMEventRequestPort", "BswMLogicalExpression", "BswMModeCondition", "BswMModeRequestPort", "BswMRule"]

    control = module.getContainer("BswMModeControl")
    assert [child.getName() for child in control.getIncludedContainers()] == ["BswMAction", "BswMActionList", "BswMRteModeRequestPort", "BswMSwitchPort"]


def test_available_actions_choice_container_is_complete():
    module = load_module()

    available = module.getContainer("BswMAvailableActions")
    assert available is not None
    assert available.getContainerType() == "EcucChoiceContainerDef"
    assert len(available.getIncludedContainers()) == 34
    assert "BswMClearEventRequest" in [child.getName() for child in available.getIncludedContainers()]
    assert "BswMUserCallout" in [child.getName() for child in available.getIncludedContainers()]


def test_known_parameters_keep_their_ecuc_classification():
    module = load_module()

    config = module.getContainer("BswMConfig")
    partition_ref = config.getReferences()[0]
    assert partition_ref.getName() == "BswMPartitionRef"
    assert partition_ref.getReferenceType() == "EcucReferenceDef"
    assert partition_ref.getTargets() == ["EcucPartition"]

    general = module.getContainer("BswMGeneral")
    names = [parameter.getName() for parameter in general.getParameters()]
    assert "BswMMainFunctionPeriod" in names
    assert "BswMVersionInfoApi" in names
    period = next(parameter for parameter in general.getParameters() if parameter.getName() == "BswMMainFunctionPeriod")
    assert period.getParameterType() == "EcucFloatParamDef"


def test_workbook_has_one_sheet_per_container_with_action_first(tmp_path: Path):
    module = load_module()
    output = tmp_path / "bswm_ecuc_configuration.xlsx"

    BswmConfigXlsxExporter().export(module, output)

    workbook = load_workbook(output)
    assert workbook.sheetnames[0] == "BswMAction"
    assert workbook.sheetnames[1] == "BswMActionList"
    assert "BswM" in workbook.sheetnames
    assert len(workbook.sheetnames) == 91

    general_sheet = workbook["BswMGeneral"]
    assert general_sheet.cell(row=1, column=2).value == "BswMGeneral"
    rows = [general_sheet.cell(row=row, column=3).value for row in range(7, 30)]
    assert "BswMMainFunctionPeriod" in rows
```

- [ ] **Step 2: Run the integration test**

Run: `uv run pytest tests/test_armodel/report/test_bswm_ecuc_export.py -v`
Expected: 5 passed (if a count fails, fix the parser — do not weaken the assertion without re-measuring the document)

- [ ] **Step 3: Commit**

```bash
git add tests/test_armodel/report/test_bswm_ecuc_export.py
git commit -m "test: canary the BswM ECUC export against the real SWS chapter 10.2"
```

---

### Task 8: Quality gates and generate the workbook

**Files:**
- Generated (untracked): `out/bswm_ecuc_configuration.xlsx`

- [ ] **Step 1: Format and lint**

Run: `npm run black && npm run lint`
Expected: black rewrites nothing or only the new files; flake8/ruff/mypy all exit 0. Common fixes if mypy complains: add `Optional[...]` annotations (never `X | None`), and keep imports in `parser/__init__.py` sorted exactly as shown (circular-import order matters in this repo).

- [ ] **Step 2: Run the full test suite**

Run: `python scripts/run_tests.py`
Expected: the whole suite passes, including the pre-existing OS/exporter tests.

- [ ] **Step 3: Generate the workbook**

Run: `mkdir -p out && uv run bswm-ecuc-export autosar/ECUC/markdown/ModeManagement/AUTOSAR_CP_SWS_BSWModeManager.md out/bswm_ecuc_configuration.xlsx`
Expected: stderr shows `Parsed 91 containers and 135 parameters/references` and `Wrote 91 container sheets`.

- [ ] **Step 4: Sanity-check the workbook**

Run: `uv run python -c "from openpyxl import load_workbook; wb = load_workbook('out/bswm_ecuc_configuration.xlsx'); print(len(wb.sheetnames)); print(wb.sheetnames[:3]); print([c.value for c in wb['BswMActionList'][6]])"`
Expected: `91`, `['BswMAction', 'BswMActionList', 'BswMArbitration', ...]`, and the 13 header names starting with `Kind`.

- [ ] **Step 5: Final commit**

```bash
git status --short
git add -A src tests pyproject.toml docs
git commit -m "feat: BswM ECUC export (SWS chapter 10.2 -> xlsx)" --allow-empty
```

Leave `out/` untracked (generated artefact).
