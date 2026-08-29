# Parser/Writer Naming Conventions

Source of truth: `src/armodel/parser/arxml_parser.py` (1051 methods), `src/armodel/writer/arxml_writer.py` (1054 methods), and their abstract bases `parser/abstract_arxml_parser.py` / `writer/abstract_arxml_writer.py`. Statistics and deviations below were derived from a static scan of the current tree.

## 1. Method-Naming Matrix

| Layer | Parser (ARXML → model) | Writer (model → ARXML) |
|---|---|---|
| Class-level (whole element) | `read<ClassName>(element, instance)` | `write<ClassName>(element, instance)` |
| Composite child helper | `get<Name>(element, key)` | `set<Name>(element, key, value)` |
| Primitive child helper (abstract base) | `getChildElementOptional<X>(element, key)` | `setChildElementOptional<X>(element, key, value)` |
| Top-level entry | `load()` | `save()` |

### 1.1 Class-level readers — `read<ClassName>(element, instance)`

- `element` is already positioned **at** the object's own element (the caller found it).
- Starts the heritage chain: `readIdentifiable(element, instance)` → `readMultilanguageReferrable` → `readReferrable` → `readARObjectAttributes`.
- Fills the instance exclusively through model mutators (`setXxx`, `addXxx`), never by touching fields directly.
- Logs via `self.logger.debug("Read <ClassName> %s" % instance.getShortName())` (optional).
- Never creates elements — the parser is read-only over the tree it was given.

### 1.2 Class-level writers — `write<ClassName>(element, instance)`

- `element` is the **parent**; the writer creates its own element first:
  `child_element = ET.SubElement(element, "TAG-NAME")`.
- Then calls the heritage chain: `writeIdentifiable(child_element, instance)` (which reaches `writeReferrable` → `setShortName`).
- Reads the instance exclusively through model getters (`getXxx()`).

### 1.3 Composite helpers

- Parser `get<Name>(element, key) -> Optional[Model]`: finds child `key`; if present, constructs the model object (see §2 for the short-name argument) and returns it, otherwise returns `None`. Example: `getInfrastructureServices(element, key)` (parser:6901).
- Writer `set<Name>(element, key, value)`: if `value is None`, writes nothing; otherwise creates `ET.SubElement(element, key)` and fills it. Example: `setInfrastructureServices(element, key, services)` (writer:7210).
- Naming is mirrored: `getDoIpEntity` ↔ `setDoIpEntity`, `getCouplingPortDetails` ↔ `setCouplingPortDetails`, etc.

### 1.4 Primitive helpers (abstract bases)

- Parser `getChildElementOptionalLiteral/RefType/IntegerValue/BooleanValue/TimeValue/...` return a parsed value or `None`.
- Writer `setChildElementOptionalLiteral/RefType/IntegerValue/...` skip emission when the value is `None`.
- Both sides accept the tag name as the `key` argument — the tag is never hardcoded inside these helpers.

## 2. Short-Name vs No-Short-Name Classes

The model splits cleanly at `Referrable` (`models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`):

- **Short-name classes** — every subclass of `Referrable` (≈ half of the ~1127 model classes): `__init__(self, parent, short_name)`; `short_name` is mandatory and immutable after construction (read-only `shortName` property, no `setShortName`).
- **No-short-name classes** — direct `ARObject` descendants (enums, `ARLiteral`/`ARNumerical` value types, `AdminData` inner structures, `VariationPoint`, instance-ref value objects, ...): constructed without `short_name`, and no `SHORT-NAME` is ever read or written for them.

### 2.1 Parser rules for short-name classes

1. The `SHORT-NAME` is read **once, at the construction site**, via `self.getShortName(element)` (442 call sites) and passed into the constructor:
   `instance = ClassName(parent, self.getShortName(child_element))` — or via the class factory `parent.createXxx(self.getShortName(child_element))`.
2. The heritage reader `readReferrable` does **not** read `SHORT-NAME` — it only reads `SHORT-NAME-FRAGMENTS/SHORT-NAME-FRAGMENT` (`ROLE`, `FRAGMENT`).
3. Content-level readers (see §2.2) never handle the short name.

### 2.2 Element-level vs content-level methods

Not every `read<ClassName>`/`write<ClassName>` handles the whole element. Two shapes exist and both are legitimate:

- **Element-level**: owns the element. Reader starts with `readIdentifiable`; writer creates the `ET.SubElement` and calls `writeIdentifiable`. Applies to `ARElement` subclasses and composite children.
- **Content-level**: fills a fragment whose element was created/positioned by the caller (e.g. `readCommunicationController` fills `ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL`; `writeTraceable` fills `TRACE-REFS` inside an already-created element). These deliberately do **not** touch `SHORT-NAME` or the identifiable chain — the outer element-level method owns it.

When reviewing, a short-name class reader/writer without a chain call is only a defect if the method is element-level.

### 2.3 get/set legality by scenario

`AUTOSAR.find(path)` resolves path segments via `getElement(short_name)`, which reads `element_mappings` — populated **exclusively by `addElement()`** (Identifiable.py). It never walks the `parent` chain (that is `getFullName()`). Therefore the legality of a `setXxx()` accessor depends on *where the attached object lives in the object graph*, not on whether the object has a short name:

| Scenario | Correct API | Rationale |
|---|---|---|
| No-short-name value object (SoAdConfig, AdminData inner parts, DhcpServerConfiguration, value specs, ...) | `setXxx()` / `getXxx()` | Never find-reachable; plain field storage is the intended pattern (e.g. `setSoAdConfig`, CoreTopology.py) |
| Short-name child of a **package-level collection** (findable: `AUTOSAR` → `ARPackage` → `CollectableElement`) | `create<Name>(short_name)` + `add<Name>()` (which call `addElement`) | A plain setter bypassing `addElement` would hide the child from `find()` **and** from `IsElementExists` duplicate detection — such a setter is invalid |
| Short-name child of a **nested composite** (coupling ports, shapers, captions, events inside behaviors, ...) | `setXxx(child)` with the child constructed as `Child(parent, short_name)` | The container does not implement `getElement`, so the child was never `find()`-reachable regardless of attach method; constructor-bound `parent` keeps `getFullName()` correct and the parser round-trips. Plain get/set is the valid, intended pattern here |
| Reference to any Referrable | `set<Name>Ref(RefType)` | No object ownership involved |

Audit result (static scan of all model setters whose parameter is a short-name class): 11 exist (`setShaper`, `setFormulaCaption`, `setBulkNvBlock`, `setRamBlock`, `setIdent` variants, `setServiceNeeds`, `setTimingConditionFormula`, `setHwPinGroup`, `setRootSwCompositionPrototype`) — all attach nested-composite children, none target a `find()`-traversable collection. So no actual `find()` breakage exists today.

Borderline case: `setRootSwCompositionPrototype(ARElement)` on the `AUTOSAR` root — the root **is** a find-traversal container, but the prototype is field-stored and therefore not `find()`-reachable. Harmless today (nothing references it by path), but it is the one place where the "collected child must go through `addElement`" rule has a real target.

## 3. Deviations Found

Each item: location, what violates which rule, impact.

### D1 — `writeInternalTriggerOccurredEvent` is a `pass` stub (round-trip data loss) — FIXED

- [arxml_writer.py:2851](../../src/armodel/writer/arxml_writer.py#L2851): was `def writeInternalTriggerOccurredEvent(self, element, event: DataReceivedEvent): pass`
- Violated §1.2 (a class-level writer must serialize its instance) and used the **wrong type annotation** (`DataReceivedEvent` instead of `InternalTriggerOccurredEvent`).
- It **is dispatched** by the SWC events writer (arxml_writer.py:2896-2897), while the parser reads the event normally (arxml_parser.py:4471, dispatched via `readSwcInternalBehaviorEvents` tag dispatch).
- Impact: any SWC `INTERNAL-TRIGGER-OCCURRED-EVENT` was silently dropped on write — parse → write → re-parse lost the event.
- **Fix applied**: implemented the writer mirroring the parser and the sibling `writeAsynchronousServerCallReturnsEvent` — element creation → `setRTEEvent` → `EVENT-SOURCE-REF`; annotation corrected to `InternalTriggerOccurredEvent`. The writer test that previously *asserted the empty-output bug* (`assert len(parent) == 0`) now asserts the event and its `EVENT-SOURCE-REF` are emitted, plus a `None` no-op case and the dispatch assertion in `test_writeSwcInternalBehaviorEvents`.

### D2 — Parser `read*` methods that create elements

Rule §1.1: the parser must not create elements. Four readers call `ET.SubElement`:

- `readSdgSdxRefs` ([arxml_parser.py:918](../../src/armodel/parser/arxml_parser.py#L918))
- `readSdgSdxfRefs` ([arxml_parser.py:922](../../src/armodel/parser/arxml_parser.py#L922))
- `readHwPinGroup` ([arxml_parser.py:7718](../../src/armodel/parser/arxml_parser.py#L7718))
- `readAbstractCanCommunicationControllerCanControllerAttributes` ([arxml_parser.py:9168](../../src/armodel/parser/arxml_parser.py#L9168))

Impact: low today (they build detached scratch elements), but they break the parser-is-read-only invariant and mirror nothing on the writer side.

### D3 — Private method named like a public convention

- `_readVariableAccesses` ([arxml_parser.py:1292](../../src/armodel/parser/arxml_parser.py#L1292)) — a `read*`-shaped method hidden behind a `_` prefix. Either rename to `readVariableAccesses` (if it is a normal helper) or restructure; the underscore hides it from the naming-based audits used above.

### D4 — Concrete `getChildElement*/setChildElement*` names colliding with the primitive-helper namespace

The abstract bases own the `getChildElementOptional*` / `setChildElementOptional*` namespace (§1.4). Two concrete composite helpers squat in the same `getChildElement*`/`setChildElement*` namespace with a *class-name* suffix instead of following the `get<Name>`/`set<Name>` convention:

- Parser: `getChildElementRxIdentifierRange` ([arxml_parser.py:868](../../src/armodel/parser/arxml_parser.py#L868)), `getChildElementJ1939NodeName` ([arxml_parser.py:877](../../src/armodel/parser/arxml_parser.py#L877))
- Writer: `setChildElementRxIdentifierRange` ([arxml_writer.py:805](../../src/armodel/writer/arxml_writer.py#L805)), `setChildElementJ1939NodeName` ([arxml_writer.py:811](../../src/armodel/writer/arxml_writer.py#L811))

Should be `getRxIdentifierRange`/`setRxIdentifierRange`, `getJ1939NodeName`/`setJ1939NodeName`.

### D5 — `setTimeSynchronization` hardcodes its tag

- [arxml_writer.py:7185](../../src/armodel/writer/arxml_writer.py#L7185): `setTimeSynchronization(self, element, sync)` writes a literal `"TIME-SYNCHRONIZATION"` tag, while every sibling composite helper takes the tag as `key` — including its parser counterpart `getTimeSynchronization(element, key)` and its own sibling `setDoIpEntity(element, key, entity)`.
- Impact: signature asymmetry; callers cannot reuse the helper for a differently-keyed element.

### D6 — Short-name-fragment handling is asymmetric

- Writer: dedicated helpers `setShortNameFragments` ([arxml_writer.py:970](../../src/armodel/writer/arxml_writer.py#L970)) / `setShortNameFragment`.
- Parser: `readReferrable` parses `SHORT-NAME-FRAGMENTS` **inline** — no `getShortNameFragments` helper exists.
- Impact: the writer/reader mirror (§1.3) is broken for this member; refactors must touch two unrelated places.

### D7 — Minor abstract-base asymmetries

- Writer has `setChildElementOptionalNumberValue` ([abstract_arxml_writer.py:85](../../src/armodel/writer/abstract_arxml_writer.py#L85)) but the parser has no `getChildElementOptionalNumberValue` (only `...NumericalValue`). One of the two names is superfluous.
- Both sides share the `DataTime` typo (`getChildElementOptionalDataTime` / `setChildElementOptionalDataTime`) — symmetric, but should be `DateTime`.

### D8 — Broken duplicate guards in `create<Name>()` factory methods (model-side, related to §2.3) — FIXED

- The pattern `if short_name not in self.elements` was used in **56 `create<Name>()` methods across 13 model files**. `self.elements` is a list of *objects*, so the string-membership test was always true. `addElement`'s internal guard prevented duplicate mappings, but side-lists (e.g. `networkEndpoints`) still received duplicates on repeated create calls (double emission by the writer).
- **Fix applied (two parts):**
  1. Replace the broken test with `IsElementExists(short_name, TYPE)` — **type-qualified**, because AUTOSAR allows the same short name to coexist across *different* element types (per §2.3). A type-less check would wrongly block e.g. an `ISignalTriggering` and a `PduTriggering` both named `X` under the same `EthernetPhysicalChannel`.
  2. Also qualify the paired fallback lookup: `return self.getElement(short_name, TYPE)` — otherwise a same-short-name element of a different type could be returned.
- Affected files: CoreTopology.py (12), ResourceConsumption (12), NetworkManagement (6), Implementation.py (7), SystemTemplate/\_\_init\_\_.py (4), InternalBehavior.py (4), ServiceNeeds.py (3), BswBehavior/\_\_init\_\_.py (18), BswOverview/\_\_init\_\_.py (10), SwcInternalBehavior (29+21), PortInterface/\_\_init\_\_.py (10), ECUCParameterDefTemplate (19), and others (FlatMap, CryptoKeySlot, ImplementationDataTypes, EthernetTopology, ServiceInstances, CoreCommunication, EcuInstance, TransportProtocols, Transformer, ModeDeclaration, Timing*, Composition, Datatypes, EndToEndProtection, ImplicitCommunicationBehavior, EcuResourceTemplate, ECUCDescriptionTemplate, Keyword).
- Verified: same short name with different types coexist and return distinct instances; same type returns the existing instance; side-lists stay singleton. Full unit suite, lint, and black-check pass.
- **Rule going forward:** every new `create<Name>()` factory method must guard with `IsElementExists(short_name, <ConstructedType>)` and fall back via `getElement(short_name, <ConstructedType>)`.

### Related-but-previously-reported

The dedicated review `arxml_parser_code_review.md` already documents parser-side defects (stub readers, cross-wired names, dead code, etc.); the items above cover only the naming/short-name conventions defined in this document.

## 4. Scan Methodology (for reproducibility)

1. Enumerate `def` methods per file; group by prefix (`read*`/`write*`/`get*`/`set*`/`getChildElement*`/`setChildElement*`/other).
2. Build the static class graph from model sources; `Referrable`-reachability defines the short-name class set.
3. For every short-name-class `read<Name>`/`write<Name>`, walk the transitive `self.read*/get*` (parser) and `self.write*/set*` (writer) call graph; element-level methods that never reach `readIdentifiable`/`readReferrable` (parser) or `writeIdentifiable`/`writeReferrable` (writer) are flagged, then manually triaged as content-level (OK) vs defect.
4. Scan `read*` bodies for `ET.SubElement` and constructions of short-name classes lacking `getShortName`.
