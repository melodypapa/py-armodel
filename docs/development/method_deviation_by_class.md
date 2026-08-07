# Method/Attribute Deviations by Class

Each class implemented in py-armodel whose OWN spec attributes (R23-11 XSD,
mirroring the PDF attribute tables) deviate from the Python implementation.
The PDF reference `Kind` suffix (`Ref`/`TRef`/`IRef`/`Refs`) is appended to
the member name and is recognised in matching, so e.g. a spec attr `type` of
kind `TRef` is correctly implemented by `typeTRef`. `variationPoint`/
`shortLabel` are excluded as framework-level.

- Classes with deviations: **292**
- Missing accessors: **665**
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
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces/BswEntryRelationship.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bswEntryRelationshipType` | `BswEntryRelationshipEnum` | — | missing |
| — *(missing)* | `—` | `fromRef` | `Ref (BswModuleEntry)` | Ref | missing |
| — *(missing)* | `—` | `toRef` | `Ref (BswModuleEntry)` | Ref | missing |

## `BswEntryRelationshipSet`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 51
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces/BswEntryRelationshipSet.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bswEntryRelationship` | `BswEntryRelationship` | — | missing |

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

## `BswModeSwitchedAckEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 95
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modeGroupRef` | `Optional[RefType]` | `modeGroup` | `Ref (ModeDeclarationGroupPrototype)` | Ref | ok |

## `BswAsynchronousServerCallReturnsEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 98
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `eventSourceRef` | `Optional[RefType]` | `eventSource` | `Ref (BswAsynchronousServerCallResultPoint)` | Ref | ok |

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
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 143
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `memClassSymbol` | `CIdentifier` | — | — | attr | present in XSD (`MEM-CLASS-SYMBOL`), absent from the PDF Table 8.2 attribute rendering; kept with parser/writer coverage |

## `SectionNamePrefix`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 147
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py`

No deviations.

## `StackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 149
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

No deviations (abstract base; tested through concrete subclasses).

## `WorstCaseStackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 150
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

No deviations.

## `MeasuredStackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 150
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

No deviations.

## `RoughEstimateStackUsage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 151
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py`

No deviations.

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
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HardwareConfiguration.py`

No deviations.

## `SoftwareContext`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 163
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/SoftwareContext.py`

No deviations.

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

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `activateAtStart` | `Boolean` | — | missing |
| — *(missing)* | `—` | `checkpoints` | `SupervisedEntityCheckpointNeedsRefConditional` | — | missing |
| — *(missing)* | `—` | `enableDeactivation` | `Boolean` | — | missing |
| — *(missing)* | `—` | `expectedAliveCycle` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `maxAliveCycle` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `minAliveCycle` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `toleratedFailedCycles` | `PositiveInteger` | — | missing |

## `ComMgrUserNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 235
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maxCommMode` | `MaxCommModeEnum` | — | missing |

## `DiagnosticIoControlNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 248
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `currentValueRef` | `Ref (DiagnosticValueNeeds)` | Ref | missing |
| — *(missing)* | `—` | `didNumber` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `freezeCurrentStateSupported` | `Boolean` | — | missing |
| — *(missing)* | `—` | `resetToDefaultSupported` | `Boolean` | — | missing |
| — *(missing)* | `—` | `shortTermAdjustmentSupported` | `Boolean` | — | missing |

## `DiagnosticEventNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 258
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `considerPtoStatus` | `Boolean` | — | missing |
| `inhibitingSecondaryFidRef` | `—` | `inhibitingSecondaryFidRefs` | `Ref (FunctionInhibitionNeeds)` | Refs | type (spec many vs py single) |
| — *(missing)* | `—` | `obdDtcNumber` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `reportBehavior` | `ReportBehaviorEnum` | — | missing |

## `ErrorTracerNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 263
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `tracedFailure` | `DevelopmentError` | — | missing |

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
| — *(missing)* | `—` | `swAxisCont` | `RuleBasedAxisCont` | — | missing |
| — *(missing)* | `—` | `swValueCont` | `RuleBasedValueCont` | — | missing |

## `ArgumentDataPrototype`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 303
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `typeBlueprint` | `AutosarDataTypeRefConditional` | — | missing |

## `AtomicSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 304
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `internalBehavior` | `—` | `internalBehavior` | `SwcInternalBehavior` | — | type (spec many vs py single) |

## `AtpBlueprint`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 305
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure/AtpBlueprint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blueprintPolicy` | `BlueprintPolicyList` | — | missing |
| — *(missing)* | `—` | `shortNamePattern` | `String` | — | missing |

## `ClientServerInterface`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 308
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `possibleError` | `ApplicationError` | — | missing |

## `ClientServerOperation`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 309
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `diagArgIntegrity` | `Boolean` | — | missing |
| — *(missing)* | `—` | `fireAndForget` | `Boolean` | — | missing |
| — *(missing)* | `—` | `possibleApErrorRefs` | `Ref (ApApplicationError)` | Refs | missing |
| — *(missing)* | `—` | `possibleApErrorSetRefs` | `Ref (ApApplicationErrorSet)` | Refs | missing |

## `ExecutableEntityActivationReason`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 315
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bitPosition` | `PositiveInteger` | — | missing |

## `FunctionInhibitionAvailabilityNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 318
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `controlledFidRef` | `Ref (FunctionInhibitionNeeds)` | Ref | missing |

## `ImplementationDataType`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 320
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `symbolProps` | `—` | `symbolProps` | `SymbolProps` | — | type (spec one vs py list) |

## `NumericalOrText`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 323
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `vf` | `NumericalValueVariationPoint` | — | missing |
| — *(missing)* | `—` | `vt` | `String` | — | missing |

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

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `shortName` | `Identifier` | — | missing |
| — *(missing)* | `—` | `shortNameFragment` | `ShortNameFragment` | — | missing |

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
| — *(missing)* | `—` | `v` | `NumericalValue` | — | missing |
| — *(missing)* | `—` | `vf` | `NumericalValueVariationPoint` | — | missing |
| — *(missing)* | `—` | `vt` | `VerbatimString` | — | missing |
| — *(missing)* | `—` | `vtf` | `NumericalOrText` | — | missing |

## `RuleBasedValueCont`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 330
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ruleBasedValues` | `RuleBasedValueSpecification` | — | missing |
| — *(missing)* | `—` | `swArraysize` | `ValueList` | — | missing |
| — *(missing)* | `—` | `unitRef` | `Ref (Unit)` | Ref | missing |

## `RuleBasedValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 331
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `arguments` | `RuleArguments` | — | missing |
| — *(missing)* | `—` | `maxSizeToFill` | `Integer` | — | missing |

## `RunnableEntity`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 331
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `waitPoints` | `Dict[str, WaitPoint]` | `waitPoint` | `WaitPoint` | — | type (spec many vs py single) |

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
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 339
- **Package:** `M2::MSR::DataDictionary::DataDefProperties`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `swDataDefPropsVariant` | `SwDataDefPropsConditional` | — | missing |

## `SwTextProps`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 343
- **Package:** `M2::MSR::DataDictionary::DataDefProperties`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `arraySizeSemantics` | `ArraySizeSemanticsEnum` | — | missing |
| — *(missing)* | `—` | `baseTypeRef` | `Ref (SwBaseType)` | Ref | missing |
| — *(missing)* | `—` | `swFillCharacter` | `Integer` | — | missing |
| — *(missing)* | `—` | `swMaxTextSize` | `IntegerValueVariationPoint` | — | missing |

## `DocumentationBlock`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 52
- **Package:** `M2::MSR::Documentation::BlockElements`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/BlockElements/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `defList` | `DefList` | `defList` | `DefList` | — | type (spec many vs py single) |
| `formula` | `—` | `formula` | `MlFormula` | — | type (spec many vs py single) |
| `labeledList` | `LabeledList` | `labeledList` | `LabeledList` | — | type (spec many vs py single) |
| `note` | `Note` | `note` | `Note` | — | type (spec many vs py single) |
| `structuredReq` | `StructuredReq` | `structuredReq` | `StructuredReq` | — | type (spec many vs py single) |
| `trace` | `TraceableText` | `trace` | `TraceableText` | — | type (spec many vs py single) |
| `verbatim` | `MultiLanguageVerbatim` | `verbatim` | `MultiLanguageVerbatim` | — | type (spec many vs py single) |

## `LLongName`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 179
- **Package:** `M2::MSR::Documentation::TextModel::LanguageDataModel`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blueprintValue` | `?` | — | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 302
- **Package:** `M2::MSR::AsamHdo::BaseTypes`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maxBaseTypeSize` | `PositiveInteger` | — | missing |

## `CompositionSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 307
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `physicalDimensionMappingRef` | `Ref (PhysicalDimensionMappingSet)` | Ref | missing |

## `EcuInstance`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 312
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `canTpAddressRefs` | `Ref (CanTpAddress)` | Refs | missing |
| — *(missing)* | `—` | `diagnosticProps` | `DiagnosticEcuProps` | — | missing |
| — *(missing)* | `—` | `ecuInstanceProps` | `Ref (OsTaskProxy)` | — | missing |
| `firewallRuleRef` | `—` | `firewallRuleRefs` | `Ref (StateDependentFirewall)` | Refs | type (spec many vs py single) |
| — *(missing)* | `—` | `tpAddressRefs` | `Ref (TpAddress)` | Refs | missing |

## `ISignal`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 315
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `dataTransformationRef` | `—` | `dataTransformation` | `DataTransformationRefConditional` | — | type (spec many vs py single) |
| `transformationISignalProps` | `—` | `iSignalProps` | `ISignalProps` | — | type (spec one vs py list) |

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
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 330
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `consistencyNeeds` | `ConsistencyNeeds` | — | missing |
| — *(missing)* | `—` | `swComponentDocumentation` | `SwComponentDocumentation` | — | missing |
| — *(missing)* | `—` | `swcMappingConstraintRefs` | `Ref (SwComponentMappingConstraints)` | Refs | missing |
| — *(missing)* | `—` | `unitGroupRefs` | `Ref (UnitGroup)` | Refs | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 65
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecucLinkerSymbolDefVariant` | `EcucLinkerSymbolDefConditional` | — | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 304
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `compuMethodRef` | `Ref (CompuMethod)` | Ref | missing |

## `PostBuildVariantCriterionValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 305
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `annotation` | `Annotation` | — | missing |
| — *(missing)* | `—` | `variantCriterionRef` | `Ref (PostBuildVariantCriterion)` | Ref | missing |

## `VariationPoint`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 315
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `formalBlueprintGenerator` | `BlueprintGenerator` | — | missing |

## `VerbatimString`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 316
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blueprintValue` | `?` | — | missing |
| — *(missing)* | `—` | `xmlSpace` | `?` | — | missing |

## `HwAttributeValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 16
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwAttributeValue.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `annotation` | `Annotation` | — | missing |
| — *(missing)* | `—` | `v` | `NumericalValueVariationPoint` | — | missing |
| — *(missing)* | `—` | `vt` | `VerbatimString` | — | missing |

## `HwPin`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 20
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `functionName` | `—` | `functionName` | `String` | — | type (spec many vs py single) |

## `HwPinGroupContent`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 20
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwPinGroup` | `—` | `hwPinGroup` | `HwPinGroup` | — | type (spec many vs py single) |

## `HwElementConnector`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 21
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementConnector.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `hwElementRef` | `—` | `hwElementRefs` | `Ref (HwElement)` | Refs | type (spec many vs py single) |
| — *(missing)* | `—` | `hwPinConnection` | `HwPinConnector` | — | missing |
| — *(missing)* | `—` | `hwPinGroupConnection` | `HwPinGroupConnector` | — | missing |

## `PassThroughSwConnector`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 83
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `serviceInterfaceElementMappingRefs` | `Ref (ServiceInterfaceElementMapping)` | Refs | missing |

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
| `textTableMappings` | `—` | `textTableMapping` | `TextTableMapping` | — | type (spec one vs py list) |

## `ModeDeclarationMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `secondModeRef` | `—` | `secondModeRef` | `Ref (ModeDeclaration)` | Ref | type (spec one vs py list) |

## `ReceiverComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 170
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataUpdatePeriod` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `externalReplacementRef` | `Ref (AutosarDataPrototype)` | Ref | missing |
| `compositeNetworkRepresentation` | `—` | `networkRepresentation` | `SwDataDefProps` | — | type (spec one vs py list) |
| — *(missing)* | `—` | `receiverIntent` | `ReceiverIntentEnum` | — | missing |
| — *(missing)* | `—` | `receptionProps` | `ReceptionComSpecProps` | — | missing |
| — *(missing)* | `—` | `replaceWith` | `VariableAccess` | — | missing |
| — *(missing)* | `—` | `syncCounterInit` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `transformationComSpecProps` | `EndToEndTransformationComSpecProps` | — | missing |

## `NonqueuedReceiverComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 172
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `enableUpdated` | `—` | `enableUpdate` | `Boolean` | — | naming |
| `timeoutSubstitution` | `—` | `timeoutSubstitutionValue` | `ApplicationAssocMapValueSpecification` | — | naming |

## `SenderComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 178
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataUpdatePeriod` | `TimeValue` | — | missing |
| `compositeNetworkRepresentations` | `—` | `networkRepresentation` | `SwDataDefProps` | — | type (spec one vs py list) |
| — *(missing)* | `—` | `senderIntent` | `SenderIntentEnum` | — | missing |
| — *(missing)* | `—` | `transmissionProps` | `TransmissionComSpecProps` | — | missing |

## `NonqueuedSenderComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 179
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataFilter` | `DataFilter` | — | missing |

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

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `transformationDescription` | `—` | `transformationDescription` | `EndToEndTransformationDescription` | — | type (spec many vs py single) |

## `EndToEndTransformationComSpecProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 200
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `windowSizeInit` | `—` | `windowSize` | `PositiveInteger` | — | naming |

## `ApplicationArrayDataType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 252
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `applicationArrayElement` | `—` | `element` | `ApplicationArrayElement` | — | type (spec one vs py list) |

## `ParameterInAtomicSWCTypeInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 319
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstanceRefsUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `contextDataPrototypeRef` | `—` | `contextDataPrototypeRef` | `Ref (ApplicationCompositeElementDataPrototype)` | Ref | type (spec many vs py single) |

## `SwCalprmAxis`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 352
- **Package:** `M2::MSR::DataDictionary::CalibrationParameter`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `baseTypeRef` | `Ref (SwBaseType)` | Ref | missing |
| — *(missing)* | `—` | `swAxisIndex` | `AxisIndexType` | — | missing |

## `SwAxisGeneric`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 355
- **Package:** `M2::MSR::DataDictionary::Axis`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/Axis.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `swNumberOfAxisPoints` | `IntegerValueVariationPoint` | — | missing |

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
| — *(missing)* | `—` | `vf` | `NumericalValueVariationPoint` | — | missing |
| — *(missing)* | `—` | `vg` | `ValueGroup` | — | missing |
| — *(missing)* | `—` | `vtf` | `NumericalOrText` | — | missing |

## `RuleBasedAxisCont`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 464
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `category` | `CalprmAxisCategoryEnum` | — | missing |
| — *(missing)* | `—` | `ruleBasedValues` | `RuleBasedValueSpecification` | — | missing |
| — *(missing)* | `—` | `swArraysize` | `ValueList` | — | missing |
| — *(missing)* | `—` | `swAxisIndex` | `AxisIndexType` | — | missing |
| — *(missing)* | `—` | `unitRef` | `Ref (Unit)` | Ref | missing |

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
| — *(missing)* | `—` | `operationCycle` | `OperationCycleTypeEnum` | — | missing |
| — *(missing)* | `—` | `operationCycleAutomaticEnd` | `Boolean` | — | missing |
| — *(missing)* | `—` | `operationCycleAutostart` | `Boolean` | — | missing |

## `DiagnosticEnableConditionNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 762
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `initialStatus` | `EventAcceptanceStatusEnum` | — | missing |

## `DiagnosticStorageConditionNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 762
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `initialStatus` | `StorageConditionStatusEnum` | — | missing |

## `IndicatorStatusNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 766
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `type` | `DiagnosticIndicatorTypeEnum` | — | missing |

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

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `contextDataPrototypeRef` | `—` | `contextDataPrototypeRef` | `Ref (ApplicationCompositeElementDataPrototype)` | Ref | type (spec many vs py single) |

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
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 981
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DataMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `communicationDirection` | `CommunicationDirectionType` | — | missing |
| — *(missing)* | `—` | `eventGroupRefs` | `Ref (ConsumedEventGroup)` | Refs | missing |
| — *(missing)* | `—` | `eventHandlerRefs` | `Ref (EventHandler)` | Refs | missing |
| — *(missing)* | `—` | `serviceInstanceRefs` | `Ref (AbstractServiceInstance)` | Refs | missing |

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

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `transformationISignalProps` | `—` | `transformationISignalProps` | `EndToEndTransformationISignalProps` | — | type (spec many vs py single) |

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
| — *(missing)* | `—` | `possibleErrorReaction` | `PossibleErrorReaction` | — | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 84
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `flexrayCommunicationControllerVariant` | `FlexrayCommunicationControllerConditional` | — | missing |

## `LinCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 93
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `linClusterVariant` | `LinClusterConditional` | — | missing |

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

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `partitionRef` | `Ref (EcuPartition)` | Ref | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 355
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `containedPduTriggeringRef` | `Ref (PduTriggering)` | Ref | missing |
| — *(missing)* | `—` | `priority` | `PositiveInteger` | — | missing |

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
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/Timing.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modeDeclarationRef` | `—` | `modeDeclarationRefs` | `Ref (ModeDeclaration)` | Refs | type (spec many vs py single) |

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
| — *(missing)* | `—` | `dataLinkLayerRule` | `DataLinkLayerRule` | — | missing |
| — *(missing)* | `—` | `ddsRule` | `DdsRule` | — | missing |
| — *(missing)* | `—` | `doIpRule` | `DoIpRule` | — | missing |
| — *(missing)* | `—` | `networkLayerRule` | `Ipv4Rule` | — | missing |
| — *(missing)* | `—` | `payloadBytePatternRule` | `PayloadBytePatternRule` | — | missing |
| — *(missing)* | `—` | `refillAmount` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `someipRule` | `SomeipProtocolRule` | — | missing |
| — *(missing)* | `—` | `someipSdRule` | `SomeipSdRule` | — | missing |
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
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 615
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::TransportProtocols`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dropNotRequestedNad` | `Boolean` | — | missing |
| — *(missing)* | `—` | `maxNumberOfRespPendingFrames` | `PositiveInteger` | — | missing |
| — *(missing)* | `—` | `p2Max` | `TimeValue` | — | missing |
| — *(missing)* | `—` | `p2Timing` | `TimeValue` | — | missing |

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
| — *(missing)* | `—` | `busSpecificNmEcu` | `Ref (EcuInstance)` | — | missing |
| — *(missing)* | `—` | `nmMultipleChannelsEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmPassiveModeEnabled` | `Boolean` | — | missing |

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
| — *(missing)* | `—` | `nmControlBitVectorEnabled` | `Boolean` | — | missing |
| — *(missing)* | `—` | `nmDataDisabled` | `Boolean` | — | missing |

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
| — *(missing)* | `—` | `nmCarWakeUpFilterEnabled` | `Boolean` | — | missing |

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
| — *(missing)* | `—` | `canXlNmProps` | `CanXlNmNodeProps` | — | missing |

## `UdpNmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 687
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `networkConfiguration` | `UdpNmNetworkConfiguration` | — | missing |
| — *(missing)* | `—` | `nmUserDataLength` | `Integer` | — | missing |
| — *(missing)* | `—` | `nmUserDataOffset` | `PositiveInteger` | — | missing |

## `UdpNmClusterCoupling`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 688
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmBusLoadReductionEnabled` | `Boolean` | — | missing |

## `UdpNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 688
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmRepeatMsgIndicationEnabled` | `Boolean` | — | missing |

## `UdpNmNode`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 688
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `communicationConnectorRef` | `Ref (EthernetCommunicationConnector)` | Ref | missing |
| — *(missing)* | `—` | `nmPnHandleMultipleNetworkRequests` | `Boolean` | — | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 808
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `endToEndTransformationISignalPropsVariant` | `EndToEndTransformationISignalPropsConditional` | — | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 2057
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ObsoleteModel`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `autosarConnector` | `SoAdConnectorType` | — | missing |
| — *(missing)* | `—` | `doIpSourceAddressRef` | `Ref (LogicAddress)` | Ref | missing |
| — *(missing)* | `—` | `doIpTargetAddressRef` | `Ref (LogicAddress)` | Ref | missing |
| — *(missing)* | `—` | `ident` | `TpConnectionIdent` | — | missing |
| — *(missing)* | `—` | `localPortRef` | `Ref (SocketAddress)` | Ref | missing |
| — *(missing)* | `—` | `nPduRef` | `Ref (NPdu)` | Ref | missing |
| — *(missing)* | `—` | `remotePortRef` | `Ref (SocketAddress)` | Ref | missing |
| — *(missing)* | `—` | `socketProtocol` | `SoAdProtocolType` | — | missing |

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
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 38
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInSwcInstanceRef.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextComponentRef` | `Ref (SwComponentPrototype)` | Ref | missing |
| — *(missing)* | `—` | `contextModeDeclarationGroupPrototypeRef` | `Ref (ModeDeclarationGroupPrototype)` | Ref | missing |
| — *(missing)* | `—` | `contextPortRef` | `Ref (PortPrototype)` | Ref | missing |
| — *(missing)* | `—` | `targetModeDeclarationRef` | `Ref (ModeDeclaration)` | Ref | missing |

## `SynchronizationTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 92
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `eventOccurrenceKind` | `EventOccurrenceKindEnum` | — | missing |
| — *(missing)* | `—` | `scopeEventRefs` | `Ref (TimingDescriptionEvent)` | Refs | missing |
| — *(missing)* | `—` | `scopeRefs` | `Ref (TimingDescriptionEventChain)` | Refs | missing |
| — *(missing)* | `—` | `synchronizationConstraintType` | `SynchronizationTypeEnum` | — | missing |
| — *(missing)* | `—` | `tolerance` | `MultidimensionalTime` | — | missing |

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

## `OffsetTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 114
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::OffsetConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/OffsetConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maximum` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `minimum` | `MultidimensionalTime` | — | missing |
| — *(missing)* | `—` | `sourceRef` | `Ref (TimingDescriptionEvent)` | Ref | missing |
| — *(missing)* | `—` | `targetRef` | `Ref (TimingDescriptionEvent)` | Ref | missing |

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
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintMapping/BlueprintMappingSet.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blueprintMap` | `BlueprintMapping` | — | missing |

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
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 424
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintGenerator`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator/BlueprintGenerator.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `expression` | `VerbatimString` | — | missing |
| — *(missing)* | `—` | `introduction` | `DocumentationBlock` | — | missing |

## `CryptoKeySlot`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 57
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::CryptoDeployment`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/CryptoKeySlot.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `allocateShadowCopy` | `Boolean` | — | missing |
| — *(missing)* | `—` | `cryptoObjectType` | `CryptoObjectTypeEnum` | — | missing |
| — *(missing)* | `—` | `keySlotAllowedModification` | `CryptoKeySlotAllowedModification` | — | missing |
| — *(missing)* | `—` | `keySlotContentAllowedUsage` | `CryptoKeySlotContentAllowedUsage` | — | missing |

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
