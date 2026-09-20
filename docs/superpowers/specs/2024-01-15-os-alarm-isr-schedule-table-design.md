# Design: Add OsAlarm, OsIsr, and OsScheduleTable to py-armodel

**Date:** 2024-01-15  
**Project:** py-armodel  
**Feature:** OS ECUC Export Enhancement  
**Status:** Design Review

---

## 1. Overview

Extend the OS configuration export (`os-ecuc-export`) to include three additional semantic entity types from AUTOSAR ECUC:

- **OsAlarm** — asynchronous alarm with action (task activation, event setting, counter increment, or callback)
- **OsIsr** — interrupt service routine with category, priority, and optional timing protection
- **OsScheduleTable** — statically defined set of timed alarm actions with expiry points

Currently, `OsApplication` stores these as string references. The enhancement builds complete object representations following the existing `OsTask`/`OsApplication` pattern.

---

## 2. Data Model Classes

All classes follow py-armodel conventions:
- Getters/setters with method chaining (return `self`)
- Camel-case AUTOSAR property names (`osAlarmCounterRef`, not `os_alarm_counter_ref`)
- Optional fields use `Optional[T]` from `typing` (Python 3.8+ compatible)
- Lists use `List[T]`
- No default values; all start as `None` or `[]`

### 2.1 OsAlarm

**File:** `src/armodel/data_models/ecuc/os.py`

```python
class OsAlarm:
    """AUTOSAR OS alarm as defined by SWS_Os_00114."""
    
    # Core properties
    name: str
    osAlarmCounterRef: Optional[str]           # Reference to counter
    osAlarmAccessingApplication: List[str]     # Application references
    
    # Action fields (all optional, mutually exclusive)
    osAlarmActivateTaskRef: Optional[str]      # Task to activate
    osAlarmSetEventTaskRef: Optional[str]      # Task that receives event
    osAlarmSetEventRef: Optional[str]          # Event reference
    osAlarmIncrementCounterRef: Optional[str]  # Counter to increment
    osAlarmCallbackName: Optional[str]         # Callback function name
    
    # Autostart configuration (sub-container)
    osAlarmAlarmTime: Optional[int]            # Initial offset (ticks)
    osAlarmAutostartType: Optional[str]        # ABSOLUTE or RELATIVE
    osAlarmCycleTime: Optional[int]            # Period (ticks) for periodic alarms
    osAlarmAppModeRef: Optional[str]           # App mode for autostart
```

Methods: `getName()`, `setName()`, `getOsAlarmCounterRef()`, `setOsAlarmCounterRef()`, etc.  
List methods: `getOsAlarmAccessingApplications()`, `addOsAlarmAccessingApplication()`

---

### 2.2 OsIsr

**File:** `src/armodel/data_models/ecuc/os.py`

```python
class OsIsr:
    """AUTOSAR OS interrupt service routine as defined by SWS_Os_00128."""
    
    # Core properties
    name: str
    osIsrName: Optional[str]                   # C function name
    osIsrCategory: Optional[str]               # CATEGORY_1 or CATEGORY_2
    osIsrPriority: Optional[int]               # Priority (category 2 only)
    osIsrInterruptSource: Optional[str]        # Hardware interrupt reference
    osIsrAccessingApplication: List[str]       # Application references
    
    # Timing Protection (optional, sub-container OsIsrTimingProtection)
    osIsrExecutionBudget: Optional[float]      # Execution time budget
    osIsrTimeFrame: Optional[float]            # Arrival protection window
    osIsrAllInterruptLockBudget: Optional[float]
    osIsrOsInterruptLockBudget: Optional[float]
    
    # Resource Locks (optional, sub-container OsIsrResourceLock)
    osIsrResourceLockBudget: List[float]       # Lock budgets per resource
    osIsrResourceLockResourceRef: List[str]    # Resource references
```

Methods: Similar getter/setter pattern to `OsTask`

---

### 2.3 OsScheduleTableExpiryPoint

**File:** `src/armodel/data_models/ecuc/os.py` (nested or separate, TBD)

```python
class OsScheduleTableExpiryPoint:
    """Single expiry point within an OsScheduleTable."""
    
    # Timing
    osScheduleTableExpiryPointOffset: Optional[float]    # Offset in counter ticks
    osScheduleTableMaxShorten: Optional[float]           # Max reduction (sync)
    osScheduleTableMaxLengthen: Optional[float]          # Max extension (sync)
    
    # Action fields (all optional, mutually exclusive)
    osScheduleTableTaskActivationRef: Optional[str]      # Task to activate
    osScheduleTableEventSettingTaskRef: Optional[str]    # Task for event
    osScheduleTableEventSettingRef: Optional[str]        # Event reference
```

Methods: `getOffset()`, `setOffset()`, `getOsScheduleTableMaxShorten()`, etc.

---

### 2.4 OsScheduleTable

**File:** `src/armodel/data_models/ecuc/os.py`

```python
class OsScheduleTable:
    """AUTOSAR OS schedule table as defined by SWS_Os_00232."""
    
    # Core properties
    name: str
    osScheduleTableCounterRef: Optional[str]   # Reference to counter
    osScheduleTableDuration: Optional[float]   # Duration in ticks
    osScheduleTableAccessingApplication: List[str]
    
    # Expiry points
    osScheduleTableExpiryPoint: List[OsScheduleTableExpiryPoint]
    
    # Autostart configuration (sub-container)
    osScheduleTableAutostartType: Optional[str]         # ABSOLUTE/RELATIVE
    osScheduleTableAutostartValue: Optional[int]        # Initial offset
    osScheduleTableAutostartAppModeRef: Optional[str]   # App mode
    
    # Synchronization (sub-container OsScheduleTableSync)
    osScheduleTableSyncStrategy: Optional[str]          # IMPLICIT/EXPLICIT
    osScheduleTableSyncNetRefValue: Optional[float]
```

Methods: Similar getter/setter pattern; `getOsScheduleTableExpiryPoints()`, `addOsScheduleTableExpiryPoint()`

---

### 2.5 OsOs Changes

**File:** `src/armodel/data_models/ecuc/os.py`

Add three new collections to existing `OsOs` class:

```python
class OsOs:
    # ... existing fields ...
    osAlarm: List[OsAlarm] = []
    osIsr: List[OsIsr] = []
    osScheduleTable: List[OsScheduleTable] = []
    
    # New methods
    def getOsAlarms(self) -> List[OsAlarm]:
        return self.osAlarm
    
    def addOsAlarm(self, value: OsAlarm) -> "OsOs":
        self.osAlarm.append(value)
        return self
    
    # Similar for osIsr and osScheduleTable
```

---

## 3. Parser Changes

**File:** `src/armodel/parser/os_ecuc_parser.py`

### 3.1 New Methods

Add to `OsEcucParser`:

```python
def get_collect_alarm(self, alarm: OsAlarm, container: Container, 
                      index: Dict[str, Container], warning: bool) -> None:
    """Extract OsAlarm parameters from ECUC container."""
    # Similar structure to get_collect_task()
    # Parse parameters: OsAlarmAlarmTime, OsAlarmCycleTime, OsAlarmAutostartType
    # Parse references: OsAlarmCounterRef, OsAlarmActivateTaskRef, etc.
    # Handle sub-containers: OsAlarmAutostart, OsAlarmAction
    pass

def get_collect_isr(self, isr: OsIsr, container: Container,
                    index: Dict[str, Container], warning: bool) -> None:
    """Extract OsIsr parameters from ECUC container."""
    # Parse: OsIsrCategory, OsIsrPriority, OsIsrName
    # Parse refs: OsIsrInterruptSource, OsIsrAccessingApplication
    # Handle sub-containers: OsIsrTimingProtection, OsIsrResourceLock
    pass

def get_collect_schedule_table(self, sched_table: OsScheduleTable, 
                               container: Container, 
                               index: Dict[str, Container], warning: bool) -> None:
    """Extract OsScheduleTable and expirypoints from ECUC container."""
    # Parse: OsScheduleTableDuration, OsScheduleTableCounterRef
    # Iterate sub-containers: OsScheduleTableExpiryPoint
    # For each expiry point, extract offset, max shorten/lengthen, action fields
    pass
```

### 3.2 Integration into parseEcuc()

In `parseEcuc()` method, add parsing phases (after task/application parsing):

```python
# Phase 1: Collect containers by definition name
# Phase 2: Create OsTask objects → populate OsOs.osTask
# Phase 3: Create OsApplication objects → populate OsOs.osApplication
# Phase 4: Create OsAlarm objects → populate OsOs.osAlarm
# Phase 5: Create OsIsr objects → populate OsOs.osIsr
# Phase 6: Create OsScheduleTable objects → populate OsOs.osScheduleTable
# Phase 7: Resolve cross-references (task→app, app→task, app→alarm, etc.)
```

---

## 4. Exporter Changes

**File:** `src/armodel/report/os_export.py`

### 4.1 OsConfigModelMapper

Add to `OsConfigModelMapper`:

```python
def alarm_to_dict(self, alarm: OsAlarm) -> Dict[str, Any]:
    """Convert OsAlarm to exportable dictionary."""
    return {
        "name": alarm.getName(),
        "OsAlarmCounterRef": alarm.getOsAlarmCounterRef(),
        "OsAlarmActivateTaskRef": alarm.getOsAlarmActivateTaskRef(),
        "OsAlarmSetEventTaskRef": alarm.getOsAlarmSetEventTaskRef(),
        "OsAlarmSetEventRef": alarm.getOsAlarmSetEventRef(),
        "OsAlarmIncrementCounterRef": alarm.getOsAlarmIncrementCounterRef(),
        "OsAlarmCallbackName": alarm.getOsAlarmCallbackName(),
        "OsAlarmAlarmTime": alarm.getOsAlarmAlarmTime(),
        "OsAlarmAutostartType": alarm.getOsAlarmAutostartType(),
        "OsAlarmCycleTime": alarm.getOsAlarmCycleTime(),
        "OsAlarmAppModeRef": alarm.getOsAlarmAppModeRef(),
        "OsAlarmAccessingApplication": list(alarm.getOsAlarmAccessingApplications()),
    }

def isr_to_dict(self, isr: OsIsr) -> Dict[str, Any]:
    """Convert OsIsr to exportable dictionary."""
    # Similar structure, all optional fields

def schedule_table_to_dict(self, sched_table: OsScheduleTable) -> Dict[str, Any]:
    """Convert OsScheduleTable to exportable dictionary."""
    # Include expirypoint list with nested dicts
    # Each expirypoint as dict with offset, action fields, etc.
```

### 4.2 to_dict() Update

Update `OsConfigModelMapper.to_dict()`:

```python
def to_dict(self, os_os: OsOs) -> Dict[str, List[Dict[str, Any]]]:
    return {
        "OsApplication": [...],
        "OsTask": [...],
        "OsAlarm": [self.alarm_to_dict(a) for a in os_os.getOsAlarms()],
        "OsIsr": [self.isr_to_dict(i) for i in os_os.getOsIsrs()],
        "OsScheduleTable": [self.schedule_table_to_dict(s) for s in os_os.getOsScheduleTables()],
    }
```

### 4.3 Exporters

Both `OsConfigYamlExporter` and `OsConfigXlsxExporter` already use `mapper.to_dict()`, so no changes needed (auto-includes new sheets).

---

## 5. Integration Points

### 5.1 Bi-directional References

**OsApplication → Alarms/Isrs/ScheduleTables:**
- `OsApplication.osAppAlarmRef` (already exists as string list)
- `OsApplication.osAppIsrRef` (already exists as string list)
- `OsApplication.osAppScheduleTableRef` (already exists as string list)
- These remain as string paths; no object reference needed (one-way)

**Reverse (optional, for graph queries):**
- Could add `OsAlarm.osAlarmAccessingApplication` to track which apps reference it
- Already in data model above; populated during parsing

### 5.2 Duplicate UUID Checking

Standard ARXMLParser already checks for duplicate UUIDs. No additional validation needed.

### 5.3 Warning Mode

All three new parsers follow `OsEcucParser.get_lookup_*()` pattern:
- `warning=True` → log unresolved references, continue
- `warning=False` → raise `OsEcucConversionError` on missing references

---

## 6. Data Flow

```
ARXML file
    ↓
ARXMLParser.load()
    ↓
OsEcucParser.parseEcuc()
    ├─ get_modules() → find Os module
    ├─ get_module_containers() → index all ECUC containers
    ├─ collect OsTask → OsOs.osTask
    ├─ collect OsApplication → OsOs.osApplication
    ├─ collect OsAlarm → OsOs.osAlarm          [NEW]
    ├─ collect OsIsr → OsOs.osIsr              [NEW]
    ├─ collect OsScheduleTable → OsOs.osScheduleTable [NEW]
    └─ resolve cross-references
    ↓
OsOs (in-memory semantic model)
    ├─ osApplication[]: List[OsApplication]
    ├─ osTask[]: List[OsTask]
    ├─ osAlarm[]: List[OsAlarm]               [NEW]
    ├─ osIsr[]: List[OsIsr]                   [NEW]
    └─ osScheduleTable[]: List[OsScheduleTable] [NEW]
    ↓
OsConfigExporter
    ├─ OsConfigYamlExporter
    └─ OsConfigXlsxExporter
    ↓
Output: YAML or XLSX with 5 sheets
    ├─ OsApplication
    ├─ OsTask
    ├─ OsAlarm              [NEW]
    ├─ OsIsr                [NEW]
    └─ OsScheduleTable      [NEW]
```

---

## 7. Testing Strategy

### 7.1 Unit Tests

**File:** `tests/test_armodel/data_models/ecuc/test_os.py`

- Constructor + method chaining for each class
- Getters/setters return correct types
- Lists initialize empty, can append/retrieve

### 7.2 Integration Tests

**File:** `tests/integration_tests/test_os_ecuc_parser.py` (create or extend)

- Parse Os_ECUC.arxml (already has OsAlarm examples)
- Verify OsAlarm objects created with correct properties
- Create/add OsIsr and OsScheduleTable examples to test file
- Round-trip: parse → export YAML → re-parse → compare

### 7.3 Exporter Tests

**File:** `tests/integration_tests/test_os_export.py` (create or extend)

- Export OsAlarm/OsIsr/OsScheduleTable to YAML
- Verify sheet names and column headers in XLSX
- Check filtering (None values, empty lists excluded)

---

## 8. Scope & Constraints

### 8.1 Out of Scope

- Validation rules (e.g., "OsAlarmCounterRef must exist")
  - Handled by warning mode during parsing
- Memory protection configuration (separate ECUC domains)
- Multi-core specific ISR affinity (handled as string reference)
- ARTI (AUTOSAR Runtime for Integration) objects

### 8.2 Backwards Compatibility

- Existing `OsApplication.osAppAlarmRef` (string list) unchanged
- Existing exporters auto-include new sheets (no format change to old sheets)
- Old code can ignore new lists; `OsOs` remains extensible

### 8.3 Limitations

- OsAlarmAction is flat, not strongly typed (user must check which field is populated)
  - By design per Option C discussion
- OsScheduleTable.expiryPoints stored as simple DTO list, no lazy loading
- No schema validation against AUTOSAR PDF (parser is permissive)

---

## 9. File Changes Summary

| File | Change | LOC |
|------|--------|-----|
| `src/armodel/data_models/ecuc/os.py` | Add 4 new classes | ~800 |
| `src/armodel/parser/os_ecuc_parser.py` | Add 3 collection + 3 resolve methods | ~400 |
| `src/armodel/report/os_export.py` | Add 3 to_dict() methods | ~150 |
| `tests/integration_tests/test_files/Os_ECUC.arxml` | Add OsIsr + OsScheduleTable examples | ~200 |
| `tests/integration_tests/test_files/Os_ECUC.yaml` | Add 3 new sections | ~100 |
| Test new classes | Unit + integration | ~300 |
| **Total** | | **~1950** |

---

## 10. Success Criteria

✅ OsAlarm objects parsed from ECUC and exported to YAML/XLSX  
✅ OsIsr objects parsed from ECUC and exported to YAML/XLSX  
✅ OsScheduleTable objects with expirypoints parsed and exported  
✅ All integration tests pass (round-trip integrity)  
✅ `python scripts/run_tests.py` passes with 100% new code coverage  
✅ No breaking changes to existing OsApplication/OsTask/OsOs APIs  
✅ CLI tool `arxml-os-config` works with enhanced export  

---

## 11. Implementation Phases

**Phase 1: Data Models** (os.py)
- Add 4 new classes with getters/setters
- Add OsOs.osAlarm/osIsr/osScheduleTable fields + methods

**Phase 2: Parser** (os_ecuc_parser.py)
- Implement get_collect_*() methods
- Integrate into parseEcuc() flow
- Add warning mode handling

**Phase 3: Exporter** (os_export.py)
- Add mapper methods
- Update to_dict() to include new sections
- Verify YAML/XLSX sheet generation

**Phase 4: Testing**
- Unit tests for all classes
- Integration tests with Os_ECUC.arxml
- Add OsIsr/OsScheduleTable examples to test file

---

## Appendix: AUTOSAR References

- SWS_Os_00114 — OsAlarm definition
- SWS_Os_00128 — OsIsr definition
- SWS_Os_00232 — OsScheduleTable definition
- AUTOSAR_CP_SWS_OS.md § 10.2 (ECUC configuration tables)

