# Method/Attribute Deviations by Class (v2)

Regenerated from the markdown class attribute tables of all 15 AUTOSAR spec
pairs (`autosar/markdown/*.md`, mirroring the R23-11 PDF attribute tables) against
the Python sources. Classes whose checklist carries `# Spec verified: R<YY>-<MM>`
are considered OK and skipped. The PDF reference `Kind` suffix (`Ref`/`TRef`/`IRef`/
`Refs`) is appended to the member name and recognised in matching. `variationPoint`/
`shortLabel` are excluded as framework-level.

- Py classes scanned: **1030**
- Skipped (spec verified stamp): **295**
- Classes with deviations: **301**
- No spec table found (appendix): **133**
- Missing accessors: **376**
- Naming deviations: **15**
- Type deviations (list/single multiplicity): **37**

## `ExclusiveAreaNestingOrder`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 84 | **table:** Table 5.19
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `exclusiveAreaRefs` | `List[RefType]` | `exclusiveArea(ordered)` | ``ExclusiveArea`` | ref | naming (Refs suffix) |

## `AbstractEvent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 541 | **table:** Table 7.8
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `activationReasonRepresentationRef` | `Optional[RefType]` | `activationReasonRepresentation` | ``ExecutableEntityActivationReason`` | ref | naming (Ref suffix) |

- **Note:** `RTEEvent` now derives from `AbstractEvent` (spec Base includes AbstractEvent); reader/writer coverage for `ACTIVATION-REASON-REPRESENTATION-REF` added for both RTE and BSW event paths (2026-08-20).

## `BswEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 87 | **table:** Table 5.22
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `contextLimitationRefs` | `List[RefType]` | `contextLimitation` | ``BswDistinguishedPartition`` | ref | naming (Refs suffix) |
| `disabledInModeIRefs` | `List[ModeInBswModuleDescriptionInstanceRef]` | `disabledInMode` | ``ModeDeclaration`` | iref | naming (IRefs suffix) |
| `startsOnEventRef` | `Optional[RefType]` | `startsOnEvent` | ``BswModuleEntity`` | ref | naming (Ref suffix) |

## `BswModeSwitchEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 95  | **table:** Table 5.31
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `activation` | `Optional[ModeActivationKind]` | `activation` | ``ModeActivationKind`` | attr | — |
| `modeIRefs` | `List[ModeInBswModuleDescriptionInstanceRef]` | `mode(ordered)` | ``ModeDeclaration`` | iref | naming (IRefs suffix) |

## `BswImplementation`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 120 | **table:** Table 6.1
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswImplementation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `arReleaseVersion` | `RevisionLabelString` | `arReleaseVersion` | ``RevisionLabelString`` | attr | — |
| `behaviorRef` | `RefType` | `behavior` | ``BswInternalBehavior`` | ref | naming (Ref suffix) |
| `preconfiguredConfigurationRefs` | `List[RefType]` | `preconfiguredConfiguration` | ``EcucModuleConfigurationValues`` | ref | naming (Refs suffix) |
| `recommendedConfigurationRefs` | `List[RefType]` | `recommendedConfiguration` | ``EcucModuleConfigurationValues`` | ref | naming (Refs suffix) |
| `vendorApiInfix` | `Identifier` | `vendorApiInfix` | ``Identifier`` | attr | — |
| `vendorSpecificModuleDefRefs` | `List[RefType]` | `vendorSpecificModuleDef` | ``EcucModuleDef`` | ref | naming (Refs suffix) |

## `Implementation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 621  | **table:** Table 8.1
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Implementation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `buildActionManifestRef` | `RefType` | `buildActionManifest` | ``BuildActionManifest`` | ref | naming (Ref suffix) |
| `codeDescriptors` | `List[Code]` | `codeDescriptor` | ``Code`` | aggr | naming (plural) |
| `compilers` | `List[Compiler]` | `compiler` | ``Compiler`` | aggr | naming (plural) |
| `generatedArtifacts` | `List[DependencyOnArtifact]` | `generatedArtifact` | ``DependencyOnArtifact`` | aggr | naming (plural) |
| `hwElementRefs` | `List[RefType]` | `hwElement` | ``HwElement`` | ref | naming (plural + Ref suffix) |
| `linkers` | `List[Linker]` | `linker` | ``Linker`` | aggr | naming (plural) |
| `requiredArtifacts` | `List[DependencyOnArtifact]` | `requiredArtifact` | ``DependencyOnArtifact`` | aggr | naming (plural) |
| `requiredGeneratorTools` | `List[DependencyOnArtifact]` | `requiredGeneratorTool` | ``DependencyOnArtifact`` | aggr | naming (plural) |
| `swcBswMappingRef` | `RefType` | `swcBswMapping` | ``SwcBswMapping`` | ref | naming (Ref suffix) |
| `getCodeDescriptors` | `List[Code]` | `codeDescriptor` | ``Code`` | aggr | getter filters `self.elements` (isinstance Code) instead of returning dedicated `codeDescriptors` field |
| `create*` methods | — | `-` | ``-`` | - | guard `if short_name not in self.elements` compares str against ARObject list (always truthy) — duplicate element created on repeated same-name call |

## `AutosarEngineeringObject`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 132  | **table:** Table 7.5
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/EngineeringObject.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ARPackage`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 300
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `arPackage` | ``ARPackage`` | aggr | missing |
| `element` | `—` | `element` | ``PackageableElement`` | aggr | type (spec many vs py single) |

## `AUTOSAR`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 301
- **Package:** `M2::AUTOSARTemplates::AutosarTopLevelStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `adminData` | ``AdminData`` | aggr | missing |
| — *(missing)* | `—` | `arPackage` | ``ARPackage`` | aggr | missing |
| — *(missing)* | `—` | `fileInfoComment` | ``FileInfoComment`` | aggr | missing |

## `SwcInternalBehavior`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 518
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `arTypedPerInstanceMemory` | ``VariableDataPrototype`` | aggr | missing |

## `SwAddrMethod`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::DataDictionary::AuxillaryObjects`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/AuxillaryObjects.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `memoryAllocationKeywordPolicy` | `ARLiteral` | `memoryAllocationKeywordPolicy` | ``MemoryAllocation KeywordPolicyType`` | attr | type (PDF MemoryAllocation KeywordPolicyType vs py ARLiteral) |

## `SwServiceArg`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::DataDictionary::ServiceProcessTask`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/ServiceProcessTask.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `swArraysize` | `ValueList` | `swArraysize` | ``ValueList`` | aggr | type (spec one vs py list) |

## `EcucModuleConfigurationValues`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 111 | **table:** Table 2.47
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `containers` | `List[EcucContainerValue]` | `container` | ``EcucContainerValue`` | aggr | naming |
| `definitionRef` | `RefType` | `definition` | ``EcucModuleDef`` | ref | type (PDF EcucModuleDef vs py RefType) |
| `ecucDefEdition` | `ARLiteral` | `ecucDefEdition` | ``RevisionLabelString`` | attr | type (PDF RevisionLabelString vs py ARLiteral) |
| `implementationConfigVariant` | `ARLiteral` | `implementationConfigVariant` | ``EcucConfiguration VariantEnum`` | attr | type (PDF EcucConfiguration VariantEnum vs py ARLiteral) |
| `moduleDescriptionRef` | `RefType` | `moduleDescription` | ``BswImplementation`` | ref | type (PDF BswImplementation vs py RefType) |
| `postBuildVariantUsed` | `ARBoolean` | `postBuildVariantUsed` | ``Boolean`` | attr | type (PDF Boolean vs py ARBoolean) |

- **Note:** reader/writer coverage for `ECUC-DEF-EDITION` and `POST-BUILD-VARIANT-USED` added (2026-08-20); all six XML elements now round-trip.

## `EcucModuleDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** 32 | **table:** Table 2.2
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `apiServicePrefix` | `CIdentifier` | `apiServicePrefix` | ``CIdentifier`` | attr | — |
| `containers` | `List[EcucContainerDef]` | `container` | ``EcucContainerDef`` | aggr | naming |
| `postBuildVariantSupport` | `Boolean` | `postBuildVariantSupport` | ``Boolean`` | attr | — |
| `refinedModuleDefRef` | `RefType` | `refinedModuleDef` | ``EcucModuleDef`` | ref | naming (Ref suffix) |
| `supportedConfigVariants` | `List[EcucConfigurationVariantEnum]` | `supportedConfigVariant` | ``EcucConfiguration VariantEnum`` | attr | naming |

## `System`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `fibexelementrefs` | `—` | `fibexElement` | ``FibexElement`` | ref | type (spec many vs py single) |
| — *(missing)* | `—` | `j1939SharedAddressCluster` | ``J1939SharedAddress Cluster`` | aggr | missing |
| — *(missing)* | `—` | `mapping` | ``SystemMapping`` | aggr | missing |

## `SenderReceiverInterface`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `dataelement` | `—` | `dataElement` | ``VariableDataPrototype`` | aggr | type (spec many vs py single) |

## `ApplicationDataType`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `PRPortPrototype`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `providedRequiredInterface` | `TRefType` | `providedRequiredInterface` | ``PortInterface`` | tref | type (PDF PortInterface vs py TRefType) |

## `ServiceSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AsynchronousServerCallResultPoint`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `asynchronousServerCallPointRef` | `RefType` | `asynchronousServerCallPoint` | ``AsynchronousServer CallPoint`` | ref | type (PDF AsynchronousServer CallPoint vs py RefType) |

## `ARElement`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswInterruptEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInterruptEvent`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswInterruptEvent.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswSchedulerNamePrefix`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 5.21
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswSchedulerNamePrefix`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswSchedulerNamePrefix.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswAsynchronousServerCallResultPoint`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `asynchronousServerCallPoint` | ``BswAsynchronous ServerCallPoint`` | ref | missing |

## `BswDistinguishedPartition`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswCalledEntity`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswSchedulableEntity`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswScheduleEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 88 | **table:** Table 5.23
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | *(no attributes — Table 5.23 is empty)* | — | — | — |

## `BswBackgroundEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 5.27
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswOsTaskExecutionEvent`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswInternalBehavior`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** 68  | **table:** Table 5.2
- **Package:** `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/__init__.py`
- **Deferred:** full sync (member policy classes missing; reader/writer partial)

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `arTypedPerInstanceMemories` | `List[VariableDataPrototype]` | `arTypedPerInstanceMemory` | ``VariableDataPrototype`` | aggr | naming (plural) |
| `bswPerInstanceMemoryPolicies` | `List` | `bswPerInstanceMemoryPolicy` | ``BswPerInstanceMemoryPolicy`` | aggr | member class `BswPerInstanceMemoryPolicy` missing |
| `clientPolicies` | `List` | `clientPolicy` | ``BswClientPolicy`` | aggr | member class `BswClientPolicy` missing |
| `distinguishedPartitions` | `List[BswDistinguishedPartition]` | `distinguishedPartition` | ``BswDistinguishedPartition`` | aggr | naming (plural) |
| `entities` | `List` | `entity` | ``BswModuleEntity`` | aggr | naming (plural); untyped |
| `events` | `List` | `event` | ``BswEvent`` | aggr | naming (plural); untyped |
| `exclusiveAreaPolicies` | `List` | `exclusiveAreaPolicy` | ``BswExclusiveAreaPolicy`` | aggr | naming (plural); untyped |
| `includedDataTypeSets` | `List[IncludedDataTypeSet]` | `includedDataTypeSet` | ``IncludedDataTypeSet`` | aggr | naming (plural) |
| `includedModeDeclarationGroupSets` | `List[IncludedModeDeclarationGroupSet]` | `includedModeDeclarationGroupSet` | ``IncludedModeDeclarationGroupSet`` | aggr | naming (plural) |
| `internalTriggeringPointPolicies` | `List` | `internalTriggeringPointPolicy` | ``BswInternalTriggeringPointPolicy`` | aggr | member class `BswInternalTriggeringPointPolicy` missing |
| `modeReceiverPolicies` | `List` | `modeReceiverPolicy` | ``BswModeReceiverPolicy`` | aggr | naming (plural); untyped |
| `modeSenderPolicies` | `List` | `modeSenderPolicy` | ``BswModeSenderPolicy`` | aggr | naming (plural); untyped |
| `parameterPolicies` | `List` | `parameterPolicy` | ``BswParameterPolicy`` | aggr | member class `BswParameterPolicy` missing |
| `perInstanceParameters` | `List` | `perInstanceParameter` | ``ParameterDataPrototype`` | aggr | naming (plural) |
| `receptionPolicies` | `List` | `receptionPolicy` | ``BswDataReceptionPolicy`` | aggr | naming (plural); untyped |
| `releasedTriggerPolicies` | `List` | `releasedTriggerPolicy` | ``BswReleasedTriggerPolicy`` | aggr | member class `BswReleasedTriggerPolicy` missing |
| `schedulerNamePrefixes` | `List` | `schedulerNamePrefix` | ``BswSchedulerNamePrefix`` | aggr | naming (plural) |
| `sendPolicies` | `List` | `sendPolicy` | ``BswDataSendPolicy`` | aggr | member class `BswDataSendPolicy` missing |
| `serviceDependencies` | `List` | `serviceDependency` | ``BswServiceDependency`` | aggr | naming (plural) |
| `triggerDirectImplementations` | `List` | `triggerDirectImplementation` | ``BswTriggerDirectImplementation`` | aggr | naming (plural) |
| `variationPointProxies` | `List` | `variationPointProxy` | ``VariationPointProxy`` | aggr | naming (plural) |
| `addModeSenderPolicy`/`getModeSenderPolicies` | — | `modeSenderPolicy` | ``BswModeSenderPolicy`` | aggr | **fixed** — previously operated on `modeReceiverPolicies`; now uses `modeSenderPolicies` |

## `FlatMap`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `instance` | ``FlatInstanceDescriptor`` | aggr | missing |

## `ExclusiveArea`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `InternalBehavior`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `constantMemory` | ``ParameterData Prototype`` | aggr | missing |
| — *(missing)* | `—` | `constantValueMapping` | ``ConstantSpecification MappingSet`` | ref | missing |
| — *(missing)* | `—` | `exclusiveArea` | ``ExclusiveArea`` | aggr | missing |
| — *(missing)* | `—` | `exclusiveAreaNestingOrder` | ``ExclusiveAreaNesting Order`` | aggr | missing |

## `ServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ServiceDependency`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 12.2
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `assigneddatatype` | `—` | `assignedDataType` | ``RoleBasedDataType Assignment`` | aggr | type (spec one vs py list) |

## `DiagEventDebounceAlgorithm`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 12.32
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagEventDebounceMonitorInternal`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `EcuStateMgrUserNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 12.15
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DltUserNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 12.16
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagnosticComponentNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagnosticUploadDownloadNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagnosticsCommunicationSecurityNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 12.28
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `FunctionInhibitionNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 12.20
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `GlobalSupervisionNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `HardwareTestNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `SupervisedEntityCheckpointNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `SyncTimeBaseMgrUserNeeds`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —  | **table:** Table 12.17
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `RecordValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `field(ordered)` | ``ValueSpecification`` | aggr | missing |

## `ArrayValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `element(ordered)` | ``ValueSpecification`` | aggr | missing |

## `CompositionSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** 307
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `component` | ``SwComponent Prototype`` | aggr | missing |
| — *(missing)* | `—` | `connector` | ``SwConnector`` | aggr | missing |
| `constantvaluemappingrefs` | `—` | `constantValueMapping` | ``ConstantSpecification MappingSet`` | ref | type (spec many vs py single) |

## `EcuInstance`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 50
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::EcuInstance`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `associatedcomipdugrouprefs` | `—` | `associatedComIPduGroup` | ``ISignalIPduGroup`` | ref | type (spec many vs py single) |

## `DiagnosticConnection`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DiagnosticConnection.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `functionalrequestrefs` | `—` | `functionalRequest` | ``TpConnectionIdent`` | ref | type (spec many vs py single) |

## `TpConnectionIdent`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::TransportProtocols`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `PhysicalChannel`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `commconnectorrefs` | `—` | `commConnector` | ``Communication Connector`` | ref | type (spec many vs py single) |
| — *(missing)* | `—` | `frameTriggering` | ``FrameTriggering`` | aggr | missing |
| — *(missing)* | `—` | `iSignalTriggering` | ``ISignalTriggering`` | aggr | missing |

## `EthernetPhysicalChannel`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `networkEndpoint` | ``NetworkEndpoint`` | aggr | missing |

## `IdentCaption`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DataInterface`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `NvDataInterface`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `nvdata` | `—` | `nvData` | ``VariableDataPrototype`` | aggr | type (spec many vs py single) |

## `ApplicationPrimitiveDataType`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —  | **table:** Table 5.6
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `SwComponentPrototype`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `typeTRef` | `RefType` | `type` | ``SwComponentType`` | tref | type (PDF SwComponentType vs py RefType) |

## `PPortPrototype`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `providedInterfaceTRef` | `TRefType` | `providedInterface` | ``PortInterface`` | tref | type (PDF PortInterface vs py TRefType) |

## `ApplicationSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AtpInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `atpContextElement(ordered)` | ``AtpPrototype`` | ref | missing |

## `DiagnosticCommonElement`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonElement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticCommonElement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagnosticServiceTable`
- **PDF:** `AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticContribution.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `serviceInstance` | ``DiagnosticService Instance`` | ref | missing |

## `AdminData`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::MSR::AsamHdo::AdminData`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/AdminData.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `docRevision(ordered)` | ``DocRevision`` | aggr | missing |

## `EcucTextualParamValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `value` | `ARLiteral` | `value` | ``VerbatimString`` | attr | type (PDF VerbatimString vs py ARLiteral) |

## `EcucNumericalParamValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `value` | `ARNumerical` | `value` | ``Numerical`` | attr | type (PDF Numerical vs py ARNumerical) |

## `EcucAbstractReferenceValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `definitionRef` | `RefType` | `definition` | ``EcucAbstractReference Def`` | ref | type (PDF EcucAbstractReference Def vs py RefType) |
| `isAutoValue` | `ARBoolean` | `isAutoValue` | ``Boolean`` | attr | type (PDF Boolean vs py ARBoolean) |

## `EcucInstanceReferenceValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `valueIRef` | `AnyInstanceRef` | `value` | ``AtpFeature`` | iref | type (PDF AtpFeature vs py AnyInstanceRef) |

## `EcucReferenceValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `valueRef` | `RefType` | `value` | ``Referrable`` | ref | type (PDF Referrable vs py RefType) |

## `EcucContainerValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `definitionRef` | `RefType` | `definition` | ``EcucContainerDef`` | ref | type (PDF EcucContainerDef vs py RefType) |
| `subContainers` | `List[EcucContainerValue]` | `subContainer` | ``EcucContainerValue`` | aggr | naming |

## `EcucValueConfigurationClass`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —  | **table:** Table 2.10
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `EcucEnumerationParamDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `literal` | ``EcucEnumerationLiteral Def`` | aggr | missing |

## `EcucChoiceContainerDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `choice` | ``EcucParamConf ContainerDef`` | aggr | missing |

## `EcucParamConfContainerDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `parameter` | ``EcucParameterDef`` | aggr | missing |
| — *(missing)* | `—` | `reference` | ``EcucAbstractReference Def`` | aggr | missing |
| — *(missing)* | `—` | `subContainer` | ``EcucContainerDef`` | aggr | missing |

## `EcucAddInfoParamDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::ECUCParameterDefTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `Frame`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `pduToFrameMapping` | ``PduToFrameMapping`` | aggr | missing |

## `NmPdu`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `iSignalToIPduMapping` | ``ISignalToIPduMapping`` | aggr | missing |

## `NPdu`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `PduTriggering`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `ipduportrefs` | `—` | `iPduPort` | ``IPduPort`` | ref | type (spec many vs py single) |
| `isignaltriggeringrefs` | `—` | `iSignalTriggering` | ``ISignalTriggering`` | ref | type (spec many vs py single) |

## `FrameTriggering`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `pdutriggeringrefs` | `—` | `pduTriggering` | ``PduTriggering`` | ref | type (spec many vs py single) |

## `PredefinedVariant`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::VariantHandling`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `includedvariantrefs` | `—` | `includedVariant` | ``PredefinedVariant`` | ref | type (spec many vs py single) |
| `swsystemconstantvaluesetrefs` | `—` | `swSystemconstantValueSet` | ``SwSystemconstant ValueSet`` | ref | type (spec many vs py single) |

## `AnyInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_ECUConfiguration.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AnyInstanceRef`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/AnyInstanceRef.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextElement(ordered)` | ``AtpFeature`` | ref | missing |

## `HwAttributeValue`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** 16
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate::HwAttributeValue`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwAttributeValue.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `annotation` | ``Annotation`` | aggr | missing |
| — *(missing)* | `—` | `v` | ``Numerical`` | attr | missing |
| — *(missing)* | `—` | `vt` | ``VerbatimString`` | attr | missing |

## `HwAttributeLiteralDef`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate::HwAttributeValue`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwAttributeValue.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `HwType`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `HwCategory`
- **PDF:** `AUTOSAR_CP_TPS_ECUResourceTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `hwAttributeDef` | ``HwAttributeDef`` | aggr | missing |

## `ApplicationArrayDataType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 252  | **table:** Table 5.9
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `element` | ``ApplicationArray Element`` | aggr | missing |

## `SwRecordLayoutV`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 421
- **Package:** `M2::MSR::DataDictionary::RecordLayout`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/RecordLayout.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `baseTypeRef` | `RefType` | `baseType` | ``SwBaseType`` | ref | type (PDF SwBaseType vs py RefType) |
| `swGenericAxisParamTypeRef` | `RefType` | `swGenericAxisParamType` | ``SwGenericAxisParam Type`` | ref | type (PDF SwGenericAxisParam Type vs py RefType) |

## `ReferenceValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 436
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `referenceValue` | ``DataPrototype`` | ref | missing |

## `NotAvailableValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 440
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `defaultPattern` | ``PositiveInteger`` | attr | missing |

## `ConstantSpecificationMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 443  | **table:** Table 5.118
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `applConstant` | ``ConstantSpecification`` | ref | missing |
| — *(missing)* | `—` | `implConstant` | ``ConstantSpecification`` | ref | missing |

## `RuleBasedAxisCont`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 464
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `category` | `ARLiteral` | `category` | ``CalprmAxisCategory Enum`` | attr | type (PDF CalprmAxisCategory Enum vs py ARLiteral) |
| `swArraysize` | `ValueList` | `swArraysize` | ``ValueList`` | aggr | type (spec one vs py list) |
| `swAxisIndex` | `ARLiteral` | `swAxisIndex` | ``AxisIndexType`` | attr | type (PDF AxisIndexType vs py ARLiteral) |
| `unitRef` | `RefType` | `unit` | ``Unit`` | ref | type (PDF Unit vs py RefType) |

## `CompositeRuleBasedValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 471
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `argument(ordered)` | ``CompositeValue Specification`` | aggr | missing |
| — *(missing)* | `—` | `compoundPrimitiveArgument(ordered)` | ``CompositeRuleBased ValueArgument`` | aggr | missing |
| — *(missing)* | `—` | `maxSizeToFill` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `rule` | ``Identifier`` | attr | missing |

## `IncludedDataTypeSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 600
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::IncludedDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/IncludedDataTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `data_type_refs` | `List[RefType]` | `dataType` | ``AutosarDataType`` | ref | type (PDF AutosarDataType vs py List[RefType]) |
| `literal_prefix` | `ARLiteral` | `literalPrefix` | ``Identifier`` | attr | type (PDF Identifier vs py ARLiteral) |

## `SensorActuatorSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 646
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `sensorActuator` | ``HwDescriptionEntity`` | ref | missing |

## `ApplicationCompositeElementInPortInterfaceInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 952
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/InstanceRefs.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextDataPrototype(ordered)` | ``ApplicationComposite ElementDataPrototype`` | ref | missing |

## `ConsumedServiceInstance`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 980
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `allowedserviceproviderrefs` | `—` | `allowedServiceProvider` | ``NetworkEndpoint`` | ref | type (spec many vs py single) |
| — *(missing)* | `—` | `blocklistedVersion` | ``SomeipServiceVersion`` | aggr | missing |
| — *(missing)* | `—` | `consumedEventGroup` | ``ConsumedEventGroup`` | aggr | missing |

## `ISignalGroup`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 993
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `combasedsignalgrouptransformationref` | `—` | `comBasedSignalGroupTransformation` | ``DataTransformation`` | ref | type (spec one vs py list) |
| `transformationisignalprops` | `—` | `transformationISignalProps` | ``TransformationISignal Props`` | aggr | type (spec many vs py single) |

## `ProvidedServiceInstance`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 1000
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `allowedServiceConsumer` | ``NetworkEndpoint`` | ref | missing |
| — *(missing)* | `—` | `autoAvailable` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `eventHandler` | ``EventHandler`` | aggr | missing |
| — *(missing)* | `—` | `loadBalancingPriority` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `loadBalancingWeight` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `localUnicastAddress` | ``ApplicationEndpoint`` | ref | missing |
| — *(missing)* | `—` | `minorVersion` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `remoteMulticastSubscriptionAddress` | ``ApplicationEndpoint`` | ref | missing |
| — *(missing)* | `—` | `remoteUnicastAddress` | ``ApplicationEndpoint`` | ref | missing |

## `RootSwCompositionPrototype`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** 1003
- **Package:** `M2::AUTOSARTemplates::SystemTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `calibrationparametervaluesetref` | `—` | `calibrationParameterValueSet` | ``CalibrationParameter ValueSet`` | ref | type (spec many vs py single) |

## `GeneralAnnotation`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 4.57
- **Package:** `M2::MSR::Documentation::Annotation`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Annotation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `annotationOrigin` | `ARLiteral` | `annotationOrigin` | ``String`` | attr | type (PDF String vs py ARLiteral) |

## `CompuContent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.63
- **Package:** `M2::MSR::AsamHdo::ComputationMethod`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CompuConstContent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.72
- **Package:** `M2::MSR::AsamHdo::ComputationMethod`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CompuScaleContents`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.67
- **Package:** `M2::MSR::AsamHdo::ComputationMethod`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CompuNominatorDenominator`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::AsamHdo::ComputationMethod`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `v(ordered)` | ``Numerical`` | attr | missing |

## `CompuScales`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.65
- **Package:** `M2::MSR::AsamHdo::ComputationMethod`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `compuScale(ordered)` | ``CompuScale`` | aggr | missing |

## `DataConstrRule`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::AsamHdo::Constraints::GlobalConstraints`
- **Source:** `src/armodel/models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `constrLevel` | ``Integer`` | attr | missing |

## `SwValueCont`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::CalibrationData::CalibrationValue`
- **Source:** `src/armodel/models/M2/MSR/CalibrationData/CalibrationValue.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `swArraysize` | `ValueList` | `swArraysize` | ``ValueList`` | aggr | type (spec one vs py list) |
| `unitRef` | `RefType` | `unit` | ``Unit`` | ref | type (PDF Unit vs py RefType) |

## `SwAxisIndividual`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::DataDictionary::Axis`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/Axis.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `compuMethodRef` | `RefType` | `compuMethod` | ``CompuMethod`` | ref | type (PDF CompuMethod vs py RefType) |
| `dataConstrRef` | `RefType` | `dataConstr` | ``DataConstr`` | ref | type (PDF DataConstr vs py RefType) |
| `inputVariableTypeRef` | `RefType` | `inputVariableType` | ``ApplicationPrimitive DataType`` | ref | type (PDF ApplicationPrimitive DataType vs py RefType) |
| `swMaxAxisPoints` | `ARNumerical` | `swMaxAxisPoints` | ``Integer`` | attr | type (PDF Integer vs py ARNumerical) |
| `swMinAxisPoints` | `ARNumerical` | `swMinAxisPoints` | ``Integer`` | attr | type (PDF Integer vs py ARNumerical) |
| `swVariableRefs` | `List` | `swVariableRef(ordered)` | ``SwVariableRefProxy`` | aggr | naming |

## `SwAxisGrouped`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::DataDictionary::Axis`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/Axis.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `sharedAxisTypeRef` | `RefType` | `sharedAxisType` | ``ApplicationPrimitive DataType`` | ref | type (PDF ApplicationPrimitive DataType vs py RefType) |
| `swAxisIndex` | `ARNumerical` | `swAxisIndex` | ``AxisIndexType`` | attr | type (PDF AxisIndexType vs py ARNumerical) |
| `swCalprmRef` | `RefType` | `swCalprmRef` | ``SwCalprmRefProxy`` | aggr | type (PDF SwCalprmRefProxy vs py RefType) |

## `SwCalprmAxisSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.46
- **Package:** `M2::MSR::DataDictionary::CalibrationParameter`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `_swCalprmAxis` | `List[SwCalprmAxis]` | `swCalprmAxis` | ``SwCalprmAxis`` | aggr | type (PDF SwCalprmAxis vs py List[SwCalprmAxis]) |

## `SwRecordLayoutGroup`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::MSR::DataDictionary::RecordLayout`
- **Source:** `src/armodel/models/M2/MSR/DataDictionary/RecordLayout.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `category` | `ARLiteral` | `category` | ``AsamRecordLayout Semantics`` | attr | type (PDF AsamRecordLayout Semantics vs py ARLiteral) |
| `swGenericAxisParamTypeRef` | `RefType` | `swGenericAxisParamType` | ``SwGenericAxisParam Type`` | ref | type (PDF SwGenericAxisParam Type vs py RefType) |
| `swRecordLayoutComponent` | `ARLiteral` | `swRecordLayoutComponent` | ``Identifier`` | attr | type (PDF Identifier vs py ARLiteral) |
| `swRecordLayoutGroupFrom` | `ARLiteral` | `swRecordLayoutGroupFrom` | ``RecordLayoutIterator Point`` | attr | type (PDF RecordLayoutIterator Point vs py ARLiteral) |

## `QueuedSenderComSpec`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 4.68
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `UserDefinedTransformationComSpecProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Communication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `EndToEndProtectionVariablePrototype`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `sender` | ``VariableDataPrototype`` | iref | missing |

## `EndToEndProtectionSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 4.96
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `endToEndProtection` | ``EndToEndProtection`` | aggr | missing |

## `ModeAccessPointIdent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 14.6
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ParameterInterface`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `parameter` | ``ParameterData Prototype`` | aggr | missing |

## `MetaDataItemSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `metaDataItem(ordered)` | ``MetaDataItem`` | aggr | missing |

## `TriggerInterface`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 4.12
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `trigger` | ``Trigger`` | aggr | missing |

## `PortInterfaceMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `SubElementMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `texttablemapping` | `—` | `textTableMapping` | ``TextTableMapping`` | aggr | type (spec one vs py list) |

## `TriggerInterfaceMapping`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 4.31
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `triggermapping` | `—` | `triggerMapping` | ``TriggerMapping`` | aggr | type (spec many vs py single) |

## `ModeDeclarationMappingSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 4.29
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `modeDeclarationMapping` | ``ModeDeclaration Mapping`` | aggr | missing |

## `PortInterfaceMappingSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 4.20
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `portInterfaceMappings` | `List[PortInterfaceMapping]` | `portInterfaceMapping` | ``PortInterfaceMapping`` | aggr | naming |

## `ApplicationCompositeDataType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ApplicationRecordDataType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `element(ordered)` | ``ApplicationRecord Element`` | aggr | missing |

## `DelegationSwConnector`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Composition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `innerPort` | ``PortPrototype`` | iref | missing |

## `VariableInAtomicSwcInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `abstractTargetDataElement` | ``VariableDataPrototype`` | ref | missing |
| — *(missing)* | `—` | `base` | ``AtomicSwComponent Type`` | ref | missing |
| — *(missing)* | `—` | `contextPort` | ``PortPrototype`` | ref | missing |

## `InnerPortGroupInCompositionInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `context(ordered)` | ``SwComponent Prototype`` | ref | missing |

## `SymbolProps`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `RPortPrototype`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 3.5
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `mayBeUnconnected` | `ARBoolean` | `mayBeUnconnected` | ``Boolean`` | attr | type (PDF Boolean vs py ARBoolean) |
| `requiredInterfaceTRef` | `TRefType` | `requiredInterface` | ``PortInterface`` | tref | type (PDF PortInterface vs py TRefType) |

## `PortGroup`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `_inner_group_iref` | `List[InnerPortGroupInCompositionInstanceRef]` | `innerGroup` | ``PortGroup`` | iref | type (PDF PortGroup vs py List[InnerPortGroupInCompositionInstanceRef]) |
| `_outer_port_ref` | `List[RefType]` | `outerPort` | ``PortPrototype`` | ref | type (PDF PortPrototype vs py List[RefType]) |

## `NvBlockSwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 11.5
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `nvblockdescriptor` | `—` | `nvBlockDescriptor` | ``NvBlockDescriptor`` | aggr | type (spec many vs py single) |

## `ServiceProxySwComponentType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ArVariableInImplementationDataInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::InstanceRefsUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstanceRefsUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextDataPrototype(ordered)` | ``AbstractImplementation DataTypeElement`` | ref | missing |

## `VariableInAtomicSWCTypeInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::InstanceRefsUsage`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstanceRefsUsage.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextDataPrototype(ordered)` | ``ApplicationComposite ElementDataPrototype`` | ref | missing |

## `IncludedModeDeclarationGroupSet`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modedeclarationgrouprefs` | `—` | `modeDeclarationGroup` | ``ModeDeclarationGroup`` | ref | type (spec many vs py single) |

## `PortAPIOption`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 7.43
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PortAPIOptions.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `portArgValue(ordered)` | ``PortDefinedArgument Value`` | aggr | missing |

## `InitEvent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 7.23
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BackgroundEvent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 7.17
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ExternalTriggeringPointIdent`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `RunnableEntityArgument`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `symbol` | `ARLiteral` | `symbol` | ``CIdentifier`` | attr | type (PDF CIdentifier vs py ARLiteral) |

## `AsynchronousServerCallPoint`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 7.38
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `SynchronousServerCallPoint`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `calledFromWithinExclusiveAreaRef` | `RefType` | `calledFromWithinExclusiveArea` | ``ExclusiveAreaNesting Order`` | ref | type (PDF ExclusiveAreaNesting Order vs py RefType) |

## `AbstractImplementationDataTypeElement`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.16
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AbstractImplementationDataType`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.15
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BswMgrNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CryptoKeyManagementNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CryptoServiceJobNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagnosticControlNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagnosticEventManagerNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 13.14
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DiagnosticRequestFileTransferNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DoIpActivationLineNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DoIpGidNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 13.55
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DoIpGidSynchronizationNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 13.56
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DoIpPowerModeStatusNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 13.58
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `FurtherActionByteNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `IdsMgrCustomTimestampNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `J1939DcmDm19Support`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `J1939RmIncomingRequestServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `J1939RmOutgoingRequestServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 13.71
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `V2xDataManagerNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `V2xFacUserNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `V2xMUserNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `VendorSpecificServiceNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `WarningIndicatorRequestedBitNeeds`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CompositeValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —  | **table:** Table 5.111
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AbstractRuleBasedValueSpecification`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CompositeRuleBasedValueArgument`
- **PDF:** `AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Constants`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CanControllerXlConfiguration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 70  | **table:** Table 3.18
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `errorSignalingEnabled` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `propSeg` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `pwmL` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `pwmO` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `pwmS` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `sspOffset` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `syncJumpWidth` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `timeSeg1` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `timeSeg2` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `trcvPwmModeEnabled` | ``Boolean`` | attr | missing |

## `CanControllerXlConfigurationRequirements`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 71
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `errorSignalingEnabled` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `maxPwmL` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `maxPwmO` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `maxPwmS` | ``PositiveInteger`` | attr | missing |

## `CouplingPort`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 109
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `defaultVlanRef` | `RefType` | `defaultVlan` | ``EthernetPhysical Channel`` | ref | type (PDF EthernetPhysical Channel vs py RefType) |
| `macMulticastAddressRefs` | `List[RefType]` | `macMulticastAddress` | ``MacMulticastGroup`` | ref | type (PDF MacMulticastGroup vs py List[RefType]) |
| `macSecProps` | `List[MacSecProps]` | `macSecProps` | ``MacSecProps`` | aggr | type (PDF MacSecProps vs py List[MacSecProps]) |
| `pncMappingRefs` | `List[RefType]` | `pncMapping` | ``PncMappingIdent`` | ref | type (PDF PncMappingIdent vs py List[RefType]) |
| — *(missing)* | `—` | `vlanModifier` | ``EthernetPhysical Channel`` | ref | missing |

## `EthernetCommunicationConnector`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 117
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `ethIpPropsRef` | `RefType` | `ethIpProps` | ``EthIpProps`` | ref | type (PDF EthIpProps vs py RefType) |

## `CouplingPortDetails`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 121
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `couplingPortStructuralElements` | `List[CouplingPortStructuralElement]` | `couplingPortStructuralElement` | ``CouplingPortStructural Element`` | aggr | naming |
| `ethernetPriorityRegenerations` | `List[EthernetPriorityRegeneration]` | `ethernetPriorityRegeneration` | ``EthernetPriority Regeneration`` | aggr | naming |
| `ethernetTrafficClassAssignments` | `List[CouplingPortTrafficClassAssignment]` | `ethernetTrafficClassAssignment` | ``CouplingPortTraffic ClassAssignment`` | aggr | naming |

## `CouplingPortFifo`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 124
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `assignedtrafficclass` | `—` | `assignedTrafficClass` | ``PositiveInteger`` | attr | type (spec one vs py list) |

## `SenderRecArrayTypeMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 235  | **table:** Table 5.28
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DataMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `arrayElementMapping` | ``SenderRecArray ElementMapping`` | aggr | missing |
| — *(missing)* | `—` | `senderToSignalTextTableMapping` | ``TextTableMapping`` | aggr | missing |

## `ComManagementMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 282
- **Package:** `M2::AUTOSARTemplates::SystemTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `commanagementportgrouprefs` | `—` | `comManagementPortGroup` | ``PortGroup`` | iref | type (spec many vs py single) |
| `physicalchannelref` | `—` | `physicalChannel` | ``PhysicalChannel`` | ref | type (spec many vs py single) |

## `ContainedIPduProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 355
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `containedPduTriggering` | ``PduTriggering`` | ref | missing |

## `ModeDrivenTransmissionModeCondition`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 393
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::Timing`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/Timing.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `modedeclarationref` | `—` | `modeDeclaration` | ``ModeDeclaration`` | ref | type (spec many vs py single) |

## `LinConfigurationEntry`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 434
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `assignedController` | ``LinSlave`` | ref | missing |
| — *(missing)* | `—` | `assignedLinSlaveConfig` | ``LinSlaveConfigIdent`` | ref | missing |

## `SoAdConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 451
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `connections` | `List[SocketConnection]` | `connection` | ``SocketConnection`` | aggr | naming |
| `connectionBundles` | `List[SocketConnectionBundle]` | `connectionBundle` | ``SocketConnection Bundle`` | aggr | naming |

## `ApplicationEndpoint`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 457
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `consumedServiceInstance` | ``ConsumedService Instance`` | aggr | missing |

## `Ipv6Configuration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 466
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::NetworkEndpoint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dnsServerAddress` | ``Ip6AddressString`` | attr | missing |

## `AbstractServiceInstance`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 476
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `routingGroupRefs` | `List[RefType]` | `routingGroup` | ``SoAdRoutingGroup`` | ref | type (PDF SoAdRoutingGroup vs py List[RefType]) |

## `EventHandler`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 492
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `eventGroupIdentifier` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `eventMulticastAddress` | ``ApplicationEndpoint`` | ref | missing |
| — *(missing)* | `—` | `pduActivationRoutingGroup` | ``PduActivationRouting Group`` | aggr | missing |
| — *(missing)* | `—` | `sdServerEgTimingConfig` | ``SomeipSdServerEvent GroupTimingConfig`` | ref | missing |

## `DoIpLogicTesterAddressProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 556
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DoIp`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `doiptesterroutingactivationref` | `—` | `doIpTesterRoutingActivation` | ``DoIpRoutingActivation`` | ref | type (spec many vs py single) |

## `TlsCryptoServiceMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 559
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `keyexchangeref` | `—` | `keyExchange` | ``CryptoServicePrimitive`` | ref | type (spec many vs py single) |

## `StateDependentFirewall`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 583  | **table:** Table 6.234
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall::StateDependentFirewall`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/StateDependentFirewall.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `defaultAction` | ``FirewallActionEnum`` | attr | missing |
| — *(missing)* | `—` | `firewallRuleProps(ordered)` | ``FirewallRuleProps`` | aggr | missing |
| — *(missing)* | `—` | `firewallStateModeDeclaration` | ``ModeDeclaration`` | ref | missing |

## `FirewallRule`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 584
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall::FirewallRule`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRule.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bucketSize` | ``PositiveInteger`` | attr | missing |

## `FirewallRuleProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 584  | **table:** Table 6.235
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall::FirewallRuleProps`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRuleProps.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `action` | ``FirewallActionEnum`` | attr | missing |
| — *(missing)* | `—` | `matchingEgressRule(ordered)` | ``FirewallRule`` | ref | missing |
| — *(missing)* | `—` | `matchingIngressRule(ordered)` | ``FirewallRule`` | ref | missing |

## `NmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 672
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `communicationClusterRef` | `RefType` | `communicationCluster` | ``CommunicationCluster`` | ref | type (PDF CommunicationCluster vs py RefType) |
| `nmNodes` | `List[NmNode]` | `nmNode` | ``NmNode`` | aggr | naming |

## `FlexrayNmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 678
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmCarWakeUpBitPosition` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `nmCarWakeUpFilterEnabled` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `nmCarWakeUpFilterNodeId` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `nmCarWakeUpRxEnabled` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `nmDataCycle` | ``Integer`` | attr | missing |
| — *(missing)* | `—` | `nmMainFunctionPeriod` | ``TimeValue`` | attr | missing |
| — *(missing)* | `—` | `nmRemoteSleepIndicationTime` | ``TimeValue`` | attr | missing |
| — *(missing)* | `—` | `nmRepeatMessageTime` | ``TimeValue`` | attr | missing |
| — *(missing)* | `—` | `nmRepetitionCycle` | ``Integer`` | attr | missing |
| — *(missing)* | `—` | `nmVotingCycle` | ``Integer`` | attr | missing |

## `FlexrayNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 679  | **table:** Table 6.308
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmHwVoteEnabled` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `nmMainFunctionAcrossFrCycle` | ``Boolean`` | attr | missing |

## `FlexrayNmNode`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 679  | **table:** Table 6.310
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CanNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 683  | **table:** Table 6.313
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `UdpNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 688  | **table:** Table 6.316
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `J1939NmCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 691  | **table:** Table 6.319
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `addressClaimEnabled` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `usesDynamicAddressing` | ``Boolean`` | attr | missing |

## `IPduMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 840
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `pduMaxLength` | ``PositiveInteger`` | attr | missing |

## `RtePluginProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** 971
- **Package:** `M2::AUTOSARTemplates::CommonStructure::FlatMap`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `associatedCrossSwClusterComRtePlugin` | ``EcucContainerValue`` | ref | missing |
| — *(missing)* | `—` | `associatedRtePlugin` | ``EcucContainerValue`` | ref | missing |

## `SenderRecCompositeTypeMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 5.27
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DataMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AbstractDoIpLogicAddressProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.208
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DoIp`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DoIpLogicTargetAddressProps`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.209
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::DoIp`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ECUMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::ECUResourceMapping`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/ECUResourceMapping.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `commControllerMappings` | `List[CommunicationControllerMapping]` | `commControllerMapping` | ``Communication ControllerMapping`` | aggr | naming |
| `ecuRef` | `RefType` | `ecu` | ``HwElement`` | ref | type (PDF HwElement vs py RefType) |
| `ecuInstanceRef` | `RefType` | `ecuInstance` | ``EcuInstance`` | ref | type (PDF EcuInstance vs py RefType) |
| `hwPortMappings` | `List[HwPortMapping]` | `hwPortMapping` | ``HwPortMapping`` | aggr | naming |

## `VariableDataPrototypeInSystemInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextComponent(ordered)` | ``SwComponent Prototype`` | ref | missing |

## `ComponentInSystemInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::InstanceRefs`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextComponent(ordered)` | ``SwComponent Prototype`` | ref | missing |

## `NmClusterCoupling`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `BusspecificNmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.301
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `J1939NmEcu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `NmConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.298
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::NetworkManagement`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `nmCluster` | ``NmCluster`` | aggr | missing |
| — *(missing)* | `—` | `nmClusterCoupling` | ``NmClusterCoupling`` | aggr | missing |
| — *(missing)* | `—` | `nmIfEcu` | ``NmEcu`` | aggr | missing |

## `CryptoServiceMapping`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CanTpConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::TransportProtocols`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `tpAddress` | ``CanTpAddress`` | aggr | missing |
| — *(missing)* | `—` | `tpChannel` | ``CanTpChannel`` | aggr | missing |
| — *(missing)* | `—` | `tpNode` | ``CanTpNode`` | aggr | missing |

## `DoIpTpConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.205
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::TransportProtocols`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `doIpLogicAddress` | ``DoIpLogicAddress`` | aggr | missing |

## `LinTpConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::TransportProtocols`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `tpAddress` | ``TpAddress`` | aggr | missing |
| — *(missing)* | `—` | `tpNode` | ``LinTpNode`` | aggr | missing |

## `J1939SharedAddressCluster`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `participatingj1939clusterrefs` | `—` | `participatingJ1939Cluster` | ``J1939Cluster`` | ref | type (spec many vs py single) |

## `PduMappingDefaultValue`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 8.6
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `defaultValueElement` | ``DefaultValueElement`` | aggr | missing |

## `ISignalTriggering`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `isignalportrefs` | `—` | `iSignalPort` | ``ISignalPort`` | ref | type (spec many vs py single) |

## `StaticPart`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.74
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `iPduRef` | `RefType` | `iPdu` | ``ISignalIPdu`` | ref | type (PDF ISignalIPdu vs py RefType) |

## `DynamicPartAlternative`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `iPduRef` | `RefType` | `iPdu` | ``ISignalIPdu`` | ref | type (PDF ISignalIPdu vs py RefType) |

## `GeneralPurposePdu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `GeneralPurposeIPdu`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CommunicationCycle`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.84
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AbstractCanPhysicalChannel`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 3.21
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CanPhysicalChannel`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `FramePort`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.3
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CommunicationConnector`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 3.5
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `ecuCommPortInstance` | ``CommConnectorPort`` | aggr | missing |
| — *(missing)* | `—` | `pncFilterArrayMask(ordered)` | ``PositiveInteger`` | attr | missing |

## `AbstractEthernetFrame`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.229
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetFrame`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetFrame.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `GenericEthernetFrame`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.231
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetFrame`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetFrame.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CouplingPortStructuralElement`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CouplingPortScheduler`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 3.65
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `predecessorRefs` | `List[RefType]` | `predecessor(ordered)` | ``CouplingPortStructural Element`` | ref | naming |

## `VlanMembership`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `vlanRef` | `RefType` | `vlan` | ``EthernetPhysical Channel`` | ref | type (PDF EthernetPhysical Channel vs py RefType) |

## `NetworkEndpointAddress`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::NetworkEndpoint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `TimeSyncClientConfiguration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.146
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::NetworkEndpoint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `orderedMaster(ordered)` | ``OrderedMaster`` | aggr | missing |

## `TransportProtocolConfiguration`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `TcpUdpConfig`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.128
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CanFrame`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.110
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `CanFrameTriggering`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.111
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `absolutelyScheduledTiming` | ``TtcanAbsolutely ScheduledTiming`` | aggr | missing |

## `AbstractCanCommunicationConnector`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 3.23
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `FlexrayFrame`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.80
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `LinFrame`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.87
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `LinUnconditionalFrame`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `FreeFormatEntry`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 6.99
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `DataTransformationSet`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —  | **table:** Table 7.2
- **Package:** `M2::AUTOSARTemplates::SystemTemplate::Transformer`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `dataTransformation` | ``DataTransformation`` | aggr | missing |
| — *(missing)* | `—` | `transformationTechnology` | ``Transformation Technology`` | aggr | missing |

## `Collection`
- **PDF:** `AUTOSAR_CP_TPS_SystemTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ElementCollection.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `collectedInstance` | ``AtpFeature`` | iref | missing |
| `elementrefs` | `—` | `element` | ``Identifiable`` | ref | type (spec many vs py single) |
| `sourceelementrefs` | `—` | `sourceElement` | ``Identifiable`` | ref | type (spec many vs py single) |
| — *(missing)* | `—` | `sourceInstance` | ``AtpFeature`` | iref | missing |

## `SwcTiming`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 25
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::TimingExtensions`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingExtensions.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `behavior` | ``SwcInternalBehavior`` | ref | missing |

## `TimingCondition`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 35  | **table:** Table 3.7
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingCondition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingCondition.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingConditionFormula` | ``TimingCondition Formula`` | aggr | missing |

## `TimingExtensionResource`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 35
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingExtensionResource`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingExtensionResource.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingArgument` | ``AutosarOperation ArgumentInstance`` | aggr | missing |

## `TimingModeInstance`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 37  | **table:** Table 3.11
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingModeInstance`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingModeInstance.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `modeInstance` | ``ModeInSwcBsw InstanceRef`` | aggr | missing |

## `ModeInBswInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 38
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::ModeInBswInstanceRef`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInBswInstanceRef.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `contextBswImplementation` | ``BswImplementation`` | ref | missing |
| — *(missing)* | `—` | `contextModeDeclarationGroupPrototype` | ``ModeDeclarationGroup Prototype`` | ref | missing |
| — *(missing)* | `—` | `targetModeDeclaration` | ``ModeDeclaration`` | ref | missing |

## `ModeInSwcInstanceRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 38
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::ModeInSwcInstanceRef`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInSwcInstanceRef.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `base` | ``SwComponentType`` | ref | missing |
| — *(missing)* | `—` | `contextComponent` | ``SwComponent Prototype`` | ref | missing |
| — *(missing)* | `—` | `contextModeDeclarationGroupPrototype` | ``ModeDeclarationGroup Prototype`` | ref | missing |
| — *(missing)* | `—` | `contextPort` | ``PortPrototype`` | ref | missing |

## `SynchronizationTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 92  | **table:** Table 3.55
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `scope` | ``TimingDescriptionEvent Chain`` | ref | missing |
| — *(missing)* | `—` | `scopeEvent` | ``TimingDescriptionEvent`` | ref | missing |
| — *(missing)* | `—` | `synchronizationConstraintType` | ``SynchronizationType Enum`` | attr | missing |
| — *(missing)* | `—` | `tolerance` | ``MultidimensionalTime`` | aggr | missing |

## `LatencyTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 95
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `latencyConstraintType` | ``LatencyConstraintType Enum`` | attr | missing |
| — *(missing)* | `—` | `maximum` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `minimum` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `nominal` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `scope` | ``TimingDescriptionEvent Chain`` | ref | missing |

## `EventTriggeringConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 100
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `event` | ``TimingDescriptionEvent`` | ref | missing |

## `PeriodicEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 101
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `jitter` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `minimumInterArrivalTime` | ``MultidimensionalTime`` | aggr | missing |

## `SporadicEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 105
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `jitter` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `maximumInterArrivalTime` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `minimumInterArrivalTime` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `period` | ``MultidimensionalTime`` | aggr | missing |

## `ConcretePatternEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 106
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `offset` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `patternJitter` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `patternLength` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `patternPeriod` | ``MultidimensionalTime`` | aggr | missing |

## `BurstPatternEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 109
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maxNumberOfOccurrences` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `minimumInterArrivalTime` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `minNumberOfOccurrences` | ``PositiveInteger`` | attr | missing |
| — *(missing)* | `—` | `patternJitter` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `patternLength` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `patternPeriod` | ``MultidimensionalTime`` | aggr | missing |

## `ArbitraryEventTriggering`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 111
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `confidenceInterval` | ``ConfidenceInterval`` | aggr | missing |

## `ConfidenceInterval`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 112
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `propability` | ``Float`` | attr | missing |

## `OffsetTimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 114
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::OffsetConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/OffsetConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maximum` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `minimum` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `source` | ``TimingDescriptionEvent`` | ref | missing |
| — *(missing)* | `—` | `target` | ``TimingDescriptionEvent`` | ref | missing |

## `AgeConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 115
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::AgeConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/AgeConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `maximum` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `minimum` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `scope` | ``TimingDescriptionEvent`` | ref | missing |

## `ExecutionOrderConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 118
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `baseComposition` | ``CompositionSw ComponentType`` | ref | missing |
| — *(missing)* | `—` | `executionOrderConstraintType` | ``ExecutionOrder ConstraintTypeEnum`` | attr | missing |
| — *(missing)* | `—` | `ignoreOrderAllowed` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `isEvent` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `orderedElement` | ``EOCExecutableEntity RefAbstract`` | aggr | missing |
| — *(missing)* | `—` | `permitMultipleReferencesToEE` | ``Boolean`` | attr | missing |

## `EOCExecutableEntityRefAbstract`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 119  | **table:** Table 3.70
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `directSuccessor` | ``EOCExecutableEntity RefAbstract`` | ref | missing |

## `EOCExecutableEntityRefGroup`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 119
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `letDataExchangeParadigm` | ``LetDataExchange ParadigmEnum`` | attr | missing |
| — *(missing)* | `—` | `letInterval` | ``TimingDescriptionEvent Chain`` | ref | missing |
| — *(missing)* | `—` | `maxCycleRepetitions` | ``PositiveInteger`` | attr | missing |

## `EOCEventRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 120
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bswModuleInstance` | ``BswImplementation`` | ref | missing |
| — *(missing)* | `—` | `component` | ``SwComponent Prototype`` | iref | missing |
| — *(missing)* | `—` | `successor` | ``EOCExecutableEntity RefAbstract`` | ref | missing |

## `EOCExecutableEntityRef`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 120  | **table:** Table 3.72
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `bswModuleInstance` | ``BswImplementation`` | ref | missing |
| — *(missing)* | `—` | `component` | ``SwComponent Prototype`` | iref | missing |
| — *(missing)* | `—` | `executable` | ``ExecutableEntity`` | ref | missing |

## `ExecutionTimeConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 130  | **table:** Table 3.75
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `component` | ``SwComponent Prototype`` | iref | missing |
| — *(missing)* | `—` | `executable` | ``ExecutableEntity`` | ref | missing |
| — *(missing)* | `—` | `executionTimeType` | ``ExecutionTimeType Enum`` | attr | missing |
| — *(missing)* | `—` | `maximum` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `minimum` | ``MultidimensionalTime`` | aggr | missing |

## `SynchronizationPointConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 132
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationPointConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationPointConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `sourceEec` | ``EOCExecutableEntity RefGroup`` | ref | missing |
| — *(missing)* | `—` | `sourceEvent` | ``AbstractEvent`` | ref | missing |
| — *(missing)* | `—` | `targetEec` | ``EOCExecutableEntity RefGroup`` | ref | missing |
| — *(missing)* | `—` | `targetEvent` | ``AbstractEvent`` | ref | missing |

## `TDLETZoneClock`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 252
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock::TDLETZoneClock`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TDLETZoneClock.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `accuracyExt` | ``MultidimensionalTime`` | aggr | missing |
| — *(missing)* | `—` | `accuracyInt` | ``MultidimensionalTime`` | aggr | missing |

## `TimingClock`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 252
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock::TimingClock`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClock.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `platformTimeBase` | ``GlobalTimeDomain`` | ref | missing |

## `TimingClockSyncAccuracy`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 252
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock::TimingClockSyncAccuracy`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClockSyncAccuracy.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `lower` | ``TimingClock`` | ref | missing |
| — *(missing)* | `—` | `upper` | ``TimingClock`` | ref | missing |

## `TimingConstraint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 253
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::TimingConstraint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingConstraint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingCondition` | ``TimingCondition`` | ref | missing |

## `TimingExtension`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** 254
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::TimingExtensions`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingExtensions.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `timingClock` | ``TimingClock`` | aggr | missing |
| — *(missing)* | `—` | `timingClockSyncAccuracy` | ``TimingClockSync Accuracy`` | aggr | missing |
| — *(missing)* | `—` | `timingCondition` | ``TimingCondition`` | aggr | missing |

## `PortPrototypeBlueprint`
- **PDF:** `AUTOSAR_CP_TPS_TimingExtensions.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::PortPrototypeBlueprint`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintDedicated/PortPrototypeBlueprint.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `initValue` | ``PortPrototypeBlueprint InitValue`` | aggr | missing |
| — *(missing)* | `—` | `providedComSpec` | ``PPortComSpec`` | aggr | missing |
| — *(missing)* | `—` | `requiredComSpec` | ``RPortComSpec`` | aggr | missing |

## `ApplicationDeferredDataType`
- **PDF:** `AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::AbstractPlatform::ApplicationDeferredDataType`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform/ApplicationDeferredDataType.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `MsrQueryChapter`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 343
- **Package:** `M2::MSR::Documentation::Chapters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Chapters.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `msrQueryResultChapter` | ``MsrQueryResult Chapter`` | aggr | missing |

## `MsrQueryTopic1`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 343  | **table:** Table 9.84
- **Package:** `M2::MSR::Documentation::Chapters`
- **Source:** `src/armodel/models/M2/MSR/Documentation/Chapters.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `msrQueryResultTopic1` | ``MsrQueryResultTopic1`` | aggr | missing |

## `BlueprintMappingSet`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 48
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintMapping::BlueprintMappingSet`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintMapping/BlueprintMappingSet.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `blueprintMap` | ``AtpBlueprintMapping`` | aggr | missing |

## `MultiLanguageParagraph`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 290
- **Package:** `M2::MSR::Documentation::TextModel::MultilanguageData`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `helpEntry` | ``String`` | attr | missing |

## `Map`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 305
- **Package:** `M2::MSR::Documentation::BlockElements::Figure`
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `area` | ``Area`` | aggr | missing |
| — *(missing)* | `—` | `class` | ``String`` | attr | missing |
| — *(missing)* | `—` | `name` | ``NameToken`` | attr | missing |
| — *(missing)* | `—` | `onclick` | ``String`` | attr | missing |
| — *(missing)* | `—` | `ondblclick` | ``String`` | attr | missing |

## `MlFigure`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 307  | **table:** Table 9.24
- **Package:** `M2::MSR::Documentation::BlockElements::Figure`
- **Source:** `src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `frame` | ``FrameEnum`` | attr | missing |
| `lGraphics` | `List[LGraphic]` | `lGraphic` | ``LGraphic`` | aggr | naming |

## `Traceable`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 312  | **table:** Table 9.29
- **Package:** `M2::AUTOSARTemplates::CommonStructure::Timing::Traceable`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/Traceable.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `trace` | ``Traceable`` | ref | missing |

## `DocumentViewSelectable`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** 340  | **table:** Table 9.78
- **Package:** `M2::MSR::Documentation::TextModel::BlockElements::PaginationAndView`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/BlockElements/PaginationAndView.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `si` | ``NameTokens`` | attr | missing |
| — *(missing)* | `—` | `view` | ``ViewTokens`` | attr | missing |

## `MsrQueryP1`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —  | **table:** Table 9.82
- **Package:** `M2::MSR::Documentation::TextModel::MsrQuery`
- **Source:** `src/armodel/models/M2/MSR/Documentation/TextModel/MsrQuery.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `msrQueryProps` | ``MsrQueryProps`` | aggr | missing |
| — *(missing)* | `—` | `msrQueryResultP1` | ``TopicContent`` | aggr | missing |

## `AtpBlueprintable`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AtpClassifier`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —  | **table:** Table 5.1
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `atpFeature` | ``AtpFeature`` | aggr | missing |

## `AtpFeature`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —  | **table:** Table 5.3
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AtpType`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AtpPrototype`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —  | **table:** Table 5.4
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `atpType` | ``AtpType`` | ref | missing |

## `AtpStructureElement`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —  | **table:** Table 5.6
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `AtpDefinition`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::RolesAndRights::AtpDefinition`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/RolesAndRights/AtpDefinition.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `ARObject`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ArObject`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `checksum` | ``String`` | attr | missing |
| — *(missing)* | `—` | `timestamp` | ``DateTime`` | attr | missing |

## `CollectableElement`
- **PDF:** — *(no spec counterpart)*
- **Package:** `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — | — | — | — | — | internal helper class (no AUTOSAR meta-class) |

- **Note:** `CollectableElement` is a py-armodel internal abstract base that provides collection/lookup management (`elements`, `element_mappings`, `getElement`/`addElement`/`removeElement`/`getTotalElement`/`IsElementExists`) for classes such as `Identifiable` and `ARElement`. It does not correspond to any AUTOSAR meta-class and is deliberately kept as-is (per 2026-08-20 decision; NO `# Spec verified` stamp).

## `FileInfoComment`
- **PDF:** `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::AutosarTopLevelStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| `sdgs` | `List[Sdg]` | `sdg` | ``Sdg`` | aggr | naming |

## `CryptoKeySlot`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 57
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::CryptoDeployment::CryptoKeySlot`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/CryptoKeySlot.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `allocateShadowCopy` | ``Boolean`` | attr | missing |
| — *(missing)* | `—` | `cryptoAlgId` | ``String`` | attr | missing |

## `IdsPlatformInstantiation`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 63
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem::IdsPlatformInstantiation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsPlatformInstantiation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `networkInterface` | ``PlatformModule EthernetEndpoint Configuration`` | ref | missing |
| — *(missing)* | `—` | `timeBase` | ``TimeBaseResource`` | ref | missing |

## `IdsmModuleInstantiation`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 63
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem::IdsmModuleInstantiation`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsmModuleInstantiation.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `-` | ``-`` | - | missing |

## `PlatformModuleEthernetEndpointConfiguration`
- **PDF:** `AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf`  | **page:** 65
- **Package:** `M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::AdaptiveModule::PlatformModuleEthernetEndpointConfiguration`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/AdaptiveModule/PlatformModuleEthernetEndpointConfiguration.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `communicationConnector` | ``EthernetCommunication Connector`` | ref | missing |
| — *(missing)* | `—` | `ipv4MulticastIpAddress` | ``Ip4AddressString`` | attr | missing |
| — *(missing)* | `—` | `ipv6MulticastIpAddress` | ``Ip6AddressString`` | attr | missing |

## `AtpBlueprintMapping`
- **PDF:** `AUTOSAR_FO_TPS_StandardizationTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::GenericStructure::AbstractStructure`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `atpBlueprint` | ``AtpBlueprint`` | ref | missing |
| — *(missing)* | `—` | `atpBlueprintedElement` | ``AtpBlueprintable`` | ref | missing |

## `KeywordSet`
- **PDF:** `AUTOSAR_FO_TPS_StandardizationTemplate.pdf`  | **page:** —
- **Package:** `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Keyword`
- **Source:** `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/Keyword.py`

| Name in source code | Type (source) | Member name (spec) | Type (PDF) | Kind | Deviation |
|---|---|---|---|---|---|
| — *(missing)* | `—` | `keyword` | ``Keyword`` | aggr | missing |

## Appendix: classes without a spec attribute table

- `ChapterContent` (`M2::MSR::Documentation::Chapters`)
- `TopicContent` (`M2::MSR::Documentation::Chapters`)
- `TopicContentOrMsrQuery` (`M2::MSR::Documentation::Chapters`)
- `GraphicFitEnum` (`M2::MSR::Documentation::BlockElements::Figure`)
- `LOverviewParagraph` (`M2::MSR::Documentation::TextModel::LanguageDataModel`)
- `LParagraph` (`M2::MSR::Documentation::TextModel::LanguageDataModel`)
- `LPlainText` (`M2::MSR::Documentation::TextModel::LanguageDataModel`)
- `LVerbatim` (`M2::MSR::Documentation::TextModel::LanguageDataModel`)
- `ListEnum` (`M2::MSR::Documentation::TextModel::BlockElements::ListElements`)
- `ARList` (`M2::MSR::Documentation::TextModel::BlockElements::ListElements`)
- `SingleLanguageUnitNames` (`M2::MSR::AsamHdo::Units`)
- `SwValues` (`M2::MSR::CalibrationData::CalibrationValue`)
- `ValueList` (`M2::MSR::DataDictionary::DataDefProperties`)
- `AxisIndexType` (`M2::MSR::DataDictionary::RecordLayout`)
- `SwRecordLayoutGroupContent` (`M2::MSR::DataDictionary::RecordLayout`)
- `EcucScopeEnum` (`M2::AUTOSARTemplates::ECUCParameterDefTemplate`)
- `EcucDestinationUriDefRefType` (`M2::AUTOSARTemplates::ECUCParameterDefTemplate`)
- `EcucConfigurationClassEnum` (`M2::AUTOSARTemplates::ECUCParameterDefTemplate`)
- `EcucSymbolicNameReferenceDef` (`M2::AUTOSARTemplates::ECUCParameterDefTemplate`)
- `EcucLinkerSymbolDef` (`M2::AUTOSARTemplates::ECUCParameterDefTemplate`)
- `PduToFrameMapping` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication`)
- `CycleRepetitionType` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `FlexrayChannelName` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `CommunicationCluster` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `AbstractCanCluster` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `CanCluster` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `LinCluster` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `CommunicationController` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `PncGatewayTypeEnum` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `CommunicationDirectionType` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `IPduSignalProcessingEnum` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology`)
- `SocketConnectionIpduIdentifier` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetCommunication`)
- `SocketConnectionBundle` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetCommunication`)
- `EthernetCluster` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`)
- `EthernetCommunicationController` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`)
- `SdClientConfig` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology`)
- `SdServerConfig` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances`)
- `AbstractCanCommunicationController` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`)
- `CanCommunicationController` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology`)
- `FlexrayCommunicationController` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology`)
- `FlexrayCluster` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology`)
- `ResumePosition` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication`)
- `LinCommunicationController` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology`)
- `LinMaster` (`M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology`)
- `DataTransformationKindEnum` (`M2::AUTOSARTemplates::SystemTemplate::Transformer`)
- `DataIdModeEnum` (`M2::AUTOSARTemplates::SystemTemplate::Transformer`)
- `EndToEndProfileBehaviorEnum` (`M2::AUTOSARTemplates::SystemTemplate::Transformer`)
- `TransformationISignalProps` (`M2::AUTOSARTemplates::SystemTemplate::Transformer`)
- `EndToEndTransformationISignalProps` (`M2::AUTOSARTemplates::SystemTemplate::Transformer`)
- `HandleInvalidEnum` (`M2::AUTOSARTemplates::SWComponentTemplate::Communication`)
- `NumericalValueVariationPoint` (`M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints`)
- `AutoCollectEnum` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Enumerations`)
- `BindingTimeEnum` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Enumerations`)
- `XmlSpaceEnum` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Enumerations`)
- `ARType` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `ARNumerical` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `ARFloat` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `Float` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `TimeValue` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `ARLiteral` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `AREnum` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `AlignmentType` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `CseCodeType` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `ReferrableSubtypesEnum` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `ARPositiveInteger` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `ARBoolean` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `NameToken` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `PositiveInteger` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `PositiveUnlimitedInteger` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `Integer` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `UnlimitedInteger` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `Boolean` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `CIdentifier` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `RevisionLabelString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `Limit` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `RefType` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `TRefType` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `DiagRequirementIdString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `Ip4AddressString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `Ip6AddressString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `MacAddressString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `CategoryString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `DateTime` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `VerbatimString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `VerbatimStringPlain` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `RegularExpression` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `SymbolString` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `McdIdentifier` (`M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`)
- `BswEntryKindEnum` (`M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`)
- `BswCallType` (`M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`)
- `BswExecutionContext` (`M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`)
- `SwServiceImplPolicyEnum` (`M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`)
- `BswEntryRelationshipEnum` (`M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`)
- `BswInterruptCategory` (`M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`)
- `BswApiOptions` (`M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`)
- `AbstractAUTOSAR` (`M2::AUTOSARTemplates::AutosarTopLevelStructure`)
- `AUTOSARDoc` (`M2::AUTOSARTemplates::AutosarTopLevelStructure`)
- `CryptoKeySlotContent` (`M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::CryptoDeployment::CryptoKeySlotContent`)
- `DataFilterTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::Filter`)
- `DependencyUsageEnum` (`M2::AUTOSARTemplates::CommonStructure::Implementation`)
- `ProgramminglanguageEnum` (`M2::AUTOSARTemplates::CommonStructure::Implementation`)
- `ArrayImplPolicyEnum` (`M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`)
- `ArraySizeSemanticsEnum` (`M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`)
- `ReentrancyLevelEnum` (`M2::AUTOSARTemplates::CommonStructure::InternalBehavior`)
- `ApiPrincipleEnum` (`M2::AUTOSARTemplates::CommonStructure::InternalBehavior`)
- `ModeActivationKind` (`M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`)
- `ModeErrorReactionPolicyEnum` (`M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`)
- `RamBlockStatusControlEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `NvBlockNeedsReliabilityEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `NvBlockNeedsWritingPriorityEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `ServiceDiagnosticRelevanceEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DiagnosticAudienceEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DiagnosticServiceRequestCallbackTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DiagnosticRoutineTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DiagnosticValueAccessEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DiagnosticProcessingStyleEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DtcKindEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DiagnosticClearDtcNotificationEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DtcFormatTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `DiagnosticDenominatorConditionEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `ObdRatioConnectionKindEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `PossibleErrorReaction` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `VerificationStatusIndicationModeEnum` (`M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`)
- `RteEventInEcuInstanceRef` (`M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`)
- `VariableAccessInEcuInstanceRef` (`M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`)
- `TimingConditionFormula` (`M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingConditionFormula`)
- `ExecutionOrderConstraintTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`)
- `LetDataExchangeParadigmEnum` (`M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint`)
- `ExecutionTimeTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint`)
- `LatencyConstraintTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint`)
- `SynchronizationTypeEnum` (`M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming`)
- `EventOccurrenceKindEnum` (`M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming`)
- `HwPinGroupContent` (`M2::AUTOSARTemplates::EcuResourceTemplate`)
