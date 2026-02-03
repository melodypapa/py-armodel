# Package Implementation Comparison Report

This report compares AUTOSAR M2 package requirements with actual Python implementations.

## Overall Summary

- **Total Packages**: 257

### Classes
- **Required**: 1623
- **Implemented**: 504
- **Missing**: 1119
- **Extra**: 432

### Enumerations
- **Required**: 264
- **Implemented**: 48
- **Missing**: 216
- **Extra**: 30
- **Literal Mismatches**: 38

### Overall Status
**❌ Incomplete**

## Legend

- ✅ Implemented: Class/enum is implemented and matches requirements
- ❌ Missing: Class/enum is required but not found in implementation
- ⚠️ Literal Mismatch: Enum exists but has different literal values
- ➕ Extra: Class/enum exists in implementation but not in requirements

## Packages with Problems

**Total packages with issues**: 210 out of 257

### M2::AUTOSARTemplates::AutosarTopLevelStructure

- **M2::AUTOSARTemplates::AutosarTopLevelStructure**: 2 missing classes

### M2::AUTOSARTemplates::BswModuleTemplate

- **M2::AUTOSARTemplates::BswModuleTemplate::BswOverview**: 1 missing classes
- **M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces**: 4 literal mismatches

### M2::AUTOSARTemplates::CommonStructure

- **M2::AUTOSARTemplates::CommonStructure::ModeDeclaration**: 1 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::InternalBehavior**: 1 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::Implementation**: 2 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::ResourceConsumption**: 1 missing classes
- **M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime**: 6 missing classes
- **M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport**: 4 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::ServiceNeeds**: 14 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::Constants**: 23 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure**: 6 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Port**: 2 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Generic**: 1 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::ClientServerInterfaceToBsw**: 2 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint**: 2 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common**: 4 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data**: 23 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange**: 3 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintFormula**: 1 missing classes
- **M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Blueprint**: 1 missing classes
- **M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes**: 2 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation**: 1 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::Filter**: 1 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions**: 7 missing classes
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription**: 3 missing classes
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription**: 30 missing classes, 12 missing enums
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming**: 2 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint**: 1 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint**: 2 missing enums
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint**: 1 literal mismatches
- **M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster**: 3 missing classes

### M2::AUTOSARTemplates::DiagnosticExtract

- **M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics**: 17 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution**: 3 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonProps**: 1 missing classes, 3 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode**: 8 missing classes, 6 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent**: 8 missing classes, 5 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticMemoryDestination**: 3 missing classes, 4 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticExtendedDataRecord**: 1 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticFreezeFrame**: 1 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticCondition**: 3 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticDebouncingAlgorithm**: 1 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup**: 3 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticOperationCycle**: 1 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticAging**: 1 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticIndicator**: 1 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult**: 3 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm**: 5 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommonService**: 3 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CustomServiceInstance**: 1 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SessionControl**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SecurityAccess**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication**: 9 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset**: 2 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl**: 4 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ControlDTCSetting**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier**: 7 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::IOControl**: 3 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RoutineControl**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineDataIdentifier**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineData**: 2 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID**: 3 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent**: 3 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDTCInformation**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ClearDiagnosticInfo**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress**: 15 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RequestFileTransfer**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition**: 10 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x01_RequestCurrentPowertrain**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x02_RequestPowertrainFreeze**: 3 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x03_0x07_RequestEmission**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x04_ClearResetEmission**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x06_RequestOnBoard**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x08_RequestControlOfOnBoard**: 3 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x09_RequestVehicleInformation**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x0A_RequestEmissionRelated**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping**: 17 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping**: 8 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::FimMapping**: 2 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping**: 3 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster**: 4 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::Fim**: 6 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::DiagnosticExtract::J1939**: 4 missing classes
- **M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs**: 3 missing classes

### M2::AUTOSARTemplates::ECUCDescriptionTemplate

- **M2::AUTOSARTemplates::ECUCDescriptionTemplate**: 11 missing classes

### M2::AUTOSARTemplates::ECUCParameterDefTemplate

- **M2::AUTOSARTemplates::ECUCParameterDefTemplate**: 40 missing classes, 4 missing enums

### M2::AUTOSARTemplates::EcuResourceTemplate

- **M2::AUTOSARTemplates::EcuResourceTemplate**: 7 missing classes
- **M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory**: 1 missing classes

### M2::AUTOSARTemplates::FeatureModelTemplate

- **M2::AUTOSARTemplates::FeatureModelTemplate**: 17 missing classes, 1 missing enums

### M2::AUTOSARTemplates::GenericStructure

- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes**: 2 missing enums, 1 literal mismatches
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultidimensionalTime**: 1 missing classes
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage**: 2 missing classes
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable**: 2 missing classes
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::GeneralAnnotation**: 1 missing classes
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::TagWithOptionalValue**: 1 missing classes
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection**: 1 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef**: 12 missing classes
- **M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes**: 3 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::GenericStructure::BuildActionManifest**: 8 missing classes
- **M2::AUTOSARTemplates::GenericStructure::VariantHandling**: 11 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints**: 13 missing classes
- **M2::AUTOSARTemplates::GenericStructure::DocumentationOnM1**: 2 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::GenericStructure::ViewMapSet**: 2 missing classes
- **M2::AUTOSARTemplates::GenericStructure::FormulaLanguage**: 1 missing classes
- **M2::AUTOSARTemplates::GenericStructure::RolesAndRights**: 4 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::GenericStructure::LifeCycles**: 2 missing classes
- **M2::AUTOSARTemplates::GenericStructure::ImpositionTimes**: 1 missing classes

### M2::AUTOSARTemplates::LogAndTraceExtract

- **M2::AUTOSARTemplates::LogAndTraceExtract**: 7 missing classes

### M2::AUTOSARTemplates::SWComponentTemplate

- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior**: 2 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount**: 2 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping**: 1 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements**: 6 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::InstanceRefs**: 2 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents**: 5 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions**: 2 missing classes, 3 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::InstantiationDataDefProps**: 1 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::VariantHandling**: 1 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes**: 1 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario**: 7 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent**: 4 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::PortInterface**: 31 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::Components**: 18 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs**: 6 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation**: 1 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::Composition**: 8 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs**: 2 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::Communication**: 23 missing classes, 5 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes**: 10 missing classes, 5 missing enums
- **M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection**: 4 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior**: 3 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef**: 4 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine**: 3 missing classes
- **M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::CalibrationParameter**: 2 missing classes

### M2::AUTOSARTemplates::SecurityExtractTemplate

- **M2::AUTOSARTemplates::SecurityExtractTemplate**: 24 missing classes, 2 missing enums

### M2::AUTOSARTemplates::SystemTemplate

- **M2::AUTOSARTemplates::SystemTemplate**: 8 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection**: 3 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore**: 1 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology**: 2 missing classes, 1 literal mismatches
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication**: 41 missing classes, 11 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing**: 10 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology**: 68 missing classes, 16 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances**: 12 missing classes, 6 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds**: 25 missing classes, 7 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList**: 2 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet**: 2 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetFrame**: 3 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ObsoleteModel**: 2 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology**: 7 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication**: 1 missing classes, 3 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ttcan::TtcanTopology**: 4 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ttcan::TtcanCommunication**: 1 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology**: 3 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology**: 7 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication**: 12 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport**: 4 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster**: 17 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest**: 12 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::SecureCommunication**: 19 missing classes, 13 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::NetworkManagement**: 2 missing classes, 3 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Transformer**: 23 missing classes, 6 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef**: 4 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::DataMapping**: 3 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::EndToEndProtection**: 1 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::ECUResourceMapping**: 2 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::SWmapping**: 10 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping**: 5 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::SignalPaths**: 7 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::PncMapping**: 2 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::GeneralPurposeConnection**: 1 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::DoIP**: 3 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::TransportProtocols**: 19 missing classes, 4 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp**: 4 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv**: 4 missing classes, 9 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf**: 6 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::BusMirror**: 9 missing classes, 1 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::Dlt**: 2 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::GlobalTime**: 7 missing classes, 4 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::GlobalTime::CAN**: 3 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH**: 6 missing classes, 2 missing enums
- **M2::AUTOSARTemplates::SystemTemplate::GlobalTime::FR**: 3 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::GlobalTime::UserDefined**: 2 missing classes
- **M2::AUTOSARTemplates::SystemTemplate::InstanceRefs**: 3 missing classes

### M2::MSR::AsamHdo

- **M2::MSR::AsamHdo::ComputationMethod**: 1 missing classes
- **M2::MSR::AsamHdo::Constraints::GlobalConstraints**: 1 missing classes
- **M2::MSR::AsamHdo::SpecialData**: 2 missing classes
- **M2::MSR::AsamHdo::Units**: 2 missing classes

### M2::MSR::CalibrationData

- **M2::MSR::CalibrationData::CalibrationValue**: 2 missing classes

### M2::MSR::DataDictionary

- **M2::MSR::DataDictionary::ServiceProcessTask**: 1 missing enums
- **M2::MSR::DataDictionary::DataDefProperties**: 3 missing classes, 2 missing enums, 1 literal mismatches
- **M2::MSR::DataDictionary::AuxillaryObjects**: 2 missing enums
- **M2::MSR::DataDictionary::CalibrationParameter**: 1 missing enums
- **M2::MSR::DataDictionary::Axis**: 2 missing classes
- **M2::MSR::DataDictionary::DatadictionaryProxies**: 2 missing classes

### M2::MSR::Documentation

- **M2::MSR::Documentation::BlockElements**: 2 missing classes
- **M2::MSR::Documentation::BlockElements::RequirementsTracing**: 3 missing classes
- **M2::MSR::Documentation::BlockElements::Formula**: 1 missing classes
- **M2::MSR::Documentation::BlockElements::ListElements**: 7 missing classes, 2 missing enums
- **M2::MSR::Documentation::BlockElements::Figure**: 1 missing classes, 3 missing enums, 1 literal mismatches
- **M2::MSR::Documentation::BlockElements::Note**: 1 missing classes, 1 missing enums
- **M2::MSR::Documentation::BlockElements::PaginationAndView**: 2 missing classes, 2 missing enums
- **M2::MSR::Documentation::BlockElements::OasisExchangeTable**: 6 missing classes, 5 missing enums
- **M2::MSR::Documentation::BlockElements::GerneralParameters**: 1 missing classes
- **M2::MSR::Documentation::TextModel::MultilanguageData**: 1 missing classes
- **M2::MSR::Documentation::TextModel::LanguageDataModel**: 2 missing classes, 1 missing enums
- **M2::MSR::Documentation::TextModel::SingleLanguageData**: 4 missing classes
- **M2::MSR::Documentation::TextModel::InlineTextModel**: 6 missing classes
- **M2::MSR::Documentation::TextModel::InlineTextElements**: 9 missing classes
- **M2::MSR::Documentation::TextModel::InlineAttributeEnums**: 12 missing enums
- **M2::MSR::Documentation::Chapters**: 9 missing classes
- **M2::MSR::Documentation::MsrQuery**: 8 missing classes

## Package Details

### Package: M2::AUTOSARTemplates::BswModuleTemplate::BswOverview

**Summary:**
- Classes: 0/1 implemented, 1 missing, 1 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BswModuleDescription | - | Not found in implementation |
| ➕ Extra | ModeInBswModuleDescriptionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/InstanceRefs/ModeInBswModuleDescriptionInstanceRef.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::InstanceRefs

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InstanceRefs/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ModeInBswModuleDescriptionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/InstanceRefs/ModeInBswModuleDescriptionInstanceRef.py | Line 16 |

### Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces

**Summary:**
- Classes: 5/5 implemented, 5 extra
- Enums: 4/4 implemented, 4 literal mismatches, 1 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BswEntryRelationship | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 597 |
| ✅ Implemented | BswEntryRelationshipSet | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 649 |
| ✅ Implemented | BswModuleClientServerEntry | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 493 |
| ✅ Implemented | BswModuleDependency | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 71 |
| ✅ Implemented | BswModuleEntry | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 167 |
| ➕ Extra | BswCallType | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Not documented in requirements |
| ➕ Extra | BswEntryKindEnum | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Not documented in requirements |
| ➕ Extra | BswEntryRelationshipEnum | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Not documented in requirements |
| ➕ Extra | BswExecutionContext | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Not documented in requirements |
| ➕ Extra | SwServiceImplPolicyEnum | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | BswCallType | callback, callout, interrupt, regular, scheduled | ASYNCHRONOUS, SYNCHRONOUS | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 28; Missing: callback, callout, interrupt, regular, scheduled; Extra: ASYNCHRONOUS, SYNCHRONOUS |
| ⚠️ Literal Mismatch | BswEntryKindEnum | AUTOSAR, Basic, abstract, concrete | FUNCTION | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 19; Missing: AUTOSAR, Basic, abstract, concrete; Extra: FUNCTION |
| ⚠️ Literal Mismatch | BswEntryRelationshipEnum | derivedFrom | calls, reads, triggers, writes | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 624; Missing: derivedFrom; Extra: calls, reads, triggers, writes |
| ⚠️ Literal Mismatch | BswExecutionContext | hook, interruptCat1, interruptCat2, task, unspecified | HOOK, INTERRUPT-CAT-1, INTERRUPT-CAT-2, TASK, UNSPECIFIED | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Line 39; Missing: hook, interruptCat1, interruptCat2, task, unspecified; Extra: HOOK, INTERRUPT-CAT-1, INTERRUPT-CAT-2, TASK, UNSPECIFIED |
| ➕ Extra | SwServiceImplPolicyEnum | - | INLINE, INLINE-CONDITIONAL, MACRO, STANDARD | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior

**Summary:**
- Classes: 37/37 implemented, 2 extra
- Enums: 1/1 implemented, 3 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BswAsynchronousServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 74 |
| ✅ Implemented | BswAsynchronousServerCallResultPoint | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 258 |
| ✅ Implemented | BswAsynchronousServerCallReturnsEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2234 |
| ✅ Implemented | BswBackgroundEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1177 |
| ✅ Implemented | BswCalledEntity | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 638 |
| ✅ Implemented | BswDataReceivedEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 983 |
| ✅ Implemented | BswDataReceptionPolicy | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1299 |
| ✅ Implemented | BswDirectCallPoint | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 118 |
| ✅ Implemented | BswDistinguishedPartition | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 344 |
| ✅ Implemented | BswEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 758 |
| ✅ Implemented | BswExclusiveAreaPolicy | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2261 |
| ✅ Implemented | BswExternalTriggerOccurredEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1211 |
| ✅ Implemented | BswInternalBehavior | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1427 |
| ✅ Implemented | BswInternalTriggerOccurredEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1025 |
| ✅ Implemented | BswInternalTriggeringPoint | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1383 |
| ✅ Implemented | BswInterruptEntity | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 692 |
| ✅ Implemented | BswInterruptEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2282 |
| ✅ Implemented | BswModeManagerErrorEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2299 |
| ✅ Implemented | BswModeReceiverPolicy | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2318 |
| ✅ Implemented | BswModeSenderPolicy | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1105 |
| ✅ Implemented | BswModeSwitchAckRequest | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1067 |
| ✅ Implemented | BswModeSwitchEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 867 |
| ✅ Implemented | BswModeSwitchedAckEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 909 |
| ✅ Implemented | BswModuleCallPoint | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 29 |
| ✅ Implemented | BswModuleEntity | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 364 |
| ✅ Implemented | BswOperationInvokedEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 803 |
| ✅ Implemented | BswOsTaskExecutionEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1194 |
| ✅ Implemented | BswQueuedDataReceptionPolicy | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 1343 |
| ✅ Implemented | BswSchedulableEntity | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 655 |
| ✅ Implemented | BswScheduleEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 847 |
| ✅ Implemented | BswSchedulerNamePrefix | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2341 |
| ✅ Implemented | BswServiceDependency | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2369 |
| ✅ Implemented | BswSynchronousServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 188 |
| ✅ Implemented | BswTimingEvent | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 927 |
| ✅ Implemented | BswTriggerDirectImplementation | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2397 |
| ✅ Implemented | BswVariableAccess | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 278 |
| ✅ Implemented | RoleBasedBswModuleEntryAssignment | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 2419 |
| ➕ Extra | BswApiOptions | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Not documented in requirements |
| ➕ Extra | BswInterruptCategory | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ✅ Implemented | BswInterruptCategory | cat1, cat2 | cat1, cat2 | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Line 672 |
| ➕ Extra | BswExclusiveAreaPolicy | - | none, internal, external | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Not documented in requirements |
| ➕ Extra | BswModeReceiverPolicy | - | none, immediate, deferred | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Not documented in requirements |
| ➕ Extra | BswTriggerDirectImplementation | - | not-allowed, allowed | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BswImplementation | src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswImplementation.py | Line 12 |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes

**Summary:**
- Classes: 0/0 implemented, 33 extra
- Enums: 2/4 implemented, 2 missing, 1 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ➕ Extra | ARBoolean | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | AREnum | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ARFloat | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ARLiteral | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ARNumerical | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ARPositiveInteger | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ARType | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ArgumentDirectionEnum | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | Boolean | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ByteOrderEnum | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | CIdentifier | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | CategoryString | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | DateTime | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | DiagRequirementIdString | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | Float | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | Identifier | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | Integer | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | Ip4AddressString | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | Ip6AddressString | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | Limit | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | MacAddressString | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | NameToken | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | PositiveInteger | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | PositiveUnlimitedInteger | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | RefType | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | ReferrableSubtypesEnum | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | RegularExpression | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | RevisionLabelString | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | String | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | TRefType | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | TimeValue | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | UnlimitedInteger | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |
| ➕ Extra | VerbatimString | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | ByteOrderEnum | AUTOSAR, Diagnostic, First, mostSignificantByte, mostSignificantByteLast, opaque | - | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Line 856; Missing: AUTOSAR, Diagnostic, First, mostSignificantByte, mostSignificantByteLast, opaque |
| ✅ Implemented | ArgumentDirectionEnum | in, inout, out | in, inout, out | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py | Line 782 |
| ❌ Missing | IntervalTypeEnum | closed, open | - | - | Not found in implementation |
| ❌ Missing | MonotonyEnum | decreasing, increasing, monotonous, noMonotony, strictlyDecreasing, strictlyIncreasing, strictMonotonous | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject

**Summary:**
- Classes: 2/2 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AutosarEngineeringObject | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/EngineeringObject.py | Line 123 |
| ✅ Implemented | EngineeringObject | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/EngineeringObject.py | Line 12 |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultidimensionalTime

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory MultidimensionalTime/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | MultidimensionalTime | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage

**Summary:**
- Classes: 2/4 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both ARPackage.py and ARPackage/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ARPackage | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py | Line 266 |
| ✅ Implemented | ReferenceBase | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py | Line 82 |
| ❌ Missing | ARElement | - | Not found in implementation |
| ❌ Missing | PackageableElement | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable

**Summary:**
- Classes: 4/6 implemented, 2 missing, 3 extra
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both Identifiable.py and Identifiable/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Describable | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py | Line 479 |
| ✅ Implemented | Identifiable | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py | Line 221 |
| ✅ Implemented | MultilanguageReferrable | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py | Line 76 |
| ✅ Implemented | Referrable | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py | Line 17 |
| ❌ Missing | ShortNameFragment | - | Not found in implementation |
| ❌ Missing | SingleLanguageReferrable | - | Not found in implementation |
| ➕ Extra | ARElement | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py | Not documented in requirements |
| ➕ Extra | CollectableElement | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py | Not documented in requirements |
| ➕ Extra | PackageableElement | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AnyInstanceRef

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AnyInstanceRef | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/AnyInstanceRef.py | Line 11 |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::GeneralAnnotation

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory GeneralAnnotation/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | GeneralAnnotation | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::TagWithOptionalValue

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TagWithOptionalValue/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | TagWithOptionalValue | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection

**Summary:**
- Classes: 1/2 implemented, 1 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both ElementCollection.py and ElementCollection/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Collection | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ElementCollection.py | Line 14 |
| ❌ Missing | CollectableElement | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | AutoCollectEnum | refAll, refNone, refNonStandard | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef

**Summary:**
- Classes: 0/12 implemented, 12 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory SpecialDataDef/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | SdgAbstractForeignReference | - | Not found in implementation |
| ❌ Missing | SdgAbstractPrimitiveAttribute | - | Not found in implementation |
| ❌ Missing | SdgAggregationWithVariation | - | Not found in implementation |
| ❌ Missing | SdgAttribute | - | Not found in implementation |
| ❌ Missing | SdgClass | - | Not found in implementation |
| ❌ Missing | SdgDef | - | Not found in implementation |
| ❌ Missing | SdgElementWithGid | - | Not found in implementation |
| ❌ Missing | SdgForeignReference | - | Not found in implementation |
| ❌ Missing | SdgForeignReferenceWithVariation | - | Not found in implementation |
| ❌ Missing | SdgPrimitiveAttribute | - | Not found in implementation |
| ❌ Missing | SdgPrimitiveAttributeWithVariation | - | Not found in implementation |
| ❌ Missing | SdgReference | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ModelRestrictionTypes/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbstractMultiplicityRestriction | - | Not found in implementation |
| ❌ Missing | AbstractValueRestriction | - | Not found in implementation |
| ❌ Missing | AbstractVariationRestriction | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | FullBindingTimeEnum | blueprintDerivationTime, codeGenerationTime, linkTime, postBuild, preCompileTime, systemDesignTime | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ArObject

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ARObject | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py | Line 10 |

### Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest

**Summary:**
- Classes: 0/8 implemented, 8 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory BuildActionManifest/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BuildAction | - | Not found in implementation |
| ❌ Missing | BuildActionEntity | - | Not found in implementation |
| ❌ Missing | BuildActionEnvironment | - | Not found in implementation |
| ❌ Missing | BuildActionInvocator | - | Not found in implementation |
| ❌ Missing | BuildActionIoElement | - | Not found in implementation |
| ❌ Missing | BuildActionManifest | - | Not found in implementation |
| ❌ Missing | BuildEngineeringObject | - | Not found in implementation |
| ❌ Missing | GenericModelReference | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling

**Summary:**
- Classes: 0/11 implemented, 11 missing
- Enums: 0/2 implemented, 2 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ConditionByFormula | - | Not found in implementation |
| ❌ Missing | EvaluatedVariantSet | - | Not found in implementation |
| ❌ Missing | PostBuildVariantCondition | - | Not found in implementation |
| ❌ Missing | PostBuildVariantCriterion | - | Not found in implementation |
| ❌ Missing | PostBuildVariantCriterionValue | - | Not found in implementation |
| ❌ Missing | PostBuildVariantCriterionValueSet | - | Not found in implementation |
| ❌ Missing | PredefinedVariant | - | Not found in implementation |
| ❌ Missing | SwSystemconstDependentFormula | - | Not found in implementation |
| ❌ Missing | SwSystemconstValue | - | Not found in implementation |
| ❌ Missing | SwSystemconstantValueSet | - | Not found in implementation |
| ❌ Missing | VariationPoint | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | AdditionalBindingTimeEnum | blueprintDerivationTime, postBuild | - | - | Not found in implementation |
| ❌ Missing | BindingTimeEnum | codeGenerationTime, linkTime, preCompileTime, systemDesignTime | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints

**Summary:**
- Classes: 0/13 implemented, 13 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory AttributeValueVariationPoints/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbstractEnumerationValueVariationPoint | - | Not found in implementation |
| ❌ Missing | AbstractNumericalVariationPoint | - | Not found in implementation |
| ❌ Missing | AttributeValueVariationPoint | - | Not found in implementation |
| ❌ Missing | BooleanValueVariationPoint | - | Not found in implementation |
| ❌ Missing | EnumerationMappingEntry | - | Not found in implementation |
| ❌ Missing | EnumerationMappingTable | - | Not found in implementation |
| ❌ Missing | FloatValueVariationPoint | - | Not found in implementation |
| ❌ Missing | IntegerValueVariationPoint | - | Not found in implementation |
| ❌ Missing | LimitValueVariationPoint | - | Not found in implementation |
| ❌ Missing | NumericalValueVariationPoint | - | Not found in implementation |
| ❌ Missing | PositiveIntegerValueVariationPoint | - | Not found in implementation |
| ❌ Missing | TimeValueValueVariationPoint | - | Not found in implementation |
| ❌ Missing | UnlimitedIntegerValueVariationPoint | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::DocumentationOnM1

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DocumentationOnM1/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Documentation | - | Not found in implementation |
| ❌ Missing | DocumentationContext | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | StandardNameEnum | Diagnostic, AUTOSARAP, CP, FO, TA, TC | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure

**Summary:**
- Classes: 6/6 implemented, 2 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AtpClassifier | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Line 120 |
| ✅ Implemented | AtpFeature | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Line 143 |
| ✅ Implemented | AtpInstanceRef | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Line 14 |
| ✅ Implemented | AtpPrototype | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Line 198 |
| ✅ Implemented | AtpStructureElement | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Line 227 |
| ✅ Implemented | AtpType | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Line 172 |
| ➕ Extra | AtpBlueprintMapping | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Not documented in requirements |
| ➕ Extra | AtpBlueprintable | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::GenericStructure::ViewMapSet

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ViewMapSet/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ViewMap | - | Not found in implementation |
| ❌ Missing | ViewMapSet | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::FormulaLanguage

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory FormulaLanguage/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | FormulaExpression | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights

**Summary:**
- Classes: 1/5 implemented, 4 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory RolesAndRights/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AtpDefinition | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/RolesAndRights/AtpDefinition.py | Line 10 |
| ❌ Missing | AclObjectSet | - | Not found in implementation |
| ❌ Missing | AclOperation | - | Not found in implementation |
| ❌ Missing | AclPermission | - | Not found in implementation |
| ❌ Missing | AclRole | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | AclScopeEnum | dependant, descendant, explicit | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles

**Summary:**
- Classes: 3/5 implemented, 2 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | LifeCycleInfo | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py | Line 101 |
| ✅ Implemented | LifeCycleInfoSet | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py | Line 262 |
| ✅ Implemented | LifeCyclePeriod | src/armodel/models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py | Line 15 |
| ❌ Missing | LifeCycleState | - | Not found in implementation |
| ❌ Missing | LifeCycleStateDefinitionGroup | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::GenericStructure::ImpositionTimes

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ImpositionTime | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration

**Summary:**
- Classes: 7/7 implemented, 2 extra
- Enums: 2/2 implemented, 1 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ModeDeclaration | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 121 |
| ✅ Implemented | ModeDeclarationGroup | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 228 |
| ✅ Implemented | ModeDeclarationGroupPrototype | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 332 |
| ✅ Implemented | ModeDeclarationGroupPrototypeMapping | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 29 |
| ✅ Implemented | ModeErrorBehavior | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 427 |
| ✅ Implemented | ModeRequestTypeMap | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 164 |
| ✅ Implemented | ModeTransition | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 448 |
| ➕ Extra | ModeActivationKind | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Not documented in requirements |
| ➕ Extra | ModeErrorReactionPolicyEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | ModeErrorReactionPolicyEnum | defaultMode, lastMode | keep-mode, transition-to-default-mode, transition-to-safe-mode | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 477; Missing: defaultMode, lastMode; Extra: keep-mode, transition-to-default-mode, transition-to-safe-mode |
| ✅ Implemented | ModeActivationKind | onEntry, onExit, onTransition | onEntry, onExit, onTransition | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py | Line 16 |

### Package: M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration

**Summary:**
- Classes: 2/2 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Trigger | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/TriggerDeclaration.py | Line 14 |
| ✅ Implemented | TriggerMapping | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/TriggerDeclaration.py | Line 84 |

### Package: M2::AUTOSARTemplates::CommonStructure::InternalBehavior

**Summary:**
- Classes: 6/6 implemented, 2 extra
- Enums: 2/2 implemented, 1 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AbstractEvent | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 330 |
| ✅ Implemented | ExclusiveArea | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 30 |
| ✅ Implemented | ExclusiveAreaNestingOrder | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 392 |
| ✅ Implemented | ExecutableEntity | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 48 |
| ✅ Implemented | ExecutableEntityActivationReason | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 413 |
| ✅ Implemented | InternalBehavior | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 203 |
| ➕ Extra | ApiPrincipleEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Not documented in requirements |
| ➕ Extra | ReentrancyLevelEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | ApiPrincipleEnum | common, perExecutableModule | callee, caller | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 377; Missing: common, perExecutableModule; Extra: callee, caller |
| ✅ Implemented | ReentrancyLevelEnum | multicoreReentrant, nonReentrant, singleCoreReentrant | multicoreReentrant, nonReentrant, singleCoreReentrant | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py | Line 17 |

### Package: M2::AUTOSARTemplates::CommonStructure::Implementation

**Summary:**
- Classes: 6/6 implemented, 2 extra
- Enums: 2/2 implemented, 2 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Code | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 62 |
| ✅ Implemented | Compiler | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 112 |
| ✅ Implemented | DependencyOnArtifact | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 226 |
| ✅ Implemented | Implementation | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 292 |
| ✅ Implemented | ImplementationProps | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 16 |
| ✅ Implemented | Linker | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 711 |
| ➕ Extra | DependencyUsageEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Not documented in requirements |
| ➕ Extra | ProgramminglanguageEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | DependencyUsageEnum | build, codegeneration, compile, execute, link | optional, required | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 696; Missing: build, codegeneration, compile, execute, link; Extra: optional, required |
| ⚠️ Literal Mismatch | ProgramminglanguageEnum | c, cpp, java | C, C++, Java, Python | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py | Line 740; Missing: c, cpp, java; Extra: C, C++, Java, Python |

### Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping

**Summary:**
- Classes: 4/4 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwcBswMapping | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py | Line 79 |
| ✅ Implemented | SwcBswRunnableMapping | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py | Line 13 |
| ✅ Implemented | SwcBswSynchronizedModeGroupPrototype | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py | Line 221 |
| ✅ Implemented | SwcBswSynchronizedTrigger | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py | Line 257 |

### Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption

**Summary:**
- Classes: 2/3 implemented, 1 missing, 10 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | HardwareConfiguration | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HardwareConfiguration.py | Line 9 |
| ✅ Implemented | SoftwareContext | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/SoftwareContext.py | Line 9 |
| ❌ Missing | ResourceConsumption | - | Not found in implementation |
| ➕ Extra | HeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Not documented in requirements |
| ➕ Extra | MeasuredHeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Not documented in requirements |
| ➕ Extra | MeasuredStackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Not documented in requirements |
| ➕ Extra | MemorySection | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py | Not documented in requirements |
| ➕ Extra | RoughEstimateHeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Not documented in requirements |
| ➕ Extra | RoughEstimateStackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Not documented in requirements |
| ➕ Extra | SectionNamePrefix | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py | Not documented in requirements |
| ➕ Extra | StackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Not documented in requirements |
| ➕ Extra | WorstCaseHeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Not documented in requirements |
| ➕ Extra | WorstCaseStackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage

**Summary:**
- Classes: 2/2 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | MemorySection | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py | Line 11 |
| ✅ Implemented | SectionNamePrefix | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py | Line 206 |

### Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage

**Summary:**
- Classes: 4/4 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | MeasuredStackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Line 130 |
| ✅ Implemented | RoughEstimateStackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Line 195 |
| ✅ Implemented | StackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Line 13 |
| ✅ Implemented | WorstCaseStackUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py | Line 236 |

### Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage

**Summary:**
- Classes: 4/4 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | HeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Line 10 |
| ✅ Implemented | MeasuredHeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Line 30 |
| ✅ Implemented | RoughEstimateHeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Line 47 |
| ✅ Implemented | WorstCaseHeapUsage | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py | Line 64 |

### Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime

**Summary:**
- Classes: 0/6 implemented, 6 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ExecutionTime/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AnalyzedExecutionTime | - | Not found in implementation |
| ❌ Missing | ExecutionTime | - | Not found in implementation |
| ❌ Missing | MeasuredExecutionTime | - | Not found in implementation |
| ❌ Missing | MemorySectionLocation | - | Not found in implementation |
| ❌ Missing | RoughEstimateOfExecutionTime | - | Not found in implementation |
| ❌ Missing | SimulatedExecutionTime | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport

**Summary:**
- Classes: 8/8 implemented, 12 extra
- Enums: 0/0 implemented, 4 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ImplementationElementInParameterInstanceRef | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/ImplementationElementInParameterInstanceRef.py | Line 5 |
| ✅ Implemented | McDataAccessDetails | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McDataAccessDetails.py | Line 4 |
| ✅ Implemented | McDataInstance | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McDataInstance.py | Line 6 |
| ✅ Implemented | McFunction | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McFunction.py | Line 6 |
| ✅ Implemented | McParameterElementGroup | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McParameterElementGroup.py | Line 6 |
| ✅ Implemented | McSupportData | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McSupportData.py | Line 6 |
| ✅ Implemented | McSwEmulationMethodSupport | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McSwEmulationMethodSupport.py | Line 4 |
| ✅ Implemented | RoleBasedMcDataAssignment | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RoleBasedMcDataAssignment.py | Line 5 |
| ➕ Extra | McFunctionDataRefSet | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/McFunctionDataRefSet.py | Not documented in requirements |
| ➕ Extra | RptAccessEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptAccessEnum.py | Not documented in requirements |
| ➕ Extra | RptComponent | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptComponent.py | Not documented in requirements |
| ➕ Extra | RptEnablerImplTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptEnablerImplTypeEnum.py | Not documented in requirements |
| ➕ Extra | RptExecutableEntity | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutableEntity.py | Not documented in requirements |
| ➕ Extra | RptExecutableEntityEvent | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutableEntityEvent.py | Not documented in requirements |
| ➕ Extra | RptExecutionContext | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionContext.py | Not documented in requirements |
| ➕ Extra | RptExecutionControlEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionControlEnum.py | Not documented in requirements |
| ➕ Extra | RptPreparationEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptPreparationEnum.py | Not documented in requirements |
| ➕ Extra | RptServicePoint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptServicePoint.py | Not documented in requirements |
| ➕ Extra | RptSupportData | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptSupportData.py | Not documented in requirements |
| ➕ Extra | RptSwPrototypingAccess | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptSwPrototypingAccess.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ➕ Extra | RptAccessEnum | - | read, read-write, write | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptAccessEnum.py | Not documented in requirements |
| ➕ Extra | RptEnablerImplTypeEnum | - | external, internal | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptEnablerImplTypeEnum.py | Not documented in requirements |
| ➕ Extra | RptExecutionControlEnum | - | asynchronous, synchronous | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionControlEnum.py | Not documented in requirements |
| ➕ Extra | RptPreparationEnum | - | prepared, unprepared | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptPreparationEnum.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport

**Summary:**
- Classes: 8/8 implemented, 4 extra
- Enums: 4/4 implemented, 4 literal mismatches

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory RptSupport/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | McFunctionDataRefSet | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/McFunctionDataRefSet.py | Line 6 |
| ✅ Implemented | RptComponent | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptComponent.py | Line 4 |
| ✅ Implemented | RptExecutableEntity | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutableEntity.py | Line 6 |
| ✅ Implemented | RptExecutableEntityEvent | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutableEntityEvent.py | Line 6 |
| ✅ Implemented | RptExecutionContext | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionContext.py | Line 5 |
| ✅ Implemented | RptServicePoint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptServicePoint.py | Line 6 |
| ✅ Implemented | RptSupportData | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptSupportData.py | Line 9 |
| ✅ Implemented | RptSwPrototypingAccess | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptSwPrototypingAccess.py | Line 6 |
| ➕ Extra | RptAccessEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptAccessEnum.py | Not documented in requirements |
| ➕ Extra | RptEnablerImplTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptEnablerImplTypeEnum.py | Not documented in requirements |
| ➕ Extra | RptExecutionControlEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionControlEnum.py | Not documented in requirements |
| ➕ Extra | RptPreparationEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptPreparationEnum.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | RptAccessEnum | enabled, none, protected | read, read-write, write | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptAccessEnum.py | Line 4; Missing: enabled, none, protected; Extra: read, read-write, write |
| ⚠️ Literal Mismatch | RptEnablerImplTypeEnum | none, rptEnablerRam, rptEnablerRamAndRom, rptEnablerRom | external, internal | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptEnablerImplTypeEnum.py | Line 4; Missing: none, rptEnablerRam, rptEnablerRamAndRom, rptEnablerRom; Extra: external, internal |
| ⚠️ Literal Mismatch | RptExecutionControlEnum | conditional, none | asynchronous, synchronous | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionControlEnum.py | Line 4; Missing: conditional, none; Extra: asynchronous, synchronous |
| ⚠️ Literal Mismatch | RptPreparationEnum | none, original, rptLevel1, rptLevel2, rptLevel3 | prepared, unprepared | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptPreparationEnum.py | Line 4; Missing: none, original, rptLevel1, rptLevel2, rptLevel3; Extra: prepared, unprepared |

### Package: M2::AUTOSARTemplates::CommonStructure::FlatMap

**Summary:**
- Classes: 5/5 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AliasNameAssignment | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py | Line 199 |
| ✅ Implemented | AliasNameSet | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py | Line 228 |
| ✅ Implemented | FlatInstanceDescriptor | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py | Line 16 |
| ✅ Implemented | FlatMap | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py | Line 154 |
| ✅ Implemented | RtePluginProps | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py | Line 247 |

### Package: M2::AUTOSARTemplates::CommonStructure::McGroups

**Summary:**
- Classes: 2/2 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | McGroup | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py | Line 8 |
| ✅ Implemented | McGroupDataRefSet | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py | Line 37 |

### Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

**Summary:**
- Classes: 71/71 implemented, 22 extra
- Enums: 18/18 implemented, 14 literal mismatches, 3 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BswMgrNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1864 |
| ✅ Implemented | ComMgrUserNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1881 |
| ✅ Implemented | CryptoKeyManagementNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1898 |
| ✅ Implemented | CryptoServiceJobNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1915 |
| ✅ Implemented | CryptoServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1712 |
| ✅ Implemented | DevelopmentError | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1932 |
| ✅ Implemented | DiagEventDebounceAlgorithm | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1073 |
| ✅ Implemented | DiagEventDebounceCounterBased | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1094 |
| ✅ Implemented | DiagEventDebounceMonitorInternal | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1193 |
| ✅ Implemented | DiagEventDebounceTimeBased | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1210 |
| ✅ Implemented | DiagnosticCapabilityElement | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 657 |
| ✅ Implemented | DiagnosticCommunicationManagerNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 773 |
| ✅ Implemented | DiagnosticComponentNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1961 |
| ✅ Implemented | DiagnosticControlNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1978 |
| ✅ Implemented | DiagnosticEnableConditionNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2010 |
| ✅ Implemented | DiagnosticEventInfoNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1268 |
| ✅ Implemented | DiagnosticEventManagerNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2027 |
| ✅ Implemented | DiagnosticEventNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1461 |
| ✅ Implemented | DiagnosticIoControlNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2044 |
| ✅ Implemented | DiagnosticOperationCycleNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2076 |
| ✅ Implemented | DiagnosticRequestFileTransferNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2093 |
| ✅ Implemented | DiagnosticRoutineNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 816 |
| ✅ Implemented | DiagnosticStorageConditionNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2110 |
| ✅ Implemented | DiagnosticUploadDownloadNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2127 |
| ✅ Implemented | DiagnosticValueNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 930 |
| ✅ Implemented | DiagnosticsCommunicationSecurityNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2144 |
| ✅ Implemented | DltUserNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1847 |
| ✅ Implemented | DoIpActivationLineNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2161 |
| ✅ Implemented | DoIpGidNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2178 |
| ✅ Implemented | DoIpGidSynchronizationNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2195 |
| ✅ Implemented | DoIpPowerModeStatusNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2212 |
| ✅ Implemented | DoIpRoutingActivationAuthenticationNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2229 |
| ✅ Implemented | DoIpRoutingActivationConfirmationNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2246 |
| ✅ Implemented | DoIpServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2263 |
| ✅ Implemented | DtcStatusChangeNotificationNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1390 |
| ✅ Implemented | EcuStateMgrUserNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1830 |
| ✅ Implemented | ErrorTracerNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2280 |
| ✅ Implemented | FunctionInhibitionAvailabilityNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2312 |
| ✅ Implemented | FunctionInhibitionNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2329 |
| ✅ Implemented | FurtherActionByteNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2346 |
| ✅ Implemented | GlobalSupervisionNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2363 |
| ✅ Implemented | HardwareTestNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2380 |
| ✅ Implemented | IdsMgrCustomTimestampNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2397 |
| ✅ Implemented | IdsMgrNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2414 |
| ✅ Implemented | IndicatorStatusNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2431 |
| ✅ Implemented | J1939DcmDm19Support | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2448 |
| ✅ Implemented | J1939RmIncomingRequestServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2465 |
| ✅ Implemented | J1939RmOutgoingRequestServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2482 |
| ✅ Implemented | NvBlockNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 219 |
| ✅ Implemented | ObdControlServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2516 |
| ✅ Implemented | ObdInfoServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2533 |
| ✅ Implemented | ObdMonitorServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2550 |
| ✅ Implemented | ObdPidServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2567 |
| ✅ Implemented | ObdRatioDenominatorNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2599 |
| ✅ Implemented | ObdRatioServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2616 |
| ✅ Implemented | RoleBasedDataAssignment | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 18 |
| ✅ Implemented | RuntimeError | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2650 |
| ✅ Implemented | SecureOnBoardCommunicationNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2679 |
| ✅ Implemented | ServiceDependency | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 513 |
| ✅ Implemented | ServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 132 |
| ✅ Implemented | SupervisedEntityCheckpointNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2728 |
| ✅ Implemented | SupervisedEntityNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2745 |
| ✅ Implemented | SymbolicNameProps | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2762 |
| ✅ Implemented | SyncTimeBaseMgrUserNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2783 |
| ✅ Implemented | TracedFailure | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2800 |
| ✅ Implemented | TransientFault | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2829 |
| ✅ Implemented | V2xDataManagerNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2858 |
| ✅ Implemented | V2xFacUserNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2875 |
| ✅ Implemented | V2xMUserNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2892 |
| ✅ Implemented | VendorSpecificServiceNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2909 |
| ✅ Implemented | WarningIndicatorRequestedBitNeeds | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2941 |
| ➕ Extra | DiagnosticAudienceEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DiagnosticClearDtcNotificationEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DiagnosticDenominatorConditionEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DiagnosticMonitorUpdateKindEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DiagnosticProcessingStyleEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DiagnosticRoutineTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DiagnosticServiceRequestCallbackTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DiagnosticValueAccessEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DtcFormatTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DtcKindEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | EventAcceptanceStatusEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | MaxCommModeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | NvBlockNeedsReliabilityEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | NvBlockNeedsWritingPriorityEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | ObdRatioConnectionKindEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | OperationCycleTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | RamBlockStatusControlEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | RoleBasedDataTypeAssignment | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | ServiceDiagnosticRelevanceEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | ServiceProviderEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | StorageConditionStatusEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | VerificationStatusIndicationModeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | DiagnosticClearDtcNotificationEnum | finish, start | - | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1364; Missing: finish, start |
| ⚠️ Literal Mismatch | DiagnosticDenominatorConditionEnum | _500miles, coldstart, csers, evap, evappurgeflow, obd | denominator-off, denominator-on | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 1995; Missing: _500miles, coldstart, csers, evap, evappurgeflow, obd; Extra: denominator-off, denominator-on |
| ⚠️ Literal Mismatch | DiagnosticMonitorUpdateKindEnum | always, steady | immediate, on-request | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2061; Missing: always, steady; Extra: immediate, on-request |
| ⚠️ Literal Mismatch | DiagnosticProcessingStyleEnum | AUTOSAR, Basic, processingStyle, processingStyleError, processingStyleSynchronous | processingStyleAsynchronous, processingStyleAsynchronousWithError, processingStyleSynchronous | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 907; Missing: AUTOSAR, Basic, processingStyle, processingStyleError; Extra: processingStyleAsynchronous, processingStyleAsynchronousWithError |
| ⚠️ Literal Mismatch | DiagnosticServiceRequestCallbackTypeEnum | AUTOSAR, Software, requestCallback | requestCallbackTypeManufacturer, requestCallbackTypeSupplier | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 637; Missing: AUTOSAR, Software, requestCallback; Extra: requestCallbackTypeManufacturer, requestCallbackTypeSupplier |
| ⚠️ Literal Mismatch | DiagnosticValueAccessEnum | readOnlyinformation, readWrite, writeOnly | readOnly, readWrite, writeOnly | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 884; Missing: readOnlyinformation; Extra: readOnly |
| ⚠️ Literal Mismatch | EventAcceptanceStatusEnum | eventAcceptanceDisabled, eventAcceptanceEnabled | accepted, rejected | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2297; Missing: eventAcceptanceDisabled, eventAcceptanceEnabled; Extra: accepted, rejected |
| ⚠️ Literal Mismatch | MaxCommModeEnum | full, none, silent | full-communication, no-communication, silent-communication | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2499; Missing: full, none, silent; Extra: full-communication, no-communication, silent-communication |
| ⚠️ Literal Mismatch | ObdRatioConnectionKindEnum | apiUse, observer | logical-and, logical-or | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2584; Missing: apiUse, observer; Extra: logical-and, logical-or |
| ⚠️ Literal Mismatch | OperationCycleTypeEnum | ignition, obdDcy, other, power, time, warmup | all-cycles, ignition-cycle, power-cycle | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2633; Missing: ignition, obdDcy, other, power, time, warmup; Extra: all-cycles, ignition-cycle, power-cycle |
| ⚠️ Literal Mismatch | ServiceDiagnosticRelevanceEnum | isNotRelevant, isRelevant | - | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 500; Missing: isNotRelevant, isRelevant |
| ⚠️ Literal Mismatch | ServiceProviderEnum | AUTOSAR, Software, anyStandardized, basicSoftwareModeManager, comManager, cryptoKeyManagement, cryptoServiceManager, defaultErrorTracer, diagnosticCommunication, diagnosticEventManager, diagnosticLogAndTrace, ecuManager, errorTracer, functionInhibitionManager, hardwareTestManager, intrusionDetectionSecurity, j1939Dcm, j1939RequestManager, nonVolatileRamManager, operatingSystem, secureOnBoardCommunication, syncBaseTimeManager, v2xFacilities, v2xManagement, vendorSpecific, watchDogManager | bsw, rte, swc | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2696; Missing: AUTOSAR, Software, anyStandardized, basicSoftwareModeManager, comManager, cryptoKeyManagement, cryptoServiceManager, defaultErrorTracer, diagnosticCommunication, diagnosticEventManager, diagnosticLogAndTrace, ecuManager, errorTracer, functionInhibitionManager, hardwareTestManager, intrusionDetectionSecurity, j1939Dcm, j1939RequestManager, nonVolatileRamManager, operatingSystem, secureOnBoardCommunication, syncBaseTimeManager, v2xFacilities, v2xManagement, vendorSpecific, watchDogManager; Extra: bsw, rte, swc |
| ⚠️ Literal Mismatch | StorageConditionStatusEnum | eventStorageDisabled, eventStorageEnabled | condition-false, condition-true | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2713; Missing: eventStorageDisabled, eventStorageEnabled; Extra: condition-false, condition-true |
| ⚠️ Literal Mismatch | VerificationStatusIndicationModeEnum | failureAndSuccess, failureOnly | direct, indirect | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 2926; Missing: failureAndSuccess, failureOnly; Extra: direct, indirect |
| ✅ Implemented | DiagnosticAudienceEnum | afterSales, aftermarket, development, manufacturing, supplier | afterSales, aftermarket, development, manufacturing, supplier | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 608 |
| ✅ Implemented | DiagnosticRoutineTypeEnum | asynchronous, synchronous | asynchronous, synchronous | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 753 |
| ✅ Implemented | NvBlockNeedsReliabilityEnum | errorCorrection, errorDetection, noProtection | errorCorrection, errorDetection, noProtection | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 173 |
| ✅ Implemented | NvBlockNeedsWritingPriorityEnum | high, low, medium | high, low, medium | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Line 196 |
| ➕ Extra | DtcFormatTypeEnum | - | - | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | DtcKindEnum | - | - | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |
| ➕ Extra | RamBlockStatusControlEnum | - | api, nvRamManager | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::CommonStructure::Constants

**Summary:**
- Classes: 0/23 implemented, 23 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Constants/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbstractRuleBasedValueSpecification | - | Not found in implementation |
| ❌ Missing | ApplicationRuleBasedValueSpecification | - | Not found in implementation |
| ❌ Missing | ApplicationValueSpecification | - | Not found in implementation |
| ❌ Missing | ArrayValueSpecification | - | Not found in implementation |
| ❌ Missing | CompositeRuleBasedValueArgument | - | Not found in implementation |
| ❌ Missing | CompositeRuleBasedValueSpecification | - | Not found in implementation |
| ❌ Missing | CompositeValueSpecification | - | Not found in implementation |
| ❌ Missing | ConstantReference | - | Not found in implementation |
| ❌ Missing | ConstantSpecification | - | Not found in implementation |
| ❌ Missing | ConstantSpecificationMapping | - | Not found in implementation |
| ❌ Missing | ConstantSpecificationMappingSet | - | Not found in implementation |
| ❌ Missing | NotAvailableValueSpecification | - | Not found in implementation |
| ❌ Missing | NumericalOrText | - | Not found in implementation |
| ❌ Missing | NumericalRuleBasedValueSpecification | - | Not found in implementation |
| ❌ Missing | NumericalValueSpecification | - | Not found in implementation |
| ❌ Missing | RecordValueSpecification | - | Not found in implementation |
| ❌ Missing | ReferenceValueSpecification | - | Not found in implementation |
| ❌ Missing | RuleArguments | - | Not found in implementation |
| ❌ Missing | RuleBasedAxisCont | - | Not found in implementation |
| ❌ Missing | RuleBasedValueCont | - | Not found in implementation |
| ❌ Missing | RuleBasedValueSpecification | - | Not found in implementation |
| ❌ Missing | TextValueSpecification | - | Not found in implementation |
| ❌ Missing | ValueSpecification | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure

**Summary:**
- Classes: 1/7 implemented, 6 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory AbstractBlueprintStructure/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AtpBlueprint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure/AtpBlueprint.py | Line 10 |
| ❌ Missing | AtpBlueprintMapping | - | Not found in implementation |
| ❌ Missing | AtpBlueprintable | - | Not found in implementation |
| ❌ Missing | BlueprintPolicy | - | Not found in implementation |
| ❌ Missing | BlueprintPolicyList | - | Not found in implementation |
| ❌ Missing | BlueprintPolicyNotModifiable | - | Not found in implementation |
| ❌ Missing | BlueprintPolicySingle | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Port

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Port/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | PortPrototypeBlueprint | - | Not found in implementation |
| ❌ Missing | PortPrototypeBlueprintInitValue | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Generic

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BlueprintMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintMapping

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory BlueprintMapping/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BlueprintMappingSet | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintMapping/BlueprintMappingSet.py | Line 5 |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintGenerator

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory BlueprintGenerator/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BlueprintGenerator | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator/BlueprintGenerator.py | Line 4 |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Keyword

**Summary:**
- Classes: 2/2 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Keyword | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/Keyword.py | Line 14 |
| ✅ Implemented | KeywordSet | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/Keyword.py | Line 84 |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::ClientServerInterfaceToBsw

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ClientServerInterfaceToBswModuleEntryBlueprintMapping | - | Not found in implementation |
| ❌ Missing | ClientServerOperationBlueprintMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/2 implemented, 2 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Baseline | - | Not found in implementation |
| ❌ Missing | DataExchangePoint | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DataExchangePointKind | agreed | - | - | Not found in implementation |
| ❌ Missing | SeverityEnum | error, info, warning | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DataFormatElementReference | - | Not found in implementation |
| ❌ Missing | RestrictionWithSeverity | - | Not found in implementation |
| ❌ Missing | SpecElementReference | - | Not found in implementation |
| ❌ Missing | SpecElementScope | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data

**Summary:**
- Classes: 0/23 implemented, 23 missing
- Enums: 0/1 implemented, 1 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbstractClassTailoring | - | Not found in implementation |
| ❌ Missing | AbstractCondition | - | Not found in implementation |
| ❌ Missing | AggregationCondition | - | Not found in implementation |
| ❌ Missing | AggregationTailoring | - | Not found in implementation |
| ❌ Missing | AttributeCondition | - | Not found in implementation |
| ❌ Missing | AttributeTailoring | - | Not found in implementation |
| ❌ Missing | ClassContentConditional | - | Not found in implementation |
| ❌ Missing | ClassTailoring | - | Not found in implementation |
| ❌ Missing | ConcreteClassTailoring | - | Not found in implementation |
| ❌ Missing | ConstraintTailoring | - | Not found in implementation |
| ❌ Missing | DataFormatElementScope | - | Not found in implementation |
| ❌ Missing | DataFormatTailoring | - | Not found in implementation |
| ❌ Missing | InvertCondition | - | Not found in implementation |
| ❌ Missing | MultiplicityRestrictionWithSeverity | - | Not found in implementation |
| ❌ Missing | PrimitiveAttributeCondition | - | Not found in implementation |
| ❌ Missing | PrimitiveAttributeTailoring | - | Not found in implementation |
| ❌ Missing | ReferenceCondition | - | Not found in implementation |
| ❌ Missing | ReferenceTailoring | - | Not found in implementation |
| ❌ Missing | SdgTailoring | - | Not found in implementation |
| ❌ Missing | TextualCondition | - | Not found in implementation |
| ❌ Missing | UnresolvedReferenceRestrictionWithSeverity | - | Not found in implementation |
| ❌ Missing | ValueRestrictionWithSeverity | - | Not found in implementation |
| ❌ Missing | VariationRestrictionWithSeverity | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DefaultValueApplicationStrategyEnum | defaultIfRevision, defaultIfUndefined | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DocumentElementScope | - | Not found in implementation |
| ❌ Missing | SpecificationDocumentScope | - | Not found in implementation |
| ❌ Missing | SpecificationScope | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintFormula

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BlueprintFormula | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Blueprint

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ConsistencyNeedsBlueprintSet | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes

**Summary:**
- Classes: 4/4 implemented, 2 extra
- Enums: 2/2 implemented, 2 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AbstractImplementationDataType | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Line 94 |
| ✅ Implemented | AbstractImplementationDataTypeElement | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Line 13 |
| ✅ Implemented | ImplementationDataType | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Line 102 |
| ✅ Implemented | ImplementationDataTypeElement | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Line 20 |
| ➕ Extra | ArrayImplPolicyEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Not documented in requirements |
| ➕ Extra | ArraySizeSemanticsEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | ArrayImplPolicyEnum | payloadAsArray, payloadAsPointerToArray | dynamic, static | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Line 309; Missing: payloadAsArray, payloadAsPointerToArray; Extra: dynamic, static |
| ⚠️ Literal Mismatch | ArraySizeSemanticsEnum | AUTOSAR, Diagnostic, fixedSize, variableSize | fixed-size, variable-size | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py | Line 324; Missing: AUTOSAR, Diagnostic, fixedSize, variableSize; Extra: fixed-size, variable-size |

### Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation

**Summary:**
- Classes: 4/4 implemented, 1 extra
- Enums: 1/1 implemented, 1 literal mismatches

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory SignalServiceTranslation/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SignalServiceTranslationElementProps | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationElementProps.py | Line 4 |
| ✅ Implemented | SignalServiceTranslationEventProps | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationEventProps.py | Line 4 |
| ✅ Implemented | SignalServiceTranslationProps | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationProps.py | Line 5 |
| ✅ Implemented | SignalServiceTranslationPropsSet | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationPropsSet.py | Line 5 |
| ➕ Extra | SignalServiceTranslationControlEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationControlEnum.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | SignalServiceTranslationControlEnum | allPartialNetworksActive, anyPartialNetworkActive, partialNetwork, serviceDiscovery, translationStart | automatic, manual | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationControlEnum.py | Line 4; Missing: allPartialNetworksActive, anyPartialNetworkActive, partialNetwork, serviceDiscovery, translationStart; Extra: automatic, manual |

### Package: M2::AUTOSARTemplates::CommonStructure::Filter

**Summary:**
- Classes: 1/1 implemented, 1 extra
- Enums: 1/1 implemented, 1 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | DataFilter | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Filter.py | Line 47 |
| ➕ Extra | DataFilterTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Filter.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | DataFilterTypeEnum | AUTOSAR, Software, always, maskedNewDiffersMaskedOld, maskedNewDiffersX, maskedNewEqualsX, never, newIsOutside, newIsWithinmin, oneEveryN | maskedNewDiffersMaskedOld, maskedNewDiffersX, maskedNewEqualsX, never, newIsOutside, newIsWithin, oneEveryN | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Filter.py | Line 11; Missing: AUTOSAR, Software, always, newIsWithinmin; Extra: newIsWithin |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions

**Summary:**
- Classes: 0/7 implemented, 7 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TimingExtensions/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BswCompositionTiming | - | Not found in implementation |
| ❌ Missing | BswModuleTiming | - | Not found in implementation |
| ❌ Missing | EcuTiming | - | Not found in implementation |
| ❌ Missing | SwcTiming | - | Not found in implementation |
| ❌ Missing | SystemTiming | - | Not found in implementation |
| ❌ Missing | TimingExtension | - | Not found in implementation |
| ❌ Missing | VfbTiming | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition

**Summary:**
- Classes: 6/6 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TimingCondition/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ModeInBswInstanceRef | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInBswInstanceRef.py | Line 4 |
| ✅ Implemented | ModeInSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInSwcInstanceRef.py | Line 4 |
| ✅ Implemented | TimingCondition | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingCondition.py | Line 5 |
| ✅ Implemented | TimingConditionFormula | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingConditionFormula.py | Line 4 |
| ✅ Implemented | TimingExtensionResource | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingExtensionResource.py | Line 4 |
| ✅ Implemented | TimingModeInstance | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingModeInstance.py | Line 5 |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | TimingDescription | - | Not found in implementation |
| ❌ Missing | TimingDescriptionEvent | - | Not found in implementation |
| ❌ Missing | TimingDescriptionEventChain | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

**Summary:**
- Classes: 0/30 implemented, 30 missing
- Enums: 0/12 implemented, 12 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TimingDescription/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AutosarOperationArgumentInstance | - | Not found in implementation |
| ❌ Missing | AutosarVariableInstance | - | Not found in implementation |
| ❌ Missing | TDEventBsw | - | Not found in implementation |
| ❌ Missing | TDEventBswInternalBehavior | - | Not found in implementation |
| ❌ Missing | TDEventBswModeDeclaration | - | Not found in implementation |
| ❌ Missing | TDEventBswModule | - | Not found in implementation |
| ❌ Missing | TDEventCom | - | Not found in implementation |
| ❌ Missing | TDEventComplex | - | Not found in implementation |
| ❌ Missing | TDEventCycleStart | - | Not found in implementation |
| ❌ Missing | TDEventFrClusterCycleStart | - | Not found in implementation |
| ❌ Missing | TDEventFrame | - | Not found in implementation |
| ❌ Missing | TDEventFrameEthernet | - | Not found in implementation |
| ❌ Missing | TDEventIPdu | - | Not found in implementation |
| ❌ Missing | TDEventISignal | - | Not found in implementation |
| ❌ Missing | TDEventModeDeclaration | - | Not found in implementation |
| ❌ Missing | TDEventOccurrenceExpression | - | Not found in implementation |
| ❌ Missing | TDEventOccurrenceExpressionFormula | - | Not found in implementation |
| ❌ Missing | TDEventOperation | - | Not found in implementation |
| ❌ Missing | TDEventSLLET | - | Not found in implementation |
| ❌ Missing | TDEventSLLETPort | - | Not found in implementation |
| ❌ Missing | TDEventSwc | - | Not found in implementation |
| ❌ Missing | TDEventSwcInternalBehavior | - | Not found in implementation |
| ❌ Missing | TDEventSwcInternalBehaviorReference | - | Not found in implementation |
| ❌ Missing | TDEventTTCanCycleStart | - | Not found in implementation |
| ❌ Missing | TDEventTrigger | - | Not found in implementation |
| ❌ Missing | TDEventVariableDataPrototype | - | Not found in implementation |
| ❌ Missing | TDEventVfb | - | Not found in implementation |
| ❌ Missing | TDEventVfbPort | - | Not found in implementation |
| ❌ Missing | TDEventVfbReference | - | Not found in implementation |
| ❌ Missing | TDHeaderIdRange | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | TDEventBswInternalBehaviorTypeEnum | bswModuleEntity, bswModuleEntity, bswModuleEntityTerminated | - | - | Not found in implementation |
| ❌ Missing | TDEventBswModeDeclarationTypeEnum | modeDeclarationRequested, modeDeclaration, modeDeclaration | - | - | Not found in implementation |
| ❌ Missing | TDEventBswModuleTypeEnum | bswMEntryCalled, bswMEntryCallReturned | - | - | Not found in implementation |
| ❌ Missing | TDEventFrameEthernetTypeEnum | frameEthernetTransmission, frameEthernet, frameEthernet, frameEthernetSent | - | - | Not found in implementation |
| ❌ Missing | TDEventFrameTypeEnum | frameQueuedFor, frameReceivedByIfcorresponding, frameTransmitted | - | - | Not found in implementation |
| ❌ Missing | TDEventIPduTypeEnum | iPduReceivedBy, COM, iPduSentToIfspecific | - | - | Not found in implementation |
| ❌ Missing | TDEventISignalTypeEnum | iSignalAvailableFor, RTE, iSignalSentToCOM | - | - | Not found in implementation |
| ❌ Missing | TDEventModeDeclarationTypeEnum | modeDeclaration, modeDeclaration | - | - | Not found in implementation |
| ❌ Missing | TDEventOperationTypeEnum | operationCalled, operationCallReceived, operationCallResponseReceived, operationCall | - | - | Not found in implementation |
| ❌ Missing | TDEventSwcInternalBehaviorTypeEnum | runnableEntity, runnableEntity, runnableEntityTerminated, runnableEntityVariableAccess | - | - | Not found in implementation |
| ❌ Missing | TDEventTriggerTypeEnum | triggerActivated, triggerReleased | - | - | Not found in implementation |
| ❌ Missing | TDEventVariableDataPrototypeTypeEnum | variableData, variableData | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint

**Summary:**
- Classes: 1/1 implemented, 24 extra
- Enums: 0/0 implemented, 4 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | TimingConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingConstraint.py | Line 26 |
| ➕ Extra | AgeConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/AgeConstraint.py | Not documented in requirements |
| ➕ Extra | ArbitraryEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Not documented in requirements |
| ➕ Extra | BurstPatternEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Not documented in requirements |
| ➕ Extra | ConcretePatternEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Not documented in requirements |
| ➕ Extra | ConfidenceInterval | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Not documented in requirements |
| ➕ Extra | EOCEventRef | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | EOCExecutableEntityRef | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | EOCExecutableEntityRefAbstract | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | EOCExecutableEntityRefGroup | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | EventOccurrenceKindEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Not documented in requirements |
| ➕ Extra | EventTriggeringConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Not documented in requirements |
| ➕ Extra | ExecutionOrderConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | ExecutionOrderConstraintTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | ExecutionTimeConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py | Not documented in requirements |
| ➕ Extra | ExecutionTimeTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py | Not documented in requirements |
| ➕ Extra | LatencyConstraintTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py | Not documented in requirements |
| ➕ Extra | LatencyTimingConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py | Not documented in requirements |
| ➕ Extra | LetDataExchangeParadigmEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | OffsetTimingConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/OffsetConstraint.py | Not documented in requirements |
| ➕ Extra | PeriodicEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Not documented in requirements |
| ➕ Extra | SporadicEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Not documented in requirements |
| ➕ Extra | SynchronizationPointConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationPointConstraint.py | Not documented in requirements |
| ➕ Extra | SynchronizationTimingConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Not documented in requirements |
| ➕ Extra | SynchronizationTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ➕ Extra | EventOccurrenceKindEnum | - | start, end, start-and-end | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Not documented in requirements |
| ➕ Extra | ExecutionTimeTypeEnum | - | best-case, worst-case, average-case | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py | Not documented in requirements |
| ➕ Extra | LatencyConstraintTypeEnum | - | response-time, reaction-time, end-to-end-latency | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py | Not documented in requirements |
| ➕ Extra | SynchronizationTypeEnum | - | hard-synchronization, soft-synchronization, no-synchronization | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming

**Summary:**
- Classes: 1/1 implemented, 2 extra
- Enums: 2/2 implemented, 2 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SynchronizationTimingConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Line 53 |
| ➕ Extra | EventOccurrenceKindEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Not documented in requirements |
| ➕ Extra | SynchronizationTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | EventOccurrenceKindEnum | multipleOccurrences, singleOccurrence | end, start, start-and-end | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Line 36; Missing: multipleOccurrences, singleOccurrence; Extra: end, start, start-and-end |
| ⚠️ Literal Mismatch | SynchronizationTypeEnum | response, stimulus | hard-synchronization, no-synchronization, soft-synchronization | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py | Line 19; Missing: response, stimulus; Extra: hard-synchronization, no-synchronization, soft-synchronization |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint

**Summary:**
- Classes: 1/1 implemented, 1 extra
- Enums: 1/1 implemented, 1 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | LatencyTimingConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py | Line 36 |
| ➕ Extra | LatencyConstraintTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | LatencyConstraintTypeEnum | age, reaction | end-to-end-latency, reaction-time, response-time | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py | Line 19; Missing: age, reaction; Extra: end-to-end-latency, reaction-time, response-time |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint

**Summary:**
- Classes: 7/7 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ArbitraryEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Line 94 |
| ✅ Implemented | BurstPatternEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Line 111 |
| ✅ Implemented | ConcretePatternEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Line 147 |
| ✅ Implemented | ConfidenceInterval | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Line 164 |
| ✅ Implemented | EventTriggeringConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Line 26 |
| ✅ Implemented | PeriodicEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Line 40 |
| ✅ Implemented | SporadicEventTriggering | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py | Line 67 |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::OffsetConstraint

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | OffsetTimingConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/OffsetConstraint.py | Line 16 |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::AgeConstraint

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AgeConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/AgeConstraint.py | Line 17 |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint

**Summary:**
- Classes: 5/5 implemented, 2 extra
- Enums: 0/2 implemented, 2 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | EOCEventRef | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Line 101 |
| ✅ Implemented | EOCExecutableEntityRef | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Line 35 |
| ✅ Implemented | EOCExecutableEntityRefAbstract | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Line 22 |
| ✅ Implemented | EOCExecutableEntityRefGroup | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Line 137 |
| ✅ Implemented | ExecutionOrderConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Line 64 |
| ➕ Extra | ExecutionOrderConstraintTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |
| ➕ Extra | LetDataExchangeParadigmEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | ExecutionOrderConstraintTypeEnum | hierarchicalEOC, ordinaryEOC, repetitiveEOC | - | - | Not found in implementation |
| ❌ Missing | LetDataExchangeParadigmEnum | interLetOnly, intraLetEOC | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint

**Summary:**
- Classes: 1/1 implemented, 1 extra
- Enums: 1/1 implemented, 1 literal mismatches

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ExecutionTimeConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py | Line 37 |
| ➕ Extra | ExecutionTimeTypeEnum | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | ExecutionTimeTypeEnum | gross, net | average-case, best-case, worst-case | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py | Line 20; Missing: gross, net; Extra: average-case, best-case, worst-case |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationPointConstraint

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SynchronizationPointConstraint | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationPointConstraint.py | Line 17 |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TimingCpSoftwareCluster/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | TDCpSoftwareClusterMapping | - | Not found in implementation |
| ❌ Missing | TDCpSoftwareClusterMappingSet | - | Not found in implementation |
| ❌ Missing | TDCpSoftwareClusterResourceMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock

**Summary:**
- Classes: 3/3 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TimingClock/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | TDLETZoneClock | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TDLETZoneClock.py | Line 5 |
| ✅ Implemented | TimingClock | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClock.py | Line 4 |
| ✅ Implemented | TimingClockSyncAccuracy | src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClockSyncAccuracy.py | Line 4 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior

**Summary:**
- Classes: 1/3 implemented, 2 missing, 34 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | RunnableEntity | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RunnableEntity.py | Line 32 |
| ❌ Missing | SwcExclusiveAreaPolicy | - | Not found in implementation |
| ❌ Missing | SwcInternalBehavior | - | Not found in implementation |
| ➕ Extra | AbstractAccessPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py | Not documented in requirements |
| ➕ Extra | ArVariableInImplementationDataInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstanceRefsUsage.py | Not documented in requirements |
| ➕ Extra | AsynchronousServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Not documented in requirements |
| ➕ Extra | AsynchronousServerCallResultPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Not documented in requirements |
| ➕ Extra | AsynchronousServerCallReturnsEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | AutosarParameterRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstanceRefsUsage.py | Not documented in requirements |
| ➕ Extra | AutosarVariableRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AutosarVariableRef.py | Not documented in requirements |
| ➕ Extra | BackgroundEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | DataReceiveErrorEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | DataReceivedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | DataSendCompletedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | DataWriteCompletedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | ExternalTriggeringPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py | Not documented in requirements |
| ➕ Extra | ExternalTriggeringPointIdent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py | Not documented in requirements |
| ➕ Extra | IncludedDataTypeSet | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/IncludedDataTypes.py | Not documented in requirements |
| ➕ Extra | IncludedModeDeclarationGroupSet | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py | Not documented in requirements |
| ➕ Extra | InitEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | InternalTriggerOccurredEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | InternalTriggeringPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py | Not documented in requirements |
| ➕ Extra | ModeAccessPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py | Not documented in requirements |
| ➕ Extra | ModeSwitchPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py | Not documented in requirements |
| ➕ Extra | ModeSwitchedAckEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | OperationInvokedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | PerInstanceMemory | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PerInstanceMemory.py | Not documented in requirements |
| ➕ Extra | PortAPIOption | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PortAPIOptions.py | Not documented in requirements |
| ➕ Extra | PortDefinedArgumentValue | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PortAPIOptions.py | Not documented in requirements |
| ➕ Extra | RTEEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | RoleBasedPortAssignment | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping.py | Not documented in requirements |
| ➕ Extra | RunnableEntityArgument | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RunnableEntity.py | Not documented in requirements |
| ➕ Extra | ServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Not documented in requirements |
| ➕ Extra | SwcModeSwitchEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |
| ➕ Extra | SwcServiceDependency | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping.py | Not documented in requirements |
| ➕ Extra | SynchronousServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Not documented in requirements |
| ➕ Extra | TimingEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount

**Summary:**
- Classes: 1/3 implemented, 2 missing
- Enums: 0/1 implemented, 1 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AbstractAccessPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py | Line 11 |
| ❌ Missing | AccessCount | - | Not found in implementation |
| ❌ Missing | AccessCountSet | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | RteApiReturnValueProvisionEnum | noReturnValueProvided, returnValueProvided | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping

**Summary:**
- Classes: 2/3 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | RoleBasedPortAssignment | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping.py | Line 16 |
| ✅ Implemented | SwcServiceDependency | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping.py | Line 38 |
| ❌ Missing | RoleBasedDataTypeAssignment | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall

**Summary:**
- Classes: 4/4 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AsynchronousServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Line 37 |
| ✅ Implemented | AsynchronousServerCallResultPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Line 57 |
| ✅ Implemented | ServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Line 12 |
| ✅ Implemented | SynchronousServerCallPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py | Line 42 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements

**Summary:**
- Classes: 0/6 implemented, 6 missing
- Enums: 0/1 implemented, 1 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ArParameterInImplementationDataInstanceRef | - | Not found in implementation |
| ❌ Missing | ArVariableInImplementationDataInstanceRef | - | Not found in implementation |
| ❌ Missing | AutosarParameterRef | - | Not found in implementation |
| ❌ Missing | AutosarVariableRef | - | Not found in implementation |
| ❌ Missing | ParameterAccess | - | Not found in implementation |
| ❌ Missing | VariableAccess | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | VariableAccessScopeEnum | communicationInter, communicationIntra, interPartitionIntra | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::InstanceRefs

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InstanceRefs/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ParameterInAtomicSWCTypeInstanceRef | - | Not found in implementation |
| ❌ Missing | VariableInAtomicSWCTypeInstanceRef | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger

**Summary:**
- Classes: 2/2 implemented, 1 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ExternalTriggeringPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py | Line 33 |
| ✅ Implemented | InternalTriggeringPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py | Line 13 |
| ➕ Extra | ExternalTriggeringPointIdent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup

**Summary:**
- Classes: 3/3 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | IncludedModeDeclarationGroupSet | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py | Line 49 |
| ✅ Implemented | ModeAccessPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py | Line 14 |
| ✅ Implemented | ModeSwitchPoint | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py | Line 35 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents

**Summary:**
- Classes: 13/18 implemented, 5 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AsynchronousServerCallReturnsEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 40 |
| ✅ Implemented | BackgroundEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 202 |
| ✅ Implemented | DataReceiveErrorEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 118 |
| ✅ Implemented | DataReceivedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 82 |
| ✅ Implemented | DataSendCompletedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 54 |
| ✅ Implemented | DataWriteCompletedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 68 |
| ✅ Implemented | InitEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 147 |
| ✅ Implemented | InternalTriggerOccurredEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 187 |
| ✅ Implemented | ModeSwitchedAckEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 207 |
| ✅ Implemented | OperationInvokedEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 132 |
| ✅ Implemented | RTEEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 16 |
| ✅ Implemented | SwcModeSwitchEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 96 |
| ✅ Implemented | TimingEvent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py | Line 152 |
| ❌ Missing | ExternalTriggerOccurredEvent | - | Not found in implementation |
| ❌ Missing | OsTaskExecutionEvent | - | Not found in implementation |
| ❌ Missing | SwcModeManagerErrorEvent | - | Not found in implementation |
| ❌ Missing | TransformerHardErrorEvent | - | Not found in implementation |
| ❌ Missing | WaitPoint | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions

**Summary:**
- Classes: 2/4 implemented, 2 missing
- Enums: 0/3 implemented, 3 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | PortAPIOption | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PortAPIOptions.py | Line 32 |
| ✅ Implemented | PortDefinedArgumentValue | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PortAPIOptions.py | Line 11 |
| ❌ Missing | CommunicationBufferLocking | - | Not found in implementation |
| ❌ Missing | SwcSupportedFeature | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DataTransformationErrorHandlingEnum | noTransformerErrorHandling, transformerErrorHandling | - | - | Not found in implementation |
| ❌ Missing | DataTransformationStatusForwardingEnum | noTransformerStatusForwarding, transformerStatusForwarding | - | - | Not found in implementation |
| ❌ Missing | SupportBufferLockingEnum | doesNotSupportBufferLocking, supportsBufferLocking | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RunnableEntity

**Summary:**
- Classes: 1/1 implemented, 1 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | RunnableEntityArgument | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RunnableEntity.py | Line 18 |
| ➕ Extra | RunnableEntity | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RunnableEntity.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::InstantiationDataDefProps

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | InstantiationDataDefProps | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PerInstanceMemory

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | PerInstanceMemory | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PerInstanceMemory.py | Line 12 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::IncludedDataTypes

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | IncludedDataTypeSet | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/IncludedDataTypes.py | Line 10 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::VariantHandling

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | VariationPointProxy | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes

**Summary:**
- Classes: 7/7 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ApplicationArrayElement | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py | Line 78 |
| ✅ Implemented | ApplicationCompositeElementDataPrototype | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py | Line 61 |
| ✅ Implemented | ApplicationRecordElement | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py | Line 119 |
| ✅ Implemented | AutosarDataPrototype | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py | Line 32 |
| ✅ Implemented | DataPrototype | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py | Line 16 |
| ✅ Implemented | ParameterDataPrototype | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py | Line 134 |
| ✅ Implemented | VariableDataPrototype | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py | Line 48 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes

**Summary:**
- Classes: 8/8 implemented
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both Datatypes.py and Datatypes/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ApplicationArrayDataType | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 57 |
| ✅ Implemented | ApplicationCompositeDataType | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 49 |
| ✅ Implemented | ApplicationDataType | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 36 |
| ✅ Implemented | ApplicationPrimitiveDataType | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 44 |
| ✅ Implemented | ApplicationRecordDataType | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 80 |
| ✅ Implemented | AutosarDataType | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 19 |
| ✅ Implemented | DataTypeMap | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 97 |
| ✅ Implemented | DataTypeMappingSet | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py | Line 118 |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | ArraySizeHandlingEnum | allIndicesDifferentArraySize, allIndicesSameArraySize, Software, AUTOSAR, inheritedFromArray | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario

**Summary:**
- Classes: 2/9 implemented, 7 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both RPTScenario.py and RPTScenario/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | IdentCaption | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py | Line 11 |
| ✅ Implemented | ModeAccessPointIdent | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py | Line 20 |
| ❌ Missing | ExternalTriggeringPointIdent | - | Not found in implementation |
| ❌ Missing | RapidPrototypingScenario | - | Not found in implementation |
| ❌ Missing | RptContainer | - | Not found in implementation |
| ❌ Missing | RptExecutableEntityProperties | - | Not found in implementation |
| ❌ Missing | RptHook | - | Not found in implementation |
| ❌ Missing | RptImplPolicy | - | Not found in implementation |
| ❌ Missing | RptProfile | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | RptServicePointEnum | enabled, none | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory NvBlockComponent/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BulkNvDataDescriptor | - | Not found in implementation |
| ❌ Missing | ModeSwitchEventTriggeredActivity | - | Not found in implementation |
| ❌ Missing | NvBlockDataMapping | - | Not found in implementation |
| ❌ Missing | NvBlockDescriptor | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | RamBlockStatusControlEnum | api, nvRamManager | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

**Summary:**
- Classes: 0/31 implemented, 31 missing, 1 extra
- Enums: 0/2 implemented, 2 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ApplicationCompositeDataTypeSubElementRef | - | Not found in implementation |
| ❌ Missing | ApplicationError | - | Not found in implementation |
| ❌ Missing | ArgumentDataPrototype | - | Not found in implementation |
| ❌ Missing | ClientServerApplicationErrorMapping | - | Not found in implementation |
| ❌ Missing | ClientServerInterface | - | Not found in implementation |
| ❌ Missing | ClientServerInterfaceMapping | - | Not found in implementation |
| ❌ Missing | ClientServerOperation | - | Not found in implementation |
| ❌ Missing | ClientServerOperationMapping | - | Not found in implementation |
| ❌ Missing | DataInterface | - | Not found in implementation |
| ❌ Missing | DataPrototypeMapping | - | Not found in implementation |
| ❌ Missing | ImplementationDataTypeSubElementRef | - | Not found in implementation |
| ❌ Missing | InvalidationPolicy | - | Not found in implementation |
| ❌ Missing | MetaDataItem | - | Not found in implementation |
| ❌ Missing | MetaDataItemSet | - | Not found in implementation |
| ❌ Missing | ModeDeclarationMapping | - | Not found in implementation |
| ❌ Missing | ModeDeclarationMappingSet | - | Not found in implementation |
| ❌ Missing | ModeInterfaceMapping | - | Not found in implementation |
| ❌ Missing | ModeSwitchInterface | - | Not found in implementation |
| ❌ Missing | NvDataInterface | - | Not found in implementation |
| ❌ Missing | ParameterInterface | - | Not found in implementation |
| ❌ Missing | PortInterface | - | Not found in implementation |
| ❌ Missing | PortInterfaceMapping | - | Not found in implementation |
| ❌ Missing | PortInterfaceMappingSet | - | Not found in implementation |
| ❌ Missing | SenderReceiverInterface | - | Not found in implementation |
| ❌ Missing | SubElementMapping | - | Not found in implementation |
| ❌ Missing | SubElementRef | - | Not found in implementation |
| ❌ Missing | TextTableMapping | - | Not found in implementation |
| ❌ Missing | TextTableValuePair | - | Not found in implementation |
| ❌ Missing | TriggerInterface | - | Not found in implementation |
| ❌ Missing | TriggerInterfaceMapping | - | Not found in implementation |
| ❌ Missing | VariableAndParameterInterfaceMapping | - | Not found in implementation |
| ➕ Extra | ApplicationCompositeElementInPortInterfaceInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/InstanceRefs.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | MappingDirectionEnum | bidirectional, firstToSecond, secondToFirst | - | - | Not found in implementation |
| ❌ Missing | ServerArgumentImplPolicyEnum | useArgumentType, useVoid | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::InstanceRefs

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ApplicationCompositeElementInPortInterfaceInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/InstanceRefs.py | Line 10 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

**Summary:**
- Classes: 0/18 implemented, 18 missing, 7 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbstractProvidedPortPrototype | - | Not found in implementation |
| ❌ Missing | AbstractRequiredPortPrototype | - | Not found in implementation |
| ❌ Missing | ApplicationSwComponentType | - | Not found in implementation |
| ❌ Missing | AtomicSwComponentType | - | Not found in implementation |
| ❌ Missing | ComplexDeviceDriverSwComponentType | - | Not found in implementation |
| ❌ Missing | EcuAbstractionSwComponentType | - | Not found in implementation |
| ❌ Missing | NvBlockSwComponentType | - | Not found in implementation |
| ❌ Missing | PPortPrototype | - | Not found in implementation |
| ❌ Missing | PRPortPrototype | - | Not found in implementation |
| ❌ Missing | ParameterSwComponentType | - | Not found in implementation |
| ❌ Missing | PortGroup | - | Not found in implementation |
| ❌ Missing | PortPrototype | - | Not found in implementation |
| ❌ Missing | RPortPrototype | - | Not found in implementation |
| ❌ Missing | SensorActuatorSwComponentType | - | Not found in implementation |
| ❌ Missing | ServiceProxySwComponentType | - | Not found in implementation |
| ❌ Missing | ServiceSwComponentType | - | Not found in implementation |
| ❌ Missing | SwComponentType | - | Not found in implementation |
| ❌ Missing | SymbolProps | - | Not found in implementation |
| ➕ Extra | InnerPortGroupInCompositionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | ModeGroupInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | PModeGroupInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | RModeGroupInAtomicSWCInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | RModeInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | RVariableInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | VariableInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs

**Summary:**
- Classes: 7/13 implemented, 6 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | InnerPortGroupInCompositionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Line 160 |
| ✅ Implemented | ModeGroupInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Line 14 |
| ✅ Implemented | PModeGroupInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Line 48 |
| ✅ Implemented | RModeGroupInAtomicSWCInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Line 69 |
| ✅ Implemented | RModeInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Line 91 |
| ✅ Implemented | RVariableInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Line 139 |
| ✅ Implemented | VariableInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py | Line 128 |
| ❌ Missing | OperationInAtomicSwcInstanceRef | - | Not found in implementation |
| ❌ Missing | POperationInAtomicSwcInstanceRef | - | Not found in implementation |
| ❌ Missing | PTriggerInAtomicSwcTypeInstanceRef | - | Not found in implementation |
| ❌ Missing | ROperationInAtomicSwcInstanceRef | - | Not found in implementation |
| ❌ Missing | RTriggerInAtomicSwcInstanceRef | - | Not found in implementation |
| ❌ Missing | TriggerInAtomicSwcInstanceRef | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SoftwareComponentDocumentation

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwComponentDocumentation | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SoftwareComponentDocumentation.py | Line 9 |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation

**Summary:**
- Classes: 1/2 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both SwcImplementation.py and SwcImplementation/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwcImplementation | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py | Line 10 |
| ❌ Missing | PerInstanceMemorySize | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition

**Summary:**
- Classes: 0/8 implemented, 8 missing, 6 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AssemblySwConnector | - | Not found in implementation |
| ❌ Missing | CompositionSwComponentType | - | Not found in implementation |
| ❌ Missing | DelegationSwConnector | - | Not found in implementation |
| ❌ Missing | InstantiationRTEEventProps | - | Not found in implementation |
| ❌ Missing | InstantiationTimingEventProps | - | Not found in implementation |
| ❌ Missing | PassThroughSwConnector | - | Not found in implementation |
| ❌ Missing | SwComponentPrototype | - | Not found in implementation |
| ❌ Missing | SwConnector | - | Not found in implementation |
| ➕ Extra | OperationInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | POperationInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | PPortInCompositionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | PortInCompositionTypeInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | ROperationInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | RPortInCompositionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs

**Summary:**
- Classes: 3/5 implemented, 2 missing, 3 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | PPortInCompositionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Line 44 |
| ✅ Implemented | PortInCompositionTypeInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Line 11 |
| ✅ Implemented | RPortInCompositionInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Line 66 |
| ❌ Missing | ComponentInCompositionInstanceRef | - | Not found in implementation |
| ❌ Missing | InstanceEventInCompositionInstanceRef | - | Not found in implementation |
| ➕ Extra | OperationInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | POperationInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | ROperationInAtomicSwcInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

**Summary:**
- Classes: 0/23 implemented, 23 missing
- Enums: 0/5 implemented, 5 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Communication/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ClientComSpec | - | Not found in implementation |
| ❌ Missing | CompositeNetworkRepresentation | - | Not found in implementation |
| ❌ Missing | ModeSwitchReceiverComSpec | - | Not found in implementation |
| ❌ Missing | ModeSwitchSenderComSpec | - | Not found in implementation |
| ❌ Missing | ModeSwitchedAckRequest | - | Not found in implementation |
| ❌ Missing | NonqueuedReceiverComSpec | - | Not found in implementation |
| ❌ Missing | NonqueuedSenderComSpec | - | Not found in implementation |
| ❌ Missing | NvProvideComSpec | - | Not found in implementation |
| ❌ Missing | NvRequireComSpec | - | Not found in implementation |
| ❌ Missing | PPortComSpec | - | Not found in implementation |
| ❌ Missing | ParameterProvideComSpec | - | Not found in implementation |
| ❌ Missing | ParameterRequireComSpec | - | Not found in implementation |
| ❌ Missing | QueuedReceiverComSpec | - | Not found in implementation |
| ❌ Missing | QueuedSenderComSpec | - | Not found in implementation |
| ❌ Missing | RPortComSpec | - | Not found in implementation |
| ❌ Missing | ReceiverComSpec | - | Not found in implementation |
| ❌ Missing | ReceptionComSpecProps | - | Not found in implementation |
| ❌ Missing | SenderComSpec | - | Not found in implementation |
| ❌ Missing | ServerComSpec | - | Not found in implementation |
| ❌ Missing | TransformationComSpecProps | - | Not found in implementation |
| ❌ Missing | TransmissionAcknowledgementRequest | - | Not found in implementation |
| ❌ Missing | TransmissionComSpecProps | - | Not found in implementation |
| ❌ Missing | UserDefinedTransformationComSpecProps | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | HandleInvalidEnum | dontInvalidate, external, keep, replace | - | - | Not found in implementation |
| ❌ Missing | HandleOutOfRangeEnum | default, externalReplacement, ignore, invalid, none, saturate | - | - | Not found in implementation |
| ❌ Missing | HandleOutOfRangeStatusEnum | indicate, silent | - | - | Not found in implementation |
| ❌ Missing | HandleTimeoutEnum | none, replace, replaceByTimeoutSubstitutionValue | - | - | Not found in implementation |
| ❌ Missing | TransmissionModeDefinitionEnum | cyclic, cyclicAndOn, triggered | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes

**Summary:**
- Classes: 0/10 implemented, 10 missing
- Enums: 0/5 implemented, 5 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ApplicationAttributes/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ClientServerAnnotation | - | Not found in implementation |
| ❌ Missing | DelegatedPortAnnotation | - | Not found in implementation |
| ❌ Missing | IoHwAbstractionServerAnnotation | - | Not found in implementation |
| ❌ Missing | ModePortAnnotation | - | Not found in implementation |
| ❌ Missing | NvDataPortAnnotation | - | Not found in implementation |
| ❌ Missing | ParameterPortAnnotation | - | Not found in implementation |
| ❌ Missing | ReceiverAnnotation | - | Not found in implementation |
| ❌ Missing | SenderAnnotation | - | Not found in implementation |
| ❌ Missing | SenderReceiverAnnotation | - | Not found in implementation |
| ❌ Missing | TriggerPortAnnotation | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DataLimitKindEnum | max, Software, AUTOSAR, min, none | - | - | Not found in implementation |
| ❌ Missing | FilterDebouncingEnum | debounceData, rawData, waitTimeDate | - | - | Not found in implementation |
| ❌ Missing | ProcessingKindEnum | filtered, none, raw | - | - | Not found in implementation |
| ❌ Missing | PulseTestEnum | disable, enable | - | - | Not found in implementation |
| ❌ Missing | SignalFanEnum | nfold, single | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory EndToEndProtection/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | EndToEndDescription | - | Not found in implementation |
| ❌ Missing | EndToEndProtection | - | Not found in implementation |
| ❌ Missing | EndToEndProtectionSet | - | Not found in implementation |
| ❌ Missing | EndToEndProtectionVariablePrototype | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ConsistencyNeeds | - | Not found in implementation |
| ❌ Missing | DataPrototypeGroup | - | Not found in implementation |
| ❌ Missing | RunnableEntityGroup | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InstanceRef/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | InnerDataPrototypeGroupInCompositionInstanceRef | - | Not found in implementation |
| ❌ Missing | InnerRunnableEntityGroupInCompositionInstanceRef | - | Not found in implementation |
| ❌ Missing | RunnableEntityInCompositionInstanceRef | - | Not found in implementation |
| ❌ Missing | VariableDataPrototypeInCompositionInstanceRef | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InterpolationRoutine/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | InterpolationRoutine | - | Not found in implementation |
| ❌ Missing | InterpolationRoutineMapping | - | Not found in implementation |
| ❌ Missing | InterpolationRoutineMappingSet | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::CalibrationParameter

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CalibrationParameter/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | CalibrationParameterValue | - | Not found in implementation |
| ❌ Missing | CalibrationParameterValueSet | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::AutosarTopLevelStructure

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory AutosarTopLevelStructure/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AUTOSAR | - | Not found in implementation |
| ❌ Missing | FileInfoComment | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate

**Summary:**
- Classes: 0/11 implemented, 11 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ECUCDescriptionTemplate/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | EcucAbstractReferenceValue | - | Not found in implementation |
| ❌ Missing | EcucAddInfoParamValue | - | Not found in implementation |
| ❌ Missing | EcucContainerValue | - | Not found in implementation |
| ❌ Missing | EcucIndexableValue | - | Not found in implementation |
| ❌ Missing | EcucInstanceReferenceValue | - | Not found in implementation |
| ❌ Missing | EcucModuleConfigurationValues | - | Not found in implementation |
| ❌ Missing | EcucNumericalParamValue | - | Not found in implementation |
| ❌ Missing | EcucParameterValue | - | Not found in implementation |
| ❌ Missing | EcucReferenceValue | - | Not found in implementation |
| ❌ Missing | EcucTextualParamValue | - | Not found in implementation |
| ❌ Missing | EcucValueCollection | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

**Summary:**
- Classes: 0/40 implemented, 40 missing
- Enums: 0/4 implemented, 4 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ECUCParameterDefTemplate/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | EcucAbstractConfigurationClass | - | Not found in implementation |
| ❌ Missing | EcucAbstractExternalReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucAbstractInternalReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucAbstractReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucAbstractStringParamDef | - | Not found in implementation |
| ❌ Missing | EcucAddInfoParamDef | - | Not found in implementation |
| ❌ Missing | EcucBooleanParamDef | - | Not found in implementation |
| ❌ Missing | EcucChoiceContainerDef | - | Not found in implementation |
| ❌ Missing | EcucChoiceReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucCommonAttributes | - | Not found in implementation |
| ❌ Missing | EcucConditionFormula | - | Not found in implementation |
| ❌ Missing | EcucConditionSpecification | - | Not found in implementation |
| ❌ Missing | EcucContainerDef | - | Not found in implementation |
| ❌ Missing | EcucDefinitionCollection | - | Not found in implementation |
| ❌ Missing | EcucDefinitionElement | - | Not found in implementation |
| ❌ Missing | EcucDerivationSpecification | - | Not found in implementation |
| ❌ Missing | EcucDestinationUriDef | - | Not found in implementation |
| ❌ Missing | EcucDestinationUriDefSet | - | Not found in implementation |
| ❌ Missing | EcucDestinationUriPolicy | - | Not found in implementation |
| ❌ Missing | EcucEnumerationLiteralDef | - | Not found in implementation |
| ❌ Missing | EcucEnumerationParamDef | - | Not found in implementation |
| ❌ Missing | EcucFloatParamDef | - | Not found in implementation |
| ❌ Missing | EcucForeignReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucFunctionNameDef | - | Not found in implementation |
| ❌ Missing | EcucInstanceReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucIntegerParamDef | - | Not found in implementation |
| ❌ Missing | EcucLinkerSymbolDef | - | Not found in implementation |
| ❌ Missing | EcucModuleDef | - | Not found in implementation |
| ❌ Missing | EcucMultilineStringParamDef | - | Not found in implementation |
| ❌ Missing | EcucMultiplicityConfigurationClass | - | Not found in implementation |
| ❌ Missing | EcucParamConfContainerDef | - | Not found in implementation |
| ❌ Missing | EcucParameterDef | - | Not found in implementation |
| ❌ Missing | EcucParameterDerivationFormula | - | Not found in implementation |
| ❌ Missing | EcucQuery | - | Not found in implementation |
| ❌ Missing | EcucQueryExpression | - | Not found in implementation |
| ❌ Missing | EcucReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucStringParamDef | - | Not found in implementation |
| ❌ Missing | EcucUriReferenceDef | - | Not found in implementation |
| ❌ Missing | EcucValidationCondition | - | Not found in implementation |
| ❌ Missing | EcucValueConfigurationClass | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | EcucConfigurationClassEnum | Link, PostBuild, PreCompile, Published | - | - | Not found in implementation |
| ❌ Missing | EcucConfigurationVariantEnum | PreconfiguredConfiguration, AUTOSAR, RecommendedConfiguration, VariantLinkTime, VariantPostBuild, VariantPreCompile | - | - | Not found in implementation |
| ❌ Missing | EcucDestinationUriNestingContractEnum | leafOfTarget, targetContainer, vertexOfTarget | - | - | Not found in implementation |
| ❌ Missing | EcucScopeEnum | ECU, local | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate

**Summary:**
- Classes: 0/8 implemented, 8 missing, 168 extra
- Enums: 0/0 implemented, 6 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ClientIdDefinition | - | Not found in implementation |
| ❌ Missing | ClientIdDefinitionSet | - | Not found in implementation |
| ❌ Missing | ComManagementMapping | - | Not found in implementation |
| ❌ Missing | J1939SharedAddressCluster | - | Not found in implementation |
| ❌ Missing | PortElementToCommunicationResourceMapping | - | Not found in implementation |
| ❌ Missing | RootSwCompositionPrototype | - | Not found in implementation |
| ❌ Missing | System | - | Not found in implementation |
| ❌ Missing | SystemMapping | - | Not found in implementation |
| ➕ Extra | AbstractCanCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | AbstractCanCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | AbstractCanCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | AbstractCanCommunicationControllerAttributes | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | AbstractCanPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | AbstractDoIpLogicAddressProps | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIP.py | Not documented in requirements |
| ➕ Extra | AbstractEthernetFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetFrame.py | Not documented in requirements |
| ➕ Extra | AbstractServiceInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | AppOsTaskProxyToEcuTaskProxyMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/RteEventToOsTaskMapping.py | Not documented in requirements |
| ➕ Extra | ApplicationEndpoint | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | ApplicationEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | ApplicationPartitionToEcuPartitionMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SWmapping.py | Not documented in requirements |
| ➕ Extra | BusspecificNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | CanCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanClusterBusOffRecovery | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | CanCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | CanControllerConfigurationRequirements | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | CanControllerFdConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | CanControllerFdConfigurationRequirements | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | CanControllerXlConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | CanControllerXlConfigurationRequirements | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Not documented in requirements |
| ➕ Extra | CanFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py | Not documented in requirements |
| ➕ Extra | CanFrameTriggering | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py | Not documented in requirements |
| ➕ Extra | CanNmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | CanNmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | CanNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | CanNmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | CanPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanTpAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | CanTpChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | CanTpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | CanTpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | CanTpEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | CanTpNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | CommConnectorPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationCycle | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationDirectionType | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | ComponentInSystemInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | ConsumedEventGroup | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | ConsumedServiceInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | CouplingPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | CouplingPortDetails | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | CouplingPortFifo | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | CouplingPortScheduler | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | CouplingPortStructuralElement | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | CryptoServiceMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py | Not documented in requirements |
| ➕ Extra | CycleCounter | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleRepetition | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleRepetitionType | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | DataMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | DefaultValueElement | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Not documented in requirements |
| ➕ Extra | DiagnosticConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DiagnosticConnection.py | Not documented in requirements |
| ➕ Extra | DoIpEntity | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | DoIpLogicAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | DoIpLogicTargetAddressProps | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIP.py | Not documented in requirements |
| ➕ Extra | DoIpLogicTesterAddressProps | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIP.py | Not documented in requirements |
| ➕ Extra | DoIpTpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | DoIpTpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | ECUMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/ECUResourceMapping.py | Not documented in requirements |
| ➕ Extra | EcuInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py | Not documented in requirements |
| ➕ Extra | EthernetCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | EthernetCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | EthernetCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | EthernetPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | EthernetPriorityRegeneration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | EventHandler | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | FlexrayAbsolutelyScheduledTiming | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py | Not documented in requirements |
| ➕ Extra | FlexrayChannelName | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py | Not documented in requirements |
| ➕ Extra | FlexrayFrameTriggering | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py | Not documented in requirements |
| ➕ Extra | FlexrayNmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | FlexrayNmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | FlexrayNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | FlexrayNmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | FlexrayPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FrameMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Not documented in requirements |
| ➕ Extra | FramePort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FreeFormatEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | Gateway | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Not documented in requirements |
| ➕ Extra | GenericEthernetFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetFrame.py | Not documented in requirements |
| ➕ Extra | GenericTp | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | IPduMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Not documented in requirements |
| ➕ Extra | IPduPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduSignalProcessingEnum | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | ISignalMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Not documented in requirements |
| ➕ Extra | ISignalPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IndexedArrayElement | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | InfrastructureServices | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | InitialSdDelayConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | Ipv4Configuration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | Ipv6Configuration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | J1939NmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | J1939NmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | J1939NmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | LinCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | LinCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py | Not documented in requirements |
| ➕ Extra | LinCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py | Not documented in requirements |
| ➕ Extra | LinConfigurationEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | LinFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | LinFrameTriggering | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | LinMaster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py | Not documented in requirements |
| ➕ Extra | LinPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | LinScheduleTable | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | LinTpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | LinTpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | LinTpNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | LinUnconditionalFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | MacMulticastGroup | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | NetworkEndpoint | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | NetworkEndpointAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | NmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | NmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | NmConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | NmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | NmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | PduMappingDefaultValue | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Not documented in requirements |
| ➕ Extra | PhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | PncGatewayTypeEnum | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | ProvidedServiceInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | RequestResponseDelay | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | ResumePosition | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | RxIdentifierRange | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py | Not documented in requirements |
| ➕ Extra | ScheduleTableEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |
| ➕ Extra | SdClientConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | SdServerConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | SecOcCryptoServiceMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py | Not documented in requirements |
| ➕ Extra | SenderRecArrayElementMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | SenderRecArrayTypeMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | SenderRecCompositeTypeMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | SenderRecRecordElementMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | SenderRecRecordTypeMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | SenderReceiverToSignalGroupMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | SenderReceiverToSignalMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Not documented in requirements |
| ➕ Extra | SoAdConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | SoAdRoutingGroup | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py | Not documented in requirements |
| ➕ Extra | SocketAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | SocketConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py | Not documented in requirements |
| ➕ Extra | SocketConnectionBundle | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py | Not documented in requirements |
| ➕ Extra | SocketConnectionIpduIdentifier | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py | Not documented in requirements |
| ➕ Extra | SwcToImplMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SWmapping.py | Not documented in requirements |
| ➕ Extra | TargetIPduRef | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Not documented in requirements |
| ➕ Extra | TcpTp | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | TcpUdpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | TimeSyncClientConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | TimeSyncServerConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | TimeSynchronization | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py | Not documented in requirements |
| ➕ Extra | TlsCryptoServiceMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py | Not documented in requirements |
| ➕ Extra | TpAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | TpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | TpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | TpConnectionIdent | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | TpPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | TransportProtocolConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | UdpNmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | UdpNmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | UdpNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | UdpNmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Not documented in requirements |
| ➕ Extra | UdpTp | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | VariableDataPrototypeInSystemInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py | Not documented in requirements |
| ➕ Extra | VlanConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | VlanMembership | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ➕ Extra | CommunicationDirectionType | - | in, out | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleRepetitionType | - | - | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayChannelName | - | channelA, channelB | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduSignalProcessingEnum | - | deferred, immediate | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | PncGatewayTypeEnum | - | active, none, passive | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | ResumePosition | - | continueAtItPosition, startFromBeginning | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection

**Summary:**
- Classes: 1/4 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both DiagnosticConnection.py and DiagnosticConnection/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | DiagnosticConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DiagnosticConnection.py | Line 8 |
| ❌ Missing | DoIpTpConnection | - | Not found in implementation |
| ❌ Missing | TpConnection | - | Not found in implementation |
| ❌ Missing | TpConnectionIdent | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore

**Summary:**
- Classes: 0/1 implemented, 1 missing, 27 extra
- Enums: 0/0 implemented, 5 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | FibexElement | - | Not found in implementation |
| ➕ Extra | AbstractCanCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | AbstractCanPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanClusterBusOffRecovery | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommConnectorPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationCycle | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationDirectionType | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleCounter | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleRepetition | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleRepetitionType | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | EcuInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py | Not documented in requirements |
| ➕ Extra | EthernetPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayChannelName | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FramePort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduSignalProcessingEnum | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | ISignalPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | LinCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | LinPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | PhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | PncGatewayTypeEnum | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | VlanConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ➕ Extra | CommunicationDirectionType | - | in, out | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleRepetitionType | - | - | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayChannelName | - | channelA, channelB | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduSignalProcessingEnum | - | deferred, immediate | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | PncGatewayTypeEnum | - | active, none, passive | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

**Summary:**
- Classes: 8/10 implemented, 2 missing, 18 extra
- Enums: 2/2 implemented, 1 literal mismatches, 3 extra

⚠️ **Structure Mismatch Warning**

Hybrid structure: both CoreTopology.py and CoreTopology/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | CommConnectorPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 570 |
| ✅ Implemented | CommunicationCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 313 |
| ✅ Implemented | CommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 723 |
| ✅ Implemented | CommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 515 |
| ✅ Implemented | CommunicationCycle | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 17 |
| ✅ Implemented | CycleCounter | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 30 |
| ✅ Implemented | CycleRepetition | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 59 |
| ✅ Implemented | PhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 88 |
| ❌ Missing | ClientIdRange | - | Not found in implementation |
| ❌ Missing | EcuInstance | - | Not found in implementation |
| ➕ Extra | AbstractCanCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | AbstractCanPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanClusterBusOffRecovery | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CanPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CommunicationDirectionType | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | CycleRepetitionType | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | EthernetPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayChannelName | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FramePort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduSignalProcessingEnum | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | ISignalPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | LinCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | LinPhysicalChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | PncGatewayTypeEnum | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | VlanConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | CycleRepetitionType | AUTOSAR, System, cycleRepetition1, cycleRepetition10, cycleRepetition16, cycleRepetition2, cycleRepetition20, cycleRepetition32, cycleRepetition4, cycleRepetition40, cycleRepetition5, cycleRepetition50, cycleRepetition64, cycleRepetition8 | - | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 49; Missing: AUTOSAR, System, cycleRepetition1, cycleRepetition10, cycleRepetition16, cycleRepetition2, cycleRepetition20, cycleRepetition32, cycleRepetition4, cycleRepetition40, cycleRepetition5, cycleRepetition50, cycleRepetition64, cycleRepetition8 |
| ✅ Implemented | PncGatewayTypeEnum | active, none, passive | active, none, passive | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Line 537 |
| ➕ Extra | CommunicationDirectionType | - | in, out | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | FlexrayChannelName | - | channelA, channelB | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |
| ➕ Extra | IPduSignalProcessingEnum | - | deferred, immediate | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication

**Summary:**
- Classes: 0/41 implemented, 41 missing
- Enums: 0/11 implemented, 11 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ContainedIPduProps | - | Not found in implementation |
| ❌ Missing | ContainerIPdu | - | Not found in implementation |
| ❌ Missing | DcmIPdu | - | Not found in implementation |
| ❌ Missing | DynamicPart | - | Not found in implementation |
| ❌ Missing | DynamicPartAlternative | - | Not found in implementation |
| ❌ Missing | Frame | - | Not found in implementation |
| ❌ Missing | FramePort | - | Not found in implementation |
| ❌ Missing | FrameTriggering | - | Not found in implementation |
| ❌ Missing | GeneralPurposeIPdu | - | Not found in implementation |
| ❌ Missing | GeneralPurposePdu | - | Not found in implementation |
| ❌ Missing | IPdu | - | Not found in implementation |
| ❌ Missing | IPduPort | - | Not found in implementation |
| ❌ Missing | IPduTiming | - | Not found in implementation |
| ❌ Missing | ISignal | - | Not found in implementation |
| ❌ Missing | ISignalGroup | - | Not found in implementation |
| ❌ Missing | ISignalIPdu | - | Not found in implementation |
| ❌ Missing | ISignalIPduGroup | - | Not found in implementation |
| ❌ Missing | ISignalPort | - | Not found in implementation |
| ❌ Missing | ISignalProps | - | Not found in implementation |
| ❌ Missing | ISignalToIPduMapping | - | Not found in implementation |
| ❌ Missing | ISignalTriggering | - | Not found in implementation |
| ❌ Missing | J1939DcmIPdu | - | Not found in implementation |
| ❌ Missing | MultiplexedIPdu | - | Not found in implementation |
| ❌ Missing | MultiplexedPart | - | Not found in implementation |
| ❌ Missing | NPdu | - | Not found in implementation |
| ❌ Missing | NmPdu | - | Not found in implementation |
| ❌ Missing | Pdu | - | Not found in implementation |
| ❌ Missing | PduToFrameMapping | - | Not found in implementation |
| ❌ Missing | PduTriggering | - | Not found in implementation |
| ❌ Missing | PdurIPduGroup | - | Not found in implementation |
| ❌ Missing | SecureCommunicationAuthenticationProps | - | Not found in implementation |
| ❌ Missing | SecureCommunicationFreshnessProps | - | Not found in implementation |
| ❌ Missing | SecureCommunicationProps | - | Not found in implementation |
| ❌ Missing | SecureCommunicationPropsSet | - | Not found in implementation |
| ❌ Missing | SecuredIPdu | - | Not found in implementation |
| ❌ Missing | SegmentPosition | - | Not found in implementation |
| ❌ Missing | StaticPart | - | Not found in implementation |
| ❌ Missing | SystemSignal | - | Not found in implementation |
| ❌ Missing | SystemSignalGroup | - | Not found in implementation |
| ❌ Missing | UserDefinedIPdu | - | Not found in implementation |
| ❌ Missing | UserDefinedPdu | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | CommunicationDirectionType | in, out | - | - | Not found in implementation |
| ❌ Missing | ContainedIPduCollectionSemanticsEnum | lastIsBest, queued | - | - | Not found in implementation |
| ❌ Missing | ContainerIPduHeaderTypeEnum | longHeader, noHeader, shortHeader | - | - | Not found in implementation |
| ❌ Missing | ContainerIPduTriggerEnum | defaultTrigger, firstContained, Trigger | - | - | Not found in implementation |
| ❌ Missing | DiagPduType | diagRequest, diagResponse | - | - | Not found in implementation |
| ❌ Missing | IPduSignalProcessingEnum | deferred, immediate | - | - | Not found in implementation |
| ❌ Missing | ISignalTypeEnum | array, primitive | - | - | Not found in implementation |
| ❌ Missing | RxAcceptContainedIPduEnum | acceptAll, acceptConfigured | - | - | Not found in implementation |
| ❌ Missing | SecuredPduHeaderEnum | noHeader, System, AUTOSARsecuredPduHeader08Bit, securedPduHeader16Bit, securedPduHeader32Bit | - | - | Not found in implementation |
| ❌ Missing | TransferPropertyEnum | pending, triggered, triggeredOnChange, triggeredOnChange, triggeredWithout, Repetition | - | - | Not found in implementation |
| ❌ Missing | TriggerMode | dynamicPartTrigger, none, staticOrDynamicPartTrigger, staticPartTrigger | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing

**Summary:**
- Classes: 0/10 implemented, 10 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Timing/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbsoluteTolerance | - | Not found in implementation |
| ❌ Missing | CyclicTiming | - | Not found in implementation |
| ❌ Missing | EventControlledTiming | - | Not found in implementation |
| ❌ Missing | ModeDrivenTransmissionModeCondition | - | Not found in implementation |
| ❌ Missing | RelativeTolerance | - | Not found in implementation |
| ❌ Missing | TimeRangeType | - | Not found in implementation |
| ❌ Missing | TransmissionModeCondition | - | Not found in implementation |
| ❌ Missing | TransmissionModeDeclaration | - | Not found in implementation |
| ❌ Missing | TransmissionModeTiming | - | Not found in implementation |
| ❌ Missing | TriggerIPduSendCondition | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

**Summary:**
- Classes: 11/79 implemented, 68 missing, 3 extra
- Enums: 0/16 implemented, 16 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both EthernetTopology.py and EthernetTopology/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | CouplingPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 345 |
| ✅ Implemented | CouplingPortDetails | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 196 |
| ✅ Implemented | CouplingPortFifo | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 91 |
| ✅ Implemented | CouplingPortScheduler | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 138 |
| ✅ Implemented | CouplingPortStructuralElement | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 78 |
| ✅ Implemented | EthernetCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 29 |
| ✅ Implemented | EthernetCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 560 |
| ✅ Implemented | EthernetCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 482 |
| ✅ Implemented | EthernetPriorityRegeneration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 167 |
| ✅ Implemented | MacMulticastGroup | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 9 |
| ✅ Implemented | VlanMembership | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Line 298 |
| ❌ Missing | ApplicationEndpoint | - | Not found in implementation |
| ❌ Missing | CouplingElement | - | Not found in implementation |
| ❌ Missing | CouplingElementAbstractDetails | - | Not found in implementation |
| ❌ Missing | CouplingElementSwitchDetails | - | Not found in implementation |
| ❌ Missing | CouplingPortAsynchronousTrafficShaper | - | Not found in implementation |
| ❌ Missing | CouplingPortConnection | - | Not found in implementation |
| ❌ Missing | CouplingPortCreditBasedShaper | - | Not found in implementation |
| ❌ Missing | CouplingPortRatePolicy | - | Not found in implementation |
| ❌ Missing | CouplingPortShaper | - | Not found in implementation |
| ❌ Missing | CouplingPortTrafficClassAssignment | - | Not found in implementation |
| ❌ Missing | DhcpServerConfiguration | - | Not found in implementation |
| ❌ Missing | Dhcpv6Props | - | Not found in implementation |
| ❌ Missing | DoIpEntity | - | Not found in implementation |
| ❌ Missing | EthIpProps | - | Not found in implementation |
| ❌ Missing | EthTcpIpIcmpProps | - | Not found in implementation |
| ❌ Missing | EthTcpIpProps | - | Not found in implementation |
| ❌ Missing | EthernetPhysicalChannel | - | Not found in implementation |
| ❌ Missing | EthernetWakeupSleepOnDatalineConfig | - | Not found in implementation |
| ❌ Missing | EthernetWakeupSleepOnDatalineConfigSet | - | Not found in implementation |
| ❌ Missing | GenericTp | - | Not found in implementation |
| ❌ Missing | GlobalTimeCouplingPortProps | - | Not found in implementation |
| ❌ Missing | HttpTp | - | Not found in implementation |
| ❌ Missing | Ieee1722Tp | - | Not found in implementation |
| ❌ Missing | InfrastructureServices | - | Not found in implementation |
| ❌ Missing | Ipv4ArpProps | - | Not found in implementation |
| ❌ Missing | Ipv4AutoIpProps | - | Not found in implementation |
| ❌ Missing | Ipv4Configuration | - | Not found in implementation |
| ❌ Missing | Ipv4DhcpServerConfiguration | - | Not found in implementation |
| ❌ Missing | Ipv4FragmentationProps | - | Not found in implementation |
| ❌ Missing | Ipv4Props | - | Not found in implementation |
| ❌ Missing | Ipv6Configuration | - | Not found in implementation |
| ❌ Missing | Ipv6DhcpServerConfiguration | - | Not found in implementation |
| ❌ Missing | Ipv6FragmentationProps | - | Not found in implementation |
| ❌ Missing | Ipv6NdpProps | - | Not found in implementation |
| ❌ Missing | Ipv6Props | - | Not found in implementation |
| ❌ Missing | MacMulticastConfiguration | - | Not found in implementation |
| ❌ Missing | NetworkEndpoint | - | Not found in implementation |
| ❌ Missing | NetworkEndpointAddress | - | Not found in implementation |
| ❌ Missing | OrderedMaster | - | Not found in implementation |
| ❌ Missing | PlcaProps | - | Not found in implementation |
| ❌ Missing | RtpTp | - | Not found in implementation |
| ❌ Missing | StreamFilterIEEE1722Tp | - | Not found in implementation |
| ❌ Missing | StreamFilterIpv4Address | - | Not found in implementation |
| ❌ Missing | StreamFilterIpv6Address | - | Not found in implementation |
| ❌ Missing | StreamFilterMACAddress | - | Not found in implementation |
| ❌ Missing | StreamFilterPortRange | - | Not found in implementation |
| ❌ Missing | StreamFilterRuleDataLinkLayer | - | Not found in implementation |
| ❌ Missing | StreamFilterRuleIpTp | - | Not found in implementation |
| ❌ Missing | SwitchAsynchronousTrafficShaperGroupEntry | - | Not found in implementation |
| ❌ Missing | SwitchFlowMeteringEntry | - | Not found in implementation |
| ❌ Missing | SwitchStreamFilterActionDestPortModification | - | Not found in implementation |
| ❌ Missing | SwitchStreamFilterEntry | - | Not found in implementation |
| ❌ Missing | SwitchStreamFilterRule | - | Not found in implementation |
| ❌ Missing | SwitchStreamGateEntry | - | Not found in implementation |
| ❌ Missing | SwitchStreamIdentification | - | Not found in implementation |
| ❌ Missing | TcpIpIcmpv4Props | - | Not found in implementation |
| ❌ Missing | TcpIpIcmpv6Props | - | Not found in implementation |
| ❌ Missing | TcpProps | - | Not found in implementation |
| ❌ Missing | TcpTp | - | Not found in implementation |
| ❌ Missing | TcpUdpConfig | - | Not found in implementation |
| ❌ Missing | TimeSyncClientConfiguration | - | Not found in implementation |
| ❌ Missing | TimeSyncServerConfiguration | - | Not found in implementation |
| ❌ Missing | TimeSynchronization | - | Not found in implementation |
| ❌ Missing | TpPort | - | Not found in implementation |
| ❌ Missing | TransportProtocolConfiguration | - | Not found in implementation |
| ❌ Missing | UdpProps | - | Not found in implementation |
| ❌ Missing | UdpTp | - | Not found in implementation |
| ❌ Missing | VlanConfig | - | Not found in implementation |
| ➕ Extra | InitialSdDelayConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | RequestResponseDelay | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |
| ➕ Extra | SdClientConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | CouplingElementEnum | hub, router, switch | - | - | Not found in implementation |
| ❌ Missing | CouplingPortRatePolicyActionEnum | blockSource, dropFrame | - | - | Not found in implementation |
| ❌ Missing | CouplingPortRoleEnum | hostPortElement, standardPort, upLinkPortECU | - | - | Not found in implementation |
| ❌ Missing | DoIpEntityRoleEnum | edgeNode, gateway, node | - | - | Not found in implementation |
| ❌ Missing | EthernetConnectionNegotiationEnum | auto, master, slave | - | - | Not found in implementation |
| ❌ Missing | EthernetCouplingPortSchedulerEnum | deficitRoundRobin, strictPriority, weightedRoundRobin | - | - | Not found in implementation |
| ❌ Missing | EthernetMacLayerTypeEnum | xGMII, xMII, xXGMII | - | - | Not found in implementation |
| ❌ Missing | EthernetPhysicalLayerTypeEnum | _1000BASE_T, _1000BASE_T1, _100BASE_T1, _100BASE_TX, _10BASE_T1S, iEEE802_11P | - | - | Not found in implementation |
| ❌ Missing | EthernetSwitchVlanEgressTaggingEnum | notSent | - | - | Not found in implementation |
| ❌ Missing | EthernetSwitchVlanIngressTagEnum | dropUntagged, forwardAsIs | - | - | Not found in implementation |
| ❌ Missing | FlowMeteringColorModeEnum | colorAware, System, AUTOSAR, colorBlind | - | - | Not found in implementation |
| ❌ Missing | IpAddressKeepEnum | forget, storePersistently | - | - | Not found in implementation |
| ❌ Missing | Ipv4AddressSourceEnum | autoIp, autoIp_doip, dhcpv4, fixed | - | - | Not found in implementation |
| ❌ Missing | Ipv6AddressSourceEnum | dhcpv6, fixed, linkLocal, linkLocal_doip, routerAdvertisement | - | - | Not found in implementation |
| ❌ Missing | SwitchStreamFilterActionPortModificationEnum | extend, overwrite | - | - | Not found in implementation |
| ❌ Missing | TimeSyncTechnologyEnum | System, AUTOSAR, avb_ieee802_1AS, ntp_rfc958, ptp_ieee1588_2002, ptp_ieee1588_2008 | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances

**Summary:**
- Classes: 8/20 implemented, 12 missing, 8 extra
- Enums: 0/6 implemented, 6 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both ServiceInstances.py and ServiceInstances/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AbstractServiceInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 185 |
| ✅ Implemented | ConsumedEventGroup | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 234 |
| ✅ Implemented | ConsumedServiceInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 326 |
| ✅ Implemented | EventHandler | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 585 |
| ✅ Implemented | InitialSdDelayConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 464 |
| ✅ Implemented | ProvidedServiceInstance | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 641 |
| ✅ Implemented | SoAdConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 886 |
| ✅ Implemented | SocketAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Line 771 |
| ❌ Missing | ConsumedProvidedServiceInstanceGroup | - | Not found in implementation |
| ❌ Missing | PduActivationRoutingGroup | - | Not found in implementation |
| ❌ Missing | RequestResponseDelay | - | Not found in implementation |
| ❌ Missing | ServiceInstanceCollectionSet | - | Not found in implementation |
| ❌ Missing | SoConIPduIdentifier | - | Not found in implementation |
| ❌ Missing | SocketConnectionIpduIdentifierSet | - | Not found in implementation |
| ❌ Missing | SomeipSdClientEventGroupTimingConfig | - | Not found in implementation |
| ❌ Missing | SomeipSdClientServiceInstanceConfig | - | Not found in implementation |
| ❌ Missing | SomeipSdServerEventGroupTimingConfig | - | Not found in implementation |
| ❌ Missing | SomeipSdServerServiceInstanceConfig | - | Not found in implementation |
| ❌ Missing | SomeipServiceVersion | - | Not found in implementation |
| ❌ Missing | StaticSocketConnection | - | Not found in implementation |
| ➕ Extra | ApplicationEndpoint | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | GenericTp | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | SdServerConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | TcpTp | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | TcpUdpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | TpPort | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | TransportProtocolConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |
| ➕ Extra | UdpTp | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | EventGroupControlTypeEnum | activationAnd, activationMulticast, activationUnicast, triggerUnicast | - | - | Not found in implementation |
| ❌ Missing | PduCollectionSemanticsEnum | lastIsBest, queued | - | - | Not found in implementation |
| ❌ Missing | PduCollectionTriggerEnum | always, never | - | - | Not found in implementation |
| ❌ Missing | ServiceVersionAcceptanceKindEnum | exactOrAnyMinor, System, AUTOSAR, minimumMinor | - | - | Not found in implementation |
| ❌ Missing | TcpRoleEnum | connect, listen | - | - | Not found in implementation |
| ❌ Missing | UdpChecksumCalculationEnum | udpChecksumDisabled, udpChecksumEnabled | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds

**Summary:**
- Classes: 0/25 implemented, 25 missing
- Enums: 0/7 implemented, 7 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Dds/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DdsCpConfig | - | Not found in implementation |
| ❌ Missing | DdsCpConsumedServiceInstance | - | Not found in implementation |
| ❌ Missing | DdsCpDomain | - | Not found in implementation |
| ❌ Missing | DdsCpISignalToDdsTopicMapping | - | Not found in implementation |
| ❌ Missing | DdsCpPartition | - | Not found in implementation |
| ❌ Missing | DdsCpProvidedServiceInstance | - | Not found in implementation |
| ❌ Missing | DdsCpQosProfile | - | Not found in implementation |
| ❌ Missing | DdsCpServiceInstance | - | Not found in implementation |
| ❌ Missing | DdsCpServiceInstanceEvent | - | Not found in implementation |
| ❌ Missing | DdsCpServiceInstanceOperation | - | Not found in implementation |
| ❌ Missing | DdsCpTopic | - | Not found in implementation |
| ❌ Missing | DdsDeadline | - | Not found in implementation |
| ❌ Missing | DdsDestinationOrder | - | Not found in implementation |
| ❌ Missing | DdsDurability | - | Not found in implementation |
| ❌ Missing | DdsDurabilityService | - | Not found in implementation |
| ❌ Missing | DdsHistory | - | Not found in implementation |
| ❌ Missing | DdsLatencyBudget | - | Not found in implementation |
| ❌ Missing | DdsLifespan | - | Not found in implementation |
| ❌ Missing | DdsLiveliness | - | Not found in implementation |
| ❌ Missing | DdsOwnership | - | Not found in implementation |
| ❌ Missing | DdsOwnershipStrength | - | Not found in implementation |
| ❌ Missing | DdsReliability | - | Not found in implementation |
| ❌ Missing | DdsResourceLimits | - | Not found in implementation |
| ❌ Missing | DdsTopicData | - | Not found in implementation |
| ❌ Missing | DdsTransportPriority | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DdsDestinationOrderKindEnum | byReceptionTimestampbySourceTimestamp | - | - | Not found in implementation |
| ❌ Missing | DdsDurabilityKindEnum | persistenttransienttransientLocalvolatile | - | - | Not found in implementation |
| ❌ Missing | DdsDurabilityServiceHistoryKindEnum | keepAllkeepLast | - | - | Not found in implementation |
| ❌ Missing | DdsHistoryKindEnum | keepAllkeepLast | - | - | Not found in implementation |
| ❌ Missing | DdsLivenessKindEnum | automaticmanualByParticipantmanualByTopic | - | - | Not found in implementation |
| ❌ Missing | DdsOwnershipKindEnum | exclusiveshared | - | - | Not found in implementation |
| ❌ Missing | DdsReliabilityKindEnum | bestEffortreliable | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory IPv6HeaderFilterList/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | IPv6ExtHeaderFilterList | - | Not found in implementation |
| ❌ Missing | IPv6ExtHeaderFilterSet | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TcpOptionFilterSet/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | TcpOptionFilterList | - | Not found in implementation |
| ❌ Missing | TcpOptionFilterSet | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetFrame

**Summary:**
- Classes: 2/5 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both EthernetFrame.py and EthernetFrame/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AbstractEthernetFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetFrame.py | Line 9 |
| ✅ Implemented | GenericEthernetFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetFrame.py | Line 23 |
| ❌ Missing | EthernetFrameTriggering | - | Not found in implementation |
| ❌ Missing | Ieee1722TpEthernetFrame | - | Not found in implementation |
| ❌ Missing | UserDefinedEthernetFrame | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ObsoleteModel

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ObsoleteModel/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | SoAdRoutingGroup | - | Not found in implementation |
| ❌ Missing | SocketConnection | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology

**Summary:**
- Classes: 10/17 implemented, 7 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both CanTopology.py and CanTopology/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AbstractCanCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 562 |
| ✅ Implemented | AbstractCanCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 530 |
| ✅ Implemented | AbstractCanCommunicationControllerAttributes | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 425 |
| ✅ Implemented | CanCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 575 |
| ✅ Implemented | CanCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 552 |
| ✅ Implemented | CanControllerConfigurationRequirements | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 471 |
| ✅ Implemented | CanControllerFdConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 12 |
| ✅ Implemented | CanControllerFdConfigurationRequirements | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 86 |
| ✅ Implemented | CanControllerXlConfiguration | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 187 |
| ✅ Implemented | CanControllerXlConfigurationRequirements | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py | Line 324 |
| ❌ Missing | AbstractCanCluster | - | Not found in implementation |
| ❌ Missing | AbstractCanPhysicalChannel | - | Not found in implementation |
| ❌ Missing | CanCluster | - | Not found in implementation |
| ❌ Missing | CanClusterBusOffRecovery | - | Not found in implementation |
| ❌ Missing | CanControllerConfiguration | - | Not found in implementation |
| ❌ Missing | CanPhysicalChannel | - | Not found in implementation |
| ❌ Missing | J1939Cluster | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication

**Summary:**
- Classes: 3/4 implemented, 1 missing
- Enums: 0/3 implemented, 3 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both CanCommunication.py and CanCommunication/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | CanFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py | Line 34 |
| ✅ Implemented | CanFrameTriggering | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py | Line 43 |
| ✅ Implemented | RxIdentifierRange | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py | Line 8 |
| ❌ Missing | CanXlFrameTriggeringProps | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | CanAddressingModeType | extended, standard | - | - | Not found in implementation |
| ❌ Missing | CanFrameRxBehaviorEnum | any, can20, canFd | - | - | Not found in implementation |
| ❌ Missing | CanFrameTxBehaviorEnum | can20, canFd | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ttcan::TtcanTopology

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TtcanTopology/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | TtcanCluster | - | Not found in implementation |
| ❌ Missing | TtcanCommunicationConnector | - | Not found in implementation |
| ❌ Missing | TtcanCommunicationController | - | Not found in implementation |
| ❌ Missing | TtcanPhysicalChannel | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ttcan::TtcanCommunication

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory TtcanCommunication/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | TtcanAbsolutelyScheduledTiming | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | TtcanTriggerType | rxTrigger, txRefTrigger, txRefTriggerGap, txTriggerMerged, txTriggerSingle, watchTrigger, watchTriggerGap | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology

**Summary:**
- Classes: 3/6 implemented, 3 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both FlexrayTopology.py and FlexrayTopology/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | FlexrayCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py | Line 346 |
| ✅ Implemented | FlexrayCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py | Line 308 |
| ✅ Implemented | FlexrayCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py | Line 8 |
| ❌ Missing | FlexrayFifoConfiguration | - | Not found in implementation |
| ❌ Missing | FlexrayFifoRange | - | Not found in implementation |
| ❌ Missing | FlexrayPhysicalChannel | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | FlexrayChannelName | channelA, channelB | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayCommunication

**Summary:**
- Classes: 3/3 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | FlexrayAbsolutelyScheduledTiming | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py | Line 19 |
| ✅ Implemented | FlexrayFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py | Line 8 |
| ✅ Implemented | FlexrayFrameTriggering | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py | Line 48 |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

**Summary:**
- Classes: 3/10 implemented, 7 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both LinTopology.py and LinTopology/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | LinCommunicationConnector | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py | Line 66 |
| ✅ Implemented | LinCommunicationController | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py | Line 7 |
| ✅ Implemented | LinMaster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py | Line 29 |
| ❌ Missing | LinCluster | - | Not found in implementation |
| ❌ Missing | LinConfigurableFrame | - | Not found in implementation |
| ❌ Missing | LinOrderedConfigurableFrame | - | Not found in implementation |
| ❌ Missing | LinPhysicalChannel | - | Not found in implementation |
| ❌ Missing | LinSlave | - | Not found in implementation |
| ❌ Missing | LinSlaveConfig | - | Not found in implementation |
| ❌ Missing | LinSlaveConfigIdent | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

**Summary:**
- Classes: 8/20 implemented, 12 missing, 1 extra
- Enums: 1/3 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both LinCommunication.py and LinCommunication/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ApplicationEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 114 |
| ✅ Implemented | FreeFormatEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 133 |
| ✅ Implemented | LinConfigurationEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 145 |
| ✅ Implemented | LinFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 10 |
| ✅ Implemented | LinFrameTriggering | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 31 |
| ✅ Implemented | LinScheduleTable | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 158 |
| ✅ Implemented | LinUnconditionalFrame | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 22 |
| ✅ Implemented | ScheduleTableEntry | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 73 |
| ❌ Missing | AssignFrameId | - | Not found in implementation |
| ❌ Missing | AssignFrameIdRange | - | Not found in implementation |
| ❌ Missing | AssignNad | - | Not found in implementation |
| ❌ Missing | ConditionalChangeNad | - | Not found in implementation |
| ❌ Missing | DataDumpEntry | - | Not found in implementation |
| ❌ Missing | FramePid | - | Not found in implementation |
| ❌ Missing | FreeFormat | - | Not found in implementation |
| ❌ Missing | LinErrorResponse | - | Not found in implementation |
| ❌ Missing | LinEventTriggeredFrame | - | Not found in implementation |
| ❌ Missing | LinSporadicFrame | - | Not found in implementation |
| ❌ Missing | SaveConfigurationEntry | - | Not found in implementation |
| ❌ Missing | UnassignFrameId | - | Not found in implementation |
| ➕ Extra | ResumePosition | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ✅ Implemented | ResumePosition | continueAtItPosition, startFromBeginning | continueAtItPosition, startFromBeginning | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py | Line 59 |
| ❌ Missing | LinChecksumType | classic, enhanced | - | - | Not found in implementation |
| ❌ Missing | RunMode | RunContinuous, runOnce | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CddSupport/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | UserDefinedCluster | - | Not found in implementation |
| ❌ Missing | UserDefinedCommunicationConnector | - | Not found in implementation |
| ❌ Missing | UserDefinedCommunicationController | - | Not found in implementation |
| ❌ Missing | UserDefinedPhysicalChannel | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform

**Summary:**
- Classes: 7/7 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | DefaultValueElement | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Line 67 |
| ✅ Implemented | FrameMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Line 9 |
| ✅ Implemented | Gateway | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Line 170 |
| ✅ Implemented | IPduMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Line 127 |
| ✅ Implemented | ISignalMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Line 38 |
| ✅ Implemented | PduMappingDefaultValue | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Line 90 |
| ✅ Implemented | TargetIPduRef | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py | Line 104 |

### Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster

**Summary:**
- Classes: 0/17 implemented, 17 missing
- Enums: 0/2 implemented, 2 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | ClientServerOperationComProps | - | Not found in implementation |
| ❌ Missing | CpSoftwareCluster | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterCommunicationResource | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterCommunicationResourceProps | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterMappingSet | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterResource | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterResourcePool | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterResourceToApplicationPartitionMapping | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterServiceResource | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterToApplicationPartitionMapping | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterToEcuInstanceMapping | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterToResourceMapping | - | Not found in implementation |
| ❌ Missing | DataComProps | - | Not found in implementation |
| ❌ Missing | RoleBasedResourceDependency | - | Not found in implementation |
| ❌ Missing | SwComponentPrototypeAssignment | - | Not found in implementation |
| ❌ Missing | SystemSignalGroupToCommunicationResourceMapping | - | Not found in implementation |
| ❌ Missing | SystemSignalToCommunicationResourceMapping | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DataConsistencyPolicyEnum | consistencyMechanism, noConsistency | - | - | Not found in implementation |
| ❌ Missing | SendIndicationEnum | System, AUTOSAR, anySendOperation, none | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

**Summary:**
- Classes: 0/12 implemented, 12 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory BinaryManifest/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BinaryManifestAddressableObject | - | Not found in implementation |
| ❌ Missing | BinaryManifestItem | - | Not found in implementation |
| ❌ Missing | BinaryManifestItemDefinition | - | Not found in implementation |
| ❌ Missing | BinaryManifestItemNumericalValue | - | Not found in implementation |
| ❌ Missing | BinaryManifestItemPointerValue | - | Not found in implementation |
| ❌ Missing | BinaryManifestItemValue | - | Not found in implementation |
| ❌ Missing | BinaryManifestMetaDataField | - | Not found in implementation |
| ❌ Missing | BinaryManifestProvideResource | - | Not found in implementation |
| ❌ Missing | BinaryManifestRequireResource | - | Not found in implementation |
| ❌ Missing | BinaryManifestResource | - | Not found in implementation |
| ❌ Missing | BinaryManifestResourceDefinition | - | Not found in implementation |
| ❌ Missing | CpSoftwareClusterBinaryManifestDescriptor | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

**Summary:**
- Classes: 3/22 implemented, 19 missing
- Enums: 0/13 implemented, 13 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both SecureCommunication.py and SecureCommunication/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | CryptoServiceMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py | Line 10 |
| ✅ Implemented | SecOcCryptoServiceMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py | Line 23 |
| ✅ Implemented | TlsCryptoServiceMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py | Line 61 |
| ❌ Missing | CryptoEllipticCurveProps | - | Not found in implementation |
| ❌ Missing | CryptoServiceCertificate | - | Not found in implementation |
| ❌ Missing | CryptoServiceKey | - | Not found in implementation |
| ❌ Missing | CryptoServicePrimitive | - | Not found in implementation |
| ❌ Missing | CryptoServiceQueue | - | Not found in implementation |
| ❌ Missing | CryptoSignatureScheme | - | Not found in implementation |
| ❌ Missing | IPSecConfig | - | Not found in implementation |
| ❌ Missing | IPSecConfigProps | - | Not found in implementation |
| ❌ Missing | IPSecRule | - | Not found in implementation |
| ❌ Missing | MacSecCipherSuiteConfig | - | Not found in implementation |
| ❌ Missing | MacSecCryptoAlgoConfig | - | Not found in implementation |
| ❌ Missing | MacSecGlobalKayProps | - | Not found in implementation |
| ❌ Missing | MacSecKayParticipant | - | Not found in implementation |
| ❌ Missing | MacSecLocalKayProps | - | Not found in implementation |
| ❌ Missing | MacSecParticipantSet | - | Not found in implementation |
| ❌ Missing | MacSecProps | - | Not found in implementation |
| ❌ Missing | TlsCryptoCipherSuite | - | Not found in implementation |
| ❌ Missing | TlsCryptoCipherSuiteProps | - | Not found in implementation |
| ❌ Missing | TlsPskIdentity | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | CryptoCertificateAlgorithmFamilyEnum | ecc, rsa | - | - | Not found in implementation |
| ❌ Missing | CryptoCertificateFormatEnum | cvc, x509 | - | - | Not found in implementation |
| ❌ Missing | CryptoServiceKeyGenerationEnum | keyDerivation, keyStorage | - | - | Not found in implementation |
| ❌ Missing | IPsecDpdActionEnum | clear, restart | - | - | Not found in implementation |
| ❌ Missing | IPsecHeaderTypeEnum | ah, esp, none | - | - | Not found in implementation |
| ❌ Missing | IPsecIpProtocolEnum | System, AUTOSAR, any, icmp, tcp, udp | - | - | Not found in implementation |
| ❌ Missing | IPsecModeEnum | transport, tunnel | - | - | Not found in implementation |
| ❌ Missing | IPsecPolicyEnum | drop, ipsec, passthrough, reject | - | - | Not found in implementation |
| ❌ Missing | MacSecCapabilityEnum | intergrityAndConfidentiality, intergrityWithoutConfidentiality | - | - | Not found in implementation |
| ❌ Missing | MacSecConfidentialityOffsetEnum | ConfidentialityOffset_0Offset_30, System, AUTOSAROffset_50 | - | - | Not found in implementation |
| ❌ Missing | MacSecFailPermissiveModeEnum | never, System, AUTOSAR, timeout | - | - | Not found in implementation |
| ❌ Missing | MacSecRoleEnum | keyServer, peer | - | - | Not found in implementation |
| ❌ Missing | TlsVersionEnum | tls12, tls13 | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement

**Summary:**
- Classes: 21/23 implemented, 2 missing
- Enums: 0/3 implemented, 3 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both NetworkManagement.py and NetworkManagement/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BusspecificNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 265 |
| ✅ Implemented | CanNmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 598 |
| ✅ Implemented | CanNmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 24 |
| ✅ Implemented | CanNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 276 |
| ✅ Implemented | CanNmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 162 |
| ✅ Implemented | FlexrayNmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 736 |
| ✅ Implemented | FlexrayNmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 58 |
| ✅ Implemented | FlexrayNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 284 |
| ✅ Implemented | FlexrayNmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 219 |
| ✅ Implemented | J1939NmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 745 |
| ✅ Implemented | J1939NmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 292 |
| ✅ Implemented | J1939NmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 228 |
| ✅ Implemented | NmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 497 |
| ✅ Implemented | NmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 12 |
| ✅ Implemented | NmConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 447 |
| ✅ Implemented | NmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 320 |
| ✅ Implemented | NmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 85 |
| ✅ Implemented | UdpNmCluster | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 783 |
| ✅ Implemented | UdpNmClusterCoupling | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 754 |
| ✅ Implemented | UdpNmEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 300 |
| ✅ Implemented | UdpNmNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py | Line 237 |
| ❌ Missing | J1939NodeName | - | Not found in implementation |
| ❌ Missing | NmCoordinator | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | FlexrayNmScheduleVariant | scheduleVariant1, scheduleVariant2, scheduleVariant3recommended, scheduleVariant4, scheduleVariant5, scheduleVariant6, scheduleVariant7 | - | - | Not found in implementation |
| ❌ Missing | J1939NmAddressConfigurationCapabilityEnum | J1939NM_AAC, J1939NM_CCA, J1939NM_NCA, J1939NM_SCA, J1939NM_SVCA | - | - | Not found in implementation |
| ❌ Missing | NmCoordinatorRoleEnum | Active, Passive | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Transformer

**Summary:**
- Classes: 0/23 implemented, 23 missing
- Enums: 0/6 implemented, 6 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BufferProperties | - | Not found in implementation |
| ❌ Missing | DataPrototypeInPortInterfaceRef | - | Not found in implementation |
| ❌ Missing | DataPrototypeReference | - | Not found in implementation |
| ❌ Missing | DataPrototypeTransformationProps | - | Not found in implementation |
| ❌ Missing | DataTransformation | - | Not found in implementation |
| ❌ Missing | DataTransformationSet | - | Not found in implementation |
| ❌ Missing | E2EProfileCompatibilityProps | - | Not found in implementation |
| ❌ Missing | EndToEndTransformationComSpecProps | - | Not found in implementation |
| ❌ Missing | EndToEndTransformationDescription | - | Not found in implementation |
| ❌ Missing | EndToEndTransformationISignalProps | - | Not found in implementation |
| ❌ Missing | SOMEIPTransformationDescription | - | Not found in implementation |
| ❌ Missing | SOMEIPTransformationISignalProps | - | Not found in implementation |
| ❌ Missing | SOMEIPTransformationProps | - | Not found in implementation |
| ❌ Missing | TlvDataIdDefinition | - | Not found in implementation |
| ❌ Missing | TlvDataIdDefinitionSet | - | Not found in implementation |
| ❌ Missing | TransformationDescription | - | Not found in implementation |
| ❌ Missing | TransformationISignalProps | - | Not found in implementation |
| ❌ Missing | TransformationProps | - | Not found in implementation |
| ❌ Missing | TransformationPropsSet | - | Not found in implementation |
| ❌ Missing | TransformationTechnology | - | Not found in implementation |
| ❌ Missing | UserDefinedTransformationDescription | - | Not found in implementation |
| ❌ Missing | UserDefinedTransformationISignalProps | - | Not found in implementation |
| ❌ Missing | UserDefinedTransformationProps | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | CSTransformerErrorReactionEnum | applicationOnly, autonomous | - | - | Not found in implementation |
| ❌ Missing | DataIdModeEnum | all16Bit, alternating8Bitcounter, lower12Bit, lower8Bitare | - | - | Not found in implementation |
| ❌ Missing | DataTransformationKindEnum | asymmetricFrom, asymmetricToByteArray, symmetric | - | - | Not found in implementation |
| ❌ Missing | EndToEndProfileBehaviorEnum | PRE_R4_2, R4_2 | - | - | Not found in implementation |
| ❌ Missing | SOMEIPMessageTypeEnum | notification, request, requestNoReturn, response | - | - | Not found in implementation |
| ❌ Missing | TransformerClassEnum | custom, safety, security, serializer | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InstanceRef/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DataPrototypeInClientServerInterfaceInstanceRef | - | Not found in implementation |
| ❌ Missing | DataPrototypeInPortInterfaceInstanceRef | - | Not found in implementation |
| ❌ Missing | DataPrototypeInSenderReceiverInterfaceInstanceRef | - | Not found in implementation |
| ❌ Missing | ImplementationDataTypeElementInPortInterfaceRef | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping

**Summary:**
- Classes: 9/12 implemented, 3 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both DataMapping.py and DataMapping/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | DataMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 14 |
| ✅ Implemented | IndexedArrayElement | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 188 |
| ✅ Implemented | SenderRecArrayElementMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 226 |
| ✅ Implemented | SenderRecArrayTypeMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 264 |
| ✅ Implemented | SenderRecCompositeTypeMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 89 |
| ✅ Implemented | SenderRecRecordElementMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 102 |
| ✅ Implemented | SenderRecRecordTypeMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 168 |
| ✅ Implemented | SenderReceiverToSignalGroupMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 302 |
| ✅ Implemented | SenderReceiverToSignalMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py | Line 37 |
| ❌ Missing | ClientServerToSignalMapping | - | Not found in implementation |
| ❌ Missing | SenderReceiverCompositeElementToSignalMapping | - | Not found in implementation |
| ❌ Missing | TriggerToSignalMapping | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DataTypePolicyEnum | ddsService, ddsSignal, legacy, network, Representation, FromComSpec, override, transformingISignal | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::EndToEndProtection

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory EndToEndProtection/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | EndToEndProtectionISignalIPdu | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::ECUResourceMapping

**Summary:**
- Classes: 1/3 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both ECUResourceMapping.py and ECUResourceMapping/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ECUMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/ECUResourceMapping.py | Line 4 |
| ❌ Missing | CommunicationControllerMapping | - | Not found in implementation |
| ❌ Missing | HwPortMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping

**Summary:**
- Classes: 2/12 implemented, 10 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both SWmapping.py and SWmapping/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ApplicationPartitionToEcuPartitionMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SWmapping.py | Line 39 |
| ✅ Implemented | SwcToImplMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SWmapping.py | Line 10 |
| ❌ Missing | ApplicationPartition | - | Not found in implementation |
| ❌ Missing | ComponentClustering | - | Not found in implementation |
| ❌ Missing | ComponentSeparation | - | Not found in implementation |
| ❌ Missing | EcuPartition | - | Not found in implementation |
| ❌ Missing | EcuResourceEstimation | - | Not found in implementation |
| ❌ Missing | J1939ControllerApplication | - | Not found in implementation |
| ❌ Missing | J1939ControllerApplicationToJ1939NmNodeMapping | - | Not found in implementation |
| ❌ Missing | MappingConstraint | - | Not found in implementation |
| ❌ Missing | SwcToApplicationPartitionMapping | - | Not found in implementation |
| ❌ Missing | SwcToEcuMapping | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | MappingScopeEnum | mappingScopeCore, System, AUTOSAR, mappingScopeEcu, mappingScopePartition | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping

**Summary:**
- Classes: 1/6 implemented, 5 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both RteEventToOsTaskMapping.py and RteEventToOsTaskMapping/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AppOsTaskProxyToEcuTaskProxyMapping | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/RteEventToOsTaskMapping.py | Line 8 |
| ❌ Missing | OsTaskProxy | - | Not found in implementation |
| ❌ Missing | RteEventInCompositionSeparation | - | Not found in implementation |
| ❌ Missing | RteEventInCompositionToOsTaskProxyMapping | - | Not found in implementation |
| ❌ Missing | RteEventInSystemSeparation | - | Not found in implementation |
| ❌ Missing | RteEventInSystemToOsTaskProxyMapping | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | OsTaskPreemptabilityEnum | full, none | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths

**Summary:**
- Classes: 0/7 implemented, 7 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory SignalPaths/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | CommonSignalPath | - | Not found in implementation |
| ❌ Missing | ForbiddenSignalPath | - | Not found in implementation |
| ❌ Missing | PermissibleSignalPath | - | Not found in implementation |
| ❌ Missing | SeparateSignalPath | - | Not found in implementation |
| ❌ Missing | SignalPathConstraint | - | Not found in implementation |
| ❌ Missing | SwcToSwcOperationArguments | - | Not found in implementation |
| ❌ Missing | SwcToSwcSignal | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | SwcToSwcOperationArgumentsDirectionEnum | in, out | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::PncMapping

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory PncMapping/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | PncMapping | - | Not found in implementation |
| ❌ Missing | PncMappingIdent | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::GeneralPurposeConnection

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory GeneralPurposeConnection/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | GeneralPurposeConnection | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::DoIP

**Summary:**
- Classes: 3/6 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both DoIP.py and DoIP/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AbstractDoIpLogicAddressProps | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIP.py | Line 11 |
| ✅ Implemented | DoIpLogicTargetAddressProps | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIP.py | Line 24 |
| ✅ Implemented | DoIpLogicTesterAddressProps | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/DoIP.py | Line 34 |
| ❌ Missing | DoIpConfig | - | Not found in implementation |
| ❌ Missing | DoIpInterface | - | Not found in implementation |
| ❌ Missing | DoIpRoutingActivation | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols

**Summary:**
- Classes: 13/32 implemented, 19 missing, 3 extra
- Enums: 0/4 implemented, 4 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both TransportProtocols.py and TransportProtocols/ exist. Requirements say this is a non-leaf package. Expected: directory.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | CanTpAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 35 |
| ✅ Implemented | CanTpChannel | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 63 |
| ✅ Implemented | CanTpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 369 |
| ✅ Implemented | CanTpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 121 |
| ✅ Implemented | CanTpEcu | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 275 |
| ✅ Implemented | CanTpNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 303 |
| ✅ Implemented | DoIpLogicAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 430 |
| ✅ Implemented | DoIpTpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 496 |
| ✅ Implemented | LinTpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 700 |
| ✅ Implemented | LinTpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 544 |
| ✅ Implemented | LinTpNode | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 635 |
| ✅ Implemented | TpAddress | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 526 |
| ✅ Implemented | TpConfig | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Line 13 |
| ❌ Missing | EthTpConfig | - | Not found in implementation |
| ❌ Missing | EthTpConnection | - | Not found in implementation |
| ❌ Missing | FlexrayArTpChannel | - | Not found in implementation |
| ❌ Missing | FlexrayArTpConfig | - | Not found in implementation |
| ❌ Missing | FlexrayArTpConnection | - | Not found in implementation |
| ❌ Missing | FlexrayArTpNode | - | Not found in implementation |
| ❌ Missing | FlexrayTpConfig | - | Not found in implementation |
| ❌ Missing | FlexrayTpConnection | - | Not found in implementation |
| ❌ Missing | FlexrayTpConnectionControl | - | Not found in implementation |
| ❌ Missing | FlexrayTpEcu | - | Not found in implementation |
| ❌ Missing | FlexrayTpNode | - | Not found in implementation |
| ❌ Missing | FlexrayTpPduPool | - | Not found in implementation |
| ❌ Missing | J1939TpConfig | - | Not found in implementation |
| ❌ Missing | J1939TpConnection | - | Not found in implementation |
| ❌ Missing | J1939TpNode | - | Not found in implementation |
| ❌ Missing | J1939TpPg | - | Not found in implementation |
| ❌ Missing | SomeipTpChannel | - | Not found in implementation |
| ❌ Missing | SomeipTpConfig | - | Not found in implementation |
| ❌ Missing | SomeipTpConnection | - | Not found in implementation |
| ➕ Extra | DoIpTpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | TpConnection | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |
| ➕ Extra | TpConnectionIdent | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | CanTpAddressingFormatType | extended, System, AUTOSAR, mixed, mixed29bit, normalfixed, standard | - | - | Not found in implementation |
| ❌ Missing | FrArTpAckType | ackWithoutRt, ackWithRt, noAck | - | - | Not found in implementation |
| ❌ Missing | MaximumMessageLengthType | I4glength, iso, iso6, route | - | - | Not found in implementation |
| ❌ Missing | NetworkTargetAddressType | functional, physical | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | IEEE1722TpAcfConnection | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAvConnection | - | Not found in implementation |
| ❌ Missing | IEEE1722TpConfig | - | Not found in implementation |
| ❌ Missing | IEEE1722TpConnection | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/9 implemented, 9 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory IEEE1722TpAv/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | IEEE1722TpAafConnection | - | Not found in implementation |
| ❌ Missing | IEEE1722TpCrfConnection | - | Not found in implementation |
| ❌ Missing | IEEE1722TpIidcConnection | - | Not found in implementation |
| ❌ Missing | IEEE1722TpRvfConnection | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | IEEE1722TpAafAes3DataTypeEnum | iec61937, pcm, smpte338, unspecified, vendor | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAafFormatEnum | aes3_32bit, float_32bit, int_16bit, int_24bit, int_32bit, user | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAafNominalRateEnum | _16kHz, _176_4kHz, _192kHz, _24kHz, _32kHz, _44_1kHz, _48kHz, System, AUTOSAR_88_2kHz, _8kHz, _96kHz, user | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpCrfPullEnum | _1_0, _1_001, _1_1_001, _1_8, _24_25, _25_24 | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpCrfTypeEnum | audioSample, machineCycle, user, videoFrame, videoLine | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpRvfColorSpaceEnum | bt_rec_601, bt_rec_709, grayscale, itu_bt_2020, user, xyz, ycbcr, ycgco, ycm | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpRvfFrameRateEnum | _1, System, AUTOSAR, System, AUTOSAR | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpRvfPixelDepthEnum | _10 | - | - | Not found in implementation |
| ❌ Missing | IEEE1722TpRvfPixelFormatEnum | _4_1_1 | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf

**Summary:**
- Classes: 0/6 implemented, 6 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory IEEE1722TpAcf/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | IEEE1722TpAcfBus | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAcfBusPart | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAcfCan | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAcfCanPart | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAcfLin | - | Not found in implementation |
| ❌ Missing | IEEE1722TpAcfLinPart | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | IEEE1722TpAcfCanMessageTypeEnum | System, AUTOSAR, can, canBrief | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

**Summary:**
- Classes: 0/9 implemented, 9 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory BusMirror/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BusMirrorCanIdRangeMapping | - | Not found in implementation |
| ❌ Missing | BusMirrorCanIdToCanIdMapping | - | Not found in implementation |
| ❌ Missing | BusMirrorChannel | - | Not found in implementation |
| ❌ Missing | BusMirrorChannelMapping | - | Not found in implementation |
| ❌ Missing | BusMirrorChannelMappingCan | - | Not found in implementation |
| ❌ Missing | BusMirrorChannelMappingFlexray | - | Not found in implementation |
| ❌ Missing | BusMirrorChannelMappingIp | - | Not found in implementation |
| ❌ Missing | BusMirrorChannelMappingUserDefined | - | Not found in implementation |
| ❌ Missing | BusMirrorLinPidToCanIdMapping | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | MirroringProtocolEnum | none | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::Dlt

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Dlt/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DltConfig | - | Not found in implementation |
| ❌ Missing | DltLogChannel | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DltDefaultTraceStateEnum | DefaultTraceStateDisabled, DefaultTraceStateEnabled | - | - | Not found in implementation |
| ❌ Missing | LogTraceDefaultLogLevelEnum | debug, error, fatal, info, System, AUTOSAR, verbose, warn | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime

**Summary:**
- Classes: 0/7 implemented, 7 missing
- Enums: 0/4 implemented, 4 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbstractGlobalTimeDomainProps | - | Not found in implementation |
| ❌ Missing | GlobalTimeCorrectionProps | - | Not found in implementation |
| ❌ Missing | GlobalTimeDomain | - | Not found in implementation |
| ❌ Missing | GlobalTimeGateway | - | Not found in implementation |
| ❌ Missing | GlobalTimeMaster | - | Not found in implementation |
| ❌ Missing | GlobalTimeSlave | - | Not found in implementation |
| ❌ Missing | NetworkSegmentIdentification | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | GlobalTimeCrcSupportEnum | crcNotSupported, crcSupported | - | - | Not found in implementation |
| ❌ Missing | GlobalTimeCrcValidationEnum | crcIgnored, crcNotValidated, crcOptional, crcValidated | - | - | Not found in implementation |
| ❌ Missing | GlobalTimeIcvSupportEnum | icvNotSupported, icvSupported | - | - | Not found in implementation |
| ❌ Missing | GlobalTimeIcvVerificationEnum | icvIgnored, icvNotVerified, icvOptional, icvVerified | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::CAN

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CAN/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | CanGlobalTimeDomainProps | - | Not found in implementation |
| ❌ Missing | GlobalTimeCanMaster | - | Not found in implementation |
| ❌ Missing | GlobalTimeCanSlave | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH

**Summary:**
- Classes: 0/6 implemented, 6 missing
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ETH/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | EthGlobalTimeDomainProps | - | Not found in implementation |
| ❌ Missing | EthGlobalTimeManagedCouplingPort | - | Not found in implementation |
| ❌ Missing | EthTSynCrcFlags | - | Not found in implementation |
| ❌ Missing | EthTSynSubTlvConfig | - | Not found in implementation |
| ❌ Missing | GlobalTimeEthMaster | - | Not found in implementation |
| ❌ Missing | GlobalTimeEthSlave | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | EthGlobalTimeMessageFormatEnum | IEEE802_1AS, IEEE802_1AS_AUTOSAR | - | - | Not found in implementation |
| ❌ Missing | GlobalTimePortRoleEnum | dynamic, System, AUTOSAR, timeSlave | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::FR

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory FR/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | FrGlobalTimeDomainProps | - | Not found in implementation |
| ❌ Missing | GlobalTimeFrMaster | - | Not found in implementation |
| ❌ Missing | GlobalTimeFrSlave | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::UserDefined

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory UserDefined/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | UserDefinedGlobalTimeMaster | - | Not found in implementation |
| ❌ Missing | UserDefinedGlobalTimeSlave | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs

**Summary:**
- Classes: 2/5 implemented, 3 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ComponentInSystemInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py | Line 55 |
| ✅ Implemented | VariableDataPrototypeInSystemInstanceRef | src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py | Line 9 |
| ❌ Missing | OperationInSystemInstanceRef | - | Not found in implementation |
| ❌ Missing | PortGroupInSystemInstanceRef | - | Not found in implementation |
| ❌ Missing | TriggerInSystemInstanceRef | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics

**Summary:**
- Classes: 1/18 implemented, 17 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both CommonDiagnostics.py and CommonDiagnostics/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | DiagnosticCommonElement | src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/CommonDiagnostics.py | Line 8 |
| ❌ Missing | DiagnosticAbstractDataIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticAbstractParameter | - | Not found in implementation |
| ❌ Missing | DiagnosticDataElement | - | Not found in implementation |
| ❌ Missing | DiagnosticDataIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticDynamicDataIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticInfoType | - | Not found in implementation |
| ❌ Missing | DiagnosticParameter | - | Not found in implementation |
| ❌ Missing | DiagnosticParameterElement | - | Not found in implementation |
| ❌ Missing | DiagnosticParameterIdent | - | Not found in implementation |
| ❌ Missing | DiagnosticParameterIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticParameterSupportInfo | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestRoutineResults | - | Not found in implementation |
| ❌ Missing | DiagnosticRoutine | - | Not found in implementation |
| ❌ Missing | DiagnosticRoutineSubfunction | - | Not found in implementation |
| ❌ Missing | DiagnosticStartRoutine | - | Not found in implementation |
| ❌ Missing | DiagnosticStopRoutine | - | Not found in implementation |
| ❌ Missing | DiagnosticSupportInfoByte | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution

**Summary:**
- Classes: 1/4 implemented, 3 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both DiagnosticContribution.py and DiagnosticContribution/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | DiagnosticServiceTable | src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticContribution.py | Line 21 |
| ❌ Missing | DiagnosticContributionSet | - | Not found in implementation |
| ❌ Missing | DiagnosticEcuInstanceProps | - | Not found in implementation |
| ❌ Missing | DiagnosticProtocol | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticObdSupportEnum | masterEcu, noObdSupport, primaryEcu, secondaryEcu | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonProps

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/3 implemented, 3 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticCommonProps/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticCommonProps | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticEventCombinationBehaviorEnum | eventCombination, eventCombination, OnStorage | - | - | Not found in implementation |
| ❌ Missing | DiagnosticEventCombinationReportingBehaviorEnum | reportingInChronlogicalOrder | - | - | Not found in implementation |
| ❌ Missing | DiagnosticOccurrenceCounterProcessingEnum | Diagnostic, AUTOSAR, confirmedDtcBit, testFailedBit | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode

**Summary:**
- Classes: 0/8 implemented, 8 missing
- Enums: 0/6 implemented, 6 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticTroubleCode/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticDataIdentifierSet | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCode | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCodeGroup | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCodeJ1939 | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCodeObd | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCodeProps | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCodeUds | - | Not found in implementation |
| ❌ Missing | EventObdReadinessGroup | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticSignificanceEnum | fault, occurence | - | - | Not found in implementation |
| ❌ Missing | DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum | statusBitAgingAndDisplacement, statusBitNormal | - | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCodeJ1939DtcKindEnum | serviceOnly, standard | - | - | Not found in implementation |
| ❌ Missing | DiagnosticTypeOfDtcSupportedEnum | iso11992_4, iso14229_1, iso15031_6, saeJ1939_73, saeJ2012_da | - | - | Not found in implementation |
| ❌ Missing | DiagnosticUdsSeverityEnum | checkAtNextHalt, immediately, maintenanceOnly, noSeverity | - | - | Not found in implementation |
| ❌ Missing | DiagnosticWwhObdDtcClassEnum | Diagnostic, AUTOSAR, demDtcWwhObdClassA, demDtcWwhObdClassB1, demDtcWwhObdClassB2, demDtcWwhObdClassC, demDtcWwhObd, ClassNoInformation | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent

**Summary:**
- Classes: 0/8 implemented, 8 missing
- Enums: 0/5 implemented, 5 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticEvent/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticAbstractAliasEvent | - | Not found in implementation |
| ❌ Missing | DiagnosticConnectedIndicator | - | Not found in implementation |
| ❌ Missing | DiagnosticEvent | - | Not found in implementation |
| ❌ Missing | DiagnosticFimAliasEventMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticIumpr | - | Not found in implementation |
| ❌ Missing | DiagnosticIumprDenominatorGroup | - | Not found in implementation |
| ❌ Missing | DiagnosticIumprGroup | - | Not found in implementation |
| ❌ Missing | DiagnosticIumprGroupIdentifier | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticClearEventAllowedBehaviorEnum | noStatusByteChange, onlyThisCycleAndReadiness | - | - | Not found in implementation |
| ❌ Missing | DiagnosticConnectedIndicatorBehaviorEnum | blinkMode, blinkOrContinuousOnMode, continuousOnMode, fastFlashingMode, slowFlashingMode | - | - | Not found in implementation |
| ❌ Missing | DiagnosticEventClearAllowedEnum | always, requiresCallback, Execution | - | - | Not found in implementation |
| ❌ Missing | DiagnosticEventKindEnum | bsw, swc | - | - | Not found in implementation |
| ❌ Missing | DiagnosticIumprKindEnum | apiBased, observerBased | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticMemoryDestination

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/4 implemented, 4 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticMemoryDestination/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticMemoryDestination | - | Not found in implementation |
| ❌ Missing | DiagnosticMemoryDestinationPrimary | - | Not found in implementation |
| ❌ Missing | DiagnosticMemoryDestinationUserDefined | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticClearDtcLimitationEnum | allSupportedDtcs, clearAllDtcs | - | - | Not found in implementation |
| ❌ Missing | DiagnosticEventDisplacementStrategyEnum | full, none, prioOcc | - | - | Not found in implementation |
| ❌ Missing | DiagnosticMemoryEntryStorageTriggerEnum | confirmed, fdcThreshold, testFailed | - | - | Not found in implementation |
| ❌ Missing | DiagnosticTypeOfFreezeFrameRecordNumerationEnum | calculated, configured | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticExtendedDataRecord

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticExtendedDataRecord/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticExtendedDataRecord | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticFreezeFrame

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticFreezeFrame/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticFreezeFrame | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticRecordTriggerEnum | confirmed, testFailedThisOperationCycle, testPassed | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticCondition

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticCondition/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticCondition | - | Not found in implementation |
| ❌ Missing | DiagnosticEnableCondition | - | Not found in implementation |
| ❌ Missing | DiagnosticStorageCondition | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticDebouncingAlgorithm

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticDebouncingAlgorithm/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticDebounceAlgorithmProps | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticDebounceBehaviorEnum | freeze, reset | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticConditionGroup/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticConditionGroup | - | Not found in implementation |
| ❌ Missing | DiagnosticEnableConditionGroup | - | Not found in implementation |
| ❌ Missing | DiagnosticStorageConditionGroup | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticOperationCycle

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticOperationCycle/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticOperationCycle | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticOperationCycleTypeEnum | ignition, obdDrivingCycle, warmup | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticAging

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticAging/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticAging | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticIndicator

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticIndicator/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticIndicator | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticIndicatorTypeEnum | amberWarning, malfunction, protectLamp, redStopLamp, warning | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticTestResult/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticMeasurementIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticTestIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticTestResult | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticTestResultUpdateEnum | always, steady | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm

**Summary:**
- Classes: 0/5 implemented, 5 missing
- Enums: 0/1 implemented, 1 missing

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticAccessPermission | - | Not found in implementation |
| ❌ Missing | DiagnosticAuthRole | - | Not found in implementation |
| ❌ Missing | DiagnosticAuthRoleProxy | - | Not found in implementation |
| ❌ Missing | DiagnosticSecurityLevel | - | Not found in implementation |
| ❌ Missing | DiagnosticSession | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticJumpToBootLoaderEnum | noBoot, oemBoot, oemBootRespApp, systemSupplierBoot, systemSupplierBoot | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommonService

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CommonService/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticCustomServiceClass | - | Not found in implementation |
| ❌ Missing | DiagnosticServiceClass | - | Not found in implementation |
| ❌ Missing | DiagnosticServiceInstance | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CustomServiceInstance

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CustomServiceInstance/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticCustomServiceInstance | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SessionControl

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory SessionControl/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticSessionControl | - | Not found in implementation |
| ❌ Missing | DiagnosticSessionControlClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SecurityAccess

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory SecurityAccess/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticSecurityAccess | - | Not found in implementation |
| ❌ Missing | DiagnosticSecurityAccessClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication

**Summary:**
- Classes: 0/9 implemented, 9 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Authentication/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticAuthTransmitCertificate | - | Not found in implementation |
| ❌ Missing | DiagnosticAuthTransmitCertificateEvaluation | - | Not found in implementation |
| ❌ Missing | DiagnosticAuthentication | - | Not found in implementation |
| ❌ Missing | DiagnosticAuthenticationClass | - | Not found in implementation |
| ❌ Missing | DiagnosticAuthenticationConfiguration | - | Not found in implementation |
| ❌ Missing | DiagnosticDeAuthentication | - | Not found in implementation |
| ❌ Missing | DiagnosticProofOfOwnership | - | Not found in implementation |
| ❌ Missing | DiagnosticVerifyCertificateBidirectional | - | Not found in implementation |
| ❌ Missing | DiagnosticVerifyCertificateUnidirectional | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory EcuReset/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticEcuReset | - | Not found in implementation |
| ❌ Missing | DiagnosticEcuResetClass | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticResponseToEcuResetEnum | respondAfterReset, respondBeforeReset | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CommunicationControl/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticComControl | - | Not found in implementation |
| ❌ Missing | DiagnosticComControlClass | - | Not found in implementation |
| ❌ Missing | DiagnosticComControlSpecificChannel | - | Not found in implementation |
| ❌ Missing | DiagnosticComControlSubNodeChannel | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ControlDTCSetting

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ControlDTCSetting/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticControlDTCSetting | - | Not found in implementation |
| ❌ Missing | DiagnosticControlDTCSettingClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier

**Summary:**
- Classes: 0/7 implemented, 7 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DataByIdentifier/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticDataByIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticReadDataByIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticReadDataByIdentifierClass | - | Not found in implementation |
| ❌ Missing | DiagnosticReadScalingDataByIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticReadScalingDataByIdentifierClass | - | Not found in implementation |
| ❌ Missing | DiagnosticWriteDataByIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticWriteDataByIdentifierClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::IOControl

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory IOControl/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticControlEnableMaskBit | - | Not found in implementation |
| ❌ Missing | DiagnosticIOControl | - | Not found in implementation |
| ❌ Missing | DiagnosticIoControlClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RoutineControl

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory RoutineControl/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRoutineControl | - | Not found in implementation |
| ❌ Missing | DiagnosticRoutineControlClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineDataIdentifier

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DynamicallyDefineDataIdentifier/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticDynamicallyDefineDataIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticDynamicallyDefineDataIdentifierClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineData

**Summary:**
- Classes: 0/0 implemented
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DynamicallyDefineData/

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum | clearDynamicallyDefineDataIdentifier, defineByIdentifier, defineByMemoryAddress | - | - | Not found in implementation |
| ❌ Missing | DiagnosticHandleDDDIConfigurationEnum | nonVolatile, volatile | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ReadDataByPeriodicID/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticPeriodicRate | - | Not found in implementation |
| ❌ Missing | DiagnosticReadDataByPeriodicID | - | Not found in implementation |
| ❌ Missing | DiagnosticReadDataByPeriodicIDClass | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticPeriodicRateCategoryEnum | periodicRateFast, periodicRateMedium, periodicRateSlow | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ResponseOnEvent/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticEventWindow | - | Not found in implementation |
| ❌ Missing | DiagnosticResponseOnEvent | - | Not found in implementation |
| ❌ Missing | DiagnosticResponseOnEventClass | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticEventWindowTimeEnum | infiniteTimeTo, powerWindowTime | - | - | Not found in implementation |
| ❌ Missing | DiagnosticResponseOnEventActionEnum | clear, onChangeOfDataIdentifier, onComparisonOfValues, onDTCStatusChange, report, reportDTCRecordInformationOnDtc, reportMostRecentDtcOnStatus, start, stop | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDTCInformation

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ReadDTCInformation/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticReadDTCInformation | - | Not found in implementation |
| ❌ Missing | DiagnosticReadDTCInformationClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ClearDiagnosticInfo

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ClearDiagnosticInfo/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticClearDiagnosticInformation | - | Not found in implementation |
| ❌ Missing | DiagnosticClearDiagnosticInformationClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress

**Summary:**
- Classes: 0/15 implemented, 15 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory MemoryByAddress/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticDataTransfer | - | Not found in implementation |
| ❌ Missing | DiagnosticDataTransferClass | - | Not found in implementation |
| ❌ Missing | DiagnosticMemoryAddressableRangeAccess | - | Not found in implementation |
| ❌ Missing | DiagnosticMemoryByAddress | - | Not found in implementation |
| ❌ Missing | DiagnosticMemoryIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticReadMemoryByAddress | - | Not found in implementation |
| ❌ Missing | DiagnosticReadMemoryByAddressClass | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestDownload | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestDownloadClass | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestUpload | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestUploadClass | - | Not found in implementation |
| ❌ Missing | DiagnosticTransferExit | - | Not found in implementation |
| ❌ Missing | DiagnosticTransferExitClass | - | Not found in implementation |
| ❌ Missing | DiagnosticWriteMemoryByAddress | - | Not found in implementation |
| ❌ Missing | DiagnosticWriteMemoryByAddressClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RequestFileTransfer

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory RequestFileTransfer/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRequestFileTransfer | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestFileTransferClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition

**Summary:**
- Classes: 0/10 implemented, 10 missing
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory EnvironmentalCondition/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticEnvBswModeElement | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvCompareCondition | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvConditionFormula | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvConditionFormulaPart | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvDataCondition | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvDataElementCondition | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvModeCondition | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvModeElement | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvSwcModeElement | - | Not found in implementation |
| ❌ Missing | DiagnosticEnvironmentalCondition | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticCompareTypeEnum | isEqual | - | - | Not found in implementation |
| ❌ Missing | DiagnosticLogicalOperatorEnum | logicalAnd, logicalOr | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x01_RequestCurrentPowertrain

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x01_RequestCurrentPowertrain/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRequestCurrentPowertrainData | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestCurrentPowertrainDataClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x02_RequestPowertrainFreeze

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x02_RequestPowertrainFreeze/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticPowertrainFreezeFrame | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestPowertrainFreezeFrameData | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestPowertrainFreezeFrameDataClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x03_0x07_RequestEmission

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x03_0x07_RequestEmission/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRequestEmissionRelatedDTC | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestEmissionRelatedDTCClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x04_ClearResetEmission

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x04_ClearResetEmission/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticClearResetEmissionRelatedInfo | - | Not found in implementation |
| ❌ Missing | DiagnosticClearResetEmissionRelatedInfoClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x06_RequestOnBoard

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x06_RequestOnBoard/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRequestOnBoardMonitoringTestResults | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestOnBoardMonitoringTestResultsClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x08_RequestControlOfOnBoard

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x08_RequestControlOfOnBoard/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRequestControlOfOnBoardDevice | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestControlOfOnBoardDeviceClass | - | Not found in implementation |
| ❌ Missing | DiagnosticTestRoutineIdentifier | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x09_RequestVehicleInformation

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x09_RequestVehicleInformation/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRequestVehicleInfo | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestVehicleInfoClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x0A_RequestEmissionRelated

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Mode_0x0A_RequestEmissionRelated/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticRequestEmissionRelatedDTCPermanentStatus | - | Not found in implementation |
| ❌ Missing | DiagnosticRequestEmissionRelatedDTCPermanentStatusClass | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping

**Summary:**
- Classes: 0/17 implemented, 17 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticAuthTransmitCertificateMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEnableConditionPortMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEventPortMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEventToDebounceAlgorithmMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEventToEnableConditionGroupMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEventToOperationCycleMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEventToSecurityEventMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEventToStorageConditionGroupMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticEventToTroubleCodeUdsMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticIumprToFunctionIdentifierMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticMasterToSlaveEventMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticOperationCyclePortMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticSecureCodingMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticStorageConditionPortMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticSwMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticTroubleCodeUdsToTroubleCodeObdMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

**Summary:**
- Classes: 0/8 implemented, 8 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ServiceMapping/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | BswServiceDependencyIdent | - | Not found in implementation |
| ❌ Missing | DiagnosticDemProvidedDataMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticFimFunctionMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticParameterElementAccess | - | Not found in implementation |
| ❌ Missing | DiagnosticSecurityEventReportingModeMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticServiceDataMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticServiceMappingDiagTarget | - | Not found in implementation |
| ❌ Missing | DiagnosticServiceSwMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::FimMapping

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory FimMapping/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticFimAliasEventGroupMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticInhibitSourceEventMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DiagnosticJ1939Mapping/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticEventToTroubleCodeJ1939Mapping | - | Not found in implementation |
| ❌ Missing | DiagnosticJ1939SpnMapping | - | Not found in implementation |
| ❌ Missing | DiagnosticJ1939SwMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CpSoftwareCluster/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | CpSwClusterResourceToDiagDataElemMapping | - | Not found in implementation |
| ❌ Missing | CpSwClusterResourceToDiagFunctionIdMapping | - | Not found in implementation |
| ❌ Missing | CpSwClusterToDiagEventMapping | - | Not found in implementation |
| ❌ Missing | CpSwClusterToDiagRoutineSubfunctionMapping | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim

**Summary:**
- Classes: 0/6 implemented, 6 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Fim/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticFimAliasEvent | - | Not found in implementation |
| ❌ Missing | DiagnosticFimAliasEventGroup | - | Not found in implementation |
| ❌ Missing | DiagnosticFimEventGroup | - | Not found in implementation |
| ❌ Missing | DiagnosticFunctionIdentifier | - | Not found in implementation |
| ❌ Missing | DiagnosticFunctionIdentifierInhibit | - | Not found in implementation |
| ❌ Missing | DiagnosticFunctionInhibitSource | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | DiagnosticInhibitionMaskEnum | lastFailed, notTested, tested, testedAndFailed | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::J1939

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory J1939/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DiagnosticJ1939ExpandedFreezeFrame | - | Not found in implementation |
| ❌ Missing | DiagnosticJ1939FreezeFrame | - | Not found in implementation |
| ❌ Missing | DiagnosticJ1939Node | - | Not found in implementation |
| ❌ Missing | DiagnosticJ1939Spn | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InstanceRefs/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DataPrototypeInSystemInstanceRef | - | Not found in implementation |
| ❌ Missing | PModeInSystemInstanceRef | - | Not found in implementation |
| ❌ Missing | SwcServiceDependencyInSystemInstanceRef | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::SecurityExtractTemplate

**Summary:**
- Classes: 0/24 implemented, 24 missing
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory SecurityExtractTemplate/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | AbstractSecurityEventFilter | - | Not found in implementation |
| ❌ Missing | BlockState | - | Not found in implementation |
| ❌ Missing | IdsCommonElement | - | Not found in implementation |
| ❌ Missing | IdsDesign | - | Not found in implementation |
| ❌ Missing | IdsMapping | - | Not found in implementation |
| ❌ Missing | IdsmInstance | - | Not found in implementation |
| ❌ Missing | IdsmProperties | - | Not found in implementation |
| ❌ Missing | IdsmRateLimitation | - | Not found in implementation |
| ❌ Missing | IdsmSignatureSupportAp | - | Not found in implementation |
| ❌ Missing | IdsmSignatureSupportCp | - | Not found in implementation |
| ❌ Missing | IdsmTrafficLimitation | - | Not found in implementation |
| ❌ Missing | SecurityEventAggregationFilter | - | Not found in implementation |
| ❌ Missing | SecurityEventContextData | - | Not found in implementation |
| ❌ Missing | SecurityEventContextMapping | - | Not found in implementation |
| ❌ Missing | SecurityEventContextMappingApplication | - | Not found in implementation |
| ❌ Missing | SecurityEventContextMappingBswModule | - | Not found in implementation |
| ❌ Missing | SecurityEventContextMappingCommConnector | - | Not found in implementation |
| ❌ Missing | SecurityEventContextMappingFunctionalCluster | - | Not found in implementation |
| ❌ Missing | SecurityEventContextProps | - | Not found in implementation |
| ❌ Missing | SecurityEventDefinition | - | Not found in implementation |
| ❌ Missing | SecurityEventFilterChain | - | Not found in implementation |
| ❌ Missing | SecurityEventOneEveryNFilter | - | Not found in implementation |
| ❌ Missing | SecurityEventStateFilter | - | Not found in implementation |
| ❌ Missing | SecurityEventThresholdFilter | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | SecurityEventContextDataSourceEnum | useFirstContextData, useLastContextData | - | - | Not found in implementation |
| ❌ Missing | SecurityEventReportingModeEnum | brief, briefBypassing, detailed, Security, AUTOSAR, detailedBypassing, off | - | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::EcuResourceTemplate

**Summary:**
- Classes: 1/8 implemented, 7 missing, 5 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | HwElementConnector | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementConnector.py | Line 12 |
| ❌ Missing | HwDescriptionEntity | - | Not found in implementation |
| ❌ Missing | HwElement | - | Not found in implementation |
| ❌ Missing | HwPin | - | Not found in implementation |
| ❌ Missing | HwPinConnector | - | Not found in implementation |
| ❌ Missing | HwPinGroup | - | Not found in implementation |
| ❌ Missing | HwPinGroupConnector | - | Not found in implementation |
| ❌ Missing | HwPinGroupContent | - | Not found in implementation |
| ➕ Extra | HwAttributeDef | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Not documented in requirements |
| ➕ Extra | HwAttributeLiteralDef | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwAttributeValue.py | Not documented in requirements |
| ➕ Extra | HwAttributeValue | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Not documented in requirements |
| ➕ Extra | HwCategory | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Not documented in requirements |
| ➕ Extra | HwType | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory

**Summary:**
- Classes: 4/5 implemented, 1 missing
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | HwAttributeDef | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Line 108 |
| ✅ Implemented | HwAttributeValue | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Line 27 |
| ✅ Implemented | HwCategory | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Line 201 |
| ✅ Implemented | HwType | src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py | Line 91 |
| ❌ Missing | HwAttributeLiteralDef | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::LogAndTraceExtract

**Summary:**
- Classes: 0/7 implemented, 7 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory LogAndTraceExtract/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DltApplication | - | Not found in implementation |
| ❌ Missing | DltArgument | - | Not found in implementation |
| ❌ Missing | DltContext | - | Not found in implementation |
| ❌ Missing | DltEcu | - | Not found in implementation |
| ❌ Missing | DltMessage | - | Not found in implementation |
| ❌ Missing | LogAndTraceMessageCollectionSet | - | Not found in implementation |
| ❌ Missing | PrivacyLevel | - | Not found in implementation |

### Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall

**Summary:**
- Classes: 3/3 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Firewall/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | FirewallRule | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRule.py | Line 6 |
| ✅ Implemented | FirewallRuleProps | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRuleProps.py | Line 4 |
| ✅ Implemented | StateDependentFirewall | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/StateDependentFirewall.py | Line 6 |

### Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::CryptoDeployment

**Summary:**
- Classes: 1/1 implemented, 1 extra
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory CryptoDeployment/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | CryptoKeySlot | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/CryptoKeySlot.py | Line 22 |
| ➕ Extra | CryptoKeySlotContent | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/CryptoKeySlotContent.py | Not documented in requirements |

### Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem

**Summary:**
- Classes: 2/2 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory IntrusionDetectionSystem/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | IdsPlatformInstantiation | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsPlatformInstantiation.py | Line 11 |
| ✅ Implemented | IdsmModuleInstantiation | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsmModuleInstantiation.py | Line 9 |

### Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::AdaptiveModule

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory AdaptiveModule/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | PlatformModuleEthernetEndpointConfiguration | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/AdaptiveModule/PlatformModuleEthernetEndpointConfiguration.py | Line 16 |

### Package: M2::AUTOSARTemplates::AdaptivePlatform::ApplicationDesign::PortInterface

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory PortInterface/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Field | src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/ApplicationDesign/PortInterface/Field.py | Line 6 |

### Package: M2::AUTOSARTemplates::AbstractPlatform

**Summary:**
- Classes: 2/2 implemented
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory AbstractPlatform/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | ApplicationDeferredDataType | src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform/ApplicationDeferredDataType.py | Line 9 |
| ✅ Implemented | ApplicationInterface | src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform/ApplicationInterface.py | Line 19 |

### Package: M2::AUTOSARTemplates::FeatureModelTemplate

**Summary:**
- Classes: 0/17 implemented, 17 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory FeatureModelTemplate/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | FMAttributeDef | - | Not found in implementation |
| ❌ Missing | FMAttributeValue | - | Not found in implementation |
| ❌ Missing | FMConditionByFeaturesAndAttributes | - | Not found in implementation |
| ❌ Missing | FMConditionByFeaturesAndSwSystemconsts | - | Not found in implementation |
| ❌ Missing | FMFeature | - | Not found in implementation |
| ❌ Missing | FMFeatureDecomposition | - | Not found in implementation |
| ❌ Missing | FMFeatureMap | - | Not found in implementation |
| ❌ Missing | FMFeatureMapAssertion | - | Not found in implementation |
| ❌ Missing | FMFeatureMapCondition | - | Not found in implementation |
| ❌ Missing | FMFeatureMapElement | - | Not found in implementation |
| ❌ Missing | FMFeatureModel | - | Not found in implementation |
| ❌ Missing | FMFeatureRelation | - | Not found in implementation |
| ❌ Missing | FMFeatureRestriction | - | Not found in implementation |
| ❌ Missing | FMFeatureSelection | - | Not found in implementation |
| ❌ Missing | FMFeatureSelectionSet | - | Not found in implementation |
| ❌ Missing | FMFormulaByFeaturesAndAttributes | - | Not found in implementation |
| ❌ Missing | FMFormulaByFeaturesAndSwSystemconsts | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | FMFeatureSelectionState | deselected, selected, undecided | - | - | Not found in implementation |

### Package: M2::MSR::DataDictionary::ServiceProcessTask

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both ServiceProcessTask.py and ServiceProcessTask/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwServiceArg | src/armodel/models/M2/MSR/DataDictionary/ServiceProcessTask.py | Line 4 |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | SwServiceImplPolicyEnum | inline, inlineConditional, standard | - | - | Not found in implementation |

### Package: M2::MSR::DataDictionary::DataDefProperties

**Summary:**
- Classes: 4/7 implemented, 3 missing, 2 extra
- Enums: 1/3 implemented, 2 missing, 1 literal mismatches

⚠️ **Structure Mismatch Warning**

Hybrid structure: both DataDefProperties.py and DataDefProperties/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwDataDefProps | src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py | Line 53 |
| ✅ Implemented | SwPointerTargetProps | src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py | Line 301 |
| ✅ Implemented | SwTextProps | src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py | Line 352 |
| ✅ Implemented | ValueList | src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py | Line 331 |
| ❌ Missing | SwBitRepresentation | - | Not found in implementation |
| ❌ Missing | SwDataDependency | - | Not found in implementation |
| ❌ Missing | SwDataDependencyArgs | - | Not found in implementation |
| ➕ Extra | SwDataDefPropsConditional | src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py | Not documented in requirements |
| ➕ Extra | SwImplPolicyEnum | src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | SwImplPolicyEnum | AUTOSAR, Basic, const, fixed, measurementPoint, queued, standard | const, fixed, measurementPoint, queued, standard | src/armodel/models/M2/MSR/DataDictionary/DataDefProperties.py | Line 7; Missing: AUTOSAR, Basic |
| ❌ Missing | DisplayPresentationEnum | presentationContinuous, presentationDiscrete | - | - | Not found in implementation |
| ❌ Missing | SwCalibrationAccessEnum | notAccessible, readOnly, readWrite | - | - | Not found in implementation |

### Package: M2::MSR::DataDictionary::AuxillaryObjects

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both AuxillaryObjects.py and AuxillaryObjects/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwAddrMethod | src/armodel/models/M2/MSR/DataDictionary/AuxillaryObjects.py | Line 5 |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | MemoryAllocationKeywordPolicyType | addrMethodShort, Name, addrMethodShort, NameAndAlignment | - | - | Not found in implementation |
| ❌ Missing | MemorySectionType | calibrationVariables, calprm, code, configData, const, excludeFromFlashtime, var | - | - | Not found in implementation |

### Package: M2::MSR::DataDictionary::SystemConstant

**Summary:**
- Classes: 1/1 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwSystemconst | src/armodel/models/M2/MSR/DataDictionary/SystemConstant.py | Line 10 |

### Package: M2::MSR::DataDictionary::CalibrationParameter

**Summary:**
- Classes: 3/3 implemented
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both CalibrationParameter.py and CalibrationParameter/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwCalprmAxis | src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py | Line 16 |
| ✅ Implemented | SwCalprmAxisSet | src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py | Line 26 |
| ✅ Implemented | SwCalprmAxisTypeProps | src/armodel/models/M2/MSR/DataDictionary/CalibrationParameter.py | Line 5 |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | CalprmAxisCategoryEnum | Software, AUTOSAR, comAxis, fixAXIS, resAxis, stdAxis | - | - | Not found in implementation |

### Package: M2::MSR::DataDictionary::Axis

**Summary:**
- Classes: 4/6 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both Axis.py and Axis/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwAxisGeneric | src/armodel/models/M2/MSR/DataDictionary/Axis.py | Line 25 |
| ✅ Implemented | SwAxisGrouped | src/armodel/models/M2/MSR/DataDictionary/Axis.py | Line 116 |
| ✅ Implemented | SwAxisIndividual | src/armodel/models/M2/MSR/DataDictionary/Axis.py | Line 46 |
| ✅ Implemented | SwGenericAxisParam | src/armodel/models/M2/MSR/DataDictionary/Axis.py | Line 4 |
| ❌ Missing | SwAxisType | - | Not found in implementation |
| ❌ Missing | SwGenericAxisParamType | - | Not found in implementation |

### Package: M2::MSR::DataDictionary::DatadictionaryProxies

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory DatadictionaryProxies/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | SwCalprmRefProxy | - | Not found in implementation |
| ❌ Missing | SwVariableRefProxy | - | Not found in implementation |

### Package: M2::MSR::DataDictionary::RecordLayout

**Summary:**
- Classes: 4/4 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwRecordLayout | src/armodel/models/M2/MSR/DataDictionary/RecordLayout.py | Line 196 |
| ✅ Implemented | SwRecordLayoutGroup | src/armodel/models/M2/MSR/DataDictionary/RecordLayout.py | Line 103 |
| ✅ Implemented | SwRecordLayoutGroupContent | src/armodel/models/M2/MSR/DataDictionary/RecordLayout.py | Line 73 |
| ✅ Implemented | SwRecordLayoutV | src/armodel/models/M2/MSR/DataDictionary/RecordLayout.py | Line 4 |

### Package: M2::MSR::AsamHdo::ComputationMethod

**Summary:**
- Classes: 15/16 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both ComputationMethod.py and ComputationMethod/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Compu | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 42 |
| ✅ Implemented | CompuConst | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 24 |
| ✅ Implemented | CompuConstContent | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 68 |
| ✅ Implemented | CompuConstFormulaContent | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 117 |
| ✅ Implemented | CompuConstNumericContent | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 100 |
| ✅ Implemented | CompuConstTextContent | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 82 |
| ✅ Implemented | CompuContent | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 12 |
| ✅ Implemented | CompuMethod | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 326 |
| ✅ Implemented | CompuNominatorDenominator | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 209 |
| ✅ Implemented | CompuRationalCoeffs | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 166 |
| ✅ Implemented | CompuScale | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 227 |
| ✅ Implemented | CompuScaleConstantContents | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 149 |
| ✅ Implemented | CompuScaleContents | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 137 |
| ✅ Implemented | CompuScaleRationalFormula | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 192 |
| ✅ Implemented | CompuScales | src/armodel/models/M2/MSR/AsamHdo/ComputationMethod.py | Line 309 |
| ❌ Missing | CompuGenericMath | - | Not found in implementation |

### Package: M2::MSR::AsamHdo::BaseTypes

**Summary:**
- Classes: 4/4 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | BaseType | src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py | Line 69 |
| ✅ Implemented | BaseTypeDefinition | src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py | Line 6 |
| ✅ Implemented | BaseTypeDirectDefinition | src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py | Line 18 |
| ✅ Implemented | SwBaseType | src/armodel/models/M2/MSR/AsamHdo/BaseTypes.py | Line 89 |

### Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints

**Summary:**
- Classes: 4/5 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both GlobalConstraints.py and GlobalConstraints/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | DataConstr | src/armodel/models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py | Line 45 |
| ✅ Implemented | DataConstrRule | src/armodel/models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py | Line 32 |
| ✅ Implemented | InternalConstrs | src/armodel/models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py | Line 7 |
| ✅ Implemented | PhysConstrs | src/armodel/models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py | Line 19 |
| ❌ Missing | ScaleConstr | - | Not found in implementation |

### Package: M2::MSR::AsamHdo::SpecialData

**Summary:**
- Classes: 3/5 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both SpecialData.py and SpecialData/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Sd | src/armodel/models/M2/MSR/AsamHdo/SpecialData.py | Line 7 |
| ✅ Implemented | Sdg | src/armodel/models/M2/MSR/AsamHdo/SpecialData.py | Line 51 |
| ✅ Implemented | SdgCaption | src/armodel/models/M2/MSR/AsamHdo/SpecialData.py | Line 32 |
| ❌ Missing | Sdf | - | Not found in implementation |
| ❌ Missing | SdgContents | - | Not found in implementation |

### Package: M2::MSR::AsamHdo::Units

**Summary:**
- Classes: 3/5 implemented, 2 missing, 1 extra
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both Units.py and Units/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | PhysicalDimension | src/armodel/models/M2/MSR/AsamHdo/Units.py | Line 16 |
| ✅ Implemented | Unit | src/armodel/models/M2/MSR/AsamHdo/Units.py | Line 93 |
| ✅ Implemented | UnitGroup | src/armodel/models/M2/MSR/AsamHdo/Units.py | Line 136 |
| ❌ Missing | PhysicalDimensionMapping | - | Not found in implementation |
| ❌ Missing | PhysicalDimensionMappingSet | - | Not found in implementation |
| ➕ Extra | SingleLanguageUnitNames | src/armodel/models/M2/MSR/AsamHdo/Units.py | Not documented in requirements |

### Package: M2::MSR::AsamHdo::AdminData

**Summary:**
- Classes: 3/3 implemented
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | AdminData | src/armodel/models/M2/MSR/AsamHdo/AdminData.py | Line 111 |
| ✅ Implemented | DocRevision | src/armodel/models/M2/MSR/AsamHdo/AdminData.py | Line 37 |
| ✅ Implemented | Modification | src/armodel/models/M2/MSR/AsamHdo/AdminData.py | Line 8 |

### Package: M2::MSR::Documentation::BlockElements

**Summary:**
- Classes: 0/2 implemented, 2 missing, 5 extra
- Enums: 0/0 implemented, 1 extra

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Caption | - | Not found in implementation |
| ❌ Missing | DocumentationBlock | - | Not found in implementation |
| ➕ Extra | Graphic | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Not documented in requirements |
| ➕ Extra | GraphicFitEnum | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Not documented in requirements |
| ➕ Extra | LGraphic | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Not documented in requirements |
| ➕ Extra | Map | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Not documented in requirements |
| ➕ Extra | MlFigure | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ➕ Extra | GraphicFitEnum | - | - | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Not documented in requirements |

### Package: M2::MSR::Documentation::BlockElements::RequirementsTracing

**Summary:**
- Classes: 0/3 implemented, 3 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory RequirementsTracing/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | StructuredReq | - | Not found in implementation |
| ❌ Missing | Traceable | - | Not found in implementation |
| ❌ Missing | TraceableText | - | Not found in implementation |

### Package: M2::MSR::Documentation::BlockElements::Formula

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Formula/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | MlFormula | - | Not found in implementation |

### Package: M2::MSR::Documentation::BlockElements::ListElements

**Summary:**
- Classes: 0/7 implemented, 7 missing
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory ListElements/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DefItem | - | Not found in implementation |
| ❌ Missing | DefList | - | Not found in implementation |
| ❌ Missing | IndentSample | - | Not found in implementation |
| ❌ Missing | Item | - | Not found in implementation |
| ❌ Missing | LabeledItem | - | Not found in implementation |
| ❌ Missing | LabeledList | - | Not found in implementation |
| ❌ Missing | List | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | ItemLabelPosEnum | newline, newlineIfNecessary, noNewline | - | - | Not found in implementation |
| ❌ Missing | ListEnum | number, unnumber | - | - | Not found in implementation |

### Package: M2::MSR::Documentation::BlockElements::Figure

**Summary:**
- Classes: 4/5 implemented, 1 missing, 1 extra
- Enums: 1/4 implemented, 3 missing, 1 literal mismatches

⚠️ **Structure Mismatch Warning**

Hybrid structure: both Figure.py and Figure/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Graphic | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Line 16 |
| ✅ Implemented | LGraphic | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Line 81 |
| ✅ Implemented | Map | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Line 76 |
| ✅ Implemented | MlFigure | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Line 114 |
| ❌ Missing | Area | - | Not found in implementation |
| ➕ Extra | GraphicFitEnum | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ⚠️ Literal Mismatch | GraphicFitEnum | AUTOSAR, AsIs, FitToPage, Generic, LimitToPage, LimitToText, Rotate180Rotate180LimitTo, Rotate90CcwFitToTextRotate90CcwLimit, Rotate90Cw, Rotate90CwFitToTextRotate90CwLimitTo, Rotate90ccw, Text, ToText | - | src/armodel/models/M2/MSR/Documentation/BlockElements/Figure.py | Line 9; Missing: AUTOSAR, AsIs, FitToPage, Generic, LimitToPage, LimitToText, Rotate180Rotate180LimitTo, Rotate90CcwFitToTextRotate90CcwLimit, Rotate90Cw, Rotate90CwFitToTextRotate90CwLimitTo, Rotate90ccw, Text, ToText |
| ❌ Missing | AreaEnumNohref | nohref | - | - | Not found in implementation |
| ❌ Missing | AreaEnumShape | Generic, AUTOSAR, circle, default, poly, rect | - | - | Not found in implementation |
| ❌ Missing | GraphicNotationEnum | bmp, eps, gif, jpg, pdf, png, Generic, AUTOSAR, tiff | - | - | Not found in implementation |

### Package: M2::MSR::Documentation::BlockElements::Note

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Note/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Note | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | NoteTypeEnum | caution, example, exercise, hint, instruction, other, tip | - | - | Not found in implementation |

### Package: M2::MSR::Documentation::BlockElements::PaginationAndView

**Summary:**
- Classes: 0/2 implemented, 2 missing
- Enums: 0/2 implemented, 2 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory PaginationAndView/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | DocumentViewSelectable | - | Not found in implementation |
| ❌ Missing | Paginateable | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | ChapterEnumBreak | break, noBreak | - | - | Not found in implementation |
| ❌ Missing | KeepWithPreviousEnum | Generic, AUTOSAR, keep, noKeep | - | - | Not found in implementation |

### Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable

**Summary:**
- Classes: 0/6 implemented, 6 missing
- Enums: 0/5 implemented, 5 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory OasisExchangeTable/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Colspec | - | Not found in implementation |
| ❌ Missing | Entry | - | Not found in implementation |
| ❌ Missing | Row | - | Not found in implementation |
| ❌ Missing | Table | - | Not found in implementation |
| ❌ Missing | Tbody | - | Not found in implementation |
| ❌ Missing | Tgroup | - | Not found in implementation |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | AlignEnum | center, justify, leftright | - | - | Not found in implementation |
| ❌ Missing | FloatEnum | float, noFloat | - | - | Not found in implementation |
| ❌ Missing | FrameEnum | all, bottom, none, sides, top, topbot | - | - | Not found in implementation |
| ❌ Missing | PgwideEnum | noPgwide, Generic, AUTOSAR, pgwide | - | - | Not found in implementation |
| ❌ Missing | ValignEnum | bottom, middle, top | - | - | Not found in implementation |

### Package: M2::MSR::Documentation::BlockElements::GerneralParameters

**Summary:**
- Classes: 0/1 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory GerneralParameters/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Prms | - | Not found in implementation |

### Package: M2::MSR::Documentation::TextModel::MultilanguageData

**Summary:**
- Classes: 4/5 implemented, 1 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both MultilanguageData.py and MultilanguageData/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | MultiLanguageOverviewParagraph | src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py | Line 21 |
| ✅ Implemented | MultiLanguageParagraph | src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py | Line 7 |
| ✅ Implemented | MultiLanguagePlainText | src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py | Line 48 |
| ✅ Implemented | MultilanguageLongName | src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py | Line 35 |
| ❌ Missing | MultiLanguageVerbatim | - | Not found in implementation |

### Package: M2::MSR::Documentation::TextModel::LanguageDataModel

**Summary:**
- Classes: 5/7 implemented, 2 missing, 1 extra
- Enums: 0/1 implemented, 1 missing

⚠️ **Structure Mismatch Warning**

Hybrid structure: both LanguageDataModel.py and LanguageDataModel/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | LLongName | src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py | Line 50 |
| ✅ Implemented | LOverviewParagraph | src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py | Line 40 |
| ✅ Implemented | LParagraph | src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py | Line 45 |
| ✅ Implemented | LPlainText | src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py | Line 55 |
| ✅ Implemented | LanguageSpecific | src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py | Line 15 |
| ❌ Missing | LVerbatim | - | Not found in implementation |
| ❌ Missing | WhitespaceControlled | - | Not found in implementation |
| ➕ Extra | LEnum | src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py | Not documented in requirements |

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | LEnum | aa, ab, af, am, ar, as, ay, az, ba, be, bg, bh, Generic, AUTOSARbi, bn, bo, br, ca, co, cs, cy, da, de, dz, el, en, eo, es, et, eu, fa, fi, fj, fo, Generic, AUTOSAR, forAll, fr, fy, ga, gd, gl, gn, gu, ha, hi, hr, hu, hy, ia, ie, ik, in, is, it, iw, ja, Generic, AUTOSARji, jw, ka, kk, kl, km, kn, ko, ks, ku, ky, la, ln, lo, lt, lv, mg, mi, mk, ml, mn, Generic, AUTOSARmo, mr, ms, mt, my, na, ne, nl, no, oc, om, or, pa, pl, ps, pt, qu, rm, rn, ro, ru, Generic, AUTOSARrw, sa, sd, sg, sh, si, sk, sl, sm, sn, so, sq, sr, ss, st, su, sv, sw, ta, te, tg, Generic, AUTOSARth, ti, tk, tl, tn, to, tr, ts, tt, tw, uk, ur, uz, vi, vo, wo, xh, yo, zh, zu | - | - | Not found in implementation |

### Package: M2::MSR::Documentation::TextModel::SingleLanguageData

**Summary:**
- Classes: 0/4 implemented, 4 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory SingleLanguageData/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | SingleLanguageLongName | - | Not found in implementation |
| ❌ Missing | SingleLanguageUnitNames | - | Not found in implementation |
| ❌ Missing | SlOverviewParagraph | - | Not found in implementation |
| ❌ Missing | SlParagraph | - | Not found in implementation |

### Package: M2::MSR::Documentation::TextModel::InlineTextModel

**Summary:**
- Classes: 0/6 implemented, 6 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InlineTextModel/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | MixedContentForLongName | - | Not found in implementation |
| ❌ Missing | MixedContentForOverviewParagraph | - | Not found in implementation |
| ❌ Missing | MixedContentForParagraph | - | Not found in implementation |
| ❌ Missing | MixedContentForPlainText | - | Not found in implementation |
| ❌ Missing | MixedContentForUnitNames | - | Not found in implementation |
| ❌ Missing | MixedContentForVerbatim | - | Not found in implementation |

### Package: M2::MSR::Documentation::TextModel::InlineTextElements

**Summary:**
- Classes: 0/9 implemented, 9 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InlineTextElements/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Br | - | Not found in implementation |
| ❌ Missing | EmphasisText | - | Not found in implementation |
| ❌ Missing | IndexEntry | - | Not found in implementation |
| ❌ Missing | Std | - | Not found in implementation |
| ❌ Missing | Tt | - | Not found in implementation |
| ❌ Missing | Xdoc | - | Not found in implementation |
| ❌ Missing | Xfile | - | Not found in implementation |
| ❌ Missing | Xref | - | Not found in implementation |
| ❌ Missing | XrefTarget | - | Not found in implementation |

### Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums

**Summary:**
- Classes: 0/0 implemented
- Enums: 0/12 implemented, 12 missing

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory InlineAttributeEnums/

#### Enumerations

| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |
|--------|-----------|-------------------|----------------------|----------|-------|
| ❌ Missing | EEnum | bold, bolditalic, italic, plain | - | - | Not found in implementation |
| ❌ Missing | EEnumFont | default, mono | - | - | Not found in implementation |
| ❌ Missing | ResolutionPolicyEnum | noSloppy, sloppy | - | - | Not found in implementation |
| ❌ Missing | ShowContentEnum | noShowContent, showContent | - | - | Not found in implementation |
| ❌ Missing | ShowResourceAliasNameEnum | noShowAliasName, showAliasName | - | - | Not found in implementation |
| ❌ Missing | ShowResourceCategoryEnum | noShowCategory, showCategory | - | - | Not found in implementation |
| ❌ Missing | ShowResourceLongNameEnum | noShowLongName, showLongName | - | - | Not found in implementation |
| ❌ Missing | ShowResourceNumberEnum | noShowNumber, showNumber | - | - | Not found in implementation |
| ❌ Missing | ShowResourcePageEnum | noShowPage, showPage | - | - | Not found in implementation |
| ❌ Missing | ShowResourceShortNameEnum | noShowShortName, showShortName | - | - | Not found in implementation |
| ❌ Missing | ShowResourceTypeEnum | noShowType, showType | - | - | Not found in implementation |
| ❌ Missing | ShowSeeEnum | noShowSee, showSee | - | - | Not found in implementation |

### Package: M2::MSR::Documentation::Annotation

**Summary:**
- Classes: 1/1 implemented, 1 extra
- Enums: 0/0 implemented

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | Annotation | src/armodel/models/M2/MSR/Documentation/Annotation.py | Line 39 |
| ➕ Extra | GeneralAnnotation | src/armodel/models/M2/MSR/Documentation/Annotation.py | Not documented in requirements |

### Package: M2::MSR::Documentation::Chapters

**Summary:**
- Classes: 0/9 implemented, 9 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory Chapters/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | Chapter | - | Not found in implementation |
| ❌ Missing | ChapterContent | - | Not found in implementation |
| ❌ Missing | ChapterModel | - | Not found in implementation |
| ❌ Missing | ChapterOrMsrQuery | - | Not found in implementation |
| ❌ Missing | PredefinedChapter | - | Not found in implementation |
| ❌ Missing | Topic1 | - | Not found in implementation |
| ❌ Missing | TopicContent | - | Not found in implementation |
| ❌ Missing | TopicContentOrMsrQuery | - | Not found in implementation |
| ❌ Missing | TopicOrMsrQuery | - | Not found in implementation |

### Package: M2::MSR::Documentation::MsrQuery

**Summary:**
- Classes: 0/8 implemented, 8 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Wrong structure: Package should be a single file (no subpackages) but is implemented as a directory MsrQuery/

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ❌ Missing | MsrQueryArg | - | Not found in implementation |
| ❌ Missing | MsrQueryChapter | - | Not found in implementation |
| ❌ Missing | MsrQueryP1 | - | Not found in implementation |
| ❌ Missing | MsrQueryP2 | - | Not found in implementation |
| ❌ Missing | MsrQueryProps | - | Not found in implementation |
| ❌ Missing | MsrQueryResultChapter | - | Not found in implementation |
| ❌ Missing | MsrQueryResultTopic1 | - | Not found in implementation |
| ❌ Missing | MsrQueryTopic1 | - | Not found in implementation |

### Package: M2::MSR::CalibrationData::CalibrationValue

**Summary:**
- Classes: 2/4 implemented, 2 missing
- Enums: 0/0 implemented

⚠️ **Structure Mismatch Warning**

Hybrid structure: both CalibrationValue.py and CalibrationValue/ exist. Requirements say this is a leaf package. Expected: single file.

#### Classes

| Status | Class Name | Location | Notes |
|--------|------------|----------|-------|
| ✅ Implemented | SwValueCont | src/armodel/models/M2/MSR/CalibrationData/CalibrationValue.py | Line 20 |
| ✅ Implemented | SwValues | src/armodel/models/M2/MSR/CalibrationData/CalibrationValue.py | Line 6 |
| ❌ Missing | SwAxisCont | - | Not found in implementation |
| ❌ Missing | ValueGroup | - | Not found in implementation |

---

*Report generated by compare-package-implementation.py*
