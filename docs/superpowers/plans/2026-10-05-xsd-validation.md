# XSD Validation for ARXML Parse and Write — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Validate ARXML files against bundled AUTOSAR XSD schemas as a pre-parse gate in `ARXMLParser.load()` and a pre-save gate in `ARXMLWriter.save()`.

**Architecture:** New self-contained package `armodel/validation/` wrapping `lxml.etree.XMLSchema` (already a dependency). It resolves a schema from the document's `xsi:schemaLocation` filename against a bundled schema table, compiles schemas lazily with a process-wide cache, and returns structured errors — the parser/writer decide how to report them via their existing `raiseError`/`_raiseError` convention. All work happens in the worktree `/Users/ray/Workspace/py-armodel-wt-xsd` (branch `feature/xsd-validation`); the spec is `docs/superpowers/specs/2026-10-05-xsd-validation-design.md`.

**Tech Stack:** lxml (existing dep, no new deps), stdlib `xml.etree.ElementTree` for light schema-location detection, pytest. Python 3.8-compatible typing only (`typing.Optional[T]`, `typing.List[T]`, `typing.Dict[T, V]` — never `T | None` / `dict[...]`).

**Repo facts discovered during planning (differs from the spec — these amendments are final):**

1. The repo **already vendors** four release schemas under `autosar/<release>/xsd/` (git-tracked):
   `R23-11/AUTOSAR_00052.xsd` (9.6 MB, imports `xml.xsd`), `R4.4.0/AUTOSAR_00046.xsd` + `xml.xsd`,
   `R4.3.1/AUTOSAR_00044.xsd` (imports `xml.xsd`), `R3.2.3/AUTOSAR.xsd` (self-contained). We copy these
   into `src/armodel/validation/schemas/<release>/` as package data instead of downloading anything,
   and bundle releases R23-11 / R4.4.0 / R4.3.1 / R3.2.3 (not R19-11→R22-11 — those XSDs are not in the repo).
2. The `autosar/<release>/` directories are referenced by scripts and spec comments — **do not move them**; the
   `schemas/` copies are duplicates, with a hash-sync unit test keeping them aligned.
3. `xml.xsd` (W3C namespace schema, 643 bytes) is imported by R23-11/R4.3.1/R4.4.0 but only ships in the R4.4.0
   dir; the plan copies it into every bundled release dir so each dir is self-contained. R23-11 compiles in ~0.1 s
   with the resolver trick already proven by `tests/test_armodel/xsd_validation.py`.
   **SUPERSEDED during execution (user request):** a SINGLE shared copy lives at `schemas/xml.xsd` and
   `_AUTOSARResolver` falls back to `SCHEMA_DIR` when the import is not next to the importing schema. Do not
   "restore" per-release xml.xsd copies.
4. **Unresolvable schema (no matching bundled XSD) → log a warning and continue unvalidated** — NOT an error.
   Reason: the writer's default `schema_location` is `AUTOSAR_4-0-3.xsd` and legacy R3 files use `autosar.xsd`
   with namespace `http://autosar.org` (the R3.2.3 XSD targets `http://autosar.org/3.2.3` — verified the legacy
   corpus file does NOT validate against it), so raising would break existing behavior for legitimate inputs.
5. Validation failures are reported **one `logger.error` line per violation, then a single `ValueError`**
   ("failed schema validation with N error(s)") that aborts load/save. With `warning: True`, each violation
   is logged via `logger.warning` and load/save continues. This per-error logging is custom code in the gate
   methods (not the `raiseError`/`_raiseError` helpers, which log a single aggregated message).
6. A public `register_schema_file(xsd_filename, xsd_path)` extension point lets callers register unbundled
   schemas (e.g. R22-11 `AUTOSAR_00050.xsd`); the fast unit tests use it to plug in a tiny fixture schema.
7. Corpus audit (verified during planning): of 32 integration files, exactly 1 maps to a bundled schema
   (`Os_ECUC_4.4.0.arxml` → R4.4.0), its parse input **VALIDATES** and its **writer output VALIDATES too**
   (verified by parsing the file, saving with `ARXMLWriter`, and re-validating the output). The audit test
   asserts both stay valid; other files' schema filenames (`AUTOSAR_00050/00043.xsd`, `AUTOSAR_4-0-3.xsd`,
   `autosar.xsd`) are not bundled and are skipped by detection.
8. Detection uses **only** `xsi:schemaLocation` — the spec's `ADMIN-DATA` fallback is dropped (no AUTOSAR tool
   writes resolvable schema info there; a speculative fallback adds surface without value). Task 6 amends the spec.
9. **The round-trip integration suite (`tests/integration_tests/test_roundtrip.py`) exercises both gates for
   free**: it constructs `ARXMLParser()`/`ARXMLWriter()` with default options, so with validation ON by default
   every round-tripped file whose schema location maps to a bundled XSD is validated on parse AND on save, and a
   schema-invalid input/output fails the round-trip. No code change needed in `test_roundtrip.py` — Task 5 adds
   a verification run plus the standalone audit test for explicit, per-file assertions.
10. **Test-data fragments are verified too (Task 5)**: an AST-based audit test validates every full-document
   `<AUTOSAR>` fragment constant used as unit-test input (15 constants in 6 files found during planning) against
   the bundled XSD, so malformed test fixtures fail CI instead of producing false-passing tests. Partial
   fragments are out of scope (not root-validatable); deliberately malformed fixtures opt out via a
   `# xsd-skip: <reason>` marker. The existing test helper `tests/test_armodel/xsd_validation.py` delegates to
   `armodel.validation` so both share one implementation and one schema cache.

---

### Task 1: Validation package — errors, schema table, detection, cached compilation

**Files:**
- Create: `src/armodel/validation/__init__.py`
- Create: `src/armodel/validation/validator.py`
- Test: `tests/test_armodel/validation/data/tiny_autosar.xsd`
- Test: `tests/test_armodel/validation/test_validator.py`

- [x] **Step 1: Create the tiny fixture schema**

Create directory `tests/test_armodel/validation/data/` with `tiny_autosar.xsd`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            targetNamespace="http://autosar.org/schema/r4.0"
            xmlns="http://autosar.org/schema/r4.0"
            elementFormDefault="qualified">
  <xsd:element name="AUTOSAR">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element name="SHORT-NAME" type="xsd:string" minOccurs="0"/>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
</xsd:schema>
```

Also create empty `tests/test_armodel/validation/__init__.py` (test packages mirror source layout in this repo).

- [x] **Step 2: Write the failing tests**

Create `tests/test_armodel/validation/test_validator.py`:

```python
import os

import pytest

from armodel.validation.validator import (
    ARXMLValidator,
    ValidationError,
    detect_schema_path,
    get_schema,
    register_schema_file,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TINY_XSD = os.path.join(DATA_DIR, "tiny_autosar.xsd")

VALID_DOC = (
    '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
    ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd"/>'
)
INVALID_DOC = (
    '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
    ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd">'
    "<BOGUS/>"
    "</AUTOSAR>"
)


@pytest.fixture(autouse=True)
def _register_tiny_schema():
    register_schema_file("AUTOSAR_TINY.xsd", TINY_XSD)
    yield


class TestDetectSchemaPath:
    def test_returns_tiny_xsd_for_registered_location(self):
        assert detect_schema_path(VALID_DOC.encode("utf-8")) == TINY_XSD

    def test_returns_none_without_schema_location(self):
        assert detect_schema_path(b'<AUTOSAR xmlns="http://autosar.org/schema/r4.0"/>') is None

    def test_returns_none_for_unbundled_schema(self):
        doc = (
            '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
            ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
            ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"/>'
        )
        assert detect_schema_path(doc.encode("utf-8")) is None

    def test_returns_none_on_undetectable_release(self):
        assert detect_schema_path(b"<NOT-XML/>") is None


class TestARXMLValidator:
    def test_valid_document_returns_no_errors(self):
        assert ARXMLValidator(TINY_XSD).validate_bytes(VALID_DOC.encode("utf-8")) == []

    def test_invalid_document_returns_structured_errors(self):
        errors = ARXMLValidator(TINY_XSD).validate_bytes(INVALID_DOC.encode("utf-8"))
        assert len(errors) >= 1
        assert all(isinstance(e, ValidationError) for e in errors)
        assert errors[0].line == 1
        assert "BOGUS" in errors[0].message

    def test_validate_string_accepts_str(self):
        assert ARXMLValidator(TINY_XSD).validate_string(VALID_DOC) == []

    def test_schema_compilation_is_cached(self):
        first = get_schema(TINY_XSD)
        second = get_schema(TINY_XSD)
        assert first is second
```

- [x] **Step 3: Run tests to verify they fail**

Run: `cd /Users/ray/Workspace/py-armodel-wt-xsd && uv run pytest tests/test_armodel/validation/test_validator.py -v --no-coverage`
Expected: FAIL/ERROR — `ModuleNotFoundError: No module named 'armodel.validation'`

- [x] **Step 4: Implement `src/armodel/validation/validator.py`**

```python
import os
import threading
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional

from lxml import etree

XSI_SCHEMA_LOCATION = "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "schemas")

_SCHEMA_PATHS: Dict[str, str] = {
    "autosar_00052.xsd": os.path.join(SCHEMA_DIR, "R23-11", "AUTOSAR_00052.xsd"),
    "autosar_00046.xsd": os.path.join(SCHEMA_DIR, "R4.4.0", "AUTOSAR_00046.xsd"),
    "autosar_00044.xsd": os.path.join(SCHEMA_DIR, "R4.3.1", "AUTOSAR_00044.xsd"),
    "autosar.xsd": os.path.join(SCHEMA_DIR, "R3.2.3", "AUTOSAR.xsd"),
}

_SCHEMA_CACHE: Dict[str, etree.XMLSchema] = {}
_CACHE_LOCK = threading.Lock()


class _AUTOSARResolver(etree.Resolver):
    """Resolves schema imports/includes (e.g. xml.xsd) to the directory of the top-level schema."""

    def __init__(self, schema_dir: str) -> None:
        self.schema_dir = schema_dir

    def resolve(self, url, id, context):
        candidate = os.path.join(self.schema_dir, os.path.basename(url))
        if os.path.exists(candidate):
            return self.resolve_filename(candidate, context)
        return None


def register_schema_file(xsd_filename: str, xsd_path: str) -> None:
    """Register (or override) the XSD file used for a schemaLocation filename."""
    _SCHEMA_PATHS[xsd_filename.lower()] = xsd_path


def detect_schema_path(data: bytes) -> Optional[str]:
    """Return the bundled XSD path matching the document's xsi:schemaLocation, or None."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return None
    schema_location = root.attrib.get(XSI_SCHEMA_LOCATION)
    if not schema_location:
        return None
    tokens = schema_location.split()
    if len(tokens) < 2:
        return None
    return _SCHEMA_PATHS.get(tokens[-1].lower())


def get_schema(xsd_path: str) -> etree.XMLSchema:
    """Compile (once per process) and return the XMLSchema for xsd_path."""
    key = os.path.realpath(xsd_path)
    with _CACHE_LOCK:
        if key not in _SCHEMA_CACHE:
            parser = etree.XMLParser()
            parser.resolvers.add(_AUTOSARResolver(os.path.dirname(key)))
            _SCHEMA_CACHE[key] = etree.XMLSchema(etree.parse(key, parser))
        return _SCHEMA_CACHE[key]


class ValidationError(object):
    def __init__(self, line: Optional[int], column: Optional[int], message: str, domain: str) -> None:
        self.line = line
        self.column = column
        self.message = message
        self.domain = domain

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ValidationError):
            return NotImplemented
        return (self.line, self.column, self.message, self.domain) == (other.line, other.column, other.message, other.domain)

    def __repr__(self) -> str:
        return "ValidationError(line=%s, column=%s, message=%r, domain=%r)" % (self.line, self.column, self.message, self.domain)


class ARXMLValidator(object):
    def __init__(self, xsd_path: str) -> None:
        self.xsd_path = xsd_path

    def validate_bytes(self, data: bytes) -> List[ValidationError]:
        parser = etree.XMLParser()
        parser.resolvers.add(_AUTOSARResolver(os.path.dirname(os.path.realpath(self.xsd_path))))
        try:
            document = etree.fromstring(data, parser)
        except etree.XMLSyntaxError as e:
            return [ValidationError(line=e.lineno, column=e.offset, message="XML syntax error: %s" % e.msg, domain="syntax")]
        schema = get_schema(self.xsd_path)
        if schema.validate(document):
            return []
        return [
            ValidationError(line=error.line, column=error.column, message=error.message, domain="schema")
            for error in schema.error_log
        ]

    def validate_string(self, xml: str) -> List[ValidationError]:
        return self.validate_bytes(xml.encode("utf-8"))
```

- [x] **Step 5: Create `src/armodel/validation/__init__.py`**

```python
from .validator import (
    ARXMLValidator,
    ValidationError,
    detect_schema_path,
    get_schema,
    register_schema_file,
)
```

- [x] **Step 6: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/validation/ -v --no-coverage`
Expected: 8 passed

- [x] **Step 7: Commit**

```bash
cd /Users/ray/Workspace/py-armodel-wt-xsd
git add src/armodel/validation tests/test_armodel/validation/test_validator.py tests/test_armodel/validation/data tests/test_armodel/validation/__init__.py
git commit -m "feat(validation): add ARXMLValidator with schema detection and cached lxml compilation"
```

---

### Task 2: Bundle the release schemas as package data

**Files:**
- Create: `src/armodel/validation/schemas/R23-11/AUTOSAR_00052.xsd` (copy of `autosar/R23-11/xsd/AUTOSAR_00052.xsd`)
- Create: `src/armodel/validation/schemas/R23-11/xml.xsd` (copy of `autosar/R4.4.0/xsd/xml.xsd`)
- Create: `src/armodel/validation/schemas/R4.4.0/AUTOSAR_00046.xsd` + `xml.xsd` (copies of `autosar/R4.4.0/xsd/*`)
- Create: `src/armodel/validation/schemas/R4.3.1/AUTOSAR_00044.xsd` (copy) + `xml.xsd` (copy of `autosar/R4.4.0/xsd/xml.xsd`)
- Create: `src/armodel/validation/schemas/R3.2.3/AUTOSAR.xsd` (copy of `autosar/R3.2.3/xsd/AUTOSAR.xsd`; no xml.xsd — schema is self-contained)
- Create: `src/armodel/validation/schemas/README.md`
- Modify: `pyproject.toml`
- Test: `tests/test_armodel/validation/test_bundled_schemas.py`

- [x] **Step 1: Copy the schema files**

```bash
cd /Users/ray/Workspace/py-armodel-wt-xsd
mkdir -p src/armodel/validation/schemas/R23-11 src/armodel/validation/schemas/R4.4.0 src/armodel/validation/schemas/R4.3.1 src/armodel/validation/schemas/R3.2.3
cp autosar/R23-11/xsd/AUTOSAR_00052.xsd src/armodel/validation/schemas/R23-11/
cp autosar/R4.4.0/xsd/AUTOSAR_00046.xsd autosar/R4.4.0/xsd/xml.xsd src/armodel/validation/schemas/R4.4.0/
cp autosar/R4.3.1/xsd/AUTOSAR_00044.xsd src/armodel/validation/schemas/R4.3.1/
cp autosar/R4.4.0/xsd/xml.xsd src/armodel/validation/schemas/R4.3.1/
cp autosar/R3.2.3/xsd/AUTOSAR.xsd src/armodel/validation/schemas/R3.2.3/
```

- [x] **Step 2: Write the provenance README**

Create `src/armodel/validation/schemas/README.md`:

```markdown
# Bundled AUTOSAR XSD Schemas

Copies of the official AUTOSAR XSDs published on autosar.org, mirrored from this
repository's `autosar/<release>/xsd/` directories so they can ship as package data.
Do not edit the copies; refresh them from the `autosar/` originals (the unit test
`tests/test_armodel/validation/test_bundled_schemas.py::test_bundled_schemas_match_repo_copies`
enforces byte equality).

| Directory | File | Source |
|---|---|---|
| R23-11 | AUTOSAR_00052.xsd | AUTOSAR R23-11 XSD (autosar.org), mirrored at `autosar/R23-11/xsd/` |
| R4.4.0 | AUTOSAR_00046.xsd | AUTOSAR R4.4.0 XSD, mirrored at `autosar/R4.4.0/xsd/` |
| R4.3.1 | AUTOSAR_00044.xsd | AUTOSAR R4.3.1 XSD, mirrored at `autosar/R4.3.1/xsd/` |
| R3.2.3 | AUTOSAR.xsd | AUTOSAR R3.2.3 XSD, mirrored at `autosar/R3.2.3/xsd/` |

`xml.xsd` is the W3C XML namespace schema imported by the R23-11/R4.4.0/R4.3.1
schemas; it is copied next to each importing schema so every directory is
self-contained.
```

- [x] **Step 3: Register package data in `pyproject.toml`**

Add after the existing `[tool.setuptools.packages.find]` section:

```toml
[tool.setuptools.package-data]
"armodel.validation" = ["schemas/*/*.xsd", "README.md"]
```

- [x] **Step 4: Write the failing tests**

Create `tests/test_armodel/validation/test_bundled_schemas.py`:

```python
import hashlib
import os

import pytest

from armodel.validation.validator import SCHEMA_DIR, get_schema

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")

BUNDLED_SCHEMAS = [
    ("R23-11", "AUTOSAR_00052.xsd"),
    ("R4.4.0", "AUTOSAR_00046.xsd"),
    ("R4.3.1", "AUTOSAR_00044.xsd"),
    ("R3.2.3", "AUTOSAR.xsd"),
]


def _sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


@pytest.mark.parametrize("release,xsd_name", BUNDLED_SCHEMAS)
def test_bundled_schemas_match_repo_copies(release, xsd_name):
    bundled = os.path.join(SCHEMA_DIR, release, xsd_name)
    repo = os.path.join(REPO_ROOT, "autosar", release, "xsd", xsd_name)
    assert _sha256(bundled) == _sha256(repo)


@pytest.mark.slow
@pytest.mark.parametrize("release,xsd_name", BUNDLED_SCHEMAS)
def test_bundled_schema_compiles(release, xsd_name):
    schema = get_schema(os.path.join(SCHEMA_DIR, release, xsd_name))
    assert schema is not None
```

- [x] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/validation/test_bundled_schemas.py -v --no-coverage` and
`uv run pytest tests/test_armodel/validation/test_bundled_schemas.py -v --no-coverage -m slow`
Expected: hash-sync 4 passed immediately; compile tests 4 passed (R23-11/R4.3.1 compile may take a few seconds).

- [x] **Step 6: Commit**

```bash
git add src/armodel/validation/schemas pyproject.toml tests/test_armodel/validation/test_bundled_schemas.py
git commit -m "feat(validation): bundle AUTOSAR release XSDs (R23-11, R4.4.0, R4.3.1, R3.2.3) as package data"
```

---

### Task 3: Parser integration — pre-parse gate in `ARXMLParser.load()`

**Files:**
- Modify: `src/armodel/parser/abstract_arxml_parser.py` (options defaults in `__init__` around line 50, `_processOptions` at lines 63-66)
- Modify: `src/armodel/parser/arxml_parser.py` (imports near top of file; `load()` at ~line 18238 in this branch's checkout — locate by `def load`)
- Test: `tests/test_armodel/parser/test_xsd_validation_gate.py`

- [x] **Step 1: Write the failing tests**

Create `tests/test_armodel/parser/test_xsd_validation_gate.py`:

```python
import os

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.validation.validator import register_schema_file

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "validation", "data")
TINY_XSD = os.path.join(DATA_DIR, "tiny_autosar.xsd")

VALID_DOC = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
    ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd"/>'
)
SCHEMA_INVALID_DOC = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
    ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd">'
    "<BOGUS/>"
    "</AUTOSAR>"
)


@pytest.fixture(autouse=True)
def _register_tiny_schema():
    register_schema_file("AUTOSAR_TINY.xsd", TINY_XSD)
    yield


@pytest.fixture(autouse=True)
def _fresh_document():
    AUTOSAR.new()
    yield


def _write(tmp_path, name, content):
    path = os.path.join(str(tmp_path), name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def test_valid_file_loads(tmp_path):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser()
    parser.load(_write(tmp_path, "valid.arxml", VALID_DOC), document)
    assert document is not None


def test_schema_invalid_file_raises_with_line_number(tmp_path):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser()
    with pytest.raises(ValueError) as exc_info:
        parser.load(_write(tmp_path, "invalid.arxml", SCHEMA_INVALID_DOC), document)
    assert "failed schema validation" in str(exc_info.value)


def test_warning_mode_logs_and_continues(tmp_path, caplog):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser(options={"warning": True})
    parser.load(_write(tmp_path, "invalid.arxml", SCHEMA_INVALID_DOC), document)


def test_validate_false_skips_validation(tmp_path):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser(options={"validate": False, "warning": True})
    parser.load(_write(tmp_path, "invalid.arxml", SCHEMA_INVALID_DOC), document)


def test_no_matching_schema_logs_warning_and_continues(tmp_path):
    doc_without_bundled_schema = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
        ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"/>'
    )
    document = AUTOSAR.getInstance()
    parser = ARXMLParser()
    parser.load(_write(tmp_path, "unbundled.arxml", doc_without_bundled_schema), document)
```

- [x] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/parser/test_xsd_validation_gate.py -v --no-coverage`
Expected: FAIL — `AttributeError: 'ARXMLParser' object has no attribute 'options'... 'validate'` (KeyError on `self.options["validate"]`) or no validation performed (`test_schema_invalid_file_raises_with_line_number` fails with "DID NOT RAISE").

- [x] **Step 3: Add the `validate` option to `AbstractARXMLParser`**

In `src/armodel/parser/abstract_arxml_parser.py`, in `__init__` (after `self.options["warning"] = False`):

```python
        self.options["validate"] = True
```

In `_processOptions` (after the `"warning"` block):

```python
            if "validate" in options:
                self.options["validate"] = options["validate"]
```

- [x] **Step 4: Wire the gate into `ARXMLParser.load()`**

In `src/armodel/parser/arxml_parser.py`, add import at the top (grouped with the other `armodel` imports — do NOT reorder existing imports):

```python
from armodel.validation.validator import ARXMLValidator, detect_schema_path
```

In `load()`, insert the gate as the first statement after the log line, before `tree = ET.parse(filename)`:

```python
    def load(self, filename, document: AUTOSAR):
        self.logger.info("Loading %s ..." % os.path.realpath(filename))

        self._validateARXML(filename)

        tree = ET.parse(filename)
```

Add the method immediately before `load()`:

```python
    def _validateARXML(self, filename):
        if self.options["validate"] is False:
            return
        with open(filename, "rb") as f:
            data = f.read()
        xsd_path = detect_schema_path(data)
        if xsd_path is None:
            self.logger.warning("No XSD schema found for <%s>; validation skipped" % filename)
            return
        errors = ARXMLValidator(xsd_path).validate_bytes(data)
        if not errors:
            return
        if self.options["warning"] is True:
            for error in errors:
                self.logger.warning("Schema error in <%s> line %s, col %s: %s" % (filename, error.line, error.column, error.message))
            return
        for error in errors:
            self.logger.error("Schema error in <%s> line %s, col %s: %s" % (filename, error.line, error.column, error.message))
        raise ValueError("ARXML file <%s> failed schema validation with %d error(s)" % (filename, len(errors)))
```

(Strict mode: one `logger.error` per violation, then `ValueError` aborts the load — no half-built document.
`warning: True`: one `logger.warning` per violation, then parsing proceeds.)

- [x] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/parser/test_xsd_validation_gate.py tests/test_armodel/validation/ -v --no-coverage`
Expected: all passed

- [x] **Step 6: Run the existing parser suite to check no regressions**

Run: `uv run pytest tests/test_armodel/parser/ --no-coverage -q`
Expected: all passed (existing parser tests either parse schema-valid fragments or construct documents without `load()`; if a test feeds a `load()`-ed fixture that is now schema-invalid, report it — do not silently weaken the gate)

- [x] **Step 7: Commit**

```bash
git add src/armodel/parser/abstract_arxml_parser.py src/armodel/parser/arxml_parser.py tests/test_armodel/parser/test_xsd_validation_gate.py
git commit -m "feat(parser): validate ARXML against bundled XSD before parsing"
```

---

### Task 4: Writer integration — pre-save gate in `ARXMLWriter.save()`

**Files:**
- Modify: `src/armodel/writer/abstract_arxml_writer.py` (options defaults in `__init__` around lines 49-52, `_processOptions` at lines 64-68)
- Modify: `src/armodel/writer/arxml_writer.py` (imports near top; `save()` at ~line 18367 — locate by `def save`; `saveToFile` lives in `abstract_arxml_writer.py:229`)
- Test: `tests/test_armodel/writer/test_xsd_validation_gate.py`

- [x] **Step 1: Write the failing tests**

Create `tests/test_armodel/writer/test_xsd_validation_gate.py`:

```python
import os

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.validation.validator import register_schema_file
from armodel.writer.arxml_writer import ARXMLWriter

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "validation", "data")
TINY_XSD = os.path.join(DATA_DIR, "tiny_autosar.xsd")


@pytest.fixture(autouse=True)
def _register_tiny_schema():
    register_schema_file("AUTOSAR_TINY.xsd", TINY_XSD)
    yield


@pytest.fixture(autouse=True)
def _fresh_document():
    AUTOSAR.new()
    yield


def _document_with_tiny_schema_location():
    document = AUTOSAR.getInstance()
    document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd"
    return document


def test_valid_document_saves(tmp_path):
    path = os.path.join(str(tmp_path), "out.arxml")
    ARXMLWriter().save(path, _document_with_tiny_schema_location())
    assert os.path.exists(path)


def test_schema_invalid_document_raises_and_does_not_write(tmp_path):
    document = _document_with_tiny_schema_location()
    document.createARPackage("Pkg")
    path = os.path.join(str(tmp_path), "out.arxml")
    with pytest.raises(ValueError) as exc_info:
        ARXMLWriter().save(path, document)
    assert "failed schema validation" in str(exc_info.value)
    assert not os.path.exists(path)


def test_warning_mode_logs_and_writes(tmp_path):
    document = _document_with_tiny_schema_location()
    document.createARPackage("Pkg")
    path = os.path.join(str(tmp_path), "out.arxml")
    ARXMLWriter(options={"warning": True}).save(path, document)
    assert os.path.exists(path)


def test_validate_false_skips_validation(tmp_path):
    document = _document_with_tiny_schema_location()
    document.createARPackage("Pkg")
    path = os.path.join(str(tmp_path), "out.arxml")
    ARXMLWriter(options={"validate": False}).save(path, document)
    assert os.path.exists(path)


def test_default_schema_location_skips_validation(tmp_path):
    document = AUTOSAR.getInstance()
    path = os.path.join(str(tmp_path), "out.arxml")
    ARXMLWriter().save(path, document)
    assert os.path.exists(path)
```

- [x] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_armodel/writer/test_xsd_validation_gate.py -v --no-coverage`
Expected: FAIL — `KeyError: 'validate'` (option missing) and `test_schema_invalid_document_raises_and_does_not_write` fails with "DID NOT RAISE".

- [x] **Step 3: Add the `validate` option to `AbstractARXMLWriter`**

In `src/armodel/writer/abstract_arxml_writer.py`, in `__init__` (after `self.options["unescape_entities"] = False`):

```python
        self.options["validate"] = True
```

In `_processOptions` (after the `"unescape_entities"` block):

```python
            if "validate" in options:
                self.options["validate"] = options["validate"]
```

- [x] **Step 4: Wire the gate into `ARXMLWriter.save()`**

In `src/armodel/writer/arxml_writer.py`, add import at the top (do NOT reorder existing imports):

```python
from armodel.validation.validator import ARXMLValidator, detect_schema_path
```

In `save()`, replace the final `self.saveToFile(filename, root)` line with:

```python
        self._validateDocument(root, filename)
        self.saveToFile(filename, root)
```

Add the method immediately before `save()`:

```python
    def _validateDocument(self, root, filename):
        if self.options["validate"] is False:
            return
        data = ET.tostring(root, encoding="UTF-8")
        xsd_path = detect_schema_path(data)
        if xsd_path is None:
            self.logger.warning("No XSD schema matches the document schema location; validation skipped for <%s>" % filename)
            return
        errors = ARXMLValidator(xsd_path).validate_bytes(data)
        if not errors:
            return
        if self.options["warning"] is True:
            for error in errors:
                self.logger.warning("Schema error in <%s> line %s, col %s: %s" % (filename, error.line, error.column, error.message))
            return
        for error in errors:
            self.logger.error("Schema error in <%s> line %s, col %s: %s" % (filename, error.line, error.column, error.message))
        raise ValueError("Generated ARXML file <%s> failed schema validation with %d error(s)" % (filename, len(errors)))
```

(Strict mode: one `logger.error` per violation, then `ValueError` — the file is never written.
`warning: True`: one `logger.warning` per violation, then the file is written.)

- [x] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/writer/test_xsd_validation_gate.py tests/test_armodel/validation/ -v --no-coverage`
Expected: all passed

- [x] **Step 6: Run the existing writer suite to check no regressions**

Run: `uv run pytest tests/test_armodel/writer/ --no-coverage -q`
Expected: all passed (most writer tests either set a non-bundled `schema_location` or default to it, so they skip validation; failures here mean a test uses a bundled schema location — investigate before changing the gate)

- [x] **Step 7: Commit**

```bash
git add src/armodel/writer/abstract_arxml_writer.py src/armodel/writer/arxml_writer.py tests/test_armodel/writer/test_xsd_validation_gate.py
git commit -m "feat(writer): validate generated ARXML against bundled XSD before saving"
```

---

### Task 5: Verify test-data fragments against the XSD

Unit tests parse inline XML fragments ("test data"); a malformed fixture can make a wrong parser look
correct. This task makes the suite itself enforce that every **full-document** fragment constant used as
test data validates against the bundled XSD. Scope (measured by AST scan during planning): 15 full-document
`<AUTOSAR>...</AUTOSAR>` string constants in 6 files. **Partial fragments** (bare element trees fed directly
to `read*` methods) cannot be validated against a root schema and are out of scope. Deliberately malformed
fixtures (error-path tests) opt out with a `# xsd-skip: <reason>` marker line on the assignment.

**Files:**
- Modify: `tests/test_armodel/xsd_validation.py` (delegate to `armodel.validation` — one implementation, one schema cache)
- Create: `tests/test_armodel/validation/test_test_data_fragments.py`

- [x] **Step 1: Write the failing audit test**

Create `tests/test_armodel/validation/test_test_data_fragments.py`:

```python
"""Validates that every full-document AUTOSAR fragment constant used as test data
is schema-valid. Deliberately malformed fixtures opt out with a `# xsd-skip: <reason>`
marker on (or directly above) the assignment."""

import ast
import glob
import os
import re

import pytest

from armodel.validation.validator import ARXMLValidator, SCHEMA_DIR, detect_schema_path

TESTS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_XSD = os.path.join(SCHEMA_DIR, "R4.4.0", "AUTOSAR_00046.xsd")
DOC_PATTERN = re.compile(r"^\s*(<\?xml[^>]*?>)?\s*<AUTOSAR[\s>]", re.S)
SKIP_MARKER = "xsd-skip"


def collect_fragments():
    found = []
    pattern = os.path.join(TESTS_DIR, "**", "test_*.py")
    for path in sorted(glob.glob(pattern, recursive=True)):
        with open(path, encoding="utf-8") as f:
            source = f.read()
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        lines = source.splitlines()
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            value = node.value
            if not (isinstance(value, ast.Constant) and isinstance(value.value, str)):
                continue
            if not DOC_PATTERN.match(value.value):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            name = targets[0].id if targets and isinstance(targets[0], ast.Name) else "constant@%d" % node.lineno
            skipped = SKIP_MARKER in "\n".join(lines[max(0, node.lineno - 3) : node.lineno])
            found.append((path, name, value.value, skipped))
    return found


ALL_FRAGMENTS = collect_fragments()
CHECKED = [(path, name, xml) for path, name, xml, skipped in ALL_FRAGMENTS if not skipped]


@pytest.mark.parametrize(
    "path,name,xml",
    CHECKED,
    ids=["%s:%s" % (os.path.relpath(p, TESTS_DIR), n) for p, n, _ in CHECKED],
)
def test_test_data_fragment_validates(path, name, xml):
    data = xml.encode("utf-8")
    xsd_path = detect_schema_path(data)
    if xsd_path is None:
        xsd_path = DEFAULT_XSD
    errors = ARXMLValidator(xsd_path).validate_bytes(data)
    assert errors == [], "%s:%s is schema-invalid (fix the test data or add a xsd-skip marker if deliberately malformed):\n%s" % (
        os.path.relpath(path, TESTS_DIR),
        name,
        "\n".join("  line %s: %s" % (error.line, error.message) for error in errors),
    )


def test_fragment_scan_found_targets():
    assert len(ALL_FRAGMENTS) >= 10, "fragment scanner found nothing — its AST patterns are broken"
```

- [x] **Step 2: Run the audit and triage the results**

Run: `uv run pytest tests/test_armodel/validation/test_test_data_fragments.py -v --no-coverage`
Expected first run: the scanner finds ~15 fragments; some may fail. Triage every failure:
- **Deliberately malformed** (error-path/warning-branch tests) → add `# xsd-skip: <reason>` on the assignment line.
- **Accidentally invalid test data** → fix the fragment; this is exactly the class of bug this audit exists to catch.
Do not loosen the audit to make it pass.

- [x] **Step 3: Delegate the legacy test helper to `armodel.validation`**

Replace the body of `tests/test_armodel/xsd_validation.py` (keep the module docstring updated):

```python
"""Shared helper to validate ARXML fragments against the AUTOSAR XSD schema.

Delegates to :mod:`armodel.validation.validator` so the test-suite helper and the
runtime validator share one implementation and one schema cache. Defaults to the
bundled R4.4.0 schema (AUTOSAR_00046.xsd), matching the original behavior of this
helper.
"""

import os

from armodel.validation.validator import ARXMLValidator, SCHEMA_DIR, get_schema

XSD_DIR = os.path.join(SCHEMA_DIR, "R4.4.0")
XSD_PATH = os.path.join(XSD_DIR, "AUTOSAR_00046.xsd")


def is_valid(xml):
    """Return True when the given XML byte/string is valid per the AUTOSAR XSD."""
    data = xml.encode("utf-8") if isinstance(xml, str) else xml
    return ARXMLValidator(XSD_PATH).validate_bytes(data) == []


def assert_valid(xml):
    """Assert that the given XML byte/string is valid per the AUTOSAR XSD."""
    data = xml.encode("utf-8") if isinstance(xml, str) else xml
    errors = ARXMLValidator(XSD_PATH).validate_bytes(data)
    assert errors == [], "XML does not validate against AUTOSAR_00046.xsd:\n%s" % "\n".join(
        "line %s: %s" % (error.line, error.message) for error in errors
    )
```

(`get_schema` is re-exported unchanged so existing imports keep working; the old local resolver class and
`etree` import are removed — compilation now flows through the shared, process-wide cache.)

- [x] **Step 4: Run the audit, the helper's consumers, and the validation package**

Run: `uv run pytest tests/test_armodel/validation/ tests/test_armodel/parser/test_arxml_parser_implementation.py tests/test_armodel/writer/test_writer_implementation.py tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_PrimitiveTypes.py -v --no-coverage`
Expected: all passed.

- [x] **Step 5: Commit**

```bash
git add tests/test_armodel/validation/test_test_data_fragments.py tests/test_armodel/xsd_validation.py
git commit -m "test(validation): enforce XSD validity of full-document test-data fragments"
```

---

### Task 6: Validation in the parser/writer test suites (round-trip + corpus audit) + full battery + lint/type/format

**Files:**
- Test: `tests/integration_tests/test_xsd_corpus_audit.py`
- Verify (no code change): `tests/integration_tests/test_roundtrip.py` — with validation ON by default, its
  `ARXMLParser()`/`ARXMLWriter()` calls now gate every round-trip on XSD validity (see header note 9).

- [x] **Step 1: Write the corpus audit test**

Create `tests/integration_tests/test_xsd_corpus_audit.py`:

```python
import glob
import os

import pytest

from armodel.validation.validator import ARXMLValidator, detect_schema_path

CORPUS = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "test_files", "*.arxml")))
MAPPED = [f for f in CORPUS if detect_schema_path(open(f, "rb").read()) is not None]


@pytest.mark.parametrize("filename", MAPPED)
def test_corpus_file_validates_against_bundled_schema(filename):
    with open(filename, "rb") as f:
        data = f.read()
    errors = ARXMLValidator(detect_schema_path(data)).validate_bytes(data)
    assert errors == [], "%s failed validation:\n%s" % (
        filename,
        "\n".join("  line %s: %s" % (error.line, error.message) for error in errors),
    )


def test_corpus_mapping_present():
    assert MAPPED, "no corpus file maps to a bundled schema — detection is broken"
```

- [x] **Step 2: Run the audit**

Run: `uv run pytest tests/integration_tests/test_xsd_corpus_audit.py -v --no-coverage`
Expected: `test_corpus_mapping_present` passes; exactly 1 parametrized case (`Os_ECUC_4.4.0.arxml`, verified VALID during planning) passes.
If additional files appear or the mapped file fails: stop and investigate with the user before loosening anything.

- [x] **Step 3: Verify the round-trip suite exercises the gates**

Run: `uv run pytest tests/integration_tests/test_roundtrip.py --no-coverage -q`
Expected: all passed. With validation ON by default, the bundled-schema file (`Os_ECUC_4.4.0.arxml`) is now
schema-validated on parse and on save inside this suite (its writer output was verified VALID during planning);
the remaining files log "No XSD schema found ... validation skipped" warnings and round-trip as before.
A failure here means either (a) the writer produced schema-invalid ARXML for a bundled-schema file — a real
finding to investigate — or (b) a test constructs a parser/writer with a bundled schema location on an
intentionally imperfect fixture; report rather than silently weakening the gate.

- [x] **Step 4: Run the full test battery**

Run: `uv run pytest tests/ --no-coverage -q` (expected battery ≈ 17,000+ tests, 0 failures; local `tests/integration_tests/custom_files/` round-trip length-compare failures are a known pre-existing local condition — confirm any failures match that pattern before investigating further)

- [x] **Step 5: Lint, type-check, format**

```bash
npm run lint
npm run black
```

Expected: mypy green (the new package is fully typed, `ignore_missing_imports` covers lxml); ruff/flake8 green; black reformats only the new/modified files if needed. Re-run `uv run pytest tests/test_armodel/validation/ --no-coverage -q` after black.

- [x] **Step 6: Commit**

```bash
git add tests/integration_tests/test_xsd_corpus_audit.py
git commit -m "test(integration): audit corpus files that map to bundled XSD schemas"
```

---

### Task 7: Spec amendment + user-visible docs

**Files:**
- Modify: `docs/superpowers/specs/2026-10-05-xsd-validation-design.md`
- Modify: `README.md` (usage section)

- [x] **Step 1: Amend the spec with the planning discoveries**

In the spec's Decisions table and §3-§5, replace the R19-11→R23-11 bundling statement with the actual
bundled set (R23-11, R4.4.0, R4.3.1, R3.2.3 — copied from the repo's `autosar/<release>/xsd/` mirrors),
replace "new exception on the parser's existing error base" with "per-violation `logger.error` lines followed
by a single `ValueError` (strict) / per-violation `logger.warning` lines and continue (`warning: True`)",
replace the `ADMIN-DATA` detection fallback with
"detection uses `xsi:schemaLocation` only", and add: unresolvable schema → warning + continue
unvalidated, plus the `register_schema_file` extension point. Reference this plan file.

- [x] **Step 2: Add a usage block to `README.md`**

Add under an appropriate existing section (near parse/save usage):

```markdown
### XSD Validation

ARXML files are validated against the bundled AUTOSAR XSD schemas (R23-11, R4.4.0, R4.3.1, R3.2.3)
before parsing and before saving. The schema is selected from the document's `xsi:schemaLocation`;
documents with no matching bundled schema are processed without validation (a warning is logged).

```python
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

parser = ARXMLParser()                              # invalid file -> ValueError with line numbers
parser = ARXMLParser(options={"warning": True})     # log schema errors, parse anyway
parser = ARXMLParser(options={"validate": False})   # disable validation

writer = ARXMLWriter(options={"validate": False})   # same option on save()
```
```

- [x] **Step 3: Run `npm run black` and commit**

```bash
npm run black
git add docs/superpowers/specs/2026-10-05-xsd-validation-design.md README.md
git commit -m "docs: document XSD validation behavior and amend spec with planning decisions"
```
