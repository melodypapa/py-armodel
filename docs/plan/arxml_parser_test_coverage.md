# Improve ARXML Parser Test Coverage (62.9% → ~85%+)

> Living documentation for the ARXML parser test coverage improvement effort.
> Update this file at the end of each phase with actual test counts and coverage numbers.

## Goal

Drive line coverage of `src/armodel/parser/arxml_parser.py` (5,941 lines, currently 62.9%) to **85%+** by adding targeted unit tests across four focus areas: complex orchestrators, communication & network, BSW module behavior, and error/edge cases. Follow established patterns from commit `279a375f` (the recent 240-test batch).

## Starting State

- `arxml_parser.py`: 5,941 lines, 62.9% covered (~2,200 lines uncovered)
- `abstract_arxml_parser.py`: 98.7% covered (already excellent — leave alone)
- Total passing tests: 2,599; parser-specific tests: 340
- Recent batch of 240 tests added only ~2 points (most verified dispatch routing, not handler bodies)

## Established Patterns to Follow

Minimal XML snippet + direct handler invocation, with these standard fixtures/helpers per file:

```python
NS = "http://autosar.org/schema/r4.0"

@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()

@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()

@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})

def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")

def _autosar_root():
    return AUTOSAR.getInstance()
```

Three test styles (per commit `279a375f`):
- **Dispatch test** — route through `readARPackageElements`, assert object creation
- **Handler test** — invoke specific `readXxx`/`getXxx` directly with minimal XML, assert model state
- **Error/warning test** — use `warning_parser` + `caplog.at_level(logging.ERROR)` to assert else/raise branches log without raising

## File Strategy

Create 4 new files; extend 4 existing files. All paths under `D:\workspace\py-armodel\tests\test_armodel\parser\`.

| Action | File | Phase |
|--------|------|-------|
| New | `test_arxml_parser_bsw_handlers.py` | F |
| New | `test_arxml_parser_network_handlers.py` | G |
| New | `test_arxml_parser_orchestrators.py` | H |
| New | `test_arxml_parser_warning_branches.py` | I |
| Extend | `test_arxml_parser_error_paths.py` | I |
| Extend | `test_arxml_parser_internals.py` | J |
| Extend | `test_arxml_parser_handlers.py` (new Group F) | K |
| Extend | `test_arxml_parser_snippets.py` | L |

## Phased Implementation

### Phase F — BSW Module Behavior (~88 tests)
**File:** `test_arxml_parser_bsw_handlers.py` (new)

Target the BSW area (lines 461-1148). Test classes:
- `TestBswModuleDescriptionHandlers` — `readBswModuleDescription` orchestrator + provided/required mode groups, datas, client/server entries, triggers (L461-510, 1040-1100)
- `TestBswModuleEntryHandlers` — `readBswModuleEntry`, `readSwServiceArg`, `readBswModuleEntryArguments/ReturnType`, `readBswModuleClientServerEntry` (L1076-1148)
- `TestBswInternalBehaviorOrchestrator` — `readBswInternalBehavior` full orchestration, internal triggering points, reception policies, mode sender policy, entities dispatch, events dispatch (L540-546, 928-1028)
- `TestBswModuleEntityHandlers` — `readBswModuleEntity` + send/receive/call points, trigger refs, managed mode groups; `readBswCalledEntity/SchedulableEntity/InterruptEntity`; call point variants (L501-535, 851-926)
- `TestBswInternalBehaviorEventsDetailed` — one test per BSW event type (L513-534, 943-950)
- `TestBswReceptionAndApiOptions` — `readBswApiOptions`, reception policies, `readBswInternalTriggeringPoint`, `readBswVariableAccess` (L851, 981-1006)

### Phase G — Communication & Network (~187 tests)
**File:** `test_arxml_parser_network_handlers.py` (new)

Largest contiguous uncovered region (lines 2750-5350). Test classes:
- `TestCanClusterHandlers` (~15) — cluster variants, busOffRecovery, baudrate, physical channels (L3491-3538)
- `TestLinClusterHandlers` (~10) — cluster, physical channel, schedule tables, frame triggering, comm controller/connector (L3022-3169, 4883-4966)
- `TestFlexrayClusterHandlers` (~12) — cluster, physical channel, frame triggering, scheduled timings, cycle repetition (L3028-3061, 3487, 3545, 4256-4260, 4969)
- `TestEthernetClusterHandlers` (~25) — cluster, MAC multicast, physical channel, VLAN, network endpoints, IPv6, DoIp, comm controller, coupling ports/FIFO/scheduler (L3173-3597, 4804-4961)
- `TestSoAdAndSocketHandlers` (~25) — SoAd config, socket addresses, application endpoints, consumed/provided service instances, event handlers, SD configs, connection bundles, socket connections/PDUs (L3232-3466)
- `TestTransportProtocolHandlers` (~10) — UDP/TCP/Generic TP configs, TP port (L3279-3303)
- `TestFrameAndPduHandlers` (~20) — frame/pdu triggering, ISignal triggering, physical channel orchestrator, all PDU variants, frame mappings (L3004-3131, 3837-3890)
- `TestISignalAndGroupHandlers` (~6) — ISignal, ISignalIPdu, transmission mode timing, data filter, ISignalIPduGroup (L5055, 5263-5354)
- `TestEndToEndProtectionHandlers` (~10) — set, protections, variable prototypes, ISignalIPdu refs, description, data IDs (L2758-2841)
- `TestNmConfigHandlers` (~18) — NM config orchestrator, ECU/cluster/node/coupling variants, secured IPdu (L3895-4074)
- `TestCanTpAndLinTpHandlers` (~18) — CanTp config, nodes, ECUs, connections, channels, addresses; LinTp config (L4085-4245)
- `TestEcuInstanceHandlers` (~18) — orchestrator, comm controllers (CAN/LIN/FlexRay/Ethernet), connectors, comm port instances (L4740-4995)

### Phase H — Complex Orchestrators (~250 tests)
**File:** `test_arxml_parser_orchestrators.py` (new)

Deep call-graph coverage (lines 426-2700, 5020-5640). Test classes:
- `TestSwcInternalBehaviorOrchestrator` (~20) — full orchestrator + per-instance memories, events, explicit inter-runnable variables, mode declaration group sets, port API options, runnables, service dependencies, shared parameters, role-based assignments (L587-842, 1466-1602)
- `TestServiceNeedsHandlers` (~12) — one test per needs type: NvBlock, DiagCommManager, DiagRoutine, DiagValue, DiagEvent, DiagEventInfo, Crypto, EcuStateMgr, DtcStatusChange, DltUser; plus debounce monitors (L633-725)
- `TestRunnableEntityOrchestrator` (~30) — full orchestrator + arguments, async server call result points, all 5 variable-access types, sync/async server call points, internal triggering points, mode access/switch points, parameter accesses, local variables (L426, 1254-1445)
- `TestRteEventHandlers` (~15) — `readRTEEvent`, operation invoked, timing, data received/sent, mode switch, internal trigger, init, async server call returns, mode switch ack, background (L1321-1597)
- `TestSwComponentTypeDeepHandlers` (~20) — port groups, all 5 provided com specs + 6 required com specs, port prototypes, composition orchestrator + components/connectors, assembly/delegation connectors (L1940-2384)
- `TestPortInterfaceHandlers` (~15) — sender/receiver, client/server (operations, arguments, possible errors), parameter, nvdata, data, mode switch, trigger interfaces (L2410-2528, 2937-2963)
- `TestDataTypeAndCompuHandlers` (~25) — CompuMethod (constant/rational/scale), DataConstr rules, Unit, ApplicationPrimitive/Record/Array data types, ImplementationDataType sub-elements, SwBaseType, SwRecordLayout, SwAddrMethod (L1860-1997, 2571-2928)
- `TestValueSpecificationHandlers` (~12) — all 6 value spec branches + application/numerical/text/array/constant reference + record fields + sw values/value cont/value list (L1952-1999, 2639-2704)
- `TestSystemAndMappingHandlers` (~30) — system orchestrator, fibex refs, root sw composition (incl. ValueError→raiseWarning path), system/data/sw/impl/ECU mappings, sender/receiver record & array element mappings, gateway (L5020-5513)
- `TestEcucDefAndValueHandlers` (~30) — ECUC value collection, parameter values, all ECUC def/description handlers (L4453-4669, 5065-5250)
- `TestLifeCycleAndVariantHandlers` (~12) — life cycle info set/info, predefined variant, sw systemconst/value sets, flat map, flat instance descriptor (L4676-4731, 5517-5569)
- `TestImplementationsHandlers` (~12) — code/artifact descriptors, engineering objects, resource consumption, memory sections/stack/heap, BSW/Swc implementation, SwcBsw mapping (L1149-1246, 2625-2632)
- `TestTimingAndExecutionOrderHandlers` (~6) — swc timing, timing extension, execution order constraint + ordered elements (L2968-2999)
- `TestPortInterfaceMappingHandlers` (~10) — port interface mapping set, variable/parameter mapping, client/server operation mapping (L5574-5640)

### Phase I — Edge Cases & Warning-Mode Branches (~93 tests)
**Files:** `test_arxml_parser_warning_branches.py` (new) + `test_arxml_parser_error_paths.py` (extend)

Target every `else`/`raiseError`/`notImplemented`/`raiseWarning` branch. Test classes:
- `TestWarningModeFallbackBranches` (~60, parametrized where possible) — one test per `notImplemented`/`raiseError` site across all readers (use `warning_parser` + `caplog` pattern from `test_arxml_parser_error_paths.py` lines 61-86)
- `TestOptionalGetterDefensivePaths` (~15) — `None`-return branches of `get*` helpers (variable refs, component refs, multilanguage paragraphs/plaintexts, sw pointer/data def props)
- `TestRaiseWarningFallbacks` (~10) — `raiseWarning` and try/except paths; specifically `readRootSwCompositionPrototype` (L5494) ValueError→raiseWarning
- `TestLoadAndDispatchBoundaries` (~8) — `load()` error cases, empty `AR-PACKAGES`/`ELEMENTS`, `readReferenceBases` present/absent, `readARPackage` orchestrator

### Phase J — Documentation & Internal Helpers (~45 tests)
**File:** `test_arxml_parser_internals.py` (extend)

Cover lines 255-1830 documentation/SDG blocks. Test classes:
- `TestDocumentationBlockHandlers` (~12) — `readDocumentationBlock`, `getDocumentationBlock(List)`, LParagraphs, multi-language paragraphs/plaintexts, list elements, language-specific (L1655-1763)
- `TestGraphicAndFigureHandlers` (~8) — `getGraphic`, `readMlFigure`, LGraphics, document view selectable, paginateable, mlFigures list (L1701-1728)
- `TestAnnotationHandlers` (~6) — `getAnnotations`, `readGeneralAnnotation` (L1771-1776)
- `TestSwDataDefPropsHandlers` (~10) — sw data def props, invalid value, sw pointer target props, sw axis individual/grouped/calprm/set, composite network representation, application composite element in port interface instance ref (L1638-1647, 1788-1933)
- `TestSdgDeepHandlers` (~6) — SDG with nested SDG/SDG-CAPTION/SDX-REF, admin data SDGs/doc revisions/modifications, else branches (L264-315)
- `TestDescribableHandlers` (~3) — `readDescribable`, transformation description, end-to-end transformation description (L4325-4331)

### Phase K — Misc Handlers Group F (~23 tests)
**File:** `test_arxml_parser_handlers.py` (extend, new `TestMiscHandlersGroupF`)

Cover lines 4290-4450. Test classes:
- `TestDataTransformationHandlers` (~10) — `readDataTransformationSet` orchestrator, transformation technologies, transformation descriptions, data transformations + buffer properties (L4290-4378)
- `TestKeywordAndCollectionHandlers` (~6) — `readKeywordSet/Keywords`, `readKeyword/Classifications`, `readCollection` + element refs (L4384-4419)
- `TestModeDeclarationMappingHandlers` (~4) — `readModeDeclarationMappingSet/Mappings`, `readModeDeclarationMapping`, first mode refs, port prototype blueprint (L4424-4448)
- `TestModeDeclarationGroupPrototypeHandlers` (~3) — `readModeDeclarationGroupPrototype` (L468)

### Phase L — Real-ARXML Round-Trip Catch-Alls (~10 tests)
**File:** `test_arxml_parser_snippets.py` (extend, `TestRealArxmlRoundTripBranches`)

Load real test files and assert presence of key elements (catch-all for nested paths hard to reach via snippets):
- `CanSystem.arxml` → CanClusters, PhysicalChannels, ISignals, ISignalIPdus, SystemSignals, EcuInstances, Gateways, Mappings
- `BswM_Bswmd.arxml` → BswModuleDescriptions, BswInternalBehaviors, Entities, Events
- `SoftwareComponents.arxml` → SwComponentTypes, SwcInternalBehaviors, Runnables, Events
- `AUTOSAR_Datatypes.arxml` → ImplementationDataTypes, CompuMethods, DataConstrs, Units, SwBaseTypes

## Expected Coverage Trajectory

| Phase | Tests | Coverage Delta | Cumulative |
|-------|-------|----------------|------------|
| Start | — | — | 62.9% |
| F | ~88 | +3.1 | ~66% |
| G | ~187 | +8 | ~74% |
| H | ~250 | +8 | ~82% |
| I | ~93 | +2 | ~84% |
| J | ~45 | +1.5 | ~85.5% |
| K | ~23 | +0.5 | ~86% |
| L | ~10 | +1 | ~87% |
| **Total** | **~596** | | **~86-87%** |

## Actual Progress

| Phase | Tests Added | Coverage After | Notes |
|-------|-------------|----------------|-------|
| Start | — | 62.9% | baseline |
| F | 80 | 68% | Exceeded +3.1 estimate; BSW handlers are deep |
| G | — | — | pending |
| H | — | — | pending |
| I | — | — | pending |
| J | — | — | pending |
| K | — | — | pending |
| L | — | — | pending |

## Critical Files

**Source under test:**
- `D:\workspace\py-armodel\src\armodel\parser\arxml_parser.py` (5,941 lines)

**Reference test files (read before writing):**
- `D:\workspace\py-armodel\tests\test_armodel\parser\test_arxml_parser_handlers.py` — fixture/helper template (lines 26-55) and Groups A-E class layout
- `D:\workspace\py-armodel\tests\test_armodel\parser\test_arxml_parser_dispatch.py` — `_dispatch` helper (lines 53-61) — avoid duplicating dispatch routing already covered here
- `D:\workspace\py-armodel\tests\test_armodel\parser\test_arxml_parser_error_paths.py` — `caplog` assertion pattern (lines 61-86) and `warning_parser` fixture (lines 40-44)
- `D:\workspace\py-armodel\tests\test_armodel\parser\test_arxml_parser_internals.py` — internal-method test style

**Helpers:**
- `D:\workspace\py-armodel\src\armodel\parser\abstract_arxml_parser.py` — defines `getChildElementOptional*`, `find`, `findall`, `raiseError`, `notImplemented` referenced throughout

## Verification

After each phase, in this order:

1. **Run the new file with coverage on the parser only:**
   ```bash
   pytest tests/test_armodel/parser/test_arxml_parser_<phase>.py --cov=armodel.parser.arxml_parser --cov-report term-missing
   ```
   Confirm targeted methods turn green and the line coverage number increased vs. previous phase.

2. **Full regression run:**
   ```bash
   python scripts/run_tests.py
   ```
   All previous tests + new ones must pass. No flaky behavior, no skipped-by-error tests.

3. **Lint check on new files:**
   ```bash
   flake8 --select=E9,F63,F7,F82 tests/test_armodel/parser/test_arxml_parser_<phase>.py
   ```
   Must return 0. Also check complexity/line-length warnings:
   ```bash
   flake8 --max-complexity=10 --max-line-length=127 tests/test_armodel/parser/test_arxml_parser_<phase>.py
   ```

4. **Visual confirmation (optional but recommended):**
   ```bash
   pytest --cov=armodel.parser.arxml_parser --cov-report html:coverage_html
   ```
   Open `coverage_html/armodel/parser/arxml_parser_py.html` and verify previously-red methods are now green. Note any remaining uncovered regions for follow-up in next phase.

5. **Final phase: regenerate the project coverage report:**
   ```bash
   python scripts/run_tests.py --coverage
   ```
   Confirm `arxml_parser.py` line coverage is 85%+ and `reports/coverage.md` reflects the new numbers.

## Quality Gates (Per Phase)

Before marking a phase complete:
- All new tests pass
- No regression in existing tests (2,599 baseline)
- Lint clean on new test file(s)
- Coverage gain observed on targeted methods in HTML report
- Tests assert only on public getters (no `_private` attribute access) unless following an established documented exception

## Notes

- Use `warning_parser` for tests that exercise else/raiseError branches — these branches log rather than throw, so caplog assertions are the right tool
- Prefer parametrized tests where only the XML tag name varies (compresses Phase I significantly)
- For orchestrator tests (Phase H), build rich XML fixtures that populate multiple sub-elements in a single test — each test exercises 10-40 lines of dispatch logic
- Avoid re-testing dispatch routing already covered in `test_arxml_parser_dispatch.py` — focus on handler bodies
- Some branches may be unreachable in normal operation (dead code, impossible state). Document these in `tests/test_armodel/parser/COVERAGE_PROGRESS.md` rather than forcing coverage with brittle tests
