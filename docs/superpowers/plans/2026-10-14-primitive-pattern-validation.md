# Primitive Pattern Validation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enforce the spec regex (`PATTERN`) on `ARLiteral` values — always on — raising `PrimitivePatternError`, with the parser's `warning=True` option downgrading violations to `logger.warning`.

**Architecture:** Per-class `PATTERN: Optional[str]` attribute on `ARLiteral` subclasses (XSD-grounded, populated by an extraction script); a `checkValue` hook wired into the existing `value` setter; thread-local warning mode in `armodel/validation/` activated by `ARXMLParser.load()` when `options["warning"] is True`. Task 7 wires Rule 0028 into the `sync-autosar-class` skill (rules + audit) so future synced classes stay covered. Spec: `docs/superpowers/specs/2026-10-13-primitive-pattern-validation-design.md`.

**Tech Stack:** Python 3.8-compatible typing (`typing.Optional`, `typing.Dict` — NEVER `T | None`), stdlib `re` + `threading`, uv toolchain. Repo rules (AGENTS.md): Black 200-char, no comments in code, `uv run` for all commands, mypy must stay green.

**Work in:** repo root `/Users/ray/Workspace/py-armodel`, current feature branch (`feature/g21-sync-fixes` or successor). Verify first: `git branch --show-current`.

---

### Task 1: `PrimitivePatternError` + thread-local warning mode

**Files:**
- Create: `src/armodel/validation/exceptions.py`
- Create: `src/armodel/validation/pattern_context.py`
- Modify: `src/armodel/validation/__init__.py`
- Test: `tests/test_armodel/validation/test_pattern_context.py`

- [ ] **Step 1: Read current validation `__init__.py`**

Run: `cat src/armodel/validation/__init__.py`
Note existing re-exports (`ARXMLValidator`, `ValidationError`, ...) — keep them, append new ones.

- [ ] **Step 2: Write the failing tests**

Create `tests/test_armodel/validation/test_pattern_context.py`:

```python
import logging

import pytest

from armodel.validation import PrimitivePatternError, is_warning_mode, set_warning_mode, warning_mode


class TestPrimitivePatternError:
    def test_fields_and_message_with_xsd_type(self):
        error = PrimitivePatternError("MetaClassName", "bad-name", "[A-Z][a-zA-Z0-9_]*", "META-CLASS-NAME")
        assert error.class_name == "MetaClassName"
        assert error.value == "bad-name"
        assert error.pattern == "[A-Z][a-zA-Z0-9_]*"
        assert error.xsd_type == "META-CLASS-NAME"
        assert str(error) == 'value "bad-name" does not match pattern "[A-Z][a-zA-Z0-9_]*" (META-CLASS-NAME)'

    def test_fields_and_message_without_xsd_type(self):
        error = PrimitivePatternError("CIdentifier", "9bad", "[a-zA-Z_][a-zA-Z0-9_]*")
        assert error.xsd_type is None
        assert str(error) == 'value "9bad" does not match pattern "[a-zA-Z_][a-zA-Z0-9_]*" (CIdentifier)'

    def test_is_value_error(self):
        with pytest.raises(ValueError):
            raise PrimitivePatternError("X", "v", "p")


class TestWarningMode:
    def test_default_is_off(self):
        with warning_mode(False):
            assert is_warning_mode() is False

    def test_scoped_enable(self):
        assert is_warning_mode() is False
        with warning_mode(True, context="file.arxml"):
            assert is_warning_mode() is True
            from armodel.validation import get_context

            assert get_context() == "file.arxml"
        assert is_warning_mode() is False
        assert get_context() is None

    def test_nested_restore(self):
        with warning_mode(True, "outer"):
            with warning_mode(False):
                assert is_warning_mode() is False
            assert is_warning_mode() is True
            from armodel.validation import get_context

            assert get_context() == "outer"

    def test_set_warning_mode_direct(self):
        previous = is_warning_mode()
        try:
            set_warning_mode(True, "ctx")
            assert is_warning_mode() is True
        finally:
            set_warning_mode(previous)

    def test_thread_isolation(self):
        import threading

        result = {}

        def worker():
            result["mode"] = is_warning_mode()

        with warning_mode(True, "main"):
            thread = threading.Thread(target=worker)
            thread.start()
            thread.join()
        assert result["mode"] is False
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/validation/test_pattern_context.py -v`
Expected: FAIL — `ImportError: cannot import name 'PrimitivePatternError'`

- [ ] **Step 4: Implement `exceptions.py`**

Create `src/armodel/validation/exceptions.py`:

```python
from typing import Optional


class PrimitivePatternError(ValueError):
    def __init__(self, class_name: str, value: str, pattern: str, xsd_type: Optional[str] = None) -> None:
        self.class_name = class_name
        self.value = value
        self.pattern = pattern
        self.xsd_type = xsd_type
        type_label = xsd_type if xsd_type is not None else class_name
        super().__init__('value "%s" does not match pattern "%s" (%s)' % (value, pattern, type_label))
```

- [ ] **Step 5: Implement `pattern_context.py`**

Create `src/armodel/validation/pattern_context.py`:

```python
import threading
from contextlib import contextmanager
from typing import Optional

_local = threading.local()


def set_warning_mode(enabled: bool, context: Optional[str] = None) -> None:
    _local.pattern_warning = enabled
    _local.pattern_context = context if enabled else None


def is_warning_mode() -> bool:
    return getattr(_local, "pattern_warning", False)


def get_context() -> Optional[str]:
    return getattr(_local, "pattern_context", None)


@contextmanager
def warning_mode(enabled: bool, context: Optional[str] = None):
    previous_enabled = is_warning_mode()
    previous_context = get_context()
    set_warning_mode(enabled, context)
    try:
        yield
    finally:
        set_warning_mode(previous_enabled, previous_context)
```

- [ ] **Step 6: Re-export from `validation/__init__.py`**

Append to `src/armodel/validation/__init__.py` (keep existing imports; if the file uses `__all__`, extend it):

```python
from .exceptions import PrimitivePatternError
from .pattern_context import get_context, is_warning_mode, set_warning_mode, warning_mode
```

- [ ] **Step 7: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/validation/test_pattern_context.py -v`
Expected: 8 PASS

- [ ] **Step 8: Lint + format**

Run: `uv run ruff check src/armodel/validation tests/test_armodel/validation && uv run black src/armodel/validation tests/test_armodel/validation`
Expected: clean

- [ ] **Step 9: Commit**

```bash
git add src/armodel/validation/exceptions.py src/armodel/validation/pattern_context.py src/armodel/validation/__init__.py tests/test_armodel/validation/test_pattern_context.py
git commit -m "feat: add PrimitivePatternError and thread-local warning mode"
```

---

### Task 2: `ARLiteral.checkValue` hook

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py` (module header imports; `ARLiteral` class lines 59-112)
- Test: `tests/test_armodel/validation/test_arliteral_pattern.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_armodel/validation/test_arliteral_pattern.py`:

```python
import logging

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.validation import PrimitivePatternError, warning_mode


class _DummyLiteral(ARLiteral):
    PATTERN = r"[A-Z][a-zA-Z0-9_]*"


class _UnconstrainedLiteral(ARLiteral):
    pass


class TestCheckValue:
    def test_valid_value_accepted(self):
        literal = _DummyLiteral()
        literal.value = "Valid_Name2"
        assert literal.value == "Valid_Name2"

    def test_invalid_value_raises_by_default(self):
        with pytest.raises(PrimitivePatternError) as exc_info:
            _DummyLiteral().value = "9bad"
        assert exc_info.value.class_name == "_DummyLiteral"
        assert exc_info.value.value == "9bad"
        assert exc_info.value.pattern == r"[A-Z][a-zA-Z0-9_]*"

    def test_warning_mode_logs_and_keeps_value(self, caplog):
        literal = _DummyLiteral()
        with warning_mode(True, "test.arxml"), caplog.at_level(logging.WARNING, logger="armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes"):
            literal.value = "9bad"
        assert literal.value == "9bad"
        assert any("9bad" in record.message and "test.arxml" in record.message for record in caplog.records)

    def test_none_pattern_passthrough(self):
        literal = _UnconstrainedLiteral()
        literal.value = "anything ! goes"
        assert literal.value == "anything ! goes"

    def test_empty_string_passthrough(self):
        literal = _DummyLiteral()
        literal.value = ""
        assert literal.value == ""

    def test_nonempty_string_not_a_str_type_still_rejected(self):
        with pytest.raises(ValueError) as exc_info:
            _DummyLiteral().value = 123
        assert "Unsupported Type" in str(exc_info.value)

    def test_set_value_flows_through_check(self):
        literal = _DummyLiteral()
        with pytest.raises(PrimitivePatternError):
            literal.setValue("bad")
        literal.setValue("Good")
        assert literal.getValue() == "Good"

    def test_pattern_cache_reuse(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import _PATTERN_CACHE

        _DummyLiteral().value = "A"
        assert r"[A-Z][a-zA-Z0-9_]*" in _PATTERN_CACHE
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/validation/test_arliteral_pattern.py -v`
Expected: FAIL — `ImportError: cannot import name '_PATTERN_CACHE'`

- [ ] **Step 3: Implement the hook**

In `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`:

Add to the module imports at the top (`re` plus the validation imports — merge into the existing import block, do NOT reorder existing imports):

```python
import logging
import re
from typing import Dict

from armodel.validation import get_context, is_warning_mode, PrimitivePatternError
```

Add after the imports, before `class ARType`:

```python
_logger = logging.getLogger(__name__)
_PATTERN_CACHE: Dict[str, re.Pattern] = {}
```

In `class ARLiteral(ARType)` — add the class attribute right after the checklist comment block (before `def __init__`), and change the `value` setter at lines 86-90 to:

```python
    PATTERN: Optional[str] = None

    def checkValue(self, val: Optional[str]) -> None:
        """Raises PrimitivePatternError if val violates the class PATTERN; logs a warning instead when warning mode is active."""
        if self.PATTERN is None or not isinstance(val, str) or val == "":
            return
        compiled = _PATTERN_CACHE.get(self.PATTERN)
        if compiled is None:
            compiled = re.compile(self.PATTERN)
            _PATTERN_CACHE[self.PATTERN] = compiled
        if compiled.fullmatch(val) is None:
            if is_warning_mode():
                context = get_context()
                if context is not None:
                    _logger.warning("<%s> value \"%s\" does not match pattern \"%s\" (%s)", context, val, self.PATTERN, type(self).__name__)
                else:
                    _logger.warning("value \"%s\" does not match pattern \"%s\" (%s)", val, self.PATTERN, type(self).__name__)
                return
            raise PrimitivePatternError(type(self).__name__, val, self.PATTERN)
```

```python
    @value.setter
    def value(self, val: str):
        if not isinstance(val, str):
            raise ValueError("Unsupported Type <%s>" % type(val))
        self.checkValue(val)
        self._value = val
```

Note: `Optional` is already imported in this module (verify: `grep -n "from typing import" ...PrimitiveTypes.py | head -1`; extend that import line with `Dict` if absent).

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/validation/test_arliteral_pattern.py -v`
Expected: 8 PASS

- [ ] **Step 5: Run the existing model + parser suites for regressions**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/ tests/test_armodel/parser/ -q --no-header`
Expected: all PASS (no `PATTERN` populated yet — hook is inert)

- [ ] **Step 6: mypy + lint + format**

Run: `uv run mypy && uv run ruff check src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py tests/test_armodel/validation/test_arliteral_pattern.py && uv run black --check src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py tests/test_armodel/validation/test_arliteral_pattern.py`
Expected: clean (mypy: "Success" over all src files)

- [ ] **Step 7: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py tests/test_armodel/validation/test_arliteral_pattern.py
git commit -m "feat: add PATTERN checkValue hook to ARLiteral"
```

---

### Task 3: XSD extraction script + populate `PATTERN` attributes

**Files:**
- Create: `scripts/extract_xsd_patterns.py`
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py` (one `PATTERN` line per constrained class)
- Test: extend `tests/test_armodel/validation/test_arliteral_pattern.py`

- [ ] **Step 1: Write the extraction script**

Create `scripts/extract_xsd_patterns.py`:

```python
import re
import sys
from pathlib import Path

from lxml import etree

XSD_PATH = Path("autosar/R23-11/xsd/AUTOSAR_00052.xsd")
SRC_PATH = Path("src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py")
NS = {"xsd": "http://www.w3.org/2001/XMLSchema"}


def collect_xsd_patterns():
    tree = etree.parse(str(XSD_PATH))
    patterns = {}
    for node in tree.findall(".//xsd:simpleType", NS) + tree.findall(".//xsd:complexType", NS):
        name = node.get("name")
        if not name:
            continue
        facets = [p.get("value") for p in node.findall(".//xsd:pattern", NS) if p.get("value")]
        if facets:
            patterns[name] = facets
    return patterns


def collect_classes():
    text = SRC_PATH.read_text()
    classes = {}
    matches = list(re.finditer(r"^class (\w+)\(", text, re.M))
    for index, match in enumerate(matches):
        name = match.group(1)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end]
        custom = re.search(r"xml\.xsd\.customType=([A-Za-z0-9_\-]+)", block)
        if custom is not None:
            classes[name] = custom.group(1)
    return classes


def main():
    patterns = collect_xsd_patterns()
    classes = collect_classes()
    for class_name in sorted(classes):
        xsd_type = classes[class_name]
        for facet in patterns.get(xsd_type, []):
            print("%s\t%s\t%s" % (class_name, xsd_type, facet))
    print("classes without XSD pattern facet: %s" % ", ".join(sorted(n for n, t in classes.items() if t not in patterns)), file=sys.stderr)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the script and capture the mapping**

Run: `uv run python scripts/extract_xsd_patterns.py`
Expected output: one `ClassName<TAB>XSD-TYPE<TAB>pattern` line per constrained class. Cross-check against the expected table below; **XSD output is ground truth** — where the table and the script disagree, use the script's value. Skip every class deriving from `Numerical`/`ARType` (Integer, PositiveInteger, PositiveUnlimitedInteger, UnlimitedInteger, Float, TimeValue, Limit, Boolean) — spec: numerics keep their own parse paths.

Expected mapping (from docstrings; confirm via script):

| Class | PATTERN |
|---|---|
| MetaClassName | `[A-Z][a-zA-Z0-9_]*` |
| CIdentifier | `[a-zA-Z_][a-zA-Z0-9_]*` |
| CIdentifierWithIndex | `[a-zA-Z_][a-zA-Z0-9_]*\[[0-9]+\]` |
| StrongRevisionLabelString | `[0-9a-zA-Z-]` |
| CategoryString | `[a-zA-Z][a-zA-Z0-9_]*` |
| DiagRequirementIdString | `[0-9a-zA-Z_\-]+` |
| Identifier | `[a-zA-Z][a-zA-Z0-9_]*` |
| RevisionLabelString | `[0-9]+\.[0-9]+\.[0-9]+([\._;].*)?` |
| Ip4AddressString | `(25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.(25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.(25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.(25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\|ANY` |
| Ip6AddressString | `[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7,7}\|ANY` |
| MacAddressString | `([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}` |
| AnyServiceInstanceId | `[1-9][0-9]*\|0[xX][0-9a-fA-F]+\|0[0-7]*\|0[bB][0-1]+\|ANY\|ALL` |
| AnyVersionString | `[0-9]+\|ANY` |
| Address | `0[xX][0-9a-fA-F]+` |
| PrimitiveIdentifier | `[a-zA-Z][a-zA-Z0-9]([a-zA-Z0-9]\|_[a-zA-Z0-9])*_?` |
| McdIdentifier | `[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*\|[0-9]+)\])*(\.[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*\|[0-9]+)\])*)*` |
| Ref | `/?[a-zA-Z][a-zA-Z0-9_]{0,127}(/[a-zA-Z][a-zA-Z0-9_]{0,127})*` |

Classes the script may additionally print (XSD has facets, docstring may not): AlignmentType, CseCodeType, DisplayFormatString, NativeDeclarationString, BaseTypeEncodingString, SectionInitializationPolicyType, ReferrableSubtypesEnum, UriString — add `PATTERN` for each printed ARLiteral subclass. Classes NOT printed: leave untouched (`PATTERN` inherits `None`) — e.g. `String`, `NameToken`, `VerbatimStringPlain`.

- [ ] **Step 3: Add the `PATTERN` attributes**

For each class in the script output (minus the Numerical family), add one line immediately after the class's method-parity checklist comment block, before `def __init__`. Exact shape (shown for `McdIdentifier`, checklist block ends at line 1586):

```python
    PATTERN = r"[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*(\.[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*)*"
```

Apply the identical one-line shape for every class with its script-printed regex in a raw string (`r"..."`; use `r'...'` only if the pattern contains `"`). No docstring changes, no comment additions.

- [ ] **Step 4: Add per-class round-trip validation tests**

Append to `tests/test_armodel/validation/test_arliteral_pattern.py`:

```python
class TestPopulatedPatterns:
    def test_meta_class_name_accepts_and_rejects(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MetaClassName

        assert MetaClassName().setValue("MyMetaClass").getValue() == "MyMetaClass"
        with pytest.raises(PrimitivePatternError):
            MetaClassName().value = "lowercaseStart"

    def test_mcd_identifier_accepts_and_rejects(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import McdIdentifier

        assert McdIdentifier().setValue("Cal_prm[3].Sub[0]").getValue() == "Cal_prm[3].Sub[0]"
        with pytest.raises(PrimitivePatternError):
            McdIdentifier().value = "9bad"

    def test_c_identifier_with_index(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifierWithIndex

        assert CIdentifierWithIndex().setValue("Var[12]").getValue() == "Var[12]"
        with pytest.raises(PrimitivePatternError):
            CIdentifierWithIndex().value = "Var"

    def test_ip4_address_string(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString

        assert Ip4AddressString().setValue("192.168.0.1").getValue() == "192.168.0.1"
        with pytest.raises(PrimitivePatternError):
            Ip4AddressString().value = "999.1.1.1"

    def test_ref_pattern(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ref

        assert Ref().setValue("/Pkg/Elem").getValue() == "/Pkg/Elem"
```

Extend this class for EVERY remaining populated class from the Task 3 Step 2 script output, following the same shape: one test method per class, one `setValue` accept assertion with a spec-valid value, one `pytest.raises(PrimitivePatternError)` reject with an obviously-violating string (e.g. leading digit or `!` for identifier-like patterns; `300.1.1.1`-style out-of-range for Ip4).

- [ ] **Step 5: Run tests**

Run: `uv run pytest tests/test_armodel/validation/test_arliteral_pattern.py -v`
Expected: 13 PASS. If a populated pattern rejects a value that the table above claims valid, the script's XSD value wins — fix the test expectation, never the pattern.

- [ ] **Step 6: Full-suite regression check**

Run: `uv run pytest -q --no-header`
Expected: all PASS. **If an existing test/integration value now fails a pattern**: the value is spec-invalid — if the test data is wrong, fix the test data; if the pattern is wrong, re-verify the facet in the XSD and correct `PATTERN`. Do NOT disable the hook.

- [ ] **Step 7: Lint, format, commit**

Run: `uv run mypy && uv run ruff check src/armodel/models scripts/extract_xsd_patterns.py && uv run black src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py scripts/extract_xsd_patterns.py tests/test_armodel/validation/test_arliteral_pattern.py`

```bash
git add scripts/extract_xsd_patterns.py src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py tests/test_armodel/validation/test_arliteral_pattern.py
git commit -m "feat: populate PATTERN from XSD facets on constrained literals"
```

---

### Task 4: Parser integration

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py` (`load()` at line 22628; import block at top)

- [ ] **Step 1: Find all parser entry points**

Run: `grep -n "def load" src/armodel/parser/arxml_parser.py`
Wrap EVERY `load*` entry point the same way (Step 2 shows `load()`; repeat for any `loadString`/`loads` found).

- [ ] **Step 2: Wrap `load()` in warning mode**

In `src/armodel/parser/arxml_parser.py`:

Add to imports (merge into existing blocks; do NOT reorder):

```python
from contextlib import nullcontext
```

```python
from armodel.validation import warning_mode
```

Change `load()` (currently starts at line 22628):

```python
    def load(self, filename, document: AUTOSAR):
        self.logger.info("Loading %s ..." % os.path.realpath(filename))

        if self.options["warning"] is True:
            context_manager = warning_mode(True, context=os.path.basename(filename))
        else:
            context_manager = nullcontext()
        with context_manager:
            self._validateARXML(filename)

            tree = ET.parse(filename)
            root = tree.getroot()
            if self.getPureTagName(root.tag) != "AUTOSAR":
                self.raiseError("Invalid ARXML file <%s>" % filename)

            self.detectNamespace(root)
            self.getAUTOSARInfo(root, document)
            document.setAdminData(self.getAdminData(root, "ADMIN-DATA"))
```

Then indent the ENTIRE remaining body of `load()` one additional level (4 spaces) under the `with context_manager:` block, through the end of the method. No other logic changes.

- [ ] **Step 3: Run parser tests**

Run: `uv run pytest tests/test_armodel/parser/ tests/test_armodel/validation/ -q --no-header`
Expected: all PASS (existing tests either don't set `warning` or have valid data)

- [ ] **Step 4: Commit**

```bash
git add src/armodel/parser/arxml_parser.py
git commit -m "feat: parser activates pattern warning mode with warning option"
```

---

### Task 5: Parser integration test (build → write → corrupt → re-parse)

**Files:**
- Test: `tests/test_armodel/validation/test_parser_pattern_integration.py`

- [ ] **Step 1: Verify the construction API names**

Run: `grep -n "def createApplicationSwComponentType\|def createSwcInternalBehavior\|def createPerInstanceMemory" src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ComponentType/*.py src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/*.py src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py`
Adjust the test below to the exact names/signatures found (mirroring `tests/test_armodel/parser/test_arxml_parser_*.py` usage if needed).

- [ ] **Step 2: Write the failing test**

Create `tests/test_armodel/validation/test_parser_pattern_integration.py`:

```python
import logging

import pytest

from armodel.models.AUTOSAR import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier
from armodel.parser.arxml_parser import ARXMLParser
from armodel.validation import PrimitivePatternError
from armodel.writer.arxml_writer import ARXMLWriter


def _build_arxml_with_type(tmp_path, type_text):
    document = AUTOSAR.new()
    document.setARRelease("R23-11")
    package = document.createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    behavior = swc.createSwcInternalBehavior("Ib")
    memory = behavior.createPerInstanceMemory("Pim")
    memory.setType(CIdentifier().setValue(type_text))
    filename = str(tmp_path / "pim.arxml")
    ARXMLWriter().save(filename, document)
    with open(filename) as handle:
        return handle.read(), filename


class TestParserPatternIntegration:
    def test_bad_value_raises_by_default(self, tmp_path):
        xml_text, filename = _build_arxml_with_type(tmp_path, "U8")
        bad_text = xml_text.replace("<TYPE>U8</TYPE>", "<TYPE>9BAD</TYPE>")
        assert bad_text != xml_text
        with open(filename, "w") as handle:
            handle.write(bad_text)
        parser = ARXMLParser(options={"validate": False})
        with pytest.raises(PrimitivePatternError):
            parser.load(filename, AUTOSAR.getInstance())

    def test_bad_value_warns_with_warning_option(self, tmp_path, caplog):
        xml_text, filename = _build_arxml_with_type(tmp_path, "U8")
        bad_text = xml_text.replace("<TYPE>U8</TYPE>", "<TYPE>9BAD</TYPE>")
        with open(filename, "w") as handle:
            handle.write(bad_text)
        parser = ARXMLParser(options={"validate": False, "warning": True})
        with caplog.at_level(logging.WARNING):
            parser.load(filename, AUTOSAR.getInstance())
        assert any("9BAD" in record.message for record in caplog.records)
```

Notes: `AUTOSAR.getInstance()` requires `AUTOSAR.new()` to have reset state — the helper calls `AUTOSAR.new()` first, so the instance is fresh; if the repo's singleton API differs (check `src/armodel/models/AUTOSAR.py`), mirror the import/usage from an existing parser test.

- [ ] **Step 3: Run the test**

Run: `uv run pytest tests/test_armodel/validation/test_parser_pattern_integration.py -v`
Expected: 2 PASS. If the writer serializes `TYPE` with attributes/namespace prefixes, relax the corruption to a regex: `re.sub(r"(<TYPE[^>]*>)U8(</TYPE>)", r"\g<1>9BAD\g<2>", xml_text, count=1)`.

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/validation/test_parser_pattern_integration.py
git commit -m "test: parser pattern violation raise/warn integration"
```

---

### Task 6: Full battery

- [ ] **Step 1: Run the complete verification battery**

Run: `uv run pytest -q --no-header` → expect all PASS (~26k tests)
Run: `uv run mypy` → expect "Success"
Run: `uv run ruff check src tests scripts` → expect clean
Run: `uv run black --check src/armodel/validation src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py src/armodel/parser/arxml_parser.py tests/test_armodel/validation scripts/extract_xsd_patterns.py` → expect clean

- [ ] **Step 2: Commit any remaining formatting fallout**

```bash
git add -u
git commit -m "style: black formatting for pattern validation"
```

(If nothing to commit, skip.)

---

## Out of scope

- Writer-side validation, XSD codegen, registry generation.

(The sync-workflow integration was originally deferred to Phase 2; it is now Task 7.)

---

### Task 7: sync-autosar-class skill integration (Rule 0028)

**Files:**
- Modify: `.agents/skills/sync-autosar-class/audit_class.py` (new `check_pattern` + call site)
- Modify: `.agents/skills/sync-autosar-class/rules.md` (append Rule 0028 after Rule 0027, line ~2186)
- Modify: `.agents/skills/sync-autosar-class/SKILL.md` (one sentence in the Step 3 bullet)
- Test: `tests/test_scripts/test_audit_class_pattern.py`

- [ ] **Step 1: Locate the integration points**

Run: `ls .trae/skills/sync-autosar-class/ 2>/dev/null` — if the directory exists, apply the SKILL.md/rules.md edits to BOTH copies; otherwise edit `.agents/` only.
Run: `grep -n "check_members(rep" .agents/skills/sync-autosar-class/audit_class.py` — the `check_pattern` call goes immediately after that invocation in the per-class audit flow.
Run: `grep -n "class Report" .agents/skills/sync-autosar-class/audit_class.py` and check how `tests/test_scripts/test_audit_model_test_behavior.py` imports the audit module — mirror that import mechanism in Step 2.

- [ ] **Step 2: Write the failing test**

Create `tests/test_scripts/test_audit_class_pattern.py` (adapt the import block to the mechanism found in Step 1):

```python
import ast

from audit_class import Report, check_pattern


def _class_node(source):
    return ast.parse(source).body[0]


class TestCheckPattern:
    def test_warns_when_docstring_has_pattern_but_no_attr(self):
        node = _class_node(
            'class Foo(ARLiteral):\n'
            '    """docstring\n'
            '\n'
            '    Tags: xml.xsd.pattern=[A-Z][a-zA-Z0-9_]*\n'
            '    """\n'
            '\n'
            '    def __init__(self):\n'
            '        super().__init__()\n'
        )
        report = Report()
        check_pattern(report, node)
        assert report.failed() is False
        assert any("Rule 0028" in warning.message for warning in report.warnings)

    def test_silent_when_attr_declared(self):
        node = _class_node(
            'class Foo(ARLiteral):\n'
            '    """docstring\n'
            '\n'
            '    Tags: xml.xsd.pattern=[A-Z][a-zA-Z0-9_]*\n'
            '    """\n'
            '\n'
            '    PATTERN = r"[A-Z][a-zA-Z0-9_]*"\n'
            '\n'
            '    def __init__(self):\n'
            '        super().__init__()\n'
        )
        report = Report()
        check_pattern(report, node)
        assert not any("Rule 0028" in warning.message for warning in report.warnings)

    def test_silent_when_no_pattern_tag(self):
        node = _class_node(
            'class Foo(ARLiteral):\n'
            '    """docstring\n'
            '\n'
            '    Tags: xml.xsd.customType=NMTOKEN-STRING\n'
            '    """\n'
            '\n'
            '    def __init__(self):\n'
            '        super().__init__()\n'
        )
        report = Report()
        check_pattern(report, node)
        assert not any("Rule 0028" in warning.message for warning in report.warnings)
```

If `Report`'s findings container attribute is not named `warnings` (check the class at the `grep -n "class Report"` line: `self.fail`/`self.warn`/`self.info` append target), adjust the assertions to that attribute.

- [ ] **Step 3: Run the test to verify it fails**

Run: `uv run pytest tests/test_scripts/test_audit_class_pattern.py -v`
Expected: FAIL — `ImportError: cannot import name 'check_pattern'`

- [ ] **Step 4: Implement `check_pattern` in `audit_class.py`**

Add after `check_members` (keep helper ordering; `ast` and `Report` already imported):

```python
def check_pattern(rep: Report, node: ast.ClassDef) -> None:
    doc = ast.get_docstring(node) or ""
    if "xml.xsd.pattern=" not in doc:
        return
    for stmt in node.body:
        targets = []
        if isinstance(stmt, ast.Assign):
            targets = [t.id for t in stmt.targets if isinstance(t, ast.Name)]
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            targets = [stmt.target.id]
        if "PATTERN" in targets:
            return
    rep.warn("PATTERN", "Rule 0028: docstring carries xml.xsd.pattern but no PATTERN attribute is declared — add the XSD-facet regex (an inherited attribute from a pattern-declaring base satisfies the rule; verify by hand)")
```

Wire the call site found in Step 1: `check_pattern(rep, node)` immediately after the `check_members(rep, ...)` invocation.

- [ ] **Step 5: Run the test to verify it passes**

Run: `uv run pytest tests/test_scripts/test_audit_class_pattern.py -v`
Expected: 3 PASS

- [ ] **Step 6: Append Rule 0028 to rules.md**

Append at the end of `.agents/skills/sync-autosar-class/rules.md` (and the `.trae` copy if present):

```markdown
## Rule 0028 — Constrained literal classes carry `PATTERN` *(added after the primitive pattern validation feature, 2026-10-14)*

An `ARLiteral` subclass whose value space is regex-constrained — its docstring carries
`xml.xsd.pattern=...` and/or its `xml.xsd.customType` has an `<xsd:pattern>` facet in the release
XSD — must declare a `PATTERN` class attribute holding that regex:

1. The release XSD is authoritative; the docstring's `xml.xsd.pattern` line is the fallback only
   when the XSD has no matching facet. Never copy the markdown rendering verbatim (escapes are
   mangled).
2. Declare it as a raw string immediately after the method-parity checklist block, before
   `__init__`: `PATTERN = r"..."`.
3. Classes without a constraint inherit `ARLiteral.PATTERN = None` and are skipped by the
   runtime check — do not add `PATTERN` to them.
4. `Numerical`/`ARType` numeric subclasses are excluded (they parse values numerically, not
   by regex).
5. `audit_class.py` reports a `PATTERN` warning when a docstring carries `xml.xsd.pattern=` but
   no `PATTERN` attribute is declared on the class; an attribute inherited from a
   pattern-declaring base satisfies the rule (verify by hand).
```

- [ ] **Step 7: One sentence in SKILL.md**

In `SKILL.md` (both copies if present), find the Phase 1 step list entry for **Step 3** ("Implement model class (Green)") and append to that bullet:

```
For constrained literal classes (docstring `xml.xsd.pattern`), declare `PATTERN` from the XSD facet (Rule 0028).
```

- [ ] **Step 8: Run the skill tests + regression battery subset**

Run: `uv run pytest tests/test_scripts/ -q --no-header` → all PASS
Run: `uv run python .agents/skills/sync-autosar-class/audit_class.py McdIdentifier` → PASS expected (no PATTERN warnings after Task 3)

- [ ] **Step 9: Commit**

```bash
git add .agents/skills/sync-autosar-class/ .trae/skills/sync-autosar-class/ tests/test_scripts/test_audit_class_pattern.py
git commit -m "feat: sync skill Rule 0028 — PATTERN attribute on constrained literals"
```

(If `.trae/skills/sync-autosar-class/` does not exist, drop it from the `git add` list.)
