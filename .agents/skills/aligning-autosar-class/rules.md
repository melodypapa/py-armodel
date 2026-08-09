# AUTOSAR Model Class Check Rules

Self-contained rule reference for aligning any AUTOSAR model class in py-armodel.
`ClassName` denotes the class under check:

- source: `src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py`
  (or `<package>/<ClassName>/__init__.py`)
- mirrored test: `tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py`
- spec table: the class's attribute table in the AUTOSAR PDF
  (PDF `autosar/pdf/AUTOSAR_CP_TPS_*.pdf`, markdown `autosar/markdown/AUTOSAR_CP_TPS_*.md`,
  XSD `autosar-pdf/examples/xsd/`). The **PDF name, Table ID, and page number come from
  the PDF file directly** — the markdown carries no page numbers.

**IDs:** rules carry contiguous 4-digit IDs (`Rule 0001` …). Each notes its former
number for traceability. The 9-step workflow in `SKILL.md` references these IDs.

**Source of truth:** the AUTOSAR PDF spec table. When the XSD disagrees with the PDF,
follow the PDF. AUTOSAR version **must** be set before parse or write:
`AUTOSAR.getInstance().setARRelease('R23-11')`.

---

## Rule 0001 — Spec Alignment *(formerly Rule 1)*

The class must reflect the AUTOSAR PDF specification for its attributes.

### 1.1 Attribute existence and element kind

- Every attribute in the class exists in its spec table (search the markdown for the
  class name). The class is the right kind of element: a spec table headed `Class`
  with `Attribute` rows → a model class with fields/accessors, **not** an enum. A table
  headed `Enumeration` with `Literal` rows → an `AREnum`. Check the header **and**
  column structure; the `Base` column alone does not decide enum vs class.
- A placeholder enum from an earlier stage that does not match its `Class` spec table is
  a Rule 0001 violation.

### 1.2 Base class and inheritance chain

- The spec `Base` column determines the Python base and constructor signature.
  `Referrable`/`Identifiable` in `Base` → inherit that and
  `__init__(self, parent, short_name)`. `ARObject` only (no `Referrable`/`Identifiable`)
  → `__init__(self)` with all fields defaulted.
- Inherit the **most-derived** model class in the `Base` chain as the direct parent
  (never a more general ancestor); when `Base` lists a sibling/mid-hierarchy abstract
  class, choose it over the ancestor it extends.
- `ARElement` in the `Base` chain → inherit `ARElement` (it is the most-derived model
  class); do not downgrade to `Identifiable` because a sibling was. The parser/writer
  need no extra handling (`readIdentifiable`/`writeIdentifiable` is shared).
- A `Base` row naming two parallel inheritance chains selects one role-matching branch
  (the abstract base the codebase already provides for the class's primary role); do not
  add the second chain via Python multiple inheritance.
- "`InstanceRef`"-named classes take their base from the spec `Base` column — the name
  and `context`/`target` shape do **not** justify a `RefType`/`AtpInstanceRef` base.

### 1.3 Attribute-level completeness

- Every spec attribute maps to a field **plus** an accessor pair. The checklist (Rule
  0002) only tracks methods, so a class can be checklist-complete while missing
  accessors. For an `Identifiable` aggregator, a spec `*` `aggr` row still maps to its
  **own** typed list field (Rule 0004); the getter reads the field, not a
  `list(filter(isinstance, elements))` view of the registry.
- **Deprecated/removed** attributes (`atp.Status="removed"` in the XSD) map to **no**
  field; record `"deprecated (atp.Status=removed), not implemented"`.
- **The PDF is the source of truth for the attribute type.** When the parser/writer use
  a looser type than the PDF, upgrade them to the spec-typed helper (e.g.
  `getChildElementOptionalPositiveInteger`), the writer to `setChildElementOptional…`,
  and the field/getter/setter to `Optional[PositiveInteger]` — no deviation. Only when
  the XML form genuinely forces a different model type is a type deviation recorded.
- **No untyped accessors.** Every getter return and setter parameter must carry the
  concrete type. Field annotation, getter return, setter parameter, parser, and writer
  must all agree on the same type.
- **No fabricated attributes.** Every field must trace to a spec attribute. Three
  fabrication shapes, all fixed by **removing** the fabricated field(s) and adding the
  spec-aligned replacement(s) — not by recording a deviation:
  1. *N:1 collapse* — one generic field stands in for several spec refs (e.g. one
     `AnyInstanceRef` for two mutually-exclusive refs) → N spec-aligned fields, each
     with its concrete `RefType` + `Ref` suffix.
  2. *Shadowing rename* — an invented field name shadows a real spec attribute
     semantically → rename to the spec name **and** re-type to the spec primitive.
  3. *Whole-class stub* — every field fabricated; the class models none of its spec
     attributes → full rewrite from the spec table.
  Detector for shape 3: a class with no `# Spec:` line and no `# Spec verified:` marker
  (and a fully-`[ ]` checklist) has never had a field-to-spec pass; treat its entire
  field set as unverified. Exception: a class with **no own spec table** (attributes
  XSD-only, e.g. a concrete `<name>InstanceRef`) legitimately lacks these — excluded.
- **PDF-table omission vs fabricated API.** An attribute absent from the PDF
  `Attribute` column but **present in the XSD with a documentation block** (no
  `atp.Status="removed"`) is a rendering gap — **keep** it with coverage and record
  `"present in XSD, absent from PDF table rendering; kept"`. A field with **no spec
  basis anywhere** is fabricated — **remove**. Grep the XSD to decide.
  *Stale-XSD caveat:* if the repo's XSD predates the class's verified release, an
  XSD-only attribute may be an upstream deletion (not a rendering gap) — treat like
  `atp.Status="removed"` (no field) when absent from all verified-release PDF
  renderings. "Deleted Constraints in R\<release\>" appendix rows are **not**
  attribute-removal signals (they drop *constraints*, not attributes). Integration
  fixtures are authoritative — if a fixture carries an element, keep round-tripping it.
- **Cross-table aggregation:** an attribute whose definition lives in another class's
  table (discoverable via that table's `Aggregated by` row) is a spec attribute of the
  aggregator like its own rows.
- **Read-only derived convenience property** (`@property`, no backing field, no setter,
  e.g. a ms value derived from a `TimeValue`) is **kept**, not fabricated — give it a
  checklist row, test it, and record it as an "added convenience property".

### 1.4 Multiplicity

- `*` → `List[T]` (default `[]`); `0..1` → optional single `T` (default `None`). A
  bounded ordered mult like `0..2` still maps to `List[T]` with `getXxxs`/`addXxx`.
- A spec-`*` member whose **name is singular** still maps to a **plural** Python list
  field + plural accessors (`revisionLabel` `*` → `revisionLabels` +
  `addRevisionLabel`/`getRevisionLabels`). The per-item XML element keeps the singular
  form; pluralization lives only in Python naming.
- A `type (spec many vs py single)` (or reverse) deviation row is a **to-fix**, not an
  accepted deviation — convert the field/accessors to the list shape, add the
  wrapper-element parser/writer (1.7), update tests, and **remove** the row. A
  `type (spec many vs py single)` whose "many" came from the XSD (PDF Mult `0..1`) is a
  stale row to remove — the single-field model is PDF-correct.

### 1.5 Naming

- Kind suffix: `ref` → `Ref`/`Refs`, `tref` → `TRef`, `iref` → `IRef`/`IRefs`. An `iref`
  attribute's element type is a concrete `<name>InstanceRef` class; the list annotation
  is that class, **not** `RefType`. Within a `<name>InstanceRef` class, the inner
  attributes are ordinary Kind `ref` rows → `Optional[RefType]` with the plain `Ref`
  suffix appended to the full camelCase name.
- The field **base name** comes **verbatim** from the spec `Attribute` column; the Kind
  suffix is appended to that exact base. An already-plural base keeps its plural form
  (`measurableSystemConstantValues` → `…ValuesRefs`). A name mismatch is fixed by
  **renaming** (field + accessors + checklist + consumers), never recorded as a
  `naming` deviation — remove the row once renamed.

### 1.6 `createXxx` vs `setXxx`

- If the aggregated child's spec `Base` lists `Referrable`/`Identifiable` → expose
  `createXxx(short_name)`. If the child is a plain non-Identifiable object → `setXxx`
  (`0..1`) or `addXxx(value)` (`*`). The test is "does the child's `Base` include
  `Referrable`", not narrowly "is it `Identifiable`".
- A working `setXxx`/`getXxx` pair for a `0..1` `Referrable` child is a **violation
  even when implemented/tested** — migrate to `createXxx(short_name)` + `getXxx()`.
- For a `*` non-Identifiable child: `addXxx(value)` + `getXxxs()` — do **not** invent a
  `createXxx(short_name)` factory (no short name to duplicate-check) and do **not**
  invent a no-arg `createXxx()` (the parser instantiates and hands to `addXxx`).
- An **abstract aggregated child** gets one `createXxx<Subtype>(short_name)` factory per
  concrete subtype (the abstract type is not instantiable); for `0..1` each assigns the
  single field, for `*` each appends. The parser dispatches on the XSD child tag, the
  writer on `isinstance`.
- An already-aligned sibling in the wrong shape is a prior deviation, not a template —
  the shape rule wins; record the sibling to reconcile later.
- A factory named after the child type does **not** make a `*` member "missing": for
  `ClientServerInterface.possibleError` (type `ApplicationError`), `createApplicationError`
  is the factory, `getPossibleErrors` is the getter — a `missing` row for `possibleError`
  is stale; remove it.

### 1.7 Reader (parser) and writer coverage

- Every implemented attribute must be covered by **both** the reader and the writer; an
  attribute with field + accessors but no reader/writer element is silently dropped on
  round-trip. The checklist (Rule 0002) is **blind** to this — verify by grepping the
  reader and writer for each field's XML tag. A shared `readXxx`/`writeXxx` helper's
  existence is **not** evidence a given aggregator calls it — grep each aggregator.
- **Polymorphic dispatch (five-place pattern):** a concrete subtype of an abstract base
  needs (a) the subtype class, (b) the aggregator's `createXxx`/`getXxxs` + checklist
  rows, (c) the reader dispatch branch, (d) the writer dispatch branch, (e) reader
  **and** writer dispatch tests. A top-level package element (`Aggregated by:
  ARPackage.element`) applies the same pattern with `ARPackage` as aggregator. Dispatch
  **nests** — a subtype that itself aggregates is its own dispatcher.
- A concrete `<name>InstanceRef` subclass is polymorphic like any subtype: needs a
  reader `readXxx`/`getXxxIRef` branch + writer branch + dispatch tests. Inner
  `atpAbstract` attributes are concretized by subclasses; `atpDerived` inner attributes
  have no XML element (exempt).
- **Typed vs polymorphic iref shape.** A fixed-concrete iref (XSD element `type` is the
  `<name>InstanceRef` class) is read/written **flat** — inner refs directly under the
  attribute-named element, no nested wrapper, no flat-ref text. Polymorphic irefs
  (choice of subtype elements) use the nested wrapper. Mixing the shapes silently drops
  inner refs on round-trip.
- **Exception:** an `atpDerived` attribute has no XML element — no reader/writer
  coverage, but still a field + accessor pair; record `atpDerived`.
- **Wrapper-element lists.** A spec-`*` attribute whose items live in a wrapper element
  (`<REVISION-LABELS><REVISION-LABEL>`) → the field is the flat list, no model field for
  the wrapper. Reader: iterate `WRAPPER/ITEM` and `addXxx` each; writer: emit the
  wrapper **only when non-empty**, one item per entry. The item tag is XSD-driven (may
  be the type's element name, a `<NAME>-REF-CONDITIONAL`, or `<BASE>-IREF` for iref
  wrappers) — read it from the XSD, do not derive by rule of thumb.
- **`atpVariation`** classes wrap attributes in `VARIANTS/CONDITIONAL`; read/write the
  conditional transparently into the owning object (no separate Conditional model).
  Attribute-level `atpVariation` flattens to a plain wrapper list, **not**
  `VARIANTS/CONDITIONAL`.
- **Identity-only child serialization** (a not-yet-aligned child) is debt: an aligned
  model whose aggregator still emits an empty item element is a Rule 1.7 violation; when
  the child's alignment lands, replace the placeholder with a real `readXxx`/`writeXxx`
  in the same change, and assert the child's field values in the round-trip test.
- **Aggregator sequenced after the child:** an aggregator with zero serialization whose
  only child is unaligned defers its own reader/writer coverage (recorded as pending),
  while its **model** is fully aligned in the meantime.
- A shared `readXxx`/`writeXxx` that calls `readIdentifiable`/`writeIdentifiable` is not
  reusable by every sibling subtype — check the subtype's own XSD complexType; a
  non-`Referrable` subtype must call `readARObjectAttributes`/`writeARObjectAttributes`
  and may need a companion `<Name>Ident` (`IdentCaption`) class as its reference target.
- **Inherited base attributes** must trace to an element in the subtype's effective
  element set, not just to the model field — grep the base **and** subtype reader/writer
  for the element tag; an inherited attribute with an XSD element but no reader/writer is
  dropped on round-trip.

### 1.8 Cross-package types

- A field whose type lives in a different package that imports back → import under
  `TYPE_CHECKING` and annotate with a string forward reference; the reader/writer may
  import it directly (they sit below the model graph).
- A shared spec enum used by classes in >1 package is defined once in the lowest common
  package (typically `CommonStructure`) and imported directly by consumers.

### 1.9 Deviations

- Intentional deviations are recorded in the deviation tracker (Rule 0014) with the
  reason (`PDF-only`, `deprecated, not implemented`, `atpDerived`, `added convenience
  property`, …).

### 1.10 Missing referenced classes — collect and report later *(formerly "implement first")*

- The class may reference other model classes (a `ref`/`tref`/`iref` target, an
  `<name>InstanceRef` element type, an aggregated child type, a `Base` parent/sibling, a
  shared enum, a primitive container type). When such a type is declared in the spec but
  does **not** exist in the codebase, **implement it first** per these rules (create it
  from its own spec table, mirroring siblings/abstract parent, give it a checklist,
  tests, reader/writer coverage), then type the referencing attribute against it.
- **Workflow relaxation:** in the 9-step workflow, do **not** block on this — collect
  the referenced non-existent classes and **report them later** (Step 8), use a
  placeholder, and switch to the real type when that class gets its own pass. Rule
  0001.10 remains the standard for the referenced class's own alignment.
- A referenced class that **exists but is a stub** (no `# Spec:` line / marker, or
  fabricated fields) counts as missing — align it in the same pass. The same applies to
  a referenced enum whose members don't match its `Enumeration` table. A stub can be a
  whole family (align the transitive closure).
- A missing **primitive** has a `Primitive <Name>` table (not `Class`/`Enumeration`),
  possibly in a different PDF — implement it as an `ARLiteral` subclass.
- Exception: a class with no own spec table (XSD-only attributes) is **not** a stub.
- A placeholder substitute (`RefType` for a concrete class) is a last resort; record
  "class not yet implemented" and switch to the real type once implemented.

### 1.11 Member order follows the PDF

- Fields, accessor methods, and checklist rows are declared in the **displayed PDF row
  order** (top-to-bottom), not alphabetical or file-of-creation. `sequenceOffset` is a
  secondary signal; the displayed order wins when they diverge. The reader/writer still
  emit XML elements in XSD `sequenceOffset` order regardless of Python member order.
- **Group accessors per attribute, in spec row order** — one attribute's accessor pair(s)
  are contiguous, then the next attribute's. Grouping by method kind (all `create*` then
  all `get*`) is a violation even when every method is present. The set-based check is
  order-blind, so verify source order explicitly.
- Within one attribute, pair order depends on accessor kind: scalar `getXxx`/`setXxx` →
  **getter first** (`getName`/`setName`); list/aggregated `addXxx`/`getXxxs` or
  `createXxx`/`getXxxs` → **mutator first** (`createOperation`/`getOperations`). The
  "getter first" rule applies only to the scalar shape.
- Page-split tables: displayed order is the concatenation of per-page row groups. A
  class rendered in >1 PDF: verify the order agrees across renderings. A polymorphic
  family can span PDFs — each subtype cites its **own** table.

---

## Rule 0002 — Method Parity Checklist *(formerly Rule 2)*

A comment block at the top of the class lists every method with five columns:
`impl`, `docstring`, `test`, `reader`, `writer`. Each must be `[x]`. The first line after
the checklist title cites the spec table, then the version marker:

```
# ClassName method parity checklist:
# Spec: AUTOSAR_CP_TPS_<Template>.pdf, Table X.Y, p.NN
# Spec verified: R<YY>-<MM>
# Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
# [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
# [x] createFoo    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
# [x] getFoos      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
# [x] setBar       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
# [x] getBar       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
```

- **`reader [x]` on the mutator row** (`setXxx`/`addXxx`/`createXxx`) — the reader's
  `readXxx` populates the model via that method. **`writer [x]` on the getter row**
  (`getXxx`/`getXxxs`) — the writer's `writeXxx` reads via that method. **`[—]`** (N/A)
  for members with no XML element: `__init__`, `atpDerived` attributes, read-only
  convenience properties. The split matches how coverage is verified (grep the reader
  for the mutator call, the writer for the getter call) and closes the Rule 0001.7
  blind spot.
- The checklist covers every method 1:1 (no missing/extra); a `@property` counts as a
  method (needs a row + test). A commented-out member block is dead code — remove it.
- Every row fully `[x]` (impl **and** docstring **and** test **and** reader/writer as
  applicable); a `[ ]` whose obligation is actually done is stale — cross it. A row is
  `[x]` only when all obligations are complete and verified.
- Rows in **source order** matching the methods (Rule 0011).
- The `# Spec:` line names the correct PDF/table/page — the **PDF name, Table ID, and
  page number come from the PDF file directly** (`autosar/pdf/AUTOSAR_CP_TPS_*.pdf`); the
  markdown (`autosar/markdown/...`) carries no page numbers. Cite the header-row page
  (where `Class <Name>` first appears), in format `Table X.Y, p.NN`. A class rendered in >1 PDF
  cites the PDF its sibling family uses. For the enum attribute type, cite the PDF that
  renders the enum's own `Enumeration` table (independent of the class's PDF).
- **Exception — no own spec table:** a class whose attributes are XSD-only (e.g. a
  concrete `<name>InstanceRef`) carries **no** `# Spec:` line, **no** `# Spec verified:`
  marker, and every row stays `[ ]` (a provenance statement, not "not done"). An
  empty-attribute-rendering class (own table, all attrs inherited) is **not** this
  exception — it has the line, the marker, and `[x]` rows for the methods it defines.
- **Field-to-spec cross-check (both directions):** walk each model field → spec (catches
  fabricated fields) **and** each spec attr → code (catches missing). A tracker built
  only spec→code is not evidence of completeness. Strip suffixes, search the `Attribute`
  column + `Aggregated by` rows; if not found, grep the XSD (keep if present with docs,
  else remove).
- The checklist is method-only — it cannot detect fabricated attributes; the field-to-spec
  cross-check is the gate.

---

## Rule 0003 — Type Hints *(formerly Rule 3)*

Python 3.8-compatible: `Optional[T]` / `List[T]` / `Dict[K,V]` from `typing` — **never**
`T | None`, `list[…]`, `dict[…]` (runtime errors on 3.8–3.9) unless
`from __future__ import annotations`.

| kind | signature |
|---|---|
| list getter | `def getFoos(self) -> List[Foo]:` |
| single getter | `def getFoo(self) -> Optional[Foo]:` |
| setter | `def setFoo(self, value: Optional[Foo]) -> "ClassName":` |
| add | `def addFoo(self, value: Optional[Foo]) -> "ClassName":` |
| create | `def createFoo(self, short_name: str) -> Foo:` |

- Getters for collections return `List[T]`; getters that may return `None` return
  `Optional[T]`. Setters/adds declare `value` and return `"ClassName"`. Factories accept
  `short_name: str` and return the concrete type. `Optional`/`List` imported from
  `typing`. `__init__` fields annotated, matching getter/setter type.
- **No untyped accessors** — every getter return and setter parameter carries the
  concrete type even if the field is annotated.
- A `None`-defaulted `0..1` field is annotated `Optional[T]`, never bare `T = None`.
- **No looser-union coercion setters** — `value` is exactly the field type, never
  `Optional[Union[String, str]]` with an `isinstance` branch (dead convenience API that
  breaks the Rule 0004 None no-op). Callers construct typed primitives
  (`CseCodeType().setValue("100")`).

---

## Rule 0004 — Getter / Setter Behavior *(formerly Rule 4)*

- Setters return `self` (chaining). Setters/adds are **no-ops on `None`** — they must
  not overwrite or append `None` (parser helpers return `None` for missing elements).
  Validation setters run only for non-`None`. Getters return the field directly.
- `createXxx` returns the existing element when the short name already exists (no
  duplicate creation), else appends. In an `Identifiable` aggregator the check uses the
  `elements` registry (`IsElementExists`/`getElement`); in a plain `ARObject` aggregator
  it scans the owning field list. Exposing `createXxx` forces the child to be
  constructible as `Child(self, short_name)`.
- `createXxx` only for `Referrable`/`Identifiable` children; others use `setXxx`/`addXxx`.
- **A spec-`*` aggregated attribute on an `Identifiable` aggregator is backed by a
  dedicated typed list field, not by filtering the `elements` registry.** Each spec `*`
  `aggr` row maps to its own field (`self.operations: List[ClientServerOperation] = []`),
  declared in `__init__` in spec row order with the spec `Note` as comment. `createXxx`
  appends to it **in addition to** `addElement`; `getXxxs()` returns the field **directly
  — never** `list(filter(isinstance, elements))`. Filtering the registry gives the
  attribute no model field (Rule 0001.3 fails) and discriminates by Python type rather
  than spec role. Established pattern: `ParameterInterface.parameters`,
  `ClientServerInterface.operations`/`possibleErrors`. The registry keeps the
  duplicate-detection job; only the getter reads the field.
- **An `Identifiable` aggregator that handles members *only* via the `elements` registry
  is a to-fix, not an accepted shape.** Tell-tale: a getter
  `list(filter(isinstance, elements))` (or `sorted(filter(...))`) for a spec `*` `aggr`
  attribute with no dedicated field. It survives a fully-`[x]` checklist and a passing
  round-trip — so do not treat those as evidence. Migrate per attribute: add the
  dedicated typed list field; make `createXxx` append after `addElement`; rewrite
  `getXxxs()` to `return self.<field>`; assert the `[]` default in the test. The
  reader/writer need no change. `ClientServerInterface` is the worked example; a
  fully-`[x]` sibling still in the old shape (e.g. `NvDataInterface.getNvDatas`) is a
  deviation to reconcile, not a pattern to copy.

### Rule 0004.1 — Abstract base + concrete subclass uniformity

Every setter across a base + subclass hierarchy guards with `if value is not None:`.
A `@property` setter is a setter too and must guard.

---

## Rule 0005 — Formatting *(formerly Rule 6)*

- All imports at the top (module docstring, then `from __future__`, then imports, then
  code — PEP 8 E402). No mid-file imports to work around cycles; break cycles with
  `TYPE_CHECKING` + `from __future__ import annotations` for annotations, or a
  function-local import for runtime instantiation. `from __future__ import annotations`
  also resolves intra-module forward references (a class annotated with a type declared
  later in the same module).
- A blank line separates each attribute block (comment + assignment) in `__init__`.
- Black `line-length = 200` (`pyproject.toml`, `npm run black-check`); the 79-char limit
  is obsolete.
- No trailing whitespace (`W291`/`W293`), at most one blank line between definitions
  (`E303`). Two linters: `npm run flake8` (CI, syntax-only `E9/F63/F7/F82`) and
  `npm run ruff-check` (broader `E/F/W/I` from `pyproject.toml` `[tool.ruff]`, ignoring
  only `E501`) — ruff **enforces** `W291`/`W293`/`E303` and unused-import `F401` that
  flake8 leaves as warnings, so new/edited code must pass both `npm run ruff-check` and
  `npm run black-check`.
- No comments unless they carry spec information.

---

## Rule 0006 — Tests *(formerly Rule 7)*

Every method has coverage in the mirrored test file. TDD: **write the test first (Red),
then implement (Green)** — for the model (Step 2→3) and for the reader/writer (Step 5→6).

**Test placement & naming** — the Red test for each phase lives in a different folder:

| Phase | Folder | File ↔ test class |
|---|---|---|
| model (Step 2) | `tests/test_armodel/models/M2/AUTOSARTemplates/<package>/` | `test_<ClassName>.py` → `class Test<ClassName>`, pairs 1:1 with source `<ClassName>.py` |
| parser (Step 5) | `tests/test_armodel/parser/` | `test_*.py` → `class Test*`, organized by feature/handler (load with `ARXMLParser`, assert model fields) |
| writer (Step 5) | `tests/test_armodel/writer/` | `test_*.py` → `class Test*`, organized by feature (set → save → reload round-trip) |

- `test_initialization` asserts all `__init__` field defaults (`None`/`[]`).
- Abstract classes: test `__init__` defaults + base accessors through a concrete subclass
  (`test_<name>_base_properties`: exercise every base getter/setter, assert chaining +
  round-trip, finish with None no-op for the whole set).
- Getter/setter pairs: combined `test_get_set_*` — (1) setter returns `self`, (2) value
  round-trips, (3) `setXxx(None)` is a no-op.
- Construct typed primitives (`CseCodeType().setValue("100")`), never bare `str`/`int`.
  For **numericals** pass the value as a **string** (`PositiveInteger().setValue("4")`)
  so the writer serializes `_text`; read back with `getValue() == 4`. To set an enum
  attribute, construct an instance (`MyEnum().setValue(MyEnum.MEMBER)`), never pass the
  bare member.
- `add*`: appending, return value, None no-op. `create*`: short name + appended +
  duplicate returns existing. Plain getters: default-value test.
- When a class gains reader/writer support, run the full **round-trip** (set → save →
  reload → assert) end-to-end — the write path also serializes inherited base fields,
  and base deviations surface only here. Assert **field values**, not just
  `len(...) == n` / `getXxx() is not None` (a lossy empty-element round-trip passes
  those), including aggregated children one level down.
- A wrapper-element list needs an **empty-list** round-trip case: assert the serialized
  file has **no** wrapper tag and re-parsing yields `[]`, paired with `None`-valued
  optional attributes.

**Verification (run in repo root; replace paths):**

```bash
python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py -q
# Step 5 reader/writer tests live in their own folders — run the files you touched:
#   tests/test_armodel/parser/test_<feature>.py   and   tests/test_armodel/writer/test_writer_<feature>.py
python -m pytest tests/test_armodel/parser/ tests/test_armodel/writer/ -q
PATH=".venv/Scripts:$PATH" flake8 --exclude=.venv,build --select=E9,F63,F7,F82 \
  src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py
PATH=".venv/Scripts:$PATH" ruff check \
  src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py
npm run ruff-check && npm run black-check
```

Set-based checklist vs. methods check (adapt paths + `CLASS_NAME`):

```python
import re, ast
CLASS_NAME = "ClassName"
SRC = "src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py"
TEST_SRC = "tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py"
src = open(SRC, encoding="utf-8").read(); test_src = open(TEST_SRC, encoding="utf-8").read()
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
if "# Spec:" in src and "not yet implemented" not in src and "carried as a" not in src:
    assert re.search(r"# Spec verified: R\d\d-\d\d", src), "missing # Spec verified marker"
```

---

## Rule 0007 — Package Location *(formerly Rule 8)*

The class is defined in the module matching its spec `Package` row (`M2::…::Pkg` →
`…/Pkg.py` or `…/Pkg/__init__.py`).

- All classes in a spec package live in that single module. Prefer defining classes
  directly in `__init__.py`; split into per-class submodules only when the package is
  large, and never name a submodule after the class.
- **Package-name match anti-pattern:** when the package tail (`SomeGroup`) differs from
  the class (`ClassName`), do not nest it as `SomeGroup/ClassName.py` (implies package
  `…::SomeGroup::ClassName`). The class is a direct member of `SomeGroup/__init__.py`.
  Element-type packages whose tail **is** the class (`BswImplementation` →
  `BswImplementation.py`) are the correct aligned case, not the anti-pattern.
- Classes sharing a parent package tail are all direct members of that `__init__.py`
  (consolidate placeholder submodule families into the package `__init__.py`); break
  resulting cycles with `from __future__ import annotations` + `TYPE_CHECKING`.
- **Shadowing:** if `X.py` and a directory `X/` both exist, the file wins and classes in
  `X/*.py` are dead code — migrate them to `X.py` (or make `X/` a real package) and
  update `KNOWN_NAME_COLLISION_CLASSES` in `tests/test_armodel/test_model_imports.py`.
  A `KNOWN_NAME_COLLISION_CLASSES` entry is a live signal of possible shadowing.
- Import statements match the location: consumers import from the defining package, never
  from a class-named submodule. Latent broken imports surface when an aggregator first
  imports a sibling subpackage — run the full import + test suite after cross-package
  imports.
- **Top-level export chain:** an aligned class must be importable as `armodel.<ClassName>`
  (`hasattr(armodel, "<ClassName>")`); add the package's `import *` to
  `models/__init__.py` and remove it from `INTENTIONALLY_UNEXPORTED_MODULES`. A name
  colliding at top level goes into `KNOWN_NAME_COLLISION_CLASSES`.

---

## Rule 0008 — Attribute Spacing *(formerly Rule 9)*

Each member is separated by exactly one blank line.

- Every `__init__` attribute has a blank line before/after its comment + assignment block.
  **Manual-only** — Black leaves contiguous `# comment / self.field = …` blocks
  untouched; ruff's `E303` caps the *maximum* blank lines but enforces no *minimum*, so a
  class can pass `black-check`, `npm run ruff-check`, `flake8`, the set-based checklist,
  and all tests while its fields are glued together. Verify by eye or a small AST audit.
- Every enum literal block separated by one blank line. Every method preceded/followed by
  a blank line (except the first after `__init__`). No consecutive blank lines.

---

## Rule 0009 — Method Signatures *(formerly Rule 10)*

Each method definition and all its parameters fit on the same logical line; Black
collapses a signature that fits within 200 chars, so do not hand-break one that fits.

- `def` starts the signature; all parameters in parentheses; return annotation via `->`
  on the same logical line; body starts on a new line after `:`. `npm run black-check`
  passes. A trailing "magic comma" forces the exploded form — keep it only when the
  signature genuinely exceeds 200 chars.

---

## Rule 0010 — Enums Inherit `AREnum` *(formerly Rule 11)*

Every enum inherits `AREnum` (not `Enum`, `str`+`Enum`, `IntEnum`, …), imported from
`…GenericStructure.GeneralTemplateClasses.PrimitiveTypes`. The body has members with
string values (`MEMBER = "member_value"`).

---

## Rule 0011 — Enum Specification Alignment *(formerly Rule 12)*

- Locate the enum's spec `Enumeration` table; members 1:1 with the `Literal` rows — no
  extra, no missing. Placeholder shapes keep the right count with wrong values (hyphenated
  `full-communication` for spec `full`, paraphrased names) — verify each value against the
  `Literal` column (`mmt.qualifiedName`) and the name against the literal's UPPER_CASE.
- Member name: spec literal → UPPER_CASE (`derivedFrom` → `DERIVED_FROM`). Member value:
  **exactly** the spec literal (`DERIVED_FROM = "derivedFrom"`).
- **Member value vs XML form:** the member value is the camelCase `mmt.qualifiedName`
  (`DependencyUsageEnum.BUILD = "build"`); the **XSD** serializes enum literals in
  **UPPERCASE**. Keep the member matching the spec; write UPPERCASE only in test XML
  fixtures/XSD-valid fragments.
- Class docstring: the spec `Note` **verbatim** (do not paraphrase). Each member has an
  inline comment citing the literal's description + Tags (`atp.EnumerationLiteralIndex=N`).
- Tests reference members like `MyEnum.MEMBER_NAME` for reading; to **set** an enum
  attribute construct `MyEnum().setValue(MyEnum.MEMBER_NAME)`; assert round-tripped values
  with `.getValue() == "memberName"` (the parser returns a generic `ARLiteral`). An
  aligned enum defines `__init__(self)` passing the tuple to `AREnum`, so `MyEnum()` is
  instantiable.

---

## Rule 0012 — Docstring & Comment Sync *(formerly Rule 13)*

Class docstrings, inline `__init__` comments, and getter/setter docstrings copy the PDF
`Note` **verbatim** — never summarize, paraphrase, or rephrase the wording — and stay
synced across AUTOSAR upgrades. This is one ordered procedure per class (Rule 0006's
mechanical check only confirms the marker *string* exists, not that content is correct).

### 0012.1 Versioning

- The checklist includes `# Spec verified: R<YY>-<MM>` immediately after the `# Spec:`
  line (`R23-11` = Nov 2023). Verify during every alignment pass.
- **The marker certifies all spec info, including member types** — do not claim it while a
  member is a placeholder. When a Rule 0001.10 placeholder remains, **keep the `# Spec:`
  line but omit the stamp**; the affected rows stay `[ ]`. The stamp flips back on once
  the real type lands. (Rule 0006's `assert` allows a `# Spec:` line with no stamp when a
  placeholder comment is present.)
- **Exception — no own spec table:** a class with XSD-only attributes carries no marker
  and all-`[ ]` rows. An empty-attribute-rendering class (own table, attrs inherited) is
  **not** this exception — it gets the marker and `[x]` rows.

### 0012.2 Per-class sync procedure (run in order)

0. **Exception gate:** XSD-only class (no own table)? Stop — no `# Spec:`, no marker,
   `[ ]` rows; record in the tracker. Otherwise continue.
1. Locate the spec table + page (`grep "Table N.M: <ClassName>" autosar/markdown/*.md`;
   confirm the page in the PDF via `pypdf`, matching the printed footer).
2. Add the version marker.
3. **Class docstring** = the PDF `Note` **verbatim** (no invented recap prose, no `Base`
   chain summary); append class-level `constr_*` rows (including ones targeting inherited
   attributes). For a terse citation Note, append the XSD complexType doc as an
   elaboration (also verbatim).
4. **Per-attribute loop** (all five, per attribute, before the next):
   1. Referenced type must exist and be aligned before typing (Rule 0010/0011); its
      `# Spec:` cites its **own** table, independent of the owning class.
   2. Inline `__init__` comment: the attribute's `Note` semantic sentence verbatim
      (drop `Stereotypes:`/`Tags:` tail); append any `constr_*` wording + id.
   3. Getter docstring: the PDF `Note` **verbatim** + constraint — never summarize or
      rephrase into "Gets the value of X"; for an `iref`, name the concrete
      `<name>InstanceRef` class.
   4. Setter docstring: the PDF `Note` **verbatim** (same wording as the getter) +
      constraint; the chainable-return and (if guarded) None-no-op lines are **added
      code-behavior notes, not Note content** — append them without altering the Note
      text: *"A None value is a no-op and does not overwrite an existing `<attr>`."*
   5. Cross-check comment/getter/setter for consistency.
5. Verify by **diff**, not status — no mechanical check proves wording matches the PDF;
   re-open the Note/XSD doc and diff against the comment and both docstrings.

### 0012.3 Drift on upgrade

An AUTOSAR upgrade is the identical per-member walk diffed against the new PDF; update
the marker, run tests, commit with the spec notes.

---

## Rule 0013 — Reader / Writer Source Style *(formerly Rule 14)*

The reader/writer must not use chained `set`/`create`/`add` calls — each is its own
statement on the receiver. Setters return `self` for consumer convenience; the
reader/writer source does not exploit it.

- No statement chains two+ `set`/`create`/`add` on one receiver (`obj.setA(x).setB(y)`),
  including a multi-line chain that continues after a closing paren. A chain beginning
  with a factory (`AUTOSAR.getInstance().addXxx(...)`) is split by binding the shared
  object to a local first (`document = AUTOSAR.getInstance(); document.addXxx(...)`).
- Getter/attribute chains **used as values** (`ref.getDest()`,
  `event.getPeriod().getValue()`) are read-only sub-expressions — left as-is.

### 0013.1 Reader helpers mirror the model inheritance chain

A `readXxx` helper models the class's own attribute level and calls the reader helper
of its **direct model base** — it never re-reads an ancestor from outside:

- `readIdentifiable` → `readMultilanguageReferrable` → `readReferrable` →
  `readARObjectAttributes` (T/UUID + `addARObject`).
- `readImplementationProps` → `readReferrable` + the `SYMBOL` element
  (`ImplementationProps` is a direct child of `Referrable`, so its helper owns the
  `readReferrable` call).
- A concrete subclass reads only one level: `readExecutableEntityActivationReason`
  calls `readImplementationProps` (which handles `readReferrable`) plus its own element
  (`BIT-POSITION`) — never `readReferrable` again.

Calling `readReferrable` both in a base helper **and** in the subclass **double-registers**
the object: `readARObjectAttributes` → `AUTOSAR.getInstance().addARObject` →
`UUIDMgr.addObject` appends to `uuid_object_mappings[uuid]` with no dedupe, so duplicate
entries surface in `getObjects`/`getDuplicateUUIDs`. Fix = remove the explicit
`readReferrable` from the subclass call site (worked example: `readSymbolicNameProps` and
`readExecutableEntityActivationReason` each dropped their redundant call once
`readImplementationProps` gained it).

The writer keeps the same leveling (`writeImplementationProps` calls `writeReferrable` at
its own level) — the reader and writer must stay symmetric. A shared base reader helper's
existence is not evidence a given subclass calls it; grep each subclass:

```bash
grep -nE '(readReferrable|readImplementationProps|readIdentifiable)\([^)]*\)' src/armodel/parser/arxml_parser.py
```

Verify (must return nothing):

```bash
grep -nE '(^|[^.a-zA-Z_])([a-zA-Z_][a-zA-Z0-9_]*)\.(set|create|add)[A-Z][a-zA-Z0-9_]*\([^)]*\)\.(set|create|add)' \
    src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py
grep -nE 'AUTOSAR\.getInstance\(\)\.' \
    src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py
```

After any reader/writer edit, run `npm run ruff-check`, `npm run black-check`, and the
full suite; the round-trip must remain lossless for every integration fixture.

---

## Rule 0014 — Deviation Tracking *(conventions from the project deviation tracker)*

Intentional spec/code deviations are recorded per class in the project's deviation
tracker. Each class entry has a header and a deviation table:

```
## `ClassName`
- **PDF:** `AUTOSAR_CP_TPS_<Template>.pdf`  | **page:** NN
- **Package:** `M2::AUTOSARTemplates::…`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/…/<ClassName>.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `<field>` | `<PyType>` | `<specMember>` | `<PDFType>` | `<kind>` | `<reason>` |
| — *(missing)* | `—` | `<specMember>` | `<PDFType>` | — | missing |
```

- The PDF `Kind` suffix (`Ref`/`TRef`/`IRef`/`Refs`) is appended to the member name and
  is recognized in matching (spec `type` kind `TRef` → implemented by `typeTRef`).
  `variationPoint`/`shortLabel` are excluded as framework-level.
- **Reason codes** (use precisely):
  - `missing` — spec attr has no code (but first check Rule 0001.10: a referenced class
    may need implementing first).
  - `type (spec many vs py single)` / `type (spec one vs py list)` — multiplicity
    mismatch. **To-fix**, not accepted: convert to the list/single shape and **remove**
    the row.
  - `type (PDF <X> vs py <Y>; parser <helper> produces <Y>)` — type deviation; only when
    the XML form forces it. Otherwise upgrade the parser/writer to the spec type (Rule
    0001.3) and clear the row.
  - `naming` — base-name mismatch. **To-fix**: rename and **remove** the row.
  - `atpDerived`, `deprecated (atp.Status=removed), not implemented`,
    `present in XSD, absent from PDF table rendering; kept …`,
    `removed upstream: …; not modeled`, `added convenience property`.
- **Stale rows are removed, not left:** a `naming`/`type`/`missing` row for a member that
  is now correctly implemented is removed in the same pass. A surviving such row means
  the field-to-spec cross-check has not actually been done.
- A class with no deviations records `No deviations — …` with a one-line summary.
- **The `# Spec verified:` stamp (Rule 0012.1) is not set while any non-`atpDerived`/
  non-`convenience` deviation remains unresolved.**
