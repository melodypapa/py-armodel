# ECUC Handler Test Coverage Design

## Goal

Improve arxml_parser.py coverage from 86.47% to ~90%+ by adding tests for uncovered ECUC (ECU Configuration) parsing handlers.

## Target Gaps

Current uncovered ECUC regions (53 lines total):

| Lines | Handler | Size |
|-------|---------|------|
| 4576-4595 | `readEcucContainerDefParameters` | 20 |
| 4507-4515 | `readEcucCommonAttributes` | 9 |
| 4615-4622 | `readEcucContainerDefReferences` | 8 |
| 4627-4634 | `readEcucContainerDefSubContainers` | 8 |
| 779-786 | `getIncludedDataTypeSets` | 8 |

## Approach

Create a new dedicated test file following the established pattern from Phase F/G/H test files.

## File Structure

**New file:** `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

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

## Test Classes

### TestEcucContainerDefParameters (~15 tests)

Tests for `readEcucContainerDefParameters` covering:

- `ECUC-PARAM-CONF-CONTAINER-DEF` with BOOLEAN parameters
- `ECUC-PARAM-CONF-CONTAINER-DEF` with STRING parameters
- `ECUC-PARAM-CONF-CONTAINER-DEF` with INTEGER parameters
- `ECUC-PARAM-CONF-CONTAINER-DEF` with FLOAT parameters
- `ECUC-PARAM-CONF-CONTAINER-DEF` with ENUMERATION parameters
- `ECUC-PARAM-CONF-CONTAINER-DEF` with FUNCTION-NAME parameters
- Each with variants: with value, without value, with defaults, with limits

### TestEcucCommonAttributes (~8 tests)

Tests for `readEcucCommonAttributes` covering:

- `lowerMultiplicity` / `upperMultiplicity`
- `multiplicityClasses` (lower/upper)
- `origin` attribute
- `postBuildVariant` attributes

### TestEcucContainerDefReferences (~7 tests)

Tests for `readEcucContainerDefReferences` covering:

- `ECUC-REFERENCE-DEF` element parsing
- `ECUC-FOREIGN-REFERENCE-DEF` variants
- Reference type attributes

**Total: ~30 focused tests** targeting 53 uncovered lines.

## Test Data Strategy

- Use inline XML snippets via `_snip()` helper
- Each test creates minimal XML elements to exercise specific code paths
- No external test files needed — keeps tests self-contained

**Example test pattern:**

```python
def test_readEcucBooleanParamDef_with_value(self, parser):
    xml = '''
    <ECUC-PARAM-CONF-CONTAINER-DEF UUID="test-uuid">
        <SHORT-NAME>ContainerDef</SHORT-NAME>
        <PARAMETERS>
            <ECUC-BOOLEAN-PARAM-DEF>
                <SHORT-NAME>EnableFeature</SHORT-NAME>
                <VALUE>true</VALUE>
            </ECUC-BOOLEAN-PARAM-DEF>
        </PARAMETERS>
    </ECUC-PARAM-CONF-CONTAINER-DEF>
    '''
    elem = _snip(xml, "ECUC-PARAM-CONF-CONTAINER-DEF")
    parser.readEcucContainerDefParameters(elem, container, _autosar_root())
    # Assert parameter was parsed correctly
```

## Verification

1. Run tests: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py -v`
2. Coverage check: `pytest --cov=armodel.parser.arxml_parser --cov-report=term-missing`
3. Target: Reduce uncovered ECUC lines from 53 to <10

## Success Criteria

- All ~30 tests pass
- Coverage increases from 86.47% to ~90%+
- No regressions in existing tests