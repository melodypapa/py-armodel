# AUTOSAR Model Class Check Rules

This document defines the mandatory check rules for verifying **any** AUTOSAR
model class before it is considered complete. The rules are derived from the
alignment work on `BswModuleDescription` (Table 3.1), `BswModuleEntry`
(Table 4.1), and `ModeDeclarationGroup` / `ModeTransition` (Tables 4.10, 4.12)
against the AUTOSAR PDF specification, and are intended to be applied uniformly
to every class under `src/armodel/models/M2/AUTOSARTemplates/`.

Each rule lists what to check and how to verify it. Throughout this document,
`ClassName` denotes the class under check, with:

- source file: `src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py`
  (or `<package>/<ClassName>/__init__.py` for package-style modules)
- mirrored test file: `tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py`
- spec table: the class's attribute table in the corresponding AUTOSAR PDF
  (markdown sources under `autosar/markdown/`, XSD under
  `autosar-pdf/examples/xsd/`)

---

## Rule 1: Spec Alignment

**Maturity**: accept

The class must reflect the AUTOSAR PDF specification for its attributes.

Check:
- [ ] Every attribute in the class exists in the class's spec table (find the
      table by searching the AUTOSAR PDF markdown for the class name).
- [ ] The PDF spec is the source of truth for multiplicity. When the XSD
      disagrees with the PDF, follow the PDF (example: `bswModuleDocumentation`
      is `0..1` in the PDF but `many` in the XSD — the PDF wins).
- [ ] Deprecated attributes that the PDF has replaced are **not** added
      (example: `outgoingCallback` / `providedEntry` are deprecated and replaced
      by `expectedEntry` / `implementedEntry`).
- [ ] Type deviations are recorded as well, not only missing/extra attributes
      (example: `BswModuleEntry.serviceId` is `PositiveInteger` in the PDF but
      `ARNumerical` in the model because the parser's
      `getChildElementOptionalNumericalValue` produces `ARNumerical`).
      Changing a type requires coordinated parser and writer changes.
- [ ] Field annotation, getter return, setter parameter, parser, and writer must
      all agree on the same type. When the PDF type conflicts with what the
      parser produces (e.g. PDF `PositiveInteger` vs parser
      `getChildElementOptionalNumericalValue` → `ARNumerical`), align the field
      and accessors to the parser's type and record the deviation — a field
      annotated differently from its own accessors is an internal inconsistency,
      not a clean deviation (`ModeDeclarationGroup.onTransitionValue` was typed
      `PositiveInteger` while its getter/setter/parser/writer all used
      `ARNumerical`; the field was aligned and the deviation recorded).
- [ ] Attribute-level completeness: every spec attribute must map to a field
      **plus** an accessor pair. The method parity checklist only tracks
      methods, so a class can be checklist-complete while still missing
      accessors — a field without a getter/setter is a gap
      (`ModeDeclarationGroup.modeManagerErrorBehavior` / `modeUserErrorBehavior`
      had fields but no accessors; pairs were added).
- [ ] Multiplicity maps to the Python representation: `*` → `List[T]` (default
      `[]`), `0..1` → optional single `T` (default `None`). A spec-`*` attribute
      held as a single value is a deviation and must be fixed
      (`modeTransition` was a single field; fixed to
      `modeTransitions: List[ModeTransition]`).
- [ ] Choose `createXXX` vs `setXXX` from the aggregated child's spec `Base`:
      if the child type is an `Identifiable` (its spec `Base` lists
      `Identifiable`, i.e. it has a short name), expose a
      `createXXX(short_name)` factory. If the child is a plain non-Identifiable
      object (e.g. `ModeErrorBehavior`, spec `Base` is only `ARObject`), expose
      a plain `setXXX` setter — do not invent a factory for a child that has no
      short name (`ModeTransition` is `Identifiable` per Table 4.12, so
      `createModeTransition(short_name)` is used).
- [ ] Intentional deviations are recorded in `docs/method_deviation_by_class.md`
      with the reason (e.g. "PDF-only", "deprecated, not implemented").

Verification: cross-check each attribute (name, multiplicity, **type**) against
the PDF table and the corresponding XSD in `autosar-pdf/examples/xsd/`. Confirm
any deviation against the parser/writer code before recording it.

---

## Rule 2: Method Parity Checklist

**Maturity**: accept

A comment block at the top of the class lists every method with three columns:
`impl`, `docstring`, `test`. Each column must be marked `[x]`.

```python
# ClassName method parity checklist:
# [x] __init__                     [x] impl  [x] docstring  [x] test
# [x] getFoos                      [x] impl  [x] docstring  [x] test
# [x] setFoos                      [x] impl  [x] docstring  [x] test
# [x] createFoo                    [x] impl  [x] docstring  [x] test
```

Check:
- [ ] The checklist covers every method defined on the class, 1:1 (no missing,
      no extra).
- [ ] Every row is fully `[x]` — no stale `[ ]` entries.

Verification: extract the checklist names and the class method names and compare
them set-wise (see the script in Rule 7). **Additionally**, a row marked `[x] test`
must correspond to a real test: verify each method name appears in the mirrored
test file. A stale `[ ] test` was found on `BswModuleEntry` for 19 methods that
already had tests — the set-based class check alone does not catch this.

---

## Rule 3: Type Hints

**Maturity**: accept

All function parameters and return values must have type hints (Python
3.8-compatible syntax — use `typing.List` / `typing.Optional`, never `X | None`
or `list[...]` unless `from __future__ import annotations` is present).

| Method kind  | Signature                                                    |
|--------------|--------------------------------------------------------------|
| list getter  | `def getFoos(self) -> List[Foo]:`                            |
| single getter| `def getFoo(self) -> Foo:` or `def getFoo(self) -> Optional[Foo]:` |
| setter       | `def setFoo(self, value: Foo) -> "ClassName":`               |
| add          | `def addFoo(self, value: Foo) -> "ClassName":`               |
| create       | `def createFoo(self, short_name: str) -> Foo:`               |

Check:
- [ ] Getters for collections return `List[T]`.
- [ ] Getters that may return `None` return `Optional[T]` (applies to all
      `0..1` / `0..*` optional attributes).
- [ ] Setters/adds declare the `value` parameter and return `"ClassName"`
      (string self-reference).
- [ ] All factories accept `short_name: str` and return the concrete type.
- [ ] `Optional` / `List` are imported from `typing`.
- [ ] `__init__` attribute fields are annotated too (`self.foo: Type = None`),
      matching the getter/setter type.

Example:
```python
def getBswModuleDocumentation(self) -> Optional[SwComponentDocumentation]:
    return self.bswModuleDocumentation

def setModuleId(self, value: PositiveInteger) -> "BswModuleDescription":
    if value is not None:
        self.moduleId = value
    return self
```

---

## Rule 4: Getter / Setter Behavior

**Maturity**: accept

- [ ] Setters return `self` for method chaining.
- [ ] Setters and adds are **no-ops when the value is `None`** — they must not
      overwrite the existing value and must not append `None`. This is
      parser-safe: the parser helpers (`getChildElementOptional*` in
      `abstract_arxml_parser.py`) return `None` for missing XML elements, so a
      `None` value simply leaves the default in place.
- [ ] Validation setters (e.g. `setExecutionContext`, `setSwServiceImplPolicy`)
      follow the same pattern: validation runs only for non-`None` values, and
      `None` is a no-op.
- [ ] Getters return the underlying field directly (no copies, no exceptions
      when unset — they return `None` / `[]`).
- [ ] `create*` factories return the existing element when a short name already
      exists (no duplicate creation), and append the new element to the
      corresponding list otherwise.
- [ ] `create*` factories are only used for children that are `Identifiable`
      per their spec `Base`; non-Identifiable children use `setXXX` instead
      (see Rule 1).

Note: this rule is not uniformly applied across the codebase yet. When a class
under check violates it (e.g. `BswModuleEntry` setters previously overwrote the
field with `None`), align the class to the no-op behavior as part of the check.

Example:
```python
def setExpectedEntryRefs(self, value: List[RefType]) -> "BswModuleDescription":
    if value is not None:
        self.expectedEntryRefs = value
    return self

def addImplementedEntryRef(self, value: RefType) -> "BswModuleDescription":
    if value is not None:
        self.implementedEntryRefs.append(value)
    return self
```

---

## Rule 5: Comments from the Spec

**Maturity**: accept

Inline comments and docstrings must reflect the PDF spec wording, not loose
paraphrase.

- [ ] Each attribute in `__init__` has an inline `#` comment based on the PDF
      table note for that attribute.
- [ ] The class docstring reflects the PDF class note (the element's purpose).
- [ ] Getter/setter docstrings summarize the PDF note (e.g. mention
      "Replacement of outgoingCallback / requiredEntry", "can be called from
      another partition or core", "connected ... via the configuration of the
      BSW Scheduler").

Example:
```python
# Indicates an entry which is required by this module.
# Replacement of outgoingCallback / requiredEntry.
self.expectedEntryRefs: List[RefType] = []
```

---

## Rule 6: Formatting

**Maturity**: accept

- [ ] A blank line separates each attribute block (comment + assignment) in
      `__init__`.
- [ ] Lines are at most 79 characters (docstrings 72).
- [ ] No trailing whitespace on blank lines (`W293`) or after code (`W291`),
      and at most one blank line between definitions (`E303`).
      (`W291`/`W293`/`E303` are not part of the enforced CI set
      `E9/F63/F7/F82` plus line length, so violations are warnings only and are
      tracked as a separate cleanup, but new or edited code must not introduce
      them.)
- [ ] No comments are added unless they carry spec information (per AGENTS.md,
      comments are only written when asked).

---

## Rule 7: Tests

**Maturity**: accept

Every method on the class must have test coverage in the mirrored test file
(`tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py`).

- [ ] `test_initialization` asserts all attributes have correct default values
      (`None` / `[]`).
- [ ] Getter/setter pairs share a combined test (`test_get_set_*`) that checks:
      setter returns `self`, value round-trips, and setting `None` is a no-op.
      (On `BswModuleEntry` these `None` no-op assertions were missing and were
      added for every get/set pair.)
- [ ] `add*` methods test appending and the `None` no-op.
- [ ] Every `create*` factory has a test asserting the short name and that the
      element is appended to the corresponding list.
- [ ] Plain getters have a default-value test.

Verification (run in the repo root; replace the paths for the class under
check):

```bash
python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py -q
PATH=".venv/Scripts:$PATH" flake8 --exclude=.venv,build --select=E9,F63,F7,F82 \
  src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py
```

Set-based checklist vs. methods check (also confirms every method name is
referenced by the test file; adapt the two paths and `CLASS_NAME` for the class
under check):

```python
import re
import ast

CLASS_NAME = "ClassName"
SRC = "src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py"
TEST_SRC = "tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py"
src = open(SRC).read()
test_src = open(TEST_SRC).read()
tree = ast.parse(src)
cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == CLASS_NAME)
lines = src.splitlines()
checklist = set()
for i in range(cls.lineno - 1, cls.end_lineno):
    checklist.update(re.findall(r"# \[.\] (\S+)", lines[i]))
methods = {n.name for n in cls.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
assert checklist == methods, f"checklist mismatch: {checklist ^ methods}"
untested = [m for m in methods if m != "__init__" and m not in test_src]
assert not untested, f"methods without test coverage: {untested}"
```

---

## Rule 8: Package Location

**Maturity**: accept

The class must be defined in the module that matches the `Package` row of its
spec table.

Check:
- [ ] The spec table's `Package` row (e.g. `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`)
      maps 1:1 to the module under `src/armodel/models/`: strip the leading `M2::`
      and replace `::` with `/`. The last segment names the module file
      (`...::ModeDeclaration` → `ModeDeclaration.py`).
- [ ] A package-style module (a class that owns a whole spec sub-package) lives in
      `<package>/__init__.py` (`BswOverview` → `BswModuleTemplate/BswOverview/__init__.py`).
- [ ] A spec package may split its classes across sibling files as long as they
      stay under the matching directory (`ModeTransition` and `ModeErrorBehavior`
      share spec package `...::CommonStructure::ModeDeclaration` but live in
      `ModeDeclarationExtra.py` next to `ModeDeclaration.py`).
- [ ] Classes are **not** placed under a spec package different from their own.

Verification: read the `Package` row from the class's spec table and compare it
with the module path under `src/armodel/models/`.

Examples:

| Class | Spec package (PDF) | Python module |
|---|---|---|
| `BswModuleDescription` | `M2::AUTOSARTemplates::BswModuleTemplate::BswOverview` | `BswModuleTemplate/BswOverview/__init__.py` |
| `BswModuleEntry` | `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces` | `BswModuleTemplate/BswInterfaces.py` |
| `ModeDeclarationGroup` | `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration` | `CommonStructure/ModeDeclaration.py` |
| `ModeTransition` | `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration` | `CommonStructure/ModeDeclarationExtra.py` |

---

## How to Use This Document

1. Pick a class (`ClassName`) and locate its source, mirrored test file, and
   PDF spec table.
2. Work through Rules 1-8, ticking each check box. Fix the class, its checklist,
   comments, type hints, or tests as needed.
3. If a rule does not fit the class cleanly, or you encounter something the
   rules do not cover, **record the feedback** (what, where, why) and update
   this document so the rules stay accurate for future classes.
4. Run the Rule 7 verification commands and the set-based script before
   declaring the class complete.

## Reference

- Reference implementations (all satisfy every rule):
  - `BswModuleDescription`
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/__init__.py`)
  - `BswModuleEntry`
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`)
  - `ModeDeclarationGroup`
    (`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`)
  - `ModeTransition`
    (`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclarationExtra.py`)
- Spec sources: `autosar/markdown/*.md` (PDF-derived class tables)
- XSD ground truth: `autosar-pdf/examples/xsd/AUTOSAR_00052.xsd`
- Deviation tracker: `docs/method_deviation_by_class.md`
- General coding standards: `docs/development/coding_rules.md`
