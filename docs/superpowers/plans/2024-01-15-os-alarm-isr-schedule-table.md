# OsAlarm / OsIsr / OsScheduleTable for os-ecuc-export Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Parse `OsAlarm`, `OsIsr`, and `OsScheduleTable` ECUC containers into semantic objects and export them alongside `OsApplication`/`OsTask` in the `os-ecuc-export` tool (YAML + XLSX).

**Architecture:** Extend the existing semantic data model in `src/armodel/data_models/ecuc/os.py` with 4 new flat classes (per approved design: Option A + flat fields, all optional). Extend `OsEcucParser` with one `get_collect_*` method per entity, wired into `parseEcuc()`. Extend `OsConfigModelMapper` with one `*_to_dict` method per entity; both exporters consume `to_dict()` so YAML/XLSX pick up the new sections automatically. Cross-references between entities remain string paths (one-way, per design §5.1) — no object-resolution methods needed.

**Tech Stack:** Python 3.8+, pytest, openpyxl (XLSX), pyyaml (YAML), uv-managed venv.

**Design spec:** `docs/superpowers/specs/2024-01-15-os-alarm-isr-schedule-table-design.md`

## Global Constraints

- Type annotations MUST be Python 3.8-compatible: `typing.Optional[T]` / `typing.List[T]` — NEVER `T | None` or `list[T]`
- Setters return `self` (method chaining)
- Black formatting at 200 chars — run `npm run black` before committing
- Lint with `npm run lint` (flake8 syntax checks + ruff)
- Run tests via `uv run pytest <path> -v` (uv-managed `.venv`, Python 3.11)
- AUTOSAR property names in camelCase (`osAlarmCounterRef`), classes in PascalCase
- No code comments unless necessary; brief docstrings matching existing class style are OK
- Do NOT modify files under `src/armodel/models/M2/AUTOSARTemplates/**`, `parser/arxml_parser.py`, `writer/arxml_writer.py` import order (ruff I001 rule — not touched by this work anyway)
- Do NOT re-sort imports in any file (existing import blocks stay as-is; only add new lines in place)
- ECUC parameter names come from the AUTOSAR R23-11 spec, which differs slightly from the design draft: `OsScheduleTblExpPointOffset`, `OsScheduleTblSyncStrategy`, `OsScheduleTblExplicitPrecision`, `OsScheduleTableStartValue` (not "InitialOffset"/"AutostartValue"), and schedule-table numeric params are integers per spec (`EcucIntegerParamDef`), not floats
- `OsIsr` gains 3 fields beyond the design draft, aligned with the actual spec + existing `OsTask` pattern: `osIsrPeriod` (float, `OsIsrPeriod`), `osIsrResourceRef` (`OsIsrResourceRef`), `osMemoryMappingCodeLocationRef` (`OsMemoryMappingCodeLocationRef`)

---

### Task 1: OsAlarm data model

**Files:**
- Modify: `src/armodel/data_models/ecuc/os.py` (append class after `OsTask`, before `OsOs`)
- Modify: `src/armodel/data_models/ecuc/__init__.py`
- Modify: `src/armodel/data_models/ecuc/os.py` (`OsOs` class — add alarm collection)
- Test: `tests/test_armodel/data_models/ecuc/test_os.py`

**Interfaces:**
- Consumes: nothing (leaf model)
- Produces: `OsAlarm` class with `getName/setName`, `getOsAlarmCounterRef/setOsAlarmCounterRef`, `getOsAlarmAccessingApplications/addOsAlarmAccessingApplication`, `getOsAlarmActivateTaskRef/setOsAlarmActivateTaskRef`, `getOsAlarmSetEventTaskRef/setOsAlarmSetEventTaskRef`, `getOsAlarmSetEventRef/setOsAlarmSetEventRef`, `getOsAlarmIncrementCounterRef/setOsAlarmIncrementCounterRef`, `getOsAlarmCallbackName/setOsAlarmCallbackName`, `getOsAlarmAlarmTime/setOsAlarmAlarmTime`, `getOsAlarmAutostartType/setOsAlarmAutostartType`, `getOsAlarmCycleTime/setOsAlarmCycleTime`, `getOsAlarmAppModeRef/setOsAlarmAppModeRef`; `OsOs.getOsAlarms/addOsAlarm`; export name `OsAlarm` in `armodel.data_models.ecuc`

- [ ] **Step 1: Write the failing tests**

In `tests/test_armodel/data_models/ecuc/test_os.py`, replace the import line at the top:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsOs, OsTask
```

Append tests:

```python
def test_os_alarm_default_values():
    alarm = OsAlarm()

    assert alarm.getName() == ""
    assert alarm.getOsAlarmCounterRef() is None
    assert alarm.getOsAlarmAccessingApplications() == []
    assert alarm.getOsAlarmActivateTaskRef() is None
    assert alarm.getOsAlarmSetEventTaskRef() is None
    assert alarm.getOsAlarmSetEventRef() is None
    assert alarm.getOsAlarmIncrementCounterRef() is None
    assert alarm.getOsAlarmCallbackName() is None
    assert alarm.getOsAlarmAlarmTime() is None
    assert alarm.getOsAlarmAutostartType() is None
    assert alarm.getOsAlarmCycleTime() is None
    assert alarm.getOsAlarmAppModeRef() is None


def test_os_alarm_chained_setters_return_self():
    alarm = OsAlarm()
    result = (
        alarm.setName("Alarm1")
        .setOsAlarmCounterRef("/Os/Os/HwCounter")
        .setOsAlarmActivateTaskRef("/Os/Os/Task1")
        .setOsAlarmSetEventTaskRef("/Os/Os/Task2")
        .setOsAlarmSetEventRef("/Os/Os/Event1")
        .setOsAlarmIncrementCounterRef("/Os/Os/Counter1")
        .setOsAlarmCallbackName("AlarmCb")
        .setOsAlarmAlarmTime(1)
        .setOsAlarmAutostartType("RELATIVE")
        .setOsAlarmCycleTime(2)
        .setOsAlarmAppModeRef("/Os/Os/OSDEFAULTAPPMODE")
    )

    assert result is alarm
    assert alarm.getName() == "Alarm1"
    assert alarm.getOsAlarmCounterRef() == "/Os/Os/HwCounter"
    assert alarm.getOsAlarmActivateTaskRef() == "/Os/Os/Task1"
    assert alarm.getOsAlarmSetEventTaskRef() == "/Os/Os/Task2"
    assert alarm.getOsAlarmSetEventRef() == "/Os/Os/Event1"
    assert alarm.getOsAlarmIncrementCounterRef() == "/Os/Os/Counter1"
    assert alarm.getOsAlarmCallbackName() == "AlarmCb"
    assert alarm.getOsAlarmAlarmTime() == 1
    assert alarm.getOsAlarmAutostartType() == "RELATIVE"
    assert alarm.getOsAlarmCycleTime() == 2
    assert alarm.getOsAlarmAppModeRef() == "/Os/Os/OSDEFAULTAPPMODE"


def test_os_alarm_accessing_application_list_is_per_instance():
    first = OsAlarm().setName("A1")
    second = OsAlarm().setName("A2")
    first.addOsAlarmAccessingApplication("/Os/Os/App1")

    assert first.getOsAlarmAccessingApplications() == ["/Os/Os/App1"]
    assert second.getOsAlarmAccessingApplications() == []


def test_os_os_alarm_collection():
    alarm = OsAlarm().setName("A1")
    os_os = OsOs().setName("Os")
    other = OsOs().setName("OtherOs")

    assert os_os.addOsAlarm(alarm) is os_os

    assert os_os.getOsAlarms() == [alarm]
    assert other.getOsAlarms() == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_os.py -v -k "alarm"`
Expected: FAIL — `ImportError: cannot import name 'OsAlarm'`

- [ ] **Step 3: Implement OsAlarm and OsOs alarm collection**

In `src/armodel/data_models/ecuc/os.py`, insert after the end of the `OsTask` class (before `class OsOs`):

```python
class OsAlarm:
    """AUTOSAR OS alarm configuration as defined by SWS_Os_00114."""

    def __init__(self) -> None:
        # Short name identifying the OS alarm.
        self.name: str = ""

        # References the counter that drives the alarm.
        self.osAlarmCounterRef: Optional[str] = None

        # References the OS-Applications that have access to the alarm.
        self.osAlarmAccessingApplication: List[str] = []

        # References the task that is activated when the alarm expires (OsAlarmActivateTask action).
        self.osAlarmActivateTaskRef: Optional[str] = None

        # References the task that receives the event when the alarm expires (OsAlarmSetEvent action).
        self.osAlarmSetEventTaskRef: Optional[str] = None

        # References the event that is set when the alarm expires (OsAlarmSetEvent action).
        self.osAlarmSetEventRef: Optional[str] = None

        # References the counter that is incremented when the alarm expires (OsAlarmIncrementCounter action).
        self.osAlarmIncrementCounterRef: Optional[str] = None

        # Specifies the callback function that is called when the alarm expires (OsAlarmCallback action).
        self.osAlarmCallbackName: Optional[str] = None

        # Specifies the alarm time of the autostart alarm (ticks).
        self.osAlarmAlarmTime: Optional[int] = None

        # Specifies whether the autostart alarm is ABSOLUTE or RELATIVE.
        self.osAlarmAutostartType: Optional[str] = None

        # Specifies the cycle time of a periodic autostart alarm (ticks).
        self.osAlarmCycleTime: Optional[int] = None

        # References the application mode in which the alarm is started automatically.
        self.osAlarmAppModeRef: Optional[str] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsAlarm":
        self.name = value
        return self

    def getOsAlarmCounterRef(self) -> Optional[str]:
        return self.osAlarmCounterRef

    def setOsAlarmCounterRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmCounterRef = value
        return self

    def getOsAlarmAccessingApplications(self) -> List[str]:
        return self.osAlarmAccessingApplication

    def addOsAlarmAccessingApplication(self, value: str) -> "OsAlarm":
        self.osAlarmAccessingApplication.append(value)
        return self

    def getOsAlarmActivateTaskRef(self) -> Optional[str]:
        return self.osAlarmActivateTaskRef

    def setOsAlarmActivateTaskRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmActivateTaskRef = value
        return self

    def getOsAlarmSetEventTaskRef(self) -> Optional[str]:
        return self.osAlarmSetEventTaskRef

    def setOsAlarmSetEventTaskRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmSetEventTaskRef = value
        return self

    def getOsAlarmSetEventRef(self) -> Optional[str]:
        return self.osAlarmSetEventRef

    def setOsAlarmSetEventRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmSetEventRef = value
        return self

    def getOsAlarmIncrementCounterRef(self) -> Optional[str]:
        return self.osAlarmIncrementCounterRef

    def setOsAlarmIncrementCounterRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmIncrementCounterRef = value
        return self

    def getOsAlarmCallbackName(self) -> Optional[str]:
        return self.osAlarmCallbackName

    def setOsAlarmCallbackName(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmCallbackName = value
        return self

    def getOsAlarmAlarmTime(self) -> Optional[int]:
        return self.osAlarmAlarmTime

    def setOsAlarmAlarmTime(self, value: Optional[int]) -> "OsAlarm":
        self.osAlarmAlarmTime = value
        return self

    def getOsAlarmAutostartType(self) -> Optional[str]:
        return self.osAlarmAutostartType

    def setOsAlarmAutostartType(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmAutostartType = value
        return self

    def getOsAlarmCycleTime(self) -> Optional[int]:
        return self.osAlarmCycleTime

    def setOsAlarmCycleTime(self, value: Optional[int]) -> "OsAlarm":
        self.osAlarmCycleTime = value
        return self

    def getOsAlarmAppModeRef(self) -> Optional[str]:
        return self.osAlarmAppModeRef

    def setOsAlarmAppModeRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmAppModeRef = value
        return self
```

In the `OsOs` class, add after the `osTask` attribute declaration and before `getName`:

```python
        # Contains the semantic OS alarm objects extracted from ECUC.
        self.osAlarm: List[OsAlarm] = []
```

And add after `addOsTask` (before `from_ecuc`):

```python
    def getOsAlarms(self) -> List[OsAlarm]:
        return self.osAlarm

    def addOsAlarm(self, value: OsAlarm) -> "OsOs":
        self.osAlarm.append(value)
        return self
```

In `src/armodel/data_models/ecuc/__init__.py`, replace the whole content with:

```python
from armodel.data_models.ecuc.os import OsAlarm, OsApplication, OsOs, OsTask

__all__ = ["OsAlarm", "OsApplication", "OsOs", "OsTask"]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_os.py -v`
Expected: PASS (all tests, including pre-existing 4)

- [ ] **Step 5: Commit**

```bash
git add src/armodel/data_models/ecuc/os.py src/armodel/data_models/ecuc/__init__.py tests/test_armodel/data_models/ecuc/test_os.py
git commit -m "feat: add OsAlarm semantic data model with OsOs collection"
```

---

### Task 2: OsIsr data model

**Files:**
- Modify: `src/armodel/data_models/ecuc/os.py` (append class after `OsAlarm`)
- Modify: `src/armodel/data_models/ecuc/os.py` (`OsOs` — add ISR collection)
- Modify: `src/armodel/data_models/ecuc/__init__.py`
- Test: `tests/test_armodel/data_models/ecuc/test_os.py`

**Interfaces:**
- Consumes: nothing
- Produces: `OsIsr` class with `getName/setName`, `getOsIsrName/setOsIsrName`, `getOsIsrCategory/setOsIsrCategory`, `getOsIsrPriority/setOsIsrPriority`, `getOsIsrPeriod/setOsIsrPeriod`, `getOsIsrResourceRef/setOsIsrResourceRef`, `getOsIsrInterruptSource/setOsIsrInterruptSource`, `getOsIsrAccessingApplications/addOsIsrAccessingApplication`, `getOsMemoryMappingCodeLocationRef/setOsMemoryMappingCodeLocationRef`, `getOsIsrExecutionBudget/setOsIsrExecutionBudget`, `getOsIsrTimeFrame/setOsIsrTimeFrame`, `getOsIsrAllInterruptLockBudget/setOsIsrAllInterruptLockBudget`, `getOsIsrOsInterruptLockBudget/setOsIsrOsInterruptLockBudget`, `getOsIsrResourceLockBudgets/addOsIsrResourceLockBudget`, `getOsIsrResourceLockResourceRefs/addOsIsrResourceLockResourceRef`; `OsOs.getOsIsrs/addOsIsr`; export name `OsIsr`

- [ ] **Step 1: Write the failing tests**

Update the import in `tests/test_armodel/data_models/ecuc/test_os.py` to:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsTask
```

Append tests:

```python
def test_os_isr_default_values():
    isr = OsIsr()

    assert isr.getName() == ""
    assert isr.getOsIsrName() is None
    assert isr.getOsIsrCategory() is None
    assert isr.getOsIsrPriority() is None
    assert isr.getOsIsrPeriod() is None
    assert isr.getOsIsrResourceRef() is None
    assert isr.getOsIsrInterruptSource() is None
    assert isr.getOsIsrAccessingApplications() == []
    assert isr.getOsMemoryMappingCodeLocationRef() is None
    assert isr.getOsIsrExecutionBudget() is None
    assert isr.getOsIsrTimeFrame() is None
    assert isr.getOsIsrAllInterruptLockBudget() is None
    assert isr.getOsIsrOsInterruptLockBudget() is None
    assert isr.getOsIsrResourceLockBudgets() == []
    assert isr.getOsIsrResourceLockResourceRefs() == []


def test_os_isr_chained_setters_return_self():
    isr = OsIsr()
    result = (
        isr.setName("CanIsr")
        .setOsIsrName("CanIsrFunction")
        .setOsIsrCategory("CATEGORY_2")
        .setOsIsrPriority(5)
        .setOsIsrPeriod(0.005)
        .setOsIsrResourceRef("/Os/Os/Res1")
        .setOsIsrInterruptSource("/Os/Os/Source1")
        .setOsMemoryMappingCodeLocationRef("/Os/Os/MemRegion")
        .setOsIsrExecutionBudget(0.001)
        .setOsIsrTimeFrame(0.02)
        .setOsIsrAllInterruptLockBudget(0.0001)
        .setOsIsrOsInterruptLockBudget(0.0002)
    )

    assert result is isr
    assert isr.getName() == "CanIsr"
    assert isr.getOsIsrName() == "CanIsrFunction"
    assert isr.getOsIsrCategory() == "CATEGORY_2"
    assert isr.getOsIsrPriority() == 5
    assert isr.getOsIsrPeriod() == 0.005
    assert isr.getOsIsrResourceRef() == "/Os/Os/Res1"
    assert isr.getOsIsrInterruptSource() == "/Os/Os/Source1"
    assert isr.getOsMemoryMappingCodeLocationRef() == "/Os/Os/MemRegion"
    assert isr.getOsIsrExecutionBudget() == 0.001
    assert isr.getOsIsrTimeFrame() == 0.02
    assert isr.getOsIsrAllInterruptLockBudget() == 0.0001
    assert isr.getOsIsrOsInterruptLockBudget() == 0.0002


def test_os_isr_resource_lock_lists_are_per_instance():
    first = OsIsr().setName("ISR1")
    second = OsIsr().setName("ISR2")
    first.addOsIsrResourceLockBudget(0.0005)
    first.addOsIsrResourceLockResourceRef("/Os/Os/Res1")

    assert first.getOsIsrResourceLockBudgets() == [0.0005]
    assert first.getOsIsrResourceLockResourceRefs() == ["/Os/Os/Res1"]
    assert second.getOsIsrResourceLockBudgets() == []
    assert second.getOsIsrResourceLockResourceRefs() == []


def test_os_os_isr_collection():
    isr = OsIsr().setName("CanIsr")
    os_os = OsOs().setName("Os")

    assert os_os.addOsIsr(isr) is os_os
    assert os_os.getOsIsrs() == [isr]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_os.py -v -k "isr"`
Expected: FAIL — `ImportError: cannot import name 'OsIsr'`

- [ ] **Step 3: Implement OsIsr and OsOs ISR collection**

In `src/armodel/data_models/ecuc/os.py`, insert after the end of the `OsAlarm` class (before `class OsOs`):

```python
class OsIsr:
    """AUTOSAR OS interrupt service routine configuration as defined by SWS_Os_00128."""

    def __init__(self) -> None:
        # Short name identifying the OS ISR.
        self.name: str = ""

        # Specifies the name of the ISR function.
        self.osIsrName: Optional[str] = None

        # Specifies whether the ISR is CATEGORY_1 or CATEGORY_2.
        self.osIsrCategory: Optional[str] = None

        # Specifies the priority of the ISR.
        self.osIsrPriority: Optional[int] = None

        # Specifies the period in seconds of a cyclically triggered interrupt.
        self.osIsrPeriod: Optional[float] = None

        # References the resource that is assigned to the ISR.
        self.osIsrResourceRef: Optional[str] = None

        # References the hardware interrupt source of the ISR.
        self.osIsrInterruptSource: Optional[str] = None

        # References the OS-Applications that have access to the ISR.
        self.osIsrAccessingApplication: List[str] = []

        # Specifies the memory mapping code location of the ISR.
        self.osMemoryMappingCodeLocationRef: Optional[str] = None

        # Specifies the execution-time budget of the ISR (OsIsrTimingProtection).
        self.osIsrExecutionBudget: Optional[float] = None

        # Specifies the time frame used for ISR arrival protection (OsIsrTimingProtection).
        self.osIsrTimeFrame: Optional[float] = None

        # Specifies the maximum time for which the ISR may lock all interrupts (OsIsrTimingProtection).
        self.osIsrAllInterruptLockBudget: Optional[float] = None

        # Specifies the maximum time for which the ISR may lock OS interrupts (OsIsrTimingProtection).
        self.osIsrOsInterruptLockBudget: Optional[float] = None

        # Specifies the resource-lock budgets configured for the ISR (OsIsrResourceLock).
        self.osIsrResourceLockBudget: List[float] = []

        # References the resources associated with the resource-lock budgets.
        self.osIsrResourceLockResourceRef: List[str] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsIsr":
        self.name = value
        return self

    def getOsIsrName(self) -> Optional[str]:
        return self.osIsrName

    def setOsIsrName(self, value: Optional[str]) -> "OsIsr":
        self.osIsrName = value
        return self

    def getOsIsrCategory(self) -> Optional[str]:
        return self.osIsrCategory

    def setOsIsrCategory(self, value: Optional[str]) -> "OsIsr":
        self.osIsrCategory = value
        return self

    def getOsIsrPriority(self) -> Optional[int]:
        return self.osIsrPriority

    def setOsIsrPriority(self, value: Optional[int]) -> "OsIsr":
        self.osIsrPriority = value
        return self

    def getOsIsrPeriod(self) -> Optional[float]:
        return self.osIsrPeriod

    def setOsIsrPeriod(self, value: Optional[float]) -> "OsIsr":
        self.osIsrPeriod = value
        return self

    def getOsIsrResourceRef(self) -> Optional[str]:
        return self.osIsrResourceRef

    def setOsIsrResourceRef(self, value: Optional[str]) -> "OsIsr":
        self.osIsrResourceRef = value
        return self

    def getOsIsrInterruptSource(self) -> Optional[str]:
        return self.osIsrInterruptSource

    def setOsIsrInterruptSource(self, value: Optional[str]) -> "OsIsr":
        self.osIsrInterruptSource = value
        return self

    def getOsIsrAccessingApplications(self) -> List[str]:
        return self.osIsrAccessingApplication

    def addOsIsrAccessingApplication(self, value: str) -> "OsIsr":
        self.osIsrAccessingApplication.append(value)
        return self

    def getOsMemoryMappingCodeLocationRef(self) -> Optional[str]:
        return self.osMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value: Optional[str]) -> "OsIsr":
        self.osMemoryMappingCodeLocationRef = value
        return self

    def getOsIsrExecutionBudget(self) -> Optional[float]:
        return self.osIsrExecutionBudget

    def setOsIsrExecutionBudget(self, value: Optional[float]) -> "OsIsr":
        self.osIsrExecutionBudget = value
        return self

    def getOsIsrTimeFrame(self) -> Optional[float]:
        return self.osIsrTimeFrame

    def setOsIsrTimeFrame(self, value: Optional[float]) -> "OsIsr":
        self.osIsrTimeFrame = value
        return self

    def getOsIsrAllInterruptLockBudget(self) -> Optional[float]:
        return self.osIsrAllInterruptLockBudget

    def setOsIsrAllInterruptLockBudget(self, value: Optional[float]) -> "OsIsr":
        self.osIsrAllInterruptLockBudget = value
        return self

    def getOsIsrOsInterruptLockBudget(self) -> Optional[float]:
        return self.osIsrOsInterruptLockBudget

    def setOsIsrOsInterruptLockBudget(self, value: Optional[float]) -> "OsIsr":
        self.osIsrOsInterruptLockBudget = value
        return self

    def getOsIsrResourceLockBudgets(self) -> List[float]:
        return self.osIsrResourceLockBudget

    def addOsIsrResourceLockBudget(self, value: float) -> "OsIsr":
        self.osIsrResourceLockBudget.append(value)
        return self

    def getOsIsrResourceLockResourceRefs(self) -> List[str]:
        return self.osIsrResourceLockResourceRef

    def addOsIsrResourceLockResourceRef(self, value: str) -> "OsIsr":
        self.osIsrResourceLockResourceRef.append(value)
        return self
```

In the `OsOs` class, add after the `osAlarm` attribute declaration:

```python
        # Contains the semantic OS ISR objects extracted from ECUC.
        self.osIsr: List[OsIsr] = []
```

And add after `addOsAlarm` (before `from_ecuc`):

```python
    def getOsIsrs(self) -> List[OsIsr]:
        return self.osIsr

    def addOsIsr(self, value: OsIsr) -> "OsOs":
        self.osIsr.append(value)
        return self
```

In `src/armodel/data_models/ecuc/__init__.py`, replace the whole content with:

```python
from armodel.data_models.ecuc.os import OsAlarm, OsApplication, OsIsr, OsOs, OsTask

__all__ = ["OsAlarm", "OsApplication", "OsIsr", "OsOs", "OsTask"]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_os.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/armodel/data_models/ecuc/os.py src/armodel/data_models/ecuc/__init__.py tests/test_armodel/data_models/ecuc/test_os.py
git commit -m "feat: add OsIsr semantic data model with OsOs collection"
```

---

### Task 3: OsScheduleTableExpiryPoint and OsScheduleTable data models

**Files:**
- Modify: `src/armodel/data_models/ecuc/os.py` (append both classes after `OsIsr`)
- Modify: `src/armodel/data_models/ecuc/os.py` (`OsOs` — add schedule table collection)
- Modify: `src/armodel/data_models/ecuc/__init__.py`
- Test: `tests/test_armodel/data_models/ecuc/test_os.py`

**Interfaces:**
- Consumes: nothing
- Produces: `OsScheduleTableExpiryPoint` with `getOsScheduleTableExpiryPointOffset/setOsScheduleTableExpiryPointOffset`, `getOsScheduleTableMaxShorten/setOsScheduleTableMaxShorten`, `getOsScheduleTableMaxLengthen/setOsScheduleTableMaxLengthen`, `getOsScheduleTableActivateTaskRef/setOsScheduleTableActivateTaskRef`, `getOsScheduleTableSetEventTaskRef/setOsScheduleTableSetEventTaskRef`, `getOsScheduleTableSetEventRef/setOsScheduleTableSetEventRef`; `OsScheduleTable` with `getName/setName`, `getOsScheduleTableCounterRef/setOsScheduleTableCounterRef`, `getOsScheduleTableDuration/setOsScheduleTableDuration`, `getOsScheduleTableRepeating/setOsScheduleTableRepeating`, `getOsScheduleTableAccessingApplications/addOsScheduleTableAccessingApplication`, `getOsScheduleTableExpiryPoints/addOsScheduleTableExpiryPoint`, `getOsScheduleTableAutostartType/setOsScheduleTableAutostartType`, `getOsScheduleTableStartValue/setOsScheduleTableStartValue`, `getOsScheduleTableAppModeRef/setOsScheduleTableAppModeRef`, `getOsScheduleTableSyncStrategy/setOsScheduleTableSyncStrategy`, `getOsScheduleTableExplicitPrecision/setOsScheduleTableExplicitPrecision`; `OsOs.getOsScheduleTables/addOsScheduleTable`

- [ ] **Step 1: Write the failing tests**

Update the import in `tests/test_armodel/data_models/ecuc/test_os.py` to:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask
```

Append tests:

```python
def test_os_schedule_table_expiry_point_default_values_and_setters():
    expiry_point = OsScheduleTableExpiryPoint()

    assert expiry_point.getOsScheduleTableExpiryPointOffset() is None
    assert expiry_point.getOsScheduleTableMaxShorten() is None
    assert expiry_point.getOsScheduleTableMaxLengthen() is None
    assert expiry_point.getOsScheduleTableActivateTaskRef() is None
    assert expiry_point.getOsScheduleTableSetEventTaskRef() is None
    assert expiry_point.getOsScheduleTableSetEventRef() is None

    assert (
        expiry_point.setOsScheduleTableExpiryPointOffset(2)
        .setOsScheduleTableMaxShorten(1)
        .setOsScheduleTableMaxLengthen(1)
        .setOsScheduleTableActivateTaskRef("/Os/Os/Task1")
        .setOsScheduleTableSetEventTaskRef("/Os/Os/Task2")
        .setOsScheduleTableSetEventRef("/Os/Os/Event1")
        is expiry_point
    )

    assert expiry_point.getOsScheduleTableExpiryPointOffset() == 2
    assert expiry_point.getOsScheduleTableMaxShorten() == 1
    assert expiry_point.getOsScheduleTableMaxLengthen() == 1
    assert expiry_point.getOsScheduleTableActivateTaskRef() == "/Os/Os/Task1"
    assert expiry_point.getOsScheduleTableSetEventTaskRef() == "/Os/Os/Task2"
    assert expiry_point.getOsScheduleTableSetEventRef() == "/Os/Os/Event1"


def test_os_schedule_table_default_values():
    schedule_table = OsScheduleTable()

    assert schedule_table.getName() == ""
    assert schedule_table.getOsScheduleTableCounterRef() is None
    assert schedule_table.getOsScheduleTableDuration() is None
    assert schedule_table.getOsScheduleTableRepeating() is None
    assert schedule_table.getOsScheduleTableAccessingApplications() == []
    assert schedule_table.getOsScheduleTableExpiryPoints() == []
    assert schedule_table.getOsScheduleTableAutostartType() is None
    assert schedule_table.getOsScheduleTableStartValue() is None
    assert schedule_table.getOsScheduleTableAppModeRef() is None
    assert schedule_table.getOsScheduleTableSyncStrategy() is None
    assert schedule_table.getOsScheduleTableExplicitPrecision() is None


def test_os_schedule_table_chained_setters_return_self():
    schedule_table = OsScheduleTable()
    first = OsScheduleTableExpiryPoint().setOsScheduleTableExpiryPointOffset(2)
    second = OsScheduleTableExpiryPoint().setOsScheduleTableExpiryPointOffset(5)
    result = (
        schedule_table.setName("Table1")
        .setOsScheduleTableCounterRef("/Os/Os/HwCounter")
        .setOsScheduleTableDuration(10)
        .setOsScheduleTableRepeating(True)
        .setOsScheduleTableAutostartType("RELATIVE")
        .setOsScheduleTableStartValue(0)
        .setOsScheduleTableAppModeRef("/Os/Os/OSDEFAULTAPPMODE")
        .setOsScheduleTableSyncStrategy("IMPLICIT")
        .setOsScheduleTableExplicitPrecision(0)
    )

    assert result is schedule_table
    assert schedule_table.addOsScheduleTableAccessingApplication("/Os/Os/App1") is schedule_table
    assert schedule_table.addOsScheduleTableExpiryPoint(first) is schedule_table
    schedule_table.addOsScheduleTableExpiryPoint(second)

    assert schedule_table.getName() == "Table1"
    assert schedule_table.getOsScheduleTableCounterRef() == "/Os/Os/HwCounter"
    assert schedule_table.getOsScheduleTableDuration() == 10
    assert schedule_table.getOsScheduleTableRepeating() is True
    assert schedule_table.getOsScheduleTableAccessingApplications() == ["/Os/Os/App1"]
    assert schedule_table.getOsScheduleTableExpiryPoints() == [first, second]
    assert schedule_table.getOsScheduleTableAutostartType() == "RELATIVE"
    assert schedule_table.getOsScheduleTableStartValue() == 0
    assert schedule_table.getOsScheduleTableAppModeRef() == "/Os/Os/OSDEFAULTAPPMODE"
    assert schedule_table.getOsScheduleTableSyncStrategy() == "IMPLICIT"
    assert schedule_table.getOsScheduleTableExplicitPrecision() == 0


def test_os_os_schedule_table_collection():
    schedule_table = OsScheduleTable().setName("Table1")
    os_os = OsOs().setName("Os")

    assert os_os.addOsScheduleTable(schedule_table) is os_os
    assert os_os.getOsScheduleTables() == [schedule_table]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_os.py -v -k "schedule_table"`
Expected: FAIL — `ImportError: cannot import name 'OsScheduleTable'`

- [ ] **Step 3: Implement the classes and OsOs collection**

In `src/armodel/data_models/ecuc/os.py`, insert after the end of the `OsIsr` class (before `class OsOs`):

```python
class OsScheduleTableExpiryPoint:
    """AUTOSAR OS schedule table expiry point configuration as defined by SWS_Os_00235."""

    def __init__(self) -> None:
        # Specifies the offset of the expiry point (counter ticks).
        self.osScheduleTableExpiryPointOffset: Optional[int] = None

        # Specifies the maximum number of ticks that can be subtracted from the expiry point offset.
        self.osScheduleTableMaxShorten: Optional[int] = None

        # Specifies the maximum number of ticks that can be added to the expiry point offset.
        self.osScheduleTableMaxLengthen: Optional[int] = None

        # References the task that is activated at the expiry point (OsScheduleTableTaskActivation).
        self.osScheduleTableActivateTaskRef: Optional[str] = None

        # References the task that receives the event at the expiry point (OsScheduleTableEventSetting).
        self.osScheduleTableSetEventTaskRef: Optional[str] = None

        # References the event that is set at the expiry point (OsScheduleTableEventSetting).
        self.osScheduleTableSetEventRef: Optional[str] = None

    def getOsScheduleTableExpiryPointOffset(self) -> Optional[int]:
        return self.osScheduleTableExpiryPointOffset

    def setOsScheduleTableExpiryPointOffset(self, value: Optional[int]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableExpiryPointOffset = value
        return self

    def getOsScheduleTableMaxShorten(self) -> Optional[int]:
        return self.osScheduleTableMaxShorten

    def setOsScheduleTableMaxShorten(self, value: Optional[int]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableMaxShorten = value
        return self

    def getOsScheduleTableMaxLengthen(self) -> Optional[int]:
        return self.osScheduleTableMaxLengthen

    def setOsScheduleTableMaxLengthen(self, value: Optional[int]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableMaxLengthen = value
        return self

    def getOsScheduleTableActivateTaskRef(self) -> Optional[str]:
        return self.osScheduleTableActivateTaskRef

    def setOsScheduleTableActivateTaskRef(self, value: Optional[str]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableActivateTaskRef = value
        return self

    def getOsScheduleTableSetEventTaskRef(self) -> Optional[str]:
        return self.osScheduleTableSetEventTaskRef

    def setOsScheduleTableSetEventTaskRef(self, value: Optional[str]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableSetEventTaskRef = value
        return self

    def getOsScheduleTableSetEventRef(self) -> Optional[str]:
        return self.osScheduleTableSetEventRef

    def setOsScheduleTableSetEventRef(self, value: Optional[str]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableSetEventRef = value
        return self


class OsScheduleTable:
    """AUTOSAR OS schedule table configuration as defined by SWS_Os_00232."""

    def __init__(self) -> None:
        # Short name identifying the OS schedule table.
        self.name: str = ""

        # References the counter that drives the schedule table.
        self.osScheduleTableCounterRef: Optional[str] = None

        # Specifies the duration of the schedule table (counter ticks).
        self.osScheduleTableDuration: Optional[int] = None

        # Specifies whether the schedule table is repeated after completion.
        self.osScheduleTableRepeating: Optional[bool] = None

        # References the OS-Applications that have access to the schedule table.
        self.osScheduleTableAccessingApplication: List[str] = []

        # Contains the expiry points of the schedule table in configuration order.
        self.osScheduleTableExpiryPoint: List[OsScheduleTableExpiryPoint] = []

        # Specifies whether the autostart schedule table is ABSOLUTE or RELATIVE.
        self.osScheduleTableAutostartType: Optional[str] = None

        # Specifies the absolute tick value or relative offset when the schedule table starts.
        self.osScheduleTableStartValue: Optional[int] = None

        # References the application mode in which the schedule table is started automatically.
        self.osScheduleTableAppModeRef: Optional[str] = None

        # Specifies the synchronization strategy (NONE, IMPLICIT, or EXPLICIT).
        self.osScheduleTableSyncStrategy: Optional[str] = None

        # Specifies the maximum adjustment for explicit synchronization (counter ticks).
        self.osScheduleTableExplicitPrecision: Optional[int] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsScheduleTable":
        self.name = value
        return self

    def getOsScheduleTableCounterRef(self) -> Optional[str]:
        return self.osScheduleTableCounterRef

    def setOsScheduleTableCounterRef(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableCounterRef = value
        return self

    def getOsScheduleTableDuration(self) -> Optional[int]:
        return self.osScheduleTableDuration

    def setOsScheduleTableDuration(self, value: Optional[int]) -> "OsScheduleTable":
        self.osScheduleTableDuration = value
        return self

    def getOsScheduleTableRepeating(self) -> Optional[bool]:
        return self.osScheduleTableRepeating

    def setOsScheduleTableRepeating(self, value: Optional[bool]) -> "OsScheduleTable":
        self.osScheduleTableRepeating = value
        return self

    def getOsScheduleTableAccessingApplications(self) -> List[str]:
        return self.osScheduleTableAccessingApplication

    def addOsScheduleTableAccessingApplication(self, value: str) -> "OsScheduleTable":
        self.osScheduleTableAccessingApplication.append(value)
        return self

    def getOsScheduleTableExpiryPoints(self) -> List[OsScheduleTableExpiryPoint]:
        return self.osScheduleTableExpiryPoint

    def addOsScheduleTableExpiryPoint(self, value: OsScheduleTableExpiryPoint) -> "OsScheduleTable":
        self.osScheduleTableExpiryPoint.append(value)
        return self

    def getOsScheduleTableAutostartType(self) -> Optional[str]:
        return self.osScheduleTableAutostartType

    def setOsScheduleTableAutostartType(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableAutostartType = value
        return self

    def getOsScheduleTableStartValue(self) -> Optional[int]:
        return self.osScheduleTableStartValue

    def setOsScheduleTableStartValue(self, value: Optional[int]) -> "OsScheduleTable":
        self.osScheduleTableStartValue = value
        return self

    def getOsScheduleTableAppModeRef(self) -> Optional[str]:
        return self.osScheduleTableAppModeRef

    def setOsScheduleTableAppModeRef(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableAppModeRef = value
        return self

    def getOsScheduleTableSyncStrategy(self) -> Optional[str]:
        return self.osScheduleTableSyncStrategy

    def setOsScheduleTableSyncStrategy(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableSyncStrategy = value
        return self

    def getOsScheduleTableExplicitPrecision(self) -> Optional[int]:
        return self.osScheduleTableExplicitPrecision

    def setOsScheduleTableExplicitPrecision(self, value: Optional[int]) -> "OsScheduleTable":
        self.osScheduleTableExplicitPrecision = value
        return self
```

In the `OsOs` class, add after the `osIsr` attribute declaration:

```python
        # Contains the semantic OS schedule table objects extracted from ECUC.
        self.osScheduleTable: List[OsScheduleTable] = []
```

And add after `addOsIsr` (before `from_ecuc`):

```python
    def getOsScheduleTables(self) -> List[OsScheduleTable]:
        return self.osScheduleTable

    def addOsScheduleTable(self, value: OsScheduleTable) -> "OsOs":
        self.osScheduleTable.append(value)
        return self
```

In `src/armodel/data_models/ecuc/__init__.py`, replace the whole content with:

```python
from armodel.data_models.ecuc.os import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask

__all__ = ["OsAlarm", "OsApplication", "OsIsr", "OsOs", "OsScheduleTable", "OsScheduleTableExpiryPoint", "OsTask"]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/data_models/ecuc/test_os.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/armodel/data_models/ecuc/os.py src/armodel/data_models/ecuc/__init__.py tests/test_armodel/data_models/ecuc/test_os.py
git commit -m "feat: add OsScheduleTable and OsScheduleTableExpiryPoint semantic data models"
```

---

### Task 4: Parser — collect OsAlarm

**Files:**
- Modify: `src/armodel/parser/os_ecuc_parser.py` (import + new method + `parseEcuc` wiring)
- Test: `tests/test_armodel/parser/test_os_ecuc_parser.py`

**Interfaces:**
- Consumes: `OsAlarm` from Task 1; base helpers `get_parameter_values`, `get_reference_values`, `get_sub_containers_by_name`, `get_definition_name`, `get_raw_value`, `get_check_reference_path`, `get_bool`, `get_int`, `get_str` on `OsEcucParser`
- Produces: `OsEcucParser.get_collect_alarm(alarm: OsAlarm, container: Container, index: Dict[str, Container], warning: bool) -> None`; `parseEcuc()` now returns an `OsOs` whose `getOsAlarms()` is populated for `OsAlarm` containers. Reuses the module-local test helpers `_container`, `_int_parameter`, `_reference`, `_build_document` already defined in the test file.

ECUC mapping handled by this task:
- OsAlarm parameters: `OsAlarmCallbackName` (string)
- OsAlarm references: `OsAlarmCounterRef`, `OsAlarmAccessingApplication` (multi)
- `OsAlarmAutostart` sub-container: params `OsAlarmAlarmTime` (int), `OsAlarmAutostartType` (str), `OsAlarmCycleTime` (int); ref `OsAlarmAppModeRef`
- Alarm action sub-containers (choice container may appear under any of the 4 concrete definition names `OsAlarmActivateTask`, `OsAlarmCallback`, `OsAlarmIncrementCounter`, `OsAlarmSetEvent` — the test fixture uses short-name `OsAlarmAction` with a concrete definition-ref, so `get_sub_containers_by_name` keys it by the definition name, e.g. `OsAlarmIncrementCounter`): refs `OsAlarmActivateTaskRef`, `OsAlarmSetEventTaskRef`, `OsAlarmSetEventRef`, `OsAlarmIncrementCounterRef`; param `OsAlarmCallbackName`

- [ ] **Step 1: Write the failing tests**

In `tests/test_armodel/parser/test_os_ecuc_parser.py`, update the data-model import at the top:

```python
from armodel.data_models.ecuc import OsAlarm, OsOs
```

Append tests:

```python
def _alarm_action_container(definition_name, references=()):
    return _container("OsAlarmAction", "OsAlarmAction/" + definition_name, references=references)


def test_collect_alarm_with_autostart_and_increment_counter_action():
    alarm_container = _container(
        "Alarm1",
        "OsAlarm",
        references=[_reference("OsAlarmCounterRef", "/Os/Os/HwCounter")],
        sub_containers=[
            _container(
                "OsAlarmAutostart",
                "OsAlarmAutostart",
                parameters=[
                    _int_parameter("OsAlarmAlarmTime", 1),
                    _enum_parameter("OsAlarmAutostartType", "RELATIVE"),
                    _int_parameter("OsAlarmCycleTime", 2),
                ],
                references=[_reference("OsAlarmAppModeRef", "/Os/Os/OSDEFAULTAPPMODE")],
            ),
            _alarm_action_container("OsAlarmIncrementCounter", references=[_reference("OsAlarmIncrementCounterRef", "/Os/Os/Rte_Counter")]),
        ],
    )
    containers = [
        _container("HwCounter", "OsCounter"),
        _container("Rte_Counter", "OsCounter"),
        _container("OSDEFAULTAPPMODE", "OsAppMode"),
        alarm_container,
    ]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document)

    alarm = result.getOsAlarms()[0]
    assert alarm.getName() == "Alarm1"
    assert alarm.getOsAlarmCounterRef() == "/Os/Os/HwCounter"
    assert alarm.getOsAlarmAlarmTime() == 1
    assert alarm.getOsAlarmAutostartType() == "RELATIVE"
    assert alarm.getOsAlarmCycleTime() == 2
    assert alarm.getOsAlarmAppModeRef() == "/Os/Os/OSDEFAULTAPPMODE"
    assert alarm.getOsAlarmIncrementCounterRef() == "/Os/Os/Rte_Counter"


def test_collect_alarm_with_set_event_activate_task_and_callback_actions():
    set_event_container = _container(
        "Alarm2",
        "OsAlarm",
        sub_containers=[
            _alarm_action_container(
                "OsAlarmSetEvent",
                references=[
                    _reference("OsAlarmSetEventTaskRef", "/Os/Os/Task1"),
                    _reference("OsAlarmSetEventRef", "/Os/Os/Event1"),
                ],
            )
        ],
    )
    activate_task_container = _container(
        "Alarm3",
        "OsAlarm",
        sub_containers=[_alarm_action_container("OsAlarmActivateTask", references=[_reference("OsAlarmActivateTaskRef", "/Os/Os/Task1")])],
    )
    callback_container = _container(
        "Alarm4",
        "OsAlarm",
        sub_containers=[_alarm_action_container("OsAlarmCallback", parameters=[_string_parameter("OsAlarmCallbackName", "AlarmCb")])],
    )
    containers = [
        _container("Task1", "OsTask"),
        _container("Event1", "OsEvent"),
        set_event_container,
        activate_task_container,
        callback_container,
    ]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document)

    alarms = {alarm.getName(): alarm for alarm in result.getOsAlarms()}
    assert alarms["Alarm2"].getOsAlarmSetEventTaskRef() == "/Os/Os/Task1"
    assert alarms["Alarm2"].getOsAlarmSetEventRef() == "/Os/Os/Event1"
    assert alarms["Alarm3"].getOsAlarmActivateTaskRef() == "/Os/Os/Task1"
    assert alarms["Alarm4"].getOsAlarmCallbackName() == "AlarmCb"


def test_collect_alarm_unresolved_counter_ref_raises_in_strict_mode():
    containers = [_container("Alarm5", "OsAlarm", references=[_reference("OsAlarmCounterRef", "/Os/Os/MissingCounter")])]
    document = _build_document(containers)

    with pytest.raises(OsEcucConversionError, match="MissingCounter"):
        OsEcucParser().parseEcuc(document)


def test_collect_alarm_accessing_application_collected_as_path():
    containers = [
        _container("App1", "OsApplication"),
        _container("Alarm6", "OsAlarm", references=[_reference("OsAlarmAccessingApplication", "/Os/Os/App1")]),
    ]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document)

    assert result.getOsAlarms()[0].getOsAlarmAccessingApplications() == ["/Os/Os/App1"]
```

Note: the parameter helpers in the existing test file build definition-refs ending in `/TS/Os/OsTask/<name>`; the parser only reads the trailing definition name, so reusing them for alarm parameters is safe.

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/parser/test_os_ecuc_parser.py -v -k "collect_alarm"`
Expected: FAIL — `AttributeError: 'OsEcucParser' object has no attribute 'get_collect_alarm'` (and `getOsAlarms` returns `[]` so index errors occur)

- [ ] **Step 3: Implement get_collect_alarm and wire into parseEcuc**

In `src/armodel/parser/os_ecuc_parser.py`, update the import:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsOs, OsTask
```

Add the new method after `get_lookup_application` (before `get_collect_task`):

```python
    def get_collect_alarm(self, alarm: OsAlarm, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            raw = self.get_raw_value(parameter)
            if name == "OsAlarmCallbackName":
                alarm.setOsAlarmCallbackName(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsAlarm parameter %s" % name)

        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
            if name == "OsAlarmCounterRef":
                alarm.setOsAlarmCounterRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsAlarmAccessingApplication":
                alarm.addOsAlarmAccessingApplication(self.get_check_reference_path(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsAlarm reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for autostart in sub_containers.get("OsAlarmAutostart", []):
            for parameter in self.get_parameter_values(autostart):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsAlarmAlarmTime":
                    alarm.setOsAlarmAlarmTime(self.get_int(name, raw))
                elif name == "OsAlarmAutostartType":
                    alarm.setOsAlarmAutostartType(self.get_str(name, raw))
                elif name == "OsAlarmCycleTime":
                    alarm.setOsAlarmCycleTime(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAutostart parameter %s" % name)
            for reference in self.get_reference_values(autostart):
                name = self.get_definition_name(reference.getDefinitionRef())
                value_ref = reference.getValueRef()
                if value_ref is None or value_ref.getValue() is None:
                    continue
                path = value_ref.getValue().strip()
                if name == "OsAlarmAppModeRef":
                    alarm.setOsAlarmAppModeRef(self.get_check_reference_path(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAutostart reference %s" % name)

        action_containers = []
        for choice in ("OsAlarmActivateTask", "OsAlarmCallback", "OsAlarmIncrementCounter", "OsAlarmSetEvent"):
            action_containers.extend(sub_containers.get(choice, []))
        for action in action_containers:
            for reference in self.get_reference_values(action):
                name = self.get_definition_name(reference.getDefinitionRef())
                value_ref = reference.getValueRef()
                if value_ref is None or value_ref.getValue() is None:
                    continue
                path = value_ref.getValue().strip()
                if name == "OsAlarmActivateTaskRef":
                    alarm.setOsAlarmActivateTaskRef(self.get_check_reference_path(name, path, index, warning))
                elif name == "OsAlarmSetEventTaskRef":
                    alarm.setOsAlarmSetEventTaskRef(self.get_check_reference_path(name, path, index, warning))
                elif name == "OsAlarmSetEventRef":
                    alarm.setOsAlarmSetEventRef(self.get_check_reference_path(name, path, index, warning))
                elif name == "OsAlarmIncrementCounterRef":
                    alarm.setOsAlarmIncrementCounterRef(self.get_check_reference_path(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAction reference %s" % name)
            for parameter in self.get_parameter_values(action):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsAlarmCallbackName":
                    alarm.setOsAlarmCallbackName(self.get_str(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAction parameter %s" % name)
```

In `parseEcuc`, after the applications collection loop (`applications[path] = application` / `os_os.addOsApplication(application)`) and before the `get_resolve_task_objects` loop, add:

```python
        alarms: Dict[str, OsAlarm] = {}
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsAlarm":
                alarm = OsAlarm()
                alarm.setName(container.getShortName())
                self.logger.info("Parsing OsAlarm: %s", alarm.getName())
                self.get_collect_alarm(alarm, container, index, warning)
                alarms[path] = alarm
                os_os.addOsAlarm(alarm)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/parser/test_os_ecuc_parser.py -v`
Expected: PASS (new + all pre-existing parser tests)

- [ ] **Step 5: Commit**

```bash
git add src/armodel/parser/os_ecuc_parser.py tests/test_armodel/parser/test_os_ecuc_parser.py
git commit -m "feat: parse OsAlarm containers into semantic OsAlarm objects"
```

---

### Task 5: Parser — collect OsIsr

**Files:**
- Modify: `src/armodel/parser/os_ecuc_parser.py` (import + new method + `parseEcuc` wiring)
- Test: `tests/test_armodel/parser/test_os_ecuc_parser.py`

**Interfaces:**
- Consumes: `OsIsr` from Task 2; base helpers as Task 4 plus `get_float`
- Produces: `OsEcucParser.get_collect_isr(isr: OsIsr, container: Container, index: Dict[str, Container], warning: bool) -> None`; `parseEcuc()` populates `getOsIsrs()`

ECUC mapping handled by this task:
- OsIsr parameters: `OsIsrCategory` (str), `OsIsrPeriod` (float), `OsIsrPriority` (int), `OsIsrName` (str)
- OsIsr references: `OsIsrResourceRef`, `OsIsrInterruptSource`, `OsIsrAccessingApplication` (multi), `OsMemoryMappingCodeLocationRef`
- `OsIsrTimingProtection` sub-container: params `OsIsrExecutionBudget`, `OsIsrTimeFrame`, `OsIsrAllInterruptLockBudget`, `OsIsrOsInterruptLockBudget` (floats)
- `OsIsrResourceLock` sub-sub-container: param `OsIsrResourceLockBudget` (float, multi); ref `OsIsrResourceLockResourceRef` (multi)

- [ ] **Step 1: Write the failing tests**

In `tests/test_armodel/parser/test_os_ecuc_parser.py`, update the data-model import:

```python
from armodel.data_models.ecuc import OsAlarm, OsIsr, OsOs
```

Append tests:

```python
def test_collect_isr_with_timing_protection_and_resource_lock():
    isr_container = _container(
        "CanIsr",
        "OsIsr",
        parameters=[
            _enum_parameter("OsIsrCategory", "CATEGORY_2"),
            _float_parameter("OsIsrPeriod", 0.005),
        ],
        references=[_reference("OsIsrResourceRef", "/Os/Os/OsStackResource")],
        sub_containers=[
            _container(
                "OsIsrTimingProtection",
                "OsIsrTimingProtection",
                parameters=[
                    _float_parameter("OsIsrExecutionBudget", 0.001),
                    _float_parameter("OsIsrTimeFrame", 0.02),
                ],
                sub_containers=[
                    _container(
                        "OsIsrResourceLock",
                        "OsIsrResourceLock",
                        parameters=[_float_parameter("OsIsrResourceLockBudget", 0.0005)],
                        references=[_reference("OsIsrResourceLockResourceRef", "/Os/Os/OsStackResource")],
                    )
                ],
            )
        ],
    )
    containers = [_container("OsStackResource", "OsResource"), isr_container]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document)

    isr = result.getOsIsrs()[0]
    assert isr.getName() == "CanIsr"
    assert isr.getOsIsrCategory() == "CATEGORY_2"
    assert isr.getOsIsrPeriod() == 0.005
    assert isr.getOsIsrResourceRef() == "/Os/Os/OsStackResource"
    assert isr.getOsIsrExecutionBudget() == 0.001
    assert isr.getOsIsrTimeFrame() == 0.02
    assert isr.getOsIsrResourceLockBudgets() == [0.0005]
    assert isr.getOsIsrResourceLockResourceRefs() == ["/Os/Os/OsStackResource"]


def test_collect_isr_with_lock_budgets_and_accessing_applications():
    isr_container = _container(
        "IscIsr",
        "OsIsr",
        parameters=[_enum_parameter("OsIsrCategory", "CATEGORY_1"), _int_parameter("OsIsrPriority", 3)],
        references=[
            _reference("OsIsrAccessingApplication", "/Os/Os/App1"),
            _reference("OsIsrAccessingApplication", "/Os/Os/App2"),
            _reference("OsMemoryMappingCodeLocationRef", "/Os/Os/MemRegion1"),
        ],
        sub_containers=[
            _container(
                "OsIsrTimingProtection",
                "OsIsrTimingProtection",
                parameters=[
                    _float_parameter("OsIsrAllInterruptLockBudget", 0.0001),
                    _float_parameter("OsIsrOsInterruptLockBudget", 0.0002),
                ],
                sub_containers=[
                    _container(
                        "OsIsrResourceLock",
                        "OsIsrResourceLock",
                        parameters=[_float_parameter("OsIsrResourceLockBudget", 0.0003), _float_parameter("OsIsrResourceLockBudget", 0.0004)],
                        references=[
                            _reference("OsIsrResourceLockResourceRef", "/Os/Os/Res1"),
                            _reference("OsIsrResourceLockResourceRef", "/Os/Os/Res2"),
                        ],
                    )
                ],
            )
        ],
    )
    containers = [
        _container("App1", "OsApplication"),
        _container("App2", "OsApplication"),
        _container("MemRegion1", "OsMemorySection"),
        _container("Res1", "OsResource"),
        _container("Res2", "OsResource"),
        isr_container,
    ]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document)

    isr = result.getOsIsrs()[0]
    assert isr.getOsIsrCategory() == "CATEGORY_1"
    assert isr.getOsIsrPriority() == 3
    assert isr.getOsIsrAccessingApplications() == ["/Os/Os/App1", "/Os/Os/App2"]
    assert isr.getOsMemoryMappingCodeLocationRef() == "/Os/Os/MemRegion1"
    assert isr.getOsIsrAllInterruptLockBudget() == 0.0001
    assert isr.getOsIsrOsInterruptLockBudget() == 0.0002
    assert isr.getOsIsrResourceLockBudgets() == [0.0003, 0.0004]
    assert isr.getOsIsrResourceLockResourceRefs() == ["/Os/Os/Res1", "/Os/Os/Res2"]


def test_collect_isr_unresolved_resource_ref_raises_in_strict_mode():
    containers = [_container("BadIsr", "OsIsr", references=[_reference("OsIsrResourceRef", "/Os/Os/MissingResource")])]
    document = _build_document(containers)

    with pytest.raises(OsEcucConversionError, match="MissingResource"):
        OsEcucParser().parseEcuc(document)
```

NOTE: the `_float_parameter` and `_enum_parameter` helpers produce definition-refs ending in `/OsTask/<name>`; the parser keys on the trailing name only, so this is fine.

One nuance: the two-`OsIsrResourceLockBudget`-parameter case relies on `addParameterValue` retaining both entries; the existing `_container` helper appends each parameter, and `Container.getParameterValues()` returns the full list — this mirrors the real ARXML where `OsIsrResourceLock` may repeat. If `addParameterValue` deduplicates by definition-ref (verify in Step 2 — if the assertion `[0.0003, 0.0004]` fails because only one entry is retained, change the fixture to two separate `OsIsrResourceLock` sub-containers instead of two parameters).

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/parser/test_os_ecuc_parser.py -v -k "collect_isr"`
Expected: FAIL — `IndexError: list index out of range` (no ISRs parsed yet)

- [ ] **Step 3: Implement get_collect_isr and wire into parseEcuc**

In `src/armodel/parser/os_ecuc_parser.py`, update the import:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsTask
```

Add the new method after `get_collect_alarm`:

```python
    def get_collect_isr(self, isr: OsIsr, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            raw = self.get_raw_value(parameter)
            if name == "OsIsrCategory":
                isr.setOsIsrCategory(self.get_str(name, raw))
            elif name == "OsIsrPeriod":
                isr.setOsIsrPeriod(self.get_float(name, raw))
            elif name == "OsIsrPriority":
                isr.setOsIsrPriority(self.get_int(name, raw))
            elif name == "OsIsrName":
                isr.setOsIsrName(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsIsr parameter %s" % name)

        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
            if name == "OsIsrResourceRef":
                isr.setOsIsrResourceRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsIsrInterruptSource":
                isr.setOsIsrInterruptSource(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsIsrAccessingApplication":
                isr.addOsIsrAccessingApplication(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsMemoryMappingCodeLocationRef":
                isr.setOsMemoryMappingCodeLocationRef(self.get_check_reference_path(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsIsr reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for timing_protection in sub_containers.get("OsIsrTimingProtection", []):
            for parameter in self.get_parameter_values(timing_protection):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsIsrExecutionBudget":
                    isr.setOsIsrExecutionBudget(self.get_float(name, raw))
                elif name == "OsIsrTimeFrame":
                    isr.setOsIsrTimeFrame(self.get_float(name, raw))
                elif name == "OsIsrAllInterruptLockBudget":
                    isr.setOsIsrAllInterruptLockBudget(self.get_float(name, raw))
                elif name == "OsIsrOsInterruptLockBudget":
                    isr.setOsIsrOsInterruptLockBudget(self.get_float(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsIsrTimingProtection parameter %s" % name)
            for resource_lock in self.get_sub_containers_by_name(timing_protection).get("OsIsrResourceLock", []):
                for parameter in self.get_parameter_values(resource_lock):
                    name = self.get_definition_name(parameter.getDefinitionRef())
                    raw = self.get_raw_value(parameter)
                    if name == "OsIsrResourceLockBudget":
                        isr.addOsIsrResourceLockBudget(self.get_float(name, raw))
                    else:
                        self.logger.debug("Ignore non-standard OsIsrResourceLock parameter %s" % name)
                for reference in self.get_reference_values(resource_lock):
                    name = self.get_definition_name(reference.getDefinitionRef())
                    value_ref = reference.getValueRef()
                    if value_ref is None or value_ref.getValue() is None:
                        continue
                    path = value_ref.getValue().strip()
                    if name == "OsIsrResourceLockResourceRef":
                        isr.addOsIsrResourceLockResourceRef(self.get_check_reference_path(name, path, index, warning))
                    else:
                        self.logger.debug("Ignore non-standard OsIsrResourceLock reference %s" % name)
```

In `parseEcuc`, after the alarms collection loop from Task 4 and before the `get_resolve_task_objects` loop, add:

```python
        isrs: Dict[str, OsIsr] = {}
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsIsr":
                isr = OsIsr()
                isr.setName(container.getShortName())
                self.logger.info("Parsing OsIsr: %s", isr.getName())
                self.get_collect_isr(isr, container, index, warning)
                isrs[path] = isr
                os_os.addOsIsr(isr)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/parser/test_os_ecuc_parser.py -v`
Expected: PASS (if the two-budget test failed on deduplication, switch that fixture to two `OsIsrResourceLock` sub-containers per the Step 1 note, then re-run)

- [ ] **Step 5: Commit**

```bash
git add src/armodel/parser/os_ecuc_parser.py tests/test_armodel/parser/test_os_ecuc_parser.py
git commit -m "feat: parse OsIsr containers into semantic OsIsr objects"
```

---

### Task 6: Parser — collect OsScheduleTable

**Files:**
- Modify: `src/armodel/parser/os_ecuc_parser.py` (import + new method + `parseEcuc` wiring)
- Test: `tests/test_armodel/parser/test_os_ecuc_parser.py`

**Interfaces:**
- Consumes: `OsScheduleTable`, `OsScheduleTableExpiryPoint` from Task 3; base helpers as Task 4 plus `get_bool`
- Produces: `OsEcucParser.get_collect_schedule_table(schedule_table: OsScheduleTable, container: Container, index: Dict[str, Container], warning: bool) -> None`; `parseEcuc()` populates `getOsScheduleTables()`

ECUC mapping handled by this task:
- OsScheduleTable parameters: `OsScheduleTableDuration` (int), `OsScheduleTableRepeating` (bool)
- OsScheduleTable references: `OsScheduleTableCounterRef`, `OsScheduleTableAccessingApplication` (multi)
- `OsScheduleTableAutostart` sub-container: params `OsScheduleTableAutostartType` (str), `OsScheduleTableStartValue` (int); ref `OsScheduleTableAppModeRef`
- `OsScheduleTableSync` sub-container: params `OsScheduleTblSyncStrategy` (str), `OsScheduleTblExplicitPrecision` (int)
- `OsScheduleTableExpiryPoint` sub-containers: params `OsScheduleTblExpPointOffset` (int), `OsScheduleTableMaxShorten` (int), `OsScheduleTableMaxLengthen` (int); nested `OsScheduleTableTaskActivation` (ref `OsScheduleTableActivateTaskRef`) and `OsScheduleTableEventSetting` (refs `OsScheduleTableSetEventTaskRef`, `OsScheduleTableSetEventRef`)

- [ ] **Step 1: Write the failing tests**

In `tests/test_armodel/parser/test_os_ecuc_parser.py`, update the data-model import:

```python
from armodel.data_models.ecuc import OsAlarm, OsIsr, OsOs, OsScheduleTable
```

Append tests:

```python
def test_collect_schedule_table_with_autostart_sync_and_expiry_points():
    schedule_table_container = _container(
        "Table1",
        "OsScheduleTable",
        parameters=[
            _int_parameter("OsScheduleTableDuration", 10),
            _bool_parameter("OsScheduleTableRepeating", True),
        ],
        references=[_reference("OsScheduleTableCounterRef", "/Os/Os/HwCounter")],
        sub_containers=[
            _container(
                "OsScheduleTableAutostart",
                "OsScheduleTableAutostart",
                parameters=[
                    _enum_parameter("OsScheduleTableAutostartType", "RELATIVE"),
                    _int_parameter("OsScheduleTableStartValue", 0),
                ],
                references=[_reference("OsScheduleTableAppModeRef", "/Os/Os/OSDEFAULTAPPMODE")],
            ),
            _container(
                "OsScheduleTableSync",
                "OsScheduleTableSync",
                parameters=[_enum_parameter("OsScheduleTblSyncStrategy", "IMPLICIT")],
            ),
            _container(
                "ExpiryPoint1",
                "OsScheduleTableExpiryPoint",
                parameters=[
                    _int_parameter("OsScheduleTblExpPointOffset", 2),
                    _int_parameter("OsScheduleTableMaxShorten", 1),
                    _int_parameter("OsScheduleTableMaxLengthen", 1),
                ],
                sub_containers=[
                    _container(
                        "OsScheduleTableTaskActivation",
                        "OsScheduleTableTaskActivation",
                        references=[_reference("OsScheduleTableActivateTaskRef", "/Os/Os/Task1")],
                    )
                ],
            ),
            _container(
                "ExpiryPoint2",
                "OsScheduleTableExpiryPoint",
                parameters=[_int_parameter("OsScheduleTblExpPointOffset", 5)],
                sub_containers=[
                    _container(
                        "OsScheduleTableEventSetting",
                        "OsScheduleTableEventSetting",
                        references=[
                            _reference("OsScheduleTableSetEventTaskRef", "/Os/Os/Task2"),
                            _reference("OsScheduleTableSetEventRef", "/Os/Os/Event1"),
                        ],
                    )
                ],
            ),
        ],
    )
    containers = [
        _container("HwCounter", "OsCounter"),
        _container("OSDEFAULTAPPMODE", "OsAppMode"),
        _container("Task1", "OsTask"),
        _container("Task2", "OsTask"),
        _container("Event1", "OsEvent"),
        schedule_table_container,
    ]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document)

    schedule_table = result.getOsScheduleTables()[0]
    assert schedule_table.getName() == "Table1"
    assert schedule_table.getOsScheduleTableCounterRef() == "/Os/Os/HwCounter"
    assert schedule_table.getOsScheduleTableDuration() == 10
    assert schedule_table.getOsScheduleTableRepeating() is True
    assert schedule_table.getOsScheduleTableAutostartType() == "RELATIVE"
    assert schedule_table.getOsScheduleTableStartValue() == 0
    assert schedule_table.getOsScheduleTableAppModeRef() == "/Os/Os/OSDEFAULTAPPMODE"
    assert schedule_table.getOsScheduleTableSyncStrategy() == "IMPLICIT"

    expiry_points = schedule_table.getOsScheduleTableExpiryPoints()
    assert len(expiry_points) == 2
    assert expiry_points[0].getOsScheduleTableExpiryPointOffset() == 2
    assert expiry_points[0].getOsScheduleTableMaxShorten() == 1
    assert expiry_points[0].getOsScheduleTableMaxLengthen() == 1
    assert expiry_points[0].getOsScheduleTableActivateTaskRef() == "/Os/Os/Task1"
    assert expiry_points[1].getOsScheduleTableExpiryPointOffset() == 5
    assert expiry_points[1].getOsScheduleTableSetEventTaskRef() == "/Os/Os/Task2"
    assert expiry_points[1].getOsScheduleTableSetEventRef() == "/Os/Os/Event1"


def test_collect_schedule_table_unresolved_counter_ref_raises_in_strict_mode():
    containers = [_container("BadTable", "OsScheduleTable", references=[_reference("OsScheduleTableCounterRef", "/Os/Os/MissingCounter")])]
    document = _build_document(containers)

    with pytest.raises(OsEcucConversionError, match="MissingCounter"):
        OsEcucParser().parseEcuc(document)


def test_collect_schedule_table_accessing_application_collected_as_path():
    containers = [
        _container("App1", "OsApplication"),
        _container("Table2", "OsScheduleTable", references=[_reference("OsScheduleTableAccessingApplication", "/Os/Os/App1")]),
    ]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document)

    assert result.getOsScheduleTables()[0].getOsScheduleTableAccessingApplications() == ["/Os/Os/App1"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/parser/test_os_ecuc_parser.py -v -k "schedule_table"`
Expected: FAIL — `IndexError: list index out of range` (no schedule tables parsed yet)

- [ ] **Step 3: Implement get_collect_schedule_table and wire into parseEcuc**

In `src/armodel/parser/os_ecuc_parser.py`, update the import:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask
```

Add the new method after `get_collect_isr`:

```python
    def get_collect_schedule_table(self, schedule_table: OsScheduleTable, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            raw = self.get_raw_value(parameter)
            if name == "OsScheduleTableDuration":
                schedule_table.setOsScheduleTableDuration(self.get_int(name, raw))
            elif name == "OsScheduleTableRepeating":
                schedule_table.setOsScheduleTableRepeating(self.get_bool(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsScheduleTable parameter %s" % name)

        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
            if name == "OsScheduleTableCounterRef":
                schedule_table.setOsScheduleTableCounterRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsScheduleTableAccessingApplication":
                schedule_table.addOsScheduleTableAccessingApplication(self.get_check_reference_path(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsScheduleTable reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for autostart in sub_containers.get("OsScheduleTableAutostart", []):
            for parameter in self.get_parameter_values(autostart):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsScheduleTableAutostartType":
                    schedule_table.setOsScheduleTableAutostartType(self.get_str(name, raw))
                elif name == "OsScheduleTableStartValue":
                    schedule_table.setOsScheduleTableStartValue(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableAutostart parameter %s" % name)
            for reference in self.get_reference_values(autostart):
                name = self.get_definition_name(reference.getDefinitionRef())
                value_ref = reference.getValueRef()
                if value_ref is None or value_ref.getValue() is None:
                    continue
                path = value_ref.getValue().strip()
                if name == "OsScheduleTableAppModeRef":
                    schedule_table.setOsScheduleTableAppModeRef(self.get_check_reference_path(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableAutostart reference %s" % name)

        for sync in sub_containers.get("OsScheduleTableSync", []):
            for parameter in self.get_parameter_values(sync):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsScheduleTblSyncStrategy":
                    schedule_table.setOsScheduleTableSyncStrategy(self.get_str(name, raw))
                elif name == "OsScheduleTblExplicitPrecision":
                    schedule_table.setOsScheduleTableExplicitPrecision(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableSync parameter %s" % name)

        for expiry_container in sub_containers.get("OsScheduleTableExpiryPoint", []):
            expiry_point = OsScheduleTableExpiryPoint()
            for parameter in self.get_parameter_values(expiry_container):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsScheduleTblExpPointOffset":
                    expiry_point.setOsScheduleTableExpiryPointOffset(self.get_int(name, raw))
                elif name == "OsScheduleTableMaxShorten":
                    expiry_point.setOsScheduleTableMaxShorten(self.get_int(name, raw))
                elif name == "OsScheduleTableMaxLengthen":
                    expiry_point.setOsScheduleTableMaxLengthen(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableExpiryPoint parameter %s" % name)
            expiry_sub_containers = self.get_sub_containers_by_name(expiry_container)
            for task_activation in expiry_sub_containers.get("OsScheduleTableTaskActivation", []):
                for reference in self.get_reference_values(task_activation):
                    name = self.get_definition_name(reference.getDefinitionRef())
                    value_ref = reference.getValueRef()
                    if value_ref is None or value_ref.getValue() is None:
                        continue
                    path = value_ref.getValue().strip()
                    if name == "OsScheduleTableActivateTaskRef":
                        expiry_point.setOsScheduleTableActivateTaskRef(self.get_check_reference_path(name, path, index, warning))
                    else:
                        self.logger.debug("Ignore non-standard OsScheduleTableTaskActivation reference %s" % name)
            for event_setting in expiry_sub_containers.get("OsScheduleTableEventSetting", []):
                for reference in self.get_reference_values(event_setting):
                    name = self.get_definition_name(reference.getDefinitionRef())
                    value_ref = reference.getValueRef()
                    if value_ref is None or value_ref.getValue() is None:
                        continue
                    path = value_ref.getValue().strip()
                    if name == "OsScheduleTableSetEventTaskRef":
                        expiry_point.setOsScheduleTableSetEventTaskRef(self.get_check_reference_path(name, path, index, warning))
                    elif name == "OsScheduleTableSetEventRef":
                        expiry_point.setOsScheduleTableSetEventRef(self.get_check_reference_path(name, path, index, warning))
                    else:
                        self.logger.debug("Ignore non-standard OsScheduleTableEventSetting reference %s" % name)
            schedule_table.addOsScheduleTableExpiryPoint(expiry_point)
```

In `parseEcuc`, after the ISRs collection loop from Task 5 and before the `get_resolve_task_objects` loop, add:

```python
        schedule_tables: Dict[str, OsScheduleTable] = {}
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsScheduleTable":
                schedule_table = OsScheduleTable()
                schedule_table.setName(container.getShortName())
                self.logger.info("Parsing OsScheduleTable: %s", schedule_table.getName())
                self.get_collect_schedule_table(schedule_table, container, index, warning)
                schedule_tables[path] = schedule_table
                os_os.addOsScheduleTable(schedule_table)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/parser/test_os_ecuc_parser.py -v`
Expected: PASS (new + all pre-existing parser tests)

- [ ] **Step 5: Commit**

```bash
git add src/armodel/parser/os_ecuc_parser.py tests/test_armodel/parser/test_os_ecuc_parser.py
git commit -m "feat: parse OsScheduleTable containers into semantic objects"
```

---

### Task 7: Exporter — mapper methods, to_dict, XLSX empty-sheet headers

**Files:**
- Modify: `src/armodel/report/os_export.py` (import, 4 new mapper methods, `to_dict`, XLSX headers fallback, list formatting)
- Test: `tests/test_armodel/report/test_os_export.py`

**Interfaces:**
- Consumes: `OsAlarm`, `OsIsr`, `OsScheduleTable`, `OsScheduleTableExpiryPoint` from Tasks 1–3; `OsOs.getOsAlarms/getOsIsrs/getOsScheduleTables`
- Produces: `OsConfigModelMapper.alarm_to_dict(alarm: OsAlarm) -> Dict[str, Any]`, `isr_to_dict(isr: OsIsr) -> Dict[str, Any]`, `expiry_point_to_dict(expiry_point: OsScheduleTableExpiryPoint) -> Dict[str, Any]`, `schedule_table_to_dict(schedule_table: OsScheduleTable) -> Dict[str, Any]`; `to_dict()` now returns 5 sections (`OsApplication`, `OsTask`, `OsAlarm`, `OsIsr`, `OsScheduleTable`); module-level `_format_list_item(item)`; `OsConfigXlsxExporter._headers_for(sheet_name, rows)` — empty sheets get correct per-section headers

- [ ] **Step 1: Write the failing tests**

In `tests/test_armodel/report/test_os_export.py`, update the data-model import:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask
```

Append tests:

```python
def test_write_yaml_exports_alarm_isr_and_schedule_table_sections(tmp_path: Path):
    alarm = OsAlarm().setName("Alarm1").setOsAlarmCounterRef("/Os/Os/HwCounter").setOsAlarmIncrementCounterRef("/Os/Os/Rte_Counter").setOsAlarmAlarmTime(1).setOsAlarmAutostartType("RELATIVE")
    isr = OsIsr().setName("CanIsr").setOsIsrCategory("CATEGORY_2").setOsIsrPeriod(0.005).setOsIsrExecutionBudget(0.001)
    isr.addOsIsrResourceLockBudget(0.0005)
    isr.addOsIsrResourceLockResourceRef("/Os/Os/OsStackResource")
    expiry_point1 = OsScheduleTableExpiryPoint().setOsScheduleTableExpiryPointOffset(2).setOsScheduleTableActivateTaskRef("/Os/Os/Rte_Time_Task")
    expiry_point2 = OsScheduleTableExpiryPoint().setOsScheduleTableExpiryPointOffset(5).setOsScheduleTableMaxShorten(1).setOsScheduleTableSetEventTaskRef("/Os/Os/Rte_Event_Task").setOsScheduleTableSetEventRef("/Os/Os/Rte_OSShutdownEvent")
    schedule_table = (
        OsScheduleTable()
        .setName("SystemScheduleTable")
        .setOsScheduleTableCounterRef("/Os/Os/HwCounter")
        .setOsScheduleTableDuration(10)
        .setOsScheduleTableRepeating(True)
        .setOsScheduleTableAutostartType("RELATIVE")
        .setOsScheduleTableSyncStrategy("IMPLICIT")
    )
    schedule_table.addOsScheduleTableExpiryPoint(expiry_point1)
    schedule_table.addOsScheduleTableExpiryPoint(expiry_point2)
    os_os = OsOs().setName("Os")
    os_os.addOsAlarm(alarm)
    os_os.addOsIsr(isr)
    os_os.addOsScheduleTable(schedule_table)
    output = tmp_path / "os.yaml"

    OsConfigYamlExporter().export(os_os, output)

    data = yaml.safe_load(output.read_text(encoding="utf-8"))
    assert set(data) == {"OsApplication", "OsTask", "OsAlarm", "OsIsr", "OsScheduleTable"}
    assert data["OsAlarm"][0] == {
        "name": "Alarm1",
        "OsAlarmCounterRef": "/Os/Os/HwCounter",
        "OsAlarmIncrementCounterRef": "/Os/Os/Rte_Counter",
        "OsAlarmAlarmTime": 1,
        "OsAlarmAutostartType": "RELATIVE",
    }
    assert data["OsIsr"][0] == {
        "name": "CanIsr",
        "OsIsrCategory": "CATEGORY_2",
        "OsIsrPeriod": 0.005,
        "OsIsrExecutionBudget": 0.001,
        "OsIsrResourceLockBudget": [0.0005],
        "OsIsrResourceLockResourceRef": ["/Os/Os/OsStackResource"],
    }
    assert data["OsScheduleTable"][0] == {
        "name": "SystemScheduleTable",
        "OsScheduleTableCounterRef": "/Os/Os/HwCounter",
        "OsScheduleTableDuration": 10,
        "OsScheduleTableRepeating": True,
        "OsScheduleTableAutostartType": "RELATIVE",
        "OsScheduleTableSyncStrategy": "IMPLICIT",
        "OsScheduleTableExpiryPoint": [
            {"OsScheduleTblExpPointOffset": 2, "OsScheduleTableActivateTaskRef": "/Os/Os/Rte_Time_Task"},
            {
                "OsScheduleTblExpPointOffset": 5,
                "OsScheduleTableMaxShorten": 1,
                "OsScheduleTableSetEventTaskRef": "/Os/Os/Rte_Event_Task",
                "OsScheduleTableSetEventRef": "/Os/Os/Rte_OSShutdownEvent",
            },
        ],
    }


def test_mapper_to_dict_contains_five_sections_with_defaults():
    data = OsConfigModelMapper().to_dict(OsOs().setName("Os"))

    assert set(data) == {"OsApplication", "OsTask", "OsAlarm", "OsIsr", "OsScheduleTable"}
    assert data["OsApplication"] == []
    assert data["OsTask"] == []
    assert data["OsAlarm"] == []
    assert data["OsIsr"] == []
    assert data["OsScheduleTable"] == []


def test_write_xlsx_uses_correct_headers_for_empty_new_sections(tmp_path: Path):
    output = tmp_path / "os.xlsx"

    OsConfigXlsxExporter().export(OsOs().setName("Os"), output)

    workbook = load_workbook(output)
    assert workbook.sheetnames == ["OsApplication", "OsTask", "OsAlarm", "OsIsr", "OsScheduleTable"]
    isr_headers = [cell.value for cell in workbook["OsIsr"][1]]
    assert isr_headers[0] == "name"
    assert "OsIsrCategory" in isr_headers
    table_headers = [cell.value for cell in workbook["OsScheduleTable"][1]]
    assert table_headers[0] == "name"
    assert "OsScheduleTableCounterRef" in table_headers


def test_write_xlsx_formats_expiry_point_dicts_readably(tmp_path: Path):
    expiry_point = OsScheduleTableExpiryPoint().setOsScheduleTableExpiryPointOffset(2).setOsScheduleTableActivateTaskRef("/Os/Os/Task1")
    schedule_table = OsScheduleTable().setName("Table1").setOsScheduleTableDuration(10)
    schedule_table.addOsScheduleTableExpiryPoint(expiry_point)
    os_os = OsOs().setName("Os")
    os_os.addOsScheduleTable(schedule_table)
    output = tmp_path / "os.xlsx"

    OsConfigXlsxExporter().export(os_os, output)

    workbook = load_workbook(output)
    sheet = workbook["OsScheduleTable"]
    headers = [cell.value for cell in sheet[1]]
    cell = sheet.cell(row=2, column=headers.index("OsScheduleTableExpiryPoint") + 1)
    assert cell.value == "OsScheduleTblExpPointOffset=2,OsScheduleTableActivateTaskRef=/Os/Os/Task1"
```

Also update the existing import line to add `OsConfigModelMapper`:

```python
from armodel.report import OsConfigExporter, OsConfigModelMapper, OsConfigXlsxExporter, OsConfigYamlExporter
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/report/test_os_export.py -v`
Expected: FAIL — `ImportError: cannot import name 'OsConfigModelMapper'` (or `KeyError: 'OsAlarm'` for the sections test)

- [ ] **Step 3: Implement the mapper methods and exporter updates**

In `src/armodel/report/os_export.py`, update the data-model import:

```python
from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask
```

Add a module-level helper after the imports (before `class OsConfigModelMapper`):

```python
def _format_list_item(item: Any) -> str:
    if isinstance(item, dict):
        return ",".join("%s=%s" % (key, item[key]) for key in item)
    return str(item)
```

In `OsConfigModelMapper`, add after `task_to_dict`:

```python
    def alarm_to_dict(self, alarm: OsAlarm) -> Dict[str, Any]:
        return {
            "name": alarm.getName(),
            "OsAlarmCounterRef": alarm.getOsAlarmCounterRef(),
            "OsAlarmAccessingApplication": list(alarm.getOsAlarmAccessingApplications()),
            "OsAlarmActivateTaskRef": alarm.getOsAlarmActivateTaskRef(),
            "OsAlarmSetEventTaskRef": alarm.getOsAlarmSetEventTaskRef(),
            "OsAlarmSetEventRef": alarm.getOsAlarmSetEventRef(),
            "OsAlarmIncrementCounterRef": alarm.getOsAlarmIncrementCounterRef(),
            "OsAlarmCallbackName": alarm.getOsAlarmCallbackName(),
            "OsAlarmAlarmTime": alarm.getOsAlarmAlarmTime(),
            "OsAlarmAutostartType": alarm.getOsAlarmAutostartType(),
            "OsAlarmCycleTime": alarm.getOsAlarmCycleTime(),
            "OsAlarmAppModeRef": alarm.getOsAlarmAppModeRef(),
        }

    def isr_to_dict(self, isr: OsIsr) -> Dict[str, Any]:
        return {
            "name": isr.getName(),
            "OsIsrName": isr.getOsIsrName(),
            "OsIsrCategory": isr.getOsIsrCategory(),
            "OsIsrPriority": isr.getOsIsrPriority(),
            "OsIsrPeriod": isr.getOsIsrPeriod(),
            "OsIsrResourceRef": isr.getOsIsrResourceRef(),
            "OsIsrInterruptSource": isr.getOsIsrInterruptSource(),
            "OsIsrAccessingApplication": list(isr.getOsIsrAccessingApplications()),
            "OsMemoryMappingCodeLocationRef": isr.getOsMemoryMappingCodeLocationRef(),
            "OsIsrExecutionBudget": isr.getOsIsrExecutionBudget(),
            "OsIsrTimeFrame": isr.getOsIsrTimeFrame(),
            "OsIsrAllInterruptLockBudget": isr.getOsIsrAllInterruptLockBudget(),
            "OsIsrOsInterruptLockBudget": isr.getOsIsrOsInterruptLockBudget(),
            "OsIsrResourceLockBudget": list(isr.getOsIsrResourceLockBudgets()),
            "OsIsrResourceLockResourceRef": list(isr.getOsIsrResourceLockResourceRefs()),
        }

    def expiry_point_to_dict(self, expiry_point: OsScheduleTableExpiryPoint) -> Dict[str, Any]:
        return {
            key: value
            for key, value in {
                "OsScheduleTblExpPointOffset": expiry_point.getOsScheduleTableExpiryPointOffset(),
                "OsScheduleTableMaxShorten": expiry_point.getOsScheduleTableMaxShorten(),
                "OsScheduleTableMaxLengthen": expiry_point.getOsScheduleTableMaxLengthen(),
                "OsScheduleTableActivateTaskRef": expiry_point.getOsScheduleTableActivateTaskRef(),
                "OsScheduleTableSetEventTaskRef": expiry_point.getOsScheduleTableSetEventTaskRef(),
                "OsScheduleTableSetEventRef": expiry_point.getOsScheduleTableSetEventRef(),
            }.items()
            if value is not None
        }

    def schedule_table_to_dict(self, schedule_table: OsScheduleTable) -> Dict[str, Any]:
        return {
            "name": schedule_table.getName(),
            "OsScheduleTableCounterRef": schedule_table.getOsScheduleTableCounterRef(),
            "OsScheduleTableDuration": schedule_table.getOsScheduleTableDuration(),
            "OsScheduleTableRepeating": schedule_table.getOsScheduleTableRepeating(),
            "OsScheduleTableAccessingApplication": list(schedule_table.getOsScheduleTableAccessingApplications()),
            "OsScheduleTableAutostartType": schedule_table.getOsScheduleTableAutostartType(),
            "OsScheduleTableStartValue": schedule_table.getOsScheduleTableStartValue(),
            "OsScheduleTableAppModeRef": schedule_table.getOsScheduleTableAppModeRef(),
            "OsScheduleTableSyncStrategy": schedule_table.getOsScheduleTableSyncStrategy(),
            "OsScheduleTableExplicitPrecision": schedule_table.getOsScheduleTableExplicitPrecision(),
            "OsScheduleTableExpiryPoint": [self.expiry_point_to_dict(point) for point in schedule_table.getOsScheduleTableExpiryPoints()],
        }
```

Replace `to_dict` with:

```python
    def to_dict(self, os_os: OsOs) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "OsApplication": [self.application_to_dict(application) for application in os_os.getOsApplications()],
            "OsTask": [self.task_to_dict(task) for task in os_os.getOsTasks()],
            "OsAlarm": [self.alarm_to_dict(alarm) for alarm in os_os.getOsAlarms()],
            "OsIsr": [self.isr_to_dict(isr) for isr in os_os.getOsIsrs()],
            "OsScheduleTable": [self.schedule_table_to_dict(schedule_table) for schedule_table in os_os.getOsScheduleTables()],
        }
```

In `OsConfigXlsxExporter.export`, replace the header computation:

```python
            headers = (
                list(rows[0].keys()) if rows else list(self.mapper.application_to_dict(OsApplication()).keys()) if sheet_name == "OsApplication" else list(self.mapper.task_to_dict(OsTask()).keys())
            )
```

with:

```python
            headers = self._headers_for(sheet_name, rows)
```

And add the method to `OsConfigXlsxExporter`:

```python
    def _headers_for(self, sheet_name: str, rows: List[Dict[str, Any]]) -> List[str]:
        if rows:
            return list(rows[0].keys())
        empty_row = {
            "OsApplication": self.mapper.application_to_dict(OsApplication()),
            "OsTask": self.mapper.task_to_dict(OsTask()),
            "OsAlarm": self.mapper.alarm_to_dict(OsAlarm()),
            "OsIsr": self.mapper.isr_to_dict(OsIsr()),
            "OsScheduleTable": self.mapper.schedule_table_to_dict(OsScheduleTable()),
        }[sheet_name]
        return list(empty_row.keys())
```

In the same `export` method, replace the list formatting:

```python
                    if isinstance(value, list):
                        value = "\n".join(str(item) for item in value)
                        format = {"alignment": Alignment(wrap_text=True)}
```

with:

```python
                    if isinstance(value, list):
                        value = "\n".join(_format_list_item(item) for item in value)
                        format = {"alignment": Alignment(wrap_text=True)}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/report/test_os_export.py tests/test_armodel/data_models/ecuc/test_os.py tests/test_armodel/parser/test_os_ecuc_parser.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/armodel/report/os_export.py tests/test_armodel/report/test_os_export.py
git commit -m "feat: export OsAlarm, OsIsr and OsScheduleTable sections in YAML and XLSX"
```

---

### Task 8: Integration fixtures — ARXML examples, YAML fixture, CLI test updates

**Files:**
- Modify: `tests/integration_tests/test_files/Os_ECUC.arxml` (add alarm/ISR/resource/schedule-table containers)
- Modify: `tests/integration_tests/test_files/Os_ECUC.yaml` (regenerate from exporter output)
- Modify: `tests/integration_tests/test_os_config_export_cli.py` (sheet names, section set, new assertions)

**Interfaces:**
- Consumes: everything from Tasks 1–7 via the `os-ecuc-export` CLI entry point
- Produces: updated fixtures + updated integration assertions; the round-trip test (`test_roundtrip.py`) re-validates the modified ARXML automatically since it scans `test_files/`

- [ ] **Step 1: Add fixture containers to Os_ECUC.arxml**

In `tests/integration_tests/test_files/Os_ECUC.arxml`, locate this unique anchor (the opening of the OsApplication container):

```
            <CONTAINER>
              <SHORT-NAME>OsApplication_QM</SHORT-NAME>
```

Insert the following block immediately BEFORE that `<CONTAINER>` line (keeps 14-space container indentation used by the file):

```xml
            <CONTAINER>
              <SHORT-NAME>AlarmSetRteShutdownEvent</SHORT-NAME>
              <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsAlarm</DEFINITION-REF>
              <REFERENCE-VALUES>
                <REFERENCE-VALUE>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsAlarm/OsAlarmCounterRef</DEFINITION-REF>
                  <VALUE-REF>/Os/Os/Rte_Counter</VALUE-REF>
                </REFERENCE-VALUE>
              </REFERENCE-VALUES>
              <SUB-CONTAINERS>
                <CONTAINER>
                  <SHORT-NAME>OsAlarmAction</SHORT-NAME>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsAlarm/OsAlarmAction/OsAlarmSetEvent</DEFINITION-REF>
                  <REFERENCE-VALUES>
                    <REFERENCE-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsAlarm/OsAlarmAction/OsAlarmSetEvent/OsAlarmSetEventTaskRef</DEFINITION-REF>
                      <VALUE-REF>/Os/Os/Rte_Event_Task</VALUE-REF>
                    </REFERENCE-VALUE>
                    <REFERENCE-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsAlarm/OsAlarmAction/OsAlarmSetEvent/OsAlarmSetEventRef</DEFINITION-REF>
                      <VALUE-REF>/Os/Os/Rte_OSShutdownEvent</VALUE-REF>
                    </REFERENCE-VALUE>
                  </REFERENCE-VALUES>
                </CONTAINER>
              </SUB-CONTAINERS>
            </CONTAINER>
            <CONTAINER>
              <SHORT-NAME>CanIsr</SHORT-NAME>
              <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr</DEFINITION-REF>
              <PARAMETER-VALUES>
                <ENUMERATION-VALUE>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrCategory</DEFINITION-REF>
                  <VALUE>CATEGORY_2</VALUE>
                </ENUMERATION-VALUE>
                <FLOAT-VALUE>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrPeriod</DEFINITION-REF>
                  <VALUE>0.005</VALUE>
                </FLOAT-VALUE>
              </PARAMETER-VALUES>
              <SUB-CONTAINERS>
                <CONTAINER>
                  <SHORT-NAME>OsIsrTimingProtection</SHORT-NAME>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrTimingProtection</DEFINITION-REF>
                  <PARAMETER-VALUES>
                    <FLOAT-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrTimingProtection/OsIsrExecutionBudget</DEFINITION-REF>
                      <VALUE>0.001</VALUE>
                    </FLOAT-VALUE>
                    <FLOAT-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrTimingProtection/OsIsrTimeFrame</DEFINITION-REF>
                      <VALUE>0.02</VALUE>
                    </FLOAT-VALUE>
                  </PARAMETER-VALUES>
                  <SUB-CONTAINERS>
                    <CONTAINER>
                      <SHORT-NAME>OsIsrResourceLock</SHORT-NAME>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrTimingProtection/OsIsrResourceLock</DEFINITION-REF>
                      <PARAMETER-VALUES>
                        <FLOAT-VALUE>
                          <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrTimingProtection/OsIsrResourceLock/OsIsrResourceLockBudget</DEFINITION-REF>
                          <VALUE>0.0005</VALUE>
                        </FLOAT-VALUE>
                      </PARAMETER-VALUES>
                      <REFERENCE-VALUES>
                        <REFERENCE-VALUE>
                          <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsIsr/OsIsrTimingProtection/OsIsrResourceLock/OsIsrResourceLockResourceRef</DEFINITION-REF>
                          <VALUE-REF>/Os/Os/OsStackResource</VALUE-REF>
                        </REFERENCE-VALUE>
                      </REFERENCE-VALUES>
                    </CONTAINER>
                  </SUB-CONTAINERS>
                </CONTAINER>
              </SUB-CONTAINERS>
            </CONTAINER>
            <CONTAINER>
              <SHORT-NAME>OsStackResource</SHORT-NAME>
              <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsResource</DEFINITION-REF>
            </CONTAINER>
            <CONTAINER>
              <SHORT-NAME>SystemScheduleTable</SHORT-NAME>
              <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable</DEFINITION-REF>
              <PARAMETER-VALUES>
                <INTEGER-VALUE>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableDuration</DEFINITION-REF>
                  <VALUE>10</VALUE>
                </INTEGER-VALUE>
                <BOOLEAN-VALUE>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableRepeating</DEFINITION-REF>
                  <VALUE>true</VALUE>
                </BOOLEAN-VALUE>
              </PARAMETER-VALUES>
              <REFERENCE-VALUES>
                <REFERENCE-VALUE>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableCounterRef</DEFINITION-REF>
                  <VALUE-REF>/Os/Os/HwCounter</VALUE-REF>
                </REFERENCE-VALUE>
              </REFERENCE-VALUES>
              <SUB-CONTAINERS>
                <CONTAINER>
                  <SHORT-NAME>OsScheduleTableAutostart</SHORT-NAME>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableAutostart</DEFINITION-REF>
                  <PARAMETER-VALUES>
                    <ENUMERATION-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableAutostart/OsScheduleTableAutostartType</DEFINITION-REF>
                      <VALUE>RELATIVE</VALUE>
                    </ENUMERATION-VALUE>
                    <INTEGER-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableAutostart/OsScheduleTableStartValue</DEFINITION-REF>
                      <VALUE>0</VALUE>
                    </INTEGER-VALUE>
                  </PARAMETER-VALUES>
                  <REFERENCE-VALUES>
                    <REFERENCE-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableAutostart/OsScheduleTableAppModeRef</DEFINITION-REF>
                      <VALUE-REF>/Os/Os/OSDEFAULTAPPMODE</VALUE-REF>
                    </REFERENCE-VALUE>
                  </REFERENCE-VALUES>
                </CONTAINER>
                <CONTAINER>
                  <SHORT-NAME>OsScheduleTableSync</SHORT-NAME>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableSync</DEFINITION-REF>
                  <PARAMETER-VALUES>
                    <ENUMERATION-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableSync/OsScheduleTblSyncStrategy</DEFINITION-REF>
                      <VALUE>IMPLICIT</VALUE>
                    </ENUMERATION-VALUE>
                  </PARAMETER-VALUES>
                </CONTAINER>
                <CONTAINER>
                  <SHORT-NAME>ExpiryPoint1</SHORT-NAME>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint</DEFINITION-REF>
                  <PARAMETER-VALUES>
                    <INTEGER-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTblExpPointOffset</DEFINITION-REF>
                      <VALUE>2</VALUE>
                    </INTEGER-VALUE>
                  </PARAMETER-VALUES>
                  <SUB-CONTAINERS>
                    <CONTAINER>
                      <SHORT-NAME>OsScheduleTableTaskActivation</SHORT-NAME>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTableTaskActivation</DEFINITION-REF>
                      <REFERENCE-VALUES>
                        <REFERENCE-VALUE>
                          <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTableTaskActivation/OsScheduleTableActivateTaskRef</DEFINITION-REF>
                          <VALUE-REF>/Os/Os/Rte_Time_Task</VALUE-REF>
                        </REFERENCE-VALUE>
                      </REFERENCE-VALUES>
                    </CONTAINER>
                  </SUB-CONTAINERS>
                </CONTAINER>
                <CONTAINER>
                  <SHORT-NAME>ExpiryPoint2</SHORT-NAME>
                  <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint</DEFINITION-REF>
                  <PARAMETER-VALUES>
                    <INTEGER-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTblExpPointOffset</DEFINITION-REF>
                      <VALUE>5</VALUE>
                    </INTEGER-VALUE>
                    <INTEGER-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTableMaxShorten</DEFINITION-REF>
                      <VALUE>1</VALUE>
                    </INTEGER-VALUE>
                    <INTEGER-VALUE>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTableMaxLengthen</DEFINITION-REF>
                      <VALUE>1</VALUE>
                    </INTEGER-VALUE>
                  </PARAMETER-VALUES>
                  <SUB-CONTAINERS>
                    <CONTAINER>
                      <SHORT-NAME>OsScheduleTableEventSetting</SHORT-NAME>
                      <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTableEventSetting</DEFINITION-REF>
                      <REFERENCE-VALUES>
                        <REFERENCE-VALUE>
                          <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTableEventSetting/OsScheduleTableSetEventTaskRef</DEFINITION-REF>
                          <VALUE-REF>/Os/Os/Rte_Event_Task</VALUE-REF>
                        </REFERENCE-VALUE>
                        <REFERENCE-VALUE>
                          <DEFINITION-REF>/TS_T19D1M6I1R0_AS403/Os/OsScheduleTable/OsScheduleTableExpiryPoint/OsScheduleTableEventSetting/OsScheduleTableSetEventRef</DEFINITION-REF>
                          <VALUE-REF>/Os/Os/Rte_OSShutdownEvent</VALUE-REF>
                        </REFERENCE-VALUE>
                      </REFERENCE-VALUES>
                    </CONTAINER>
                  </SUB-CONTAINERS>
                </CONTAINER>
              </SUB-CONTAINERS>
            </CONTAINER>
```

All referenced paths (`/Os/Os/Rte_Counter`, `/Os/Os/Rte_Event_Task`, `/Os/Os/Rte_OSShutdownEvent`, `/Os/Os/HwCounter`, `/Os/Os/Rte_Time_Task`, `/Os/Os/OSDEFAULTAPPMODE`) already exist as top-level containers in the file, so strict-mode reference checks pass.

- [ ] **Step 2: Update the integration test assertions**

In `tests/integration_tests/test_os_config_export_cli.py`:

Replace:

```python
    workbook = load_workbook(output)
    assert workbook.sheetnames == ["OsApplication", "OsTask"]
    assert workbook["OsApplication"]["A2"].value == "OsApplication_QM"
    assert workbook["OsTask"]["A2"].value == "Init_Task"
    assert (tmp_path / "os_ecuc_export.log").exists()
```

with:

```python
    workbook = load_workbook(output)
    assert workbook.sheetnames == ["OsApplication", "OsTask", "OsAlarm", "OsIsr", "OsScheduleTable"]
    assert workbook["OsApplication"]["A2"].value == "OsApplication_QM"
    assert workbook["OsTask"]["A2"].value == "Init_Task"
    alarm_headers = [cell.value for cell in workbook["OsAlarm"][1]]
    alarm_names = [row[0] for row in workbook["OsAlarm"].iter_rows(min_row=2, values_only=True)]
    assert alarm_names == ["AlarmIncrementRteCounter", "AlarmSetRteShutdownEvent"]
    assert "OsAlarmCounterRef" in alarm_headers
    assert workbook["OsIsr"]["A2"].value == "CanIsr"
    assert workbook["OsScheduleTable"]["A2"].value == "SystemScheduleTable"
    assert (tmp_path / "os_ecuc_export.log").exists()
```

Replace:

```python
    assert generated == expected
    assert set(generated) == {"OsApplication", "OsTask"}
    assert generated["OsApplication"]
    assert generated["OsTask"]
    assert all(set(application) == APPLICATION_FIELDS for application in generated["OsApplication"])
    assert all(value is not None and value != [] for task in generated["OsTask"] for value in task.values())
```

with:

```python
    assert generated == expected
    assert set(generated) == {"OsApplication", "OsTask", "OsAlarm", "OsIsr", "OsScheduleTable"}
    assert generated["OsApplication"]
    assert generated["OsTask"]
    assert generated["OsAlarm"]
    assert generated["OsIsr"]
    assert generated["OsScheduleTable"]
    assert all(set(application) == APPLICATION_FIELDS for application in generated["OsApplication"])
    assert all(value is not None and value != [] for task in generated["OsTask"] for value in task.values())
    assert [alarm["name"] for alarm in generated["OsAlarm"]] == ["AlarmIncrementRteCounter", "AlarmSetRteShutdownEvent"]
    assert generated["OsIsr"][0]["name"] == "CanIsr"
    assert generated["OsIsr"][0]["OsIsrCategory"] == "CATEGORY_2"
    assert [point["OsScheduleTblExpPointOffset"] for point in generated["OsScheduleTable"][0]["OsScheduleTableExpiryPoint"]] == [2, 5]
```

- [ ] **Step 3: Regenerate the YAML fixture**

Run the CLI against the updated ARXML and copy the output over the fixture:

```bash
uv run python -c "
from armodel.cli.os_config_export_cli import main
import sys
sys.argv = ['os-ecuc-export', 'tests/integration_tests/test_files/Os_ECUC.arxml', 'tests/integration_tests/test_files/Os_ECUC.yaml']
main()
"
rm -f tests/integration_tests/test_files/os_ecuc_export.log
```

Then inspect the fixture: it must now contain `OsAlarm`, `OsIsr`, and `OsScheduleTable` top-level keys with the AlarmIncrementRteCounter, AlarmSetRteShutdownEvent, CanIsr, and SystemScheduleTable rows, and the OsApplication/OsTask sections unchanged from before.

- [ ] **Step 4: Run the integration tests**

Run: `uv run pytest tests/integration_tests/test_os_config_export_cli.py -v`
Expected: PASS (all 4 tests, including `matches_complete_yaml_fixture` and the 4.4.0 variant — the 4.4.0 file has no alarm/isr/table containers, so its new sections are empty lists and the assertions only compare OsApplication/OsTask)

Also run the round-trip suite (the modified ARXML is part of its scan):

Run: `uv run pytest tests/integration_tests/test_roundtrip.py -v -k "Os_ECUC"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/integration_tests/test_files/Os_ECUC.arxml tests/integration_tests/test_files/Os_ECUC.yaml tests/integration_tests/test_os_config_export_cli.py
git commit -m "test: add OsIsr/OsScheduleTable/set-event-alarm fixtures and update os-ecuc-export integration tests"
```

---

### Task 9: Full quality gates — lint, black, complete test suite

**Files:**
- Modify: any file flagged by lint/black (likely none beyond reformatting)
- Test: full suite

**Interfaces:**
- Consumes: all previous tasks
- Produces: green CI-equivalent state

- [ ] **Step 1: Run black**

Run: `npm run black`
Expected: reformats any files needing it (200-char line length)

- [ ] **Step 2: Run lint**

Run: `npm run lint`
Expected: no errors (flake8 E9/F63/F7/F82 + ruff E/F/W/I; warnings about line length are exit-zero and acceptable)

- [ ] **Step 3: Run the full test suite**

Run: `uv run python scripts/run_tests.py`
Expected: all unit + integration tests pass, coverage summary printed

- [ ] **Step 4: Fix any failures**

If black reformatted files or lint flagged issues, fix and re-run Steps 1–3 until green.

- [ ] **Step 5: Commit (if there are changes)**

```bash
git add -u
git commit -m "style: apply black formatting for OS export feature"
```

- [ ] **Step 6: Update the design spec status**

In `docs/superpowers/specs/2024-01-15-os-alarm-isr-schedule-table-design.md`, change the header line `**Status:** Design Review` to `**Status:** Implemented` and note the two spec corrections in a new "Implementation notes" section at the bottom:

```markdown
## Implementation Notes

- Schedule-table numeric parameters follow the R23-11 spec (`EcucIntegerParamDef`): `osScheduleTableDuration`, offsets, `MaxShorten`/`MaxLengthen`, `StartValue`, `ExplicitPrecision` are `Optional[int]`, not `Optional[float]` as sketched in §2.3/§2.4.
- ECUC names use the spec spellings: `OsScheduleTblExpPointOffset`, `OsScheduleTblSyncStrategy`, `OsScheduleTblExplicitPrecision`, `OsScheduleTableStartValue`.
- `OsIsr` includes three spec-aligned fields not in §2.2: `osIsrPeriod`, `osIsrResourceRef`, `osMemoryMappingCodeLocationRef`.
- No `get_resolve_*` methods were needed: per §5.1 all cross-references remain string paths.
- The XLSX exporter's empty-sheet header fallback was replaced by `OsConfigXlsxExporter._headers_for()` covering all five sections (§4.3).
```

Commit:

```bash
git add docs/superpowers/specs/2024-01-15-os-alarm-isr-schedule-table-design.md
git commit -m "docs: mark OS alarm/isr/schedule-table design as implemented"
```
