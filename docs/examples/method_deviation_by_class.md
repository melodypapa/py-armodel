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

**Note:** Synced 2026-09-26 against R23-11 FO GST Table E.2 (p.421, page located via direct pypdf scan — the caption index does not cover letter-table ids; the R4.3.1 GST Table E.1 reproduction is row-identical; CP SWCT — the queue row's original TBC hint — has no own class table, only Subclasses mentions). New class: the 2026-09-24 AVP audit recorded it as unmodeled — superseded by this sync. No open deviations: exactly the two Table E.2 attribute rows implemented (`base` `Optional[Identifier]`, `enumTable` `Optional[RefType]` — spec Ref; XSD REF--SIMPLE L96364 is a plain string pattern so the XML attribute carries the value only, no DEST), both 0..1 attr, xml.attribute=true; abstract class per the table header; class docstring = the Table E.2 Note verbatim (Note-only form); 6-column checklist written at creation. `Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula` anchored on its most-derived member `AttributeValueVariationPoint` (the stamped-sibling form; the XSD 00052 complexTypes composing the AEVP group — e.g. DIAGNOSTIC-DEBOUNCE-BEHAVIOR-ENUM-VALUE-VARIATION-POINT L34752 — compose AR-OBJECT + FORMULA-EXPRESSION + SSCDF + AVP + AEVP groups and attributeGroups). Reader/writer via the new own-group helper pair `readAbstractEnumerationValueVariationPoint`/`writeAbstractEnumerationValueVariationPoint` (the BASE/ENUM-TABLE XML attributes; the XSD element group L274 is an empty sequence); no `VALUE_ACCESS_TAG_TO_CLASS`/`VALUE_ACCESS_CLASS_TO_TAG` dispatch entry — the auto-generated `{Type}ValueVariationPoint` concrete subclasses (TPS_GST_00206/00373; their 4 XSD complexTypes live in DiagnosticExtract/SystemTemplate domains) are not modeled in src, so no wire tag can map to the abstract class; the helpers are exercised by direct element-level round-trip tests (the `TestRead/WriteSwSystemconstDependentFormula` own-group-helper precedent) and are ready for the future concrete-subclass syncs. Stamp deferred to batch confirmation.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Both Table E.2 attributes implemented: `base` (`Optional[Identifier]`, 0..1, attr, xml.attribute=true), `enumTable` (`Optional[RefType]`, 0..1, attr, xml.attribute=true); abstract class per the table header; docstrings verbatim from the table Notes; reader/writer via the own-group attribute helpers. Stamp deferred to batch confirmation. |

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

No deviations — Table 3.8 attributes (`internalBehavior`, `symbolProps`) are implemented
with parser/writer coverage. The previously recorded `internalBehavior`
`type (spec many vs py single)` row is removed: the PDF table states `0..1` (the XSD `*`
is only the atpVariation flattening), so the single-value model is PDF-correct.

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
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 320
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `symbolProps` | `—` | `symbolProps` | `SymbolProps` | — | type (spec one vs py list) |

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
| — *(no deviation)* | — | — | — | — | Aligned to Table D.72 (R23-11): `arraySizeSemantics`, `baseTypeRef`, `swFillCharacter`, `swMaxTextSize` all present with reader/writer; fabricated `encoding`/`format` fields removed. |

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
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 290
- **Package:** `M2::MSR::AsamHdo::BaseTypes`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maxBaseTypeSize` | `PositiveInteger` | — | deprecated (atp.Status=removed), not implemented |

## `BaseType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 291
- **Package:** `M2::MSR::AsamHdo::BaseTypes`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `baseTypeDefinition` | `BaseTypeDirectDefinition` | `baseTypeDefinition` | `BaseTypeDefinition` | aggr | type (PDF abstract BaseTypeDefinition vs py BaseTypeDirectDefinition; the abstract aggregated type is instantiated as the concrete subtype) |

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
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `consistencyNeeds` | `List[ARObject]` | `consistencyNeeds` | `ConsistencyNeeds` | aggr | Table 4.99 class not yet implemented — ARObject placeholder; reader/writer pending |
| `swcMappingConstraintsRefs` | `List[RefType]` | `swcMappingConstraintRefs` | `Ref (SwComponentMappingConstraints)` | Refs | class not in markdown/PDF — skipped per user; RefType placeholder |
| `unitGroupRefs` | `List[RefType]` | `unitGroupRefs` | `Ref (UnitGroup)` | Refs | `UnitGroup` not yet synced (stub); RefType placeholder |

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

**Note:** Spec verified R23-11. Bare ARLiteral subclass per spec (no own attributes). Spec Table 4.67 defines two XML attributes (blueprintValue with atp.Status=draft, xmlSpace requiring missing XmlSpaceEnum); not implemented due to draft status and missing enum dependency. Stamped.

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | Modeled as bare ARLiteral subclass. Spec attributes blueprintValue (String, 0..1, attr, atp.Status=draft) and xmlSpace (XmlSpaceEnum, 0..1, attr) not implemented (draft status; XmlSpaceEnum missing enum). Per Rule 0001.4 guidance on draft/missing-dependency attributes. |

## `XmlSpaceEnum`
- **PDF:** *no own spec table*  |  **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Enumerations`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Enumerations.py`

XSD-only — synced 2026-09-24 from `AUTOSAR_00052.xsd` line 145398 (`XML-SPACE-ENUM`); both-corpora gate re-verified (no caption line, no header cell in R23-11 CP_TPS/FO_TPS or R4.3.1 markdown — only consumer attribute-type refs). Literals `default` (idx 0) / `preserve` (idx 1), wire tokens = the xml:space values themselves; class docstring + per-literal comments verbatim from XSD documentation. No open deviation rows. Supersedes the earlier "skipped per user / left as-is" note below. Consumer findings (not deviations of this class): writer `writeSds` emits `xml:space` but parser `readSd` does not read it back (Sd reader gap, flagged for Sd sync); `VerbatimString.xmlSpace` still unimplemented (flagged for VerbatimString sync). Stamp (`# XSD verified: AUTOSAR_00052.xsd`) deferred to batch confirmation.

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

## `NonqueuedReceiverComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 173
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | All 8 spec attributes implemented; `handleDataStatus` reader/writer coverage added. |

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
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 84
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `flexrayCommunicationControllerVariant` | `FlexrayCommunicationControllerConditional` | — | missing |

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

## `ConcreteTDEventVfb`
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
| — *(no deviation)* | — | — | — | — | Both Table C.16 attributes implemented spec-named: `ecuc` → `ecucRef` (`Optional[RefType]`, 1, ref — Kind-suffix Rule 1.5 per `sysc`→`syscRef`), `verbatim` (`Optional[MultiLanguageVerbatim]`, 1, aggr); concrete class per the table header and XSD abstract="false"; docstrings verbatim from the table Notes; reader/writer covered by the class's own `readBlueprintFormula`/`writeBlueprintFormula` helper pair, element-level tests (dedicated parser + writer test files). Stamp deferred to batch confirmation. |

**Note:** Synced 2026-09-26 against R23-11 FO StandardizationTemplate Table C.16 (p.163; appendix C caption-shift — the table body renders ABOVE the caption on the same page, per the BlueprintGenerator appendix precedent; pdf_page.py does not index appendix-letter ids, page via direct pypdf scan; R4.3.1 reproduction Table D.12 carries the same rows). XSD 00052 corroboration: group `BLUEPRINT-FORMULA` (L9023) is a choice of ECUC-QUERY-REF (`atp.Status="removed"` — not modeled, the PDF table wins per Rule 1.5/0015) / ECUC-REF (`mmt.RestrictToStandards="CP"`, DEST `ECUC-DEFINITION-ELEMENT--SUBTYPES-ENUM`) / VERBATIM (type `MULTI-LANGUAGE-VERBATIM`); complexType (L9068, abstract="false", `mixed="true"`) composes AR-OBJECT + FORMULA-EXPRESSION (empty sequence — skipped atpDerived associations) + SW-SYSTEMCONST-DEPENDENT-FORMULA + own group, attributeGroup AR-OBJECT only — Base row `ARObject, FormulaExpression, SwSystemconstDependentFormula` confirmed, most-derived provided base `SwSystemconstDependentFormula` (ConditionByFormula precedent). The queue row's "pure-text formula class" Phase-0 assumption (CompuGenericMath shape — zero own content members) was corrected at Step 1: the class has TWO own content members. The sole consuming element `VariationPoint.formalBlueprintCondition` (FORMAL-BLUEPRINT-CONDITION, VARIATION-POINT group L130040) is `atp.Status="removed"` in R23-11, absent from VariationPoint's R23-11 table, and deliberately not read/written by the stamped VariationPoint sync (documented at the readVariationPoint helper) — there is NO live dispatcher to wire into; reader/writer coverage is therefore the class's own helper pair (mixed text + ECUC-REF + VERBATIM + the inherited SYSC refs via the shared SwSystemconstDependentFormula helpers), pinned at element level with dedicated parser/writer test files (PostBuildVariantCriterionValue precedent: own helper pair + element-level tests until a dispatcher is sanctioned; wiring the removed consumer element would violate VariationPoint's own R23-11 table per Rule 0015). Field-to-spec cross-check both directions EXACT (two attributes → two PEP 526 `Optional` fields in displayed row order; no extra fields; no create/add — neither member is a Referrable child; the `verbatim` aggregation round-trips through the shared `getMultiLanguageVerbatim`/`setMultiLanguageVerbatim` pair). Docstrings verbatim from the Table C.16 Notes (class docstring = Note verbatim; setters append the None-no-op sentence). NO open deviations; no `# Spec verified:` stamp — deferred to batch confirmation.

## `FMConditionByFeaturesAndAttributes`
- **PDF:** `AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf`  | **page:** 62 (Table 7.2)
- **Package:** `M2::AUTOSARTemplates::FeatureModelTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/FeatureModelTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(no deviation)* | — | — | — | — | No deviations — Table 7.2 declares NO attribute rows (the `-` row), and the class declares zero own members; the `<<atpMixedString>>` content is the inherited `getMixedString`/`setMixedString` mixin accessors, the reference lists the inherited `FormulaExpression` `atpReferences`/`atpStringReferences`. Stamp deferred to batch confirmation. |

**Note:** Synced 2026-09-26 against R23-11 FO FeatureModelExchangeFormat Table 7.2 (section 7.2.2, p.62 — numeric id indexed by pdf_page.py, p.62 in both R23-11 and R4.3.1; R4.3.1 reproduction Table 7.2 carries the same rows, AUTOSAR_TPS_FeatureModelExchangeFormat.md line 1780). XSD 00052 corroboration: group `FM-CONDITION-BY-FEATURES-AND-ATTRIBUTES` (L62013) is an empty sequence; complexType (L62022, `abstract="false"`, `mixed="true"`) composes AR-OBJECT + FORMULA-EXPRESSION + FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES + own group, attributeGroup AR-OBJECT only — concrete `<<atpMixedString>>` class confirmed (no `(abstract)` marker in the table header, unlike Tables 7.1/7.3). Base row `ARObject, FMFormulaByFeaturesAndAttributes, FormulaExpression`: the most-derived base `FMFormulaByFeaturesAndAttributes` (Table 7.1, abstract, GROUP-ONLY in the XSD — no own complexType) is missing from the model and is a separate Group8 FM* sync row, so the class derives from the nearest available ancestor `FormulaExpression` (stamped R23-11, Table C.5 pp.73-74) — re-base finding (not an open deviation): when the sibling row lands, `FMConditionByFeaturesAndAttributes` may be re-based onto it. Closure check (queue-row note): `FMFeature` and `FMAttributeDef` (the Table 7.1 ref targets) and ALL Aggregated-by consumers `FMFeatureMapCondition` (FM-COND, L62309), `FMFeatureRelation` (RESTRICTION, L62523), `FMFeatureRestriction` (RESTRICTION, L62560) are missing from src — collected and reported, NONE created (Rule 0016 / 0001.10); the table has no ref rows, so no `Optional[RefType]` members are needed. Because no dispatcher exists at all (unlike BlueprintFormula, whose consumer VariationPoint exists but deliberately does not dispatch the removed FORMAL-BLUEPRINT-CONDITION), reader/writer coverage is the class's own helper pair `readFMConditionByFeaturesAndAttributes`/`writeFMConditionByFeaturesAndAttributes` (element key `FM-COND` per `FMFeatureMapCondition.fmCond`, the `RESTRICTION` roles via the key parameter; ARObject attributes + mixed text only — the parent-group members ATTRIBUTE-REF/FEATURE-REF are the Table 7.1 sibling row's business, Rule 0015 the PDF table wins), pinned at element level with dedicated parser/writer test files (BlueprintFormula / PostBuildVariantCriterionValue precedent). Docstrings verbatim from the Table 7.2 Note (class docstring only — zero attribute rows means no member docstrings exist). NO open deviations; no `# Spec verified:` stamp — deferred to batch confirmation.

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
