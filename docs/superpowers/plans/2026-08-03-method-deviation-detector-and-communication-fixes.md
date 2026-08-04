# Attribute/Method-Deviation Detector + SWComponentTemplate::Communication Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a tested tool that detects, for every py-armodel model class, which AUTOSAR attributes (aggregations/associations) defined in the R23-11 spec (XSD, cross-checked against the TPS PDFs) have no Python accessor method, then use that tool to fix all attribute deviations in the `SWComponentTemplate::Communication` package as the reference pattern and emit a machine-readable backlog for the remaining ~440 classes.

**Architecture:** The detector compares each implemented class's **own** XSD attributes against the class's **effective** Python accessor set (resolved through the Python MRO). A name-normalization matcher absorbs the project's naming conventions (pluralisation, `Ref`/`Refs`/`RefConditional`/`Value` suffixes, subtype-prefix splitting like `assemblySwConnector`→`connector`, and near-misses like `enableUpdated`→`enableUpdate`). The detector lives in `src/armodel/analysis/method_parity/` (importable, src-layout), emits a JSON + Markdown backlog, and is run as a console script. Fixes are TDD against the existing `test_Communication.py` harness.

**Tech Stack:** Python 3.8+, `ast` (stdlib) for Python-side extraction, regex over the R23-11 XSD text for spec-side extraction, `pytest`, py-armodel's existing model + test harness. No new runtime dependencies.

## Global Constraints

- AUTOSAR release target is **R23-11** (set via `AUTOSAR.setARRelease('R23-11')` before any parse/write). The XSD ground truth is `AUTOSAR_00052.xsd` (`Part of AUTOSAR Release: R23-11`).
- Source layout: library code under `src/armodel/`, tests mirror under `tests/test_armodel/`.
- Code style: max line length **79**, 4-space indent, **double quotes**, no comments unless asked, `camelCase` for AUTOSAR-derived methods, setters return `self`.
- Type annotations use Python 3.8-compatible syntax (project supports 3.8–3.13): use `typing.List`/`typing.Dict`/`typing.Optional`, **not** `list[...]`/`X | None`.
- Lint must pass: `npm run flake8` (E9, F63, F7, F82) and exclude generated `build/`.
- Every model-class test must instantiate via the `AUTOSAR` singleton with the release set (see existing `tests/.../test_Communication.py`).
- Do NOT rename a public accessor without keeping a deprecated alias for one release cycle (callers depend on current names).

## Background facts established by investigation

These are verified facts (not assumptions) that the tasks rely on:

1. The XSD marks every class attribute with `mmt.qualifiedName="ClassName.attrName"` inside the class's `<!-- element group for class <path> -->` block, and multiplicity with `pureMM.maxOccurs="-1"` (unbounded) or `"1"` (single). Class identity (no dot) is `mmt.qualifiedName="ClassName"`.
2. A clean deviation signal is obtained by comparing each class's **own** XSD attributes (framework attrs like `uuid`/`timestamp` are owned by `ARObject`/`Identifiable`, so they never appear as "own" of a domain class) against the class's **effective Python accessor set** (own + inherited via Python bases).
3. py-armodel accessor conventions per attribute `foo`:
   - single-valued: `self.foo: T = None`, `def getFoo(self) -> T:`, `def setFoo(self, value: T) -> "Self":`
   - multi-valued: `self.foos: List[T] = []`, `def addFoo(self, value: T)`, `def getFoos(self) -> List[T]:`
4. Confirmed deviations in `SWComponentTemplate::Communication` (from running the prototype detector), excluding the framework attr `variationPoint`:

   | Class | Genuinely missing accessors | Naming deviations (accessor exists, wrong name) |
   |---|---|---|
   | `ServerComSpec` | `getter`, `setter` | — |
   | `ClientComSpec` | `clientIntent`, `endToEndCallResponseTimeout`, `getter`, `setter`, `transformationComSpecProps` | — |
   | `SenderComSpec` | `dataUpdatePeriod`, `senderIntent`, `transmissionProps` | — |
   | `ReceiverComSpec` | `dataUpdatePeriod`, `externalReplacement`, `receiverIntent`, `receptionProps`, `replaceWith`, `syncCounterInit`, `transformationComSpecProps` | — |
   | `NonqueuedSenderComSpec` | — | `filter`→`dataFilter` (Task 8) |
   | `NonqueuedReceiverComSpec` | — | `enableUpdated`→`enableUpdate` (Task 7), `filter`→`dataFilter` (Task 8), `timeoutSubstitution`→`timeoutSubstitutionValue` (Task 8) |
   | `ParameterProvideComSpec` | `initValue`, `parameter` | — |

5. All listed missing attributes are single-valued (`pureMM.maxOccurs="1"`).
6. `Communication.py` already imports: `RefType`, `TimeValue`, `PositiveInteger`, `ValueSpecification`, `ARBoolean`, `ARNumerical`, `Describable`, `SwDataDefProps`, and defines/imports `TransformationComSpecProps`, `TransmissionAcknowledgementRequest`, `CompositeNetworkRepresentation`, `DataFilter`, `ReceptionComSpecProps`.

## File Structure

New detector package (importable, tested):

- Create `src/armodel/analysis/__init__.py` — empty, makes `armodel.analysis` a package.
- Create `src/armodel/analysis/method_parity/__init__.py` — re-exports the public API.
- Create `src/armodel/analysis/method_parity/xsd_attributes.py` — XSD text → `{class: {attr: AttrSpec}}`.
- Create `src/armodel/analysis/method_parity/py_accessors.py` — AST walk of `src/armodel/models` → `{class: effective-attr-set}` + `{class: file}`.
- Create `src/armodel/analysis/method_parity/normalize.py` — `matches(spec_attr, py_attr) -> bool` and the framework-exclude set.
- Create `src/armodel/analysis/method_parity/compare.py` — `find_deviations(...) -> {class: [AttrSpec]}`.
- Create `src/armodel/analysis/method_parity/report.py` — JSON + Markdown backlog writers.
- Create `src/armodel/analysis/method_parity/__main__.py` — CLI entry: `python -m armodel.analysis.method_parity <models_dir> <xsd> [--pdf-bases <json>] -o <out>`.

Tests (mirror under `tests/test_armodel/analysis/method_parity/`):

- Create `tests/test_armodel/analysis/__init__.py`
- Create `tests/test_armodel/analysis/method_parity/__init__.py`
- Create `tests/test_armodel/analysis/method_parity/test_xsd_attributes.py`
- Create `tests/test_armodel/analysis/method_parity/test_py_accessors.py`
- Create `tests/test_armodel/analysis/method_parity/test_normalize.py`
- Create `tests/test_armodel/analysis/method_parity/test_compare.py`

Model fixes (existing file, one new test file):

- Modify `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`
- Modify `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py`

Generated artifacts:

- Create `docs/requirements/method_parity_backlog.json` — detector output (committed).
- Create `docs/requirements/method_parity_backlog.md` — human-readable backlog (committed).

---

### Task 1: XSD attribute extractor

**Files:**
- Create: `src/armodel/analysis/__init__.py`
- Create: `src/armodel/analysis/method_parity/__init__.py`
- Create: `src/armodel/analysis/method_parity/xsd_attributes.py`
- Create: `tests/test_armodel/analysis/__init__.py`
- Create: `tests/test_armodel/analysis/method_parity/__init__.py`
- Test: `tests/test_armodel/analysis/method_parity/test_xsd_attributes.py`

**Interfaces:**
- Produces: `extract_class_attributes(xsd_text: str) -> Dict[str, Dict[str, "AttrSpec"]]` and dataclass `AttrSpec(name: str, multiplicity: str, container: str)`. `multiplicity` is `"many"` when `pureMM.maxOccurs="-1"`, else `"one"`. `container` is the nearest enclosing `name="<UPPER>"` element (e.g. `"DATA-UPDATE-PERIOD"`).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_armodel/analysis/method_parity/test_xsd_attributes.py
from armodel.analysis.method_parity.xsd_attributes import (
    AttrSpec, extract_class_attributes,
)

XSD_FIXTURE = """<?xml version="1.0"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <!-- element group for class AUTOSAR Templates::Demo::Widget -->
   <xsd:group name="WIDGET">
      <xsd:annotation>
         <xsd:appinfo source="tags">mmt.qualifiedName="Widget"</xsd:appinfo>
      </xsd:annotation>
      <xsd:sequence>
         <xsd:element maxOccurs="1" minOccurs="0" name="OWNER">
            <xsd:annotation>
               <xsd:appinfo source="tags">mmt.qualifiedName="Widget.owner";pureMM.maxOccurs="1"</xsd:appinfo>
            </xsd:annotation>
         </xsd:element>
         <xsd:element maxOccurs="1" minOccurs="0" name="PARTS">
            <xsd:annotation>
               <xsd:appinfo source="tags">mmt.qualifiedName="Widget.parts";pureMM.maxOccurs="-1"</xsd:appinfo>
            </xsd:annotation>
         </xsd:element>
      </xsd:sequence>
   </xsd:group>
</xsd:schema>
"""


def test_extract_class_attributes_returns_own_attributes():
    result = extract_class_attributes(XSD_FIXTURE)
    assert "Widget" in result
    assert set(result["Widget"].keys()) == {"owner", "parts"}
    assert result["Widget"]["owner"] == AttrSpec("owner", "one", "OWNER")
    assert result["Widget"]["parts"] == AttrSpec("parts", "many", "PARTS")


def test_attr_spec_is_hashable_and_comparable():
    a = AttrSpec("owner", "one", "OWNER")
    b = AttrSpec("owner", "one", "OWNER")
    assert a == b
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_xsd_attributes.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'armodel.analysis'`

- [ ] **Step 3: Write minimal implementation**

```python
# src/armodel/analysis/__init__.py
```

```python
# src/armodel/analysis/method_parity/__init__.py
from armodel.analysis.method_parity.xsd_attributes import (
    AttrSpec,
    extract_class_attributes,
)

__all__ = ["AttrSpec", "extract_class_attributes"]
```

```python
# src/armodel/analysis/method_parity/xsd_attributes.py
import re
from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class AttrSpec:
    name: str
    multiplicity: str
    container: str


_GROUP_COMMENT = re.compile(
    r"<!--\s*\w+\s+group for class\s+(.+?)\s*-->"
)
_QNAME = re.compile(r'mmt\.qualifiedName="([^"]+)"')
_MAXOCCURS = re.compile(r'pureMM\.maxOccurs="(-?\d)"')
_ELEMENT_NAME = re.compile(r'name="([A-Z][A-Z0-9-]+)"')


def _last_token(path: str) -> str:
    m = re.search(r"([A-Za-z0-9_]+)$", path.strip())
    return m.group(1) if m else ""


def extract_class_attributes(xsd_text: str) -> Dict[str, Dict[str, AttrSpec]]:
    result: Dict[str, Dict[str, AttrSpec]] = {}
    parts = _GROUP_COMMENT.split(xsd_text)
    # parts layout: [pre, path, body, path, body, ...]
    i = 1
    while i < len(parts):
        path = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        cls = _last_token(path)
        if cls:
            attrs: Dict[str, AttrSpec] = {}
            for qn in _QNAME.findall(body):
                if "." in qn:
                    owner, attr = qn.split(".", 1)
                    if owner == cls and attr not in attrs:
                        attrs[attr] = AttrSpec(attr, "one", "")
            # multiplicity + container: scan each qualifiedName occurrence
            for m in re.finditer(
                r'mmt\.qualifiedName="' + re.escape(cls) + r"\.([^.\"]+)\"",
                body,
            ):
                attr = m.group(1)
                window = body[max(0, m.start() - 1500): m.end() + 200]
                mo = _MAXOCCURS.search(window)
                mult = "many" if (mo and mo.group(1) == "-1") else "one"
                names = _ELEMENT_NAME.findall(
                    body[max(0, m.start() - 1500): m.start()]
                )
                container = names[-1] if names else ""
                attrs[attr] = AttrSpec(attr, mult, container)
            result[cls] = attrs
        i += 2
    return result
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_xsd_attributes.py -q`
Expected: PASS (2 passed)

- [ ] **Step 5: Validate against the real R23-11 XSD**

Run:
```bash
python -c "from armodel.analysis.method_parity import extract_class_attributes; t=open(r'D:/workspace/autosar-pdf/examples/xsd/AUTOSAR_00052.xsd',encoding='utf-8').read(); d=extract_class_attributes(t); print(len(d)); print(d['CompositionSwComponentType'])"
```
Expected: prints `2323` (or close) and a dict whose keys are exactly `{'component','connector','constantValueMapping','dataTypeMapping','instantiationRTEEventProps','physicalDimensionMapping'}`.

- [ ] **Step 6: Commit**

```bash
git add src/armodel/analysis tests/test_armodel/analysis
git commit -m "feat(analysis): add XSD attribute extractor for method-parity checks"
```

---

### Task 2: Python accessor extractor

**Files:**
- Create: `src/armodel/analysis/method_parity/py_accessors.py`
- Test: `tests/test_armodel/analysis/method_parity/test_py_accessors.py`

**Interfaces:**
- Consumes: `AttrSpec` is not needed here; this module is Python-only.
- Produces: `extract_python_classes(models_dir: str) -> Tuple[Dict[str, Set[str]], Dict[str, List[str]], Dict[str, str]]` returning `(own_attrs, bases, file_path)`. `effective_attrs(cls, own_attrs, bases, seen=None) -> Set[str]` walks the Python inheritance chain. Attribute names are derived from `self.<x> = ...` assignments in `__init__` plus accessor-method names (`get`/`set`/`add`/`create`/`removeAll` prefixes), with dunder and the noise set `{"parent","short_name","shortName"}` removed.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_armodel/analysis/method_parity/test_py_accessors.py
import os
import tempfile

from armodel.analysis.method_parity.py_accessors import (
    effective_attrs, extract_python_classes,
)


def _write(tmp, name, body):
    path = os.path.join(tmp, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    return path


def test_extract_python_classes_collects_attrs_and_bases():
    with tempfile.TemporaryDirectory() as tmp:
        _write(tmp, "pkg/__init__.py", "")
        _write(tmp, "pkg/base.py", "class Base:\n    def __init__(self):\n        self.uuid = None\n        self.getUuid\n")
        _write(tmp, "pkg/widget.py",
               "from pkg.base import Base\n"
               "class Widget(Base):\n"
               "    def __init__(self):\n"
               "        super().__init__()\n"
               "        self.parts = []\n"
               "    def getParts(self):\n"
               "        return self.parts\n"
               "    def addPart(self, value):\n"
               "        self.parts.append(value)\n"
               "    def removeAllParts(self):\n"
               "        self.parts.clear()\n")
        own, bases, files = extract_python_classes(tmp)
        assert "Widget" in own and "Base" in own
        assert "parts" in own["Widget"]
        assert "uuid" not in own["Widget"]  # owned by Base, not Widget
        assert bases["Widget"] == ["Base"]


def test_effective_attrs_walks_inheritance():
    own = {"Widget": {"parts"}, "Base": {"uuid"}}
    bases = {"Widget": ["Base"], "Base": []}
    assert effective_attrs("Widget", own, bases) == {"parts", "uuid"}


def test_method_name_prefixes_become_attrs():
    with tempfile.TemporaryDirectory() as tmp:
        _write(tmp, "pkg/__init__.py", "")
        _write(tmp, "pkg/c.py",
               "class C:\n"
               "    def __init__(self):\n"
               "        pass\n"
               "    def getHandleOutOfRange(self):\n"
               "        pass\n"
               "    def setHandleOutOfRange(self, v):\n"
               "        pass\n")
        own, _b, _f = extract_python_classes(tmp)
        assert "handleOutOfRange" in own["C"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_py_accessors.py -q`
Expected: FAIL with `ModuleNotFoundError: ... py_accessors`

- [ ] **Step 3: Write minimal implementation**

```python
# src/armodel/analysis/method_parity/py_accessors.py
import ast
import os
from typing import Dict, List, Set, Tuple

_NOISE = {"parent", "short_name", "shortName"}
_PREFIXES = ("get", "set", "add", "create")


def _from_method(name: str) -> Set[str]:
    out: Set[str] = set()
    for pre in _PREFIXES:
        if name.startswith(pre) and len(name) > len(pre):
            rest = name[len(pre):]
            out.add(rest[0].lower() + rest[1:])
    if name.startswith("removeAll") and len(name) > len("removeAll"):
        rest = name[len("removeAll"):]
        if rest.endswith("s"):
            rest = rest[:-1]
        out.add(rest[0].lower() + rest[1:])
    return out


def _class_attrs(node: ast.ClassDef) -> Set[str]:
    attrs: Set[str] = set()
    for item in node.body:
        if isinstance(item, ast.FunctionDef) and item.name == "__init__":
            for st in ast.walk(item):
                if (isinstance(st, ast.Assign)
                        and isinstance(st.targets[0], ast.Attribute)
                        and isinstance(st.targets[0].value, ast.Name)
                        and st.targets[0].value.id == "self"):
                    attrs.add(st.targets[0].attr)
        if isinstance(item, ast.FunctionDef):
            attrs |= _from_method(item.name)
    return {a for a in attrs if not a.startswith("_")} - _NOISE


def extract_python_classes(
    models_dir: str,
) -> Tuple[Dict[str, Set[str]], Dict[str, List[str]], Dict[str, str]]:
    own: Dict[str, Set[str]] = {}
    bases: Dict[str, List[str]] = {}
    files: Dict[str, str] = {}
    for dp, _dn, fns in os.walk(models_dir):
        if "__pycache__" in dp:
            continue
        for fn in fns:
            if not fn.endswith(".py"):
                continue
            path = os.path.join(dp, fn)
            try:
                tree = ast.parse(open(path, encoding="utf-8").read())
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if not isinstance(node, ast.ClassDef):
                    continue
                own[node.name] = _class_attrs(node)
                bases[node.name] = [
                    b.id for b in node.bases if isinstance(b, ast.Name)
                ]
                files[node.name] = path.replace("\\", "/")
    return own, bases, files


def effective_attrs(
    cls: str,
    own: Dict[str, Set[str]],
    bases: Dict[str, List[str]],
    seen: Set[str] = None,
) -> Set[str]:
    seen = seen or set()
    if cls in seen or cls not in own:
        return set()
    seen.add(cls)
    result: Set[str] = set(own[cls])
    for b in bases.get(cls, []):
        result |= effective_attrs(b, own, bases, seen)
    return result
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_py_accessors.py -q`
Expected: PASS (3 passed)

- [ ] **Step 5: Validate against the real models**

Run:
```bash
python -c "from armodel.analysis.method_parity.py_accessors import extract_python_classes, effective_attrs; o,b,f=extract_python_classes('src/armodel/models'); print(len(o)); print(sorted(effective_attrs('CompositionSwComponentType',o,b)))"
```
Expected: prints a class count (~924) and an attribute set that includes `components`, `constantValueMappingRefs`, `dataTypeMappings`, `instantiationRTEEventProps`.

- [ ] **Step 6: Commit**

```bash
git add src/armodel/analysis/method_parity/py_accessors.py tests/test_armodel/analysis/method_parity/test_py_accessors.py
git commit -m "feat(analysis): add Python accessor extractor for method-parity checks"
```

---

### Task 3: Name-normalization matcher

**Files:**
- Create: `src/armodel/analysis/method_parity/normalize.py`
- Test: `tests/test_armodel/analysis/method_parity/test_normalize.py`

**Interfaces:**
- Produces: `matches(spec_attr: str, py_attr: str) -> bool` and constant `FRAMEWORK_EXCLUDE: Set[str]` (attribute names treated as framework-level and excluded from deviation output, currently `{"variationPoint", "shortLabel"}`).

- [ ] **Step 1: Write the failing test (all real cases from the investigation)**

```python
# tests/test_armodel/analysis/method_parity/test_normalize.py
import pytest

from armodel.analysis.method_parity.normalize import FRAMEWORK_EXCLUDE, matches


@pytest.mark.parametrize("spec_attr,py_attr,expected", [
    # accepted equivalences (standard py-armodel conventions)
    ("component", "components", True),                 # plural
    ("component", "swComponentPrototype", True),       # subtype-prefix split (py longer)
    ("connector", "assemblySwConnector", True),        # subtype-prefix split (py longer)
    ("constantValueMapping", "constantValueMappingRefs", True),  # Refs suffix
    ("parameter", "parameterRef", True),               # Ref suffix
    ("parameter", "parameterRefConditional", True),    # RefConditional suffix
    ("enableUpdate", "enableUpdate", True),            # exact
    # flagged deviations: accessor exists under a wrong name -> renamed in fix tasks
    ("dataFilter", "filter", False),                   # 'data' prefix dropped
    ("timeoutSubstitutionValue", "timeoutSubstitution", False),  # 'Value' missing
    ("enableUpdate", "enableUpdated", False),          # trailing 'd' typo
    # genuine mismatches
    ("physicalDimensionMapping", "elements", False),
    ("getter", "operationRef", False),
])
def test_matches(spec_attr, py_attr, expected):
    assert matches(spec_attr, py_attr) is expected


def test_framework_exclude_contains_variation_point():
    assert "variationPoint" in FRAMEWORK_EXCLUDE
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_normalize.py -q`
Expected: FAIL with `ModuleNotFoundError: ... normalize`

- [ ] **Step 3: Write minimal implementation**

```python
# src/armodel/analysis/method_parity/normalize.py
import re
from typing import Set

FRAMEWORK_EXCLUDE: Set[str] = {"variationPoint", "shortLabel"}

# Only the well-established py-armodel reference suffixes are treated as
# equivalences. Near-misses (enableUpdated, filter vs dataFilter, missing
# 'Value') are intentionally NOT matched so they get flagged and renamed.
_REF_SUFFIX = re.compile(r"(refs?|refconditional|instanceref)s?$")


def _singular(word: str) -> str:
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def _variants(attr: str) -> Set[str]:
    a = attr.lower()
    stripped = _REF_SUFFIX.sub("", a)
    return {a, _singular(a), stripped, _singular(stripped)}


def matches(spec_attr: str, py_attr: str) -> bool:
    s = spec_attr.lower()
    if s == py_attr.lower():
        return True
    pvars = _variants(py_attr)
    if s in pvars:
        return True
    # subtype-prefix split: '<Subtype><SpecAttr>' (py longer) ends with spec attr
    for v in pvars:
        if v.endswith(s) and len(v) > len(s):
            return True
    return False
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_normalize.py -q`
Expected: PASS (12 passed). If any case fails, adjust the order of suffix stripping in `_variants` only — do not weaken a `False` assertion.

- [ ] **Step 5: Commit**

```bash
git add src/armodel/analysis/method_parity/normalize.py tests/test_armodel/analysis/method_parity/test_normalize.py
git commit -m "feat(analysis): add name-normalization matcher for attribute parity"
```

---

### Task 4: Deviation comparator

**Files:**
- Create: `src/armodel/analysis/method_parity/compare.py`
- Test: `tests/test_armodel/analysis/method_parity/test_compare.py`

**Interfaces:**
- Consumes: `AttrSpec` (Task 1), `effective_attrs` (Task 2), `matches`/`FRAMEWORK_EXCLUDE` (Task 3).
- Produces: `find_deviations(xsd_own, py_own, py_bases) -> Dict[str, List[AttrSpec]]` returning, for each implemented class that owns at least one XSD attribute with no matching Python accessor (after normalization and framework exclusion), the list of missing `AttrSpec`. A class is "implemented" iff it appears in both `xsd_own` and `py_own`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_armodel/analysis/method_parity/test_compare.py
from armodel.analysis.method_parity.compare import find_deviations
from armodel.analysis.method_parity.xsd_attributes import AttrSpec


def test_find_deviations_reports_unmatched_own_attrs():
    xsd_own = {
        "Widget": {
            "owner": AttrSpec("owner", "one", "OWNER"),
            "parts": AttrSpec("parts", "many", "PARTS"),
            "color": AttrSpec("color", "one", "COLOR"),
        },
        "NotImplemented": {
            "x": AttrSpec("x", "one", "X"),
        },
    }
    py_own = {
        "Widget": {"owner", "partsList"},   # partsList should match parts via subtype-prefix
        "Other": {"q"},
    }
    py_bases = {"Widget": [], "Other": []}

    dev = find_deviations(xsd_own, py_own, py_bases)
    assert dev == {"Widget": [AttrSpec("color", "one", "COLOR")]}


def test_find_deviations_excludes_framework_attrs():
    xsd_own = {"Widget": {"variationPoint": AttrSpec("variationPoint", "one", "")}}
    py_own = {"Widget": set()}
    dev = find_deviations(xsd_own, py_own, {})
    assert dev == {}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_compare.py -q`
Expected: FAIL with `ModuleNotFoundError: ... compare`

- [ ] **Step 3: Write minimal implementation**

```python
# src/armodel/analysis/method_parity/compare.py
from typing import Dict, List, Set

from armodel.analysis.method_parity.normalize import (
    FRAMEWORK_EXCLUDE, matches,
)
from armodel.analysis.method_parity.py_accessors import effective_attrs
from armodel.analysis.method_parity.xsd_attributes import AttrSpec


def find_deviations(
    xsd_own: Dict[str, Dict[str, AttrSpec]],
    py_own: Dict[str, Set[str]],
    py_bases: Dict[str, List[str]],
) -> Dict[str, List[AttrSpec]]:
    deviations: Dict[str, List[AttrSpec]] = {}
    for cls, attrs in xsd_own.items():
        if cls not in py_own:
            continue
        eff = effective_attrs(cls, py_own, py_bases)
        missing: List[AttrSpec] = []
        for name, spec in attrs.items():
            if name in FRAMEWORK_EXCLUDE:
                continue
            if not any(matches(name, p) for p in eff):
                missing.append(spec)
        if missing:
            deviations[cls] = sorted(missing, key=lambda s: s.name)
    return deviations
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_compare.py -q`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add src/armodel/analysis/method_parity/compare.py tests/test_armodel/analysis/method_parity/test_compare.py
git commit -m "feat(analysis): add deviation comparator for attribute parity"
```

---

### Task 5: Report writers + CLI runner

**Files:**
- Create: `src/armodel/analysis/method_parity/report.py`
- Create: `src/armodel/analysis/method_parity/__main__.py`
- Modify: `src/armodel/analysis/method_parity/__init__.py` (re-export new API)
- Test: extend `tests/test_armodel/analysis/method_parity/test_compare.py` (reuse existing module; report is covered by an end-to-end run in Step 5)

**Interfaces:**
- Produces: `write_json(deviations, py_files, path) -> None`, `write_markdown(deviations, xsd_own, path) -> None`, and CLI `python -m armodel.analysis.method_parity <models_dir> <xsd_path> -o <out_prefix>` that writes `<out_prefix>.json` and `<out_prefix>.md`.

- [ ] **Step 1: Write the failing test**

```python
# append to tests/test_armodel/analysis/method_parity/test_compare.py
import json
import os

from armodel.analysis.method_parity.report import write_json, write_markdown


def test_write_json_and_markdown_roundtrip(tmp_path):
    xsd_own = {
        "Widget": {"color": AttrSpec("color", "one", "COLOR")},
    }
    deviations = {"Widget": [AttrSpec("color", "one", "COLOR")]}
    py_files = {"Widget": "pkg/widget.py"}
    j = tmp_path / "out.json"
    m = tmp_path / "out.md"
    write_json(deviations, py_files, str(j))
    write_markdown(deviations, xsd_own, str(m))
    data = json.loads(j.read_text(encoding="utf-8"))
    assert data["Widget"][0]["name"] == "color"
    assert "Widget" in m.read_text(encoding="utf-8")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/test_compare.py::test_write_json_and_markdown_roundtrip -q`
Expected: FAIL with `ModuleNotFoundError: ... report`

- [ ] **Step 3: Write minimal implementation**

```python
# src/armodel/analysis/method_parity/report.py
import json
from dataclasses import asdict
from typing import Dict

from armodel.analysis.method_parity.xsd_attributes import AttrSpec


def write_json(deviations: Dict[str, list], py_files: Dict[str, str], path: str) -> None:
    out = {
        cls: [asdict(s) for s in specs]
        for cls, specs in deviations.items()
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"deviations": out,
                   "files": {c: py_files.get(c, "") for c in out}}, f, indent=2)


def write_markdown(
    deviations: Dict[str, list],
    xsd_own: Dict[str, Dict[str, AttrSpec]],
    path: str,
) -> None:
    lines = ["# Method-Parity Deviation Backlog", ""]
    lines.append(
        "Own AUTOSAR attributes (per R23-11 XSD) with no matching Python "
        "accessor, after name normalisation. `variationPoint`/`shortLabel` "
        "are treated as framework-level and excluded."
    )
    lines.append("")
    for cls in sorted(deviations):
        lines.append(f"## {cls}")
        lines.append("")
        lines.append("| Attribute | Multiplicity | Container |")
        lines.append("|---|---|---|")
        for spec in deviations[cls]:
            lines.append(f"| {spec.name} | {spec.multiplicity} | {spec.container} |")
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
```

```python
# src/armodel/analysis/method_parity/__main__.py
import argparse
import sys

from armodel.analysis.method_parity.compare import find_deviations
from armodel.analysis.method_parity.py_accessors import extract_python_classes
from armodel.analysis.method_parity.report import write_json, write_markdown
from armodel.analysis.method_parity.xsd_attributes import extract_class_attributes


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="armodel.analysis.method_parity")
    p.add_argument("models_dir")
    p.add_argument("xsd_path")
    p.add_argument("-o", "--out", required=True, help="output prefix")
    args = p.parse_args(argv)

    xsd_text = open(args.xsd_path, encoding="utf-8").read()
    xsd_own = extract_class_attributes(xsd_text)
    py_own, py_bases, py_files = extract_python_classes(args.models_dir)
    dev = find_deviations(xsd_own, py_own, py_bases)
    write_json(dev, py_files, args.out + ".json")
    write_markdown(dev, xsd_own, args.out + ".md")
    total = sum(len(v) for v in dev.values())
    print(f"{len(dev)} classes, {total} missing attributes -> {args.out}.json/.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Update `__init__.py`:
```python
# src/armodel/analysis/method_parity/__init__.py
from armodel.analysis.method_parity.compare import find_deviations
from armodel.analysis.method_parity.py_accessors import (
    effective_attrs, extract_python_classes,
)
from armodel.analysis.method_parity.normalize import FRAMEWORK_EXCLUDE, matches
from armodel.analysis.method_parity.report import write_json, write_markdown
from armodel.analysis.method_parity.xsd_attributes import (
    AttrSpec, extract_class_attributes,
)

__all__ = [
    "AttrSpec", "extract_class_attributes", "extract_python_classes",
    "effective_attrs", "matches", "FRAMEWORK_EXCLUDE", "find_deviations",
    "write_json", "write_markdown",
]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_armodel/analysis/method_parity/ -q`
Expected: PASS (all detector tests green)

- [ ] **Step 5: Generate the committed backlog and verify against the known Communication figures**

Run:
```bash
python -m armodel.analysis.method_parity src/armodel/models D:/workspace/autosar-pdf/examples/xsd/AUTOSAR_00052.xsd -o docs/requirements/method_parity_backlog
```
Expected: prints `4XX classes, ~1200 missing attributes`. Open `docs/requirements/method_parity_backlog.md` and confirm the `## ClientComSpec` section lists `clientIntent`, `endToEndCallResponseTimeout`, `getter`, `setter`, `transformationComSpecProps`.

- [ ] **Step 6: Commit**

```bash
git add src/armodel/analysis/method_parity/report.py src/armodel/analysis/method_parity/__main__.py src/armodel/analysis/method_parity/__init__.py tests/test_armodel/analysis/method_parity/test_compare.py docs/requirements/method_parity_backlog.json docs/requirements/method_parity_backlog.md
git commit -m "feat(analysis): add method-parity report writers, CLI, and R23-11 backlog"
```

---

### Task 6: Reference fix — ServerComSpec getter/setter accessors

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py` (class `ServerComSpec`, currently at lines ~1591–1665; `__init__` ends after `self.transformationComSpecProps: List[TransformationComSpecProps] = []`)
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py`

**Interfaces:**
- Produces: `ServerComSpec.getGetter() -> RefType`, `setGetter(value: RefType) -> ServerComSpec`, `getSetter() -> RefType`, `setSetter(value: RefType) -> ServerComSpec`. Both are single-valued references (`GETTER-REF`/`SETTER-REF` to `Field`), typed `RefType` to match the existing `operationRef` accessor.

- [ ] **Step 1: Write the failing test**

Append to `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py`:

```python
def test_ServerComSpec_getter_setter_accessors(self):
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ServerComSpec
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    spec = ServerComSpec()
    assert spec.getGetter() is None
    assert spec.getSetter() is None

    getter = RefType()
    setter = RefType()
    spec.setGetter(getter).setSetter(setter)

    assert spec.getGetter() is getter
    assert spec.getSetter() is setter
```

(Place it inside the existing `Test_..._Communication` class in that file; use the class/section the file already uses for ServerComSpec.)

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest "tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py" -k ServerComSpec_getter -q`
Expected: FAIL with `AttributeError: 'ServerComSpec' object has no attribute 'getGetter'`

- [ ] **Step 3: Write minimal implementation**

In `ServerComSpec.__init__`, after the `self.transformationComSpecProps` line, add:

```python
        self.getter: RefType = None
        self.setter: RefType = None
```

After the existing `addTransformationComSpecProps`/`getTransformationComSpecProps` methods in `ServerComSpec`, add:

```python
    def getGetter(self) -> RefType:
        return self.getter

    def setGetter(self, value: RefType):
        self.getter = value
        return self

    def getSetter(self) -> RefType:
        return self.setter

    def setSetter(self, value: RefType):
        self.setter = value
        return self
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest "tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py" -k ServerComSpec_getter -q`
Expected: PASS

- [ ] **Step 5: Verify ServerComSpec drops out of the deviation backlog**

Run:
```bash
python -m armodel.analysis.method_parity src/armodel/models D:/workspace/autosar-pdf/examples/xsd/AUTOSAR_00052.xsd -o /tmp/mp_check
grep -A4 "## ServerComSpec" /tmp/mp_check.md || echo "ServerComSpec clean (no longer in backlog)"
```
Expected: `ServerComSpec clean (no longer in backlog)` — or its section lists no `getter`/`setter`.

- [ ] **Step 6: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py
git commit -m "feat(models): add ServerComSpec getter/setter accessors per R23-11"
```

---

### Task 7: Reference fix — naming deviations in NonqueuedReceiverComSpec

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py` (class `NonqueuedReceiverComSpec`)
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py`

**Context:** The spec attributes are `enableUpdate`, `timeoutSubstitutionValue`, `dataFilter`. Python currently exposes `enableUpdated`, `timeoutSubstitution`, `filter`. Renames are made **additively**: new canonical accessors are added; old accessors are kept as thin deprecated aliases that delegate, so existing callers keep working.

**Interfaces:**
- Produces (new, canonical): `getEnableUpdate`/`setEnableUpdate`. Keeps (deprecated alias): `getEnableUpdated`/`setEnableUpdated` delegating to the canonical accessor.

- [ ] **Step 1: Write the failing test**

Append to `test_Communication.py`:

```python
def test_NonqueuedReceiverComSpec_canonical_enableUpdate(self):
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean

    spec = NonqueuedReceiverComSpec()
    assert spec.getEnableUpdate() is None

    flag = ARBoolean()
    spec.setEnableUpdate(flag)
    assert spec.getEnableUpdate() is flag
    assert spec.getEnableUpdated() is flag  # deprecated alias delegates

    spec.setEnableUpdated(None)
    assert spec.getEnableUpdate() is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest "tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py" -k NonqueuedReceiverComSpec_canonical -q`
Expected: FAIL with `AttributeError: ... getEnableUpdate`

- [ ] **Step 3: Write minimal implementation**

This task demonstrates the additive-rename pattern for ONE attribute: `enableUpdate`. (The other naming deviations on this class — `dataFilter`, `timeoutSubstitutionValue` — are handled in Task 8.) In `NonqueuedReceiverComSpec.__init__`, rename the field `self.enableUpdated` to the canonical name:

```python
        self.enableUpdate: ARBoolean = None
```

Replace the existing `getEnableUpdated`/`setEnableUpdated` methods with canonical accessors plus a delegating alias:

```python
    def getEnableUpdate(self):
        return self.enableUpdate

    def setEnableUpdate(self, value):
        self.enableUpdate = value
        return self

    def getEnableUpdated(self):   # deprecated alias
        return self.getEnableUpdate()

    def setEnableUpdated(self, value):   # deprecated alias
        return self.setEnableUpdate(value)
```

Do not touch `filter` or `timeoutSubstitution` in this task.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest "tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py" -k NonqueuedReceiverComSpec -q`
Expected: PASS

- [ ] **Step 5: Grep for external callers of the old names and confirm nothing breaks**

Run:
```bash
npm run flake8
python -m pytest tests/test_armodel -q
```
Expected: flake8 clean; all model tests pass.

- [ ] **Step 6: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py
git commit -m "fix(models): align NonqueuedReceiverComSpec attribute names with R23-11 (additive aliases)"
```

---

### Task 8: Communication sweep — remaining classes per backlog

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py`

**Context:** Apply the pattern proven in Tasks 6–7 to the remaining Communication classes listed in the investigation table. Each attribute is single-valued (`pureMM.maxOccurs="1"`). Resolve each Python type from the XSD container name using this table; when the container is `*-REF`/`*-REFS`, the type is `RefType`; `*-PROPS`/`*-PROPSS` aggregations become `List[TransformationComSpecProps]` via `addX`/`getX`; everything else uses the named AUTOSAR type already imported in `Communication.py`.

| Class | Attribute | Container | Python type / pattern |
|---|---|---|---|
| `SenderComSpec` | `dataUpdatePeriod` | `DATA-UPDATE-PERIOD` | `TimeValue` (imported) |
| `SenderComSpec` | `senderIntent` | `SENDER-INTENT` | `TransmissionAcknowledgementRequest` (defined in this module) |
| `SenderComSpec` | `transmissionProps` | `TRANSMISSION-PROPS` | `List[TransformationComSpecProps]` (`addTransmissionProps`/`getTransmissionProps`) |
| `NonqueuedSenderComSpec` | `dataFilter` | `DATA-FILTER` | `DataFilter` (naming deviation: rename `filter`→`dataFilter` additively, mirroring Task 7) |
| `NonqueuedReceiverComSpec` | `dataFilter` | `DATA-FILTER` | `DataFilter` (naming deviation: rename `filter`→`dataFilter` additively, mirroring Task 7) |
| `NonqueuedReceiverComSpec` | `timeoutSubstitutionValue` | `TIMEOUT-SUBSTITUTION-VALUE` | `ValueSpecification` (naming deviation: rename `timeoutSubstitution`→`timeoutSubstitutionValue` additively) |
| `ClientComSpec` | `clientIntent` | `CLIENT-INTENT` | `RefType` (reference, `*-REF`) |
| `ClientComSpec` | `endToEndCallResponseTimeout` | `END-TO-END-CALL-RESPONSE-TIMEOUT` | `TimeValue` |
| `ClientComSpec` | `getter` | `GETTER-REF` | `RefType` |
| `ClientComSpec` | `setter` | `SETTER-REF` | `RefType` |
| `ClientComSpec` | `transformationComSpecProps` | `TRANSFORMATION-COM-SPEC-PROPSS` | `List[TransformationComSpecProps]` (`addTransformationComSpecProps`/`getTransformationComSpecProps`) |
| `ReceiverComSpec` | `dataUpdatePeriod` | `DATA-UPDATE-PERIOD` | `TimeValue` |
| `ReceiverComSpec` | `externalReplacement` | `EXTERNAL-REPLACEMENT-REF` | `RefType` |
| `ReceiverComSpec` | `receiverIntent` | `RECEIVER-INTENT` | `ReceptionComSpecProps` (single-valued; add `getReceiverIntent`/`setReceiverIntent` with its own field) |
| `ReceiverComSpec` | `receptionProps` | `RECEPTION-PROPS` | `List[ReceptionComSpecProps]` (`addReceptionProps`/`getReceptionProps`; import `ReceptionComSpecProps` if not already imported) |
| `ReceiverComSpec` | `replaceWith` | `REPLACE-WITH` | `PositiveInteger` (imported) |
| `ReceiverComSpec` | `syncCounterInit` | `SYNC-COUNTER-INIT` | `PositiveInteger` |
| `ReceiverComSpec` | `transformationComSpecProps` | `TRANSFORMATION-COM-SPEC-PROPSS` | `List[TransformationComSpecProps]` |
| `ParameterProvideComSpec` | `initValue` | `INIT-VALUE` | `ValueSpecification` (imported) |
| `ParameterProvideComSpec` | `parameter` | `PARAMETER-REF` | `RefType` (genuinely missing on this class; add `getParameter`/`setParameter`) |

If running the detector after Task 5 shows any of the above are already satisfied (e.g. an accessor exists under a name the matcher now accepts), skip that attribute — do not add a duplicate.

**Interfaces:**
- Produces: the accessors listed above, each following the `get`/`set` (single) or `add`/`get` (multi) convention with setters returning `self`. For naming deviations (`dataFilter` on both `*SenderComSpec`/`NonqueuedReceiverComSpec`, and `timeoutSubstitutionValue`), old accessors are kept as deprecated aliases.

- [ ] **Step 1: Write the failing tests (parametrised over single-valued accessors)**

Append to `test_Communication.py`:

```python
import pytest


@pytest.mark.parametrize("class_name,attr", [
    ("SenderComSpec", "dataUpdatePeriod"),
    ("SenderComSpec", "senderIntent"),
    ("ClientComSpec", "clientIntent"),
    ("ClientComSpec", "endToEndCallResponseTimeout"),
    ("ClientComSpec", "getter"),
    ("ClientComSpec", "setter"),
    ("ReceiverComSpec", "dataUpdatePeriod"),
    ("ReceiverComSpec", "externalReplacement"),
    ("ReceiverComSpec", "replaceWith"),
    ("ReceiverComSpec", "syncCounterInit"),
    ("ParameterProvideComSpec", "initValue"),
])
def test_Communication_missing_single_valued_accessor(self, class_name, attr):
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate import Communication as M
    cls = getattr(M, class_name)
    obj = cls()
    cap = attr[:1].upper() + attr[1:]
    getter = getattr(obj, "get" + cap)
    setter = getattr(obj, "set" + cap)
    assert getter() is None
    sentinel = object()
    assert setter(sentinel) is obj   # setter returns self for chaining
    assert getter() is sentinel


def test_Communication_transformation_com_spec_props_multi():
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
        ClientComSpec, ReceiverComSpec, SenderComSpec, TransformationComSpecProps,
    )
    for cls, add_name, get_name in [
        (ClientComSpec, "addTransformationComSpecProps", "getTransformationComSpecProps"),
        (ReceiverComSpec, "addTransformationComSpecProps", "getTransformationComSpecProps"),
        (SenderComSpec, "addTransmissionProps", "getTransmissionProps"),
    ]:
        obj = cls()
        item = TransformationComSpecProps.__new__(TransformationComSpecProps)
        getattr(obj, add_name)(item)
        assert item in getattr(obj, get_name)()
```

Also add focused tests for the two `ReceptionComSpecProps`-typed attributes and the
`parameter` reference, which need their own fields:

```python
def test_ReceiverComSpec_reception_props_and_receiver_intent():
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
        ReceiverComSpec, ReceptionComSpecProps,
    )
    obj = ReceiverComSpec()
    assert obj.getReceptionProps() == []
    item = ReceptionComSpecProps.__new__(ReceptionComSpecProps)
    obj.addReceptionProps(item)
    assert item in obj.getReceptionProps()
    assert obj.getReceiverIntent() is None
    obj.setReceiverIntent(item)
    assert obj.getReceiverIntent() is item


def test_ParameterProvideComSpec_parameter():
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ParameterProvideComSpec
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
    obj = ParameterProvideComSpec()
    assert obj.getParameter() is None
    ref = RefType()
    assert obj.setParameter(ref) is obj
    assert obj.getParameter() is ref
```

And tests for the two remaining naming deviations (canonical name introduced, old name kept as alias):

```python
def test_Communication_data_filter_naming_deviation():
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
        NonqueuedSenderComSpec, NonqueuedReceiverComSpec,
    )
    for cls in (NonqueuedSenderComSpec, NonqueuedReceiverComSpec):
        obj = cls()
        assert obj.getDataFilter() is None
        sentinel = object()
        obj.setDataFilter(sentinel)
        assert obj.getDataFilter() is sentinel
        assert obj.getFilter() is sentinel     # deprecated alias delegates


def test_NonqueuedReceiverComSpec_timeout_substitution_value_naming():
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec
    obj = NonqueuedReceiverComSpec()
    assert obj.getTimeoutSubstitutionValue() is None
    sentinel = object()
    obj.setTimeoutSubstitutionValue(sentinel)
    assert obj.getTimeoutSubstitutionValue() is sentinel
    assert obj.getTimeoutSubstitution() is sentinel   # deprecated alias delegates
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest "tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py" -k "Communication_missing_single_valued_accessor or Communication_transformation" -q`
Expected: FAIL (accessors missing)

- [ ] **Step 3: Write minimal implementation**

For each row, add the field in the class `__init__` and the accessor pair, following the exact style of `ServerComSpec.getOperationRef`/`setOperationRef` (single) and `ServerComSpec.addTransformationComSpecProps`/`getTransformationComSpecProps` (multi). Add `ReceptionComSpecProps` to the imports at the top of `Communication.py` if it is not already imported, and define a minimal `ReceptionComSpecProps(ARObject)` class in this module if it does not yet exist (constructor taking no args, like `TransformationComSpecProps`).

For the naming deviations `NonqueuedSenderComSpec.dataFilter` and `NonqueuedReceiverComSpec.dataFilter` (current accessor `filter` on both classes) and `NonqueuedReceiverComSpec.timeoutSubstitutionValue` (current `timeoutSubstitution`), apply the additive-rename pattern: introduce the canonical accessor operating on a renamed field, and make the old accessor delegate. Concretely, apply this to BOTH `NonqueuedSenderComSpec` and `NonqueuedReceiverComSpec` (rename `self.filter` -> `self.dataFilter` in their `__init__`):

```python
    # in __init__: rename self.filter -> self.dataFilter
    def getDataFilter(self):
        return self.dataFilter

    def setDataFilter(self, value):
        self.dataFilter = value
        return self

    def getFilter(self):          # deprecated alias
        return self.getDataFilter()

    def setFilter(self, value):   # deprecated alias
        return self.setDataFilter(value)
```

And for `NonqueuedReceiverComSpec` rename `self.timeoutSubstitution` -> `self.timeoutSubstitutionValue` with `getTimeoutSubstitutionValue`/`setTimeoutSubstitutionValue` canonical and `getTimeoutSubstitution`/`setTimeoutSubstitution` delegating aliases (mirror exactly the Task 7 `enableUpdate`/`enableUpdated` pair).

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest "tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py" -q`
Expected: PASS (all Communication tests green)

- [ ] **Step 5: Confirm naming deviations are also resolved by the matcher**

Run:
```bash
npm run flake8
python -m armodel.analysis.method_parity src/armodel/models D:/workspace/autosar-pdf/examples/xsd/AUTOSAR_00052.xsd -o /tmp/mp_check
grep -E "## (SenderComSpec|NonqueuedSenderComSpec|ClientComSpec|ReceiverComSpec|NonqueuedReceiverComSpec|ParameterProvideComSpec)" -A6 /tmp/mp_check.md
```
Expected: flake8 clean; the grep shows none of those class headings with remaining `dataFilter`/`parameter`/`enableUpdate`/`getter`/`setter` rows. (Abstract-base mismatches are acceptable; only the rows above must be gone.)

- [ ] **Step 6: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/test_Communication.py
git commit -m "feat(models): complete SWComponentTemplate::Communication attribute parity per R23-11"
```

---

### Task 9: Regenerate backlog and verify Communication is clean

**Files:**
- Modify (regenerate): `docs/requirements/method_parity_backlog.json`, `docs/requirements/method_parity_backlog.md`

- [ ] **Step 1: Regenerate the committed backlog**

Run:
```bash
python -m armodel.analysis.method_parity src/armodel/models D:/workspace/autosar-pdf/examples/xsd/AUTOSAR_00052.xsd -o docs/requirements/method_parity_backlog
```
Expected: prints a class/attribute total **lower** than the Task 5 baseline (Communication classes removed).

- [ ] **Step 2: Verify the full test suite still passes**

Run:
```bash
python scripts/run_tests.py --unit
```
Expected: all unit tests pass, including the new accessor tests and the existing integration tests are unaffected.

- [ ] **Step 3: Commit the regenerated backlog**

```bash
git add docs/requirements/method_parity_backlog.json docs/requirements/method_parity_backlog.md
git commit -m "docs(requirements): regenerate method-parity backlog after Communication fixes"
```

---

## Follow-up plans (explicitly out of scope for this plan)

The detector produced in Tasks 1–5 is the force multiplier. The remaining ~440 classes with deviations (top contributors: `SystemTemplate::Fibex`, `CommonStructure::Timing`, `CommonStructure::MeasurementCalibrationSupport`, `BswModuleTemplate::BswBehavior`, `SystemTemplate::NetworkManagement`) should each become a **separate plan per template**, following the identical workflow:

1. Read the class section in `docs/requirements/method_parity_backlog.md`.
2. For each missing attribute, resolve its Python type from the XSD container (`*-REF`→`RefType`, `*-PROPSS`→`List[TransformationComSpecProps]`-style aggregation, primitive→`ARBoolean`/`ARFloat`/`PositiveInteger`/`TimeValue`, else the named model class).
3. Add `get`/`set` (single) or `add`/`get` (multi) accessors TDD; apply additive renames for naming deviations.
4. Re-run the detector and confirm the class drops out.

Do not attempt all 440 in one plan — each template is an independently reviewable unit.
