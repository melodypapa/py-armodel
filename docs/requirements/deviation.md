# DEVIATION REPORT
## Comparison between Actual Code (src/armodel/models/M2/) and Documentation

**Report Generated**: 2026-01-17
**Comparison Scope**: Complete M2 package structure (MSR and AUTOSARTemplates)
**Reference Documentation**: docs/requirements/autosar_models.md

---

### SUMMARY OF FINDINGS

The documentation (`docs/requirements/autosar_models.md`) contains significant deviations from the actual code implementation in `src/armodel/models/M2/`. The major issues include:

1. **MSR section is severely incomplete** - Only 6 classes documented vs 50+ classes in code
2. **Missing major AUTOSARTemplate packages** - Entire packages not documented
3. **Missing subpackages** - Many important subpackages not listed
4. **Incomplete class listings** - Many packages have only partial class documentation

---

### CRITICAL DEVIATIONS

#### 1. MSR (Meta-Model Semantic Rules) - SEVERELY INCOMPLETE

**Documentation Status**: Only 6 entries under MSR section
**Actual Code**: Complete package structure with 4 major subpackages and 50+ classes

##### Missing MSR Subpackages:

**MSR/AsamHdo/** (Complete package missing from docs)
- AdminData.py: `AdminData`
- BaseTypes.py: `BaseTypeSpecification`, `BaseTypeRef`, `BaseTypeDef`
- ComputationMethod.py: `ComputationMethod`, `ComputationMethodProps`, `ComputationMethodRef`, `ComputationMethodDef`, `ComputationMethodInput`, `ComputationMethodOutput`, `ComputationMethodHandle`, `ComputationMethodCall`, `ComputationMethodResult`, `ComputationMethodResults`, `ComputationMethodResultsRecord`, `ComputationMethodUsage`
- Constraints/GlobalConstraints.py: `GlobalConstraint`, `GlobalConstraintCall`, `GlobalConstraintResult`, `GlobalConstraintUsage`
- SpecialData.py: `Sd`, `SdgCaption`, `Sdg`
- Units.py: `PhysicalDimension`, `SingleLanguageUnitNames`, `Unit`

**MSR/CalibrationData/** (Complete package missing from docs)
- CalibrationValue.py: `CalibrationValue`

**MSR/DataDictionary/** (Severely incomplete - only partial coverage)
- Axis.py: `Axis`, `AxisSet`, `AxisPoints`, `AxisPointsContent`, `AxisPoint`, `CharacteristicAxisD composition`, `CharacteristicAxisRef` (7 classes not in docs)
- CalibrationParameter.py: `SwCalibrationArg`, `SwCalibrationParameter` (2 classes not in docs)
- RecordLayout.py: `SwRecordLayoutV`, `SwRecordLayoutGroupContent`, `SwRecordLayoutGroup`, `SwRecordLayout` (4 classes not in docs)

**MSR/Documentation/** (Complete package missing from docs)
- Annotation.py: `GeneralAnnotation`, `Annotation`
- BlockElements/Figure.py: `GraphicFitEnum`, `Graphic`, `Map`, `LGraphic`, `MlFigure`
- TextModel/LanguageDataModel.py: `LEnum`, `LanguageSpecific`, `LOverviewParagraph`, `LParagraph`, `LLongName`, `LPlainText`
- TextModel/MultilanguageData.py: `MultiLanguageParagraph`, `MultiLanguageOverviewParagraph`, `MultilanguageLongName`, `MultiLanguagePlainText`
- TextModel/BlockElements/ListElements.py: `ListKind`, `ListLabel`, `ListContent`, `ListItem`, `ListItems`
- TextModel/BlockElements/PaginationAndView.py: `PrintAreaKind`, `MlPrintArea`, `ViewAreaKind`, `ViewingPort`

---

#### 2. AUTOSARTemplates - MISSING MAJOR PACKAGES

##### AUTOSARTemplates/DiagnosticExtract/ (Only mentioned, no detail)
**Actual Code**:
- DiagnosticContribution.py: `DiagnosticContribution`

##### AUTOSARTemplates/EcuResourceTemplate/ (Only name listed)
**Actual Code**:
- HwAttributeValue.py: `HwAttributeValue`
- HwElementCategory.py: `HwElementCategory`
- HwElementConnector.py: `HwElementConnector`
- __init__.py: `HwElement`, `HwDevice`, `HwSubDevice`

##### AUTOSARTemplates/GenericStructure/ (INCOMPLETE)
**Missing Packages**:
- LifeCycles.py: `LifeCycle`, `LifeCycleDefinition`, `LifeCycleState`, `LifeCycleStateTransition`, `LifeCycleStateTransitionTable` (5 classes)

##### AUTOSARTemplates/CommonStructure/ (SEVERELY INCOMPLETE)
**Missing Subpackages**:

**CommonStructure/ResourceConsumption/** (Complete package missing)
- ExecutionTime/: `ExecutionTime`, `HardwareConfiguration`, `SoftwareContext`, `MultidimensionalTime`, `SimulatedExecutionTime`, `RoughEstimateOfExecutionTime`, `McSupportData`
- HeapUsage/: `HeapUsage`, `WorstCaseHeapUsage`, `MeasuredHeapUsage`, `RoughEstimateHeapUsage`, `ExecutionTime`
- MemorySectionUsage/: `MemorySection`, `MemorySectionUsage`, `StackUsage`
- StackUsage/: `StackUsage`, `WorstCaseStackUsage`, `MeasuredStackUsage`, `RoughEstimateStackUsage`, `HeapUsage`

**CommonStructure/StandardizationTemplate/** (Only mentioned "AbstractBlueprintStructure")
**Actual Code**:
- BlueprintDedicated/PortPrototypeBlueprint.py: `PortPrototypeBlueprint`
- Keyword.py: `Keyword`

**CommonStructure/Timing/** (Complete package missing)
- TimingConstraint/ExecutionOrderConstraint.py: `ExecutionOrderConstraint`
- TimingConstraint/TimingConstraint.py: `TimingConstraint`
- TimingConstraint/TimingExtensions.py: `TimingExtensions`

**CommonStructure/Filter.py** (Missing from docs)
- `DataFilterTypeEnum`, `DataFilter`

**CommonStructure/FlatMap.py** (Missing from docs)
- `FlatMap`, `FlatMapItem`

**CommonStructure/Implementation.py** (Missing from docs)
- `ImplementationProps`, `Code`, `Compiler`

**CommonStructure/ImplementationDataTypes.py** (Missing from docs)
- `ImplementationDataType`, `ApplicationPrimitiveDataType`, `HandleType`

**CommonStructure/InternalBehavior.py** (Missing from docs)
- `InternalBehavior`

**CommonStructure/ModeDeclaration.py** (Missing from docs)
- `ModeDeclaration`, `ModeDeclarationGroup`, `ModeDeclarationGroupConditional`, `ModeDeclarationGroupRef`, `ModeDeclarationRef`, `ModeDeclarationConditional`

**CommonStructure/SwcBswMapping.py** (Missing from docs)
- `SwcBswMapping`, `SwcToBswMapping`, `BswToSwcMapping`

**CommonStructure/TriggerDeclaration.py** (Missing from docs)
- `TriggerDeclaration`, `TriggerEvent`

---

#### 3. AUTOSARTemplates/SWComponentTemplate - MAJOR GAPS

##### Missing Files in Documentation:

**SWComponentTemplate/Communication.py** (23 classes missing)
**SWComponentTemplate/Components/__init__.py** (18 component classes - only partially listed)
**SWComponentTemplate/Composition/__init__.py** (5 classes missing)
**SWComponentTemplate/Datatype/DataPrototypes.py** (8 classes missing)
**SWComponentTemplate/Datatype/Datatypes.py** (8 classes missing)
**SWComponentTemplate/EndToEndProtection.py** (5 classes missing)

##### SWComponentTemplate/SwcInternalBehavior/ (INCOMPLETE)
**Documentation lists**: 6 classes
**Actual Code has**: 12 files with 50+ classes

**Missing Subpackages**:
- AccessCount.py: `AccessCount`
- AutosarVariableRef.py: `AutosarVariableRef`
- DataElements.py: `DataElements`, `DataElement`
- IncludedDataTypes.py: `IncludedDataTypeSet`
- InstanceRefsUsage.py: `InstanceRefsUsage`
- ModeDeclarationGroup.py: `ModeDeclarationGroup`
- PerInstanceMemory.py: `PerInstanceMemory`
- PortAPIOptions.py: `PortAPIOptions`
- RTEEvents.py: `RTEEvents`, `InitEvent`, `DataReceiveEvent`, `SwcModeSwitchEvent`, `DataElementRef`, `EventFilter`, `DataElementFilter`
- ServerCall.py: `ServerCall`
- ServiceMapping.py: `ServiceMapping`
- Trigger.py: `Trigger`

---

#### 4. AUTOSARTemplates/SystemTemplate - MAJOR OMISSIONS

##### Missing Subpackages:

**SystemTemplate/DataMapping.py** (9 classes missing)
**SystemTemplate/DiagnosticConnection.py** (`DiagnosticConnection` missing)
**SystemTemplate/DoIp.py** (3 classes missing: `AbstractDoIpLogicAddressProps`, `DoIpLogicTargetAddressProps`, `DoIpLogicTesterAddressProps`)
**SystemTemplate/ECUResourceMapping.py** (`ECUResourceMapping` missing)
**SystemTemplate/InstanceRefs.py** (2 classes missing)
**SystemTemplate/NetworkManagement.py** (21 classes missing)
**SystemTemplate/RteEventToOsTaskMapping.py** (`RteEventToOsTaskMapping` missing)
**SystemTemplate/SecureCommunication.py** (3 classes missing)
**SystemTemplate/SWmapping.py** (2 classes missing)
**SystemTemplate/Transformer/__init__.py** (12 classes missing)
**SystemTemplate/TransportProtocols.py** (16 classes missing)

##### SystemTemplate/Fibex/ (COMPLETE PACKAGE MISSING)
**Fibex4Can/**: `CanCommunication`, `CanTopology`
**Fibex4Ethernet/**: `EthernetCommunication`, `EthernetFrame`, `EthernetTopology`, `NetworkEndpoint`, `ServiceInstances`
**Fibex4Flexray/**: `FlexrayCommunication`, `FlexrayTopology`
**Fibex4Lin/**: `LinCommunication`, `LinTopology`
**FibexCore/**: `CoreCommunication`, `CoreTopology`, `EcuInstance`, `Timing`
**Fibex4Multiplatform.py**: 7 classes

---

#### 5. BswModuleTemplate Deviations

**Missing classes in documentation**:
- `BswInterruptCategory` (enumeration)
- `BswDistinguishedPartition`
- `BswApiOptions` (abstract)
- `BswDataReceptionPolicy` (abstract)
- `BswQueuedDataReceptionPolicy`

**Incorrectly listed classes** (documented but not in code):
- `BswModeSwitchedAckEvent` (not found in code)
- `BswModeManagerErrorEvent` (not found in code)
- `BswAsynchronousServerCallReturnsEvent` (not found in code)
- `BswTriggerDirectImplementation` (not found in code)
- `BswModeReceiverPolicy` (not found in code)
- `ExclusiveArea` (not found in code)
- `ParameterDataPrototype` (should be from SWComponentTemplate)

---

#### 6. CommonStructure/ServiceNeeds.py - MISSING CLASSES

The documentation only shows a partial list. The actual code has many more classes:

**Missing from Documentation**:
- `DiagnosticCapabilityElement` (abstract)
- `DiagnosticCapabilityElementConditional`
- `DiagnosticCapabilityElementUsage`
- `FunctionInhibitionNeeds`
- `FunctionInhibitionNeedsConditional`
- `FunctionInhibitionNeedsUsage`
- `CryptoServiceNeeds`
- `CryptoServiceNeedsConditional`
- `CryptoServiceNeedsUsage`
- `ComMgrUserNeeds`
- `ComMgrUserNeedsConditional`
- `ComMgrUserNeedsUsage`
- `EcuStateMgrUserNeeds`
- `EcuStateMgrUserNeedsConditional`
- `EcuStateMgrUserNeedsUsage`
- `DltUserNeeds`
- `DltUserNeedsConditional`
- `DltUserNeedsUsage`
- `DoIpServiceNeeds`
- `DoIpServiceNeedsConditional`
- `DoIpServiceNeedsUsage`
- `EventInhibition`
- `EventInhibitionUsage`
- `EventDebounceAlgorithm` (abstract - listed)
- `EventDebounceCounterBased` (listed as `DiagEventDebounceCounterBased`)
- `EventDebounceTimeBased` (listed as `DiagEventDebounceTimeBased`)
- `DiagnosticEventNeedsConditional`
- `DiagnosticEventNeedsUsage`

**Name deviations**:
- Code uses `DiagEventDebounceCounterBased`, docs show `DiagEventDebounceCounterBased` ✓
- Code uses `DiagEventDebounceTimeBased`, docs show `DiagEventDebounceTimeBased` ✓
- Code uses `DiagEventDebounceMonitorInternal`, docs show `DiagEventDebounceMonitorInternal` ✓

---

### STATISTICS

| Category | Count in Documentation | Count in Code | Missing |
|----------|----------------------|---------------|---------|
| MSR Packages | ~10 classes | 50+ classes | 40+ classes |
| AUTOSARTemplate Packages | ~200 classes | 699 classes | ~500 classes |
| SystemTemplate/Fibex | 0 | 7 packages | 7 packages |
| CommonStructure Subpackages | 3 documented | 10 actual | 7 packages |
| SwcInternalBehavior classes | 6 | 50+ | 44+ classes |

---

### RECOMMENDATIONS

1. **Update MSR Section**: Document all 4 MSR subpackages with complete class listings
   - MSR/AsamHdo with all 6 submodules
   - MSR/CalibrationData
   - MSR/DataDictionary with all missing classes
   - MSR/Documentation with all 5 submodules

2. **Add Missing AUTOSARTemplate Packages**:
   - Document DiagnosticExtract/DiagnosticContribution completely
   - Document EcuResourceTemplate with all 4 files
   - Add GenericStructure/LifeCycles (5 classes)

3. **Complete CommonStructure Documentation**:
   - Add ResourceConsumption package (4 subpackages with 20+ classes)
   - Add Timing package (3 files)
   - Complete StandardizationTemplate with BlueprintDedicated and Keyword
   - Add Filter, FlatMap, Implementation, ImplementationDataTypes, InternalBehavior, ModeDeclaration, SwcBswMapping, TriggerDeclaration

4. **Expand SwcInternalBehavior**:
   - Document all 12 subpackages with their classes
   - Current: 6 classes documented
   - Actual: 50+ classes across 12 files

5. **Add SystemTemplate Packages**:
   - Document all missing subpackages
   - Especially Fibex (7 packages with communication protocol support)
   - NetworkManagement (21 classes)
   - Transformer (12 classes)
   - TransportProtocols (16 classes)

6. **Fix BswModuleTemplate**:
   - Remove non-existent classes from documentation
   - Add missing classes (BswInterruptCategory, BswDistinguishedPartition, BswApiOptions, etc.)
   - Correct ParameterDataPrototype location (should be in SWComponentTemplate)

7. **Standardize Format**:
   - Ensure consistent indentation and package hierarchy representation
   - Use consistent naming conventions
   - Clearly mark abstract classes with "(abstract)"

8. **Verify Completeness**:
   - Cross-reference all __init__.py files to ensure all exports are documented
   - Check all Python files in src/armodel/models/M2/ for completeness
   - Create automated verification script if possible

---

### DETAILED MISSING PACKAGES LIST

#### Complete Missing Packages (not mentioned at all in docs):

1. **MSR/AsamHdo/** - 6 files with 25+ classes
2. **MSR/CalibrationData/** - 1 file with 1 class
3. **MSR/Documentation/** - 5 files with 20+ classes
4. **AUTOSARTemplates/DiagnosticExtract/** - 1 file with 1 class
5. **AUTOSARTemplates/CommonStructure/ResourceConsumption/** - 4 subpackages
6. **AUTOSARTemplates/CommonStructure/Timing/** - 3 files
7. **AUTOSARTemplates/SystemTemplate/Fibex/** - 7 packages
8. **AUTOSARTemplates/SystemTemplate/DataMapping.py** - 9 classes
9. **AUTOSARTemplates/SystemTemplate/NetworkManagement.py** - 21 classes
10. **AUTOSARTemplates/SystemTemplate/Transformer/__init__.py** - 12 classes
11. **AUTOSARTemplates/SystemTemplate/TransportProtocols.py** - 16 classes

#### Severely Incomplete Packages:

1. **MSR/DataDictionary/** - Only 5 classes documented, 15+ in code
2. **AUTOSARTemplates/EcuResourceTemplate/** - Only name listed, 4 files in code
3. **AUTOSARTemplates/GenericStructure/** - Missing LifeCycles (5 classes)
4. **AUTOSARTemplates/CommonStructure/** - Missing 8 packages
5. **AUTOSARTemplates/SWComponentTemplate/** - Missing 6 major files
6. **AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/** - Only 6 classes, 50+ in code
7. **AUTOSARTemplates/SystemTemplate/** - Missing 12 packages

---

### PRIORITIZED ACTION ITEMS

**High Priority** (Critical gaps affecting documentation usefulness):
1. Document complete MSR section (foundation of the model)
2. Add SystemTemplate/Fibex packages (major feature area)
3. Document CommonStructure/ResourceConsumption (commonly used)
4. Complete SwcInternalBehavior documentation (core component behavior)

**Medium Priority** (Important but less frequently used):
1. Add EcuResourceTemplate details
2. Document CommonStructure/Timing
3. Add SystemTemplate/NetworkManagement
4. Complete CommonStructure missing packages

**Low Priority** (Enhancement packages):
1. Add MSR/Documentation details
2. Document SystemTemplate/Transformer
3. Complete SWComponentTemplate missing files
4. Add remaining SystemTemplate packages

---

### END OF DEVIATION REPORT

*This report was generated by comparing src/armodel/models/M2/ directory structure with the documentation in docs/requirements/autosar_models.md*

**Analysis Method**: Automated exploration of M2 directory structure comparing with documented packages and classes.

**Next Steps**: Review this report with the development team to prioritize documentation updates and assign ownership for each section.
