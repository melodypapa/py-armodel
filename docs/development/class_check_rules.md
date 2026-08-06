# AUTOSAR Model Class Check Rules

This document defines the mandatory check rules for verifying **any** AUTOSAR
model class before it is considered complete. The rules apply uniformly to
every class under `src/armodel/models/M2/AUTOSARTemplates/` that is derived
from an AUTOSAR PDF specification table.

Throughout this document, `ClassName` denotes the class under check, with:

- source file: `src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py`
  (or `<package>/<ClassName>/__init__.py` for package-style modules)
- mirrored test file: `tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py`
- spec table: the class's attribute table in the corresponding AUTOSAR PDF
  (markdown sources under `autosar/markdown/`, XSD under
  `autosar-pdf/examples/xsd/`)

The rules are grouped into themed sections. Each rule keeps its original
number for traceability across docs/tooling that may cite it (e.g.
`docs/method_deviation_by_class.md`).

**How to use this document:**

1. Pick a class (`ClassName`) and locate its source, mirrored test file, and
   PDF spec table.
2. Work through every section below, ticking each check box. Fix the class,
   its checklist, comments, type hints, tests, spacing, method signatures,
   enum types, and enum specifications as needed.
3. If a rule does not fit the class cleanly, or you encounter something the
   rules do not cover, update this document so it stays accurate for future
   classes — record the generalization directly in the relevant rule, not as
   a standalone anecdote.
4. Run the Rule 7 verification commands and the set-based script (Rule 2/7)
   before declaring the class complete.

**No separate planning phase:** a request of the form "update `ClassName`
(or a rule) following this document, collect the change feedback, and update
this document to make the rule more general" is executed directly — this
document **is** the plan. Do not brainstorm or write a separate plan
document first; go straight to step 1 above.

---

# Section 1: Spec Alignment (Rules 1, 11, 12)

## Rule 1: Spec Alignment

**Maturity**: accept

The class must reflect the AUTOSAR PDF specification for its attributes.

### 1.1 Attribute existence and kind of element

- [ ] Every attribute in the class exists in the class's spec table (find the
       table by searching the AUTOSAR PDF markdown for the class name).
- [ ] The class is the right kind of element: when the spec table header is
       `Class` and its `Attribute` column has rows, the Python class must be a
       model class with fields/accessors — **not** an enum. Enums correspond to
       spec tables headed `Enumeration` with `Literal` rows only. (A class
       mistakenly modeled as an `AREnum` with a handful of ad-hoc members that
       appear nowhere in its spec table is a Rule 1 violation; the spec table
       defines it as a class with real attributes instead.) **This occurs when a
       placeholder enum implementation from an earlier development stage is not
       synchronized with the spec table it should represent. Always verify the
       spec table structure (Class vs. Enumeration header) before assuming the
       current implementation is correct.**
- [ ] Distinguishing enums from classes: check the table header **and** column
       structure, not the package name or domain assumptions.
       1. Header `Enumeration` + `Literal` column → enum → use `AREnum` with
          members.
       2. Header `Class` + `Attribute`/`Type`/`Mult`/`Kind`/`Note` columns →
          regular class → use `ARObject` (or its appropriate base) with
          field/accessor pairs.
       3. The `Base` column alone does **not** determine enum vs. class — a
          class whose `Base` is just `ARObject` can still be a class, not an
          enum, if the table shows attribute columns.
       Searching the PDF for "Enumeration" + the class name finds enums
       quickly; searching for "Table" + the class name finds class tables.
       Cross-reference both.

### 1.2 Base class and inheritance chain

- [ ] Base-class alignment: the spec table's `Base` column determines the
      Python base class and therefore the constructor signature. When `Base`
      lists `Referrable` (or `Identifiable`, which extends `Referrable`) the
      Python class must inherit from `Referrable`/`Identifiable` and its
      constructor must take `(self, parent, short_name)` — a class whose spec
      `Base` is `ARObject, Referrable` but which inherits only from `ARObject`
      and defines `__init__(self)` is misaligned. The `Base` column may also
      name a concrete abstract base the class must inherit rather than plain
      `ARObject` (e.g. an instance-reference class whose `Base` is
      `ARObject, AtpInstanceRef` must inherit `AtpInstanceRef`, matching its
      sibling instance-ref classes). The `Base` column also drives the
      `createXXX` vs `setXXX` choice (see 1.6 below).
- [ ] Classes that inherit only from `ARObject` (no `Referrable`/`Identifiable`
      in `Base`) take no `parent`/`short_name` parameters: `__init__(self)`
      with all fields defaulted to `None`/`[]`. Check the spec `Base` column
      before assuming a class needs a short name.
- [ ] The `Base` column usually lists the *entire* inheritance chain, ending in
      the model classes the class belongs to (e.g. `ARObject, AbstractFoo,
      ConcreteFoo, MidLevelFoo, Identifiable, MultilanguageReferrable,
      Referrable`). The class must inherit the **most-derived** model class in
      that chain as its direct parent — never a more general ancestor. When
      the `Base` column lists a sibling/mid-hierarchy model class (an abstract
      base shared by several concrete classes), choose it over the ancestor
      it extends, matching the direct parent used by its siblings. The
      auto-generated `reports/deviation_class_hierarchy_mismatches.md` flags
      this kind of parent mismatch for review.
- [ ] The PDF spec is the source of truth for multiplicity and base class.
      When the XSD disagrees with the PDF, follow the PDF.

### 1.3 Attribute-level completeness

- [ ] Deprecated attributes that the PDF has replaced are **not** added. An attribute
       that is absent from the PDF `Attribute` column but present in the XSD with an
       `atp.Status="removed"` tag (e.g. `BswImplementation.debugInfo`) is
       deprecated/removed: it maps to **no** field, and the deviation tracker row
       records the reason `"deprecated (atp.Status=removed), not implemented"`
       instead of a bare `"missing"`. This is distinct from the `atpDerived`
       exception in Rule 1.7 — `atp.Status="removed"` means the attribute was
       deleted upstream (do **not** model it), whereas `atpDerived` means the
       attribute is derived in the model (model it with a field, no XML element).
       To tell them apart, inspect the XSD element's appinfo tags for
       `atp.Status="removed"` vs the `atpDerived` stereotype.
- [ ] **The PDF is the source of truth for the attribute type.** When the
      parser/writer use a looser type than the PDF, do **not** accept the
      loose type and record a deviation — first upgrade the parser and writer
      to the spec-typed helper so the model carries the PDF type. Example:
      `MemorySection.size` is a PDF `PositiveInteger` and the XSD element
      `SIZE` is `AR:POSITIVE-INTEGER`, so the parser must use
      `getChildElementOptionalPositiveInteger` (not the generic
      `getChildElementOptionalNumericalValue`), the writer
      `setChildElementOptionalPositiveInteger`, and the
      field/getter/setter are typed `Optional[PositiveInteger]` — no
      deviation at all. Only when the XML representation genuinely forces a
      different model type (e.g. a PDF enum type that is not modeled, so the
      element is carried as `String`) is a type deviation recorded, with the
      reason naming the forced difference. Changing a type requires
      coordinated parser and writer changes.
- [ ] **No untyped accessor pairs.** A `getXxx`/`setXxx` pair with no
      annotations at all (`def getSize(self):` / `def setSize(self, value):`)
      is a Rule 3 violation even if the field is annotated — every getter
      return and every setter parameter must carry the concrete type (e.g.
      `getSize() -> Optional[PositiveInteger]`,
      `setSize(value: Optional[PositiveInteger])`).
- [ ] Field annotation, getter return, setter parameter, parser, and writer
      must all agree on the same type. A field annotated differently from its
      own accessors is an internal inconsistency, not a clean deviation —
      align the field and accessors to the parser's actual type and record
      the PDF-vs-parser deviation separately.
- [ ] Every spec attribute must map to a field **plus** an accessor pair. The
      method parity checklist (Rule 2) only tracks methods, so a class can be
      checklist-complete while still missing accessors — a field without a
      getter/setter is a gap.
- [ ] No fabricated attributes: the reverse of attribute-level completeness —
      every field in the class must trace back to a spec attribute. A class
      can be checklist-complete (every method `[x] impl/docstring/test`) yet
      carry a field with a full accessor pair that appears **nowhere** in the
      spec table. Such a field is fabricated and must be **removed**, not
      merely recorded as a deviation — a deviation records an intentional
      spec/code gap, not invented API. The method parity checklist cannot
      detect this on its own because it only verifies that listed methods
      exist; it does not verify that each field maps to the spec.
      Cross-check the `__init__` field list against the spec `Attribute` rows
      and account for every field.
- [ ] **PDF-table omission vs. fabricated API.** An attribute that is absent
      from the class's PDF `Attribute` column but **present in the XSD with a
      real documentation block** (no `atp.Status="removed"`) is *not*
      fabricated — it is a rendering gap in the PDF table (e.g.
      `MemorySection.memClassSymbol`, present as `MEM-CLASS-SYMBOL` in the XSD
      but missing from Table 8.2's attribute rendering). It is **kept** with
      its accessor pair and parser/writer coverage, and recorded in the
      deviation tracker as `"present in XSD, absent from PDF table
      rendering; kept with parser/writer coverage"` — never deleted just
      because the table omits it. A class whose **whole table is a partial
      rendering** is handled identically: `McDataInstance`'s PDF Table 9.4
      lists only 4 of its 12 attributes (`role`, `rptImplPolicy`,
      `subElement`, `symbol`); the other 8 (`arraySize`,
      `displayIdentifier`, `flatMapEntryRef`, `instanceInMemory`,
      `mcDataAccessDetails`, `mcDataAssignment`, `resultingProperties`,
      `resultingRptSwPrototypingAccess`) come from the XSD `MC-DATA-INSTANCE`
      group and are implemented with the same field + accessor + parser/writer
      obligations, following the XSD attribute order when the partial PDF rows
      give no order. The *fabricated* case remains: a field with
      **no spec basis anywhere** (not in the PDF, not in the XSD) is removed.
      Before deciding, grep the XSD for the element tag: presence with
      documentation ⇒ omission (keep, record); absence everywhere ⇒ invented
      API (remove).
- [ ] **Cross-table aggregation.** A class may aggregate attributes whose
      definition lives in **another class's spec table**, discoverable via
      that table's `Aggregated by` row (e.g. `ResourceConsumption`'s Table
      8.1 lists five attributes, but `accessCountSet` — defined in the
      `AccessCountSet` table 4.22 whose `Aggregated by` row reads
      `ResourceConsumption.accessCountSet` — still belongs to
      `ResourceConsumption`). These attributes are spec attributes of the
      aggregator exactly like its own table rows: same field + accessor
      requirements, same parser/writer coverage, same `# Spec:` citation of
      the class's **own** table (the referenced table is named in a
      deviation-tracker note, not in the class checklist).
- [ ] **Exception — read-only derived convenience properties.** A `@property`
      computed from a spec attribute, with no backing field of its own and no
      setter (e.g. a millisecond value derived from a spec `TimeValue`), is
      **not** fabricated API and is **kept**, provided it (a) gets a
      method-parity checklist row like any other member, (b) is tested, and
      (c) is recorded in the deviation tracker as an "added convenience
      property" (mirrors the `atpDerived` handling: derived, no XML element,
      no parser/writer coverage). Do **not** delete a convenience property
      that real consumers (CLI, parser tests) rely on just because it is
      absent from the spec table — removing it is a breaking change;
      recording it is the aligned action.

### 1.4 Multiplicity

- [ ] Multiplicity maps to the Python representation: `*` → `List[T]` (default
      `[]`), `0..1` → optional single `T` (default `None`). A spec-`*`
      attribute held as a single value is a deviation and must be fixed. The
      reverse is equally a deviation: a spec-`0..1` attribute held as a `List`.
- [ ] A **bounded ordered** multiplicity such as `0..2` (upper bound > 1 but
      not `*`) still maps to `List[T]` (default `[]`) with the usual
      `getXxxs`/`addXxx` accessors — the upper bound is not enforced in the
      model; order is preserved by insertion order in `addXxx`.
- [ ] A spec-`*` member whose *name is singular* still maps to a **plural**
      Python list field and plural accessors (`addXxx`/`getXxxs`): the spec
      column says `revisionLabel` but its multiplicity is `*`, so the field is
      `revisionLabels: List[RevisionLabelString] = []` with
      `addRevisionLabel()`/`getRevisionLabels()` — do **not** model a single
      `revisionLabel` value or a singular `setRevisionLabel` setter. The
      per-item element name (e.g. `REVISION-LABEL`) is the singular form; the
      pluralization lives only in Python naming.
- [ ] Getter/setter docstrings must match the chosen representation — "list
      of ..." wording on a single ref (or vice versa) is a symptom of a
      multiplicity mismatch.

### 1.5 Naming

- [ ] Ref/TRef/IRef suffix naming: when the spec table's Kind column is `ref`,
      `tref`, or `iref`, include the corresponding suffix in the Python field
      and method names. The spec table Attribute column determines the base
      name, Kind determines the suffix: `ref` → `Ref`/`Refs`, `tref` → `TRef`,
      `iref` → `IRef`/`IRefs`. Example: Attribute `targetElement`, Kind `ref`
      → Python field `targetElementRef: RefType`, getter
      `getTargetElementRef()`. Attribute `disabledInContext`, Kind `iref` →
      Python field `disabledInContextIRefs:
      List[SomeContextInstanceRef]`, getter `getDisabledInContextIRefs()`.
      An `iref` Kind means the attribute is an instance reference — its
      element type is a `<name>InstanceRef` class, and the list type
      annotation is that class, **not** `RefType`.
- [ ] An `iref` attribute's element type is a concrete `<name>InstanceRef`
      class. When that class — or the abstract `<name>InstanceRef` parent
      listed in its `Base` column (e.g. `TriggerInAtomicSwcInstanceRef`) —
      does **not** exist in the codebase, **implement it first** per Rule 1.10
      instead of deferring: create the abstract parent and the concrete
      subclass from their own spec tables, mirroring the sibling
      `<name>InstanceRef` classes (same abstract parent, same
      base/context/target inner-attribute shape), and give them parser/writer
      coverage. Rule 1.10 applies to **every** referenced class, of which
      `<name>InstanceRef` types are one case. Only when the iref's model is
      genuinely out of scope is a `RefType` placeholder allowed; it must then
      forward-reference the not-yet-defined instance ref class in the inline
      comment and in the getter/setter docstrings, and be recorded in
      `docs/method_deviation_by_class.md` as "instance ref class not yet
      implemented". When the class is implemented, switch the field/getter/
      setter annotation to the concrete `<name>InstanceRef` type (with a
      `TYPE_CHECKING` import if needed to avoid cycles) and clear the
      deviation.
- [ ] Within a `<name>InstanceRef` class itself, its *inner* attributes are
      ordinary Kind `ref` rows (the sub-elements of the instance ref) and
      therefore map to `Optional[RefType]` with the plain `Ref` suffix — do
      **not** annotate them as the `<name>InstanceRef` class or hold object
      references. For a Kind `ref` inner attribute, the `Ref` suffix is
      appended to the *full* camelCase spec attribute name (e.g.
      `contextGroup` → `contextGroupRef`, `targetItem` → `targetItemRef`) —
      do not drop the suffix or collapse multi-word attribute names.
- [ ] The **base name** of an attribute field comes **verbatim** from the spec
      table's `Attribute` column; the Kind suffix is appended to that exact
      base, never to a paraphrased or semantically-equivalent rename. A
      plausible-sounding name is still a Rule 1 violation when it does not
      match the spec Attribute. The set-based checklist (Rule 2) cannot catch
      a wrong-but-consistent name: field, getter, setter, and checklist can
      all agree on a misnamed field, so the checklist alone is not sufficient
      — only the field-to-spec cross-check against the `Attribute` column
      catches this, and it applies to **every** field, not just missing/extra
      ones.
      An already-plural base keeps its plural form when the `Ref`/`Refs`
      suffix is appended: spec `measurableSystemConstantValues` (Kind `ref`, `*`)
      → field `measurableSystemConstantValuesRefs` with
      `addMeasurableSystemConstantValuesRef`/`getMeasurableSystemConstantValuesRefs` —
      the doubled trailing `s` is the correct suffix append, not a typo.

### 1.6 `createXXX` vs `setXXX`

- [ ] Choose `createXXX` vs `setXXX` from the aggregated child's spec `Base`:
      if the child type has a short name (its spec `Base` lists `Referrable`
      or `Identifiable`), expose a `createXXX(short_name)` factory. If the
      child is a plain non-Identifiable object with no short name (spec
      `Base` is only `ARObject`), expose a plain `setXXX` setter — do not
      invent a factory for a child that has no short name. The test is
      "does the child's `Base` include `Referrable`", not narrowly
      "is the child `Identifiable`" — a child whose `Base` is
      `ARObject, Referrable` (but not `Identifiable`) still carries a short
      name and still uses a `createXXX(short_name)` factory.
- [ ] The child's **multiplicity** selects the exact accessor shape for
      non-Identifiable children (`Base` is only `ARObject`):
      1. multiplicity `0..1` → `setXxx(value)` + `getXxx()` (the plain setter
         above);
      2. multiplicity `*` → the ordinary **list accessors** `addXxx(value)`
         (append the passed instance, `None` no-op per Rule 4) +
         `getXxxs()` — the exact same shape as a `*` `ref`/`attr` list (e.g.
         `AccessCountSet.addAccessCount(value)`, `addMemorySectionLocation`,
         `addAccessCountSet`). Do **not** invent a `createXxx(short_name)`
         factory (the child has no short name, so there is nothing to
         duplicate-check against) **and** do **not** invent a no-arg
         `createXxx()` factory that creates-and-appends internally: the
         parser instantiates the child itself and hands it to `addXxx`, so a
         no-arg factory duplicates what `addXxx` plus the parser's
         instantiation already does. The `createXXX(short_name)` factory —
         with its duplicate-by-short-name return behavior (Rule 4) — exists
         **only** for children whose `Base` lists `Referrable`/
         `Identifiable`.

### 1.7 Parser and writer coverage

- [ ] Every implemented attribute must be covered by **both** the parser and
      the writer. A spec attribute with a field and accessors but no parser
      or writer handling is silently dropped on round-trip.
      The method-parity checklist (Rule 2) is **blind to this**: it tracks only
      method existence, so a fully `[x]` checklist says nothing about whether
      the attribute is serialized. (e.g. `BswImplementation.preconfiguredConfiguration`
      had a complete field + accessor pair + `[x]` checklist rows yet no XML
      read/write at all.) Verify coverage separately by grepping the parser and
      writer for the XML element tag of every field — a field whose accessor
      methods are present and tested is *not* evidence that any code serializes it.
- [ ] This extends to **polymorphic dispatch**: a class that is a concrete
      subtype of an abstract base (event, entity, policy, etc.) may have a
      dedicated `readXxx`/`writeXxx` method yet still be silently dropped if
      the *dispatch* function (an `if isinstance(...)` / tag-name chain) has
      no branch for it — a `notImplemented(...)` fallback only logs. Adding a
      concrete subtype therefore touches **five** places:
      (a) the subtype class itself;
      (b) the aggregator that owns the instances — it must expose a
      `createXxx(short_name)` factory and a `getXxxs()` getter, and both rows
      must be added to the aggregator's method-parity checklist (without the
      factory, the parser's tag-name branch has nothing to instantiate);
      (c) the parser dispatch;
      (d) the writer dispatch; and
      (e) the parser **and** writer dispatch *tests* — the
      "dispatches all types"-style tests that assert every subtype is routed
      must gain the new subtype, otherwise a branch exists that no test
      exercises and a later refactor can silently break the dispatch without
      failing CI.
- [ ] A concrete `<name>InstanceRef` subclass is a polymorphic type like any
      other subtype: it needs a parser `readXxx`/`getXxxIRef` dispatch branch
      and a matching writer `writeXxx`/`setXxxIRef` branch, plus dispatch-test
      coverage — the five-place pattern above applies even though the iref is
      attribute-typed rather than aggregated. Inner attributes marked
      `Stereotypes: atpAbstract` in the abstract `<name>InstanceRef` parent are
      declared there but concretized by the subclasses (a differently-named,
      concretely-typed attribute, e.g. `contextPort` →
      `contextPPort`/`contextRPort`), so only the subclass's concrete attribute
      carries the XML element; `atpDerived` inner attributes (e.g. `base`)
      have no XML element and are exempt (see the exception below).
- [ ] **Typed vs polymorphic iref serialization shape.** When the spec/XSD
      types an iref attribute as a *fixed* concrete `<name>InstanceRef` class
      (the XSD element's `type` is that class, e.g.
      `SwcBswSynchronizedTrigger.swcTrigger` → `SWC-TRIGGER-IREF` of type
      `P-TRIGGER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF`), the attribute-named
      element *is* the iref: parser and writer read/write its inner refs
      **directly under** that element (flat), mirroring
      `setVariableInAtomicSWCTypeInstanceRef`. Do **not** emit a nested
      `<P-...-INSTANCE-REF>` wrapper element. That nested shape is only for
      *polymorphic* irefs — a choice of subtype elements such as
      `MODE-GROUP-IREF`'s `P-MODE-GROUP...`/`R-MODE-GROUP...`, which dispatch
      on the child tag. Mixing the two shapes silently drops the inner refs on
      round-trip, because the reader looks for inner refs directly under the
      iref element.
- [ ] **Exception:** an attribute marked `Stereotypes: atpDerived` is a
      *derived* attribute — it is computed from its context and has **no**
      XML element, so it has no parser/writer element and is exempt from this
      requirement. It still maps to a field + accessor pair (attribute-level
      completeness) and is recorded as `atpDerived` in the deviation tracker.
- [ ] **Wrapper-element lists.** When a spec-`*` attribute's items live inside
      a *wrapper* element (e.g. `revisionLabel` `*` → XML
      `<REVISION-LABELS><REVISION-LABEL>…</REVISION-LABEL></REVISION-LABELS>`),
      the wrapper is pure container with no model counterpart: the field is
      the flat list (`revisionLabels`) and there is **no** `revisionLabels`
      element attribute in `__init__` for the wrapper. Parser: iterate
      `self.findall(element, "REVISION-LABELS/REVISION-LABEL")` and build each
      item (via `getChildElementOptionalRevisionLabelString(child, ".")` or a
      literal-list helper), calling `addXxx` per item. Writer: create the
      wrapper `ET.SubElement(element, "REVISION-LABELS")` only when the list is
      non-empty, then emit each item as a child. Guard both sides so an empty
      list round-trips to **no** wrapper element at all. (Engineered in
      `EngineeringObject.revisionLabels`; the typed revision-label helper
      `getChildElementOptionalRevisionLabelString` validates the
      `[0-9]+\.[0-9]+\.[0-9]+…` format, so prefer it over a raw literal for
      `RevisionLabelString` items.) The same wrapper pattern applies when the
      item type is an **aggregated object**, not a literal: the wrapper is
      still a pure container with no model counterpart, but the per-item
      element tag is **XSD-driven and may be the aggregated type's element
      name, not the attribute singular** — e.g. `McSupportData.emulationSupport`
      `*` → `<EMULATION-SUPPORTS><MC-SW-EMULATION-METHOD-SUPPORT>…`, while
      `mcParameterInstance`/`mcVariableInstance` `*` → `<MC-PARAMETER-INSTANCES>`/
      `<MC-VARIABLE-INSTANCES>` wrappers each containing `<MC-DATA-INSTANCE>`
      (the type `McDataInstance`). A ref wrapper's item tag *is* the attribute
      base plus `-REF` (`MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS/MEASURABLE-SYSTEM-CONSTANT-VALUES-REF`).
      Read the item tag from the XSD `choice`/element declaration — do not
      derive it from the attribute name or the type name by rule of thumb.
      Parser: iterate `self.findall(element, "WRAPPER/ITEM")` and build each
      item object via the aggregator's `addXxx`/`createXxx`. Writer: create
      the wrapper only when the list is non-empty and emit one item element
      per entry. When an aggregated child is itself not yet aligned to its
      own spec table, still parse/emit the item element **by identity only**
      (the `SHORT-NAME` for `Identifiable` children; an empty element for
      plain `ARObject` children) rather than serializing placeholder fields —
      this keeps the XML schema-valid and the round-trip lossless at the
      aggregator level, and is recorded in the deviation tracker pending the
      child's own pass (e.g. `McSupportData`'s `McSwEmulationMethodSupport`
      and `RptSupportData` children).

### 1.8 Cross-package types

- [ ] When a field's type lives in a **different spec package** that imports
      back into the current module, import the type under `TYPE_CHECKING` and
      annotate fields/getters with a string forward reference (`"ClassName"`);
      the parser and writer may import it directly because they sit below the
      model classes in the import graph and cannot create a cycle.
- [ ] A spec enum that is the *attribute type* of classes in **more than one**
      spec package (a shared enum) is defined once in the lowest common
      package that both consumers can import without creating a cycle
      (typically `CommonStructure`), and each consuming template class
      imports it directly — no `TYPE_CHECKING` needed if that shared package
      sits below the consuming templates in the import graph. The `# Spec:`
      line names the table that *defines the enum*, which may be a different
      PDF page/table than the class that uses it.

### 1.9 Deviations

- [ ] Intentional deviations are recorded in `docs/method_deviation_by_class.md`
      with the reason (e.g. "PDF-only", "deprecated, not implemented",
      "atpDerived", "added convenience property").

### 1.10 Missing referenced classes must be implemented first

- [ ] The class under check may reference other model classes in its spec
      table: a `ref`/`tref`/`iref` attribute's target or `<name>InstanceRef`
      element type, an aggregated child type, a `Base`-column parent/sibling,
      a shared spec enum, an attribute's primitive container type, a
      **primitive type** (e.g. `MemorySection.alignment` is a PDF
      `AlignmentType` primitive — when no such class exists in
      `PrimitiveTypes.py`, add it as an `ARLiteral` subclass mirroring
      `String`/`NameToken`/`CIdentifier`, with the PDF note and
      `xml.xsd.pattern`/`xml.xsd.type` tags in its docstring, and type the
      attribute with it) etc. When any such type is declared in the spec but
      does **not** exist in the codebase, **implement it first** per these
      rules instead of deferring or substituting a placeholder — create the
      missing class from its own spec table, mirroring its siblings and its
      abstract parent if the `Base` column lists one, give it a method-parity
      checklist, tests, and parser/writer coverage, and only then type the
      referencing attribute against it. This applies to **every** kind of
      referenced class, not only `<name>InstanceRef` types (see the `iref`
      specifics in Rule 1.5).
- [ ] A missing **primitive** has its own spec table in the AUTOSAR markdown,
      formatted `Primitive <Name>` (e.g. Table 4.15 `CseCodeType`), **not** a
      `Class`/`Enumeration` table — verify the referenced type's actual kind
      from that table before implementing or recording a deviation (a prior
      row that read "PDF enum `CseCodeType` not modeled" mislabeled a
      primitive as an enum, which hid the fact that Rule 1.10 applied). The
      primitive's `Primitive` table may live in a **different** PDF/table than
      the class that uses it (e.g. `MultidimensionalTime.cseCode` — defined in
      the BSWModuleDescriptionTemplate PDF Table 8.22 — uses `CseCodeType`,
      whose `Primitive` table is in the SoftwareComponentTemplate PDF Table
      4.15); search the markdown for `Primitive <Name>` across PDFs, not just
      in the consuming class's own document. Implement the primitive as an
      `ARLiteral` subclass mirroring its siblings (`AlignmentType`, `String`),
      copy the `Primitive` table's `Note` verbatim plus its `Tags:`
      (`xml.xsd.customType=...`, `xml.xsd.type=...`) into the docstring, add a
      mirrored primitive test, re-type the referencing attribute against it,
      and **clear** the type-deviation row in the deviation tracker once the
      parser/writer already carry the element (the generic
      `getChildElementOptionalLiteral` / `setChildElementOptionalLiteral`
      helpers suffice when the element's lexical form is textual, matching the
      `AlignmentType` precedent).
- [ ] A placeholder substitute (e.g. `RefType` where the spec names a concrete
      class) is allowed only as a last resort when the missing class's model is
      genuinely out of scope; it must then be recorded in
      `docs/method_deviation_by_class.md` (reason "class not yet implemented"),
      forward-reference the real class in the inline comment and docstrings,
      and be switched to the real class (with a `TYPE_CHECKING` import if
      needed to avoid cycles) once it is implemented, clearing the deviation.

### 1.11 Member order follows the PDF

- [ ] Members are declared in the **same order as the spec table's attribute
      rows** — i.e. ascending `xml.sequenceOffset` (the PDF's `Tags:
      xml.sequenceOffset=NN` value). The order of the `__init__` fields, the
      order of the getter/setter/adder methods, and the order of the method
      parity checklist rows (Rule 2) must all follow the spec table row order,
      **not** alphabetical or file-of-creation order. A class whose accessors
      are ordered by name or by refactor history rather than by the spec is
      misaligned. (Example: `EngineeringObject` attributes are
      `shortLabel`(offset 10), `category`(20), `revisionLabel`(30),
      `domain`(40), so the accessors and checklist list them in exactly that
      sequence.)
- [ ] Within one attribute, the accessor pair order is `getXxx` then
      `setXxx` (or `addXxx`/`getXxxs` for list attributes) — getter before
      setter for each attribute, mirroring the sibling classes that are already
      aligned (e.g. `Compiler` lists `getName`/`setName`, `getOptions`/
      `setOptions`, ...). The getter-first pairing is uniform across aligned
      classes; only the *attribute* sequence varies, and that sequence comes
      from the PDF.

Verification: cross-check each attribute (name, multiplicity, **type**)
against the PDF table and the corresponding XSD in
`autosar-pdf/examples/xsd/`. Confirm any deviation against the parser/writer
code before recording it.

---

## Rule 11: Enum Types Must Inherit from `AREnum`

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

    # Literal one comment
    MEMBER_ONE = "member_one"

    # Literal two comment
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
the model.

---

## Rule 12: Enum Specification Alignment and Docstring Sync

**Maturity**: accept

Every enumeration class must have its member list and documentation synced with
the AUTOSAR PDF specification. Enums are easy to implement incorrectly because
the spec table may be sparse, incomplete, or the enum may have been created with
placeholder/assumed values that do not match the spec.

Check:
- [ ] Locate the enum's specification table in the AUTOSAR PDF markdown.
      Search by enum class name or the table number if known.
- [ ] Verify the enum members: every literal row in the spec table must have a
      corresponding Python enum member. There must be **no extra members** (not
      in spec) and **no missing members** (in spec but not in code).
- [ ] Enum member naming: convert the spec literal to Python UPPER_CASE naming.
      Example: spec literal `derivedFrom` → Python member `DERIVED_FROM`.
- [ ] Enum member value: the string value must **exactly match** the spec literal
      value. Example: `DERIVED_FROM = "derivedFrom"` (not `"derived_from"` or
      variations).
- [ ] **Member value vs. XML serialization form.** The Python member value is the
      spec literal read from the table header's `mmt.qualifiedName` tag — it is
      the camelCase form shared by the unified naming schemes of multiple
      releases (e.g. `DependencyUsageEnum.BUILD = "build"`). The **XSD**,
      however, serializes enum literals in **UPPERCASE** (e.g. the schema value
      for `DEPENDENCY-USAGE-ENUM` is `BUILD`, and for `PROGRAMMINGLANGUAGE-ENUM`
      it is `C`). These two forms are not interchangeable for tests: a *model
      round-trip* carries the member value verbatim and is lossless either way,
      but an **XSD-valid** fragment (e.g. a fixture fed to an XSD validator, or a
      reference document) must always use the **UPPERCASE serialized** literal,
      not the camelCase member value — otherwise the schema rejects it. Do not
      "fix" the member value to UPPERCASE to satisfy the schema: keep the member
      matching the spec's `mmt.qualifiedName`, and write the UPPERCASE form only
      in test XML fixtures and fragments.
- [ ] Class docstring: summarize the spec table's "Note" row (the enum's purpose
      and scope).
- [ ] Enum member documentation: each member must have an inline comment that
      cites the spec literal's description (not paraphrased, use the PDF wording).
      Include Tags information (e.g., `atp.EnumerationLiteralIndex=0`) to document
      the spec's ordering.
- [ ] Sync with PDF on every review: when updating an enum, always check the
      PDF spec table first. Do not assume previous implementations are correct
      — placeholder/assumed member sets recur often enough that "trust but
      verify" is not sufficient; always re-derive the member list from the
      table.
- [ ] Tests reference enum literals like `MyEnum.MEMBER_NAME` (a plain `str`
      equal to the spec literal) for comparison and reading. To **set** an
      enum-typed attribute, construct an enum **instance** —
      `MyEnum().setValue(MyEnum.MEMBER_NAME)` — never pass the bare member to a
      setter: `setRptHookAccess(RptAccessEnum.ENABLED)` stores a `str` in the
      model and crashes the writer, which expects an `ARLiteral`/`AREnum`
      instance (`writeARObjectAttributes` reads `.timestamp`). To assert a
      round-tripped enum value use `.getValue() == "memberName"`, because the
      parser returns a generic `ARLiteral`, not a `MyEnum` instance.
      An aligned enum defines its own `__init__(self)` that passes the
      valid-value tuple to `AREnum`, so `MyEnum()` **is** instantiable;
      `MyEnum()` raises a `TypeError` only for an enum without that custom
      `__init__` (where `AREnum.__init__` expects the tuple).

Example from a spec table (`Literal` column):

| Literal       | Description |
|---------------|-------------|
| derivedFrom   | Describes that ... . Tags: atp.EnumerationLiteralIndex=0 |

**Correct implementation** (matches spec):
```python
class MyEnum(AREnum):
    """
    Enumeration for something.
    """
    # MyEnum method parity checklist:
    # (no methods)

    # Describes that ... . Tags: atp.EnumerationLiteralIndex=0
    DERIVED_FROM = "derivedFrom"
```

**Incorrect implementation** (had members NOT in spec):
```python
class MyEnum(AREnum):
    # WRONG: these are not in the spec table
    READS = "reads"
    WRITES = "writes"
```

Verification: search the AUTOSAR markdown (`autosar/markdown/*.md`) for the
enum's spec table. Compare the literal rows (Literal column) 1:1 with the enum
members defined in Python code:
```bash
grep -A 10 "^Table.*: <EnumName>" autosar/markdown/AUTOSAR*.md
```

If there is a mismatch (extra members, missing members, wrong values, or
missing docstrings), correct the enum implementation and update all
corresponding tests.

---

# Section 2: Package and Module Location (Rule 8)

## Rule 8: Package Location

**Maturity**: accept

The class must be defined in the module that matches the `Package` row of its
spec table. There is exactly one module file per spec package, and all classes
in that spec package must be defined in that single module.

Check:
- [ ] The spec table's `Package` row (e.g.
      `M2::AUTOSARTemplates::SomeTemplate::SomeGroup`) maps 1:1 to a module
      under `src/armodel/models/`: strip the leading `M2::` and replace `::`
      with `/`. The last segment names the module file or package directory
      (`...::SomeGroup` → `SomeGroup.py` or `SomeGroup/__init__.py`).
- [ ] If the module is a file (`SomeGroup.py`), all classes in that spec
      package must be defined in that single file.
- [ ] Package **name match** (the last segment is the package, not the class):
      the `Package` row names the spec package and the class is its *direct
      member* — the class name comes from the table's `Class` header, **not
      from the package path**. Do **not** place the class in a sub-module/
      sub-package whose tail is the class name, because that makes the class
      name look like a package and mismatches the `Package` row. Example:
      if `SomeGroup`'s `Package` row is
      `M2::AUTOSARTemplates::SomeTemplate::SomeGroup`, the class is a member
      of `SomeGroup` — putting it in `SomeGroup/ClassName.py` is a
      package-name mismatch, because that path implies package
      `...::SomeGroup::ClassName`. The class must be defined **directly** in
      `SomeGroup/__init__.py`.
- [ ] **Element-type packages whose tail equals the class name are the correct,
      aligned case, not the anti-pattern.** When the `Package` row's last
      segment *is* the class itself (e.g. `BswImplementation` →
      `M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation` → module
      file `BswImplementation.py`), the class is the package's direct member
      and is defined directly in that `ClassName.py` module. This is common for
      root element types and needs no sub-package. The package-name-match
      anti-pattern above applies only when the package tail (`SomeGroup`)
      differs from the class (`ClassName`) and the class is wrongly nested as
      `SomeGroup/ClassName.py` — do not conflate the two, and do not move a
      class out of a class-named element-type module.
- [ ] **Classes sharing the parent package tail.** When several classes' `Package`
      rows end in the same tail (e.g. `HardwareConfiguration`, `SoftwareContext`,
      and `ResourceConsumption` all have `Package` =
      `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption`), they are
      **all** direct members of that package's `__init__.py`. Do not give each
      its own `<ClassName>.py` submodule even though *other* class-named modules
      sit in the same directory (`HeapUsage.py`, `StackUsage.py`, …) — those
      modules belong to their own separate spec packages
      (`...::HeapUsage`, `...::StackUsage`) and are the element-type case, not
      a precedent for adding a class-named module. This also applies when the
      class-named submodules **already exist from an earlier placeholder
      stage** — a group package (`...::MeasurementCalibrationSupport`,
      `...::RptSupport`) whose classes were each filed as
      `MeasurementCalibrationSupport/McSupportData.py`,
      `RptSupport/RptSupportData.py`, … must be consolidated into the package
      `__init__.py` (all 8 `...::MeasurementCalibrationSupport` classes in
      `MeasurementCalibrationSupport/__init__.py`, all 12 `...::RptSupport`
      classes in `RptSupport/__init__.py`), and every consumer import rewritten
      from the submodule path to the package path. When the consolidated
      `__init__.py` needs classes from a *sibling* package that would import it
      back (e.g. `RptSupport` needs `RoleBasedMcDataAssignment` from its
      parent, the parent needs `RptSupportData`/`RptSwPrototypingAccess` from
      `RptSupport`, and `RPTScenario` needs `RptSupport`'s enums), break the
      cycle with `from __future__ import annotations` + `TYPE_CHECKING`
      imports for every cross-package name that is used only in annotations
      (Rule 6) — the parser/writer keep runtime imports because they sit below
      the model graph. When the `__init__.py` also
      imports those sibling submodules and they import the package-level
      classes back, define the package-level classes **before** the submodule
      import statements in `__init__.py` to break the cycle.
- [ ] If the module is a directory/package (`SomeGroup/__init__.py`), the spec
      package's classes are defined in that `__init__.py` file (or imported
      and re-exported from `__init__.py` if split into submodules). Prefer
      defining classes **directly** in `__init__.py`; only split into
      per-class submodules when the spec package grows large enough that
      splitting clearly aids maintainability — a sparse package (one or a few
      classes) must not add an extra `__init__.py` re-export hop for each
      class — and a sub-module name must never reuse the class name (see
      package-name-match above).
- [ ] Do **not** create sibling files (e.g. `SomeGroupExtra.py`) to house
      classes that belong in the spec package's single module — consolidate
      all classes for a spec package in one place.
- [ ] The module path must not be shadowed by a same-named sibling directory:
      when the spec `Package` maps to `X.py` but a directory `X/` also exists
      (without `__init__.py`), the module file wins in the import system and
      classes placed only in `X/*.py` are unreachable dead code. Define the
      classes in `X.py`, or make `X/` a real package with an `__init__.py`.
      This shadowing can hide a **whole family** of classes at once — every
      class in the shadowed directory must be migrated out, one at a time.
      When migrating a class out of a shadowed directory, update
      `tests/test_armodel/test_model_imports.py`: remove the class name from
      `KNOWN_NAME_COLLISION_CLASSES` **and** adjust the count in that module's
      docstring, so the class becomes importable from `armodel` and stays
      covered by the import test. A class listed in
      `KNOWN_NAME_COLLISION_CLASSES` is a live signal that it may live in a
      shadowed directory and deserves a Rule 8 review. A shadowed class is
      **dead code** even though report scans still find it, so a clean rule
      review of the class is not enough — the class must be relocated to the
      real module. After relocating, audit **every** reference to the old
      shadowed path, not just live imports: stale `# from ...` comments in
      `src/armodel/models/__init__.py`, the source path in
      `docs/development/method_deviation_by_class.md`, and any docs/reports
      that name the old path.
- [ ] Classes are **not** placed under a spec package different from their own.
- [ ] Import statements **match** the package location: every consumer imports
      the class from the package that defines it — `from ...<Args>.<Package>
      import <ClassName>` when the class lives in a package's `__init__.py`,
      and never from a class-named sub-module (`from
      ...<Package>.<ClassName> import ...`), which would imply a
      non-existent sub-package. After relocating a class, audit every import
      site (parser, writer, `__init__.py` re-exports, tests) so no stale
      class-named sub-module import remains.
- [ ] **Latent broken imports surface when an aggregator starts importing its
      child package.** Aligning an aggregator that aggregates/refs classes in
      a sibling subpackage pulls that subpackage into the import graph for
      the first time; never-imported sibling modules can then fail with stale
      package paths (e.g. `RptSupport/RptExecutableEntity.py` imported
      `...MeasurementCalibrationSupport.RptAccessEnum` while the module lives
      at `...MeasurementCalibrationSupport.RptSupport.RptAccessEnum`). Such a
      module is dead code that passes lint and coverage scans until something
      imports it, so after adding any cross-package import run the full
      import + test suite, not just the class's own mirrored test.
- [ ] **Top-level export chain (`src/armodel/models/__init__.py`).** A class is
      "correctly placed" only when it is also reachable from `armodel` via the
      wildcard export chain. When a class in an aligned package is **not**
      importable as `armodel.<ClassName>` (check with
      `hasattr(armodel, "<ClassName>")`), either the package is missing from
      `models/__init__.py` (e.g. `MeasurementCalibrationSupport` and its
      `RptSupport` subpackage had no `import *` lines while every other
      `CommonStructure` subpackage did) or the class is still listed in
      `INTENTIONALLY_UNEXPORTED_MODULES` in `tests/test_armodel/test_model_imports.py`.
      Aligned classes must be **removed** from that exclusion set (it is for
      "incomplete/experimental" classes only) and the package's `import *`
      lines added to `models/__init__.py` — follow the per-subpackage pattern
      already used for `ResourceConsumption.HeapUsage` etc. Run
      `test_model_imports.py` after the change; a name that collides at top
      level goes into `KNOWN_NAME_COLLISION_CLASSES`, not
      `INTENTIONALLY_UNEXPORTED_MODULES`.

**Practical shadowing checklist:**

1. In the target directory, run `ls` (or `dir` on Windows).
2. Do you see both `ModuleName.py` AND a `ModuleName/` directory (without
   `__init__.py`, or even with `__init__.py`)? → **Shadowing exists**.
3. Any classes defined only in `ModuleName/*.py` (not in `ModuleName.py`) are
   unreachable.
4. Fix: define all classes for that spec package in the winning `.py` file; do
   **not** create submodule files in the `ModuleName/` directory. After
   moving classes out, update `KNOWN_NAME_COLLISION_CLASSES` in
   `test_model_imports.py`, any stale imports, and the deviation tracker.

Verification: read the `Package` row from the class's spec table and compare
it with the module path under `src/armodel/models/`. Verify all classes for
that spec package are in the same module file.

---

# Section 3: Type Hints and Method Signatures (Rules 3, 10)

## Rule 3: Type Hints

**Maturity**: accept

All function parameters and return values must have type hints (Python
3.8-compatible syntax — use `typing.List` / `typing.Optional`, never `X | None`
or `list[...]` unless `from __future__ import annotations` is present).

**IMPORTANT — Python 3.8 compatibility (the most common mistake):** the
project requires **Python >= 3.8** (see `pyproject.toml`), but the `|` union
syntax was introduced in Python 3.10. Always use `Optional[T]` / `List[T]` /
`Dict[K, V]` from the `typing` module, not `T | None` / `list[T]` /
`dict[K, V]`. Violating this creates **runtime errors** in Python 3.8–3.9
environments. Before committing any class, verify there are no bare `|`
operators in type hints.

| Method kind  | Signature                                                    |
|--------------|--------------------------------------------------------------|
| list getter  | `def getFoos(self) -> List[Foo]:`                            |
| single getter| `def getFoo(self) -> Foo:` or `def getFoo(self) -> Optional[Foo]:` |
| setter       | `def setFoo(self, value: Optional[Foo]) -> "ClassName":`      |
| add          | `def addFoo(self, value: Optional[Foo]) -> "ClassName":`      |
| create       | `def createFoo(self, short_name: str) -> Foo:`               |

The `setFoo`/`addFoo` `value` parameter is `Optional[Foo]` because `None` is a
no-op per Rule 4 — aligned classes consistently annotate it so (e.g.
`MemorySection.setAlignment(value: Optional[AlignmentType])`, `addExecutableEntityRef(value: Optional[RefType])`).

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
- [ ] **No untyped accessor pairs.** A `getXxx`/`setXxx` pair with **no
      annotations at all** (`def getSize(self):` / `def setSize(self, value):`)
      is a Rule 3 violation even if the field itself is annotated — every
      getter return and every setter parameter must carry the concrete type
      (e.g. `MemorySection.size` → `getSize() -> Optional[PositiveInteger]`
      and `setSize(value: Optional[PositiveInteger])`).
- [ ] A field that defaults to `None` and maps to a spec `0..1` attribute must
      be annotated `Optional[T]` — never a non-optional `T` initialized to
      `None`. A bare `self.fooRef: RefType = None` contradicts its own
      getter's `Optional[RefType]` return and is an internal inconsistency.
      Optionality is expressed in the annotation, not just by the `None`
      default. This applies equally to Kind `attr` single-valued attributes
      (e.g. an enum-typed field) as it does to Kind `ref`.
- [ ] **No looser-union coercion setters.** A setter parameter must be exactly
      the field/primitive type — never `Optional[Union[String, str]]` or
      `Optional[Union[Integer, int]]` that converts a bare `str`/`int` into the
      typed primitive via an `isinstance` branch. The parser and writer already
      produce the typed primitive, so the coercion is dead convenience API that
      (a) is an internal type mismatch — field, getter, and setter no longer
      agree (Rule 1.3) — and (b) silently breaks the Rule 4 no-op contract:
      `setCseCode(None)` falls through the `isinstance(value, str)` branch into
      the else branch and **overwrites** the existing value with `None`. Type
      the setter `value: Optional[T]` and guard with the uniform
      `if value is not None:`. Callers (including tests) must construct the
      typed primitive — `CseCodeType().setValue("100")`, `Integer().setValue(2)`
      — not pass a bare `str`/`int`.

Example:
```python
def getFoo(self) -> Optional[Foo]:
    return self.foo

def setBarId(self, value: PositiveInteger) -> "ClassName":
    if value is not None:
        self.barId = value
    return self
```

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
remove the trailing comma and let Black collapse it. This supersedes any older
79-character line guidance.

Example (correct):
```python
def setSomeEnumValue(self, value: Optional[SomeEnum]) -> "ClassName":
    """Sets the value."""
    if value is not None:
        self.someEnumValue = value
    return self
```

Example (incorrect):
```python
# DON'T do this:
def setSomeEnumValue(self, value):
    # Type information moved to comment, not in signature
    # value: Optional[SomeEnum]
    if value is not None:
        self.someEnumValue = value
    return self
```

---

# Section 4: Getter / Setter Behavior (Rule 4)

## Rule 4: Getter / Setter Behavior

**Maturity**: accept

- [ ] Setters return `self` for method chaining.
- [ ] Setters and adds are **no-ops when the value is `None`** — they must not
      overwrite the existing value and must not append `None`. This is
      parser-safe: the parser helpers (`getChildElementOptional*` in
      `abstract_arxml_parser.py`) return `None` for missing XML elements, so a
      `None` value simply leaves the default in place.
- [ ] Validation setters follow the same pattern: validation runs only for
      non-`None` values, and `None` is a no-op.
- [ ] Getters return the underlying field directly (no copies, no exceptions
      when unset — they return `None` / `[]`).
- [ ] `create*` factories return the existing element when a short name already
      exists (no duplicate creation), and append the new element to the
      corresponding list otherwise. In an `Identifiable`-based aggregator the
      existing-element check uses the `elements` registry
      (`if not self.IsElementExists(short_name)` / `self.getElement(short_name)`);
      in a **plain `ARObject` aggregator** (no `elements` registry, e.g.
      `McSupportData`) the check scans the owning field list directly —
      `for instance in self.foos: if instance.short_name == short_name: return instance` —
      and the factory appends to that same list and returns the new instance.
      Exposing a `createXxx(short_name)` factory also **forces the aggregated
      child to be constructible as `Child(self, short_name)`**: a placeholder
      child that still declares `__init__(self)` and inherits only `ARObject`
      must be realigned to its spec `Base` (e.g. `McDataInstance` →
      `Identifiable` with `__init__(self, parent, short_name)`) at least far
      enough for the factory to build it; the remainder of the child's own
      alignment is tracked separately in the deviation tracker.
- [ ] `create*` factories are only used for children that are
      `Referrable`/`Identifiable` per their spec `Base`; non-Identifiable
      children use `setXXX` (multiplicity `0..1`) or `addXxx(value)`
      (multiplicity `*`) instead — never a no-arg factory (see Rule 1.6).

Every setter and add method follows the uniform pattern:
```python
def setSomething(self, value: T) -> "ClassName":
    if value is not None:
        self.something = value
    return self

def addSomething(self, value: T) -> "ClassName":
    if value is not None:
        self.somethings.append(value)
    return self
```

This pattern is critical because:
1. **Parser safety**: parser helpers return `None` for missing XML elements.
2. **No overwriting**: setting `None` must not overwrite an existing value.
3. **Consistency**: all classes apply this pattern uniformly.

Tests must verify this explicitly: after `setter(value)`, then `setter(None)`,
the getter must still return the original value. The same holds for
`addXxx(value)` followed by `addXxx(None)` (nothing appended).

### Rule 4.1: Abstract Base + Concrete Subclass Uniformity

When a class hierarchy consists of an abstract base class and one or more
concrete subclasses (e.g., `StackUsage` → `MeasuredStackUsage`,
`RoughEstimateStackUsage`, `WorstCaseStackUsage`), **all setters across the
entire hierarchy must follow the same `if value is not None:` guard pattern**.
A concrete subclass setter cannot break the guard that the abstract base
establishes — mixing guarded base setters with unguarded subclass setters
introduces a silent inconsistency where some setters preserve existing values
when `None` is passed, while others overwrite them.

Check:
- [ ] **Every** setter in the concrete subclass guards with `if value is not None:`
      (or inherits a guarded setter from the base).
- [ ] When testing the concrete subclass, verify that setting `None` on
      inherited base setters and subclass-specific setters both no-op. Use a
      combined base-properties test (see Rule 7) to exercise all setters from
      the base as well as the subclass's own setters, followed by `setter(None)`
      assertions for the whole set. This ensures the guard is actually present
      and working, not merely declared in the signature.
- [ ] A property setter (a `@property` decorated `def foobar(self, value):
      self.foo = value`) is a setter too and must guard — treat it the same way.

Example (correct hierarchy):
```python
class StackUsage(Identifiable, ABC):
    def setHwElementRef(self, value: Optional[RefType]) -> "StackUsage":
        if value is not None:  # Guard present
            self.hwElementRef = value
        return self

class MeasuredStackUsage(StackUsage):
    def setAverageMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsage":
        if value is not None:  # Guard present — consistent with base
            self.averageMemoryConsumption = value
        return self
```

Example (wrong — inconsistent hierarchy):
```python
class StackUsage(Identifiable, ABC):
    def setHwElementRef(self, value: Optional[RefType]) -> "StackUsage":
        if value is not None:  # Guard present
            self.hwElementRef = value
        return self

class MeasuredStackUsage(StackUsage):
    def setAverageMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsage":
        self.averageMemoryConsumption = value  # WRONG: no guard
        return self
```

Note: this rule is not uniformly applied across the codebase yet. When a class
under check violates it, align the class to the no-op behavior as part of the
check — this includes **every** setter of the class, its abstract bases, and
its package siblings (e.g. `StackUsage`/`HeapUsage`/`ExecutionTime` all had
unguarded setters while their aggregated siblings were already guarded), and
property setters that back a field (a `@property` setter is a setter too and
must no-op on `None`).

---

# Section 5: Documentation — Checklist and Comments (Rules 2, 5)

## Rule 2: Method Parity Checklist

**Maturity**: accept

A comment block at the top of the class lists every method with three columns:
`impl`, `docstring`, `test`. Each column must be marked `[x]`. The first line
after the checklist title must cite the AUTOSAR PDF spec table the class is
aligned against: `# Spec: <PDF file>.pdf, Table <X.Y>, p.<page>` (page from
the PDF itself). This makes Rule 1 traceable — every later check refers back
to the spec source named in the class comment.

```python
# ClassName method parity checklist:
# Spec: AUTOSAR_CP_TPS_SomeTemplate.pdf, Table X.Y, p.NN
# [x] __init__                     [x] impl  [x] docstring  [x] test
# [x] getFoos                      [x] impl  [x] docstring  [x] test
# [x] setFoos                      [x] impl  [x] docstring  [x] test
# [x] createFoo                    [x] impl  [x] docstring  [x] test
```

Check:
- [ ] The checklist covers every method defined on the class, 1:1 (no missing,
      no extra). A `@property` member counts as a method here: it is an
      `ast.FunctionDef` in the class body, so it needs a checklist row (`[x]
      impl/docstring/test`) and a test just like a normal method — it is not
      exempt just because it is not a `def getXxx` accessor. A field backed by
      a property therefore produces **three** rows: `getXxx`, the property
      name itself, and `setXxx` (e.g. `MemorySection` lists `getAlignment`,
      `alignment`, `setAlignment`).
- [ ] Every row is fully `[x]` — no stale `[ ]` entries. A row can look
      incomplete even when the method/docstring/test all already exist —
      always double-check by reading the class, not just the checklist text.
      A `[ ] test` row whose method already has a test in the mirrored test
      file is stale and must be crossed (e.g. `StackUsage`'s abstract base
      accessors were tested via a concrete subclass, but the rows stayed
      `[ ]`). Grep the class body for `# [ ]` during every review — the
      set-based script alone does not flag them.
- [ ] A row is crossed (`[x]`) **only** when all three of its obligations are
      complete and verified — the implementation, the docstring, and the unit
      test. A method that is implemented but whose docstring or test is not
      yet done stays `[ ]` ("impl done, docstring/test pending"). Never cross
      an item speculatively in anticipation of work that has not finished:
      the checklist reflects the *current* verified state, and it is updated
      only when the last outstanding obligation is actually done and the test
      passes. This keeps a partially-implemented class visibly incomplete
      instead of falsely appearing complete.
- [ ] The `# Spec:` line names the correct PDF, table number, and page for the
      class (cross-check against the actual PDF).

**Spec reference format** (supports automated tooling and traceability):
`# Spec: <PDF-filename>.pdf, Table <X.Y>, p.<page>`
- The PDF filename must match exactly (check the actual PDF file name in the
  repo).
- Table number must be in format `X.Y` (e.g., `5.38`, not `5-38` or `538`).
- The page number must **always** be present — a `# Spec:` line without
  `p.<page>` is a violation. Page number is from the PDF's own printed page
  counter (the `X of NNNN` footer), not document section numbers or markdown
  line numbers.
- Cite the page where the table's **header row** first appears — the `Class
  <Name>` (or `Enumeration <Name>` for enums) heading in the PDF markdown —
  not necessarily the caption's page. Long tables can split across pages, with
  the caption on the page *after* the header row (e.g. Table 8.1
  `Implementation`: header row p.619, caption p.621); the header row and the
  caption can also be on the **same** page with the table *ending* on the
  caption page (e.g. `ResourceConsumption` Table 8.1: header row p.137,
  caption p.138; `MemorySection` Table 8.2: header p.143, caption p.144;
  `ExecutionTime` Table 8.17: header p.159, caption p.160;
  `MultidimensionalTime` Table 8.22: header p.164, caption p.165;
  `RoughEstimateOfExecutionTime` Table 8.25: header p.167, caption p.168) —
  in **both** layouts always cite the header row's page so the reader lands
  on the class definition. Verify the header page directly in the PDF
  (search for the `Class <Name>` heading), do not assume the caption page.
- Adjacent tables that appear on the same or consecutive pages (e.g. an
  abstract class and its subclasses) are easy to confuse with one another or
  with the section's start page — verify each class's **own** `Table X.Y`
  page independently against the PDF's printed page counter, and never reuse a
  neighboring class's already-checked value. Cross-check against the page in
  `docs/method_deviation_by_class.md`, which may already be correct.
- **Abstract base + concrete subclass sharing one page.** When the spec page
  holds *two* tables on the same page — an abstract base (e.g.
  `EngineeringObject`, Table 7.6, p.132) and a concrete subclass
  (`AutosarEngineeringObject`, Table 7.5, p.132) whose table has **no** own
  attribute rows — both classes still get their **own** `# Spec:` line with
  their **own** table number/page, and the concrete subclass declares no
  fields of its own (the base carries the attributes). The concrete subclass's
  checklist lists only `__init__` (plus any methods it actually adds); do not
  copy the base's accessor rows into the subclass checklist, since a concrete
  subclass inheriting all accessors from the abstract base defines no methods
  of its own. The set-based script (Rule 7) then passes with a one-row
  checklist because the subclass body contains only `__init__`.
- Different AUTOSAR release PDFs may have different page numbers; verify
  you're reading the correct release.

Verification: extract the checklist names and the class method names and
compare them set-wise (see the script in Rule 7). **Additionally**, a row
marked `[x] test` must correspond to a real test: verify each method name
appears in the mirrored test file.

The checklist is method-only: it verifies that listed methods exist and are
tested, but it cannot detect a *fabricated attribute* — a field with accessors
that appears nowhere in the spec (see the "no fabricated attributes" check in
Rule 1.3). A 100%-checked-off class can still carry invented API, so Rule 1's
field-to-spec cross-check is the gate, not the checklist.

**Field-to-spec cross-check procedure** (systematic, per field):
1. Strip any suffix (`Ref`, `TRef`, `IRef`, `s` for plurals).
2. Search the spec table's `Attribute` column for the **base name** (without
   suffix). Also check the `Aggregated by` rows of other spec tables — a
   field may be defined there (cross-table aggregation, see Rule 1.3).
3. If found → field is spec-aligned; continue.
4. If **not found** → check the XSD for the XML element tag: if present with a
   documentation block, the PDF table omits it — keep and record the
   deviation (see Rule 1.3). Otherwise the field is fabricated. **Remove it**
   (unless it's a documented read-only derived convenience property with
   tests, recorded in the deviation tracker — see Rule 1.3).

---

## Rule 5: Comments from the Spec

**Maturity**: accept

Inline comments and docstrings must reflect the PDF spec wording, not loose
paraphrase.

- [ ] Each attribute in `__init__` has an inline `#` comment based on the PDF
      table note for that attribute. The comment should include the key
      semantic information from the spec. Quote the **semantic sentence** of
      the `Note` column (verbatim or near-verbatim); do **not** paste the
      `Stereotypes:`/`Tags:` tail of the note (e.g.
      `Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=...`) — that
      tail is tooling metadata already captured in the markdown and adds no
      semantics to the comment. Example: `AccessCountSet.accessCount`'s note
      "Count value for a AbstractAccessPoint. Stereotypes: ..." is quoted in
      the inline comment as "Count value for a AbstractAccessPoint."
- [ ] Constraint rows are spec material for the comment just like the
      attribute note: when the PDF's `constr_*` rows impose a constraint on
      the attribute, include the constraint wording in the inline comment and
      cite its id. The full constraint wording is typically rendered as a
      `[constr_NNNNN]` paragraph **immediately after the class's own table**
      (in addition to any consolidated constraint index elsewhere in the PDF)
      — e.g. `AccessCountSet`'s Table 4.22 is followed by `constr_10270`
      constraining `countProfile`. Grep both the table neighborhood and the
      constraint index when collecting constraint material for a class. Class-level `constr_*` rows belong in the class docstring
      alongside the note — **including constraints on inherited
      attributes**: a constraint may target an attribute the subclass does
      not declare itself (e.g. `constr_4103` constrains
      `SectionNamePrefix.symbol`, which is inherited from
      `ImplementationProps`, and therefore belongs in the
      `SectionNamePrefix` class docstring, not in the parent's). Conversely,
      an attribute-level `constr_*` (e.g. `constr_4072` on
      `SectionNamePrefix.implementedIn`) is cited in the `__init__` inline
      comment **and** in the getter/setter docstrings.
- [ ] The class docstring reflects the PDF class note (the element's
      purpose).
- [ ] Getter/setter docstrings summarize the PDF note and semantic meaning,
      not just "Gets/sets the value". They should mention what the attribute
      represents in AUTOSAR, cite the applicable `constr_*` id, and for `iref`
      attributes name the implementing `<name>InstanceRef` class (so the
      concrete iref type is discoverable in the code, not only in the
      deviation tracker). Docstrings connect spec semantics to code
      intent; setter docstrings should also mention the no-op behavior and
      the chainable return.
      **When a setter is guarded (`if value is not None:`), the docstring
      must explicitly state**: "A None value is a no-op and does not
      overwrite an existing [attribute]."
      This documents the guard behavior so consumers understand that setting
      `None` is safe and intentional, not a bug.

Example from a spec PDF:
```python
# Indicates an entry which is required by this module.
# Replacement of a deprecated attribute.
self.expectedEntryRefs: List[RefType] = []
```

Example (attribute optional because an alternate reference exists per the
spec note):
```python
# AUTOSAR identifier of the target module; optional as the target may be
# identified by targetModuleRef instead.
self.targetModuleId: Optional[PositiveInteger] = None
```

---

# Section 6: Formatting (Rules 6, 9)

## Rule 6: Formatting

**Maturity**: accept

- [ ] All imports are at the beginning of the file (module docstring first,
      then `from __future__` if any, then imports, then code — PEP 8 E402).
      Mid-file imports are **not** used to work around circular imports; the
      cycle is broken properly instead: modules that only reference another
      module's classes in type annotations import them under `TYPE_CHECKING`
      and add `from __future__ import annotations`; a module that needs the
      other class at runtime (instantiation) uses a function-local import
      inside the method that instantiates (e.g. `Implementation` keeps no
      module-level `ResourceConsumption` import — annotations are
      `TYPE_CHECKING`, and `createResourceConsumption` imports it locally;
      the `ResourceConsumption` package submodules likewise import
      `HardwareConfiguration`/`SoftwareContext` under `TYPE_CHECKING`).
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

## Rule 9: Attribute Spacing in Classes

**Maturity**: accept

Each member (attribute, enum literal, or method) in a class must be separated
by exactly one blank line. This improves readability and clearly delineates
separate logical units within the class.

Check:
- [ ] Every attribute in `__init__` has a blank line before and after its
      comment + assignment block.
- [ ] Every enum literal block (inline comment + `NAME = "value"`) is
      separated from the next by exactly one blank line.
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

Example (enum):
```python
class MyEnum(AREnum):
    # Literal one comment
    MEMBER_ONE = "member_one"

    # Literal two comment
    MEMBER_TWO = "member_two"
```
```

---

# Section 7: Tests (Rule 7)

## Rule 7: Tests

**Maturity**: accept

Every method on the class must have test coverage in the mirrored test file
(`tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py`).

- [ ] `test_initialization` asserts all attributes have correct default values
      (`None` / `[]`).
- [ ] Abstract classes cannot be instantiated directly, so test their
      `__init__` defaults through a concrete subclass. The reference pattern
      is `test_concrete_subclass_initialization`: instantiate a known
      concrete subclass (or a local subclass defined in the test) and assert
      every default set by the abstract `__init__`. Include the literal
      `__init__` in the test (docstring or a local subclass `def __init__`)
      so the checklist's `[x] test` for `__init__` stays verifiable by the
      set-based check.
- [ ] **Abstract base accessors** are tested through a concrete subclass in
      one combined base-properties test (`test_<name>_base_properties`):
      instantiate a concrete subclass, exercise every getter/setter the base
      declares, assert chaining + round-trip, and finish with the None no-op
      assertions for the whole set (e.g. `StackUsage`/`HeapUsage`/
      `ExecutionTime` base accessors via `MeasuredStackUsage`/
      `MeasuredHeapUsage`/`AnalyzedExecutionTime`). This is what crosses the
      abstract class's checklist rows — a base whose accessor rows stay
      `[ ]` while such a test exists is a stale checklist.
- [ ] Getter/setter pairs share a combined test (`test_get_set_*`) that checks:
      (1) setter returns `self` for method chaining, (2) value round-trips
      (getter returns the set value), (3) setting `None` is a no-op (existing
      value is preserved). The None no-op test is critical: verify that after
      `setter(value)` followed by `setter(None)`, the getter still returns the
      original value.
- [ ] Tests construct typed primitive values (`CseCodeType().setValue("100")`,
      `Integer().setValue(2)`), never a bare `str`/`int` passed to a setter —
      a test relying on a setter's `str`/`int` coercion (e.g.
      `MultidimensionalTime().setCseCode("cse").setCseCodeFactor(2)`) depends on
      exactly the looser-union behavior Rule 3 forbids, so aligning the class
      breaks such a test; update the call site to the typed primitive at the
      same time. For **numerical** primitives pass the value as a **string**:
      `PositiveInteger().setValue("4")`, not `setValue(4)` — the writer
      serializes `ARNumerical._text`, which is populated only when the value is
      assigned as a string (int assignment leaves `_text` `None` and the
      element round-trips as `<ELEMENT></ELEMENT>`, dropping the value on
      re-parse). Round-trip assertions then read `getValue() == 4` (an `int`).
- [ ] `add*` methods test appending, the return value (`self`), and the `None`
      no-op (setting None does not append).
- [ ] Every `create*` factory has a test asserting the short name and that the
      element is appended to the corresponding list.
- [ ] Plain getters have a default-value test.
- [ ] When a class gains new attributes covered by parser/writer support,
      verify the round trip end-to-end (set values → save → reload → assert
      the values come back) in addition to the unit-level get/set tests; this
      is the practical test that Rule 1.7's "parser and writer coverage" check
      is meant to guarantee. Run the full round trip **even when the class's
      own methods look complete**: the write path also serializes the
      *inherited base-class* fields, and a base-class deviation can crash or
      silently drop the whole element (e.g. `Implementation.swVersion` typed
      as a `List` but written through a scalar literal writer, and
      `vendorId` defaulting to a raw `int` while the numerical writer expects
      an `ARNumerical`) — such failures surface only in the end-to-end round
      trip, never in the class's own unit tests. A minimal robustness fix in
      the base writer is a legitimate part of aligning the subclass.

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
# Rule 13.1: the class must carry the spec-version marker (a fully-[x]
# checklist can still miss it, so check it explicitly)
assert re.search(r"# Spec verified: R\d\d-\d\d", src), "missing # Spec verified marker (Rule 13.1)"
```

---

# Section 8: Docstring Specification Synchronization (Rule 13)

## Rule 13: Docstring Synchronization with AUTOSAR Specification

**Maturity**: accept

Class docstrings and attribute/method docstrings must remain synchronized with
the AUTOSAR PDF specification source. When the AUTOSAR version is upgraded,
stale docstrings become silent documentation drift — docstrings that no longer
match the spec but the code still compiles and tests still pass. This rule
defines how to detect and prevent that drift.

### 13.1 Docstring Versioning

- [ ] The class's method parity checklist includes an AUTOSAR version marker
      indicating which AUTOSAR release the spec docstrings were verified against.
      Add a comment line immediately after the `# Spec:` line:
      ```python
      # HeapUsage method parity checklist:
      # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.13, p.152
      # Spec verified: R23-11
      ```
      Use the format `R<YY>-<MM>` (e.g., `R23-11` for November 2023 release,
      `R24-11` for November 2024). This marker makes it discoverable which
      classes need review after an AUTOSAR upgrade.
- [ ] Verify the marker during **every** alignment pass, not only when a class
      is first implemented. A class aligned before this rule existed can carry
      a fully-`[x]` checklist and a correct `# Spec:` line yet still lack the
      marker — the Rule 2/7 set-based script does not check for it, so extend
      that script with an explicit `assert re.search(r"# Spec verified:
      R\d\d-\d\d", src)` (see Rule 7) to catch it mechanically.

### 13.2 Drift Detection on AUTOSAR Upgrade

When the AUTOSAR specification version is upgraded in the repository:

1. **Identify affected classes**: search the codebase for the old version marker
   (e.g., `# Spec verified: R23-11`) using:
   ```bash
   grep -r "Spec verified: R23-11" src/armodel/models/
   ```

2. **For each affected class**, perform these steps:
   - [ ] Open the class source file in an editor.
   - [ ] Locate the corresponding spec table in the new AUTOSAR PDF markdown
         (search `autosar/markdown/AUTOSAR_CP_TPS_*.md` for the table name).
   - [ ] Read the spec table's `Note` row (the class purpose/definition).
   - [ ] Compare the `Note` text verbatim with the class docstring (first line
         after `"""`).
   - [ ] If different: update the class docstring to match the new PDF `Note`
         exactly (use the PDF wording verbatim, not paraphrased).
   - [ ] For each attribute, compare the PDF table's `Note` column entry with
         the inline comment in `__init__` (the line after `self.attributeName`).
   - [ ] If different: update the inline comment to match the new PDF `Note`.
   - [ ] For each getter/setter, compare the PDF `Note` and applicable
         constraints (`constr_*` rows) with the docstring.
   - [ ] If different: update the docstring.
   - [ ] Update the version marker to the new release:
         ```python
         # Spec verified: R24-11
         ```
   - [ ] Run tests to ensure no functional breakage (the docstring-only
         changes should not affect behavior).
   - [ ] Create a commit with message:
         ```
         Updated <ClassName> docstrings for AUTOSAR R24-11
         
         Spec table notes:
         - Class note: "..."
         - attribute1: "..."
         Verified against autosar/markdown/AUTOSAR_CP_TPS_*.md
         ```

### 13.3 During Class Alignment (Initial Synchronization)

When aligning a class to the rules for the first time:

- [ ] Verify **every** class docstring against the PDF `Note` field in its
      spec table (the source is always the PDF, not loose paraphrase).
- [ ] **Terse cross-reference PDF notes.** Some PDF `Note` rows carry only a
      cross-reference (e.g. `MultidimensionalTime` Table 8.22's note reads
      `Specifies a time value based on [20] see [TPS_GST_00354]`) while the
      actual semantic description lives in the XSD complexType documentation
      (`This is used to specify a multidimensional time value based on ASAM CSE
      codes...`). Still **lead the class docstring with the PDF `Note` verbatim**
      (the `[n]` bibliography marker included) and append the XSD complexType
      documentation text as an elaboration paragraph — it is also verbatim spec
      wording, so it satisfies Rule 5 — but never silently substitute the XSD
      text for the PDF `Note`, and never invent prose to "expand" a terse note.
- [ ] Use `autosar/markdown/AUTOSAR_CP_TPS_*.md` as the reference source
      (markdown extracted from the PDF).
- [ ] When writing docstrings, copy the PDF `Note` text verbatim; do not
      paraphrase or abbreviate.
- [ ] Add the version marker to indicate the baseline:
      ```python
      # Spec verified: R23-11
      ```
      This signals to future developers that docstrings were aligned to a
      specific AUTOSAR release and may need review if the spec version changes.

### 13.4 Rationale

Docstring drift is a **silent bug**:
- Code compiles and tests pass even when docstrings are outdated.
- Developers reading the code assume docstrings are current (a reasonable
  assumption).
- Stale docstrings mislead API consumers and maintainers.
- Unlike code bugs, drift is discovered only by manual inspection or explicit
  verification (there is no automatic synchronization between PDF and code).

The version marker and upgrade checklist provide explicit reminders and a
structured process to catch and fix drift at the natural point when AUTOSAR
is upgraded, rather than silently accumulating outdated documentation.

### 13.5 No Automatic Enforcement

There is currently **no CI check** that validates docstrings against the PDF
or detects version skew. This rule relies on:
- Developers' awareness of the synchronization requirement.
- The version marker as a visible signal in the code.
- Manual verification during AUTOSAR upgrades (triggered by the grep search
  above).
- Code review to catch docstring mismatches during PR review.

If automatic tooling is added in the future (e.g., a docstring validator that
parsels the PDF markdown and compares against Python docstrings), this rule
will be updated to incorporate it.

---

## Reference

- Spec sources: `autosar/markdown/*.md` (PDF-derived class tables)
- XSD ground truth: `autosar-pdf/examples/xsd/AUTOSAR_00052.xsd`
- Deviation tracker: `docs/method_deviation_by_class.md`
- General coding standards: `docs/development/coding_rules.md`

## Feedback and Improvements to This Document

As new classes are aligned to these rules, generalize any new observation
directly into the relevant rule above (with a short, anonymized example if
needed) rather than appending a class-specific anecdote — this keeps the
document a lean, reusable reference instead of a growing changelog.
