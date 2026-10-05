# Method/Attribute Deviations by Class

Each class implemented in py-armodel whose OWN spec attributes (R23-11 XSD,
mirroring the PDF attribute tables) deviate from the Python implementation.
The PDF reference `Kind` suffix (`Ref`/`TRef`/`IRef`/`Refs`) is appended to
the member name and is recognised in matching, so e.g. a spec attr `type` of
kind `TRef` is correctly implemented by `typeTRef`. `variationPoint`/
`shortLabel` are excluded as framework-level.

- Classes with deviations: **293**
- Missing accessors: **664**
- Naming deviations: **11**
- Type deviations (list/single multiplicity): **60**

## `BswModuleDescription`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 26
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswOverview`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `bswModuleDocumentation` | `—` | `bswModuleDocumentation` | `SwComponentDocumentation` | — | type (spec many vs py single) |
| — *(missing)* | `—` | `outgoingCallback` | `BswModuleEntryRefConditional` | — | missing |
| — *(missing)* | `—` | `providedEntry` | `BswModuleEntryRefConditional` | — | missing |

## `BswModuleEntry`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 32
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `serviceId` | `ARNumerical` | `serviceId` | `PositiveInteger` | attr | type (PDF PositiveInteger vs py ARNumerical; parser `getChildElementOptionalNumericalValue` produces ARNumerical) |
| `returnType` | `—` | `returnType` | `SwServiceArg` | — | type (spec one vs py list) |

## `ModeDeclarationGroup`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 42
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|---|
| `onTransitionValue` | `ARNumerical` | `onTransitionValue` | `PositiveInteger` | attr | type (PDF PositiveInteger vs py ARNumerical; parser `getChildElementOptionalNumericalValue` produces ARNumerical) |

> Note: `modeTransition` deviation (spec many vs py single) resolved — now `modeTransitions: List[ModeTransition]`.

## `ModeTransition`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 43
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclarationExtra.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | `enteredModeRef`/`exitedModeRef` now present (was missing); `sourceModeRef`/`targetModeRef` removed. |

## `ModeErrorBehavior`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 44
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclarationExtra.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `defaultModeRef` | `Ref (ModeDeclaration)` | Ref | missing |
| — *(missing)* | `—` | `errorReactionPolicy` | `ModeErrorReactionPolicyEnum` | — | missing |

## `BswModuleDependency`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 47
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `expectedCallback` | `BswModuleEntryRefConditional` | — | missing |
| — *(missing)* | `—` | `requiredEntry` | `BswModuleEntryRefConditional` | — | missing |
| `targetModuleRef` | `—` | `targetModuleRef` | `BswModuleDescriptionRefConditional` | Refs | type (spec many vs py single) |

## `BswEntryRelationship`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 51
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `bswEntryRelationshipType` | `Optional[BswEntryRelationshipEnum]` | `bswEntryRelationshipType` | `BswEntryRelationshipEnum` | Attr | ok |
| `fromRef` | `Optional[RefType]` | `from` | `Ref (BswModuleEntry)` | Ref | ok (Rule 0001.5 ref-suffix) |
| `toRef` | `Optional[RefType]` | `to` | `Ref (BswModuleEntry)` | Ref | ok (Rule 0001.5 ref-suffix) |

Deviations resolved (2026-09-26 sync, Table 4.19, p.51): the three `missing` rows above were
stale (the classes were audited against non-existent leaf files `BswInterfaces/BswEntryRelationship.py`;
the members always existed in `BswInterfaces.py`) — all three members verified present and retyped;
`__init__` docstring and paraphrased docstrings wiped and rewritten verbatim from the markdown Notes
(the spec's own "drivedFrom" typo kept verbatim); old 4-col checklist replaced with the 6-column
format. Reader/writer coverage ADDED this sync: read/writeBswEntryRelationship with
FROM-REF/TO-REF/BSW-ENTRY-RELATIONSHIP-TYPE (XSD token DERIVED-FROM via
BSW_ENTRY_RELATIONSHIP_XML_MAP; XSD element order FROM-REF, TO-REF, BSW-ENTRY-RELATIONSHIP-TYPE
per xml.sequenceOffset=5), value-asserting round-trip test.

## `BswModuleDependency`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 48
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `targetModuleId` | `Optional[PositiveInteger]` | `targetModuleId` | `PositiveInteger` | Attr | ok |
| `targetModuleRef` | `Optional[RefType]` | `targetModuleRef` | `Ref (BswModuleDescription)` | Ref | type (wire many vs py single) — markdown 0..1 wins for the model (Rule 0015); R23-11 XSD wire is TARGET-MODULE-REFS wrapper + unbounded BSW-MODULE-DESCRIPTION-REF-CONDITIONAL items (pureMM.maxOccurs=-1); reader takes the first item, writer writes one |

2026-09-26 sync (Table 4.17, p.48): fabricated class docstring, `__init__` docstring and
paraphrased docstrings wiped, rewritten verbatim from the markdown Notes (Tags tails kept);
VariationPointCapable mixin REMOVED — the R23-11 complexType BSW-MODULE-DEPENDENCY has no
class-level VARIATION-POINT group (the atpVariation stereotype lives on the targetModuleRef
attribute, expressed via the per-item VP of the REF-CONDITIONAL wrapper, which the single-ref
model cannot carry); reader/writer REWIRED to the R23-11 wire format
(TARGET-MODULE-REFS/BSW-MODULE-DESCRIPTION-REF-CONDITIONAL/BSW-MODULE-DESCRIPTION-REF, DEST
BSW-MODULE-DESCRIPTION; the old bare TARGET-MODULE-REF element does not exist in the R23-11 XSD);
reader retyped to getChildElementOptionalPositiveInteger (spec type). atp.Status="removed"
members (requiredEntry seq 10, expectedCallback seq 15, serviceItem seq 20) deliberately not
modeled and not read/written (R23-11 removal; no fixture carries them). Stamp deferred to batch
confirmation.

## `BswModuleClientServerEntry`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 54
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `encapsulatedEntryRef` | `Optional[RefType]` | `encapsulatedEntry` | `Ref (BswModuleEntry)` | Ref | ok (Rule 0001.5 ref-suffix) |
| `isReentrant` | `Optional[Boolean]` | `isReentrant` | `Boolean` | Attr | ok |
| `isSynchronous` | `Optional[Boolean]` | `isSynchronous` | `Boolean` | Attr | ok — IS an R23-11 Table 4.21 attribute (cross-page row, markdown L1400; original extraction missed the page-split continuation past the caption L1394). Confirmed by user at 9b 2026-10-01; release column unified to R23-11, docstring re-synced to the R23-11 Note casing (R4.3.1 used "• True:"/"• False:") |

2026-09-26 sync (Table 4.21, p.54): fabricated class docstring, `__init__` docstring and paraphrased
docstrings wiped, rewritten verbatim from the R23-11 Notes (the legacy row from the R4.3.1 Note);
bare-typed fields retyped `Optional[...]` (R4.3.1 Mult 1 for encapsulatedEntry superseded by the
R23-11 0..1); VARIATION-POINT coverage ADDED to read/writeBswModuleClientServerEntry (own-group
VP element, AUTOSAR_00052.xsd L11320). Stamp deferred to batch confirmation.

## `BswEntryRelationshipSet`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 51
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `bswEntryRelationships` | `List[BswEntryRelationship]` | `bswEntryRelationship` | `BswEntryRelationship` | Aggr (0..*) | ok (Rule 0001.5 plural) |

Deviation resolved (2026-09-26 sync, Table 4.18, p.51): the `missing` row was stale (audited
against a non-existent leaf file `BswInterfaces/BswEntryRelationshipSet.py`; the member always
existed in `BswInterfaces.py`) — verified present as a dedicated typed-list field. Base corrected
`Identifiable` → `ARElement` (spec Base chain ARObject..CollectableElement..PackageableElement..
ARElement; AtpBlueprint/AtpBlueprintable collapse per the established attribute-less-abstract-base
precedent). Reader/writer coverage ADDED this sync: createBswEntryRelationshipSet factory +
getBswEntryRelationshipSets getter on ARPackage, read/writeBswEntryRelationshipSet
(BSW-ENTRY-RELATIONSHIPS wrapper + BSW-ENTRY-RELATIONSHIP items), ARPackage element dispatch
both directions, document round-trip test.

## `BswModuleEntity`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 70
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `calledEntry` | `BswModuleEntryRefConditional` | — | missing |

## `ExecutableEntity`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 70
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | `canEnter`/`exclusiveAreaNestingOrderRefs`/`runsInside` now present (were missing) as `canEnterRefs`/`exclusiveAreaNestingOrderRefs`/`runsInsideRefs`; `runsInsideExclusiveAreaRefs` maps to `runsInsideRefs`. `minimumStartIntervalMs` is an added convenience property (ms from the `TimeValue` `minimumStartInterval`, mirroring `BswEvent.periodMs`). |

## `BswExclusiveAreaPolicy`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 82
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswExclusiveAreaPolicy.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `apiPrinciple` | `ApiPrincipleEnum` | — | missing |
| — *(missing)* | `—` | `exclusiveAreaRef` | `Ref (ExclusiveArea)` | Ref | missing |

## `ExclusiveAreaNestingOrder`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 84
- **Spec table:** Table 5.19, p.84 — Base `ARObject, Referrable`; single attribute `exclusiveArea` (ordered, `*`, ref).
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `exclusiveAreaRefs` | `List[RefType]` | `exclusiveArea` | `Ref (ExclusiveArea)` | ref | partial: field + accessors exist, not yet wired in parser/writer |
| *(removed)* | `int` (was `order`) | — *(not in spec)* | — | — | removed: fabricated attribute `order` with `getOrder`/`setOrder` had no spec counterpart; deleted during realignment |
| *(base)* | `Referrable` (was `ARObject`) | `Base` | `ARObject, Referrable` | — | base: aligned Python base from `ARObject` to `Referrable` per spec `Base`; constructor changed from `__init__(self)` to `__init__(self, parent, short_name)` |

`InternalBehavior.exclusiveAreaNestingOrders` is declared as a bare `List` with no
factory (`createExclusiveAreaNestingOrder`) and is never populated by the parser —
the aggregation is itself a partial implementation and remains to be wired.

## `BswEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 87
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `contextLimitationRefs` | `List[RefType]` | `contextLimitation` | `Ref (BswDistinguishedPartition)` | Refs | ok |
| `disabledInModeIRefs` | `List[ModeInBswModuleDescriptionInstanceRef]` | `disabledInMode` | `Ref (ModeInBswModuleDescriptionInstanceRef)` | IRefs | ok |
| `startsOnEventRef` | `Optional[RefType]` | `startsOnEvent` | `Ref (BswModuleEntity)` | Ref | ok |

## `BswTimingEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 89
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `period` | `Optional[TimeValue]` | `period` | `TimeValue` | Attr | ok |
| `periodMs` | `Optional[int]` (property) | — *(not in spec)* | — | — | added convenience property (ms from the `TimeValue` `period`, mirroring `ExecutableEntity.minimumStartIntervalMs`) |

No deviations beyond the recorded convenience property (2026-09-26 sync, Table 5.25, p.89): fabricated class docstring extension (BswScheduler/OS-timer sentence not in this table) and `__init__` docstring wiped, class/attribute docstrings rewritten verbatim from the markdown Note with constr_10281/constr_4043 recorded in the inline member comment, bare `TimeValue` setter parameter retyped to `Optional[TimeValue]` (0..1), old 3-col checklist replaced with the 6-column format (periodMs row marked "convenience, no spec row"); reader/writer already covered the `PERIOD` element via matched read/writeBswTimingEvent helpers + EVENTS dispatch + createBswTimingEvent factory

## `BswModeSwitchEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 94
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `activation` | `Optional[ModeActivationKind]` | `activation` | `ModeActivationKind` | Attr | ok |
| `modeIRefs` | `List[ModeInBswModuleDescriptionInstanceRef]` | `mode` | `ModeInBswModuleDescriptionInstanceRef` | IRefs | ok |

## `BswModeManagerErrorEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 95
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modeGroupRef` | `Optional[RefType]` | `modeGroup` | `Ref (ModeDeclarationGroupPrototype)` | Ref | ok |

No deviations (2026-09-26 sync, Table 5.33, p.95): bare `RefType` setter parameter retyped to
`Optional[RefType]` (0..1), fabricated class docstring (constr_4081 text not in this table)
and `__init__` docstring removed, paraphrased docstrings and the inline comment wiped and
rewritten verbatim from the markdown Note (constr_10286 appended to the inline comment), old
4-col checklist replaced by the 6-column checklist; no fake intake marker was present.
Reader/writer already covered the `MODE-GROUP-REF` element via matched
read/writeBswModeManagerErrorEvent helpers with dispatch + createBswModeManagerErrorEvent
factory on BswInternalBehavior; writer reads via the getter (no direct-field-read defect).
VP capability inherited via the BswEvent mixin (VARIATION-POINT lives in the ancestor
BSW-EVENT group; Rule 0020). Base drift observed (not this row): `readBswEvent` lacks a
`readIdentifiable` call while `writeBswEvent` calls `writeIdentifiable`
(BswEvent/BswScheduleEvent base-owned; both unstamped, no queue rows yet).

## `BswModeSwitchedAckEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 95
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modeGroupRef` | `Optional[RefType]` | `modeGroup` | `Ref (ModeDeclarationGroupPrototype)` | Ref | ok |

No deviations (2026-09-26 sync, Table 5.32, p.95): fabricated class docstring (constr_4026 text not in this table) and `__init__` docstring wiped, class/attribute docstrings rewritten verbatim from the markdown Note, bare `RefType` setter parameter retyped to `Optional[RefType]` (0..1), old 3-col checklist replaced with the 6-column format; reader/writer already covered the `MODE-GROUP-REF` element via matched read/writeBswModeSwitchedAckEvent helpers + EVENTS dispatch + createBswModeSwitchedAckEvent factory

## `BswAsynchronousServerCallReturnsEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 98
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `eventSourceRef` | `Optional[RefType]` | `eventSource` | `Ref (BswAsynchronousServerCallResultPoint)` | Ref | ok |

No deviations (2026-09-26 sync, Table 5.36, p.98): bare `RefType` setter parameter retyped to
`Optional[RefType]` (0..1), `__init__` docstring and paraphrased docstrings wiped and rewritten
verbatim from the markdown Note, 6-column checklist; reader/writer already covered the
`EVENT-SOURCE-REF` element via matched read/writeBswAsynchronousServerCallReturnsEvent helpers
with dispatch + createBswAsynchronousServerCallReturnsEvent factory on BswInternalBehavior.
Base drift observed (not this row): `readBswEvent` lacks a `readIdentifiable` call while
`writeBswEvent` calls `writeIdentifiable` (BswEvent/BswScheduleEvent base-owned; both
unstamped, no queue rows yet).

## `BswDataReceivedEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 99
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `dataRef` | `Optional[RefType]` | `data` | `Ref (VariableDataPrototype)` | Ref | ok |

No deviations (2026-09-26 sync, Table 5.37, p.99): bare `RefType` field/setter parameter
retyped to `Optional[RefType]` (0..1), missing None no-op on the setter added, `__init__`
docstring and paraphrased docstrings wiped and rewritten verbatim from the markdown Note,
stale 4-col checklist (unchecked getDataRef row) replaced by the 6-column checklist; no
fake intake marker was present. Reader/writer already covered the `DATA-REF` element via
matched read/writeBswDataReceivedEvent helpers with dispatch + createBswDataReceivedEvent
factory on BswInternalBehavior; writer reads via the getter (no direct-field-read defect).
Base drift observed (not this row): `readBswEvent` lacks a `readIdentifiable` call while
`writeBswEvent` calls `writeIdentifiable` (BswEvent/BswScheduleEvent base-owned; both
unstamped, no queue rows yet).

## `BswInternalTriggerOccurredEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 91
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `eventSourceRef` | `Optional[RefType]` | `eventSource` | `Ref (BswInternalTriggeringPoint)` | Ref | ok |

No deviations (2026-09-26 sync, Table 5.29, p.91): bare `RefType` field retyped to
`Optional[RefType]` (0..1), accessors typed, missing None no-op on the setter added,
fabricated class docstring and `__init__` docstring removed, paraphrased docstrings and
the fabricated inline comment wiped and rewritten verbatim from the markdown Note
(constr_10282 appended to the inline comment), stale 3-col checklist (unchecked
getEventSourceRef row) replaced by the 6-column checklist; no fake intake marker was
present. Reader/writer already covered the `EVENT-SOURCE-REF` element via matched
read/writeBswInternalTriggerOccurredEvent helpers with dispatch +
createBswInternalTriggerOccurredEvent factory on BswInternalBehavior; writer reads via
the getter (no direct-field-read defect). VP capability inherited via the BswEvent mixin
(VARIATION-POINT lives in the ancestor BSW-EVENT group; Rule 0020). Base drift observed
(not this row): `readBswEvent` lacks a `readIdentifiable` call while `writeBswEvent`
calls `writeIdentifiable` (BswEvent/BswScheduleEvent base-owned; both unstamped, no
queue rows yet).

## `BswModeSenderPolicy`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 102
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `ackRequest` | `Optional[BswModeSwitchAckRequest]` | `ackRequest` | `BswModeSwitchAckRequest` | aggr | ok |
| `enhancedModeApi` | `Optional[Boolean]` | `enhancedModeApi` | `Boolean` | attr | ok |
| `providedModeGroupRef` | `Optional[RefType]` | `providedModeGroup` | `Ref (ModeDeclarationGroupPrototype)` | ref | ok |
| `queueLength` | `Optional[PositiveInteger]` | `queueLength` | `PositiveInteger` | attr | ok |

## `BswModeSwitchAckRequest`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 103
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `timeout` | `Optional[TimeValue]` | `timeout` | `TimeValue` | attr | ok |

No deviations (2026-09-26 sync, Table 5.40, p.103): bare `Float` field retyped to
`Optional[TimeValue]`, accessors typed, None no-op added, docstrings rewritten verbatim from the
markdown Note, 6-column checklist; reader/writer already covered `ACK-REQUEST`/`TIMEOUT` via
matched get/setBswModeSwitchAckRequest helpers.

## `BswQueuedDataReceptionPolicy`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 105
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `queueLength` | `Optional[PositiveInteger]` | `queueLength` | `PositiveInteger` | attr | ok |

No deviations (2026-09-26 sync, Table 5.43, p.105): bare `PositiveInteger` field retyped to
`Optional[PositiveInteger]`, accessors typed, None no-op kept, fabricated class/`__init__`
docstrings and fake 4-col intake checklist removed, docstrings rewritten verbatim from the
markdown Note, 6-column checklist; reader/writer already covered the
`BSW-QUEUED-DATA-RECEPTION-POLICY` wrapper and `QUEUE-LENGTH` via matched
read/writeBswQueuedDataReceptionPolicy helpers. Base `BswDataReceptionPolicy` itself remains
unstamped/drifted (own queue row, not this pass).

## `BswTriggerDirectImplementation`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 102
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswTriggerDirectImplementation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `cat2Isr` | `Identifier` | — | missing |
| — *(missing)* | `—` | `masteredTriggerRef` | `Ref (Trigger)` | Ref | missing |
| — *(missing)* | `—` | `task` | `Identifier` | — | missing |

## `BswModeReceiverPolicy`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 103
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswModeReceiverPolicy.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `enhancedModeApi` | `Boolean` | — | missing |
| — *(missing)* | `—` | `requiredModeGroupRef` | `Ref (ModeDeclarationGroupPrototype)` | Ref | missing |
| — *(missing)* | `—` | `supportsAsynchronousModeSwitch` | `Boolean` | — | missing |

## `SwcBswSynchronizedModeGroupPrototype`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 111
- **Package:** `M2::AUTOSARTemplates::CommonStructure::SwcBswMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `bswModeGroupRef` | `Optional[RefType]` | `bswModeGroupRef` | `Ref (ModeDeclarationGroupPrototype)` | Ref | — |
| `swcModeGroupIRef` | `Optional[PModeGroupInAtomicSwcInstanceRef]` | `swcModeGroupIRef` | `PModeGroupInAtomicSwcInstanceRef` | IRef | — |

## `SwcBswSynchronizedTrigger`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 111
- **Package:** `M2::AUTOSARTemplates::CommonStructure::SwcBswMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `bswTriggerRef` | `Optional[RefType]` | `bswTriggerRef` | `Ref (Trigger)` | Ref | — |
| `swcTriggerIRef` | `Optional[PTriggerInAtomicSwcTypeInstanceRef]` | `swcTriggerIRef` | `PTriggerInAtomicSwcTypeInstanceRef` | IRef | — |

## `BswImplementation`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 120
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswImplementation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `debugInfo` | `Ref (EcucModuleConfigurationValues)` | — | deprecated (`atp.Status=removed`), not implemented |

## `Implementation`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 126
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Implementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|

## `DependencyOnArtifact`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 131
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Implementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py`

No deviations (multiplicity/type resolved to spec).

## `ProgramminglanguageEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 621
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Implementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py`

No deviations — members `C`/`CPP`/`JAVA` match the Table 8.2 literals `c`/`cpp`/`java`
1:1 (UPPER_CASE member names, member values = spec literals exactly, indexes 0/1/2 per
`atp.EnumerationLiteralIndex`); class docstring = Table 8.2 Note verbatim; standalone
`AREnum` (Steps 5/6 N/A — serialized as the `Implementation.programmingLanguage`
attribute value and round-tripped there).

## `Describable`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 438
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `removeAdminData` | — | — *(not in spec)* | — | — | added convenience method (resets `adminData` to `None`; used by the admin-data transformer) |

## `EngineeringObject`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/EngineeringObject.py`

No deviations (shortLabel/category/domain/revisionLabel multiplicity resolved to spec).

## `AutosarEngineeringObject`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/EngineeringObject.py`

No deviations (abstract base `EngineeringObject` carries the attributes; subclass has none of its own).

## `Linker`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 134
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Implementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py`

No deviations (vendor/version implemented per spec).

## `ResourceConsumption`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 137
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/__init__.py`

No deviations — all Table 8.1 attributes (`executionTime`, `heapUsage`, `memorySection`,
`sectionNamePrefix`, `stackUsage`) are implemented with parser/writer coverage. The
`accessCountSet` aggregation (defined in Table 4.22, `AccessCountSet`) is implemented
as well. The previously recorded `memoryUsage` member is **not** part of the R23-11
Table 8.1 and has been dropped.

## `MemorySection`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 144
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `alignment` | `Optional[AlignmentType]` | `alignment` | `AlignmentType` | Attr | ok |
| `executableEntityRefs` | `List[RefType]` | `executableEntity` | `Ref (ExecutableEntity)` | Ref `*` | ok (Rule 0001.5 Refs-suffix) |
| `memClassSymbol` | `Optional[CIdentifier]` | `memClassSymbol` | `CIdentifier` | Attr | legacy (R4.3.1 Table 9.2, p.145) — absent from the R23-11 Table 8.2 attribute rows but retained by the R23-11 XSD itself (MEM-CLASS-SYMBOL, atp.Status="removed", group MEMORY-SECTION, AUTOSAR_00052.xsd L80899); docstring verbatim from the R4.3.1 Note; kept with parser/writer coverage |
| `options` | `List[Identifier]` | `option` | `Identifier` | Attr `*` | ok (plural per Rule 0001.4) |
| `prefixRef` | `Optional[RefType]` | `prefix` | `Ref (SectionNamePrefix)` | Ref | ok (Rule 0001.5 ref-suffix) |
| `size` | `Optional[PositiveInteger]` | `size` | `PositiveInteger` | Attr | ok |
| `swAddrMethodRef` | `Optional[RefType]` | `swAddrmethod` | `Ref (SwAddrMethod)` | Ref | ok (Rule 0001.5 ref-suffix; `AddrMethod` casing matches sibling classes) |
| `symbol` | `Optional[Identifier]` | `symbol` | `Identifier` | Attr | ok |

2026-09-27 sync (Table 8.2, p.144): paraphrased docstrings wiped, rewritten verbatim from the R23-11
Notes; reader retyped to the spec-typed helpers (getChildElementOptionalAlignmentType,
getChildElementOptionalCIdentifier, getChildElementIdentifierValueList,
getChildElementOptionalIdentifier); writer retyped accordingly (setChildElementOptionalAlignmentType,
setChildElementOptionalCIdentifier, setChildElementOptionalIdentifier, OPTIONS items via
setChildElementOptionalIdentifier); VARIATION-POINT ordering fixed for the XSD group sequence
(writeIdentifiable called with write_variation_point=False, VP emitted after SYMBOL per
seqOffset=10000, AUTOSAR_00052.xsd group MEMORY-SECTION L80899). Stamp deferred to batch
confirmation.

## `SectionNamePrefix`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 147
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `implementedInRef` | `Optional[RefType]` | `implementedIn` | `Ref (DependencyOnArtifact)` | Ref | ok (Rule 0001.5 ref-suffix) |

2026-09-27 sync (Table 8.8, p.147): docstrings rewritten verbatim from the R23-11 Note; reader
switched readReferrable → readImplementationProps so the inherited SYMBOL (IMPLEMENTATION-PROPS
group) round-trips (Rule 0001.7); VARIATION-POINT read/write coverage added (Referrable-level VP,
per the readBswModuleCallPoint precedent); writer switched writeReferrable → writeImplementationProps
plus trailing writeVariationPoint (XSD group order REFERRABLE → IMPLEMENTATION-PROPS →
SECTION-NAME-PREFIX → VARIATION-POINT, AUTOSAR_00052.xsd L102807/L102840). Stamp deferred to batch
confirmation.

## `StackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 149
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `executableEntityRef` | `Optional[RefType]` | `executableEntity` | `ExecutableEntity` | ref | ok (Rule 0001.5 Ref suffix) |
| `hardwareConfiguration` | `Optional[HardwareConfiguration]` | `hardwareConfiguration` | `HardwareConfiguration` | aggr | ok (markdown row renders "hardware Configuration" — line-wrap artifact) |
| `hwElementRef` | `Optional[RefType]` | `hwElement` | `HwElement` | ref | ok (Rule 0001.5 Ref suffix) |
| `softwareContext` | `Optional[SoftwareContext]` | `softwareContext` | `SoftwareContext` | aggr | ok |

No deviations (abstract base per the spec header — TypeError guard kept; tested through concrete
subclasses; the shared readStackUsage/setStackUsage helpers are the Rule 0001.7 abstract
XML-bearing-base helpers called by all three subclass readers/writers).

2026-09-27 sync (Table 8.9, p.149): stale 4-column checklist replaced with the 6-column format (stamp
deferred to batch confirmation); fabricated class-docstring second sentence removed and `__init__`
docstrings/paraphrase accessor docstrings wiped and rewritten verbatim from the R23-11 Notes;
HardwareConfiguration/SoftwareContext imports moved from TYPE_CHECKING-only to a bottom-of-module
runtime cycle-breaker (Rule 0005) so get_type_hints resolves (Rule 0001.8); writer setStackUsage now
emits VARIATION-POINT after SOFTWARE-CONTEXT (writeIdentifiable with write_variation_point=False +
trailing writeVariationPoint, XSD seqOffset=10000 per AUTOSAR_00052.xsd group STACK-USAGE L111994) —
previously the VP was emitted inside the identifiable block; reader readStackUsage reordered to the
XSD group order EXECUTABLE-ENTITY-REF → HARDWARE-CONFIGURATION → HW-ELEMENT-REF → SOFTWARE-CONTEXT
(VARIATION-POINT is read inside readIdentifiable). Tests: test_StackUsage.py (model),
test_stack_usage.py (parser + writer).

## `WorstCaseStackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 150
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `memoryConsumption` | `Optional[PositiveInteger]` | `memoryConsumption` | `PositiveInteger` | attr | ok (markdown row renders "memory Consumption" — line-wrap artifact) |

No deviations.

2026-09-27 sync (Table 8.10, p.150): stale 4-column checklist replaced with the 6-column format (stamp
deferred to batch confirmation); fabricated class-docstring second sentence removed and `__init__`
docstring/paraphrase accessor docstrings wiped and rewritten verbatim from the R23-11 Note. Parser/writer
coverage already asserted the field end-to-end via the family tests (Table 8.9 step). Tests:
test_StackUsage.py (model).

## `MeasuredStackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 150
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `averageMemoryConsumption` | `Optional[PositiveInteger]` | `averageMemoryConsumption` | `PositiveInteger` | attr | ok (markdown row renders "averageMemory Consumption" — line-wrap artifact) |
| `maximumMemoryConsumption` | `Optional[PositiveInteger]` | `maximumMemoryConsumption` | `PositiveInteger` | attr | ok (markdown row renders "maximum Memory Consumption" — line-wrap artifact) |
| `minimumMemoryConsumption` | `Optional[PositiveInteger]` | `minimumMemoryConsumption` | `PositiveInteger` | attr | ok (markdown row renders "minimum Memory Consumption" — line-wrap artifact) |
| `testPattern` | `Optional[String]` | `testPattern` | `String` | attr | ok |

No deviations.

2026-09-27 sync (Table 8.11, p.150): stale 4-column checklist replaced with the 6-column format (stamp
deferred to batch confirmation); fabricated class-docstring second sentence removed and `__init__`
docstring/paraphrase accessor docstrings wiped and rewritten verbatim from the R23-11 Notes; testPattern
inline Note fixed to "Description of the test pattern used to acquire the measured values.". Parser/writer
coverage already asserted all four fields via the family tests (Table 8.9 step). Tests: test_StackUsage.py
(model).

## `RoughEstimateStackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 151
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `memoryConsumption` | `Optional[PositiveInteger]` | `memoryConsumption` | `PositiveInteger` | attr | ok (markdown row renders "memory Consumption" — line-wrap artifact) |

No deviations.

2026-09-27 sync (Table 8.12, p.151): stale 4-column checklist replaced with the 6-column format (stamp
deferred to batch confirmation); fabricated class-docstring second sentence removed and `__init__`
docstring/paraphrase accessor docstrings wiped and rewritten verbatim from the R23-11 Note. Parser/writer
coverage already asserted the field end-to-end via the family tests (Table 8.9 step). Tests:
test_StackUsage.py (model).

## `HeapUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 152
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py`

No deviations (abstract base; tested through concrete subclasses).

## `WorstCaseHeapUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 152
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py`

No deviations.

## `MeasuredHeapUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 152
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py`

No deviations.

## `RoughEstimateHeapUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 153
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py`

No deviations.

## `HardwareConfiguration`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 161
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `additionalInformation` | `Optional[String]` | `additionalInformation` | `String` | Attr | ok (markdown Note renders "Hardware Configuration" — line-wrap artifact of "HardwareConfiguration", cf. XSD documentation) |
| `processorMode` | `Optional[String]` | `processorMode` | `String` | Attr | ok |
| `processorSpeed` | `Optional[String]` | `processorSpeed` | `String` | Attr | ok |

2026-09-27 sync (Table 8.18, p.161): stale 4-column checklist replaced with the 6-column format (stamp
deferred to batch confirmation); `__init__` docstring removed and paraphrase accessor docstrings wiped
and rewritten verbatim from the R23-11 Notes (the existence constraints constr_10315..10317 are separate
spec items, not part of the Note cells); source path corrected to the non-leaf package `__init__.py` (the
previously recorded `HardwareConfiguration.py` file does not exist). Reader/writer (readHardwareConfiguration
/ setHardwareConfiguration) pre-existed with the XSD group order ADDITIONAL-INFORMATION → PROCESSOR-MODE →
PROCESSOR-SPEED (AUTOSAR_00052.xsd L65234) and were verified by new parser/writer tests — no source change.
Tests: test_ResourceConsumption.py::TestHardwareConfiguration (model), test_hardware_configuration.py (parser + writer).

## `SoftwareContext`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 163
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `input` | `Optional[String]` | `input` | `String` | Attr | ok |
| `state` | `Optional[String]` | `state` | `String` | Attr | ok (markdown Note renders "the Execution Time is provided" — line-wrap artifact of "ExecutionTime", cf. XSD documentation) |

2026-09-27 sync (Table 8.20, p.163): stale 4-column checklist replaced with the 6-column format (stamp
deferred to batch confirmation); `__init__` docstring removed and paraphrase accessor docstrings wiped
and rewritten verbatim from the R23-11 Notes (the existence constraints constr_10320/10321 are separate
spec items, not part of the Note cells); source path corrected to the non-leaf package `__init__.py` (the
previously recorded `SoftwareContext.py` file does not exist). Reader/writer (readSoftwareContext /
setSoftwareContext) pre-existed with the XSD group order INPUT → STATE (AUTOSAR_00052.xsd L109295) and
were verified by new parser/writer tests — no source change. Tests: test_ResourceConsumption.py::TestSoftwareContext
(model), test_software_context.py (parser + writer).

## `ExecutionTime`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 159
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py`

No deviations (abstract base; tested through concrete subclasses).

## `MemorySectionLocation`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 162
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py`

No deviations.

## `MultidimensionalTime`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 164
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/MultidimensionalTime.py`

No deviations.

> Resolution Note (sync 2026-09-24): resynced against the home document `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`, Table 4.74, p.165 — the BSWModuleDescriptionTemplate Table 8.22 row above is a byte-equivalent reproduction, and its p.164 page reference was off by one (actual p.165). Fields/accessors match the spec exactly (cseCode CseCodeType 0..1, cseCodeFactor Integer 0..1, displayed order cseCode→cseCodeFactor); no naming/type/missing deviations. Sync fixes: the old 4-column checklist and the pre-existing `# Spec verified: R23-11` stamp were replaced with the 6-column format (marker withheld pending batch confirmation); fabricated class-docstring paragraphs and "Gets/Sets the…" paraphrase docstrings wiped and rewritten verbatim from the spec Notes; reader type gap fixed — parser/writer now use the matched `getChildElementOptionalCseCodeType`/`setChildElementOptionalCseCodeType` leaf pair (cseCode round-trips as CseCodeType, not plain ARLiteral). Tests: test_MultidimensionalTime.py (model), test_multidimensional_time.py (parser + writer).

## `LifeCyclePeriod`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 392 (Table 12.4)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::LifeCycles`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py`

**Note:** Synced 2026-09-24 against R23-11 Table 12.4 (R4.3.1 Table 11.4 reproduction byte-identical, same displayed order). Deviations found and fixed during the sync — no open rows remain: `date` retyped `Optional[datetime]` → `Optional[DateTime]` per the spec DateTime type (reader now uses the matched `getChildElementOptionalDateTime` helper, whose ARLiteral-delegating body was fixed to instantiate `DateTime` — the same reader type gap previously fixed for CseCodeType); reader/writer coverage extended from AR-RELEASE-VERSION-only to all three attributes with XSD sequenceOffset emission order DATE → AR-RELEASE-VERSION → PRODUCT-RELEASE (consumer wiring of PERIOD-END / DEFAULT-PERIOD-BEGIN / DEFAULT-PERIOD-END belongs to the LifeCycleInfo / LifeCycleInfoSet syncs). Stamp (`# Spec verified: R23-11`) deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All Table 12.4 attributes implemented: `arReleaseVersion` (`Optional[RevisionLabelString]`, 0..1, attr, xml.sequenceOffset=20), `date` (`Optional[DateTime]`, 0..1, attr, xml.sequenceOffset=10), `productRelease` (`Optional[RevisionLabelString]`, 0..1, attr, xml.sequenceOffset=30); setters None-no-op + chaining; docstrings verbatim from the table Notes. |

## `LifeCycleInfo`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 392-393 (Table 12.5)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::LifeCycles`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py`

**Note:** Synced 2026-09-24 against R23-11 Table 12.5 (page-split table: body main fragment p.392, `Table 12.5` caption + continuation fragment p.393; R4.3.1 Table 11.5 p.364 reproduction identical except useInstead Note "must" vs R23-11 "shall"; appendix Table C.63 carries the identical Note — the FO GST table cited). Deviations found and fixed during the sync — no open rows remain: PERIOD-END was silently dropped by both `readLifeCycleInfo` and `writeLifeCycleInfo` — reader now reads `setPeriodEnd(getLifeCyclePeriod(element, "PERIOD-END"))` and writer emits `setLifeCyclePeriod(child, "PERIOD-END", getPeriodEnd())` in XSD group LIFE-CYCLE-INFO order (LC-OBJECT-REF → LC-STATE-REF → PERIOD-BEGIN → PERIOD-END → REMARK → USE-INSTEAD-REFS); setters/addUseInsteadRef gained the family `Optional[T]` value + chained-return annotations; fabricated class docstring and "Gets/Sets the…" paraphrase docstrings wiped and rewritten verbatim from the table Notes; old 4-column checklist rebuilt 6-column with release column (marker withheld pending batch confirmation). The LifeCycleInfoSet-level DEFAULT-PERIOD-BEGIN/DEFAULT-PERIOD-END reader/writer wiring belongs to the LifeCycleInfoSet sync.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All Table 12.5 attributes implemented: `lcObjectRef` (`Optional[RefType]`, 1, ref — LC-OBJECT-REF), `lcStateRef` (`Optional[RefType]`, 0..1, ref — LC-STATE-REF), `periodBegin` (`Optional[LifeCyclePeriod]`, 0..1, aggr — PERIOD-BEGIN), `periodEnd` (`Optional[LifeCyclePeriod]`, 0..1, aggr — PERIOD-END), `remark` (`Optional[DocumentationBlock]`, 0..1, aggr — REMARK), `useInsteadRefs` (`List[RefType]`, *, ref — USE-INSTEAD-REFS wrapper with unbounded USE-INSTEAD-REF); setters/add None-no-op + chaining; docstrings verbatim from the table Notes. |

## `LifeCycleInfoSet`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 392 (Table 12.3)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::LifeCycles`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py`

**Note:** Synced 2026-09-24 against R23-11 Table 12.3 (page-split table: body main fragment + `Table 12.3` caption + continuation fragment all on p.392; R4.3.1 Table 11.3 p.363 reproduction identical on Note/Base/attribute rows with no Aggregated-by row — the FO GST table cited). Deviations found and fixed during the sync — no open rows remain: DEFAULT-PERIOD-BEGIN/DEFAULT-PERIOD-END were silently dropped by both `readLifeCycleInfoSet` and `writeLifeCycleInfoSet` (the gap the LifeCyclePeriod/LifeCycleInfo syncs deliberately left to this row) — reader now reads `setDefaultPeriodBegin/End(getLifeCyclePeriod(element, "DEFAULT-PERIOD-BEGIN"/"DEFAULT-PERIOD-END"))` and writer emits `setLifeCyclePeriod(child, "DEFAULT-PERIOD-BEGIN"/"DEFAULT-PERIOD-END", getDefaultPeriodBegin/End())` in XSD group LIFE-CYCLE-INFO-SET order (DEFAULT-LC-STATE-REF → DEFAULT-PERIOD-BEGIN → DEFAULT-PERIOD-END → LIFE-CYCLE-INFOS → USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF); the five setter/add signatures gained the family `Optional[T]` value + `-> "LifeCycleInfoSet"` chained-return annotations and the `__init__` attribute blocks gained the mandatory blank lines; fabricated class docstring and "Gets/Sets the…" paraphrase docstrings wiped and rewritten verbatim from the table Notes (class Note keeps its `Tags: atp.recommendedPackage=LifeCycleInfoSets` tail); old 4-column checklist rebuilt 6-column with release column (marker withheld pending batch confirmation). Consumer wiring (readARPackageElements dispatch, ARElement writer branch, `ARPackage.createLifeCycleInfoSet` factory) pre-existed from the orphan intake and was verified, not rewritten.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All Table 12.3 attributes implemented: `defaultLcStateRef` (`Optional[RefType]`, 1, ref — DEFAULT-LC-STATE-REF, DEST LIFE-CYCLE-STATE--SUBTYPES-ENUM), `defaultPeriodBegin` (`Optional[LifeCyclePeriod]`, 0..1, aggr — DEFAULT-PERIOD-BEGIN), `defaultPeriodEnd` (`Optional[LifeCyclePeriod]`, 0..1, aggr — DEFAULT-PERIOD-END), `lifeCycleInfos` (`List[LifeCycleInfo]`, *, aggr — LIFE-CYCLE-INFOS wrapper with unbounded LIFE-CYCLE-INFO + addLifeCycleInfo), `usedLifeCycleStateDefinitionGroupRef` (`Optional[RefType]`, 1, ref — USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF, DEST LIFE-CYCLE-STATE-DEFINITION-GROUP--SUBTYPES-ENUM); setters/add None-no-op + chaining; docstrings verbatim from the table Notes. |

## `AnalyzedExecutionTime`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 164
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py`

No deviations.

## `MeasuredExecutionTime`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 166
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py`

No deviations.

## `SimulatedExecutionTime`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 167
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py`

No deviations.

## `RoughEstimateOfExecutionTime`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 167
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py`

No deviations.

## `AccessCount`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 57
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py`

No deviations.

## `AccessCountSet`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 57
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py`

No deviations — `accessCountSet` is aggregated by `ResourceConsumption` (see Table 4.22 "Aggregated by" row).

## `McSupportData`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 172
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

No deviations — all Table 9.1 attributes (`emulationSupport` via `addEmulationSupport`, `mcParameterInstance`/`mcVariableInstance` via `createMcParameterInstance`/`createMcVariableInstance`, `measurableSystemConstantValues` refs, `rptSupportData`) are implemented with parser/writer coverage (`readMcSupportData`/`writeMcSupportData` hooked into `readImplementation`/`writeImplementation`).

Note:
- `McDataInstance` is fully aligned (Table 9.4 + XSD additions) and serialized with its inner attributes (`readMcDataInstance`/`writeMcDataInstance`).
- The RptSupport children are aligned and serialized recursively under `RPT-SUPPORT-DATA`.
- `McSwEmulationMethodSupport` is aligned and serialized with its inner attributes (`readMcSwEmulationMethodSupport`/`writeMcSwEmulationMethodSupport`), replacing the earlier identity-only placeholder.

## `AliasNameSet`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 174
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

Model aligned: inherits `ARElement` (spec `Base`) with `__init__(self, parent, short_name)`;
the single spec attribute `aliasName` (`AliasNameAssignment`, `*`, `aggr`) is modeled as
`aliasNames`/`addAliasName`/`getAliasNames` (the earlier `alias`/`aliases` naming deviation
has been fixed and this row cleared).

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(pending)* | `—` | `aliasName` | `AliasNameAssignment` | aggr | parser/writer coverage pending the aggregated child `AliasNameAssignment`'s own alignment pass (it still carries fabricated `aliasName`/`elementRef` and is missing `shortLabel`/`label`/`identifiableRef`/`flatInstanceRef`); `AliasNameSet` is not yet wired into any `ARPackage.element` dispatch |

## `AliasNameAssignment`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 175
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

Model aligned: the four spec attributes `shortLabel` (String), `label`
(MultilanguageLongName), `identifiableRef` (Ref → Identifiable) and
`flatInstanceRef` (Ref → FlatInstanceDescriptor) are implemented in
sequenceOffset order (10/20/50/60). Two fabricated fields were removed:
`aliasName` (a `str` shadowing spec `shortLabel`) and `elementRef`
(an `AnyInstanceRef` collapsing the two mutually-exclusive spec refs
`identifiable` + `flatInstance` into one) — these had not been tracked as
fabricated; only the *missing* spec attributes had rows (the code→spec
direction of the cross-check had not been run).

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(pending)* | `—` | `shortLabel`/`label`/`identifiableRef`/`flatInstanceRef` | String / MultilanguageLongName / Ref / Ref | attr/aggr/ref/ref | parser/writer coverage pending `AliasNameSet`'s wiring into the `ARPackage.element` read/write dispatch (`AliasNameAssignment` is never a standalone element; it is serialized only inside `ALIAS-NAME-SET/ALIAS-NAMES`) |

## `FlatMap`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 966
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

Model aligned 2026-09-05 (Table 14.1): heritage fixed `AtpBlueprintable` → `ARElement`
(spec `Base` most-derived; restores the `CollectableElement` → `PackageableElement` →
`ARElement` chain required by the `ARPackage.element` aggregation and re-enables the
inherited `VariationPointCapable` of `PackageableElement`, so the XSD `VARIATION-POINT`
(PACKAGEABLE-ELEMENT group, "Applicable for: ARPackage.element") round-trips through
`readIdentifiable`/`writeIdentifiable` instead of being dropped with a parser warning).
`getInstances()` now returns the dedicated `instances` field directly (was an
`elements`-registry isinstance filter — Rule 0004 to-fix, cleared).

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `instances` | `List[FlatInstanceDescriptor]` | `instance` | `FlatInstanceDescriptor` | aggr | - (conforms Table 14.1; spec-singular `*` name maps to the plural field + `createFlatInstanceDescriptor`/`getInstances` per Rule 0001.4/0001.6) |

## `FlatInstanceDescriptor`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 967
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

Model aligned 2026-09-05 (Table 14.2): all five spec attributes implemented with typed
`Optional[T]` fields/accessors and full reader/writer coverage in XSD group order
(ROLE, RTE-PLUGIN-PROPS, SW-DATA-DEF-PROPS, UPSTREAM-REFERENCE-IREF,
ECU-EXTRACT-REFERENCE-IREF; VARIATION-POINT via the `VariationPointCapable` mixin
through `readIdentifiable`/`writeIdentifiable`). The iref members keep the `IRef` Kind
suffix (`ecuExtractReferenceIRef`/`upstreamReferenceIRef` typed `AnyInstanceRef` per
"InstanceRef implemented by: AnyInstanceRef"). Prior bare-`T`/unannotated `0..1` fields
retyped per the spec `Mult.` column.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `rtePluginProps` | `Optional[RtePluginProps]` | `rtePluginProps` | `RtePluginProps` | aggr | - (conforms Table 14.2; nested references now serialize via the aligned RtePluginProps reader/writer) |

## `RtePluginProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 971
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

No deviations — Table 14.5's two optional references are modeled and covered by the
reader/writer in XSD order.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `associatedCrossSwClusterComRtePluginRef` | `Optional[RefType]` | `associatedCrossSwClusterComRtePlugin` | `EcucContainerValue` | ref | - |
| `associatedRtePluginRef` | `Optional[RefType]` | `associatedRtePlugin` | `EcucContainerValue` | ref | - |

## `McDataInstance`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 177
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

No deviations — all Table 9.4 attributes (`role`, `rptImplPolicy`, `subElement`, `symbol`) plus the XSD-only attributes the PDF table omits (`arraySize`, `displayIdentifier`, `flatMapEntryRef`, `instanceInMemory`, `mcDataAccessDetails`, `mcDataAssignment`, `resultingProperties`, `resultingRptSwPrototypingAccess`) are implemented with parser/writer coverage (`readMcDataInstance`/`writeMcDataInstance`). Note: `instanceInMemory` is typed as the concrete `ImplementationElementInParameterInstanceRef` (an `ARObject`, not a `RefType`) and serialized as a typed iref with `CONTEXT-REF`/`TARGET-REF` directly under the `INSTANCE-IN-MEMORY` element; the child classes it aggregates (`McDataAccessDetails`, `RoleBasedMcDataAssignment`, `SwDataDefProps`, `RptSwPrototypingAccess`) are carried with their own coverage where aligned and by identity where not.

## `McSwEmulationMethodSupport`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 180
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

No deviations — all Table 9.5 attributes (`baseReference`, `category`, `elementGroup`, `referenceTable`, `shortLabel`) are implemented with parser/writer coverage (`readMcSwEmulationMethodSupport`/`writeMcSwEmulationMethodSupport`, reached from `readMcSupportData`/`writeMcSupportData`). `elementGroup` is an `aggr` of `McParameterElementGroup` (`*`) serialized through the `ELEMENT-GROUPS`/`MC-PARAMETER-ELEMENT-GROUP` wrapper; the earlier tracker rows mistyped it as a ref and omitted `shortLabel` entirely. The previously fabricated `emulationMethodName` field (no spec basis, PDF or XSD) has been removed.

## `McParameterElementGroup`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 181
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

No deviations — all Table 9.6 attributes (`ramLocation`, `romLocation`, `shortLabel`) are implemented with parser/writer coverage (`readMcParameterElementGroup`/`writeMcParameterElementGroup`). The previously fabricated `parameterRefs` list (no spec basis, PDF or XSD) has been removed; `shortLabel` was missing from the earlier tracker rows.

## `ImplementationElementInParameterInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 184
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

No deviations — all Table 9.7 attributes (`context`, `target`) are implemented with parser/writer coverage (`readImplementationElementInParameterInstanceRef`/`writeMcDataInstance`). The class's base was corrected from `RefType` to `ARObject` (spec `Base` row; the earlier `RefType` base was a hierarchy mismatch flagged by `reports/deviation_class_hierarchy_mismatches.md`); `INSTANCE-IN-MEMORY` is a typed iref and is serialized with `CONTEXT-REF`/`TARGET-REF` directly under the `INSTANCE-IN-MEMORY` element, not as a flat ref. The earlier tracker rows recorded `contextRef`/`targetRef` as missing; they are now implemented.

## `McFunction`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 186
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

No deviations — all Table 9.8 attributes (`defCalprmSet`, `refCalprmSet`, `inMeasurementSet`, `locMeasurementSet`, `outMeasurementSet`, `subFunction`) are implemented with parser/writer coverage (`readMcFunction`/`writeMcFunction`, dispatched from `readARPackageElements`/`writeARPackageElement` via the new `ARPackage.createMcFunction`/`getMcFunctions`). The class's base was corrected from `ARObject` to `Identifiable` (spec `Base` row ends in `Packageable`/`Identifiable`), making `McFunction` a real `ARPackage.element`. The earlier tracker rows recorded the deprecated `outMeasurmentSet` (XSD `atp.Status="removed"` — "Due to miss spell was set to obsolete. Please use outMeasurementSet instead.") as a separate missing attribute; it is correctly **not** modeled.

## `McFunctionDataRefSet`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 187
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py`

No deviations — all Table 9.9 attributes (`flatMapEntry`, `mcDataInstance`) are implemented with parser/writer coverage (`readMcFunctionDataRefSet`/`writeMcFunctionDataRefSet`). The class is `<<atpVariation>>`: the XSD nests its attributes under `<MC-FUNCTION-DATA-REF-SET-VARIANTS>/<MC-FUNCTION-DATA-REF-SET-CONDITIONAL>`, and per the established cluster-class precedent (`LinCluster`/`CanCluster`/`FlexrayCluster`) the wrapper is read/written transparently into the owning object — no separate `McFunctionDataRefSetConditional` model class, and no `variationPoint` is modeled. The earlier tracker row recorded `mcFunctionDataRefSetVariant` (the alternative explicit `Variants`/`Conditional` modeling) as missing; the transparent wrapper is the codebase-consistent choice.

## `McGroup`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 190
- **Package:** `M2::AUTOSARTemplates::CommonStructure::McGroups`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py`

No deviations — all Table 9.10 attributes (`mcFunction`, `refCalprmSet`, `refMeasurementSet`, `subGroup`) are implemented with parser/writer coverage (`readMcGroup`/`writeMcGroup`, dispatched from `readARPackageElements`/`writeARPackageElement` via the new `ARPackage.createMcGroup`/`getMcGroups`). The class's base was corrected from `ARObject` to `ARElement` (the spec `Base` row names `ARElement`, the most-derived model class that exists in the codebase), making `McGroup` a real `ARPackage.element`. Note: the sibling `McFunction` models the same `Base` chain with `Identifiable`; McGroup follows the spec's most-derived `ARElement` per Rule 1.2 (see the Rule 1.2 generalization in `class_check_rules.md`).

## `McGroupDataRefSet`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 191
- **Package:** `M2::AUTOSARTemplates::CommonStructure::McGroups`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py`

No deviations — all Table 9.11 attributes (`flatMapEntry`, `mcDataInstance`) are implemented with parser/writer coverage (`readMcGroupDataRefSet`/`writeMcGroupDataRefSet`). The class is `<<atpVariation>>`: the XSD nests its attributes under `<MC-GROUP-DATA-REF-SET-VARIANTS>/<MC-GROUP-DATA-REF-SET-CONDITIONAL>`, and per the established cluster-class precedent (`LinCluster`/`CanCluster`/`FlexrayCluster`, and the sibling `McFunctionDataRefSet`) the wrapper is read/written transparently into the owning object — no separate `McGroupDataRefSetConditional` model class, and no `variationPoint` is modeled. The earlier tracker row recorded `mcGroupDataRefSetVariant` (the alternative explicit `Variants`/`Conditional` modeling) as missing; the transparent wrapper is the codebase-consistent choice.

## `McDataAccessDetails`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 195
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

No deviations — all Table 9.12 attributes (`rteEvent`, `variableAccess`) are implemented as `*` iref lists with parser/writer coverage (`readMcDataAccessDetails`/`writeMcDataAccessDetails`, wired into `readMcDataInstance`/`writeMcDataInstance`). The earlier placeholder implementation was a Rule 1.3 whole-class stub: the fabricated fields `accessType`/`address` appeared nowhere in the spec and were removed. The two `iref` element types were missing and were implemented first per Rule 1.10 as `RteEventInEcuInstanceRef`/`VariableAccessInEcuInstanceRef` (concrete subclasses of the existing abstract `AtpInstanceRef`), co-located in this package alongside the sibling iref `ImplementationElementInParameterInstanceRef`. Note on the iref classes: they have **no own spec table** in any rendered PDF (their inner attributes — `contextRootComposition`, `contextAtomicComponent`, `targetRteEvent`/`targetVariableAccess` — are defined only in the XSD groups `RTE-EVENT-IN-ECU-INSTANCE-REF`/`VARIABLE-ACCESS-IN-ECU-INSTANCE-REF`), so their checklists carry **no `# Spec:` line and no `# Spec verified:` marker** and every row stays `[ ]` — nothing about them is PDF-confirmed; `base` is `atpDerived` (field + accessor, no XML element).

## `RptSupportData`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 198
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py`

No deviations — all Table 9.13 attributes (`executionContext`, `rptComponent`, `rptServicePoint`) implemented via `createXXX(short_name)` factories (all three children are `Identifiable`) with parser/writer coverage (`readRptSupportData`/`writeRptSupportData`).

## `RptComponent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 199
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py`

No deviations — all Table 9.15 attributes (`mcDataAssignment`, `rpImplPolicy`, `rptExecutableEntity`) implemented with parser/writer coverage (`readRptComponent`/`writeRptComponent`).

## `RptSwPrototypingAccess`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 199
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py`

No deviations — all Table 9.14 attributes (`rptHookAccess`, `rptReadAccess`, `rptWriteAccess`) implemented with parser/writer coverage (`readRptSwPrototypingAccess`/`writeRptSwPrototypingAccess`).

## `RptExecutableEntity`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 200
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py`

No deviations — all Table 9.16 attributes (`rptExecutableEntityEvent`, `rptRead`, `rptWrite`, `symbol`) implemented with parser/writer coverage (`readRptExecutableEntity`/`writeRptExecutableEntity`).

## `RptExecutableEntityEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 201
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py`

No deviations — all Table 9.17 attributes (`executionContextRefs`, `mcDataAssignment`, `rptEventId`, `rptExecutableEntityProperties`, `rptImplPolicy`, `rptServicePointPostRefs`, `rptServicePointPreRefs`) implemented with parser/writer coverage (`readRptExecutableEntityEvent`/`writeRptExecutableEntityEvent`).

## `RptServicePoint`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 206
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py`

No deviations — all Table 9.26 attributes (`serviceId`, `symbol`) implemented with parser/writer coverage (`readRptServicePoint`/`writeRptServicePoint`).

## `BswServiceDependency`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 225
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

Aligned to `class_check_rules.md` on 2026-08-07. Rule-compliance fixes applied this pass:
- **Rule 3 (type hints):** all 8 accessors (`getAssignedData`, `addAssignedData`, `getAssignedEntryRole`, `addAssignedEntryRole`, `getIdent`, `setIdent`, `getServiceNeeds`, `setServiceNeeds`) were untyped — now annotated with `List[T]` / `Optional[T]` return and `Optional[T]` parameters returning `"BswServiceDependency"`. Fields `ident` / `serviceNeeds` corrected from `T = None` to `Optional[T] = None`.
- **Rule 4 (no-op on None):** `addAssignedData` / `addAssignedEntryRole` appended the value unconditionally (a `None` would be appended) — now guarded with `if value is not None:`. Docstrings gained the "None value is a no-op" sentence.
- **Rule 4.1 (abstract base uniformity):** the inherited `ServiceDependency.addAssignedDataType`, `setDiagnosticRelevance`, `setSymbolicNameProps` were unguarded and untyped — aligned to the uniform `if value is not None:` guard + `Optional[T]` signatures (see the `ServiceDependency` tracker row).
- **Rule 2 (checklist):** stale `[ ]` rows (every accessor was `[ ]` despite impl/docstring/test existing) crossed to `[x]`; the `Spec verified: R23-11` marker was already present.

Residual deviations (intentionally **not** serialized this pass — recorded honestly rather than claimed covered):
- **`symbolicNameProps` (0..1, `SymbolicNameProps`):** RESOLVED 2026-08-07 (re-synced to PDF 2026-08-07). Spec `Table 7.59` (`SWCT`): `SymbolicNameProps` Base = `ARObject, ImplementationProps, Referrable` with **no own attributes**; aggregated by `ServiceDependency.symbolicNameProps` (0..1, aggr). The XSD `SYMBOLIC-NAME-PROPS` complexType = `AR-OBJECT` + `REFERRABLE` + `IMPLEMENTATION-PROPS` (and an empty own group). `SymbolicNameProps` therefore inherits `ImplementationProps` (giving the `symbol` / `SYMBOL` 0..1 `C-Identifier` attr) and `Referrable` (SHORT-NAME), and has **no** `symbolicName` field — the earlier `symbolicName: String` attribute was spurious (no `SYMBOLIC-NAME` XSD element exists) and was removed. `readSymbolicNameProps` / `writeSymbolicNameProps` now call `readImplementationProps` / `writeImplementationProps`, serializing both `SHORT-NAME` and `SYMBOL`, wired into base + both subtype readers/writers. Tests: parser `test_readBswServiceDependency_symbolic_name_props` (with `SYMBOL`), writer `test_writeBswServiceDependency_symbolic_name_props` (with `SYMBOL`), model `TestSymbolicNameProps` (inherited `symbol` + `issubclass(ImplementationProps)`). The aggregation on `ServiceDependency` (0..1, aggr) matches spec `Table 7.57`.
- **`diagnosticRelevance` (0..1, `ServiceDiagnosticRelevanceEnum`):** declared in spec Table 12.1 but **absent** from the `SERVICE-DEPENDENCY` XSD group (no `DIAGNOSTIC-RELEVANCE` element at all). It is a model-only attribute with no serialization element — recorded as a deviation, not a coverage gap.
- The parser/writer five-place dispatch for `BswServiceDependency` is already correct: `readBswServiceDependency` calls `readARObjectAttributes` (not `readIdentifiable`, since the class is non-Referrable) and `getBswServiceDependencyIdent` builds the nested `ident` via `BswServiceDependencyIdent(parent, short_name)`; the writer mirrors this. No change needed there.

## `BswServiceDependencyIdent`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 240
- **Package:** `M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

Has its own spec table — `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf` Table 5.16 — a `Class` table whose `Attribute` section is empty (`-` rows), because every attribute is inherited from `IdentCaption` (Base chain ends in `IdentCaption` → `Identifiable` → `Referrable`). This is **not** the "no own spec table" exception (Rule 1.5/13.1): that exception is for classes with no rendered PDF table at all, not for classes whose rendered PDF `Class` table simply contributes no *new* attributes. The class therefore carries a `# Spec:` line + `# Spec verified: R23-11` marker and a checklist listing only the methods it defines itself (`__init__`, all `[x]`). No deviations: no own attributes to implement; `ident` (0..1, aggr) on `BswServiceDependency` already has parser/writer coverage (`getBswServiceDependencyIdent`).

- **Rule 8 (package location) — OPEN:** the spec `Package` is `DiagnosticExtract::DiagnosticMapping::ServiceMapping`, but the class is currently defined in `BswModuleTemplate/BswBehavior.py` alongside its aggregator `BswServiceDependency` (Table 12.2). The sibling `IdentCaption` subclasses (`ModeAccessPointIdent`, `ExternalTriggeringPointIdent`, `DiagnosticParameterIdent`) are likewise defined next to their aggregators rather than in their nominal spec packages. Relocating would touch the model module, `BswServiceDependency.ident` annotation, parser/writer, top-level `models/__init__.py` exports, and imports in `test_BswBehavior.py` / `test_writer_bsw_module.py`. Deferred pending a separate pass; recorded here so the placement is a known, intentional deviation rather than an unconsidered one.

## `RoleBasedBswModuleEntryAssignment`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 226
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

No deviations — all attributes (`assignedEntryRef`, `role`) implemented with parser/writer coverage (`getRoleBasedBswModuleEntryAssignment`/`writeRoleBasedBswModuleEntryAssignment`).

## `SupervisedEntityNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 234
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

Model aligned (Table 12.12, p.234): all 7 spec attributes implemented in PDF
display order with accessors, tests, and parser/writer coverage
(`readSupervisedEntityNeeds`/`writeSupervisedEntityNeeds` + `BswServiceDependency`
SERVICE-NEEDS dispatch branches). The earlier state was a bare placeholder
(zero attributes) whose 7 `missing` rows had been recorded but never
implemented.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `checkpointsRefs` | `List[RefType]` | `checkpoints` | `SupervisedEntityCheckpointNeedsRefConditional` | ref | modeled as plain `List[RefType]` per the codebase-wide REF-CONDITIONAL convention: the XSD `CHECKPOINTSS` wrapper → `SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF-CONDITIONAL` item (atpVariation directed-association) is unwrapped by the parser (`...-REF-CONDITIONAL/...-REF`) and re-wrapped by the writer; the CONDITION/VARIATION-POINT children are not modeled |

## `ComMgrUserNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 235
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

Model aligned (Table 12.13, p.235): the single spec attribute `maxCommMode` is
implemented in PDF display order with accessors, tests, and parser/writer
coverage (`readComMgrUserNeeds`/`writeComMgrUserNeeds` + the
`BswServiceDependency`/`SwcServiceDependency` SERVICE-NEEDS dispatch branches
and `SwcServiceDependency.createComMgrUserNeeds`). The enum attribute type
`MaxCommModeEnum` was realigned to its own spec table (SoftwareComponentTemplate
Table 13.6, p.711): member values corrected from `"full-communication"` etc. to
the spec literals `full`/`none`/`silent` and member names to `FULL`/`NONE`/
`SILENT`.

## `ChapterContent`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 330
- **Package:** `M2::MSR::Documentation::Chapters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Chapters.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `topicContent` | `Optional[TopicContentOrMsrQuery]` | `topicContent` | `TopicContentOrMsrQuery` | aggr | synced via the `TopicContentOrMsrQuery` pass; `prms` member (Table 9.60) still pending its own pass |

## `TopicContentOrMsrQuery`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 342
- **Package:** `M2::MSR::Documentation::Chapters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Chapters.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `msrQueryP1` | `Optional[MsrQueryP1]` | `msrQueryP1` | `MsrQueryP1` | aggr | referenced class `MsrQueryP1` (Table 9.82) deferred to a 2nd-level placeholder; `# Spec:` line kept without the `# Spec verified:` stamp until resolved |
| `topicContent` | `Optional[TopicContent]` | `topicContent` | `TopicContent` | aggr | synced via the `TopicContent` pass |

## `TopicContent`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 478
- **Package:** `M2::MSR::Documentation::Chapters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Chapters.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `blockLevelContent` | `Optional[DocumentationBlock]` | `blockLevelContent` | `DocumentationBlock` | aggr | synced; XSD group holds DOCUMENTATION-BLOCK (unbounded) while the spec table E.81 lists mult. 1 |
| — *(missing)* | `—` | `table` | `Table` | — | missing |
| — *(missing)* | `—` | `traceableTable` | `TraceableTable` | — | missing |

## `MsrQueryChapter`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 343
- **Package:** `M2::MSR::Documentation::Chapters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Chapters.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `msrQueryProps` | `Optional[MsrQueryProps]` | `msrQueryProps` | `MsrQueryProps` | aggr | synced via the `MsrQueryProps` pass |
| — *(missing)* | `—` | `msrQueryResultChapter` | `MsrQueryResultChapter` | — | missing |

Base deviation: spec Base is `ARObject , DocumentViewSelectable , Paginateable`; implemented as `ARObject` (matches the sibling `MsrQueryP2`). `# Spec:` line kept without the `# Spec verified:` stamp until `msrQueryResultChapter` lands.

## `MsrQueryTopic1`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 343
- **Package:** `M2::MSR::Documentation::Chapters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Chapters.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `msrQueryProps` | `Optional[MsrQueryProps]` | `msrQueryProps` | `MsrQueryProps` | aggr | synced via the `MsrQueryProps` pass |
| — *(missing)* | `—` | `msrQueryResultTopic1` | `MsrQueryResultTopic1` | — | missing |

Base deviation: spec Base is `ARObject , DocumentViewSelectable , Paginateable`; implemented as `ARObject` (matches the sibling `MsrQueryP2`). `# Spec:` line kept without the `# Spec verified:` stamp until `msrQueryResultTopic1` lands.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `maxCommMode` | `Optional[MaxCommModeEnum]` | `maxCommMode` | `MaxCommModeEnum` | attr | — |

## `DiagnosticIoControlNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 248
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

Model aligned (Table 12.26, p.248): all R23-11 spec attributes implemented in
PDF display order with accessors, tests, and parser/writer coverage
(`readDiagnosticIoControlNeeds`/`writeDiagnosticIoControlNeeds` + the
`BswServiceDependency`/`SwcServiceDependency` SERVICE-NEEDS dispatch branches
and `SwcServiceDependency.createDiagnosticIoControlNeeds`). The base class was
corrected from `ServiceNeeds` to `DiagnosticCapabilityElement` (the most-derived
model class in the spec `Base` chain). `didNumber` is **not implemented**: it
appears only in the stale `docs/requirements/xsd/AUTOSAR_00046.xsd` (AUTOSAR
CP 4.4.0 / AP 18-10, i.e. 2018) as `DID-NUMBER`, but is absent from the R23-11
PDF tables (both BSW Table 12.26 and DiagnosticExtract Table 4.82) — it was
removed upstream between 4.4.0 and R23-11, so it is treated like an
`atp.Status="removed"` attribute rather than a PDF rendering gap.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `currentValueRef` | `Optional[RefType]` | `currentValue` | `Ref (DiagnosticValueNeeds)` | ref | — |
| `freezeCurrentStateSupported` | `Optional[Boolean]` | `freezeCurrentStateSupported` | `Boolean` | attr | — |
| `resetToDefaultSupported` | `Optional[Boolean]` | `resetToDefaultSupported` | `Boolean` | attr | — |
| `shortTermAdjustmentSupported` | `Optional[Boolean]` | `shortTermAdjustmentSupported` | `Boolean` | attr | — |
| — *(not implemented)* | `—` | `didNumber` | `PositiveInteger` | attr | removed upstream: present only in the stale 2018 XSD (`DID-NUMBER` in AUTOSAR_00046.xsd), absent from the R23-11 PDF tables; not modeled (see Rule 1.3 release-alignment caveat) |

## `DiagnosticEventNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 258
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `dtcKind` *(removed)* | `—` | — | — | — | removed upstream: present only in the stale 2018 XSD (`DTC-KIND` in AUTOSAR_00046.xsd), absent from the R23-11 PDF tables; not modeled (see Rule 1.3 release-alignment caveat) |
| — *(not modeled)* | `—` | `considerPtoStatus` | `Boolean` | attr | removed upstream: present only in the stale 2018 XSD (`CONSIDER-PTO-STATUS` in AUTOSAR_00046.xsd), absent from the R23-11 PDF tables; not modeled (see Rule 1.3 release-alignment caveat) |
| — *(not modeled)* | `—` | `obdDtcNumber` | `PositiveInteger` | attr | removed upstream: present only in the stale 2018 XSD (`OBD-DTC-NUMBER` in AUTOSAR_00046.xsd), absent from the R23-11 PDF tables; not modeled (see Rule 1.3 release-alignment caveat) |
| — *(not modeled)* | `—` | `reportBehavior` | `ReportBehaviorEnum` | attr | removed upstream: present only in the stale 2018 XSD (`REPORT-BEHAVIOR` in AUTOSAR_00046.xsd), absent from the R23-11 PDF tables; not modeled (see Rule 1.3 release-alignment caveat) |
| `udsDtcNumber` *(removed)* | `—` | — | — | — | removed upstream: present only in the stale 2018 XSD (`UDS-DTC-NUMBER` in AUTOSAR_00046.xsd), absent from the R23-11 PDF tables; not modeled (see Rule 1.3 release-alignment caveat) |

## `ErrorTracerNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 263
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations |

## `TracedFailure`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 263
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations |

## `DevelopmentError`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 263
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations |

## `RuntimeError`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 263
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations |

## `PossibleErrorReaction`
- **PDF:** *no own spec table*  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `reactionCode` | `Optional[PositiveInteger]` | `reactionCode` | `PositiveInteger` (XSD `REACTION-CODE`) | attr | no own spec table; attributes from XSD group `POSSIBLE-ERROR-REACTION` |

## `ARPackage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 300
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `arPackages` | `—` | `arPackage` | `ArPackage` | — | type (spec many vs py single) |

## `AUTOSAR`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 301
- **Package:** `M2::AUTOSARTemplates::AutosarTopLevelStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `adminData` | `AdminData` | — | missing |
| — *(missing)* | `—` | `fileInfoComment` | `FileInfoComment` | — | missing |
| — *(missing)* | `—` | `introduction` | `DocumentationBlock` | — | missing |

## `ApplicationRuleBasedValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 302
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations — Table D.6 attributes (`category` via `getCategory`/`setCategory`, `swAxisCont` `*` via plural `swAxisConts`/`addSwAxisCont`/`getSwAxisConts`, `swValueCont` 0..1 via guarded `getSwValueCont`/`setSwValueCont`) all implemented per Rule 1.4. |

## `ArgumentDataPrototype`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 303
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `typeBlueprint` | `AutosarDataTypeRefConditional` | — | missing |

## `AttributeValueVariationPoint`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 210 (Table 7.2)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/__init__.py`

**Note:** Synced 2026-09-24 against R23-11 FO GST Table 7.2 (p.210; reproductions CP SWCT Table 7.65 p.617 and FO STDT Table 4.3 carry byte-identical attribute rows; only the CP SWCT render carries the Package/Note/Base meta-rows — the FO GST markdown render omits them). Deviations found and fixed during the sync — no open rows remain: class docstring reduced to the Table 7.2 Note verbatim (the Package/Base/Stereotypes header block was removed), and the `Tags: xml.attribute=true` suffix was wiped from all getter/setter docstrings (stamped form: Note text only, setters carry the None-no-op sentence). The pre-existing 5-column checklist + `# Spec verified: R23-11` stamp were rebuilt/withheld — the stamp is deferred to batch confirmation. All four Table 7.2 attributes were already implemented (`bindingTime` `Optional[BindingTimeEnum]`, `blueprintValue`/`sd` `Optional[String]`, `shortLabel` `Optional[PrimitiveIdentifier]`, all 0..1 attr, xml.attribute=true) plus the `<<atpMixedString>>` content as `_text`/`getText`/`setText`. Reader/writer via the `VALUE-ACCESS` dispatch (`VALUE_ACCESS_TAG_TO_CLASS`/`VALUE_ACCESS_CLASS_TO_TAG`, all 8 concrete wire tags) and the shared `readAttributeValueVariationPoint`/`writeAttributeValueVariationPoint` helpers (parser sets via mutators, writer reads via getters). `Base: ARObject, FormulaExpression, SwSystemconstDependentFormula` — the two mixin bases are unmodeled: XSD 00052 confirms the `FORMULA-EXPRESSION` group is an empty sequence and the `SW-SYSTEMCONST-DEPENDENT-FORMULA` group's `SYSC-STRING-REF` member belongs to SwSystemconstDependentFormula's own table (no flattening per Rule 1.3); most-derived modeled base is `ARObject` (XSD subclass composition confirms the AR-OBJECT attributeGroup). The `AbstractEnumerationValueVariationPoint` abstract subclass is likewise unmodeled (extended-meta-model derivation; the 7 concrete subclasses of the table's Subclasses row exist in the same file and in the dispatch maps). **Update 2026-09-26:** `AbstractEnumerationValueVariationPoint` is NOW modeled (`AttributeValueVariationPoints/__init__.py`, synced against R23-11 FO GST Table E.2 p.421 — see its own section below); the "unmodeled" wording above is superseded by that sync.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All four Table 7.2 attributes implemented: `bindingTime` (`Optional[BindingTimeEnum]`, 0..1, attr, xml.attribute=true), `blueprintValue` (`Optional[String]`, 0..1, attr, xml.attribute=true), `sd` (`Optional[String]`, 0..1, attr, xml.attribute=true), `shortLabel` (`Optional[PrimitiveIdentifier]`, 0..1, attr, xml.attribute=true); abstract class per the table header; docstrings verbatim from the table Notes; reader/writer via the VALUE-ACCESS dispatch helpers. Stamp deferred to batch confirmation. |

## `AbstractEnumerationValueVariationPoint`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 421 (Table E.2)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/__init__.py`

**Note:** Synced 2026-09-26 against R23-11 FO GST Table E.2 (p.421, page located via direct pypdf scan — the caption index does not cover letter-table ids; the R4.3.1 GST Table E.1 reproduction is row-identical; CP SWCT — the queue row's original TBC hint — has no own class table, only Subclasses mentions). New class: the 2026-09-24 AVP audit recorded it as unmodeled — superseded by this sync. No open deviations: exactly the two Table E.2 attribute rows implemented (`base` `Optional[Identifier]`, `enumTableRef` `Optional[Ref]` — spec member `enumTable`, Rule 0001.5 ref suffix applied; XSD REF--SIMPLE L96364 is a plain string pattern so the XML attribute carries the value only, no DEST), both 0..1 attr, xml.attribute=true; abstract class per the table header; class docstring = the Table E.2 Note verbatim plus the stamped-sibling `Package`/`Base`/`Stereotypes: atpMixedString` meta block; 6-column checklist written at creation. `Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula` anchored on its most-derived member `AttributeValueVariationPoint` (the stamped-sibling form; the XSD 00052 complexTypes composing the AEVP group — e.g. DIAGNOSTIC-DEBOUNCE-BEHAVIOR-ENUM-VALUE-VARIATION-POINT L34752 — compose AR-OBJECT + FORMULA-EXPRESSION + SSCDF + AVP + AEVP groups and attributeGroups). Reader/writer via the new own-group helper pair `readAbstractEnumerationValueVariationPoint`/`writeAbstractEnumerationValueVariationPoint` (the BASE/ENUM-TABLE XML attributes; the XSD element group L274 is an empty sequence); no `VALUE_ACCESS_TAG_TO_CLASS`/`VALUE_ACCESS_CLASS_TO_TAG` dispatch entry — the auto-generated `{Type}ValueVariationPoint` concrete subclasses (TPS_GST_00206/00373; their 5 XSD complexTypes — L34753 DiagnosticDebounceBehaviorEnumValueVariationPoint, L38282 DiagnosticIndicatorTypeEnumValueVariationPoint, L46038 DiagnosticTestResultUpdateEnumValueVariationPoint, L46955 DiagnosticUdsSeverityEnumValueVariationPoint, L47351 DiagnosticWwhObdDtcClassEnumValueVariationPoint — live in DiagnosticExtract/SystemTemplate domains; count corrected 2026-09-27 from the 4 recorded by the 2026-09-26 sync) are not modeled in src, so no wire tag can map to the abstract class; the helpers are exercised by direct element-level round-trip tests (the `TestRead/WriteSwSystemconstDependentFormula` own-group-helper precedent) and are ready for the future concrete-subclass syncs. Stamped `# Spec verified: R23-11 (2026-09-27, user 9b confirmation)` — commit 0518a7bca. **Update 2026-09-27:** three fixes, user-confirmed 2026-09-27 and stamped in commit 0518a7bca — (1) `enumTable` renamed to `enumTableRef` in source (Rule 0001.5 ref-kind suffix), (2) the class docstring gained the `Package`/`Base`/`Stereotypes: atpMixedString` meta block (user decision; the Note-only form above was superseded), (3) the field type changed `RefType` → `Ref` after the missing AUTOSAR primitive `Primitive Ref` (SWCT Table 5.35 p.318) was implemented in `PrimitiveTypes.py` (Group3 queue row) and `RefType` was confirmed a mismatched legacy class.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Both Table E.2 attributes implemented: `base` (`Optional[Identifier]`, 0..1, attr, xml.attribute=true), `enumTableRef` (`Optional[Ref]`, spec member `enumTable`, 0..1, attr, xml.attribute=true); abstract class per the table header; docstrings verbatim from the table Notes; reader/writer via the own-group attribute helpers. Stamped `# Spec verified: R23-11 (2026-09-27, user 9b confirmation)` — commit 0518a7bca. |

## `ConditionByFormula`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 231 (Table 7.5)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

**Note:** Synced 2026-09-24 against R23-11 FO GST Table 7.5 (p.231; reproductions CP SWCT Table 7.62 p.613 and CP SystemTemplate Table F.35 carry byte-identical rows; the FO FeatureModelExchangeFormat appendix "Table C.4: ConditionByFormula" caption is a PDF-extraction mislabel — its content is the FormulaExpression class table). Deviations found and fixed during the sync — no open rows remain: the `<<atpMixedString>>` mixed content (XSD 00052 element group CONDITION-BY-FORMULA L21862 is an empty sequence, complexType L21886 `mixed="true"`) was previously unmodeled — added `_text`/`getText`/`setText` per the stamped AttributeValueVariationPoint convention, and wired the reader (`readConditionByFormula` now reads `element.text` → `setText`) and writer (`writeConditionByFormula` now emits `getText()` → `element.text`) for it, mirroring the AVP helpers; the class docstring was reduced to the Table 7.5 Note verbatim and the line-wrapped getter/setter docstrings rewritten to the verbatim single-line Note form (setters carry the None-no-op sentence). The pre-existing 5-column checklist + `# Spec verified: R23-11` stamp were rebuilt 6-column/withheld — the stamp is deferred to batch confirmation. The single Table 7.5 attribute was already implemented and spec-correct (`bindingTime` `Optional[BindingTimeEnum]`, 1, attr, xml.attribute=true; enum synced with BindingTimeEnum). `Base: ARObject, FormulaExpression, SwSystemconstDependentFormula` — the two mixin bases are unmodeled (same finding as AttributeValueVariationPoint: XSD confirms the `FORMULA-EXPRESSION` group is an empty sequence and the `SW-SYSTEMCONST-DEPENDENT-FORMULA` group's `SYSC-STRING-REF`/`SYSC-REF` members belong to SwSystemconstDependentFormula's own table — no flattening per Rule 1.3); most-derived modeled base is `ARObject` (XSD complexType L21886 abstract="false" composes the AR-OBJECT group). Aggregations `VariationPoint.swSyscond` (SW-SYSCOND, sequenceOffset=30) and `VariationPointProxy.conditionAccess` (CONDITION-ACCESS) pre-exist on both the reader and writer sides.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | The single Table 7.5 attribute implemented: `bindingTime` (`Optional[BindingTimeEnum]`, 1, attr, xml.attribute=true); `<<atpMixedString>>` content as `_text`/`getText`/`setText` (repo convention, no spec row); concrete class per the table header and XSD abstract="false"; docstrings verbatim from the table Notes; reader/writer cover the attribute plus the mixed text on both SW-SYSCOND and CONDITION-ACCESS paths. Stamp deferred to batch confirmation. |

## `SwSystemconstValue`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 235 (Table 7.9)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

**Note:** Synced 2026-09-24 against R23-11 FO GST Table 7.9 (p.235; reproductions CP SystemTemplate Table F.129 and FO FMXF Table C.19 carry byte-identical attribute rows, but both renders have caption-placement extraction artifacts: F.129's caption sits under the SwSystemconstantValueSet table body with the real SwSystemconstValue rows above it, and C.19's table body renders above its caption — unlike the ConditionByFormula C.4 mislabel, both captions match their content class). Deviations found and fixed during the sync — no open rows remain: `value` was typed non-Optional `ARNumerical` on the field and accessors with missing setter return annotations — retyped `Optional[ARNumerical]` (spec Numerical, stamped Optional[X] convention); the verbose Package/Base/Attributes class docstring and the docstring-less accessors were replaced with the Table 7.9 Notes verbatim (inline comments carry Stereotypes/Tags, getters drop Tags, setters add the None-no-op sentence); the old 4-column checklist was rebuilt 6-column; and the writer emitted `ANNOTATIONS` before `SW-SYSTEMCONST-REF`/`VALUE` — reordered to the XSD 00052 element-group order (REF seqOffset=10, VALUE=20, ANNOTATIONS=30), parser read order mirrored. Attribute naming per Rule 1.5 Kind-suffix precedents: spec `annotation` (* aggr → plural) → `annotations`, spec `swSystemconst` (1, ref) → `swSystemconstRef` (as `compuMethod`→`compuMethodRef`, `variantCriterion`→`variantCriterionRef`). `Base: ARObject` (XSD complexType SW-SYSTEMCONST-VALUE L116440 abstract="false" composes only the AR-OBJECT group + attributeGroup — no mixin groups). Aggregation `SwSystemconstantValueSet.swSystemconstantValue` pre-exists on both sides. The `VALUE` element's XSD type is NUMERICAL-VALUE-VARIATION-POINT (atpMixedString) — read/written as mixed text via the shared `getChildElementOptionalNumericalValue`/`setChildElementOptionalNumericalValue` pair, the repo convention for Numerical attributes. Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | The three Table 7.9 attributes implemented spec-named: `annotation` → `annotations` (`List[Annotation]`, * aggr → plural), `swSystemconst` → `swSystemconstRef` (`RefType`, ref Kind suffix), `value` (`Optional[ARNumerical]`, 1, attr); concrete class per the table header and XSD abstract="false"; docstrings verbatim from the table Notes; reader `readSwSystemconstValue` + writer `writeSwSystemconstValue` cover all three attributes in XSD element order. Stamp deferred to batch confirmation. |

## `PostBuildVariantCondition`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 232 (Table 7.6)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

**Note:** Synced 2026-09-24 against R23-11 FO GST Table 7.6 (p.232; reproduction CP SWCT Table 7.64 carries byte-identical class-Note + attribute rows; FO FMXF "Table C.10" is caption-shifted — the PostBuildVariantCondition table body renders above its caption between C.9 PositiveInteger and C.10, row-identical to the home doc, while the rows under the C.10 caption belong to PostBuildVariantCriterion). Deviations found and fixed during the sync — no open rows remain: the class docstring carried a stale Package/Base/Stereotypes/Tags/Attributes meta block (the `Stereotypes: atpVariation` / `Tags: vh.latestBindingTime=preCompileTime` lines belong to the `value` attribute) and all docstrings were line-wrapped — wiped and rewritten to the Table 7.6 Notes verbatim single-line form (inline comments carry Stereotypes/Tags, getters drop Tags, setters add the None-no-op sentence); the pre-existing 5-column checklist + `# Spec verified: R23-11` stamp were rebuilt 6-column/withheld — the stamp is deferred to batch confirmation; and the reader `readPostBuildVariantCondition` used the mandatory `getChildElementRefType` (the only mandatory ref call in the parser — `raiseError` on absence) for `MATCHING-CRITERION-REF`, so an XSD-legal empty or value-only POST-BUILD-VARIANT-CONDITION raised ValueError in strict mode while its own writer emitted the empty form — switched to `getChildElementOptionalRefType` (XSD 00052 group POST-BUILD-VARIANT-CONDITION L93223: both children minOccurs="0"). Both Table 7.6 attributes were already implemented spec-named (`matchingCriterion` → `matchingCriterionRef` (`RefType`, Kind ref suffix per the compuMethodRef/variantCriterionRef precedents), `value` (`Optional[Integer]`, 1, attr)). `Base: ARObject` (XSD complexType POST-BUILD-VARIANT-CONDITION L93256 abstract="false" composes only the AR-OBJECT group + attributeGroup — no mixin groups). The VALUE element's XSD type is INTEGER-VALUE-VARIATION-POINT (atpMixedString, mixed="true", empty element group) — read/written as mixed text via the shared `getChildElementOptionalIntegerValue`/`setChildElementOptionalIntegerValue` pair, the repo convention for Integer attributes. Aggregations `VariationPoint.postBuildVariantCondition` and `VariationPointProxy.postBuildVariantCondition` pre-exist on both the reader and writer sides (the parser's "Unsupported POST-BUILD-VARIANT-CONDITIONS content" notImplemented branch is the defensive else for unknown tags only — this class's content is not dropped). Writer element order (MATCHING-CRITERION-REF → VALUE per the XSD group sequence) was already correct — now test-pinned. Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Both Table 7.6 attributes implemented spec-named: `matchingCriterion` → `matchingCriterionRef` (`RefType`, 1, ref Kind suffix), `value` (`Optional[Integer]`, 1, attr); concrete class per the table header and XSD abstract="false"; docstrings verbatim from the table Notes; reader `readPostBuildVariantCondition` + writer `writePostBuildVariantCondition` cover both attributes in XSD element order on the VariationPoint and VariationPointProxy paths. Stamp deferred to batch confirmation. |

## `AtomicSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 70
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 3.8 attributes (`internalBehavior`, `symbolProps`, each `0..1` aggr) are modeled as `Optional[T]` with `createXxx(short_name)` + getter (children are Referrable), with full reader/writer coverage. The previously recorded `internalBehavior` `type (spec many vs py single)` row stays removed: the PDF table states `0..1` (the XSD `*` is only the atpVariation flattening), so the single-value model is PDF-correct. |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 4-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.8, p.70 (abstract Class; Base chain most-derived `SwComponentType`). Docstrings wiped and rewritten verbatim from the markdown Notes; the instantiation guard (`type(self) is AtomicSwComponentType`) added per the abstract table header — one pre-existing test that instantiated the abstract class directly was re-pinned to a concrete subclass. VP: not an XSD anchor (the atpVariation on the internalBehavior row lands on SwcInternalBehavior, Rule 0020); mixin correctly absent. `SwcInternalBehavior` stays a `TYPE_CHECKING`-only import (a runtime bottom import cannot break the Components↔SwcInternalBehavior cycle, and no test resolves that hint at runtime — Rule 0005 exemption). Reader `readAtomicSwComponentType` (readSwComponentType + INTERNAL-BEHAVIORS/SWC-INTERNAL-BEHAVIOR dispatch + SYMBOL-PROPS) and writer `writeAtomicSwComponentType` verified against the XSD group ATOMIC-SW-COMPONENT-TYPE order (INTERNAL-BEHAVIORS before SYMBOL-PROPS) — no edit needed. Round-trip coverage in tests/test_armodel/writer/test_sw_component_type_hierarchy.py (via the dispatched ApplicationSwComponentType). No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `AtpBlueprint`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 305
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure/__init__.py` (non-leaf package — class lives in `__init__.py`; path updated 2026-09-24, was the pre-reorg `AtpBlueprint.py`)

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `blueprintPolicys` | `List[BlueprintPolicy]` | `blueprintPolicy` | `BlueprintPolicy` | aggr | spec member type upgraded to `BlueprintPolicy` (abstract, `*` aggr) — `BlueprintPolicy` is now synced per R23-11 `AUTOSAR_FO_TPS_StandardizationTemplate` Table C.18, p.164 (its attribute `attributeName` modeled; carries `# Spec verified: R23-11`). The concrete subclasses `BlueprintPolicyList`/`BlueprintPolicyNotModifiable`/`BlueprintPolicySingle`/`BlueprintPolicyModifiable` are NOT yet synced, so the `blueprintPolicy` aggregation's reader/writer stays deferred (Rule 1.10 blocker moves to the subclasses); `AtpBlueprint` keeps `# Spec verified:` withheld until then |
| — *(not modeled)* | `—` | `shortNamePattern` | `String` | — | deprecated (atp.Status=removed), not implemented — present only in the XSD `ATP-BLUEPRINT` group (`SHORT-NAME-PATTERN`), absent from the R23-11 PDF Table D.11 rendering |

Aligned to `class_check_rules.md` on 2026-08-08 (Table D.11, p.305). Base `ARObject, Identifiable, MultilanguageReferrable, Referrable` → inherits `Identifiable`. Class docstring is the verbatim Table D.11 Note. Carries `# Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.11, p.305` (provenance) but **no `# Spec verified:` stamp, and the checklist rows stay `[ ]` (reader/writer unchecked)**: `blueprintPolicy` is now typed as the spec type `BlueprintPolicy` (synced 2026-09-03, R23-11 Table C.18), but its **reader/writer stays deferred** because the concrete `BlueprintPolicy` subclasses (`BlueprintPolicyList`/`BlueprintPolicyNotModifiable`/`BlueprintPolicySingle`/`BlueprintPolicyModifiable`) are not yet synced — they own the `BLUEPRINT-POLICY-LIST`/`-NOT-MODIFIABLE`/`-SINGLE` XML elements and thus the `attributeName` coverage (Rule 1.10 blocker moved to the subclasses; see Rule 13.1 marker-omission + unchecked-row rule). `AtpBlueprint` is abstract with no concrete serialization of its own — its members serialize only through concrete blueprint subclasses, so no parser/writer wiring is expected until those land (Rule 1.7 abstract-class exception).

**Note:** Re-synced 2026-09-24 (alignment pass, batch group6-batch-9b). Citation re-verified and kept at Table D.11, p.305 (page via direct pypdf scan; pdf_page.py does not index appendix-letter ids) — D.11 is the only ALIGNED AtpBlueprint table in the R23-11 corpus; the row-identical bodies also render under the extraction-shifted captions C.12 (`AUTOSAR_FO_TPS_StandardizationTemplate`, caption p.161, actual body one caption early above it) and E.10 (`AUTOSAR_FO_TPS_GenericStructureTemplate`, caption p.424, same shift) — verified row-identical in all three (Class `AtpBlueprint (abstract)`; Base `ARObject, Identifiable, MultilanguageReferrable, Referrable`; single attribute `blueprintPolicy | BlueprintPolicy | * | aggr`; no numeric main table exists in R23-11). XSD 00052 corroboration: AtpBlueprint is group-only (`ATP-BLUEPRINT`, L6652) = abstract verified; the group's `SHORT-NAME-PATTERN` carries `atp.Status="removed"` and is absent from the PDF table, so the *not modeled* row above STANDS as an accepted deviation (Rule 0015 — PDF wins). Field-to-spec cross-check both directions EXACT (one attribute `blueprintPolicy` `*` aggr → `blueprintPolicys: List[BlueprintPolicy]` + `addBlueprintPolicy`/`getBlueprintPolicys`; no extra fields; most-derived base Identifiable). Deviations found and fixed during the sync — no new open rows: `getBlueprintPolicys` return annotation was `List[ARObject]`, fixed to the spec type `List[BlueprintPolicy]` (fixed in-band ⇒ no row per Rule 1.4/1.14); stale test docstrings (claiming `BlueprintPolicy` unimplemented / a `List[ARObject]` placeholder) corrected in `tests/test_armodel/parser/test_atp_blueprint.py`. Reader/writer deferral RE-CONFIRMED: the concrete XML-bearing subclasses (`BlueprintPolicyList`/`BlueprintPolicyNotModifiable`/`BlueprintPolicySingle`; `BlueprintPolicyModifiable` abstract per Table C.18 Subclasses row) are neither implemented nor queued in Group8/Group9 — the two `[ ]` rows and the withheld stamp stay owned by their future syncs. Both rows above remain: row 1 is informational (type upgrade complete, deferral stands), row 2 is the accepted `shortNamePattern` deviation. Stamp (`# Spec verified: R23-11`) deferred to batch confirmation.

## `AtpBlueprintable`
- **PDF:** `AUTOSAR_FO_TPS_StandardizationTemplate.pdf`  | **page:** 162
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — Base re-parented `PackageableElement` → `Identifiable` per R23-11 Table C.14, p.162 (spec Base = `ARObject, Identifiable, MultilanguageReferrable, Referrable`, Attribute column empty). `PackageableElement`/`CollectableElement` are empty abstract markers (no fields/methods); the `element` aggregation lives on `Identifiable`, so the 13 subclasses (`CompuMethod`, `DataConstr`, `SwAddrMethod`, `PortPrototype`, `ModeDeclaration`, …) retain it. Source corpus corrected R4.3.1 → R23-11: the class exists in R23-11 (StandardizationTemplate Table C.14, p.162); the Phase-0 todo cited R4.3.1 (Table 4.3, p.45) only because the `pdf_page.py` helper regex matches unprefixed table ids (`4.3`) and skips R23-11 `C.14`; R23-11 is authoritative (target release, identical content). |

## `ClientServerInterface`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 101
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

No deviations — Table 4.6 attributes (`operation`, `possibleError`) are implemented with
parser/writer coverage and tests. The previously recorded `possibleError` row was stale: the
member is implemented via the `createApplicationError` factory (named after the child type
`ApplicationError` per Rule 1.6) plus the `getPossibleErrors` getter, both wired in
`parser/arxml_parser.py` (`readPossibleErrors`) and `writer/arxml_writer.py`. Cross-checked
across all four renderings (BSW Table D.17, Diag Table 5.13, System Table F.28) — all agree
on the member set and order; SWC Table 4.6 is cited as the complete rendering (Package,
Note, Base, Aggregated-by and Attribute rows).

## `ClientServerOperation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 102
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

No deviations — Table 4.7 attributes (`argument`, `diagArgIntegrity`, `possibleError`) are
implemented with parser/writer coverage and tests. The previously recorded `diagArgIntegrity`
`missing` row is removed: the member is now implemented as a `0..1` `Boolean` attribute
(field + `getDiagArgIntegrity`/`setDiagArgIntegrity` pair) wired into
`parser/arxml_parser.py` (`readClientServerOperation`) and
`writer/arxml_writer.py` (`writeClientServerOperation`) via `DIAG-ARG-INTEGRITY`.

The previously recorded `fireAndForget`, `possibleApErrorRefs` (`possibleApError`),
and `possibleApErrorSetRefs` (`possibleApErrorSet`) `missing` rows are removed as
stale, not modeled: each is an `mmt.RestrictToStandards="AP"`, `atp.Status="draft"`
member of the old-release XSD (`docs/requirements/xsd/AUTOSAR_00046.xsd`) only, absent
from **every** CP R23-11 rendering of the class's table (SWC Table 4.7, BSW Table D.18,
DiagnosticExtract Table C.14) — they are AP-restricted draft attributes, not CP spec
attributes of `ClientServerOperation`, so no field is required and no deviation applies.

Cross-checked across the renderings (SWC Table 4.7, BSW Table D.18, DiagnosticExtract
Table C.14) — all agree on the member set and order (`argument`, `diagArgIntegrity`,
`possibleError`) and on the Package/Note/Base rows; SWC Table 4.7 is cited as the
complete rendering, matching the sibling family (`ClientServerInterface` cites SWC
Table 4.6).

## `ExecutableEntityActivationReason`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 315
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bitPosition` | `PositiveInteger` | — | missing |

## `ImplementationDataType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 268
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`

No deviations — all 5 `Attribute` rows modeled 1:1 in displayed order: `dynamicArraySizeProfile` (`Optional[String]`, 0..1 attr), `isStructWithOptionalElement` (`Optional[Boolean]`, 0..1 attr), `subElement` (`subElements: List[ImplementationDataTypeElement]` + `createImplementationDataTypeElement`/`getSubElements`, `*` aggr via the `SUB-ELEMENTS` wrapper), `symbolProps` (`Optional[SymbolProps]` + `createSymbolProps`/`getSymbolProps`, 0..1 aggr), `typeEmitter` (`Optional[NameToken]`, 0..1 attr); concrete Class, most-derived base `AbstractImplementationDataType` (Table 5.14 — already stamped R23-11, no own attributes).

**Note:** Batch sync 2026-10-04 (Group28 row; re-sync of a pre-existing class — the checklist carried a stale `# Spec verified: R23-11` stamp in the 5-column pre-release-column format with a wrong citation (BSWModuleDescriptionTemplate Table D.37, p.321 — a reproduction of the same class table); the stamp was removed at session start (Rule 0023) and stays WITHHELD pending the 9b batch confirmation, user instruction; `# Spec:` citation corrected to the defining document SWCT Table 5.15, p.268; the prior stale tracker row `symbolProps / type (spec one vs py list)` was removed — the field is the spec-shaped `Optional[SymbolProps]` single). Placement kept in `CommonStructure/ImplementationDataTypes.py` — the spec Package row is `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`; the queue's InstanceRef.py misplacement hint was stale (only `ImplementationDataTypeElementInPortInterfaceRef` lives there). Cross-checked the second rendering AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md Table 5.7, p.231 — content-identical page-split (header rows before the caption, `symbolProps`/`typeEmitter` after); defining doc SWCT wins. Writer fix: `writeImplementationDataType` reordered to the XSD group order (`SUB-ELEMENTS` before `SYMBOL-PROPS`, per `AUTOSAR_00052.xsd` group IMPLEMENTATION-DATA-TYPE); parser unchanged (find-based, all 5 mutators already called). The pre-existing `CATEGORY_*` class constants are kept as added convenience constants (not spec attributes, no checklist rows; consumed by `AutosarTopLevelStructure.getDataType`). No VARIATION-POINT anchor in the class's XSD group — not VP-capable (the `subElement` atpVariation lands on `ImplementationDataTypeElement`, already VP-capable via the mixin). No Rule 0001.10 missing referenced classes (`SymbolProps`, `NameToken`, `ImplementationDataTypeElement` all synced/stamped).

## `Integer`
- **PDF:** *no own spec table*  |  **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`

Class not in markdown/PDF — skipped per user (primitive `Integer` has no dedicated spec table in any rendered PDF; XSD-only, `xml.xsd.customType="INTEGER"`). Left as-is; not part of this sync pass.

## `NumericalOrText`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 323
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `vf` | `ARNumerical` | `vf` | `Numerical` | attr | implemented |
| `vt` | `ARLiteral` | `vt` | `String` | attr | implemented |

## `ObdInfoServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 324
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataLength` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `infoType` | `PositiveInteger` | — | missing |

## `ObdPidServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 325
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataLength` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `parameterId` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `standard` | `String` | — | missing |

## `PortPrototype`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 326
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `portPrototypeProps` | `RPortPrototypeProps` | — | missing |

## `Referrable`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 328
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

**Note:** Resolved 2026-09-24. `shortName` is the constructor `short_name` parameter with `getShortName()`; the `shortNameFragment` aggregation is implemented as `shortNameFragments: List[ShortNameFragment]` with `addShortNameFragment`/`getShortNameFragments` (SHORT-NAME-FRAGMENTS wrapper; parser `readReferrable`/`getShortNameFragments`, writer `writeReferrable`/`setShortNameFragment(s)`). The aggregated `ShortNameFragment` class (FO GenericStructureTemplate Table 4.13) is synced — see its section below. Supersedes the two "missing" rows below (stale CP BSWModuleDescriptionTemplate audit — both members exist in current code).

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `shortName` | `Identifier` | — | missing |
| — *(missing)* | `—` | `shortNameFragment` | `ShortNameFragment` | — | missing |

## `ShortNameFragment`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 64
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

No deviations.

> Resolution Note (sync 2026-09-24, section added 2026-09-25 — the sync's Step 8 claimed this section but it never landed): synced against the home document `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`, Table 4.13, p.64 (R4.3.1 Table 4.18, p.64 reproduction byte-identical). Fields/accessors match the spec exactly — `fragment` (Identifier, 1, attr) then `role` (String, 1, attr) in displayed order; no naming/type/missing deviations. Sync fixes: `role` retyped `Optional[str]` → `Optional[String]` (Rule 0001.3) and member/accessor order corrected role→fragment to the displayed fragment→role order (Rule 0001.11); reader ROLE read now uses the matched `getChildElementOptionalString`/`setChildElementOptionalString` pair and the writer the getter counterpart (fixes raw-string assignment of a `String` object). `9b` confirmed 2026-09-25 (user, one-by-one review) — `# Spec verified: R23-11` written, feat commit 519d50539. Tests: test_Identifiable.py (model), test_short_name_fragments.py (parser + writer round-trip). This section also resolves the dangling "see its section below" pointer in the `## Referrable` note above.

## `RoleBasedMcDataAssignment`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 329
- **Package:** `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `executionContextRefs` | `Ref (RptExecutionContext)` | Refs | missing |
| — *(missing)* | `—` | `mcDataInstanceRefs` | `Ref (McDataInstance)` | Refs | missing |

## `RuleArguments`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 329
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | `v` (Numerical 0..1 attr via `getV`/`setV`), `vf` (Numerical 0..1 attr via `getVf`/`setVf`), `vt` (VerbatimString 0..1 attr via `getVt`/`setVt`), `vtf` (NumericalOrText 0..1 aggr via `getVtf`/`setVtf`) all implemented per Table D.57. The old `addV`/`getVs` and `addVtf`/`getVtfs` list shapes and the missing `vf` are resolved. |

## `RuleBasedValueCont`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 330
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations — Table D.58 attributes (`ruleBasedValues` 0..1 aggr via `getRuleBasedValues`/`setRuleBasedValues`, `swArraysize` 0..1 aggr via `getSwArraysize`/`setSwArraysize`, `unit` Ref via `getUnitRef`/`setUnitRef`) all implemented per Rule 1.4; member order follows the PDF displayed row order. |

## `RuleBasedValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 331
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | `arguments` (`*` wrapper list via `addArgument`/`getArguments` — the XSD wrapper `ARGUMENTSS` carries multiple `RULE-ARGUMENTS`), `maxSizeToFill` (Integer 0..1 attr via `getMaxSizeToFill`/`setMaxSizeToFill`), `rule` (Identifier 0..1 attr via `getRule`/`setRule`) all implemented per Table D.59. Base aligned to `ARObject` per the spec `Base` column. |

## `RunnableEntity`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 525 (Table 7.3)
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | `waitPoint` resolved: `waitPoints` is now `List[WaitPoint]` via `createWaitPoint`/`getWaitPoints` (Table 7.3); the missing `WaitPoint` class (Table 7.25) is implemented (`timeout` TimeValue 0..1, `trigger` ref) with reader/writer (`WAIT-POINTS` wrapper). All 18 Table 7.3 attributes (`argument`, `asynchronousServerCallResultPoint`, `canBeInvokedConcurrently`, `dataReadAccess`, `dataReceivePointByArgument`, `dataReceivePointByValue`, `dataSendPoint`, `dataWriteAccess`, `externalTriggeringPoint`, `internalTriggeringPoint`, `modeAccessPoint`, `modeSwitchPoint`, `parameterAccess`, `readLocalVariable`, `serverCallPoint`, `symbol`, `waitPoint`, `writtenLocalVariable`) are implemented with accessors + reader/writer coverage; `DATA-RECEIVE-POINT-BY-VALUES` writer added. Member/accessor docstrings synced to the Table 7.3 Notes; `# Spec verified: R23-11` carried. |

## `ShortNameFragment`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 64 (Table 4.13)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

**Note:** Synced 2026-09-24 against R23-11 Table 4.13 (R4.3.1 Table 4.18 reproduction byte-identical, same displayed order). Deviations found and fixed during the sync — no open rows remain: `role` retyped `Optional[str]` → `Optional[String]` per the spec String type (parser now reads via `getChildElementOptionalString`, writer emits via `setChildElementOptionalString`); member/accessor order aligned to the markdown displayed order fragment → role. Reader/writer coverage via parser `getShortNameFragments` / writer `setShortNameFragment(s)` consumed by `readReferrable`/`writeReferrable` (SHORT-NAME-FRAGMENTS wrapper, xml.sequenceOffset=-90). Stamp (`# Spec verified: R23-11`) deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Both Table 4.13 attributes implemented: `fragment` (`Optional[Identifier]`, 1, attr, xml.sequenceOffset=20) and `role` (`Optional[String]`, 1, attr, xml.sequenceOffset=10); setters None-no-op + chaining; docstrings verbatim from the table Notes; reader/writer via the matched typed helpers. |

## `SwcInternalBehavior`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 518 (Table 7.2 header block)
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

Aligned to `class_check_rules.md` on 2026-08-08. PDF-synced (Rule 1):
- **Rule 1.3 (XSD-only attribute, PDF table omission — KEPT):** `handleTerminationAndRestart` is **present** in the XSD (`HANDLE-TERMINATION-AND-RESTART`, `HANDLE-TERMINATION-AND-RESTART-ENUM`, with documentation) but absent from the R23-11 PDF table renderings (Tables 7.2 / D.74 / F.132). Per the Rule 1.3 PDF-table-omission rule it is **kept** with field + accessors + parser/writer coverage. **The `[constr_1934] Existence of attribute SwcInternalBehavior.handleTerminationAndRestart` entry under the "G.16.6 Deleted Constraints in R23-11" appendix is NOT a removal signal** — it means the mandatory-*existence* requirement was deleted, not the attribute. The field is typed `Optional[ARLiteral]` because the PDF enum `HandleTerminationAndRestartEnum` (literals `canBeTerminated`/`canBeTerminatedAndRestarted`/`noSupport`) is not modeled.
- **Rule 1.7 (parser/writer pending for one aggregation):** `variationPointProxy` got its aggregated type class (`VariationPointProxy` Table 7.61) and accessors (`addVariationPointProxy`/`getVariationPointProxies`) in this pass, but the **parser/writer wrapper serialization is pending**: the nested aggregated children (`ConditionByFormula`, `PostBuildVariantCondition`) have no `readXxx`/`writeXxx` helpers yet, so serialization is sequenced after the children's alignment (Rule 1.7 "Aggregator serialization sequenced after the child's alignment"). `instantiationDataDefProps` reader/writer (Table 7.41) is now implemented (`INSTANTIATION-DATA-DEF-PROPSS` wrapper) since its children (`SwDataDefProps`, `AutosarParameterRef`, `AutosarVariableRef`) all have helpers.
- **Dual storage:** the `events`/`runnables`/`serviceDependencies` fields map to the spec `event`/`runnable`/`serviceDependency` attributes but the instances are registered via the `elements` registry (Identifiable) and retrieved by the typed getters (`getRteEvents`, `getRunnableEntities`, `getSwcServiceDependencies`); the fields are kept as empty list placeholders for backward compatibility.
- **Method declaration order:** kept the existing logical grouping (per-attribute create/get groups) rather than a strict PDF-row reorder — a deliberate scoping choice for a large legacy aggregator; `__init__` fields follow the PDF (alphabetical) displayed order.
- **Rule 13.1:** no `# Spec verified:` marker carried — **confirmed** on 2026-08-10: the class is implemented and tested but the full per-member 13.2 docstring sync (verbatim Note in every accessor + all constraint citations) is not yet completed (accessor docstrings are summarized, e.g. "Gets the ... owned by this behavior"), so no verification claim is made. The `# Spec:` line (Table 7.2, p.518) is present; the stamp flips on once every accessor docstring is verbatim.

## `SwcExclusiveAreaPolicy`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 556 (Table 7.28)
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

Aligned to `class_check_rules.md` on 2026-08-08 (Table 7.28, p.556). Implements `apiPrinciple` (`ApiPrincipleEnum`, 0..1) and `exclusiveArea` (ref → `exclusiveAreaRef: Optional[RefType]`, 0..1); Base `ARObject`. Parser (`readSwcInternalBehaviorExclusiveAreaPolicies`) and writer (`writeSwcInternalBehaviorExclusiveAreaPolicies`) added for the `EXCLUSIVE-AREA-POLICYS`/`SWC-EXCLUSIVE-AREA-POLICY` wrapper. No deviations.

## `InstantiationDataDefProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 588 (Table 7.41)
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::InstantiationDataDefProps`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstantiationDataDefProps.py`

Aligned to `class_check_rules.md` on 2026-08-08 (Table 7.41, p.588). Implements `parameterInstance`/`swDataDefProps`/`variableInstance` (all 0..1 aggr, types `AutosarParameterRef`/`SwDataDefProps`/`AutosarVariableRef`); Base `ARObject`. Parser/writer for the `INSTANTIATION-DATA-DEF-PROPSS` wrapper is pending the child serializers (see SwcInternalBehavior entry).

## `VariationPointProxy`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 613 (Table 7.61)
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/VariantHandling.py`

Aligned to `class_check_rules.md` on 2026-08-08 (Table 7.61, p.613). Base `ARObject, Identifiable, MultilanguageReferrable, Referrable` → inherits `Identifiable`. Implements `conditionAccess` (`ConditionByFormula`), `implementationDataType` (ref → `implementationDataTypeRef`), `postBuildValueAccess` (ref → `postBuildValueAccessRef`), `postBuildVariantCondition` (`*` aggr). **No `# Spec verified:` marker carried**: `valueAccess` (spec type `AttributeValueVariationPoint`, abstract) is carried as an `Optional[ARObject]` placeholder because the `AttributeValueVariationPoint` abstract base and its bases `FormulaExpression`/`SwSystemconstDependentFormula` are not yet implemented (Rule 1.10 "class not yet implemented" placeholder; forward-referenced in the inline comment). ~~Parser/writer for the `VARIATION-POINT-PROXYS` wrapper is pending the child serializers.~~ Resolved 2026-08-21: `readSwcInternalBehaviorVariationPointProxies`/`writeSwcInternalBehaviorVariationPointProxies` now serialize the `VARIATION-POINT-PROXYS` wrapper (child serializers `ConditionByFormula`/`PostBuildVariantCondition` landed with the structural `VariationPoint` plan); `VALUE-ACCESS` is skipped by the reader with `notImplemented` while the `valueAccess` deviation stands.

**Note:** Resolved 2026-09-24. The claim that `VALUE-ACCESS` is skipped by the reader is superseded: the reader (`readVariationPointProxy`) now dispatches `VALUE-ACCESS` content via `VALUE_ACCESS_TAG_TO_CLASS` (all 8 concrete `AttributeValueVariationPoint` wire tags incl. `LIMIT`) into the shared `readAttributeValueVariationPoint` helper, and the writer mirrors it via `VALUE_ACCESS_CLASS_TO_TAG`/`writeAttributeValueVariationPoint`. The `valueAccess` placeholder deviation stands resolved — `AttributeValueVariationPoint` is fully implemented and synced (see its section above); the `proxy.setValueAccess` mutator takes the concrete typed subclasses, no `Optional[ARObject]` placeholder remains.

## `SignalServiceTranslationProps`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 336
- **Package:** `M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationProps.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `controlConsumedEventGroupRefs` | `Ref (ConsumedEventGroup)` | Refs | missing |
| — *(missing)* | `—` | `controlPncRefs` | `Ref (PncMappingIdent)` | Refs | missing |
| — *(missing)* | `—` | `controlProvidedEventGroupRefs` | `Ref (EventHandler)` | Refs | missing |
| — *(missing)* | `—` | `serviceControl` | `SignalServiceTranslationControlEnum` | — | missing |
| — *(missing)* | `—` | `signalServiceTranslationEventProps` | `SignalServiceTranslationEventProps` | — | missing |

## `SwDataDefProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 332  | **table:** Table 5.39
- **Package:** `M2::MSR::DataDictionary::DataDefProperties`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py`

No deviations — all 30 Table 5.39 attributes are modeled with spec shapes and full reader/writer coverage: `additionalNativeTypeQualifier` (NativeDeclarationString), `annotation` (`*` aggr → `annotations` + `add`/`get`), `baseType`/`compuMethod`/`dataConstr`/`implementationDataType`/`swAddrMethod`/`swRecordLayout`/`unit`/`valueAxisDataType` (refs → `RefType` + Kind-suffix), `displayFormat` (DisplayFormatString), `displayPresentation` (DisplayPresentationEnum), `invalidValue` (ValueSpecification aggr), `stepSize` (Float), `swAlignment` (AlignmentType), `swBitRepresentation`/`swCalprmAxisSet`/`swDataDependency`/`swHostVariable`/`swPointerTargetProps`/`swRefreshTiming`/`swTextProps` (0..1 aggr), `swCalibrationAccess` (SwCalibrationAccessEnum), `swComparisonVariable` (`*` aggr → `swComparisonVariables`), `swImplPolicy` (SwImplPolicyEnum), `swIntendedResolution`/`swValueBlockSize`/`swValueBlockSizeMult (ordered)` (Numerical; the `*` → `swValueBlockSizeMults`), `swInterpolationMethod` (Identifier), `swIsVirtual` (Boolean). Base most-derived `ARObject`. The class-row stereotype is `<<atpVariation>>` — per Rule 0020 that is NOT a VP-aggregation indicator: the reader/writer emit/parse the `SW-DATA-DEF-PROPS-VARIANTS`/`SW-DATA-DEF-PROPS-CONDITIONAL` wrapper (no `VARIATION-POINT` element is carried; no fixture carries one). XSD-only `MC-FUNCTION` (group `SW-DATA-DEF-PROPS-CONTENT`) is absent from the PDF table and is not modeled (Rule 0015); the former `swDataDefPropsVariant missing` row was stale — the VARIANTS/CONDITIONAL split is the atpVariation serialization shape handled by the reader/writer, not an attribute.

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — pre-release-column format with stale `# Spec verified: R23-11` stamp citing the reproducing BSWModuleDescriptionTemplate rendering; the marker was removed at session start, the citation FIXED to the defining SWCT Table 5.39 p.332 — cross-checked against DEXT Table 4.11 p.49 and FO_TPS AbstractPlatformSpecification Table 3.11 p.32, SWCT wins — and the stamp stays WITHHELD pending the 9b batch confirmation, user instruction). Model Red vacuous on behavior (all 30 fields pre-existed with correct types/multiplicity/guarded setters; noted); genuine Reds: (1) Rule 0001.11 member order — fields and accessor groups sat in XSD-offset order instead of the markdown displayed order, and the three `*` lists were getter-first instead of mutator-first — reordered (source-order pin test failed before the fix); (2) Rule 0003 — `SwCalprmAxisSet`/`ValueSpecification` were TYPE_CHECKING-only, so `get_type_hints` on `setSwCalprmAxisSet`/`getInvalidValue` raised NameError on Python 3.8 — both moved to bottom-of-module runtime imports (`# noqa: E402`), and `CommonStructure/Constants/__init__.py` moved its own `ValueList` import below the `ValueSpecification` definition (Rule 0005 cycle-break). Reader/writer Red genuine: writer `setSwDataDefProps` emitted the 30 child elements in mixed order violating the XSD `sequenceOffset` (AUTOSAR_00052.xsd group `SW-DATA-DEF-PROPS-CONTENT`, L115383) — writer and parser reordered to the group order (`test_write_sw_data_def_props_element_order_follows_xsd` failed before the fix). All 4 SW-DATA-DEF-PROPS-carrying integration fixtures round-trip lossless with byte-identical re-writes. No missing referenced classes.

## `SwTextProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 250  | **table:** Table 5.7
- **Package:** `M2::MSR::DataDictionary::DataDefProperties`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py`

No deviations — all four Table 5.7 attributes are modeled with spec shapes: `arraySizeSemantics` (ArraySizeSemanticsEnum, `0..1`, attr), `baseType` (SwBaseType, `0..1`, ref → `baseTypeRef`, Kind-suffix per Rule 0001.5), `swFillCharacter` (Integer, `0..1`, attr), `swMaxTextSize` (Integer, `0..1`, attr) — each `Optional[T]` PEP 526 member + guarded `get/setXxx` pair with full reader/writer coverage. Base most-derived `ARObject` (XSD complexType `SW-TEXT-PROPS`, `AUTOSAR_00052.xsd` L116546, refs AR-OBJECT group only). `swMaxTextSize` carries the `atpVariation` stereotype but its Kind is `attr` → attribute-value variation only (XSD types the element `INTEGER-VALUE-VARIATION-POINT`; PDF type `Integer` wins per Rule 0015); XSD group `SW-TEXT-PROPS` (L116499) anchors NO `VARIATION-POINT` → not VP-capable.

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — pre-release-column format with stale `# Spec verified: R23-11` stamp citing the reproducing BSWModuleDescriptionTemplate Table D.72; the marker was removed at session start, the citation FIXED to the defining SWCT Table 5.7 p.250, and the stamp stays WITHHELD pending the 9b batch confirmation, user instruction). Table 5.7 is page-split (p.249→250): the markdown renders the Class/Package/Note/Base/Aggregated-by rows + `arraySizeSemantics`/`baseType`/`swFillCharacter` before the caption and `swMaxTextSize` after it — displayed order is the class member order; XSD element order is independent (ARRAY-SIZE-SEMANTICS, SW-MAX-TEXT-SIZE [20], BASE-TYPE-REF [30], SW-FILL-CHARACTER [40]). Model Red vacuous (impl already conformed — base, members, guarded setters, verbatim docstrings all in place; noted). The genuine fix of this pass: reader `getSwTextProps` and writer `setSwTextProps` emitted the four child elements in markdown order (SW-MAX-TEXT-SIZE last), violating the XSD sequenceOffset — both reordered to the group order (writer Red genuine: `test_write_element_order_matches_xsd_group` failed with `['ARRAY-SIZE-SEMANTICS', 'BASE-TYPE-REF', 'SW-FILL-CHARACTER', 'SW-MAX-TEXT-SIZE']` before the fix). Aggregator dispatch pre-exists both sides (parser `getSwDataDefProps` / writer `setSwDataDefProps` call sites) — unchanged. Referenced member type `ArraySizeSemanticsEnum` (Table 5.10) is stamped R23-11; no missing classes.

## `DocumentationBlock`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 287
- **Package:** `M2::MSR::Documentation::BlockElements`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/BlockElements/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Aligned to Table 9.1 (R23-11). All 11 attributes present with reader/writer. Referenced classes Note (9.27), TraceableText/StructuredReq (9.30/9.31), DefList/DefItem (9.15/9.16), LabeledList/LabeledItem/IndentSample (9.11–9.13), MultiLanguageVerbatim (9.5), MsrQueryP2/MsrQueryProps/MsrQueryArg (9.85/9.86/E.56) implemented. `figure`/`list`/`p` kept as lists for atpSplitable/atpVariation XML. TraceableText/StructuredReq/DefItem simplified to ARObject base (spec lists Identifiable/Referrable; no shortName modeled). `DefItem.def` backed by field `def_doc` (Python keyword). |

## `LLongName`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 62
- **Package:** `M2::MSR::Documentation::TextModel::LanguageDataModel`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Aligned to Table 4.8/4.9 (R23-11): `blueprintValue` (draft) + MixedContentForLongName attrs `e`/`ie`/`sub`/`sup`/`tt` present with reader/writer. Referenced classes EmphasisText/IndexEntry/Superscript/Tt implemented (Tables 9.34/9.36/9.38/9.39). Inherits LanguageSpecific (`l`, `value`). |

## `LanguageSpecific`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 350
- **Package:** `M2::MSR::Documentation::TextModel::LanguageDataModel`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Aligned to Table 9.97 (R23-11): `l` (LEnum attr) present with reader/writer; `value` carries the atpMixedString text content. Referenced `LEnum` now a spec-aligned `AREnum` (34 literals, Table 9.97). |

## `SymbolicNameProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** (Table 7.59, R23-11)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

Aligned to `class_check_rules.md` on 2026-08-07. PDF-synced (Rule 1):
- **Rule 1.2 (base class):** spec `Base` = `ARObject, ImplementationProps, Referrable`. The class now inherits `ImplementationProps` (which itself extends `Referrable, ABC`), matching the spec chain — previously it inherited only `Referrable`, missing the `ImplementationProps` link that supplies the `symbol` / `SYMBOL` (0..1 `C-Identifier`) attribute.
- **Rule 1.1 (own attributes):** spec `Table 7.59` has **no own attribute rows** (all `-`). The earlier `symbolicName: String` field (and `getSymbolicName` / `setSymbolicName`) was spurious — there is no `SYMBOLIC-NAME` XSD element — and was removed. `SymbolicNameProps` now carries only inherited members (`symbol` from `ImplementationProps`, SHORT-NAME from `Referrable`).
- **Rule 1.7 / serialization:** `SYMBOLIC-NAME-PROPS` XSD complexType = `AR-OBJECT` + `REFERRABLE` + `IMPLEMENTATION-PROPS`; the parser `readSymbolicNameProps` and writer `writeSymbolicNameProps` call `readImplementationProps` / `writeImplementationProps`, so both `SHORT-NAME` and `SYMBOL` round-trip.
- Aggregated 0..1 by `ServiceDependency.symbolicNameProps` (spec `Table 7.57`, Kind `aggr`) — verified against PDF; the aggregation is correct in the model.

## `SwcServiceDependency`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 224
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `assignedDataType` | `—` | `assignedData` | `RoleBasedDataAssignment` | — | naming |
| — *(missing)* | `—` | `assignedPort` | `Ref (PortGroup)` | — | missing |
| — *(missing)* | `—` | `representedPortGroupRef` | `Ref (PortGroup)` | Ref | missing |
| `cryptoServiceNeeds` | `—` | `serviceNeeds` | `BswMgrNeeds` | — | type (spec one vs py list) |

## `ObdControlServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 233
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `testId` | `PositiveInteger` | — | missing |

## `BaseTypeDirectDefinition`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 291  | **table:** Table 5.24
- **Package:** `M2::MSR::AsamHdo::BaseTypes`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py`

No deviations among the modeled members — all five Table 5.24 attributes (`baseTypeEncoding`, `baseTypeSize`, `byteOrder`, `memAlignment`, `nativeDeclaration`, all 0..1 attr) map 1:1 to `Optional[T]` PEP 526 fields + guarded self-returning getter/setter pairs in the markdown displayed order (page-split table: the `baseTypeEncoding` row renders before the caption, the other four after it — Rule 0001.11). Base most-derived = `BaseTypeDefinition` (Table 5.23 — abstract, zero own attrs); concrete class, aggregated by `BaseType.baseTypeDefinition` — the aggregation is flattened in XML (the XSD group BASE-TYPE, AUTOSAR_00052.xsd L8384, embeds a 0..1 choice of the BASE-TYPE-DIRECT-DEFINITION group inline, role/type/wrapper flags all false): reader `readBaseTypeDirectDefinition` (arxml_parser.py:7428) / writer `setBaseTypeDirectDefinition` (arxml_writer.py:3979), both reached from `readSwBaseType`/`writeSwBaseType`, cover all five elements in XSD sequenceOffset order (BASE-TYPE-SIZE 70, BASE-TYPE-ENCODING 90, MEM-ALIGNMENT 100, BYTE-ORDER 110, NATIVE-DECLARATION 120). Not VP-capable (no VARIATION-POINT in the XSD group, Rule 0020).

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maxBaseTypeSize` | `PositiveInteger` | — | deprecated (atp.Status=removed), not implemented |

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — no per-row release column, stale p.290 citation; stale `# Spec verified: R23-11` marker removed at session start, stamp WITHHELD pending the 9b batch confirmation, user instruction). Entry page citation corrected 290 → 291 per pdf_page.py; the `maxBaseTypeSize` accepted row retained (`atp.Status="removed"` in the XSD group AND absent from the PDF Attribute column — Rule 0001.3/0015, stays not modeled). Model Red genuine on the accessor-docstring pin (all 5 setters carried the stale two-paragraph None-no-op form → rewritten to the inline batch convention); module adopted PEP 563 + bare self-ref returns (6 quoted returns unquoted — 5 on this class + 1 on `BaseType.setBaseTypeDefinition`, same-change rule, RunnableEntityGroup precedent). Reader/writer tests extended per-attribute on both sides (parser `test_SwBaseType.py` isolated reads incl. the UPPERCASE XSD BYTE-ORDER form read verbatim; writer `test_writer_SwBaseType.py` isolated emissions incl. the camelCase member-value form) — parser/writer source unchanged (coverage pre-existed in XSD order, vacuous reader/writer Red noted). Referenced types: base `BaseTypeDefinition` (Table 5.23, synced this batch), `BaseTypeEncodingString` (Table 5.25), `ByteOrderEnum` (Table 5.27, queued for its own Group28 pass) — all exist and are behaviorally complete; no missing classes. (Update, same day — ByteOrderEnum pass: the BYTE-ORDER test forms described above were superseded by the canonical XSD-token round-trip — reader maps `MOST-SIGNIFICANT-*` to the camelCase member via `BYTE_ORDER_XML_MAP`, writer emits the XSD token; see the `## ByteOrderEnum` entry.)

## `BuildActionIoElement`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 369 (Table 10.3)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::BuildActionManifest`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/BuildActionManifest.py`

**Note:** Synced 2026-09-24 against R23-11 Table 10.3 (R4.3.1 Table 9.3, p.338, is the byte-equivalent pre-split table; Base `ARObject` confirmed against the XSD complexType `BUILD-ACTION-IO-ELEMENT`, which references only the `AR-OBJECT` group). Reader type gap fixed during the sync — the parser read CATEGORY via `getChildElementOptionalLiteral` (plain `ARLiteral`) while the spec type is `NameToken`; a matched `getChildElementOptionalNameToken`/`setChildElementOptionalNameToken` leaf pair was added and CATEGORY now round-trips as `NameToken` (same reader-type-gap fix as the CseCodeType/DateTime precedents). Reader/writer XML element order already matches the XSD group sequence CATEGORY → SDGS → ECUC-DEFINITION-REF → ENGINEERING-OBJECT → FOREIGN-MODEL-REFERENCE → ROLE (sequenceOffset -100/-90/—/—/—/30); the XSD's `MODEL-OBJECT-REFERENCE` row (GenericModelReference) carries `atp.Status="removed"` and is absent from the R23-11 table, so it stays unmodeled (Rule 0015). Stamp (`# Spec verified: R23-11`) deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `foreignModelReference` | `ForeignModelReference` | aggr | missing (member class has no Class table in the R23-11 or R4.3.1 corpus — XSD-only, `AUTOSAR_00052.xsd` FOREIGN-MODEL-REFERENCE complexType — and is outside the confirmed sync closure, Rule 0001.10; queued for its own XSD-derived sync, reader/writer coverage deferred with it) |

## `CompositionSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 307
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|---|
| `physicalDimensionMappingRef` | `RefType` | `physicalDimensionMappingRef` | `Ref (PhysicalDimensionMappingSet)` | Ref | model implemented; reader/writer not (element absent from AUTOSAR XSD) |

## `EcuInstance`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 50
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `canTpAddressRefs` | `Ref (CanTpAddress)` | Refs | deprecated (atp.Status=removed), not implemented |
| — *(missing)* | `—` | `diagnosticProps` | `DiagnosticEcuProps` | — | deprecated (atp.Status=removed), not implemented |
| — *(missing)* | `—` | `tpAddressRefs` | `Ref (TpAddress)` | Refs | deprecated (atp.Status=removed), not implemented |

No `# Spec verified:` stamp this pass: `firewallRule` → `firewallRuleRefs` (list ref) and `ecuTaskProxy` → `addEcuTaskProxyRef` (list-add shape) were converted to the Table 3.1 `*` ref shape; the XSD-only `diagnosticAddress` was removed per Rule 0015. Reader/writer coverage is pending for the aggregate attributes whose referenced classes are missing (Rule 0001.10 placeholders): `clientIdRange` → `ClientIdRange`, `dltConfig` → `DltConfig`, `doIpConfig` → `DoIpConfig`, `partition` → `EcuPartition`. All 13 spec scalar/ref attributes and the four list-ref groups now round-trip.

## `ISignal`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 320
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `iSignalProps` | `ISignalProps` | — | missing (referenced class `ISignalProps` not implemented; Rule 0001.10 placeholder) |

The previous `dataTransformation` "type (spec many vs py single)" row was stale — the "many" came from the XSD wrapper (`pureMM.maxOccurs="-1"`); the PDF Table 6.7 multiplicity is `0..1`, so the single `dataTransformationRef` is PDF-correct. The `transformationISignalProps`/`iSignalProps` "type (spec one vs py list)" row was generator noise: both shapes are correct (`iSignalProps` is `0..1` single, `transformationISignalProps` is `*` list). Reader/writer for `DATA-TRANSFORMATIONS`, `TIMEOUT-SUBSTITUTION-VALUE`, and the `TRANSFORMATION-I-SIGNAL-PROPSS` wrapper were added. No `# Spec verified:` stamp while `ISignalProps` remains missing.

## `J1939NmNode`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 322
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `addressConfigurationCapability` | `J1939NmAddressConfigurationCapabilityEnum` | — | missing |
| — *(missing)* | `—` | `nodeName` | `J1939NodeName` | — | missing |

## `ModeInBswModuleDescriptionInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 323
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/InstanceRefs/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `baseRef` | `Optional[RefType]` | `base` | `Ref (BswModuleDescription)` | Ref | atpDerived, not serialized (no parser/writer) |
| `contextModeDeclarationGroupRef` | `Optional[RefType]` | `contextModeDeclarationGroup` | `Ref (ModeDeclarationGroupPrototype)` | Ref | ok |
| `targetModeRef` | `Optional[RefType]` | `targetMode` | `Ref (ModeDeclaration)` | Ref | ok |

## `ObdMonitorServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 324
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `applicationDataTypeRef` | `Ref (ApplicationDataType)` | Ref | missing |
| — *(missing)* | `—` | `eventNeedsRef` | `Ref (DiagnosticEventNeeds)` | Ref | missing |
| — *(missing)* | `—` | `onBoardMonitorId` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `testId` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `unitAndScalingId` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `updateKind` | `DiagnosticMonitorUpdateKindEnum` | — | missing |

## `PortInterface`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 326
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `namespace` | `SymbolProps` | — | missing |

## `SwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 65
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all six Table 3.1 attributes (consistencyNeeds, port, portGroup, swcMappingConstraint, swComponentDocumentation, unitGroup) are modeled with full reader/writer coverage; the earlier placeholder rows (ConsistencyNeeds/UnitGroup/MappingConstraints) are removed — ConsistencyNeeds and UnitGroup are implemented, and swcMappingConstraint/unitGroup are ref-kind (RefType DEST), needing no aggregate class. |

**Note:** Batch sync 2026-10-05 (Group27; legacy checklist without the release column and a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.1, p.65 (abstract Class; page-split render — the consistencyNeeds chunk precedes the caption, port..unitGroup follow it; displayed order kept). Base fixed from `AtpType` to `ARElement` per the spec Base chain (most-derived; Package/Note/Base rows verified against FO_TPS_AbstractPlatformSpecification Table 3.5, p.22 — row-identical, nothing merged). Docstrings wiped and rewritten verbatim from the markdown Notes (Stereotypes/Tags tails dropped); `SwComponentDocumentation` moved from `TYPE_CHECKING`-only to a bottom-of-module runtime import so `get_type_hints` pins resolve (Rule 0003/0005). `getPPortPrototypes`/`getRPortPrototypes`/`getPRPortPrototypes`/`getPortPrototypes` kept as added convenience getters (no spec rows). VP: none of the four hierarchy classes is an XSD VARIATION-POINT anchor — the atpVariation stereotypes on the aggr rows land on the member classes (PortPrototype etc., Rule 0020); the mixin is correctly absent. Reader/writer verified against the XSD group SW-COMPONENT-TYPE element order (SW-COMPONENT-DOCUMENTATIONS sequenceOffset=-10 first) — no edit needed. No Rule 0001.10 missing classes (`SwComponentMappingConstraints` is ref-DEST only). `# Spec verified:` withheld (batch 9b).

Stale row removed 2026-10-04: the `consistencyNeeds` "class not yet implemented — ARObject placeholder" row is obsolete — `ConsistencyNeeds` is synced (Group28, Table 4.99) with its own entry below; the model field was already `List[ConsistencyNeeds]`, and reader/writer coverage pre-exists (parser `readSwComponentTypeConsistencyNeeds` + ARPackage dispatch, writer mirror).

## `SwComponentDocumentation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 698
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SoftwareComponentDocumentation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SoftwareComponentDocumentation.py`

Model aligned (Table 12.1, p.698): `chapter` (*, aggr) and the seven predefined
0..1 chapters (`swCalibrationNotes`, `swCarbDoc`, `swDiagnosticsNotes`,
`swFeatureDef`, `swFeatureDesc`, `swMaintenanceNotes`, `swTestDesc`) implemented
as `List[Chapter]` / `Optional[Chapter]` with `createXXX`/`getXXX` accessors,
tests, and reader/writer coverage. The aggregated Chapter family lives in
`M2::MSR::Documentation::Chapters`. `# Spec verified: R23-11` stamped.

## `EcucDefinitionCollection`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 25
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `moduleRefs` | `Ref (EcucModuleDef)` | Refs | missing |

## `EcucContainerDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 36
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `destinationUriRef` | `—` | `destinationUriRefs` | `Ref (EcucDestinationUriDef)` | Refs | type (spec many vs py single) |
| — *(missing)* | `—` | `postBuildChangeable` | `Boolean` | — | missing |

## `EcucCommonAttributes`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 48
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `configurationClassAffection` | `EcucConfigurationClassAffection` | — | missing |
| — *(missing)* | `—` | `implementationConfigClass` | `EcucImplementationConfigurationClass` | — | missing |

## `EcucMultilineStringParamDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 64
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucMultilineStringParamDefVariant` | `EcucMultilineStringParamDefConditional` | — | missing |

## `EcucStringParamDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 64
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucStringParamDefVariant` | `EcucStringParamDefConditional` | — | missing |

## `EcucFunctionNameDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 65
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucFunctionNameDefVariant` | `EcucFunctionNameDefConditional` | — | missing |

## `EcucLinkerSymbolDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf` (R23-11)  | **page:** 65 (Table 2.21; caption md l.1705)
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(removed)* | `—` | `ecucLinkerSymbolDefVariant` | `EcucLinkerSymbolDefConditional` | — | resolved to removed 2026-09-30 (Rule 0015) — stale pre-sync `missing` row: Table 2.21's attribute column is EMPTY (corpus l.1699 "The class EcucLinkerSymbolDef does not introduce any additional attributes"); the variant conditional is the XSD-only atpVariation split artifact (ECUC-LINKER-SYMBOL-DEF-VARIANTS/ECUC-LINKER-SYMBOL-DEF-CONDITIONAL wrapper, AUTOSAR_00052.xsd l.52608), not a spec attribute. |
| — *(no deviation)* | — | — | — | — | No deviations — Table 2.21 has zero attribute rows; the class declares no own fields and inherits its accessors from the stamped base EcucAbstractStringParamDef (Table 2.18, R23-11) — Rule 0002 empty-attribute case, no fabrication/flattening. The pre-sync state had NO reader/writer coverage (ECUC-LINKER-SYMBOL-DEF elements were silently dropped on round-trip): readEcucLinkerSymbolDef/writeEcucLinkerSymbolDef helpers (VARIANTS/CONDITIONAL wrapper pattern of the stamped sibling EcucMultilineStringParamDef), both aggregation dispatch branches (EcucParamConfContainerDef via the new createEcucLinkerSymbolDef factory; EcucDestinationUriPolicy via direct construction + addParameter) and the round-trip tests were added in this pass (Rule 0001.7 five-place pattern completed), not deviation rows. |

**Note:** Batch sync 2026-09-30 (Group19 row 10; the class pre-existed unstamped). Table 2.21 is complete in the markdown (caption l.1705, body l.1707-1714); PDF p.65 caption hit via pdf_page.py. XSD group ECUC-LINKER-SYMBOL-DEF (AUTOSAR_00052.xsd l.52608, complexType l.52630) = base groups (… + ECUC-ABSTRACT-STRING-PARAM-DEF) + the VARIANTS/CONDITIONAL wrapper only (sequenceOffset=10000 LAST); the CONDITIONAL content group carries the ECUC-ABSTRACT-STRING-PARAM-DEF content (DEFAULT-VALUE/MAX-LENGTH/MIN-LENGTH/REGULAR-EXPRESSION), populated via the inherited base accessors. Class docstring = Table 2.21 Note verbatim + class requirement [TPS_ECUC_02031] (md l.1697, `\_` unescaped, glyph markers stripped — batch convention). The class-row `<<atpVariation>>` split wrapper is handled transparently in reader/writer per Rule 0001.7 (EcucMultilineStringParamDef precedent); not a Rule 0020 mixin case. No Rule 0001.10 missing referenced types. No integration fixture carries ECUC-LINKER-SYMBOL-DEF (no Rule 0019 combine case).

## `EcucChoiceReferenceDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 74
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `destinationRef` | `—` | `destinationRefs` | `Ref (EcucContainerDef)` | Refs | type (spec many vs py single) |

## `EcucInstanceReferenceDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 77
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `destinationContext` | `String` | — | missing |

## `EcucDestinationUriDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 82
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `destinationUriPolicy` | `EcucDestinationUriPolicy` | — | missing |

## `EcucDestinationUriPolicy`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 83
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `container` | `EcucChoiceContainerDef` | — | missing |
| — *(missing)* | `—` | `destinationUriNestingContract` | `EcucDestinationUriNestingContractEnum` | — | missing |
| — *(missing)* | `—` | `parameter` | `EcucAddInfoParamDef` | — | missing |
| — *(missing)* | `—` | `reference` | `EcucChoiceReferenceDef` | — | missing |

## `EcucDerivationSpecification`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 87
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `calculationFormula` | `EcucParameterDerivationFormula` | — | missing |
| — *(missing)* | `—` | `ecucQuery` | `EcucQuery` | — | missing |
| — *(missing)* | `—` | `informalFormula` | `MlFormula` | — | missing |

## `EcucParameterDerivationFormula`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 88
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucQueryRef` | `Ref (EcucQuery)` | Ref | missing |
| — *(missing)* | `—` | `ecucQueryStringRef` | `Ref (EcucQuery)` | Ref | missing |

## `EcucQuery`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 89
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucQueryExpression` | `EcucQueryExpression` | — | missing |

## `EcucQueryExpression`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 89
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `configElementDefGlobalRef` | `Ref (EcucDefinitionElement)` | Ref | missing |
| — *(missing)* | `—` | `configElementDefLocalRef` | `Ref (EcucDefinitionElement)` | Ref | missing |

## `EcucConditionFormula`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 100
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucQueryRef` | `Ref (EcucQuery)` | Ref | missing |
| — *(missing)* | `—` | `ecucQueryStringRef` | `Ref (EcucQuery)` | Ref | missing |

## `EcucConditionSpecification`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 100
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucQuery` | `EcucQuery` | — | missing |
| — *(missing)* | `—` | `informalFormula` | `MlFormula` | — | missing |

## `EcucValidationCondition`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 103
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucQuery` | `EcucQuery` | — | missing |
| — *(missing)* | `—` | `validationFormula` | `EcucConditionFormula` | — | missing |

## `EcucIndexableValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 110
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `index` | `PositiveInteger` | — | missing |

## `Documentation`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 294
- **Package:** `M2::AUTOSARTemplates::GenericStructure::DocumentationOnM1`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/DocumentationOnM1/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `context` | `DocumentationContext` | — | missing |
| — *(missing)* | `—` | `documentationContent` | `PredefinedChapter` | — | missing |

## `Identifier`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 299
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blueprintValue` | `?` | — | missing |
| — *(missing)* | `—` | `namePattern` | `?` | — | missing |

## `MlFormula`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 301
- **Package:** `M2::MSR::Documentation::BlockElements::Formula`
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/Formula/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `formulaCaption` | `Caption` | — | missing |
| — *(missing)* | `—` | `genericMath` | `MultiLanguagePlainText` | — | missing |
| — *(missing)* | `—` | `texMath` | `MultiLanguagePlainText` | — | missing |
| — *(missing)* | `—` | `verbatim` | `MultiLanguageVerbatim` | — | missing |

## `Pdu`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 303
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `metaDataLength` | `PositiveInteger` | — | missing |

## `PostBuildVariantCriterion`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 614 (Table 7.63)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

**Note:** Synced 2026-09-24 against R23-11 CP SWCT Table 7.63 (p.614; reproductions FO GST Table 7.7 p.232 and CP ECUConfiguration Table F.30 carry row-identical content; FO FMXF "Table C.11" is caption-shifted — the PostBuildVariantCriterion table body renders ABOVE its caption split by inline images, row-identical to the primary, and nothing sits under the C.11 caption). The stale "compuMethodRef missing" row below was outdated even when written — the member has been implemented with full reader/writer coverage since intake (`compuMethodRef: RefType`, Kind ref suffix). Deviations found and fixed during the sync — no open rows remain: the class docstring carried a stale Package/Base/Tags/Attributes meta block (unlike PostBuildVariantCondition, this table's `Tags: atp.recommendedPackage=PostBuildVariantCriterions` line IS part of the class Note and stays) and the accessor docstrings were line-wrapped — wiped and rewritten to the Table 7.63 Notes verbatim single-line form (getter drops nothing, setter adds the None-no-op sentence); the pre-existing 5-column checklist + `# Spec verified: R23-11` stamp were rebuilt 6-column/withheld — the stamp is deferred to batch confirmation. `Base: ARElement` (most-derived; XSD 00052 complexType POST-BUILD-VARIANT-CRITERION L93296 abstract="false" composes the full base-group chain + own group — no flattening; aggregated by ARPackage.element, dispatch + factory pre-exist on both reader and writer sides). The own XSD group (L93273) has the single element COMPU-METHOD-REF (minOccurs="0", DEST COMPU-METHOD--SUBTYPES-ENUM) — reader lenient via `getChildElementOptionalRefType`, writer emits it only when set, order after all base groups per the XSD sequence (test-pinned). No SemanticallyNeutral-style subtypes (SUBTYPES-ENUM L93316 lists only POST-BUILD-VARIANT-CRITERION). Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | The single Table 7.63 attribute implemented spec-named: `compuMethod` → `compuMethodRef` (`RefType`, 1, ref Kind suffix); concrete class per the table header and XSD abstract="false"; docstrings verbatim from the table Notes; reader `readPostBuildVariantCriterion` + writer `writePostBuildVariantCriterion` cover the attribute (ARPackage.element dispatch on both sides). Stamp deferred to batch confirmation. |

## `PostBuildVariantCriterionValue`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 259 (Table 7.27)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

**Note:** Synced 2026-09-24 against R23-11 FO GST Table 7.27 (p.259; reproductions FMXF Table C.12 — the one family table whose body sits complete UNDER its caption — and CP ECUConfiguration Table F.31 carry row-identical content; F.31 is caption-shifted like the rest of the family: the real F.31 body renders ABOVE its caption and the body below it is PredefinedVariant's). The two "missing" rows below were outdated even when written — `annotation` (Annotation, * aggr → `annotations: List[Annotation]` + get/add pair) and `variantCriterion` (→ `variantCriterionRef: RefType`, Kind ref suffix) have been implemented since intake. Deviations found and fixed during the sync — no open rows remain: the class docstring was a stale paraphrase with typos ("specifies a the value", "must must match") plus a Package/Base/Attributes meta block and all three setter docstrings were line-wrapped — wiped and rewritten to the Table 7.27 Notes verbatim single-line form (getters drop the Tags suffix, setters/adder append the None-no-op sentence); the pre-existing 5-column checklist with unchecked reader/writer columns was rebuilt 6-column with release R23-11. `Base: ARObject` (most-derived; XSD 00052 complexType POST-BUILD-VARIANT-CRITERION-VALUE L93362 composes group AR:AR-OBJECT (empty sequence) + own group — no flattening; NOT an ARElement, aggregation is via PostBuildVariantCriterionValueSet.postBuildVariantCriterionValue). The own XSD group (L93322) orders VARIANT-CRITERION-REF (DEST POST-BUILD-VARIANT-CRITERION required) → VALUE (type INTEGER-VALUE-VARIATION-POINT mixed wrapper — the reader/writer use the same getChildElementOptionalIntegerValue/setChildElementOptionalIntegerValue helpers the PostBuildVariantCondition sibling uses for its identically-typed VALUE) → ANNOTATIONS wrapper. Consume-path disposition: the aggregating PostBuildVariantCriterionValueSet class does NOT exist in armodel (no model class, no ARPackage dispatch for POST-BUILD-VARIANT-CRITERION-VALUE-SET, not queued in Group8/9), so no document-level dispatch reaches this element; standalone helpers `readPostBuildVariantCriterionValue`/`writePostBuildVariantCriterionValue` were added beside the Condition sibling pair and are test-pinned directly (parser read tests incl. the empty + VALUE-only forms, writer element-order + bare-element tests, element-level write→re-read round-trip). Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All three Table 7.27 attributes implemented spec-named: `annotation` (Annotation, *, aggr → `annotations` typed list + getAnnotations/addAnnotation), `value` (Integer, 1, attr → Optional[Integer] + getValue/setValue), `variantCriterion` (PostBuildVariantCriterion, 1, ref → `variantCriterionRef` RefType Kind-ref suffix); Base ARObject concrete class per the table header; docstrings verbatim from the table Notes; reader `readPostBuildVariantCriterionValue` + writer `writePostBuildVariantCriterionValue` cover all three attributes via their own helper pair (no dispatcher exists until the PostBuildVariantCriterionValueSet aggregator is classed). Stamp deferred to batch confirmation. |

## `VariationPoint`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  |  **page:** 226 (Table 7.4)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

**Note:** Re-synced 2026-09-24 (alignment pass, batch group6-batch-9b). Citation re-verified and moved to the NUMERIC MAIN TABLE — R23-11 FO GST Table 7.4, p.226 (page via pdf_page.py; the tracker's old `AUTOSAR_CP_TPS_ECUConfiguration.pdf p.315` citation pointed at appendix Table F.47, which is caption-shifted: the VariationPoint body renders ABOVE the F.46 ValueList caption and only the trailing `swSyscond` row sits under the F.47 caption). Reproductions verified row-identical: FO StandardizationTemplate Table 4.2 (p.39), CP SWCT Table E.51, CP SystemTemplate Table F.145, CP ECUConfiguration Table F.47 (caption-shifted), FMXF Table C.20 (caption-shifted). XSD 00052 corroboration: complexType `VARIATION-POINT` (L130082, abstract="false") composes group AR:AR-OBJECT + own group `VARIATION-POINT` (L130012) — Base row `ARObject` confirmed, most-derived base ARObject; element order SHORT-LABEL (offset 10) → DESC (20) → BLUEPRINT-CONDITION (28) → FORMAL-BLUEPRINT-CONDITION (29, **atp.Status="removed"** — no R23-11 PDF row, deliberately not modeled per the PDF-wins rule) → FORMAL-BLUEPRINT-GENERATOR (30, atp.Status=draft — modeled, the PDF table carries the row) → SW-SYSCOND (30) → POST-BUILD-VARIANT-CONDITIONS (40, wrapper + unbounded choice) → SDG (50). Field-to-spec cross-check both directions EXACT (seven table rows ↔ seven fields/accessor pairs in displayed row order; `postBuildVariantCondition` `*` aggr → dedicated typed list `postBuildVariantConditions`; no fabricated/extra fields). Reader/writer FULLY covered both sides since intake: `readVariationPoint`/`writeVariationPoint` read/set and get/write all seven attributes in XSD order (reader includes a defensive `notImplemented` branch for unknown POST-BUILD-VARIANT-CONDITIONS content; the writer omits the wrapper when the list is empty). The `missing` row below was STALE (pre-dated the implementation) and is superseded by the no-deviation row. Docstrings wiped and rewritten verbatim from the Table 7.4 Notes (mid-identifier PDF-extraction spaces "postBuildVariant Criterion"/"formal BlueprintGenerator" normalized to camelCase, XSD documentation strings corroborate — BindingTimeEnum precedent; Tags/Stereotypes suffixes kept out of docstrings); the pre-existing 5-column checklist with a stale `# Spec verified: R23-11` stamp was rebuilt 6-column with release R23-11 and the stamp WITHHELD — deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All seven Table 7.4 attributes implemented spec-named: `blueprintCondition` (DocumentationBlock, 0..1, aggr), `desc` (MultiLanguageOverviewParagraph, 0..1, aggr), `formalBlueprintGenerator` (BlueprintGenerator, 0..1, aggr, atp.Status=draft — former `missing` row superseded), `postBuildVariantCondition` (`*`, aggr → `postBuildVariantConditions` typed list + add/get), `sdg` (Sdg, 0..1, aggr), `shortLabel` (Identifier, 0..1, attr, atpIdentityContributor), `swSyscond` (ConditionByFormula, 0..1, aggr); Base ARObject per the Base row (XSD complexType confirms, no flattening); docstrings verbatim from the table Notes; reader `readVariationPoint` + writer `writeVariationPoint` cover all seven in XSD element order. Stamp deferred to batch confirmation. |

## `VerbatimString`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 115 (Table 4.67)
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`

**Note:** Spec verified R23-11. Bare ARLiteral subclass per spec (no own attributes). Spec Table 4.67 defines two XML attributes (blueprintValue with atp.Status=draft, xmlSpace typed XmlSpaceEnum): blueprintValue not implemented due to its draft status; xmlSpace deferred to the VerbatimString sync row (the XmlSpaceEnum dependency has existed since the 2026-09-24 Sd sync — the original "missing enum" premise is stale; wiring spans the ad-hoc VT/VALUE writer sites). Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Modeled as bare ARLiteral subclass. Spec attributes blueprintValue (String, 0..1, attr, atp.Status=draft) and xmlSpace (XmlSpaceEnum, 0..1, attr) not implemented (draft status; XmlSpaceEnum missing enum). Per Rule 0001.4 guidance on draft/missing-dependency attributes. |

## `XmlSpaceEnum`
- **PDF:** *no own spec table*  |  **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Enumerations`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Enumerations.py`

XSD-only — synced 2026-09-24 from `AUTOSAR_00052.xsd` line 145398 (`XML-SPACE-ENUM`); both-corpora gate re-verified (no caption line, no header cell in R23-11 CP_TPS/FO_TPS or R4.3.1 markdown — only consumer attribute-type refs). Literals `default` (idx 0) / `preserve` (idx 1), wire tokens = the xml:space values themselves; class docstring + per-literal comments verbatim from XSD documentation. No open deviation rows. Supersedes the earlier "skipped per user / left as-is" note below. Consumer findings (not deviations of this class): the Sd reader gap (writer `writeSds` emitted `xml:space` but parser `readSd` did not read it back) was CLOSED 2026-09-26 in the WhitespaceControlled change set — `readSd` now calls the shared `readWhitespaceControlled`, and both helpers take `Union[Sd, WhitespaceControlled]` (Sd's xml:space is its own SD attributeGroup attribute, not WhitespaceControlled specialization); `VerbatimString.xmlSpace` still unimplemented (flagged for VerbatimString sync). Stamp (`# XSD verified: AUTOSAR_00052.xsd`) deferred to batch confirmation.

## `Annotation`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 163 (Table 4.72)
- **Package:** `M2::MSR::Documentation::Annotation`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Annotation.py`

**Note:** Spec verified R23-11. Concrete subclass of GeneralAnnotation with no own attributes. Per spec: "This is a plain annotation which does not have further formal data." Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Empty concrete subclass of GeneralAnnotation (inherits annotationOrigin, annotationText, label from parent). No own attributes per spec. |

## `HwAttributeDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 26 (Table 2.13)
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py`

**Note:** Spec verified R23-11. All spec attributes implemented: hwAttributeLiterals (List[HwAttributeLiteralDef], *), isRequired (Optional[Boolean], 0..1), unitRef (Optional[RefType], 0..1). Reader/writer coverage pending. Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwAttributeLiterals` | `List[HwAttributeLiteralDef]` | `hwAttributeLiteral` | `HwAttributeLiteralDef` | aggr | spec `*`; modeled as list. |
| `isRequired` | `Optional[Boolean]` | `isRequired` | `Boolean` | attr | spec `0..1`; modeled as Optional. |
| `unitRef` | `Optional[RefType]` | `unit` | `Unit` | Ref | spec `0..1`; modeled as Optional ref (RefType). |

## `HwPinGroup`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 19 (Table 2.5)
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

**Note:** Spec verified R23-11. Single spec attribute implemented: hwPinGroupContent (Optional[HwPinGroupContent], 0..1). Extends HwDescriptionEntity. Reader/writer coverage present. Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwPinGroupContent` | `Optional[HwPinGroupContent]` | `hwPinGroupContent` | `HwPinGroupContent` | aggr | spec `0..1`; modeled as Optional. |

## `HwPinConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 22 (Table 2.10)
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwPinConnector.py`

**Note:** Spec verified R23-11. **NEW CLASS** created. Single spec attribute: hwPinRefs (List[RefType], *, ref to HwPin). Extends Describable. Methods: addHwPinRef, getHwPinRefs. Reader/writer coverage pending. Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwPinRefs` | `List[RefType]` | `hwPin` | `HwPin` | Refs | spec `*`; modeled as list. |

## `HwPinGroupConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 22 (Table 2.9)
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwPinGroupConnector.py`

**Note:** Spec verified R23-11. **NEW CLASS** created. Two spec attributes: hwPinConnections (List[HwPinConnector], *, aggr), hwPinGroupRefs (List[RefType], *, ref to HwPinGroup). Extends Describable. Methods: addHwPinConnection/getHwPinConnections, addHwPinGroupRef/getHwPinGroupRefs. Reader/writer coverage pending. Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwPinConnections` | `List[HwPinConnector]` | `hwPinConnection` | `HwPinConnector` | aggr | spec `*`; modeled as list. |
| `hwPinGroupRefs` | `List[RefType]` | `hwPinGroup` | `HwPinGroup` | Refs | spec `*`; modeled as list. |

## `HwAttributeValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 16
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwAttributeValue.py`

**Note:** Class requires rework in future sync pass. Current implementation has fabricated fields (hwAttributeDefRef, value) instead of spec attributes (annotation, hwAttributeDef, v, vt). Spec Table 2.2 defines: annotation (Annotation, 0..1, aggr), hwAttributeDef (HwAttributeDef, 0..1, ref), v (Numerical, 0..1, attr), vt (VerbatimString, 0..1, attr). Not stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwAttributeDefRef` | `RefType` | `hwAttributeDef` | `HwAttributeDef` | Ref | type/name mismatch (spec 0..1 ref, model uses RefType; needs rework) |
| `value` | `str` | — | — | — | fabricated (not in spec) |
| — *(missing)* | `—` | `annotation` | `Annotation` | — | missing (needs impl) |
| — *(missing)* | `—` | `v` | `Numerical` | attr | missing (needs impl) |
| — *(missing)* | `—` | `vt` | `VerbatimString` | attr | missing (needs impl) |

## `HwPin`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 20
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

**Note:** Spec verified R23-11. All attributes implemented: functionName (List[String], *), packagingPinName (Optional[String], 0..1), pinNumber (Optional[Integer], 0..1). PDF-spec deviation: functionName/packagingPinName are in PDF Table 2.7 but have no corresponding XSD elements (only PIN-NUMBER exists in XSD); modeled with reader/writer for round-trip lossless compatibility (per Rule 0015: PDF authoritative for membership, reader/writer for serialization). Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `functionName` | `List[String]` | `functionName` | `String` | attr | spec `*` (mult many); XSD has no element (PDF-only); reader/writer covers for round-trip. |
| `packagingPinName` | `Optional[String]` | `packagingPinName` | `String` | attr | spec `0..1`; XSD has no element (PDF-only); reader/writer covers. |
| `pinNumber` | `Optional[Integer]` | `pinNumber` | `Integer` | attr | spec `0..1`; XSD has PIN-NUMBER element; covered by reader/writer. |

## `HwPinGroupContent`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 20
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

**Note:** Spec verified R23-11. Resolved multiplicity deviation from earlier tracker: PDF Table 2.6 lists hwPin and hwPinGroup as 0..1 single fields (not * as XSD atpMixed variation suggested); modeled as Optional single fields per PDF authoritative rule. XSD choice semantics (HW-PIN | HW-PIN-GROUP) handled in reader/writer. Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwPin` | `Optional[HwPin]` | `hwPin` | `HwPin` | aggr | spec `0..1` (single, not many); deviation row now resolved per PDF Table 2.6. |
| `hwPinGroup` | `Optional[HwPinGroup]` | `hwPinGroup` | `HwPinGroup` | aggr | spec `0..1` (single, not many); deviation row now resolved per PDF Table 2.6. |

## `HwElementConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 21
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementConnector.py`

**Note:** Class requires rework in future sync pass. Current implementation has fabricated fields (hwElementRef, hwPinRef) instead of spec-defined lists (hwElementRefs, hwPinConnections, hwPinGroupConnections). Spec Table 2.8: hwElement (HwElement, *, ref), hwPinConnection (HwPinConnector, *, aggr), hwPinGroupConnection (HwPinGroupConnector, *, aggr). Classes HwPinConnector/HwPinGroupConnector now exist and are stamped R23-11; HwElementConnector awaits rework to use them. Not stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwElementRef` | `RefType` | `hwElementRefs` | `Ref (HwElement)` | Refs | type (spec many → list[RefType]); fabricated single field (needs rework) |
| `hwPinRef` | `RefType` | `hwPinConnection` | `HwPinConnector` | aggr | wrong type/name (spec aggr list, model has single ref; needs rework) |
| — *(missing)* | `—` | `hwPinGroupConnection` | `HwPinGroupConnector` | aggr | missing (needs impl with HwPinGroupConnector) |



## `PassThroughSwConnector`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 83
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 3.15 attributes are modeled per multiplicity/kind: `providedOuterPort` (AbstractProvidedPortPrototype, 0..1, ref) as `providedOuterPortRef: Optional[RefType]` and `requiredOuterPort` (AbstractRequiredPortPrototype, 0..1, ref) as `requiredOuterPortRef: Optional[RefType]`, each with its get/set pair (None no-op, chaining). The pre-sync stale `missing` row for `serviceInterfaceElementMappingRefs` was removed: Table 3.15 lists no such attribute (stale row, Rule 0014). |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.15, p.83 (concrete Class; Base chain most-derived `SwConnector`, re-synced in this batch). Docstrings wiped and rewritten verbatim from the Table 3.15 Note and the two row Notes in the batch split-paragraph no-op style. Reader/writer coverage already complete: `readPassThroughSwConnector`/`writePassThroughSwConnector` handle PROVIDED-OUTER-PORT-REF / REQUIRED-OUTER-PORT-REF in the PASS-THROUGH-SW-CONNECTOR XSD group order, dispatched from CompositionSwComponentType CONNECTORS. Round-trip coverage in tests/test_armodel/writer/test_sw_composition_connectors.py (field values incl. DEST, element order, empty case). No Rule 0001.10 missing classes (`AbstractProvidedPortPrototype`/`AbstractRequiredPortPrototype` exist as modeled classes; ref kind → RefType per the sibling DelegationSwConnector.outerPort pattern). `# Spec verified:` withheld (batch 9b).

## `ApplicationError`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 108
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `errorCode` | `Integer` | — | missing |

## `ModeSwitchInterface`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 113
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modeGroup` | `—` | `modeGroup` | `ModeDeclarationGroupPrototype` | — | type (spec one vs py list) |

## `DataPrototypeMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 125
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All 6 spec attributes implemented (`firstDataPrototypeRef`, `firstToSecondDataTransformationRef`, `secondDataPrototypeRef`, `secondToFirstDataTransformationRef`, `subElementMappings`, `textTableMappings` with mult `0..2` → list). Reader/writer coverage added (incl. `SUB-ELEMENT-MAPPINGS`/`TEXT-TABLE-MAPPINGS` wrappers). |

## `ModeDeclarationMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | `secondModeRef` is `Optional[RefType]` (spec mult `0..1`), `firstModeRefs` is `List[RefType]` (spec mult `*`). |

## `ReceiverComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 172
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All 12 spec attributes implemented (`compositeNetworkRepresentation` mult `*` → list; `dataElement`, `handleOutOfRange`, `handleOutOfRangeStatus`, `maxDeltaCounterInit`, `maxNoNewOrRepeatedData`, `networkRepresentation`, `receptionProps`, `replaceWith`, `syncCounterInit`, `transformationComSpecProps` mult `*` → list, `usesEndToEndProtection`). Reader/writer coverage complete. |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified all 12 attributes both directions against Table 4.60, the verbatim Notes (Stereotypes/Tags tails dropped per Rule 0012.2.5.2), the abstract guard, member order, and the XSD RECEIVER-COM-SPEC group element order (AUTOSAR_00052.xsd l.95987): NETWORK-REPRESENTATION moved after MAX-NO-NEW-OR-REPEATED-DATA and USES-END-TO-END-PROTECTION moved to last in reader and writer; XSD-only `dataUpdatePeriod`/`externalReplacementRef`/`receiverIntent` elements are absent from the PDF table and stay unmodeled per Rule 0015). The legacy 5-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column format and the marker removed per the batch convention, re-stamp deferred to the batch 9b. Round-trip covered via NonqueuedReceiverComSpec on an RPortPrototype in tests/test_armodel/writer/test_com_spec_family.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `NonqueuedReceiverComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 173
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All 8 spec attributes implemented (`aliveTimeout`, `enableUpdate`, `filter`, `handleDataStatus`, `handleNeverReceived`, `handleTimeoutType`, `initValue`, `timeoutSubstitutionValue`); reader/writer coverage complete. |

**Note:** Rule-0023 re-sync 2026-10-05 (this pass re-verified all 8 attributes both directions against Table 4.62, the verbatim Notes, member order, and the XSD NONQUEUED-RECEIVER-COM-SPEC group element order; the legacy 5-column checklist was normalized to the 6-column format and the stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Reader/writer: dropped the duplicate `readARObject` call (`readReceiverComSpec` already chains `readRPortComSpec` → `readARObject`), upgraded `ALIVE-TIMEOUT` from the `Float`-typed helper to the spec-typed `TimeValue` helper (Table 4.66), and routed `HANDLE-TIMEOUT-TYPE` through `HANDLE_TIMEOUT_XML_MAP` + `_readEnumToken`/`_writeEnumToken` so the XML carries the XSD tokens (`NONE`/`REPLACE`/`REPLACE-BY-TIMEOUT-SUBSTITUTION-VALUE`) while the model keeps the camelCase literals. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `HandleTimeoutEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 174
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

No deviations — members `NONE`/`REPLACE`/`REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE` match the Table 4.65 literals
`none`/`replace`/`replaceByTimeoutSubstitutionValue` 1:1 (UPPER_CASE member names, member values = spec literals
exactly, indexes 0/1/2 per `atp.EnumerationLiteralIndex`); class docstring = Table 4.65 Note verbatim; standalone
`AREnum` (Steps 5/6 N/A — serialized as the `NonqueuedReceiverComSpec.handleTimeoutType` attribute value and
round-tripped there through `HANDLE_TIMEOUT_XML_MAP`); legacy 5-column checklist normalized to the 6-column format,
stale marker removed, re-stamp deferred to the batch 9b.

## `SenderComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 179
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(not modeled)* | `—` | `dataUpdatePeriod` | `TimeValue` | — | deprecated (atp.Status=removed), not implemented |

**Note:** Rule-0023 re-sync 2026-10-05 (this pass re-verified all 7 attributes both directions against Table 4.67, the verbatim Notes with their Stereotypes/Tags tails, member order (page-split table: `usesEndToEndProtection` last), and the XSD SENDER-COM-SPEC group element order; the legacy 5-column checklist was normalized to the 6-column format, the page citation corrected to p.179 per `pdf_page.py`, and the stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Reader/writer: `writeSenderComSpec` now calls `writeARObject` itself (audit `BASE` — the abstract base owns the reusable helper; `writeNonqueuedSenderComSpec`/`writeQueuedSenderComSpec` dropped their own call so each construction path calls it exactly once) and `readSenderComSpec` re-leveled to its direct base helper `readPPortComSpec`. Stale rows removed: the former `compositeNetworkRepresentations`/`networkRepresentation` "type (spec one vs py list)" row was wrong (Table 4.67 mult is `*` for `compositeNetworkRepresentation`, `0..1` for `networkRepresentation` — both modeled correctly); `senderIntent` is an XSD-only AP-candidate element absent from the CP PDF table and is simply not modeled (Rule 0015, no row); `transmissionProps` exists (`getTransmissionProps`/`setTransmissionProps`) so its "missing" row was stale. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `NonqueuedSenderComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 179
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Both spec attributes implemented (`dataFilter`, `initValue`); reader/writer coverage complete. |

**Note:** Rule-0023 re-sync 2026-10-05 (this pass re-verified both attributes both directions against Table 4.69, the verbatim Notes, and the XSD NONQUEUED-SENDER-COM-SPEC group element order DATA-FILTER → INIT-VALUE; the legacy 5-column checklist was normalized to the 6-column format and the stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Reader unchanged (`readSenderComSpec` base call + own attrs); writer's base call moved into `writeSenderComSpec` (see the SenderComSpec row). The former `dataFilter` "missing" row was stale — the accessor pair exists. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `TransmissionComSpecProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 180
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All 3 spec attributes implemented (`dataUpdatePeriod`, `minimumSendInterval`, `transmissionMode`, each `0..1` → `Optional[T]`); reader/writer coverage complete. |

**Note:** Rule-0023 re-sync 2026-10-05 (this pass re-verified all 3 attributes both directions against Table 4.70, the verbatim Notes, member order, and the XSD TRANSMISSION-COM-SPEC-PROPS group element order DATA-UPDATE-PERIOD → MINIMUM-SEND-INTERVAL → TRANSMISSION-MODE; Base `ARObject` per the table (XSD complexType refs `AR:AR-OBJECT` only); the legacy 5-column checklist was normalized to the 6-column format, the page citation corrected to p.180 per `pdf_page.py`, and the stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Reader/writer: `TRANSMISSION-MODE` routed through the new `TRANSMISSION_MODE_DEFINITION_XML_MAP` + `_readEnumToken`/`_writeEnumToken` in `getTransmissionComSpecProps`/`writeTransmissionComSpecProps` so the XML carries the XSD tokens (`CYCLIC`/`CYCLIC-AND-ON-CHANGE`/`TRIGGERED`) while the model keeps the camelCase literals; `readARObject`/`writeARObject` base calls unchanged. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `TransmissionAcknowledgementRequest`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 180
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | The single spec attribute implemented (`timeout`, `0..1` → `Optional[TimeValue]`); reader/writer coverage complete. |

**Note:** Rule-0023 re-sync 2026-10-05 (this pass re-verified the attribute both directions against Table 4.71, the verbatim Note, and the XSD TRANSMISSION-ACKNOWLEDGEMENT-REQUEST group (TIMEOUT); Base `ARObject` per the table (XSD complexType refs `AR:AR-OBJECT` only); the class docstring now carries the Table 4.71 Note verbatim with the class-level `[constr_1892]` row appended (Rule 0012.2.4); the legacy 5-column checklist was normalized to the 6-column format and the stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Reader/writer unchanged — `readTransmissionAcknowledgementRequest`/`writeTransmissionAcknowledgementRequest` call `readARObject`/`writeARObject` (audit `BASE` pass, S/T round-trip pinned by test). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `HandleOutOfRangeEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 180 *(also cited: `AUTOSAR_CP_TPS_SystemTemplate.pdf` Table 6.11, p.323)*
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

No deviations — members `DEFAULT`/`EXTERNAL_REPLACEMENT`/`IGNORE`/`INVALID`/`NONE`/`SATURATE` match the Table 4.72
literals `default`/`externalReplacement`/`ignore`/`invalid`/`none`/`saturate` 1:1 (UPPER_CASE member names, member
values = spec literals exactly, indexes 0-5 per `atp.EnumerationLiteralIndex`); class docstring = Table 4.72 Note
verbatim; standalone `AREnum` (Steps 5/6 N/A for the enum itself — serialized as the `ISignalProps`/`ReceiverComSpec`/
`SenderComSpec` `handleOutOfRange` attribute value and round-tripped there); legacy checklist normalized to the
6-column format, stale marker removed, re-stamp deferred to the batch 9b.

**Reader/writer note (consuming sites):** all three `HANDLE-OUT-OF-RANGE` read/write sites (`readReceiverComSpec`,
`readSenderComSpec`, `readISignalProps` / `writeReceiverComSpec`, `writeSenderComSpec`, `writeISignalProps`) are now
routed through the new `HANDLE_OUT_OF_RANGE_XML_MAP` + `_readEnumToken`/`_writeEnumToken` so the XML carries the XSD
tokens (`DEFAULT`/`EXTERNAL-REPLACEMENT`/`IGNORE`/`INVALID`/`NONE`/`SATURATE` per
`AR:HANDLE-OUT-OF-RANGE-ENUM--SIMPLE`) while the model keeps the camelCase literals. No Rule 0001.10 missing classes.
No stamp (batch 9b).

## `TransmissionModeDefinitionEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 181
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

No deviations — members `CYCLIC`/`CYCLIC_AND_ON_CHANGE`/`TRIGGERED` match the Table 4.73 literals
`cyclic`/`cyclicAndOnChange`/`triggered` 1:1 (UPPER_CASE member names, member values = spec literals exactly,
indexes 0/2/1 per `atp.EnumerationLiteralIndex`, member order = markdown displayed row order); class docstring =
Table 4.73 Note verbatim; standalone `AREnum` (Steps 5/6 N/A — serialized as the `TransmissionComSpecProps.
transmissionMode` attribute value and round-tripped there through `TRANSMISSION_MODE_DEFINITION_XML_MAP`, landed
with the TransmissionComSpecProps commit); legacy 5-column checklist normalized to the 6-column format, stale
marker removed, re-stamp deferred to the batch 9b.

## `ClientComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 187
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `clientIntent` | `ClientIntentEnum` | — | missing |
| — *(missing)* | `—` | `endToEndCallResponseTimeout` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `getterRef` | `Ref (Field)` | Ref | missing |
| — *(missing)* | `—` | `setterRef` | `Ref (Field)` | Ref | missing |
| — *(missing)* | `—` | `transformationComSpecProps` | `EndToEndTransformationComSpecProps` | — | missing |

## `ServerComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 188
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `getterRef` | `Ref (Field)` | Ref | missing |
| — *(missing)* | `—` | `setterRef` | `Ref (Field)` | Ref | missing |

## `ParameterProvideComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 192
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `initValue` | `ApplicationAssocMapValueSpecification` | — | missing |
| — *(missing)* | `—` | `parameterRef` | `Ref (ParameterDataPrototype)` | Ref | missing |

## `TransformationTechnology`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 198
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

No deviations — the stale `type (spec many vs py single)` row on `transformationDescription` is removed (Rule 0001.4 stale row): the "many" came only from the XSD (`pureMM.maxOccurs="-1"` after atpVariation resolution, AUTOSAR_00052.xsd group TRANSFORMATION-TECHNOLOGY line 125800), while the PDF Table 4.87 row is Mult `0..1` — the single `Optional[TransformationDescription]` field is PDF-correct (Rule 0015).

## `TransformationDescription`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 199
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

No deviations — abstract Class (Table 4.89) with no own `Attribute` rows; Base `ARObject, Describable` modeled as `Describable` (already stamped); the atpVariation capability on the aggregation row `TransformationTechnology.transformationDescription` is carried by the `VariationPointCapable` mixin (Rule 0020; XSD group TRANSFORMATION-DESCRIPTION line 125461 holds VARIATION-POINT), with reader/writer coverage via the reusable `readTransformationDescription`/`writeTransformationDescription` helpers.

## `EndToEndTransformationComSpecProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 201
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(not modeled)* | `—` | `windowSize` | `PositiveInteger` | — | deprecated (atp.Status=removed), not implemented — XSD group `END-TO-END-TRANSFORMATION-COM-SPEC-PROPS` (`AUTOSAR_00052.xsd` L54577) carries `WINDOW-SIZE` with `atp.Status="removed"`; absent from the R23-11 PDF Table 4.92 `Attribute` rendering (Rule 0015) |

**Note:** Batch sync 2026-10-04 (Group28 row 4; Rule 0023 legacy checklist re-sync). The stale `naming` row claiming source `windowSizeInit` maps to spec `windowSize` is removed (Rule 0014 stale row): the spec row is `windowSizeInit` (Table 4.92), while `windowSize` is the deprecated XSD-only attribute above. Two reader/writer to-fix defects found and fixed in this pass (rows removed per Rule 0014): (1) reader/writer used element tag `E2E-PROFILE-COMPATIBILITY-PROPS-REF` where the XSD spells `E-2-E-PROFILE-COMPATIBILITY-PROPS-REF` — XSD-valid files silently lost the ref; (2) writer `writeReceiverComSpec` dispatched E2E props through the base `writeTransformationComSpecProps` helper, dropping all 16 attributes for receiver com specs (Rule 0001.7 aggregator-coverage violation) — replaced with the shared `writeTransformationComSpecPropss` dispatcher.

## `ApplicationArrayDataType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 252  | **table:** Table 5.8
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

No deviations — both Table 5.8 attributes are modeled with spec shapes: `dynamicArraySizeProfile` (String, `0..1`, attr), `element` (ApplicationArrayElement, `0..1`, aggr → Referrable child, so `createApplicationArrayElement(short_name)` + `getApplicationArrayElement()` per Rule 0001.6) — each `Optional[T]` PEP 526 member + guarded accessors with full reader/writer coverage. Base most-derived `ApplicationCompositeDataType` (Table 5.6, p.241, already stamped). Stale row removed this pass: `applicationArrayElement` / `type (spec one vs py list)` described a superseded shape — the field is the spec-named `element`, `Optional[ApplicationArrayElement]` (py single), matching the PDF `0..1`.

**Note:** Batch re-sync 2026-10-04 (Group28 row; pre-release-column checklist with stale `# Spec verified: R23-11` stamp — the marker was removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). Class docstring rewritten verbatim from the markdown Note (`Tags:` tail dropped per ApplicationRecordDataType/SwTextProps convention) with constr_1907 appended; accessor docstrings wiped and rewritten verbatim (Args/Returns blocks and the "Named getApplicationArrayElement…" rationale sentence removed). One Rule 0001.11 fix: the `element` accessor pair reordered mutator-first (create before get). Reader/writer coverage and ARPackage dispatch pre-existed in XSD group order (DYNAMIC-ARRAY-SIZE-PROFILE [then] ELEMENT) — no parser/writer change; round-trip tests added on both sides. Referenced member type `ApplicationArrayElement` (Table 5.9) is queued separately in Group28 — no missing classes; FO_TPS AbstractPlatformSpecification Table 3.16, p.35 rendering is identical (SWCT defining doc cited).

## `ApplicationArrayElement`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 252  | **table:** Table 5.9
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py`

No deviations — all four Table 5.9 attributes are modeled with spec shapes: `arraySizeHandling` (ArraySizeHandlingEnum, `0..1`, attr), `arraySizeSemantics` (ArraySizeSemanticsEnum, `0..1`, attr), `indexDataType` (ApplicationPrimitiveDataType, `0..1`, ref → `indexDataTypeRef: Optional[RefType]`, Kind-suffix per Rule 0001.5), `maxNumberOfElements` (PositiveInteger, `0..1`, attr — the XSD's `POSITIVE-INTEGER-VALUE-VARIATION-POINT` element type is the atpVariation attribute-value serialization form; the PDF type PositiveInteger wins per Rule 0001.3/0015). Base most-derived `ApplicationCompositeElementDataPrototype` (Table 5.30, p.306, already stamped — inherited `type` tref stays on the base, no flattening). `maxNumberOfElements` carries `atpVariation` but Kind=attr → attribute-value variation only; the XSD group APPLICATION-ARRAY-ELEMENT (AUTOSAR_00052.xsd L2846) anchors no VARIATION-POINT → not VP-capable (Rule 0020).

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). Accessor docstrings wiped and rewritten verbatim (Args/Returns blocks removed; `maxNumberOfElements` inline comment dropped the `Stereotypes:/Tags:` tail). One Rule 0001.3 to-fix fixed in this pass (no deviation row remains): reader `readApplicationArrayElement` used the looser `getChildElementOptionalNumericalValue` (materializing `Numerical` where the field/getter/setter declare `Optional[PositiveInteger]`) — upgraded to the spec-typed `getChildElementOptionalPositiveInteger`, writer to `setChildElementOptionalPositiveInteger` (matched leaf pair). Reader/writer element order and ARPackage dispatch pre-existed in XSD group order; round-trip tests added on both sides. Referenced member types `ArraySizeHandlingEnum` (Table 5.11) and `ArraySizeSemanticsEnum` (Table 5.10) are stamped R23-11 — no missing classes.

## `ParameterInAtomicSWCTypeInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 319  | **table:** Table 5.36
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::InstanceRefsUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/DataElements/InstanceRefsUsage.py`

No deviations — all five Table 5.36 attributes are modeled with the spec shape: `base` (AtomicSwComponentType, 0..1, ref, atpDerived — XSD skips the element) as `baseRef: Optional[RefType]` + `getBaseRef()`/`setBaseRef()` with `[—]` reader/writer; `contextDataPrototype` (ordered, *, ref) as the dedicated typed list `contextDataPrototypeRefs: List[RefType]` + `addContextDataPrototypeRef()`/`getContextDataPrototypeRefs()`; `portPrototype`, `rootParameterDataPrototype`, `targetDataPrototype` (each 0..1, ref) as `Optional[RefType]` members with the plain `Ref` suffix per Rule 0001.5. Concrete Class (Base most-derived = `AtpInstanceRef`, Table 5.3, stamped R23-11 — no flattening: all five rows are the subclass's own). Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction): docstrings wiped and rewritten verbatim (Args/Returns blocks removed; `base` keeps its pure-stereotype Note; the spec's "This ist the context" typo kept verbatim). The stale `type (spec many vs py single)` tracker row for `contextDataPrototypeRef` removed — the dedicated typed list pre-dated this pass and is spec-shaped. Writer `setParameterInAtomicSWCTypeInstanceRef` element order fixed to the XSD group sequenceOffset order (PORT → ROOT-PARAMETER → CONTEXT → TARGET; CONTEXT was emitted first), reader statement order aligned for symmetry (read is tag-based, order-independent). Referenced types `RefType` and base `AtpInstanceRef` exist and are stamped — no missing classes.

## `SwCalprmAxis`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 352
- **Package:** `M2::MSR::DataDictionary::CalibrationParameter`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(not modeled)* | `—` | `baseType` | `Ref (SwBaseType)` | Ref | deprecated (atp.Status="removed"), not implemented |

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, reader [x] misplaced on getter rows, stale `# Spec verified: R23-11` marker removed at session start; the checklist is rewritten in the 6-column release form and the stamp stays WITHHELD pending the 9b batch confirmation, user instruction). Model Red genuine: `get_type_hints` on `setSwAxisIndex`/`setSwCalibrationAccess` raised NameError (both names were TYPE_CHECKING-only, Rule 0001.8) — `AxisIndexType` moved to a top-level import (RecordLayout has no back-import) and `SwCalibrationAccessEnum` to a bottom-of-module cycle-breaker import; the new edge closed `Constants→CalibrationParameter→DataDefProperties→Constants` mid-initialization, so `CommonStructure/Constants/__init__.py` moved its `CalprmAxisCategoryEnum`/`AxisIndexType` imports below the `ValueSpecification` definition (Rule 0005; ValueList precedent). Behavioral/docstring pins were already conforming (vacuous Red portion, noted). Reader Red genuine (Rule 0001.3): `getSwCalprmAxis` materialized `swAxisIndex`/`displayFormat` as plain `ARLiteral` behind `cast` while the PDF types them `AxisIndexType`/`DisplayFormatString` — both upgraded to typed materialization (ApplicationArrayElement precedent); the enum `category` keeps the generic-literal+cast shared consumer pattern (same flagged-for-9b decision as the ArraySizeSemanticsEnum/ArraySizeHandlingEnum siblings — CalprmAxisCategoryEnum is a later Group28 row; its wire forms equal the member values so no token map applies). Writer already conformed (XSD group order SW-AXIS-INDEX(20), CATEGORY(30), SW-AXIS-GROUPED|SW-AXIS-INDIVIDUAL(40), SW-CALIBRATION-ACCESS(90), DISPLAY-FORMAT(100); UPPERCASE wire token via `SW_CALIBRATION_ACCESS_XML_MAP` from the SwCalibrationAccessEnum pass) — vacuous writer Red, noted. Two stale tracker rows removed: `swAxisIndex missing` (implemented with full reader/writer coverage) and `baseTypeRef missing` (the attribute is not in the PDF table at all; XSD BASE-TYPE-REF sequenceOffset 110 carries `atp.Status="removed"` — replaced by the accepted deprecated row above, XSD member name `baseType`). Two missed consumer tests from the SwCalibrationAccessEnum pass aligned to the XSD wire form (both failing at committed HEAD): `test_arxml_parser_internals.py::test_getSwCalprmAxis_access_and_display_format` fed the non-XSD camelCase form and `test_arxml_writer.py::test_setSwCalprmAxis_access_and_display_format` asserted the camelCase emission. Out-of-scope observations for the 9b reviewer: `getSwAxisGrouped` (arxml_parser.py L7239) and `getRuleBasedAxisCont` (arxml_parser.py L8862) keep the `AxisIndexType` cast — SwAxisCont (Table 5.124) and RuleBasedAxisCont (Table 5.130) are queued Group28 rows with their own passes; SwAxisGrouped/SwAxisIndividual are likewise outside this class's ledger. No Rule 0001.10 missing referenced classes (CalprmAxisCategoryEnum/SwCalprmAxisTypeProps exist in-module as later Group28 rows; DisplayFormatString is a core primitive; AxisIndexType exists as the ARLiteral-subclass primitive in RecordLayout.py; SwCalibrationAccessEnum was just synced).

## `SwCalprmAxisTypeProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 353
- **Package:** `M2::MSR::DataDictionary::CalibrationParameter`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py`

No deviations — both Table 5.49 attributes are modeled with spec shapes: `maxGradient` (Float, `0..1`, attr), `monotony` (MonotonyEnum, `0..1`, attr) — each `Optional[T]` PEP 526 member + guarded accessors. Abstract class (spec renders `SwCalprmAxisTypeProps (abstract)`; Base `ARObject` → `ARObject, ABC` with the `type(self) is SwCalprmAxisTypeProps` instantiation guard); concrete subclasses `SwAxisGrouped`/`SwAxisIndividual` (Table 5.55/5.50, Axis.py) exist and consume the group through the polymorphic SW-AXIS-GROUPED|SW-AXIS-INDIVIDUAL choice at SwCalprmAxis (XSD sequenceOffset 40).

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). Model Red vacuous (impl conforms — noted): fields, accessors, guard, verbatim docstrings and PEP 526 annotations were already spec-shaped from the prior pass; the new parity pins (class-note verbatim, member order, accessor order, `get_type_hints` resolution, docstring verbatim) pass unchanged. Reader/writer Red genuine (Rule 0001.7 — an abstract XML-bearing base owns reusable helpers): the MAX-GRADIENT/MONOTONY reads/writes were duplicated inline in all four concrete handlers (`getSwAxisIndividual`/`getSwAxisGrouped`, `setSwAxisIndividual`/`setSwAxisGrouped`); extracted into the matched pair `readSwCalprmAxisTypeProps`/`writeSwCalprmAxisTypeProps` called by both branches. Reader Red genuine (Rule 0001.3, ApplicationArrayElement precedent): MONOTONY materialized a plain `ARLiteral` behind `cast(Optional[MonotonyEnum], …)` — upgraded to typed materialization via `_readEnumToken` + the new `MONOTONY_XML_MAP` (AR:MONOTONY-ENUM--SIMPLE); writer upgraded from the non-XSD camelCase emission to the UPPERCASE wire token via `_writeEnumToken` (Rule 0011; no integration fixture carries MONOTONY). Three stale consumer tests aligned to the XSD wire form (the first two failing at committed HEAD after the fix): `test_arxml_parser_internals.py::test_getSwCalprmAxis_individual_type_props` (fed camelCase `strictlyIncreasing`), `…grouped_type_props` (fed camelCase `monotonous`), `test_arxml_writer.py::test_setSwCalprmAxis_individual_type_props` (asserted camelCase emission); the element-level round-trip test additionally pins `isinstance(…, MonotonyEnum)`. One adjacent round-trip fix made in passing (the parser hand was already in `getSwAxisGrouped`): the handler never called `readARObject`, so the S/T checksum/timestamp attributes its own writer emits (`setSwAxisGrouped` → `writeARObject`) were silently dropped on re-parse; `getSwAxisIndividual` already read them — flagged for the 9b reviewer (SwAxisGrouped's own ledger). Out-of-scope observation for the 9b reviewer: `setSwAxisIndividual` emits SW-VARIABLE-REFS before INPUT-VARIABLE-TYPE-REF while the XSD group SW-AXIS-INDIVIDUAL (L114507) orders INPUT-VARIABLE-TYPE-REF first — SwAxisIndividual (Table 5.50) is its own queued row with its own pass. No Rule 0001.10 missing referenced classes (Float is a core primitive; MonotonyEnum is stamped R23-11, Table 5.87).

## `SwAxisGeneric`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 355
- **Package:** `M2::MSR::DataDictionary::Axis`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/Axis.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(not implemented)* | `—` | `swNumberOfAxisPoints` | `IntegerValueVariationPoint` | — | deprecated (atp.Status=removed), not implemented |

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed, 6-column rewrite, stamp WITHHELD pending the 9b batch confirmation, user instruction). Both Table 5.51 attributes were already spec-shaped (`swAxisType` ref 0..1 → `swAxisTypeRef: Optional[RefType]`; `swGenericAxisParam` aggr * → `swGenericAxisParams: List[SwGenericAxisParam]` + dedicated typed list, add/get). Model Red genuine on two pins: the list attribute's accessor pair order fixed to mutator-first (`addSwGenericAxisParam` now precedes `getSwGenericAxisParams`, Rule 0001.11 — MsrQuery precedent) and the setter docstrings rewritten single-line (stale two-line form; verbatim Note + None-no-op sentence preserved). Reader/writer Red vacuous — dispatch already existed and conforms (`getSwAxisGeneric`/`setSwAxisGeneric`; SW-AXIS-TYPE-REF sequenceOffset 20 before the SW-GENERIC-AXIS-PARAMS wrapper at 40; wrapper emitted only when non-empty); new direct reader tests (full field values, empty-wrapper → `[]`, minimal defaults) and writer tests (round-trip, wrapper omission) genuinely exercise the pair. The XSD group's third element SW-NUMBER-OF-AXIS-POINTS (AUTOSAR_00052.xsd L114419, sequenceOffset 30) carries `atp.Status="removed"` and is absent from the R23-11 PDF table — not modeled (Rules 0001.3/0015); the former stale `missing` tracker row is corrected to the accepted `deprecated (atp.Status=removed)` reason. No Rule 0001.10 blockers: ref target `SwAxisType` exists as an ARElement stub whose own sync is the next Group28 row (Table 5.52; the ref is a `RefType` — no Python-typed dependency), and member type `SwGenericAxisParam` exists in the same module with its own later queue row (Table 5.53).

## `SwGenericAxisParam`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 356
- **Package:** `M2::MSR::DataDictionary::Axis`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/Axis.py`

No deviations — both Table 5.53 attributes are modeled 1:1 in displayed order (`swGenericAxisParamType` SwGenericAxisParamType 0..1 ref → `swGenericAxisParamTypeRef: Optional[RefType]` + get/set pair, getter first; `vf (ordered)` Numerical `*` attr → `vfs: List[Numerical]` dedicated typed list + add/get pair, mutator first). Base `ARObject` → `__init__(self)`; concrete class aggregated by `SwAxisGeneric.swGenericAxisParam` — the SW-GENERIC-AXIS-PARAM complexType IS a real element type inside the SW-GENERIC-AXIS-PARAMS role wrapper (AUTOSAR_00052.xsd L114435), so S/T apply and `getSwGenericAxisParam`/`setSwGenericAxisParam` call `readARObject`/`writeARObject` (Rule 0025 clean both directions, audit BASE pass).

**Note:** Batch re-sync 2026-10-05 (Group28 follow-up; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed at session start, 6-column rewrite, stamp WITHHELD pending the 9b batch confirmation, user instruction). Model Red genuine on two pins: the `vf` accessor pair order fixed to mutator-first (`addVf` now precedes `getVfs`, Rule 0001.11 — SwAxisGeneric precedent in the same module) and the attribute comments/docstrings rewritten to carry the spec `Note` tails verbatim (`Tags: xml.sequenceOffset=20` on swGenericAxisParamType; `Stereotypes: atpVariation Tags: vh.latestBindingTime=…` on vf) per Rule 0012.2.5.3 (2026-10-05 settlement — the prior pass predated it); setter docstrings single-line per the sibling shape. Reader/writer Red vacuous — `getSwGenericAxisParam`/`setSwGenericAxisParam` already existed and conform (readARObject/writeARObject; XSD group order SW-GENERIC-AXIS-PARAM-TYPE-REF at sequenceOffset 20 before the VF elements at 30; no wrapper elements named after groups); new parser tests (field values, multi-param order, empty wrapper → `[]`, S/T on the element, no-SW-AXIS-GENERIC default) and writer tests (element order + DEST attr, unset members omitted) plus a full-document XSD-validated round-trip through SwCalprmAxis → SwAxisIndividual → SwAxisGeneric genuinely pin the pair. No Rule 0001.10 missing referenced classes (ref target `SwGenericAxisParamType` Table 5.54 stamped in-module; `Numerical` is a stamped core primitive).

## `PhysConstrs`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 406
- **Package:** `M2::MSR::AsamHdo::Constraints::GlobalConstraints`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `lowerLimit` | `Limit` | — | missing |
| — *(missing)* | `—` | `maxDiff` | `NumericalValue` | — | missing |
| — *(missing)* | `—` | `maxGradient` | `NumericalValue` | — | missing |
| — *(missing)* | `—` | `monotony` | `MonotonyEnum` | — | missing |
| — *(missing)* | `—` | `scaleConstr` | `ScaleConstr` | — | missing |
| `unit_ref` | `—` | `unitRef` | `Ref (Unit)` | Ref | naming |
| — *(missing)* | `—` | `upperLimit` | `Limit` | — | missing |

## `InternalConstrs`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 407
- **Package:** `M2::MSR::AsamHdo::Constraints::GlobalConstraints`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `lowerLimit` | `Limit` | — | missing |
| — *(missing)* | `—` | `maxDiff` | `NumericalValue` | — | missing |
| — *(missing)* | `—` | `maxGradient` | `NumericalValue` | — | missing |
| — *(missing)* | `—` | `monotony` | `MonotonyEnum` | — | missing |
| — *(missing)* | `—` | `scaleConstr` | `ScaleConstr` | — | missing |
| — *(missing)* | `—` | `upperLimit` | `Limit` | — | missing |

## `SwRecordLayoutV`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 421
- **Package:** `M2::MSR::DataDictionary::RecordLayout`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/RecordLayout.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `category` | `AsamRecordLayoutSemantics` | — | missing |

## `ReferenceValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 436
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `referenceValueRef` | `Ref (DataPrototype)` | Ref | missing |

## `NotAvailableValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 440
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `defaultPattern` | `PositiveInteger` | — | missing |

## `ConstantSpecificationMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 443
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `applConstantRef` | `Ref (ConstantSpecification)` | Ref | missing |
| — *(missing)* | `—` | `implConstantRef` | `Ref (ConstantSpecification)` | Ref | missing |

## `SwValues`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 458
- **Package:** `M2::MSR::CalibrationData::CalibrationValue`
- **Source:** `src/armodel/models/M2/MSR/CalibrationData/CalibrationValue.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `_v` | `List[ARNumerical]` | `v` | `NumericalValue` | — | type (spec one vs py list) |
| `_vf` | `List[ARNumerical]` | `vf` | `NumericalValueVariationPoint` | — | type (spec one vs py list) |
| `_vg` | `Optional[ValueGroup]` | `vg` | `ValueGroup` | — | — |
| `_vt` | `Optional[VerbatimString]` | `vt` | `VerbatimString` | — | — |
| `_vtf` | `List[NumericalOrText]` | `vtf` | `NumericalOrText` | — | type (spec one vs py list) |

- **Note:** `v`, `vf`, and `vtf` are modelled as Python lists (`List[...]`) instead of the PDF's single-valued (`0..1`) attributes. This is an accepted deviation (Rule 0001.3 XML-forces carve-out): `SwValues` is an `<<atpMixed>>` choice group where the `V`/`VF`/`VTF` elements may repeat in the XSD (the XSD documentation raises their upper multiplicity to `*`, and multi-value curves/value-sets require many `V` elements); a single-valued field cannot hold them. `vg` and `vt` match the PDF `0..1` multiplicity exactly. Reader (`getSwValues`) and writer (`setSwValues`/`setValueGroup`) coverage added for all five members (2026-08-23).

## `RuleBasedAxisCont`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 464
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations — Table 5.130 attributes (`category` via `getCategory`/`setCategory`, `unit` Ref via `getUnitRef`/`setUnitRef`, `swArraysize` via `getSwArraysize`/`setSwArraysize`, `swAxisIndex` via `getSwAxisIndex`/`setSwAxisIndex`, `ruleBasedValues` via `getRuleBasedValues`/`setRuleBasedValues`) all implemented per Rule 1.4. |

## `NumericalRuleBasedValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 467
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ruleBasedValues` | `RuleBasedValueSpecification` | — | missing |

## `CompositeRuleBasedValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 471
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `compoundPrimitiveArgument` | `ApplicationRuleBasedValueSpecification` | — | missing |
| — *(missing)* | `—` | `maxSizeToFill` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `rule` | `Identifier` | — | missing |

## `SwcModeSwitchEvent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 544
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modeIRef` | `—` | `mode` | `RModeInAtomicSwcInstanceRef` | — | type (spec one vs py list) |

## `IncludedDataTypeSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 600
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::IncludedDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/IncludedDataTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `literalPrefix` | `Identifier` | — | missing |

## `SensorActuatorSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 646
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `sensorActuatorRef` | `Ref (HwDescriptionEntity)` | Ref | missing |

## `DiagnosticOperationCycleNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 761
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `operationCycleAutomaticEnd` | `Boolean` | — | missing |
| — *(missing)* | `—` | `operationCycleAutostart` | `Boolean` | — | missing |

## `ObdRatioServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 795
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `connectionType` | `ObdRatioConnectionKindEnum` | — | missing |
| — *(missing)* | `—` | `denominatorGroup` | `DiagnosticDenominatorConditionEnum` | — | missing |
| — *(missing)* | `—` | `iumprGroup` | `NmtokenString` | — | missing |
| — *(missing)* | `—` | `rateBasedMonitoredEventRef` | `Ref (DiagnosticEventNeeds)` | Ref | missing |
| — *(missing)* | `—` | `usedFidRef` | `Ref (FunctionInhibitionNeeds)` | Ref | missing |
| — *(missing)* | `—` | `usedSecondaryFidRefs` | `Ref (FunctionInhibitionNeeds)` | Refs | missing |

## `ObdRatioDenominatorNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 802
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `denominatorCondition` | `DiagnosticDenominatorConditionEnum` | — | missing |

## `DoIpRoutingActivationAuthenticationNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 806
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataLengthRequest` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `dataLengthResponse` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `routingActivationType` | `NmtokenString` | — | missing |

## `DoIpRoutingActivationConfirmationNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 807
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataLengthRequest` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `dataLengthResponse` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `routingActivationType` | `NmtokenString` | — | missing |

## `SecureOnBoardCommunicationNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 824
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `verificationStatusIndicationMode` | `VerificationStatusIndicationModeEnum` | — | missing |

## `IdsMgrNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 842
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `useSmartSensorApi` | `Boolean` | — | missing |

## `ApplicationCompositeElementInPortInterfaceInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 952
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/InstanceRefs.py`

No deviations (synced to R23-11 Table D.17, p.953 — `contextDataPrototype` now a typed `List[RefType]` matching the spec `*` multiplicity).

## `ConsumedEventGroup`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 978
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `instanceIdentifier` | `PositiveInteger` | — | missing |
| `sdClientTimerConfigRef` | `—` | `sdClientTimerConfig` | `SomeipSdClientEventGroupTimingConfigRefConditional` | — | type (spec many vs py single) |

## `ConsumedServiceInstance`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 980
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blacklistedVersion` | `SomeipServiceVersion` | — | missing |
| `eventMulticastSubscriptionAddressRef` | `—` | `eventMulticastSubscriptionAddress` | `ApplicationEndpointRefConditional` | — | type (spec many vs py single) |
| `sdClientTimerConfigRef` | `—` | `sdClientTimerConfig` | `SomeipSdClientServiceInstanceConfigRefConditional` | — | type (spec many vs py single) |

## `DataMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 217  | **table:** Table 5.22
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DataMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `communicationDirection` | `Optional[CommunicationDirectionType]` | `communicationDirection` | `CommunicationDirectionType` | attr | `legacy (R4.3.1 Table 5.14, p.142); removed in R23-11` |
| `eventGroupRefs` | `List[RefType]` | `eventGroup` | `ConsumedEventGroup` | ref | `legacy (R4.3.1 Table 5.14, p.142); removed in R23-11` |
| `eventHandlerRefs` | `List[RefType]` | `eventHandler` | `EventHandler` | ref | `legacy (R4.3.1 Table 5.14, p.142); removed in R23-11` |
| `serviceInstanceRefs` | `List[RefType]` | `serviceInstance` | `AbstractServiceInstance` | ref | `legacy (R4.3.1 Table 5.14, p.142); removed in R23-11` |

Rule 0019 combine case. R23-11 Table 5.22 no longer lists these four members, but all four are documented in the older verified corpus (R4.3.1 Table 5.14, p.142) and authentic R22-11 `*_SystemMapping.arxml` fixtures carry `<COMMUNICATION-DIRECTION>` inside `SENDER-RECEIVER-TO-SIGNAL-MAPPING` (which inlines the `DATA-MAPPING` group). Removing `communicationDirection` broke the lossless integration round-trip over 8 fixtures, so all four are kept as optional legacy members with full reader/writer coverage in XSD group order (`COMMUNICATION-DIRECTION`, `EVENT-GROUP-REFS`, `EVENT-HANDLER-REFS`, `INTRODUCTION`, `SERVICE-INSTANCE-REFS`, `VARIATION-POINT`); fixtures are never edited to force a removal. No other deviations.

## `EndToEndTransformationDescription`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 987
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `windowSizeInit` | `—` | `windowSize` | `PositiveInteger` | — | naming |

## `ISignalGroup`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 993
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

No deviations — the stale `type (spec many vs py single)` row on `transformationISignalProps` is removed (Rule 0014 to-fix, now fixed): both `ISignal` and `ISignalGroup` model `transformationISignalProps: List[TransformationISignalProps]` (spec `*`, R23-11 XSD wrapper TRANSFORMATION-I-SIGNAL-PROPSS) with `addTransformationISignalProps`/`getTransformationISignalProps` and full reader/writer dispatch over the three concrete subclasses.

## `ISignalIPdu`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 994
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `iPduTimingSpecification` | `—` | `iPduTimingSpecification` | `IPduTiming` | — | type (spec many vs py single) |
| — *(missing)* | `—` | `pduCounter` | `SignalIPduCounter` | — | missing |
| — *(missing)* | `—` | `pduReplication` | `SignalIPduReplication` | — | missing |

## `ProvidedServiceInstance`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 1000
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `allowedServiceConsumer` | `NetworkEndpointRefConditional` | — | missing |
| — *(missing)* | `—` | `autoAvailable` | `Boolean` | — | missing |
| — *(missing)* | `—` | `loadBalancingPriority` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `loadBalancingWeight` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `localUnicastAddress` | `ApplicationEndpointRefConditional` | — | missing |
| — *(missing)* | `—` | `minorVersion` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `remoteMulticastSubscriptionAddress` | `ApplicationEndpointRefConditional` | — | missing |
| — *(missing)* | `—` | `remoteUnicastAddress` | `ApplicationEndpointRefConditional` | — | missing |
| — *(missing)* | `—` | `sdServerTimerConfig` | `SomeipSdServerServiceInstanceConfigRefConditional` | — | missing |

## `RootSwCompositionPrototype`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 1003
- **Package:** `M2::AUTOSARTemplates::SystemTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `calibrationParameterValueSetRef` | `—` | `calibrationParameterValueSetRefs` | `Ref (CalibrationParameterValueSet)` | Refs | type (spec many vs py single) |

## `TransientFault`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 1009
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | No deviations |

## `CanCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 62
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `canClusterVariant` | `CanClusterConditional` | — | missing |

## `CanCommunicationController`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 63
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `canCommunicationControllerVariant` | `CanCommunicationControllerConditional` | — | missing |

## `CanControllerFdConfiguration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 66
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `trcvDelayCompensationOffset` | `TimeValue` | — | missing |

## `CanControllerXlConfiguration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 70
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `errorSignalingEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `propSeg` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `pwmL` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `pwmO` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `pwmS` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `sspOffset` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `syncJumpWidth` | `PositiveInteger` | — | missing |
| `timeSeg1Data` | `—` | `timeSeg1` | `PositiveInteger` | — | naming |
| `timeSeg2Data` | `—` | `timeSeg2` | `PositiveInteger` | — | naming |
| — *(missing)* | `—` | `trcvPwmModeEnabled` | `Boolean` | — | missing |

## `CanControllerXlConfigurationRequirements`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 71
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `errorSignalingEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `maxPwmL` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `maxPwmO` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `maxPwmS` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `minPwmL` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `minPwmO` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `minPwmS` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `trcvPwmModeEnabled` | `Boolean` | — | missing |

## `FlexrayCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 80
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `flexrayClusterVariant` | `FlexrayClusterConditional` | — | missing |

## `FlexrayCommunicationController`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 86
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py`

No deviations — Table 3.30 has no variant-attribute rows; the `flexrayCommunicationControllerVariant` missing row is removed because the `<<atpVariation>>` wrapper (`FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS`/`FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL`) is read/written transparently into the owning object per the cluster-class precedent (LinCluster, Table 3.36).

## `LinCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 93
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py`

No deviations — Table 3.36 has no `Attribute` rows (all members inherited from `CommunicationCluster`); the `<<atpVariation>>` wrapper (`LIN-CLUSTER-VARIANTS`/`LIN-CLUSTER-CONDITIONAL`) is read/written transparently into the owning object per the cluster-class precedent, so the earlier `linClusterVariant` missing row is removed. The class now lives in its spec package module (`Fibex4Lin/LinTopology.py`).

## `LinMaster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 94
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `linMasterVariant` | `LinMasterConditional` | — | missing |

## `EthernetCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 103
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ethernetClusterVariant` | `EthernetClusterConditional` | — | missing |

## `CouplingPort`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 109
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `couplingPortSpeed` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `vlanModifierRef` | `Ref (EthernetPhysicalChannel)` | Ref | missing |

## `EthernetCommunicationController`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 115
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ethernetCommunicationControllerVariant` | `EthernetCommunicationControllerConditional` | — | missing |

## `EthernetCommunicationConnector`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 117
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `apApplicationEndpoint` | `Ref (CanXlProps)` | — | missing |
| — *(missing)* | `—` | `canXlPropsRefs` | `Ref (CanXlProps)` | Refs | missing |
| — *(missing)* | `—` | `ipV6PathMtuEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `ipV6PathMtuTimeout` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `pncFilterDataMask` | `PositiveUnlimitedInteger` | — | missing |
| — *(missing)* | `—` | `unicastNetworkEndpointRefs` | `Ref (NetworkEndpoint)` | Refs | missing |

## `CouplingPortDetails`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 121
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `ethernetPriorityRegenerations` | `List[EthernetPriorityRegeneration]` | `ethernetPriorityRegeneration` | `Ref (?)` | — | type (spec one vs py list) |
| `ethernetTrafficClassAssignments` | `List[CouplingPortTrafficClassAssignment]` | `ethernetTrafficClassAssignment` | `Ref (CouplingPortScheduler)` | — | type (spec one vs py list) |

## `CouplingPortFifo`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 124
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `assignedTrafficClass` | `—` | `assignedTrafficClass` | `PositiveInteger` | — | type (spec one vs py list) |

## `SwcToEcuMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 197
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::SWmapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/__init__.py`

No deviations — all 4 Table 5.2 attributes modeled with full reader/writer coverage (`component` `*` iref → `componentIRefs: List[ComponentInSystemInstanceRef]` per the "InstanceRef implemented by" row, `controlledHwElement`/`ecuInstance`/`processingUnit` 0..1 ref → `Optional[RefType]` per the Kind `ref`→`Ref` suffix); XSD-only `PARTITION-REF` (atp.Status="removed", replaced by SwcToApplicationPartitionMapping/ApplicationPartitionToEcuPartitionMapping) not modeled (Rule 0015; no fixture carries it) — the former v1 `partitionRef` missing row resolved to removed in the 2026-09 sync; writer helper renamed `setSwcToEcuMapping` → `writeSwcToEcuMapping` (Rule 0013.2 matched readXxx/writeXxx pair, resolved in-pass) and the dropped CONTROLLED-HW-ELEMENT-REF/PROCESSING-UNIT-REF elements restored on both sides.

## `SenderRecArrayTypeMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 235
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DataMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `senderToSignalTextTableMapping` | `TextTableMapping` | — | missing |

## `ComManagementMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 282
- **Package:** `M2::AUTOSARTemplates::SystemTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `physicalChannelRef` | `—` | `physicalChannelRefs` | `Ref (PhysicalChannel)` | Refs | type (spec many vs py single) |

## `ContainedIPduProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 356
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py`

No deviations — all 9 Table 6.39 attributes modeled (`collectionSemantics`, `containedPduTriggeringRef` `Ref (PduTriggering)` per the Kind `ref`→`Ref` suffix, `headerIdLongHeader`, `headerIdShortHeader`, `offset`, `priority`, `timeout` `TimeValue`, `trigger`, `updateIndicationBitPosition`); former `missing` rows for `containedPduTriggeringRef`/`priority` resolved in the 2026-09 sync (members implemented with full reader/writer coverage); enum member types `ContainedIPduCollectionSemanticsEnum` (Table 6.40) and `PduCollectionTriggerEnum` (Table 6.41) implemented in the same pass.

## `SecureCommunicationProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 369
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `authAlgorithm` | `String` | — | missing |
| — *(missing)* | `—` | `freshnessCounterSyncAttempts` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `freshnessTimestampTimePeriodFactor` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `useFreshnessTimestamp` | `Boolean` | — | missing |

## `SecureCommunicationFreshnessProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 370
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `freshnessCounterSyncAttempts` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `freshnessTimestampTimePeriodFactor` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `useFreshnessTimestamp` | `Boolean` | — | missing |

## `SecureCommunicationPropsSet`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 370
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `authenticationProps` | `SecureCommunicationAuthenticationProps` | — | missing |
| — *(missing)* | `—` | `freshnessProps` | `SecureCommunicationFreshnessProps` | — | missing |

## `SecureCommunicationAuthenticationProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 371
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `authAlgorithm` | `String` | — | missing |
| — *(missing)* | `—` | `authInfoTxLength` | `PositiveInteger` | — | missing |

## `ModeDrivenTransmissionModeCondition`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 393
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/Timing.py`

No deviations — the single Table 6.61 attribute `modeDeclaration` (Mult `*`, Kind `ref`) modeled as `modeDeclarationRefs: List[RefType]` with `getModeDeclarationRefs`/`addModeDeclarationRef` per the Kind `ref`→`Refs` suffix and singular-spec-`*`→plural rule; former `type (spec many vs py single)` row for `modeDeclarationRef` resolved in the 2026-09 sync (list shape + full reader/writer coverage via `readModeDrivenTransmissionModeCondition`/`writeModeDrivenTransmissionModeCondition` and TransmissionModeDeclaration dispatch).

## `MacMulticastGroup`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 104  | **table:** Table 3.48
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

No deviations — the single Table 3.48 attribute `macMulticastAddress` (`MacAddressString 0..1`, Kind `attr`) is modeled as `macMulticastAddress: Optional[MacAddressString]` with `getMacMulticastAddress`/`setMacMulticastAddress` (scalar pair, getter-first per Rule 0001.11). Base `ARObject , Identifiable , MultilanguageReferrable , Referrable` ⇒ most-derived Python base `Identifiable`, `__init__(self, parent, short_name)`. Reader fixed 2026-10-03 (G16-3): the reader previously materialized the generic `ARLiteral` via `getChildElementOptionalLiteral`; it now constructs the declared `MacAddressString` (Rule 0013.2) — the writer keeps `setChildElementOptionalLiteral`, which accepts `ARLiteral` subclasses.

## `MultiplexedIPdu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 408
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `dynamicPart` | `DynamicPart` | `dynamicPart` | `DynamicPart` | — | type (spec many vs py single) |
| `staticPart` | `StaticPart` | `staticPart` | `StaticPart` | — | type (spec many vs py single) |

## `LinConfigurationEntry`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 434
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `assignedControllerRef` | `Ref (LinSlave)` | Ref | missing |
| — *(missing)* | `—` | `assignedLinSlaveConfigRef` | `Ref (LinSlaveConfigIdent)` | Ref | missing |

## `SoAdConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 451
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `logicAddress` | `LogicAddress` | — | missing |

## `SocketAddress`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 452
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `applicationEndpoint` | `—` | `applicationEndpoint` | `ApplicationEndpoint` | — | type (spec one vs py list) |
| — *(missing)* | `—` | `ipAddress` | `String` | — | missing |

## `ApplicationEndpoint`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 457
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `discoveryTechnology` | `DiscoveryTechnology` | — | missing |
| — *(missing)* | `—` | `remotingTechnology` | `RemotingTechnology` | — | missing |
| — *(missing)* | `—` | `serializationTechnologyRef` | `Ref (SerializationTechnology)` | Ref | missing |

## `Ipv6Configuration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 466
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `dnsServerAddresses` | `—` | `dnsServerAddress` | `Ip6AddressString` | — | naming |

## `InfrastructureServices`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 469
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dhcpServerConfiguration` | `DhcpServerConfiguration` | — | missing |

## `AbstractServiceInstance`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 476
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `methodActivationRoutingGroup` | `PduActivationRoutingGroup` | `methodActivationRoutingGroup` | `Ref (SoAdRoutingGroup)` | — | type (spec many vs py single) |
| `methodActivationRoutingGroup` | `PduActivationRoutingGroup` | `routingGroupRefs` | `Ref (SoAdRoutingGroup)` | Refs | type (spec many vs py single) |

## `EventHandler`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 492
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `eventGroupIdentifier` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `eventMulticastAddress` | `ApplicationEndpointRefConditional` | — | missing |
| — *(missing)* | `—` | `pduActivationRoutingGroup` | `Ref (SoAdRoutingGroup)` | — | missing |
| — *(missing)* | `—` | `sdServerEgTimingConfig` | `SomeipSdServerEventGroupTimingConfigRefConditional` | — | missing |

## `DoIpLogicTesterAddressProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 556
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DoIP`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `doIpTesterRoutingActivationRef` | `—` | `doIpTesterRoutingActivationRefs` | `Ref (DoIpRoutingActivation)` | Refs | type (spec many vs py single) |

## `TlsCryptoServiceMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 559
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `keyExchangeRef` | `—` | `keyExchangeRefs` | `Ref (CryptoServicePrimitive)` | Refs | type (spec many vs py single) |

## `StateDependentFirewall`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 583
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/StateDependentFirewall.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `defaultAction` | `FirewallActionEnum` | — | missing |
| `firewallRule` | `—` | `firewallRuleProps` | `Ref (?)` | — | naming |
| — *(missing)* | `—` | `firewallState` | `Ref (ModeDeclaration)` | — | missing |
| — *(missing)* | `—` | `firewallStateModeDeclarationRefs` | `Ref (ModeDeclaration)` | Refs | missing |

## `FirewallRule`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 584
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRule.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bucketSize` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `ddsRule` | `DdsRule` | — | missing |
| — *(missing)* | `—` | `networkLayerRule` | `Ipv4Rule` | — | missing |
| — *(missing)* | `—` | `refillAmount` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `transportLayerRule` | `TcpRule` | — | missing |

## `FirewallRuleProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 584
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRuleProps.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `action` | `FirewallActionEnum` | — | missing |
| — *(missing)* | `—` | `matchingEgressRuleRefs` | `Ref (FirewallRule)` | Refs | missing |
| — *(missing)* | `—` | `matchingIngressRuleRefs` | `Ref (FirewallRule)` | Refs | missing |
| — *(missing)* | `—` | `matchingRuleRefs` | `Ref (FirewallRule)` | Refs | missing |

## `CanTpConnection`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 608
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::TransportProtocols`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `transmitCancellation` | `Boolean` | — | missing |

## `LinTpConnection`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 616
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::TransportProtocols`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dropNotRequestedNad` | `Boolean` | — | deprecated (atp.Status=removed), not implemented |
| — *(missing)* | `—` | `maxNumberOfRespPendingFrames` | `PositiveInteger` | — | deprecated (atp.Status=removed), not implemented |
| — *(missing)* | `—` | `p2Max` | `TimeValue` | — | deprecated (atp.Status=removed), not implemented |
| — *(missing)* | `—` | `p2Timing` | `TimeValue` | — | deprecated (atp.Status=removed), not implemented |

Resolved at the Table 6.261 sync (R23-11): the four "missing" rows were stale — all four elements carry `atp.Status="removed"` in the XSD (superseded by LinTpNode.dropNotRequestedNad or moved to LinTpNode p2Max/p2Timing/maxNumberOfRespPendingFrames), are absent from the R23-11 attribute column, and no integration fixture carries them (Rule 0019 condition 3 fails; Rule 0015). The former reader/writer gaps (MULTICAST-REF and VARIATION-POINT dropped on both sides) were fixed in the same pass; all nine Table 6.261 attributes now round-trip with full reader/writer coverage. Sibling note: the stamped CanTpConnection reader/writer has the same VARIATION-POINT gap (CAN-TP-CONNECTION is an XSD anchor) — to reconcile in a drift pass.

## `NmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 672
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `pncClusterVectorLength` | `PositiveInteger` | — | missing |

## `NmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 674
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `nmCoordinator` | `Optional[ARObject]` | `nmCoordinator` | `NmCoordinator` | aggr | placeholder — aggregated child class `NmCoordinator` (Table 6.302) not yet implemented; reader/writer coverage deferred (Rule 0001.10 / 0001.7). Stale 2026-09-23 rows (busSpecificNmEcu, nmMultipleChannelsEnabled, nmPassiveModeEnabled) removed at the Table 6.300 sync — none is an R23-11 NmEcu attribute. |

## `NmNode`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 675
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `machineRef` | `Ref (MachineDesign)` | Ref | missing |

## `FlexrayNmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 678
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmCarWakeUpBitPosition` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `nmCarWakeUpFilterEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmCarWakeUpFilterNodeId` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `nmCarWakeUpRxEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmControlBitVectorActive` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmDataCycle` | `Integer` | — | missing |
| — *(missing)* | `—` | `nmDataEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmDetectionLock` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `nmMainFunctionPeriod` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `nmMessageTimeoutTime` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `nmReadySleepCount` | `Integer` | — | missing |
| — *(missing)* | `—` | `nmRemoteSleepIndicationTime` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `nmRepeatMessageBitActive` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmRepeatMessageTime` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `nmRepetitionCycle` | `Integer` | — | missing |
| — *(missing)* | `—` | `nmVotingCycle` | `Integer` | — | missing |

## `FlexrayNmClusterCoupling`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 679
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(removed)* | — | `nmControlBitVectorEnabled` | `Boolean` | — | stale row removed at Table 6.308 sync — XSD-only (FLEXRAY-NM-CLUSTER-COUPLING/NM-CONTROL-BIT-VECTOR-ENABLED), absent from R23-11 Table 6.308; PDF authoritative (Rule 0015) |
| — *(removed)* | — | `nmDataDisabled` | `Boolean` | — | stale row removed at Table 6.308 sync — XSD-only (FLEXRAY-NM-CLUSTER-COUPLING/NM-DATA-DISABLED), absent from R23-11 Table 6.308; PDF authoritative (Rule 0015) |

## `FlexrayNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 679
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmHwVoteEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmMainFunctionAcrossFrCycle` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmRepeatMessageBitEnable` | `Boolean` | — | missing |

## `FlexrayNmNode`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 679
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmInstanceId` | `PositiveInteger` | — | missing |

## `CanNmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 682
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(removed)* | — | `nmCarWakeUpFilterEnabled` | `Boolean` | — | stale row removed at Table 6.311 sync — not a CanNmCluster attribute in any verified corpus (owner in R23-11: CanNmNode Table 6.314); XSD-only NM-CAR-WAKE-UP-FILTER-ENABLED not modeled (Rule 0015) |
| — *(removed)* | — | `nmCarWakeUpRxEnabled` / `nmChannelActive` / `nmUserDataLength` | `Boolean` / `Boolean` / `Integer` | — | XSD-only elements (CAN-NM-CLUSTER group, AUTOSAR_00052.xsd), absent from R23-11 Table 6.311 and from the R4.3.1 Table 6.232 rendering; fields + parser/writer elements removed at sync (Rule 0015); no fixture carries the tags |

## `CanNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 683
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmRepeatMsgIndicationEnabled` | `Boolean` | — | missing |

## `CanNmNode`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 684
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(removed)* | — | `canXlNmProps` | `CanXlNmNodeProps` | aggr | stale row removed at Table 6.314 sync — AP-only XSD element (CAN-XL-NM-PROPS, RestrictToStandards="AP", CAN-NM-NODE group, AUTOSAR_00052.xsd), absent from R23-11 Table 6.314; PDF authoritative (Rule 0015); not modeled |
| — *(removed)* | — | `nmRangeConfig` | `CanNmRangeConfig` | aggr | XSD-only element with atp.Status="removed" (CAN-NM-NODE group, AUTOSAR_00052.xsd), absent from R23-11 Table 6.314 AND R4.3.1 Table 6.235; no fixture carries NM-RANGE-CONFIG so Rule 0019 merge condition 3 fails — fabricated field (was typed `RxIdentifierRange`, mismatching the XSD `CAN-NM-RANGE-CONFIG` shape) + parser/writer element removed at sync (Rule 0015 / Rule 0001.3 deprecated atp.Status="removed") |

## `UdpNmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 687
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(removed)* | — | `networkConfiguration` / `nmUserDataLength` / `nmUserDataOffset` | `UdpNmNetworkConfiguration` / `Integer` / `PositiveInteger` | — | stale rows removed at Table 6.315 sync — XSD-only elements (UDP-NM-CLUSTER group, AUTOSAR_00052.xsd), absent from R23-11 Table 6.315; PDF authoritative (Rule 0015); no fixture carries the tags |
| — *(removed)* | — | `nmChannelActive` | `Boolean` | — | XSD-only element present in R4.3.1 Table 6.237 but removed in R23-11 Table 6.315; no fixture carries NM-CHANNEL-ACTIVE so Rule 0019 merge condition 3 fails — field + parser/writer element removed at sync (Rule 0015) |

## `UdpNmClusterCoupling`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 688
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(removed)* | — | `nmBusLoadReductionEnabled` | `Boolean` | — | stale row removed at Table 6.317 sync — XSD-only (UDP-NM-CLUSTER-COUPLING/NM-BUS-LOAD-REDUCTION-ENABLED), absent from R23-11 Table 6.317; PDF authoritative (Rule 0015) |

## `UdpNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 688
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmRepeatMsgIndicationEnabled` | `Boolean` | — | missing |

## `UdpNmNode`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 689
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(removed)* | — | `communicationConnector` | `Ref (EthernetCommunicationConnector)` | ref | stale row removed at Table 6.318 sync — AP-only XSD element (COMMUNICATION-CONNECTOR-REF, RestrictToStandards="AP", UDP-NM-NODE group, AUTOSAR_00052.xsd), absent from R23-11 Table 6.318; PDF authoritative (Rule 0015); not modeled |
| — *(removed)* | — | `nmPnHandleMultipleNetworkRequests` | `Boolean` | attr | stale row removed at Table 6.318 sync — AP-only XSD element (NM-PN-HANDLE-MULTIPLE-NETWORK-REQUESTS, RestrictToStandards="AP", UDP-NM-NODE group, AUTOSAR_00052.xsd), absent from R23-11 Table 6.318; PDF authoritative (Rule 0015); not modeled |

## `J1939NmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 691
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `addressClaimEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `usesDynamicAddressing` | `Boolean` | — | missing |

## `SignalServiceTranslationPropsSet`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 730
- **Package:** `M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationPropsSet.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `signalServiceTranslationProps` | `SignalServiceTranslationProps` | — | missing |

## `SignalServiceTranslationEventProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 731
- **Package:** `M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationEventProps.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `elementProps` | `Ref (?)` | — | missing |
| — *(missing)* | `—` | `safeTranslation` | `Boolean` | — | missing |
| — *(missing)* | `—` | `secureTranslation` | `Boolean` | — | missing |
| — *(missing)* | `—` | `serviceElementMappingRefs` | `Ref (AbstractSignalBasedToISignalTriggeringMapping)` | Refs | missing |
| — *(missing)* | `—` | `translationTargetIRef` | `VariableDataPrototypeInSystemInstanceRef` | IRef | missing |

## `SignalServiceTranslationElementProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 735
- **Package:** `M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationElementProps.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `filter` | `DataFilter` | — | missing |
| — *(missing)* | `—` | `transmissionTrigger` | `Boolean` | — | missing |

## `EndToEndTransformationISignalProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 809
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

No deviations — every Table 7.27 attribute (dataId `*` ordered, dataLength, maxDataLength, minDataLength, sourceId — all PositiveInteger) is modeled with typed fields, accessors and full reader/writer coverage through the VARIANTS/CONDITIONAL split wrapper. The stale `missing endToEndTransformationISignalPropsVariant` row is removed: the member is absent from the Table 7.27 Attribute column (XSD-only variation-split artifact of the `<<atpVariation>>` class stereotype, Rule 0015 — not modeled as a field); the END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/...-CONDITIONAL wrapper is read/written transparently into the owning object with no separate Conditional model (Rule 0001.7). Page corrected 808 → 809 (pdf_page.py caption page).

## `IPduMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 840
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `pduMaxLength` | `PositiveInteger` | — | missing |

## `RtePluginProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 971
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `associatedCrossSwClusterComRtePluginRef` | `Ref (EcucContainerValue)` | Ref | missing |
| — *(missing)* | `—` | `associatedRtePluginRef` | `Ref (EcucContainerValue)` | Ref | missing |

## `SocketConnection`
- **PDF:** `AUTOSAR_TPS_SystemTemplate.pdf` (R4.3.1) | **page:** 319 (Table 6.120)
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Ethernet Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `runtimePortConfiguration` | `Optional[RuntimeAddressConfigurationEnum]` | `runtimePortConfiguration` | `RuntimeAddressConfigurationEnum` | attr | - (conforms R4.3.1 Table 6.120; enum per Table 6.121) |
| `shortLabel` | `Optional[Identifier]` | `shortLabel` | `Identifier` | attr | - (conforms R4.3.1 Table 6.120) |

Base stays `Describable` per R4.3.1 Table 6.120 (DESCRIBABLE). The prior 19-member XSD-derived shape (incl. SoAdConnectorType/SoAdProtocolType `ARLiteral` placeholders) was dropped 2026-08-29 per Rule 0015 (PDF/markdown table wins, no fabrication).

## `SwcTiming`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 25
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingExtensions.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `behaviorRef` | `Ref (SwcInternalBehavior)` | Ref | missing |
| — *(missing)* | `—` | `componentRef` | `Ref (SwComponentType)` | Ref | missing |

## `TimingCondition`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 35
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingCondition.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingConditionFormula` | `TimingConditionFormula` | — | missing |

## `TimingConditionFormula`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 35
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingConditionFormula.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingArgumentRef` | `Ref (AutosarOperationArgumentInstance)` | Ref | missing |
| — *(missing)* | `—` | `timingConditionRef` | `Ref (TimingCondition)` | Ref | missing |
| — *(missing)* | `—` | `timingEventRef` | `Ref (TimingDescriptionEvent)` | Ref | missing |
| — *(missing)* | `—` | `timingModeRef` | `Ref (TimingModeInstance)` | Ref | missing |
| — *(missing)* | `—` | `timingVariableRef` | `Ref (AutosarVariableInstance)` | Ref | missing |

## `TimingExtensionResource`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 35
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingExtensionResource.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingArgument` | `AutosarOperationArgumentInstance` | — | missing |
| — *(missing)* | `—` | `timingMode` | `TimingModeInstance` | — | missing |
| — *(missing)* | `—` | `timingVariable` | `AutosarVariableInstance` | — | missing |

## `TimingModeInstance`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 37
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingModeInstance.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `modeInstance` | `ModeInBswInstanceRef` | — | missing |

## `ModeInBswInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 38
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInBswInstanceRef.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextBswImplementationRef` | `Ref (BswImplementation)` | Ref | missing |
| — *(missing)* | `—` | `contextModeDeclarationGroupPrototypeRef` | `Ref (ModeDeclarationGroupPrototype)` | Ref | missing |
| — *(missing)* | `—` | `targetModeDeclarationRef` | `Ref (ModeDeclaration)` | Ref | missing |

## `ModeInSwcInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 39 (Table 3.12)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition.py`

**Note:** Synced 2026-09-24 against R23-11 CP_TPS_TimingExtensions Table 3.12 (p.39 — the section below previously cited p.38, which is Table 3.11's page; R4.3.1 reproduction AUTOSAR_TPS_TimingExtensions Table 4.6 is row-identical, its Mults being the pre-fix 1s on base/contextModeDeclarationGroupPrototype/contextPort). The four "missing" rows below were outdated even when written — all members have been implemented since intake, and `base` was never listed. Deviations found and fixed during the sync — no open rows remain: the class docstring carried the Table 3.12 Note verbatim plus the four section-level constraint paragraphs ([constr_6855]/[constr_6856]/[constr_6857]/[constr_6899]) and a fabricated "The Python bases ... jointly stand in for the abstract spec base ModeInSwcBswInstanceRef." sentence, and the member docstrings/inline comments carried [constr_*] tails plus the base row's "Stereotypes: atpDerived" cell suffix — all wiped and rewritten to the Note prose verbatim (constraint paragraphs live in the section-level constraints table, not the Note rows — SynchronizationTimingConstraint Table 3.54 precedent; in-cell Stereotypes/Tags suffixes kept out of member docstrings per the batch VariationPoint Table 7.4 convention). `Base: ARObject, AtpInstanceRef, ModeInSwcBswInstanceRef` (XSD 00052 complexType MODE-IN-SWC-INSTANCE-REF L82755 abstract="false" composes AR-OBJECT → ATP-INSTANCE-REF → MODE-IN-SWC-BSW-INSTANCE-REF → own group; Python bases `(AtpInstanceRef, ModeInSwcBswInstanceRef)` conform, AtpInstanceRef's atpBaseRef/atpContextElementRefs/atpTargetRef stay INHERITED members of the stamped base — no flattening; aggregated by TimingModeInstance.modeInstance). The own XSD group (L82692) opens with `<!-- Association <<atpDerived>>base skipped -->` — `base` has NO XML element (field kept per the PDF table, Rule 0015 PDF-wins; reader/writer `[—]` genuine) — and orders CONTEXT-COMPONENT-REF → CONTEXT-PORT-REF → CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF → TARGET-MODE-DECLARATION-REF (seqOffset 20/30/40/50, DEST SW-COMPONENT-PROTOTYPE/PORT-PROTOTYPE/MODE-DECLARATION-GROUP-PROTOTYPE/MODE-DECLARATION --SUBTYPES-ENUM); the markdown displayed row order (base, contextComponent, contextModeDeclarationGroupPrototype, contextPort, targetModeDeclaration) governs the class member order (Rule 0001.11), the XSD sequence governs the reader/writer element order (writer order now test-pinned). Consume path: parser `readModeInSwcInstanceRef` + writer `writeModeInSwcInstanceRef` pre-existed and cover all four XSD elements via the TimingModeInstance.modeInstance dispatch (tag branch / isinstance branch). Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All five Table 3.12 attributes implemented spec-named: `base` (SwComponentType, 0..1, ref, atpDerived → `baseRef` Optional[RefType] + get/setBaseRef; XSD-skipped association, no XML element), `contextComponent` (SwComponentPrototype, *, ref → `contextComponentRefs` List[RefType] singular-`*`-plural + getContextComponentRefs/addContextComponentRef), `contextModeDeclarationGroupPrototype` (ModeDeclarationGroupPrototype, 0..1, ref → `contextModeDeclarationGroupPrototypeRef` + get/set), `contextPort` (PortPrototype, 0..1, ref → `contextPortRef` + get/set), `targetModeDeclaration` (ModeDeclaration, 0..1, ref → `targetModeDeclarationRef` + get/set); docstrings verbatim from the table Notes (no Stereotypes/Tags/constr suffixes); reader + writer cover the four XSD-present elements in XSD order; no iref-kind member (all rows Kind=ref — the OperationArgumentInComponentInstanceRef IRef precedent does not apply). Stamp deferred to batch confirmation. |

## `SynchronizationTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 92 (Table 3.54)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py`

**Note:** Synced 2026-09-24 against R23-11 CP_TPS_TimingExtensions Table 3.54 (p.92; R4.3.1 reproduction AUTOSAR_TPS_TimingExtensions Table 7.12 carries row-identical content — caption-shift artifact: the table body renders ABOVE its caption; PDF-extraction spacing artifacts only). The five "missing" rows below were outdated even when written — all members have been implemented since intake. Deviations found and fixed during the sync — no open rows remain: the class docstring carried the Table 3.54 Note verbatim plus three extraneous `[constr_4522/4514/4521]` paragraphs (those constraints live in the section-level constraints table, not the Note row — and `[constr_4513]` was already missing, evidence of a partial intake artifact) and dropped the Note's tail "interval are permitted." (cut mid-sentence by an inline image in the markdown; confirmed by the XSD group documentation and the R4.3.1 Note) — wiped and rewritten to the Table 3.54 Note verbatim; `getScopeEvents` carried a trailing "." and `addScopeEvent` an inserted "." before the None-no-op sentence (the `scopeEvent` Note ends WITHOUT a period in the markdown) — normalized verbatim; the pre-existing 5-column checklist with a stale `# Spec verified: R23-11` stamp was rebuilt 6-column with release R23-11 and the stamp withheld — deferred to batch confirmation. `Base: TimingConstraint` (most-derived per the table row header; XSD 00052 complexType SYNCHRONIZATION-TIMING-CONSTRAINT L118962 abstract="false" composes AR-OBJECT → REFERRABLE → MULTILANGUAGE-REFERRABLE → IDENTIFIABLE → TRACEABLE → TIMING-CONSTRAINT → own group — no flattening; aggregated by TimingExtension.timingGuarantee/timingRequirement). The own XSD group (L118881) orders EVENT-OCCURRENCE-KIND → SCOPE-EVENT-REFS → SCOPE-REFS → SYNCHRONIZATION-CONSTRAINT-TYPE → TOLERANCE (SCOPE-EVENT-REF DEST TIMING-DESCRIPTION-EVENT--SUBTYPES-ENUM required, SCOPE-REF DEST TIMING-DESCRIPTION-EVENT-CHAIN--SUBTYPES-ENUM required) — the markdown displayed order (eventOccurrenceKind, scope, scopeEvent, synchronizationConstraintType, tolerance) governs the class member order (Rule 0001.11), the XSD sequence governs the reader/writer element order (both already conform). Consume-path disposition: the TimingExtension dispatch pre-exists on both sides (parser `readTimingExtensionConstraint` SYNCHRONIZATION-TIMING-CONSTRAINT branch, writer `writeTimingConstraintItem` tag map) with own helpers `readSynchronizationTimingConstraint`/`writeSynchronizationTimingConstraint` — now test-pinned at element level AND through the TimingExtension aggregation round-trip (guarantees + requirements wrapper lists). Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All five Table 3.54 attributes implemented spec-named: `eventOccurrenceKind` (EventOccurrenceKindEnum, 0..1, attr → Optional[EventOccurrenceKindEnum] + get/setEventOccurrenceKind), `scope` (TimingDescriptionEventChain, *, ref → `scopeRefs` List[RefType] Kind-`*`-ref plural suffix + add/getScopes), `scopeEvent` (TimingDescriptionEvent, *, ref → `scopeEventRefs` List[RefType] + add/addScopeEvent·getScopeEvents), `synchronizationConstraintType` (SynchronizationTypeEnum, 0..1, attr → Optional[SynchronizationTypeEnum] + get/setSynchronizationConstraintType), `tolerance` (MultidimensionalTime, 0..1, aggr → Optional[MultidimensionalTime] + get/setTolerance); Base TimingConstraint (stamped R23-11 Table D.61) concrete subclass per the table header; docstrings verbatim from the table Notes; reader `readSynchronizationTimingConstraint` + writer `writeSynchronizationTimingConstraint` cover all five attributes via the pre-existing TimingExtension dispatch (TimingExtension.timingGuarantee/timingRequirement). Stamp deferred to batch confirmation. |

## `LatencyTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 95
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `latencyConstraintType` | `LatencyConstraintTypeEnum` | — | missing |
| — *(missing)* | `—` | `maximum` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `minimum` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `nominal` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `scopeRef` | `Ref (TimingDescriptionEventChain)` | Ref | missing |

## `EventTriggeringConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 100
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `eventRef` | `Ref (TimingDescriptionEvent)` | Ref | missing |

## `PeriodicEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 101
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `jitter` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `minimumInterArrivalTime` | `MultidimensionalTime` | — | missing |

## `SporadicEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 105
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `jitter` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `maximumInterArrivalTime` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `minimumInterArrivalTime` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `period` | `MultidimensionalTime` | — | missing |

## `ConcretePatternEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 106
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `offset` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `patternJitter` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `patternLength` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `patternPeriod` | `MultidimensionalTime` | — | missing |

## `BurstPatternEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 109
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maxNumberOfOccurrences` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `minNumberOfOccurrences` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `minimumInterArrivalTime` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `patternJitter` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `patternLength` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `patternPeriod` | `MultidimensionalTime` | — | missing |

## `ArbitraryEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 111
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `confidenceInterval` | `ConfidenceInterval` | — | missing |
| — *(missing)* | `—` | `maximumDistance` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `minimumDistance` | `MultidimensionalTime` | — | missing |

## `ConfidenceInterval`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 112
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `lowerBound` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `propability` | `Float` | — | missing |
| — *(missing)* | `—` | `upperBound` | `MultidimensionalTime` | — | missing |

## `TimingDescriptionEventChain`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 41 (Table 3.13)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/__init__.py`

**Note:** Synced 2026-09-24 against R23-11 CP_TPS_TimingExtensions Table 3.13 (p.41; R4.3.1 reproduction AUTOSAR_TPS_TimingExtensions Table 6.1 is row-identical EXCEPT it predates the draft attribute `isPipeliningPermitted` (atp.Status=draft) and carries no "Aggregated by" row — PDF-extraction spacing artifacts only). This section is new — the v1 intake scan produced NO rows for this class (it was mentioned only as a ref-target type inside other classes' stale rows). Deviations found and fixed during the sync — no open rows remain: the class member/accessor order followed the XSD sequence order (stimulus → response → segment) instead of the Table 3.13 markdown displayed order (isPipeliningPermitted → response → segment → stimulus) — reordered per Rule 0001.11 (the XSD group TIMING-DESCRIPTION-EVENT-CHAIN, L123715, orders IS-PIPELINING-PERMITTED → STIMULUS-REF → RESPONSE-REF → SEGMENT-REFS and continues to govern the reader/writer element order, both already conform); the class docstring carried the XSD ''-quoted italics form of the Note — rewritten to the markdown wording verbatim (the trailing italic-extraction artifact "event chain segments ." — space before the final period, present in both the R23-11 and R4.3.1 markdown — normalized by dropping the artifact space); getter/setter/adder docstrings carried the "Tags: atp.Status=draft"/"Tags: xml.sequenceOffset=10/20/30" tails — dropped per the OffsetTimingConstraint family convention (inline comments keep the tails); the pre-existing 5-column checklist was rebuilt 6-column with release R23-11; no stale `# Spec verified:` stamp was present and none was added — deferred to batch confirmation. `Base: TimingDescription` (most-derived per the table row header; XSD 00052 complexType TIMING-DESCRIPTION-EVENT-CHAIN L123778 abstract="false" composes AR-OBJECT → REFERRABLE → MULTILANGUAGE-REFERRABLE → IDENTIFIABLE → TIMING-DESCRIPTION → own group — no flattening; aggregated by TimingExtension.timingDescription). Consume-path disposition: the TimingExtension TIMING-DESCRIPTIONS dispatch had NO TIMING-DESCRIPTION-EVENT-CHAIN branch on either side (silent round-trip drop) — added to parser `readTimingDescriptions` and writer `writeTimingExtension` this sync; own helpers `readTimingDescriptionEventChain`/`writeTimingDescriptionEventChain` pre-existed in XSD element order — now test-pinned at element level AND through the TimingExtension aggregation round-trip (TIMING-DESCRIPTIONS wrapper list).

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All four Table 3.13 attributes implemented spec-named: `isPipeliningPermitted` (Boolean, 0..1, attr → Optional[Boolean] + get/setIsPipeliningPermitted), `response` (TimingDescriptionEvent, 0..1, ref → `responseRef` RefType Kind-ref suffix), `segment` (TimingDescriptionEventChain, *, ref → `segmentRefs` List[RefType] Kind-`*`-ref plural suffix + addSegmentRef/getSegmentRefs), `stimulus` (TimingDescriptionEvent, 0..1, ref → `stimulusRef` RefType Kind-ref suffix); Base TimingDescription (stamped R23-11 Table D.62) concrete subclass per the table header; docstrings verbatim from the table Notes; reader `readTimingDescriptionEventChain` + writer `writeTimingDescriptionEventChain` cover all four attributes via the TIMING-DESCRIPTIONS dispatch added this sync (TimingExtension.timingDescription). Stamp deferred to batch confirmation. |

## `OffsetTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 114 (Table 3.66)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::OffsetConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/OffsetConstraint.py`

**Note:** Synced 2026-09-24 against R23-11 CP_TPS_TimingExtensions Table 3.66 (p.114; R4.3.1 reproduction AUTOSAR_TPS_TimingExtensions Table 7.15 carries row-identical content — PDF-extraction spacing artifacts only). The four "missing" rows below were outdated even when written — all members have been implemented since intake. Deviations found and fixed during the sync — no open rows remain: the class docstring carried the Table 3.66 Note verbatim plus a stale "(source/target -> TimingDescriptionEvent placeholders, Rule 0001.10)" paragraph and the `sourceRef`/`targetRef` inline comments carried "(TimingDescriptionEvent placeholder, Rule 0001.10)" suffixes — both stale (TimingDescriptionEvent IS modeled, abstract, and stamped `# Spec verified: R23-11` Table D.63; refs are plain `RefType` values with DEST `TIMING-DESCRIPTION-EVENT`, no placeholder class is involved) — wiped and rewritten to the Table 3.66 Notes verbatim (getters drop the Tags suffix, setters append the None-no-op sentence, inline comments keep the "Tags: xml.sequenceOffset=10/20" tails per the LatencyTimingConstraint family style); the pre-existing 5-column checklist with a stale `# Spec verified: R23-11` stamp was rebuilt 6-column with release R23-11 and the stamp withheld — deferred to batch confirmation. `Base: TimingConstraint` (most-derived per the table row header; XSD 00052 complexType OFFSET-TIMING-CONSTRAINT L86877 abstract="false" composes AR-OBJECT → REFERRABLE → MULTILANGUAGE-REFERRABLE → IDENTIFIABLE → TRACEABLE → TIMING-CONSTRAINT → own group — no flattening; aggregated by TimingExtension.timingGuarantee/timingRequirement). The own XSD group (L86823) orders SOURCE-REF → TARGET-REF (both minOccurs="0", AR:REF base, DEST TIMING-DESCRIPTION-EVENT--SUBTYPES-ENUM required) → MINIMUM (MULTIDIMENSIONAL-TIME, xml.sequenceOffset=10) → MAXIMUM (xml.sequenceOffset=20) — the markdown displayed order (maximum, minimum, source, target) governs the class member order (Rule 0001.11), the XSD sequence governs the reader/writer element order (both already conform). Consume-path disposition: the TimingExtension dispatch pre-exists on both sides (parser `readTimingExtensionConstraint` OFFSET-TIMING-CONSTRAINT branch, writer `writeTimingConstraintItem` tag map) with own helpers `readOffsetTimingConstraint`/`writeOffsetTimingConstraint` — now test-pinned at element level AND through the TimingExtension aggregation round-trip (guarantees + requirements wrapper lists). Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All four Table 3.66 attributes implemented spec-named: `maximum` (MultidimensionalTime, 0..1, aggr → Optional[MultidimensionalTime] + get/setMaximum), `minimum` (MultidimensionalTime, 0..1, aggr → Optional[MultidimensionalTime] + get/setMinimum), `source` (TimingDescriptionEvent, 0..1, ref → `sourceRef` RefType Kind-ref suffix), `target` (TimingDescriptionEvent, 0..1, ref → `targetRef` RefType Kind-ref suffix); Base TimingConstraint (stamped R23-11 Table D.61) concrete subclass per the table header; docstrings verbatim from the table Notes; reader `readOffsetTimingConstraint` + writer `writeOffsetTimingConstraint` cover all four attributes via the pre-existing TimingExtension dispatch (TimingExtension.timingGuarantee/timingRequirement). Stamp deferred to batch confirmation. |

## `AutosarOperationArgumentInstance`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 85 (Table 3.53)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventOccurrenceExpression`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventOccurrenceExpression.py`

**Note:** Synced 2026-09-24 against R23-11 CP_TPS_TimingExtensions Table 3.53 (p.85; R4.3.1 reproduction AUTOSAR_TPS_TimingExtensions Table 5.40 is row-identical — PDF-extraction spacing artifacts only, the R4.3.1 render omits the "Aggregated by" row). This section is new — the v1 intake scan produced NO rows for this class (it was mentioned only as a ref-target type inside the stale TimingConditionFormula/TimingExtensionResource rows, which belong to those classes' own syncs). Deviations found and fixed during the sync — no open rows remain: the class docstring carried the markdown's second-bullet wrap artifact "ClientServer Interface" (space inside the class name, absent from the first bullet of the same Note) — normalized to "ClientServerInterface" (XSD 00052 group doc AUTOSAR-OPERATION-ARGUMENT-INSTANCE L8076/L8110 canonicalizes both bullets); the getter/setter docstrings carried a trailing "." not present in the markdown Note cell (which ends "...OperationArgumentIn ComponentInstanceRef" with the same wrap-artifact space) — dropped (the setter appends the None-no-op sentence with no terminal punctuation added, SynchronizationTimingConstraint addScopeEvent family form); the pre-existing 5-column checklist was rebuilt 6-column with release R23-11 and the `__init__` row corrected to [—] reader/[—] writer; no stale `# Spec verified:` stamp was present and none was added — deferred to batch confirmation. `Base: Identifiable` (most-derived per the table row header ARObject , Identifiable , MultilanguageReferrable , Referrable; XSD 00052 complexType AUTOSAR-OPERATION-ARGUMENT-INSTANCE L8100 abstract="false" composes AR-OBJECT → REFERRABLE → MULTILANGUAGE-REFERRABLE → IDENTIFIABLE → own group — no flattening; the `Identifiable, VariationPointCapable` mixin form kept — the XSD own group carries the optional VARIATION-POINT element xml.sequenceOffset=10000, "Applicable for: TimingExtensionResource.timingArgument / Not Applicable for: TDEventOccurrenceExpression.argument", and the stamped sibling AutosarVariableInstance Table 3.52 carries the identical shape). Consume-path disposition: BOTH Aggregated-by paths pre-exist and are wired both sides — TDEventOccurrenceExpression.argument (parser `readTDEventOccurrenceExpression` ARGUMENTS dispatch / writer `writeTDEventOccurrenceExpression` ARGUMENTS dispatch) and TimingExtensionResource.timingArgument (parser `readTimingExtensionResource` TIMING-ARGUMENTS dispatch / writer `writeTimingExtensionResource` TIMING-ARGUMENTS dispatch); own helpers `readAutosarOperationArgumentInstance`/`writeAutosarOperationArgumentInstance` + `readOperationArgumentInComponentInstanceRef`/`writeOperationArgumentInComponentInstanceRef` pre-existed in XSD element order — now test-pinned at element level AND through the ARGUMENTS aggregation round-trip (field values + DESTs + element order). Out-of-scope observations for sibling classes (no rows here): the XSD group OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF (L86902) includes an optional BASE-REF element that the XSD-verified OperationArgumentInComponentInstanceRef class does not model; `writeIdentifiable` would emit VARIATION-POINT before the own-group IREF if a variation point were ever set on this class (latent, family-wide mixin behavior, no-op while variationPoint stays None).

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | The single Table 3.53 attribute implemented spec-named: `operationArgumentInstance` (DataPrototype, 0..1, iref → `operationArgumentInstanceIRef` Optional[OperationArgumentInComponentInstanceRef] Kind-iref IRef suffix per Rule 0001.5; XSD element OPERATION-ARGUMENT-INSTANCE-IREF of type OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF); Base Identifiable + VariationPointCapable mixin per the XSD atpVariation element (see Note); docstrings verbatim from the table Note (wrap artifacts normalized); reader `readAutosarOperationArgumentInstance` + writer `writeAutosarOperationArgumentInstance` cover the attribute via BOTH aggregations (TDEventOccurrenceExpression.argument ARGUMENTS wrapper, TimingExtensionResource.timingArgument TIMING-ARGUMENTS wrapper). Stamp deferred to batch confirmation. |

## `GeneralParameter`
- **Spec:** XSD-only (no own table in repo corpus — both-corpora verified absent 2026-09-27) | AUTOSAR_00052.xsd complexType l.63790, group l.63774 | **Package:** `M2::MSR::Documentation::BlockElements::GerneralParameters` (spec-faithful "Gerneral" typo; R4.3.1 AUTOSAR_00044.xsd l.43692/l.43676)
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/GerneralParameters.py`
- **Synced:** 2026-09-27 (commit a3cf04c73; queued from the ChapterModel member-type closure audit) — Base Identifiable; one member prmChar (PRM-CHAR 0..* aggr, addPrmChar/getPrmChars, no createPrmChar — ARObject child per Rule 0001.6). The XSD-only member family PrmChar/PrmCharContents/PrmCharNumericalValue/PrmCharAbsTol/PrmCharMinTypMax/PrmCharNumericalContents/PrmCharTextualContents is implemented and checklisted within this class's module (Rule 0016.4 stub convention); PRM-CHAR-NUMERICAL-VALUE is GROUP-ONLY in both XSDs (abstract parent — type(self) guard) and cites its group line. Docstrings = XSD documentation verbatim (incl. spec typos "exressed"/"ablolute"/"represnts"). Reader/writer: readGeneralParameter/writeGeneralParameter + readPrmChar/writePrmChar (+AbsTol/MinTypMax pairs) with the choice alternatives inlined per the XSD group refs; no deviation rows open.

## `Prms`
- **Spec:** AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.74, p.339 (R23-11; markdown render loses the meta rows — meta verified against the R4.3.1 reproduction Table 8.75, p.305, row-identical) | **Package:** `M2::MSR::Documentation::BlockElements::GerneralParameters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/GerneralParameters.py`
- **Synced:** 2026-09-27 (commit a3cf04c73) — Base Paginateable (DocumentViewSelectable mixin carries SI/VIEW); label (MultilanguageLongName 0..1) + prm (GeneralParameter 1..*, createPrm factory + addPrm/getPrms). Closes the 2026-09-24 ChapterContent.prms Rule 0001.10 deferral: the parent-side member (prms, seq150, Table 9.60 first attribute row) is now modeled with full reader/writer coverage (readChapterContent/writeChapterContent PRMS branches). R4.3.1 "the the" PDF artifact documented, not copied. No deviation rows open.

## `TDEventVfb`
- **Spec:** `AUTOSAR_CP_TPS_TimingExtensions.pdf` | **page:** 51 (Table 3.14) | **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventVfb` (leaf package named after the class; R4.3.1 reproduction Table 5.2 p.50)
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventVfb.py`

**Note:** Re-synced 2026-09-27 (Rule 0012.3 drift pass, user-directed). The class is spec-stamped R23-11 (Table 3.14: abstract, Base ARObject/Identifiable/MultilanguageReferrable/Referrable/TimingDescription/TimingDescriptionEvent, Aggregated by TimingExtension.timingDescription, one attribute component 0..1 iref → componentIRef: Optional[ComponentInCompositionInstanceRef]). The re-sync retired the fabricated ConcreteTDEventVfb subclass and moved the direct-use form onto TDEventVfb itself: ABC base + TypeError guard dropped (instantiability is now the direct-use contract), field set unchanged (exactly componentIRef — Table 3.14 field-to-spec both directions intact), class docstring stays the Table 3.14 Note verbatim, checklist rebuilt to the 6-column format with the release column and the direct-use disposition note.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(accepted, user-directed 2026-09-27)* | — | — | — | — | Spec Table 3.14 declares the class "(abstract)" and the model formerly raised TypeError on direct instantiation; the meta-model permits the abstract TDEventVfb DIRECTLY (TD-EVENT-VFB value in TD-EVENT-VFB--SUBTYPES-ENUM, AUTOSAR_00052.xsd L122350/L122356; R4.3.1 AUTOSAR_00044.xsd L85995-86005), so per the user decision of 2026-09-27 the class is instantiable and carries the direct-use form itself (former fabricated ConcreteTDEventVfb retired). NOTE: no <TD-EVENT-VFB> element declaration exists in either XSD — serializing a direct-use instance (parser TIMING-DESCRIPTIONS tag branch / writer TDEventVfb isinstance catch-all after all concrete subclasses) is a defensive/legacy-only path. |

## `ConcreteTDEventVfb`
**RETIRED 2026-09-27 (user decision):** the class name was a repo fabrication (no spec table and no XSD complexType/element declaration ever named it) — the direct-use form it modeled is now carried by TDEventVfb ITSELF: the ABC base and the TypeError abstract guard were dropped from TDEventVfb (accepted deviation: spec declares "(abstract)" but the meta-model's TD-EVENT-VFB--SUBTYPES-ENUM permits the abstract class directly as a choice member/DEST), the parser TD-EVENT-VFB dispatch now constructs TDEventVfb, and the writer's TDEventVfb isinstance catch-all (placed AFTER all concrete subclasses) emits the TD-EVENT-VFB tag. See the `## TDEventVfb` section for the live record. The historical sync record below is preserved for provenance.

- **Spec:** XSD-only — `AUTOSAR_00052.xsd` line 122350 (no own table in repo corpus) | **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventVfb`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventVfb.py`

**Note:** Synced 2026-09-24 as an XSD-only class (Rule 0002 XSD-only variant). BOTH-CORPORA VERIFICATION (mandatory before the XSD-only claim): caption `^Table [\w.]+: ConcreteTDEventVfb$` 0 hits in `autosar/R23-11/markdown/` AND `autosar/R4.3.1/markdown/`; tolerant case-insensitive `ConcreteTDEvent` 0 hits in both corpora (spacing-tolerant sweep also 0); all `TDEventVfb` hits are sibling noise — the abstract base (R23-11 Table 3.14, p.51, whose Subclasses row lists only TDEventVfbPort/TDEventVfbReference — ConcreteTDEventVfb is NOT a meta-model subclass in either release) and Base rows of other tables. XSD sweep: `"CONCRETE[A-Z-]*"` over AUTOSAR_00052.xsd AND AUTOSAR_00044.xsd → only CONCRETE / CONCRETE-CLASS-TAILORING / CONCRETE-PATTERN-EVENT-TRIGGERING; no complexType and no element declaration named TD-EVENT-VFB exists in either XSD — only the abstract group. THE grounding that exists: `TD-EVENT-VFB--SUBTYPES-ENUM` (AUTOSAR_00052.xsd L122350, enum value "TD-EVENT-VFB" L122356; byte-identical enum in AUTOSAR_00044.xsd L85995-86005) — the meta-model permits the abstract TDEventVfb DIRECTLY as a choice member/DEST; body = the abstract group TD-EVENT-VFB (00052 L122335: one optional COMPONENT-IREF of type COMPONENT-IN-COMPOSITION-INSTANCE-REF), owned in the model by the stamped base TDEventVfb (`# Spec verified: R23-11`, Table 3.14 p.51). The class is therefore the model of that direct instantiation and carries NO attributes of its own — the intake `pass` body was spec-correct. Deviations found and fixed during the sync — no open rows remain: the intake orphan defined no own `__init__` (inherited the abstract base's) — explicit family-form `__init__(parent, short_name)` chaining to super added (every sibling concrete event class declares one); the intake one-line docstring was replaced with an honest XSD-derivation note (NO spec Note exists anywhere for this class — no table in either corpus, and the XSD group documentation "This is the abstract parent class..." belongs to the BASE and is already its verbatim docstring — so the verbatim-Note contract is n/a and the wording documents the derivation source instead); checklist built fresh in the 6-column format with release R23-11 and the XSD-only `# Spec:` citation form; NO `# Spec verified:` / `# XSD verified:` marker was added — deferred to batch confirmation. `Base: TDEventVfb` (stamped R23-11 Table 3.14; no flattening — the base IS modeled and carries the COMPONENT-IREF attribute). Consume-path disposition: the TimingExtension TIMING-DESCRIPTIONS dispatch had NO branch for the plain <TD-EVENT-VFB> member on EITHER side (parser `readTimingDescriptions` had no "TD-EVENT-VFB" tag branch; writer `writeTimingExtension` isinstance chain had no ConcreteTDEventVfb branch and ended without else — silent drop both ways) — added to both this sync; inherited base helpers `readTDEventVfb`/`writeTDEventVfb` pre-existed in XSD element order (SHORT-NAME → COMPONENT-IREF; iref group CONTEXT-COMPONENT-REF* → TARGET-COMPONENT-REF) — now test-pinned at element level AND through the SwcTiming TIMING-DESCRIPTIONS round-trip AND the full-file VFB-family round-trip. Referenced classes: base TDEventVfb (stamped) + inherited attribute type ComponentInCompositionInstanceRef (modeled, tested) — no missing classes. Out-of-scope observation for sibling classes (no rows here): the same SUBTYPES-ENUM also lists the abstract names "TD-EVENT-VFB-PORT" (L122357) whose port-family members are abstract in the markdown — XSD-permitted-direct-instantiation artifacts of the abstract port level, belonging to those classes' own syncs.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No own table exists in either corpus and the XSD grants the class no own members: the SUBTYPES-ENUM direct instantiation adds nothing to the abstract group body (COMPONENT-IREF stays owned by the base TDEventVfb), so the class declares zero fields (test-pinned via re.findall on the own `__init__` source) and zero own accessors (get/setComponentIRef remain the base's implementations); reader `readTDEventVfb` + writer `writeTDEventVfb` cover the element via the newly added TIMING-DESCRIPTIONS dispatch branches (tag TD-EVENT-VFB / isinstance ConcreteTDEventVfb). Stamp deferred to batch confirmation. |

## `AgeConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 115
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::AgeConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/AgeConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maximum` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `minimum` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `scopeRef` | `Ref (TimingDescriptionEvent)` | Ref | missing |

## `ExecutionOrderConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 118
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `baseCompositionRef` | `Ref (CompositionSwComponentType)` | Ref | missing |
| — *(missing)* | `—` | `executionOrderConstraintType` | `ExecutionOrderConstraintTypeEnum` | — | missing |
| — *(missing)* | `—` | `ignoreOrderAllowed` | `Boolean` | — | missing |
| — *(missing)* | `—` | `isEvent` | `Boolean` | — | missing |
| — *(missing)* | `—` | `orderedElement` | `EocEventRef` | — | missing |
| — *(missing)* | `—` | `permitMultipleReferencesToEE` | `Boolean` | — | missing |

## `EOCExecutableEntityRefAbstract`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 119
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `directSuccessorRefs` | `Ref (EocExecutableEntityRefAbstract)` | Refs | missing |

## `EOCExecutableEntityRefGroup`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 119
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `letDataExchangeParadigm` | `LetDataExchangeParadigmEnum` | — | missing |
| — *(missing)* | `—` | `letIntervalRefs` | `Ref (TimingDescriptionEventChain)` | Refs | missing |
| — *(missing)* | `—` | `maxCycleRepetitions` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `maxCycles` | `Integer` | — | missing |
| — *(missing)* | `—` | `maxSlots` | `Integer` | — | missing |
| — *(missing)* | `—` | `maxSlotsPerCycle` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `nestedElementRefs` | `Ref (EocExecutableEntityRefAbstract)` | Refs | missing |
| — *(missing)* | `—` | `successorRefs` | `Ref (EocExecutableEntityRefAbstract)` | Refs | missing |
| — *(missing)* | `—` | `triggeringEventRef` | `Ref (TimingDescriptionEvent)` | Ref | missing |

## `EOCEventRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 120
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bswModuleInstanceRef` | `Ref (BswImplementation)` | Ref | missing |
| — *(missing)* | `—` | `componentIRef` | `ComponentInCompositionInstanceRef` | IRef | missing |
| — *(missing)* | `—` | `successorRefs` | `Ref (EocExecutableEntityRefAbstract)` | Refs | missing |

## `EOCExecutableEntityRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 120
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bswModuleInstanceRef` | `Ref (BswImplementation)` | Ref | missing |
| — *(missing)* | `—` | `componentIRef` | `ComponentInCompositionInstanceRef` | IRef | missing |
| — *(missing)* | `—` | `executableRef` | `Ref (ExecutableEntity)` | Ref | missing |

## `ExecutionTimeConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 130
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `componentIRef` | `ComponentInCompositionInstanceRef` | IRef | missing |
| — *(missing)* | `—` | `executableRef` | `Ref (ExecutableEntity)` | Ref | missing |
| — *(missing)* | `—` | `executionTimeType` | `ExecutionTimeTypeEnum` | — | missing |
| — *(missing)* | `—` | `maximum` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `minimum` | `MultidimensionalTime` | — | missing |

## `SynchronizationPointConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationPointConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationPointConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `sourceEecRefs` | `Ref (EocExecutableEntityRefGroup)` | Refs | missing |
| — *(missing)* | `—` | `sourceEventRefs` | `Ref (AbstractEvent)` | Refs | missing |
| — *(missing)* | `—` | `targetEecRefs` | `Ref (EocExecutableEntityRefGroup)` | Refs | missing |
| — *(missing)* | `—` | `targetEventRefs` | `Ref (AbstractEvent)` | Refs | missing |

## `TDLETZoneClock`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 252
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TDLETZoneClock.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `accuracyExt` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `accuracyInt` | `MultidimensionalTime` | — | missing |

## `TimingClock`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 252
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClock.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `platformTimeBase` | `GlobalTimeDomainRefConditional` | — | missing |

## `TimingClockSyncAccuracy`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 252
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClockSyncAccuracy.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `lowerRef` | `Ref (TimingClock)` | Ref | missing |
| — *(missing)* | `—` | `upperRef` | `Ref (TimingClock)` | Ref | missing |

## `TimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 253
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingConditionRef` | `Ref (TimingCondition)` | Ref | missing |

## `TimingExtension`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 254
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingExtensions.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingClock` | `TdletZoneClock` | — | missing |
| — *(missing)* | `—` | `timingClockSyncAccuracy` | `TimingClockSyncAccuracy` | — | missing |
| — *(missing)* | `—` | `timingCondition` | `TimingCondition` | — | missing |
| — *(missing)* | `—` | `timingDescription` | `TdEventBswInternalBehavior` | — | missing |
| — *(missing)* | `—` | `timingGuarantee` | `AgeConstraint` | — | missing |
| — *(missing)* | `—` | `timingRequirement` | `AgeConstraint` | — | missing |
| — *(missing)* | `—` | `timingResource` | `TimingExtensionResource` | — | missing |

## `BlueprintMappingSet`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 48
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintMapping.py` (non-leaf file holding both BlueprintMappingSet and BlueprintMapping — path updated 2026-09-24, was the pre-reorg `BlueprintMapping/BlueprintMappingSet.py`)

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the former `missing` row (`blueprintMap` `BlueprintMapping`/`AtpBlueprintMapping` aggr) is implemented as `blueprintMaps: List[AtpBlueprintMapping]` + `addBlueprintMap`/`getBlueprintMaps` with full reader/writer coverage via `readBlueprintMappingSet`/`writeBlueprintMappingSet` polymorphic dispatch (BlueprintMapping, PortInterfaceBlueprintMapping, PortPrototypeBlueprintMapping). |

**Note:** Reconciled 2026-09-24 during the BlueprintMapping alignment pass (batch group6-batch-9b). The `blueprintMap` member is fully covered since the BlueprintMappingSet sync (R23-11 FO_TPS_GenericStructureTemplate Table 3.1, p.48, `# Spec verified: R23-11`); the row above was STALE (pre-dated the implementation) and is superseded by the no-deviation row. BlueprintMapping itself (the concrete mapping element this row's type names) was re-synced the same day against R23-11 FO_TPS_StandardizationTemplate Table C.17, p.163 — the ONLY BlueprintMapping table in R23-11 (no numeric main table; R4.3.1 reproduction Table D.13 identical; the R4.3.1 TR GeneralBlueprintsSupplement L2302 hit is a different class, ClientServerInterfaceToBswModuleEntryBlueprintMapping). Appendix C caption-shift applies: the actual body renders ABOVE the C.17 caption (L4977-4985); the rows under the caption are BlueprintPolicy. XSD 00052 corroboration: group `BLUEPRINT-MAPPING` (L9118) BLUEPRINT-REF (0..1, mmt.qualifiedName="BlueprintMapping.blueprint") → DERIVED-OBJECT-REF (0..1, mmt.qualifiedName="BlueprintMapping.derivedObject"); base group `ATP-BLUEPRINT-MAPPING` (L6888) empty (both atpDerived associations skipped). Field-to-spec cross-check both directions EXACT (two ref attributes → two PEP 526 `Optional[RefType]` fields `blueprintRef`/`derivedObjectRef` in displayed row order; no extra fields, no flattening; most-derived base AtpBlueprintMapping kept). The intake class carried ZERO fields — both accessors, both fields, and reader/writer coverage are NEW 2026-09-24: `readBlueprintMapping`/`writeBlueprintMapping` (BLUEPRINT-REF before DERIVED-OBJECT-REF per XSD) dispatched from the `readBlueprintMappingSet` BLUEPRINT-MAPPING branch / `writeBlueprintMappingSet` else-branch; matched name pairs verified; new element-level parser tests + writer order/round-trip tests added. Docstrings verbatim (class docstring = the C.17 Note verbatim incl. the spec typo "map two an object"; per-attribute docstrings are the XSD element documentations — the appendix table carries no per-attribute Notes). The v2 tracker's `## AtpBlueprintMapping` entry (atpDerived realization note) is confirmed accurate by this sync and left untouched (v2 is the historical audit); the v2 `## BlueprintMappingSet` missing-row is stale in the same way and is superseded by this note. NO open deviations for BlueprintMapping or BlueprintMappingSet; no `# Spec verified:` stamp — deferred to batch confirmation.

## `Sd`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 91
- **Package:** `M2::MSR::AsamHdo::SpecialData`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/SpecialData.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `xmlSpace` | `?` | — | missing |

## `MultiLanguageParagraph`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 290
- **Package:** `M2::MSR::Documentation::TextModel::MultilanguageData`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `helpEntry` | `?` | — | missing |

## `Graphic`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 302
- **Package:** `M2::MSR::Documentation::BlockElements::Figure`
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `generator` | `?` | — | missing |
| — *(missing)* | `—` | `htmlFit` | `?` | — | missing |
| — *(missing)* | `—` | `htmlHeight` | `?` | — | missing |
| — *(missing)* | `—` | `htmlScale` | `?` | — | missing |
| — *(missing)* | `—` | `htmlWidth` | `?` | — | missing |
| — *(missing)* | `—` | `notation` | `?` | — | missing |

## `HwElementConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 23
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementConnector.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwElementRef` | `RefType` (ref, 0..1) | `hwElement` | `HW-ELEMENT` (ref) | 2× | retained existing single-ref API; spec models two `hwElement` refs (`HW-ELEMENT-REFS`, multiplicity 2). Deferred per bounded-sync decision. |
| `hwPinRef` | `RefType` (ref, 0..1) | — *(not in spec)* | — | — | convenience ref retained; spec models pin wiring via `hwPinConnection` (aggr `HwPinConnector`\*) and `hwPinGroupConnection` (ref `HwPinGroupConnector`\*), which are not yet modeled. Deferred per bounded-sync decision. |
| — *(missing)* | `—` | `hwPinConnection` | `HwPinConnector` | aggr\* | not modeled (class `HwPinConnector` does not exist yet) |
| — *(missing)* | `—` | `hwPinGroupConnection` | `HwPinGroupConnector` | ref\* | not modeled (class `HwPinGroupConnector` does not exist yet) |

> **Note:** Per the bounded-sync decision, the pre-existing `HwElementConnector` API (`hwElementRef`/`hwPinRef`) is retained unchanged and its reader/writer coverage was added for round-trip integrity. No `# Spec verified` marker is applied because the attribute set does not match the spec table. Full spec alignment (introduce `HwPinConnector`/`HwPinGroupConnector`, model `hwElement` as a 2-ref set and the two pin-connection members) is deferred work.

## `Map`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 305
- **Package:** `M2::MSR::Documentation::BlockElements::Figure`
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `class` | `?` | — | missing |
| — *(missing)* | `—` | `name` | `?` | — | missing |
| — *(missing)* | `—` | `onclick` | `?` | — | missing |
| — *(missing)* | `—` | `ondblclick` | `?` | — | missing |
| — *(missing)* | `—` | `onkeydown` | `?` | — | missing |
| — *(missing)* | `—` | `onkeypress` | `?` | — | missing |
| — *(missing)* | `—` | `onkeyup` | `?` | — | missing |
| — *(missing)* | `—` | `onmousedown` | `?` | — | missing |
| — *(missing)* | `—` | `onmousemove` | `?` | — | missing |
| — *(missing)* | `—` | `onmouseout` | `?` | — | missing |
| — *(missing)* | `—` | `onmouseover` | `?` | — | missing |
| — *(missing)* | `—` | `onmouseup` | `?` | — | missing |
| — *(missing)* | `—` | `style` | `?` | — | missing |
| — *(missing)* | `—` | `title` | `?` | — | missing |

## `MlFigure`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 307
- **Package:** `M2::MSR::Documentation::BlockElements::Figure`
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `frame` | `?` | — | missing |

## `Traceable`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 312
- **Package:** `M2::MSR::Documentation::BlockElements::RequirementsTracing`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/Traceable.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `traceRefs` | `Ref (Traceable)` | Refs | missing |

## `DocumentViewSelectable`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 340
- **Package:** `M2::MSR::Documentation::BlockElements::PaginationAndView`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/BlockElements/PaginationAndView.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `si` | `?` | — | missing |
| — *(missing)* | `—` | `view` | `?` | — | missing |

## `LOverviewParagraph`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 348
- **Package:** `M2::MSR::Documentation::TextModel::LanguageDataModel`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blueprintValue` | `?` | — | missing |

## `BlueprintGenerator`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **pages:** 424-425
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintGenerator`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator.py` (leaf package — path updated 2026-09-24, was the pre-reorg `BlueprintGenerator/BlueprintGenerator.py`)

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both members of the former `missing` rows above (`expression` `VerbatimString` 0..1 attr, `introduction` `DocumentationBlock` 0..1 aggr) are implemented with full reader/writer coverage since the re-sync. |

**Note:** Re-synced 2026-09-24 (alignment pass, batch group6-batch-9b). Citation re-verified and updated to Table E.12, pp.424-425 (page via direct pypdf scan; pdf_page.py does not index appendix-letter ids) — E.12 is the ONLY BlueprintGenerator table in either corpus (no numeric main table in R23-11; R4.3.1 fallback case-insensitive sweep 0 hits — genuinely R23-11-only), and the appendix E caption-shift documented on the AtpBlueprint sync applies here too: the table body renders ABOVE the caption (main fragment incl. the `expression` row under the E.11 caption position, p.424; `introduction` continuation fragment + the `Table E.12` caption on p.425; the Boolean body renders under the E.12 caption matching its own E.13 caption). XSD 00052 corroboration: group `BLUEPRINT-GENERATOR` (L9083) sequence INTRODUCTION (offset 10) → EXPRESSION (offset 20), complexType (L9105, abstract="false") composes AR-OBJECT group + own group — Base row `ARObject` confirmed, most-derived base ARObject; consumed by `VARIATION-POINT` group L130046 `FORMAL-BLUEPRINT-GENERATOR` (0..1, seqOffset 30, atp.Status="draft"). Field-to-spec cross-check both directions EXACT (two attributes → two PEP 526 `Optional` fields in displayed row order; no extra fields; no create/add — neither member is a Referrable child). Reader/writer FULLY covered both sides since intake: `readBlueprintGenerator`/`writeBlueprintGenerator` (INTRODUCTION before EXPRESSION per XSD) dispatched from `readVariationPoint`/`writeVariationPoint` via `FORMAL-BLUEPRINT-GENERATOR` — matched name pairs verified; new element-level reader tests + writer order/round-trip tests added 2026-09-24 (the parser side had zero FORMAL-BLUEPRINT-GENERATOR coverage before). Docstrings wiped and rewritten verbatim from the Table E.12 Notes (class docstring = Note minus the `Tags: atp.Status=valid` tail; setters append the None-no-op sentence). The two `missing` rows above were STALE (pre-dated the implementation) and are superseded by the no-deviation row. NO open deviations; no `# Spec verified:` stamp — deferred to batch confirmation.

## `BlueprintFormula`
- **PDF:** `AUTOSAR_FO_TPS_StandardizationTemplate.pdf`  | **page:** 163 (Table C.16)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintFormula`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintFormula.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Both Table C.16 attributes implemented spec-named: `ecuc` → `ecucRef` (`Optional[RefType]`, 1, ref — Kind-suffix Rule 1.5 per `sysc`→`syscRef`), `verbatim` (`Optional[MultiLanguageVerbatim]`, 1, aggr); concrete class per the table header and XSD abstract="false"; docstrings verbatim from the table Notes; reader/writer covered by the class's own `readBlueprintFormula`/`writeBlueprintFormula` helper pair, element-level tests (dedicated parser + writer test files). Stamped `# Spec verified: R23-11 (2026-09-27, user 9b confirmation)` (commit 6d8ace028). |

**Note:** Synced 2026-09-26 against R23-11 FO StandardizationTemplate Table C.16 (p.163; appendix C caption-shift — the table body renders ABOVE the caption on the same page, per the BlueprintGenerator appendix precedent; pdf_page.py does not index appendix-letter ids, page via direct pypdf scan; R4.3.1 reproduction Table D.12 carries the same rows). XSD 00052 corroboration: group `BLUEPRINT-FORMULA` (L9023) is a choice of ECUC-QUERY-REF (`atp.Status="removed"` — not modeled, the PDF table wins per Rule 1.5/0015) / ECUC-REF (`mmt.RestrictToStandards="CP"`, DEST `ECUC-DEFINITION-ELEMENT--SUBTYPES-ENUM`) / VERBATIM (type `MULTI-LANGUAGE-VERBATIM`); complexType (L9068, abstract="false", `mixed="true"`) composes AR-OBJECT + FORMULA-EXPRESSION (empty sequence — skipped atpDerived associations) + SW-SYSTEMCONST-DEPENDENT-FORMULA + own group, attributeGroup AR-OBJECT only — Base row `ARObject, FormulaExpression, SwSystemconstDependentFormula` confirmed, most-derived provided base `SwSystemconstDependentFormula` (ConditionByFormula precedent). The queue row's "pure-text formula class" Phase-0 assumption (CompuGenericMath shape — zero own content members) was corrected at Step 1: the class has TWO own content members. The sole consuming element `VariationPoint.formalBlueprintCondition` (FORMAL-BLUEPRINT-CONDITION, VARIATION-POINT group L130040) is `atp.Status="removed"` in R23-11, absent from VariationPoint's R23-11 table, and deliberately not read/written by the stamped VariationPoint sync (documented at the readVariationPoint helper) — there is NO live dispatcher to wire into; reader/writer coverage is therefore the class's own helper pair (mixed text + ECUC-REF + VERBATIM + the inherited SYSC refs via the shared SwSystemconstDependentFormula helpers), pinned at element level with dedicated parser/writer test files (PostBuildVariantCriterionValue precedent: own helper pair + element-level tests until a dispatcher is sanctioned; wiring the removed consumer element would violate VariationPoint's own R23-11 table per Rule 0015). Field-to-spec cross-check both directions EXACT (two attributes → two PEP 526 `Optional` fields in displayed row order; no extra fields; no create/add — neither member is a Referrable child; the `verbatim` aggregation round-trips through the shared `getMultiLanguageVerbatim`/`setMultiLanguageVerbatim` pair). Docstrings verbatim from the Table C.16 Notes (class docstring = Note verbatim; setters append the None-no-op sentence). NO open deviations; no `# Spec verified:` stamp — written 2026-09-27 (6d8ace028).

## `FMConditionByFeaturesAndAttributes`
- **PDF:** `AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf`  | **page:** 62 (Table 7.2)
- **Package:** `M2::AUTOSARTemplates::FeatureModelTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/FeatureModelTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — Table 7.2 declares NO attribute rows (the `-` row), and the class declares zero own members; the `<<atpMixedString>>` content is the inherited `getMixedString`/`setMixedString` mixin accessors, the reference lists the inherited `FormulaExpression` `atpReferences`/`atpStringReferences`. Stamped `# Spec verified: R23-11 (2026-09-27, user 9b confirmation)` (commit d69232bdf). |

**Note:** Synced 2026-09-26 against R23-11 FO FeatureModelExchangeFormat Table 7.2 (section 7.2.2, p.62 — numeric id indexed by pdf_page.py, p.62 in both R23-11 and R4.3.1; R4.3.1 reproduction Table 7.2 carries the same rows, AUTOSAR_TPS_FeatureModelExchangeFormat.md line 1780). XSD 00052 corroboration: group `FM-CONDITION-BY-FEATURES-AND-ATTRIBUTES` (L62013) is an empty sequence; complexType (L62022, `abstract="false"`, `mixed="true"`) composes AR-OBJECT + FORMULA-EXPRESSION + FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES + own group, attributeGroup AR-OBJECT only — concrete `<<atpMixedString>>` class confirmed (no `(abstract)` marker in the table header, unlike Tables 7.1/7.3). Base row `ARObject, FMFormulaByFeaturesAndAttributes, FormulaExpression`: the most-derived base `FMFormulaByFeaturesAndAttributes` (Table 7.1, abstract, GROUP-ONLY in the XSD — no own complexType) is missing from the model and is a separate Group8 FM* sync row, so the class derives from the nearest available ancestor `FormulaExpression` (stamped R23-11, Table C.5 pp.73-74) — re-base finding (not an open deviation): when the sibling row lands, `FMConditionByFeaturesAndAttributes` may be re-based onto it. Closure check (queue-row note): `FMFeature` and `FMAttributeDef` (the Table 7.1 ref targets) and ALL Aggregated-by consumers `FMFeatureMapCondition` (FM-COND, L62309), `FMFeatureRelation` (RESTRICTION, L62523), `FMFeatureRestriction` (RESTRICTION, L62560) are missing from src — collected and reported, NONE created (Rule 0016 / 0001.10); the table has no ref rows, so no `Optional[RefType]` members are needed. Because no dispatcher exists at all (unlike BlueprintFormula, whose consumer VariationPoint exists but deliberately does not dispatch the removed FORMAL-BLUEPRINT-CONDITION), reader/writer coverage is the class's own helper pair `readFMConditionByFeaturesAndAttributes`/`writeFMConditionByFeaturesAndAttributes` (element key `FM-COND` per `FMFeatureMapCondition.fmCond`, the `RESTRICTION` roles via the key parameter; ARObject attributes + mixed text only — the parent-group members ATTRIBUTE-REF/FEATURE-REF are the Table 7.1 sibling row's business, Rule 0015 the PDF table wins), pinned at element level with dedicated parser/writer test files (BlueprintFormula / PostBuildVariantCriterionValue precedent). Docstrings verbatim from the Table 7.2 Note (class docstring only — zero attribute rows means no member docstrings exist). NO open deviations; no `# Spec verified:` stamp — written 2026-09-27 (d69232bdf).

## `FMFormulaByFeaturesAndAttributes`
- **PDF:** `AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf`  | **page:** 61 (Table 7.1)
- **Package:** `M2::AUTOSARTemplates::FeatureModelTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/FeatureModelTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Both Table 7.1 attribute rows implemented spec-named with the Kind-suffix: `attribute` → `attributeRef` (`Optional[RefType]`, 0..1, ref), `feature` → `featureRef` (`Optional[RefType]`, 0..1, ref); ref targets `FMAttributeDef` / `FMFeature` are missing from the model, so the fields carry `RefType` (TlvDataIdDefinition precedent — referenced-missing reported, classes not created); abstract class per the table's `(abstract)` marker with the FormulaExpression-precedent type guard. Stamped `# Spec verified: R23-11 (2026-09-27, user 9b confirmation)` (commit d69232bdf). |

**Note:** Synced 2026-09-26 against R23-11 FO FeatureModelExchangeFormat Table 7.1 (section 7.2.1, p.61 per pdf_page.py — p.61 in both R23-11 and R4.3.1; the dispatch intel's "p.62" pointed at the Table 7.2 region; R4.3.1 reproduction Table 7.1 carries the same rows, AUTOSAR_TPS_FeatureModelExchangeFormat.md line 1757). XSD 00052 corroboration: the class is GROUP-ONLY — no own complexType; group `FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES` (L62746, stereotypes `atpMixedString,atpObject`) is an unbounded 0..* choice of ATTRIBUTE-REF (DEST `FM-ATTRIBUTE-DEF--SUBTYPES-ENUM`, required) and FEATURE-REF (DEST `FM-FEATURE--SUBTYPES-ENUM`, required), each 0..1 per the appinfo `pureMM minOccurs=0/maxOccurs=1`; constraints constr_3665/constr_3666 (the reference in the role shall exist). Base row `ARObject, FormulaExpression` → most-derived provided base `FormulaExpression` (stamped R23-11, Table C.5). The Table 7.1 attribute rows carry NO Note column, so the member docstrings are verbatim from the XSD group member documentation (ATTRIBUTE-REF "An expression of type FMFormulaByFeaturesAndAttributes may refer to attributes of FMFeatures." / FEATURE-REF "…may refer to FMFeatures."); the class docstring is the Table 7.1 Note verbatim. Consumer re-base applied in this pass (Rule 0012.3): `FMConditionByFeaturesAndAttributes` re-based from `FormulaExpression` onto this class per its Table 7.2 Base row `ARObject, FMFormulaByFeaturesAndAttributes, FormulaExpression` (sibling model-test base-chain pin updated; the re-base note added to its checklist header and todo row). Per Rule 0001.7 (abstract XML-bearing bases own reusable helpers) the class owns the `readFMFormulaByFeaturesAndAttributes`/`writeFMFormulaByFeaturesAndAttributes` helper pair; the concrete subclass composes them via isinstance dispatch (readConditionByFormula / readBlueprintFormula precedent — its complexType L62022 composes this group); no standalone dispatcher exists for the Aggregated-by consumers (all missing from src), so coverage is pinned at element level with dedicated parser/writer test files (BlueprintFormula / PostBuildVariantCriterionValue precedent). Closure check: `FMFeature`, `FMAttributeDef`, `FMFeatureMapCondition` (FM-COND, L62309), `FMFeatureRelation` (RESTRICTION, L62523), `FMFeatureRestriction` (RESTRICTION, L62560) all missing from src — collected and reported, NONE created (Rule 0016 / 0001.10). Field-to-spec cross-check both directions EXACT (two attribute rows → two PEP 526 `Optional[RefType]` fields in displayed row order; no extra fields; get/set shape — neither ref target is a Referrable child in src). NO open deviations; no `# Spec verified:` stamp — written 2026-09-27 (d69232bdf).

## `CryptoKeySlot`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 57
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::CryptoDeployment`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the four formerly-`missing` rows (allocateShadowCopy, cryptoObjectType, keySlotAllowedModification, keySlotContentAllowedUsage) are implemented on CryptoKeySlot with full reader/writer coverage (Table B.5); stale rows removed 2026-09-27 during the Group20 member-type sync (CryptoObjectTypeEnum / CryptoKeySlotAllowedModification / CryptoKeySlotContentAllowedUsage). Source path updated to the consolidated CryptoDeployment/__init__.py module (class-named submodule no longer exists). |

## `IdsPlatformInstantiation`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 63
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsPlatformInstantiation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `networkInterfaceRefs` | `Ref (PlatformModuleEthernetEndpointConfiguration)` | Refs | missing |
| `timeBases` | `—` | `timeBase` | `TimeBaseResourceRefConditional` | — | type (spec many vs py single) |

## `IdsmModuleInstantiation`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 63
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsmModuleInstantiation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `reportableSecurityEventRefs` | `Ref (SecurityEventMapping)` | Refs | missing |

## `PlatformModuleEthernetEndpointConfiguration`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 65
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::AdaptiveModule`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/AdaptiveModule/PlatformModuleEthernetEndpointConfiguration.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `communicationConnectorRef` | `Ref (EthernetCommunicationConnector)` | Ref | missing |
| — *(missing)* | `—` | `ipv4MulticastIpAddress` | `Ip4AddressString` | — | missing |
| — *(missing)* | `—` | `ipv6MulticastIpAddress` | `Ip6AddressString` | — | missing |
| — *(missing)* | `—` | `secureComPropsForTcpRef` | `Ref (SecureComProps)` | Ref | missing |
| — *(missing)* | `—` | `secureComPropsForUdpRef` | `Ref (SecureComProps)` | Ref | missing |
| — *(missing)* | `—` | `tcpPortRef` | `Ref (ApApplicationEndpoint)` | Ref | missing |
| — *(missing)* | `—` | `udpPortRef` | `Ref (ApApplicationEndpoint)` | Ref | missing |

## `SdClientConfig`
- **PDF:** `(not in these PDFs)`  | **page:** -
- **Package:** `?`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `capabilityRecord` | `TagWithOptionalValue` | `capabilityRecord` | `TagWithOptionalValue` | — | type (spec many vs py single) |

## `CompuGenericMath`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 374 (Table 5.60)
- **Package:** `M2::MSR::AsamHdo::ComputationMethod`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Sole Table 5.60 attribute `level` (0..1, xml.attribute) implemented spec-named `level` (`Optional[PrimitiveIdentifier]`, PEP 526 annotated assignment in displayed row order); base `FormulaExpression` = most-derived of spec Base `ARObject, FormulaExpression`; no `create*`/`add*` (member is not a Referrable child); reader/writer coverage for the kept attrs: LEVEL attribute, atpMixedString element text, and S/T checksum/timestamp via the matched `readARObject`/`writeARObject` pair; docstrings/comment copied verbatim from the markdown Note. Stamp deferred to batch confirmation (9b). |

**Note:** Synced 2026-09-26 against R23-11 CP SoftwareComponentTemplate Table 5.60 (p.374); class Note "This meta-class represents the ability to specify a generic formula expression." XSD 00052 corroboration (Rule 0015): attributeGroup COMPU-GENERIC-MATH = exactly LEVEL typed PRIMITIVE-IDENTIFIER--SIMPLE (no XSD-only attrs), stereotypes atpMixedString + atpObject, complexType mixed="true" with empty sequence, FORMULA-EXPRESSION associations atpDerived-skipped (no child elements) — PDF table and XSD agree exactly. All five Step-1 gaps closed in this sync: (G1) reader LEVEL now `PrimitiveIdentifier()` instead of `ARLiteral()`; (G2) atpMixedString element text now round-trips (reader strip-guarded `readMixedStringText`, writer `formula_element.text = getMixedString()`, sibling formula pattern); (G3) reader now calls `readARObject` on SW-DATA-DEPENDENCY / SW-DATA-DEPENDENCY-FORMULA / SW-DATA-DEPENDENCY-ARGS matching the writer's `writeARObject` — S/T checksum/timestamp were silently dropped on read; (G4) class/inline/getter/setter texts verbatim from the markdown Note incl. the `Tags: xml.attribute=true` tail; (G5) checklist migrated to the 6-column release format (rows + `Spec:` line only — `Spec verified` withheld pending 9b). Rule-tension resolution (0012.2.5.2 parenthetical vs Rule 0012 overview / 9b checklist "copied verbatim"): the `Tags:` tail is KEPT in all three positions (inline comment, getter, setter) — matches the 9b-confirmed GeneralAnnotation and CompuMethod precedent; the setter joins the None-no-op sentence single-line per the sibling BlueprintFormula shape. Consumer context: `SwDataDependency.swDataDependencyFormula` (Table 5.58, already stamped). No missing referenced classes (Phase-0 closure resolved interactively: FormulaExpression, ARObject, PrimitiveIdentifier all exist; queue = this class only). Out-of-closure observation, not fixed here: the proxy sub-readers (`readSwCalprmRefProxy`/`readSwVariableRefProxy`) still lack the writer's `writeARObject` — separate helper parity, unrelated to Table 5.60. No open deviations.

## `WhitespaceControlled`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 292 (Table 9.7)
- **Package:** `M2::MSR::Documentation::TextModel::LanguageDataModel`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Sole Table 9.7 attribute `xmlSpace` (Mult. 1, xml.attribute) implemented spec-named `xmlSpace` (`Optional[XmlSpaceEnum]`, PEP 526 annotated assignment; Mult. 1 documented but modeled Optional per the repo-wide convention — same as the Sd.xmlSpace precedent); base `(ARObject, ABC)` = spec Base `ARObject` + abstract-class anchor (XSD group appinfo stereotype `atpObject` only — no atpMixedString); reader/writer coverage via the owned helper pair `readWhitespaceControlled`/`writeWhitespaceControlled` wired into the L-10 (getLPlainTexts/setLPlainText) and L-5 (getMultiLanguageVerbatim loop/setLVerbatim) consumer paths, namespace form `{http://www.w3.org/XML/1998/namespace}space` mirroring writeSds; class/inline texts verbatim from the markdown Note incl. the `Tags: …xml.nsPrefix=xml` tail (inline carries Tags, getter/setter sans Tags — in-file MCFV family disposition). Stamp `# Spec verified: R23-11` written 2026-09-26 on user 9b confirmation. |

**Note:** Synced 2026-09-26 against R23-11 FO GenericStructureTemplate Table 9.7 (p.292); class Note "This meta-class represents the ability to control the white-space handling e.g. in xml serialization. This is implemented by adding the attribute "space"." XSD 00052 corroboration (Rule 0015): group WHITESPACE-CONTROLLED L130864 = empty sequence (no child elements), attributeGroup L130873 = exactly the required `xml:space` ref with tags `xml.name=space; xml.nsPrefix=xml` matching the table row — no XSD-only attributes; member type `XmlSpaceEnum` (Enumerations.py, `# XSD verified` stamped) skipped per Rule 0016.5. All four Step-1 gaps closed in this sync: (G1) class created from its spec table; (G2) `xml:space` now round-trips on L-10 and L-5 (previously never read or written outside the Sd writer); (G3) Tags disposition resolved to the in-file family convention (inline-with-Tags, accessors sans-Tags — cross-file variance vs the CompuGenericMath Tags-everywhere resolution recorded for 9b); (G4) 6-col checklist written, `Spec verified` withheld pending 9b. Consumer drift in the same change set (Rule 0012.3-style, MCFPT-session precedent): `LPlainText` and `LVerbatim` re-parented to add `WhitespaceControlled` per their own Base rows (Tables 9.96 / 9.89 `ARObject , LanguageSpecific , MixedContentFor<…> , WhitespaceControlled`) — bases ordered `(parent, LanguageSpecific, WhitespaceControlled)` to stay MRO-valid before AND after the queued MCFPT/MCFV re-parents; MCFPT (Table 9.94) and MCFV (Table 9.6) re-parents NOT done here (their own queue rows, Rule 0017.1). Out-of-closure observations RESOLVED same change set (2026-09-26 review follow-up): parser `readSd` now reads Sd.xmlSpace via the shared `readWhitespaceControlled` (closes the readSd/writeSds asymmetry; both helpers widened to `Union[Sd, WhitespaceControlled]`, SD parser/writer/round-trip tests + the AdminDataWhitespace.arxml integration fixture added); `VerbatimString.xmlSpace` remains unimplemented — its stale "missing enum type" docstring reason corrected to "deferred" (implementation needs the ~10 ad-hoc VT/VALUE writer sites wired, its own sync row + 9b). No open deviations.

## `MixedContentForPlainText`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 349 (Table 9.94)
- **Package:** `M2::MSR::Documentation::TextModel::InlineTextModel`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Table 9.94 carries ZERO Attribute rows (header + `-` separator only) and the class models exactly that: no own fields, no own accessors, no `create*`/`add*` (not a Referrable child); base `(WhitespaceControlled, AtpMixedString, ABC)` = spec Base `ARObject , WhitespaceControlled` with the most-derived base WhitespaceControlled (ARObject dropped as redundant — reachable via WhitespaceControlled, LPlainText precedent) plus the `<<atpMixedString>>` mixin per Rule 0021 (XSD 00052 L81511 stereotypes `atpMixedString,atpObject`); abstract TypeError guard; class docstring verbatim from the Table 9.94 Note (byte-equal to the markdown Note cell AND to the XSD group documentation L81509); reader/writer columns `[—]` — XSD group MIXED-CONTENT-FOR-PLAIN-TEXT L81507 is an empty sequence, so the class owns no XML surface (Rule 0001.7 standalone N/A for an abstract class with no own XML-bearing attributes); inherited `getMixedString`/`setMixedString` (AtpMixedString mixin) and `getXmlSpace`/`setXmlSpace` (WhitespaceControlled) are tracked on their declaring classes' checklists. |

**Note:** Rerun 2026-09-26 (user-ordered full 9-step re-run; the class was marker-less after its first pass, which recorded WhitespaceControlled as referenced-missing and deferred Step 9). Deltas closed in this rerun: (G1) WhitespaceControlled now exists in src and is stamped `# Spec verified: R23-11` (Table 9.7, commit a78d444af) → the class re-parented `(ARObject, AtpMixedString, ABC)` → `(WhitespaceControlled, AtpMixedString, ABC)` per Rule 0001.2 (most-derived base in the Base chain); MRO verified before and after — MixedContentForPlainText → WhitespaceControlled → ARObject → AtpMixedString → ABC, and the consumer `LPlainText` keeps its exact prior MRO (LPlainText → MixedContentForPlainText → LanguageSpecific → WhitespaceControlled → ARObject → AtpMixedString → ABC) with its own Table 9.96 base list untouched; (G2) the first pass's "referenced-missing WhitespaceControlled" report is now resolved (nothing missing, nothing to defer); (G3) checklist trailing note extended to record the inherited WhitespaceControlled accessors. No serialization change: the class's XSD group is an empty sequence, and `xml:space` reaches L-PLAIN-TEXT through the WhitespaceControlled attributeGroup already wired by the stamped `readWhitespaceControlled`/`writeWhitespaceControlled` pair (298/298 across the L-10/L-5 parser+writer suites after the re-parent). Consumers: `LPlainText` (Table 9.96, re-parented in the first pass) and `MultiLanguagePlainText.l10` (Table 9.95). No missing referenced classes (WhitespaceControlled, AtpMixedString, ARObject all exist). 6-column checklist written; `# Spec verified: R23-11` written 2026-09-26 on user 9b confirmation.

## `MixedContentForVerbatim`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 292 (Table 9.6)
- **Package:** `M2::MSR::Documentation::TextModel::InlineTextModel`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Table 9.6 carries four Attribute rows — `br` (Br), `e` (EmphasisText), `tt` (Tt), `xref` (Xref), all Mult. 1 / aggr / `xml.sequenceOffset` 50-30-(-)-40 — implemented as spec-named `Optional[Br|EmphasisText|Tt|Xref]` annotated fields (Mult. 1 modeled Optional per repo convention; each setter is a documented None-no-op); base `(WhitespaceControlled, AtpMixedString, ABC)` = spec Base `ARObject , WhitespaceControlled` with the most-derived base WhitespaceControlled (ARObject dropped as redundant — reachable via WhitespaceControlled, MCFPT precedent) plus the `<<atpMixedString>>` mixin per Rule 0021 (XSD 00052 L81543 stereotypes `atpMixedString,atpObject`); abstract TypeError guard; class docstring verbatim from the Table 9.6 Note (byte-equal to the markdown Note cell AND to the XSD group documentation L81542); all 4 inline comments / 4 getter / 4 setter docstrings byte-equal to the attribute Notes (inline carries the `Tags: xml.sequenceOffset=…` tail, accessors sans Tags, setter appends the None-no-op sentence — in-file family disposition); reader/writer columns `[—]`/`[x]` as serialized on the consuming L-5 element via the helper pair `readMixedContentForVerbatim`/`writeMixedContentForVerbatim` (parser L1842, writer L1515, wired at parser L6490 / writer L3059); inherited `getMixedString`/`setMixedString` (AtpMixedString mixin) and `getXmlSpace`/`setXmlSpace` (WhitespaceControlled) are tracked on their declaring classes' checklists. |

**Note:** Rerun 2026-09-26 (user-ordered sync run; the class was marker-less after its first pass, which had deferred Step 9 to a batch and recorded WhitespaceControlled only via the queue row). Deltas closed in this rerun: (G1) WhitespaceControlled now exists in src and is stamped `# Spec verified: R23-11` (Table 9.7, commit a78d444af) → the class re-parented `(ARObject, AtpMixedString, ABC)` → `(WhitespaceControlled, AtpMixedString, ABC)` per Rule 0001.2 (most-derived base in the Base chain); MRO verified before and after — MixedContentForVerbatim → WhitespaceControlled → ARObject → AtpMixedString → ABC, and the consumer `LVerbatim` keeps its exact prior MRO (LVerbatim → MixedContentForVerbatim → LanguageSpecific → WhitespaceControlled → ARObject → AtpMixedString → ABC) with its own Table 9.89 base list untouched; (G2) Step 1 corrected the queue row's placeholder `GST Table E.5x` to the located **Table 9.6, p.292** (R4.3.1 counterpart: Table 8.7, p.255); (G3) checklist trailing note extended to record the inherited WhitespaceControlled accessors. Step 1 three-way diff clean: 13/13 cells byte-equal (class docstring, 4 inline comments, 4 getters, 4 setters) against the markdown Note/attribute rows and XSD 00052 group MIXED-CONTENT-FOR-VERBATIM L81540 (docs `TT`/`E`/`XREF`/`BR`, appinfo offsets 30/40/50, `TT` unoffset — no XSD-only elements); no docstring rewrite needed. Reader/writer verified unchanged: all four members read/written (BR, E, TT, XREF) with the absent-child path covered — 6/6 dedicated round-trip tests (`tests/test_armodel/parser/test_mixed_content_for_verbatim.py`, `tests/test_armodel/writer/test_mixed_content_for_verbatim.py`) pass after the re-parent; no serialization change (pure Python base-class change). New Step-2 tests: `test_base_anchoring` (new bases + issubclass asserts), `test_inherits_whitespace_controlled_accessors`, `test_field_to_spec_cross_check` (`_BareBases` reference form asserting exactly `br/e/tt/xref` beyond the bases). Consumers: `LVerbatim` (Table 9.89) and `MultiLanguageVerbatim`'s L-5 loop. No missing referenced classes (WhitespaceControlled, AtpMixedString, ARObject, Br/EmphasisText/Tt/Xref all exist). 6-column checklist written; `# Spec verified: R23-11` written 2026-09-26 on user 9b confirmation.

## `PerInstanceMemorySize`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 624  | **table:** Table 8.8
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 8.8 attributes are modeled with the PDF types and 0..1 shapes: `alignment`/`size` as `Optional[PositiveInteger]`, and `perInstanceMemory` as `perInstanceMemoryRef: Optional[RefType]` with the Kind `ref` suffix. The concrete class uses `ARObject` plus the `VariationPointCapable` mixin required by the `SwcImplementation.perInstanceMemorySize` atpVariation aggregation. Reader/writer coverage is present for ALIGNMENT, PER-INSTANCE-MEMORY-REF, SIZE, and the generated VARIATION-POINT; the parent wrapper is emitted only for nonempty lists. All closure member types are already stamped. No open deviations; the `# Spec verified: R23-11` stamp awaits the user 9b confirmation. |

**Note:** Reviewed 2026-09-28 against R23-11 CP SoftwareComponentTemplate Table 8.8, p.624; XSD 00052 group PER-INSTANCE-MEMORY-SIZE sequence ALIGNMENT → PER-INSTANCE-MEMORY-REF → SIZE → VARIATION-POINT and complexType PER-INSTANCE-MEMORY-SIZE composes AR-OBJECT plus that group. The VARIATION-POINT annotation says `Applicable for: SwcImplementation.perInstanceMemorySize`, matching the atpVariation aggregation and the mixin capability. The alignment Note's markdown split `Per InstanceMemory` is normalized to `PerInstanceMemory` per the XSD documentation. The class was not present in src at intake; the consumer's Rule 0001.10 placeholder was replaced with the real model type and both sides now round-trip the child values. No existing v2 tracker section was found; that audit report was left unchanged.

## `ConfigReferenceValue`
- **PDF:** `AUTOSAR_ECU_Configuration.pdf` (R3.2.3)  | **page:** markdown l.2284 (Table 3.40; pdf_page.py has no R3.2.3 caption hit — markdown line cited per the batch brief)
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `definitionRef` | `Optional[RefType]` | `definition` | ``ConfigReference`` | ref | naming (Ref suffix per Rule 0001.5 — module convention, not a deviation); type (spec Mul 1 vs py Optional) — accepted: XSD group CONFIG-REFERENCE-VALUE (AUTOSAR.xsd l.6087) DEFINITION-REF has minOccurs="0" |
| — *(attribute)* | — | `definition` DEST attribute | — | — | accepted: XSD DEST use="required" (CONFIG-REFERENCE--SUBTYPES-ENUM) but the Os_ECUC.arxml integration fixture carries DEFINITION-REF with no DEST; reader/writer treat DEST as optional for a lossless round-trip |

**Note:** Batch re-sync 2026-09-30 (Group19 row 1; the class had already been synced and 9b-stamped `# Spec verified: R3.2.3` by the R3x-ECUC passes, commits 500cfd2bd..3f0dac184). This pass re-verified the full field-to-spec cross-check against R3.2.3 Table 3.40 (abstract Class; Base ARObject; one attr `definition`, ConfigReference, 1, ref) and the XSD group CONFIG-REFERENCE-VALUE l.6087; all class/attr docstrings diffed verbatim against the markdown Note + ecuc_sws_3027/3028/3029 and the XSD DEFINITION-REF doc. Deltas: (1) the `# Spec:` line's unverifiable `p.103 (R3.2 Rev 3)` re-cited to the markdown line (no R3.2.3 PDF caption hit via pdf_page.py); (2) the marker line stripped per batch mode — stamp deferred to the batch confirmation; (3) the stale "Rule 0019.3" citation replaced with the real XSD evidence; (4) a get_type_hints annotation pin test added (`TestConfigReferenceValue.test_member_annotations`; the setter's quoted self-return stays — the module has no PEP 563 and a bare self-referential return annotation raises NameError at class creation). Model/reader/writer source otherwise unchanged; the two deviation rows above mirror the inline checklist notes and are accepted (XSD-anchored + fixture-required).

## `EcucValueCollection`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf` (R23-11)  | **page:** 108 (Table 2.45; caption md l.2949 — pdf_page.py has no caption hit, page via direct pypdf caption scan)
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 2.45 attributes are modeled with the Kind `ref` suffix: `ecucValueRefs: List[RefType]` (spec `*`, get/add pair, dedicated typed list) and `ecuExtractRef: Optional[RefType]` (spec 0..1, get/set pair). Base stays `ARElement` (most-derived of the spec Base chain). Reader coverage was already complete (`readEcucValueCollection` via `getChildElementOptionalRefType`; ECUC-VALUES wrapper of ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL per the XSD group); the writer gained the missing `writeARPackageElement` dispatch branch (the element was previously dropped on save). No integration fixture carries ECUC-VALUE-COLLECTION. No open deviations; the `# Spec verified: R23-11` stamp awaits the batch confirmation. |

**Note:** Batch sync 2026-09-30 (Group19 row 2; the class existed unstamped with an old 4-column checklist, untyped fields and a paraphrased class docstring). This pass synced it against R23-11 CP ECUConfiguration Table 2.45, p.108 (concrete Class; Note "This represents the anchor point of the ECU configuration description. Tags: atp.recommendedPackage=EcucValueCollections"; Base ARElement, ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable; attrs `ecucValue` EcucModuleConfigurationValues `*` ref, `ecuExtract` System 0..1 ref) and the XSD group ECUC-VALUE-COLLECTION (AUTOSAR_00052.xsd l.53750; XML order ECU-EXTRACT-REF → ECUC-VALUES, already followed by reader/writer). Not VP-capable per Rule 0020 — the atpVariation sits on a Kind=ref row (association pattern lands on the wrapper class, not the referenced type) and the XSD complexType declares no VARIATION-POINT. The class docstring carries the Note verbatim plus [TPS_ECUC_02151] (md l.8351) and [constr_3588] (md l.8395). RefType covers both kind-ref targets (EcucModuleConfigurationValues / System are the ref destinations, not field types) — no Rule 0001.10 missing classes.

## `ModuleConfiguration`
- **PDF:** `AUTOSAR_ECU_Configuration.pdf` (R3.2.3)  | **page:** markdown l.1916 (Table 3.30; pdf_page.py has no R3.2.3 caption hit — markdown line cited per the batch brief)
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `containers` | `List[Container]` | `container` | `Container` | aggr | naming (spec-`*` singular name → plural list + create/get pair per Rule 0001.4/0001.6 — not a deviation) |
| `definitionRef` | `Optional[RefType]` | `definition` | ``ModuleDef`` | ref | naming (Ref suffix per Rule 0001.5 — module convention, not a deviation); type (spec Mul 1 vs py Optional) — accepted: XSD group MODULE-CONFIGURATION (AUTOSAR.xsd l.16416) DEFINITION-REF has minOccurs="0"; Os_ECUC.arxml carries no DEFINITION-REF |
| — *(attribute)* | — | `definition` DEST attribute | — | — | accepted: XSD DEST use="required" (MODULE-DEF--SUBTYPES-ENUM) but the Os_ECUC.arxml integration fixture carries DEFINITION-REF with no DEST; reader/writer treat DEST as optional for a lossless round-trip (BASE/DEST round-trip when present) |
| `implementationConfigVariant` | `Optional[EcucConfigurationVariantEnum]` | `implementationConfigVariant` | ``ConfigurationVariant`` | attr | type (spec Mul 1 vs py Optional) — accepted: XSD IMPLEMENTATION-CONFIG-VARIANT has minOccurs="0" (AUTOSAR.xsd l.16445); AND class not yet implemented — spec type ConfigurationVariant (R3.2.3 AUTOSAR_ECU_Configuration.md Table 3.11, l.1200, ECUCParameterDefTemplate) is missing from the codebase (Rule 0001.10); placeholder R23-11 EcucConfigurationVariantEnum in use (literal sets differ: R3.2.3 adds VARIANT-POST-BUILD-LOADABLE and VARIANT-POST-BUILD-SELECTABLE, has no RECOMMENDED-CONFIGURATION); switch to the real type when that class gets its own pass |
| `moduleDescriptionRef` | `Optional[RefType]` | `moduleDescription` | ``BswImplementation`` | ref | naming (Ref suffix per Rule 0001.5 — module convention, not a deviation); matches spec Mul 0..1 |
| — *(attribute)* | — | `moduleDescription` DEST attribute | — | — | accepted: XSD DEST use="required" (BSW-IMPLEMENTATION--SUBTYPES-ENUM) but no fixture carries MODULE-DESCRIPTION-REF at all; reader/writer treat DEST as optional for a lossless round-trip |

**Note:** Batch re-sync 2026-09-30 (Group19 row 3; the class had already been synced and 9b-stamped `# Spec verified: R3.2.3` by the R3x-ECUC passes). This pass re-verified the full field-to-spec cross-check against R3.2.3 Table 3.30 (concrete Class; Base ARElement most-derived; Note "Head of the configuration of one Module…" verbatim incl. the spec "tthe" typo; 4 attrs in displayed order container/definition/implementationConfigVariant/moduleDescription) and the XSD group MODULE-CONFIGURATION l.16416. Deltas: (1) the `# Spec:` line's unverifiable `p.86 (R3.2 Rev 3)` re-cited to the markdown line (no R3.2.3 PDF caption hit via pdf_page.py); (2) the marker line stripped per batch mode — stamp deferred to the batch confirmation; (3) the container Note's missing `Stereotypes: atpSplitable` tail restored verbatim in the inline comment + createContainer/getContainers docstrings; (4) the stale "Rule 0019.3" citation replaced with the real XSD evidence; (5) the mirrored model tests were absent — added the standard set (defaults / createContainer append + duplicate / get-set + None no-op x3 / docstring verbatim / get_type_hints pins) plus a writer save→reload round-trip asserting field values incl. DEST attrs and the enum. Not VP-capable per Rule 0020 (atpSplitable only; no VARIATION-POINT in the XSD group). The container member type is fully synced in the same file (R3.2.3 Table 3.31) — not a stub. The Rule 0001.10 missing ConfigurationVariant enum should be queued (R3.2.3 Table 3.11) for a later pass.

## `EcucConfigurationClassEnum`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf` (R23-11)  | **page:** 52 (Table 2.12; caption md l.1356)
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all 4 Table 2.12 literals modeled 1:1 in displayed order (Link=0, PostBuild=1, PreCompile=2, PublishedInformation=3), member names = literal UPPER_CASE, values retyped to the spec literals exactly ("Link"/"PostBuild"/"PreCompile"/"PublishedInformation") per Rule 0011 — the pre-sync XSD-uppercase wire forms (LINK/POST-BUILD/PRE-COMPILE/PUBLISHED-INFORMATION) were drift, fixed in this pass, not a deviation row. Base AREnum (Enumeration header); consumer EcucAbstractConfigurationClass.configClass (stamped R23-11) already covers CONFIG-CLASS reader/writer. |

**Note:** Batch sync 2026-09-30 (Group19 row 4; the enum pre-existed unstamped with correct docstring/comments but XSD-form member values). The R23-11 markdown block at l.1356 is page-split-garbled — its Enumeration/Note/Aggregated-by header rows and the "Preconfigured Configuration" literal belong to Table 2.13 EcucConfigurationVariantEnum (XSD mmt.qualifiedName `EcucConfigurationVariantEnum.PreconfiguredConfiguration` proves it); the table was therefore read from the PDF page 52 text and cross-checked against ECUC-CONFIGURATION-CLASS-ENUM (AUTOSAR_00052.xsd l.135895, 4 literals, none atp.Status=removed). Member values follow the PDF Literal column per Rule 0011 + the FlexrayNmScheduleVariant batch precedent (XSD-uppercase forms belong to XML fixtures only). No integration fixture carries CONFIG-CLASS (no Rule 0019 combine case). Reconciliation item, not this class's row: sibling EcucConfigurationVariantEnum (stamped R23-11, Table 2.13) keeps XSD-uppercase member values — a prior Rule 0011 drift to revisit if that class is ever re-opened; not propagated, not fixed here (out of row scope). The v2 tracker's appendix lists this enum under "classes without a spec attribute table" — stale (Enumeration Table 2.12 exists); the v2 tracker is script-generated and left to its next regen (ConfigReferenceValue batch precedent).

## `EcucScopeEnum`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf` (R23-11)  | **page:** 46 (Table 2.7; caption md l.1163)
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 2.7 literals modeled 1:1 in displayed order (ECU=0, local=1), member names = literal UPPER_CASE, LOCAL retyped to the spec literal exactly ("local") per Rule 0011 — the pre-sync XSD-uppercase wire form ("LOCAL") was drift, fixed in this pass, not a deviation row; ECU was already correct (uppercase in the table itself). Base AREnum (Enumeration header); consumer EcucDefinitionElement.scope (stamped R23-11) already covers SCOPE reader/writer. |

**Note:** Batch sync 2026-09-30 (Group19 row 5; the enum pre-existed unstamped with correct docstring/comments but the XSD-form LOCAL value). Table 2.7 is complete in the markdown (not page-split); the PDF p.46 text and ECUC-SCOPE-ENUM (AUTOSAR_00052.xsd l.136032/l.136044 — values ECU/LOCAL, mmt.qualifiedName tails EcucScopeEnum.ECU / EcucScopeEnum.local) corroborate verbatim. Member values follow the PDF Literal column per Rule 0011 + the FlexrayNmScheduleVariant batch precedent (XSD-uppercase forms belong to XML fixtures only). No integration fixture carries SCOPE (no Rule 0019 combine case). The stale v2-tracker appendix classification ("classes without a spec attribute table") is left to that script's next regen (batch precedent).

## `EcucBooleanParamDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf` (R23-11)  | **page:** 58 (Table 2.15; caption md l.1495)
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.15 attr defaultValue (Boolean, 0..1, attr) is modeled 1:1 as `defaultValue: Optional[Boolean]` + get/setDefaultValue (None-guard, chaining); the pre-sync bare-`Boolean` annotations and missing setter chaining return were Rule 0001.4/0003 drift, fixed in this pass, not deviation rows. Base = most-derived EcucParameterDef (stamped R23-11, Table 2.14) — no flattening; reader/writer matched pair pre-existed (DEFAULT-VALUE via getChild/setChildElementOptionalBooleanValue, XSD group ECUC-BOOLEAN-PARAM-DEF l.51216, no VARIANTS wrapper). |

**Note:** Batch sync 2026-09-30 (Group19 row 7; the class pre-existed unstamped with bare-T annotations and no Note comment/docstrings). Table 2.15 is complete in the markdown (not page-split); PDF p.58 caption hit via pdf_page.py; XSD group l.51216 + complexType l.51234 corroborate (DEFAULT-VALUE minOccurs=0 maxOccurs=1, BOOLEAN-VALUE-VARIATION-POINT type — read/written as a flat optional element, no wrapper). Note tails (`atpVariation: [RS_ECUC_00083] Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime`) kept verbatim in the inline comment + getter/setter docstrings per the stamped module precedent (EcucEnumerationParamDef/EcucParamConfContainerDef). Not VP-capable per Rule 0020 (Kind=attr atpVariation row — attribute-value variation only; no VARIATION-POINT element in the XSD complexType). No Rule 0001.10 missing referenced types (Boolean is a stamped PrimitiveTypes class; base EcucParameterDef stamped in-file). Aggregated-by consumers EcucParamConfContainerDef + EcucDestinationUriPolicy already dispatch createEcucBooleanParamDef (stamped/covered).

## `EcucFloatParamDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf` (R23-11)  | **page:** 62 (Table 2.17; caption md l.1609, page-split body l.1589-1599)
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 2.17 attrs modeled 1:1 in displayed order (defaultValue Float 0..1, max Limit 0..1, min Limit 0..1) as `Optional[...]` fields + get/set pairs (None-guard, chaining); the pre-sync bare-`Float`/`Limit` annotations and missing setter chaining returns were Rule 0001.4/0003 drift, fixed in this pass, not deviation rows. Base = most-derived EcucParameterDef (stamped R23-11, Table 2.14) — no flattening; reader/writer matched pair pre-existed (DEFAULT-VALUE via getChild/setChildElementOptionalFloatValue, MAX/MIN via getChild/setChildLimitElement; XSD group ECUC-FLOAT-PARAM-DEF l.52244, no VARIANTS wrapper). |

**Note:** Batch sync 2026-09-30 (Group19 row 8; the class pre-existed unstamped with bare-T annotations and no Note comments/docstrings). Table 2.17 is PAGE-SPLIT in the markdown — the body rows (header + defaultValue + max) sit at l.1589-1599 before the caption at l.1609, min follows at l.1611; displayed order = defaultValue, max, min (Rule 0001.11 per-page concatenation — matches the XSD group sequence order l.52244 too, so member order and XML order agree here); PDF p.62 caption hit via pdf_page.py (cited header-row page). XSD DEFAULT-VALUE type FLOAT-VALUE-VARIATION-POINT, MAX/MIN type AR:LIMIT — all minOccurs=0 maxOccurs=1, read/written as flat optional elements. Note tails (`atpVariation: [RS_ECUC_00083]/[RS_ECUC_00084] Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime`) kept verbatim per the stamped module precedent (EcucEnumerationParamDef/EcucParamConfContainerDef). Not VP-capable per Rule 0020 (Kind=attr atpVariation rows; no VARIATION-POINT element in the XSD complexType l.52278). No Rule 0001.10 missing referenced types (Float/Limit stamped PrimitiveTypes classes; base EcucParameterDef stamped in-file). Aggregated-by consumers EcucParamConfContainerDef + EcucDestinationUriPolicy already dispatch createEcucFloatParamDef (stamped/covered). TPS_ECUC_06083/06084 (intervalType defaults to CLOSED when MIN/MAX INTERVAL-TYPE absent) are consumer-Limit semantics — Limit is stamped with INTERVAL-TYPE handling in getChild/setChildLimitElement.

## `EcucForeignReferenceDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf` (R23-11)  | **page:** 75 (Table 2.31; caption md l.2007)
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.31 attr destinationType (String, 0..1, attr) is modeled 1:1 as `destinationType: Optional[String]` + get/setDestinationType (None-guard, chaining); the pre-sync bare-`String` annotations, the "Gets/Sets the…" paraphrased docstrings and the reflowed class docstring were Rule 0001.4/0003 drift, fixed in this pass, not deviation rows. Base = most-derived EcucAbstractExternalReferenceDef (stamped R23-11, Table 2.28) — no flattening; the pre-sync state had NO reader/writer coverage at all — readEcucForeignReferenceDef/writeEcucForeignReferenceDef helpers, both aggregation dispatch branches and the createEcucForeignReferenceDef factory were added in this pass (Rule 0001.7 five-place pattern completed), not a deviation row. |

**Note:** Batch sync 2026-09-30 (Group19 row 9; the class pre-existed unstamped with bare-T annotations, paraphrased docstrings and zero reader/writer coverage — elements were silently dropped on round-trip). Table 2.31 is complete in the markdown (caption l.2007, body l.2009-2016); PDF p.75 caption hit via pdf_page.py. XSD group ECUC-FOREIGN-REFERENCE-DEF (AUTOSAR_00052.xsd l.52299, complexType l.52315): DESTINATION-TYPE (AR:STRING) minOccurs=0 maxOccurs=1, flat optional element — NO VARIANTS wrapper and NO VARIATION-POINT in the complexType → not VP-capable per Rule 0020 (no atpVariation row either). Class docstring carries the Note verbatim + [TPS_ECUC_02041]/[TPS_ECUC_02042]/[TPS_ECUC_06088] (md l.2005/l.2018/l.2024, `\_` unescaped, glyph markers stripped — batch convention). Reader/writer use getChild/setChildElementOptionalLiteral for DESTINATION-TYPE — the stamped sibling EcucInstanceReferenceDef's helper choice for String-typed fields in this family (module convention). Aggregated-by consumers: EcucParamConfContainerDef.reference (createEcucForeignReferenceDef factory added next to createEcucInstanceReferenceDef) + EcucDestinationUriPolicy.reference (direct construction + addReference, policy convention) — dispatch branches added on both sides of both aggregators. No Rule 0001.10 missing referenced types (String is a stamped PrimitiveTypes class). No integration fixture carries ECUC-FOREIGN-REFERENCE-DEF (no Rule 0019 combine case).
## `IPSecConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 571  | **table:** Table 6.221
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 6.221 attributes are modeled with the PDF types and multiplicity in the markdown displayed row order: `ipSecConfig Props` (`IPSecConfigProps`, `0..1`, `ref`) → `ipSecConfigPropsRef: Optional[RefType]` with the Kind `Ref` suffix; `ipSecRule` (`IPSecRule`, `*`, `aggr`) → dedicated typed list `ipSecRules: List[IPSecRule]` + `createIPSecRule(short_name)`/`getIPSecRules` (Rule 0001.6 — the aggregated child `IPSecRule` lists `Identifiable` in its spec `Base`, so the factory shape is required; corrected at the 9b gate from the prior `addIPSecRule(value)`). Base `ARObject` (spec `Base` column) ⇒ `class IPSecConfig(ARObject)` / `__init__(self)` with all fields defaulted. Reader/writer coverage for both kept attributes inside the matched `readIPSecConfig`/`writeIPSecConfig` helper pair (`IP-SEC-CONFIG-PROPS-REF` via `setIpSecConfigPropsRef`/`getIpSecConfigPropsRef`; the `IP-SEC-RULES` wrapper of unbounded `IP-SEC-RULE` via `createIPSecRule`/`getIPSecRules`, wrapper emitted only when non-empty; the parser constructs each rule through the factory); class/inline/getter/setter texts copied verbatim from the markdown `Note` cells. |

**Note:** Re-synced 2026-10-03 against R23-11 CP SystemTemplate Table 6.221, p.571 (markdown body renders ABOVE the caption at line 14964 — the trailing-caption trap: the caption `Table 6.221: IPSecConfig` is followed by the *IPSecRule* body, so the IPSecConfig rows are markdown lines 14954-14962; there is no split/continuation block for this class). **Rule 0007 fix (the reason for this pass):** the spec `Package` row is `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication`, but the class was defined in `Fibex/Fibex4Ethernet/EthernetTopology.py`; it is now defined in `SecureCommunication.py` (user-approved relocation) and removed from `EthernetTopology.py`. `EthernetTopology` still annotates `NetworkEndpoint.ipSecConfig`, so `IPSecConfig` is imported there on the existing top-of-module `from ...SecureCommunication import ...` line — no new cycle-breaker is needed (`SecureCommunication` imports nothing from `EthernetTopology` at runtime; its bottom-of-module `CommunicationDirectionType` cycle-breaker is untouched), and `IPSecRule` was dropped from that line because the move left it unused (ruff `F401`). All consumers re-pointed: `arxml_parser.py` (`SecureCommunication` import block, removed from the `EthernetTopology` block), `arxml_writer.py` (same), and the parser/writer test modules; the model mirror test moved per Rule 0006 to `tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/test_IPSecConfig.py`. `armodel.IPSecConfig` still resolves (wildcard export via `models/__init__.py` L92, ahead of the `EthernetTopology` wildcard at L99); both import orders (`EthernetTopology` first / `SecureCommunication` first) resolve in fresh interpreters and `typing.get_type_hints` resolves `IPSecConfig`'s accessors plus `NetworkEndpoint.getIpSecConfig`/`setIpSecConfig`. Referenced member types (Rule 0001.10) both already exist in the destination module — `IPSecRule` (L1144) and `IPSecConfigProps` (L1513) — so no placeholder remains; their own `# Spec verified:` stamps are still deferred to the batch 9b confirmation per their tracker notes. Out-of-closure observation, not fixed here: `NetworkEndpoint`'s checklist rows for `getIpSecConfig`/`setIpSecConfig` still read `[—] reader  [—] writer` although `readNetworkEndPoint`/`writeNetworkEndPoint` do wire the `IP-SEC-CONFIG` element (NetworkEndpoint's own pass).

## `IPSecRule`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 572  | **table:** Table 6.222
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ikeAuthenticationMethod` | `IkeAuthenticationMethodEnum` | attr | deprecated (atp.Status=removed), not implemented — XSD 00052 group IP-SEC-RULE carries `IKE-AUTHENTICATION-METHOD` (L73903) with `atp.Status="removed"`; absent from the R23-11 PDF Table 6.222 rendering (PDF-wins rule) |

**Note:** Synced 2026-09-30 against R23-11 CP SystemTemplate Table 6.222, p.572. The markdown table body is split by an image/glyph interruption after the `localPortRangeEnd` row; the continuation block (`localPortRangeStart`..`remotePortRangeStart`) was re-verified row-by-row against the XSD group IP-SEC-RULE (AUTOSAR_00052.xsd L73884-L74057) — all 16 attributes carry verbatim R23-11 markdown text, so no R4.3.1 / XSD-doc fallback rows were needed and the checklist carries a single `# Spec:` line. The 7 attributes beyond the markdown's first block (`preSharedKey`, `priority`, `remoteCertificate`, `remoteId`, `remoteIpAddress`, `remotePortRangeEnd`, `remotePortRangeStart`) come from the markdown continuation block itself, cross-checked against the XSD (`PRE-SHARED-KEY-REF` DEST CRYPTO-SERVICE-KEY, `REMOTE-*-REFS/REMOTE-*-REF` wrappers, `REMOTE-IP-ADDRESS-REF` DEST NETWORK-ENDPOINT). Member order = displayed row order (== XSD sequenceOffset order minus the removed attribute); `ref *` rows model `List[RefType]` fields with the Kind suffix (`localCertificateRefs`/`remoteCertificateRefs`/`remoteIpAddressRefs`, `add*Ref`/`get*Refs`); `ref 0..1` rows model `Optional[RefType]` with the `Ref` suffix (`preSharedKeyRef`). Reader `readIPSecRule`/writer `writeIPSecRule` serialize the `IP-SEC-RULE` element per the XSD group order; the IPSecConfig aggregator wiring stays deferred to its own pass. The `# Spec verified: R23-11` stamp is deferred to the batch 9b confirmation (user instruction).

## `IPSecConfigProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 573  | **table:** Table 6.223
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all 12 Table 6.223 attributes are modeled with the PDF types and multiplicities: `ahCipherSuiteName`/`espCipherSuiteName` (`String *`) as `List[String]` + `add*Name`/`get*Names` behind the XSD `AH-CIPHER-SUITE-NAMES`/`ESP-CIPHER-SUITE-NAMES` wrappers, `dpdAction` (`IPsecDpdActionEnum 0..1`), `dpdDelay`/`ikeOverTime`/`ikeReauthTime`/`ikeRekeyTime`/`saRandTime`/`saRekeyTime` (`TimeValue 0..1`), `ikeCipherSuiteName` (`String 0..1`), `ikeRandTime`/`saOverTime` (`PositiveInteger 0..1`). |

**Note:** Synced 2026-09-30 against R23-11 CP SystemTemplate Table 6.223, p.573. The markdown attribute set matches the XSD group IP-SEC-CONFIG-PROPS (AUTOSAR_00052.xsd L73693-L73803) 1:1 — no XSD-only members, no markdown-only members; the class-level constraint [TPS_SYST_02270] is carried in the class docstring. Base = `ARElement` (most-derived in the spec Base chain; the XSD complexType composes the full AR-OBJECT..AR-ELEMENT group chain). The sync-todo module bullet was corrected from GenericStructure/GeneralTemplateClasses/ARPackage.py to SystemTemplate/SecureCommunication.py per the spec Package row (Rule 0007); the stub was rehoused out of SystemTemplate/__init__.py (name re-imported from .SecureCommunication) per the IPSecRule (041bc7125) precedent and the stub-batch test tuple rehoused. The ikeOverTime Note's markdown cell wrap `ikeRekey Time` is normalized to `ikeRekeyTime` per the XSD documentation (mmt.qualifiedName join rule). Member order = displayed row order (== XSD sequenceOffset order); reader `readIPSecConfigProps`/writer `writeIPSecConfigProps` serialize the `IP-SEC-CONFIG-PROPS` element per the XSD group order; the ARPackage.element aggregator wiring stays deferred to its own pass. The `# Spec verified: R23-11` stamp is deferred to the batch 9b confirmation (user instruction).

## CouplingPortAbstractShaper

**No deviations.** No Class/Enumeration table exists for `CouplingPortAbstractShaper` in the R23-11, R4.3.1 or R4.4.0 markdown corpora. The class IS XSD-grounded: the R23-11 XSD models it as the abstract empty `xsd:group COUPLING-PORT-ABSTRACT-SHAPER` (`AUTOSAR_00052.xsd` L23449-23455, `atp.Status="candidate"`, documentation "Abstract class for the definition of coupling port shapers." — carried verbatim as the class docstring; the 2026-09-28 "no own construct in any XSD" finding was wrong). The spec consumes it only through the `CouplingPortFifo.shaper` choice (L23763: `COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER` | `COUPLING-PORT-CREDIT-BASED-SHAPER`), and the reader and writer dispatch that choice by comparing the element name against those two XSD tags.

| Name in source code | Type (source) | Member name (spec) | Type (XSD) | Kind | Deviation |
|---|---|---|---|---|---|
| `CouplingPortAbstractShaper` | class | — *(abstract, no spec attributes)* | `xsd:group COUPLING-PORT-ABSTRACT-SHAPER` (empty `xsd:sequence`) | aggr base | **none:** the class models the XSD abstract base directly — zero own attributes, and the `CouplingPortFifo.shaper` `xsd:choice` is dispatched by element-name comparison in `readCouplingPortFifoShaper` / `writeCouplingPortFifoShaper` (round-tripped by `tests/test_armodel/writer/test_coupling_port_abstract_shaper.py` for both choice branches plus both unsupported paths). |

**Note:** Checklist rebuilt 2026-09-30 in the XSD-only 6-column variant. Re-synced 2026-10-03 (Group16 Task 11, no marker ⇒ full 9-step): `# Spec:` reshaped to the pure XSD form (`AUTOSAR_00052.xsd line 23449 (xsd:group COUPLING-PORT-ABSTRACT-SHAPER, atp.Status="candidate"; XSD-only, no Class/Enumeration table in the repo corpora)` — dropped the bogus PDF/release token); the 3 registry-helper docstrings added (repo-mechanism role — no spec Note exists for them, empty XSD sequence); checklist rows corrected to `[x] test` and put in source order; class docstring = XSD `<xsd:documentation>` verbatim; abstract class ⇒ no own XML element ⇒ reader/writer `[—]`. No `# XSD verified:` marker (9b gate). `CouplingPortFifo`'s own Group16 row owns the SHAPER-choice round-trip coverage.

**Superseded 2026-10-04 (registry retired, user-approved):** this entry previously carried an **accepted deviation** for `_shaper_registry` + `registerShaper`/`getShaperClass`/`getShaperTag` — a tag↔class registry the two concrete children populated at import time (originally arbitrated 2026-09-30). The registry is **deleted**: `readCouplingPortFifoShaper` now compares the element name against the two XSD tags directly and `writeCouplingPortFifoShaper` picks the tag from the instance type, so the mapping mirrors the `xsd:choice` instead of abstracting it. That removed the mutable class-level global state, the import-order dependency (a missing registration silently dropped shapers on write), and the registry-only test fixture. The three helper rows left the class checklist (4 rows → 1: `__init__`), and the untyped-accessor finding on the three helpers (Rule 0003) disappeared with them. Retirement of the *class* (ConcreteTDEventVfb pattern) remains rejected — unlike that case, the concrete children are real XSD classes.

## `InitialSdDelayConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 514  | **table:** Table 6.170
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all 4 Table 6.170 attributes are modeled with the PDF types and multiplicity (`TimeValue 0..1` × 3 → `Optional[TimeValue]`, `PositiveInteger 0..1` → `Optional[PositiveInteger]`), in the markdown displayed row order: `initialDelayMaxValue`, `initialDelayMinValue`, `initialRepetitionsBaseDelay`, `initialRepetitionsMax`. Base `ARObject` (spec `Base` column) ⇒ `__init__(self)` with all fields defaulted; no `create*`/`add*` (all four are `attr`, not `aggr`); reader/writer coverage for every kept attribute inside the matched `getInitialSdDelayConfig`/`setInitialSdDelayConfig` helper pair, with S/T checksum/timestamp via the matched `readARObject`/`writeARObject` pair; class/inline/getter/setter texts copied verbatim from the markdown `Note` cells. |

**Note:** Re-synced 2026-10-03 against R23-11 CP SystemTemplate Table 6.170, p.514 (markdown single un-split table block, lines 13506-13516; XSD group `INITIAL-SD-DELAY-CONFIG` `AUTOSAR_00052.xsd` L72399-72447 corroborates the attribute set, the `TimeValue`/`PositiveInteger` types and the element order 1:1). **Rule 0007 fix (the reason for this pass):** the spec `Package` row is `…::Fibex4Ethernet::ServiceInstances`, but the class was defined in `EthernetTopology.py`; it is now defined in `ServiceInstances.py` (user-approved relocation), removed from `EthernetTopology.py`, and all consumers re-pointed (`arxml_parser.py`, `arxml_writer.py`, the three model test modules). `EthernetTopology.SdClientConfig` still annotates `initialFindBehavior`, so the name is imported there under `TYPE_CHECKING` — the same shape the module already uses for `RequestResponseDelay`; no runtime import cycle is introduced. `armodel.InitialSdDelayConfig` still resolves (wildcard export via `models/__init__.py` L103). **Reader/writer gap closed:** the helper never called `readARObject`/`writeARObject`, so the `AR:AR-OBJECT` attributes (`S` checksum / `T` timestamp, XSD L4900-4912) were silently dropped on round-trip; both calls were added (parser L10173, writer L10226). Out-of-closure observations, not fixed here: (1) the sibling ARObject SD-config helpers `getRequestResponseDelay`/`setRequestResponseDelay`, `getSdClientConfig`/`setSdClientConfig`, `getSdServerConfig`/`setSdServerConfig` and `read/writeSomeipSdClientServiceInstanceConfig` still omit the same `readARObject`/`writeARObject` pair (siblings to reconcile in their own passes — Rule 0013.1); (2) `SomeipSdServerServiceInstanceConfig` — the fourth spec `Aggregated by` parent — exists only as a misplaced stub in `GenericStructure/GeneralTemplateClasses/ArObject.py` and has no parser/writer handler, so `InitialSdDelayConfig.initialOfferBehavior` is not round-tripped through that aggregator (Rule 0001.10 referenced class; own sync needed). The `# Spec verified: R23-11` stamp is withheld pending the 9b gate.

## `SdServerConfig`
- **PDF:** `AUTOSAR_TPS_SystemTemplate.pdf` (R4.3.1)  | **page:** 355  | **table:** Table 6.171
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `ttl` | `Optional[PositiveInteger]` | `ttl` | `PositiveInteger` | `attr` | type (PDF Mult 1 vs py Optional[PositiveInteger]; repo-wide Optional-for-required convention, 106:14 stamped precedent, user-confirmed 2026-10-03) |

**Note:** Re-synced 2026-10-03 against the R4.3.1 fallback corpus (Rule 0016.3 — verified there is **no** R23-11 table for the class: `grep "^Table [0-9.]*: SdServerConfig" autosar/R23-11/markdown/` is empty, and R23-11 Table 6.171 is `RequestResponseDelay`), Table 6.171, p.355 (body at markdown L8313-8325 below the L8311 caption — the nearby `RequestResponseDelay` `Class` row at L8372 belongs to a different table and was not merged). **Rule 0007 fix (the reason for this pass):** the spec `Package` row is `M2::…::Fibex4Ethernet::Ethernet Topology`, but the class was defined in `ServiceInstances.py`; it is now defined in `EthernetTopology.py` (user-approved relocation, placed directly before the sibling `SdClientConfig`), removed from `ServiceInstances.py`, and all consumers re-pointed (`arxml_parser.py` L1034, `arxml_writer.py` L929, `test_SdServerConfig.py`, `test_ServiceInstances.py`, `test_event_handler.py`, `test_writer_frame_channel.py`). `ServiceInstances.py` still annotates `EventHandler.sdServerConfig` and `ProvidedServiceInstance.sdServerConfig`, so `SdServerConfig` was added to that module's existing bottom-of-module cycle-breaker import (`# noqa: E402`, Rule 0005) — both import orders resolve, and `armodel.SdServerConfig` still resolves via the `models/__init__.py` L99 wildcard export. **Reader/writer gap closed:** `getSdServerConfig`/`setSdServerConfig` never covered the spec `capabilityRecord` (`* aggr`), so `CAPABILITY-RECORDS/TAG-WITH-OPTIONAL-VALUE` was silently dropped in both directions; the reader now iterates `getTagWithOptionalValues` → `addCapabilityRecord` (parser L10230-10231) and the writer calls `setTagWithOptionalValues` (writer L10235), in XSD `sequenceOffset` order (group `SD-SERVER-CONFIG`, `AUTOSAR_00044.xsd` L72991-73048). All 7 Table 6.171 attributes are now covered in both directions inside the shared helper pair. **Docstrings:** all class/method docstrings and `__init__` member comments were wiped (verified `__doc__ is None` for the class and all 14 methods) and rewritten from the markdown `Note` cells — every one of the 22 texts diffs clean character-for-character. **Closed at the 9b gate (this class's own compliance — not scope creep):** (a) the helper now calls `readARObject`/`writeARObject`, so the `AR:AR-OBJECT` `S`/`T` attributes (XSD L4900-4912) round-trip again (parser L10230 / writer L10235), pinned by `test_round_trip_preserves_arobject_checksum_and_timestamp`; (b) the `capabilityRecord` accessor pair is **mutator-first** (`addCapabilityRecord` then `getCapabilityRecords`) in both source and checklist, per Rule 0001.11. Still open in *other* classes (reported, not touched): `ProvidedServiceInstance.getSdServerConfig`/`setSdServerConfig` are untyped accessors (no return/parameter annotations; Rule 0001.3) — a `ProvidedServiceInstance`-sync item. Rule 0001.10 references: `TagWithOptionalValue` (Table 6.159, stamped `# Spec verified: R23-11`), `InitialSdDelayConfig` (Table 6.170, stamped `R23-11`), `RequestResponseDelay` (Table 6.171 R23-11, spec-faithful 6-column checklist but **not yet stamped** — pending 9b in the Group16 queue), `TimeValue`/`PositiveInteger` (primitives, exist). The `# Spec verified: R4.3.1` stamp is withheld pending the 9b gate.

## `NetworkEndpoint`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 463  | **table:** Table 6.134
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all 5 Table 6.134 attributes are modeled with the PDF types and multiplicity (`String 0..1` → `Optional[String]`, `InfrastructureServices 0..1` → `Optional[InfrastructureServices]`, `IPSecConfig 0..1` → `Optional[IPSecConfig]`, `NetworkEndpointAddress *` → `List[NetworkEndpointAddress]`, `PositiveInteger 0..1` → `Optional[PositiveInteger]`), in the markdown displayed row order: `fullyQualifiedDomainName`, `infrastructureServices`, `ipSecConfig`, `networkEndpointAddress`, `priority`. Base `ARObject , Identifiable , MultilanguageReferrable , Referrable` ⇒ most-derived Python base `Identifiable`, `__init__(self, parent, short_name)`. `networkEndpointAddress` is a `*` aggr of a non-`Referrable` child (`NetworkEndpointAddress(ARObject, ABC)`), so it keeps `addNetworkEndpointAddress`/`getNetworkEndpointAddresses` (Rule 0001.6) and the pair is **mutator-first** (Rule 0001.11). |

**Note:** Re-synced 2026-10-03 against R23-11 CP SystemTemplate Table 6.134, p.463 (markdown `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` L12286 caption + body L12288-12299; XSD group `NETWORK-ENDPOINT` `AUTOSAR_00052.xsd` L84066-84111 corroborates the attribute set, types and element order 1:1). **Rule 0001.7 coverage gap closed (the reason for this pass):** `FULLY-QUALIFIED-DOMAIN-NAME` appeared in neither `arxml_parser.py` nor `arxml_writer.py` — the field + accessor pair existed and the checklist claimed `[x] reader`/`[x] writer`, but the attribute was silently dropped on round-trip. The reader now sets `end_point.setFullyQualifiedDomainName(self.getChildElementOptionalString(element, "FULLY-QUALIFIED-DOMAIN-NAME"))` and the writer emits `self.setChildElementOptionalString(child_element, "FULLY-QUALIFIED-DOMAIN-NAME", end_point.getFullyQualifiedDomainName())`, both **first** in the matched `readNetworkEndPoint`/`writeNetworkEndPoint` pair — XSD `sequenceOffset` 1, before `INFRASTRUCTURE-SERVICES` (the other four elements follow in XSD order: INFRASTRUCTURE-SERVICES, IP-SEC-CONFIG, NETWORK-ENDPOINT-ADDRESSES, PRIORITY). Leaf pair `getChildElementOptionalString`/`setChildElementOptionalString` matches (Rule 0013.2); no chained mutator calls (Rule 0013). **Stale checklist rows corrected:** `getIpSecConfig`/`setIpSecConfig` were marked `[—] reader`/`[—] writer` although the helpers wire `IP-SEC-CONFIG` (parser L9877-9881, writer L9927-9929); they now read `[x] writer` on the getter and `[x] reader` on the setter. **Rule 0006 mirror-test gap closed:** `getNetworkEndpointAddresses` was never asserted in `test_NetworkEndpoint.py`; the mirror test now asserts the `[]` default, append/return/None-no-op, `getFullyQualifiedDomainName().getValue()`, and typing pins. **Docstrings:** all class/method docstrings and the `__init__` member comments were wiped and rewritten from the markdown `Note` cells; the `Tags: xml.namePlural=NETWORK-ENDPOINT-ADDRESSES` tail on the `networkEndpointAddress` Note was dropped per Rule 0012.2.5.2 (the other four notes were already verbatim). No referenced-class placeholder remains (`InfrastructureServices`, `IPSecConfig`, `NetworkEndpointAddress` all exist and are stamped/pending their own 9b). The `# Spec verified: R23-11` stamp is withheld pending the 9b gate.

## `Ipv4Configuration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 465  | **table:** Table 6.136
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all 8 Table 6.136 attributes are modeled with the PDF types and multiplicity (7×`0..1` → `Optional[T]`; `dnsServerAddress *` → `List[Ip4AddressString]`), in the markdown displayed row order: `assignmentPriority`, `defaultGateway`, `dnsServerAddress`, `ipAddressKeepBehavior`, `ipv4Address`, `ipv4AddressSource`, `networkMask`, `ttl`. Base `ARObject , NetworkEndpointAddress` ⇒ most-derived Python base `NetworkEndpointAddress`, `__init__(self)`. The `dnsServerAddress` list pair is mutator-first (`addDnsServerAddress`/`getDnsServerAddresses`, Rule 0001.11); the seven scalars are getter-first. |

**Note:** Re-synced 2026-10-03 against R23-11 CP SystemTemplate Table 6.136, p.465 (markdown `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` L12339 Class header, L12342 Note, L12343 Base, L12345 attribute header, L12346-12353 the 8 attribute rows, caption L12355; XSD group `IPV-4-CONFIGURATION` `AUTOSAR_00052.xsd` L74157-74219 corroborates the attribute set, types and element order 1:1). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.465` is taken from the pre-existing `# Spec:` line and the plan Task 8 interface. **Rule 0006 fix (the reason for this pass):** the mirror test called `addDnsServerAddress` but never asserted `getDnsServerAddresses()` — the list contents and the `[]` default were unverified; the mirror test now asserts the `[]` default, append/return/None-no-op via the getter, and the mutator-first source order. **Rule 0001.11 fix:** the `dnsServerAddress` list accessor pair was getter-first; reordered **mutator-first** (`addDnsServerAddress` before `getDnsServerAddresses`) in source and checklist. **Rule 0013.2/0001.3 fix:** `getIpv4Configuration` stored plain `ARLiteral` for the four spec `Ip4AddressString` fields (`DEFAULT-GATEWAY`, `IPV-4-ADDRESS`, `NETWORK-MASK`, and the `DNS-SERVER-ADDRESS` items) and for `IPV-4-ADDRESS-SOURCE` (never wrapped into `Ipv4AddressSourceEnum`) — inconsistent with the `Ipv6Configuration` sibling and the `readIpv4Rule` pattern; the reader now materialises `Ip4AddressString()` and `Ipv4AddressSourceEnum()` (parser L9760+). XSD `sequenceOffset` order preserved: ASSIGNMENT-PRIORITY, DEFAULT-GATEWAY, DNS-SERVER-ADDRESSES, IP-ADDRESS-KEEP-BEHAVIOR, IPV-4-ADDRESS, IPV-4-ADDRESS-SOURCE, NETWORK-MASK, TTL. The accessor groups, class member order and checklist rows follow the markdown displayed order; the class docstring, all 8 attribute inline comments and the getter/setter docstrings were wiped then rewritten verbatim from the Table 6.136 `Note` cells; `__init__` has no docstring; the `Tags: xml.namePlural=DNS-SERVER-ADDRESSES` tail was dropped from the `dnsServerAddress` docstrings. **Report-only (other classes, untouched):** `Ipv6Configuration` (`EthernetTopology.py`) reads its `Ip6AddressString` fields (`defaultRouter`, `ipv6Address`, dns items) through the generic literal reader with the same Rule 0013.2 pattern — its own sync item.

## `TimeSyncServerConfiguration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 470  | **table:** Table 6.147
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all 4 Table 6.147 attributes are modeled with the PDF types and multiplicity (`PositiveInteger 0..1` → `Optional[PositiveInteger]`, `TimeValue 0..1` → `Optional[TimeValue]`, `String 0..1` → `Optional[String]`, `TimeSyncTechnologyEnum 0..1` → `Optional[TimeSyncTechnologyEnum]`), in the markdown displayed row order: `priority`, `syncInterval`, `timeSyncServerIdentifier`, `timeSyncTechnology`. Base `ARObject , Referrable` ⇒ most-derived Python base `Referrable`, `__init__(self, parent, short_name)`. All four are `attr` (no `create*`/`add*`); the scalar accessor pairs are getter-first (Rule 0001.11). |

**Note:** Re-synced 2026-10-03 against R23-11 CP SystemTemplate Table 6.147, p.470 (markdown `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` L12528 caption + body L12530-12538; XSD group `TIME-SYNC-SERVER-CONFIGURATION` `AUTOSAR_00052.xsd` L123140-123173 corroborates the attribute set, types and element order 1:1). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.470` is taken from the pre-existing `# Spec:` line and the plan Task 5 interface. **Rule 0001.7 coverage gap closed (the reason for this pass):** the parser's `TIME-SYNC-SERVER` branch inside `getTimeSynchronization` set **only** `setTimeSyncTechnology`, and the writer's server branch inside `setTimeSynchronization` wrote **only** `TIME-SYNC-TECHNOLOGY`; `PRIORITY`, `SYNC-INTERVAL` and `TIME-SYNC-SERVER-IDENTIFIER` were read/written nowhere, so 3 of 4 attributes were silently dropped while the checklist claimed `[x] reader`/`[x] writer`. The reader now additionally sets `server.setPriority(getChildElementOptionalPositiveInteger(..., "PRIORITY"))`, `server.setSyncInterval(getChildElementOptionalTimeValue(..., "SYNC-INTERVAL"))` and `server.setTimeSyncServerIdentifier(getChildElementOptionalString(..., "TIME-SYNC-SERVER-IDENTIFIER"))` (parser L9848-9853); the writer now additionally emits `PRIORITY`, `SYNC-INTERVAL` and `TIME-SYNC-SERVER-IDENTIFIER` (writer L9902-9905) — all in XSD `sequenceOffset` order `PRIORITY, SYNC-INTERVAL, TIME-SYNC-SERVER-IDENTIFIER, TIME-SYNC-TECHNOLOGY`. Leaf pairs are matched (`getChildElementOptionalPositiveInteger`/`setChildElementOptionalPositiveInteger`, `…TimeValue`/`…TimeValue`, `…String`/`…String`, Rule 0013.2); no chained mutator calls (Rule 0013). **Malformed-checklist repair:** the class carried only the `__init__` row in the top block, with the eight accessor rows misplaced *inside* `__init__` as the member comments above each `self.` assignment; the accessor rows were removed from `__init__` and the full 6-column block was rebuilt at the top in source order, with the member comments now the verbatim spec `Note`. **Docstrings:** the misplaced rows were wiped from `__init__`; the class docstring and all eight accessor docstrings were re-verified character-for-character against the markdown `Note` cells (already verbatim from the prior pass — no textual delta), and guarded setters keep the None-no-op sentence. **Tests:** new `tests/test_armodel/parser/test_time_sync_server_configuration.py` and `tests/test_armodel/writer/test_time_sync_server_configuration.py` assert all four field values in both directions plus the absent case; the mirror test was strengthened to use typed primitives and a getter-first order pin (Rule 0006). **Reported, not fixed (other classes' items):** `TimeSynchronization.timeSyncServer` is a `0..1 aggr` of a `Referrable` child but exposes `setTimeSyncServer`/`getTimeSyncServer` instead of `createTimeSyncServer(short_name)`/`getTimeSyncServer()` — a Rule 0001.6 shape violation in the sibling aggregator (`TimeSynchronization` has its own Group16 row / own queue entry; deliberately not touched here). The `# Spec verified: R23-11` stamp is withheld pending the 9b gate.

## `IPv6ExtHeaderFilterList`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 456  | **table:** Table 6.121
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/IPv6HeaderFilterList.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 6.121 attribute `allowedIPv6ExtHeader` (`PositiveInteger *`, `attr`) is modeled as `List[PositiveInteger]` + the mutator-first pair `addAllowedIPv6ExtHeader`/`getAllowedIPv6ExtHeaders` (Rules 0001.4/0011). Base `ARObject , Identifiable , MultilanguageReferrable , Referrable` ⇒ most-derived Python base `Identifiable`, `__init__(self, parent, short_name)`. |

**Note:** Re-synced 2026-10-03 against R23-11 CP SystemTemplate Table 6.121, p.456 (markdown `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` — header block L12031-12036, split attribute block below the L12042 caption at L12044-12047; XSD group `I-PV-6-EXT-HEADER-FILTER-LIST` `AUTOSAR_00052.xsd` L66599-66618 corroborates the attribute, `AR:POSITIVE-INTEGER` item type and wrapper). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.456` is taken from the pre-existing `# Spec:` line and the plan Task 6 interface. **Rule 0001.7 wrapper-list reader/writer added (the reason for this pass):** the prior checklist marked reader/writer `[—]` on the justification "consumed as ref target via `ALLOWED-I-PV-6-EXT-HEADERS-REF`" — that was **wrong**: the table lists `allowedIPv6ExtHeader` as an `attr`, and the XSD defines the class's own `ALLOWED-I-PV-6-EXT-HEADERS` wrapper of unbounded `ALLOWED-I-PV-6-EXT-HEADER` items (L66606-66616); the `…-REF` element (L107861/L108070) belongs to `SocketAddress`/`SocketConnection`, not this class. The matched pair is now `readIPv6ExtHeaderFilterList` (parser; `readIdentifiable` + iterate the wrapper via `getChildElementPositiveIntegerValueList` → `addAllowedIPv6ExtHeader`) and `writeIPv6ExtHeaderFilterList` (writer; `writeIdentifiable` + emit the wrapper **only when non-empty**, one `setChildElementOptionalPositiveInteger` item per entry) — matched leaf pair (Rule 0013.2), no chained mutator calls (Rule 0013). **Rule 0003 fix:** `addAllowedIPv6ExtHeader` returned the quoted `"IPv6ExtHeaderFilterList"`; the module now carries `from __future__ import annotations` (it had none) and the return annotation is the bare `IPv6ExtHeaderFilterList`; the module has no other quoted signature, and `test_pep563_annotations.py` / `test_member_annotations.py` both cover it now. The list accessor pair was also reordered **mutator-first** (`addAllowedIPv6ExtHeader` then `getAllowedIPv6ExtHeaders`, Rule 0001.11). **Docstrings:** class docstring + `__init__` member comment + both accessor docstrings diffed verbatim against the markdown `Note` cells; `__init__` has no docstring; no legacy checklist rows lived inside `__init__`. **Reported, not fixed (other classes' items, Rule 0001.10):** `IPv6ExtHeaderFilterSet` — the spec `Aggregated by` parent — is a `pass` stub in `GenericStructure/GeneralTemplateClasses/ARPackage.py` L9695 with no parser/writer handler, so the wrapper list is not reachable through the full `EXT-HEADER-FILTER-LISTS` aggregator (the class's own helper pair is covered directly by the Step-5 tests); it needs its own sync pass. Report-only sibling: `TcpOptionFilterList` has the same wrapper-list shape but its accessor pair is **getter-first** (Rule 0001.11) — its own Group16 row (Task 7) owns that fix. The `# Spec verified: R23-11` stamp is withheld pending the 9b gate.

## `TcpOptionFilterList`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 457  | **table:** Table 6.123
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/TcpOptionFilterSet.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 6.123 attribute `allowedTcpOption` (`PositiveInteger *`, `attr`) is modeled as `List[PositiveInteger]` + the mutator-first pair `addAllowedTcpOption`/`getAllowedTcpOptions` (Rules 0001.4/0011). Base `ARObject , Identifiable , MultilanguageReferrable , Referrable` ⇒ most-derived Python base `Identifiable`, `__init__(self, parent, short_name)`. |

**Note:** Re-synced 2026-10-03 against R23-11 CP SystemTemplate Table 6.123, p.457 (markdown `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` — caption `Table 6.123: TcpOptionFilterList` L12074, body Class `TcpOptionFilterList` L12076-12083; XSD group `TCP-OPTION-FILTER-LIST` `AUTOSAR_00052.xsd` L120400-120419 corroborates the `ALLOWED-TCP-OPTIONS` wrapper of unbounded `AR:POSITIVE-INTEGER` `ALLOWED-TCP-OPTION` items and the `AR:AR-OBJECT`+`AR:IDENTIFIABLE` attribute groups). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.457` is taken from the pre-existing `# Spec:` line and the plan Task 7 interface. **Rule 0003 fix (the reason for this pass):** `addAllowedTcpOption` returned the quoted `"TcpOptionFilterList"`; the module had no `from __future__ import annotations`, so the future import was added and the return annotation is now the bare `TcpOptionFilterList` — the module has no other quoted signature, and `test_pep563_annotations.py` / `test_member_annotations.py` cover it. **Rule 0001.11 fix:** the list accessor pair was getter-first; reordered **mutator-first** (`addAllowedTcpOption` then `getAllowedTcpOptions`) in both source and checklist. **Rule 0001.7 verify:** the reader `readTcpOptionFilterList` (parser L9988) and writer `writeTcpOptionFilterList` (writer L10019) are this class's own helpers, reached via `readTcpOptionFilterSet`/`writeTcpOptionFilterSet` and the ARPackage dispatch (parser L16671, writer L16097); wrapper/item element names match the XSD. The reader was upgraded from the generic `getChildElementNumericalValueList` + manual `PositiveInteger` wrap to the spec-typed `getChildElementPositiveIntegerValueList`, the matched pair of the writer's `setChildElementOptionalPositiveInteger` (Rule 0013.2); no chained mutator calls (Rule 0013). **Docstrings:** class docstring, the attribute inline comment and both accessor docstrings were wiped then rewritten verbatim from the Table 6.123 `Note` cells ("Permitted list for the filtering of TCP options." / "TCP option kind allowed by this filter." with the guarded-append no-op sentence); `__init__` has no docstring; the checklist is a single 6-column block at the top in source order.

## `SocketConnectionIpduIdentifier`
- **PDF:** `AUTOSAR_TPS_SystemTemplate.pdf` (R4.3.1)  | **page:** 321  | **table:** Table 6.122
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Ethernet Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all 6 Table 6.122 attributes are modeled with the PDF types and multiplicity (`headerId` `PositiveInteger 0..1` → `Optional[PositiveInteger]`, `pduCollectionPduTimeout` `TimeValue 0..1` → `Optional[TimeValue]`, `pduCollectionSemantics` `PduCollectionSemanticsEnum 0..1` → `Optional[PduCollectionSemanticsEnum]`, `pduCollectionTrigger` `PduCollectionTriggerEnum 0..1` → `Optional[PduCollectionTriggerEnum]`, `pduTriggering` `PduTriggering 0..1 ref` → `Optional[RefType]` `pduTriggeringRef`, `routingGroup` `SoAdRoutingGroup * ref` → `List[RefType]` `routingGroupRefs` + mutator-first `addRoutingGroupRef`/`getRoutingGroupRefs`), in the markdown displayed row order. Base `ARObject` (only) ⇒ `__init__(self)`. The XSD `PDU-REF` element (`AUTOSAR_00052.xsd` L108406, `atp.Status="removed"`) is **not** modeled. |

**Note:** Re-synced 2026-10-03 against the R4.3.1 corpus (Rule 0016.3 class-scoped fallback — no R23-11 table for this class), `autosar/R4.3.1/markdown/AUTOSAR_TPS_SystemTemplate.md` Table 6.122 (caption L7451, body L7453-7464). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.321` is taken from the pre-existing `# Spec:` line and the plan Task 9 interface. Defects fixed this pass: **(1) Rule 0006** — the mirror test was misnamed `test_SocketConnectionIpduIdentifier2.py`; `git mv`'d to `test_SocketConnectionIpduIdentifier.py` keeping `class TestSocketConnectionIpduIdentifier`. **(2) Rule 0001.4/0001.6/0001.11** — `routingGroup` (`* ref`) was modeled with a `setRoutingGroupRefs(List)` setter instead of the required plural getter + `addXxx` mutator; replaced with `addRoutingGroupRef(value)` and reordered **mutator-first** (the sibling `AbstractServiceInstance`/`ConsumedEventGroup` shapes). The parser's own `getSocketConnectionIpduIdentifier` was updated (`setRoutingGroupRefs(list)` → a loop of `addRoutingGroupRef(ref)`); the writer's own path is `setSocketConnectionIpduIdentifier` (L9954) and already called `getRoutingGroupRefs()` — the other four `getRoutingGroupRefs()` writer call sites belong to other classes and were untouched. Consumers updated: `tests/.../test_EthernetCommunication.py`, `tests/test_armodel/writer/test_so_ad_config.py`. **(3) Rule 0001.3** — the previously-fabricated `PduRef` member / `PDU-REF` reader-writer wiring remains removed (the element is `atp.Status="removed"` in both XSDs). Docstrings/comments re-verified verbatim against the R4.3.1 `Note` cells; `# Spec:` normalized to `AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.122, p.321` (dropped the `R4.3.1/` prefix and trailing `(R4.3.1)`); checklist rebuilt as a single 6-column block at the top, 13 rows source order, every row `R4.3.1`.

## `SocketConnectionBundle`
- **PDF:** `AUTOSAR_TPS_SystemTemplate.pdf` (R4.3.1)  | **page:** 316  | **table:** Table 6.118
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Ethernet Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `serverPortRef` | `Optional[RefType]` | `serverPort` | `SocketAddress` | `ref` | type (PDF Mult 1 vs py Optional[RefType]; repo-wide Optional-for-required convention, 106:14 stamped precedent, user-confirmed 2026-10-03) |

**Note:** Re-synced 2026-10-03 against the R4.3.1 corpus (Rule 0016.3 class-scoped fallback — no R23-11 table for this class), `autosar/R4.3.1/markdown/AUTOSAR_TPS_SystemTemplate.md` Table 6.118 (body L7352-7364, caption L7366 — the R4.3.1 markdown renders the table body **before** its caption; the header block at L7352-7357 confirms `Class SocketConnectionBundle`, Package `…::Ethernet Communication`, Note, and `Base = ARObject, Referrable`). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.316` is taken from the pre-existing `# Spec:` line and the plan Task 10 interface. All 7 Table 6.118 attributes are modeled with the spec types and multiplicity (`bundledConnection` `SocketConnection 1..*` → `List[SocketConnection]` + mutator-first `addBundledConnection`/`getBundledConnections`; `differentiatedServiceField`/`flowLabel` `PositiveInteger 0..1` → `Optional[PositiveInteger]`; `pathMtuDiscoveryEnabled` `Boolean 0..1` → `Optional[Boolean]`; `pdu` `SocketConnectionIpduIdentifier *` → `List[SocketConnectionIpduIdentifier]` + mutator-first `addPdu`/`getPdus`; `serverPort` `SocketAddress 1 ref` → `serverPortRef` (accepted deviation above); `udpChecksumHandling` `UdpChecksumCalculationEnum 0..1` → `Optional[UdpChecksumCalculationEnum]`), in the markdown displayed row order. Base `ARObject, Referrable` ⇒ most-derived Python base `Referrable`, `__init__(self, parent, short_name)`. Defects fixed this pass: **(1) Rule 0006** — the mirror test was misnamed `test_SocketConnectionBundle2.py`; `git mv`'d to `test_SocketConnectionBundle.py` keeping `class TestSocketConnectionBundle`. **(2) Rule 0001.11** — both list accessor pairs (`bundledConnections`, `pdus`) were getter-first; reordered **mutator-first** in source and checklist (`addBundledConnection` before `getBundledConnections`, `addPdu` before `getPdus`). **(3) Rule 0013.1/0001.7** — `readSocketConnectionBundle` never called the direct base's reader helper, while `writeSocketConnectionBundle` always calls `writeReferrable`; the `AR:AR-OBJECT` `S`/`T` attributes (XSD `SOCKET-CONNECTION-BUNDLE` complexType refs `AR:AR-OBJECT` + `AR:REFERRABLE`, `AUTOSAR_00044.xsd` L77923-77935) were therefore silently dropped on round-trip. The reader now calls `self.readReferrable(element, bundle)` (parser L9980) — matched with the writer's `writeReferrable`, no double-registration (`createSocketConnectionBundle` appends to the owning `connectionBundles` list and does not call `addARObject`), no chained mutator calls. All 7 attributes remain covered in both directions inside the matched `readSocketConnectionBundle`/`writeSocketConnectionBundle` helper pair; aggregated children asserted one level down (`SocketConnection.shortLabel`/`runtimePortConfiguration`, `SocketConnectionIpduIdentifier.headerId`). **Docstrings:** the class docstring, all 7 `__init__` member comments and the getter/setter docstrings were re-verified verbatim against the R4.3.1 `Note` cells (no textual delta; setters append the None-no-op sentence); `__init__` has no docstring and there are no legacy checklist rows inside `__init__`. `# Spec:` normalized to `AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.118, p.316` (dropped the `R4.3.1/` prefix and trailing `(R4.3.1)`); checklist rebuilt as a single 6-column block at the top, 15 rows source order, every row `R4.3.1`. **Report-only (other classes / out of scope):** (a) the module header comment `EthernetCommunication.py` L5-8 still cites stale R4.3.1 table ids for the sibling classes `IPv6ExtHeaderFilterList` (listed 6.129, R23-11 id 6.121), `TcpOptionFilterSet` (listed 6.130, R23-11 id 6.122) and `TcpOptionFilterList` (listed 6.131, R23-11 id 6.123) — untouched (scope discipline); (b) **Rule 0020 (VariationPointCapable) — IMPLEMENTED this pass** (genuine gap, user-approved at the 9b gate): `SocketConnectionBundle` is the PartClass of the `SoAdConfig.connectionBundle` `* aggr` row whose Note carries `Stereotypes: atpVariation` (markdown L7342), and its own XSD complexType carries `<xsd:element name="VARIATION-POINT" type="AR:VARIATION-POINT">` (`AUTOSAR_00044.xsd` L77914, `xml.sequenceOffset="10000"`, LAST). The class now inherits `VariationPointCapable` — `class SocketConnectionBundle(Referrable, VariationPointCapable)` — and `readSocketConnectionBundle`/`writeSocketConnectionBundle` call `readVariationPointCapable`/`writeVariationPointCapable` explicitly (the non-`Identifiable` base helpers `readReferrable`/`writeReferrable` do NOT gate VP, unlike `readIdentifiable`/`writeIdentifiable`; VARIATION-POINT is written LAST per `sequenceOffset=10000`). The checklist carries no variationPoint rows (mixin annotation line only, per Rule 0020). Pinned by `test_variation_point_capable_mixin`, `test_readSocketConnectionBundle_reads_variation_point`, `test_round_trip_variation_point_is_last_element`. Tracked anchor: `docs/superpowers/plans/vp_anchors.txt` L278.

## `EthernetPriorityRegeneration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 128  | **table:** Table 3.74
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 3.74 attributes are modeled with the PDF types and multiplicity (`ingressPriority` `PositiveInteger 0..1` → `Optional[PositiveInteger]`, `regeneratedPriority` `PositiveInteger 0..1` → `Optional[PositiveInteger]`), in the markdown displayed row order. Base `ARObject , Referrable` ⇒ most-derived Python base `Referrable`, `__init__(self, parent, short_name)`. Both attributes are covered in the reader (`INGRESS-PRIORITY`/`REGENERATED-PRIORITY`) and the writer. |

**Note:** Re-synced 2026-10-03 (Group16 Task 12; no `# Spec verified:` marker ⇒ full 9-step re-run), `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` Table 3.74 (caption L3440, body L3442-3450). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.128` is taken from the pre-existing `# Spec:` line and the plan interface. Defects fixed this pass: **(1) Rule 0013.1/0001.7** — `readEthernetPriorityRegeneration` never called the base `readReferrable`, while `writeEthernetPriorityRegeneration` did call `writeReferrable`; the inherited `AR:AR-OBJECT` `S`/`T` (and `SHORT-NAME-FRAGMENTS`) were dropped on round-trip. Added `self.readReferrable(element, regeneration)` (parser L13791); single caller (the aggregator L13800), no double-registration (class is `Referrable`, not `Identifiable`). **(2) Rule 0002** — the checklist was malformed (only the `__init__` row at the top; the four accessor rows were scattered inside `__init__` as member comments); rebuilt as a single 6-column block at the top with rows in source order, every row `[x]`. **(3)** dropped the stale ` (R23-11)` suffix from the `# Spec:` line. **(4) Rule 0006** — the mirror test passed a bare `int` (`setIngressPriority(7)`); rewritten with typed `PositiveInteger().setValue("7")` plus a getter-first source-order pin. Docstrings/comments wiped (`__doc__ is None` verified for class + `__init__` + 4 accessors) then rewritten verbatim from the Table 3.74 `Note` cells. New tests: `tests/test_armodel/parser/test_ethernet_priority_regeneration.py` (4) + `tests/test_armodel/writer/test_ethernet_priority_regeneration.py` (4); RED was 2 failed / 6 passed (S/T dropped), GREEN 8 passed. No open deviation; **no** `# Spec verified:` marker written (9b gate). Report-only (other classes, untouched): sibling `CouplingPortTrafficClassAssignment` (Table 3.75) declares `priority` as `PositiveInteger 0..8` `attr`; its own sync row is separate.

## `TimeSynchronization`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 469  | **table:** Table 6.145
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 6.145 attributes are modeled with the PDF types and multiplicity (`timeSyncClient` `TimeSyncClientConfiguration 0..1 aggr` → `Optional[TimeSyncClientConfiguration]` + scalar getter-first `getTimeSyncClient`/`setTimeSyncClient` (child Base `ARObject`, Table 6.146); `timeSyncServer` `TimeSyncServerConfiguration 0..1 aggr` → `Optional[TimeSyncServerConfiguration]` + factory mutator-first `createTimeSyncServer(short_name)`/`getTimeSyncServer` (child Base `ARObject , Referrable`, Table 6.147)), in the markdown displayed row order. Base `ARObject` (only) ⇒ `__init__(self)`. Both attributes are covered in the reader (`TIME-SYNC-CLIENT` / `TIME-SYNC-SERVER`) and the writer, in XSD `sequenceOffset` order (`TIME-SYNC-CLIENT` then `TIME-SYNC-SERVER`). |

**Note:** Re-synced 2026-10-03 (Group16 Task 13; no `# Spec verified:` marker ⇒ full 9-step re-run), `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` Table 6.145 (header block L12495-12500, attribute rows L12502-12503, caption L12505; XSD group `TIME-SYNCHRONIZATION` `AUTOSAR_00052.xsd` L123194). `pdf_page.py` could not run (the shared venv lacks `pypdf`), so `p.469` is taken from the pre-existing `# Spec:` line and the plan Task 13 interface. Defects fixed this pass: **(1) Rule 0001.6** — `timeSyncServer` was exposed as `setTimeSyncServer`/`getTimeSyncServer`, but its child `TimeSyncServerConfiguration` has `Base = ARObject , Referrable` (Table 6.147), so a `0..1` `Referrable` child requires the factory shape; replaced with `createTimeSyncServer(short_name)` (returns the existing child when the short name matches, else constructs `TimeSyncServerConfiguration(self, short_name)`) + `getTimeSyncServer()`. `timeSyncClient` keeps `set`/`get` (child Base `ARObject`, Table 6.146). **(2) Rule 0002** — the checklist was malformed (only the `__init__` row at the top; the accessor rows were scattered inside `__init__` as member comments); rebuilt as a single 6-column block at the top, 5 rows in source order, scalar pair getter-first / factory pair mutator-first, `reader [x]` on the mutators and `writer [x]` on the getters, every row `R23-11`. **(3)** dropped the stale ` (R23-11)` suffix from the `# Spec:` line. **(4) Rule 0013.2** — the parser call site `ARXMLParser.getTimeSynchronization` (L9866-9878) still called the removed `sync.setTimeSyncServer(server)`; updated to `server = sync.createTimeSyncServer(self.getShortName(server_element))` (the `setTimeSyncServer` statement deleted; `readReferrable` + the four attribute reads unchanged), and the now-unused `TimeSyncServerConfiguration` import dropped (ruff F401). The writer `setTimeSynchronization` (L9894) needed no change — it already reads via `getTimeSyncClient()`/`getTimeSyncServer()` and emits `TIME-SYNC-CLIENT` before `TIME-SYNC-SERVER` per XSD `sequenceOffset`. **(5) Rule 0012.2.3** — all docstrings and inline `__init__` member comments were wiped (`__init__` docstring absent) then rewritten verbatim from the Table 6.145 `Note` cells; the wipe-then-rewrite round-tripped byte-identically to the pre-Step-4 text (md5 `533162d995b463af834aaa5aec894568`). Tests: mirror `test_TimeSynchronization.py` 7 passed; reader `tests/test_armodel/parser/test_time_sync_server_configuration.py` (5) + writer `tests/test_armodel/writer/test_time_sync_server_configuration.py` (6); RED 3 failed / 15 passed (all three `AttributeError: 'TimeSynchronization' object has no attribute 'setTimeSyncServer'`, parser L9878) → GREEN 18 passed. A **4th stale call site** outside the reader/writer test pair was also found and fixed: the class-level test `tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/test_EthernetTopology.py::Test_Fibex4EthernetNetworkEndpoint::test_TimeSynchronization` (L1312-1333) still called the removed `setTimeSyncServer`; rewritten to the `createTimeSyncServer` factory shape (plus short-name and parent assertions). Broader regression run over `Fibex4Ethernet/` + `parser/` + `writer/` = 7900 passed. No open deviation; **no** `# Spec verified:` marker written (withheld pending the 9b gate). **No Rule 0001.10 report-only item:** the referenced classes `TimeSyncClientConfiguration` (Table 6.146), `TimeSyncServerConfiguration` (Table 6.147), `TimeSyncTechnologyEnum` and `OrderedMaster` all already carry `# Spec verified: R23-11`.

## `EcucIndexableValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 110
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.46 attribute `index` (`PositiveInteger 0..1 attr`) is modeled as `index: Optional[PositiveInteger]` with the getIndex/setIndex pair (None no-op, chaining). Base stays `ARObject` (most-derived of the spec Base chain; abstract class, guarded instantiation). |

**Note:** Batch sync 2026-10-04 (Group27 batch 2; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.46, p.110 (abstract Class; Note "Used to support the specification of ordering of parameter values."; Base ARObject; subclasses EcucAbstractReferenceValue, EcucContainerValue, EcucParameterValue) and the XSD group ECUC-INDEXABLE-VALUE (AUTOSAR_00052.xsd l.52461; INDEX, sequenceOffset=-5). Abstract XML-bearing base per Rule 0001.7: now owns the reusable `readEcucIndexableValue`/`writeEcucIndexableValue` helpers; the previously inline-duplicated INDEX handling was replaced by helper calls in `readEcucParameterValue`/`readEcucAbstractReferenceValue`/`readEcucContainerValue` and `writeEcucParameterValue`/`writeEcucAbstractReferenceValue`/`writeEcucContainValue` (XML element order unchanged). Round-trip coverage rides the concrete subclasses (the group has no standalone element). No open deviations.

## `EcucModuleConfigurationValues`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 111
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all six Table 2.47 attributes are modeled with the PDF types and multiplicity in display order (`container` `EcucContainerValue * aggr` → `containers: List[EcucContainerValue]` + createContainer/getContainers, dedicated typed list plus the registry duplicate check; `definition` `EcucModuleDef 0..1 ref` → `definitionRef: Optional[RefType]`; `ecucDefEdition` `RevisionLabelString 0..1 attr`; `implementationConfigVariant` `EcucConfigurationVariantEnum 0..1 attr`; `moduleDescription` `BswImplementation 0..1 ref` → `moduleDescriptionRef: Optional[RefType]`; `postBuildVariantUsed` `Boolean 0..1 attr`). The five 0..1 setters were Optional-ized (Rule 0001.4) and getContainers now returns the typed field directly (Rule 0004). Base stays `ARElement` (most-derived of the spec Base chain; XSD complexType group sequence AR-OBJECT→AR-ELEMENT confirms). |

**Note:** Batch sync 2026-10-04 (Group27 batch 2; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.47, p.111 (markdown table body split around the caption: Package/Note rows before it, Class/Base/Aggregated-by/Attribute rows after; PDF line-wrap spaces inside identifiers joined, e.g. "variation Point.shortLabel" → "variationPoint.shortLabel") and the XSD group ECUC-MODULE-CONFIGURATION-VALUES (AUTOSAR_00052.xsd l.52693; XML order DEFINITION-REF → ECUC-DEF-EDITION → IMPLEMENTATION-CONFIG-VARIANT → MODULE-DESCRIPTION-REF → POST-BUILD-VARIANT-USED → CONTAINERS, already followed by reader/writer). Writer fix: ECUC-DEF-EDITION now goes through the spec-typed `setChildElementOptionalRevisionLabelString` (matched Rule 0013.2 pair with the reader's `getChildElementOptionalRevisionLabelString`). EcucModuleDef/BswImplementation are ref destinations only — no Rule 0001.10 missing classes. No open deviations.

## `EcucParameterValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 125
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all Table 2.49 members are modeled with the PDF types and multiplicity in display order (`annotation` `Annotation * aggr` (page-split first-page fragment before the caption) → `annotations: List[Annotation]` + addAnnotation/getAnnotations; `definition` `EcucParameterDef 0..1 ref` → `definitionRef: Optional[RefType]`; `isAutoValue` `Boolean 0..1 attr`). Base most-derived `EcucIndexableValue` (page-split Base row `ARObject , EcucIndexableValue`). `variationPoint` deliberately NOT modeled: Table 2.49 has no variationPoint row and the VARIATION-POINT element in the XSD group ECUC-PARAMETER-VALUE is an atpVariation artifact documented "Applicable for: EcucContainerValue.parameterValue" — removed per Rule 0015 (PDF/markdown wins), including the writer emission and the reader call; no integration fixture carries VARIATION-POINT inside an ECUC param value. |

**Note:** Batch sync 2026-10-04 (Group27 batch 3, finished inline after the batch dispatch was stopped by the user; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.49, p.125 (abstract Class; class Note "Common class to all types of configuration values."; markdown table split around the caption: Base + annotation rows before it, definition + isAutoValue after) and the XSD complexType/group ECUC-PARAMETER-VALUE (XML order DEFINITION-REF → INDEX (group ECUC-INDEXABLE-VALUE) → ANNOTATION → IS-AUTO-VALUE, already followed by reader/writer). VariationPointCapable mixin dropped from the bases; writer `writeEcucParameterValue` no longer emits VARIATION-POINT and parser `readEcucParameterValue` no longer reads it (symmetric); setter docstrings moved to the batch-2 split-paragraph no-op style. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `EcucTextualParamValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 127
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.50 attribute `value` (`VerbatimString 0..1 attr`, Note "Value of the parameter, not subject to variant handling.") is modeled as `value: Optional[VerbatimString]` with the getValue/setValue pair (None no-op, chaining, split-paragraph setter docstring). Base most-derived `EcucParameterValue` (spec Base `ARObject , EcucIndexableValue , EcucParameterValue`); no VariationPointCapable (no aggr row). |

**Note:** Batch sync 2026-10-04 (Group27 batch 3; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.50, p.127 (concrete Class; no page-split rows) and the XSD group ECUC-TEXTUAL-PARAM-VALUE (AUTOSAR_00052.xsd l.53629; VALUE type AR:VERBATIM-STRING, 0..1). Writer fix: `writeEcucTextualParamValue` VALUE now goes through the spec-typed `setChildElementOptionalVerbatimString` (new one-line delegation in abstract_arxml_writer.py, matched Rule 0013.2 pair with the reader's `getChildElementOptionalVerbatimString`; was the generic `setChildElementOptionalLiteral`). Round-trip coverage in tests/test_armodel/writer/test_ecuc_textual_param_value.py asserts field values, VARIATION-POINT absence and the empty/minimal case. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `EcucNumericalParamValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 128
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.51 attribute `value` (`Numerical 0..1 attr`) is modeled as `value: Optional[Numerical]` with the getValue/setValue pair (None no-op, chaining, split-paragraph setter docstring); the full Note including the `atpVariation: [RS_ECUC_00080] Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime` tail is copied verbatim. Base most-derived `EcucParameterValue`; no VariationPointCapable (the atpVariation sits on the `value` attr row — attribute-value variation, Rule 0020 NOT-indicator, no class capability). |

**Note:** Batch sync 2026-10-04 (Group27 batch 3; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.51, p.128 (concrete Class; no page-split rows) and the XSD group ECUC-NUMERICAL-PARAM-VALUE (AUTOSAR_00052.xsd l.53047; VALUE element type AR:NUMERICAL-VALUE-VARIATION-POINT is the atpVariation artifact — PDF type Numerical wins per Rule 0015, 0..1). Reader/writer already used the matched spec-typed pair `getChildElementOptionalNumerical`/`setChildElementOptionalNumerical` (Rule 0013.2 verified by inspection + source pin in the round-trip test). Round-trip coverage in tests/test_armodel/writer/test_ecuc_numerical_param_value.py asserts field values, hex-text preservation, VARIATION-POINT absence and the empty/minimal case. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `EcucAddInfoParamValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 129
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.52 attribute `value` (`DocumentationBlock 0..1 aggr`, Note "Holds the content of the formated text.") is modeled as `value: Optional[DocumentationBlock]` with the getValue/setValue pair (None no-op, chaining, split-paragraph setter docstring). setValue (not createXxx) is correct per Rule 0001.6 — DocumentationBlock is a plain non-Referrable class. Base most-derived `EcucParameterValue`; no VariationPointCapable (no aggr atpVariation row). |

**Note:** Batch sync 2026-10-04 (Group27 batch 3; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.52, p.129 (concrete Class; no page-split rows) and the XSD group ECUC-ADD-INFO-PARAM-VALUE (AUTOSAR_00052.xsd l.51185; VALUE type AR:DOCUMENTATION-BLOCK, 0..1). Reader/writer already used the matched spec-typed pair `getDocumentationBlock`/`writeDocumentationBlock` — the repo-wide DocumentationBlock element convention (Rule 0013.2 verified by inspection and by the nested-content round-trip test). Round-trip coverage in tests/test_armodel/writer/test_ecuc_add_info_param_value.py asserts field values one level into the DocumentationBlock (P → L10N text), VARIATION-POINT absence and the empty/minimal case. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `EcucAbstractReferenceValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 131
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all Table 2.53 attributes are modeled with the PDF types and multiplicity in display order (`annotation` `Annotation * aggr` → `annotations: List[Annotation]` + addAnnotation/getAnnotations; `definition` `EcucAbstractReferenceDef 0..1 ref` → `definitionRef: Optional[RefType]`; `isAutoValue` `Boolean 0..1 attr`). Base most-derived `EcucIndexableValue` (spec Base `ARObject , EcucIndexableValue`). `variationPoint` deliberately NOT modeled: Table 2.53 has no variationPoint row and the VARIATION-POINT element in the XSD group ECUC-ABSTRACT-REFERENCE-VALUE is an atpVariation artifact documented "Applicable for: EcucContainerValue.referenceValue" — it belongs to the container's referenceValue aggregation, not to the reference values (Rule 0015, same arbitration as EcucParameterValue/Table 2.49). |

**Note:** Batch sync 2026-10-04 (Group27 batch 4; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.53, p.131 (abstract Class; class Note "Abstract class to be used as common parent for all reference values in the ECU Configuration Description."; PDF line-wrap space inside identifiers joined, "EcucAbstractReference Def" → "EcucAbstractReferenceDef") and the XSD group ECUC-ABSTRACT-REFERENCE-VALUE (AUTOSAR_00052.xsd l.51058; XML order DEFINITION-REF → INDEX (group ECUC-INDEXABLE-VALUE) → ANNOTATIONS → IS-AUTO-VALUE, already followed by reader/writer). VariationPointCapable mixin dropped from the bases; writer `writeEcucAbstractReferenceValue` no longer emits VARIATION-POINT and parser `readEcucAbstractReferenceValue` no longer reads it (symmetric); scalar setter docstrings moved to the batch-2 split-paragraph no-op style. No integration fixture carries VARIATION-POINT inside an ECUC-REFERENCE-VALUE/ECUC-INSTANCE-REFERENCE-VALUE (verified by fixture scan). No Rule 0001.10 missing classes (Annotation, EcucAbstractReferenceDef-as-RefType dest, Boolean are all existing). `# Spec verified:` withheld (batch 9b).

## `EcucReferenceValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.54 attribute `value` (`Referrable 0..1 ref`, Note "Specifies the destination of the reference.") is modeled as `valueRef: Optional[RefType]` with the getValueRef/setValueRef pair (None no-op, chaining, split-paragraph setter docstring); XSD element VALUE-REF base AR:REF DEST REFERRABLE--SUBTYPES-ENUM confirms the RefType modeling. Base most-derived `EcucAbstractReferenceValue` (spec Base `ARObject , EcucAbstractReferenceValue , EcucIndexableValue`). No variationPoint row (Rule 0020 not triggered). |

**Note:** Batch sync 2026-10-04 (Group27 batch 4; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.54, p.132 (concrete Class; PDF line-wrap space inside identifiers joined, "EcucAbstractReference Def" → "EcucAbstractReferenceDef") and the XSD complexType ECUC-REFERENCE-VALUE (AUTOSAR_00052.xsd l.53483; group sequence AR-OBJECT → ECUC-INDEXABLE-VALUE → ECUC-ABSTRACT-REFERENCE-VALUE → ECUC-REFERENCE-VALUE, reader/writer already emit/read VALUE-REF last via the matched `getChildElementOptionalRefType`/`setChildElementOptionalRefType` pair). Reader/writer unchanged — `readEcucReferenceValue` calls only `readEcucAbstractReferenceValue` (Rule 0013.1) and `writeEcucReferenceValue` keeps its established omit-empty/None-guard serialization pinned by the existing values-variant tests. Round-trip coverage in tests/test_armodel/writer/test_ecuc_reference_value.py asserts field values, XSD element order, VARIATION-POINT absence and the minimal case. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `EcucInstanceReferenceValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 134
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.55 attribute `value` (`AtpFeature 0..1 iref`, Note "InstanceReference representation in the ECU Configuration. InstanceRef implemented by: AnyInstanceRef") is modeled as `valueIRef: Optional[AnyInstanceRef]` with the getValueIRef/setValueIRef pair (None no-op, chaining, split-paragraph setter docstring); the Kind-iref Rule 0001.5 suffix (IRef) and the AnyInstanceRef element type both follow the table row, and the XSD element VALUE-IREF is typed AR:ANY-INSTANCE-REF confirming AnyInstanceRef. Base most-derived `EcucAbstractReferenceValue` (spec Base `ARObject , EcucAbstractReferenceValue , EcucIndexableValue`). No variationPoint row (Rule 0020 not triggered). |

**Note:** Batch sync 2026-10-04 (Group27 batch 4; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b; the rules.md 0013.2 "queued fix" for getValueIRef/setValueIRef backed by the wrong field is already resolved on this branch — the accessors are backed by the dedicated `valueIRef` field). Re-synced against R23-11 CP ECUConfiguration Table 2.55, p.134 (concrete Class) and the XSD complexType ECUC-INSTANCE-REFERENCE-VALUE (AUTOSAR_00052.xsd l.52538; group sequence AR-OBJECT → ECUC-INDEXABLE-VALUE → ECUC-ABSTRACT-REFERENCE-VALUE → ECUC-INSTANCE-REFERENCE-VALUE, reader/writer already emit/read VALUE-IREF last; inner ANY-INSTANCE-REF group is CONTEXT-ELEMENT-REF* then TARGET-REF with the atpDerived `base` association carrying no XML element). Reader/writer unchanged — `readEcucInstanceReferenceValue` calls only `readEcucAbstractReferenceValue` (Rule 0013.1) and the matched `getAnyInstanceRef`/`setAnyInstanceRef` pair handles VALUE-IREF. Round-trip coverage in tests/test_armodel/writer/test_ecuc_instance_reference_value.py asserts field values, XSD element order, VARIATION-POINT absence and the minimal case. Observation (AnyInstanceRef scope, not this class): the shared `setAnyInstanceRef`/`getAnyInstanceRefFromElement` helpers also read/write a BASE-REF element although the XSD marks `base` atpDerived (no XML element) — left untouched here, flagged for the AnyInstanceRef sync. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `EcucContainerValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 119
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all four Table 2.48 attributes are modeled with the PDF types and multiplicity in display order (`definition` `EcucContainerDef 0..1 ref` → `definitionRef: Optional[RefType]`; `parameterValue` `EcucParameterValue * aggr` → `parameterValues: List[EcucParameterValue]` + addParameterValue/getParameterValues; `referenceValue` `EcucAbstractReferenceValue * aggr` → `referenceValues: List[EcucAbstractReferenceValue]` + addReferenceValue/getReferenceValues; `subContainer` `EcucContainerValue * aggr` → `subContainers: List[EcucContainerValue]` + createSubContainer/getSubContainers, dedicated typed list plus the registry duplicate check). Base most-derived `Identifiable` (spec Base `ARObject , EcucIndexableValue , Identifiable`; EcucIndexableValue kept as the second base for the shared INDEX slot). `variationPoint` deliberately NOT modeled: Table 2.48 has no variationPoint row and the VARIATION-POINT element in the XSD group ECUC-CONTAINER-VALUE is an atpVariation artifact documented "Applicable for: EcucModuleConfigurationValues.container / EcucContainerValue.subContainer" — it covers the aggregations, not the container itself (Rule 0015, same arbitration as EcucParameterValue/Table 2.49 and EcucAbstractReferenceValue/Table 2.53). |

**Note:** Batch sync 2026-10-04 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUConfiguration Table 2.48, p.119 (concrete Class; class Note "Represents a Container definition in the ECU Configuration Description."; PDF line-wrap spaces inside identifiers joined, "parameterValue.variation Point.shortLabel" → "parameterValue.variationPoint.shortLabel", "sub Container.variationPoint.shortLabel" → "subContainer.variationPoint.shortLabel", confirmed by the XSD atp.Splitkey appinfo) and the XSD group ECUC-CONTAINER-VALUE (AUTOSAR_00052.xsd l.51678; XML order DEFINITION-REF → PARAMETER-VALUES (choice of ECUC-ADD-INFO/ECUC-NUMERICAL/ECUC-TEXTUAL-PARAM-VALUE) → REFERENCE-VALUES (choice of ECUC-INSTANCE-REFERENCE-VALUE/ECUC-REFERENCE-VALUE) → SUB-CONTAINERS (ECUC-CONTAINER-VALUE) — already followed by reader/writer; INDEX from the ECUC-INDEXABLE-VALUE group emitted after DEFINITION-REF per the established sequenceOffset convention). VariationPointCapable mixin dropped from the bases (reader/writer were already VP-free — no readVariationPointCapable/writeVariationPointCapable call existed in readEcucContainerValue/writeEcucContainValue, so no parser/writer edit was needed). The 0..1 setDefinitionRef was Optional-ized (Rule 0001.4) and addParameterValue/addReferenceValue gained the None no-op guard (Rule 0004). Reader `readEcucContainerValue` calls readIdentifiable + readEcucIndexableValue exactly once each (Rule 0013.1); writer helper keeps its pre-existing public spelling `writeEcucContainValue` (name kept, not renamed — no table obligation). Round-trip coverage in tests/test_armodel/writer/test_ecuc_container_value.py asserts field values one level down (nested sub-container, polymorphic parameter/reference values), XSD element order, VARIATION-POINT absence and the minimal case. No Rule 0001.10 missing classes (EcucContainerDef is reached as a RefType DEST, Annotation/DocumentationBlock/AnyInstanceRef all exist). `# Spec verified:` withheld (batch 9b).

## `HwDescriptionEntity`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 15
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 2.1 attributes are modeled with the PDF types and multiplicity in display order (`hwAttributeValue` `HwAttributeValue * aggr` → `hwAttributeValues: List[HwAttributeValue]` + addHwAttributeValue/getHwAttributeValues; `hwCategory` `HwCategory * ref` → `hwCategoryRefs: List[RefType]` + addHwCategoryRef/getHwCategoryRefs; `hwType` `HwType 0..1 ref` → `hwTypeRef: Optional[RefType]` + getHwTypeRef/setHwTypeRef). Base most-derived `Referrable` (spec Base `ARObject , Referrable`); no variationPoint row in Table 2.1 and the XSD group HW-DESCRIPTION-ENTITY carries no VARIATION-POINT element. |

**Note:** Batch sync 2026-10-04 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUResourceTemplate Table 2.1, p.15 (abstract Class; PDF line-wrap space inside the identifier joined, "hwAttribute Value" → "hwAttributeValue") and the XSD group HW-DESCRIPTION-ENTITY (AUTOSAR_00052.xsd l.65772; XML order HW-TYPE-REF → HW-CATEGORY-REFS → HW-ATTRIBUTE-VALUES, already followed by reader/writer). addHwAttributeValue/addHwCategoryRef/setHwTypeRef gained `Optional` value parameters and `HwDescriptionEntity` return annotations (Rule 0003); getter/setter docstrings moved to the batch split-paragraph no-op style with the spec Notes verbatim. The pre-existing `TYPE_CHECKING`-only `HwAttributeValue` import was replaced by a bottom-of-module runtime import (Rule 0003/0005 cycle-breaker) so the get_type_hints pin tests resolve. Reader `readHwDescriptionEntity` walks the Identifiable chain (comment in source): the class itself is Referrable-only per its table, but every concrete subclass (HwElement, HwPin, HwPinGroup, HwType) is Identifiable per its own spec Base, so the shared helper reads the SHORT-NAME/UUID level — helper-level design note, not a spec deviation. Round-trip coverage in tests/test_armodel/writer/test_ecu_resource_template_hw.py asserts field values one level into HW-ATTRIBUTE-VALUE (HW-ATTRIBUTE-DEF-REF, V) plus the empty case. No Rule 0001.10 missing classes (HwAttributeValue, HwCategory-as-RefType dest, RefType all exist). `# Spec verified:` withheld (batch 9b).

## `HwPinGroupContent`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 20
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwPin` | `Optional[HwPin]` | `hwPin` | `HwPin` | aggr | type (XSD `*` vs PDF 0..1): the XSD group raises the upper multiplicity to unbounded "due to resolving an atpVariation stereotype. The previous value was 1" (AUTOSAR_00052.xsd l.66267); the PDF Table 2.6 Mult column keeps 0..1 — PDF wins per Rule 0015, modeled as the optional single slot |
| `hwPinGroup` | `Optional[HwPinGroup]` | `hwPinGroup` | `HwPinGroup` | aggr | type (XSD `*` vs PDF 0..1): same atpVariation-resolved XSD upper bound (l.66277); PDF Table 2.6 Mult 0..1 kept per Rule 0015 |

**Note:** Batch sync 2026-10-04 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUResourceTemplate Table 2.6, p.20 (concrete Class carrying the `<<atpMixed>>` stereotype — an element-mixture marker, not `<<atpMixedString>>`: the XSD complexType HW-PIN-GROUP-CONTENT has `mixed="false"`, so no AtpMixedString mixin) and the XSD group HW-PIN-GROUP-CONTENT (AUTOSAR_00052.xsd l.66256; `xsd:choice` of HW-PIN/HW-PIN-GROUP, no VARIATION-POINT element). Class docstring was fabricated prose — wiped and rewritten with the spec Note verbatim; `__init__` docstring removed (Rule 0012.2.4); paraphrased getter docstrings rewritten verbatim. `setHwPinGroup` migrated to `createHwPinGroup(short_name)` per Rule 0001.6 (HwPinGroup Base includes Identifiable) and both factories gained the duplicate-returns-existing check (Rule 0004); parser `readHwPinGroupContent` now populates via the mutators `createHwPin`/`createHwPinGroup` (no chained calls). Reader/writer element order per the XSD choice (HW-PIN before HW-PIN-GROUP; reader iterates children in document order, writer emits pin then group). Round-trip coverage in tests/test_armodel/writer/test_ecu_resource_template_hw.py asserts nested HwPin field values one level down, a HwPinGroup nested inside HwPinGroupContent and the empty-content case. No Rule 0001.10 missing classes (HwPin, HwPinGroup exist and are stamped). `# Spec verified:` withheld (batch 9b).

## `HwElementConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 21
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 2.8 attributes are modeled with the PDF types and multiplicity in display order (`hwElement` `HwElement * ref` → `hwElementRefs: List[RefType]` + addHwElementRef/getHwElementRefs; `hwPinConnection` `HwPinConnector * aggr` → `hwPinConnections: List[HwPinConnector]` + addHwPinConnection/getHwPinConnections; `hwPinGroupConnection` `HwPinGroupConnector * aggr` → `hwPinGroupConnections: List[HwPinGroupConnector]` + addHwPinGroupConnection/getHwPinGroupConnections). Base most-derived `Describable` (spec Base `ARObject , Describable`; Describable exists as a stamped model class, GenericStructure/GeneralTemplateClasses/Identifiable.py l.507). `variationPoint` deliberately NOT modeled: Table 2.8 has no variationPoint row and the VARIATION-POINT element in the XSD group HW-ELEMENT-CONNECTOR is an atpVariation artifact documented "Applicable for: HwElement.hwElementConnection" — it covers the containing aggregation, not the connector itself (Rule 0015, same arbitration as EcucContainerValue/Table 2.48); the VariationPointCapable mixin was dropped from the bases. |

**Note:** Batch sync 2026-10-04 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUResourceTemplate Table 2.8, p.21 (concrete Class; class Note + class-level constr_11002 appended to the docstring) and the XSD group HW-ELEMENT-CONNECTOR (AUTOSAR_00052.xsd l.65909). addHwElementRef/addHwPinConnection/addHwPinGroupConnection gained `Optional` value parameters and `HwElementConnector` return annotations (Rule 0003); docstrings moved to the batch split-paragraph no-op style with the spec Notes verbatim; parser/writer were already VP-free for this class (no readVariationPoint/writeVariationPoint call existed), so the mixin removal needed no parser/writer edit. Reader/writer re-shaped to the XSD group: wrapper elements HW-ELEMENT-REFS (choice of HW-ELEMENT-REF), HW-PIN-GROUP-CONNECTIONS (choice of HW-PIN-GROUP-CONNECTOR) and HW-PIN-CONNECTIONS (choice of HW-PIN-CONNECTOR) — the previous unwrapped serialization emitted spec-invalid XML; wrappers are emitted only when non-empty (Rule 0001.7). As part of the same aggregator-group fix the inner item element names were corrected HW-PIN-CONNECTION → HW-PIN-CONNECTOR and HW-PIN-GROUP-CONNECTION → HW-PIN-GROUP-CONNECTOR in the shared family helpers (the item names the XSD choice mandates; inner wrappers HW-PIN-REFS/HW-PIN-CONNECTIONS/HW-PIN-GROUP-REFS land with the HwPinConnector/HwPinGroupConnector syncs). Round-trip coverage in tests/test_armodel/writer/test_ecu_resource_template_hw.py asserts field values, the XSD element order and the empty-connector case. No Rule 0001.10 missing classes (HwPinConnector, HwPinGroupConnector, Describable exist). `# Spec verified:` withheld (batch 9b).

## `HwPinGroupConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 22
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 2.9 attributes are modeled with the PDF types and multiplicity in display order (`hwPinConnection` `HwPinConnector * aggr` → `hwPinConnections: List[HwPinConnector]` + addHwPinConnection/getHwPinConnections; `hwPinGroup` `HwPinGroup * ref` → `hwPinGroupRefs: List[RefType]` + addHwPinGroupRef/getHwPinGroupRefs). Base most-derived `Describable` (spec Base `ARObject , Describable`). `variationPoint` deliberately NOT modeled: Table 2.9 has no variationPoint row and the VARIATION-POINT element in the XSD group HW-PIN-GROUP-CONNECTOR is an atpVariation artifact documented "Applicable for: HwElementConnector.hwPinGroupConnection" (Rule 0015, same arbitration as HwElementConnector/Table 2.8); the VariationPointCapable mixin was dropped from the bases. |

**Note:** Batch sync 2026-10-04 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUResourceTemplate Table 2.9, p.22 (concrete Class; class Note + class-level constr_11003 appended to the docstring; PDF line-wrap space inside identifiers joined) and the XSD group HW-PIN-GROUP-CONNECTOR (AUTOSAR_00052.xsd l.66193). addHwPinConnection/addHwPinGroupRef gained `Optional` value parameters and `HwPinGroupConnector` return annotations (Rule 0003); docstrings moved to the batch split-paragraph no-op style with the spec Notes verbatim; parser/writer were already VP-free for this class, so the mixin removal needed no parser/writer edit. Reader/writer re-shaped to the XSD group: item element name HW-PIN-GROUP-CONNECTION → HW-PIN-GROUP-CONNECTOR (done with the HwElementConnector aggregator fix) and the inner wrappers HW-PIN-CONNECTIONS (choice of HW-PIN-CONNECTOR) and HW-PIN-GROUP-REFS (choice of HW-PIN-GROUP-REF) — emitted only when non-empty, read via the wrapper paths (Rule 0001.7). Round-trip coverage in tests/test_armodel/writer/test_ecu_resource_template_hw.py asserts field values, the XSD element order and the empty case. No Rule 0001.10 missing classes (HwPinConnector exists). `# Spec verified:` withheld (batch 9b).

## `HwPinConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 22
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 2.10 attribute `hwPin` (`HwPin * ref`, Note "This association connects two hardware pins.") is modeled as `hwPinRefs: List[RefType]` with the addHwPinRef/getHwPinRefs pair (None no-op, chaining); constr_11004 (exactly 2 references) is a class-level constraint carried in the docstring, not an accessor obligation. Base most-derived `Describable` (spec Base `ARObject , Describable`). `variationPoint` deliberately NOT modeled: Table 2.10 has no variationPoint row and the VARIATION-POINT element in the XSD group HW-PIN-CONNECTOR is an atpVariation artifact documented "Applicable for: HwElementConnector.hwPinConnection / HwPinGroupConnector.hwPinConnection" (Rule 0015, same arbitration as HwElementConnector/Table 2.8); the VariationPointCapable mixin was dropped from the bases. |

**Note:** Batch sync 2026-10-04 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP ECUResourceTemplate Table 2.10, p.22 (concrete Class; class Note + class-level constr_11004 appended to the docstring) and the XSD group HW-PIN-CONNECTOR (AUTOSAR_00052.xsd l.66093). addHwPinRef gained the `Optional` value parameter and the `HwPinConnector` return annotation (Rule 0003); docstrings moved to the batch split-paragraph no-op style with the spec Notes verbatim; parser/writer were already VP-free for this class, so the mixin removal needed no parser/writer edit. Reader/writer re-shaped to the XSD group: item element name HW-PIN-CONNECTION → HW-PIN-CONNECTOR (done with the aggregator fixes) and the inner wrapper HW-PIN-REFS (choice of HW-PIN-REF) — emitted only when non-empty, read via the wrapper path (Rule 0001.7); the Describable content (DESC/CATEGORY/INTRODUCTION/ADMIN-DATA) round-trips through the shared readDescribable/writeDescribable pair (Rule 0013.1/0013.2). Round-trip coverage in tests/test_armodel/writer/test_ecu_resource_template_hw.py asserts ref values/dests, the XSD element order and the empty case. No Rule 0001.10 missing classes (HwPin is reached as a RefType DEST). `# Spec verified:` withheld (batch 9b).

## `CommunicationController`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 53
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 3.3 attribute `wakeUpByControllerSupported` (Boolean, 0..1, attr) is modeled as `wakeUpByControllerSupported: Optional[Boolean]` with the get/setWakeUpByControllerSupported pair (None no-op, chaining). Base most-derived `Identifiable` (spec Base `ARObject , Identifiable , MultilanguageReferrable , Referrable`); abstract per the table header, `type(self)` guard kept. VP-capable kept: unlike the Hw* Group27 classes, the VARIATION-POINT element in the XSD group COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd l.20388) is documented "Applicable for: EcuInstance.commController", so the VariationPointCapable mixin stays and VP round-trips through the shared readIdentifiable/writeIdentifiable handling (Rule 0020). Defining-table arbitration: the row cited both CP_TPS_ECUResourceTemplate Table 3.3 p.31 and CP_TPS_SystemTemplate Table 3.3 p.53 — the ECUResource caption ("CommunicationController HwElement Attributes", the HwType category attribute `communicationControllerType`) is a same-number caption collision on a different class, so the SystemTemplate table (Package row = CoreTopology) is the defining one; nothing merged from it. |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SystemTemplate Table 3.3, p.53 (abstract Class). Class docstring dropped the stale `Tags: vh.latestBindingTime=postBuild` tail (Note verbatim); attribute inline comment + getter/setter docstrings are the spec Note verbatim in the batch split-paragraph no-op style. Model/tests: typed-primitive (`Boolean`) round-trip replaced the legacy raw-`bool` usage; docstring-verbatim pins and `get_type_hints` pins added. Reader/writer were already complete — readCommunicationController/writeCommunicationController (WAKE-UP-BY-CONTROLLER-SUPPORTED only) are called by the Can/Ethernet/Flexray/Lin concrete subclass readers/writers which own their own readIdentifiable/writeIdentifiable calls; VP handled at the Identifiable level. Round-trip coverage in tests/test_armodel/writer/test_communication_controller.py (via the dispatched LinMaster) asserts the wake-up value, VP-before-content order and the empty case. Noted, not fixed (pre-existing subclass-aggregator gap outside this class): `UserDefinedCommunicationController` (spec subclass, Table 3.3 Subclasses row) has no reader/writer dispatch branch in read/writeEcuInstanceCommControllers. No Rule 0001.10 missing classes.

## `ParameterSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 41
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 2.1 attributes (constantMapping, dataTypeMapping, instantiationDataDefProps) are modeled per multiplicity/kind: the two ref rows as `List[RefType]` with add/get pairs, the `*` aggr row as `List[InstantiationDataDefProps]` with `addInstantiationDataDefProps` (child Base `ARObject`, non-Referrable → add, not create). |

**Note:** Batch sync 2026-10-05 (Group27; class was a bare `class ParameterSwComponentType(SwComponentType): pass` stub). Implemented from R23-11 CP SoftwareComponentTemplate Table 2.1, p.41 (concrete Class; Base chain most-derived `SwComponentType`; Package row = Components verified). Class docstring is the verbatim Table 2.1 Note (Tags tail dropped); member Notes verbatim in the batch split style. Reader/writer added per the XSD group PARAMETER-SW-COMPONENT-TYPE element order (CONSTANT-MAPPING-REFS, DATA-TYPE-MAPPING-REFS, INSTANTIATION-DATA-DEF-PROPSS; item element INSTANTIATION-DATA-DEF-PROPS with PARAMETER-INSTANCE / SW-DATA-DEF-PROPS / VARIABLE-INSTANCE + VARIATION-POINT, same inline shape as the existing NvBlockDescriptor handling); AR-PACKAGE/ELEMENTS dispatch added on both sides plus `ARPackage.createParameterSwComponentType`. `InstantiationDataDefProps` (synced, Table 7.41) reached via a bottom-of-module runtime import for the `get_type_hints` pins (Rule 0003/0005). No Rule 0001.10 missing classes (`ConstantSpecificationMappingSet`/`DataTypeMappingSet` are ref-DESTs only). `# Spec verified:` withheld (batch 9b).

## `ApplicationSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 71
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — Table 3.9 has no own attributes ("-"); the class inherits the full AtomicSwComponentType/SwComponentType surface, whose reader/writer coverage (APPLICATION-SW-COMPONENT-TYPE dispatch) is verified. |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.9, p.71 (concrete Class; Base chain most-derived `AtomicSwComponentType`). The second cited rendering, CP_TPS_DiagnosticExtractTemplate Table 5.8, p.231, is row-identical (same Note without changes, same Base, "-" attributes) — nothing merged, single defining table. Checklist re-written in the 6-column format; no field/accessor/parser/writer change needed. Round-trip through the AR-PACKAGE dispatch covered in tests/test_armodel/writer/test_sw_component_type_hierarchy.py. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `InstantiationRTEEventProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 85
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 3.17 attributes are modeled per multiplicity/kind: the `refinedEvent` iref row (RTEEvent, 0..1, concretized by the XSD to INSTANCE-EVENT-IN-COMPOSITION-INSTANCE-REF) as `refinedEventIRef: Optional[InstanceEventInCompositionInstanceRef]`, and the `shortLabel` attr row (Identifier, 0..1) as `shortLabel: Optional[Identifier]`. |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.17, p.85 (abstract Class; Base `ARObject`; `type(self)` guard kept; subclass `InstantiationTimingEventProps` per the Subclasses row). Docstrings wiped and rewritten: class docstring is the verbatim Table 3.17 Note; member inline comments + getter/setter docstrings are the spec Notes verbatim in the batch split-paragraph no-op style. Rule 0015 variationPoint arbitration: Table 3.17 has no variationPoint row, so the `VariationPointCapable` mixin was removed and the symmetric parser/writer handling dropped (`readVariationPointCapable`/`writeVariationPointCapable` calls removed from read/writeInstantiationRTEEventProps; incoming VARIATION-POINT is ignored — parser re-pinned in test_variation_point_capable_arobject.py). Reader/writer coverage was already complete (REFINED-EVENT-IREF / SHORT-LABEL, XSD group order). Round-trip coverage added in tests/test_armodel/writer/test_sw_composition_connectors.py (field values via INSTANTIATION-TIMING-EVENT-PROPS dispatch, no-VP-written, incoming-VP-ignored, empty-wrapper case). No Rule 0001.10 missing classes (`RTEEvent` exists; iref concretized by `InstanceEventInCompositionInstanceRef`). `# Spec verified:` withheld (batch 9b).

## `InstantiationTimingEventProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 85
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 3.16 attribute `period` (TimeValue, 0..1, attr) is modeled as `period: Optional[TimeValue]` with the get/setPeriod pair (None no-op, chaining). |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.16, p.85 (concrete Class; Base `ARObject , InstantiationRTEEventProps` — most-derived base `InstantiationRTEEventProps`, itself re-synced in this batch). Docstrings wiped and rewritten verbatim from the Table 3.16 Note and the `period` row Note in the batch split-paragraph no-op style. Rule 0015 variationPoint arbitration: Table 3.16 has no variationPoint row; the VP handling lived on the base `InstantiationRTEEventProps` and was removed there (shared read/writeInstantiationRTEEventProps helpers). Reader/writer coverage already complete: `readInstantiationTimingEventProps`/`writeInstantiationRTEEventProps` handle PERIOD after the base group's REFINED-EVENT-IREF / SHORT-LABEL (XSD complexType INSTANTIATION-TIMING-EVENT-PROPS = AR-OBJECT + INSTANTIATION-RTE-EVENT-PROPS + INSTANTIATION-TIMING-EVENT-PROPS group order); dispatched from read/writeCompositionSwComponentTypeInstantiationRTEEventProps via the INSTANTIATION-RTE-EVENT-PROPSS wrapper. Round-trip coverage in tests/test_armodel/writer/test_sw_composition_connectors.py (field values, element order, empty-wrapper). No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `SwConnector`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 80
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 3.12 attribute `mapping` (PortInterfaceMapping, 0..1, ref) is modeled as `mappingRef: Optional[RefType]` with the get/setMappingRef pair (None no-op, chaining). |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.12, p.80 (abstract Class; Base chain most-derived `AtpStructureElement` — the modeled class exists at GenericStructure/AbstractStructure.py, so no Rule 0016.4 fallback needed; subclasses per the table: AssemblySwConnector, DelegationSwConnector, PassThroughSwConnector). Docstrings wiped and rewritten verbatim from the Table 3.12 Note and the `mapping` row Note in the batch split-paragraph no-op style. Rule 0015 variationPoint arbitration: Table 3.12 has no variationPoint row, so the `VariationPointCapable` mixin was removed from SwConnector — the already-synced subclasses AssemblySwConnector/DelegationSwConnector inherit the removal (their own tables, 3.13/3.14, likewise carry no variationPoint row; neither their readers/writers nor any test used connector VP handling, so behavior is unchanged). Reader/writer coverage already complete: `readSwConnector`/`writeSwConnector` handle MAPPING-REF (the SW-CONNECTOR XSD group's only element) and are called by all three concrete subclass readers/writers; CompositionSwComponentType dispatches ASSEMBLY/DELEGATION/PASS-THROUGH-SW-CONNECTOR. Round-trip coverage in tests/test_armodel/writer/test_sw_composition_connectors.py (field values via the PassThroughSwConnector carrier, MAPPING-REF absence case). No Rule 0001.10 missing classes (`PortInterfaceMapping` is the ref DEST only, exists as a modeled class). `# Spec verified:` withheld (batch 9b).

## `PortInterface`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 87
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 3.18 attributes are modeled per multiplicity/kind: `isService` (Boolean, 0..1, attr) as `isService: Optional[Boolean]` and `serviceKind` (ServiceProviderEnum, 0..1, attr) as `serviceKind: Optional[ServiceProviderEnum]`, each with the get/set pair (None no-op, chaining). |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 3.18, p.87 (abstract Class; defining-table decision: the Base chain names both `ARElement` and `AtpType` — kept the role-matching most-derived branch `AtpType` per Rule 0001.2, consistent with AtpType Table 5.6 listing PortInterface as a subclass). Second citation FO AbstractPlatformSpecification Table 3.6, p.27 verified row-identical (same Note/Base, no attribute rows) — no Rule 0019 merge, single defining `# Spec:` line. Docstrings wiped and rewritten verbatim (the isService Note keeps the spec's bullet rendering). Rule 0015/0020 variationPoint arbitration: the `isService` atpVariation is an **attr**-row (attribute-value variation, serialized as BOOLEAN-VALUE-VARIATION-POINT in the XSD), not an aggr VP trigger, and the PORT-INTERFACE XSD group carries no VARIATION-POINT element — PortInterface is correctly NOT VP-capable, no mixin. Step 6 fixes (inherited-attribute coverage, Rule 0001.7): `writeTriggerInterface` never wrote IS-SERVICE/SERVICE-KIND (silent drop), `writeSenderReceiverInterface` wrote IS-SERVICE but not SERVICE-KIND, and `readSenderReceiverInterface`/`readTriggerInterface` did not level through `readDataInterface` — all four now go through the shared `readPortInterface`/`writePortInterface` helpers; `writePortInterface` switched from field access to the getIsService/getServiceKind getters (Rule 0013.2). Round-trip coverage added in tests/test_armodel/writer/test_port_interface_hierarchy.py (field values, XSD element order IS-SERVICE→SERVICE-KIND, absent-element case). ServiceProviderEnum is a runtime import now (bottom of TYPE_CHECKING block) so `get_type_hints` pins resolve on all Pythons. No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `ServiceProviderEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 90 (header row; caption page 91)
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `WATCH_DOG_MANAGER` | `AREnum` literal | `watchDogManager` | literal (atp.EnumerationLiteralIndex=17) | — | missing — the literal member existed but was not registered in the `__init__` enum-value tuple; registered (stale `test_initialization` expectation re-pinned to the full 24-literal tuple). |

**Note:** Batch sync 2026-10-05 (Group27). Re-verified against R23-11 CP SoftwareComponentTemplate Table 3.20 (page-split Enumeration table: page-1 body anyStandardized…j1939RequestManager renders above the caption, page-2 body nonVolatileRamManager…watchDogManager below it; displayed order = page order, 24 literals — member names/values match the `Literal` column exactly). Defining-table decision: the `# Spec:` line keeps p.90 (header-row page where `Enumeration ServiceProviderEnum` first appears; pdf_page.py reports the caption page p.91 — noted in the checklist line). Class docstring is the table `Note` verbatim. AREnum adaptation: Steps 5/6 N/A — a standalone enum has no own XML element; it is serialized as the SERVICE-KIND attribute value on the consuming class and round-tripped there (covered by TestPortInterfaceRoundTrip in tests/test_armodel/writer/test_port_interface_hierarchy.py). `# Spec verified:` withheld (batch 9b).

## `ClientServerInterface`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 101
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 4.6 attributes are modeled per multiplicity/kind: `operation` (ClientServerOperation, *, aggr) as the dedicated typed list `operations: List[ClientServerOperation]` with `createOperation`/`getOperations` (createXxx because the child's Base reaches Referrable; duplicate short name returns the existing element), and `possibleError` (ApplicationError, *, aggr) as `possibleErrors: List[ApplicationError]` with `createApplicationError`/`getPossibleErrors`. |

**Note:** Batch sync 2026-10-05 (Group27; stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.6, p.101 (concrete Class; Base most-derived `PortInterface`). Second citation CP DiagnosticExtractTemplate Table 5.13, p.236 verified row-identical — no Rule 0019 merge, single defining `# Spec:` line. Docstrings wiped and rewritten verbatim (dropped the `Tags: atp.recommendedPackage=PortInterfaces` tail from the class docstring and the `Stereotypes:/Tags:` tail from the operation-row docstrings per Rule 0012.2.5.2). Rule 0015/0020 variationPoint arbitration: the `operation` aggr row carries atpVariation, but per Rule 0020 the capability lands on the aggregated PartClass (`ClientServerOperation` — VARIATION-POINT "Applicable for: ClientServerInterface.operation" sits in the CLIENT-SERVER-OPERATION XSD group), not on the aggregator; the CLIENT-SERVER-INTERFACE complexType carries no VARIATION-POINT element — ClientServerInterface is correctly NOT VP-capable. Reader/writer coverage already complete and symmetric (read/writeClientServerInterface → OPERATIONS then POSSIBLE-ERRORS, XSD group order; five-place dispatch via createOperation/createApplicationError). Round-trip coverage in tests/test_armodel/writer/test_port_interface_hierarchy.py (field values one level down, empty-wrapper case). No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `ClientServerOperation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 102
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 4.7 attributes are modeled per multiplicity/kind: `argument (ordered)` (ArgumentDataPrototype, *, aggr) as the dedicated typed list `arguments: List[ArgumentDataPrototype]` with `createArgumentDataPrototype`/`getArguments`, `diagArgIntegrity` (Boolean, 0..1, attr) as `diagArgIntegrity: Optional[Boolean]`, and `possibleError` (ApplicationError, *, **ref**) as `possibleErrorRefs: List[RefType]` with `addPossibleErrorRef`/`getPossibleErrorRefs`. |

**Note:** Batch sync 2026-10-05 (Group27; stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.7, p.102 (concrete Class; Base most-derived `AtpStructureElement`). Second citation FO AbstractPlatformSpecification Table 3.8, p.29 is a restricted rendering (argument row only, FO Note "remote procedure call" variant) — CP table is defining, no Rule 0019 merge. Docstrings wiped and rewritten verbatim (dropped the `Stereotypes:/Tags:` tail from the argument Note per Rule 0012.2.5.2). Accessor order corrected to spec-row/mutator-first shape (`createArgumentDataPrototype` before `getArguments`). Rule 0015/0020 variationPoint arbitration: the `argument` aggr row carries atpVariation and the XSD anchor VARIATION-POINT ("Applicable for: ClientServerInterface.operation") sits in the CLIENT-SERVER-OPERATION group — ClientServerOperation keeps the `VariationPointCapable` mixin (handled symmetrically by read/writeIdentifiable). Reader/writer coverage already complete and symmetric (read/writeClientServerOperation → ARGUMENTS wrapper, DIAG-ARG-INTEGRITY, POSSIBLE-ERROR-REFS — XSD group order). Round-trip coverage in tests/test_armodel/writer/test_port_interface_hierarchy.py (field values, element order, None no-ops). No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `ArgumentDataPrototype`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 103
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 4.8 attributes are modeled per multiplicity/kind: `direction` (ArgumentDirectionEnum, 0..1, attr) as `direction: Optional[ArgumentDirectionEnum]` and `serverArgumentImplPolicy` (ServerArgumentImplPolicyEnum, 0..1, attr) as `serverArgumentImplPolicy: Optional[ServerArgumentImplPolicyEnum]`, each with the get/set pair (None no-op, chaining). |

**Note:** Batch sync 2026-10-05 (Group27; stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.8, p.103 (concrete Class; Base most-derived `AutosarDataPrototype`) — page-split table (direction row on the header page, serverArgumentImplPolicy row on the caption page; displayed order direction→serverArgumentImplPolicy matches the member order). Defining-table decision: the checklist previously cited BSWModuleDescriptionTemplate Table D.7, p.303; re-cited to the CP SWC Table 4.8 per the batch queue. Second citation FO AbstractPlatformSpecification Table 3.10, p.29 verified row-identical for the direction row (FO drops serverArgumentImplPolicy — restricted rendering); no Rule 0019 merge. Docstrings were already the spec Notes verbatim (verified by diff). Rule 0015/0020 variationPoint arbitration: the argument aggr row on ClientServerOperation carries atpVariation and the XSD anchor VARIATION-POINT ("Applicable for: ClientServerOperation.argument") sits in the ARGUMENT-DATA-PROTOTYPE group — ArgumentDataPrototype keeps the `VariationPointCapable` mixin (symmetric via read/writeIdentifiable). Reader/writer coverage already complete and symmetric (read/writeArgumentDataPrototype → DIRECTION then SERVER-ARGUMENT-IMPL-POLICY, XSD group order; dispatched from read/writeClientServerOperationArguments via the ARGUMENTS wrapper). Round-trip coverage in tests/test_armodel/writer/test_port_interface_hierarchy.py (DIRECTION/SERVER-ARGUMENT-IMPL-POLICY element order + values). No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `ServerArgumentImplPolicyEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 105
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 4.10 `Literal` rows are modeled 1:1: `USE_ARGUMENT_TYPE = "useArgumentType"` (atp.EnumerationLiteralIndex=0) and `USE_VOID = "useVoid"` (atp.EnumerationLiteralIndex=2); the enum registers exactly these two values in displayed order. |

**Note:** Batch sync 2026-10-05 (Group27; stale `# Spec verified: R23-11` marker removed, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.10, p.105 (Enumeration; Note verbatim as class docstring). **Literal arbitration resolved by the table:** Table 4.10 defines exactly `useArgumentType` and `useVoid` — the historically pending literals (innerPort / bidirectional / firstToSecond / secondToFirst) belong to other tables (PortPrototype connectable-combination tables / MappingDirectionEnum Table 4.37) and are not part of this enum; the stale "pending user arbitration" comment block was removed and the two-literal set confirmed (the table wins). AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the SERVER-ARGUMENT-IMPL-POLICY attribute value on the consuming class (round-tripped via ArgumentDataPrototype in tests/test_armodel/writer/test_port_interface_hierarchy.py). Tests pin member presence/values, no-extra-members, instantiability, docstring and literal-comment verbatim text. `# Spec verified:` withheld (batch 9b).

## `ApplicationError`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 108
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.11 attribute `errorCode` (Integer, 0..1, attr) is modeled as `errorCode: Optional[Integer]` with the get/setErrorCode pair (None no-op, chaining). |

**Note:** Batch sync 2026-10-05 (Group27; legacy Rule 0023 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.11, p.108 (concrete Class; Base most-derived `Identifiable`). Docstrings wiped and rewritten verbatim (the previous getter/setter docstrings were "Gets/Sets the error code…" paraphrases — replaced with the spec Note; kept the spec's "error code" two-word no-op sentence). Reader/writer coverage already complete and symmetric (readPossibleErrors → readIdentifiable + ERROR-CODE via getChildElementOptionalIntegerValue; writeApplicationError → writeIdentifiable + ERROR-CODE; dispatched from read/writeClientServerInterface via the POSSIBLE-ERRORS wrapper with APPLICATION-ERROR items, XSD group order). Round-trip coverage in tests/test_armodel/writer/test_port_interface_hierarchy.py (ERROR-CODE value 42, empty POSSIBLE-ERRORS case). No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `ModeSwitchInterface`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 113
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.16 attribute `modeGroup` (ModeDeclarationGroupPrototype, 0..1, aggr) is modeled as `modeGroup: Optional[ModeDeclarationGroupPrototype]` with the `createModeGroup`/`getModeGroup` pair (Referrable child factory, duplicate short name returns the existing element). |

**Note:** Batch sync 2026-10-05 (Group27; legacy 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.16, p.113 (concrete Class; Base chain most-derived `PortInterface`). Docstrings wiped and rewritten verbatim from the Table 4.16 Note and the `modeGroup` row Note (the class Note's `Tags: atp.recommendedPackage=PortInterfaces` tail dropped per Rule 0012.2.5.2; the old createModeGroup "Creates the..." Args/Returns paraphrase replaced). Rule 0015/0020 variationPoint arbitration: Table 4.16 has no variationPoint row; the MODE-SWITCH-INTERFACE XSD group (AUTOSAR_00052.xsd l.82942) carries no VARIATION-POINT element — not VP-capable, no mixin. Reader/writer coverage verified symmetric: `readModeSwitchInterface`/`writeModeSwitchInterface` level through the shared `readPortInterface`/`writePortInterface` helpers and handle MODE-GROUP (the group's only element) via `readModeSwitchInterfaceModeGroup`/`writeModeSwitchInterfaceModeGroup`; ARPackage port dispatch already routes MODE-SWITCH-INTERFACE. Round-trip coverage added in tests/test_armodel/writer/test_port_interface_hierarchy.py (field values, XSD element order, absent MODE-GROUP case). No Rule 0001.10 missing classes. `# Spec verified:` withheld (batch 9b).

## `ModeDeclarationMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `firstModeRefs` | `List[RefType]` | `firstMode` | `ModeDeclaration` | ref | type (XML REF DEST=MODE-DECLARATION--SUBTYPES-ENUM vs PDF class) — modeled as `RefType` per the XML form; spec 1..* pragmatically modeled as `*` list |
| `secondModeRef` | `Optional[RefType]` | `secondMode` | `ModeDeclaration` | ref | type (XML REF vs PDF class) — modeled as `RefType` per the XML form |

**Note:** Batch sync 2026-10-05 (Group27; legacy 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.29, p.132 (concrete Class; Base chain most-derived `AtpStructureElement`). Docstrings wiped and rewritten: the markdown wrap artifact `Mode DeclarationMapping` joined to `ModeDeclarationMapping` in every Note (class + both attribute rows, verified against the MODE-DECLARATION-MAPPING XSD group documentation, AUTOSAR_00052.xsd l.82316). Reader/writer coverage verified symmetric and in XSD group order (FIRST-MODE-REFS wrapper with FIRST-MODE-REF items, then SECOND-MODE-REF): `readModeDeclarationMapping`/`writeModeDeclarationMapping` via `readModeDeclarationMappingFirstModeRefs`/`writeModeDeclarationMappingFirstModeRefs` (`getChildElementRefTypeList` wrapper iteration); dispatched from `readModeDeclarationMappingSet`/`writeModeDeclarationMappingSet`. Round-trip coverage added in tests/test_armodel/writer/test_port_interface_hierarchy.py (field values + DEST attributes + element order via the ModeDeclarationMappingSet carrier, empty-set case). No Rule 0001.10 missing classes (`ModeDeclaration` exists as a modeled class). `# Spec verified:` withheld (batch 9b).

## `ImplementationDataTypeSubElementRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 138
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `implementationDataTypeElement` | `Optional[ArVariableInImplementationDataInstanceRef]` | `implementationDataTypeElement` | `ArVariableInImplementationDataInstanceRef` | aggr | No deviations — 0..1 aggr of a non-Identifiable instance-ref object, setXxx/getXxx pair |
| `parameterImplementationDataTypeElement` | `Optional[ArParameterInImplementationDataInstanceRef]` | `parameterImplementationDataTypeElement` | `ArParameterInImplementationDataInstanceRef` | aggr | referenced class was a bare stub — pre-synced in this pass with its AR-PARAMETER-IN-IMPLEMENTATION-DATA-INSTANCE-REF XSD-group fields (contextDataPrototypeRefs, portPrototypeRef, rootParameterDataPrototypeRef, targetDataPrototypeRef); the class itself still owes its own spec-table sync pass |

**Note:** Batch sync 2026-10-05 (Group27; previously a bare `pass` stub with no checklist — full 9-step sync from scratch). Re-synced against R23-11 CP SoftwareComponentTemplate Table 4.34, p.138 (concrete Class; Base chain most-derived `SubElementRef`, which is abstract with the `type(self) is SubElementRef` guard). Both Table 4.34 attributes modeled per multiplicity/kind with the get/set pair (None no-op, chaining); the `ArVariableInImplementationDataInstanceRef` import sits at the bottom of the PortInterface module (Rule 0005 cycle-breaker, `# noqa: E402`) and `ArParameterInImplementationDataInstanceRef` comes from the ArObject module where it is defined. Step 6: the SubElementRef polymorphic dispatch was previously ApplicationComposite-only — `setSubElementRef` gained the IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF branch (wrapper elements IMPLEMENTATION-DATA-TYPE-ELEMENT / PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT, each emitting PORT-PROTOTYPE-REF → ROOT-*-DATA-PROTOTYPE-REF → CONTEXT-DATA-PROTOTYPE-REFS (wrapper, only when non-empty) → TARGET-DATA-PROTOTYPE-REF per the AR-*-IN-IMPLEMENTATION-DATA-INSTANCE-REF XSD groups, AUTOSAR_00052.xsd l.5576/5665) and `getSubElementMapping` gained the matching FIRST-ELEMENTS/SECOND-ELEMENTS dispatch branches (`getImplementationDataTypeSubElementRef`). Round-trip coverage added in tests/test_armodel/writer/test_port_interface_hierarchy.py (both subtype branches with field values, XSD order, empty-wrapper case, plus the ApplicationComposite subtype regression). No `# Spec verified:` stamp yet (batch 9b).

## `ApplicationCompositeDataTypeSubElementRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 138
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.35 attribute `applicationCompositeElement` (ApplicationCompositeElementDataPrototype, 0..1, iref; InstanceRef implemented by ApplicationCompositeElementInPortInterfaceInstanceRef) is modeled as `applicationCompositeElementIRef: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]` with the get/set pair (None no-op, chaining), per the Rule 0001.5 iref naming. |

**Note:** Batch re-sync 2026-10-05 (Group27; the class already carried the current 6-column checklist from an earlier pass — this pass re-verified field-to-spec both directions, verbatim docstrings, PEP 526 annotated members, blank-line attribute spacing, and reader/writer coverage; the `# Spec verified: R23-11` marker was removed at session start per the batch convention, re-stamp deferred to the batch 9b; the `# Spec:` line normalized to the batch's plain-PDF-name format). Verified against R23-11 CP SoftwareComponentTemplate Table 4.35, p.138 (concrete Class; Base chain most-derived `SubElementRef`, abstract with the instantiation guard). The iref is a fixed-concrete instance ref — read/written flat via `getApplicationCompositeElementInPortInterfaceInstanceRef`/`setApplicationCompositeElementInPortInterfaceInstanceRef` under the APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF element of the SUB-ELEMENT-REF dispatch (`getSubElementMapping` FIRST-ELEMENTS/SECOND-ELEMENTS branches, `setSubElementRef`). Round-trip coverage in tests/test_armodel/writer/test_port_interface_hierarchy.py (`test_application_composite_sub_element_ref_still_round_trips`, field values via the SubElementMapping carrier, added with the ImplementationDataTypeSubElementRef sibling). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_ApplicationCompositeDataTypeSubElementRef.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `MappingDirectionEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 146
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the three Table 4.37 Literal rows map 1:1: `BIDIRECTIONAL = "bidirectional"` (atp.EnumerationLiteralIndex=0), `FIRST_TO_SECOND = "firstToSecond"` (idx 1), `SECOND_TO_FIRST = "secondToFirst"` (idx 2). |

**Note:** Batch re-sync 2026-10-05 (Group27; the class already carried the current 6-column checklist from an earlier pass — this pass re-verified members 1:1 against the Enumeration table and instantiability; the `# Spec verified: R23-11` marker was removed at session start per the batch convention, re-stamp deferred to the batch 9b; the `# Spec:` line normalized to the batch's plain-PDF-name format). Table 4.37 carries exactly three literals — bidirectional / firstToSecond / secondToFirst. The `innerPort` literal flagged in the batch-10 arbitration note does NOT belong to this table region: it is the `innerPort` iref attribute of `DelegationSwConnector` (SWC TPS Table 4.10, md line 2408) — no `innerPort` literal exists in any MappingDirectionEnum rendering, so the enum's literal set stays at three. Steps 5/6 N/A: a standalone enum has no own XML element — it is serialized as the MAPPING-DIRECTION literal attribute value on the consuming TextTableMapping (round-tripped there). New test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_MappingDirectionEnum.py (member values, exact literal set, instantiability via `MappingDirectionEnum().setValue(...)`, docstring pin). No stamp (batch 9b).

## `TextTableValuePair`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 146
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 4.38 attributes are modeled per multiplicity/kind: `firstValue` (Numerical, 0..1, attr) and `secondValue` (Numerical, 0..1, attr), each as `Optional[Numerical]` with the get/set pair (None no-op, chaining). |

**Note:** Batch re-sync 2026-10-05 (Group27; the class already carried the current 6-column checklist from an earlier pass — this pass re-verified field-to-spec both directions, verbatim docstrings, PEP 526 annotated members, and reader/writer coverage; the `# Spec verified: R23-11` marker was removed at session start per the batch convention, re-stamp deferred to the batch 9b; the `# Spec:` line normalized to the batch's plain-PDF-name format). The attr-level `atpVariation` stereotype on both rows is attribute-value variation (Rule 0020 NOT-indicator): the XSD serializes FIRST-VALUE/SECOND-VALUE as NUMERICAL-VALUE-VARIATION-POINT (an atpVariation artifact), and the PDF Numerical type is kept per Rule 0015 — the reader/writer use the spec-typed `getChildElementOptionalNumerical`/`setChildElementOptionalNumerical` pair (TEXT-TABLE-VALUE-PAIR element, AUTOSAR_00052.xsd l.122580, order FIRST-VALUE → SECOND-VALUE). Round-trip coverage in tests/test_armodel/writer/test_text_table_mapping.py (field values via the TextTableMapping VALUE-PAIRS wrapper, empty-wrapper case). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_TextTableValuePair.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `DataTransformation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 150
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 4.39 attributes are modeled per multiplicity/kind: `dataTransformationKind` (DataTransformationKindEnum, 0..1, attr), `executeDespiteDataUnavailability` (Boolean, 0..1, attr), and `transformerChain (ordered)` (*, ref) as `transformerChainRefs: List[RefType]` with `addTransformerChainRef` (spec-singular many → plural Python naming per Rule 0001.4). |

**Note:** Batch sync 2026-10-05 (Group27; legacy 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Defining-table decision: re-cited from SystemTemplate Table 7.2, p.763 to CP SoftwareComponentTemplate Table 4.39, p.150 (the primary citation); SystemTemplate Table 7.2 verified row-identical (Package/Note/Base/Aggregated-by/all attribute rows) — single `# Spec:` line, no Rule 0019 merge. Class docstring Note verbatim + the table-adjacent class-level constraint [constr_1888] appended. Rule 0015/0020 variationPoint arbitration: Table 4.39 has no variationPoint row; the XSD VARIATION-POINT in the DATA-TRANSFORMATION group (AUTOSAR_00052.xsd l.28234, "Applicable for: DataTransformationSet.dataTransformation") is the aggregator's atpSplitable/atpVariation artifact — `VariationPointCapable` mixin removed; reader/writer never handled VARIATION-POINT on this class (verified symmetric, no parser/writer change), and the new empty-wrapper round-trip test pins VARIATION-POINT absence. Reader/writer coverage verified complete and XSD-ordered (DATA-TRANSFORMATION-KIND → EXECUTE-DESPITE-DATA-UNAVAILABILITY → TRANSFORMER-CHAIN-REFS/TRANSFORMER-CHAIN-REF wrapper). Round-trip coverage in tests/test_armodel/writer/test_data_transformation.py (field values incl. chain-ref DEST, empty-wrapper case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `DataTransformationKindEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 150
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 4.40 `Literal` rows are modeled 1:1 in displayed order: `ASYMMETRIC_FROM_BYTE_ARRAY = "asymmetricFromByteArray"` (atp.EnumerationLiteralIndex=0), `ASYMMETRIC_TO_BYTE_ARRAY = "asymmetricToByteArray"` (index=1), `SYMMETRIC = "symmetric"` (index=2). |

**Note:** Batch sync 2026-10-05 (Group27; the enum already carried the current bar from an earlier pass — this pass re-verified literal set 1:1 against Table 4.40, member values, registration-tuple order, instantiability, and the verbatim class Note; the stale `# Spec verified: R23-11` marker was removed at session start per the batch convention, re-stamp deferred to the batch 9b; the checklist normalized to the 6-column `# (no methods)`-row variant). AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the DATA-TRANSFORMATION-KIND attribute value on the consuming class (round-tripped via DataTransformation in tests/test_armodel/writer/test_data_transformation.py). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/test_DataTransformationKindEnum.py. No stamp (batch 9b).

## `TransformationTechnology`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 199
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all seven Table 4.87 attributes are modeled per multiplicity/kind in displayed order: `bufferProperties` (BufferProperties, 0..1, aggr → set/get, non-Referrable child), `hasInternalState` (Boolean, 0..1), `needsOriginalData` (Boolean, 0..1), `protocol` (String, 0..1), `transformationDescription` (TransformationDescription, 0..1, aggr of the abstract child), `transformerClass` (TransformerClassEnum, 0..1), `version` (String, 0..1). |

**Note:** Batch sync 2026-10-05 (Group27; legacy 5-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Defining-table decision: re-cited from SystemTemplate Table 7.3, p.764 to CP SoftwareComponentTemplate Table 4.87, p.199 (the primary citation); SystemTemplate Table 7.3 verified row-identical — single `# Spec:` line, no Rule 0019 merge. Class docstring Note verbatim (the `Tags: xml.namePlural=TRANSFORMATION-TECHNOLOGIES` tail dropped per Rule 0012.2.5.2). Accessor groups reordered to getter-first per attribute (Rule 0001.11 — was setter-first). Rule 0015/0020 variationPoint arbitration: Table 4.87 has no variationPoint row (the transformationDescription row's atpVariation is the aggregated class's splitkey); the XSD VARIATION-POINT in the TRANSFORMATION-TECHNOLOGY group (AUTOSAR_00052.xsd l.125871, "Applicable for: DataTransformationSet.transformationTechnology") is the aggregator's artifact — `VariationPointCapable` mixin removed; reader/writer never handled VARIATION-POINT on this class (verified symmetric, no parser/writer change), and the round-trip test pins VARIATION-POINT absence. XSD upper-multiplicity note: the XSD raises transformationDescription to * (atpVariation resolution, TRANSFORMATION-DESCRIPTIONS wrapper) while the PDF says 0..1 — the PDF single-field model is kept per Rule 0015 with the reader/writer dispatching on the concrete subtype element inside the wrapper (current behavior, verified). Reader/writer coverage verified complete and XSD-ordered (BUFFER-PROPERTIES → HAS-INTERNAL-STATE → NEEDS-ORIGINAL-DATA → PROTOCOL → TRANSFORMATION-DESCRIPTIONS → TRANSFORMER-CLASS → VERSION). Round-trip coverage added in tests/test_armodel/writer/test_data_transformation.py (field values one level down into BufferProperties/EndToEndTransformationDescription, empty-wrapper + VARIATION-POINT absence). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `SenderReceiverAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 152
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all four Table 4.41 attributes are modeled per multiplicity/kind in displayed order: `computed` (Boolean, 0..1, attr), `dataElement` (VariableDataPrototype, 0..1, ref → `dataElementRef: Optional[RefType]`), `limitKind` (DataLimitKindEnum, 0..1, attr), `processingKind` (ProcessingKindEnum, 0..1, attr). |

**Note:** Batch sync 2026-10-05 (Group27; legacy 4-column checklist with a stale `# Spec verified: R23-11` marker — marker removed at session start, re-stamp deferred to the batch 9b). Abstract-ified per the spec header "SenderReceiverAnnotation (abstract)": direct instantiation now raises TypeError (GeneralAnnotation guard pattern); concrete subclasses SenderAnnotation/ReceiverAnnotation re-pinned in tests/test_armodel/{models/.../ApplicationAttributes,models/.../Components,parser}/ — all direct `SenderReceiverAnnotation()` constructor calls across tests/ were grep-audited and re-pinned. Reader/writer element-name fix (XSD arbitration, AUTOSAR_00052.xsd): the wrapper SENDER-RECEIVER-ANNOTATIONS carries a choice of RECEIVER-ANNOTATION/SENDER-ANNOTATION elements only — the previous `<SENDER-RECEIVER-ANNOTATION>` child element is absent from the XSD; the writer now dispatches on isinstance (ReceiverAnnotation → RECEIVER-ANNOTATION, else SENDER-ANNOTATION) and the parser on the XSD child tag, both through the abstract base's reusable `readSenderReceiverAnnotation`/`writeSenderReceiverAnnotation` helpers (Rule 0001.7 abstract XML-bearing base). No integration fixture carried the removed element (grep-verified). Markdown line-wrap artifact joined: "AtomicSw ComponentType" → "AtomicSwComponentType" in the limitKind Note. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `SenderAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 153
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — Table 4.42 has no `Attribute` rows (the displayed Attribute row is `-`); the class contributes only its identity under Base `ARObject, GeneralAnnotation, SenderReceiverAnnotation` (modeled as subclass of SenderReceiverAnnotation, the most-derived base). |

**Note:** Batch sync 2026-10-05 (Group27; previously a bare `pass` subclass). Explicit `__init__` calling super() (checklist row), class Note verbatim. XSD: SENDER-ANNOTATION group is empty (`<xsd:sequence/>`, AUTOSAR_00052.xsd l.104235); the element is written/read via the base's dispatch (writer isinstance → SENDER-ANNOTATION child of SENDER-RECEIVER-ANNOTATIONS; parser tag dispatch) — covered by test_sender_annotation_round_trip in tests/test_armodel/writer/test_sw_annotations.py (Steps 5/6 via the abstract base's reusable helpers). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `ReceiverAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 153
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.43 attribute is modeled per multiplicity/kind: `signalAge` (MultidimensionalTime, 0..1, aggr → `setSignalAge`/`getSignalAge`, non-Referrable child). |

**Note:** Batch sync 2026-10-05 (Group27; previously a bare `pass` subclass — the spec signalAge attribute was entirely missing). Class Note verbatim. XSD: RECEIVER-ANNOTATION group is SIGNAL-AGE only (AUTOSAR_00052.xsd l.95956), after the inherited GENERAL-ANNOTATION and SENDER-RECEIVER-ANNOTATION groups in the complexType sequence — reader reads the inherited base group via `readSenderReceiverAnnotation` then `readReceiverAnnotation` (SIGNAL-AGE → MultidimensionalTime); writer emits the base group then SIGNAL-AGE under the RECEIVER-ANNOTATION element (isinstance dispatch). Round-trip coverage in tests/test_armodel/writer/test_sw_annotations.py (field values incl. base fields + signalAge, empty-wrapper case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `ProcessingKindEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 153
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 4.44 `Literal` rows are modeled 1:1 in displayed order: `FILTERED = "filtered"` (atp.EnumerationLiteralIndex=0), `NONE = "none"` (index=1), `RAW = "raw"` (index=2). |

**Note:** Batch sync 2026-10-05 (Group27; the enum already carried the current bar from an earlier pass — this pass re-verified literal set 1:1 against Table 4.44, member values, registration-tuple order, instantiability, and the verbatim class Note; the legacy 4-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column `# (no methods)`-row variant and the marker removed per the batch convention, re-stamp deferred to the batch 9b). AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the PROCESSING-KIND attribute value on the consuming class (round-tripped via SenderReceiverAnnotation in tests/test_armodel/writer/test_sw_annotations.py). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/test_ProcessingKindEnum.py. No stamp (batch 9b).

## `DataLimitKindEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 154
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 4.45 `Literal` rows are modeled 1:1 in displayed order: `MAX = "max"` (atp.EnumerationLiteralIndex=0), `MIN = "min"` (index=1), `NONE = "none"` (index=2). |

**Note:** Batch sync 2026-10-05 (Group27; the enum already carried the current bar from an earlier pass — this pass re-verified literal set 1:1 against Table 4.45, member values, registration-tuple order, instantiability, and the verbatim class Note; the legacy 4-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column `# (no methods)`-row variant and the marker removed per the batch convention, re-stamp deferred to the batch 9b). Page-number correction: the stale checklist cited p.153; pdf_page.py gives p.154 for Table 4.45 — `# Spec:` line corrected. AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the LIMIT-KIND attribute value on the consuming class (round-tripped via SenderReceiverAnnotation in tests/test_armodel/writer/test_sw_annotations.py). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/test_DataLimitKindEnum.py. No stamp (batch 9b).

## `ClientServerAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 155
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.46 attribute is modeled per multiplicity/kind: `operation` (ClientServerOperation, 0..1, ref → `operationRef: Optional[RefType]`). |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the field-to-spec cross-check both directions, verbatim Notes, None-no-op setter, and get/set types; the stale `# Spec verified: R23-11` marker was removed per the batch convention, re-stamp deferred to the batch 9b). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; reader/writer columns re-split per Rule 0002 (reader on setOperationRef, writer on getOperationRef — both were marked on both rows). Reader (OPERATION-REF via setOperationRef inside readPortPrototype) and writer (OPERATION-REF via getOperationRef in writeClientServerAnnotation) verified against the XSD CLIENT-SERVER-ANNOTATION group order (single element). Round-trip coverage added in tests/test_armodel/writer/test_sw_annotations.py (field values incl. DEST, empty-wrapper case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `IoHwAbstractionServerAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 157
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all eight Table 4.47 attributes are modeled per multiplicity/kind in displayed order: `age` (MultidimensionalTime, 0..1, aggr → set/get), `argument` (ArgumentDataPrototype, 0..1, ref → `argumentRef`), `bswResolution` (Float, 0..1, attr), `dataElement` (VariableDataPrototype, 0..1, ref → `dataElementRef`), `failureMonitoring` (PortPrototype, 0..1, ref → `failureMonitoringRef`), `filteringDebouncing` (FilterDebouncingEnum, 0..1, attr), `pulseTest` (PulseTestEnum, 0..1, attr), `trigger` (Trigger, 0..1, ref → `triggerRef`). |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the field-to-spec cross-check both directions, types, None-no-op setters, and member order; the stale `# Spec verified: R23-11` marker was removed per the batch convention, re-stamp deferred to the batch 9b). Docstring hygiene: the `Tags: xml.sequenceOffset=NN` tails were dropped from the inline comments and getter/setter docstrings (Rule 0012.2.5.2) — Notes now verbatim per the markdown. Checklist corrections: `# Spec:` line re-formatted with `(R23-11)`; reader/writer columns re-split per Rule 0002 (reader on each setter, writer on each getter — filteringDebouncing/pulseTest/triggerRef rows previously marked on both). Reader/writer verified against the XSD IO-HW-ABSTRACTION-SERVER-ANNOTATION group order (AGE → ARGUMENT-REF → BSW-RESOLUTION → DATA-ELEMENT-REF → FAILURE-MONITORING-REF → FILTERING-DEBOUNCING → PULSE-TEST → TRIGGER-REF, AUTOSAR_00052.xsd l.73413). Round-trip coverage added in tests/test_armodel/writer/test_sw_annotations.py (field values, empty-wrapper case); full-field round-trip in tests/test_armodel/writer/test_io_hw_annotation.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `FilterDebouncingEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 157
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — all three Table 4.48 `Literal` rows are modeled 1:1 in displayed order: `DEBOUNCE_DATA = "debounceData"` (atp.EnumerationLiteralIndex=0), `RAW_DATA = "rawData"` (index=1), `WAIT_TIME_DATE = "waitTimeDate"` (index=2). |

**Note:** Batch sync 2026-10-05 (Group27; the enum already carried the current bar from an earlier pass — this pass re-verified the literal set 1:1 against Table 4.48, member values, registration-tuple order, instantiability, and the verbatim class Note; the legacy 4-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column format and the marker removed per the batch convention, re-stamp deferred to the batch 9b). AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the FILTERING-DEBOUNCING attribute value on the consuming class (round-tripped via IoHwAbstractionServerAnnotation in tests/test_armodel/writer/test_port_annotations.py). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/test_FilterDebouncingEnum.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `PulseTestEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 157
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 4.49 `Literal` rows are modeled 1:1 in displayed order: `DISABLE = "disable"` (atp.EnumerationLiteralIndex=0), `ENABLE = "enable"` (index=1). |

**Note:** Batch sync 2026-10-05 (Group27; the enum already carried the current bar from an earlier pass — this pass re-verified the literal set 1:1 against Table 4.49, member values, registration-tuple order, instantiability, and the verbatim class Note; the legacy 4-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column format and the marker removed per the batch convention, re-stamp deferred to the batch 9b). AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the PULSE-TEST attribute value on the consuming class (round-tripped via IoHwAbstractionServerAnnotation in tests/test_armodel/writer/test_port_annotations.py). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/test_PulseTestEnum.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `ParameterPortAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 158-159
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.50 attribute is modeled per multiplicity/kind: `parameter` (ParameterDataPrototype, 0..1, ref → `parameterRef: Optional[RefType]`). |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the field-to-spec cross-check both directions, verbatim Notes, None-no-op setter, and get/set types; the stale `# Spec verified: R23-11` marker was removed per the batch convention, re-stamp deferred to the batch 9b). Step-1 finding: the markdown render of Table 4.50 drops the Class header block (Package/Note/Base rows); the PDF (p.158) shows Base = `ARObject, GeneralAnnotation` — the class keeps its `GeneralAnnotation` base (most-derived per Rule 0001.2, consistent with the XSD complexType sequence AR-OBJECT → GENERAL-ANNOTATION → own group, AUTOSAR_00052.xsd l.88153). The `# Spec:` line cites pp.158-159 (split table: header rows p.158, attribute rows + caption p.159). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; reader/writer columns re-split per Rule 0002 (reader on setParameterRef, writer on getParameterRef — both were marked on both rows). Reader (PARAMETER-REF via setParameterRef inside readPortPrototype) and writer (PARAMETER-REF via getParameterRef in writeParameterPortAnnotation, wrapper PARAMETER-PORT-ANNOTATIONS only when non-empty) verified against the XSD group order (single element). Round-trip coverage added in tests/test_armodel/writer/test_port_annotations.py (field values incl. DEST + empty-wrapper case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `ModePortAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 159
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.51 attribute is modeled per multiplicity/kind: `modeGroup` (ModeDeclarationGroupPrototype, 0..1, ref → `modeGroupRef: Optional[RefType]`). |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the field-to-spec cross-check both directions, verbatim Notes, None-no-op setter, and get/set types; the stale `# Spec verified: R23-11` marker was removed per the batch convention, re-stamp deferred to the batch 9b). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; reader/writer columns re-split per Rule 0002 (reader on setModeGroupRef, writer on getModeGroupRef — both were marked on both rows). Reader (MODE-GROUP-REF via setModeGroupRef inside readPortPrototype) and writer (MODE-GROUP-REF via getModeGroupRef in writeModePortAnnotation, wrapper MODE-PORT-ANNOTATIONS only when non-empty) verified against the XSD MODE-PORT-ANNOTATION group order (single element; complexType sequence AR-OBJECT → GENERAL-ANNOTATION → own group, AUTOSAR_00052.xsd l.82829). Round-trip coverage added in tests/test_armodel/writer/test_port_annotations.py (field values incl. DEST + empty-wrapper case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `TriggerPortAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 160
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.52 attribute is modeled per multiplicity/kind: `trigger` (Trigger, 0..1, ref → `triggerRef: Optional[RefType]`). |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the field-to-spec cross-check both directions, verbatim Notes, None-no-op setter, and get/set types; the stale `# Spec verified: R23-11` marker was removed per the batch convention, re-stamp deferred to the batch 9b). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; reader/writer columns re-split per Rule 0002 (reader on setTriggerRef, writer on getTriggerRef — both were marked on both rows). Reader (TRIGGER-REF via setTriggerRef inside readPortPrototype) and writer (TRIGGER-REF via getTriggerRef in writeTriggerPortAnnotation, wrapper TRIGGER-PORT-ANNOTATIONS only when non-empty) verified against the XSD TRIGGER-PORT-ANNOTATION group order (single element; complexType sequence AR-OBJECT → GENERAL-ANNOTATION → own group, AUTOSAR_00052.xsd l.126669). Round-trip coverage added in tests/test_armodel/writer/test_port_annotations.py (field values incl. DEST + empty-wrapper case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `NvDataPortAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 160
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.53 attribute is modeled per multiplicity/kind: `variable` (VariableDataPrototype, 0..1, ref → `variableRef: Optional[RefType]`). |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the field-to-spec cross-check both directions, verbatim Notes, None-no-op setter, and get/set types; the stale `# Spec verified: R23-11` marker was removed per the batch convention, re-stamp deferred to the batch 9b). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; reader/writer columns re-split per Rule 0002 (reader on setVariableRef, writer on getVariableRef — both were marked on both rows). Reader (VARIABLE-REF via setVariableRef inside readPortPrototype) and writer (VARIABLE-REF via getVariableRef in writeNvDataPortAnnotation, wrapper NV-DATA-PORT-ANNOTATIONS only when non-empty) verified against the XSD NV-DATA-PORT-ANNOTATION group order (single element; complexType sequence AR-OBJECT → GENERAL-ANNOTATION → own group, AUTOSAR_00052.xsd l.86329). Round-trip coverage added in tests/test_armodel/writer/test_port_annotations.py (field values incl. DEST + empty-wrapper case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `DelegatedPortAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 162
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — the single Table 4.54 attribute is modeled per multiplicity/kind: `signalFan` (SignalFanEnum, 0..1, attr → `signalFan: Optional[SignalFanEnum]`). |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the field-to-spec cross-check both directions, verbatim Notes, None-no-op setter, and get/set types; the stale `# Spec verified: R23-11` marker was removed per the batch convention, re-stamp deferred to the batch 9b). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; reader/writer columns re-split per Rule 0002 (reader on setSignalFan, writer on getSignalFan — both were marked on both rows). Reader (SIGNAL-FAN via getChildElementOptionalLiteral → SignalFanEnum().setValue inside readPortPrototype, single DELEGATED-PORT-ANNOTATION child via setDelegatedPortAnnotation) and writer (SIGNAL-FAN via getSignalFan in writeDelegatedPortAnnotation, element only when set) verified against the XSD DELEGATED-PORT-ANNOTATION group order (single element; complexType sequence AR-OBJECT → GENERAL-ANNOTATION → own group, AUTOSAR_00052.xsd l.30933). Round-trip coverage added in tests/test_armodel/writer/test_port_annotations.py (field values + absence case). No Rule 0001.10 missing classes. No stamp (batch 9b).

## `SignalFanEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 162
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 4.55 `Literal` rows are modeled 1:1 in displayed order: `NFOLD = "nfold"` (atp.EnumerationLiteralIndex=0), `SINGLE = "single"` (index=1). |

**Note:** Batch sync 2026-10-05 (Group27; the enum already carried the current bar from an earlier pass — this pass re-verified the literal set 1:1 against Table 4.55, member values, registration-tuple order, instantiability, and the verbatim class Note; the legacy 4-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column format and the marker removed per the batch convention, re-stamp deferred to the batch 9b). AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the SIGNAL-FAN attribute value on the consuming class (round-tripped via DelegatedPortAnnotation in tests/test_armodel/writer/test_port_annotations.py). New mirrored model test file tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/test_SignalFanEnum.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `PPortComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 166
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — Table 4.58 has an empty `Attribute` column; the abstract class models zero own members on Base `ARObject`, instantiation-guarded. |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the empty attribute set both directions, the verbatim class Note, the abstract guard, and instantiability via a concrete subclass; the legacy 5-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column format and the marker removed per the batch convention, re-stamp deferred to the batch 9b). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; per-row `release` column added. No XML elements (XSD P-PORT-COM-SPEC group has an empty sequence, AUTOSAR_00052.xsd l.87489) — reader/writer coverage flows through the concrete-subclass dispatch (writePPortComSpec / readPPortComSpec five-place switches), round-trip covered via ServerComSpec on a PPortPrototype in tests/test_armodel/writer/test_com_spec_family.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `RPortComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 167
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — Table 4.59 has an empty `Attribute` column; the abstract class models zero own members on Base `ARObject`, instantiation-guarded. |

**Note:** Batch sync 2026-10-05 (Group27; the class already carried the current bar from an earlier pass — this pass re-verified the empty attribute set both directions, the verbatim class Note, the abstract guard, and instantiability via a concrete subclass; the legacy 5-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column format and the marker removed per the batch convention, re-stamp deferred to the batch 9b). Checklist corrections: `# Spec:` line re-formatted with the `(R23-11)` suffix; per-row `release` column added. No XML elements (XSD R-PORT-COM-SPEC group has an empty sequence, AUTOSAR_00052.xsd l.95189) — reader/writer coverage flows through the concrete-subclass dispatch (writeRPortComSpec / readRequiredComSpec five-place switches), round-trip covered via ClientComSpec on an RPortPrototype in tests/test_armodel/writer/test_com_spec_family.py. No Rule 0001.10 missing classes. No stamp (batch 9b).

## `HandleOutOfRangeStatusEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 172
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — both Table 4.61 `Literal` rows are modeled 1:1 in displayed order: `INDICATE = "indicate"` (atp.EnumerationLiteralIndex=0), `SILENT = "silent"` (index=1). |

**Note:** Batch sync 2026-10-05 (Group27; the enum already carried the current bar from an earlier pass — this pass re-verified the literal set 1:1 against Table 4.61, member values, registration-tuple order, instantiability, and the verbatim class Note; the legacy 5-column checklist with a stale `# Spec verified: R23-11` marker was normalized to the 6-column format and the marker removed per the batch convention, re-stamp deferred to the batch 9b). AREnum adaptation: Steps 5/6 N/A — standalone enum, serialized as the HANDLE-OUT-OF-RANGE-STATUS attribute value on the consuming class (round-tripped via ReceiverComSpec in tests/test_armodel/writer/test_com_spec_family.py). No Rule 0001.10 missing classes. No stamp (batch 9b).
## `EcucDestinationUriDefRefType`
- **PDF:** — (XSD-only; no own table in the R23-11 or R4.3.1 markdown corpora)  | **XSD:** `AUTOSAR_00052.xsd` DESTINATION-URI-REF nested type, l.51614 (group ECUC-CONTAINER-DEF)
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(accepted)* | — | — | — | — | DEST modeled optional (inherited `RefType.dest: Optional[str]`) vs XSD `use="required"` (AR:ECUC-DESTINATION-URI-DEF--SUBTYPES-ENUM) on the nested type — per-subclass attribute requiredness cannot be expressed on the shared RefType base; reader/writer round-trip DEST/BASE when present. No integration fixture carries DESTINATION-URI-REF (no fixture constraint). |

**Note:** Batch sync 2026-10-04 (Group19 row 6; the retire-or-keep arbitration is RESOLVED to keep — the class is the model-side type of the real XSD DESTINATION-URI-REF element and is required for the DEST-typed isinstance dispatch in parser getEcucDestinationUriRefs l.12948 / writer setEcucDestinationUriRefs l.11283; retiring it would untype the EcucContainerDef.destinationUriRefs round-trip). XSD-only class: the nested anonymous complexType is a simpleContent extension of AR:REF with a DEST attribute (use="required", ECUC-DESTINATION-URI-DEF--SUBTYPES-ENUM) — modeled as a zero-own-field RefType subclass (inherited value/base/dest carry the element content + attribs), the same shape as the sibling TRefType. No PDF/markdown table exists in R23-11 or R4.3.1 (EcucDestinationUriDef Table 2.35, p.82 is the destination-side class, not this ref type) → `# XSD verified: AUTOSAR_00052.xsd` provenance applies, written at the 9b batch confirmation (batch mode). Class docstring rewritten from the XSD evidence (the fabricated pre-sync docstring wiped, Rule 0012.2.3); checklist rebuilt to the 6-column XSD-only form. Reader/writer coverage pre-existed complete as matched Rule 0013.2 pairs (no change) — round-trip tests added this pass (parser TestEcucContainerDefDestinationUriRefs, writer TestWriterEcucDestinationUriRefs incl. save→reload with value/DEST/BASE asserts). No Rule 0001.10 missing referenced classes (RefType is the stamped base; EcucDestinationUriDef is the destination-side class, stamped separately).

## `BufferProperties`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 199  | **table:** Table 4.88
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(not modeled)* | `—` | `bufferComputation` | `CompuScale` | — | deprecated (atp.Status=removed), not implemented — XSD group `BUFFER-PROPERTIES` (`AUTOSAR_00052.xsd` L12926) carries `BUFFER-COMPUTATION` with `atp.Status="removed"`; absent from the R23-11 PDF Table 4.88 `Attribute` rendering (Rule 0015) |

**Note:** Batch sync 2026-10-04 (Group28 row; full re-sync per Rule 0023 — the pre-existing checklist was the pre-release-column format and carried a stale `# Spec verified: R23-11` stamp citing the SystemTemplate rendering). Both Table 4.88 attributes are modeled with the PDF types and multiplicity (`Integer 0..1` → `Optional[Integer]`, `Boolean 0..1` → `Optional[Boolean]`) in the markdown displayed row order `headerLength`, `inPlace`; Base `ARObject` ⇒ most-derived Python base `ARObject`, `__init__(self)`. Cross-checked the second rendering AUTOSAR_CP_TPS_SystemTemplate.md Table 7.5, p.767 — identical rows and order. The stale marker was removed (stamp withheld pending the 9b batch confirmation, user instruction); checklist rebuilt to the 6-column format citing the defining SWCT table. Docstrings verified character-for-character against the markdown `Note` cells (wipe-and-rewrite produced identical text — already verbatim); the class docstring keeps the class-level `constr_9279`/`constr_9280` rows. Reader/writer coverage pre-existed complete as matched Rule 0013.2 pairs (`getChildElementOptionalIntegerValue`/`setChildElementOptionalIntegerValue`, `…BooleanValue` pair; XSD order HEADER-LENGTH, IN-PLACE; no chained mutators) — no parser/writer change. Dedicated tests added: model `test_BufferProperties.py` (defaults, round-trip + None no-op), parser `TestBufferPropertiesReader` (full/empty-wrapper/absent), writer `TestWriterBufferProperties` + `TestBufferPropertiesRoundTrip` (full/empty/none + save→reload value asserts). No Rule 0001.10 missing referenced classes (`Integer`, `Boolean` are primitives).

## `TransformerClassEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 200  | **table:** Table 4.90
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

No deviations — all 4 `Literal` rows modeled 1:1 in displayed order (`custom`, `safety`, `security`, `serializer`), member values exactly the spec literals, member names their UPPER_CASE forms; AREnum base (Rule 0010).

**Note:** Batch sync 2026-10-04 (Group28 row; re-sync of a pre-existing enum — the checklist carried a stale `# Spec verified: R23-11` stamp citing the SystemTemplate rendering; the stamp was removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). `# Spec:` re-cited to the defining document SWCT Table 4.90, p.200; cross-checked the second rendering AUTOSAR_CP_TPS_SystemTemplate.md Table 7.4, p.765 — byte-identical (same Package/Note/Aggregated by/4 literals with identical descriptions and atp.EnumerationLiteralIndex tags). Class docstring + per-literal comments verified character-for-character against the markdown (wipe-and-rewrite produced identical text — already verbatim, Tags tails kept per Rule 0011). Mirrored model test added (`test_TransformerClassEnum.py`: instantiation, exact member values + getEnumValues order, setValue round-trip + None no-op, validateEnumValue). Steps 5/6 N/A (standalone enum, no own XML element): consumer round-trip verified — parser `arxml_parser.py` l.12807 `setTransformerClass(getChildElementOptionalLiteral(element, "TRANSFORMER-CLASS"))` asserted by `test_readTransformationTechnology_with_properties` (`getValue() == "safety"`), writer `arxml_writer.py` l.16312 `setChildElementOptionalLiteral(..., tech.getTransformerClass())` asserted by `test_writeTransformationTechnology_full`; no consumer gap, no enum-specific token map. No Rule 0001.10 missing referenced classes.

## `E2EProfileCompatibilityProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 202  | **table:** Table 4.93
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

No deviations — the single Table 4.93 attribute `transitToInvalidExtended` (Boolean, 0..1, attr) is modeled as `Optional[Boolean]` field + `getTransitToInvalidExtended`/`setTransitToInvalidExtended` pair; Base chain most-derived `ARElement` (XSD complexType `E-2-E-PROFILE-COMPATIBILITY-PROPS`, `AUTOSAR_00052.xsd` L50004, refs the base groups then the own group); aggregated by `ARPackage.element` (factory `ARPackage.createE2EProfileCompatibilityProps` pre-exists).

**Note:** Batch sync 2026-10-04 (Group28 row; full re-sync per Rule 0023 — the pre-existing checklist was the pre-release-column format and carried a stale `# Spec verified: R23-11` stamp citing the SystemTemplate rendering; the stamp was removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). `# Spec:` re-cited to the defining document SWCT Table 4.93, p.202; cross-checked the second rendering AUTOSAR_CP_TPS_SystemTemplate.md Table 7.25, p.808 — identical rows and order. Class docstring + per-member comment/getter/setter docstrings verified character-for-character against the markdown `Note` cells (wipe-and-rewrite produced identical text — already verbatim; class docstring keeps the `Tags: atp.recommendedPackage=E2EProfileCompatibilityPropsCollection` tail per repo convention). Model Red vacuous (impl already conformed) — mirrored test `test_E2EProfileCompatibilityProps.py` added (defaults, short-name/parent wiring, round-trip + None no-op) and passes on first run. Reader/writer coverage pre-existed complete as matched Rule 0013.2 pairs (parser l.12825 `readE2EProfileCompatibilityProps` → `readARElement` + `setTransitToInvalidExtended(getChildElementOptionalBooleanValue(...))`; writer l.16312 `writeE2EProfileCompatibilityProps` → `writeIdentifiable` + `setChildElementOptionalBooleanValue(..., getTransitToInvalidExtended())`; ARPackage dispatch both sides at parser l.16673 / writer l.16714; XML order per XSD group — own element last; no chained mutators) — no parser/writer change. Dedicated tests added: parser `TestE2EProfileCompatibilityPropsReader` (true/false/empty-wrapper via `readARPackageElementsRest` dispatch), writer `TestE2EProfileCompatibilityPropsWriter` + `TestE2EProfileCompatibilityPropsRoundTrip` (full/empty/none, ARPackage dispatch, parametrized save→reload true/false + empty). No Rule 0001.10 missing referenced classes (`Boolean`, `ARElement` are stamped primitives/base classes).

## `EndToEndProtection`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 215  | **table:** Table 4.97
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py`

No deviations — all three Table 4.97 attributes are modeled with spec shapes: `endToEndProfile` (EndToEndDescription, 0..1, aggr) as `Optional[EndToEndDescription]` field + `getEndToEndProfile`/`setEndToEndProfile` pair (child is ARObject-based, non-Referrable → set shape per Rule 0001.6); `endToEndProtectionISignalIPdu` (EndToEndProtectionISignalIPdu, `*`, aggr) and `endToEndProtectionVariablePrototype` (EndToEndProtectionVariablePrototype, `*`, aggr) as dedicated typed list fields + `addXxx`/`getXxxs` pairs (no registry filtering). Base chain most-derived `Identifiable` (XSD complexType `END-TO-END-PROTECTION`, `AUTOSAR_00052.xsd` L54284, refs AR-OBJECT/REFERRABLE/MULTILANGUAGE-REFERRABLE/IDENTIFIABLE groups — no ARELEMENT); VARIATION-POINT anchored on group `END-TO-END-PROTECTION` (L54229, "Applicable for: EndToEndProtectionSet.endToEndProtection") → `VariationPointCapable` mixin kept (Rule 0020, checklist carries no VP rows — mixin-owned).

**Note:** Batch sync 2026-10-04 (Group28 row; full re-sync per Rule 0023 — the pre-existing checklist was the legacy 3-column format (rows ended at `test`, no `# Spec:` line, no release column) and carried NO stamp; rewritten in the 6-column format, marker WITHHELD pending the 9b batch confirmation, user instruction). Cross-checked the second rendering AUTOSAR_CP_TPS_SystemTemplate.md Table 6.55, p.384 — identical rows and order. Markdown PDF-conversion wrap artifacts in the `Note` cells (e.g. "End ToEndProtection", "EndTo Endprotection") were repaired to the true spec text as carried by the XSD `xsd:documentation` of the same attributes (including the spec's own "EndToEndprotection" spelling quirk); `Stereotypes:`/`Tags:` tails dropped per Rule 0012.2.5.2. Model Red genuine (3 failed: verbatim docstrings, verbatim Notes, type-hint pins/accessor order — accessors were untyped and paraphrased, list getters preceded mutators); model Green 27 passed. Accessors retyped per Rule 0003, reordered mutator-first per Rule 0001.11, module converted to PEP 563 (`from __future__ import annotations`) with all quoted return annotations unquoted module-wide, `EndToEndProtectionISignalIPdu` moved from `TYPE_CHECKING` to a real runtime import (Rule 0001.8 — name must resolve for `get_type_hints` pin tests on 3.8). Reader coverage pre-existed complete (parser `readEndToEndProtection` → `readIdentifiable`, which already reads VARIATION-POINT position-independently — parser Red vacuous); writer had a genuine VP-order bug: `writeIdentifiable` emitted VARIATION-POINT inline BEFORE the own-group elements, violating the XSD sequenceOffset 10000 (VP last) — fixed by `writeIdentifiable(..., write_variation_point=False)` + trailing `writeVariationPointCapable` (established pattern, 10 prior call sites). Dedicated tests added: parser `TestEndToEndProtectionReader` (full field values incl. VP, empty/absent wrappers), writer `TestEndToEndProtectionWriter` + `TestEndToEndProtectionRoundTrip` (full element order + values, empty wrappers omitted, none, save→load round-trips with field values). No Rule 0001.10 missing referenced classes: `EndToEndDescription` and `EndToEndProtectionVariablePrototype` (same file) and `EndToEndProtectionISignalIPdu` (SystemTemplate, Table 6.56) are fully populated synced classes — `EndToEndProtectionISignalIPdu` is marker-less only because its own 9b confirmation is deferred to the batch, not a stub.

## `ConsistencyNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 222  | **table:** Table 4.99
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ImplicitCommunicationBehavior/__init__.py`

No own deviations — all four Table 4.99 attributes are modeled with spec shapes: `dpgDoesNotRequireCoherency`, `dpgRequiresCoherency` (DataPrototypeGroup, `*`, aggr) and `regDoesNotRequireStability`, `regRequiresStability` (RunnableEntityGroup, `*`, aggr) as dedicated typed list fields + `createXxx(short_name)`/`getXxxs()` pairs (children are Referrable via `AtpStructureElement` → `Identifiable`, so the create shape is correct per Rule 0001.6; no registry filtering). Base chain most-derived `AtpBlueprint` — FIXED this pass from the pre-existing `AtpBlueprintable` (Rule 0001.2; XSD complexType `CONSISTENCY-NEEDS`, `AUTOSAR_00052.xsd` L22071, refs the groups in order AR-OBJECT/REFERRABLE/MULTILANGUAGE-REFERRABLE/IDENTIFIABLE/ATP-BLUEPRINT/ATP-BLUEPRINTABLE — `AtpBlueprint` extends `AtpBlueprintable`; the base itself is stamped R23-11, no base sync needed). VARIATION-POINT anchored directly on group `CONSISTENCY-NEEDS` (L22004, "Applicable for: ConsistencyNeedsBlueprintSet.consistencyNeeds / SwComponentType.consistencyNeeds", xml.sequenceOffset 10000 → last element) → `VariationPointCapable` mixin kept (Rule 0020, checklist carries no VP rows — mixin-owned).

**Note:** Batch sync 2026-10-04 (Group28 row; full re-sync per Rule 0023 — the pre-existing checklist was the pre-release-column format and carried a stale `# Spec verified: R23-11` stamp; the marker was removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). Field names pluralized per Rule 0001.4 (singular spec `*` names → plural list fields `dpgDoesNotRequireCoherencys`/`dpgRequiresCoherencys`/`regDoesNotRequireStabilitys`/`regRequiresStabilitys`); docstrings wiped and rewritten verbatim from the markdown `Note` cells (`Stereotypes:`/`Tags:` tails dropped per Rule 0012.2.5.2); module keeps quoted self-referential return annotations (no PEP 563 conversion — `DataPrototypeGroup`/`RunnableEntityGroup` are later queue rows and must not be touched beyond this class's needs). Model Red genuine (6 failed: base chain, plural fields, verbatim class/init/method docstrings); the 4 create*/get* tests passed unchanged (vacuous — impl already conformed). Reader coverage pre-existed complete (parser `readConsistencyNeeds` → `readIdentifiable`, which already reads VARIATION-POINT position-independently into the `VariationPointCapable` mixin — parser Red vacuous, 3 reader tests pass unmodified after fixture fixes only); writer had the same genuine VP-order bug as EndToEndProtection: `writeIdentifiable` emitted VARIATION-POINT inline BEFORE the four wrapper lists, violating the XSD sequenceOffset 10000 — fixed by `writeIdentifiable(..., write_variation_point=False)` + trailing `writeVariationPointCapable` in `writeConsistencyNeeds`. Dispatch sites pre-exist both sides (parser `readSwComponentTypeConsistencyNeeds` L7960 + ARPackage generic dispatch L16199; writer `writeSwComponentTypeConsistencyNeeds` L2932 + isinstance dispatch L16781) — unchanged. Dedicated tests added: parser `TestConsistencyNeedsReader` (full field values incl. one-level-down irefs and VP, empty/absent wrappers), writer `TestWriteConsistencyNeedsVariationPoint` (VP last per XSD order, VP omitted when unset, save→load round-trip) on top of the pre-existing wrapper round-trip tests. Inherited placeholder (owned by the stamped base, not this class): `AtpBlueprint.blueprintPolicys` reader/writer rows stay [ ] per its accepted 2026-09-26 deviation — the concrete BlueprintPolicy subtypes (BlueprintPolicyList/-NotModifiable/-Single) are unsynced, so the BLUEPRINT-POLICYS element (ATP-BLUEPRINT group) is not round-tripped for `ConsistencyNeeds` either. Referenced member types `DataPrototypeGroup` (Table 4.101) / `RunnableEntityGroup` (Table 4.100) exist as fully modeled classes in the same module; their own Rule 0023 re-syncs are later Group28 queue rows.

## `RunnableEntityGroup`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 223  | **table:** Table 4.100
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ImplicitCommunicationBehavior/__init__.py`

No deviations — both Table 4.100 attributes are modeled with spec shapes: `runnableEntity` (RunnableEntity, `*`, iref → `RunnableEntityInCompositionInstanceRef`, Table D.21) and `runnableEntityGroup` (RunnableEntityGroup, `*`, iref → `InnerRunnableEntityGroupInCompositionInstanceRef`, Table D.20) as dedicated typed list fields `runnableEntityIRefs`/`runnableEntityGroupIRefs` + `addXxx(Optional[T])`/`getXxxs()` pairs (Kind-suffix `IRef`/`IRefs` per Rule 0001.5; no registry filtering). Base chain most-derived `AtpStructureElement` (Table 5.5, stamped R23-11 — no base sync needed; XSD complexType `RUNNABLE-ENTITY-GROUP`, `AUTOSAR_00052.xsd` L101436, refs ATP-CLASSIFIER/ATP-FEATURE/ATP-STRUCTURE-ELEMENT groups). VARIATION-POINT anchored on group `RUNNABLE-ENTITY-GROUP` (L101393, "Applicable for: ConsistencyNeeds.regRequiresStability / ConsistencyNeeds.regDoesNotRequireStability", xml.sequenceOffset 10000 → last element) → `VariationPointCapable` mixin kept (Rule 0020, checklist carries no VP rows — mixin-owned).

**Note:** Batch sync 2026-10-04 (Group28 row; full re-sync per Rule 0023 — the pre-existing checklist was the pre-release-column format and carried a stale `# Spec verified: R23-11` stamp; the marker was removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). Table 4.100 is page-split (p.223→224): the markdown renders the Class/Package/Note/Base/Aggregated-by rows + the `runnableEntity` attribute row before the caption and the `runnableEntityGroup` row after it — displayed order (runnableEntity, runnableEntityGroup) is the class member order; XSD element order is independent (RUNNABLE-ENTITY-GROUP-IREFS, RUNNABLE-ENTITY-IREFS, VARIATION-POINT last). Model Red vacuous (impl already conformed — base, plural IRef fields, guarded adds, mixin all in place; noted); the sync added a VP-capability pin test, converted the module to PEP 563 (`from __future__ import annotations`) unquoting all 4 self-referential return annotations (2 on `DataPrototypeGroup` forced by the same-change rule — this completes the conversion the ConsistencyNeeds pass deferred to this class), and wiped/rewrote the class docstring, `__init__` member comments and method docstrings verbatim from the markdown `Note` cells (`Stereotypes:`/`Tags:` tails dropped per Rule 0012.2.5.2; `__init__` docstring removed). Reader coverage pre-existed complete (parser `readRunnableEntityGroup` → `readIdentifiable`, which already reads VARIATION-POINT position-independently into the `VariationPointCapable` mixin — parser Red vacuous, `TestRunnableEntityGroupReader` full field values + empty/absent wrappers added); writer had the genuine VP-order bug (same as EndToEndProtection/ConsistencyNeeds): `writeIdentifiable` emitted VARIATION-POINT inline BEFORE the two iref wrapper lists, violating the XSD sequenceOffset 10000 — fixed by `writeIdentifiable(..., write_variation_point=False)` + trailing `writeVariationPointCapable` in `writeRunnableEntityGroup` (writer Red genuine: `test_write_variation_point_last` failed with `['SHORT-NAME', 'VARIATION-POINT', 'RUNNABLE-ENTITY-GROUP-IREFS']` before the fix). Dispatch sites pre-exist both sides (parser `readConsistencyNeedsReg*Stabilitys` + ARPackage generic dispatch L16196; writer `writeConsistencyNeedsReg*Stabilitys` + isinstance dispatch L16771) — unchanged. `DataPrototypeGroup` (Table 4.101, same module) is a later Group28 queue row and was NOT touched beyond the forced annotation unquoting; its writer had the same latent VP-order bug — fixed in the DataPrototypeGroup pass (2026-10-04, see below).

## `DataPrototypeGroup`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 223  | **table:** Table 4.101
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ImplicitCommunicationBehavior/__init__.py`

No deviations — both Table 4.101 attributes are modeled with spec shapes: `dataPrototypeGroup` (DataPrototypeGroup, `*`, iref → `InnerDataPrototypeGroupInCompositionInstanceRef`, Table D.19) and `implicitDataAccess` (VariableDataPrototype, `*`, iref → `VariableDataPrototypeInCompositionInstanceRef`, Table D.22) as dedicated typed list fields `dataPrototypeGroupIRefs`/`implicitDataAccessIRefs` + `addXxx(Optional[T])`/`getXxxs()` pairs (Kind-suffix `IRef`/`IRefs` per Rule 0001.5; children are `AtpInstanceRef` → `ARObject`, not Referrable, so the add shape is correct per Rule 0001.6; no registry filtering). Base chain most-derived `AtpStructureElement` (Table 5.5, stamped R23-11 — no base sync needed; XSD complexType `DATA-PROTOTYPE-GROUP`, `AUTOSAR_00052.xsd` L27411, refs ATP-CLASSIFIER/ATP-FEATURE/ATP-STRUCTURE-ELEMENT groups). VARIATION-POINT anchored on group `DATA-PROTOTYPE-GROUP` (L27368, "Applicable for: ConsistencyNeeds.dpgRequiresCoherency / ConsistencyNeeds.dpgDoesNotRequireCoherency", xml.sequenceOffset 10000 → last element) → `VariationPointCapable` mixin kept (Rule 0020, checklist carries no VP rows — mixin-owned).

**Note:** Batch sync 2026-10-04 (Group28 row; full re-sync per Rule 0023 — the pre-existing checklist was the pre-release-column format and carried a stale `# Spec verified: R23-11` stamp; the marker was removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). Model Red vacuous (impl already conformed — base, plural IRef fields, guarded adds, mixin all in place; noted); the sync added a VP-capability pin test and wiped/rewrote the class docstring, `__init__` member comments and method docstrings verbatim from the markdown `Note` cells (`Stereotypes:`/`Tags:` tails dropped per Rule 0012.2.5.2; `__init__` docstring and Args/Returns blocks removed). Reader coverage pre-existed complete (parser `readDataPrototypeGroup` → `readIdentifiable`, which already reads VARIATION-POINT position-independently into the `VariationPointCapable` mixin — parser Red vacuous, `TestDataPrototypeGroupReader` full field values + empty/absent wrappers added); writer had the genuine VP-order bug flagged by the RunnableEntityGroup pass (same as EndToEndProtection/ConsistencyNeeds/RunnableEntityGroup): `writeIdentifiable` emitted VARIATION-POINT inline BEFORE the two iref wrapper lists, violating the XSD sequenceOffset 10000 — fixed by `writeIdentifiable(..., write_variation_point=False)` + trailing `writeVariationPointCapable` in `writeDataPrototypeGroup` (writer Red genuine: `test_write_variation_point_last` failed with `['SHORT-NAME', 'VARIATION-POINT', 'DATA-PROTOTYPE-GROUP-IREFS']` before the fix). Dispatch sites pre-exist both sides (parser `readConsistencyNeedsDpg*Coherencys` + ARPackage generic dispatch L16193; writer `writeConsistencyNeedsDpg*Coherencys` + isinstance dispatch L16770) — unchanged. Referenced member types `InnerDataPrototypeGroupInCompositionInstanceRef` (Table D.19) / `VariableDataPrototypeInCompositionInstanceRef` (Table D.22) exist and are stamped R23-11; no missing classes.

## `ArraySizeSemanticsEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 253  | **table:** Table 5.10
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`

No deviations — both `Literal` rows modeled 1:1 in displayed order (`fixedSize`, `variableSize`), member values exactly the spec literals, member names their UPPER_CASE forms; AREnum base (Rule 0010). Placement kept in `CommonStructure/ImplementationDataTypes.py` — the spec's own Package row (SWCT Table 5.10 and DEXT Table 4.10 alike) is `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`.

**Note:** Batch sync 2026-10-04 (Group28 row; re-sync of a pre-existing enum — the checklist carried a stale `# Spec verified: R23-11` stamp in the 5-column pre-release-column format; the stamp was removed at session start and stays WITHHELD pending the 9b batch confirmation, user instruction). Cited the defining document SWCT Table 5.10, p.253; cross-checked the second rendering AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md Table 4.10, p.43 — content-identical (same Package/Note/Aggregated by/2 literals with identical descriptions and atp.EnumerationLiteralIndex tags; the DEXT markdown renders the table split, header rows before the caption and the literal rows after, but the text agrees — defining doc SWCT wins, no conflict). Class docstring + per-literal comments verified character-for-character against the markdown (wipe-and-rewrite produced identical text — already verbatim, Tags tails kept per Rule 0011). Model test battery replaced in the mirrored `test_ImplementationDataTypes.py` (`TestArraySizeSemanticsEnum`: instantiation + isinstance AREnum, exact member values + getEnumValues order, setValue round-trip + None no-op, validateEnumValue, class-docstring verbatim pin). Steps 5/6 N/A (standalone enum, no own XML element): consumer round-trip verified on all 4 aggregated-by attributes — parser `arxml_parser.py` l.6499 (`getSwTextProps`), l.7406 (`readImplementationDataTypeElement`), l.9183 (`readApplicationArrayElement`) read `ARRAY-SIZE-SEMANTICS` via `getChildElementOptionalLiteral` + cast and l.11145 (`readDiagnosticDataElement`) materializes `ArraySizeSemanticsEnum().setValue(...)`; writer `arxml_writer.py` l.3915/8640/8787/14791 emit `setChildElementOptionalLiteral(..., getArraySizeSemantics())`; consumer tests 14 passed (`test_ApplicationArrayElement.py` + `test_SwTextProps.py` reader, `test_writer_ApplicationArrayElement.py` + `test_writer_SwTextProps.py` writer); literals `fixedSize`/`variableSize` round-trip, no enum-specific token map. The typed-instantiation vs cast materialization difference between reader sites is the consumer-side pattern shared with sibling `ArraySizeHandlingEnum`, not an enum value-mapping gap — flagged for 9b review, no fix. No Rule 0001.10 missing referenced classes.

## `ArraySizeHandlingEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 254  | **table:** Table 5.11
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

No deviations — all three `Literal` rows modeled 1:1 in displayed order (`allIndicesDifferentArraySize`, `allIndicesSameArraySize`, `inheritedFromArrayElementTypeSize`), member values exactly the spec literals, member names their UPPER_CASE forms; AREnum base (Rule 0010). Placement kept in `SWComponentTemplate/Datatype/Datatypes.py` — the spec's own Package row (SWCT Table 5.11) is `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`.

**Note:** Batch sync 2026-10-04 (Group28 row; re-sync of a pre-existing enum — the checklist carried a stale `# Spec verified: R23-11` stamp in the 5-column pre-release-column format with a p.253 citation; the stamp was removed at session start (Rule 0023) and stays WITHHELD pending the 9b batch confirmation, user instruction; `# Spec:` page corrected to p.254 per pdf_page.py). The SWCT markdown renders Table 5.11 page-split (body Package/Note/Aggregated-by rows + literals 0-1 before the caption, p.254 continuation carries the repeated Enumeration header + literal 2); the spaces inside the literal names ("allIndicesDifferent ArraySize") are markdown word-wrap artifacts — XSD `AUTOSAR_00052.xsd` mmt.qualifiedName confirms the camelCase forms. Class docstring + per-literal comments verified character-for-character against the markdown (wipe-and-rewrite produced identical text — already verbatim, Tags tails kept per Rule 0011). Model test battery replaced in the mirrored `test_Datatypes.py` (`TestArraySizeHandlingEnum`: instantiation + isinstance AREnum, exact member values + getEnumValues order, setValue round-trip + None no-op, validateEnumValue, class-docstring verbatim pin). Steps 5/6 N/A (standalone enum, no own XML element): consumer round-trip verified on both aggregated-by attributes — parser `arxml_parser.py` l.7405 (`readImplementationDataTypeElement`) and l.9182 (`readApplicationArrayElement`) read `ARRAY-SIZE-HANDLING` via `getChildElementOptionalLiteral` + cast; writer `arxml_writer.py` l.8639 / l.8786 emit `setChildElementOptionalLiteral(..., getArraySizeHandling())`; consumer tests assert values (e.g. writer `ARRAY-SIZE-HANDLING` text `allIndicesSameArraySize`, reader round-trips the UPPERCASE XSD form). The typed-vs-cast materialization on the reader side is the consumer pattern shared with sibling `ArraySizeSemanticsEnum`, not an enum value-mapping gap — flagged for 9b review, no fix. No Rule 0001.10 missing referenced classes.

## `BaseType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 292  | **table:** Table 5.26
- **Package:** `M2::MSR::AsamHdo::BaseTypes`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py`

No deviations — the single Table 5.26 attribute is modeled with the spec shape: `baseTypeDefinition` (BaseTypeDefinition, `1`, aggr) as the PEP 526 member `baseTypeDefinition: BaseTypeDirectDefinition` (plain T — Mult 1, pre-initialized per the constr_1910 existence constraint) + `getBaseTypeDefinition()`/`setBaseTypeDefinition()` (child `Base` is `ARObject, BaseTypeDefinition` — non-Referrable, so set/get shape per Rule 0001.6, no `createXxx`). The spec type is the abstract `BaseTypeDefinition`; the field/getter/setter are typed with its only concrete subclass `BaseTypeDirectDefinition` (the XSD group BASE-TYPE choice, AUTOSAR_00052.xsd L8384, admits only the BASE-TYPE-DIRECT-DEFINITION group and the abstract type is not instantiable) — a refinement of the spec type, not type drift. The aggregation is flattened in XML (Tags `xml.roleElement/typeWrapperElement/typeElement/roleWrapperElement` all false): the BASE-TYPE-DIRECT-DEFINITION group content sits inline under SW-BASE-TYPE — reader `readBaseTypeDirectDefinition` / writer `setBaseTypeDirectDefinition` (both reached via `getBaseTypeDefinition()` from the concrete-element helpers `readSwBaseType`/`writeSwBaseType`) cover it in XSD sequenceOffset order (BASE-TYPE-SIZE 70, BASE-TYPE-ENCODING 90, MEM-ALIGNMENT 100, BYTE-ORDER 110, NATIVE-DECLARATION 120; MAX-BASE-TYPE-SIZE 80 is `atp.Status="removed"` → not modeled, Rule 0001.3). Base most-derived = ARElement; abstract (Subclasses: SwBaseType) → ABC + instantiation guard; no VARIATION-POINT in the BASE-TYPE or SW-BASE-TYPE XSD groups → not VP-capable (Rule 0020).

**Note:** Batch re-sync 2026-10-04 (Group28 row, synced ahead of its dependent SwBaseType per Rule 0001.10/0016.5 — exists-but-legacy counts as not synced; Rule 0023 legacy checklist with reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed at session start, stamp WITHHELD pending the 9b batch confirmation, user instruction; `# Spec:` page corrected p.291 → p.292 per pdf_page.py). Table 5.26 renders page-split (Class/Package/Note/Base/Subclasses/Aggregated-by/Attribute header before the caption, the `baseTypeDefinition` row after it — displayed order preserved). Class docstring wiped and rewritten verbatim from the markdown Note with constr_1910 appended (targets the existing baseTypeDefinition row, ApplicationArrayDataType precedent); accessor docstrings wiped and rewritten verbatim — the setter's None-no-op sentence moved inline into the Note paragraph (batch convention, SwTextProps/ApplicationArrayDataType form). Model Red: genuine on the class-docstring pin (constr_1910 missing) + the setter docstring pin (two-paragraph None-no-op form); behavioral tests passed (impl already conformed — vacuous behavioral Red portion, noted). Reader/writer tests added on both sides (parser `test_SwBaseType.py`, writer `test_writer_SwBaseType.py`): first parser run failed on the harness passing the wrapper root instead of the concrete SW-BASE-TYPE element to `readSwBaseType` — corrected to the concrete element (as the production dispatch does); no implementation defect; parser/writer source unchanged (coverage pre-existed in XSD order). Referenced member types `BaseTypeDirectDefinition` (Table 5.24), `BaseTypeEncodingString` (Table 5.25) and `ByteOrderEnum` (Table 5.27) are queued separately in Group28 — no missing classes.

## `SwBaseType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 290  | **table:** Table 5.22
- **Package:** `M2::MSR::AsamHdo::BaseTypes`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py`

No deviations — Table 5.22 has zero Attribute rows and SwBaseType declares no own fields (the `baseTypeDefinition` aggregation is inherited from `BaseType`, Table 5.26 — synced ahead of it in the same batch). The Base column names two parallel chains (`…BaseType…` and `AtpBlueprint, AtpBlueprintable`); the role-matching branch selects `BaseType` (most-derived, Rule 0001.2) — no Python multiple inheritance. Concrete class (no `(abstract)` marker), aggregated by `ARPackage.element` → full five-place dispatch present (model class, ARPackage `createSwBaseType` factory, parser `SW-BASE-TYPE` branch + `readSwBaseType`, writer isinstance branch + `writeSwBaseType`, dispatch round-trip tests). The XSD group SW-BASE-TYPE (AUTOSAR_00052.xsd L114677) is empty → no own XML elements; not VP-capable (Rule 0020). The §5.2.6.2 constraints constr_1011/constr_1422/constr_1012 reference `SwBaseType.category`, which has no Attribute row in Table 5.22 and no element in the XSD group — removed upstream, not modeled (Rule 0015/0001.3: no field, and no deviation row since there is nothing to merge); the class docstring therefore stays the bare verbatim Note (SwTextProps precedent for the same document).

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist with no per-row release column, stale `# Spec verified: R23-11` marker removed at session start, stamp WITHHELD pending the 9b batch confirmation, user instruction). Model Red vacuous (impl already conforms — base, zero own attrs, verbatim docstring; noted). Reader/writer tests extended on both sides (parser `test_SwBaseType.py` field-value assertions; writer `test_writer_SwBaseType.py` element order vs the flattened XSD groups + populated/empty save→reload round-trips through the ARPackage dispatch) — coverage pre-existed and conforms (vacuous Red noted); parser/writer source unchanged. Referenced types: base `BaseType` (Table 5.26, synced this batch per Rule 0001.10); `BaseTypeDefinition`/`BaseTypeDirectDefinition` (Tables 5.23/5.24) and the member enums/primitives (`BaseTypeEncodingString` Table 5.25, `ByteOrderEnum` Table 5.27) exist and are behaviorally complete, queued for their own Group28 passes — no missing classes.

## `BaseTypeDefinition`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 290  | **table:** Table 5.23
- **Package:** `M2::MSR::AsamHdo::BaseTypes`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py`

No deviations — Table 5.23 has zero Attribute rows and BaseTypeDefinition declares no own fields (the Subclasses row names BaseTypeDirectDefinition, whose own Group28 pass follows; the `BaseType.baseTypeDefinition` aggregation is typed with that concrete subclass — see the BaseType Table 5.26 entry). Abstract Class confirmed (header `BaseTypeDefinition (abstract)`); Base = ARObject only → `(ARObject, ABC)` with the instantiation guard and `__init__(self)` per the ARObject-only base (Rule 0001.2). The XSD group BASE-TYPE-DEFINITION (AUTOSAR_00052.xsd L8395) is empty (`<xsd:sequence/>`) → the class owns no XML element and no XML-bearing attributes → the concrete-subclass helpers `readBaseTypeDirectDefinition`/`setBaseTypeDirectDefinition` serialize the aggregation (Steps 5/6 N/A per the abstract-class-without-XML-attributes exception, Rule 0001.7); not VP-capable (Rule 0020).

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist with no per-row release column, stale `# Spec verified: R23-11` marker removed at session start, stamp WITHHELD pending the 9b batch confirmation, user instruction). Model Red vacuous (impl already conforms — base, zero own attrs, verbatim class docstring; noted); parser/writer source unchanged (coverage pre-existed on the concrete-subclass path, vacuous reader/writer Red noted). Referenced types: subclass `BaseTypeDirectDefinition` (Table 5.24, queued for its own Group28 pass — untouched here) and consumer `BaseType` (Table 5.26, synced this batch) — no missing classes.

## `ByteOrderEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 297  | **table:** Table 5.27
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`

No deviations — all three `Literal` rows modeled 1:1 in displayed order (`mostSignificantByteFirst`, `mostSignificantByteLast`, `opaque`), member values exactly the spec literals, member names their UPPER_CASE forms; AREnum base (Rule 0010). Placement kept in `GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py` — the spec's own Package row (SWCT Table 5.27, SystemTemplate Table 7.12 and DEXT Table 4.22 alike) is `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`.

**Note:** Batch sync 2026-10-04 (Group28 row; re-sync of a pre-existing enum — the checklist carried a stale `# Spec verified: R23-11` stamp; the stamp was removed at session start (Rule 0023) and stays WITHHELD pending the 9b batch confirmation, user instruction). All three renderings cross-checked — SWCT Table 5.27 p.297 (defining), SystemTemplate Table 7.12 p.779, DEXT Table 4.22 p.67 — content-identical (same Package/Note/Aggregated by/3 literals with identical descriptions and atp.EnumerationLiteralIndex tags; the DEXT markdown renders only the literal rows, header rows absent — defining doc SWCT wins, no conflict). XSD cross-check: `AUTOSAR_00052.xsd` L132015 `BYTE-ORDER-ENUM` / `BYTE-ORDER-ENUM--SIMPLE` — enumeration values are the UPPERCASE kebab tokens (`MOST-SIGNIFICANT-BYTE-FIRST`/`MOST-SIGNIFICANT-BYTE-LAST`/`OPAQUE`), mmt.qualifiedName the camelCase literals; the "mostSignificantByte First" spacing in the markdown is a word-wrap artifact (ArraySizeHandlingEnum precedent). Class docstring + per-literal comments verified character-for-character against the markdown (wipe-and-rewrite produced identical text — already verbatim, Tags tails kept per Rule 0011). Model tests extended in the mirrored `test_PrimitiveTypes.py` (`TestByteOrderEnum`: added setValue round-trip + None no-op to the existing member/value battery; model Red vacuous — enum already spec-complete from a prior pass, noted).

**BYTE-ORDER XML-token decision (this pass owns the question flagged by the BaseTypeDirectDefinition pass):** the repo's established convention for enums whose XSD serialization differs from the camelCase member value IS the literal→token map (`_readEnumToken`/`_writeEnumToken` + `*_XML_MAP`; 17 diagnostic consumers; `BYTE_ORDER_XML_MAP` already defined in both `arxml_parser.py` and `arxml_writer.py` for `DiagnosticCommonProps.defaultEndianness`). Applied it to the 7 remaining consumer site pairs — parser `readBaseTypeDirectDefinition` (BYTE-ORDER), `readSegmentPosition` (SEGMENT-BYTE-ORDER), `readMultiplexedIPdu` (SELECTOR-FIELD-BYTE-ORDER), `readISignalToIPduMapping` + the ISignalToPduMappings loop (PACKING-BYTE-ORDER ×2), `readPduToFrameMappings` (PACKING-BYTE-ORDER), `readSystem` (CONTAINER-I-PDU-HEADER-BYTE-ORDER); writer `setBaseTypeDirectDefinition`, `writeSegmentPosition`, `writeMultiplexedIPdu`, `writeISignalToIPduMapping`, `writeISignalToPduMappings`, `writePduToFrameMappings`, `writeSystem`. Fixture check first: the only integration fixture carrying the family is `tests/integration_tests/test_files/CanSystem.arxml` (`<PACKING-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</PACKING-BYTE-ORDER>` ×4, UPPERCASE XSD form) — the map round-trips it byte-identically (token→member→token) while the model now holds real `ByteOrderEnum` instances; before this pass the writer emitted the XSD-invalid camelCase form whenever the enum was set via its API. Accepted consequence: reader input in the non-XSD camelCase form now warns via `notImplemented` and stores None (was: verbatim passthrough of arbitrary text) — every XSD-valid form is covered by the map. Consumer tests aligned (15 files: parser tests assert the mapped camelCase member after read; writer tests construct via `ByteOrderEnum().setValue(member)` and assert the UPPERCASE token; round-trip tests assert the member value after reload). `ApSomeipTransformationProps.byteOrder` / `SOMEIPTransformationDescription.byteOrder` (Aggregated by rows) are not modeled yet — no reader/writer sites exist; they pick the map up when their classes sync. No Rule 0001.10 missing referenced classes.

## `AutosarDataPrototype`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 306  | **table:** Table 5.29
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py`

No deviations — the single Table 5.29 attribute is modeled with the spec shape: `type` (AutosarDataType, 0..1, tref) as the PEP 526 member `typeTRef: Optional[TRefType]` + `getTypeTRef()`/`setTypeTRef()` (tref → TRef suffix per Rule 0001.5; 0..1 → Optional per Rule 0001.4; guarded chaining setter). Abstract Class confirmed (header `AutosarDataPrototype (abstract)`; Subclasses: ArgumentDataPrototype/ParameterDataPrototype/VariableDataPrototype) → ABC + instantiation guard; Base most-derived = `DataPrototype` (Table 5.28, stamped R23-11 — no flattening: `swDataDefProps` lives on the base's own table, this class declares only `typeTRef`). Abstract-with-own-XML-attributes Rule 0001.7 ownership satisfied: the reusable `readAutosarDataPrototype`/`writeAutosarDataPrototype` helpers exist and are called by all three concrete subclasses. XSD cross-check: group AUTOSAR-DATA-PROTOTYPE (`AUTOSAR_00052.xsd` L7919) holds exactly TYPE-TREF (0..1, DEST `AUTOSAR-DATA-TYPE--SUBTYPES-ENUM`) — no PDF/XSD attribute conflict (Rule 0015). Not VP-capable (no VARIATION-POINT element in the group, no atpVariation aggr row — Rule 0020).

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns present but no per-row release column; stale `# Spec verified: R23-11` marker removed at session start, stamp WITHHELD pending the 9b batch confirmation, user instruction). Model Red genuine on the getter/setter docstring pins (both carried stale google-style Args/Returns blocks → wiped and rewritten to the inline batch convention; the `Stereotypes: isOfType` tail dropped from the inline comment and docstrings per Rule 0012.2.5.2 — flagged for 9b review since the sibling `ApplicationCompositeElementDataPrototype` block keeps the tail in its pre-batch docstrings); behavioral tests passed (impl already conformed — vacuous behavioral Red portion, noted). Reader/writer tests added on both sides exercising the reusable helper pair through concrete subclasses (parser `test_autosar_data_prototype.py`: TYPE-TREF field values + absent→None via VariableDataPrototype; writer `test_autosar_data_prototype.py`: TRefType text/DEST via ParameterDataPrototype, absent→no element emitted, group order TYPE-TREF<INIT-VALUE, full write→parse round-trip) — parser/writer source unchanged (coverage pre-existed and conforms; vacuous reader/writer Red noted). Referenced types: base `DataPrototype` (Table 5.28, stamped), tref target `AutosarDataType` (abstract ARElement in `Datatypes.py` — tref carries DEST, no model-field dependency), `TRefType` (PrimitiveTypes) — no Rule 0001.10 missing classes.

## `ArParameterInImplementationDataInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 324  | **table:** Table 5.38
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/DataElements/__init__.py`

No deviations — all four Table 5.38 attributes are modeled with the spec shape: `contextDataPrototype` (ordered) (AbstractImplementationDataTypeElement, *, ref) as the dedicated typed list `contextDataPrototypeRefs: List[RefType]` + `addContextDataPrototypeRef()`/`getContextDataPrototypeRefs()` (mutator-first accessor order per Rule 0001.11); `portPrototype` (PortPrototype, 0..1, ref), `rootParameterDataPrototype` (ParameterDataPrototype, 0..1, ref) and `targetDataPrototype` (AbstractImplementationDataTypeElement, 0..1, ref) as `Optional[RefType]` members with the plain `Ref` suffix per Rule 0001.5 (inner refs of an `<name>InstanceRef` — Table 5.37 sibling precedent). Concrete Class (Base = `ARObject` — the "`InstanceRef`"-named class takes its base from the spec `Base` column, Rule 0001.2; no-arg `__init__`). Placement: implemented in the spec Package module `DataElements/__init__.py` per Rule 0007 (sibling Table 5.37 + relocation precedent 34245ba14); the 5-line stub in `GenericStructure/GeneralTemplateClasses/ArObject.py` was removed (only that class's block) and the stub-battery row in `test_group21_36_stub_classes.py` re-pointed to the defining module. XSD cross-check: complexType/group `AR-PARAMETER-IN-IMPLEMENTATION-DATA-INSTANCE-REF` (`AUTOSAR_00052.xsd` L5576/L5648) holds exactly the 4 elements — `CONTEXT-DATA-PROTOTYPE-REFS` wrapper (choice unbounded of `CONTEXT-DATA-PROTOTYPE-REF`, DEST `ABSTRACT-IMPLEMENTATION-DATA-TYPE-ELEMENT--SUBTYPES-ENUM`), `PORT-PROTOTYPE-REF`, `ROOT-PARAMETER-DATA-PROTOTYPE-REF`, `TARGET-DATA-PROTOTYPE-REF` — markdown order = XSD sequence order; no PDF/XSD attribute conflict (Rule 0015). Not VP-capable (no VARIATION-POINT element in the complexType, no atpVariation aggr row — Rule 0020). Serialization is nested-only: aggregated solely by `ImplementationDataTypeSubElementRef.parameterImplementationDataTypeElement` (`PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT`, L71876); the parent is an unsynced stub queued at Group1.md:954-955, so the class owns the named reusable `readArParameterInImplementationDataInstanceRef`/`writeArParameterInImplementationDataInstanceRef` helpers (wrapper emitted only when non-empty; XSD group order) and the parent's dispatch branch stays with the parent's own sync (Rule 0001.7 aggregator-pending precedent). No integration fixture carries any of these elements — no Rule 0019 legacy-attribute constraint.

**Note:** Batch sync 2026-10-04 (Group28 row; first sync of a Group21-36 dependency-solving stub — no pre-existing checklist/docstrings, nothing to wipe, `# Spec verified:` stamp WITHHELD pending the 9b batch confirmation, user instruction). Model Red genuine (ImportError — class absent from the spec-package module). Reader/writer tests exercise the reusable helper pair directly on the element the parent will hand over (parser `test_ar_parameter_in_implementation_data_instance_ref.py`: ordered context list field values incl. DEST, empty wrapper → `[]`, absent → defaults; writer `test_ar_parameter_in_implementation_data_instance_ref.py`: field values + XSD group order wrapper<PORT<ROOT<TARGET, empty context list emits no wrapper, all-absent emits nothing, full write→parse round-trip). Referenced types: `RefType` (PrimitiveTypes, stamped); ref targets `AbstractImplementationDataTypeElement`/`PortPrototype`/`ParameterDataPrototype` carry DEST attributes only — no model-field dependency; no Rule 0001.10 missing classes.

## `SwBitRepresentation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 333  | **table:** Table 5.41
- **Package:** `M2::MSR::DataDictionary::DataDefProperties`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py`

No deviations — both Table 5.41 attributes are modeled with the spec shape: `bitPosition` (Integer, 0..1, attr) and `numberOfBits` (Integer, 0..1, attr) as `Optional[Integer]` members with getter-first accessor pairs (`getBitPosition`/`setBitPosition`, `getNumberOfBits`/`setNumberOfBits` — scalar shape, Rule 0001.11), None-guarded chainable setters (Rule 0004), verbatim Table 5.41 Notes in the class docstring, inline `__init__` comments and accessor docstrings (`Tags:` tails dropped per Rule 0012.2.5.2). Concrete Class (Base = `ARObject` — no-arg `__init__`, Rule 0001.2); Kind `attr` rows carry no Ref/TRef/IRef suffix (Rule 0001.5). XSD cross-check: group `SW-BIT-REPRESENTATION` (`AUTOSAR_00052.xsd` L114714) + complexType (L114736) hold exactly the 2 elements `BIT-POSITION`/`NUMBER-OF-BITS` (AR:INTEGER, 0..1, sequenceOffset 20/30) — markdown order = XSD sequence order; no PDF/XSD attribute conflict (Rule 0015). Not VP-capable (no VARIATION-POINT element in the complexType, no atpVariation aggr row — Rule 0020). Reader/writer coverage rides the sole aggregator `SwDataDefProps.swBitRepresentation` (markdown "Aggregated by"; XSD L115486 is the only element reference): parser reads via mutators with `getChildElementOptionalIntegerValue` and the writer emits via `setSwBitRepresentation` + `setChildElementOptionalIntegerValue` getters — matched pairs (Rule 0013.2), children emitted in XSD offset order. Referenced types: `Integer` (PrimitiveTypes, stamped) — no Rule 0001.10 missing classes. No integration fixture carries SW-BIT-REPRESENTATION — no Rule 0019 legacy-attribute constraint.

**Note:** Batch sync 2026-10-04 (Group28 row; the class pre-existed with a legacy 5-column checklist — Rule 0023: stale `# Spec verified: R23-11` marker removed at session start and WITHHELD pending the 9b batch confirmation, user instruction; checklist rewritten in the 6-column format with the R23-11 release column). Model Red vacuous (implementation already conformed — both spec attrs present with the correct shape; the upgraded tests pin member order, accessor order, runtime type-hint resolution, verbatim class Note and None-no-op setters). Reader/writer Red vacuous (parser/writer already covered the class via the SwDataDefProps call sites; new tests add per-field optionality: partial NUMBER-OF-BITS-only read, partial + empty SwBitRepresentation write→reload round-trips, and Integer type assertions).

## `SwCalibrationAccessEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 335  | **table:** Table 5.44
- **Package:** `M2::MSR::DataDictionary::DataDefProperties`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py`

No deviations — all three `Literal` rows modeled 1:1 in displayed order (`notAccessible`, `readOnly`, `readWrite`), member values exactly the spec literals, member names their UPPER_CASE forms; AREnum base (Rule 0010). Placement kept in `M2/MSR/DataDictionary/DataDefProperties.py` — the spec Package row is `M2::MSR::DataDictionary::DataDefProperties` (shared module; only this enum's block touched).

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed at session start, stamp WITHHELD pending the 9b batch confirmation, user instruction; checklist rewritten in the 6-column `# (no methods)` form with the R23-11 release suffix and the full Aggregated-by consumer list — ModeDeclarationGroupPrototype.swCalibrationAccess, SwCalprmAxis.swCalibrationAccess, SwDataDefProps.swCalibrationAccess). XSD cross-check: `AUTOSAR_00052.xsd` L143629 `SW-CALIBRATION-ACCESS-ENUM` / L143641 `--SIMPLE` — enumeration values are the UPPERCASE kebab tokens (`NOT-ACCESSIBLE`/`READ-ONLY`/`READ-WRITE`), mmt.qualifiedName the camelCase literals; no `atp.Status="removed"` legacy forms. Class docstring + per-literal comments verified character-for-character against the markdown (wipe-and-rewrite produced identical text — already verbatim, Tags tails kept per Rule 0011). Model Red: one genuine failure on first run — the new None-no-op test asserted `getValue() is None` for a fresh unset enum, but `ARLiteral.value` returns `""` when unset (established codebase behavior, not an enum defect); test corrected to the retain-value no-op contract, the other 6 battery tests passed (enum body already spec-complete — vacuous model-side Red portion, noted).

**SW-CALIBRATION-ACCESS XML-token decision:** same situation as the ByteOrderEnum pass — the XSD serializes UPPERCASE kebab tokens while the member values are the camelCase spec literals, and the integration fixtures carry the XSD form (374× `<SW-CALIBRATION-ACCESS>READ-ONLY</SW-CALIBRATION-ACCESS>`). Applied the canonical `_readEnumToken`/`_writeEnumToken` + `SW_CALIBRATION_ACCESS_XML_MAP` convention (ByteOrderEnum precedent; map defined in both `arxml_parser.py` L1548 and `arxml_writer.py` L1298) to all consumer site pairs — parser `readModeDeclarationGroupPrototype` (replaces the ad-hoc raw-literal + `setValue(raw)` wrap that stored the non-XSD token verbatim), `getSwCalprmAxis`, `getSwDataDefProps` (SW-DATA-DEF-PROPS-CONDITIONAL); writer `setSwCalprmAxis`, `setSwDataDefProps`, `writeModeDeclarationGroupPrototype`, `writeModeSwitchInterfaceModeGroup` (the ModeDeclarationGroupPrototype element has two writer paths). Before this pass the writer emitted the XSD-invalid camelCase form whenever the enum was set via its API, and the reader stored arbitrary text verbatim; after it the token→member→token round-trip is lossless and the model holds real `SwCalibrationAccessEnum` instances. Accepted consequence (same as ByteOrderEnum): reader input in the non-XSD camelCase form now warns via `notImplemented` and stores None — every XSD-valid form is covered by the map. Consumer tests aligned (5 files: parser tests feed the UPPERCASE token and assert the mapped camelCase member; writer tests construct via `SwCalibrationAccessEnum().setValue(member)` and assert the UPPERCASE token; round-trip tests assert the member value after reload). Out-of-scope observation for the 9b reviewer: the SwDataDefProps SW-IMPL-POLICY parser site (arxml_parser.py L7296) still uses the raw `cast` form — the SwImplPolicyEnum consumer conversion (2026-09-27 batch) covered only the Trigger/InternalTriggeringPoint/BswInternalTriggeringPoint sites; belongs to that class's ledger, untouched here. No Rule 0001.10 missing referenced classes.

## `CalprmAxisCategoryEnum`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 353  | **table:** Table 5.48
- **Package:** `M2::MSR::DataDictionary::CalibrationParameter`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py`

No deviations — all four `Literal` rows modeled 1:1 in displayed order (`comAxis`, `fixAXIS`, `resAxis`, `stdAxis`), member values exactly the spec literals, member names their UPPER_CASE forms; AREnum base (Rule 0010). Placement kept in `M2/MSR/DataDictionary/CalibrationParameter.py` — the spec Package row is `M2::MSR::DataDictionary::CalibrationParameter` (shared module; only this enum's block touched). The six `atp.Status="removed"` XSD literals (`COM-AXIS`, `CURVE-AXIS`, `CURVE_AXIS`, `FIX-AXIS`, `RES-AXIS`, `STD-AXIS`) map to no member — deprecated, not implemented (Rule 0001.3).

**Note:** Batch re-sync 2026-10-04 (Group28 row; Rule 0023 legacy checklist — reader/writer columns but no per-row release column, stale `# Spec verified: R23-11` marker removed at session start, stamp WITHHELD pending the 9b batch confirmation, user instruction; checklist rewritten in the 6-column `# (no methods)` form with the R23-11 release suffix and the full Aggregated-by consumer list — RuleBasedAxisCont.category, SwAxisCont.category (read/written via the RuleBasedAxisCont reader/writer pair), SwCalprmAxis.category). Rule 0011 value repair: the committed enum carried the UPPERCASE XSD wire forms as member values (`COM_AXIS = "COM_AXIS"`, `FIX_AXIS = "FIX_AXIS"`, `RES_AXIS = "RES_AXIS"`, `STD_AXIS = "STD_AXIS"`) — the Rule 0011 placeholder shape (right count, wrong values); re-synced to the camelCase mmt.qualifiedName literals (`COM_AXIS = "comAxis"`, `FIX_AXIS = "fixAXIS"`, `RES_AXIS = "resAxis"`, `STD_AXIS = "stdAxis"`; note the spec literal `fixAXIS` keeps its internal capital A verbatim). Class docstring + per-literal comments verified character-for-character against the markdown (wipe-and-rewrite produced identical text — already verbatim, Tags tails kept per Rule 0011).

**CALPRM-AXIS-CATEGORY XML-token decision (supersedes the SwCalprmAxis pass note):** the SwCalprmAxis batch recorded "its wire forms equal the member values so no token map applies" — that check was wrong: the committed member values WERE the wire forms. The XSD (`AUTOSAR_00052.xsd` L132080 `CALPRM-AXIS-CATEGORY-ENUM--SIMPLE`) serializes the UPPERCASE underscore tokens (`COM_AXIS`/`FIX_AXIS`/`RES_AXIS`/`STD_AXIS`) while the spec member values are camelCase, so the canonical `_readEnumToken`/`_writeEnumToken` + `CALPRM_AXIS_CATEGORY_XML_MAP` convention (SwCalibrationAccessEnum/ByteOrderEnum precedent; map defined in both `arxml_parser.py` and `arxml_writer.py` next to `SW_CALIBRATION_ACCESS_XML_MAP`) was applied to all consumer site pairs — parser `getSwCalprmAxis` + `getRuleBasedAxisCont` (replacing the generic-literal + `cast` pattern), writer `setSwCalprmAxis` + `writeRuleBasedAxisCont`. Before this pass the writer emitted the XSD-invalid camelCase form whenever the enum was set via its API, and the reader stored the raw token behind an inaccurate `cast`; after it the token→member→token round-trip is lossless and the model holds real `CalprmAxisCategoryEnum` instances. Accepted consequence (same as ByteOrderEnum): reader input in the non-XSD camelCase form now warns via `notImplemented` and stores None; every XSD-valid non-removed form is covered by the map. Consumer tests aligned (parser tests feed the UPPERCASE token and assert the mapped camelCase member; writer tests assert the UPPERCASE token emission; round-trip tests assert the member value after reload). No integration fixture carries SW-CALPRM-AXIS or RULE-BASED-AXIS-CONT. No Rule 0001.10 missing referenced classes.

## `SwAxisType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 356  | **table:** Table 5.52
- **Package:** `M2::MSR::DataDictionary::Axis`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/Axis.py`

No deviations — both `Attribute` rows modeled 1:1 in displayed order (`swGenericAxisDesc` DocumentationBlock 0..1, `swGenericAxisParamType` SwGenericAxisParamType `*` aggr → `swGenericAxisParamTypes` dedicated typed list + create/get pair; the child is Referrable (Identifiable), so the createXxx shape applies per Rule 0001.6). Base ARElement (spec Base chain `ARElement, ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable`); XSD complexType `SW-AXIS-TYPE` (`AUTOSAR_00052.xsd` L114650) refs the AR-ELEMENT groups then group `SW-AXIS-TYPE` (L114621: SW-GENERIC-AXIS-DESC sequenceOffset 20, SW-GENERIC-AXIS-PARAM-TYPES role wrapper sequenceOffset 30) — no VARIATION-POINT in the group, not VP-capable.

**Note:** Batch sync 2026-10-04 (Group28 row; class was a Created 5-line stub in ARPackage.py — moved to `M2/MSR/DataDictionary/Axis.py` per Rule 0007, the spec Package row is `M2::MSR::DataDictionary::Axis` and the module hint's ARPackage placement was the nearest-modeled-ancestor fallback; stub battery row in `tests/test_armodel/models/test_group21_36_stub_classes.py` re-pointed). Placement rides the SwAxisGeneric/SwAxisGrouped/SwAxisIndividual axis-family module. Reader/writer wiring is new: parser `readARPackageElementsRest` gained the `SW-AXIS-TYPE` dispatch → new `readSwAxisType` (reuses `getDocumentationBlock` and the existing `readIdentifiable` + DATA-CONSTR-REF leaf pair for the param types, registering each child via the model's `createSwGenericAxisParamType`); writer `writeARPackageElementRest` gained the `SwAxisType` dispatch → new `writeSwAxisType` (writeIdentifiable + `writeDocumentationBlock` + the existing `setSwGenericAxisParamType` child helper; wrapper emitted only when non-empty, XSD group order). No integration fixture carries SW-AXIS-TYPE. No Rule 0001.10 missing referenced classes (SwGenericAxisParamType Table 5.54 exists in-module, stamped; DocumentationBlock stamped).
