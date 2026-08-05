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
- [ ] The class is the right kind of element: when the spec table header is
      `Class` and its `Attribute` column has rows, the Python class must be a
      model class with fields/accessors — **not** an enum. Enums correspond to
      spec tables headed `Enumeration` with `Literal` rows only.
      (`BswExclusiveAreaPolicy` was modeled as `AREnum` with
      `NONE/INTERNAL/EXTERNAL` members that appear nowhere in Table 5.17; the
      spec defines it as a class with `apiPrinciple` and `exclusiveArea`
      attributes.)
- [ ] Base-class alignment: the spec table's `Base` column determines the
      Python base class and therefore the constructor signature. When `Base`
      lists `Referrable` (or `Identifiable`, which extends `Referrable`) the
      Python class must inherit from `Referrable`/`Identifiable` and its
      constructor must take `(self, parent, short_name)` — a class whose spec
      `Base` is `ARObject, Referrable` but which inherits only from `ARObject`
      and defines `__init__(self)` is misaligned. (`ExclusiveAreaNestingOrder`
      inherited from `ARObject` with `__init__(self)` while Table 5.19 lists
      `Base = ARObject, Referrable`; it was realigned to inherit `Referrable`
      and take `(self, parent, short_name)`.) The `Base` column may also name a
      concrete abstract base the class must inherit rather than plain `ARObject` —
      e.g. `AtpInstanceRef` (`ModeInBswModuleDescriptionInstanceRef` has
      `Base = ARObject, AtpInstanceRef` and inherits `AtpInstanceRef`). The
      `Base` column is also what drives the `createXXX` vs `setXXX` choice in
      the bullet below.
- [ ] The `Base` column usually lists the *entire* inheritance chain, ending in
      the model classes the class belongs to (e.g. Table 5.33 lists
      `ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable,
      MultilanguageReferrable, Referrable`). The class must inherit the
      **most-derived** model class in that chain as its direct parent — never a
      more general ancestor. `BswModeManagerErrorEvent` was defined as
      `BswEvent` although its `Base` chain ends at `BswScheduleEvent`, the same
      direct parent as the siblings `BswModeSwitchEvent` / `BswModeSwitchedAckEvent`;
      it was realigned to `BswScheduleEvent`. When the `Base` column lists a
      sibling/mid-hierarchy model class (an abstract base shared by several
      concrete classes), choose it over the ancestor it extends. The
      auto-generated `reports/deviation_class_hierarchy_mismatches.md` flags
      this kind of parent mismatch for review.
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
- [ ] No fabricated attributes: the reverse of attribute-level completeness —
      every field in the class must trace back to a spec attribute. A class can
      be checklist-complete (every method `[x] impl/docstring/test`) yet carry a
      field with a full accessor pair that appears **nowhere** in the spec table.
      Such a field is fabricated and must be **removed**, not merely recorded as
      a deviation — a deviation records an intentional spec/code gap, not
      invented API. The method parity checklist (Rule 2) cannot detect this on
      its own because it only verifies that listed methods exist; it does not
      verify that each field maps to the spec. (`ExclusiveAreaNestingOrder.order`
      (`int`, with `getOrder`/`setOrder`) had no counterpart in Table 5.19 and
      was deleted during realignment.) Cross-check the `__init__` field list
      against the spec `Attribute` rows and account for every field.
- [ ] This bullet targets **stored** fields (backing storage + accessor pair).
      A **read-only derived convenience property** — a `@property` computed from
      a spec attribute, with no backing field of its own and no setter (e.g.
      `BswTimingEvent.periodMs`, which derives milliseconds from the spec
      `period` `TimeValue`) — is not fabricated API and is **kept**, provided it
      (a) gets a method-parity checklist row like any other member, (b) is
      tested, and (c) is recorded in the deviation tracker as an "added
      convenience property" (mirrors the `atpDerived` handling: derived, no XML
      element, no parser/writer coverage). The precedent is
      `ExecutableEntity.minimumStartIntervalMs`. Do **not** delete a convenience
      property that real consumers (CLI, parser tests) rely on just because it
      is absent from the spec table — removing it is a breaking change;
      recording it is the aligned action. (`BswTimingEvent.periodMs` was
      half-aligned — `[ ] test`, annotated `-> int` although it returns `None` —
      and was brought to full compliance (test added, `Optional[int]`) and
      recorded rather than removed.)
- [ ] Multiplicity maps to the Python representation: `*` → `List[T]` (default
      `[]`), `0..1` → optional single `T` (default `None`). A spec-`*` attribute
      held as a single value is a deviation and must be fixed
      (`modeTransition` was a single field; fixed to
       `modeTransitions: List[ModeTransition]`). The reverse is equally a
      deviation: a spec-`0..1` attribute held as a `List`
      (`BswModuleEntity.schedulerNamePrefixRef` was `List[RefType] = None`
      while the spec/XSD say a single `0..1` ref). A **bounded ordered**
      multiplicity such as `0..2` (upper bound > 1 but not `*`) still maps to
      `List[T]` (default `[]`) with the usual `getXxxs`/`addXxx` accessors —
      the upper bound is not enforced in the model
      (`BswModeSwitchEvent.mode` is `ordered, 0..2` → `modeIRefs:
      List[ModeInBswModuleDescriptionInstanceRef]`; order is preserved by
      insertion order in `addModeIRef`). Getter/setter docstrings
      must match the chosen representation — "list of ..." wording on a single
      ref (or vice versa) is a symptom of a multiplicity mismatch
      (`getSchedulerNamePrefixRef` said "list of scheduler name prefix
      references" for a single ref).
- [ ] Ref/TRef/IRef suffix naming: when the spec table's Kind column is `ref`,
      `tref`, or `iref`, include the corresponding suffix in the Python field
      and method names. The spec table Attribute column determines the base
      name, Kind determines the suffix: `ref` → `Ref`/`Refs`, `tref` → `TRef`,
      `iref` → `IRef`/`IRefs`. Example: Attribute `enteredMode`, Kind `ref` →
      Python field `enteredModeRef: RefType`, getter `getEnteredModeRef()`.
      Attribute `disabledInMode`, Kind `iref` (Table 5.22) → Python field
      `disabledInModeIRefs: List[ModeInBswModuleDescriptionInstanceRef]`,
      getter `getDisabledInModeIRefs()`. The suffix makes reference semantics
      explicit in Python names and aligns with parser conventions. An `iref`
      Kind means the attribute is an instance reference — its element type is a
      `<name>InstanceRef` class (e.g. `ModeInBswModuleDescriptionInstanceRef`),
      and the list type annotation is that class, **not** `RefType`.
      Within the `<name>InstanceRef` class itself, its *inner* attributes are
      ordinary Kind `ref` rows (the sub-elements of the instance ref, e.g.
      `contextModeDeclarationGroup`, `targetMode`) and therefore map to
      `Optional[RefType]` with the plain `Ref` suffix — do **not** annotate them
      as the `<name>InstanceRef` class or hold object references
      (`ModeInBswModuleDescriptionInstanceRef` originally held
      `bases`/`targetModes` as object references and `contextModes` as a
      non-optional `RefType`; all three were aligned to
       `baseRef`/`contextModeDeclarationGroupRef`/`targetModeRef`:
       `Optional[RefType]`).
- [ ] The **base name** of an attribute field comes **verbatim** from the spec
      table's `Attribute` column; the Kind suffix is appended to that exact
      base, never to a paraphrased or semantically-equivalent rename. A
      plausible-sounding name is still a Rule 1 violation when it does not
      match the spec Attribute (the old `BswAsynchronousServerCallReturnsEvent`
      modeled spec `eventSource` (Kind `ref`) as `serverCallPointRef` — a
      semantic paraphrase — while the spec-mandated name is `eventSourceRef`).
      The set-based checklist (Rule 2) cannot catch a wrong-but-consistent
      name: field, getter, setter, and checklist all agreed on
      `serverCallPointRef`, so the checklist was internally consistent while
      the API was misnamed relative to the spec. Only the field-to-spec
      cross-check against the `Attribute` column catches this, so it applies to
      **every** field, not just to missing/extra ones.
- [ ] Choose `createXXX` vs `setXXX` from the aggregated child's spec `Base`:
      if the child type has a short name (its spec `Base` lists `Referrable`
      or `Identifiable` — `Identifiable` extends `Referrable`, so the
      meaningful test is `Referrable`), expose a `createXXX(short_name)`
      factory. If the child is a plain non-Identifiable object with no short
      name (e.g. `ModeErrorBehavior`, spec `Base` is only `ARObject`), expose
      a plain `setXXX` setter — do not invent a factory for a child that has no
      short name. The earlier wording "if the child type is an `Identifiable`"
      was too narrow: `BswModuleCallPoint` has spec `Base`
      `ARObject, Referrable` (not `Identifiable`) but still carries a short
      name, and `BswModuleEntity` correctly uses
      `createBswAsynchronousServerCallPoint(short_name)` /
      `createBswSynchronousServerCallPoint(short_name)` factories for it
      (the parser's `readBswModuleEntityCallPoints` depends on them).
      `ModeTransition` is `Identifiable` per Table 4.12, so
      `createModeTransition(short_name)` is used.
- [ ] Every implemented attribute must be covered by **both** the parser and
      the writer. A spec attribute with a field and accessors but no parser or
      writer handling is silently dropped on round-trip
      (`BswModuleEntity.schedulerNamePrefixRef` had accessors but no
      `SCHEDULER-NAME-PREFIX-REF` read/write; parser and writer support were
      added). This extends to **polymorphic dispatch**: a class that is a
      concrete subtype of an abstract base (e.g. an event or entity) may have a
      dedicated `readXxx`/`writeXxx` method yet still be silently dropped if the
      *dispatch* function (`readBswInternalBehaviorEvents` /
      `writeBswInternalBehaviorEvents`-style `if isinstance(...)` / tag-name
      chains) has no branch for it — the `else: self.notImplemented(...)` / `self.
      notImplemented(...)` fallback only logs. Adding a subtype therefore
      requires updating the dispatch function as well as writing the dedicated
      read/write method (`BswModeSwitchEvent` was unreadable-and-unwritable
      because `writeBswInternalBehaviorEvents` had no `isinstance` branch for it;
      the branch was added alongside `writeBswModeSwitchEvent`). Concretely,
      adding a concrete subtype touches **five** places: (a) the subtype class
      itself, (b) the aggregator that owns the instances — it must expose a
      `createXxx(short_name)` factory and a `getXxxs()` getter, and both rows
      must be added to the aggregator's method-parity checklist
      (`BswInternalBehavior.createBswModeManagerErrorEvent` /
      `getBswModeManagerErrorEvents` were added when `BswModeManagerErrorEvent`
      was added; without the factory the parser's tag-name branch has nothing
      to instantiate), (c) the parser dispatch, (d) the writer dispatch, and
      (e) the parser **and** writer dispatch *tests* — the
      `test_readBswInternalBehaviorEvents_dispatches_all_types` /
      `test_dispatches_all_event_types`-style tests that assert every subtype is
      routed must gain the new subtype, otherwise a branch exists that no test
      exercises and a later refactor can silently break the dispatch without
      failing CI (`BswModeSwitchedAckEvent` was added to both dispatch tests
      when its branches were added).
      **Exception:** an
      attribute marked `Stereotypes: atpDerived` is a
      *derived* attribute — it is computed from its context and has **no** XML
      element, so it has no parser/writer element and is exempt from this
      requirement. It still maps to a field + accessor pair (Rule 1's
      attribute-level completeness) and is recorded as `atpDerived` in the
      deviation tracker (`ModeInBswModuleDescriptionInstanceRef.baseRef` is
      `atpDerived`, while `contextModeDeclarationGroupRef`/`targetModeRef` are
      normal `ref` attributes with parser/writer coverage).
- [ ] When a field's type lives in a **different spec package** that imports
      back into the current module, import the type under `TYPE_CHECKING` and
      annotate fields/getters with a string forward reference (`"ClassName"`);
      the parser and writer may import it directly because they sit below the
      model classes in the import graph and cannot create a cycle
      (`BswEvent.disabledInModeIRefs` types
      `ModeInBswModuleDescriptionInstanceRef` from
      `BswModuleTemplate/BswOverview/InstanceRefs/`, which is aggregated by
      `BswModuleDescription` — a package that itself imports `BswBehavior`, so
      `BswBehavior.py` must use `TYPE_CHECKING` to avoid the circular import).
- [ ] Intentional deviations are recorded in `docs/method_deviation_by_class.md`
      with the reason (e.g. "PDF-only", "deprecated, not implemented").

Verification: cross-check each attribute (name, multiplicity, **type**) against
the PDF table and the corresponding XSD in `autosar-pdf/examples/xsd/`. Confirm
any deviation against the parser/writer code before recording it.

---

## Rule 2: Method Parity Checklist

**Maturity**: accept

A comment block at the top of the class lists every method with three columns:
`impl`, `docstring`, `test`. Each column must be marked `[x]`. The first line
after the checklist title must cite the AUTOSAR PDF spec table the class is
aligned against: `# Spec: <PDF file>.pdf, Table <X.Y>, p.<page>` (page from
the PDF itself, e.g. p.72 = Table 5.4 in the 381-page R23-11 PDF). This makes
Rule 1 traceable — every later check refers back to the spec source named in
the class comment.

```python
# ClassName method parity checklist:
# Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.4, p.72
# [x] __init__                     [x] impl  [x] docstring  [x] test
# [x] getFoos                      [x] impl  [x] docstring  [x] test
# [x] setFoos                      [x] impl  [x] docstring  [x] test
# [x] createFoo                    [x] impl  [x] docstring  [x] test
```

Check:
- [ ] The checklist covers every method defined on the class, 1:1 (no missing,
      no extra). A `@property` member counts as a method here: it is an
      `ast.FunctionDef` in the class body, so it needs a checklist row (`[x]
      impl/docstring/test`) and a test just like a normal method
      (`BswTimingEvent.periodMs`).
- [ ] Every row is fully `[x]` — no stale `[ ]` entries.
- [ ] The `# Spec:` line names the correct PDF, table number, and page for the
      class (cross-check against the actual PDF; e.g. `ExecutableEntity` is
      `Table 5.3, p.70`, `BswModuleEntity` is `Table 5.4, p.72`,
      `ReentrancyLevelEnum` is `Table 5.5, p.73`).

Verification: extract the checklist names and the class method names and compare
them set-wise (see the script in Rule 7). **Additionally**, a row marked `[x] test`
must correspond to a real test: verify each method name appears in the mirrored
test file. A stale `[ ] test` was found on `BswModuleEntry` for 19 methods that
already had tests — the set-based class check alone does not catch this.

The checklist is method-only: it verifies that listed methods exist and are
tested, but it cannot detect a *fabricated attribute* — a field with accessors
that appears nowhere in the spec (see the "No fabricated attributes" check in
Rule 1). A 100 %-checked-off class can still carry invented API, so Rule 1's
field-to-spec cross-check is the gate, not the checklist.

---

## Rule 3: Type Hints

**Maturity**: accept

All function parameters and return values must have type hints (Python
3.8-compatible syntax — use `typing.List` / `typing.Optional`, never `X | None`
or `list[...]` unless `from __future__ import annotations` is present).

**IMPORTANT**: The project requires **Python >= 3.8** (see `pyproject.toml`), but
the `|` union syntax was introduced in Python 3.10. Always use `Optional[T]` from
the `typing` module, not `T | None`. AGENTS.md line 43 incorrectly recommends
3.10+ syntax — **ignore that and use `Optional` for compatibility**.

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
- [ ] A field that defaults to `None` and maps to a spec `0..1` attribute must
      be annotated `Optional[T]` — never a non-optional `T` initialized to
      `None`. A bare `self.xxxRef: RefType = None` contradicts its own getter's
      `Optional[RefType]` return and is an internal inconsistency
      (`BswAsynchronousServerCallReturnsEvent.serverCallPointRef` was declared
      `RefType = None`). Optionality is expressed in the annotation, not just
      by the `None` default.
- [ ] **Use `Optional[T]` for Python 3.8+ compatibility, never `T | None`**.

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
      table note for that attribute. The comment should include the key semantic
      information from the spec (e.g., "Indicates an entry which is required",
      "The mode that is entered by this transition", "AUTOSAR identifier of
      the target module").
- [ ] Constraint rows are spec material for the comment just like the attribute
      note: when the PDF's `constr_*` rows impose a constraint on the attribute,
      include the constraint wording in the inline comment and cite its id
      (`BswTimingEvent.period` carries the `constr_4043` "shall be greater than
      0" requirement; `BswModeManagerErrorEvent.modeGroupRef` carries the
      `constr_10286` existence requirement). Class-level `constr_*` rows belong
      in the class docstring alongside the note (`BswModeManagerErrorEvent` is
      subject to `constr_4081`, which appears in its docstring).
- [ ] The class docstring reflects the PDF class note (the element's purpose).
- [ ] Getter/setter docstrings summarize the PDF note and semantic meaning,
      not just "Gets/sets the value". They should mention what the attribute
      represents in AUTOSAR (e.g. mention "Replacement of outgoingCallback / 
      requiredEntry", "can be called from another partition or core", "connected
      ... via the configuration of the BSW Scheduler", or "error mode in case
      of error"). Docstrings connect spec semantics to code intent.

Example from spec PDF:
```python
# Indicates an entry which is required by this module.
# Replacement of outgoingCallback / requiredEntry.
self.expectedEntryRefs: List[RefType] = []
```

Example from BswModuleDependency (spec note: "AUTOSAR identifier of the target
module of which the dependencies are defined. This information is optional,
because the target module may also be identified by targetModuleRef"):
```python
# AUTOSAR identifier of the target module; optional as target may be
# identified by targetModuleRef instead.
self.targetModuleId: Optional[PositiveInteger] = None
```

---

## Rule 6: Formatting

**Maturity**: accept

- [ ] A blank line separates each attribute block (comment + assignment) in
      `__init__`.
- [ ] Code is formatted with Black at `line-length = 200` (per `pyproject.toml`,
      enforced by `npm run black-check`). The older 79-character limit is
      obsolete and must not be applied by hand.
- [ ] No trailing whitespace on blank lines (`W293`) or after code (`W291`),
      and at most one blank line between definitions (`E303`).
      (CI flake8 enforces only the syntax set `E9/F63/F7/F82`; line length (127)
      and style codes like `W291`/`W293`/`E303` run exit-zero, so violations are
      warnings only and are tracked as a separate cleanup, but new or edited code
      must not introduce them.)
- [ ] No comments are added unless they carry spec information (per AGENTS.md,
      comments are only written when asked).

---

## Rule 7: Tests

**Maturity**: accept

Every method on the class must have test coverage in the mirrored test file
(`tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py`).

- [ ] `test_initialization` asserts all attributes have correct default values
      (`None` / `[]`).
- [ ] Abstract classes cannot be instantiated directly, so test their
      `__init__` defaults through a concrete subclass
      (`ExecutableEntity`, `BswModuleEntity`). The reference pattern is
      `test_concrete_subclass_initialization`: instantiate a known concrete
      subclass (or a local subclass defined in the test) and assert every
      default set by the abstract `__init__`. Include the literal `__init__`
      in the test (docstring or a local subclass `def __init__`) so the
      checklist's `[x] test` for `__init__` stays verifiable by the
      set-based check.
- [ ] Getter/setter pairs share a combined test (`test_get_set_*`) that checks:
      (1) setter returns `self` for method chaining, (2) value round-trips
      (getter returns the set value), (3) setting `None` is a no-op (existing
      value is preserved). The None no-op test is critical: verify that after
      `setter(value)` followed by `setter(None)`, the getter still returns the
      original value. (On `BswModuleEntry` these `None` no-op assertions were
      missing and were added for every get/set pair; this pattern applies to
      all classes.)
- [ ] `add*` methods test appending, the return value (`self`), and the `None`
      no-op (setting None does not append).
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
spec table. There is exactly one module file per spec package, and all classes
in that spec package must be defined in that single module.

Check:
- [ ] The spec table's `Package` row (e.g. `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`)
      maps 1:1 to a module under `src/armodel/models/`: strip the leading `M2::`
      and replace `::` with `/`. The last segment names the module file or
      package directory (`...::ModeDeclaration` → `ModeDeclaration.py` or
      `ModeDeclaration/__init__.py`).
- [ ] If the module is a file (`ModeDeclaration.py`), all classes in that spec
      package (e.g., `ModeDeclaration`, `ModeTransition`, `ModeErrorBehavior`)
      must be defined in that single file.
- [ ] Package **name match** (the last segment is the package, not the class):
      the `Package` row names the spec package and the class is its *direct
      member* — the class name comes from the table's `Class` header, **not from
      the package path**. Do **not** place the class in a sub-module/sub-package
      whose tail is the class name, because that makes the class name look like a
      package and mismatches the `Package` row. Example: `ModeInBswModuleDescriptionInstanceRef`'s
      `Package` row is
      `M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::InstanceRefs`, so the
      class is a member of `InstanceRefs` — putting it in
      `InstanceRefs/ModeInBswModuleDescriptionInstanceRef.py` is a package-name
      mismatch, because that path implies package
      `...::BswOverview::InstanceRefs::ModeInBswModuleDescriptionInstanceRef`.
      The class must be defined **directly** in `InstanceRefs/__init__.py`.
- [ ] If the module is a directory/package (`BswOverview/__init__.py`), the spec
      package's classes are defined in that `__init__.py` file (or imported and
      re-exported from `__init__.py` if split into submodules). Prefer defining
      classes **directly** in `__init__.py`; only split into per-class submodules
      when the spec package grows large enough that splitting clearly aids
      maintainability — a sparse package (one or a few classes) must not add an
      extra `__init__.py` re-export hop for each class — and a sub-module name
      must never reuse the class name (see package-name-match above).
- [ ] Do **not** create sibling files like `ModeDeclarationExtra.py` to house
      classes that belong in `ModeDeclaration.py` — consolidate all classes
      for a spec package in one place.
- [ ] The module path must not be shadowed by a same-named sibling directory:
      when the spec `Package` maps to `X.py` but a directory `X/` also exists
      (without `__init__.py`), the module file wins in the import system and
      classes placed only in `X/*.py` are unreachable dead code. Define the
      classes in `X.py`, or make `X/` a real package with an `__init__.py`.
      (`BswExclusiveAreaPolicy` lived in `BswBehavior/BswExclusiveAreaPolicy.py`,
      shadowed by the `BswBehavior.py` module — importing it raised
      `ModuleNotFoundError`; it was migrated into `BswBehavior.py`.) This
      shadowing can hide a **whole family** of classes at once: `BswBehavior/`
      held 8 classes (including `BswModeManagerErrorEvent`) that were all
      unreachable, and each must be migrated out one at a time. When migrating a
      class out of a shadowed directory, update
      `tests/test_armodel/test_model_imports.py`: remove the class name from
      `KNOWN_NAME_COLLISION_CLASSES` **and** adjust the count in that module's
      docstring, so the class becomes importable from `armodel` and stays
      covered by the import test. A class listed in `KNOWN_NAME_COLLISION_CLASSES`
      is a live signal that it may live in a shadowed directory and deserves a
      Rule 8 review. A shadowed class is **dead code** even though report scans
      still find it (e.g. `reports/method_parity_review.md` analyzed the old
      shadowed `BswAsynchronousServerCallReturnsEvent`), so a clean rule review
      of the class is not enough — the class must be relocated to the real
      module. After relocating, audit **every** reference to the old shadowed
      path, not just live imports: stale `# from ...BswBehavior.<ClassName>...`
      comments in `src/armodel/models/__init__.py`, the source path in
      `docs/development/method_deviation_by_class.md`, and any docs/reports that
      name the old path.
- [ ] Classes are **not** placed under a spec package different from their own.
- [ ] Import statements **match** the package location: every consumer imports the
      class from the package that defines it — `from ...<Args>.<Package> import
      <ClassName>` when the class lives in a package's `__init__.py`, and never
      from a class-named sub-module (`from ...<Package>.<ClassName> import ...`),
      which would imply a non-existent sub-package. After relocating a class,
      audit every import site (parser, writer, `__init__.py` re-exports, tests)
      so no stale class-named sub-module import remains.

Verification: read the `Package` row from the class's spec table and compare it
with the module path under `src/armodel/models/`. Verify all classes for that
spec package are in the same module file.

Examples:

| Class | Spec package (PDF) | Python module |
|---|---|---|
| `BswModuleDescription` | `M2::AUTOSARTemplates::BswModuleTemplate::BswOverview` | `BswModuleTemplate/BswOverview/__init__.py` |
| `BswModuleEntry` | `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces` | `BswModuleTemplate/BswInterfaces.py` |
| `ModeDeclarationGroup` | `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration` | `CommonStructure/ModeDeclaration.py` |
| `ModeDeclaration` | `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration` | `CommonStructure/ModeDeclaration.py` |
| `ModeTransition` | `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration` | `CommonStructure/ModeDeclaration.py` |
| `ModeErrorBehavior` | `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration` | `CommonStructure/ModeDeclaration.py` |
| `ModeInBswModuleDescriptionInstanceRef` | `M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::InstanceRefs` | `BswModuleTemplate/BswOverview/InstanceRefs/__init__.py` |

---

## Rule 9: Attribute Spacing in Classes

**Maturity**: accept

Each member (attribute or method) in a class must be separated by exactly one
blank line. This improves readability and clearly delineates separate logical
units within the class.

Check:
- [ ] Every attribute in `__init__` has a blank line before and after its
      comment + assignment block.
- [ ] Every method is preceded by a blank line (except the first method
      immediately after `__init__`).
- [ ] Every method is followed by a blank line before the next method.
- [ ] No consecutive blank lines (only single blanks between members).

Example:
```python
class Example(ARObject):
    def __init__(self):
        super().__init__()
        # First attribute comment
        self.field1: Type1 = None

        # Second attribute comment
        self.field2: Type2 = None

    def getField1(self) -> Optional[Type1]:
        """Gets field1."""
        return self.field1

    def setField1(self, value: Optional[Type1]) -> "Example":
        """Sets field1."""
        if value is not None:
            self.field1 = value
        return self
```

---

## Rule 10: Method Signature Formatting

**Maturity**: accept

Each method definition and all of its parameters must fit on the same logical
line. Black (repo `line-length = 200`, enforced by `npm run black-check`)
collapses a signature onto a single physical line whenever it fits within 200
characters, so do **not** hand-break a signature that fits.

Do NOT split method definitions by placing some parameters on the method line
and others on subsequent lines inside the method body. All parameters and return
type must be part of the method signature, not rearranged or moved to comments.

Check:
- [ ] Method `def` keyword starts the signature.
- [ ] All parameters are declared in the signature (between parentheses).
- [ ] Return type annotation is part of the signature (on the same logical line
      via `->` notation).
- [ ] `npm run black-check` passes for the file — signatures that fit within
      200 characters are on one line, not hand-broken.
- [ ] The method body begins on a new line after the `:`.

Note: a trailing comma after the last parameter is Black's "magic trailing
comma" — it forces the exploded (one parameter per line) form even when the
signature would fit in 200 characters. Only keep a hand-multi-line signature
(and its trailing comma) when it genuinely exceeds 200 characters; otherwise
remove the trailing comma and let Black collapse it.

Example (correct):
```python
def setBswEntryRelationshipType(self, value: Optional[BswEntryRelationshipEnum]) -> "BswEntryRelationship":
    """Sets the type of relationship."""
    if value is not None:
        self.bswEntryRelationshipType = value
    return self
```

Example (incorrect):
```python
# DON'T do this:
def setBswEntryRelationshipType(self, value):
    # Type information moved to comment, not in signature
    # value: Optional[BswEntryRelationshipEnum]
    if value is not None:
        self.bswEntryRelationshipType = value
    return self
```

---

## Rule 11: Enum Types Must Inherit from AREnum

**Maturity**: accept

All enumeration classes in the AUTOSAR model must inherit from `AREnum`, not
from Python's built-in `Enum` or `str` (or other) mixins. This ensures
consistency across the codebase and allows for unified enum handling in the
parser and writer.

Check:
- [ ] Every enum class in the module inherits from `AREnum` (not `Enum`,
      `str` + `Enum`, `IntEnum`, etc.).
- [ ] The import statement includes `AREnum` from
      `armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes`.
- [ ] The enum body contains enum members with string values (e.g.,
      `MEMBER_NAME = "member_value"`).

Example (correct):
```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum

class MyEnum(AREnum):
    """Enumeration for something."""
    # MyEnum method parity checklist:
    # (no methods)

    MEMBER_ONE = "member_one"
    MEMBER_TWO = "member_two"
```

Example (incorrect):
```python
# DON'T do this:
from enum import Enum

class MyEnum(str, Enum):
    """Enumeration for something."""
    MEMBER_ONE = "member_one"
    MEMBER_TWO = "member_two"
```

Rationale: Using `AREnum` provides a standardized enum base class that
integrates with the AUTOSAR model's type system. Custom enum behavior (if
needed) can be added to `AREnum` and automatically inherited by all enums in
the model. See `BswEntryRelationshipEnum` as an example of the correct pattern.

---

## Rule 12: Enum Specification Alignment and Docstring Sync

**Maturity**: accept

Every enumeration class must have its member list and documentation synced with
the AUTOSAR PDF specification. Enums are easy to implement incorrectly because
the spec table may be sparse, incomplete, or the enum may have been created with
placeholder/assumed values that do not match the spec.

Check:
- [ ] Locate the enum's specification table in the AUTOSAR PDF markdown.
      Search by enum class name (e.g., search for `BswEntryRelationshipEnum` or
      the table number if known).
- [ ] Verify the enum members: every literal row in the spec table must have a
      corresponding Python enum member. There must be **no extra members** (not
      in spec) and **no missing members** (in spec but not in code).
- [ ] Enum member naming: convert the spec literal to Python UPPER_CASE naming.
      Example: spec literal `derivedFrom` → Python member `DERIVED_FROM`.
- [ ] Enum member value: the string value must **exactly match** the spec literal
      value. Example: `DERIVED_FROM = "derivedFrom"` (not `"derived_from"` or
      variations).
- [ ] Class docstring: summarize the spec table's "Note" row (the enum's purpose
      and scope).
- [ ] Enum member documentation: each member must have an inline comment that
      cites the spec literal's description (not paraphrased, use the PDF wording).
      Include Tags information (e.g., `atp.EnumerationLiteralIndex=0`) to document
      the spec's ordering.
- [ ] Sync with PDF on every review: when updating an enum, always check the
      PDF spec table first. Do not assume previous implementations are correct.

Example from AUTOSAR Table 4.20 (BswEntryRelationshipEnum):

| Literal       | Description |
|---------------|-------------|
| derivedFrom   | Describes that the BswModuleEntry referenced as "to" needs to have the same signature as the "abstract" BswModuleEntry referenced as "from". Tags: atp.EnumerationLiteralIndex=0 |

**Correct implementation** (matches spec):
```python
class BswEntryRelationshipEnum(AREnum):
    """
    Enumeration for BSW entry relationship types.
    Defines the type of relationship between two BswModuleEntrys.
    """
    # BswEntryRelationshipEnum method parity checklist:
    # (no methods)

    # Describes that the BswModuleEntry referenced as "to" needs to have
    # the same signature as the "abstract" BswModuleEntry referenced as
    # "from". Tags: atp.EnumerationLiteralIndex=0
    DERIVED_FROM = "derivedFrom"
```

**Incorrect implementation** (had members NOT in spec):
```python
class BswEntryRelationshipEnum(AREnum):
    # WRONG: These are not in AUTOSAR Table 4.20
    READS = "reads"          # NOT in PDF spec
    WRITES = "writes"        # NOT in PDF spec
    CALLS = "calls"          # NOT in PDF spec
    TRIGGERS = "triggers"    # NOT in PDF spec
```

Verification: search the AUTOSAR markdown (`autosar/markdown/*.md`) for the enum's
spec table. Compare the literal rows (Literal column) 1:1 with the enum members
defined in Python code. Use `grep` or `rg` to find the table:
```bash
grep -A 10 "^Table.*: <EnumName>" autosar/markdown/AUTOSAR*.md
```

If there is a mismatch (extra members, missing members, wrong values, or missing
docstrings), correct the enum implementation and update all corresponding tests.

---

## How to Use This Document

1. Pick a class (`ClassName`) and locate its source, mirrored test file, and
   PDF spec table.
2. Work through Rules 1-12, ticking each check box. Fix the class, its checklist,
   comments, type hints, tests, spacing, method signatures, enum types, and
   enum specifications as needed.
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
    (`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`)
  - `ModeErrorBehavior`
    (`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`)
  - `ExecutableEntity` — Table 5.3, p.70
    (`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`)
  - `BswModuleEntity` — Table 5.4, p.72
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
  - `ReentrancyLevelEnum` — Table 5.5, p.73
    (`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`)
  - `BswExclusiveAreaPolicy` — Table 5.17, p.83
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
  - `ApiPrincipleEnum` — Table 5.18, p.83
    (`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`)
  - `BswEvent` — Table 5.22, p.87
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
  - `ModeInBswModuleDescriptionInstanceRef` — Table C.37, p.323
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/InstanceRefs/__init__.py`)
  - `BswModeSwitchEvent` — Table 5.31, p.94
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
  - `BswModeManagerErrorEvent` — Table 5.33, p.95
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
  - `BswModeSwitchedAckEvent` — Table 5.32, p.95
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
  - `BswAsynchronousServerCallReturnsEvent` — Table 5.36, p.98
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
  - `BswTimingEvent` — Table 5.25, p.89
    (`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
- Spec sources: `autosar/markdown/*.md` (PDF-derived class tables)
- XSD ground truth: `autosar-pdf/examples/xsd/AUTOSAR_00052.xsd`
- Deviation tracker: `docs/method_deviation_by_class.md`
- General coding standards: `docs/development/coding_rules.md`

## General Patterns from Class Reviews

The following patterns emerge from reviewing classes against the rules. These
apply to all future classes.

### Python Version vs. Type Hint Syntax (CRITICAL)

**ISSUE FOUND**: AGENTS.md line 43 states "Type annotations: Python 3.10+ union
syntax (`str | None` not `Optional[str]`)" but `pyproject.toml` specifies
`requires-python = ">=3.8"`. The union operator `|` was introduced in Python
3.10, so it cannot be used.

**RESOLUTION**: Always use `Optional[T]` from `typing`, never `T | None`, to
maintain Python 3.8 compatibility. This applies to all classes under review,
regardless of what AGENTS.md says.

### Spec Attribute Mapping: Kind Column is Critical

The PDF spec table has separate columns: Attribute, Type, Mult, Kind, Note.
The **Kind column determines naming and type handling**:

- **Kind `ref`**: attribute becomes `<name>Ref: RefType`, with getter
  `get<Name>Ref()` and setter `set<Name>Ref(value: RefType)`.
  Example: spec Attribute `enteredMode`, Kind `ref` → Python `enteredModeRef: RefType`.
- **Kind `tref`**: attribute becomes `<name>TRef: TRefType`, with analogous getters/setters.
  Example: spec Attribute `typeReference`, Kind `tref` → Python `typeReferenceTRef: TRefType`.
- **Kind `attr`**: attribute name as-is, type from the Type column. No special naming suffix.
  Example: spec Attribute `errorPolicy`, Kind `attr` → Python `errorPolicy: str`.

Misaligning the Kind column naming is a Rule 1 violation that breaks parser/writer contracts.

### Consistency Across Accessors and Checklist

Once a field name is chosen (e.g., `defaultModeRef`), all accessors and checklist
entries must use that exact name:
- Field: `defaultModeRef`
- Getter: `getDefaultModeRef()`
- Setter: `setDefaultModeRef()`
- Checklist: `[x] getDefaultModeRef`, `[x] setDefaultModeRef`
- Tests: `test_get_set_default_mode_ref()`, `test_get_set_default_mode_ref_none()`

Automated set-based checklist validation catches checklist ↔ implementation mismatches,
but cannot verify checklist ↔ test correspondence. Manual inspection after
refactoring is essential.

### Docstrings Connect Spec to Intent

Attribute comments and getter/setter docstrings should cite spec semantics, not just
technical description:
- **Attribute comment**: the spec note for that attribute, bridging to Python.
  Example: `# The mode that is entered by this transition.`
- **Getter docstring**: what the attribute represents and its purpose.
  Example: `Gets the mode that is entered by this transition.`
- **Setter docstring**: include the no-op behavior and method chaining return.
  Example: `Sets the entered mode. Only sets if value is not None. Returns self for chaining.`

"Gets/sets the value" is not sufficient. Readers should understand AUTOSAR semantics from docstrings.

### None No-Op is Universal and Critical

Every setter and add method must follow:
```python
def setSomething(self, value: T) -> "ClassName":
    if value is not None:
        self.something = value
    return self
```

This pattern is critical because:
1. **Parser safety**: parser helpers return `None` for missing XML elements.
2. **No overwriting**: setting None must not overwrite an existing value.
3. **Consistency**: all classes apply this pattern uniformly.

Tests must verify this explicitly: after `setter(value)`, then `setter(None)`,
the getter must still return the original value.

## Implementation Notes

**Ref/TRef Suffix Convention (from ModeTransition)**

When a spec attribute has Kind `ref` or `tref`, include the suffix in the Python
field and method names. Example: spec Attribute `enteredMode`, Kind `ref` →
Python field `enteredModeRef: RefType`, getter `getEnteredModeRef()`. This makes
the reference semantics explicit and is consistent across the codebase (e.g.,
`BswModuleEntry`'s `expectedEntryRefs`, `implementedEntryRefs`).

## Feedback from BswAsynchronousServerCallReturnsEvent Review

When reviewing and updating `BswAsynchronousServerCallReturnsEvent` per the above
rules, the following observations emerged. They generalize the rules to any
concrete subtype of an abstract base (event/entity) living in a shadowed or
mislocated module.

### 1. Field Base Name Comes Verbatim from the Spec Attribute Column

**ISSUE**: The old class modeled spec `eventSource` (Kind `ref`) as
`serverCallPointRef` — a semantically plausible paraphrase, not the spec name.
The field, getter, setter, and checklist all agreed, so the set-based checklist
passed while the API was misnamed relative to Table 5.36.

**RESOLUTION**: Take the field base name **verbatim** from the spec `Attribute`
column and append only the Kind suffix: `eventSource` → `eventSourceRef`. Do not
"improve" the name based on the type (`serverCallPoint` was the referenced
class's role, not the attribute's name). Rule 1's verbatim-base-name bullet now
captures this; the checklist cannot, because it only checks internal
consistency.

### 2. Dead Code in a Shadowed Directory is Still Reviewed

**ISSUE**: The class lived in `BswBehavior/BswAsynchronousServerCallReturnsEvent.py`,
a non-package directory shadowed by the `BswBehavior.py` module. The class was
unreachable dead code, yet report scans (e.g. `reports/method_parity_review.md`,
`reports/deviation_package.md`, `reports/deviation_class_hierarchy_mismatches.md`)
still analyzed it — so the class could "look aligned" while never being loadable.

**RESOLUTION**: A shadowed class is a Rule 8 problem first. Relocate it into the
real module (`BswBehavior.py`) before (or while) applying Rules 1-7. Migrating it
touched five places: the class, the `BswInternalBehavior` aggregator
(`createBswAsynchronousServerCallReturnsEvent` / `getBswAsynchronousServerCallReturnsEvents`),
the parser dispatch + handler, the writer dispatch + handler, and both dispatch
tests. After relocation, update `KNOWN_NAME_COLLISION_CLASSES` counts in
`test_model_imports.py`, stale `# from ...` comments in `models/__init__.py`, and
the source path in `docs/development/method_deviation_by_class.md`.

### 3. Schedule-Event Subtype Parent Mismatch

**ISSUE**: The class inherited from `BswEvent`, but Table 5.36's `Base` chain is
`ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable,
MultilanguageReferrable, Referrable` — the most-derived model class is
`BswScheduleEvent`, the direct parent shared with the sibling schedule events.
The deviation report `deviation_class_hierarchy_mismatches.md` flagged
`expected BswScheduleEvent, got BswEvent`.

**RESOLUTION**: Follow the "most-derived model class as direct parent" bullet of
Rule 1. All `BswScheduleEvent` subtypes also take `(parent, short_name)` in
`__init__`, so the class signature changed from `__init__(self)` to
`__init__(self, parent, short_name)`.

### 4. Multiplicity 0..1 Must Be `Optional[T] = None`

**ISSUE**: `eventSource` is `0..1`, but the old field was declared
`self.serverCallPointRef: RefType = None` — non-optional annotation with a
`None` default.

**RESOLUTION**: `0..1` → `Optional[RefType] = None`; the getter returns
`Optional[RefType]`. Rule 3 now has an explicit check for a field defaulting to
`None` that is annotated non-optional.

### 5. Spec Wording for Comments and Docstrings

The spec note — "This is the 'callback' event for asynchronous
Client-Server-Communication via the BSW Scheduler which is thrown after
completion of the asynchronous Client-Server call. Its eventSource specifies the
call point to be used for retrieving the result." — is now the class docstring.
The attribute comment carries the constr_10288 existence requirement and the
getter/setter docstrings describe "the call point to be used for retrieving the
result", per Rule 5.

## Feedback from BswEntryRelationship Review

When reviewing and updating `BswEntryRelationship` and `BswEntryRelationshipSet`
classes per the above rules, the following observations emerged:

### 1. Non-Identifiable ARObject Classes

**ISSUE**: `BswEntryRelationship` inherits from `ARObject` (not `Identifiable`), so
it has no `short_name` and no `__init__` parent/short_name parameters. The class
should follow the simpler `ARObject` pattern: `__init__` with no parameters,
and all fields initialized to default values (None / []).

**RESOLUTION**: Classes inheriting from `ARObject` do not require parent/short_name
parameters in their `__init__`. Examples:
- `BswEntryRelationship(ARObject)` → `__init__(self)` with no parent/short_name
- `BswEntryRelationshipSet(Identifiable)` → `__init__(self, parent, short_name)`

When implementing a class, check its spec `Base` column:
- If it lists `Identifiable`, use `Identifiable` as the parent class and
  accept parent/short_name in `__init__`.
- If it lists only `ARObject` (or other non-Identifiable bases), inherit from
  `ARObject` and initialize only the instance fields in `__init__` without
  parent/short_name.

### 2. String Enum Instantiation in Tests

**ISSUE**: When testing classes with string enum types (e.g., `BswEntryRelationshipEnum`),
tests must use enum member values, not call the enum constructor.

**INCORRECT**:
```python
enum_value = BswEntryRelationshipEnum()  # TypeError: missing 1 required positional argument
```

**CORRECT**:
```python
enum_value = BswEntryRelationshipEnum.DERIVED_FROM  # Use enum member
```

This applies to all Python `Enum` subclasses. Tests should reference enum literals
like `EnumClass.MEMBER_NAME` rather than attempting to instantiate the enum
itself. Reference implementations use this pattern throughout (e.g.,
`BswCallType.SYNCHRONOUS`, `BswExecutionContext.TASK`).

**SPECIFICATION SYNC**: `BswEntryRelationshipEnum` contains only one literal per
AUTOSAR Table 4.20: `DERIVED_FROM = "derivedFrom"`. This describes that the
BswModuleEntry referenced as "to" needs to have the same signature as the
"abstract" BswModuleEntry referenced as "from".

### 3. Module Structure: Single File for Spec Package

**OBSERVATION**: When a spec package contains multiple classes (e.g.,
`M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`), they must all reside
in a single Python module. In this project, that means:
- Either a single file: `BswInterfaces.py` containing `BswEntryRelationship`,
  `BswEntryRelationshipEnum`, and `BswEntryRelationshipSet`.
- Or a package (directory) with `__init__.py` that imports and re-exports all
  classes from submodules.

**CORRECTION MADE**: Originally, the three classes were split across separate files
in a `BswInterfaces/` directory. Per Rule 8, they were consolidated into the
single `BswInterfaces.py` module file (which already existed and contained
`BswModuleDependency`, `BswModuleEntry`, and `BswModuleClientServerEntry`).
This ensures all classes for the spec package are in one place and improves
maintainability and import clarity.

### 4. Method Signature Length and Line Breaks

**OBSERVATION**: Method signatures are formatted by Black at
`line-length = 200` (`pyproject.toml`), enforced via `npm run black-check`.
Black collapses any signature that fits within 200 characters onto a single
line, so signatures must NOT be hand-broken when they fit:

```python
def setBswEntryRelationshipType(self, value: Optional[BswEntryRelationshipEnum]) -> "BswEntryRelationship":
```

Hand-breaking a short signature (or leaving a trailing comma) makes
`black-check` fail. Only signatures that exceed 200 characters are split, and
Black does that automatically (one parameter per line). This supersedes the
older 79-character line guidance.

### 5. Implementation of New Rules (9, 10, 11)

**NEW RULES ADDED**: Three new rules have been formally adopted for class
consistency:

- **Rule 9 (Attribute Spacing)**: Every member (attribute or method) must be
  separated by exactly one blank line. This applies within `__init__` for
  attributes and between methods.

- **Rule 10 (Method Signature Formatting)**: Method definitions and their
  parameters must be on the same logical line. Black (line-length 200) collapses
  signatures that fit onto one line and splits only those exceeding 200
  characters; the entire method signature (parameters + return type) stays
  within the method definition block.

- **Rule 11 (Enum Type Inheritance)**: All enumeration classes must inherit
  from `AREnum` (not from Python's built-in `Enum`, `str` + `Enum`, etc.).
  This ensures consistent enum handling across the AUTOSAR model.

**Implementation in BswEntryRelationshipEnum**:
- Changed from `class BswEntryRelationshipEnum(str, Enum)` to
  `class BswEntryRelationshipEnum(AREnum)`.
- Synced enum members with AUTOSAR PDF Table 4.20: now contains only
  `DERIVED_FROM = "derivedFrom"` (previously had READS, WRITES, CALLS, TRIGGERS
  which were not in the spec).
- Added spec-based inline comment documenting the literal's meaning per AUTOSAR.
- Added blank lines between enum members per Rule 9.
- Verified that the enum member access pattern (`EnumClass.MEMBER_NAME`)
  works correctly with `AREnum`.

## Feedback from BswModuleEntity Review

When reviewing and updating `BswModuleEntity` (Table 5.4,
`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
per the above rules, the following observations emerged:

### 1. Spec `0..1` ref Held as a List (Multiplicity Reversal)

**ISSUE**: `schedulerNamePrefixRef` was typed `List[RefType] = None`. The spec
Table 5.4 says `schedulerNamePrefix` is `0..1` Kind `ref`, and the XSD declares
`SCHEDULER-NAME-PREFIX-REF` with `maxOccurs="1"`. A `List` defaulting to `None`
is neither a valid list (default should be `[]`) nor a valid single ref
(default should be `None`). The existing tests already treated it as a single
`RefType`, so only the field annotation and the getter/setter docstrings
("list of scheduler name prefix references") were wrong.

**RESOLUTION**: Changed to `schedulerNamePrefixRef: Optional[RefType] = None`
and aligned the getter/setter signatures and docstrings. Rule 1 now explicitly
covers the reverse multiplicity deviation (spec `0..1` held as a list) and
notes that getter/setter docstring wording ("list of ...") is a symptom of a
multiplicity mismatch.

### 2. Missing Parser/Writer Support = Silent Round-Trip Loss

**ISSUE**: `schedulerNamePrefixRef` had a field and accessors, but neither the
parser nor the writer handled `SCHEDULER-NAME-PREFIX-REF`. Any value set in
the model would be silently dropped when writing to ARXML, and never restored
when parsing.

**RESOLUTION**: Added `entity.setSchedulerNamePrefixRef(
self.getChildElementOptionalRefType(element, "SCHEDULER-NAME-PREFIX-REF"))`
to `readBswModuleEntity` and `self.setChildElementOptionalRefType(
element, "SCHEDULER-NAME-PREFIX-REF", entity.getSchedulerNamePrefixRef())`
to `writeBswModuleEntity`. Rule 1 now requires both parser and writer coverage
for every implemented attribute.

### 3. `createXXX` Factories for Referrable (Non-Identifiable) Children

**ISSUE**: Rule 1's `createXXX` vs `setXXX` guidance only mentioned
`Identifiable` children. `BswModuleCallPoint` has spec `Base`
`ARObject, Referrable` — it is **not** `Identifiable` — yet it carries a
short name and `BswModuleEntity` correctly exposes
`createBswAsynchronousServerCallPoint(short_name)` and
`createBswSynchronousServerCallPoint(short_name)` factories (the parser's
`readBswModuleEntityCallPoints` relies on them).

**RESOLUTION**: Generalized the rule: any aggregated child whose spec `Base`
lists `Referrable` or `Identifiable` (i.e. the child has a short name) may use
a `createXXX(short_name)` factory; only plain `ARObject` children without a
short name (e.g. `ModeErrorBehavior`) use plain `setXXX`.

### 4. Testing an Abstract Class's `__init__`

**ISSUE**: `BswModuleEntity` is abstract and cannot be instantiated, so
`__init__` had no direct test and the checklist row stayed `[ ] test`.

**RESOLUTION**: Added `test_concrete_subclass_initialization` that instantiates
`BswCalledEntity` (a concrete subclass) and asserts every default set by
`BswModuleEntity.__init__` (all lists `[]`, all single refs `None`). The
docstring mentions `__init__` so the set-based checklist check can verify the
`[x] test` marker. Rule 7 now documents this abstract-class testing pattern
(`ExecutableEntity` already followed it).

### 5. Spec Reference Line in the Class Comment

**ISSUE**: The checklist comment block did not name the PDF spec table the
class is aligned against, so the alignment was not traceable from the source
file alone.

**RESOLUTION**: Added `# Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf,
Table 5.4, p.72` as the first line of the checklist block, following the
pattern already used by `ExecutableEntity` (`Table 5.3, p.70`) and
`ReentrancyLevelEnum` (`Table 5.5, p.73`). The page number was verified by
extracting the actual PDF text (`pypdf`): Table 5.3 is on p.70, the
`BswModuleEntity` class header on p.71, and the full Table 5.4 attribute table
on p.72. Rule 2 now requires the `# Spec:` line and names these three
reference classes as examples.

## Feedback from BswExclusiveAreaPolicy Review

When reviewing and updating `BswExclusiveAreaPolicy` (Table 5.17) and the
related `ApiPrincipleEnum` (Table 5.18) per the above rules, the following
observations emerged:

### 1. A Spec Class Must Not Be Modeled as an Enum

**ISSUE**: `BswExclusiveAreaPolicy` was implemented as `AREnum` with members
`NONE = "none"`, `INTERNAL = "internal"`, `EXTERNAL = "external"`. Table 5.17
defines it as a **class** (Base: `ARObject, BswApiOptions`) with attribute rows
`apiPrinciple` (ApiPrincipleEnum, `0..1`, attr) and `exclusiveArea`
(ExclusiveArea, `0..1`, ref). The three enum members appear nowhere in the
spec — they were placeholder values.

**RESOLUTION**: Rewrote `BswExclusiveAreaPolicy` as a concrete subclass of
`BswApiOptions` with `apiPrinciple: Optional[ApiPrincipleEnum]` and
`exclusiveAreaRef: Optional[RefType]` fields plus accessor pairs. Rule 1 now
states the general test: a spec table headed `Class` with populated
`Attribute` rows means a model class with fields/accessors; only tables headed
`Enumeration` with `Literal` rows become enums.

### 2. Same-Named Module File vs Directory = Dead Code

**ISSUE**: The class lived in `BswBehavior/BswExclusiveAreaPolicy.py`, a
directory without `__init__.py`. Because the sibling `BswBehavior.py` module
exists, Python resolves `BswBehavior` to the module file and the directory
classes are unreachable — importing the "full path" raised
`ModuleNotFoundError: 'BswBehavior' is not a package`. The 9 classes in
`BswBehavior/` were effectively dead code.

**RESOLUTION**: Per Rule 8 (exactly one module per spec package), the class was
migrated into `BswBehavior.py`, the duplicate file deleted, and the class
removed from the name-collision list in `test_model_imports.py` (it is now
importable from `armodel` directly). Rule 8 now calls out module-vs-directory
shadowing explicitly: when the spec `Package` maps to `X.py` but a `X/`
directory also exists without `__init__.py`, classes in the directory are
unreachable and must live in the module file.

### 3. Spec Default Value vs Model `None` Default

**ISSUE**: The Table 5.17 note for `apiPrinciple` states "The default value is
'common'", and the XSD declares `minOccurs="0"` for `API-PRINCIPLE`. The model
convention (Rule 1) maps `0..1` attributes to `Optional[T] = None`, so the
field is initialized to `None` and the spec default is preserved in the
attribute comment rather than enforced in `__init__`.

**OBSERVATION**: If an attribute's spec default must be observable in the
model (e.g. the writer should emit it when unset), initialize the field to the
spec default (e.g. `ApiPrincipleEnum.COMMON`) and record the choice — do not
silently drop the spec note.

### 4. Related Enum Had Placeholder Members

**ISSUE**: `ApiPrincipleEnum` (Table 5.18) contained `CALLEE = "callee"` and
`CALLER = "caller"` — not in the spec. The spec literals are `common`
(`atp.EnumerationLiteralIndex=0`) and `perExecutable`
(`atp.EnumerationLiteralIndex=1`).

**RESOLUTION**: Corrected to `COMMON = "common"` / `PER_EXECUTABLE =
"perExecutable"` with spec-based inline comments and Tags, added the `# Spec:`
line, and added tests. This is the second time a placeholder enum was found
(see `BswEntryRelationshipEnum`), confirming Rule 12's guidance: never trust a
previous implementation — always verify the enum members against the PDF table.

### 5. Aggregation Not Yet Implemented

**OBSERVATION**: Table 5.17 says `BswExclusiveAreaPolicy` is aggregated by
`BswInternalBehavior.exclusiveAreaPolicy`, and the XSD references
`EXCLUSIVE-AREA-POLICY` elements there. Neither the aggregation nor the
parser/writer support exists yet, so there is no round-trip surface for the
class. Parser/writer coverage (Rule 1) will be added together with the
aggregation in a follow-up task.

## Feedback from BswEvent Review

When reviewing and updating `BswEvent` (Table 5.22,
`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
per the above rules, the following observations emerged:

### 1. `iref` Kind Attributes Use `<name>IRef(s)` Naming and a `*InstanceRef` Element Type

**ISSUE**: Table 5.22 has three Kind `ref`/`iref` attributes:
`contextLimitation` (`*`, ref → `BswDistinguishedPartition`),
`disabledInMode` (`*`, iref → `ModeInBswModuleDescriptionInstanceRef`),
`startsOnEvent` (`0..1`, ref → `BswModuleEntity`). The existing model had only
`startsOnEventRef`; `contextLimitationRefs` and `disabledInModeIRefs` were
missing entirely (also flagged in `docs/method_deviation_by_class.md`).

**RESOLUTION**: Added `contextLimitationRefs: List[RefType]` and
`disabledInModeIRefs: List[ModeInBswModuleDescriptionInstanceRef]`. Note that
the two attributes, though both `*` multiplicity, use **different element
types**: a plain `ref` becomes `List[RefType]`, while an `iref` becomes
`List[<name>InstanceRef>` (the `*In*InstanceRef` class for that target type).
Do not model an `iref` attribute as `List[RefType]` — the parser must build
the structured `*InstanceRef` object from its two inner refs
(`CONTEXT-MODE-DECLARATION-GROUP-REF` / `TARGET-MODE-REF`), and the writer
must serialize it back into the same sub-elements. Rule 1's suffix-naming
check was extended to cover the `iref` Kind.

### 2. Instance Ref Types in Another Spec Package Need `TYPE_CHECKING` in the Model

**ISSUE**: `ModeInBswModuleDescriptionInstanceRef` lives in
`BswModuleTemplate/BswOverview/InstanceRefs/` and is aggregated by
`BswModuleDescription`, whose package (`BswOverview/__init__.py`) imports
`BswBehavior.py`. A direct `from ...BswOverview.InstanceRefs import
ModeInBswModuleDescriptionInstanceRef` in `BswBehavior.py` creates a circular
import at module load time.

**RESOLUTION**: Import the type under `if TYPE_CHECKING:` and annotate the
field and getter with a string forward reference
(`List["ModeInBswModuleDescriptionInstanceRef"]`). The parser and writer
import it directly — they are below the model classes in the import graph, so
no cycle occurs there. Rule 1 now documents this pattern: model modules that
type against a `*InstanceRef` (or any type aggregated by a sibling package)
must use `TYPE_CHECKING`, while parser/writer imports stay eager.

### 3. `startsOnEventRef` Multiplicity Was Fine but Annotation Was Not `Optional`

**ISSUE**: `startsOnEvent` is `0..1`, so the field
`startsOnEventRef: RefType = None` had the right default but the wrong
annotation — a single ref held as `RefType` (non-optional) with a `None`
default is internally inconsistent, and the getter lacked a return type hint.

**RESOLUTION**: Aligned to `startsOnEventRef: Optional[RefType] = None` with
`getStartsOnEventRef() -> Optional[RefType]` and a typed, chainable
`setStartsOnEventRef(value: RefType) -> "BswEvent"`. This is the same
multiplicity/annotation discipline as Rule 1's single-value bullet, applied
at the annotation level.

### 4. Parser/Writer Needed a Structured-Iref Helper Pair

**ISSUE**: `disabledInModeIRefs` is a list of *structured* instance refs, so
the parser cannot use the plain `getChildElementOptionalRefType` helper and the
writer cannot use `setChildElementOptionalRefType` — each
`DISABLED-IN-MODE-IREF` element has two sub-elements that must be read/written
together.

**RESOLUTION**: Added `getModeInBswModuleDescriptionInstanceRef(element)` to
the parser (mirrors the existing `getRModeInAtomicSwcInstanceRef`) and
`setModeInBswModuleDescriptionInstanceRef(element, key, iref)` to the writer
(mirrors `setRModeInAtomicSwcInstanceRef`). The `*InstanceRef` accessor pair
pattern generalizes: when an attribute's element type is a `*InstanceRef`
class, implement a dedicated read/write helper rather than forcing the generic
ref helpers.

### 5. Round-Trip Verification for New Fields

**OBSERVATION**: Because `BswEvent` is abstract, the new fields were verified
through a concrete subclass (`BswOperationInvokedEvent`) in a full
parse → write → re-parse round trip: set
`addContextLimitationRef` / `addDisabledInModeIRef` / `setStartsOnEventRef`
on a `BswTimingEvent`, save, reload, and assert the three values come back.
This is the practical test that Rule 1's "parser and writer coverage" check
is meant to guarantee, and it belongs in the manual verification workflow for
any class that gains attributes.

### 6. Getter Return Types Were Missing on Pre-Existing Accessors

**ISSUE**: The original `getStartsOnEventRef` had no return type hint
(`def getStartsOnEventRef(self):`), and the setter overwrote the field
unconditionally instead of following the `None` no-op pattern.

**RESOLUTION**: Added `-> Optional[RefType]` to the getter, a type hint to the
setter, and converted the setter to the `None` no-op (Rule 4). When a review
touches an existing accessor for a Rule 1 fix, bring it fully up to Rule 3/4
compliance in the same pass — do not leave half-typed accessors behind.

## Feedback from ModeInBswModuleDescriptionInstanceRef Review

When reviewing and updating `ModeInBswModuleDescriptionInstanceRef` (Table C.37,
`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/InstanceRefs/__init__.py`)
per the above rules, the following observations emerged:

### 1. Inner Attributes of a `*InstanceRef` Class Are Plain `ref`s

**ISSUE**: The outer attribute that *uses* this class (`BswEvent.disabledInMode`)
is Kind `iref` and is typed as `List[ModeInBswModuleDescriptionInstanceRef]`. But
the `ModeInBswModuleDescriptionInstanceRef` class's own attributes (the
sub-elements the parser reads: `base`, `contextModeDeclarationGroup`,
`targetMode`) are each Kind `ref`, `0..1`. The original model held them as
object references (`bases: Optional[BswModuleDescription]`,
`targetModes: Optional[ModeDeclaration]`) and one non-optional `RefType`
(`contextModes: RefType = None`).

**RESOLUTION**: The inner attributes of a `*InstanceRef` class always map to
`Optional[RefType]` with the plain `Ref` suffix (the sub-element keys in the
parser/writer, e.g. `getChildElementOptionalRefType(element,
"CONTEXT-MODE-DECLARATION-GROUP-REF")`), since the parser's reference helpers
return `RefType`. Do **not** annotate them with the `<name>InstanceRef` class
or hold resolved object references. The same correction applies to any
`*InstanceRef` class that mirrors this pattern e.g. `RModeInAtomicSwcInstanceRef`,
whose `baseRef`/`contextPortRef`/etc. are likewise `RefType`.

### 2. Spec `Base` Can Name `AtpInstanceRef`, Not Just `ARObject`

**ISSUE**: Table C.37 lists `Base = ARObject, AtpInstanceRef`, but the class
inherited only from `ARObject`. Inheriting the wrong base silently accepted the
`ARObject`-style layout even though the spec's concrete abstract base is
`AtpInstanceRef` (the shared base of all instance-reference classes). The
Rule 1 base-class guidance only covered `Referrable`/`Identifiable`/`ARObject`.

**RESOLUTION**: Generalized Rule 1's base-class bullet: when the spec `Base`
column names a concrete abstract base (such as `AtpInstanceRef`), inherit it
rather than falling back to bare `ARObject`. This matches the sibling
`RModeInAtomicSwcInstanceRef(AtpInstanceRef)`. `AtpInstanceRef` is abstract, so
the concrete subclass defines its own attrs and its checksum/`__init__` wiring
stays unchanged.

### 3. `atpDerived` Attributes Are Exempt from Parser/Writer Coverage

**ISSUE**: Rule 1 requires every implemented attribute to be covered by both
parser and writer. `base` is `atpDerived` (`Stereotypes: atpDerived`,
`xml.sequenceOffset=10`) — a derived attribute with **no** XML element in the
element group (only `CONTEXT-MODE-DECLARATION-GROUP-REF` and `TARGET-MODE-REF`
exist in the XSD), so it cannot and must not have parser/writer handling.

**RESOLUTION**: Generalized Rule 1's parser/writer bullet to exempt
`atpDerived` attributes: they still map to a field + accessor (attribute-level
completeness) but are recorded as `atpDerived` in the deviation tracker rather
than `ok`/`missing`, since their value is derived and never serialized.

### 4. `Ref` Suffix Appends to the Whole CamelCase Attribute Name

**ISSUE**: The original names `contextModes`/`targetModes`/`bases` diverged from
the spec attribute names (`contextModeDeclarationGroup`, `targetMode`, `base`)
and dropped the `Ref` suffix, which also broke matching against the parser/writer
sub-element keys (`CONTEXT-MODE-DECLARATION-GROUP-REF` / `TARGET-MODE-REF`).

**RESOLUTION**: For a Kind `ref` attribute, the `Ref` suffix is appended to the
full camelCase spec attribute name:
`contextModeDeclarationGroup` → `contextModeDeclarationGroupRef`,
`targetMode` → `targetModeRef`, `base` → `baseRef`; getters/setters
`getBaseRef`/`setBaseRef`, `getContextModeDeclarationGroupRef`/`setContextModeDeclarationGroupRef`,
`getTargetModeRef`/`setTargetModeRef`. This 1:1 maps to the parser/writer
sub-element keys, keeping the instance-ref element keys and model accessors
aligned. Multi-word Kind `ref` attributes must not be collapsed or reordered.

### 5. Package Name Mismatch: `InstanceRefs/ModeInBswModuleDescriptionInstanceRef.py` Implied a Non-Existent Sub-Package

**ISSUE**: The class was placed in `InstanceRefs/ModeInBswModuleDescriptionInstanceRef.py`.
The spec `Package` row is
`M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::InstanceRefs`, where the
class name is the table's `Class` header — a direct member of the `InstanceRefs`
package, **not** a nested package. The sub-module filename made the class name the
tail of the module path, so it falsely implied the spec package were
`...::InstanceRefs::ModeInBswModuleDescriptionInstanceRef`. That is a **package
name mismatch** (Rule 8): the Python layout did not reflect the spec `Package`
row, and it also added a pointless `__init__.py` re-export hop for a package that
holds a single class.

**RESOLUTION**: The accurate rule is *package-name-match*, not merely "move to
`__init__.py`". Because the class is a direct member of `InstanceRefs`, it must be
defined directly in `InstanceRefs/__init__.py`; the sub-module
`ModeInBswModuleDescriptionInstanceRef.py` was deleted. Every import must match
this package location and import the class from the package — `from ...InstanceRefs
import ModeInBswModuleDescriptionInstanceRef` — never from a class-named sub-module
(`from ...InstanceRefs.ModeInBswModuleDescriptionInstanceRef import ...`), which
would imply a non-existent sub-package and now raises `ModuleNotFoundError`.
The parser/writer and package `__init__.py` imports already used the package form;
the mirrored test file's import was updated from the sub-module form to the package
form. Generalizing: never let the class name become the final segment of the module
path when the spec `Package` row ends at a package that *contains* the class — define
the class as a direct member of that package's `__init__.py` and import it from the
package, not from a class-named sub-module.

## Feedback from BswModeSwitchEvent Review

When reviewing and updating `BswModeSwitchEvent` (Table 5.31,
`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`) and the
related shared enum `ModeActivationKind` (Table 5.34) per the above rules, the
following observations emerged:

### 1. An Enum Shared by Two Templates Lives in `CommonStructure`, Not the BSW Module

**ISSUE**: `ModeActivationKind` (spec Table 5.34, used as the type of
`BswModeSwitchEvent.activation` **and** `SwcModeSwitchEvent.activation`) was
defined in `CommonStructure/ModeDeclaration.py` as `class ModeActivationKind(str,
Enum)` — it violated Rule 11 (must inherit `AREnum`). Rule 11's guidance assumes
the enum lives next to the class that uses it, but `ModeActivationKind` is shared
across two spec packages (`BswModuleTemplate::BswBehavior` and
`SWComponentTemplate::SwcInternalBehavior::RTEEvents`), so it cannot live in
either consuming package without cross-template coupling.

**RESOLUTION**: A spec enum that is the *attribute type* of classes in **more than
one** spec package is defined once in the `CommonStructure` package
(`CommonStructure/ModeDeclaration.py` for `ModeActivationKind`), and each
consuming template class imports it directly (no `TYPE_CHECKING` needed because
`CommonStructure` sits below the template packages in the import graph — it does
not import the templates). Rule 11 now covers shared enums: Rule 8's
"package location" applies to the enum's own spec table's `Package` row; when an
enum is referenced from multiple templates its home is `CommonStructure`, and the
`# Spec:` line names the table that *defines the enum* (Table 5.34, p.96), which
may be in a different PDF page/table than the class that uses it.

### 2. Bounded Multiplicity `0..N` (e.g. `0..2`) Still Maps to a `List` + `add`

**ISSUE**: Table 5.31 lists `mode` with multiplicity `0..2`, `ordered`. The
multiplicity bullet in Rule 1 covered only `*` → `List` and `0..1` → optional
single, so it was unclear whether a bounded `0..2` should be a fixed-size tuple,
two separate fields, or a list.

**RESOLUTION**: Any multiplicity with an upper bound > 1 (`0..N`, not just `*`)
maps to `List[T]` (default `[]`) with the usual `getXxxs` / `addXxx` accessors.
The upper bound is *not* enforced in the model — it is a schema constraint only
(`mode` → `modeIRefs: List[ModeInBswModuleDescriptionInstanceRef]`). `ordered`
means insertion order is preserved (matters for `onTransition`, where the order of
the two modes defines the transition direction), so `add` appends and the parser
reads in document order. Rule 1's multiplicity bullet now names the bounded-`0..N`
case explicitly.

### 3. Polymorphic Dispatch Must Be Updated Alongside a New Subtype

**ISSUE**: `BswModeSwitchEvent` had a dedicated `readBswModeSwitchEvent` parser
method and factory, and the parser's `readBswInternalBehaviorEvents` tag-name
dispatch already handled `BSW-MODE-SWITCH-EVENT`, but the **writer** had no
`writeBswModeSwitchEvent` method and — critically — `writeBswInternalBehaviorEvents`
had no `isinstance(event, BswModeSwitchEvent)` branch, so the event fell into the
`else: self.notImplemented(...)` fallback and was **silently dropped** on write.
This is a round-trip loss that Rule 1's parser/writer bullet only partially covers:
the bullet checks each *attribute* has a read/write, but a subtype can pass that
check (its attributes are read/written in the dedicated method) while the
*dispatch* that routes the whole subtype is missing.

**RESOLUTION**: Rule 1's parser/writer bullet now extends to polymorphic dispatch:
when a class is a concrete subtype of an abstract base (event, entity, policy,
etc.), adding it requires (a) a dedicated `readXxx`/`writeXxx` method, **and**
(b) a branch in the parent's dispatch function (`readBswInternalBehaviorEvents` /
`writeBswInternalBehaviorEvents`). A `notImplemented(...)` / `notImplemented(...)`
fallback is a warning at best and must not be relied on as "handled". The
existing writer test `test_dispatches_all_event_types` was extended with a
`BswModeSwitchEvent` to lock in the dispatch coverage.

### 4. `attr` Kind `0..1` Holds a Literal: Same `set` + `Optional` Pattern as `ref`

**ISSUE**: `activation` (Kind `attr`, Type `ModeActivationKind`, `0..1`) was
declared `activation: ModeActivationKind = None` — the annotation omitted
`Optional`, matching the `startsOnEventRef` bug class from the BswEvent review.

**RESOLUTION**: A Kind `attr` single attribute maps to `Optional[T] = None` with
`getActivation() -> Optional[T]` / `setActivation(value: T)` just like a `ref`;
the parser stores the literal produced by `getChildElementOptionalLiteral` and the
writer emits it via `setChildElementOptionalLiteral` (`value.getText()`), so the
field, getter, setter, parser and writer all agree on `ModeActivationKind` (which
is an `AREnum`, itself an `ARLiteral`). When the attribute is used with the shared
enum from CommonStructure, the model import is a plain import (no `TYPE_CHECKING`),
but the string forward reference in annotations is still used for the `iref`
`ModeInBswModuleDescriptionInstanceRef` type.

### 5. Sub-Type Testing of a Shared Enum

**ISSUE**: `ModeActivationKind` had no unit tests at all, and the enum's `__init__`
passes the valid-value tuple to `super().__init__((...))`, which Rule 12 requires
to be exercised (the aligned `ReentrancyLevelEnum` has a
`test_initialization` that asserts every literal and `getEnumValues()`).

**RESOLUTION**: Added `TestModeActivationKind` mirroring `TestReentrancyLevelEnum`:
`test_initialization` asserts the three literals (`ON_ENTRY`/`ON_EXIT`/`ON_TRANSITION`)
and their membership in `getEnumValues()`. A shared enum's tests live in the
mirrored `CommonStructure` test file (`tests/.../CommonStructure/test_ModeDeclaration.py`),
not in the BSW test file, matching where the enum is defined.

## Feedback from BswModeManagerErrorEvent Review

When reviewing and updating `BswModeManagerErrorEvent` (Table 5.33,
`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
per the above rules, the following observations emerged:

### 1. The `Base` Column Lists the Full Chain — Inherit the Most-Derived Model Class

**ISSUE**: The class was defined as `BswEvent` with `__init__(self)` in the
shadowed `BswBehavior/BswModeManagerErrorEvent.py` submodule. Table 5.33 lists
`Base = ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable,
MultilanguageReferrable, Referrable` — a full inheritance chain ending at
`BswScheduleEvent`, the same direct parent used by the sibling events
(`BswModeSwitchEvent` and `BswModeSwitchedAckEvent`). Picking `BswEvent` (a more
general ancestor) instead of `BswScheduleEvent` was wrong; the auto-generated
`reports/deviation_class_hierarchy_mismatches.md` flagged it as a parent mismatch.

**RESOLUTION**: Realigned to `BswScheduleEvent` with `__init__(self, parent,
short_name)`. Rule 1's base-class bullet now states the general test: when the
`Base` column lists the entire chain, inherit the **most-derived** model class in
that chain as the direct parent, never a more general ancestor.

### 2. Adding a Concrete Subtype Touches Four Places, Including the Aggregator

**ISSUE**: Rule 1's polymorphic-dispatch guidance covered the parser/writer
dispatch functions, but adding `BswModeManagerErrorEvent` also required the
aggregator `BswInternalBehavior` to expose a factory and getter
(`createBswModeManagerErrorEvent` / `getBswModeManagerErrorEvents`). Without the
factory, the parser's `BSW-MODE-MANAGER-ERROR-EVENT` tag-name branch would have
had nothing to call, and the aggregator's own method-parity checklist had to gain
the two rows or the set-based check would fail.

**RESOLUTION**: Added the factory/getter pair to `BswInternalBehavior` and its
checklist, plus the parser tag-name branch and the writer `isinstance` branch.
Rule 1's polymorphic-dispatch bullet now enumerates the four touch points:
subtype class, aggregator factory + getter (+ aggregator checklist), parser
dispatch, and writer dispatch.

### 3. A Whole Spec Package Can Be Shadowed — Update the Import Test When Migrating

**ISSUE**: The `BswBehavior/` directory (no `__init__.py`) held 8 classes,
including `BswModeManagerErrorEvent.py`, all unreachable because the sibling
`BswBehavior.py` module shadows the directory. This is the same Rule 8
module-vs-directory shadowing previously seen with `BswExclusiveAreaPolicy`, but
at the scale of a whole family of classes. The class was also tracked in
`tests/test_armodel/test_model_imports.py`'s `KNOWN_NAME_COLLISION_CLASSES`,
which silently kept it excluded from the import test.

**RESOLUTION**: Migrated the class into `BswBehavior.py` (the spec package
`M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`), deleted the dead
submodule, and removed the class from `KNOWN_NAME_COLLISION_CLASSES` (also
lowering the docstring's class count from 8 to 7). Rule 8 now documents that a
class listed in `KNOWN_NAME_COLLISION_CLASSES` is a signal it may live in a
shadowed directory, and that migration requires updating both the collision set
and its count in the module docstring.

### 4. A Minimal Single-`ref` Class Exercises the Rules Cleanly — No New Rule Needed

**OBSERVATION**: `BswModeManagerErrorEvent` is the minimal case: one `0..1`
Kind `ref` attribute (`modeGroup` → `modeGroupRef: Optional[RefType] = None`),
no enums, no lists, no bounded multiplicity. Every existing rule applied
without friction: the `# Spec: Table 5.33, p.95` line (page verified against the
PDF in `autosar/`), attribute comment from the spec note, getter/setter pair with
the `None` no-op, tests for initialization/get-set/None-no-op/chaining, parser
(`readBswModeManagerErrorEvent` + dispatch), writer (`writeBswModeManagerErrorEvent`
+ dispatch), and the deviation tracker entry flipping from `missing` to `ok`. The
minimal case confirms the core rules (spec/base/multiplicity/naming/
parser/writer/checklist) are complete for single-ref event subtypes; the only
generalization the class surfaced was constraint-text in comments (item 5).

### 5. Constraint Rows Are Spec Material for Comments — Rule 5 Generalized

**ISSUE**: Table 5.33 carries two constraints for `BswModeManagerErrorEvent`:
`constr_10286` ("the reference in the role modeGroup shall exist at the time
when the configuration of the BSW module is finished") applies to the
`modeGroup` attribute, and `constr_4081` ("the ModeDeclarationGroupPrototype
used by BswModeManagerErrorEvent shall be referred as
BswModuleDescription.providedModeGroup by the same module") applies to the
class as a whole. Neither appeared in the class. The `BswTimingEvent` review
had already observed that constraint text is spec material — its `period`
comment carries the `constr_4043` "shall be greater than 0" wording — but that
observation was recorded only in the feedback section, **not promoted into Rule
5**, so a class checked against Rule 5 alone would still omit its constraints.

**RESOLUTION**: Generalized Rule 5: the inline attribute comment must include
the attribute's `constr_*` constraint wording (citing the id), and class-level
`constr_*` rows belong in the class docstring alongside the note.
`BswModeManagerErrorEvent` now carries `constr_10286` on `modeGroupRef` and
`constr_4081` in its class docstring. Item 4's "no new rule needed" conclusion
was narrowed: the minimal single-ref class *did* surface one generalization,
though every other rule held without change.

## Feedback from BswModeSwitchedAckEvent Review

When reviewing and updating `BswModeSwitchedAckEvent` (Table 5.32,
`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
per the above rules, the following observations emerged:

### 1. Dispatch Tests Are a Fifth Touch Point When Adding a Subtype

**ISSUE**: Rule 1's polymorphic-dispatch bullet enumerated four touch points
(subtype, aggregator factory/getter + checklist, parser dispatch, writer
dispatch), but adding `BswModeSwitchedAckEvent` also required extending the
dispatch *tests*: the parser's
`test_readBswInternalBehaviorEvents_dispatches_all_types` and the writer's
`test_dispatches_all_event_types` assert that every event subtype is routed.
Without extending them, the two new branches would exist with no test exercising
them, so a later refactor could silently drop the event from the dispatch without
failing CI. The `BswModeSwitchEvent` review had extended the writer dispatch test
and mentioned it in passing, but the four-point list in the rule itself did not
include tests.

**RESOLUTION**: Generalized Rule 1 to **five** touch points: (e) extend the
parser and writer "dispatches all types" tests with the new subtype.
`BswModeSwitchedAckEvent` was added to both dispatch tests alongside its
branches.

### 2. A Sibling with the Identical Shape Is Aligned by Symmetry from the Aligned Class

**ISSUE**: `BswModeSwitchedAckEvent` is the second minimal single-ref event
subtype — identical `Base` chain (ending at `BswScheduleEvent`), identical single
`0..1` Kind `ref` attribute (`modeGroup`), identical aggregator
(`BswInternalBehavior`). Unlike `BswModeManagerErrorEvent`, it was an empty
shell: no `modeGroupRef` field, no accessors, no parser/writer support, no
aggregator factory/getter, and a checklist whose `__init__` row was stale
(`[ ] impl/docstring/test` although all three existed). The aligned
`BswModeManagerErrorEvent` in the same file was the exact template for every
touch point.

**RESOLUTION**: Ported the aligned sibling's shape — the same class docstring
(Table 5.32 note + `constr_4026`), the same attribute comment (Table 5.32 note +
`constr_10285`), the same accessor pair, the same aggregator factory/getter, and
the same parser/writer methods with the sibling's tag
(`BSW-MODE-SWITCHED-ACK-EVENT`) and element keys (`MODE-GROUP-REF`). When the
class under check is a sibling of an already-aligned class, the aligned sibling
is the review template: verify each rule against it, then port the touch points
and adapt tag names/keys. Rule 2's stale-`[ ]` case was also confirmed — the
`__init__` row was marked `[ ]` despite being fully implemented; the set-based
check catches missing rows but not stale markers, so the manual `[x]` pass must
still be done per class.

### 3. The Constraint-Text Rule Applied Cleanly to a Second Class

**OBSERVATION**: Rule 5's constraint-text bullet (from the `BswModeManagerErrorEvent`
review) applied without friction: Table 5.32's `constr_10285` (attribute) and
`constr_4026` (class) went into the attribute comment and class docstring exactly
as the sibling's did. The second application confirms the generalization rather
than a one-off; no further Rule 5 change was needed.

## Feedback from BswTimingEvent Review

When reviewing and updating `BswTimingEvent` (Table 5.25,
`src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`)
per the above rules, the following observations emerged:

### 1. A Derived Convenience Property Is Not a Fabricated Attribute

**ISSUE**: `BswTimingEvent.periodMs` is a read-only `@property` that computes
milliseconds from the spec `period` `TimeValue`. It appears **nowhere** in
Table 5.25, so a literal reading of Rule 1's "No fabricated attributes" bullet
would demand its removal. But it is not a fabricated *stored* field — it has no
backing storage and no setter; it is derived API. And it is not dead: the CLI
(`arxml_dump_cli.py`) and a parser test consume it. The class also carried
half-aligned state: the checklist row was `[ ] test`, the return annotation was
`-> int` even though the property returns `None`, and the setter was a
convoluted `if not (value is None and self.period is not None):` instead of the
uniform `None` no-op.

**RESOLUTION**: Kept `periodMs` and brought it to full compliance — added a
`test_period_ms`, changed the annotation to `Optional[int]`, marked the checklist
row `[x]`, and recorded it in the deviation tracker as an "added convenience
property" (the same treatment `ExecutableEntity.minimumStartIntervalMs` already
received). Rule 1's fabricated-attributes bullet now distinguishes **stored
fabricated fields** (remove) from **read-only derived convenience properties**
(keep, checklist + test + record as deviation), so future classes with a
ms-from-TimeValue helper are handled consistently instead of being deleted as
"invented API". The convoluted setter was simplified to the uniform
`if value is not None:` (Rule 4) and typed accessors added (Rule 3).

### 2. A `@property` Is a Checklist Member Like Any Method

**ISSUE**: `periodMs` was in the checklist but half-unmarked, and it is easy to
assume properties are exempt from the method-parity checklist because they are
not `def getXxx` accessors.

**RESOLUTION**: Rule 2 now states that a `@property` is an `ast.FunctionDef` in
the class body, so it needs a checklist row and a test exactly like a normal
method — the Rule 7 set-based check already treats it that way.

### 3. The `Base`-Chain and `# Spec:` Rules Held Without Friction

**OBSERVATION**: `BswTimingEvent` already inherited the correct most-derived
`Base` class (`BswScheduleEvent`) per the Rule 1 chain bullet, and the only
missing Rule 2 item was the `# Spec:` line (`Table 5.25, p.89`, page verified
against the PDF). The attribute comment now carries the Table 5.25 note ("time
period in seconds") plus the `constr_4043` constraint ("shall be greater than
0") — constraint text in the PDF is spec material for the comment just like the
attribute note. Parser (`readBswTimingEvent`), writer (`writeBswTimingEvent`)
and both dispatch branches were already present; no round-trip gap was found.
This is the simplest aligned class so far: one `attr` Kind attribute, no refs,
no lists, no enums — and it confirmed that an existing consumer of a
convenience property (the CLI's stale `period_ms` reference) must be audited
when the property is kept or removed.
