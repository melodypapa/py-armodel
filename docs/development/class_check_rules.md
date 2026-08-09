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
- [ ] **"`InstanceRef`"-named classes are not automatically refs.** A class
      whose *name* ends in `InstanceRef` and whose attributes are the
      `context`/`target` ref pair still takes its base from the spec `Base`
      column — the name and shape do **not** justify a `RefType` or
      `AtpInstanceRef` base. The spec note may explicitly state that the
      class "follows the pattern of an InstanceRef but is not implemented
      based on the abstract classes" (e.g. `ImplementationElementInParameterInstanceRef`,
      Table 9.7, because `ImplementationDataTypeElement` isn't derived from
      `AtpPrototype`); such a class inherits plain `ARObject` and its
      `context`/`target` Kind-`ref` attributes map to `Optional[RefType]`
      fields with the `Ref` suffix. A wrongly-inherited `RefType` base (a) is
      flagged by `reports/deviation_class_hierarchy_mismatches.md` (expected
      `ARObject`, got `RefType`) and (b) forces the parser/writer into the
      flat-ref serialization shape for what is actually a typed iref
      (Rule 1.7) — silently dropping the inner refs on round-trip.
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
- [ ] **`ARElement` in the `Base` chain means inherit `ARElement`.** When the
      `Base` row lists `ARElement` (e.g. the McFunction/McGroup family:
      `ARElement, ARObject, CollectableElement, Identifiable,
      MultilanguageReferrable, Packageable, Referrable`) and the codebase has
      an `ARElement` base (the abstract `ARElement(PackageableElement, ABC)`
      with `__init__(self, parent, short_name)` in `Identifiable.py`), the
      class inherits `ARElement` — it is the most-derived model class in the
      chain, and aligned `ARElement` subclasses (`ConstantSpecification`,
      `Collection`) are the precedent. Do **not** downgrade to `Identifiable`
      merely because a sibling with the identical `Base` row was previously
      aligned that way (e.g. `McFunction` inherits `Identifiable` although its
      spec `Base` names `ARElement`); treat that sibling as a prior deviation
      to reconcile, not a pattern to copy — `McGroup` inherits `ARElement`.
      The parser/writer need no extra handling either way: an `ARElement`
      package element is read/written with `readIdentifiable`/
      `writeIdentifiable` exactly like an `Identifiable` one, because the
      `IDENTIFIABLE` XML group is shared.
- [ ] The PDF spec is the source of truth for multiplicity and base class.
      When the XSD disagrees with the PDF, follow the PDF.
- [ ] **A `Base` row naming two independent chains selects one role-matching
      branch, not both.** When the `Base` column lists two *parallel*
      inheritance chains (e.g. `ApplicationRuleBasedValueSpecification`:
      `ARObject, AbstractRuleBasedValueSpecification, ValueSpecification`
      — the value-specification branch — alongside `CompositeRuleBasedValueArgument`
      — the composite-argument branch), there is no single "most-derived"
      class across both chains to inherit. Inherit the abstract base the
      codebase already provides for the class's primary role — the one the
      auto-generated `reports/deviation_class_hierarchy_mismatches.md`
      records as its direct parent (here `CompositeRuleBasedValueArgument`) —
      and do **not** mechanically add the second chain via Python multiple
      inheritance: the abstract `ValueSpecification`/
      `AbstractRuleBasedValueSpecification` classes add no state, and the
      composite-argument base is the hub shared with the sibling
      `ApplicationValueSpecification`. A sibling that happened to inherit both
      chains is one modeling choice, not a requirement — match the recorded
      hierarchy parent.

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
      getter/setter is a gap. For an `Identifiable` aggregator, a spec `*`
      `aggr` row still maps to its **own** typed list field even though the
      created children also live in the shared `elements` registry; the getter
      reads that field directly, not a `list(filter(isinstance, elements))`
      view of the registry (see Rule 4).
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
      and account for every field. Two fabrication shapes recur that the
      plain "field appears nowhere in the spec" framing under-describes, and
      both are resolved by **removing** the fabricated field(s) and creating
      the spec-aligned replacement(s), not by recording a deviation: (a)
      **N:1 collapse** — a single generic fabricated field stands in for
      *several* distinct spec attributes (e.g. `AliasNameAssignment.elementRef`
      of type `AnyInstanceRef` collapsed the two mutually-exclusive spec refs
      `identifiable` (Ref→Identifiable) and `flatInstance`
      (Ref→FlatInstanceDescriptor) into one generic instance-ref); the fix is
      N spec-aligned fields, each with its own concrete type and, for refs,
      the proper DEST-typed `RefType` + `Ref` suffix — never one generic
      field. (b) **Shadowing rename** — a field whose *name is invented* but
      shadows a real spec attribute semantically (e.g. `aliasName` (a bare
      `str`) shadowed spec `shortLabel` (a `String` primitive), both meaning
      "the alias name"); there is no spec attribute with the invented name,
      so this is fabrication, not a naming deviation (Rule 1.5), and the fix
      is to rename to the spec name **and** re-type to the spec primitive
      (`str` → `String`) in one step. (c) **Whole-class stub** — *every*
      field is fabricated, so the class models none of its spec attributes:
      one or two loosely-typed generic fields (`someName: str`,
      `someRefs: List[RefType]`) with a complete accessor pair and a
      plausible-sounding docstring, which together make the class look
      implemented while the entire spec table is unrepresented. Shapes (a)
      and (b) still leave *some* spec attribute modeled, so a spot check
      finds real fields; a stub has none, and reviewing "does this field
      look right?" per field never fires because each individual field is
      internally consistent. The fix is a full rewrite from the spec table —
      remove all fabricated fields, add one field + accessor pair per spec
      attribute — not an incremental patch.
      **Cheap detector for shape (c):** a class with **no `# Spec:` line and
      no `# Spec verified:` marker** (Rules 2, 13.1) has never been through a
      field-to-spec pass, so treat its *entire* field set as unverified
      rather than assuming the fields are right and only the marker is
      missing. A pre-rules checklist whose rows are all `[ ]` is the same
      signal. Conversely, do not read a fully-`[x]` checklist as evidence of
      field correctness — the checklist is method-only (Rule 2).
      **Exception — a class with no own spec table is a false positive for
      this detector.** A class whose attributes are XSD-only, with no rendered
      PDF table of its own (Rule 1.5, e.g. a concrete `<name>InstanceRef`),
      legitimately has **no** `# Spec:` line, **no** `# Spec verified:`
      marker, and **all-`[ ]`** rows by rule, not by neglect — exclude classes
      whose deviation tracker row records "no own spec table; attributes from
      XSD group `…`" before applying this detector.
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
      **Release-alignment caveat — a stale XSD flips "omission" to
      "removed".** The keep-it rule above assumes the XSD is release-aligned
      with the class's verified release: its attribute set matches what the
      `# Spec verified:` release renders in the PDF. When the repo's XSD
      predates the class's verified release, an XSD-only attribute can be an
      upstream *deletion* rather than a rendering gap. Check the XSD header
      for its release (`<xsd:documentation>Part of AUTOSAR Release: …` —
      e.g. `docs/requirements/xsd/AUTOSAR_00046.xsd` is CP 4.4.0 / AP 18-10,
      i.e. 2018, while the repo PDFs are CP R23-11): if the XSD release is
      older than the class's `# Spec verified:` release, an attribute present
      only in that XSD (absent from *all* verified-release PDF renderings,
      cross-checked across the multiple PDFs that render the class, e.g. BSW
      Table 12.26 and DiagnosticExtract Table 4.82 both omit
      `DiagnosticIoControlNeeds.didNumber`) is treated like an
      `atp.Status="removed"` attribute — it maps to **no field**, it is
      **not** kept, and the deviation tracker records the reason
      `"removed upstream: present only in the <old-release> XSD, absent from
      the <verified-release> PDF tables; not modeled"` instead of the
      keep-and-record wording. An XSD-only attribute is therefore only kept
      when the XSD is release-aligned (or newer) and the omission is
      genuinely a PDF rendering gap.
      **"Deleted Constraints in R<release>" is NOT an attribute-removal
      signal.** The spec's release-diff appendix (e.g. "G.16.6 Deleted
      Constraints in R23-11") lists *constraints* that were deleted, not
      attributes. A row such as `[constr_1934] Existence of attribute
      SwcInternalBehavior.handleTerminationAndRestart` means the
      mandatory-*existence* requirement was dropped — the attribute itself
      remains in the spec. Do **not** treat this appendix as evidence of
      upstream attribute deletion: an earlier pass misread it and wrongly
      removed `handleTerminationAndRestart`, whose element
      `HANDLE-TERMINATION-AND-RESTART` is present in the XSD with a real
      documentation block (the PDF-omission case, which must be **kept**).
      The valid removal signals remain (a) `atp.Status="removed"` in a
      release-aligned XSD and (b) a stale-XSD-only attribute absent from all
      verified-release PDF renderings **and** from the verified release's own
      XSD — an appendix row is never sufficient on its own. **Integration
      fixtures as a removal check.** `tests/integration_tests/test_files/*.arxml`
      are authoritative reference content and must **not** be edited; if a
      fixture carries the attribute's XML element, the parser/writer must
      keep round-tripping it or the round-trip test's file-comparison step
      fails (3 removed lines became a hard failure). Fixture presence is
      therefore itself strong evidence the attribute is still part of the
      supported surface — resolve that conflict *before* recording a removal.
      **The caveat cuts both ways: a stale-XSD-only attribute that is
      *already modeled* (field + accessor pair + parser/writer element +
      tests) must be **removed** in the same pass, not left in place.**
      `DiagnosticEventNeeds` carried `dtcKind`/`udsDtcNumber` with complete
      fields, accessors, parser/writer reads/writes (`DTC-KIND`/
      `UDS-DTC-NUMBER`), and passing tests — all absent from every R23-11
      rendering of its own table (they were 2018-XSD group members that R23-11
      moved to the sibling `DiagnosticEventInfoNeeds`, Table D.26). The
      aligned action was a **five-place removal**: delete the field and
      accessors, delete the parser `readXxx`/writer `writeXxx` lines that
      emit the element, delete the tests, and record the tracker row as
      `"removed upstream: …; not modeled"` — leaving the field in place and
      merely recording a deviation would keep emitting elements the verified
      release no longer defines. A fully-implemented-and-tested field is
      **not** evidence that the attribute belongs to the class; the
      verified-release table is. When the stale-XSD attribute still exists in
      the verified release **under a different class** (a relocation, e.g.
      `udsDtcNumber` now owned by `DiagnosticEventInfoNeeds`), the receiving
      class may be named in the tracker reason, but the removal from *this*
      class is unconditional — do not keep the field "because the release
      still has the attribute somewhere".
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
      **A `type (spec many vs py single)` (or reverse) row in the deviation
      tracker is a to-fix signal, not an accepted deviation.** It is the
      multiplicity analogue of the Rule 1.5 naming-row anti-pattern: a
      spec-`*` ref modeled as a single field (e.g.
      `DiagnosticEventNeeds.inhibitingSecondaryFidRef` — spec
      `inhibitingSecondaryFid`, mult `*`) is always fixable by converting the
      field and accessors to the list shape (`inhibitingSecondaryFidRefs: List[RefType]`,
      `addInhibitingSecondaryFidRef`/`getInhibitingSecondaryFidRefs`) plus the
      wrapper-element parser/writer (Rule 1.7) and the updated tests — so fix
      it and **remove** the tracker row, exactly like a `naming` row; do not
      leave it recorded as a permanent deviation. A surviving
      `type (spec many vs py single)` row means the field-to-spec
      multiplicity cross-check has not been performed, not that the mismatch
      was reviewed and accepted.
      **A `type (spec many vs py single)` row whose "many" came from the XSD,
      not the PDF, is a stale row to remove, not a real deviation.** The PDF
      table is the source of truth for multiplicity (Rule 1.2), and a PDF Mult
      of `0..1` stays a single-value model even when the XSD element carries
      the attribute-level atpVariation flattening note — "The upper
      multiplicity of this role has been increased to `*` due to resolving an
      atpVariation stereotype" (e.g. `AtomicSwComponentType.internalBehavior`:
      PDF Table 3.8 Mult `0..1`, XSD `INTERNAL-BEHAVIORS` wrapper with the
      note). The `*` is an XSD-only resolution of the stereotype, so the
      single-field model is PDF-correct and the row is dropped — the XSD may
      still serialize it through a wrapper element that holds the single item.
      Only when the PDF Mult column itself reads `*` does the list shape
      apply.
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
      `<name>InstanceRef` types are one case.
      **A class may have no own spec table.** Some classes never get a
      rendered PDF table of their own; their attributes are defined **only**
      in XSD groups. The most common case is a concrete `<name>InstanceRef`
      subclass of the abstract `AtpInstanceRef` (e.g. `RteEventInEcuInstanceRef`
      and `VariableAccessInEcuInstanceRef`, used by
      `McDataAccessDetails.rteEvent`/`variableAccess`), whose inner attributes
      live only in the XSD group (`CONTEXT-ROOT-COMPOSITION-REF`/
      `CONTEXT-ATOMIC-COMPONENT-REF`/`TARGET-…-REF`, sequence offsets 20/30/40),
      but the rule applies to **any** class whose definition cannot be read
      from a PDF table. Rule 1.10's "implement it first" still applies — do
      not defer to a placeholder — but the implementation is XSD-driven rather
      than table-driven: inherit the abstract parent the XSD `Base`/type names
      (e.g. `AtpInstanceRef`, whose own `atpBase`/`atpContextElement`/
      `atpTarget` are `atpDerived`) and model the concrete inner refs as
      `Optional[RefType]` fields with the plain `Ref` suffix. **Because there
      is no own spec table, the checklist cannot be confirmed: the class
      carries no `# Spec:` line and no `# Spec verified:` marker, and every
      row stays `[ ]` — impl, docstring, and test all unchecked.** Nothing
      about a class with XSD-only attributes is confirmed against a PDF table,
      so citing the **introducing aggregator's** table (e.g.
      `McDataAccessDetails` Table 9.12) in the `# Spec:` line would falsely
      claim a PDF provenance the class does not have; do **not** set it.
      Record "no own spec table; attributes from XSD group `…`" in the
      deviation tracker. The `[ ]` rows are a *provenance* statement
      (unverified against PDF), not a claim that the implementation is absent
      — the methods are implemented and tested, but they are deliberately not
      marked `[x]` until a PDF table exists to confirm them against. Only when
      the class's model is genuinely out of scope is a placeholder allowed; it
      must then forward-reference the real class in the inline comment and in
      the getter/setter docstrings, and be recorded in
      `docs/method_deviation_by_class.md` as "class not yet implemented". When
      the class is implemented, switch the field/getter/setter annotation to
      the concrete type (with a `TYPE_CHECKING` import if needed to avoid
      cycles) and clear the deviation.
- [ ] **Empty-attribute rendering ≠ "no own spec table" (the most common
      misapplication of this exception).** This exception is triggered by the
      *absence of any rendered PDF table*, not by the *absence of own
      attributes*. A class can have its **own** rendered PDF `Class` table
      (with `Package` / `Base` / `Note` rows and an `Attribute` column whose
      only row is a `-` / empty row) while contributing **zero new
      attributes** — every attribute is inherited from its `Base` chain (e.g.
      an `IdentCaption` subclass such as `BswServiceDependencyIdent`,
      `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf` Table 5.16, whose Base
      ends in `IdentCaption` → `Identifiable` → `Referrable` and whose
      `Attribute` section is empty). Such a class is **not** covered by this
      exception: it has a spec table, so it **does** carry a `# Spec:` line +
      `# Spec verified:` marker (Rules 2 / 13.1), and its method-parity
      checklist lists **only the methods the class itself defines** — which,
      when the class adds no accessors, is just `__init__`. Those checklist
      rows are crossed `[x]` once implemented/docstringed/tested exactly like
      any other class; they do **not** stay `[ ]`. The reliable tell that a
      class is the *real* exception (no own table) rather than an
      empty-rendering class is whether a PDF `Class <Name>` heading exists for
      it at all — grep the markdown for `^Table .*: <ClassName>` (or
      `| Class   | <ClassName>`). If that heading exists, the class has its own
      table and must be treated as the empty-rendering case; if it exists
      nowhere in any PDF, it is the XSD-only case. Do not let "the class has
      no attributes of its own" shortcut the decision — that wording describes
      the *superclass contribution*, not the *table existence*, and the two
      are independent.
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
- [ ] **A name mismatch is fixed by renaming, not recorded as a `naming`
      deviation.** A field/accessor whose base name does not match the spec
      `Attribute` column (e.g. spec `aliasName` modeled as `alias`/`aliases`,
      or `targetRef` modeled as `target`) is always fixable — unlike a type
      or multiplicity deviation that the XML representation can force, a name
      has no such constraint. Recording such a mismatch as a `naming`
      deviation row in `docs/method_deviation_by_class.md` and leaving it
      there indefinitely is an anti-pattern that mirrors the "fabricated
      attribute recorded instead of removed" smell (Rule 1.3): it documents a
      bug rather than fixing it. The aligned action is to **rename** the
      field and its accessors (and the checklist rows) to the spec base name,
      update every consumer, and **remove** the `naming` deviation row — do
      not leave a stale `naming` row once the name is corrected. A surviving
      `naming` row in the tracker is itself a signal that the field-to-spec
      cross-check has not actually been performed; treat it as a to-fix, not
      as an accepted gap.

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
      **A working `setXxx(value)` setter is still a violation when the child
      is `Referrable`.** An existing `setXxx`/`getXxx` pair for a `0..1`
      aggregated child whose `Base` lists `Referrable` is misaligned even when
      it is implemented, guarded, and tested (e.g. `AtomicSwComponentType`
      held `setSymbolProps`/`getSymbolProps` for `symbolProps`, whose child
      `SymbolProps` Base is `ARObject, ImplementationProps, Referrable`).
      Migrate the accessor pair to `createXxx(short_name)` +
      `getXxx()`, update the tests that call the old setter, and wire the
      parser/writer through the factory — passing tests for the old shape are
      not evidence the shape is right.
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
- [ ] **An abstract aggregated child gets one `createXxx<Subtype>(short_name)`
      factory per concrete subtype, whatever the multiplicity.** When the
      spec `Attribute` type is an *abstract* class with concrete subtypes
      (e.g. `TracedFailure` (abstract) → `DevelopmentError`/`RuntimeError`/
      `TransientFault`), the aggregator cannot expose a single
      `createTracedFailure(short_name)` — the abstract type is not
      instantiable — nor a plain `addTracedFailure(value)` (the parser has
      no way to know which subtype to build from a bare value). Instead it
      exposes one factory per concrete subtype, each writing the same
      slot/list: for `0..1` (e.g. `DiagnosticEventNeeds.diagEventDebounceAlgorithm`)
      `createDiagEventDebounceCounterBased(short_name)`/`…MonitorInternal`/`…TimeBased`
      each assign the single field; for `*` (e.g.
      `ErrorTracerNeeds.tracedFailure`) `createDevelopmentError(short_name)`/
      `createRuntimeError(short_name)`/`createTransientFault(short_name)`
      each append to the `tracedFailures` list and return the created (or
      existing, per Rule 4) element. The parser dispatches on the XSD child
      element tag (`DEVELOPMENT-ERROR`/`RUNTIME-ERROR`/`TRANSIENT-FAULT`)
      to the matching factory; the writer dispatches on `isinstance`. This
       is the polymorphic-dispatch shape of Rule 1.7 applied to an *aggregated
       child* — the list case differs from a plain `*` list only in that the
       parser's per-item element tag selects the subtype factory instead of
       an `addXxx` call.
- [ ] **An already-aligned sibling is not an authority on accessor shape.**
      When a fully `[x]` sibling models a spec-`*` member with a single-value
      shape (`setXxx`/`getXxx`), it is a prior deviation, not a template: the
      shape rule above (plural `addXxx`/`getXxxs` for `*`) wins. Example:
      `ApplicationValueSpecification` (sibling of
      `ApplicationRuleBasedValueSpecification`) models `swAxisCont` (`*`,
      `RuleBasedAxisCont`) with `setSwAxisCont`/`getSwAxisCont`; the
      `*`-shape rule says the correct form is `addSwAxisCont`/`getSwAxisConts`
      over a `swAxisConts: List[...]` field. Align the class being worked on
      to the rule, and record the sibling as a deviation to reconcile later —
      do not copy its shape.
- [ ] **A factory named after the child type does not make a `*` member
      "missing" — the tracker heuristic keys on the member name, not on
      Rule 1.6's factory name.** For a `*` aggr member whose child type's base
      name differs from the member's (e.g. `ClientServerInterface.possibleError`
      of type `ApplicationError`), the factory is correctly named after the
      child type (`createApplicationError`) while the getter is correctly
      named after the member (`getPossibleErrors`). A member-matching script
      that searches accessors for the member base name (`possibleError`) will
      find the getter but not the child-type-named factory and can flag the
      member as `missing` in `docs/method_deviation_by_class.md`. That row is
      **stale — remove it**, do not rename the factory to
      `createPossibleError` and do not record a `naming` deviation: the
      member is implemented, parser/writer-wired, and tested. The checklist
      rows carry the truth (`createApplicationError`, `getPossibleErrors`); a
      `missing` row surviving for a member that has both a factory and a
      getter is a stale-row signal (Rule 1.4/1.5's stale-row guidance applies
      to `missing` rows as much as to `type`/`naming` rows).

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
      **A shared child reader/writer helper's existence is not evidence that
      every aggregator of that child uses it.** When the child type has a
      dedicated `readXxx`/`writeXxx` pair already in the parser/writer (written
      for a sibling aggregator, e.g. `readSymbolProps`/`writeSymbolProps` used
      by `ImplementationDataType`), a *different* aggregator of the same child
      can still silently drop it — its own `readXxx`/`writeXxx` must be grepped
      for a call to the child helper (e.g. `AtomicSwComponentType.symbolProps`
      was dropped because `readAtomicSwComponentType`/`writeAtomicSwComponentType`
      never called the existing `readSymbolProps`/`writeSymbolProps`). For an
      aggregated child the wiring is one `createXxx(short_name)` call per
      occurrence in the reader plus one `writeXxx` call per field in the
      writer — grep each aggregator's reader/writer, not just the parser/writer
      for the element tag, and wire the child helper in when the call is
      missing.
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
      The five-place pattern applies unchanged to a **top-level package
      element** (a class whose spec `Aggregated by` row reads
      `ARPackage.element`, e.g. `McFunction`): the aggregator is `ARPackage`,
      which must gain `createXxx(short_name)`/`getXxxs()` and their checklist
      rows; the parser branch goes in `readARPackageElements` (the tag-name
      chain), the writer branch in `writeARPackageElement` (the
      `isinstance` chain), and the dispatch test in the parser-dispatch test
      file. A package element that has **no** dispatch branch at all is
      silently dropped on round-trip even when its model and mirrored tests
      are complete — grep the parser and writer for the element tag before
      declaring the class aligned.
- [ ] **Polymorphic dispatch nests — a concrete subtype that itself
      aggregates is its own level of dispatch.** The five-place pattern
      applies at the top-level aggregator; a subtype that owns an aggregated
      or polymorphic attribute is *itself* a dispatcher with its own factory
      + parser loop + writer loop + dispatch tests for its children (e.g.
      `ErrorTracerNeeds.tracedFailure` dispatches
      `TRACED-FAILURES` → `DEVELOPMENT-ERROR`/`RUNTIME-ERROR`/`TRANSIENT-FAULT`,
      and the `TransientFault` subtype in turn dispatches its own
      `POSSIBLE-ERROR-REACTIONS` → `POSSIBLE-ERROR-REACTION` at the next
      level). Cover each level independently: the outer dispatch tests assert
      every outer subtype is routed, and the inner level has its own
      wrapper-list round-trip tests. Do not assume covering the outer level
      exercises the inner one — an aligned `transientFault` parse reads
      `POSSIBLE-ERROR-REACTIONS` from *its own* element, unrelated to the
      outer `TRACED-FAILURES` loop.
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
      iref element. A third, sneakier shape is to treat the typed iref as a
      **plain ref**: because the iref class name ends in `InstanceRef`, it may
      inherit `RefType` and be serialized with the flat-ref helpers
      (`getChildElementOptionalRefType`/`setChildElementOptionalRefType`),
      which read/write the attribute-named element as a ref (its text
      content) and never touch the inner refs — they vanish on round-trip
      while the iref element itself survives and the model still carries the
      iref object, so a unit-level get/set test passes. The parser must
      construct the iref class and read the inner refs directly under the
      attribute-named element, and the writer must emit them there
      (`McDataInstance.instanceInMemory` → `<INSTANCE-IN-MEMORY><CONTEXT-REF>…</CONTEXT-REF><TARGET-REF>…</TARGET-REF></INSTANCE-IN-MEMORY>` —
      no nested `<IMPLEMENTATION-ELEMENT-IN-PARAMETER-INSTANCE-REF>` wrapper,
      no flat text). Check the XSD element's `type` attribute to tell a typed
      iref from a plain `REF` element (which has `simpleContent` + `DEST`
      instead of a class `type`); the base-class fix is Rule 1.2.
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
      **`-REF-CONDITIONAL` items (atpVariation directed associations).** Some
      `ref` wrappers hold `<NAME>-REF-CONDITIONAL` items instead of plain
      `<NAME>-REF`: the element group's `mmt.qualifiedName` still names the
      attribute, but each item is a conditional-ref element with an inner
      `<NAME>-REF` and an optional CONDITION/VARIATION-POINT child
      (e.g. `SupervisedEntityNeeds.checkpoints` → `CHECKPOINTSS` wrapper →
      `SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF-CONDITIONAL` items → inner
      `SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF`). The codebase convention is
      uniform with all other conditional-ref usages: model the attribute as
      plain `List[RefType]` (the condition/variation-point is dropped — the
      XSD type name `<NAME>-REF-CONDITIONAL` is a framework-generated
      directed-association wrapper, not a class to implement), parse with
      `getChildElementRefTypeList(element, "WRAPPER/NAME-REF-CONDITIONAL/NAME-REF")`,
      and write by emitting the wrapper only when non-empty with one
      `NAME-REF-CONDITIONAL` per entry containing the inner `NAME-REF`
      (mirroring `writeBswModuleEntityIssuedTriggerRefs`). The already-plural
      base keeps its plural form: `checkpoints` → field `checkpointsRefs`,
      `addCheckpointsRef`/`getCheckpointsRefs` (Rule 1.5).
      Read the item tag from the XSD `choice`/element declaration — do not
      derive it from the attribute name or the type name by rule of thumb.
      An **iref** wrapper follows the same container pattern: the wrapper is
      `<BASE>-IREFS` and each item is `<BASE>-IREF` — the item tag is the
      attribute base plus `-IREF`, **not** the `<name>InstanceRef` type name
      (e.g. `McDataAccessDetails.rteEvent` `*` → `<RTE-EVENT-IREFS>/<RTE-EVENT-IREF>`,
      where the item's XSD type is `RTE-EVENT-IN-ECU-INSTANCE-REF`). Each item
      is a concrete `<name>InstanceRef` object whose inner refs are read/written
      **directly under the item element** (flat, no nested wrapper), via a
      per-iref `readXxx`/`writeXxx` pair wired into the iref-list loop.
      Parser: iterate `self.findall(element, "WRAPPER/ITEM")` and build each
      item object via the aggregator's `addXxx`/`createXxx`. Writer: create
      the wrapper only when the list is non-empty and emit one item element
      per entry. When an aggregated child is itself not yet aligned to its
      own spec table, still parse/emit the item element **by identity only**
      (the `SHORT-NAME` for `Identifiable` children; an empty element for
      plain `ARObject` children) rather than serializing placeholder fields —
      this keeps the XML schema-valid and the round-trip lossless at the
      aggregator level, and is recorded in the deviation tracker pending the
      child's own pass.
- [ ] **`atpVariation` classes wrap their attributes in a
      `VARIANTS/CONDITIONAL` element.** When the spec class header carries
      `<<atpVariation>>` (e.g. `McFunctionDataRefSet` Table 9.9, `LinCluster`,
      `CanCluster`), the PDF `Attribute` rows render on the class itself, but
      the XSD group contains only a `<NAME>-VARIANTS` wrapper holding a
      `<NAME>-CONDITIONAL` choice; the class's real attributes (and a
      `VARIATION-POINT`) live in the conditional's content group. The
      established model pattern reads/writes the conditional **transparently
      into the owning object** — no separate `Conditional` model class, no
      modeled `variationPoint`: the parser does
      `find(element, "NAME-VARIANTS/NAME-CONDITIONAL")` and reads the
      attributes from that element; the writer emits
      `<NAME>-VARIANTS/<NAME>-CONDITIONAL` around the attributes (as
      `writeLinCluster` does). A deviation tracker that lists
      `mcFunctionDataRefSetVariant`/`McFunctionDataRefSetConditional` as a
      "missing" attribute reflects the alternative explicit
      `Variants: List[...]` modeling; the transparent wrapper is
      codebase-consistent and schema-valid — pick one shape and record the
      choice in the tracker, do not leave a `missing` row for the unwrapped
      variant.
      **Attribute-level `atpVariation` is not the same as a class-level
      `<<atpVariation>>` header.** When the *attribute's* `Note` lists
      `Stereotypes: … atpVariation` (e.g. `ErrorTracerNeeds.tracedFailure`,
      whose Note reads "Stereotypes: atpSplitable; atpVariation"), the
      stereotype is resolved at the XSD by *flattening the multiplicity* —
      the XSD `documentation` even says so: "The upper multiplicity of this
      role has been increased to `*` due to resolving an atpVariation
      stereotype" — into a **plain wrapper list** (`<TRACED-FAILURES>` with
      `DEVELOPMENT-ERROR`/`RUNTIME-ERROR`/`TRANSIENT-FAULT` items, Rule 1.7),
      **not** a `VARIANTS/CONDITIONAL` wrapper. Only the *class-header*
      `<<atpVariation>>` stereotype produces the `VARIANTS/CONDITIONAL`
      shape. Before assuming a conditional wrapper, check the XSD group for a
      `<NAME>-VARIANTS` element: an attribute-level stereotype whose XSD
      group has no `-VARIANTS` element is the ordinary wrapper-list pattern.
- [ ] **Identity-only child serialization is a debt to be repaid by the
      child's own pass.** The identity-only shape above is deliberately
      lossy for everything except the item's existence, and for a plain
      `ARObject` child it degenerates to an **empty element**: the parser
      constructs a bare instance and ignores the element's contents, and the
      writer emits an item element with no children. Round-trip tests then
      pass while asserting only `len(getXxxs()) == n`, so nothing fails when
      the child's real attributes are dropped. When the child's own alignment
      pass lands, that placeholder must be replaced **in the same change** by
      a real `readXxx`/`writeXxx` pair for the child, wired in from the
      aggregator's loop — an aligned model whose aggregator still emits the
      empty element is a Rule 1.7 violation, not a completed pass. Verify by
      grepping the aggregator's loop for a bare `ET.SubElement(wrapper,
      "ITEM")` with no following `self.writeXxx(...)`, and for a parser loop
      whose body constructs the child but never reads from `child_element`
      (a loop variable that is bound and never used is the tell — flake8's
      `F841`-adjacent smell that the linter does not flag for `for` targets).
      Extend the aggregator's existing round-trip test to assert the child's
      *field values*, not just the list length, so the lossy shape cannot
      return unnoticed.
- [ ] **Aggregator serialization sequenced after the child's alignment.**
      The bullet above covers an aggregator that is *already* wired into a
      parser/writer dispatch and merely emits its not-yet-aligned child by
      identity. The harder case is an aggregator with **zero existing
      serialization** — no `readXxx`/`writeXxx`, no dispatch branch — whose
      *only* aggregated child type is itself not yet aligned (e.g.
      `AliasNameSet` aggregates a single `aliasName` of type
      `AliasNameAssignment`, which still carries fabricated attributes and is
      missing its spec attributes). Fully serializing the aggregator now
      would persist the child's wrong shape, so the aggregator's parser/writer
      coverage (and its dispatch wiring into the owning `ARPackage.element`
      reader/writer) is **sequenced after** the child's own alignment pass
      (Rule 1.10) and recorded as *pending* in the deviation tracker — not
      skipped and not implemented against a placeholder child. Align the
      aggregator's **model** fully in the meantime (base class, field,
      accessors, tests, docstrings — every rule except 1.7); only the
      serialization is deferred, and the tracker row names the blocking child
      so the sequencing is explicit.
- [ ] **A shared `readXxx`/`writeXxx` helper that calls
      `readIdentifiable`/`writeIdentifiable` is not automatically reusable by
      every sibling subtype of the abstract base it was written for.** When an
      abstract spec class (e.g. `ServiceDependency`) has two concrete
      subtypes and the existing helper for the base was modeled after the
      *first* subtype (`SwcServiceDependency`, whose complexType includes the
      `IDENTIFIABLE`/`REFERRABLE` groups), do not assume the second subtype
      shares that shape. Check the second subtype's own XSD complexType
      sequence: if it lists only `AR-OBJECT` + the base group + its own group
      (e.g. `BswServiceDependency` = `AR-OBJECT` + `SERVICE-DEPENDENCY` +
      `BSW-SERVICE-DEPENDENCY`, with **no** `IDENTIFIABLE`/`REFERRABLE`), the
      class has no `SHORT-NAME` and must not call `readIdentifiable`/
      `writeIdentifiable` — write a dedicated `readXxx`/`writeXxx` pair that
      calls `readARObjectAttributes`/`writeARObjectAttributes` instead, and
      reads/writes only that subtype's own group elements directly. A
      non-`Referrable` class that still needs to be the *target* of a
      reference typically has a companion `<Name>Ident` class implementing
      `IdentCaption` (itself `AtpStructureElement`) for that purpose (e.g.
      `BswServiceDependencyIdent`) — model it as a nested attribute
      (`ident: <Name>Ident`), not as the class's own identity.

- [ ] **Inherited base attributes must be traced to an element in the subtype's
      *effective* element set, not just to the model field.** A concrete
      subtype that reuses or mirrors an abstract base's reader/writer can
      silently drop an inherited base attribute the method-parity checklist
      cannot see (Rule 1.7). Two distinct failure shapes:
      1. **Inherited attribute has an XSD element but no reader/writer.** The
         base group the subtype's complexType references *does* declare the
         element (e.g. an inherited `symbolicNameProps` whose base group has
         `SYMBOLIC-NAME-PROPS`), yet neither the base `readXxx`/`writeXxx` nor
         the subtype's `readXxx`/`writeXxx` emit it — the attribute is dropped
         on round-trip. The base group's mere presence in the complexType is
         **not** proof of coverage: grep the base *and* subtype reader/writer
         for the element tag. If an inherited attribute with an XSD element
         has no reader/writer, record it as a deviation — never claim
         "parser/writer coverage".
      2. **Attribute is in the spec table but absent from the XSD group.** An
         attribute the PDF lists on the base class may have **no** element in
         the base XSD group at all (a model-only / `atpDerived`-style
         attribute with no serialization element). That is a *known deviation*
         to declare, not a coverage gap to "fix" by inventing a reader/writer.
      In both cases the deviation tracker must name the inherited attribute
      explicitly; a "No deviations" claim for a subtype that inherits
      unserialized base attributes is inaccurate.

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
      referencing attribute against it.       This applies to **every** kind of
      referenced class, not only `<name>InstanceRef` types (see the `iref`
      specifics in Rule 1.5).
- [ ] **A referenced class that *exists* but is a stub counts as missing.**
      This rule's trigger is not "the name resolves" but "the class models
      its spec table". A referenced type that imports cleanly yet carries
      only fabricated fields (Rule 1.3 shape (c)) gives the referencing
      attribute a correct *type* and a worthless *shape*, so aligning the
      referencing class against it produces a class that is aligned on paper
      and still round-trips nothing. Before typing an attribute against an
      existing class, check that class for a `# Spec:` line and a
      `# Spec verified:` marker; if either is absent, align it first in the
      same pass — the aggregated child's alignment is **in scope**, not a
      follow-up. This keeps the pass self-contained: aligning a parent whose
      child is a stub otherwise immediately re-opens as the Rule 1.7
      identity-only debt above.
      **The same test applies to a referenced enum attribute type.** An
      existing enum whose members exist but do **not** match its own
      `Enumeration` spec table gives the referencing attribute a correct
      *type* and wrong *values*: the member set and/or member strings are
      placeholder-shaped (e.g. `MaxCommModeEnum`'s `FULL_COMMUNICATION =
      "full-communication"` before alignment, while spec Table 13.6 defines
      the literals `full`/`none`/`silent`), so the referencing class aligns on
      paper and serializes garbage enum values. Realign the enum against its
      own table (Rule 12) in the same pass — rename members to the spec
      literals' UPPER_CASE form and correct the values — and update its
      checklist/marker; the referencing class's accessor annotations then
      simply retype to the corrected enum.
      **A stub can be a whole *family* — align the transitive closure, not
      just the directly-referenced child.** When the spec `Attribute` type
      is an abstract class whose own `Subclasses` row names concrete
      subtypes, and those subtypes aggregate yet another class, a
      placeholder implementation may stub **the entire family**: the
      abstract base and every subtype as plain `ARObject` with `__init__(self)`
      and invented fields that appear in no spec table (e.g.
      `ErrorTracerNeeds.tracedFailure` → abstract `TracedFailure` with
      fabricated `failureCode`/`failureDescription`, its subtypes
      `DevelopmentError`/`RuntimeError` with fabricated
      `errorCode`/`errorDescription`, `TransientFault` with fabricated
      `faultCode`/`faultDescription`, and the missing XSD-only
      `PossibleErrorReaction`). The stub-family fix is one coordinated
      pass over the closure, driven by each class's own spec `Base` column:
      realign the abstract base to its spec base (`TracedFailure` →
      `Identifiable, ABC` with `__init__(self, parent, short_name)` and its
      real `id` attribute), re-type every subtype to inherit it
      (`DevelopmentError(TracedFailure)`, …), delete all fabricated fields
      (Rule 1.3), implement the missing XSD-only grandchild first
      (`PossibleErrorReaction`, Identifiable-based, `reactionCode`), and add
      the aggregator's per-subtype create factories + parser/writer dispatch
      (Rule 1.6/1.7). Do **not** stop after aligning only the directly
      referenced child — a subtype left as an `ARObject` stub with invented
      fields silently round-trips nothing even though the parent's list is
      "aligned".
      **Sibling subtype tables can carry a copy-pasted spec Note.** When one
      subtype's table `Note` is a verbatim duplicate of a sibling's (e.g.
      `TransientFault` Table E.50 and `RuntimeError` Table 12.39 both read
      "The reported failure is classified as runtime error."), mirror each
      table's own Note verbatim in that subtype's docstring — do **not**
      "fix" the duplication by inventing a distinct description. Each
      subtype's docstring is a provenance statement of *its* table, and the
      subtypes may live in different PDFs (Rule 1.11).
      **Exception — a class with no own spec table is not a stub.** A
      referenced class whose attributes are XSD-only, with no rendered PDF
      table of its own (Rule 1.5, e.g. a concrete `<name>InstanceRef`),
      legitimately has **no** `# Spec:` line and **no** `# Spec verified:`
      marker — that absence does **not** mean it is unaligned. Only the
      missing markers of a class that *should* have a spec table (its
      attributes are PDF-defined) signal a stub. Before flagging a referenced
      class, check its deviation tracker row for "no own spec table;
      attributes from XSD group `…`" (mirroring the Rule 1.3 detector
      exclusion).
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
      rows are displayed in the PDF** — the order you read top-to-bottom when
      you open the table. The order of the `__init__` fields, the order of
      the getter/setter/adder methods, and the order of the method parity
      checklist rows (Rule 2) must all follow that displayed row order, **not**
      alphabetical-by-Python-name or file-of-creation order. A class whose
      accessors are ordered by name or by refactor history rather than by the
      spec is misaligned.
      The `Tags: xml.sequenceOffset=NN` value is only a **secondary signal**:
      it usually *agrees* with the displayed row order (most tables are
      rendered in ascending-offset order, e.g. `EngineeringObject` shows
      `shortLabel`(10), `category`(20), `revisionLabel`(30), `domain`(40) and
      the accessors/checklist follow exactly that sequence). But the two can
      **diverge**: some PDF tables are rendered alphabetically (or otherwise)
      so the displayed rows are *not* in ascending-offset order. In that case
      the **displayed row order wins** — it is literally "the order in the
      PDF". Do **not** reorder by `sequenceOffset` when the table prints
      otherwise. (Counter-example: `AliasNameAssignment` Table 9.3 prints its
      rows `flatInstance`/`identifiable`/`label`/`shortLabel` even though their
      offsets are 60/50/20/10; the aligned class therefore declares
      `flatInstanceRef`, `identifiableRef`, `label`, `shortLabel` in that
      order — the reverse of ascending offset.) Always read the actual
      PDF/markdown row order; never assume it from the offset values. Note
      that this is purely a **Python source-ordering** convention (fields,
      methods, checklist); the parser/writer still emit XML elements in the
      XSD's `sequenceOffset` order regardless of how the model members are
      declared.
      Because the two orders diverge routinely, **write them down separately**
      when they do: the PDF row order drives the Python member sequence, and
      the XSD element sequence (`sequenceOffset` ascending, negatives first)
      drives the order of `setChildElementXxx` / `getChildElementXxx` calls in
      `writeXxx`/`readXxx`. A common divergence is an alphabetically-rendered
      table whose `shortLabel`/`category` rows print *last* while their
      offsets (`-100`/`-90`) put them *first* in the XML — writing the
      parser/writer in the class's member order then emits elements out of
      XSD sequence, which a round-trip test through this library will not
      catch (the reader is order-insensitive) but a schema validator will.
      Derive the serialization order from the XSD group, never from the PDF
      table or the Python member order.
- [ ] **Page-split tables: the displayed order is the concatenation of the
      per-page row groups.** A table that spans PDF pages renders its class
      header and some rows on one page, then the caption and the remaining
      rows on the next (e.g. McGroup Table 9.10 splits as `mcFunction`
      (offset 40) + `refCalprmSet` (20) on page 1, then `refMeasurementSet`
      (30) + `subGroup` (10) on page 2). The displayed row order is the
      concatenation — first page's rows, then next page's rows —
      `mcFunction, refCalprmSet, refMeasurementSet, subGroup` — which is
      **not** ascending `sequenceOffset` (10, 20, 30, 40) and not a
      refs-then-aggr grouping. Read the rows in the order the pages render
      them and use that concatenation for the Python member/checklist order;
      the XSD offsets still drive serialization order as usual.
- [ ] **Multi-PDF cross-check.** A class's spec table can appear in more than
      one PDF (e.g. McGroup is rendered as both BSWModuleDescriptionTemplate
      Table 9.10 and SystemTemplate Table F.74). When choosing the displayed
      row order, verify every rendering shows the same order — the split
      arrangement can differ between PDFs even when the attribute rows are
      identical, so base the member order on the agreement, not on one
      document's pagination.
- [ ] **A polymorphic family can span PDFs — each subtype cites its own
      table.** The abstract parent and some subtypes may render in one PDF
      while another subtype's table lives in a different one (e.g. the
      `TracedFailure` family: the abstract base plus `DevelopmentError`/
      `RuntimeError` are BSWModuleDescriptionTemplate Tables 12.36–12.39,
      while `TransientFault`'s own table — carrying its sole
      `possibleErrorReaction` attribute — is SoftwareComponentTemplate Table
      E.50). When aligning a subtype, do **not** cite the parent's table or
      read its attributes from the parent's rows: search the other PDF for
      the subtype name and use *its* table for the `# Spec:` citation, the
      member order, and the attribute set. A subtype's own attributes are
      invisible if you only read the family's parent table.
- [ ] **Group accessors per attribute, in spec row order** — the accessor
      pair(s) of one attribute are contiguous, immediately followed by the
      next attribute's pair(s), and the checklist rows (Rule 2) follow that
      same sequence. A class whose accessors are grouped by *method kind*
      instead (all `create*`/`add*` factories together, then all `get*`
      getters together) violates this even when every method is present and
      the checklist is complete — e.g. `ClientServerInterface` (PDF order
      `operation`, `possibleError`) must read `createOperation`,
      `getOperations`, `createApplicationError`, `getPossibleErrors`, **not**
      `createOperation`, `createApplicationError`, `getOperations`,
      `getPossibleErrors`. The grouped-by-method-kind shape is easy to miss
      because the set-based check (Rule 2/7) is order-blind, so verify the
      *source order* of methods against the spec rows explicitly.
      Within one attribute the pair order depends on the accessor kind:
      1. **Scalar pair** (`getXxx`/`setXxx`): **getter first** —
         `getName`/`setName`, `getOptions`/`setOptions` (the `Compiler`
         precedent).
      2. **List/aggregated pair** (`addXxx`/`getXxxs` or
         `createXxx`/`getXxxs`): **mutator first** —
         `addEmulationSupport`/`getEmulationSupports`,
         `createMcParameterInstance`/`getMcParameterInstances`
         (`McSupportData`), `createOperation`/`getOperations`
         (`ClientServerInterface`). The "getter before setter" rule for the
         scalar shape applies *only* to `getXxx`/`setXxx`; do **not** read it
         as requiring `getOperations` before `createOperation` (that would
         contradict the aligned `addXxx`/`getXxxs` convention, which always
         writes the mutator that *builds* the element before the getter that
         *reads* the resulting list).
      Only the *attribute* sequence varies, and that sequence comes from the
      PDF.

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
      **Placeholder member shapes are the common wrong-set failure.** A
      placeholder enum from an earlier stage often keeps the *right number* of
      members with plausible-but-invented values — hyphenated or suffixed
      values (`full-communication` for spec `full`), paraphrased names
      (`FULL_COMMUNICATION` for spec `FULL`), or values split/joined differently
      than the spec literal. A right-count/wrong-value enum passes a
      member-count check and a spot check of "are there members?", so verify
      each member's string value 1:1 against the `Literal` column (the XSD
      `mmt.qualifiedName` tag is the same camelCase literal, e.g.
      `MaxCommModeEnum.full`) and the member name against the literal's
      UPPER_CASE conversion.
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
- [ ] Class docstring: lead with the spec table's "Note" row **verbatim**, the
      same as a class docstring (13.2 Step 3) — do **not** paraphrase or
      summarize it into invented prose. The enum's purpose and scope are the
      Note; a "summarize the purpose" instruction invites a loose paraphrase
      that drifts from the PDF wording (the `ServerArgumentImplPolicyEnum`/
      `ArgumentDirectionEnum` passes showed the correct shape: a verbatim,
      wrapped Note, e.g. `ArgumentDirectionEnum`'s "Use cases: • Arguments in
      ClientServerOperation can have different directions …" exactly as
      written).
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
- [ ] `npm run ruff-check` passes for the file (the broader `E`/`F`/`W`/`I`
      set, including unused-import `F401` that the syntax-only flake8 set skips).
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
- [ ] **A spec-`*` aggregated attribute on an `Identifiable` aggregator is
      backed by a dedicated typed list field, not by filtering the shared
      `elements` registry.** Rule 1.3 ("every spec attribute maps to a field")
      applies even when the created children also live in the `elements`
      registry for short-name lookup: each spec `*` `aggr` row maps to its
      **own** field (`self.operations: List[ClientServerOperation] = []`,
      `self.possibleErrors: List[ApplicationError] = []`), declared in
      `__init__` in spec row order with the spec `Note` as its comment
      (Rule 13.2 Step 4.2). The `createXxx(short_name)` factory appends to
      that field **in addition to** `addElement` (keeping the registry and
      the field in sync), and `getXxxs()` returns the field **directly** —
      never `list(filter(lambda c: isinstance(c, Xxx), self.elements))`.
      Filtering the registry on every getter call has two defects: (a) it
      gives the spec attribute no model field of its own, so the
      field-to-spec cross-check (Rule 1.3) finds the attribute unmodeled;
      and (b) it discriminates by Python type rather than by spec role, so
      two spec attributes whose children share a base type would collapse
      into one filtered list. The dedicated-field shape is the established
      sibling pattern (`ParameterInterface.parameters`, and now
      `ClientServerInterface.operations`/`possibleErrors`). The `elements`
      registry still does the factory's "return existing on same short
      name" job (`IsElementExists`/`getElement`, above) — registry and
      field coexist, each for its own purpose; only the getter reads the
      field.
- [ ] **An `Identifiable` aggregator that handles its members *only*
      through the `elements` registry is a to-fix, not an accepted shape.**
      The tell-tale is a getter of the form
      `list(filter(lambda c: isinstance(c, Xxx), self.elements))` (or
      `sorted(filter(isinstance(...), self.elements), ...)`) for a spec `*`
      `aggr` attribute that has **no** dedicated field in `__init__` — the
      class borrows the inherited registry as its only storage and
      re-derives each attribute's membership by Python type on every call.
      This is both a Rule 1.3 violation (the spec attribute has no model
      field of its own) and a Rule 4 violation (the getter does not read an
      own field), and it survives a fully-`[x]` checklist plus
      parser/writer coverage exactly like the fabricated-attribute /
      stale-row anti-patterns do — so do **not** treat a complete checklist
      or a passing round-trip as evidence the shape is right. Migrate it in
      one pass, per spec attribute row:
      1. add the dedicated typed list field in `__init__`, in spec row
         order, with the spec `Note` as its comment
         (`self.operations: List[ClientServerOperation] = []`);
      2. make the `createXxx(short_name)` factory **append** the new
         instance to that field right after `addElement` (the
         `IsElementExists`/`getElement` duplicate check stays on the
         registry);
      3. rewrite `getXxxs()` to `return self.<field>` (drop the
         `isinstance` filter entirely); and
      4. assert the field's `[]` default in the test (Rule 7) so the new
         `__init__` field is covered.
      The parser/writer need no change — they already call `createXxx`/
      `getXxxs`, which now flow through the dedicated field. The previously
      recorded deviation row (if any) for the attribute is removed once the
      field is added, since the attribute is now modeled. `ClientServerInterface`
      is the worked example (migrated from the registry-filter shape to
      `self.operations`/`self.possibleErrors`); sibling classes still in the
      old shape (e.g. `NvDataInterface.getNvDatas` returns
      `list(filter(isinstance(...), self.elements))`) are deviations to
      reconcile, **not** a pattern to copy — a fully-`[x]` sibling in the
      elements-only shape is a prior deviation, exactly like Rule 1.6's
      "an already-aligned sibling is not an authority".
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

# Section 5: Documentation — Method Parity Checklist (Rule 2)

## Rule 2: Method Parity Checklist

**Maturity**: accept

A comment block at the top of the class lists every method with three
columns: `impl`, `docstring`, `test`. Each column must be marked `[x]`. The first line
after the checklist title must cite the AUTOSAR PDF spec table the class is
aligned against: `# Spec: <PDF file>.pdf, Table <X.Y>, p.<page>` (page from
the PDF itself). This makes Rule 1 traceable — every later check refers back
to the spec source named in the class comment.
**Exception — a class with no own spec table carries no `# Spec:` line.**
When a class cannot be read from a PDF table — its attributes are defined
only in an XSD group, with no rendered table of its own (Rule 1.5, e.g. a
concrete `<name>InstanceRef` such as `RteEventInEcuInstanceRef`/
`VariableAccessInEcuInstanceRef`) — there is no PDF table to cite: do **not**
substitute the introducing aggregator's table, because that table does not
define the class. Such a class's checklist begins with the rows directly (no
`# Spec:` line), every row stays `[ ]`, and the deviation tracker records
"no own spec table; attributes from XSD group `…`".

**This exception is distinct from an empty-attribute-rendering class.**
A class whose own PDF `Class` table exists but whose `Attribute` section
contains only a `-` / empty row (all attributes inherited from its `Base`
chain, e.g. `BswServiceDependencyIdent`, `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`
Table 5.16) is **not** this exception: it has a spec table, so it **does**
carry a `# Spec:` line + `# Spec verified:` marker, and its checklist lists
only the methods the class itself defines (often just `__init__`), each
crossed `[x]` once tested. The decision rests on whether a `Class <Name>`
heading exists in any PDF, not on whether the class adds new attributes —
see the "Empty-attribute rendering ≠ no own spec table" bullet in Rule 1.5.

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
      **A commented-out member block is dead code, not a "future" method.** A
      commented-out `@property`/method (e.g. a disabled `internal_behavior`
      property block in `AtomicSwComponentType`) is invisible to the AST-based
      checklist check and to Rule 9's spacing check — it is neither a checklist
      row nor a test target, so nothing flags it. Remove it during alignment;
      do not leave it as a placeholder for future work.
- [ ] Every row is fully `[x]` — no stale `[ ]` entries. A row can look
      incomplete even when the method/docstring/test all already exist —
      always double-check by reading the class, not just the checklist text.
      A `[ ] test` row whose method already has a test in the mirrored test
      file is stale and must be crossed (e.g. `StackUsage`'s abstract base
      accessors were tested via a concrete subclass, but the rows stayed
      `[ ]`). Grep the class body for `# [ ]` during every review — the
      set-based script alone does not flag them.
      **Exception — a class with no own spec table intentionally keeps every
      row `[ ]`.** For a class whose attributes are XSD-only, with no rendered
      PDF table of its own (Rule 1.5, e.g. a concrete `<name>InstanceRef`),
      all-`[ ]` rows are the **correct** state even though the methods are
      implemented, docstringed, and tested — the rows are a *provenance*
      statement (unverified against PDF), not a claim the work is undone. Do
      **not** cross them, and do **not** let the "grep for `# [ ]`" /
      "stale `[ ]`" checks fire on such a class; both apply only to classes
      with a spec table to confirm rows against.
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
- **A class whose table renders in more than one PDF cites one PDF, chosen by
  sibling-family consistency.** Many classes are rendered in several templates
  with the *same* package and attribute rows (e.g. `ComMgrUserNeeds` appears
  as both BSWModuleDescriptionTemplate Table 12.13 and SoftwareComponentTemplate
  Table 13.5). Cite the PDF that the class's sibling family already uses for
  its `# Spec:` lines (the deviation tracker's `**PDF:**`/`**page:**` header is
  a reliable signal — it names the same document, e.g. the other
  `ServiceNeeds` subclasses all cite the BSW template), and keep that choice
  stable across the family; do **not** cite different PDFs for sibling classes
  that share a package and table structure.
      **The deviation tracker's `**PDF:**` header is not authoritative for
      this choice.** It can name a *different* rendering of the same class
      (e.g. `AtomicSwComponentType` was tracked under the BSW template,
      Table D.10, while its sibling family in `Components/__init__.py` cites
      the SWC template, Table 3.8). Choose by the siblings' actual `# Spec:`
      lines, verify the class's own header page in the chosen PDF, and correct
      a stale tracker PDF choice in the same pass — the tracker's *page* is
      already known to go stale (see below); its *PDF* can too. For the *enum attribute type*
  of such a class, the citation is independent: cite the PDF that renders the
  enum's own `Enumeration` table, which can be a different document than the
  class's (e.g. `MaxCommModeEnum` Table 13.6 lives only in the
  SoftwareComponentTemplate even though the class that uses it cites the BSW
  template). Verify the enum's page in *its* PDF (with `pypdf`, matching the
  printed footer) rather than reusing the class's page.
- **An enum that renders in more than one PDF is itself a "class in more than
  one PDF" and uses the same sibling-family rule — but its sibling family is
  the *enums* in the same template, not the class that references it.** A
  shared enum (Rule 1.8) can have its own `Enumeration` table in several
  templates with the same package and literal rows (e.g.
  `ArgumentDirectionEnum` renders as BSW Table 4.8, SWC Table 4.9, and
  SystemTemplate Table F.16; `ServerArgumentImplPolicyEnum` renders only as
  SWC Table 4.10). Cite the PDF that the enum's *sibling enums* already use
  (e.g. `ArgumentDirectionEnum` cites the SWC template because its sibling
  `ServerArgumentImplPolicyEnum` — the other enum used by
  `ArgumentDataPrototype` — cites SWC Table 4.10), and keep that choice stable
  across the enum family; the referencing class's own PDF choice does **not**
  dictate the enum's (the class may cite BSW Table D.7 while its enum
  attributes cite the SWC template). When an enum has no aligned sibling yet,
  fall back to the template that renders the enum's most complete table.
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
- **Page-split renderings emit a separate compact header block.** A page-split
  table renders two physically separate blocks in the markdown: a compact
  header block (the `Class`/`Package`/`Note`/`Base` rows as a short 4-row
  table) followed by `glyph[triangleinv]`/image markers, and then the main
  table (the repeated `Class` row plus `Aggregated by`/`Attribute` rows).
  The `Table X.Y:` caption may appear *before* the main table (SWC layout) or
  *after* it (BSW layout) — either way it is **not** co-located with the
  header block, and grepping the markdown for the class name finds **two**
  `Class <Name>` headings. Cite the page of the **first** occurrence — the
  compact header block — not the caption's page (e.g.
  `ApplicationRuleBasedValueSpecification`, BSW Table D.6: the compact header
  block with `Class`/`Note`/`Base` is on p.302, the continuation/caption on
  p.303).
- Adjacent tables that appear on the same or consecutive pages (e.g. an
  abstract class and its subclasses) are easy to confuse with one another or
  with the section's start page — verify each class's **own** `Table X.Y`
  page independently against the PDF's printed page counter, and never reuse a
  neighboring class's already-checked value. Cross-check against the page in
  `docs/method_deviation_by_class.md`, which **may** already be correct but is
  not authoritative — a stale tracker page (e.g. `ApplicationRuleBasedValueSpecification`
  recorded **page:** 303 while its header block is on p.302) must be corrected
  in the same pass, never propagated into the class's `# Spec:` line.
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
5. **Run the cross-check in both directions.** The procedure above walks
   each *model field* (code → spec) to catch fabricated fields. A deviation
   tracker that was built only by walking *spec → code* (producing only
   `missing` rows) is **not** evidence of completeness: fabricated fields
   can coexist with `missing` rows for the very spec attributes they shadow
   (e.g. `AliasNameAssignment`'s tracker held three `missing` rows for
   `flatInstanceRef`/`identifiableRef`/`label` while the fabricated
   `elementRef`/`aliasName` that masked them had no row at all — the code→spec
   pass had never been run). Always perform the code → spec pass; when a
   `missing` spec attribute has a suspiciously-similar fabricated field,
   that fabricated field is its stand-in and the removal + replacement happen
    together, clearing the `missing` row.

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
      **`from __future__ import annotations` is also the mechanism for
      intra-module forward references** — any annotation that names a class
      declared *later in the same module*, not just an aggregated child
      (e.g. `McGroup`'s `Optional[McGroupDataRefSet]` fields/getters while
      `McGroupDataRefSet` is defined below it, or `ComMgrUserNeeds`'s
      `Optional[MaxCommModeEnum]` accessors while the enum is defined later in
      the same `ServiceNeeds` module). The aggregator/ARElement parent is
      conventionally declared first; do **not** reorder the classes or move
      the referenced type up to satisfy the annotations — the future-import
      resolves the name lazily, and `TYPE_CHECKING` alone is insufficient
      because it does not defer local names. This is the single-module
      analogue of the cross-package case.
- [ ] A blank line separates each attribute block (comment + assignment) in
      `__init__`.
- [ ] Code is formatted with Black at `line-length = 200` (per `pyproject.toml`,
      enforced by `npm run black-check`). The older 79-character limit is
      obsolete and must not be applied by hand.
- [ ] No trailing whitespace on blank lines (`W293`) or after code (`W291`),
      and at most one blank line between definitions (`E303`).
      The project runs two linters: `npm run flake8` (CI, syntax-only set
      `E9/F63/F7/F82`) and `npm run ruff-check` (the broader `E`/`F`/`W`/`I`
      set from `pyproject.toml` `[tool.ruff]`, ignoring only `E501`). Ruff
      therefore **enforces** `W291`/`W293`/`E303` and unused-import `F401`
      that the flake8 syntax set leaves as warnings — so new or edited code
      must pass `npm run ruff-check` (or the file-scoped `ruff check <file>`,
      which reads the same config) as well as `npm run black-check`; an
      outstanding whole-tree cleanup is tracked separately.
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
      **This is a manual-only check — Black, flake8, and ruff do not enforce
      it.** Black leaves a run of contiguous `# comment / self.field = …` blocks
      untouched (it only separates top-level statements); ruff's `E303` caps
      the *maximum* number of blank lines but enforces no *minimum* between
      statements, so it does not require a blank line between field blocks
      either. A class can therefore pass `black-check`, `npm run ruff-check`,
      `flake8`, the set-based checklist, and all tests while its `__init__`
      fields are glued
      together (this happened to `AliasNameAssignment` and
      `SupervisedEntityNeeds` during alignment — the fields were written
      contiguously and nothing flagged it). Verify spacing by eye or with a
      small AST audit: in `__init__`, between consecutive field assignments the
      intervening lines must contain a blank line.
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
- [ ] A round-trip test asserts the **field values** that came back, not just
      that an object was reconstructed. `len(getXxxs()) == 1` /
      `getXxx() is not None` pass unchanged against a writer that emits an
      empty element and a parser that ignores its contents (the Rule 1.7
      identity-only shape), so such assertions cannot detect a lossy
      round trip — assert each attribute's value explicitly, including the
      attributes of aggregated children one level down.
- [ ] A class with a **wrapper-element list** (Rule 1.7) needs a second
      round-trip case for the *empty* list: assert the serialized file
      contains no wrapper tag at all and that re-parsing yields `[]`. The
      populated case alone cannot catch a writer that emits an empty
      `<WRAPPER/>`, because both shapes re-parse to the same model. Assert on
      the written file's text for the wrapper tag's absence, since the
      re-parsed model looks identical either way. Pair this with the
      `None`-valued optional attributes in the same case (they must be absent
      from the XML and `None` after re-parse) so the "nothing set" shape is
      covered end-to-end.

Verification (run in the repo root; replace the paths for the class under
check):

```bash
python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/<package>/test_<ClassName>.py -q
PATH=".venv/Scripts:$PATH" flake8 --exclude=.venv,build --select=E9,F63,F7,F82 \
  src/armodel/models/M2/AUTOSARTemplates/<package>/<ClassName>.py
PATH=".venv/Scripts:$PATH" ruff check \
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
# checklist can still miss it, so check it explicitly). Only a class with
# an own spec table carries the marker — a class with no own table (Rule
# 1.5) has no `# Spec:` line, no marker, and all-`[ ]` rows. A class with a
# Rule 1.10 placeholder (a "not yet implemented" / "carried as a" comment on
# a member whose spec type is a real model class) keeps its `# Spec:` line
# but legitimately omits the stamp; the marker is only required when no such
# placeholder comment is present, so condition the assert on that.
if "# Spec:" in src and "not yet implemented" not in src and "carried as a" not in src:
    assert re.search(r"# Spec verified: R\d\d-\d\d", src), "missing # Spec verified marker (Rule 13.1)"
```

---

# Section 8: Docstring and Comment Synchronization with the AUTOSAR Specification (Rule 13)

## Rule 13: Docstring and Comment Synchronization with the AUTOSAR Specification

**Maturity**: accept

Class docstrings, inline `__init__` comments, and getter/setter docstrings
must all reflect the AUTOSAR PDF specification wording — not loose paraphrase
— and must stay synchronized with it as the AUTOSAR version is upgraded.
Stale or paraphrased docstrings are silent documentation drift: the code
compiles, the tests pass, and nothing catches the mismatch automatically.
This is a **single rule** covering every docstring/comment artifact in a
class (previously split across two rules, "Comments from the Spec" and
"Docstring Synchronization"); they are merged here because they describe the
same one-pass-per-class task and splitting them made it easy to satisfy one
half (e.g. the class docstring) while forgetting the other (e.g. the
per-attribute constraint citations).

**Why this rule is one ordered procedure, not a bag of bullets:** the
individual requirements (verbatim `Note` text, the version marker,
per-attribute constraint citations, the "None is a no-op" sentence) are each
easy to satisfy for *some* members while silently skipping others — e.g.
adding the class docstring and the `# Spec:` marker but forgetting the
marker's page number, or fixing the getter's wording but not the setter's, or
citing a constraint in the comment but not in the docstring that repeats the
same attribute. None of this is caught by Rule 2/7's mechanical check (it
only verifies checklist == methods and that the marker *string* exists — not
that its content is correct, nor that every member below it was actually
synced). Follow 13.2 in order, top to bottom, once per class, and do not
consider the class done until every checkbox for every member is ticked — a
partially-synced class (e.g. class docstring fixed but attribute comments
still paraphrased) is a Rule 13 violation, not a partial credit.

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
- [ ] **The marker certifies *all* spec information, including member types —
      do not claim it while a member is a placeholder.** The marker means the
      class's spec-derived information is correct and complete. A field whose
      spec type is a real model class (e.g. `AttributeValueVariationPoint`,
      Table 7.65) but which is carried as a placeholder (e.g.
      `Optional[ARObject]`) contradicts the marker even when every docstring
      is accurate (this happened to `VariationPointProxy.valueAccess`). When
      a Rule 1.10 placeholder remains because the real type's closure is out
      of scope, **omit the `# Spec verified:` stamp** but **keep the `# Spec:`
      line** — the PDF name/table/page of a class that *does* have an own
      rendered table is a provenance statement that stays valid whether or
      not every member is fully typed (e.g. `AtpBlueprint`, Table D.11,
      p.305, keeps `# Spec:` with a `blueprintPolicy` placeholder, but carries
      no `# Spec verified: R23-11`). The `# Spec:` line without the stamp is
      the honest state; the stamp flips back on once the placeholder is
      replaced by the real type. **The affected members' checklist rows stay
      `[ ]` too — impl, docstring, and test all unchecked** (the Rule 1.5
      provenance convention: `[ ]` means "not confirmed against the spec
      type", and a placeholder is *not* the spec type even though the methods
      are written and tested). The two lines only "travel together" for the
      Rule 7 assert when the class is fully aligned — the assert must allow a
      `# Spec:` line with no stamp when a Rule 1.10 placeholder comment is
      present.
- [ ] **Exception — a class with no own spec table carries no marker.** When a
      class cannot be read from a PDF table — its attributes are defined only
      in an XSD group, with no rendered table of its own (Rule 1.5, e.g. a
      concrete `<name>InstanceRef`) — there is no PDF `Note` to verify
      docstrings against, so it gets **no** `# Spec verified:` marker and its
      checklist rows stay `[ ]`. Rule 13.1's marker requirement (and the Rule
      7 assert that checks for it) applies only to classes that have a spec
      table to be verified against. **This is the same gate as 13.2 step 0 —
      check it once, first, before starting any of the sync work below.**
      **Empty-attribute-rendering classes are NOT this exception:** a class
      with its own PDF `Class` table whose `Attribute` section is empty (all
      attributes inherited, e.g. `BswServiceDependencyIdent`, Table 5.16) has
      a PDF `Note` to verify against and therefore **does** get the
      `# Spec verified:` marker and `[x]` checklist rows. The gate is "does a
      `Class <Name>` heading exist in a PDF?", not "does the class add new
      attributes?" — see the "Empty-attribute rendering ≠ no own spec table"
      bullet in Rule 1.5.

### 13.2 Per-Class Sync Procedure (Initial Alignment or Upgrade)

Run every step below, **in order**, for every class carrying a spec table.
Do not skip a step because a similar-looking one earlier "probably covered
it" — each targets a different artifact (class docstring vs. inline comment
vs. getter vs. setter) and a fix to one does not propagate to the others.

- [ ] **Step 0 — Exception gate.** Does the class have its own PDF table
      (Rule 1.5)? If its attributes come only from an XSD group with no
      rendered table of its own (e.g. a concrete `<name>InstanceRef`), **stop
      here**: no `# Spec:` line, no `# Spec verified:` marker, checklist rows
      stay `[ ]`, and none of the steps below apply. Record "no own spec
      table; attributes from XSD group `…`" in the deviation tracker instead.
      Otherwise, continue.
- [ ] **Step 1 — Locate the spec table and its page number.**
      Search `autosar/markdown/AUTOSAR_CP_TPS_*.md` for `Table <N>.<M>:
      <ClassName>` (markdown extracted from the PDF — this is the reference
      source, never a loose paraphrase). Get the **exact page number** for
      the `# Spec:` marker: either reuse the page cited by a sibling class in
      the same table family, or confirm it directly from the PDF (e.g. with
      `pypdf`, matching the printed page-footer number, not the zero-indexed
      page count — footer text and index can be off by one).
- [ ] **Step 2 — Add the version marker.** Immediately after the
      `# <ClassName> method parity checklist:` line:
      ```python
      # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.2, p.225
      # Spec verified: R23-11
      ```
      (See 13.1 for the exception and the marker format.)
- [ ] **Step 3 — Sync the class docstring.** The first line after `"""` must
      be the PDF table's `Note` row, **verbatim** — do not paraphrase, do not
      abbreviate, and preserve the spec's own grammar even when it reads
      oddly (e.g. "an BswInternalBehavior").
      - **No invented recap prose after the verbatim Note.** The docstring is
        the Note (plus class-level constraint citations, below) — **not** a
        place to recap the `Base` chain or the class's role in an invented
        summary line. A trailing line like `Base classes: ARObject, …,
        CompositeRuleBasedValueArgument` is invented prose that appears
        nowhere in the PDF `Note` (it paraphrases the `Base` row, which the
        class's own inheritance already expresses) and must be **removed**,
        not "improved". The class docstring sync is Note-only; the `Base`
        chain is already discoverable from the class statement and the
        `# Spec:` citation.
      - **Class-level constraints, including on inherited attributes.**
        `constr_*` rows that target the class belong in this docstring
        alongside the note — a constraint may target an attribute the
        subclass does not declare itself (e.g. `constr_4103` constrains
        `SectionNamePrefix.symbol`, which is inherited from
        `ImplementationProps`, and therefore belongs in the
        `SectionNamePrefix` class docstring, not in the parent's).
      - **Terse cross-reference notes.** If the PDF `Note` is only a citation
        (e.g. `Specifies a time value based on [20] see [TPS_GST_00354]`),
        still lead with it verbatim, then append the XSD complexType
        documentation as an elaboration paragraph (it is also verbatim spec
        wording) — never silently substitute the XSD text for the PDF
        `Note`, never invent prose to "expand" a terse note.
- [ ] **Step 4 — Per-attribute sync loop.** For **every** attribute row in
      the spec table (not just the ones that look wrong), do all **five** of
      the following before moving to the next attribute — treat this as one
      unit of work per attribute, not separate passes over the whole class:
       1. **Referenced type must exist and be aligned before typing.**
          Check the attribute row's `Type` column first: if it names a model
          class or enum (e.g. an `Enumeration` like
          `ServerArgumentImplPolicyEnum`), that type must **exist** in the
          codebase and carry its own `# Spec:`/`# Spec verified:` markers —
          Rule 1.10 applies to **every** referenced type, not only
          `<name>InstanceRef`s. The field and accessor annotations are typed
          against that class, so if it is missing, implement it first from
          its own spec table (checklist, marker, tests, parser/writer
          coverage) and only then type the attribute. The referenced type's
          `# Spec:` citation is **independent** of the owning class's: it
          cites the PDF/table/page that renders the referenced type's **own**
          table. E.g. the enum `ServerArgumentImplPolicyEnum` is spec'd by
          SWC Table 4.10 even though the `ArgumentDataPrototype` field using
          it cites BSW Table D.7 — never copy the owning class's citation
          onto the referenced type or vice versa, and give the new type its
          own table location/version search.
       2. **Inline `__init__` comment**: quote the attribute's PDF `Note`
          **semantic sentence** verbatim/near-verbatim; do **not** paste the
          `Stereotypes:`/`Tags:` tail (e.g. `Stereotypes: atpSplitable;
          atpVariation Tags: atp.Splitkey=...`) — that tail is tooling
          metadata already captured in the markdown and adds no semantics to
          the comment. Example: `AccessCountSet.accessCount`'s note "Count
          value for a AbstractAccessPoint. Stereotypes: ..." is quoted as
          "Count value for a AbstractAccessPoint." If a `constr_*` row
          targets this attribute, append its wording and cite the id — the
          full constraint wording is typically rendered as a
          `[constr_NNNNN]` paragraph **immediately after the class's own
          table** (in addition to any consolidated constraint index elsewhere
          in the PDF), e.g. `AccessCountSet`'s Table 4.22 is followed by
          `constr_10270` constraining `countProfile`; grep both the table
          neighborhood and the constraint index when collecting constraint
          material. A `constr_*` whose target is an **aggregated child's
          nested attribute** (e.g. `constr_10041` constraining
          `ApplicationRuleBasedValueSpecification.swAxisCont.category`) is
          cited on the **owning attribute** — the parent's `swAxisCont`
          comment and accessor docstrings — not on the child class, and its
          wording is abbreviated to that owning attribute's context
          (`...ApplicationRuleBasedValueSpecification.swAxisCont.category
          shall not be set to fixAXIS. [constr_10041]`), not pasted as a
          `Note` replacement.
       3. **Getter docstring**: summarize the same `Note` + constraint — not
          "Gets the value of X". Mention what the attribute represents in
          AUTOSAR, cite the applicable `constr_*` id (an attribute-level
          constraint, e.g. `constr_4072` on
          `SectionNamePrefix.implementedIn`, is cited in **both** the
          `__init__` comment and the getter/setter docstrings — not just
          one), and for an `iref` attribute name the concrete
          `<name>InstanceRef` implementing class (so the concrete iref type
          is discoverable in the code, not only in the deviation tracker).
       4. **Setter docstring**: same `Note`/constraint summary as the getter,
          plus the chainable-return behavior. **If the setter is guarded**
          (`if value is not None:`), it **must** also state, verbatim: *"A
          None value is a no-op and does not overwrite an existing
          `<attr>`."* This is not optional — a guarded setter without this
          sentence is an incomplete sync even if the rest of the docstring is
          correct.
       5. **Cross-check the four against each other**: the comment, getter,
          and setter for the same attribute should tell a consistent story —
          a getter that was updated but a setter left with the old wording
          (or a constraint cited in one but not the others) is a common
          half-sync failure.

      Two worked examples of an inline comment quoting the spec `Note`:
      ```python
      # Indicates an entry which is required by this module.
      # Replacement of a deprecated attribute.
      self.expectedEntryRefs: List[RefType] = []
      ```
      ```python
      # AUTOSAR identifier of the target module; optional as the target may be
      # identified by targetModuleRef instead.
      self.targetModuleId: Optional[PositiveInteger] = None
      ```
- [ ] **Step 5 — Verify by diff, not by status.** There is **no mechanical
      check** for docstring correctness (13.5): Rule 2/7's script only
      confirms the checklist matches the methods, every method is tested,
      and the marker *string* is present — none of that proves the wording
      matches the PDF. Do not treat a fully-`[x]` checklist, a present
      `# Spec verified:` marker, or an "aligned" row in
      `docs/method_deviation_by_class.md` as evidence that steps 3–4 were
      done correctly. For each attribute, re-open the PDF/markdown `Note` (or
      the matching XSD `<xsd:documentation>`, same verbatim text) and diff it
      against the inline comment and both docstrings yourself — a real
      instance of this failure mode: `McDataInstance.displayIdentifier`'s PDF
      note "used to set the ASAM ASAP2 DISPLAY_IDENTIFIER attribute" had been
      silently rewritten to "used by an MCD system to identify this data
      instance" (a different meaning) across 8 of 12 attributes, while every
      other check — checklist, marker, tracker — still passed.

### 13.3 Drift Detection on AUTOSAR Upgrade

When the AUTOSAR specification version is upgraded in the repository, an
upgrade pass is **not** "check the class docstring only" — it is the
identical per-member walk as a first-time alignment (13.2), just diffed
against the new PDF revision instead of an assumed-blank starting point:

1. **Identify affected classes**: search the codebase for the old version marker
   (e.g., `# Spec verified: R23-11`) using:
   ```bash
   grep -r "Spec verified: R23-11" src/armodel/models/
   ```
2. **For each affected class**, run the full 13.2 procedure (steps 0–5) against
   the *new* PDF revision, then:
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

### 13.4 Rationale

Docstring drift is a **silent bug**:
- Code compiles and tests pass even when docstrings are outdated.
- Developers reading the code assume docstrings are current (a reasonable
  assumption).
- Stale docstrings mislead API consumers and maintainers.
- Unlike code bugs, drift is discovered only by manual inspection or explicit
  verification (there is no automatic synchronization between PDF and code).

The version marker and the ordered per-class procedure provide explicit
reminders and a structured process to catch and fix drift at the natural
point when AUTOSAR is upgraded, rather than silently accumulating outdated
documentation.

### 13.5 No Automatic Enforcement

There is currently **no CI check** that validates docstrings against the PDF
or detects version skew. This rule relies on:
- Developers' awareness of the synchronization requirement.
- The version marker as a visible signal in the code.
- Manual verification during AUTOSAR upgrades (triggered by the grep search
  above).
- Code review to catch docstring mismatches during PR review.
- The ordered, per-member checklist in 13.2 — the mechanical Rule 2/7 script
  can confirm the *marker* exists, but only a deliberate, in-order walk of
  13.2's steps catches a *content* mismatch or a half-synced member.

If automatic tooling is added in the future (e.g., a docstring validator that
parses the PDF markdown and compares against Python docstrings), this rule
will be updated to incorporate it.

---

# Section 9: Parser and Writer Source Style (Rule 14)

## Rule 14: No Chained Method Calls in Parser/Writer Source

**Maturity**: accept

Rule 4 makes every setter/adder/creator return `self` so that chaining
(`obj.setA(...).setB(...)`) *is possible*. That capability exists for
external/consumer convenience and for the model's own internal use; the
**parser and writer source code must not use it**. Each `set`/`create`/`add`
call is written as its own statement on the receiver.

Check:
- [ ] In `src/armodel/parser/arxml_parser.py` and
      `src/armodel/writer/arxml_writer.py` (and the abstract bases / sibling
      parsers under `src/armodel/parser/`), no statement chains two or more
      `set`/`create`/`add` calls on one receiver. `obj.setA(x).setB(y)` is a
      violation, as is a multi-line chain that wraps an argument across lines
      and continues with another call on the closing parenthesis (a line whose
      next non-whitespace token after `)` is `.set...`). The split point is any
      top-level `.` that follows a completed call, and each such call must
      become its own statement.
- [ ] A chain that begins with a factory returning a shared object is also
      split, by binding the shared object to a local first. The recurring case
      is the AUTOSAR document — `AUTOSAR.getInstance().addXxx(...)` becomes
      ```python
      document = AUTOSAR.getInstance()
      document.addXxx(...)
      ```
      Verify the chosen local name (the convention is `document`) does not
      shadow an existing name in the same scope before introducing it.
- [ ] Getter/attribute chains used as **values inside an expression** are
      **not** covered by this rule and are left as-is. These are read-only
      sub-expressions, not statement-level mutator chains, e.g.
      `"...%s" % (event.getPeriod().getValue(), ...)`,
      `ref.getDest()`, `connector.getOuterPortRef().getValue()`. The rule
      targets only the statement-position `set`/`create`/`add` idiom.

Why (before/after):

Before — one long chain, hard to read and step through:
```python
range.setLowerCanId(
    self.getChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID")
).setUpperCanId(self.getChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID"))
```

After — one mutation per statement:
```python
range.setLowerCanId(self.getChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID"))
range.setUpperCanId(self.getChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID"))
```

Rationale:
1. **Readability and review**: one mutation per line makes each XML element →
   field mapping self-evident; reviewers and diff readers see one logical
   change per line instead of a run-on expression.
2. **Debuggability**: one statement per setter means a breakpoint or stack
   trace points directly at the exact call, and stepping is line-by-line
   rather than into the middle of a chain.
3. **Editability**: reordering, commenting out, or inserting a field does not
   require rewrapping or re-indenting a long chain.
4. **Decouples tests from the chain shape**: mock-based parser tests assert
   each setter on the receiver independently (`props.setX.called` and
   `props.setY.called`), never `props.setX().setY.called`. A test that asserts
   the chained form (`props.setAuthAlgorithm.return_value.setAuthInfoTxLength.called`)
   is coupled to the chain and breaks the moment setters are called as
   separate statements — such tests must assert the flat form instead.

Verification:
- Grep the parser and writer for the chain pattern (must return nothing):
  ```bash
  grep -nE '(^|[^.a-zA-Z_])([a-zA-Z_][a-zA-Z0-9_]*)\.(set|create|add)[A-Z][a-zA-Z0-9_]*\([^)]*\)\.(set|create|add)' \
      src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py
  ```
- Grep for the document-factory chain (must return nothing):
  ```bash
  grep -nE 'AUTOSAR\.getInstance\(\)\.' \
      src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py
  ```
- After any parser/writer edit, run `npm run ruff-check`, `npm run black-check`,
  and the full suite (`python scripts/run_tests.py`). Enforcing this rule is a
  purely mechanical, behavior-preserving refactor: round-trip parse → write →
  re-parse must still match for every integration fixture (29 ARXML files).

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
