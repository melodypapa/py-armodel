"""
This module contains comprehensive tests for the ARPackage.py file
in the AUTOSAR GenericStructure module.
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIndicatorTypeEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import LifeCycleState
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    CalibrationParameterValue,
    DiagnosticCommonProps,
    DiagnosticConnectedIndicator,
    DiagnosticControlEnableMaskBit,
    DiagnosticEventWindow,
    DiagnosticIumprGroupIdentifier,
    DiagnosticMemoryDestination,
    DiagnosticParameter,
    DiagnosticSupportInfoByte,
    DiagnosticTestIdentifier,
    PhysicalDimensionMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
    ARPackage,
    CalibrationParameterValueSet,
    CpSwClusterResourceToDiagDataElemMapping,
    CpSwClusterResourceToDiagFunctionIdMapping,
    CpSwClusterToDiagEventMapping,
    CpSwClusterToDiagRoutineSubfunctionMapping,
    DiagnosticAbstractAliasEvent,
    DiagnosticAbstractDataIdentifier,
    DiagnosticAging,
    DiagnosticAuthentication,
    DiagnosticAuthenticationConfiguration,
    DiagnosticAuthRole,
    DiagnosticAuthTransmitCertificate,
    DiagnosticAuthTransmitCertificateMapping,
    DiagnosticClearDiagnosticInformation,
    DiagnosticClearResetEmissionRelatedInfo,
    DiagnosticComControl,
    DiagnosticCondition,
    DiagnosticConditionGroup,
    DiagnosticContributionSet,
    DiagnosticControlDTCSetting,
    DiagnosticCustomServiceInstance,
    DiagnosticDataByIdentifier,
    DiagnosticDataIdentifier,
    DiagnosticDataIdentifierSet,
    DiagnosticDataTransfer,
    DiagnosticDeAuthentication,
    DiagnosticDemProvidedDataMapping,
    DiagnosticDynamicallyDefineDataIdentifier,
    DiagnosticDynamicDataIdentifier,
    DiagnosticEcuInstanceProps,
    DiagnosticEcuReset,
    DiagnosticEnableCondition,
    DiagnosticEnableConditionGroup,
    DiagnosticEnableConditionPortMapping,
    DiagnosticEvent,
    DiagnosticEventPortMapping,
    DiagnosticEventToDebounceAlgorithmMapping,
    DiagnosticEventToEnableConditionGroupMapping,
    DiagnosticEventToOperationCycleMapping,
    DiagnosticEventToSecurityEventMapping,
    DiagnosticEventToStorageConditionGroupMapping,
    DiagnosticEventToTroubleCodeJ1939Mapping,
    DiagnosticEventToTroubleCodeUdsMapping,
    DiagnosticExtendedDataRecord,
    DiagnosticFimAliasEvent,
    DiagnosticFimAliasEventGroup,
    DiagnosticFimAliasEventGroupMapping,
    DiagnosticFimAliasEventMapping,
    DiagnosticFimEventGroup,
    DiagnosticFimFunctionMapping,
    DiagnosticFreezeFrame,
    DiagnosticFunctionIdentifier,
    DiagnosticIndicator,
    DiagnosticInfoType,
    DiagnosticInhibitSourceEventMapping,
    DiagnosticIOControl,
    DiagnosticIumpr,
    DiagnosticIumprDenominatorGroup,
    DiagnosticIumprGroup,
    DiagnosticIumprToFunctionIdentifierMapping,
    DiagnosticJ1939ExpandedFreezeFrame,
    DiagnosticJ1939FreezeFrame,
    DiagnosticJ1939Node,
    DiagnosticJ1939Spn,
    DiagnosticJ1939SpnMapping,
    DiagnosticJ1939SwMapping,
    DiagnosticMapping,
    DiagnosticMasterToSlaveEventMapping,
    DiagnosticMeasurementIdentifier,
    DiagnosticMemoryAddressableRangeAccess,
    DiagnosticMemoryByAddress,
    DiagnosticMemoryDestinationPrimary,
    DiagnosticMemoryIdentifier,
    DiagnosticOperationCycle,
    DiagnosticOperationCyclePortMapping,
    DiagnosticParameterElementAccess,
    DiagnosticParameterIdentifier,
    DiagnosticPowertrainFreezeFrame,
    DiagnosticProofOfOwnership,
    DiagnosticProtocol,
    DiagnosticReadDataByIdentifier,
    DiagnosticReadDataByPeriodicID,
    DiagnosticReadDTCInformation,
    DiagnosticReadMemoryByAddress,
    DiagnosticReadScalingDataByIdentifier,
    DiagnosticRequestControlOfOnBoardDevice,
    DiagnosticRequestCurrentPowertrainData,
    DiagnosticRequestDownload,
    DiagnosticRequestEmissionRelatedDTC,
    DiagnosticRequestEmissionRelatedDTCPermanentStatus,
    DiagnosticRequestFileTransfer,
    DiagnosticRequestOnBoardMonitoringTestResults,
    DiagnosticRequestPowertrainFreezeFrameData,
    DiagnosticRequestUpload,
    DiagnosticRequestVehicleInfo,
    DiagnosticResponseOnEvent,
    DiagnosticRoutine,
    DiagnosticRoutineControl,
    DiagnosticSecurityAccess,
    DiagnosticSecurityEventReportingModeMapping,
    DiagnosticServiceDataMapping,
    DiagnosticServiceMappingDiagTarget,
    DiagnosticServiceSwMapping,
    DiagnosticSessionControl,
    DiagnosticStorageCondition,
    DiagnosticStorageConditionGroup,
    DiagnosticStorageConditionPortMapping,
    DiagnosticSwMapping,
    DiagnosticTestResult,
    DiagnosticTestRoutineIdentifier,
    DiagnosticTransferExit,
    DiagnosticTroubleCode,
    DiagnosticTroubleCodeGroup,
    DiagnosticTroubleCodeJ1939,
    DiagnosticTroubleCodeUdsToTroubleCodeObdMapping,
    DiagnosticVerifyCertificateBidirectional,
    DiagnosticVerifyCertificateUnidirectional,
    DiagnosticWriteDataByIdentifier,
    DiagnosticWriteMemoryByAddress,
    LifeCycleStateDefinitionGroup,
    PackageableElement,
    PhysicalDimensionMappingSet,
    ReferenceBase,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    DiagnosticAuthTransmitCertificateEvaluation,
    DiagnosticRequestRoutineResults,
    DiagnosticStartRoutine,
    DiagnosticStopRoutine,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
    Boolean,
    DiagnosticClearEventAllowedBehaviorEnum,
    DiagnosticEventClearAllowedEnum,
    DiagnosticEventKindEnum,
    DiagnosticIumprKindEnum,
    DiagnosticObdSupportEnum,
    DiagnosticOperationCycleTypeEnum,
    DiagnosticRecordTriggerEnum,
    DiagnosticResponseOnEventActionEnum,
    DiagnosticTestResultUpdateEnum,
    DiagnosticTroubleCodeJ1939DtcKindEnum,
    DiagnosticTypeOfDtcSupportedEnum,
    Identifier,
    NameToken,
    PositiveInteger,
    ReferrableSubtypesEnum,
    RefType,
    String,
    TimeValue,
    UriString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclObjectSet,
    AclOperation,
    AclPermission,
    AclRole,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet import ViewMap, ViewMapSet


class TestReferenceBase:
    """
    Test class for ReferenceBase functionality.
    """

    def test_initialization(self):
        """
        Test ReferenceBase initialization.
        """
        obj = ReferenceBase()

        # Verify default values for attributes
        assert obj.getGlobalElements() == []
        assert obj.getGlobalInPackageRefs() == []
        assert obj.getIsDefault() is None
        assert obj.getIsGlobal() is None
        assert obj.getBaseIsThisPackage() is None
        assert obj.getPackageRef() is None
        assert obj.getShortLabel() is None

    def test_get_set_global_elements(self):
        """
        Test get/set methods for global elements.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getGlobalElements() == []

        # Test adding global element
        element = ReferrableSubtypesEnum().setValue("TestElement")
        result = obj.addGlobalElement(element)
        assert result is obj  # Verify method chaining
        assert obj.getGlobalElements() == [element]

    def test_get_set_global_in_package_refs(self):
        """
        Test get/set methods for global in-package references.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getGlobalInPackageRefs() == []

        # Test adding global in-package ref
        ref = RefType().setValue("/Package/Element")
        result = obj.addGlobalInPackageRef(ref)
        assert result is obj  # Verify method chaining
        assert obj.getGlobalInPackageRefs() == [ref]

    def test_get_set_is_default(self):
        """
        Test get/set methods for isDefault flag.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getIsDefault() is None

        # Test setting isDefault
        result = obj.setIsDefault(Boolean().setValue(True))
        assert result is obj  # Verify method chaining
        assert obj.getIsDefault().value is True

    def test_get_set_is_global(self):
        """
        Test get/set methods for isGlobal flag.

        Spec (R4.3.1): AUTOSAR_TPS_GenericStructureTemplate.pdf, Table 4.5, pp.54-55
        Attribute removed in R23-11 (absent from Table 4.14) — kept as optional legacy deviation.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getIsGlobal() is None

        # Test setting isGlobal
        result = obj.setIsGlobal(Boolean().setValue(False))
        assert result is obj  # Verify method chaining
        assert obj.getIsGlobal().value is False

    def test_get_set_base_is_this_package(self):
        """
        Test get/set methods for baseIsThisPackage flag.

        Spec (R4.3.1): AUTOSAR_TPS_GenericStructureTemplate.pdf, Table 4.5, pp.54-55
        Attribute removed in R23-11 (absent from Table 4.14) — kept as optional legacy deviation.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getBaseIsThisPackage() is None

        # Test setting baseIsThisPackage
        result = obj.setBaseIsThisPackage(Boolean().setValue(True))
        assert result is obj  # Verify method chaining
        assert obj.getBaseIsThisPackage().value is True

    def test_get_set_package_ref(self):
        """
        Test get/set methods for package references.

        Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.14, p.72
        package is 0..1 — a single optional reference, not a list.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getPackageRef() is None

        # Test setting package ref
        ref = RefType().setValue("/Package/Element")
        result = obj.setPackageRef(ref)
        assert result is obj  # Verify method chaining
        assert obj.getPackageRef() == ref

        # None is a no-op (Rule 0004)
        obj.setPackageRef(None)
        assert obj.getPackageRef() == ref

    def test_setter_none_no_op_guards(self):
        """
        Test that value setters treat None as a no-op (Rule 0004).
        """
        obj = ReferenceBase()
        obj.setIsDefault(Boolean().setValue(True))
        obj.setIsGlobal(Boolean().setValue(True))
        obj.setBaseIsThisPackage(Boolean().setValue(True))
        obj.setPackageRef(RefType().setValue("/Pkg"))
        obj.setShortLabel(Identifier().setValue("L1"))

        obj.setIsDefault(None)
        obj.setIsGlobal(None)
        obj.setBaseIsThisPackage(None)
        obj.setPackageRef(None)
        obj.setShortLabel(None)

        assert obj.getIsDefault().value is True
        assert obj.getIsGlobal().value is True
        assert obj.getBaseIsThisPackage().value is True
        assert obj.getPackageRef().getValue() == "/Pkg"
        assert obj.getShortLabel().getValue() == "L1"

    def test_get_set_short_label(self):
        """
        Test get/set methods for short label.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getShortLabel() is None

        # Test setting short label
        label = Identifier().setValue("TestLabel")
        result = obj.setShortLabel(label)
        assert result is obj  # Verify method chaining
        assert obj.getShortLabel() == label


class TestARPackage:
    """
    Test class for ARPackage functionality.
    """

    def test_initialization(self):
        """
        Test ARPackage initialization.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        obj = ARPackage(ar_root, "TestPackage")

        # Verify basic properties
        assert obj is not None
        assert obj.getShortName() == "TestPackage"
        assert obj.getParent() == ar_root

        # Verify default values for attributes
        assert obj.getARPackages() == []
        assert obj.getReferenceBases() == []

    def test_get_ar_packages(self):
        """
        Test getARPackages method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Initially should be empty
        assert package.getARPackages() == []

        # Add a sub-package
        sub_package = package.createARPackage("SubPackage")

        # Should return the sub-package
        result = package.getARPackages()
        assert len(result) == 1
        assert result[0] == sub_package
        assert result[0].getShortName() == "SubPackage"

    def test_create_ar_package(self):
        """
        Test createARPackage method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create a sub-package
        sub_package = package.createARPackage("SubPackage1")
        assert sub_package is not None
        assert sub_package.getShortName() == "SubPackage1"
        assert sub_package.getParent() == package

        # Create another sub-package with same name should return same instance
        same_sub_package = package.createARPackage("SubPackage1")
        assert same_sub_package is sub_package

        # Create a different sub-package
        sub_package2 = package.createARPackage("SubPackage2")
        assert sub_package2 is not same_sub_package
        assert sub_package2.getShortName() == "SubPackage2"

    def test_get_element(self):
        """
        Test getElement method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Initially should return None for non-existent elements
        assert package.getReferrableElement("NonExistent") is None

        # Add a sub-package
        sub_package = package.createARPackage("SubPackage")

        # Should be able to get the sub-package
        result = package.getReferrableElement("SubPackage")
        assert result == sub_package

        # Should return None for non-existent type
        result = package.getReferrableElement("SubPackage", type=str)  # Wrong type
        assert result is None

    def test_create_application_sw_component_type(self):
        """
        Test createApplicationSwComponentType method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create an ApplicationSwComponentType
        swc = package.createApplicationSwComponentType("TestAppSwc")
        assert swc is not None
        assert swc.getShortName() == "TestAppSwc"
        assert swc.getParent() == package

        # Create the same name should return same instance
        same_swc = package.createApplicationSwComponentType("TestAppSwc")
        assert same_swc is swc

    def test_create_sender_receiver_interface(self):
        """
        Test createSenderReceiverInterface method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create a SenderReceiverInterface
        sri = package.createSenderReceiverInterface("TestSRI")
        assert sri is not None
        assert sri.getShortName() == "TestSRI"
        assert sri.getParent() == package

        # Create the same name should return same instance
        same_sri = package.createSenderReceiverInterface("TestSRI")
        assert same_sri is sri

    def test_create_nv_data_interface(self):
        """
        Test createNvDataInterface method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        nv_interface = package.createNvDataInterface("TestNVDI")
        assert nv_interface is not None
        assert nv_interface.getShortName() == "TestNVDI"
        assert nv_interface.getParent() == package

        same_nv_interface = package.createNvDataInterface("TestNVDI")
        assert same_nv_interface is nv_interface

    def test_create_implementation_data_type(self):
        """
        Test createImplementationDataType method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create an ImplementationDataType
        idt = package.createImplementationDataType("TestIDT")
        assert idt is not None
        assert idt.getShortName() == "TestIDT"
        assert idt.getParent() == package

        # Create the same name should return same instance
        same_idt = package.createImplementationDataType("TestIDT")
        assert same_idt is idt

    def test_create_bsw_module_description(self):
        """
        Test createBswModuleDescription method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create a BswModuleDescription
        desc = package.createBswModuleDescription("TestBswDesc")
        assert desc is not None
        assert desc.getShortName() == "TestBswDesc"
        assert desc.getParent() == package

        # Create the same name should return same instance
        same_desc = package.createBswModuleDescription("TestBswDesc")
        assert same_desc is desc

    def test_create_mc_function(self):
        """
        Test createMcFunction and getMcFunctions methods.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create an McFunction
        func = package.createMcFunction("TestFn")
        assert func is not None
        assert func.getShortName() == "TestFn"
        assert func.getParent() == package
        assert package.getMcFunctions() == [func]

        # Create the same name should return same instance
        same_func = package.createMcFunction("TestFn")
        assert same_func is func
        assert len(package.getMcFunctions()) == 1

    def test_create_mc_group(self):
        """
        Test createMcGroup and getMcGroups methods.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create an McGroup
        group = package.createMcGroup("TestGrp")
        assert group is not None
        assert group.getShortName() == "TestGrp"
        assert group.getParent() == package
        assert package.getMcGroups() == [group]

        # Create the same name should return same instance
        same_group = package.createMcGroup("TestGrp")
        assert same_group is group
        assert len(package.getMcGroups()) == 1

    def test_get_reference_bases(self):
        """
        Test getReferenceBases method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Initially should be empty
        assert package.getReferenceBases() == []

        # Add a reference base
        ref_base = ReferenceBase()
        package.referenceBases.append(ref_base)

        # Should return the reference base
        result = package.getReferenceBases()
        assert result == [ref_base]

    def test_get_ar_packages_sorted(self):
        """
        Test getARPackages returns sub-packages sorted by short name
        (ARPackage.arPackage aggregation, Table 4.1).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Create sub-packages out of alphabetical order
        package.createARPackage("Zeta")
        package.createARPackage("Alpha")
        package.createARPackage("Mid")

        result = package.getARPackages()
        assert [p.getShortName() for p in result] == ["Alpha", "Mid", "Zeta"]

    def test_add_reference_base_none_no_op(self):
        """
        Test addReferenceBase ignores a None value (None no-op convention,
        ARPackage.referenceBase aggregation, Table 4.1).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        result = package.addReferenceBase(None)
        assert result is package  # method chaining still holds
        assert package.getReferenceBases() == []

    def test_add_reference_base(self):
        """
        Test addReferenceBase method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Initially should be empty
        assert package.getReferenceBases() == []

        # Add a reference base
        ref_base = ReferenceBase()
        result = package.addReferenceBase(ref_base)
        assert result is package  # Verify method chaining
        assert package.getReferenceBases() == [ref_base]

    def test_create_multiple_types(self):
        """
        Test creating multiple different types of elements in ARPackage.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Test creating various element types
        comp_swc = package.createComplexDeviceDriverSwComponentType("CompDeviceDriverSwc")
        assert comp_swc.getShortName() == "CompDeviceDriverSwc"

        service_swc = package.createServiceSwComponentType("ServiceSwc")
        assert service_swc.getShortName() == "ServiceSwc"

        sensor_swc = package.createSensorActuatorSwComponentType("SensorActuatorSwc")
        assert sensor_swc.getShortName() == "SensorActuatorSwc"

        comp_swc_type = package.createCompositionSwComponentType("CompSwcType")
        assert comp_swc_type.getShortName() == "CompSwcType"

        param_interface = package.createParameterInterface("ParamInterface")
        assert param_interface.getShortName() == "ParamInterface"

        eth_frame = package.createGenericEthernetFrame("EthFrame")
        assert eth_frame.getShortName() == "EthFrame"

        lifecycle_info_set = package.createLifeCycleInfoSet("LifecycleInfoSet")
        assert lifecycle_info_set.getShortName() == "LifecycleInfoSet"

        cs_interface = package.createClientServerInterface("CSInterface")
        assert cs_interface.getShortName() == "CSInterface"

        app_prim_type = package.createApplicationPrimitiveDataType("AppPrimType")
        assert app_prim_type.getShortName() == "AppPrimType"

        # Note: There's likely a bug in the original source code here - it creates ApplicationRecordDataType
        # but tries to retrieve as ApplicationPrimitiveDataType
        # Let's also test a few more
        app_rec_type = package.createApplicationRecordDataType("AppRecType")
        assert app_rec_type.getShortName() == "AppRecType"

        sw_base_type = package.createSwBaseType("SwBaseType")
        assert sw_base_type.getShortName() == "SwBaseType"

        mapping_set = package.createDataTypeMappingSet("MappingSet")
        assert mapping_set.getShortName() == "MappingSet"

        compu_method = package.createCompuMethod("CompuMethod")
        assert compu_method.getShortName() == "CompuMethod"

        bsw_entry = package.createBswModuleEntry("BswEntry")
        assert bsw_entry.getShortName() == "BswEntry"

        bsw_impl = package.createBswImplementation("BswImpl")
        assert bsw_impl.getShortName() == "BswImpl"

        swc_impl = package.createSwcImplementation("SwcImpl")
        assert swc_impl.getShortName() == "SwcImpl"

        swc_bsw_mapping = package.createSwcBswMapping("SwcBswMapping")
        assert swc_bsw_mapping.getShortName() == "SwcBswMapping"

        constant_spec = package.createConstantSpecification("ConstantSpec")
        assert constant_spec.getShortName() == "ConstantSpec"

        data_constr = package.createDataConstr("DataConstr")
        assert data_constr.getShortName() == "DataConstr"

        unit = package.createUnit("Unit")
        assert unit.getShortName() == "Unit"

        e2e_set = package.createEndToEndProtectionSet("E2ESet")
        assert e2e_set.getShortName() == "E2ESet"

        app_array_type = package.createApplicationArrayDataType("AppArrayType")
        assert app_array_type.getShortName() == "AppArrayType"

        record_layout = package.createSwRecordLayout("RecordLayout")
        assert record_layout.getShortName() == "RecordLayout"

        addr_method = package.createSwAddrMethod("AddrMethod")
        assert addr_method.getShortName() == "AddrMethod"

        trigger_interface = package.createTriggerInterface("TriggerInterface")
        assert trigger_interface.getShortName() == "TriggerInterface"

        mode_group = package.createModeDeclarationGroup("ModeGroup")
        assert mode_group.getShortName() == "ModeGroup"

        mode_interface = package.createModeSwitchInterface("ModeInterface")
        assert mode_interface.getShortName() == "ModeInterface"

        swc_timing = package.createSwcTiming("SwcTiming")
        assert swc_timing.getShortName() == "SwcTiming"

        lin_cluster = package.createLinCluster("LinCluster")
        assert lin_cluster.getShortName() == "LinCluster"

        can_cluster = package.createCanCluster("CanCluster")
        assert can_cluster.getShortName() == "CanCluster"

        lin_frame = package.createLinUnconditionalFrame("LinFrame")
        assert lin_frame.getShortName() == "LinFrame"

        nm_pdu = package.createNmPdu("NmPdu")
        assert nm_pdu.getShortName() == "NmPdu"

        n_pdu = package.createNPdu("NPdu")
        assert n_pdu.getShortName() == "NPdu"

        dcm_pdu = package.createDcmIPdu("DcmPdu")
        assert dcm_pdu.getShortName() == "DcmPdu"

        secured_pdu = package.createSecuredIPdu("SecuredPdu")
        assert secured_pdu.getShortName() == "SecuredPdu"

        nm_config = package.createNmConfig("NmConfig")
        assert nm_config.getShortName() == "NmConfig"

    def test_create_remaining_types(self):
        """
        Test creating more types to cover additional methods.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Test additional create methods
        can_tp_config = package.createCanTpConfig("CanTpConfig")
        assert can_tp_config.getShortName() == "CanTpConfig"

        lin_tp_config = package.createLinTpConfig("LinTpConfig")
        assert lin_tp_config.getShortName() == "LinTpConfig"

        can_frame = package.createCanFrame("CanFrame")
        assert can_frame.getShortName() == "CanFrame"

        ecu_instance = package.createEcuInstance("EcuInstance")
        assert ecu_instance.getShortName() == "EcuInstance"

        gateway = package.createGateway("Gateway")
        assert gateway.getShortName() == "Gateway"

        i_signal = package.createISignal("ISignal")
        assert i_signal.getShortName() == "ISignal"

        system_signal = package.createSystemSignal("SystemSignal")
        assert system_signal.getShortName() == "SystemSignal"

        system_signal_group = package.createSystemSignalGroup("SystemSignalGroup")
        assert system_signal_group.getShortName() == "SystemSignalGroup"

        i_signal_ipdu = package.createISignalIPdu("ISignalIPdu")
        assert i_signal_ipdu.getShortName() == "ISignalIPdu"

        ecuc_val_collection = package.createEcucValueCollection("EcucValueCollection")
        assert ecuc_val_collection.getShortName() == "EcucValueCollection"

        ecuc_module_config = package.createEcucModuleConfigurationValues("EcucModuleConfigValues")
        assert ecuc_module_config.getShortName() == "EcucModuleConfigValues"

        ecuc_module_def = package.createEcucModuleDef("EcucModuleDef")
        assert ecuc_module_def.getShortName() == "EcucModuleDef"

        value_set = package.createSwSystemconstantValueSet("MyValueSet")
        assert value_set.getShortName() == "MyValueSet"

        predefined_variant = package.createPredefinedVariant("MyPredefinedVariant")
        assert predefined_variant.getShortName() == "MyPredefinedVariant"

        phys_dimension = package.createPhysicalDimension("PhysicalDimension")
        assert phys_dimension.getShortName() == "PhysicalDimension"

        i_signal_group = package.createISignalGroup("ISignalGroup")
        assert i_signal_group.getShortName() == "ISignalGroup"

        i_signal_ipdu_group = package.createISignalIPduGroup("ISignalIPduGroup")
        assert i_signal_ipdu_group.getShortName() == "ISignalIPduGroup"

        system = package.createSystem("System")
        assert system.getShortName() == "System"

        flat_map = package.createFlatMap("FlatMap")
        assert flat_map.getShortName() == "FlatMap"

        port_interface_mapping_set = package.createPortInterfaceMappingSet("PortInterfaceMappingSet")
        assert port_interface_mapping_set.getShortName() == "PortInterfaceMappingSet"

        eth_cluster = package.createEthernetCluster("EthernetCluster")
        assert eth_cluster.getShortName() == "EthernetCluster"

        diag_connection = package.createDiagnosticConnection("DiagnosticConnection")
        assert diag_connection.getShortName() == "DiagnosticConnection"

        diag_service_table = package.createDiagnosticServiceTable("DiagnosticServiceTable")
        assert diag_service_table.getShortName() == "DiagnosticServiceTable"

    def test_create_more_types(self):
        """
        Test creating even more types to cover additional methods.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Continue with more create methods
        multiplexed_ipdu = package.createMultiplexedIPdu("MultiplexedIPdu")
        assert multiplexed_ipdu.getShortName() == "MultiplexedIPdu"

        user_defined_ipdu = package.createUserDefinedIPdu("UserDefinedIPdu")
        assert user_defined_ipdu.getShortName() == "UserDefinedIPdu"

        user_defined_pdu = package.createUserDefinedPdu("UserDefinedPdu")
        assert user_defined_pdu.getShortName() == "UserDefinedPdu"

        general_purpose_ipdu = package.createGeneralPurposeIPdu("GeneralPurposeIPdu")
        assert general_purpose_ipdu.getShortName() == "GeneralPurposeIPdu"

        general_purpose_pdu = package.createGeneralPurposePdu("GeneralPurposePdu")
        assert general_purpose_pdu.getShortName() == "GeneralPurposePdu"

        secure_comm_set = package.createSecureCommunicationPropsSet("SecureCommPropsSet")
        assert secure_comm_set.getShortName() == "SecureCommPropsSet"

        soad_group = package.createSoAdRoutingGroup("SoAdRoutingGroup")
        assert soad_group.getShortName() == "SoAdRoutingGroup"

        do_ip_tp_config = package.createDoIpTpConfig("DoIpTpConfig")
        assert do_ip_tp_config.getShortName() == "DoIpTpConfig"

        hw_element = package.createHwElement("HwElement")
        assert hw_element.getShortName() == "HwElement"

        hw_category = package.createHwCategory("HwCategory")
        assert hw_category.getShortName() == "HwCategory"

        hw_type = package.createHwType("HwType")
        assert hw_type.getShortName() == "HwType"

        flexray_frame = package.createFlexrayFrame("FlexrayFrame")
        assert flexray_frame.getShortName() == "FlexrayFrame"

        flexray_cluster = package.createFlexrayCluster("FlexrayCluster")
        assert flexray_cluster.getShortName() == "FlexrayCluster"

        data_transform_set = package.createDataTransformationSet("DataTransformationSet")
        assert data_transform_set.getShortName() == "DataTransformationSet"

        collection = package.createCollection("Collection")
        assert collection.getShortName() == "Collection"

        keyword_set = package.createKeywordSet("KeywordSet")
        assert keyword_set.getShortName() == "KeywordSet"

        port_proto_blueprint = package.createPortPrototypeBlueprint("PortPrototypeBlueprint")
        assert port_proto_blueprint.getShortName() == "PortPrototypeBlueprint"

        mode_decl_mapping_set = package.createModeDeclarationMappingSet("ModeDeclMappingSet")
        assert mode_decl_mapping_set.getShortName() == "ModeDeclMappingSet"

    def test_create_ecu_abstraction_type(self):
        """
        Test creating EcuAbstractionSwComponentType specifically.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Test createEcuAbstractionSwComponentType
        ecu_abs_swc = package.createEcuAbstractionSwComponentType("EcuAbstractionSwc")
        assert ecu_abs_swc.getShortName() == "EcuAbstractionSwc"

    def test_getter_methods(self):
        """
        Test various getter methods to ensure they're called and covered.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        package = ARPackage(ar_root, "TestPackage")

        # Test all the getter methods exist and return appropriate types (even if empty)
        assert isinstance(package.getApplicationPrimitiveDataTypes(), list)
        assert isinstance(package.getApplicationDataType(), list)
        assert isinstance(package.getImplementationDataTypes(), list)
        assert isinstance(package.getSwBaseTypes(), list)
        assert isinstance(package.getSwComponentTypes(), list)
        assert isinstance(package.getSensorActuatorSwComponentType(), list)
        assert isinstance(package.getAtomicSwComponentTypes(), list)
        assert isinstance(package.getCompositionSwComponentTypes(), list)
        assert isinstance(package.getComplexDeviceDriverSwComponentTypes(), list)
        assert isinstance(package.getSenderReceiverInterfaces(), list)
        assert isinstance(package.getParameterInterfaces(), list)
        assert isinstance(package.getClientServerInterfaces(), list)
        assert isinstance(package.getDataTypeMappingSets(), list)
        assert isinstance(package.getCompuMethods(), list)
        assert isinstance(package.getBswModuleDescriptions(), list)
        assert isinstance(package.getBswModuleEntries(), list)
        assert isinstance(package.getBswImplementations(), list)
        assert isinstance(package.getSwcImplementations(), list)
        assert isinstance(package.getImplementations(), list)
        assert isinstance(package.getSwcBswMappings(), list)
        assert isinstance(package.getConstantSpecifications(), list)
        assert isinstance(package.getDataConstrs(), list)
        assert isinstance(package.getUnits(), list)
        assert isinstance(package.getApplicationArrayDataTypes(), list)
        assert isinstance(package.getSwRecordLayouts(), list)
        assert isinstance(package.getSwAddrMethods(), list)
        assert isinstance(package.getTriggerInterfaces(), list)
        assert isinstance(package.getModeDeclarationGroups(), list)
        assert isinstance(package.getModeSwitchInterfaces(), list)
        assert isinstance(package.getSwcTimings(), list)
        assert isinstance(package.getLinClusters(), list)
        assert isinstance(package.getCanClusters(), list)
        assert isinstance(package.getLinUnconditionalFrames(), list)
        assert isinstance(package.getNmPdus(), list)
        assert isinstance(package.getNPdus(), list)
        assert isinstance(package.getDcmIPdus(), list)
        assert isinstance(package.getSecuredIPdus(), list)
        assert isinstance(package.getNmConfigs(), list)
        assert isinstance(package.getCanTpConfigs(), list)
        assert isinstance(package.getCanFrames(), list)
        assert isinstance(package.getEcuInstances(), list)
        assert isinstance(package.getGateways(), list)
        assert isinstance(package.getISignals(), list)
        assert isinstance(package.getEcucValueCollections(), list)
        assert isinstance(package.getEcucModuleConfigurationValues(), list)
        assert isinstance(package.getEcucModuleDefs(), list)
        assert isinstance(package.getSwSystemconstantValueSets(), list)
        assert isinstance(package.getPredefinedVariants(), list)
        assert isinstance(package.getEcucPhysicalDimensions(), list)
        assert isinstance(package.getISignalGroups(), list)
        assert isinstance(package.getSystemSignals(), list)
        assert isinstance(package.getSystemSignalGroups(), list)
        assert isinstance(package.getISignalIPdus(), list)
        assert isinstance(package.getSystems(), list)
        assert isinstance(package.getHwElements(), list)
        assert isinstance(package.getHwCategories(), list)
        assert isinstance(package.getFlexrayFrames(), list)
        assert isinstance(package.getDataTransformationSets(), list)
        assert isinstance(package.getCollections(), list)
        assert isinstance(package.getKeywordSets(), list)
        assert isinstance(package.getPortPrototypeBlueprints(), list)
        assert isinstance(package.getModeDeclarationMappingSets(), list)
        assert isinstance(package.getReferenceBases(), list)

        # Add some elements and test that getters return them
        package.createApplicationPrimitiveDataType("AppPrimDT")
        package.createImplementationDataType("ImplDT")
        package.createApplicationSwComponentType("AppSwc")
        package.createSenderReceiverInterface("SRI")

        # Now test getters return the added elements
        app_prim_dts = package.getApplicationPrimitiveDataTypes()
        assert len(app_prim_dts) >= 1  # May include other types too due to inheritance
        assert any(dt.getShortName() == "AppPrimDT" for dt in app_prim_dts)

        impl_dts = package.getImplementationDataTypes()
        assert len(impl_dts) >= 1  # May include other types too
        assert any(dt.getShortName() == "ImplDT" for dt in impl_dts)

        swc_types = package.getAtomicSwComponentTypes()  # Use AtomicSwComponentType instead of ApplicationSwComponentType
        assert len(swc_types) >= 1  # May include other AtomicSwComponentType subclasses

        sri_types = package.getSenderReceiverInterfaces()
        assert len(sri_types) == 1
        assert sri_types[0].getShortName() == "SRI"


class TestPackageableElement:
    """
    Test class for PackageableElement functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that PackageableElement cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = PackageableElement(ar_root, "TestPackageableElement")
            assert False, "PackageableElement should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_inherits_from_collectable_element(self):
        """
        Table 4.2 Base closure names CollectableElement as the most-derived direct base.
        With CollectableElement re-parented to Identifiable (commit 3b31b7c4), the full
        MRO is PackageableElement -> CollectableElement -> Identifiable -> ... -> ARObject.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        assert issubclass(PackageableElement, CollectableElement)
        assert issubclass(PackageableElement, Identifiable)
        assert issubclass(PackageableElement, ARObject)
        mro = PackageableElement.__mro__
        assert mro[0] is PackageableElement
        assert mro[1] is CollectableElement
        assert mro[2] is Identifiable

    def test_concrete_subclass_initialization(self):
        """
        A concrete PackageableElement subclass initializes the base chain via (parent, short_name)
        and reaches Identifiable members through the CollectableElement -> Identifiable chain.
        """

        class ConcretePackageableElement(PackageableElement):
            pass

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcretePackageableElement(ar_root, "TestElement")

        assert obj.getShortName() == "TestElement"
        assert obj.parent is ar_root


class TestARElement:
    """
    Test class for ARElement functionality.

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.3, p.55
    ARElement is an abstract class without own attributes; all members are
    inherited from the base chain (PackageableElement -> Identifiable -> ...).
    """

    def test_abstract_initialization(self):
        """
        Test that ARElement cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = ARElement(ar_root, "TestARElement")
            assert False, "ARElement should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_concrete_subclass_initialization(self):
        """
        Test that a concrete ARElement subclass initializes the base chain.
        """

        class ConcreteARElement(ARElement):
            pass

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcreteARElement(ar_root, "TestElement")

        assert obj.getShortName() == "TestElement"
        assert obj.parent is ar_root

    def test_inheritance_chain(self):
        """
        Test that ARElement derives from PackageableElement (most-derived base)
        and the transitive base chain of Table 4.3.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        assert issubclass(ARElement, PackageableElement)
        assert issubclass(ARElement, Identifiable)
        assert issubclass(ARElement, ARObject)


class TestAclPermission:
    """
    Test class for AclPermission functionality.

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.1, p.382
    """

    def _create_acl_permission(self) -> AclPermission:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return AclPermission(ar_root, "TestAclPermission")

    def test_initialization(self):
        """
        Test that AclPermission is initialized with the spec defaults.
        """
        obj = self._create_acl_permission()

        assert obj.getShortName() == "TestAclPermission"
        assert isinstance(obj, ARElement)
        assert obj.getAclContexts() == []
        assert obj.getAclObjectRefs() == []
        assert obj.getAclOperationRefs() == []
        assert obj.getAclRoleRefs() == []
        assert obj.getAclScope() is None

    def test_add_get_acl_contexts(self):
        """
        Test getAclContexts and addAclContext round-trip and None no-op.
        """
        obj = self._create_acl_permission()

        context = NameToken()
        context.setValue("Generate")
        result = obj.addAclContext(context)
        assert result is obj  # method chaining
        assert obj.getAclContexts() == [context]

        obj.addAclContext(None)
        assert obj.getAclContexts() == [context]  # None is a no-op

    def test_add_get_acl_object_refs(self):
        """
        Test getAclObjectRefs and addAclObjectRef round-trip and None no-op.
        """
        obj = self._create_acl_permission()

        ref = RefType()
        ref.setValue("/AUTOSAR/AccessObjectSets/MemoryStackConfiguration")
        result = obj.addAclObjectRef(ref)
        assert result is obj  # method chaining
        assert obj.getAclObjectRefs() == [ref]

        obj.addAclObjectRef(None)
        assert obj.getAclObjectRefs() == [ref]  # None is a no-op

    def test_add_get_acl_operation_refs(self):
        """
        Test getAclOperationRefs and addAclOperationRef round-trip and None no-op.
        """
        obj = self._create_acl_permission()

        ref = RefType()
        ref.setValue("/AUTOSAR/AclOperations/AssignValue")
        result = obj.addAclOperationRef(ref)
        assert result is obj  # method chaining
        assert obj.getAclOperationRefs() == [ref]

        obj.addAclOperationRef(None)
        assert obj.getAclOperationRefs() == [ref]  # None is a no-op

    def test_add_get_acl_role_refs(self):
        """
        Test getAclRoleRefs and addAclRoleRef round-trip and None no-op.
        """
        obj = self._create_acl_permission()

        ref = RefType()
        ref.setValue("/AUTOSAR/AclRoles/ECU_Integrator")
        result = obj.addAclRoleRef(ref)
        assert result is obj  # method chaining
        assert obj.getAclRoleRefs() == [ref]

        obj.addAclRoleRef(None)
        assert obj.getAclRoleRefs() == [ref]  # None is a no-op

    def test_get_set_acl_scope(self):
        """
        Test getAclScope and setAclScope round-trip and None no-op.
        """
        obj = self._create_acl_permission()

        scope = AclScopeEnum()
        scope.setValue(AclScopeEnum.DESCENDANT)
        result = obj.setAclScope(scope)
        assert result is obj  # method chaining
        assert obj.getAclScope() is scope

        result = obj.setAclScope(None)
        assert result is obj  # method chaining with None
        assert obj.getAclScope() is scope  # None is a no-op


class TestAclObjectSet:
    """
    Test class for AclObjectSet functionality.

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.2, p.383
    """

    def _create_acl_object_set(self) -> AclObjectSet:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return AclObjectSet(ar_root, "TestAclObjectSet")

    def test_initialization(self):
        """
        Test that AclObjectSet is initialized with the spec defaults.
        """
        obj = self._create_acl_object_set()

        assert obj.getShortName() == "TestAclObjectSet"
        assert isinstance(obj, ARElement)
        assert obj.getAclObjectClasses() == []
        assert obj.getAclScope() is None
        assert obj.getCollectionRef() is None
        assert obj.getDerivedFromBlueprintRefs() == []
        assert obj.getEngineeringObjects() == []
        assert obj.getObjectRefs() == []
        assert obj.getObjectDefinitionRefs() == []

    def test_add_get_acl_object_classes(self):
        """
        Test getAclObjectClasses and addAclObjectClass round-trip and None no-op.
        """
        obj = self._create_acl_object_set()

        object_class = ReferrableSubtypesEnum()
        object_class.setValue("ECUC-MODULE-DEF")
        result = obj.addAclObjectClass(object_class)
        assert result is obj  # method chaining
        assert obj.getAclObjectClasses() == [object_class]

        obj.addAclObjectClass(None)
        assert obj.getAclObjectClasses() == [object_class]  # None is a no-op

    def test_get_set_acl_scope(self):
        """
        Test getAclScope and setAclScope round-trip and None no-op.
        """
        obj = self._create_acl_object_set()

        scope = AclScopeEnum()
        scope.setValue(AclScopeEnum.DESCENDANT)
        result = obj.setAclScope(scope)
        assert result is obj  # method chaining
        assert obj.getAclScope() is scope

        result = obj.setAclScope(None)
        assert result is obj  # method chaining with None
        assert obj.getAclScope() is scope  # None is a no-op

    def test_get_set_collection_ref(self):
        """
        Test getCollectionRef and setCollectionRef round-trip and None no-op.
        """
        obj = self._create_acl_object_set()

        assert obj.getCollectionRef() is None

        ref = RefType()
        ref.setValue("/AUTOSAR/Collections/ControlledObjects")
        result = obj.setCollectionRef(ref)
        assert result is obj  # method chaining
        assert obj.getCollectionRef() is ref

        result = obj.setCollectionRef(None)
        assert result is obj  # method chaining with None
        assert obj.getCollectionRef() is ref  # None is a no-op

    def test_add_get_derived_from_blueprint_refs(self):
        """
        Test getDerivedFromBlueprintRefs and addDerivedFromBlueprintRef round-trip and None no-op.
        """
        obj = self._create_acl_object_set()

        ref = RefType()
        ref.setValue("/AUTOSAR/Blueprints/SomeBlueprint")
        result = obj.addDerivedFromBlueprintRef(ref)
        assert result is obj  # method chaining
        assert obj.getDerivedFromBlueprintRefs() == [ref]

        obj.addDerivedFromBlueprintRef(None)
        assert obj.getDerivedFromBlueprintRefs() == [ref]  # None is a no-op

    def test_add_get_engineering_objects(self):
        """
        Test getEngineeringObjects and addEngineeringObject round-trip and None no-op.
        """
        obj = self._create_acl_object_set()

        engineering_object = AutosarEngineeringObject()
        result = obj.addEngineeringObject(engineering_object)
        assert result is obj  # method chaining
        assert obj.getEngineeringObjects() == [engineering_object]

        obj.addEngineeringObject(None)
        assert obj.getEngineeringObjects() == [engineering_object]  # None is a no-op

    def test_add_get_object_refs(self):
        """
        Test getObjectRefs and addObjectRef round-trip and None no-op.
        """
        obj = self._create_acl_object_set()

        ref = RefType()
        ref.setValue("/AUTOSAR/Package/SomeObject")
        result = obj.addObjectRef(ref)
        assert result is obj  # method chaining
        assert obj.getObjectRefs() == [ref]

        obj.addObjectRef(None)
        assert obj.getObjectRefs() == [ref]  # None is a no-op

    def test_add_get_object_definition_refs(self):
        """
        Test getObjectDefinitionRefs and addObjectDefinitionRef round-trip and None no-op.
        """
        obj = self._create_acl_object_set()

        ref = RefType()
        ref.setValue("/AUTOSAR/EcucDefs/MemIf")
        result = obj.addObjectDefinitionRef(ref)
        assert result is obj  # method chaining
        assert obj.getObjectDefinitionRefs() == [ref]

        obj.addObjectDefinitionRef(None)
        assert obj.getObjectDefinitionRefs() == [ref]  # None is a no-op


class TestAclOperation:
    """
    Test class for AclOperation functionality.

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.4, p.384
    """

    def _create_acl_operation(self) -> AclOperation:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return AclOperation(ar_root, "TestAclOperation")

    def test_initialization(self):
        """
        Test that AclOperation is initialized with the spec defaults.
        """
        obj = self._create_acl_operation()

        assert obj.getShortName() == "TestAclOperation"
        assert isinstance(obj, ARElement)
        assert obj.getImpliedOperationRefs() == []

    def test_add_get_implied_operation_refs(self):
        """
        Test getImpliedOperationRefs and addImpliedOperationRef round-trip and None no-op.
        """
        obj = self._create_acl_operation()

        ref = RefType()
        ref.setValue("/AUTOSAR/AclOperations/AssignValue")
        result = obj.addImpliedOperationRef(ref)
        assert result is obj  # method chaining
        assert obj.getImpliedOperationRefs() == [ref]

        obj.addImpliedOperationRef(None)
        assert obj.getImpliedOperationRefs() == [ref]  # None is a no-op


class TestAclRole:
    """
    Test class for AclRole functionality.

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.5, p.384
    """

    def _create_acl_role(self) -> AclRole:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return AclRole(ar_root, "TestAclRole")

    def test_initialization(self):
        """
        Test that AclRole is initialized with the spec defaults.
        """
        obj = self._create_acl_role()

        assert obj.getShortName() == "TestAclRole"
        assert isinstance(obj, ARElement)
        assert obj.getLdapUrl() is None

    def test_get_set_ldap_url(self):
        """
        Test getLdapUrl and setLdapUrl round-trip and None no-op.
        """
        obj = self._create_acl_role()

        url = UriString()
        url.setValue("ldap://ldap.example.com/dc=example,dc=com")
        result = obj.setLdapUrl(url)
        assert result is obj  # method chaining
        assert obj.getLdapUrl() is url

        result = obj.setLdapUrl(None)
        assert result is obj  # method chaining with None
        assert obj.getLdapUrl() is url  # None is a no-op


class TestLifeCycleStateDefinitionGroup:
    """
    Test class for LifeCycleStateDefinitionGroup functionality.

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 12.1, p.388
    """

    def _create_group(self) -> LifeCycleStateDefinitionGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return LifeCycleStateDefinitionGroup(ar_root, "TestLifeCycleStateDefinitionGroup")

    def test_initialization(self):
        """
        Test that LifeCycleStateDefinitionGroup is initialized with the spec defaults.
        """
        obj = self._create_group()

        assert obj.getShortName() == "TestLifeCycleStateDefinitionGroup"
        assert isinstance(obj, ARElement)
        assert obj.getLcStates() == []

    def test_create_lc_state(self):
        """
        Test createLcState creates a LifeCycleState child, registers it and
        returns the existing one on a duplicate short name.
        """
        obj = self._create_group()

        state = obj.createLcState("valid")
        assert isinstance(state, LifeCycleState)
        assert state.getShortName() == "valid"
        assert obj.getLcStates() == [state]

        duplicate = obj.createLcState("valid")
        assert duplicate is state  # duplicate returns the existing child
        assert obj.getLcStates() == [state]


class TestViewMapSet:
    """
    Test class for ViewMapSet functionality.

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 14.1, p.401
    """

    def _create_view_map_set(self) -> ViewMapSet:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return ViewMapSet(ar_root, "TestViewMapSet")

    def test_initialization(self):
        """
        Test that ViewMapSet is initialized with the spec defaults.
        """
        obj = self._create_view_map_set()

        assert obj.getShortName() == "TestViewMapSet"
        assert isinstance(obj, ARElement)
        assert obj.getViewMaps() == []

    def test_create_view_map(self):
        """
        Test createViewMap creates a ViewMap child, registers it and
        returns the existing one on a duplicate short name.
        """
        obj = self._create_view_map_set()

        view_map = obj.createViewMap("TestViewMap")
        assert isinstance(view_map, ViewMap)
        assert view_map.getShortName() == "TestViewMap"
        assert obj.getViewMaps() == [view_map]

        duplicate = obj.createViewMap("TestViewMap")
        assert duplicate is view_map  # duplicate returns the existing child
        assert obj.getViewMaps() == [view_map]


class TestDiagnosticMapping:
    """
    Test class for DiagnosticMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.1, p.223
    (abstract base; exercised through the concrete subclass CpSwClusterToDiagEventMapping)
    """

    def _create_mapping(self) -> CpSwClusterToDiagEventMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return CpSwClusterToDiagEventMapping(ar_root, "TestDiagnosticMapping")

    def test_initialization(self):
        """
        Test that DiagnosticMapping is initialized with the spec defaults.
        """
        obj = self._create_mapping()

        assert obj.getShortName() == "TestDiagnosticMapping"
        assert isinstance(obj, DiagnosticMapping)
        assert isinstance(obj, ARElement)
        assert obj.getProviderSoftwareClusterRef() is None
        assert obj.getRequesterSoftwareClusterRef() is None

    def test_abstract_instantiation_raises(self):
        """
        Test that the abstract DiagnosticMapping cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticMapping(AUTOSAR.getInstance(), "DirectInstance")

    def test_get_set_provider_software_cluster_ref(self):
        """
        Test getProviderSoftwareClusterRef and setProviderSoftwareClusterRef round-trip and None no-op.
        """
        obj = self._create_mapping()

        ref = RefType()
        ref.setDest("CP-SOFTWARE-CLUSTER")
        ref.setValue("/AUTOSAR/SoftwareClusters/ProviderCluster")
        result = obj.setProviderSoftwareClusterRef(ref)
        assert result is obj  # method chaining
        assert obj.getProviderSoftwareClusterRef() is ref

        result = obj.setProviderSoftwareClusterRef(None)
        assert result is obj  # method chaining with None
        assert obj.getProviderSoftwareClusterRef() is ref  # None is a no-op

    def test_get_set_requester_software_cluster_ref(self):
        """
        Test getRequesterSoftwareClusterRef and setRequesterSoftwareClusterRef round-trip and None no-op.
        """
        obj = self._create_mapping()

        ref = RefType()
        ref.setDest("CP-SOFTWARE-CLUSTER")
        ref.setValue("/AUTOSAR/SoftwareClusters/RequesterCluster")
        result = obj.setRequesterSoftwareClusterRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequesterSoftwareClusterRef() is ref

        result = obj.setRequesterSoftwareClusterRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequesterSoftwareClusterRef() is ref  # None is a no-op


class TestDiagnosticAbstractDataIdentifier:
    """
    Test class for DiagnosticAbstractDataIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.4, p.34
    (abstract base; exercised through the concrete subclass DiagnosticDataIdentifier)
    """

    def _create_did(self) -> DiagnosticDataIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDataIdentifier(ar_root, "TestDid")

    def test_initialization(self):
        """
        Test that DiagnosticAbstractDataIdentifier is initialized with the spec defaults.
        """
        obj = self._create_did()

        assert obj.getShortName() == "TestDid"
        assert isinstance(obj, DiagnosticAbstractDataIdentifier)
        assert isinstance(obj, ARElement)
        assert obj.getId() is None

    def test_abstract_instantiation_raises(self):
        """
        Test that the abstract DiagnosticAbstractDataIdentifier cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticAbstractDataIdentifier(AUTOSAR.getInstance(), "DirectInstance")

    def test_get_set_id(self):
        """
        Test getId and setId round-trip and None no-op.
        """
        obj = self._create_did()

        id_value = PositiveInteger()
        id_value.setValue("4")
        result = obj.setId(id_value)
        assert result is obj  # method chaining
        assert obj.getId() is id_value
        assert obj.getId().getValue() == 4

        result = obj.setId(None)
        assert result is obj  # method chaining with None
        assert obj.getId() is id_value  # None is a no-op


class TestDiagnosticDataIdentifier:
    """
    Test class for DiagnosticDataIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.2, p.34
    """

    def _create_did(self) -> DiagnosticDataIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDataIdentifier(ar_root, "TestDid")

    def test_initialization(self):
        """
        Test that DiagnosticDataIdentifier is initialized with the spec defaults.
        """
        obj = self._create_did()

        assert obj.getShortName() == "TestDid"
        assert isinstance(obj, DiagnosticAbstractDataIdentifier)
        assert obj.getId() is None
        assert obj.getDataElements() == []
        assert obj.getDidSize() is None
        assert obj.getRepresentsVin() is None
        assert obj.getSupportInfoByte() is None

    def test_add_data_element(self):
        """
        Test addDataElement appends, returns self and ignores None.
        """
        obj = self._create_did()

        data_element = DiagnosticParameter()
        result = obj.addDataElement(data_element)
        assert result is obj  # method chaining
        assert obj.getDataElements() == [data_element]

        result = obj.addDataElement(None)
        assert result is obj  # method chaining with None
        assert obj.getDataElements() == [data_element]  # None is a no-op

    def test_get_set_did_size(self):
        """
        Test getDidSize and setDidSize round-trip and None no-op.
        """
        obj = self._create_did()

        did_size = PositiveInteger()
        did_size.setValue("8")
        result = obj.setDidSize(did_size)
        assert result is obj  # method chaining
        assert obj.getDidSize() is did_size
        assert obj.getDidSize().getValue() == 8

        result = obj.setDidSize(None)
        assert result is obj  # method chaining with None
        assert obj.getDidSize() is did_size  # None is a no-op

    def test_get_set_represents_vin(self):
        """
        Test getRepresentsVin and setRepresentsVin round-trip and None no-op.
        """
        obj = self._create_did()

        represents_vin = Boolean()
        represents_vin.setValue(True)
        result = obj.setRepresentsVin(represents_vin)
        assert result is obj  # method chaining
        assert obj.getRepresentsVin() is represents_vin

        result = obj.setRepresentsVin(None)
        assert result is obj  # method chaining with None
        assert obj.getRepresentsVin() is represents_vin  # None is a no-op

    def test_get_set_support_info_byte(self):
        """
        Test getSupportInfoByte and setSupportInfoByte round-trip and None no-op.
        """
        obj = self._create_did()

        support_info_byte = DiagnosticSupportInfoByte()
        result = obj.setSupportInfoByte(support_info_byte)
        assert result is obj  # method chaining
        assert obj.getSupportInfoByte() is support_info_byte

        result = obj.setSupportInfoByte(None)
        assert result is obj  # method chaining with None
        assert obj.getSupportInfoByte() is support_info_byte  # None is a no-op


class TestDiagnosticDynamicDataIdentifier:
    """
    Test class for DiagnosticDynamicDataIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.3, p.34
    (no own attributes; base members exercised through the inherited accessors)
    """

    def _create_did(self) -> DiagnosticDynamicDataIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDynamicDataIdentifier(ar_root, "TestDynamicDid")

    def test_initialization(self):
        """
        Test that DiagnosticDynamicDataIdentifier is initialized with the spec defaults.
        """
        obj = self._create_did()

        assert obj.getShortName() == "TestDynamicDid"
        assert isinstance(obj, DiagnosticAbstractDataIdentifier)
        assert obj.getId() is None

    def test_base_accessors(self):
        """
        Test that the inherited DiagnosticAbstractDataIdentifier accessors work.
        """
        obj = self._create_did()

        id_value = PositiveInteger()
        id_value.setValue("7")
        result = obj.setId(id_value)
        assert result is obj  # method chaining
        assert obj.getId() is id_value
        assert obj.getId().getValue() == 7

        obj.setId(None)
        assert obj.getId() is id_value  # None is a no-op


class TestImports:
    """
    Test that the six synced classes are exported from armodel.models.
    """

    def test_top_level_exports(self):
        """
        All six classes must be importable from armodel.models.
        """
        import armodel.models as models

        for name in ("AclPermission", "AclObjectSet", "AclOperation", "AclRole", "LifeCycleStateDefinitionGroup", "ViewMapSet"):
            assert hasattr(models, name), "%s missing from armodel.models" % name


class TestDiagnosticContributionSet:
    """
    Test class for DiagnosticContributionSet functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.14, p.57
    """

    def _create_set(self) -> DiagnosticContributionSet:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticContributionSet(ar_root, "TestContributionSet")

    def test_initialization(self):
        """
        Test that DiagnosticContributionSet is initialized with the spec defaults.
        """
        obj = self._create_set()

        assert obj.getShortName() == "TestContributionSet"
        assert isinstance(obj, ARElement)
        assert obj.getCommonProperties() is None
        assert obj.getElementRefs() == []
        assert obj.getServiceTableRefs() == []

    def test_get_set_common_properties(self):
        """
        Test getCommonProperties and setCommonProperties round-trip and None no-op.
        """
        obj = self._create_set()

        common_properties = DiagnosticCommonProps()
        result = obj.setCommonProperties(common_properties)
        assert result is obj  # method chaining
        assert obj.getCommonProperties() is common_properties

        result = obj.setCommonProperties(None)
        assert result is obj  # method chaining with None
        assert obj.getCommonProperties() is common_properties  # None is a no-op

    def test_add_element_ref(self):
        """
        Test addElementRef appends, returns self and ignores None.
        """
        obj = self._create_set()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-COMMON-ELEMENT")
        ref.setValue("/AUTOSAR/DiagnosticCommonElements/Did")
        result = obj.addElementRef(ref)
        assert result is obj  # method chaining
        assert obj.getElementRefs() == [ref]

        result = obj.addElementRef(None)
        assert result is obj  # method chaining with None
        assert obj.getElementRefs() == [ref]  # None is a no-op

    def test_add_service_table_ref(self):
        """
        Test addServiceTableRef appends, returns self and ignores None.
        """
        obj = self._create_set()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-SERVICE-TABLE")
        ref.setValue("/AUTOSAR/DiagnosticServiceTables/Table")
        result = obj.addServiceTableRef(ref)
        assert result is obj  # method chaining
        assert obj.getServiceTableRefs() == [ref]

        result = obj.addServiceTableRef(None)
        assert result is obj  # method chaining with None
        assert obj.getServiceTableRefs() == [ref]  # None is a no-op


class TestDiagnosticProtocol:
    """
    Test class for DiagnosticProtocol functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.15, p.58
    """

    def _create_protocol(self) -> DiagnosticProtocol:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticProtocol(ar_root, "TestProtocol")

    def test_initialization(self):
        """
        Test that DiagnosticProtocol is initialized with the spec defaults.
        """
        obj = self._create_protocol()

        assert obj.getShortName() == "TestProtocol"
        assert isinstance(obj, ARElement)
        assert obj.getDiagnosticConnectionRefs() == []
        assert obj.getPriority() is None
        assert obj.getProtocolKind() is None
        assert obj.getSendRespPendOnTransToBoot() is None
        assert obj.getServiceTableRef() is None

    def test_add_diagnostic_connection_ref(self):
        """
        Test addDiagnosticConnectionRef appends, returns self and ignores None.
        """
        obj = self._create_protocol()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-CONNECTION")
        ref.setValue("/AUTOSAR/DiagnosticConnections/Conn")
        result = obj.addDiagnosticConnectionRef(ref)
        assert result is obj  # method chaining
        assert obj.getDiagnosticConnectionRefs() == [ref]

        result = obj.addDiagnosticConnectionRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDiagnosticConnectionRefs() == [ref]  # None is a no-op

    def test_get_set_priority(self):
        """
        Test getPriority and setPriority round-trip and None no-op.
        """
        obj = self._create_protocol()

        priority = PositiveInteger()
        priority.setValue("5")
        result = obj.setPriority(priority)
        assert result is obj  # method chaining
        assert obj.getPriority() is priority
        assert obj.getPriority().getValue() == 5

        result = obj.setPriority(None)
        assert result is obj  # method chaining with None
        assert obj.getPriority() is priority  # None is a no-op

    def test_get_set_protocol_kind(self):
        """
        Test getProtocolKind and setProtocolKind round-trip and None no-op.
        """
        obj = self._create_protocol()

        protocol_kind = NameToken()
        protocol_kind.setValue("UDS")
        result = obj.setProtocolKind(protocol_kind)
        assert result is obj  # method chaining
        assert obj.getProtocolKind() is protocol_kind
        assert obj.getProtocolKind().getValue() == "UDS"

        result = obj.setProtocolKind(None)
        assert result is obj  # method chaining with None
        assert obj.getProtocolKind() is protocol_kind  # None is a no-op

    def test_get_set_send_resp_pend_on_trans_to_boot(self):
        """
        Test getSendRespPendOnTransToBoot and setSendRespPendOnTransToBoot round-trip and None no-op.
        """
        obj = self._create_protocol()

        send_resp_pend = Boolean()
        send_resp_pend.setValue(True)
        result = obj.setSendRespPendOnTransToBoot(send_resp_pend)
        assert result is obj  # method chaining
        assert obj.getSendRespPendOnTransToBoot() is send_resp_pend

        result = obj.setSendRespPendOnTransToBoot(None)
        assert result is obj  # method chaining with None
        assert obj.getSendRespPendOnTransToBoot() is send_resp_pend  # None is a no-op

    def test_get_set_service_table_ref(self):
        """
        Test getServiceTableRef and setServiceTableRef round-trip and None no-op.
        """
        obj = self._create_protocol()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-SERVICE-TABLE")
        ref.setValue("/AUTOSAR/DiagnosticServiceTables/Table")
        result = obj.setServiceTableRef(ref)
        assert result is obj  # method chaining
        assert obj.getServiceTableRef() is ref

        result = obj.setServiceTableRef(None)
        assert result is obj  # method chaining with None
        assert obj.getServiceTableRef() is ref  # None is a no-op


class TestDiagnosticCustomServiceInstance:
    """
    Test class for DiagnosticCustomServiceInstance functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.27, p.70
    """

    def _create_instance(self) -> DiagnosticCustomServiceInstance:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticCustomServiceInstance(ar_root, "TestCustomServiceInstance")

    def test_initialization(self):
        """
        Test that DiagnosticCustomServiceInstance is initialized with the spec defaults.
        """
        obj = self._create_instance()

        assert obj.getShortName() == "TestCustomServiceInstance"
        assert isinstance(obj, ARElement)
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getCustomServiceClassRef() is None
        assert obj.getAccessPermissionRef() is None
        assert obj.getServiceClassRef() is None

    def test_get_set_custom_service_class_ref(self):
        """
        Test getCustomServiceClassRef and setCustomServiceClassRef round-trip and None no-op.
        """
        obj = self._create_instance()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-CUSTOM-SERVICE-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass")
        result = obj.setCustomServiceClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getCustomServiceClassRef() is ref

        result = obj.setCustomServiceClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getCustomServiceClassRef() is ref  # None is a no-op

    def test_inherited_instance_accessors(self):
        """
        Test the accessPermissionRef and serviceClassRef accessors inherited from DiagnosticServiceInstance.
        """
        obj = self._create_instance()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-ACCESS-PERMISSION")
        ref.setValue("/AUTOSAR/Dcm/AccessPermission")
        result = obj.setAccessPermissionRef(ref)
        assert result is obj  # method chaining
        assert obj.getAccessPermissionRef() is ref

        class_ref = RefType()
        class_ref.setDest("DIAGNOSTIC-CUSTOM-SERVICE-CLASS")
        class_ref.setValue("/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass")
        result = obj.setServiceClassRef(class_ref)
        assert result is obj  # method chaining
        assert obj.getServiceClassRef() is class_ref

    def test_create_diagnostic_custom_service_instance(self):
        """
        Test createDiagnosticCustomServiceInstance creates, appends and returns the existing one for a duplicate short name.
        """
        package = AUTOSAR.getInstance().createARPackage("CustomInstances")

        instance = package.createDiagnosticCustomServiceInstance("Svc1")
        assert instance is not None
        assert isinstance(instance, DiagnosticCustomServiceInstance)
        assert instance.getShortName() == "Svc1"
        assert instance.getParent() is package
        assert package.getReferrableElement("Svc1", DiagnosticCustomServiceInstance) is instance

        duplicate = package.createDiagnosticCustomServiceInstance("Svc1")
        assert duplicate is instance  # duplicate short name returns the existing element


class TestDiagnosticAuthRole:
    """
    Test class for DiagnosticAuthRole functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.34, p.77
    """

    AUTH_ROLE_NOTE = "This meta-class represents the ability to specify an authentication role that can be used to deliver fine-grained access rights."
    BIT_POSITION_NOTE = "This attribute allows for the specification of the position of the enclosing role in a bitfield of roles."
    IS_DEFAULT_NOTE = "This attribute indicates whether the enclosing role is considered a default role."

    def _create_auth_role(self) -> DiagnosticAuthRole:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticAuthRole(ar_root, "TestAuthRole")

    def test_initialization(self):
        """
        Test that DiagnosticAuthRole is initialized with the spec defaults.
        """
        obj = self._create_auth_role()

        assert obj.getShortName() == "TestAuthRole"
        assert isinstance(obj, ARElement)
        assert obj.getBitPosition() is None
        assert obj.getIsDefault() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (Tags tail dropped).
        """
        assert DiagnosticAuthRole.__doc__ == self.AUTH_ROLE_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAuthRole.__init__.__doc__ is None

    def test_get_set_bit_position(self):
        """
        Test getBitPosition and setBitPosition round-trip and None no-op.
        """
        obj = self._create_auth_role()

        bit_position = PositiveInteger()
        bit_position.setValue("7")
        result = obj.setBitPosition(bit_position)
        assert result is obj  # method chaining
        assert obj.getBitPosition() is bit_position
        assert obj.getBitPosition().getValue() == 7

        result = obj.setBitPosition(None)
        assert result is obj  # method chaining with None
        assert obj.getBitPosition() is bit_position  # None is a no-op

    def test_get_set_is_default(self):
        """
        Test getIsDefault and setIsDefault round-trip and None no-op.
        """
        obj = self._create_auth_role()

        is_default = Boolean()
        is_default.setValue(True)
        result = obj.setIsDefault(is_default)
        assert result is obj  # method chaining
        assert obj.getIsDefault() is is_default
        assert obj.getIsDefault().getValue() is True

        result = obj.setIsDefault(None)
        assert result is obj  # method chaining with None
        assert obj.getIsDefault() is is_default  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim.
        """
        assert inspect.cleandoc(DiagnosticAuthRole.getBitPosition.__doc__) == self.BIT_POSITION_NOTE
        assert inspect.cleandoc(DiagnosticAuthRole.setBitPosition.__doc__) == (self.BIT_POSITION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing bitPosition.")
        assert inspect.cleandoc(DiagnosticAuthRole.getIsDefault.__doc__) == self.IS_DEFAULT_NOTE
        assert inspect.cleandoc(DiagnosticAuthRole.setIsDefault.__doc__) == (self.IS_DEFAULT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing isDefault.")

    def test_create_diagnostic_auth_role(self):
        """
        Test createDiagnosticAuthRole creates, appends and returns the existing one for a duplicate short name.
        """
        package = AUTOSAR.getInstance().createARPackage("AuthRoles")

        auth_role = package.createDiagnosticAuthRole("Role1")
        assert auth_role is not None
        assert isinstance(auth_role, DiagnosticAuthRole)
        assert auth_role.getShortName() == "Role1"
        assert auth_role.getParent() is package
        assert package.getReferrableElement("Role1", DiagnosticAuthRole) is auth_role

        duplicate = package.createDiagnosticAuthRole("Role1")
        assert duplicate is auth_role  # duplicate short name returns the existing element


class TestDiagnosticSessionControl:
    """
    Test class for DiagnosticSessionControl functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.47, p.93
    """

    SESSION_CONTROL_NOTE = 'This represents an instance of the "Session Control" diagnostic service.'
    DIAGNOSTIC_SESSION_NOTE = "This represents the applicable DiagnosticSessions"
    SESSION_CONTROL_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticSessionControl in the given context."

    def _create_session_control(self) -> DiagnosticSessionControl:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticSessionControl(ar_root, "TestSessionControl")

    def test_initialization(self):
        """
        Test that DiagnosticSessionControl is initialized with the spec defaults.
        """
        obj = self._create_session_control()

        assert obj.getShortName() == "TestSessionControl"
        assert isinstance(obj, ARElement)
        assert obj.getDiagnosticSessionRef() is None
        assert obj.getSessionControlClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (Tags tail dropped).
        """
        assert DiagnosticSessionControl.__doc__ == self.SESSION_CONTROL_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticSessionControl.__init__.__doc__ is None

    def test_get_set_diagnostic_session_ref(self):
        """
        Test that get/set diagnosticSessionRef chain and treat None as a no-op.
        """
        obj = self._create_session_control()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-SESSION")
        ref.setValue("/AUTOSAR/DiagnosticSessions/DefaultSession")
        result = obj.setDiagnosticSessionRef(ref)
        assert result is obj  # method chaining
        assert obj.getDiagnosticSessionRef() is ref

        result = obj.setDiagnosticSessionRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDiagnosticSessionRef() is ref  # None is a no-op

    def test_get_set_session_control_class_ref(self):
        """
        Test that get/set sessionControlClassRef chain and treat None as a no-op.
        """
        obj = self._create_session_control()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-SESSION-CONTROL-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticSessionControls/SessionControlClass")
        result = obj.setSessionControlClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getSessionControlClassRef() is ref

        result = obj.setSessionControlClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getSessionControlClassRef() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim.
        """
        assert inspect.cleandoc(DiagnosticSessionControl.getDiagnosticSessionRef.__doc__) == self.DIAGNOSTIC_SESSION_NOTE
        assert inspect.cleandoc(DiagnosticSessionControl.setDiagnosticSessionRef.__doc__) == (
            self.DIAGNOSTIC_SESSION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing diagnosticSessionRef."
        )
        assert inspect.cleandoc(DiagnosticSessionControl.getSessionControlClassRef.__doc__) == self.SESSION_CONTROL_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticSessionControl.setSessionControlClassRef.__doc__) == (
            self.SESSION_CONTROL_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing sessionControlClassRef."
        )

    def test_create_diagnostic_session_control(self):
        """
        Test createDiagnosticSessionControl creates, appends and returns the existing one for a duplicate short name.
        """
        package = AUTOSAR.getInstance().createARPackage("SessionControls")

        session_control = package.createDiagnosticSessionControl("SessionCtrl1")
        assert session_control is not None
        assert isinstance(session_control, DiagnosticSessionControl)
        assert session_control.getShortName() == "SessionCtrl1"
        assert session_control.getParent() is package
        assert package.getReferrableElement("SessionCtrl1", DiagnosticSessionControl) is session_control

        duplicate = package.createDiagnosticSessionControl("SessionCtrl1")
        assert duplicate is session_control  # duplicate short name returns the existing element


class TestDiagnosticSecurityAccess:
    """
    Test class for DiagnosticSecurityAccess functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.49, p.96
    """

    CLASS_NOTE = 'This represents an instance of the "Security Access" diagnostic service.'
    REQUEST_SEED_ID_NOTE = "This would be 0x01, 0x03, 0x05, ... The sendKey id can be computed by adding 1 to the requestSeedId"
    SECURITY_ACCESS_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. "
        "Thereby, the reference represents the ability to access shared attributes among all DiagnosticSecurityAccess in the given context."
    )
    SECURITY_DELAY_TIME_ON_BOOT_NOTE = "Start delay timer on power on in seconds. This delay indicates the time after ECU boot power-on where no security access request is accepted."
    SECURITY_LEVEL_NOTE = "This reference identifies the applicable security level for the security access. Stereotypes: atpSplitable Tags: atp.Splitkey=securityLevel"

    def _create_security_access(self) -> DiagnosticSecurityAccess:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticSecurityAccess(ar_root, "TestSecurityAccess")

    def test_initialization(self):
        """
        Test that DiagnosticSecurityAccess is initialized with the spec defaults.
        """
        obj = self._create_security_access()

        assert obj.getShortName() == "TestSecurityAccess"
        assert isinstance(obj, ARElement)
        assert obj.getRequestSeedId() is None
        assert obj.getSecurityAccessClass() is None
        assert obj.getSecurityDelayTimeOnBoot() is None
        assert obj.getSecurityLevel() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (Tags tail dropped).
        """
        assert DiagnosticSecurityAccess.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticSecurityAccess.__init__.__doc__ is None

    def test_get_set_request_seed_id(self):
        """
        Test getRequestSeedId and setRequestSeedId round-trip and None no-op.
        """
        obj = self._create_security_access()

        request_seed_id = PositiveInteger()
        request_seed_id.setValue("259")
        result = obj.setRequestSeedId(request_seed_id)
        assert result is obj  # method chaining
        assert obj.getRequestSeedId() is request_seed_id
        assert obj.getRequestSeedId().getValue() == 259

        result = obj.setRequestSeedId(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestSeedId() is request_seed_id  # None is a no-op

    def test_get_set_security_access_class(self):
        """
        Test getSecurityAccessClass and setSecurityAccessClass round-trip and None no-op.
        """
        obj = self._create_security_access()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-SECURITY-ACCESS-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass")
        result = obj.setSecurityAccessClass(ref)
        assert result is obj  # method chaining
        assert obj.getSecurityAccessClass() is ref
        assert obj.getSecurityAccessClass().getValue() == "/AUTOSAR/DiagnosticSecurityAccessClasses/SecAccessClass"
        assert obj.getSecurityAccessClass().getDest() == "DIAGNOSTIC-SECURITY-ACCESS-CLASS"

        result = obj.setSecurityAccessClass(None)
        assert result is obj  # method chaining with None
        assert obj.getSecurityAccessClass() is ref  # None is a no-op

    def test_get_set_security_delay_time_on_boot(self):
        """
        Test getSecurityDelayTimeOnBoot and setSecurityDelayTimeOnBoot round-trip and None no-op.
        """
        obj = self._create_security_access()

        delay = TimeValue()
        delay.setValue("3.0")
        result = obj.setSecurityDelayTimeOnBoot(delay)
        assert result is obj  # method chaining
        assert obj.getSecurityDelayTimeOnBoot() is delay
        assert obj.getSecurityDelayTimeOnBoot().getValue() == 3.0

        result = obj.setSecurityDelayTimeOnBoot(None)
        assert result is obj  # method chaining with None
        assert obj.getSecurityDelayTimeOnBoot() is delay  # None is a no-op

    def test_get_set_security_level(self):
        """
        Test getSecurityLevel and setSecurityLevel round-trip and None no-op.
        """
        obj = self._create_security_access()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-SECURITY-LEVEL")
        ref.setValue("/AUTOSAR/DiagnosticSecurityLevels/Level1")
        result = obj.setSecurityLevel(ref)
        assert result is obj  # method chaining
        assert obj.getSecurityLevel() is ref
        assert obj.getSecurityLevel().getValue() == "/AUTOSAR/DiagnosticSecurityLevels/Level1"
        assert obj.getSecurityLevel().getDest() == "DIAGNOSTIC-SECURITY-LEVEL"

        result = obj.setSecurityLevel(None)
        assert result is obj  # method chaining with None
        assert obj.getSecurityLevel() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim.
        """
        assert inspect.cleandoc(DiagnosticSecurityAccess.getRequestSeedId.__doc__) == self.REQUEST_SEED_ID_NOTE
        assert inspect.cleandoc(DiagnosticSecurityAccess.setRequestSeedId.__doc__) == (self.REQUEST_SEED_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestSeedId.")
        assert inspect.cleandoc(DiagnosticSecurityAccess.getSecurityAccessClass.__doc__) == self.SECURITY_ACCESS_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticSecurityAccess.setSecurityAccessClass.__doc__) == (
            self.SECURITY_ACCESS_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing securityAccessClass."
        )
        assert inspect.cleandoc(DiagnosticSecurityAccess.getSecurityDelayTimeOnBoot.__doc__) == self.SECURITY_DELAY_TIME_ON_BOOT_NOTE
        assert inspect.cleandoc(DiagnosticSecurityAccess.setSecurityDelayTimeOnBoot.__doc__) == (
            self.SECURITY_DELAY_TIME_ON_BOOT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing securityDelayTimeOnBoot."
        )
        assert inspect.cleandoc(DiagnosticSecurityAccess.getSecurityLevel.__doc__) == self.SECURITY_LEVEL_NOTE
        assert inspect.cleandoc(DiagnosticSecurityAccess.setSecurityLevel.__doc__) == (self.SECURITY_LEVEL_NOTE + "\n\nA None value is a no-op and does not overwrite an existing securityLevel.")

    def test_create_diagnostic_security_access(self):
        """
        Test createDiagnosticSecurityAccess creates, appends and returns the existing one for a duplicate short name.
        """
        package = AUTOSAR.getInstance().createARPackage("SecurityAccesses")

        security_access = package.createDiagnosticSecurityAccess("SecAccess1")
        assert security_access is not None
        assert isinstance(security_access, DiagnosticSecurityAccess)
        assert security_access.getShortName() == "SecAccess1"
        assert security_access.getParent() is package
        assert package.getReferrableElement("SecAccess1", DiagnosticSecurityAccess) is security_access

        duplicate = package.createDiagnosticSecurityAccess("SecAccess1")
        assert duplicate is security_access  # duplicate short name returns the existing element


class TestDiagnosticAuthentication:
    """
    Test class for DiagnosticAuthentication functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.51, p.99
    """

    CLASS_NOTE = "This meta-class represents the ability to configure the usage of the UDS service Authentication in the Diagnostic extract."
    AUTHENTICATION_CLASS_NOTE = (
        'This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of '
        'DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference.'
    )

    def _create_authentication(self) -> DiagnosticAuthenticationConfiguration:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticAuthenticationConfiguration(ar_root, "TestAuthentication")

    def test_is_abstract(self):
        """
        Test that DiagnosticAuthentication cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticAuthentication(AUTOSAR.getInstance(), "Auth1")

    def test_concrete_subclass_instantiation(self):
        """
        Test that a concrete subclass instantiates with the spec defaults.
        """
        obj = self._create_authentication()

        assert obj.getShortName() == "TestAuthentication"
        assert isinstance(obj, ARElement)
        assert obj.getAuthenticationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticAuthentication.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAuthentication.__init__.__doc__ is None

    def test_get_set_authentication_class(self):
        """
        Test getAuthenticationClass and setAuthenticationClass round-trip and None no-op.
        """
        obj = self._create_authentication()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        result = obj.setAuthenticationClass(ref)
        assert result is obj  # method chaining
        assert obj.getAuthenticationClass() is ref
        assert obj.getAuthenticationClass().getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert obj.getAuthenticationClass().getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

        result = obj.setAuthenticationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim.
        """
        assert inspect.cleandoc(DiagnosticAuthentication.getAuthenticationClass.__doc__) == self.AUTHENTICATION_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticAuthentication.setAuthenticationClass.__doc__) == (
            self.AUTHENTICATION_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing authenticationClass."
        )


class TestDiagnosticAuthenticationConfiguration:
    """
    Test class for DiagnosticAuthenticationConfiguration functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.53, p.99
    """

    CLASS_NOTE = "This meta-class represents the subfunction to configure the authentication."

    def _create_configuration(self) -> DiagnosticAuthenticationConfiguration:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticAuthenticationConfiguration(ar_root, "TestConfiguration")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticAuthenticationConfiguration instantiates with the spec defaults.
        """
        obj = self._create_configuration()

        assert obj.getShortName() == "TestConfiguration"
        assert isinstance(obj, DiagnosticAuthentication)
        assert obj.getAuthenticationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticAuthenticationConfiguration.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAuthenticationConfiguration.__init__.__doc__ is None

    def test_defines_no_new_public_members(self):
        """
        Test that the class defines no own public members (Table 4.53 attribute row is "-").
        """
        own_public = {name for name, member in vars(DiagnosticAuthenticationConfiguration).items() if not name.startswith("_")}
        assert own_public == set()

    def test_inherited_authentication_class_accessors(self):
        """
        Test the inherited getAuthenticationClass/setAuthenticationClass round-trip and None no-op.
        """
        obj = self._create_configuration()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        result = obj.setAuthenticationClass(ref)
        assert result is obj  # method chaining
        assert obj.getAuthenticationClass() is ref
        assert obj.getAuthenticationClass().getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert obj.getAuthenticationClass().getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

        result = obj.setAuthenticationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationClass() is ref  # None is a no-op

    def test_create_diagnostic_authentication_configuration(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("AuthenticationConfigurations")
        configuration = package.createDiagnosticAuthenticationConfiguration("AuthCfg1")

        assert configuration is not None
        assert isinstance(configuration, DiagnosticAuthenticationConfiguration)
        assert configuration.getShortName() == "AuthCfg1"
        assert package.getReferrableElement("AuthCfg1", DiagnosticAuthenticationConfiguration) is configuration

        duplicate = package.createDiagnosticAuthenticationConfiguration("AuthCfg1")
        assert duplicate is configuration  # duplicate short name returns the existing element


class TestDiagnosticVerifyCertificateBidirectional:
    """
    Test class for DiagnosticVerifyCertificateBidirectional functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.54, p.99
    """

    CLASS_NOTE = "This meta-class represents the subfunction to do a bidirectional verification of the certificate."

    def _create_verification(self) -> DiagnosticVerifyCertificateBidirectional:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticVerifyCertificateBidirectional(ar_root, "TestVerification")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticVerifyCertificateBidirectional instantiates with the spec defaults.
        """
        obj = self._create_verification()

        assert obj.getShortName() == "TestVerification"
        assert isinstance(obj, DiagnosticAuthentication)
        assert obj.getAuthenticationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticVerifyCertificateBidirectional.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticVerifyCertificateBidirectional.__init__.__doc__ is None

    def test_defines_no_new_public_members(self):
        """
        Test that the class defines no own public members (Table 4.54 attribute row is "-").
        """
        own_public = {name for name, member in vars(DiagnosticVerifyCertificateBidirectional).items() if not name.startswith("_")}
        assert own_public == set()

    def test_inherited_authentication_class_accessors(self):
        """
        Test the inherited getAuthenticationClass/setAuthenticationClass round-trip and None no-op.
        """
        obj = self._create_verification()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        result = obj.setAuthenticationClass(ref)
        assert result is obj  # method chaining
        assert obj.getAuthenticationClass() is ref
        assert obj.getAuthenticationClass().getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert obj.getAuthenticationClass().getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

        result = obj.setAuthenticationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationClass() is ref  # None is a no-op

    def test_create_diagnostic_verify_certificate_bidirectional(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("VerifyCertificateBidirectionals")
        verification = package.createDiagnosticVerifyCertificateBidirectional("VerifyBidir1")

        assert verification is not None
        assert isinstance(verification, DiagnosticVerifyCertificateBidirectional)
        assert verification.getShortName() == "VerifyBidir1"
        assert package.getReferrableElement("VerifyBidir1", DiagnosticVerifyCertificateBidirectional) is verification

        duplicate = package.createDiagnosticVerifyCertificateBidirectional("VerifyBidir1")
        assert duplicate is verification  # duplicate short name returns the existing element


class TestDiagnosticVerifyCertificateUnidirectional:
    """
    Test class for DiagnosticVerifyCertificateUnidirectional functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.55, p.100
    """

    CLASS_NOTE = "This meta-class represents the subfunction to do a unidirectional verification of the certificate."

    def _create_verification(self) -> DiagnosticVerifyCertificateUnidirectional:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticVerifyCertificateUnidirectional(ar_root, "TestVerification")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticVerifyCertificateUnidirectional instantiates with the spec defaults.
        """
        obj = self._create_verification()

        assert obj.getShortName() == "TestVerification"
        assert isinstance(obj, DiagnosticAuthentication)
        assert obj.getAuthenticationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticVerifyCertificateUnidirectional.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticVerifyCertificateUnidirectional.__init__.__doc__ is None

    def test_defines_no_new_public_members(self):
        """
        Test that the class defines no own public members (Table 4.55 attribute row is "-").
        """
        own_public = {name for name, member in vars(DiagnosticVerifyCertificateUnidirectional).items() if not name.startswith("_")}
        assert own_public == set()

    def test_inherited_authentication_class_accessors(self):
        """
        Test the inherited getAuthenticationClass/setAuthenticationClass round-trip and None no-op.
        """
        obj = self._create_verification()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        result = obj.setAuthenticationClass(ref)
        assert result is obj  # method chaining
        assert obj.getAuthenticationClass() is ref
        assert obj.getAuthenticationClass().getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert obj.getAuthenticationClass().getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

        result = obj.setAuthenticationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationClass() is ref  # None is a no-op

    def test_create_diagnostic_verify_certificate_unidirectional(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("VerifyCertificateUnidirectionals")
        verification = package.createDiagnosticVerifyCertificateUnidirectional("VerifyUnidir1")

        assert verification is not None
        assert isinstance(verification, DiagnosticVerifyCertificateUnidirectional)
        assert verification.getShortName() == "VerifyUnidir1"
        assert package.getReferrableElement("VerifyUnidir1", DiagnosticVerifyCertificateUnidirectional) is verification

        duplicate = package.createDiagnosticVerifyCertificateUnidirectional("VerifyUnidir1")
        assert duplicate is verification  # duplicate short name returns the existing element


class TestDiagnosticDeAuthentication:
    """
    Test class for DiagnosticDeAuthentication functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.56, p.100
    """

    CLASS_NOTE = "This meta-class represents the subfunction to remove the authentication"

    def _create_de_authentication(self) -> DiagnosticDeAuthentication:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDeAuthentication(ar_root, "TestDeAuthentication")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticDeAuthentication instantiates with the spec defaults.
        """
        obj = self._create_de_authentication()

        assert obj.getShortName() == "TestDeAuthentication"
        assert isinstance(obj, DiagnosticAuthentication)
        assert obj.getAuthenticationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticDeAuthentication.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticDeAuthentication.__init__.__doc__ is None

    def test_defines_no_new_public_members(self):
        """
        Test that the class defines no own public members (Table 4.56 attribute row is "-").
        """
        own_public = {name for name, member in vars(DiagnosticDeAuthentication).items() if not name.startswith("_")}
        assert own_public == set()

    def test_inherited_authentication_class_accessors(self):
        """
        Test the inherited getAuthenticationClass/setAuthenticationClass round-trip and None no-op.
        """
        obj = self._create_de_authentication()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        result = obj.setAuthenticationClass(ref)
        assert result is obj  # method chaining
        assert obj.getAuthenticationClass() is ref
        assert obj.getAuthenticationClass().getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert obj.getAuthenticationClass().getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

        result = obj.setAuthenticationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationClass() is ref  # None is a no-op

    def test_create_diagnostic_de_authentication(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DeAuthentications")
        de_authentication = package.createDiagnosticDeAuthentication("DeAuth1")

        assert de_authentication is not None
        assert isinstance(de_authentication, DiagnosticDeAuthentication)
        assert de_authentication.getShortName() == "DeAuth1"
        assert package.getReferrableElement("DeAuth1", DiagnosticDeAuthentication) is de_authentication

        duplicate = package.createDiagnosticDeAuthentication("DeAuth1")
        assert duplicate is de_authentication  # duplicate short name returns the existing element


class TestDiagnosticProofOfOwnership:
    """
    Test class for DiagnosticProofOfOwnership functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.57, p.100
    """

    CLASS_NOTE = "This meta-class represents the subfunction to provide proof of ownership."

    def _create_proof_of_ownership(self) -> DiagnosticProofOfOwnership:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticProofOfOwnership(ar_root, "TestProofOfOwnership")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticProofOfOwnership instantiates with the spec defaults.
        """
        obj = self._create_proof_of_ownership()

        assert obj.getShortName() == "TestProofOfOwnership"
        assert isinstance(obj, DiagnosticAuthentication)
        assert obj.getAuthenticationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticProofOfOwnership.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticProofOfOwnership.__init__.__doc__ is None

    def test_defines_no_new_public_members(self):
        """
        Test that the class defines no own public members (Table 4.57 attribute row is "-").
        """
        own_public = {name for name, member in vars(DiagnosticProofOfOwnership).items() if not name.startswith("_")}
        assert own_public == set()

    def test_inherited_authentication_class_accessors(self):
        """
        Test the inherited getAuthenticationClass/setAuthenticationClass round-trip and None no-op.
        """
        obj = self._create_proof_of_ownership()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        result = obj.setAuthenticationClass(ref)
        assert result is obj  # method chaining
        assert obj.getAuthenticationClass() is ref
        assert obj.getAuthenticationClass().getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert obj.getAuthenticationClass().getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

        result = obj.setAuthenticationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationClass() is ref  # None is a no-op

    def test_create_diagnostic_proof_of_ownership(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("ProofOfOwnerships")
        proof_of_ownership = package.createDiagnosticProofOfOwnership("Proof1")

        assert proof_of_ownership is not None
        assert isinstance(proof_of_ownership, DiagnosticProofOfOwnership)
        assert proof_of_ownership.getShortName() == "Proof1"
        assert package.getReferrableElement("Proof1", DiagnosticProofOfOwnership) is proof_of_ownership

        duplicate = package.createDiagnosticProofOfOwnership("Proof1")
        assert duplicate is proof_of_ownership  # duplicate short name returns the existing element


class TestDiagnosticAuthTransmitCertificate:
    """
    Test class for DiagnosticAuthTransmitCertificate functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.58, p.100
    """

    CLASS_NOTE = "This meta-class represents the sub-function to transmit a certificate"

    def _create_certificate(self) -> DiagnosticAuthTransmitCertificate:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticAuthTransmitCertificate(ar_root, "TestCertificate")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticAuthTransmitCertificate instantiates with the spec defaults.
        """
        obj = self._create_certificate()

        assert obj.getShortName() == "TestCertificate"
        assert isinstance(obj, DiagnosticAuthentication)
        assert obj.getAuthenticationClass() is None
        assert obj.getCertificateEvaluations() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticAuthTransmitCertificate.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAuthTransmitCertificate.__init__.__doc__ is None

    def test_inherited_authentication_class_accessors(self):
        """
        Test the inherited getAuthenticationClass/setAuthenticationClass round-trip and None no-op.
        """
        obj = self._create_certificate()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        result = obj.setAuthenticationClass(ref)
        assert result is obj  # method chaining
        assert obj.getAuthenticationClass() is ref
        assert obj.getAuthenticationClass().getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert obj.getAuthenticationClass().getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

        result = obj.setAuthenticationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationClass() is ref  # None is a no-op

    def test_create_certificate_evaluation(self):
        """
        Test that the * aggregation certificateEvaluation creates and reuses the child.
        """
        obj = self._create_certificate()

        evaluation = obj.createDiagnosticAuthTransmitCertificateEvaluation("Eval1")
        assert evaluation is not None
        assert isinstance(evaluation, DiagnosticAuthTransmitCertificateEvaluation)
        assert evaluation.getShortName() == "Eval1"
        assert obj.getCertificateEvaluations() == [evaluation]

        duplicate = obj.createDiagnosticAuthTransmitCertificateEvaluation("Eval1")
        assert duplicate is evaluation  # duplicate short name returns the existing element
        assert len(obj.getCertificateEvaluations()) == 1

    def test_create_diagnostic_auth_transmit_certificate(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
        certificate = package.createDiagnosticAuthTransmitCertificate("Certificate1")

        assert certificate is not None
        assert isinstance(certificate, DiagnosticAuthTransmitCertificate)
        assert certificate.getShortName() == "Certificate1"
        assert package.getReferrableElement("Certificate1", DiagnosticAuthTransmitCertificate) is certificate

        duplicate = package.createDiagnosticAuthTransmitCertificate("Certificate1")
        assert duplicate is certificate  # duplicate short name returns the existing element


class TestDiagnosticEcuReset:
    """
    Test class for DiagnosticEcuReset functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.60, p.102
    """

    CLASS_NOTE = 'This represents an instance of the "ECU Reset" diagnostic service.'

    def _make_obj(self) -> DiagnosticEcuReset:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEcuReset(ar_root, "TestEcuReset")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEcuReset instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEcuReset"
        assert obj.getCustomSubFunctionNumber() is None
        assert obj.getEcuResetClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEcuReset.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEcuReset.__init__.__doc__ is None

    def test_get_set_custom_sub_function_number(self):
        """
        Round-trips customSubFunctionNumber; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("5")
        result = obj.setCustomSubFunctionNumber(value)
        assert result is obj  # method chaining
        assert obj.getCustomSubFunctionNumber() is value
        assert obj.getCustomSubFunctionNumber().getValue() == 5

        obj.setCustomSubFunctionNumber(None)
        assert obj.getCustomSubFunctionNumber() is value  # None is a no-op

    def test_get_set_ecu_reset_class(self):
        """
        Round-trips the ecuResetClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-ECU-RESET-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticEcuResetClasses/ResetClass")
        result = obj.setEcuResetClass(ref)
        assert result is obj  # method chaining
        assert obj.getEcuResetClass() is ref
        assert obj.getEcuResetClass().getValue() == "/AUTOSAR/DiagnosticEcuResetClasses/ResetClass"
        assert obj.getEcuResetClass().getDest() == "DIAGNOSTIC-ECU-RESET-CLASS"

        result = obj.setEcuResetClass(None)
        assert result is obj  # method chaining with None
        assert obj.getEcuResetClass() is ref  # None is a no-op

    def test_create_diagnostic_ecu_reset(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResets")
        ecu_reset = package.createDiagnosticEcuReset("EcuReset1")

        assert ecu_reset is not None
        assert isinstance(ecu_reset, DiagnosticEcuReset)
        assert ecu_reset.getShortName() == "EcuReset1"
        assert package.getReferrableElement("EcuReset1", DiagnosticEcuReset) is ecu_reset

        duplicate = package.createDiagnosticEcuReset("EcuReset1")
        assert duplicate is ecu_reset  # duplicate short name returns the existing element


class TestDiagnosticComControl:
    """
    Test class for DiagnosticComControl functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.64, p.108
    """

    CLASS_NOTE = 'This represents an instance of the "Communication Control" diagnostic service.'

    def _make_obj(self) -> DiagnosticComControl:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticComControl(ar_root, "TestComControl")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticComControl instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestComControl"
        assert obj.getComControlClass() is None
        assert obj.getCustomSubFunctionNumber() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticComControl.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticComControl.__init__.__doc__ is None

    def test_get_set_com_control_class(self):
        """
        Round-trips the comControlClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-COM-CONTROL-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticCommunicationControls/ComControlClass")
        result = obj.setComControlClass(ref)
        assert result is obj  # method chaining
        assert obj.getComControlClass() is ref
        assert obj.getComControlClass().getValue() == "/AUTOSAR/DiagnosticCommunicationControls/ComControlClass"
        assert obj.getComControlClass().getDest() == "DIAGNOSTIC-COM-CONTROL-CLASS"

        result = obj.setComControlClass(None)
        assert result is obj  # method chaining with None
        assert obj.getComControlClass() is ref  # None is a no-op

    def test_get_set_custom_sub_function_number(self):
        """
        Round-trips customSubFunctionNumber; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("5")
        result = obj.setCustomSubFunctionNumber(value)
        assert result is obj  # method chaining
        assert obj.getCustomSubFunctionNumber() is value
        assert obj.getCustomSubFunctionNumber().getValue() == 5

        obj.setCustomSubFunctionNumber(None)
        assert obj.getCustomSubFunctionNumber() is value  # None is a no-op

    def test_create_diagnostic_com_control(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control = package.createDiagnosticComControl("ComControl1")

        assert com_control is not None
        assert isinstance(com_control, DiagnosticComControl)
        assert com_control.getShortName() == "ComControl1"
        assert package.getReferrableElement("ComControl1", DiagnosticComControl) is com_control

        duplicate = package.createDiagnosticComControl("ComControl1")
        assert duplicate is com_control  # duplicate short name returns the existing element


class TestDiagnosticFimEventGroup:
    """
    Test class for DiagnosticFimEventGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.218, p.217
    """

    CLASS_NOTE = "This meta-class represents the ability to model a Fim event group, also known as a summary event in Fim terminology. This represents a group of single diagnostic events. Tags: atp.recommendedPackage=DiagnosticFimEventGroups"

    def _make_obj(self) -> DiagnosticFimEventGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFimEventGroup(ar_root, "TestFimEventGroup")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticFimEventGroup instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFimEventGroup"
        assert obj.getEventRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticFimEventGroup.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFimEventGroup.__init__.__doc__ is None

    def test_add_get_event_refs(self):
        """
        Round-trips the event multi-reference; None is a no-op on add.
        """
        obj = self._make_obj()

        ref1 = RefType()
        ref1.setDest("DIAGNOSTIC-EVENT")
        ref1.setValue("/AUTOSAR/DiagEvents/Evt1")
        result = obj.addEventRef(ref1)
        assert result is obj  # method chaining
        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-EVENT")
        ref2.setValue("/AUTOSAR/DiagEvents/Evt2")
        obj.addEventRef(ref2)

        refs = obj.getEventRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
        assert refs[1].getValue() == "/AUTOSAR/DiagEvents/Evt2"
        assert refs[1].getDest() == "DIAGNOSTIC-EVENT"

        result = obj.addEventRef(None)
        assert result is obj  # method chaining with None
        assert len(obj.getEventRefs()) == 2  # None is a no-op

    def test_create_diagnostic_fim_event_group(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticFimEventGroups")
        fim_event_group = package.createDiagnosticFimEventGroup("FimGroup1")

        assert fim_event_group is not None
        assert isinstance(fim_event_group, DiagnosticFimEventGroup)
        assert fim_event_group.getShortName() == "FimGroup1"
        assert package.getReferrableElement("FimGroup1", DiagnosticFimEventGroup) is fim_event_group

        duplicate = package.createDiagnosticFimEventGroup("FimGroup1")
        assert duplicate is fim_event_group  # duplicate short name returns the existing element


class TestDiagnosticJ1939Spn:
    """
    Test class for DiagnosticJ1939Spn functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.219, p.219
    """

    CLASS_NOTE = "This meta-class represents the ability to model a J1939 Suspect Parameter Number (SPN). Tags: atp.recommendedPackage=DiagnosticJ1939Spns"

    def _make_obj(self) -> DiagnosticJ1939Spn:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticJ1939Spn(ar_root, "TestSpn")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticJ1939Spn instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestSpn"
        assert obj.getSpn() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticJ1939Spn.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticJ1939Spn.__init__.__doc__ is None

    def test_get_set_spn(self):
        """
        Round-trips the spn attribute; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("19000")
        result = obj.setSpn(value)
        assert result is obj  # method chaining
        assert obj.getSpn() is value
        assert obj.getSpn().getValue() == 19000

        result = obj.setSpn(None)
        assert result is obj  # method chaining with None
        assert obj.getSpn() is value  # None is a no-op

    def test_create_diagnostic_j1939_spn(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939Spns")
        spn = package.createDiagnosticJ1939Spn("Spn1")

        assert spn is not None
        assert isinstance(spn, DiagnosticJ1939Spn)
        assert spn.getShortName() == "Spn1"
        assert package.getReferrableElement("Spn1", DiagnosticJ1939Spn) is spn

        duplicate = package.createDiagnosticJ1939Spn("Spn1")
        assert duplicate is spn  # duplicate short name returns the existing element


class TestDiagnosticJ1939FreezeFrame:
    """
    Test class for DiagnosticJ1939FreezeFrame functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.220, p.220
    """

    CLASS_NOTE = "This meta-class represents the ability to model a J1939 Freeze Frame. Tags: atp.recommendedPackage=DiagnosticJ1939FreezeFrames"

    def _make_obj(self) -> DiagnosticJ1939FreezeFrame:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticJ1939FreezeFrame(ar_root, "TestFreezeFrame")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticJ1939FreezeFrame instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFreezeFrame"
        assert obj.getNodeRef() is None
        assert obj.getSpnRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticJ1939FreezeFrame.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticJ1939FreezeFrame.__init__.__doc__ is None

    def test_get_set_node_ref(self):
        """
        Round-trips the node reference; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-J-1939-NODE")
        ref.setValue("/AUTOSAR/J1939Nodes/Node1")
        result = obj.setNodeRef(ref)
        assert result is obj  # method chaining
        assert obj.getNodeRef() is ref
        assert obj.getNodeRef().getValue() == "/AUTOSAR/J1939Nodes/Node1"

        result = obj.setNodeRef(None)
        assert result is obj  # method chaining with None
        assert obj.getNodeRef() is ref  # None is a no-op

    def test_add_get_spn_refs(self):
        """
        Round-trips the spn multi-reference; None is a no-op on add.
        """
        obj = self._make_obj()

        ref1 = RefType()
        ref1.setDest("DIAGNOSTIC-J-1939-SPN")
        ref1.setValue("/AUTOSAR/Spns/Spn1")
        result = obj.addSpnRef(ref1)
        assert result is obj  # method chaining
        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-J-1939-SPN")
        ref2.setValue("/AUTOSAR/Spns/Spn2")
        obj.addSpnRef(ref2)

        refs = obj.getSpnRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
        assert refs[1].getValue() == "/AUTOSAR/Spns/Spn2"

        result = obj.addSpnRef(None)
        assert result is obj  # method chaining with None
        assert len(obj.getSpnRefs()) == 2  # None is a no-op

    def test_create_diagnostic_j1939_freeze_frame(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939FreezeFrames")
        freeze_frame = package.createDiagnosticJ1939FreezeFrame("FreezeFrame1")

        assert freeze_frame is not None
        assert isinstance(freeze_frame, DiagnosticJ1939FreezeFrame)
        assert freeze_frame.getShortName() == "FreezeFrame1"
        assert package.getReferrableElement("FreezeFrame1", DiagnosticJ1939FreezeFrame) is freeze_frame

        duplicate = package.createDiagnosticJ1939FreezeFrame("FreezeFrame1")
        assert duplicate is freeze_frame  # duplicate short name returns the existing element


class TestDiagnosticJ1939ExpandedFreezeFrame:
    """
    Test class for DiagnosticJ1939ExpandedFreezeFrame functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.221, p.221
    """

    CLASS_NOTE = "This meta-class represents the ability to model an expanded J1939 Freeze Frame. Tags: atp.recommendedPackage=DiagnosticJ1939ExpandedFreezeFrames"

    def _make_obj(self) -> DiagnosticJ1939ExpandedFreezeFrame:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticJ1939ExpandedFreezeFrame(ar_root, "TestExpandedFreezeFrame")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticJ1939ExpandedFreezeFrame instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestExpandedFreezeFrame"
        assert obj.getNodeRef() is None
        assert obj.getSpnRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticJ1939ExpandedFreezeFrame.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticJ1939ExpandedFreezeFrame.__init__.__doc__ is None

    def test_get_set_node_ref(self):
        """
        Round-trips the node reference; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-J-1939-NODE")
        ref.setValue("/AUTOSAR/J1939Nodes/Node1")
        result = obj.setNodeRef(ref)
        assert result is obj  # method chaining
        assert obj.getNodeRef() is ref

        result = obj.setNodeRef(None)
        assert result is obj  # method chaining with None
        assert obj.getNodeRef() is ref  # None is a no-op

    def test_add_get_spn_refs(self):
        """
        Round-trips the spn multi-reference; None is a no-op on add.
        """
        obj = self._make_obj()

        ref1 = RefType()
        ref1.setDest("DIAGNOSTIC-J-1939-SPN")
        ref1.setValue("/AUTOSAR/Spns/Spn1")
        result = obj.addSpnRef(ref1)
        assert result is obj  # method chaining
        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-J-1939-SPN")
        ref2.setValue("/AUTOSAR/Spns/Spn2")
        obj.addSpnRef(ref2)

        refs = obj.getSpnRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
        assert refs[1].getValue() == "/AUTOSAR/Spns/Spn2"

        result = obj.addSpnRef(None)
        assert result is obj  # method chaining with None
        assert len(obj.getSpnRefs()) == 2  # None is a no-op

    def test_create_diagnostic_j1939_expanded_freeze_frame(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939ExpandedFreezeFrames")
        expanded_freeze_frame = package.createDiagnosticJ1939ExpandedFreezeFrame("ExpandedFreezeFrame1")

        assert expanded_freeze_frame is not None
        assert isinstance(expanded_freeze_frame, DiagnosticJ1939ExpandedFreezeFrame)
        assert expanded_freeze_frame.getShortName() == "ExpandedFreezeFrame1"
        assert package.getReferrableElement("ExpandedFreezeFrame1", DiagnosticJ1939ExpandedFreezeFrame) is expanded_freeze_frame

        duplicate = package.createDiagnosticJ1939ExpandedFreezeFrame("ExpandedFreezeFrame1")
        assert duplicate is expanded_freeze_frame  # duplicate short name returns the existing element


class TestDiagnosticTroubleCode:
    """
    Test class for DiagnosticTroubleCode functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.161, p.176

    DiagnosticTroubleCode is abstract and carries no Attribute rows of its own
    (the XSD group DIAGNOSTIC-TROUBLE-CODE is an empty sequence) — the only
    members are the Identifiable defaults inherited from ARElement, so defaults
    and the factory shape are exercised directly on the class.
    """

    CLASS_NOTE = "A diagnostic trouble code defines a unique identifier that is shown to the diagnostic tester."

    def _make_obj(self) -> DiagnosticTroubleCode:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTroubleCode(ar_root, "TestTroubleCode")

    def test_initialization(self):
        """
        Test that the abstract class instantiates with the most-derived base chain and the inherited defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestTroubleCode"
        assert isinstance(obj, DiagnosticTroubleCode)
        assert isinstance(obj, ARElement)
        assert isinstance(obj, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticTroubleCode.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTroubleCode.__init__.__doc__ is None

    def test_create_diagnostic_trouble_code(self):
        """
        Test that ARPackage.createDiagnosticTroubleCode appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticTroubleCode("TroubleCode1")

        assert isinstance(obj, DiagnosticTroubleCode)
        assert obj.getShortName() == "TroubleCode1"
        assert ar_root.getReferrableElement("TroubleCode1", DiagnosticTroubleCode) is obj

        duplicate = ar_root.createDiagnosticTroubleCode("TroubleCode1")
        assert duplicate is obj


class TestDiagnosticTroubleCodeGroup:
    """
    Test class for DiagnosticTroubleCodeGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.162, p.177

    DiagnosticTroubleCodeGroup is concrete (XSD complexType abstract="false") with
    two Attribute rows in displayed order: dtc (DiagnosticTroubleCode, *, ref) —
    modeled as the dtcRefs list of RefType — and groupNumber (PositiveInteger,
    0..1, attr). Fields inherited from ARElement carry no rows of their own.
    """

    CLASS_NOTE = (
        "The diagnostic trouble code group defines the DTCs belonging together and thereby forming a group. "
        "Tags: atp.recommendedPackage=DiagnosticTroubleCodes\n"
        "\n"
        "[constr_1830] Existence of DiagnosticTroubleCodeGroup.groupNumber: "
        "For each DiagnosticTroubleCodeGroup, attribute groupNumber shall exist "
        "at the time when the DEXT is complete."
    )

    def _make_obj(self) -> DiagnosticTroubleCodeGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTroubleCodeGroup(ar_root, "TestTroubleCodeGroup")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestTroubleCodeGroup"
        assert isinstance(obj, DiagnosticTroubleCodeGroup)
        assert isinstance(obj, ARElement)
        assert isinstance(obj, Identifiable)
        assert obj.getDtcRefs() == []
        assert obj.getGroupNumber() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim plus the class constraint.
        """
        assert inspect.cleandoc(DiagnosticTroubleCodeGroup.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTroubleCodeGroup.__init__.__doc__ is None

    def test_add_get_dtc_refs(self):
        """
        Round-trips dtc refs; None is a no-op and chaining returns self.
        """
        obj = self._make_obj()

        ref1 = RefType().setValue("/DiagnosticTroubleCodes/TroubleCode1")
        ref2 = RefType().setValue("/DiagnosticTroubleCodes/TroubleCode2")

        result = obj.addDtcRef(ref1)
        assert result is obj  # method chaining
        obj.addDtcRef(ref2)

        refs = obj.getDtcRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
        assert refs[0].getValue() == "/DiagnosticTroubleCodes/TroubleCode1"
        assert refs[1].getValue() == "/DiagnosticTroubleCodes/TroubleCode2"

        result = obj.addDtcRef(None)
        assert result is obj  # method chaining with None
        assert len(obj.getDtcRefs()) == 2  # None is a no-op

    def test_get_set_group_number(self):
        """
        Round-trips groupNumber; None is a no-op and chaining returns self.
        """
        obj = self._make_obj()

        group_number = PositiveInteger()
        group_number.setValue(3)

        result = obj.setGroupNumber(group_number)
        assert result is obj  # method chaining
        assert obj.getGroupNumber() is group_number

        obj.setGroupNumber(None)
        assert obj.getGroupNumber() is group_number  # None is a no-op

    def test_create_diagnostic_trouble_code_group(self):
        """
        Test that ARPackage.createDiagnosticTroubleCodeGroup appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticTroubleCodeGroup("TroubleCodeGroup1")

        assert isinstance(obj, DiagnosticTroubleCodeGroup)
        assert obj.getShortName() == "TroubleCodeGroup1"
        assert ar_root.getReferrableElement("TroubleCodeGroup1", DiagnosticTroubleCodeGroup) is obj

        duplicate = ar_root.createDiagnosticTroubleCodeGroup("TroubleCodeGroup1")
        assert duplicate is obj


class TestDiagnosticTroubleCodeJ1939:
    """
    Test class for DiagnosticTroubleCodeJ1939 functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.223, p.222
    """

    CLASS_NOTE = "This meta-class represents the ability to model specific trouble-code related properties for J1939. Tags: atp.recommendedPackage=DiagnosticTroubleCodes"

    def _make_obj(self) -> DiagnosticTroubleCodeJ1939:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTroubleCodeJ1939(ar_root, "TestDtc")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticTroubleCodeJ1939 instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestDtc"
        assert obj.getDtcPropsRef() is None
        assert obj.getFmi() is None
        assert obj.getKind() is None
        assert obj.getNodeRef() is None
        assert obj.getSpnRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticTroubleCodeJ1939.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTroubleCodeJ1939.__init__.__doc__ is None

    def test_get_set_fmi(self):
        """
        Round-trips the fmi attribute; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("9")
        result = obj.setFmi(value)
        assert result is obj  # method chaining
        assert obj.getFmi() is value
        assert obj.getFmi().getValue() == 9

        result = obj.setFmi(None)
        assert result is obj  # method chaining with None
        assert obj.getFmi() is value  # None is a no-op

    def test_get_set_kind(self):
        """
        Round-trips the kind enum attribute; None is a no-op.
        """
        obj = self._make_obj()

        kind = DiagnosticTroubleCodeJ1939DtcKindEnum()
        kind.setValue(DiagnosticTroubleCodeJ1939DtcKindEnum.SERVICE_ONLY)
        result = obj.setKind(kind)
        assert result is obj  # method chaining
        assert obj.getKind() is kind
        assert obj.getKind().getValue() == DiagnosticTroubleCodeJ1939DtcKindEnum.SERVICE_ONLY

        result = obj.setKind(None)
        assert result is obj  # method chaining with None
        assert obj.getKind() is kind  # None is a no-op

    def test_get_set_refs(self):
        """
        Round-trips the dtcProps/node/spn references; None is a no-op.
        """
        obj = self._make_obj()

        dtc_props_ref = RefType().setValue("/AUTOSAR/DtcProps/Props1").setDest("DIAGNOSTIC-TROUBLE-CODE-PROPS")
        node_ref = RefType().setValue("/AUTOSAR/J1939Nodes/Node1").setDest("DIAGNOSTIC-J-1939-NODE")
        spn_ref = RefType().setValue("/AUTOSAR/Spns/Spn1").setDest("DIAGNOSTIC-J-1939-SPN")
        obj.setDtcPropsRef(dtc_props_ref)
        obj.setNodeRef(node_ref)
        obj.setSpnRef(spn_ref)

        assert obj.getDtcPropsRef() is dtc_props_ref
        assert obj.getNodeRef() is node_ref
        assert obj.getSpnRef() is spn_ref

        obj.setDtcPropsRef(None)
        obj.setNodeRef(None)
        obj.setSpnRef(None)
        assert obj.getDtcPropsRef() is dtc_props_ref  # None is a no-op
        assert obj.getNodeRef() is node_ref  # None is a no-op
        assert obj.getSpnRef() is spn_ref  # None is a no-op

    def test_create_diagnostic_trouble_code_j1939(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        trouble_code = package.createDiagnosticTroubleCodeJ1939("Dtc1")

        assert trouble_code is not None
        assert isinstance(trouble_code, DiagnosticTroubleCodeJ1939)
        assert trouble_code.getShortName() == "Dtc1"
        assert package.getReferrableElement("Dtc1", DiagnosticTroubleCodeJ1939) is trouble_code

        duplicate = package.createDiagnosticTroubleCodeJ1939("Dtc1")
        assert duplicate is trouble_code  # duplicate short name returns the existing element


class TestDiagnosticSwMapping:
    """
    Test class for DiagnosticSwMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.14, p.238
    """

    CLASS_NOTE = "This represents the ability to define a mapping between a diagnostic information (at this point there is no way to become more specific about the semantics) to a software-component."

    def test_is_abstract(self):
        """
        Test that DiagnosticSwMapping is abstract and cannot be instantiated.
        """
        with pytest.raises(TypeError):
            DiagnosticSwMapping(AUTOSAR.getInstance(), "SwMapping")

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticSwMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticSwMapping.__init__.__doc__ is None

    def test_concrete_subclass_instantiates(self):
        """
        Test that a concrete subclass inherits the DiagnosticMapping base accessors.
        """

        class DummySwMapping(DiagnosticSwMapping):
            pass

        package = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = DummySwMapping(package, "Dummy")

        assert obj.getShortName() == "Dummy"
        assert obj.getProviderSoftwareClusterRef() is None
        assert obj.getRequesterSoftwareClusterRef() is None


class TestDiagnosticParameterElementAccess:
    """
    Test class for DiagnosticParameterElementAccess functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.5, p.229
    """

    CLASS_NOTE = "This meta-class acts as a single point for defining structured references to a specific DiagnosticParameterElement."

    def _make_obj(self) -> DiagnosticParameterElementAccess:
        return DiagnosticParameterElementAccess()

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticParameterElementAccess instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj is not None
        assert obj.getContextElementRefs() == []
        assert obj.getTargetElementRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticParameterElementAccess.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticParameterElementAccess.__init__.__doc__ is None

    def test_add_get_context_element_refs(self):
        """
        Round-trips the contextElement multi-reference; None is a no-op on add.
        """
        obj = self._make_obj()

        ref1 = RefType()
        ref1.setDest("DIAGNOSTIC-PARAMETER-ELEMENT")
        ref1.setValue("/AUTOSAR/ParamElements/Ctx1")
        result = obj.addContextElementRef(ref1)
        assert result is obj  # method chaining
        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-PARAMETER-ELEMENT")
        ref2.setValue("/AUTOSAR/ParamElements/Ctx2")
        obj.addContextElementRef(ref2)

        refs = obj.getContextElementRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
        assert refs[1].getValue() == "/AUTOSAR/ParamElements/Ctx2"

        result = obj.addContextElementRef(None)
        assert result is obj  # method chaining with None
        assert len(obj.getContextElementRefs()) == 2  # None is a no-op

    def test_get_set_target_element_ref(self):
        """
        Round-trips the targetElement reference; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-PARAMETER-ELEMENT")
        ref.setValue("/AUTOSAR/ParamElements/Target")
        result = obj.setTargetElementRef(ref)
        assert result is obj  # method chaining
        assert obj.getTargetElementRef() is ref

        result = obj.setTargetElementRef(None)
        assert result is obj  # method chaining with None
        assert obj.getTargetElementRef() is ref  # None is a no-op


class TestDiagnosticServiceDataMapping:
    """
    Test class for DiagnosticServiceDataMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.4, p.228
    """

    CLASS_NOTE = "This represents the ability to define a mapping of a diagnostic service to a software-component. This kind of service mapping is applicable for the usage of SenderReceiverInterfaces or event/notifier semantics in ServiceInterfaces on the adaptive platform. Tags: atp.recommendedPackage=DiagnosticServiceMappings"

    def _make_obj(self) -> DiagnosticServiceDataMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticServiceDataMapping(ar_root, "TestServiceDataMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticServiceDataMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestServiceDataMapping"
        assert obj.getDiagnosticDataElementRef() is None
        assert obj.getDiagnosticParameterRef() is None
        assert obj.getMappedDataElementIRef() is None
        assert obj.getParameterElementAccess() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticServiceDataMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticServiceDataMapping.__init__.__doc__ is None

    def test_get_set_refs_and_aggregation(self):
        """
        Round-trips the references and the parameterElementAccess aggregation; None is a no-op.
        """
        obj = self._make_obj()

        data_ref = RefType().setValue("/AUTOSAR/DataElements/Did1").setDest("DIAGNOSTIC-DATA-ELEMENT")
        param_ref = RefType().setValue("/AUTOSAR/ParamIdents/Ident1").setDest("DIAGNOSTIC-PARAMETER-IDENT")
        iref = RefType().setValue("/AUTOSAR/SwDataDefs/Proto1")
        pea = DiagnosticParameterElementAccess()
        obj.setDiagnosticDataElementRef(data_ref)
        obj.setDiagnosticParameterRef(param_ref)
        obj.setMappedDataElementIRef(iref)
        obj.setParameterElementAccess(pea)

        assert obj.getDiagnosticDataElementRef() is data_ref
        assert obj.getDiagnosticParameterRef() is param_ref
        assert obj.getMappedDataElementIRef() is iref
        assert obj.getParameterElementAccess() is pea

        obj.setDiagnosticDataElementRef(None)
        obj.setDiagnosticParameterRef(None)
        obj.setMappedDataElementIRef(None)
        obj.setParameterElementAccess(None)
        assert obj.getDiagnosticDataElementRef() is data_ref  # None is a no-op
        assert obj.getDiagnosticParameterRef() is param_ref  # None is a no-op
        assert obj.getMappedDataElementIRef() is iref  # None is a no-op
        assert obj.getParameterElementAccess() is pea  # None is a no-op

    def test_create_diagnostic_service_data_mapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticServiceMappings")
        service_data_mapping = package.createDiagnosticServiceDataMapping("Mapping1")

        assert service_data_mapping is not None
        assert isinstance(service_data_mapping, DiagnosticServiceDataMapping)
        assert service_data_mapping.getShortName() == "Mapping1"
        assert package.getReferrableElement("Mapping1", DiagnosticServiceDataMapping) is service_data_mapping

        duplicate = package.createDiagnosticServiceDataMapping("Mapping1")
        assert duplicate is service_data_mapping  # duplicate short name returns the existing element


class TestDiagnosticServiceMappingDiagTarget:
    """
    Test class for DiagnosticServiceMappingDiagTarget functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.12, p.234
    """

    CLASS_NOTE = "This meta-class serves as a base class for diagnostics-related targets of subclasses of DiagnosticSwMapping."

    def test_is_abstract(self):
        """
        Test that DiagnosticServiceMappingDiagTarget is abstract and cannot be instantiated.
        """
        with pytest.raises(TypeError):
            DiagnosticServiceMappingDiagTarget()

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticServiceMappingDiagTarget.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticServiceMappingDiagTarget.__init__.__doc__ is None


class TestDiagnosticEventToDebounceAlgorithmMapping:
    """
    Test class for DiagnosticEventToDebounceAlgorithmMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.21, p.246
    """

    CLASS_NOTE = "Defines which Debounce Algorithm is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventToDebounceAlgorithmMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventToDebounceAlgorithmMapping(ar_root, "TestEventToDebounceAlgorithmMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventToDebounceAlgorithmMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventToDebounceAlgorithmMapping"
        assert obj.getDebounceAlgorithmRef() is None
        assert obj.getDiagnosticEventRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventToDebounceAlgorithmMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventToDebounceAlgorithmMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDebounceAlgorithmRef(RefType().setValue("/AUTOSAR/DebounceAlgorithm1").setDest("DEST"))
        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))

        assert obj.getDebounceAlgorithmRef() is not None
        assert obj.getDiagnosticEventRef() is not None

        obj.setDebounceAlgorithmRef(None)
        obj.setDiagnosticEventRef(None)
        assert obj.getDebounceAlgorithmRef().getValue() == "/AUTOSAR/DebounceAlgorithm1"  # None is a no-op
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op

    def test_create_diagnosticEventToDebounceAlgorithmMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventToDebounceAlgorithmMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventToDebounceAlgorithmMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventToDebounceAlgorithmMapping) is element

        duplicate = package.createDiagnosticEventToDebounceAlgorithmMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEventToEnableConditionGroupMapping:
    """
    Test class for DiagnosticEventToEnableConditionGroupMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.22, p.247
    """

    CLASS_NOTE = "Defines which EnableConditionGroup is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventToEnableConditionGroupMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventToEnableConditionGroupMapping(ar_root, "TestEventToEnableConditionGroupMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventToEnableConditionGroupMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventToEnableConditionGroupMapping"
        assert obj.getDiagnosticEventRef() is None
        assert obj.getEnableConditionGroupRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventToEnableConditionGroupMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventToEnableConditionGroupMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        obj.setEnableConditionGroupRef(RefType().setValue("/AUTOSAR/EnableConditionGroup1").setDest("DEST"))

        assert obj.getDiagnosticEventRef() is not None
        assert obj.getEnableConditionGroupRef() is not None

        obj.setDiagnosticEventRef(None)
        obj.setEnableConditionGroupRef(None)
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getEnableConditionGroupRef().getValue() == "/AUTOSAR/EnableConditionGroup1"  # None is a no-op

    def test_create_diagnosticEventToEnableConditionGroupMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventToEnableConditionGroupMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventToEnableConditionGroupMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventToEnableConditionGroupMapping) is element

        duplicate = package.createDiagnosticEventToEnableConditionGroupMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEventToOperationCycleMapping:
    """
    Test class for DiagnosticEventToOperationCycleMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.20, p.245
    """

    CLASS_NOTE = "Defines which OperationCycle is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventToOperationCycleMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventToOperationCycleMapping(ar_root, "TestEventToOperationCycleMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventToOperationCycleMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventToOperationCycleMapping"
        assert obj.getDiagnosticEventRef() is None
        assert obj.getOperationCycleRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventToOperationCycleMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventToOperationCycleMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        obj.setOperationCycleRef(RefType().setValue("/AUTOSAR/OperationCycle1").setDest("DEST"))

        assert obj.getDiagnosticEventRef() is not None
        assert obj.getOperationCycleRef() is not None

        obj.setDiagnosticEventRef(None)
        obj.setOperationCycleRef(None)
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getOperationCycleRef().getValue() == "/AUTOSAR/OperationCycle1"  # None is a no-op

    def test_create_diagnosticEventToOperationCycleMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventToOperationCycleMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventToOperationCycleMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventToOperationCycleMapping) is element

        duplicate = package.createDiagnosticEventToOperationCycleMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEventToStorageConditionGroupMapping:
    """
    Test class for DiagnosticEventToStorageConditionGroupMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.23, p.248
    """

    CLASS_NOTE = "Defines which StorageConditionGroup is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventToStorageConditionGroupMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventToStorageConditionGroupMapping(ar_root, "TestEventToStorageConditionGroupMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventToStorageConditionGroupMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventToStorageConditionGroupMapping"
        assert obj.getDiagnosticEventRef() is None
        assert obj.getStorageConditionGroupRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventToStorageConditionGroupMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventToStorageConditionGroupMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        obj.setStorageConditionGroupRef(RefType().setValue("/AUTOSAR/StorageConditionGroup1").setDest("DEST"))

        assert obj.getDiagnosticEventRef() is not None
        assert obj.getStorageConditionGroupRef() is not None

        obj.setDiagnosticEventRef(None)
        obj.setStorageConditionGroupRef(None)
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getStorageConditionGroupRef().getValue() == "/AUTOSAR/StorageConditionGroup1"  # None is a no-op

    def test_create_diagnosticEventToStorageConditionGroupMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventToStorageConditionGroupMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventToStorageConditionGroupMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventToStorageConditionGroupMapping) is element

        duplicate = package.createDiagnosticEventToStorageConditionGroupMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEventToTroubleCodeUdsMapping:
    """
    Test class for DiagnosticEventToTroubleCodeUdsMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.19, p.245
    """

    CLASS_NOTE = "Defines which UDS Diagnostic Trouble Code is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventToTroubleCodeUdsMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventToTroubleCodeUdsMapping(ar_root, "TestEventToTroubleCodeUdsMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventToTroubleCodeUdsMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventToTroubleCodeUdsMapping"
        assert obj.getDiagnosticEventRef() is None
        assert obj.getTroubleCodeUdsRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventToTroubleCodeUdsMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventToTroubleCodeUdsMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        obj.setTroubleCodeUdsRef(RefType().setValue("/AUTOSAR/TroubleCodeUds1").setDest("DEST"))

        assert obj.getDiagnosticEventRef() is not None
        assert obj.getTroubleCodeUdsRef() is not None

        obj.setDiagnosticEventRef(None)
        obj.setTroubleCodeUdsRef(None)
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getTroubleCodeUdsRef().getValue() == "/AUTOSAR/TroubleCodeUds1"  # None is a no-op

    def test_create_diagnosticEventToTroubleCodeUdsMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventToTroubleCodeUdsMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventToTroubleCodeUdsMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventToTroubleCodeUdsMapping) is element

        duplicate = package.createDiagnosticEventToTroubleCodeUdsMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEventPortMapping:
    """
    Test class for DiagnosticEventPortMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.24, p.249
    """

    CLASS_NOTE = "Defines to which SWC service ports the DiagnosticEvent is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventPortMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventPortMapping(ar_root, "TestEventPortMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventPortMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventPortMapping"
        assert obj.getBswServiceDependencyRef() is None
        assert obj.getDiagnosticEventRef() is None
        assert obj.getSwcFlatServiceDependencyRef() is None
        assert obj.getSwcServiceDependencyInSystemIRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventPortMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventPortMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setBswServiceDependencyRef(RefType().setValue("/AUTOSAR/BswServiceDependency1"))
        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        obj.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        obj.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        assert obj.getBswServiceDependencyRef() is not None
        assert obj.getDiagnosticEventRef() is not None
        assert obj.getSwcFlatServiceDependencyRef() is not None
        assert obj.getSwcServiceDependencyInSystemIRef() is not None

        obj.setBswServiceDependencyRef(None)
        obj.setDiagnosticEventRef(None)
        obj.setSwcFlatServiceDependencyRef(None)
        obj.setSwcServiceDependencyInSystemIRef(None)
        assert obj.getBswServiceDependencyRef().getValue() == "/AUTOSAR/BswServiceDependency1"  # None is a no-op
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"  # None is a no-op
        assert obj.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"  # None is a no-op

    def test_create_diagnosticEventPortMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventPortMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventPortMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventPortMapping) is element

        duplicate = package.createDiagnosticEventPortMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticOperationCyclePortMapping:
    """
    Test class for DiagnosticOperationCyclePortMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.25, p.250
    """

    CLASS_NOTE = "Defines to which SWC service ports the DiagnosticOperationCycle is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticOperationCyclePortMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticOperationCyclePortMapping(ar_root, "TestOperationCyclePortMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticOperationCyclePortMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestOperationCyclePortMapping"
        assert obj.getOperationCycleRef() is None
        assert obj.getSwcFlatServiceDependencyRef() is None
        assert obj.getSwcServiceDependencyInSystemIRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticOperationCyclePortMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticOperationCyclePortMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setOperationCycleRef(RefType().setValue("/AUTOSAR/OperationCycle1"))
        obj.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        obj.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        assert obj.getOperationCycleRef() is not None
        assert obj.getSwcFlatServiceDependencyRef() is not None
        assert obj.getSwcServiceDependencyInSystemIRef() is not None

        obj.setOperationCycleRef(None)
        obj.setSwcFlatServiceDependencyRef(None)
        obj.setSwcServiceDependencyInSystemIRef(None)
        assert obj.getOperationCycleRef().getValue() == "/AUTOSAR/OperationCycle1"  # None is a no-op
        assert obj.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"  # None is a no-op
        assert obj.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"  # None is a no-op

    def test_create_diagnosticOperationCyclePortMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticOperationCyclePortMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticOperationCyclePortMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticOperationCyclePortMapping) is element

        duplicate = package.createDiagnosticOperationCyclePortMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEnableConditionPortMapping:
    """
    Test class for DiagnosticEnableConditionPortMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.26, p.252
    """

    CLASS_NOTE = "Defines to which SWC service ports the DiagnosticEnableCondition is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEnableConditionPortMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEnableConditionPortMapping(ar_root, "TestEnableConditionPortMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEnableConditionPortMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEnableConditionPortMapping"
        assert obj.getEnableConditionRef() is None
        assert obj.getSwcFlatServiceDependencyRef() is None
        assert obj.getSwcServiceDependencyInSystemIRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEnableConditionPortMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEnableConditionPortMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setEnableConditionRef(RefType().setValue("/AUTOSAR/EnableCondition1"))
        obj.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        obj.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        assert obj.getEnableConditionRef() is not None
        assert obj.getSwcFlatServiceDependencyRef() is not None
        assert obj.getSwcServiceDependencyInSystemIRef() is not None

        obj.setEnableConditionRef(None)
        obj.setSwcFlatServiceDependencyRef(None)
        obj.setSwcServiceDependencyInSystemIRef(None)
        assert obj.getEnableConditionRef().getValue() == "/AUTOSAR/EnableCondition1"  # None is a no-op
        assert obj.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"  # None is a no-op
        assert obj.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"  # None is a no-op

    def test_create_diagnosticEnableConditionPortMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEnableConditionPortMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEnableConditionPortMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEnableConditionPortMapping) is element

        duplicate = package.createDiagnosticEnableConditionPortMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticStorageConditionPortMapping:
    """
    Test class for DiagnosticStorageConditionPortMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.27, p.253
    """

    CLASS_NOTE = "Defines to which SWC service ports with DiagnosticStorageConditionNeeds the DiagnosticStorageCondition is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticStorageConditionPortMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticStorageConditionPortMapping(ar_root, "TestStorageConditionPortMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticStorageConditionPortMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestStorageConditionPortMapping"
        assert obj.getDiagnosticStorageConditionRef() is None
        assert obj.getSwcFlatServiceDependencyRef() is None
        assert obj.getSwcServiceDependencyInSystemIRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticStorageConditionPortMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticStorageConditionPortMapping.__init__.__doc__ is None

    def test_get_set_refs(self):
        """
        Round-trips the references; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticStorageConditionRef(RefType().setValue("/AUTOSAR/DiagnosticStorageCondition1"))
        obj.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        obj.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        assert obj.getDiagnosticStorageConditionRef() is not None
        assert obj.getSwcFlatServiceDependencyRef() is not None
        assert obj.getSwcServiceDependencyInSystemIRef() is not None

        obj.setDiagnosticStorageConditionRef(None)
        obj.setSwcFlatServiceDependencyRef(None)
        obj.setSwcServiceDependencyInSystemIRef(None)
        assert obj.getDiagnosticStorageConditionRef().getValue() == "/AUTOSAR/DiagnosticStorageCondition1"  # None is a no-op
        assert obj.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"  # None is a no-op
        assert obj.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"  # None is a no-op

    def test_create_diagnosticStorageConditionPortMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticStorageConditionPortMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticStorageConditionPortMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticStorageConditionPortMapping) is element

        duplicate = package.createDiagnosticStorageConditionPortMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticAuthTransmitCertificateMapping:
    """
    Test class for DiagnosticAuthTransmitCertificateMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.17, p.242
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a CryptoServiceCertificate with a DiagnosticAuthCertificateEvaluation with the purpose to configure the evaluation of the certificate. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticAuthTransmitCertificateMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticAuthTransmitCertificateMapping(ar_root, "TestAuthTransmitCertificateMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticAuthTransmitCertificateMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestAuthTransmitCertificateMapping"
        assert obj.getCryptoServiceCertificateRefs() == []
        assert obj.getServiceInstanceRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticAuthTransmitCertificateMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAuthTransmitCertificateMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.addCryptoServiceCertificateRef(RefType().setValue("/AUTOSAR/CryptoServiceCertificate1"))
        obj.setServiceInstanceRef(RefType().setValue("/AUTOSAR/ServiceInstance1"))

        assert obj.getCryptoServiceCertificateRefs()[0].getValue() == "/AUTOSAR/CryptoServiceCertificate1"
        assert obj.getServiceInstanceRef().getValue() == "/AUTOSAR/ServiceInstance1"

        obj.addCryptoServiceCertificateRef(None)
        obj.setServiceInstanceRef(None)
        assert len(obj.getCryptoServiceCertificateRefs()) == 1  # None is a no-op
        assert obj.getServiceInstanceRef().getValue() == "/AUTOSAR/ServiceInstance1"  # None is a no-op

    def test_create_diagnosticAuthTransmitCertificateMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticAuthTransmitCertificateMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticAuthTransmitCertificateMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticAuthTransmitCertificateMapping) is element

        duplicate = package.createDiagnosticAuthTransmitCertificateMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticSecurityEventReportingModeMapping:
    """
    Test class for DiagnosticSecurityEventReportingModeMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.18, p.243
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a location in a DID with a security event. The purpose of this mapping is that the location in the DID contains the setting of the reporting mode for the specific security event. This means that the reporting mode of the security event can be set via the diagnostic service WriteDataByIdentifier. Tags: atp.Status=candidate atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticSecurityEventReportingModeMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticSecurityEventReportingModeMapping(ar_root, "TestSecurityEventReportingModeMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticSecurityEventReportingModeMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestSecurityEventReportingModeMapping"
        assert obj.getDataElementRef() is None
        assert obj.getSecurityEventRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticSecurityEventReportingModeMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticSecurityEventReportingModeMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDataElementRef(RefType().setValue("/AUTOSAR/DataElement1"))
        obj.setSecurityEventRef(RefType().setValue("/AUTOSAR/SecurityEvent1"))

        assert obj.getDataElementRef().getValue() == "/AUTOSAR/DataElement1"
        assert obj.getSecurityEventRef().getValue() == "/AUTOSAR/SecurityEvent1"

        obj.setDataElementRef(None)
        obj.setSecurityEventRef(None)
        assert obj.getDataElementRef().getValue() == "/AUTOSAR/DataElement1"  # None is a no-op
        assert obj.getSecurityEventRef().getValue() == "/AUTOSAR/SecurityEvent1"  # None is a no-op

    def test_create_diagnosticSecurityEventReportingModeMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticSecurityEventReportingModeMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticSecurityEventReportingModeMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticSecurityEventReportingModeMapping) is element

        duplicate = package.createDiagnosticSecurityEventReportingModeMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticDemProvidedDataMapping:
    """
    Test class for DiagnosticDemProvidedDataMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.28, p.255
    """

    CLASS_NOTE = "This represents the ability to define the nature of a data access for a DiagnosticDataElement in the Dem. Tags: atp.recommendedPackage=DiagnosticServiceMappings"

    def _make_obj(self) -> DiagnosticDemProvidedDataMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDemProvidedDataMapping(ar_root, "TestDemProvidedDataMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticDemProvidedDataMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestDemProvidedDataMapping"
        assert obj.getDataElementRef() is None
        assert obj.getDataProvider() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticDemProvidedDataMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticDemProvidedDataMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDataElementRef(RefType().setValue("/AUTOSAR/DataElement1"))
        obj.setDataProvider(NameToken().setValue("provider"))

        assert obj.getDataElementRef().getValue() == "/AUTOSAR/DataElement1"
        assert obj.getDataProvider().getValue() == "provider"

        obj.setDataElementRef(None)
        obj.setDataProvider(None)
        assert obj.getDataElementRef().getValue() == "/AUTOSAR/DataElement1"  # None is a no-op
        assert obj.getDataProvider().getValue() == "provider"  # None is a no-op

    def test_create_diagnosticDemProvidedDataMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticDemProvidedDataMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticDemProvidedDataMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticDemProvidedDataMapping) is element

        duplicate = package.createDiagnosticDemProvidedDataMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticMasterToSlaveEventMapping:
    """
    Test class for DiagnosticMasterToSlaveEventMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.29, p.256
    """

    CLASS_NOTE = "This meta-class provides the ability to map a master diagnostic event with a slave diagnostic event such that reporting of the master event with a given value also reports the slave event with the same value Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticMasterToSlaveEventMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticMasterToSlaveEventMapping(ar_root, "TestMasterToSlaveEventMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticMasterToSlaveEventMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMasterToSlaveEventMapping"
        assert obj.getMasterEventRef() is None
        assert obj.getSlaveEventRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticMasterToSlaveEventMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMasterToSlaveEventMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setMasterEventRef(RefType().setValue("/AUTOSAR/MasterEvent1"))
        obj.setSlaveEventRef(RefType().setValue("/AUTOSAR/SlaveEvent1"))

        assert obj.getMasterEventRef().getValue() == "/AUTOSAR/MasterEvent1"
        assert obj.getSlaveEventRef().getValue() == "/AUTOSAR/SlaveEvent1"

        obj.setMasterEventRef(None)
        obj.setSlaveEventRef(None)
        assert obj.getMasterEventRef().getValue() == "/AUTOSAR/MasterEvent1"  # None is a no-op
        assert obj.getSlaveEventRef().getValue() == "/AUTOSAR/SlaveEvent1"  # None is a no-op

    def test_create_diagnosticMasterToSlaveEventMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticMasterToSlaveEventMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticMasterToSlaveEventMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticMasterToSlaveEventMapping) is element

        duplicate = package.createDiagnosticMasterToSlaveEventMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEventToSecurityEventMapping:
    """
    Test class for DiagnosticEventToSecurityEventMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.30, p.257
    """

    CLASS_NOTE = "This meta-class represents the ability to map a security event that is defined in the context of the Security Extract to a diagnostic event defined on the context of the DiagnosticExtract. Tags: atp.Status=candidate atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventToSecurityEventMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventToSecurityEventMapping(ar_root, "TestEventToSecurityEventMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventToSecurityEventMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventToSecurityEventMapping"
        assert obj.getDiagnosticEventRef() is None
        assert obj.getSecurityEventPropsRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventToSecurityEventMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventToSecurityEventMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        obj.setSecurityEventPropsRef(RefType().setValue("/AUTOSAR/SecurityEventProps1"))

        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert obj.getSecurityEventPropsRef().getValue() == "/AUTOSAR/SecurityEventProps1"

        obj.setDiagnosticEventRef(None)
        obj.setSecurityEventPropsRef(None)
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getSecurityEventPropsRef().getValue() == "/AUTOSAR/SecurityEventProps1"  # None is a no-op

    def test_create_diagnosticEventToSecurityEventMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventToSecurityEventMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventToSecurityEventMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventToSecurityEventMapping) is element

        duplicate = package.createDiagnosticEventToSecurityEventMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticInhibitSourceEventMapping:
    """
    Test class for DiagnosticInhibitSourceEventMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.33, p.261
    """

    CLASS_NOTE = "This meta-class represents the ability to map a DiagnosticFunctionInhibitSource directly to alternatively one DiagnosticEvent or one DiagnosticFimSummaryEvent. This model element shall be used if the approach via the alias events is not applicable, i.e. when diagnostic events defined by the Dem are already available at the time the Fim configuration within the diagnostic extract is created. Tags: atp.recommendedPackage=DiagnosticInhibitSourceEventMappings"

    def _make_obj(self) -> DiagnosticInhibitSourceEventMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticInhibitSourceEventMapping(ar_root, "TestInhibitSourceEventMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticInhibitSourceEventMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestInhibitSourceEventMapping"
        assert obj.getDiagnosticEventRef() is None
        assert obj.getEventGroupRef() is None
        assert obj.getInhibitionSourceRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticInhibitSourceEventMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticInhibitSourceEventMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        obj.setEventGroupRef(RefType().setValue("/AUTOSAR/EventGroup1"))
        obj.setInhibitionSourceRef(RefType().setValue("/AUTOSAR/InhibitionSource1"))

        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert obj.getEventGroupRef().getValue() == "/AUTOSAR/EventGroup1"
        assert obj.getInhibitionSourceRef().getValue() == "/AUTOSAR/InhibitionSource1"

        obj.setDiagnosticEventRef(None)
        obj.setEventGroupRef(None)
        obj.setInhibitionSourceRef(None)
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getEventGroupRef().getValue() == "/AUTOSAR/EventGroup1"  # None is a no-op
        assert obj.getInhibitionSourceRef().getValue() == "/AUTOSAR/InhibitionSource1"  # None is a no-op

    def test_create_diagnosticInhibitSourceEventMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticInhibitSourceEventMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticInhibitSourceEventMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticInhibitSourceEventMapping) is element

        duplicate = package.createDiagnosticInhibitSourceEventMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticFimAliasEventMapping:
    """
    Test class for DiagnosticFimAliasEventMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.34, p.262
    """

    CLASS_NOTE = 'This meta-class represents the ability to model the mapping of a DiagnosticEvent to a DiagnosticAliasEvent. By this means the "preliminary" modeling by way of a DiagnosticAliasEvent is further substantiated. Tags: atp.recommendedPackage=DiagnosticFimEventMappings'

    def _make_obj(self) -> DiagnosticFimAliasEventMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFimAliasEventMapping(ar_root, "TestFimAliasEventMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticFimAliasEventMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFimAliasEventMapping"
        assert obj.getActualEventRef() is None
        assert obj.getAliasEventRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticFimAliasEventMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFimAliasEventMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setActualEventRef(RefType().setValue("/AUTOSAR/ActualEvent1"))
        obj.setAliasEventRef(RefType().setValue("/AUTOSAR/AliasEvent1"))

        assert obj.getActualEventRef().getValue() == "/AUTOSAR/ActualEvent1"
        assert obj.getAliasEventRef().getValue() == "/AUTOSAR/AliasEvent1"

        obj.setActualEventRef(None)
        obj.setAliasEventRef(None)
        assert obj.getActualEventRef().getValue() == "/AUTOSAR/ActualEvent1"  # None is a no-op
        assert obj.getAliasEventRef().getValue() == "/AUTOSAR/AliasEvent1"  # None is a no-op

    def test_create_diagnosticFimAliasEventMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticFimAliasEventMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticFimAliasEventMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticFimAliasEventMapping) is element

        duplicate = package.createDiagnosticFimAliasEventMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticFimAliasEventGroup:
    """
    Test class for DiagnosticFimAliasEventGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.35, p.263
    """

    CLASS_NOTE = "This meta-class represents the ability to define an alias for a Fim summarized event. This alias can be used in early phases of the configuration process until a further refinement is possible. Tags: atp.recommendedPackage=DiagnosticFimAliasEventGroups"

    def _make_obj(self) -> DiagnosticFimAliasEventGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFimAliasEventGroup(ar_root, "TestFimAliasEventGroup")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticFimAliasEventGroup instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFimAliasEventGroup"
        assert obj.getGroupedAliasEventRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticFimAliasEventGroup.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFimAliasEventGroup.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.addGroupedAliasEventRef(RefType().setValue("/AUTOSAR/GroupedAliasEvent1"))

        assert obj.getGroupedAliasEventRefs()[0].getValue() == "/AUTOSAR/GroupedAliasEvent1"

        obj.addGroupedAliasEventRef(None)
        assert len(obj.getGroupedAliasEventRefs()) == 1  # None is a no-op

    def test_create_diagnosticFimAliasEventGroup(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticFimAliasEventGroup("M1")

        assert element is not None
        assert isinstance(element, DiagnosticFimAliasEventGroup)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticFimAliasEventGroup) is element

        duplicate = package.createDiagnosticFimAliasEventGroup("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticFimAliasEventGroupMapping:
    """
    Test class for DiagnosticFimAliasEventGroupMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.36, p.263
    """

    CLASS_NOTE = 'This meta-class represents the ability to map a DiagnosticFimEventGroup to a DiagnosticFimAliasEventGroup. By this means the "preliminary" modeling by way of a DiagnosticFimAliasEventGroup is further substantiated. Tags: atp.recommendedPackage=DiagnosticFimAliasEventGroupMappings'

    def _make_obj(self) -> DiagnosticFimAliasEventGroupMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFimAliasEventGroupMapping(ar_root, "TestFimAliasEventGroupMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticFimAliasEventGroupMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFimAliasEventGroupMapping"
        assert obj.getActualEventRef() is None
        assert obj.getAliasEventRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticFimAliasEventGroupMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFimAliasEventGroupMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setActualEventRef(RefType().setValue("/AUTOSAR/ActualEvent1"))
        obj.setAliasEventRef(RefType().setValue("/AUTOSAR/AliasEvent1"))

        assert obj.getActualEventRef().getValue() == "/AUTOSAR/ActualEvent1"
        assert obj.getAliasEventRef().getValue() == "/AUTOSAR/AliasEvent1"

        obj.setActualEventRef(None)
        obj.setAliasEventRef(None)
        assert obj.getActualEventRef().getValue() == "/AUTOSAR/ActualEvent1"  # None is a no-op
        assert obj.getAliasEventRef().getValue() == "/AUTOSAR/AliasEvent1"  # None is a no-op

    def test_create_diagnosticFimAliasEventGroupMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticFimAliasEventGroupMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticFimAliasEventGroupMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticFimAliasEventGroupMapping) is element

        duplicate = package.createDiagnosticFimAliasEventGroupMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEventToTroubleCodeJ1939Mapping:
    """
    Test class for DiagnosticEventToTroubleCodeJ1939Mapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.43, p.269
    """

    CLASS_NOTE = "By means of this meta-class it is possible to associate a DiagnosticEvent to a DiagnosticTroubleCodeJ1939. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEventToTroubleCodeJ1939Mapping(ar_root, "TestEventToTroubleCodeJ1939Mapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticEventToTroubleCodeJ1939Mapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEventToTroubleCodeJ1939Mapping"
        assert obj.getDiagnosticEventRef() is None
        assert obj.getTroubleCodeJ1939Ref() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticEventToTroubleCodeJ1939Mapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventToTroubleCodeJ1939Mapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        obj.setTroubleCodeJ1939Ref(RefType().setValue("/AUTOSAR/TroubleCodeJ19391"))

        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert obj.getTroubleCodeJ1939Ref().getValue() == "/AUTOSAR/TroubleCodeJ19391"

        obj.setDiagnosticEventRef(None)
        obj.setTroubleCodeJ1939Ref(None)
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op
        assert obj.getTroubleCodeJ1939Ref().getValue() == "/AUTOSAR/TroubleCodeJ19391"  # None is a no-op

    def test_create_diagnosticEventToTroubleCodeJ1939Mapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticEventToTroubleCodeJ1939Mapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticEventToTroubleCodeJ1939Mapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticEventToTroubleCodeJ1939Mapping) is element

        duplicate = package.createDiagnosticEventToTroubleCodeJ1939Mapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticIumprToFunctionIdentifierMapping:
    """
    Test class for DiagnosticIumprToFunctionIdentifierMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.39, p.265
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a DiagnosticFunctionIdentifier with a DiagnosticIumpr. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticIumprToFunctionIdentifierMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticIumprToFunctionIdentifierMapping(ar_root, "TestIumprToFunctionIdentifierMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticIumprToFunctionIdentifierMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestIumprToFunctionIdentifierMapping"
        assert obj.getFunctionIdentifierRef() is None
        assert obj.getIumprRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticIumprToFunctionIdentifierMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticIumprToFunctionIdentifierMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setFunctionIdentifierRef(RefType().setValue("/AUTOSAR/FunctionIdentifier1"))
        obj.setIumprRef(RefType().setValue("/AUTOSAR/Iumpr1"))

        assert obj.getFunctionIdentifierRef().getValue() == "/AUTOSAR/FunctionIdentifier1"
        assert obj.getIumprRef().getValue() == "/AUTOSAR/Iumpr1"

        obj.setFunctionIdentifierRef(None)
        obj.setIumprRef(None)
        assert obj.getFunctionIdentifierRef().getValue() == "/AUTOSAR/FunctionIdentifier1"  # None is a no-op
        assert obj.getIumprRef().getValue() == "/AUTOSAR/Iumpr1"  # None is a no-op

    def test_create_diagnosticIumprToFunctionIdentifierMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticIumprToFunctionIdentifierMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticIumprToFunctionIdentifierMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticIumprToFunctionIdentifierMapping) is element

        duplicate = package.createDiagnosticIumprToFunctionIdentifierMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticJ1939SpnMapping:
    """
    Test class for DiagnosticJ1939SpnMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.40, p.267
    """

    CLASS_NOTE = "This meta-class represents the ability to define a mapping between an SPN and a SystemSignal. The existence of a mapping means that neither the SPN nor the SystemSignal need to be updated if the relation between the two changes. Tags: atp.recommendedPackage=DiagnosticJ1939SpnMappings"

    def _make_obj(self) -> DiagnosticJ1939SpnMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticJ1939SpnMapping(ar_root, "TestJ1939SpnMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticJ1939SpnMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestJ1939SpnMapping"
        assert obj.getSendingNodeRefs() == []
        assert obj.getSpnRef() is None
        assert obj.getSystemSignalRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticJ1939SpnMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticJ1939SpnMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.addSendingNodeRef(RefType().setValue("/AUTOSAR/SendingNode1"))
        obj.setSpnRef(RefType().setValue("/AUTOSAR/Spn1"))
        obj.setSystemSignalRef(RefType().setValue("/AUTOSAR/SystemSignal1"))

        assert obj.getSendingNodeRefs()[0].getValue() == "/AUTOSAR/SendingNode1"
        assert obj.getSpnRef().getValue() == "/AUTOSAR/Spn1"
        assert obj.getSystemSignalRef().getValue() == "/AUTOSAR/SystemSignal1"

        obj.addSendingNodeRef(None)
        obj.setSpnRef(None)
        obj.setSystemSignalRef(None)
        assert len(obj.getSendingNodeRefs()) == 1  # None is a no-op
        assert obj.getSpnRef().getValue() == "/AUTOSAR/Spn1"  # None is a no-op
        assert obj.getSystemSignalRef().getValue() == "/AUTOSAR/SystemSignal1"  # None is a no-op

    def test_create_diagnosticJ1939SpnMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticJ1939SpnMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticJ1939SpnMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticJ1939SpnMapping) is element

        duplicate = package.createDiagnosticJ1939SpnMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticJ1939Node:
    """
    Test class for DiagnosticJ1939Node functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.41, p.267
    """

    CLASS_NOTE = 'This meta-class represents the diagnostic configuration of a J1939 Nm node, which in turn represents a "virtual Ecu" on the J1939 communication bus. Tags: atp.recommendedPackage=DiagnosticJ1939Nodes'

    def _make_obj(self) -> DiagnosticJ1939Node:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticJ1939Node(ar_root, "TestJ1939Node")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticJ1939Node instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestJ1939Node"
        assert obj.getNmNodeRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticJ1939Node.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticJ1939Node.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setNmNodeRef(RefType().setValue("/AUTOSAR/NmNode1"))

        assert obj.getNmNodeRef().getValue() == "/AUTOSAR/NmNode1"

        obj.setNmNodeRef(None)
        assert obj.getNmNodeRef().getValue() == "/AUTOSAR/NmNode1"  # None is a no-op

    def test_create_diagnosticJ1939Node(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticJ1939Node("M1")

        assert element is not None
        assert isinstance(element, DiagnosticJ1939Node)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticJ1939Node) is element

        duplicate = package.createDiagnosticJ1939Node("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticJ1939SwMapping:
    """
    Test class for DiagnosticJ1939SwMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.42, p.268
    """

    CLASS_NOTE = "This meta-class represents the ability to map a piece of application software to a J1939DiagnosticNode. By this means the diagnostic configuration can be associated with the application software. Tags: atp.recommendedPackage=DiagnosticJ1939SwMappings"

    def _make_obj(self) -> DiagnosticJ1939SwMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticJ1939SwMapping(ar_root, "TestJ1939SwMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticJ1939SwMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestJ1939SwMapping"
        assert obj.getNodeRef() is None
        assert obj.getSwComponentPrototypeRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticJ1939SwMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticJ1939SwMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setNodeRef(RefType().setValue("/AUTOSAR/Node1"))
        obj.setSwComponentPrototypeRef(RefType().setValue("/AUTOSAR/SwComponentPrototype1"))

        assert obj.getNodeRef().getValue() == "/AUTOSAR/Node1"
        assert obj.getSwComponentPrototypeRef().getValue() == "/AUTOSAR/SwComponentPrototype1"

        obj.setNodeRef(None)
        obj.setSwComponentPrototypeRef(None)
        assert obj.getNodeRef().getValue() == "/AUTOSAR/Node1"  # None is a no-op
        assert obj.getSwComponentPrototypeRef().getValue() == "/AUTOSAR/SwComponentPrototype1"  # None is a no-op

    def test_create_diagnosticJ1939SwMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticJ1939SwMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticJ1939SwMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticJ1939SwMapping) is element

        duplicate = package.createDiagnosticJ1939SwMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticFimFunctionMapping:
    """
    Test class for DiagnosticFimFunctionMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.37, p.265
    """

    CLASS_NOTE = "This meta-class represents the ability to define a mapping between a function identifier (FID) and the corresponding SwcServiceDependency in the application software resp. basic software. Tags: atp.recommendedPackage=DiagnosticFimFunctionMappings"

    def _make_obj(self) -> DiagnosticFimFunctionMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFimFunctionMapping(ar_root, "TestFimFunctionMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticFimFunctionMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFimFunctionMapping"
        assert obj.getMappedBswServiceDependencyRef() is None
        assert obj.getMappedFlatSwcServiceDependencyRef() is None
        assert obj.getMappedFunctionRef() is None
        assert obj.getMappedSwcServiceDependencyRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticFimFunctionMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFimFunctionMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setMappedBswServiceDependencyRef(RefType().setValue("/AUTOSAR/MappedBswServiceDependency1"))
        obj.setMappedFlatSwcServiceDependencyRef(RefType().setValue("/AUTOSAR/MappedFlatSwcServiceDependency1"))
        obj.setMappedFunctionRef(RefType().setValue("/AUTOSAR/MappedFunction1"))
        obj.setMappedSwcServiceDependencyRef(RefType().setValue("/AUTOSAR/MappedSwcServiceDependency1"))

        assert obj.getMappedBswServiceDependencyRef().getValue() == "/AUTOSAR/MappedBswServiceDependency1"
        assert obj.getMappedFlatSwcServiceDependencyRef().getValue() == "/AUTOSAR/MappedFlatSwcServiceDependency1"
        assert obj.getMappedFunctionRef().getValue() == "/AUTOSAR/MappedFunction1"
        assert obj.getMappedSwcServiceDependencyRef().getValue() == "/AUTOSAR/MappedSwcServiceDependency1"

        obj.setMappedBswServiceDependencyRef(None)
        obj.setMappedFlatSwcServiceDependencyRef(None)
        obj.setMappedFunctionRef(None)
        obj.setMappedSwcServiceDependencyRef(None)
        assert obj.getMappedBswServiceDependencyRef().getValue() == "/AUTOSAR/MappedBswServiceDependency1"  # None is a no-op
        assert obj.getMappedFlatSwcServiceDependencyRef().getValue() == "/AUTOSAR/MappedFlatSwcServiceDependency1"  # None is a no-op
        assert obj.getMappedFunctionRef().getValue() == "/AUTOSAR/MappedFunction1"  # None is a no-op
        assert obj.getMappedSwcServiceDependencyRef().getValue() == "/AUTOSAR/MappedSwcServiceDependency1"  # None is a no-op

    def test_create_diagnosticFimFunctionMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticFimFunctionMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticFimFunctionMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticFimFunctionMapping) is element

        duplicate = package.createDiagnosticFimFunctionMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestCpSwClusterToDiagEventMapping:
    """
    Test class for CpSwClusterToDiagEventMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.46, p.272
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a CpSoftwareClusterResource with a DiagnosticEvent. This allows for indicating that the CpSoftwareClusterResource is used to convey the reporting or status query of the mapped DiagnosticEvent. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"

    def _make_obj(self) -> CpSwClusterToDiagEventMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return CpSwClusterToDiagEventMapping(ar_root, "TestCpSwClusterToDiagEventMapping")

    def test_is_concrete(self):
        """
        Test that a concrete CpSwClusterToDiagEventMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestCpSwClusterToDiagEventMapping"
        assert obj.getCpSoftwareClusterResourceRef() is None
        assert obj.getDiagnosticEventRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert CpSwClusterToDiagEventMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSwClusterToDiagEventMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        obj.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))

        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"

        obj.setCpSoftwareClusterResourceRef(None)
        obj.setDiagnosticEventRef(None)
        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"  # None is a no-op
        assert obj.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"  # None is a no-op

    def test_create_cpSwClusterToDiagEventMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createCpSwClusterToDiagEventMapping("M1")

        assert element is not None
        assert isinstance(element, CpSwClusterToDiagEventMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", CpSwClusterToDiagEventMapping) is element

        duplicate = package.createCpSwClusterToDiagEventMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestCpSwClusterResourceToDiagDataElemMapping:
    """
    Test class for CpSwClusterResourceToDiagDataElemMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.47, p.273
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a CpSoftwareClusterResource with a DiagnosticDataElement. This allows for indicating that the CpSoftwareClusterResource is used to convey the DiagnosticDataElement. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"

    def _make_obj(self) -> CpSwClusterResourceToDiagDataElemMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return CpSwClusterResourceToDiagDataElemMapping(ar_root, "TestCpSwClusterResourceToDiagDataElemMapping")

    def test_is_concrete(self):
        """
        Test that a concrete CpSwClusterResourceToDiagDataElemMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestCpSwClusterResourceToDiagDataElemMapping"
        assert obj.getCpSoftwareClusterResourceRef() is None
        assert obj.getDiagnosticDataElementRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert CpSwClusterResourceToDiagDataElemMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSwClusterResourceToDiagDataElemMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        obj.setDiagnosticDataElementRef(RefType().setValue("/AUTOSAR/DiagnosticDataElement1"))

        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"
        assert obj.getDiagnosticDataElementRef().getValue() == "/AUTOSAR/DiagnosticDataElement1"

        obj.setCpSoftwareClusterResourceRef(None)
        obj.setDiagnosticDataElementRef(None)
        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"  # None is a no-op
        assert obj.getDiagnosticDataElementRef().getValue() == "/AUTOSAR/DiagnosticDataElement1"  # None is a no-op

    def test_create_cpSwClusterResourceToDiagDataElemMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createCpSwClusterResourceToDiagDataElemMapping("M1")

        assert element is not None
        assert isinstance(element, CpSwClusterResourceToDiagDataElemMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", CpSwClusterResourceToDiagDataElemMapping) is element

        duplicate = package.createCpSwClusterResourceToDiagDataElemMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestCpSwClusterToDiagRoutineSubfunctionMapping:
    """
    Test class for CpSwClusterToDiagRoutineSubfunctionMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.48, p.274
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a CpSoftwareClusterResource with a subfunction of a DiagnosticRoutine. This allows for indicating that the CpSoftwareClusterResource is used to convey the calling or result return of the mapped DiagnosticRoutine. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"

    def _make_obj(self) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return CpSwClusterToDiagRoutineSubfunctionMapping(ar_root, "TestCpSwClusterToDiagRoutineSubfunctionMapping")

    def test_is_concrete(self):
        """
        Test that a concrete CpSwClusterToDiagRoutineSubfunctionMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestCpSwClusterToDiagRoutineSubfunctionMapping"
        assert obj.getCpSoftwareClusterResourceRef() is None
        assert obj.getRoutineSubfunctionRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert CpSwClusterToDiagRoutineSubfunctionMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSwClusterToDiagRoutineSubfunctionMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        obj.setRoutineSubfunctionRef(RefType().setValue("/AUTOSAR/RoutineSubfunction1"))

        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"
        assert obj.getRoutineSubfunctionRef().getValue() == "/AUTOSAR/RoutineSubfunction1"

        obj.setCpSoftwareClusterResourceRef(None)
        obj.setRoutineSubfunctionRef(None)
        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"  # None is a no-op
        assert obj.getRoutineSubfunctionRef().getValue() == "/AUTOSAR/RoutineSubfunction1"  # None is a no-op

    def test_create_cpSwClusterToDiagRoutineSubfunctionMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createCpSwClusterToDiagRoutineSubfunctionMapping("M1")

        assert element is not None
        assert isinstance(element, CpSwClusterToDiagRoutineSubfunctionMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", CpSwClusterToDiagRoutineSubfunctionMapping) is element

        duplicate = package.createCpSwClusterToDiagRoutineSubfunctionMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestCpSwClusterResourceToDiagFunctionIdMapping:
    """
    Test class for CpSwClusterResourceToDiagFunctionIdMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.49, p.275
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a CpSoftwareClusterResource with a subfunction of a DiagnosticFunctionIdentifier. This allows for indicating that the CpSoftwareClusterResource is used to convey the execution permission associated with the mapped function identifier. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"

    def _make_obj(self) -> CpSwClusterResourceToDiagFunctionIdMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return CpSwClusterResourceToDiagFunctionIdMapping(ar_root, "TestCpSwClusterResourceToDiagFunctionIdMapping")

    def test_is_concrete(self):
        """
        Test that a concrete CpSwClusterResourceToDiagFunctionIdMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestCpSwClusterResourceToDiagFunctionIdMapping"
        assert obj.getCpSoftwareClusterResourceRef() is None
        assert obj.getFunctionIdentifierRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert CpSwClusterResourceToDiagFunctionIdMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSwClusterResourceToDiagFunctionIdMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        obj.setFunctionIdentifierRef(RefType().setValue("/AUTOSAR/FunctionIdentifier1"))

        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"
        assert obj.getFunctionIdentifierRef().getValue() == "/AUTOSAR/FunctionIdentifier1"

        obj.setCpSoftwareClusterResourceRef(None)
        obj.setFunctionIdentifierRef(None)
        assert obj.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"  # None is a no-op
        assert obj.getFunctionIdentifierRef().getValue() == "/AUTOSAR/FunctionIdentifier1"  # None is a no-op

    def test_create_cpSwClusterResourceToDiagFunctionIdMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createCpSwClusterResourceToDiagFunctionIdMapping("M1")

        assert element is not None
        assert isinstance(element, CpSwClusterResourceToDiagFunctionIdMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", CpSwClusterResourceToDiagFunctionIdMapping) is element

        duplicate = package.createCpSwClusterResourceToDiagFunctionIdMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
    """
    Test class for DiagnosticTroubleCodeUdsToTroubleCodeObdMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.180, p.188
    """

    CLASS_NOTE = "This meta-class represents the ability to associate a UDS trouble code to an OBD trouble code. Tags: atp.recommendedPackage=DiagnosticMappings"

    def _make_obj(self) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(ar_root, "TestTroubleCodeUdsToTroubleCodeObdMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticTroubleCodeUdsToTroubleCodeObdMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestTroubleCodeUdsToTroubleCodeObdMapping"
        assert obj.getTroubleCodeObdRef() is None
        assert obj.getTroubleCodeUdsRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticTroubleCodeUdsToTroubleCodeObdMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTroubleCodeUdsToTroubleCodeObdMapping.__init__.__doc__ is None

    def test_get_set_members(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        obj.setTroubleCodeObdRef(RefType().setValue("/AUTOSAR/TroubleCodeObd1"))
        obj.setTroubleCodeUdsRef(RefType().setValue("/AUTOSAR/TroubleCodeUds1"))

        assert obj.getTroubleCodeObdRef().getValue() == "/AUTOSAR/TroubleCodeObd1"
        assert obj.getTroubleCodeUdsRef().getValue() == "/AUTOSAR/TroubleCodeUds1"

        obj.setTroubleCodeObdRef(None)
        obj.setTroubleCodeUdsRef(None)
        assert obj.getTroubleCodeObdRef().getValue() == "/AUTOSAR/TroubleCodeObd1"  # None is a no-op
        assert obj.getTroubleCodeUdsRef().getValue() == "/AUTOSAR/TroubleCodeUds1"  # None is a no-op

    def test_create_diagnosticTroubleCodeUdsToTroubleCodeObdMapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        element = package.createDiagnosticTroubleCodeUdsToTroubleCodeObdMapping("M1")

        assert element is not None
        assert isinstance(element, DiagnosticTroubleCodeUdsToTroubleCodeObdMapping)
        assert element.getShortName() == "M1"
        assert package.getReferrableElement("M1", DiagnosticTroubleCodeUdsToTroubleCodeObdMapping) is element

        duplicate = package.createDiagnosticTroubleCodeUdsToTroubleCodeObdMapping("M1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticServiceSwMapping:
    """
    Test class for DiagnosticServiceSwMapping functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.15, p.239
    """

    CLASS_NOTE = "This represents the ability to define a mapping of a diagnostic service to a software-component or a basic-software module. If the former is used then this kind of service mapping is applicable for the usage of ClientServerInterfaces. Tags: atp.recommendedPackage=DiagnosticServiceMappings"

    def _make_obj(self) -> DiagnosticServiceSwMapping:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticServiceSwMapping(ar_root, "TestServiceSwMapping")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticServiceSwMapping instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestServiceSwMapping"
        assert obj.getAccessedDataPrototypeIRef() is None
        assert obj.getDiagnosticDataElementRef() is None
        assert obj.getDiagnosticParameterRef() is None
        assert obj.getMappedBswServiceDependencyRef() is None
        assert obj.getMappedFlatSwcServiceDependencyRef() is None
        assert obj.getMappedSwcServiceDependencyInSystemIRef() is None
        assert obj.getParameterElementAccess() is None
        assert obj.getServiceInstanceRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticServiceSwMapping.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticServiceSwMapping.__init__.__doc__ is None

    def test_get_set_refs_and_aggregation(self):
        """
        Round-trips the references and the parameterElementAccess aggregation; None is a no-op.
        """
        obj = self._make_obj()

        iref1 = RefType().setValue("/AUTOSAR/Interfaces/Op1")
        data_ref = RefType().setValue("/AUTOSAR/DataElements/Did1")
        param_ref = RefType().setValue("/AUTOSAR/ParamIdents/Ident1")
        bsw_ref = RefType().setValue("/AUTOSAR/BswDeps/Dep1")
        flat_ref = RefType().setValue("/AUTOSAR/SwcDeps/Dep2")
        iref2 = RefType().setValue("/AUTOSAR/System/SwcDep3")
        pea = DiagnosticParameterElementAccess()
        si_ref = RefType().setValue("/AUTOSAR/Services/Svc1")

        obj.setAccessedDataPrototypeIRef(iref1)
        obj.setDiagnosticDataElementRef(data_ref)
        obj.setDiagnosticParameterRef(param_ref)
        obj.setMappedBswServiceDependencyRef(bsw_ref)
        obj.setMappedFlatSwcServiceDependencyRef(flat_ref)
        obj.setMappedSwcServiceDependencyInSystemIRef(iref2)
        obj.setParameterElementAccess(pea)
        obj.setServiceInstanceRef(si_ref)

        assert obj.getAccessedDataPrototypeIRef() is iref1
        assert obj.getDiagnosticDataElementRef() is data_ref
        assert obj.getDiagnosticParameterRef() is param_ref
        assert obj.getMappedBswServiceDependencyRef() is bsw_ref
        assert obj.getMappedFlatSwcServiceDependencyRef() is flat_ref
        assert obj.getMappedSwcServiceDependencyInSystemIRef() is iref2
        assert obj.getParameterElementAccess() is pea
        assert obj.getServiceInstanceRef() is si_ref

        obj.setAccessedDataPrototypeIRef(None)
        obj.setDiagnosticDataElementRef(None)
        obj.setDiagnosticParameterRef(None)
        obj.setMappedBswServiceDependencyRef(None)
        obj.setMappedFlatSwcServiceDependencyRef(None)
        obj.setMappedSwcServiceDependencyInSystemIRef(None)
        obj.setParameterElementAccess(None)
        obj.setServiceInstanceRef(None)

        assert obj.getAccessedDataPrototypeIRef() is iref1  # None is a no-op
        assert obj.getDiagnosticDataElementRef() is data_ref  # None is a no-op
        assert obj.getDiagnosticParameterRef() is param_ref  # None is a no-op
        assert obj.getMappedBswServiceDependencyRef() is bsw_ref  # None is a no-op
        assert obj.getMappedFlatSwcServiceDependencyRef() is flat_ref  # None is a no-op
        assert obj.getMappedSwcServiceDependencyInSystemIRef() is iref2  # None is a no-op
        assert obj.getParameterElementAccess() is pea  # None is a no-op
        assert obj.getServiceInstanceRef() is si_ref  # None is a no-op

    def test_create_diagnostic_service_sw_mapping(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticServiceMappings")
        element = package.createDiagnosticServiceSwMapping("Mapping1")

        assert element is not None
        assert isinstance(element, DiagnosticServiceSwMapping)
        assert element.getShortName() == "Mapping1"
        assert package.getReferrableElement("Mapping1", DiagnosticServiceSwMapping) is element

        duplicate = package.createDiagnosticServiceSwMapping("Mapping1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticControlDTCSetting:
    """
    Test class for DiagnosticControlDTCSetting functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.68, p.111
    """

    CLASS_NOTE = 'This represents an instance of the "Control DTC Setting" diagnostic service.'
    DTC_SETTING_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. "
        "Thereby, the reference represents the ability to access shared attributes among all DiagnosticControlDTCSetting in the given context."
    )

    def _make_obj(self) -> DiagnosticControlDTCSetting:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticControlDTCSetting(ar_root, "TestControlDTCSetting")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticControlDTCSetting instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestControlDTCSetting"
        assert obj.getDtcSettingClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticControlDTCSetting.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticControlDTCSetting.__init__.__doc__ is None

    def test_get_set_dtc_setting_class(self):
        """
        Round-trips the dtcSettingClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass")
        result = obj.setDtcSettingClass(ref)
        assert result is obj  # method chaining
        assert obj.getDtcSettingClass() is ref
        assert obj.getDtcSettingClass().getValue() == "/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass"
        assert obj.getDtcSettingClass().getDest() == "DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS"

        result = obj.setDtcSettingClass(None)
        assert result is obj  # method chaining with None
        assert obj.getDtcSettingClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticControlDTCSetting.getDtcSettingClass.__doc__) == self.DTC_SETTING_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticControlDTCSetting.setDtcSettingClass.__doc__) == (
            self.DTC_SETTING_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dtcSettingClass."
        )

    def test_create_diagnostic_control_dtc_setting(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        control_dtc_setting = package.createDiagnosticControlDTCSetting("ControlDTCSetting1")

        assert control_dtc_setting is not None
        assert isinstance(control_dtc_setting, DiagnosticControlDTCSetting)
        assert control_dtc_setting.getShortName() == "ControlDTCSetting1"
        assert package.getReferrableElement("ControlDTCSetting1", DiagnosticControlDTCSetting) is control_dtc_setting

        duplicate = package.createDiagnosticControlDTCSetting("ControlDTCSetting1")
        assert duplicate is control_dtc_setting


class TestDiagnosticDataByIdentifier:
    """
    Test class for DiagnosticDataByIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.73, p.113
    (abstract base; exercised through the concrete subclass DiagnosticReadDataByIdentifier)
    """

    CLASS_NOTE = "This represents an abstract base class for all diagnostic services that access data by identifier."
    DATA_IDENTIFIER_NOTE = "This represents the linked DiagnosticDataIdentifier."

    def _make_obj(self) -> DiagnosticReadDataByIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticReadDataByIdentifier(ar_root, "TestReadDataByIdentifier")

    def test_initialization(self):
        """
        Test that the abstract DiagnosticDataByIdentifier is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestReadDataByIdentifier"
        assert isinstance(obj, DiagnosticDataByIdentifier)
        assert isinstance(obj, ARElement)
        assert obj.getDataIdentifier() is None

    def test_abstract_instantiation_raises(self):
        """
        Test that the abstract DiagnosticDataByIdentifier cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticDataByIdentifier(AUTOSAR.getInstance(), "DirectInstance")

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticDataByIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticDataByIdentifier.__init__.__doc__ is None

    def test_get_set_data_identifier(self):
        """
        Round-trips the dataIdentifier ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-DATA-IDENTIFIER")
        ref.setValue("/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID")
        result = obj.setDataIdentifier(ref)
        assert result is obj  # method chaining
        assert obj.getDataIdentifier() is ref
        assert obj.getDataIdentifier().getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert obj.getDataIdentifier().getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"

        result = obj.setDataIdentifier(None)
        assert result is obj  # method chaining with None
        assert obj.getDataIdentifier() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticDataByIdentifier.getDataIdentifier.__doc__) == self.DATA_IDENTIFIER_NOTE
        assert inspect.cleandoc(DiagnosticDataByIdentifier.setDataIdentifier.__doc__) == (self.DATA_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataIdentifier.")


class TestDiagnosticReadDataByIdentifier:
    """
    Test class for DiagnosticReadDataByIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.70, p.112
    """

    CLASS_NOTE = 'This represents an instance of the "Read Data by Identifier" diagnostic service.'
    READ_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByIdentifier in the given context."
    )

    def _make_obj(self) -> DiagnosticReadDataByIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticReadDataByIdentifier(ar_root, "TestReadDataByIdentifier")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticReadDataByIdentifier instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestReadDataByIdentifier"
        assert isinstance(obj, DiagnosticDataByIdentifier)
        assert isinstance(obj, ARElement)
        assert obj.getDataIdentifier() is None
        assert obj.getReadClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticReadDataByIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticReadDataByIdentifier.__init__.__doc__ is None

    def test_get_set_read_class(self):
        """
        Round-trips the readClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass")
        result = obj.setReadClass(ref)
        assert result is obj  # method chaining
        assert obj.getReadClass() is ref
        assert obj.getReadClass().getValue() == "/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass"
        assert obj.getReadClass().getDest() == "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS"

        result = obj.setReadClass(None)
        assert result is obj  # method chaining with None
        assert obj.getReadClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticReadDataByIdentifier.getReadClass.__doc__) == self.READ_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticReadDataByIdentifier.setReadClass.__doc__) == (self.READ_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing readClass.")

    def test_create_diagnostic_read_data_by_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifiers")
        read_did = package.createDiagnosticReadDataByIdentifier("ReadDataByIdentifier1")

        assert read_did is not None
        assert isinstance(read_did, DiagnosticReadDataByIdentifier)
        assert read_did.getShortName() == "ReadDataByIdentifier1"
        assert package.getReferrableElement("ReadDataByIdentifier1", DiagnosticReadDataByIdentifier) is read_did

        duplicate = package.createDiagnosticReadDataByIdentifier("ReadDataByIdentifier1")
        assert duplicate is read_did  # duplicate short name returns the existing element


class TestDiagnosticWriteDataByIdentifier:
    """
    Test class for DiagnosticWriteDataByIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.71, p.113
    """

    CLASS_NOTE = 'This represents an instance of the "Write Data by Identifier" diagnostic service.'
    WRITE_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticWriteDataByIdentifier in the given context."
    )

    def _make_obj(self) -> DiagnosticWriteDataByIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticWriteDataByIdentifier(ar_root, "TestWriteDataByIdentifier")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticWriteDataByIdentifier instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestWriteDataByIdentifier"
        assert isinstance(obj, DiagnosticDataByIdentifier)
        assert isinstance(obj, ARElement)
        assert obj.getDataIdentifier() is None
        assert obj.getWriteClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticWriteDataByIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticWriteDataByIdentifier.__init__.__doc__ is None

    def test_get_set_write_class(self):
        """
        Round-trips the writeClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass")
        result = obj.setWriteClass(ref)
        assert result is obj  # method chaining
        assert obj.getWriteClass() is ref
        assert obj.getWriteClass().getValue() == "/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass"
        assert obj.getWriteClass().getDest() == "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS"

        result = obj.setWriteClass(None)
        assert result is obj  # method chaining with None
        assert obj.getWriteClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticWriteDataByIdentifier.getWriteClass.__doc__) == self.WRITE_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticWriteDataByIdentifier.setWriteClass.__doc__) == (self.WRITE_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing writeClass.")

    def test_create_diagnostic_write_data_by_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteDataByIdentifiers")
        write_did = package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")

        assert write_did is not None
        assert isinstance(write_did, DiagnosticWriteDataByIdentifier)
        assert write_did.getShortName() == "WriteDataByIdentifier1"
        assert package.getReferrableElement("WriteDataByIdentifier1", DiagnosticWriteDataByIdentifier) is write_did

        duplicate = package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")
        assert duplicate is write_did  # duplicate short name returns the existing element


class TestDiagnosticReadScalingDataByIdentifier:
    """
    Test class for DiagnosticReadScalingDataByIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.78, p.116
    """

    CLASS_NOTE = 'This represents an instance of the "Read Scaling Data by Identifier" diagnostic service.'
    READ_SCALING_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadScalingDataByIdentifier in the given context."
    )

    def _make_obj(self) -> DiagnosticReadScalingDataByIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticReadScalingDataByIdentifier(ar_root, "TestReadScalingDataByIdentifier")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticReadScalingDataByIdentifier instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestReadScalingDataByIdentifier"
        assert isinstance(obj, DiagnosticDataByIdentifier)
        assert isinstance(obj, ARElement)
        assert obj.getDataIdentifier() is None
        assert obj.getReadScalingDataClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticReadScalingDataByIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticReadScalingDataByIdentifier.__init__.__doc__ is None

    def test_get_set_read_scaling_data_class(self):
        """
        Round-trips the readScalingDataClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass")
        result = obj.setReadScalingDataClass(ref)
        assert result is obj  # method chaining
        assert obj.getReadScalingDataClass() is ref
        assert obj.getReadScalingDataClass().getValue() == "/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass"
        assert obj.getReadScalingDataClass().getDest() == "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS"

        result = obj.setReadScalingDataClass(None)
        assert result is obj  # method chaining with None
        assert obj.getReadScalingDataClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticReadScalingDataByIdentifier.getReadScalingDataClass.__doc__) == self.READ_SCALING_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticReadScalingDataByIdentifier.setReadScalingDataClass.__doc__) == (
            self.READ_SCALING_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing readScalingDataClass."
        )

    def test_create_diagnostic_read_scaling_data_by_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadScalingDataByIdentifiers")
        read_scaling = package.createDiagnosticReadScalingDataByIdentifier("ReadScalingDataByIdentifier1")

        assert read_scaling is not None
        assert isinstance(read_scaling, DiagnosticReadScalingDataByIdentifier)
        assert read_scaling.getShortName() == "ReadScalingDataByIdentifier1"
        assert package.getReferrableElement("ReadScalingDataByIdentifier1", DiagnosticReadScalingDataByIdentifier) is read_scaling

        duplicate = package.createDiagnosticReadScalingDataByIdentifier("ReadScalingDataByIdentifier1")
        assert duplicate is read_scaling  # duplicate short name returns the existing element


class TestDiagnosticIOControl:
    """
    Test class for DiagnosticIOControl functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.80, p.118
    """

    CLASS_NOTE = 'This represents an instance of the "I/O Control" diagnostic service.'
    CONTROL_ENABLE_MASK_BIT_NOTE = "This aggregation represents the control mask record consisting of single bits."
    DATA_IDENTIFIER_NOTE = "This represents the corresponding DiagnosticData Identifier"
    FREEZE_CURRENT_STATE_NOTE = "Setting this attribute to true represents the ability of the Dcm to execute a freezeCurrentState."
    IO_CONTROL_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticIOControl in the given context."
    )
    RESET_TO_DEFAULT_NOTE = "Setting this attribute to true represents the ability of the Dcm to execute a resetToDefault."
    SHORT_TERM_ADJUSTMENT_NOTE = "Setting this attribute to true represents the ability of the Dcm to execute a shortTermAdjustment."

    def _make_obj(self) -> DiagnosticIOControl:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticIOControl(ar_root, "TestIOControl")

    def _ref(self, dest: str, value: str) -> RefType:
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticIOControl instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestIOControl"
        assert isinstance(obj, ARElement)
        assert obj.getControlEnableMaskBits() == []
        assert obj.getDataIdentifier() is None
        assert obj.getFreezeCurrentState() is None
        assert obj.getIoControlClass() is None
        assert obj.getResetToDefault() is None
        assert obj.getShortTermAdjustment() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticIOControl.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticIOControl.__init__.__doc__ is None

    def test_add_control_enable_mask_bit(self):
        """
        Test addControlEnableMaskBit append and None no-op.
        """
        obj = self._make_obj()

        mask_bit = DiagnosticControlEnableMaskBit()
        result = obj.addControlEnableMaskBit(mask_bit)
        assert result is obj  # method chaining
        assert obj.getControlEnableMaskBits() == [mask_bit]

        result = obj.addControlEnableMaskBit(None)
        assert result is obj  # method chaining with None
        assert obj.getControlEnableMaskBits() == [mask_bit]  # None is a no-op

    def test_get_set_data_identifier(self):
        """
        Round-trips the dataIdentifier ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = self._ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID")
        result = obj.setDataIdentifier(ref)
        assert result is obj  # method chaining
        assert obj.getDataIdentifier() is ref
        assert obj.getDataIdentifier().getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert obj.getDataIdentifier().getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"

        result = obj.setDataIdentifier(None)
        assert result is obj  # method chaining with None
        assert obj.getDataIdentifier() is ref  # None is a no-op

    def test_get_set_freeze_current_state(self):
        """
        Round-trips the freezeCurrentState boolean; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean()
        value.setValue("true")
        result = obj.setFreezeCurrentState(value)
        assert result is obj  # method chaining
        assert obj.getFreezeCurrentState() is value
        assert obj.getFreezeCurrentState().getValue() is True

        result = obj.setFreezeCurrentState(None)
        assert result is obj  # method chaining with None
        assert obj.getFreezeCurrentState() is value  # None is a no-op

    def test_get_set_io_control_class(self):
        """
        Round-trips the ioControlClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = self._ref("DIAGNOSTIC-IO-CONTROL-CLASS", "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass")
        result = obj.setIoControlClass(ref)
        assert result is obj  # method chaining
        assert obj.getIoControlClass() is ref
        assert obj.getIoControlClass().getValue() == "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass"
        assert obj.getIoControlClass().getDest() == "DIAGNOSTIC-IO-CONTROL-CLASS"

        result = obj.setIoControlClass(None)
        assert result is obj  # method chaining with None
        assert obj.getIoControlClass() is ref  # None is a no-op

    def test_get_set_reset_to_default(self):
        """
        Round-trips the resetToDefault boolean; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean()
        value.setValue("true")
        result = obj.setResetToDefault(value)
        assert result is obj  # method chaining
        assert obj.getResetToDefault() is value
        assert obj.getResetToDefault().getValue() is True

        result = obj.setResetToDefault(None)
        assert result is obj  # method chaining with None
        assert obj.getResetToDefault() is value  # None is a no-op

    def test_get_set_short_term_adjustment(self):
        """
        Round-trips the shortTermAdjustment boolean; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean()
        value.setValue("true")
        result = obj.setShortTermAdjustment(value)
        assert result is obj  # method chaining
        assert obj.getShortTermAdjustment() is value
        assert obj.getShortTermAdjustment().getValue() is True

        result = obj.setShortTermAdjustment(None)
        assert result is obj  # method chaining with None
        assert obj.getShortTermAdjustment() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters/adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticIOControl.getControlEnableMaskBits.__doc__) == self.CONTROL_ENABLE_MASK_BIT_NOTE
        assert inspect.cleandoc(DiagnosticIOControl.addControlEnableMaskBit.__doc__) == (self.CONTROL_ENABLE_MASK_BIT_NOTE + "\n\nA None value is a no-op and does not append a controlEnableMaskBit.")
        assert inspect.cleandoc(DiagnosticIOControl.getDataIdentifier.__doc__) == self.DATA_IDENTIFIER_NOTE
        assert inspect.cleandoc(DiagnosticIOControl.setDataIdentifier.__doc__) == (self.DATA_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataIdentifier.")
        assert inspect.cleandoc(DiagnosticIOControl.getFreezeCurrentState.__doc__) == self.FREEZE_CURRENT_STATE_NOTE
        assert inspect.cleandoc(DiagnosticIOControl.setFreezeCurrentState.__doc__) == (
            self.FREEZE_CURRENT_STATE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing freezeCurrentState."
        )
        assert inspect.cleandoc(DiagnosticIOControl.getIoControlClass.__doc__) == self.IO_CONTROL_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticIOControl.setIoControlClass.__doc__) == (self.IO_CONTROL_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ioControlClass.")
        assert inspect.cleandoc(DiagnosticIOControl.getResetToDefault.__doc__) == self.RESET_TO_DEFAULT_NOTE
        assert inspect.cleandoc(DiagnosticIOControl.setResetToDefault.__doc__) == (self.RESET_TO_DEFAULT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing resetToDefault.")
        assert inspect.cleandoc(DiagnosticIOControl.getShortTermAdjustment.__doc__) == self.SHORT_TERM_ADJUSTMENT_NOTE
        assert inspect.cleandoc(DiagnosticIOControl.setShortTermAdjustment.__doc__) == (
            self.SHORT_TERM_ADJUSTMENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing shortTermAdjustment."
        )

    def test_create_diagnostic_io_control(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")

        assert io_control is not None
        assert isinstance(io_control, DiagnosticIOControl)
        assert io_control.getShortName() == "IOControl1"
        assert package.getReferrableElement("IOControl1", DiagnosticIOControl) is io_control

        duplicate = package.createDiagnosticIOControl("IOControl1")
        assert duplicate is io_control  # duplicate short name returns the existing element


class TestDiagnosticRoutine:
    """
    Test class for DiagnosticRoutine functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.85, p.124
    """

    CLASS_NOTE = "This meta-class represents the ability to define a diagnostic routine."
    ID_NOTE = "This is the numerical identifier used to identify the DiagnosticRoutine in the scope of diagnostic workflow"
    REQUEST_RESULT_NOTE = "This represents the ability to request the result of a running routine."
    ROUTINE_INFO_NOTE = (
        "This represents the routine info byte. The info byte contains a manufacturer-specific value"
        " (for the identification of record identifiers) that is reported to the tester."
        " Other use cases for this attribute are mentioned in ISO 27145 and ISO 26021."
    )
    START_NOTE = "This represents the ability to start a routine"
    STOP_NOTE = "This represents the ability to stop a running routine."

    def _make_obj(self) -> DiagnosticRoutine:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRoutine(ar_root, "Routine1")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRoutine instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "Routine1"
        assert isinstance(obj, ARElement)
        assert obj.getId() is None
        assert obj.getRequestResult() is None
        assert obj.getRoutineInfo() is None
        assert obj.getStart() is None
        assert obj.getStop() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRoutine.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRoutine.__init__.__doc__ is None

    def test_get_set_id(self):
        """
        Round-trips the id; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("5")
        result = obj.setId(value)
        assert result is obj  # method chaining
        assert obj.getId() is value
        assert obj.getId().getValue() == 5

        obj.setId(None)
        assert obj.getId() is value  # None is a no-op

    def test_create_get_request_result(self):
        """
        Test createRequestResult creation and duplicate reuse.
        """
        obj = self._make_obj()

        request_result = obj.createRequestResult("RequestResults1")
        assert isinstance(request_result, DiagnosticRequestRoutineResults)
        assert request_result.getShortName() == "RequestResults1"
        assert request_result.getParent() is obj
        assert obj.getRequestResult() is request_result

        duplicate = obj.createRequestResult("RequestResults1")
        assert duplicate is request_result  # existing element returned (no duplicate creation)

    def test_get_set_routine_info(self):
        """
        Round-trips the routineInfo; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("7")
        result = obj.setRoutineInfo(value)
        assert result is obj  # method chaining
        assert obj.getRoutineInfo() is value
        assert obj.getRoutineInfo().getValue() == 7

        obj.setRoutineInfo(None)
        assert obj.getRoutineInfo() is value  # None is a no-op

    def test_create_get_start(self):
        """
        Test createStart creation and duplicate reuse.
        """
        obj = self._make_obj()

        start = obj.createStart("Start1")
        assert isinstance(start, DiagnosticStartRoutine)
        assert start.getShortName() == "Start1"
        assert start.getParent() is obj
        assert obj.getStart() is start

        duplicate = obj.createStart("Start1")
        assert duplicate is start  # existing element returned (no duplicate creation)

    def test_create_get_stop(self):
        """
        Test createStop creation and duplicate reuse.
        """
        obj = self._make_obj()

        stop = obj.createStop("Stop1")
        assert isinstance(stop, DiagnosticStopRoutine)
        assert stop.getShortName() == "Stop1"
        assert stop.getParent() is obj
        assert obj.getStop() is stop

        duplicate = obj.createStop("Stop1")
        assert duplicate is stop  # existing element returned (no duplicate creation)

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRoutine.getId.__doc__) == self.ID_NOTE
        assert inspect.cleandoc(DiagnosticRoutine.setId.__doc__) == (self.ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing id.")
        assert inspect.cleandoc(DiagnosticRoutine.getRequestResult.__doc__) == self.REQUEST_RESULT_NOTE
        assert inspect.cleandoc(DiagnosticRoutine.createRequestResult.__doc__) == (
            self.REQUEST_RESULT_NOTE + "\n\nThe existing requestResult is returned when the short name already exists (no duplicate creation)."
        )
        assert inspect.cleandoc(DiagnosticRoutine.getRoutineInfo.__doc__) == self.ROUTINE_INFO_NOTE
        assert inspect.cleandoc(DiagnosticRoutine.setRoutineInfo.__doc__) == (self.ROUTINE_INFO_NOTE + "\n\nA None value is a no-op and does not overwrite an existing routineInfo.")
        assert inspect.cleandoc(DiagnosticRoutine.getStart.__doc__) == self.START_NOTE
        assert inspect.cleandoc(DiagnosticRoutine.createStart.__doc__) == (self.START_NOTE + "\n\nThe existing start is returned when the short name already exists (no duplicate creation).")
        assert inspect.cleandoc(DiagnosticRoutine.getStop.__doc__) == (self.STOP_NOTE)
        assert inspect.cleandoc(DiagnosticRoutine.createStop.__doc__) == (self.STOP_NOTE + "\n\nThe existing stop is returned when the short name already exists (no duplicate creation).")

    def test_create_diagnostic_routine(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        routine = package.createDiagnosticRoutine("Routine1")

        assert routine is not None
        assert isinstance(routine, DiagnosticRoutine)
        assert routine.getShortName() == "Routine1"
        assert package.getReferrableElement("Routine1", DiagnosticRoutine) is routine

        duplicate = package.createDiagnosticRoutine("Routine1")
        assert duplicate is routine  # duplicate short name returns the existing element


class TestDiagnosticRoutineControl:
    """
    Test class for DiagnosticRoutineControl functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.89, p.125
    """

    CLASS_NOTE = 'This represents an instance of the "Routine Control" diagnostic service.'
    ROUTINE_NOTE = "This refers to the applicable DiagnosticRoutine."
    ROUTINE_CONTROL_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticRoutineControl in the given context."
    )

    def _make_obj(self) -> DiagnosticRoutineControl:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRoutineControl(ar_root, "RoutineControl1")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRoutineControl instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "RoutineControl1"
        assert isinstance(obj, ARElement)
        assert obj.getRoutine() is None
        assert obj.getRoutineControlClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRoutineControl.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRoutineControl.__init__.__doc__ is None

    def test_get_set_routine(self):
        """
        Round-trips the routine reference; None is a no-op.
        """
        obj = self._make_obj()

        value = RefType()
        value.setDest("DIAGNOSTIC-ROUTINE")
        value.setValue("/AUTOSAR/DiagnosticRoutines/Routine1")
        result = obj.setRoutine(value)
        assert result is obj  # method chaining
        assert obj.getRoutine() is value
        assert obj.getRoutine().getValue() == "/AUTOSAR/DiagnosticRoutines/Routine1"

        obj.setRoutine(None)
        assert obj.getRoutine() is value  # None is a no-op

    def test_get_set_routine_control_class(self):
        """
        Round-trips the routineControlClass reference; None is a no-op.
        """
        obj = self._make_obj()

        value = RefType()
        value.setDest("DIAGNOSTIC-ROUTINE-CONTROL-CLASS")
        value.setValue("/AUTOSAR/DiagnosticRoutineControls/ControlClass1")
        result = obj.setRoutineControlClass(value)
        assert result is obj  # method chaining
        assert obj.getRoutineControlClass() is value
        assert obj.getRoutineControlClass().getValue() == "/AUTOSAR/DiagnosticRoutineControls/ControlClass1"

        obj.setRoutineControlClass(None)
        assert obj.getRoutineControlClass() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRoutineControl.getRoutine.__doc__) == self.ROUTINE_NOTE
        assert inspect.cleandoc(DiagnosticRoutineControl.setRoutine.__doc__) == (self.ROUTINE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing routine.")
        assert inspect.cleandoc(DiagnosticRoutineControl.getRoutineControlClass.__doc__) == self.ROUTINE_CONTROL_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticRoutineControl.setRoutineControlClass.__doc__) == (
            self.ROUTINE_CONTROL_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing routineControlClass."
        )

    def test_create_diagnostic_routine_control(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        routine_control = package.createDiagnosticRoutineControl("RoutineControl1")

        assert routine_control is not None
        assert isinstance(routine_control, DiagnosticRoutineControl)
        assert routine_control.getShortName() == "RoutineControl1"
        assert package.getReferrableElement("RoutineControl1", DiagnosticRoutineControl) is routine_control

        duplicate = package.createDiagnosticRoutineControl("RoutineControl1")
        assert duplicate is routine_control  # duplicate short name returns the existing element


class TestDiagnosticDynamicallyDefineDataIdentifier:
    """
    Test class for DiagnosticDynamicallyDefineDataIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.93, p.127
    """

    CLASS_NOTE = 'This represents an instance of the "Dynamically Define Data Identifier" diagnostic service.'
    DATA_IDENTIFIER_NOTE = "This represents the applicable DiagnosticDynamicData Identfier."
    DYNAMICALLY_DEFINE_DATA_IDENTIFIER_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticDynamicallyDefineDataIdentifier in the given context."
    )
    MAX_SOURCE_ELEMENT_NOTE = "This represents the maximum number of source elements of the dynamically created DID."

    def _make_obj(self) -> DiagnosticDynamicallyDefineDataIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDynamicallyDefineDataIdentifier(ar_root, "Dddi1")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticDynamicallyDefineDataIdentifier instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "Dddi1"
        assert isinstance(obj, ARElement)
        assert obj.getDataIdentifier() is None
        assert obj.getDynamicallyDefineDataIdentifierClass() is None
        assert obj.getMaxSourceElement() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticDynamicallyDefineDataIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticDynamicallyDefineDataIdentifier.__init__.__doc__ is None

    def test_get_set_data_identifier(self):
        """
        Round-trips the dataIdentifier reference; None is a no-op.
        """
        obj = self._make_obj()

        value = RefType()
        value.setDest("DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER")
        value.setValue("/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1")
        result = obj.setDataIdentifier(value)
        assert result is obj  # method chaining
        assert obj.getDataIdentifier() is value
        assert obj.getDataIdentifier().getValue() == "/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1"

        obj.setDataIdentifier(None)
        assert obj.getDataIdentifier() is value  # None is a no-op

    def test_get_set_dynamically_define_data_identifier_class(self):
        """
        Round-trips the dynamicallyDefineDataIdentifierClass reference; None is a no-op.
        """
        obj = self._make_obj()

        value = RefType()
        value.setDest("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS")
        value.setValue("/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1")
        result = obj.setDynamicallyDefineDataIdentifierClass(value)
        assert result is obj  # method chaining
        assert obj.getDynamicallyDefineDataIdentifierClass() is value
        assert obj.getDynamicallyDefineDataIdentifierClass().getValue() == "/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1"

        obj.setDynamicallyDefineDataIdentifierClass(None)
        assert obj.getDynamicallyDefineDataIdentifierClass() is value  # None is a no-op

    def test_get_set_max_source_element(self):
        """
        Round-trips the maxSourceElement; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("9")
        result = obj.setMaxSourceElement(value)
        assert result is obj  # method chaining
        assert obj.getMaxSourceElement() is value
        assert obj.getMaxSourceElement().getValue() == 9

        obj.setMaxSourceElement(None)
        assert obj.getMaxSourceElement() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticDynamicallyDefineDataIdentifier.getDataIdentifier.__doc__) == self.DATA_IDENTIFIER_NOTE
        assert inspect.cleandoc(DiagnosticDynamicallyDefineDataIdentifier.setDataIdentifier.__doc__) == (
            self.DATA_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataIdentifier."
        )
        assert inspect.cleandoc(DiagnosticDynamicallyDefineDataIdentifier.getDynamicallyDefineDataIdentifierClass.__doc__) == self.DYNAMICALLY_DEFINE_DATA_IDENTIFIER_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticDynamicallyDefineDataIdentifier.setDynamicallyDefineDataIdentifierClass.__doc__) == (
            self.DYNAMICALLY_DEFINE_DATA_IDENTIFIER_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dynamicallyDefineDataIdentifierClass."
        )
        assert inspect.cleandoc(DiagnosticDynamicallyDefineDataIdentifier.getMaxSourceElement.__doc__) == self.MAX_SOURCE_ELEMENT_NOTE
        assert inspect.cleandoc(DiagnosticDynamicallyDefineDataIdentifier.setMaxSourceElement.__doc__) == (
            self.MAX_SOURCE_ELEMENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing maxSourceElement."
        )

    def test_create_diagnostic_dynamically_define_data_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi = package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")

        assert dddi is not None
        assert isinstance(dddi, DiagnosticDynamicallyDefineDataIdentifier)
        assert dddi.getShortName() == "Dddi1"
        assert package.getReferrableElement("Dddi1", DiagnosticDynamicallyDefineDataIdentifier) is dddi

        duplicate = package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")
        assert duplicate is dddi  # duplicate short name returns the existing element


class TestDiagnosticReadDataByPeriodicID:
    """
    Test class for DiagnosticReadDataByPeriodicID functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.97, p.130
    """

    CLASS_NOTE = 'This represents an instance of the "Read Data by periodic Identifier" diagnostic service.'
    READ_DATA_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByPeriodicID in the given context."
    )

    def _make_obj(self) -> DiagnosticReadDataByPeriodicID:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticReadDataByPeriodicID(ar_root, "Rdbpid1")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticReadDataByPeriodicID instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "Rdbpid1"
        assert isinstance(obj, ARElement)
        assert obj.getReadDataClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticReadDataByPeriodicID.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticReadDataByPeriodicID.__init__.__doc__ is None

    def test_get_set_read_data_class(self):
        """
        Round-trips the readDataClass reference; None is a no-op.
        """
        obj = self._make_obj()

        value = RefType()
        value.setDest("DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS")
        value.setValue("/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1")
        result = obj.setReadDataClass(value)
        assert result is obj  # method chaining
        assert obj.getReadDataClass() is value
        assert obj.getReadDataClass().getValue() == "/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1"

        obj.setReadDataClass(None)
        assert obj.getReadDataClass() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticReadDataByPeriodicID.getReadDataClass.__doc__) == self.READ_DATA_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticReadDataByPeriodicID.setReadDataClass.__doc__) == (
            self.READ_DATA_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing readDataClass."
        )

    def test_create_diagnostic_read_data_by_periodic_id(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        obj = package.createDiagnosticReadDataByPeriodicID("Rdbpid1")

        assert obj is not None
        assert isinstance(obj, DiagnosticReadDataByPeriodicID)
        assert obj.getShortName() == "Rdbpid1"
        assert package.getReferrableElement("Rdbpid1", DiagnosticReadDataByPeriodicID) is obj

        duplicate = package.createDiagnosticReadDataByPeriodicID("Rdbpid1")
        assert duplicate is obj  # duplicate short name returns the existing element


class TestDiagnosticResponseOnEvent:
    """
    Test class for DiagnosticResponseOnEvent functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.101, p.132
    """

    CLASS_NOTE = 'This represents an instance of the "Response on Event" diagnostic service.'
    EVENT_WINDOW_NOTE = "This represents the applicable DiagnosticEventWindows"
    RESPONSE_ON_EVENT_ACTION_NOTE = "Defines sub-functions of the service ResponseOnEvent."
    RESPONSE_ON_EVENT_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticResponseOnEvent in the given context."
    )

    def _make_obj(self) -> DiagnosticResponseOnEvent:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticResponseOnEvent(ar_root, "TestResponseOnEvent")

    def _ref(self, dest: str, value: str) -> RefType:
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticResponseOnEvent instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestResponseOnEvent"
        assert isinstance(obj, ARElement)
        assert obj.getEventWindows() == []
        assert obj.getResponseOnEventAction() is None
        assert obj.getResponseOnEventClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticResponseOnEvent.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticResponseOnEvent.__init__.__doc__ is None

    def test_add_event_window(self):
        """
        Test addEventWindow append and None no-op.
        """
        obj = self._make_obj()

        event_window = DiagnosticEventWindow()
        result = obj.addEventWindow(event_window)
        assert result is obj  # method chaining
        assert obj.getEventWindows() == [event_window]

        result = obj.addEventWindow(None)
        assert result is obj  # method chaining with None
        assert obj.getEventWindows() == [event_window]  # None is a no-op

    def test_get_set_response_on_event_action(self):
        """
        Round-trips the responseOnEventAction enum; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticResponseOnEventActionEnum().setValue(DiagnosticResponseOnEventActionEnum.ON_CHANGE_OF_DATA_IDENTIFIER)
        result = obj.setResponseOnEventAction(value)
        assert result is obj  # method chaining
        assert obj.getResponseOnEventAction() is value
        assert obj.getResponseOnEventAction().getValue() == DiagnosticResponseOnEventActionEnum.ON_CHANGE_OF_DATA_IDENTIFIER

        result = obj.setResponseOnEventAction(None)
        assert result is obj  # method chaining with None
        assert obj.getResponseOnEventAction() is value  # None is a no-op

    def test_get_set_response_on_event_class(self):
        """
        Round-trips the responseOnEventClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = self._ref("DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS", "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass")
        result = obj.setResponseOnEventClass(ref)
        assert result is obj  # method chaining
        assert obj.getResponseOnEventClass() is ref
        assert obj.getResponseOnEventClass().getValue() == "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass"
        assert obj.getResponseOnEventClass().getDest() == "DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS"

        result = obj.setResponseOnEventClass(None)
        assert result is obj  # method chaining with None
        assert obj.getResponseOnEventClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters/adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticResponseOnEvent.getEventWindows.__doc__) == self.EVENT_WINDOW_NOTE
        assert inspect.cleandoc(DiagnosticResponseOnEvent.addEventWindow.__doc__) == (self.EVENT_WINDOW_NOTE + "\n\nA None value is a no-op and does not append an eventWindow.")
        assert inspect.cleandoc(DiagnosticResponseOnEvent.getResponseOnEventAction.__doc__) == self.RESPONSE_ON_EVENT_ACTION_NOTE
        assert inspect.cleandoc(DiagnosticResponseOnEvent.setResponseOnEventAction.__doc__) == (
            self.RESPONSE_ON_EVENT_ACTION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing responseOnEventAction."
        )
        assert inspect.cleandoc(DiagnosticResponseOnEvent.getResponseOnEventClass.__doc__) == self.RESPONSE_ON_EVENT_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticResponseOnEvent.setResponseOnEventClass.__doc__) == (
            self.RESPONSE_ON_EVENT_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing responseOnEventClass."
        )

    def test_create_diagnostic_response_on_event(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")

        assert response_on_event is not None
        assert isinstance(response_on_event, DiagnosticResponseOnEvent)
        assert response_on_event.getShortName() == "ResponseOnEvent1"
        assert package.getReferrableElement("ResponseOnEvent1", DiagnosticResponseOnEvent) is response_on_event

        duplicate = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")
        assert duplicate is response_on_event  # duplicate short name returns the existing element


class TestDiagnosticReadDTCInformation:
    """
    Test class for DiagnosticReadDTCInformation functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.106, p.136
    """

    CLASS_NOTE = 'This represents an instance of the "Read DTC Information" diagnostic service.'
    READ_DTC_INFORMATION_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDTCInformation in the given context."
    )

    def _make_obj(self) -> DiagnosticReadDTCInformation:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticReadDTCInformation(ar_root, "TestReadDTCInformation")

    def _ref(self, dest: str, value: str) -> RefType:
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticReadDTCInformation instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestReadDTCInformation"
        assert isinstance(obj, ARElement)
        assert obj.getReadDTCInformationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticReadDTCInformation.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticReadDTCInformation.__init__.__doc__ is None

    def test_get_set_read_dtc_information_class(self):
        """
        Round-trips the readDTCInformationClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = self._ref("DIAGNOSTIC-READ-DTC-INFORMATION-CLASS", "/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass")
        result = obj.setReadDTCInformationClass(ref)
        assert result is obj  # method chaining
        assert obj.getReadDTCInformationClass() is ref
        assert obj.getReadDTCInformationClass().getValue() == "/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass"
        assert obj.getReadDTCInformationClass().getDest() == "DIAGNOSTIC-READ-DTC-INFORMATION-CLASS"

        result = obj.setReadDTCInformationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getReadDTCInformationClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticReadDTCInformation.getReadDTCInformationClass.__doc__) == self.READ_DTC_INFORMATION_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticReadDTCInformation.setReadDTCInformationClass.__doc__) == (
            self.READ_DTC_INFORMATION_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing readDTCInformationClass."
        )

    def test_create_diagnostic_read_dtc_information(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDtcInformations")
        read_dtc_information = package.createDiagnosticReadDTCInformation("ReadDTCInformation1")

        assert read_dtc_information is not None
        assert isinstance(read_dtc_information, DiagnosticReadDTCInformation)
        assert read_dtc_information.getShortName() == "ReadDTCInformation1"
        assert package.getReferrableElement("ReadDTCInformation1", DiagnosticReadDTCInformation) is read_dtc_information

        duplicate = package.createDiagnosticReadDTCInformation("ReadDTCInformation1")
        assert duplicate is read_dtc_information  # duplicate short name returns the existing element


class TestDiagnosticClearDiagnosticInformation:
    """
    Test class for DiagnosticClearDiagnosticInformation functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.108, p.137
    """

    CLASS_NOTE = 'This represents an instance of the "Clear Diagnostic Information" diagnostic service.'
    CLEAR_DIAGNOSTIC_INFORMATION_CLASS_NOTE = (
        "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class."
        " Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearDiagnosticInformation in the given context."
    )

    def _make_obj(self) -> DiagnosticClearDiagnosticInformation:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticClearDiagnosticInformation(ar_root, "TestClearDiagnosticInformation")

    def _ref(self, dest: str, value: str) -> RefType:
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticClearDiagnosticInformation instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestClearDiagnosticInformation"
        assert isinstance(obj, ARElement)
        assert obj.getClearDiagnosticInformationClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticClearDiagnosticInformation.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticClearDiagnosticInformation.__init__.__doc__ is None

    def test_get_set_clear_diagnostic_information_class(self):
        """
        Round-trips the clearDiagnosticInformationClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = self._ref("DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS", "/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass")
        result = obj.setClearDiagnosticInformationClass(ref)
        assert result is obj  # method chaining
        assert obj.getClearDiagnosticInformationClass() is ref
        assert obj.getClearDiagnosticInformationClass().getValue() == "/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass"
        assert obj.getClearDiagnosticInformationClass().getDest() == "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS"

        result = obj.setClearDiagnosticInformationClass(None)
        assert result is obj  # method chaining with None
        assert obj.getClearDiagnosticInformationClass() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticClearDiagnosticInformation.getClearDiagnosticInformationClass.__doc__) == self.CLEAR_DIAGNOSTIC_INFORMATION_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticClearDiagnosticInformation.setClearDiagnosticInformationClass.__doc__) == (
            self.CLEAR_DIAGNOSTIC_INFORMATION_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing clearDiagnosticInformationClass."
        )

    def test_create_diagnostic_clear_diagnostic_information(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticClearDiagnosticInformations")
        clear_diagnostic_information = package.createDiagnosticClearDiagnosticInformation("ClearDiagnosticInformation1")

        assert clear_diagnostic_information is not None
        assert isinstance(clear_diagnostic_information, DiagnosticClearDiagnosticInformation)
        assert clear_diagnostic_information.getShortName() == "ClearDiagnosticInformation1"
        assert package.getReferrableElement("ClearDiagnosticInformation1", DiagnosticClearDiagnosticInformation) is clear_diagnostic_information

        duplicate = package.createDiagnosticClearDiagnosticInformation("ClearDiagnosticInformation1")
        assert duplicate is clear_diagnostic_information  # duplicate short name returns the existing element


class TestDiagnosticMemoryByAddress:
    """
    Test class for DiagnosticMemoryByAddress functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.110, p.139
    (abstract base with no own attributes; exercised through the concrete
    subclass DiagnosticTransferExit)
    """

    CLASS_NOTE = "This represents an abstract base class for diagnostic services that deal with accessing memory by address."

    def _make_obj(self) -> DiagnosticTransferExit:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTransferExit(ar_root, "TestTransferExit")

    def test_initialization(self):
        """
        Test that a concrete subclass of the abstract DiagnosticMemoryByAddress is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestTransferExit"
        assert isinstance(obj, DiagnosticMemoryByAddress)
        assert isinstance(obj, ARElement)

    def test_abstract_instantiation_raises(self):
        """
        Test that the abstract DiagnosticMemoryByAddress cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticMemoryByAddress(AUTOSAR.getInstance(), "DirectInstance")

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticMemoryByAddress.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMemoryByAddress.__init__.__doc__ is None


class _MemoryAddressableRangeAccessStub(DiagnosticMemoryAddressableRangeAccess):
    """Concrete test stub for the abstract DiagnosticMemoryAddressableRangeAccess."""

    pass


class TestDiagnosticMemoryAddressableRangeAccess:
    """
    Test class for DiagnosticMemoryAddressableRangeAccess functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.111, p.140
    (abstract base; exercised through the test stub subclass
    _MemoryAddressableRangeAccessStub until a concrete sibling syncs)
    """

    CLASS_NOTE = "This abstract base class"
    MEMORY_RANGE_NOTE = "This represents the formal description of the memory segment to which the DiagnosticMemoryByAddress applies."

    def _make_obj(self) -> _MemoryAddressableRangeAccessStub:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return _MemoryAddressableRangeAccessStub(ar_root, "TestRangeAccess")

    def test_initialization(self):
        """
        Test that a concrete subclass of the abstract DiagnosticMemoryAddressableRangeAccess is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestRangeAccess"
        assert isinstance(obj, DiagnosticMemoryAddressableRangeAccess)
        assert isinstance(obj, DiagnosticMemoryByAddress)
        assert isinstance(obj, ARElement)
        assert obj.getMemoryRanges() == []

    def test_abstract_instantiation_raises(self):
        """
        Test that the abstract DiagnosticMemoryAddressableRangeAccess cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticMemoryAddressableRangeAccess(AUTOSAR.getInstance(), "DirectInstance")

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticMemoryAddressableRangeAccess.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMemoryAddressableRangeAccess.__init__.__doc__ is None

    def test_add_get_memory_ranges(self):
        """
        Appends memoryRange refs; None is a no-op.
        """
        obj = self._make_obj()

        ref1 = RefType()
        ref1.setDest("DIAGNOSTIC-MEMORY-IDENTIFIER")
        ref1.setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1")
        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-MEMORY-IDENTIFIER")
        ref2.setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2")

        result = obj.addMemoryRange(ref1)
        assert result is obj  # method chaining
        result = obj.addMemoryRange(ref2)
        assert result is obj  # method chaining
        assert obj.getMemoryRanges() == [ref1, ref2]
        assert obj.getMemoryRanges()[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert obj.getMemoryRanges()[0].getDest() == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert obj.getMemoryRanges()[1].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"

        result = obj.addMemoryRange(None)
        assert result is obj  # method chaining with None
        assert obj.getMemoryRanges() == [ref1, ref2]  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticMemoryAddressableRangeAccess.getMemoryRanges.__doc__) == self.MEMORY_RANGE_NOTE
        assert inspect.cleandoc(DiagnosticMemoryAddressableRangeAccess.addMemoryRange.__doc__) == (self.MEMORY_RANGE_NOTE + "\n\nA None value is a no-op and does not append a memoryRange.")


class TestDiagnosticMemoryDestinationPrimary:
    """
    Test class for DiagnosticMemoryDestinationPrimary functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.173, p.184

    DiagnosticMemoryDestinationPrimary is the concrete ARElement branch of the
    abstract DiagnosticMemoryDestination (Table 4.167, synced in ArObject.py as
    an ARObject-derived value container): the class joins the ARElement
    Identifiable chain with the base's nine inherited attributes plus its single
    own attribute typeOfDtcSupported (XSD group
    DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY, AUTOSAR_00052.xsd l.39661).
    """

    CLASS_NOTE = "This represents a primary memory for a diagnostic event. Tags: atp.recommendedPackage=DiagnosticMemoryDestinations"
    TYPE_OF_DTC_SUPPORTED_NOTE = "This attribute defines the format returned by Dem_Dcm GetTranslationType and does not relate to/influence the supported Dem functionality."

    def _make_obj(self) -> DiagnosticMemoryDestinationPrimary:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticMemoryDestinationPrimary(ar_root, "TestMemoryDestinationPrimary")

    def test_initialization(self):
        """
        Test that the concrete class instantiates on the ARElement x DiagnosticMemoryDestination chain with the own and inherited defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMemoryDestinationPrimary"
        assert isinstance(obj, DiagnosticMemoryDestinationPrimary)
        assert isinstance(obj, DiagnosticMemoryDestination)
        assert isinstance(obj, ARElement)
        assert obj.getTypeOfDtcSupported() is None
        assert obj.getAgingRequiresTestedCycle() is None
        assert obj.getMaxNumberOfEventEntries() is None
        assert obj.getStatusBitStorageTestFailed() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticMemoryDestinationPrimary.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMemoryDestinationPrimary.__init__.__doc__ is None

    def test_get_set_type_of_dtc_supported(self):
        """
        Round-trips the own typeOfDtcSupported; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticTypeOfDtcSupportedEnum().setValue(DiagnosticTypeOfDtcSupportedEnum.ISO14229_1)
        result = obj.setTypeOfDtcSupported(value)
        assert result is obj  # method chaining
        assert obj.getTypeOfDtcSupported() is value
        assert obj.getTypeOfDtcSupported().getValue() == DiagnosticTypeOfDtcSupportedEnum.ISO14229_1

        result = obj.setTypeOfDtcSupported(None)
        assert result is obj  # method chaining with None
        assert obj.getTypeOfDtcSupported() is value  # None is a no-op

    def test_get_set_inherited_attribute(self):
        """
        Spot-checks the inherited base attribute maxNumberOfEventEntries (Table 4.167); None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger().setValue(10)
        result = obj.setMaxNumberOfEventEntries(value)
        assert result is obj  # method chaining
        assert obj.getMaxNumberOfEventEntries() is value
        assert obj.getMaxNumberOfEventEntries().getValue() == 10

        result = obj.setMaxNumberOfEventEntries(None)
        assert result is obj  # method chaining with None
        assert obj.getMaxNumberOfEventEntries() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticMemoryDestinationPrimary.getTypeOfDtcSupported.__doc__) == self.TYPE_OF_DTC_SUPPORTED_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestinationPrimary.setTypeOfDtcSupported.__doc__) == (
            self.TYPE_OF_DTC_SUPPORTED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing typeOfDtcSupported."
        )

    def test_create_diagnostic_memory_destination_primary(self):
        """
        Test that ARPackage.createDiagnosticMemoryDestinationPrimary appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticMemoryDestinationPrimary("MemoryDestinationPrimary1")

        assert isinstance(obj, DiagnosticMemoryDestinationPrimary)
        assert obj.getShortName() == "MemoryDestinationPrimary1"
        assert ar_root.getReferrableElement("MemoryDestinationPrimary1", DiagnosticMemoryDestinationPrimary) is obj

        duplicate = ar_root.createDiagnosticMemoryDestinationPrimary("MemoryDestinationPrimary1")
        assert duplicate is obj


class TestDiagnosticMemoryIdentifier:
    """
    Test class for DiagnosticMemoryIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.112, p.140
    """

    CLASS_NOTE = "This meta-class represents the ability to define memory properties from the diagnostics point of view. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"
    ACCESS_PERMISSION_NOTE = "This represents that access permission defined for the specific DiagnosticMemoryIdentifier. Stereotypes: atpSplitable Tags: atp.Splitkey=accessPermission"
    ID_NOTE = "This represents the identification of the memory segment."
    MEMORY_HIGH_ADDRESS_NOTE = "This represents the upper bound for addresses of the memory segment."
    MEMORY_HIGH_ADDRESS_LABEL_NOTE = "This represents a symbolic label for the upper bound for addresses of the memory segment."
    MEMORY_LOW_ADDRESS_NOTE = "This represents the lower bound for addresses of the memory segment."
    MEMORY_LOW_ADDRESS_LABEL_NOTE = "This represents a symbolic label for the lower bound for addresses of the memory segment."

    def _make_obj(self) -> DiagnosticMemoryIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticMemoryIdentifier(ar_root, "TestMemoryIdentifier")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticMemoryIdentifier instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMemoryIdentifier"
        assert isinstance(obj, ARElement)
        assert obj.getAccessPermissionRef() is None
        assert obj.getId() is None
        assert obj.getMemoryHighAddress() is None
        assert obj.getMemoryHighAddressLabel() is None
        assert obj.getMemoryLowAddress() is None
        assert obj.getMemoryLowAddressLabel() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticMemoryIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMemoryIdentifier.__init__.__doc__ is None

    def test_get_set_access_permission_ref(self):
        """
        Round-trips the accessPermission ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-ACCESS-PERMISSION")
        ref.setValue("/AUTOSAR/DiagnosticAccessPermissions/Permission1")
        result = obj.setAccessPermissionRef(ref)
        assert result is obj  # method chaining
        assert obj.getAccessPermissionRef() is ref
        assert obj.getAccessPermissionRef().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Permission1"
        assert obj.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"

        result = obj.setAccessPermissionRef(None)
        assert result is obj  # method chaining with None
        assert obj.getAccessPermissionRef() is ref  # None is a no-op

    def test_get_set_id(self):
        """
        Round-trips id; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("1")
        result = obj.setId(value)
        assert result is obj  # method chaining
        assert obj.getId() is value
        assert obj.getId().getValue() == 1

        obj.setId(None)
        assert obj.getId() is value  # None is a no-op

    def test_get_set_memory_high_address(self):
        """
        Round-trips memoryHighAddress; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("4096")
        result = obj.setMemoryHighAddress(value)
        assert result is obj  # method chaining
        assert obj.getMemoryHighAddress() is value
        assert obj.getMemoryHighAddress().getValue() == 4096

        obj.setMemoryHighAddress(None)
        assert obj.getMemoryHighAddress() is value  # None is a no-op

    def test_get_set_memory_high_address_label(self):
        """
        Round-trips memoryHighAddressLabel; None is a no-op.
        """
        obj = self._make_obj()

        value = String()
        value.setValue("0x1000")
        result = obj.setMemoryHighAddressLabel(value)
        assert result is obj  # method chaining
        assert obj.getMemoryHighAddressLabel() is value
        assert obj.getMemoryHighAddressLabel().getValue() == "0x1000"

        obj.setMemoryHighAddressLabel(None)
        assert obj.getMemoryHighAddressLabel() is value  # None is a no-op

    def test_get_set_memory_low_address(self):
        """
        Round-trips memoryLowAddress; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("0")
        result = obj.setMemoryLowAddress(value)
        assert result is obj  # method chaining
        assert obj.getMemoryLowAddress() is value
        assert obj.getMemoryLowAddress().getValue() == 0

        obj.setMemoryLowAddress(None)
        assert obj.getMemoryLowAddress() is value  # None is a no-op

    def test_get_set_memory_low_address_label(self):
        """
        Round-trips memoryLowAddressLabel; None is a no-op.
        """
        obj = self._make_obj()

        value = String()
        value.setValue("0x0")
        result = obj.setMemoryLowAddressLabel(value)
        assert result is obj  # method chaining
        assert obj.getMemoryLowAddressLabel() is value
        assert obj.getMemoryLowAddressLabel().getValue() == "0x0"

        obj.setMemoryLowAddressLabel(None)
        assert obj.getMemoryLowAddressLabel() is value  # None is a no-op

    def test_create_diagnostic_memory_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMemoryIdentifiers")
        element = package.createDiagnosticMemoryIdentifier("Segment1")

        assert element is not None
        assert isinstance(element, DiagnosticMemoryIdentifier)
        assert element.getShortName() == "Segment1"
        assert package.getReferrableElement("Segment1", DiagnosticMemoryIdentifier) is element

        duplicate = package.createDiagnosticMemoryIdentifier("Segment1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.getAccessPermissionRef.__doc__) == self.ACCESS_PERMISSION_NOTE
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.setAccessPermissionRef.__doc__) == (
            self.ACCESS_PERMISSION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing accessPermissionRef."
        )
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.getId.__doc__) == self.ID_NOTE
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.setId.__doc__) == (self.ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing id.")
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.getMemoryHighAddress.__doc__) == self.MEMORY_HIGH_ADDRESS_NOTE
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.setMemoryHighAddress.__doc__) == (
            self.MEMORY_HIGH_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing memoryHighAddress."
        )
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.getMemoryHighAddressLabel.__doc__) == self.MEMORY_HIGH_ADDRESS_LABEL_NOTE
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.setMemoryHighAddressLabel.__doc__) == (
            self.MEMORY_HIGH_ADDRESS_LABEL_NOTE + "\n\nA None value is a no-op and does not overwrite an existing memoryHighAddressLabel."
        )
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.getMemoryLowAddress.__doc__) == self.MEMORY_LOW_ADDRESS_NOTE
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.setMemoryLowAddress.__doc__) == (
            self.MEMORY_LOW_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing memoryLowAddress."
        )
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.getMemoryLowAddressLabel.__doc__) == self.MEMORY_LOW_ADDRESS_LABEL_NOTE
        assert inspect.cleandoc(DiagnosticMemoryIdentifier.setMemoryLowAddressLabel.__doc__) == (
            self.MEMORY_LOW_ADDRESS_LABEL_NOTE + "\n\nA None value is a no-op and does not overwrite an existing memoryLowAddressLabel."
        )


class TestDiagnosticWriteMemoryByAddress:
    """
    Test class for DiagnosticWriteMemoryByAddress functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.113, p.141
    """

    CLASS_NOTE = 'This represents an instance of the "Write Memory by Address" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss'
    WRITE_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticWritememoryByAddress in the given context."

    def _make_obj(self) -> DiagnosticWriteMemoryByAddress:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticWriteMemoryByAddress(ar_root, "TestWriteMemoryByAddress")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticWriteMemoryByAddress instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestWriteMemoryByAddress"
        assert isinstance(obj, DiagnosticMemoryAddressableRangeAccess)
        assert obj.getWriteClassRef() is None
        assert obj.getMemoryRanges() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticWriteMemoryByAddress.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticWriteMemoryByAddress.__init__.__doc__ is None

    def test_get_set_write_class_ref(self):
        """
        Round-trips the writeClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1")
        result = obj.setWriteClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getWriteClassRef() is ref
        assert obj.getWriteClassRef().getValue() == "/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1"
        assert obj.getWriteClassRef().getDest() == "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS"

        result = obj.setWriteClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getWriteClassRef() is ref  # None is a no-op

    def test_add_memory_range_inherited(self):
        """
        Test the inherited memoryRange accessors from DiagnosticMemoryAddressableRangeAccess.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-MEMORY-IDENTIFIER")
        ref.setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1")
        result = obj.addMemoryRange(ref)
        assert result is obj  # method chaining
        assert obj.getMemoryRanges() == [ref]
        assert obj.getMemoryRanges()[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"

        obj.addMemoryRange(None)
        assert obj.getMemoryRanges() == [ref]  # None is a no-op

    def test_create_diagnostic_write_memory_by_address(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteMemoryByAddressServices")
        element = package.createDiagnosticWriteMemoryByAddress("WriteMemoryService1")

        assert element is not None
        assert isinstance(element, DiagnosticWriteMemoryByAddress)
        assert element.getShortName() == "WriteMemoryService1"
        assert package.getReferrableElement("WriteMemoryService1", DiagnosticWriteMemoryByAddress) is element

        duplicate = package.createDiagnosticWriteMemoryByAddress("WriteMemoryService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticWriteMemoryByAddress.getWriteClassRef.__doc__) == self.WRITE_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticWriteMemoryByAddress.setWriteClassRef.__doc__) == (self.WRITE_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing writeClassRef.")


class TestDiagnosticReadMemoryByAddress:
    """
    Test class for DiagnosticReadMemoryByAddress functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.115, p.142
    """

    CLASS_NOTE = 'This represents an instance of the "Read Memory by Address" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss'
    READ_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadMemoryByAddresst in the given context."

    def _make_obj(self) -> DiagnosticReadMemoryByAddress:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticReadMemoryByAddress(ar_root, "TestReadMemoryByAddress")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticReadMemoryByAddress instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestReadMemoryByAddress"
        assert isinstance(obj, DiagnosticMemoryAddressableRangeAccess)
        assert obj.getReadClassRef() is None
        assert obj.getMemoryRanges() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticReadMemoryByAddress.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticReadMemoryByAddress.__init__.__doc__ is None

    def test_get_set_read_class_ref(self):
        """
        Round-trips the readClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1")
        result = obj.setReadClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getReadClassRef() is ref
        assert obj.getReadClassRef().getValue() == "/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1"
        assert obj.getReadClassRef().getDest() == "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS"

        result = obj.setReadClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getReadClassRef() is ref  # None is a no-op

    def test_add_memory_range_inherited(self):
        """
        Test the inherited memoryRange accessors from DiagnosticMemoryAddressableRangeAccess.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-MEMORY-IDENTIFIER")
        ref.setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1")
        result = obj.addMemoryRange(ref)
        assert result is obj  # method chaining
        assert obj.getMemoryRanges() == [ref]
        assert obj.getMemoryRanges()[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"

        obj.addMemoryRange(None)
        assert obj.getMemoryRanges() == [ref]  # None is a no-op

    def test_create_diagnostic_read_memory_by_address(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadMemoryByAddressServices")
        element = package.createDiagnosticReadMemoryByAddress("ReadMemoryService1")

        assert element is not None
        assert isinstance(element, DiagnosticReadMemoryByAddress)
        assert element.getShortName() == "ReadMemoryService1"
        assert package.getReferrableElement("ReadMemoryService1", DiagnosticReadMemoryByAddress) is element

        duplicate = package.createDiagnosticReadMemoryByAddress("ReadMemoryService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticReadMemoryByAddress.getReadClassRef.__doc__) == self.READ_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticReadMemoryByAddress.setReadClassRef.__doc__) == (self.READ_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing readClassRef.")


class TestDiagnosticTransferExit:
    """
    Test class for DiagnosticTransferExit functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.117, p.143
    """

    CLASS_NOTE = 'This represents an instance of the "Transfer Exit" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss'
    TRANSFER_EXIT_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticTransferExit in the given context."

    def _make_obj(self) -> DiagnosticTransferExit:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTransferExit(ar_root, "TestTransferExit")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticTransferExit instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestTransferExit"
        assert isinstance(obj, DiagnosticMemoryByAddress)
        assert obj.getTransferExitClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticTransferExit.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTransferExit.__init__.__doc__ is None

    def test_get_set_transfer_exit_class_ref(self):
        """
        Round-trips the transferExitClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-TRANSFER-EXIT-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticTransferExitClasses/Class1")
        result = obj.setTransferExitClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getTransferExitClassRef() is ref
        assert obj.getTransferExitClassRef().getValue() == "/AUTOSAR/DiagnosticTransferExitClasses/Class1"
        assert obj.getTransferExitClassRef().getDest() == "DIAGNOSTIC-TRANSFER-EXIT-CLASS"

        result = obj.setTransferExitClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getTransferExitClassRef() is ref  # None is a no-op

    def test_create_diagnostic_transfer_exit(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTransferExitServices")
        element = package.createDiagnosticTransferExit("TransferExitService1")

        assert element is not None
        assert isinstance(element, DiagnosticTransferExit)
        assert element.getShortName() == "TransferExitService1"
        assert package.getReferrableElement("TransferExitService1", DiagnosticTransferExit) is element

        duplicate = package.createDiagnosticTransferExit("TransferExitService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticTransferExit.getTransferExitClassRef.__doc__) == self.TRANSFER_EXIT_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticTransferExit.setTransferExitClassRef.__doc__) == (
            self.TRANSFER_EXIT_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing transferExitClassRef."
        )


class TestDiagnosticDataTransfer:
    """
    Test class for DiagnosticDataTransfer functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.119, p.143
    """

    CLASS_NOTE = 'This represents an instance of the "Data Transfer" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss'
    DATA_TRANSFER_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticDataTransfer in the given context."

    def _make_obj(self) -> DiagnosticDataTransfer:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDataTransfer(ar_root, "TestDataTransfer")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticDataTransfer instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestDataTransfer"
        assert isinstance(obj, DiagnosticMemoryByAddress)
        assert obj.getDataTransferClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticDataTransfer.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticDataTransfer.__init__.__doc__ is None

    def test_get_set_data_transfer_class_ref(self):
        """
        Round-trips the dataTransferClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-DATA-TRANSFER-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticDataTransferClasses/Class1")
        result = obj.setDataTransferClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getDataTransferClassRef() is ref
        assert obj.getDataTransferClassRef().getValue() == "/AUTOSAR/DiagnosticDataTransferClasses/Class1"
        assert obj.getDataTransferClassRef().getDest() == "DIAGNOSTIC-DATA-TRANSFER-CLASS"

        result = obj.setDataTransferClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDataTransferClassRef() is ref  # None is a no-op

    def test_create_diagnostic_data_transfer(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataTransferServices")
        element = package.createDiagnosticDataTransfer("DataTransferService1")

        assert element is not None
        assert isinstance(element, DiagnosticDataTransfer)
        assert element.getShortName() == "DataTransferService1"
        assert package.getReferrableElement("DataTransferService1", DiagnosticDataTransfer) is element

        duplicate = package.createDiagnosticDataTransfer("DataTransferService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticDataTransfer.getDataTransferClassRef.__doc__) == self.DATA_TRANSFER_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticDataTransfer.setDataTransferClassRef.__doc__) == (
            self.DATA_TRANSFER_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataTransferClassRef."
        )


class TestDiagnosticRequestDownload:
    """
    Test class for DiagnosticRequestDownload functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.121, p.144
    """

    CLASS_NOTE = 'This represents an instance of the "Request Download" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss'
    REQUEST_DOWNLOAD_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestDownload in the given context."

    def _make_obj(self) -> DiagnosticRequestDownload:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestDownload(ar_root, "TestRequestDownload")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestDownload instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestRequestDownload"
        assert isinstance(obj, DiagnosticMemoryAddressableRangeAccess)
        assert obj.getRequestDownloadClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestDownload.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestDownload.__init__.__doc__ is None

    def test_get_set_request_download_class_ref(self):
        """
        Round-trips the requestDownloadClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestDownloadClasses/Class1")
        result = obj.setRequestDownloadClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestDownloadClassRef() is ref
        assert obj.getRequestDownloadClassRef().getValue() == "/AUTOSAR/DiagnosticRequestDownloadClasses/Class1"
        assert obj.getRequestDownloadClassRef().getDest() == "DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS"

        result = obj.setRequestDownloadClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestDownloadClassRef() is ref  # None is a no-op

    def test_create_diagnostic_request_download(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestDownloadServices")
        element = package.createDiagnosticRequestDownload("RequestDownloadService1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestDownload)
        assert element.getShortName() == "RequestDownloadService1"
        assert package.getReferrableElement("RequestDownloadService1", DiagnosticRequestDownload) is element

        duplicate = package.createDiagnosticRequestDownload("RequestDownloadService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestDownload.getRequestDownloadClassRef.__doc__) == self.REQUEST_DOWNLOAD_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticRequestDownload.setRequestDownloadClassRef.__doc__) == (
            self.REQUEST_DOWNLOAD_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestDownloadClassRef."
        )


class TestDiagnosticRequestUpload:
    """
    Test class for DiagnosticRequestUpload functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.123, p.145
    """

    CLASS_NOTE = 'This represents an instance of the "Request Upload" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss'
    REQUEST_UPLOAD_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestUpload in the given context."

    def _make_obj(self) -> DiagnosticRequestUpload:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestUpload(ar_root, "TestRequestUpload")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestUpload instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestRequestUpload"
        assert isinstance(obj, DiagnosticMemoryAddressableRangeAccess)
        assert obj.getRequestUploadClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestUpload.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestUpload.__init__.__doc__ is None

    def test_get_set_request_upload_class_ref(self):
        """
        Round-trips the requestUploadClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-UPLOAD-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestUploadClasses/Class1")
        result = obj.setRequestUploadClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestUploadClassRef() is ref
        assert obj.getRequestUploadClassRef().getValue() == "/AUTOSAR/DiagnosticRequestUploadClasses/Class1"
        assert obj.getRequestUploadClassRef().getDest() == "DIAGNOSTIC-REQUEST-UPLOAD-CLASS"

        result = obj.setRequestUploadClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestUploadClassRef() is ref  # None is a no-op

    def test_create_diagnostic_request_upload(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestUploadServices")
        element = package.createDiagnosticRequestUpload("RequestUploadService1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestUpload)
        assert element.getShortName() == "RequestUploadService1"
        assert package.getReferrableElement("RequestUploadService1", DiagnosticRequestUpload) is element

        duplicate = package.createDiagnosticRequestUpload("RequestUploadService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestUpload.getRequestUploadClassRef.__doc__) == self.REQUEST_UPLOAD_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticRequestUpload.setRequestUploadClassRef.__doc__) == (
            self.REQUEST_UPLOAD_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestUploadClassRef."
        )


class TestDiagnosticRequestFileTransfer:
    """
    Test class for DiagnosticRequestFileTransfer functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.125, p.147
    """

    CLASS_NOTE = "This diagnostic service instance implements the UDS service 0x38. Tags: atp.recommendedPackage=DiagnosticRequestFileTransfers"
    REQUEST_FILE_TRANSFER_CLASS_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestFileTransfer in the given context."

    def _make_obj(self) -> DiagnosticRequestFileTransfer:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestFileTransfer(ar_root, "TestRequestFileTransfer")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestFileTransfer instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestRequestFileTransfer"
        assert isinstance(obj, ARElement)
        assert obj.getRequestFileTransferClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestFileTransfer.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestFileTransfer.__init__.__doc__ is None

    def test_get_set_request_file_transfer_class_ref(self):
        """
        Round-trips the requestFileTransferClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestFileTransferClasses/Class1")
        result = obj.setRequestFileTransferClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestFileTransferClassRef() is ref
        assert obj.getRequestFileTransferClassRef().getValue() == "/AUTOSAR/DiagnosticRequestFileTransferClasses/Class1"
        assert obj.getRequestFileTransferClassRef().getDest() == "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS"

        result = obj.setRequestFileTransferClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestFileTransferClassRef() is ref  # None is a no-op

    def test_create_diagnostic_request_file_transfer(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestFileTransferServices")
        element = package.createDiagnosticRequestFileTransfer("RequestFileTransferService1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestFileTransfer)
        assert element.getShortName() == "RequestFileTransferService1"
        assert package.getReferrableElement("RequestFileTransferService1", DiagnosticRequestFileTransfer) is element

        duplicate = package.createDiagnosticRequestFileTransfer("RequestFileTransferService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestFileTransfer.getRequestFileTransferClassRef.__doc__) == self.REQUEST_FILE_TRANSFER_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticRequestFileTransfer.setRequestFileTransferClassRef.__doc__) == (
            self.REQUEST_FILE_TRANSFER_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestFileTransferClassRef."
        )


class TestDiagnosticParameterIdentifier:
    """
    Test class for DiagnosticParameterIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.127, p.149
    """

    CLASS_NOTE = "This meta-class represents the ability to model a diagnostic parameter identifier (PID) for the purpose of executing on-board diagnostics (OBD). Tags: atp.recommendedPackage=DiagnosticParameterIdentifiers"
    DATA_ELEMENT_NOTE = "This represents the data carried by the DiagnosticParameterIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName, dataElement.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    ID_NOTE = "This is the numerical identifier used to identify the DiagnosticParameterIdentifier in the scope of diagnostic workflow (see SAE J1979-DA)."
    PID_SIZE_NOTE = "The size of the entire PID can be greater than the sum of the data elements because padding might be applied. Unit: byte."
    SUPPORT_INFO_BYTE_NOTE = "This represents the supported information associated with the DiagnosticParameterIdentifier."

    def _make_obj(self) -> DiagnosticParameterIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticParameterIdentifier(ar_root, "TestParameterIdentifier")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticParameterIdentifier instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestParameterIdentifier"
        assert isinstance(obj, ARElement)
        assert obj.getDataElements() == []
        assert obj.getId() is None
        assert obj.getPidSize() is None
        assert obj.getSupportInfoByte() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticParameterIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticParameterIdentifier.__init__.__doc__ is None

    def test_add_get_data_elements(self):
        """
        Appends DiagnosticParameter data elements; None is a no-op.
        """
        obj = self._make_obj()

        data_element = DiagnosticParameter()
        result = obj.addDataElement(data_element)
        assert result is obj  # method chaining
        assert obj.getDataElements() == [data_element]

        result = obj.addDataElement(None)
        assert result is obj  # None is a no-op
        assert obj.getDataElements() == [data_element]

    def test_get_set_id(self):
        """
        Round-trips the id; None is a no-op.
        """
        obj = self._make_obj()

        id_value = PositiveInteger()
        id_value.setValue("4")
        result = obj.setId(id_value)
        assert result is obj  # method chaining
        assert obj.getId() is id_value
        assert obj.getId().getValue() == 4

        result = obj.setId(None)
        assert result is obj  # method chaining with None
        assert obj.getId() is id_value  # None is a no-op

    def test_get_set_pid_size(self):
        """
        Round-trips the pidSize; None is a no-op.
        """
        obj = self._make_obj()

        pid_size = PositiveInteger()
        pid_size.setValue("6")
        result = obj.setPidSize(pid_size)
        assert result is obj  # method chaining
        assert obj.getPidSize() is pid_size
        assert obj.getPidSize().getValue() == 6

        result = obj.setPidSize(None)
        assert result is obj  # method chaining with None
        assert obj.getPidSize() is pid_size  # None is a no-op

    def test_get_set_support_info_byte(self):
        """
        Round-trips the supportInfoByte; None is a no-op.
        """
        obj = self._make_obj()

        support_info_byte = DiagnosticSupportInfoByte()
        result = obj.setSupportInfoByte(support_info_byte)
        assert result is obj  # method chaining
        assert obj.getSupportInfoByte() is support_info_byte

        result = obj.setSupportInfoByte(None)
        assert result is obj  # method chaining with None
        assert obj.getSupportInfoByte() is support_info_byte  # None is a no-op

    def test_create_diagnostic_parameter_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticParameterIdentifiers")
        element = package.createDiagnosticParameterIdentifier("ParameterIdentifier1")

        assert element is not None
        assert isinstance(element, DiagnosticParameterIdentifier)
        assert element.getShortName() == "ParameterIdentifier1"
        assert package.getReferrableElement("ParameterIdentifier1", DiagnosticParameterIdentifier) is element

        duplicate = package.createDiagnosticParameterIdentifier("ParameterIdentifier1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticParameterIdentifier.getDataElements.__doc__) == self.DATA_ELEMENT_NOTE
        assert inspect.cleandoc(DiagnosticParameterIdentifier.addDataElement.__doc__) == (self.DATA_ELEMENT_NOTE + "\n\nA None value is a no-op and does not append a dataElement.")
        assert inspect.cleandoc(DiagnosticParameterIdentifier.getId.__doc__) == self.ID_NOTE
        assert inspect.cleandoc(DiagnosticParameterIdentifier.setId.__doc__) == (self.ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing id.")
        assert inspect.cleandoc(DiagnosticParameterIdentifier.getPidSize.__doc__) == self.PID_SIZE_NOTE
        assert inspect.cleandoc(DiagnosticParameterIdentifier.setPidSize.__doc__) == (self.PID_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing pidSize.")
        assert inspect.cleandoc(DiagnosticParameterIdentifier.getSupportInfoByte.__doc__) == self.SUPPORT_INFO_BYTE_NOTE
        assert inspect.cleandoc(DiagnosticParameterIdentifier.setSupportInfoByte.__doc__) == (
            self.SUPPORT_INFO_BYTE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing supportInfoByte."
        )


class TestDiagnosticRequestCurrentPowertrainData:
    """
    Test class for DiagnosticRequestCurrentPowertrainData functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.130, p.151
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x01 service. Tags: atp.recommendedPackage=DiagnosticRequestCurrentPowertrainDatas"
    PID_NOTE = "This represents the PID associated with this instance of the OBD mode 0x01 service."
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestCurrentPowertrainData in the given context."

    def _make_obj(self) -> DiagnosticRequestCurrentPowertrainData:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestCurrentPowertrainData(ar_root, "TestMode01")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestCurrentPowertrainData instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode01"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getPidRef() is None
        assert obj.getRequestCurrentPowertrainDiagnosticDataClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestCurrentPowertrainData.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestCurrentPowertrainData.__init__.__doc__ is None

    def test_get_set_pid_ref(self):
        """
        Round-trips the pid ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-PARAMETER-IDENTIFIER")
        ref.setValue("/AUTOSAR/DiagnosticParameterIdentifiers/Pid1")
        result = obj.setPidRef(ref)
        assert result is obj  # method chaining
        assert obj.getPidRef() is ref
        assert obj.getPidRef().getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"
        assert obj.getPidRef().getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"

        result = obj.setPidRef(None)
        assert result is obj  # method chaining with None
        assert obj.getPidRef() is ref  # None is a no-op

    def test_get_set_request_current_powertrain_diagnostic_data_class_ref(self):
        """
        Round-trips the requestCurrentPowertrainDiagnosticDataClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestCurrentPowertrainDataClasses/Class1")
        result = obj.setRequestCurrentPowertrainDiagnosticDataClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestCurrentPowertrainDiagnosticDataClassRef() is ref
        assert obj.getRequestCurrentPowertrainDiagnosticDataClassRef().getValue() == "/AUTOSAR/DiagnosticRequestCurrentPowertrainDataClasses/Class1"
        assert obj.getRequestCurrentPowertrainDiagnosticDataClassRef().getDest() == "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS"

        result = obj.setRequestCurrentPowertrainDiagnosticDataClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestCurrentPowertrainDiagnosticDataClassRef() is ref  # None is a no-op

    def test_create_diagnostic_request_current_powertrain_data(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode01Services")
        element = package.createDiagnosticRequestCurrentPowertrainData("Mode01Service1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestCurrentPowertrainData)
        assert element.getShortName() == "Mode01Service1"
        assert package.getReferrableElement("Mode01Service1", DiagnosticRequestCurrentPowertrainData) is element

        duplicate = package.createDiagnosticRequestCurrentPowertrainData("Mode01Service1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestCurrentPowertrainData.getPidRef.__doc__) == self.PID_NOTE
        assert inspect.cleandoc(DiagnosticRequestCurrentPowertrainData.setPidRef.__doc__) == (self.PID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing pidRef.")
        assert inspect.cleandoc(DiagnosticRequestCurrentPowertrainData.getRequestCurrentPowertrainDiagnosticDataClassRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticRequestCurrentPowertrainData.setRequestCurrentPowertrainDiagnosticDataClassRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestCurrentPowertrainDiagnosticDataClassRef."
        )


class TestDiagnosticRequestPowertrainFreezeFrameData:
    """
    Test class for DiagnosticRequestPowertrainFreezeFrameData functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.132, p.152
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x02 service. Tags: atp.recommendedPackage=DiagnosticPowertrainFreezeFrames"
    FREEZE_FRAME_NOTE = "This represents the associated freeze-frame."
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestPowertrainFreezeFrameData in the given context."

    def _make_obj(self) -> DiagnosticRequestPowertrainFreezeFrameData:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestPowertrainFreezeFrameData(ar_root, "TestMode02")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestPowertrainFreezeFrameData instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode02"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getFreezeFrameRef() is None
        assert obj.getRequestPowertrainFreezeFrameDataRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestPowertrainFreezeFrameData.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestPowertrainFreezeFrameData.__init__.__doc__ is None

    def test_get_set_freeze_frame_ref(self):
        """
        Round-trips the freezeFrame ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME")
        ref.setValue("/AUTOSAR/DiagnosticPowertrainFreezeFrames/Frame1")
        result = obj.setFreezeFrameRef(ref)
        assert result is obj  # method chaining
        assert obj.getFreezeFrameRef() is ref
        assert obj.getFreezeFrameRef().getValue() == "/AUTOSAR/DiagnosticPowertrainFreezeFrames/Frame1"
        assert obj.getFreezeFrameRef().getDest() == "DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME"

        result = obj.setFreezeFrameRef(None)
        assert result is obj  # method chaining with None
        assert obj.getFreezeFrameRef() is ref  # None is a no-op

    def test_get_set_request_powertrain_freeze_frame_data_ref(self):
        """
        Round-trips the requestPowertrainFreezeFrameData ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestPowertrainFreezeFrameDataClasses/Class1")
        result = obj.setRequestPowertrainFreezeFrameDataRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestPowertrainFreezeFrameDataRef() is ref
        assert obj.getRequestPowertrainFreezeFrameDataRef().getValue() == "/AUTOSAR/DiagnosticRequestPowertrainFreezeFrameDataClasses/Class1"
        assert obj.getRequestPowertrainFreezeFrameDataRef().getDest() == "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS"

        result = obj.setRequestPowertrainFreezeFrameDataRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestPowertrainFreezeFrameDataRef() is ref  # None is a no-op

    def test_create_diagnostic_request_powertrain_freeze_frame_data(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode02Services")
        element = package.createDiagnosticRequestPowertrainFreezeFrameData("Mode02Service1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestPowertrainFreezeFrameData)
        assert element.getShortName() == "Mode02Service1"
        assert package.getReferrableElement("Mode02Service1", DiagnosticRequestPowertrainFreezeFrameData) is element

        duplicate = package.createDiagnosticRequestPowertrainFreezeFrameData("Mode02Service1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestPowertrainFreezeFrameData.getFreezeFrameRef.__doc__) == self.FREEZE_FRAME_NOTE
        assert inspect.cleandoc(DiagnosticRequestPowertrainFreezeFrameData.setFreezeFrameRef.__doc__) == (
            self.FREEZE_FRAME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing freezeFrameRef."
        )
        assert inspect.cleandoc(DiagnosticRequestPowertrainFreezeFrameData.getRequestPowertrainFreezeFrameDataRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticRequestPowertrainFreezeFrameData.setRequestPowertrainFreezeFrameDataRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestPowertrainFreezeFrameDataRef."
        )


class TestDiagnosticPowertrainFreezeFrame:
    """
    Test class for DiagnosticPowertrainFreezeFrame functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.134, p.153
    """

    CLASS_NOTE = "This meta-class represents a powertrain-related freeze-frame. In theory, this meta-class would need an additional id attribute. However, legal regulations requires only a single value for this attribute anyway. Tags: atp.recommendedPackage=DiagnosticPowertrainFreezeFrames"
    PID_NOTE = "This represents the PID associated with this instance of the OBD mode 0x02 service."

    def _make_obj(self) -> DiagnosticPowertrainFreezeFrame:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticPowertrainFreezeFrame(ar_root, "TestFreezeFrame")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticPowertrainFreezeFrame instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFreezeFrame"
        assert isinstance(obj, ARElement)
        assert obj.getPidRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticPowertrainFreezeFrame.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticPowertrainFreezeFrame.__init__.__doc__ is None

    def test_add_get_pid_refs(self):
        """
        Appends pid refs; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-PARAMETER-IDENTIFIER")
        ref.setValue("/AUTOSAR/DiagnosticParameterIdentifiers/Pid1")
        result = obj.addPidRef(ref)
        assert result is obj  # method chaining
        assert obj.getPidRefs() == [ref]
        assert obj.getPidRefs()[0].getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"
        assert obj.getPidRefs()[0].getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"

        result = obj.addPidRef(None)
        assert result is obj  # None is a no-op
        assert obj.getPidRefs() == [ref]

    def test_create_diagnostic_powertrain_freeze_frame(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticPowertrainFreezeFrames")
        element = package.createDiagnosticPowertrainFreezeFrame("FreezeFrame1")

        assert element is not None
        assert isinstance(element, DiagnosticPowertrainFreezeFrame)
        assert element.getShortName() == "FreezeFrame1"
        assert package.getReferrableElement("FreezeFrame1", DiagnosticPowertrainFreezeFrame) is element

        duplicate = package.createDiagnosticPowertrainFreezeFrame("FreezeFrame1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticPowertrainFreezeFrame.getPidRefs.__doc__) == self.PID_NOTE
        assert inspect.cleandoc(DiagnosticPowertrainFreezeFrame.addPidRef.__doc__) == (self.PID_NOTE + "\n\nA None value is a no-op and does not append a pidRef.")


class TestDiagnosticRequestEmissionRelatedDTC:
    """
    Test class for DiagnosticRequestEmissionRelatedDTC functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.135, p.154
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x03/0x07 service. Tags: atp.recommendedPackage=DiagnosticRequestEmissionRelatedDTCs"
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTC in the given context."

    def _make_obj(self) -> DiagnosticRequestEmissionRelatedDTC:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestEmissionRelatedDTC(ar_root, "TestMode0307")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestEmissionRelatedDTC instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode0307"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getRequestEmissionRelatedDtcClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestEmissionRelatedDTC.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestEmissionRelatedDTC.__init__.__doc__ is None

    def test_get_set_request_emission_related_dtc_class_ref(self):
        """
        Round-trips the requestEmissionRelatedDtcClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestEmissionRelatedDTCClasses/Class1")
        result = obj.setRequestEmissionRelatedDtcClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestEmissionRelatedDtcClassRef() is ref
        assert obj.getRequestEmissionRelatedDtcClassRef().getValue() == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCClasses/Class1"
        assert obj.getRequestEmissionRelatedDtcClassRef().getDest() == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS"

        result = obj.setRequestEmissionRelatedDtcClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestEmissionRelatedDtcClassRef() is ref  # None is a no-op

    def test_create_diagnostic_request_emission_related_dtc(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode0307Services")
        element = package.createDiagnosticRequestEmissionRelatedDTC("Mode0307Service1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestEmissionRelatedDTC)
        assert element.getShortName() == "Mode0307Service1"
        assert package.getReferrableElement("Mode0307Service1", DiagnosticRequestEmissionRelatedDTC) is element

        duplicate = package.createDiagnosticRequestEmissionRelatedDTC("Mode0307Service1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestEmissionRelatedDTC.getRequestEmissionRelatedDtcClassRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticRequestEmissionRelatedDTC.setRequestEmissionRelatedDtcClassRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestEmissionRelatedDtcClassRef."
        )


class TestDiagnosticClearResetEmissionRelatedInfo:
    """
    Test class for DiagnosticClearResetEmissionRelatedInfo functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.137, p.155
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x04 service. Tags: atp.recommendedPackage=DiagnosticClearResetEmissionRelatedInfos"
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearResteEmissionRelatedInfo in the given context."

    def _make_obj(self) -> DiagnosticClearResetEmissionRelatedInfo:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticClearResetEmissionRelatedInfo(ar_root, "TestMode04")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticClearResetEmissionRelatedInfo instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode04"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getClearResetEmissionRelatedDiagnosticInfoClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticClearResetEmissionRelatedInfo.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticClearResetEmissionRelatedInfo.__init__.__doc__ is None

    def test_get_set_clear_reset_emission_related_diagnostic_info_class_ref(self):
        """
        Round-trips the clearResetEmissionRelatedDiagnosticInfoClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticClearResetEmissionRelatedInfoClasses/Class1")
        result = obj.setClearResetEmissionRelatedDiagnosticInfoClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getClearResetEmissionRelatedDiagnosticInfoClassRef() is ref
        assert obj.getClearResetEmissionRelatedDiagnosticInfoClassRef().getValue() == "/AUTOSAR/DiagnosticClearResetEmissionRelatedInfoClasses/Class1"
        assert obj.getClearResetEmissionRelatedDiagnosticInfoClassRef().getDest() == "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS"

        result = obj.setClearResetEmissionRelatedDiagnosticInfoClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getClearResetEmissionRelatedDiagnosticInfoClassRef() is ref  # None is a no-op

    def test_create_diagnostic_clear_reset_emission_related_info(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode04Services")
        element = package.createDiagnosticClearResetEmissionRelatedInfo("Mode04Service1")

        assert element is not None
        assert isinstance(element, DiagnosticClearResetEmissionRelatedInfo)
        assert element.getShortName() == "Mode04Service1"
        assert package.getReferrableElement("Mode04Service1", DiagnosticClearResetEmissionRelatedInfo) is element

        duplicate = package.createDiagnosticClearResetEmissionRelatedInfo("Mode04Service1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticClearResetEmissionRelatedInfo.getClearResetEmissionRelatedDiagnosticInfoClassRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticClearResetEmissionRelatedInfo.setClearResetEmissionRelatedDiagnosticInfoClassRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing clearResetEmissionRelatedDiagnosticInfoClassRef."
        )


class TestDiagnosticRequestOnBoardMonitoringTestResults:
    """
    Test class for DiagnosticRequestOnBoardMonitoringTestResults functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.139, p.156
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x06 service. Tags: atp.recommendedPackage=DiagnosticRequestOnBoardMonitoringTestResultss"
    TEST_RESULT_NOTE = "This reference identifies the applicable collection of test identifiers for setting up a request message for mode 0x06."
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestOnBoardMonitoringTestResults in the given context."

    def _make_obj(self) -> DiagnosticRequestOnBoardMonitoringTestResults:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestOnBoardMonitoringTestResults(ar_root, "TestMode06")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestOnBoardMonitoringTestResults instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode06"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getDiagnosticTestResultRefs() == []
        assert obj.getRequestOnBoardMonitoringTestResultsClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestOnBoardMonitoringTestResults.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestOnBoardMonitoringTestResults.__init__.__doc__ is None

    def test_add_get_diagnostic_test_result_refs(self):
        """
        Appends diagnosticTestResult refs; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-TEST-RESULT")
        ref.setValue("/AUTOSAR/DiagnosticTestResults/Test1")
        result = obj.addDiagnosticTestResultRef(ref)
        assert result is obj  # method chaining
        assert obj.getDiagnosticTestResultRefs() == [ref]
        assert obj.getDiagnosticTestResultRefs()[0].getValue() == "/AUTOSAR/DiagnosticTestResults/Test1"
        assert obj.getDiagnosticTestResultRefs()[0].getDest() == "DIAGNOSTIC-TEST-RESULT"

        result = obj.addDiagnosticTestResultRef(None)
        assert result is obj  # None is a no-op
        assert obj.getDiagnosticTestResultRefs() == [ref]

    def test_get_set_request_on_board_monitoring_test_results_class_ref(self):
        """
        Round-trips the requestOnBoardMonitoringTestResultsClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1")
        result = obj.setRequestOnBoardMonitoringTestResultsClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestOnBoardMonitoringTestResultsClassRef() is ref
        assert obj.getRequestOnBoardMonitoringTestResultsClassRef().getValue() == "/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1"
        assert obj.getRequestOnBoardMonitoringTestResultsClassRef().getDest() == "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS"

        result = obj.setRequestOnBoardMonitoringTestResultsClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestOnBoardMonitoringTestResultsClassRef() is ref  # None is a no-op

    def test_create_diagnostic_request_on_board_monitoring_test_results(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode06Services")
        element = package.createDiagnosticRequestOnBoardMonitoringTestResults("Mode06Service1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestOnBoardMonitoringTestResults)
        assert element.getShortName() == "Mode06Service1"
        assert package.getReferrableElement("Mode06Service1", DiagnosticRequestOnBoardMonitoringTestResults) is element

        duplicate = package.createDiagnosticRequestOnBoardMonitoringTestResults("Mode06Service1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestOnBoardMonitoringTestResults.getDiagnosticTestResultRefs.__doc__) == self.TEST_RESULT_NOTE
        assert inspect.cleandoc(DiagnosticRequestOnBoardMonitoringTestResults.addDiagnosticTestResultRef.__doc__) == (
            self.TEST_RESULT_NOTE + "\n\nA None value is a no-op and does not append a diagnosticTestResultRef."
        )
        assert inspect.cleandoc(DiagnosticRequestOnBoardMonitoringTestResults.getRequestOnBoardMonitoringTestResultsClassRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticRequestOnBoardMonitoringTestResults.setRequestOnBoardMonitoringTestResultsClassRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestOnBoardMonitoringTestResultsClassRef."
        )


class TestDiagnosticRequestControlOfOnBoardDevice:
    """
    Test class for DiagnosticRequestControlOfOnBoardDevice functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.141, p.157
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x08 service. Tags: atp.recommendedPackage=DiagnosticRequestControlOfOnBoardDevices"
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestControlOfOnBoardDevice in the given context."
    TEST_ID_NOTE = "This represents the test Id for the mode 0x08."

    def _make_obj(self) -> DiagnosticRequestControlOfOnBoardDevice:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestControlOfOnBoardDevice(ar_root, "TestMode08")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestControlOfOnBoardDevice instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode08"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getRequestControlOfOnBoardDeviceClassRef() is None
        assert obj.getTestIdRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestControlOfOnBoardDevice.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestControlOfOnBoardDevice.__init__.__doc__ is None

    def test_get_set_request_control_of_on_board_device_class_ref(self):
        """
        Round-trips the requestControlOfOnBoardDeviceClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestControlOfOnBoardDeviceClasses/Class1")
        result = obj.setRequestControlOfOnBoardDeviceClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestControlOfOnBoardDeviceClassRef() is ref
        assert obj.getRequestControlOfOnBoardDeviceClassRef().getValue() == "/AUTOSAR/DiagnosticRequestControlOfOnBoardDeviceClasses/Class1"
        assert obj.getRequestControlOfOnBoardDeviceClassRef().getDest() == "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS"

        result = obj.setRequestControlOfOnBoardDeviceClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestControlOfOnBoardDeviceClassRef() is ref  # None is a no-op

    def test_get_set_test_id_ref(self):
        """
        Round-trips the testId ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER")
        ref.setValue("/AUTOSAR/DiagnosticTestRoutineIdentifiers/Tid1")
        result = obj.setTestIdRef(ref)
        assert result is obj  # method chaining
        assert obj.getTestIdRef() is ref
        assert obj.getTestIdRef().getValue() == "/AUTOSAR/DiagnosticTestRoutineIdentifiers/Tid1"
        assert obj.getTestIdRef().getDest() == "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER"

        result = obj.setTestIdRef(None)
        assert result is obj  # method chaining with None
        assert obj.getTestIdRef() is ref  # None is a no-op

    def test_create_diagnostic_request_control_of_on_board_device(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode08Services")
        element = package.createDiagnosticRequestControlOfOnBoardDevice("Mode08Service1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestControlOfOnBoardDevice)
        assert element.getShortName() == "Mode08Service1"
        assert package.getReferrableElement("Mode08Service1", DiagnosticRequestControlOfOnBoardDevice) is element

        duplicate = package.createDiagnosticRequestControlOfOnBoardDevice("Mode08Service1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestControlOfOnBoardDevice.getRequestControlOfOnBoardDeviceClassRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticRequestControlOfOnBoardDevice.setRequestControlOfOnBoardDeviceClassRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestControlOfOnBoardDeviceClassRef."
        )
        assert inspect.cleandoc(DiagnosticRequestControlOfOnBoardDevice.getTestIdRef.__doc__) == self.TEST_ID_NOTE
        assert inspect.cleandoc(DiagnosticRequestControlOfOnBoardDevice.setTestIdRef.__doc__) == (self.TEST_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing testIdRef.")


class TestDiagnosticTestResult:
    """
    Test class for DiagnosticTestResult functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.201, p.204
    """

    CLASS_NOTE = (
        "This meta-class represents the ability to define diagnostic test results. Tags: atp.recommendedPackage=DiagnosticTestResults\n"
        "\n"
        "[constr_1850] Existence of aggregation DiagnosticTestResult.testIdentifier: "
        "For each DiagnosticTestResult, the aggregation of meta-class DiagnosticTestIdentifier in the role testIdentifier shall exist at the time when the DEXT is complete.\n"
        "\n"
        "[constr_1851] Existence of reference DiagnosticTestResult.monitoredIdentifier: "
        "For each DiagnosticTestResult, the reference to meta-class DiagnosticTestIdentifier in the role monitoredIdentifier shall exist at the time when the DEXT is complete."
    )

    DIAGNOSTIC_EVENT_NOTE = (
        "This attribute represents the diagnostic event that is related to the diagnostic test result. "
        "Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticEvent.diagnosticEvent, diagnosticEvent.variationPoint.shortLabel vh.latestBindingTime=preCompileTime"
    )
    MONITORED_IDENTIFIER_NOTE = "This attribute represents the related diagnostic monitored identifier."
    TEST_IDENTIFIER_NOTE = "This attribute represents the applicable test identifier."
    UPDATE_KIND_NOTE = "This attribute controls the update behavior of the enclosing DiagnosticTestResult. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"

    def _make_obj(self) -> DiagnosticTestResult:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTestResult(ar_root, "TestResult1")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestResult1"
        assert isinstance(obj, DiagnosticTestResult)
        assert isinstance(obj, ARElement)
        assert obj.getDiagnosticEventRef() is None
        assert obj.getMonitoredIdentifierRef() is None
        assert obj.getTestIdentifier() is None
        assert obj.getUpdateKind() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (plus the class-level constraints).
        """
        assert inspect.cleandoc(DiagnosticTestResult.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTestResult.__init__.__doc__ is None

    def test_get_set_diagnostic_event_ref(self):
        """
        Round-trips the diagnosticEventRef; None is a no-op.
        """
        obj = self._make_obj()
        ref = RefType().setValue("/DiagnosticTestResults/DiagnosticEvent1")

        result = obj.setDiagnosticEventRef(ref)
        assert result is obj  # method chaining
        assert obj.getDiagnosticEventRef() is ref
        assert obj.getDiagnosticEventRef().getValue() == "/DiagnosticTestResults/DiagnosticEvent1"

        result = obj.setDiagnosticEventRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDiagnosticEventRef() is ref  # None is a no-op

    def test_get_set_monitored_identifier_ref(self):
        """
        Round-trips the monitoredIdentifierRef; None is a no-op.
        """
        obj = self._make_obj()
        ref = RefType().setValue("/DiagnosticTestResults/DiagnosticMeasurementIdentifier1")

        result = obj.setMonitoredIdentifierRef(ref)
        assert result is obj  # method chaining
        assert obj.getMonitoredIdentifierRef() is ref
        assert obj.getMonitoredIdentifierRef().getValue() == "/DiagnosticTestResults/DiagnosticMeasurementIdentifier1"

        result = obj.setMonitoredIdentifierRef(None)
        assert result is obj  # method chaining with None
        assert obj.getMonitoredIdentifierRef() is ref  # None is a no-op

    def test_get_set_test_identifier(self):
        """
        Round-trips the aggregated testIdentifier; None is a no-op.
        """
        obj = self._make_obj()
        identifier = DiagnosticTestIdentifier()
        identifier_id = PositiveInteger()
        identifier_id.setValue(4)
        identifier.setId(identifier_id)

        result = obj.setTestIdentifier(identifier)
        assert result is obj  # method chaining
        assert obj.getTestIdentifier() is identifier

        result = obj.setTestIdentifier(None)
        assert result is obj  # method chaining with None
        assert obj.getTestIdentifier() is identifier  # None is a no-op

    def test_get_set_update_kind(self):
        """
        Round-trips the updateKind enum; None is a no-op.
        """
        obj = self._make_obj()
        update_kind = DiagnosticTestResultUpdateEnum()
        update_kind.setValue(DiagnosticTestResultUpdateEnum.STEADY)

        result = obj.setUpdateKind(update_kind)
        assert result is obj  # method chaining
        assert obj.getUpdateKind() is update_kind
        assert obj.getUpdateKind().getValue() == DiagnosticTestResultUpdateEnum.STEADY

        result = obj.setUpdateKind(None)
        assert result is obj  # method chaining with None
        assert obj.getUpdateKind() is update_kind  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticTestResult.getDiagnosticEventRef.__doc__) == self.DIAGNOSTIC_EVENT_NOTE
        assert inspect.cleandoc(DiagnosticTestResult.setDiagnosticEventRef.__doc__) == (
            self.DIAGNOSTIC_EVENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing diagnosticEventRef."
        )
        assert inspect.cleandoc(DiagnosticTestResult.getMonitoredIdentifierRef.__doc__) == self.MONITORED_IDENTIFIER_NOTE
        assert inspect.cleandoc(DiagnosticTestResult.setMonitoredIdentifierRef.__doc__) == (
            self.MONITORED_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing monitoredIdentifierRef."
        )
        assert inspect.cleandoc(DiagnosticTestResult.getTestIdentifier.__doc__) == self.TEST_IDENTIFIER_NOTE
        assert inspect.cleandoc(DiagnosticTestResult.setTestIdentifier.__doc__) == (self.TEST_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing testIdentifier.")
        assert inspect.cleandoc(DiagnosticTestResult.getUpdateKind.__doc__) == self.UPDATE_KIND_NOTE
        assert inspect.cleandoc(DiagnosticTestResult.setUpdateKind.__doc__) == (self.UPDATE_KIND_NOTE + "\n\nA None value is a no-op and does not overwrite an existing updateKind.")

    def test_create_diagnostic_test_result(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTestResults")
        element = package.createDiagnosticTestResult("TestResult1")

        assert element is not None
        assert isinstance(element, DiagnosticTestResult)
        assert element.getShortName() == "TestResult1"
        assert package.getReferrableElement("TestResult1", DiagnosticTestResult) is element

        duplicate = package.createDiagnosticTestResult("TestResult1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticTestRoutineIdentifier:
    """
    Test class for DiagnosticTestRoutineIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.143, p.158
    """

    CLASS_NOTE = "This represents the test id of the DiagnosticTestIdentifier. Tags: atp.recommendedPackage=DiagnosticTestRoutineIdentifier"
    ID_NOTE = "This represents the numerical id of the DiagnosticTestIdentifier (see SAE J1979-DA)."
    REQUEST_DATA_SIZE_NOTE = "This represents the specified data size for the request message. Unit: byte."
    RESPONSE_DATA_SIZE_NOTE = "This represents the specified data size for the response message. Unit:byte."

    def _make_obj(self) -> DiagnosticTestRoutineIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticTestRoutineIdentifier(ar_root, "TestRoutine1")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticTestRoutineIdentifier instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestRoutine1"
        assert isinstance(obj, ARElement)
        assert obj.getId() is None
        assert obj.getRequestDataSize() is None
        assert obj.getResponseDataSize() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticTestRoutineIdentifier.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTestRoutineIdentifier.__init__.__doc__ is None

    def test_get_set_id(self):
        """
        Round-trips the id; None is a no-op.
        """
        obj = self._make_obj()

        id_value = PositiveInteger()
        id_value.setValue("1")
        result = obj.setId(id_value)
        assert result is obj  # method chaining
        assert obj.getId() is id_value
        assert obj.getId().getValue() == 1

        result = obj.setId(None)
        assert result is obj  # method chaining with None
        assert obj.getId() is id_value  # None is a no-op

    def test_get_set_request_data_size(self):
        """
        Round-trips the requestDataSize; None is a no-op.
        """
        obj = self._make_obj()

        size = PositiveInteger()
        size.setValue("8")
        result = obj.setRequestDataSize(size)
        assert result is obj  # method chaining
        assert obj.getRequestDataSize() is size
        assert obj.getRequestDataSize().getValue() == 8

        result = obj.setRequestDataSize(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestDataSize() is size  # None is a no-op

    def test_get_set_response_data_size(self):
        """
        Round-trips the responseDataSize; None is a no-op.
        """
        obj = self._make_obj()

        size = PositiveInteger()
        size.setValue("16")
        result = obj.setResponseDataSize(size)
        assert result is obj  # method chaining
        assert obj.getResponseDataSize() is size
        assert obj.getResponseDataSize().getValue() == 16

        result = obj.setResponseDataSize(None)
        assert result is obj  # method chaining with None
        assert obj.getResponseDataSize() is size  # None is a no-op

    def test_create_diagnostic_test_routine_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTestRoutineIdentifiers")
        element = package.createDiagnosticTestRoutineIdentifier("RoutineIdentifier1")

        assert element is not None
        assert isinstance(element, DiagnosticTestRoutineIdentifier)
        assert element.getShortName() == "RoutineIdentifier1"
        assert package.getReferrableElement("RoutineIdentifier1", DiagnosticTestRoutineIdentifier) is element

        duplicate = package.createDiagnosticTestRoutineIdentifier("RoutineIdentifier1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticTestRoutineIdentifier.getId.__doc__) == self.ID_NOTE
        assert inspect.cleandoc(DiagnosticTestRoutineIdentifier.setId.__doc__) == (self.ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing id.")
        assert inspect.cleandoc(DiagnosticTestRoutineIdentifier.getRequestDataSize.__doc__) == self.REQUEST_DATA_SIZE_NOTE
        assert inspect.cleandoc(DiagnosticTestRoutineIdentifier.setRequestDataSize.__doc__) == (
            self.REQUEST_DATA_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestDataSize."
        )
        assert inspect.cleandoc(DiagnosticTestRoutineIdentifier.getResponseDataSize.__doc__) == self.RESPONSE_DATA_SIZE_NOTE
        assert inspect.cleandoc(DiagnosticTestRoutineIdentifier.setResponseDataSize.__doc__) == (
            self.RESPONSE_DATA_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing responseDataSize."
        )


class TestDiagnosticRequestVehicleInfo:
    """
    Test class for DiagnosticRequestVehicleInfo functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.144, p.160
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x09 service. Tags: atp.recommendedPackage=DiagnosticRequestVehicleInfos"
    INFO_TYPE_NOTE = "This represents the info type associated with the mode 0x09 service."
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequesVehicleInfo in the given context."

    def _make_obj(self) -> DiagnosticRequestVehicleInfo:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestVehicleInfo(ar_root, "TestMode09")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestVehicleInfo instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode09"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getInfoTypeRef() is None
        assert obj.getRequestVehicleInformationClassRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestVehicleInfo.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestVehicleInfo.__init__.__doc__ is None

    def test_get_set_info_type_ref(self):
        """
        Round-trips the infoType ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-INFO-TYPE")
        ref.setValue("/AUTOSAR/DiagnosticInfoTypes/InfoType1")
        result = obj.setInfoTypeRef(ref)
        assert result is obj  # method chaining
        assert obj.getInfoTypeRef() is ref
        assert obj.getInfoTypeRef().getValue() == "/AUTOSAR/DiagnosticInfoTypes/InfoType1"
        assert obj.getInfoTypeRef().getDest() == "DIAGNOSTIC-INFO-TYPE"

        result = obj.setInfoTypeRef(None)
        assert result is obj  # method chaining with None
        assert obj.getInfoTypeRef() is ref  # None is a no-op

    def test_get_set_request_vehicle_information_class_ref(self):
        """
        Round-trips the requestVehicleInformationClass ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestVehicleInfoClasses/Class1")
        result = obj.setRequestVehicleInformationClassRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestVehicleInformationClassRef() is ref
        assert obj.getRequestVehicleInformationClassRef().getValue() == "/AUTOSAR/DiagnosticRequestVehicleInfoClasses/Class1"
        assert obj.getRequestVehicleInformationClassRef().getDest() == "DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS"

        result = obj.setRequestVehicleInformationClassRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestVehicleInformationClassRef() is ref  # None is a no-op

    def test_create_diagnostic_request_vehicle_info(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode09Services")
        element = package.createDiagnosticRequestVehicleInfo("Mode09Service1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestVehicleInfo)
        assert element.getShortName() == "Mode09Service1"
        assert package.getReferrableElement("Mode09Service1", DiagnosticRequestVehicleInfo) is element

        duplicate = package.createDiagnosticRequestVehicleInfo("Mode09Service1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestVehicleInfo.getInfoTypeRef.__doc__) == self.INFO_TYPE_NOTE
        assert inspect.cleandoc(DiagnosticRequestVehicleInfo.setInfoTypeRef.__doc__) == (self.INFO_TYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing infoTypeRef.")
        assert inspect.cleandoc(DiagnosticRequestVehicleInfo.getRequestVehicleInformationClassRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticRequestVehicleInfo.setRequestVehicleInformationClassRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestVehicleInformationClassRef."
        )


class TestDiagnosticInfoType:
    """
    Test class for DiagnosticInfoType functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.146, p.160
    """

    CLASS_NOTE = "This meta-class represents the ability to model an OBD info type. Tags: atp.recommendedPackage=DiagnosticInfoTypes"
    DATA_ELEMENT_NOTE = "This represents the data associated with the enclosing DiagnosticInfoType. Stereotypes: atpSplitable Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName"
    ID_NOTE = "This attribute represents the value of InfoType (see SAE J1979-DA)."

    def _make_obj(self) -> DiagnosticInfoType:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticInfoType(ar_root, "TestInfoType")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticInfoType instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestInfoType"
        assert isinstance(obj, ARElement)
        assert obj.getDataElements() == []
        assert obj.getId() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticInfoType.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticInfoType.__init__.__doc__ is None

    def test_add_get_data_elements(self):
        """
        Appends DiagnosticParameter data elements; None is a no-op.
        """
        obj = self._make_obj()

        data_element = DiagnosticParameter()
        result = obj.addDataElement(data_element)
        assert result is obj  # method chaining
        assert obj.getDataElements() == [data_element]

        result = obj.addDataElement(None)
        assert result is obj  # None is a no-op
        assert obj.getDataElements() == [data_element]

    def test_get_set_id(self):
        """
        Round-trips the id; None is a no-op.
        """
        obj = self._make_obj()

        id_value = PositiveInteger()
        id_value.setValue("6")
        result = obj.setId(id_value)
        assert result is obj  # method chaining
        assert obj.getId() is id_value
        assert obj.getId().getValue() == 6

        result = obj.setId(None)
        assert result is obj  # method chaining with None
        assert obj.getId() is id_value  # None is a no-op

    def test_create_diagnostic_info_type(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticInfoTypes")
        element = package.createDiagnosticInfoType("InfoType1")

        assert element is not None
        assert isinstance(element, DiagnosticInfoType)
        assert element.getShortName() == "InfoType1"
        assert package.getReferrableElement("InfoType1", DiagnosticInfoType) is element

        duplicate = package.createDiagnosticInfoType("InfoType1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticInfoType.getDataElements.__doc__) == self.DATA_ELEMENT_NOTE
        assert inspect.cleandoc(DiagnosticInfoType.addDataElement.__doc__) == (self.DATA_ELEMENT_NOTE + "\n\nA None value is a no-op and does not append a dataElement.")
        assert inspect.cleandoc(DiagnosticInfoType.getId.__doc__) == self.ID_NOTE
        assert inspect.cleandoc(DiagnosticInfoType.setId.__doc__) == (self.ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing id.")


class TestDiagnosticAbstractAliasEvent:
    """
    Test class for DiagnosticAbstractAliasEvent functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.213, p.214
    (abstract base with no own attributes; exercised through the concrete subclass DiagnosticFimAliasEventGroup)
    """

    CLASS_NOTE = "This meta-class represents an abstract base class for all diagnostic alias events."

    def _make_obj(self) -> DiagnosticFimAliasEventGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFimAliasEventGroup(ar_root, "TestAliasEvent")

    def test_initialization(self):
        """
        Test that a concrete subclass initializes through the abstract base with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestAliasEvent"
        assert isinstance(obj, DiagnosticAbstractAliasEvent)
        assert isinstance(obj, ARElement)
        assert obj.getGroupedAliasEventRefs() == []

    def test_abstract_instantiation_raises(self):
        """
        Test that the abstract DiagnosticAbstractAliasEvent cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticAbstractAliasEvent(AUTOSAR.getInstance(), "DirectInstance")

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticAbstractAliasEvent.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAbstractAliasEvent.__init__.__doc__ is None


class TestDiagnosticAging:
    """
    Test class for DiagnosticAging functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.198, p.202
    """

    CLASS_NOTE = "Defines the aging algorithm. Tags: atp.recommendedPackage=DiagnosticAgings"
    AGING_CYCLE_NOTE = "This represents the applicable aging cycle."
    THRESHOLD_NOTE = "Number of aging cycles needed to unlearn/delete the event."
    CONSTR_1848 = "[constr_1848] Existence of attribute DiagnosticAging.agingCycle: For each DiagnosticAging, attribute agingCycle shall exist at the time when the DEXT is complete."
    CONSTR_1849 = "[constr_1849] Existence of attribute DiagnosticAging.threshold: For each DiagnosticAging, attribute threshold shall exist at the time when the DEXT is complete."

    def _make_obj(self) -> DiagnosticAging:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticAging(ar_root, "TestAging")

    def test_initialization(self):
        """
        Test that a concrete DiagnosticAging instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestAging"
        assert isinstance(obj, ARElement)
        assert obj.getAgingCycleRef() is None
        assert obj.getThreshold() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (plus the class constr rows).
        """
        assert inspect.cleandoc(DiagnosticAging.__doc__) == (self.CLASS_NOTE + "\n\n" + self.CONSTR_1848 + "\n" + self.CONSTR_1849)

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAging.__init__.__doc__ is None

    def test_get_set_aging_cycle_ref(self):
        """
        Round-trips the agingCycleRef; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-OPERATION-CYCLE")
        ref.setValue("/AUTOSAR/DiagnosticOperationCycles/Cycle1")
        result = obj.setAgingCycleRef(ref)
        assert result is obj  # method chaining
        assert obj.getAgingCycleRef() is ref

        result = obj.setAgingCycleRef(None)
        assert result is obj  # method chaining with None
        assert obj.getAgingCycleRef() is ref  # None is a no-op

    def test_get_set_threshold(self):
        """
        Round-trips the threshold; None is a no-op.
        """
        obj = self._make_obj()

        threshold = PositiveInteger()
        threshold.setValue("5")
        result = obj.setThreshold(threshold)
        assert result is obj  # method chaining
        assert obj.getThreshold() is threshold
        assert obj.getThreshold().getValue() == 5

        result = obj.setThreshold(None)
        assert result is obj  # method chaining with None
        assert obj.getThreshold() is threshold  # None is a no-op

    def test_create_diagnostic_aging(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticAgings")
        element = package.createDiagnosticAging("Aging1")

        assert element is not None
        assert isinstance(element, DiagnosticAging)
        assert element.getShortName() == "Aging1"
        assert package.getReferrableElement("Aging1", DiagnosticAging) is element

        duplicate = package.createDiagnosticAging("Aging1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticAging.getAgingCycleRef.__doc__) == self.AGING_CYCLE_NOTE
        assert inspect.cleandoc(DiagnosticAging.setAgingCycleRef.__doc__) == (self.AGING_CYCLE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing agingCycleRef.")
        assert inspect.cleandoc(DiagnosticAging.getThreshold.__doc__) == self.THRESHOLD_NOTE
        assert inspect.cleandoc(DiagnosticAging.setThreshold.__doc__) == (self.THRESHOLD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing threshold.")


class TestDiagnosticCondition:
    """
    Test class for DiagnosticCondition functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.184, p.194

    DiagnosticCondition is abstract (spec marks it "(abstract)"; subclasses:
    DiagnosticEnableCondition, DiagnosticStorageCondition), so __init__ defaults
    and base accessors are exercised through the concrete subclass stub
    DiagnosticEnableCondition (Rule 0006 abstract-class clause).
    """

    CLASS_NOTE = "Abstract element for StorageConditions and EnableConditions."
    INIT_VALUE_NOTE = "Defines the initial status for enable or disable of acceptance/storage of event reports of a diagnostic event. The value is the initialization after power up (before this condition is reported the first time). true: acceptance/storage of a diagnostic event enabled false: acceptance/storage of a diagnostic event disabled"

    def _make_obj(self) -> DiagnosticEnableCondition:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEnableCondition(ar_root, "TestCondition")

    def test_abstract_instantiation_blocked(self):
        """
        Test that instantiating the abstract DiagnosticCondition directly raises TypeError.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")

        with pytest.raises(TypeError):
            DiagnosticCondition(ar_root, "DirectCondition")

    def test_initialization(self):
        """
        Test that a concrete subclass instantiates with the spec defaults and the most-derived base.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestCondition"
        assert isinstance(obj, DiagnosticCondition)
        assert isinstance(obj, DiagnosticCommonElement)
        assert isinstance(obj, ARElement)
        assert obj.getInitValue() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticCondition.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticCondition.__init__.__doc__ is None

    def test_get_set_init_value(self):
        """
        Round-trips the initValue; None is a no-op.
        """
        obj = self._make_obj()

        init_value = Boolean().setValue(True)
        result = obj.setInitValue(init_value)
        assert result is obj  # method chaining
        assert obj.getInitValue() is init_value
        assert obj.getInitValue().value is True

        result = obj.setInitValue(None)
        assert result is obj  # method chaining with None
        assert obj.getInitValue() is init_value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticCondition.getInitValue.__doc__) == self.INIT_VALUE_NOTE
        assert inspect.cleandoc(DiagnosticCondition.setInitValue.__doc__) == (self.INIT_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing initValue.")


class TestDiagnosticConditionGroup:
    """
    Test class for DiagnosticConditionGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.193, p.200

    DiagnosticConditionGroup is abstract (spec marks it "(abstract)"; subclasses:
    DiagnosticEnableConditionGroup, DiagnosticStorageConditionGroup) and its table
    carries no Attribute rows (the XSD group DIAGNOSTIC-CONDITION-GROUP is an empty
    sequence), so __init__ defaults and the base chain are exercised through the
    concrete subclass stub DiagnosticEnableConditionGroup (Rule 0006 abstract-class
    clause).
    """

    CLASS_NOTE = "Abstract element for StorageConditionGroups and EnableConditionGroups."

    def _make_obj(self) -> DiagnosticEnableConditionGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEnableConditionGroup(ar_root, "TestConditionGroup")

    def test_abstract_instantiation_blocked(self):
        """
        Test that instantiating the abstract DiagnosticConditionGroup directly raises TypeError.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")

        with pytest.raises(TypeError):
            DiagnosticConditionGroup(ar_root, "DirectConditionGroup")

    def test_initialization(self):
        """
        Test that a concrete subclass instantiates with the most-derived base chain and no own fields.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestConditionGroup"
        assert isinstance(obj, DiagnosticConditionGroup)
        assert isinstance(obj, DiagnosticCommonElement)
        assert isinstance(obj, ARElement)

    def test_storage_condition_group_subclass_instantiates(self):
        """
        Test that the second subclass stub DiagnosticStorageConditionGroup instantiates through the base too.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = DiagnosticStorageConditionGroup(ar_root, "StorageGroup")

        assert obj.getShortName() == "StorageGroup"
        assert isinstance(obj, DiagnosticConditionGroup)
        assert isinstance(obj, DiagnosticCommonElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticConditionGroup.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticConditionGroup.__init__.__doc__ is None


class TestDiagnosticEnableCondition:
    """
    Test class for DiagnosticEnableCondition functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.185, p.194

    DiagnosticEnableCondition is concrete but its table carries no Attribute rows
    (the XSD group DIAGNOSTIC-ENABLE-CONDITION is an empty sequence) — every field
    (initValue) is inherited from the abstract base DiagnosticCondition
    (Table 4.184), so defaults and the base accessors are exercised on the
    concrete class itself.
    """

    CLASS_NOTE = "Specification of an enable condition. Tags: atp.recommendedPackage=DiagnosticConditions"

    def _make_obj(self) -> DiagnosticEnableCondition:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEnableCondition(ar_root, "TestEnableCondition")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and the inherited defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEnableCondition"
        assert isinstance(obj, DiagnosticEnableCondition)
        assert isinstance(obj, DiagnosticCondition)
        assert isinstance(obj, DiagnosticCommonElement)
        assert isinstance(obj, ARElement)
        assert obj.getInitValue() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticEnableCondition.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEnableCondition.__init__.__doc__ is None

    def test_get_set_init_value(self):
        """
        Round-trips the inherited initValue; None is a no-op.
        """
        obj = self._make_obj()

        init_value = Boolean().setValue(True)
        result = obj.setInitValue(init_value)
        assert result is obj  # method chaining
        assert obj.getInitValue() is init_value
        assert obj.getInitValue().value is True

        result = obj.setInitValue(None)
        assert result is obj  # method chaining with None
        assert obj.getInitValue() is init_value  # None is a no-op

    def test_create_diagnostic_enable_condition(self):
        """
        Test that ARPackage.createDiagnosticEnableCondition appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticEnableCondition("EnableCondition1")

        assert isinstance(obj, DiagnosticEnableCondition)
        assert obj.getShortName() == "EnableCondition1"
        assert ar_root.getReferrableElement("EnableCondition1", DiagnosticEnableCondition) is obj

        duplicate = ar_root.createDiagnosticEnableCondition("EnableCondition1")
        assert duplicate is obj


class TestDiagnosticStorageCondition:
    """
    Test class for DiagnosticStorageCondition functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.186, p.194

    DiagnosticStorageCondition is concrete but its table carries no Attribute rows
    (the XSD group DIAGNOSTIC-STORAGE-CONDITION is an empty sequence) — every field
    (initValue) is inherited from the abstract base DiagnosticCondition
    (Table 4.184), so defaults and the base accessors are exercised on the
    concrete class itself.
    """

    CLASS_NOTE = "Specification of a storage condition. Tags: atp.recommendedPackage=DiagnosticConditions"

    def _make_obj(self) -> DiagnosticStorageCondition:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticStorageCondition(ar_root, "TestStorageCondition")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and the inherited defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestStorageCondition"
        assert isinstance(obj, DiagnosticStorageCondition)
        assert isinstance(obj, DiagnosticCondition)
        assert isinstance(obj, DiagnosticCommonElement)
        assert isinstance(obj, ARElement)
        assert obj.getInitValue() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticStorageCondition.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticStorageCondition.__init__.__doc__ is None

    def test_get_set_init_value(self):
        """
        Round-trips the inherited initValue; None is a no-op.
        """
        obj = self._make_obj()

        init_value = Boolean().setValue(True)
        result = obj.setInitValue(init_value)
        assert result is obj  # method chaining
        assert obj.getInitValue() is init_value
        assert obj.getInitValue().value is True

        result = obj.setInitValue(None)
        assert result is obj  # method chaining with None
        assert obj.getInitValue() is init_value  # None is a no-op

    def test_create_diagnostic_storage_condition(self):
        """
        Test that ARPackage.createDiagnosticStorageCondition appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticStorageCondition("StorageCondition1")

        assert isinstance(obj, DiagnosticStorageCondition)
        assert obj.getShortName() == "StorageCondition1"
        assert ar_root.getReferrableElement("StorageCondition1", DiagnosticStorageCondition) is obj

        duplicate = ar_root.createDiagnosticStorageCondition("StorageCondition1")
        assert duplicate is obj


class TestDiagnosticEnableConditionGroup:
    """
    Test class for DiagnosticEnableConditionGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.194, p.200

    DiagnosticEnableConditionGroup is concrete (XSD complexType abstract="false")
    with a single Attribute row: enableCondition (DiagnosticEnableCondition, *, ref)
    — modeled as the enableConditionRefs list of RefType. Fields inherited from the
    abstract base DiagnosticConditionGroup (Table 4.193) carry no rows of their own.
    """

    CLASS_NOTE = (
        "Enable condition group which includes one or several enable conditions. "
        "Tags: atp.recommendedPackage=DiagnosticConditions\n"
        "\n"
        "[constr_1841] Existence of attribute DiagnosticEnableConditionGroup.enableCondition: "
        "For each DiagnosticEnableConditionGroup, attribute enableCondition shall exist "
        "at the time when the DEXT is complete."
    )

    def _make_obj(self) -> DiagnosticEnableConditionGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEnableConditionGroup(ar_root, "TestEnableConditionGroup")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEnableConditionGroup"
        assert isinstance(obj, DiagnosticEnableConditionGroup)
        assert isinstance(obj, DiagnosticConditionGroup)
        assert isinstance(obj, DiagnosticCommonElement)
        assert isinstance(obj, ARElement)
        assert obj.getEnableConditionRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim plus the class constraint.
        """
        assert inspect.cleandoc(DiagnosticEnableConditionGroup.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEnableConditionGroup.__init__.__doc__ is None

    def test_add_get_enable_condition_refs(self):
        """
        Round-trips enableCondition refs; None is a no-op and chaining returns self.
        """
        obj = self._make_obj()

        ref1 = RefType().setValue("/DiagnosticConditions/EnableCondition1")
        ref2 = RefType().setValue("/DiagnosticConditions/EnableCondition2")

        result = obj.addEnableConditionRef(ref1)
        assert result is obj  # method chaining
        obj.addEnableConditionRef(ref2)

        refs = obj.getEnableConditionRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
        assert refs[0].getValue() == "/DiagnosticConditions/EnableCondition1"
        assert refs[1].getValue() == "/DiagnosticConditions/EnableCondition2"

        result = obj.addEnableConditionRef(None)
        assert result is obj  # method chaining with None
        assert len(obj.getEnableConditionRefs()) == 2  # None is a no-op

    def test_create_diagnostic_enable_condition_group(self):
        """
        Test that ARPackage.createDiagnosticEnableConditionGroup appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticEnableConditionGroup("EnableConditionGroup1")

        assert isinstance(obj, DiagnosticEnableConditionGroup)
        assert obj.getShortName() == "EnableConditionGroup1"
        assert ar_root.getReferrableElement("EnableConditionGroup1", DiagnosticEnableConditionGroup) is obj

        duplicate = ar_root.createDiagnosticEnableConditionGroup("EnableConditionGroup1")
        assert duplicate is obj


class TestDiagnosticStorageConditionGroup:
    """
    Test class for DiagnosticStorageConditionGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.195, p.200

    DiagnosticStorageConditionGroup is concrete (XSD complexType abstract="false")
    with a single Attribute row: storageCondition (DiagnosticStorageCondition, *, ref)
    — modeled as the storageConditionRefs list of RefType. Fields inherited from the
    abstract base DiagnosticConditionGroup (Table 4.193) carry no rows of their own.
    """

    CLASS_NOTE = (
        "Storage condition group which includes one or several storage conditions. "
        "Tags: atp.recommendedPackage=DiagnosticConditions\n"
        "\n"
        "[constr_1842] Existence of DiagnosticStorageConditionGroup.storageCondition: "
        "For each DiagnosticStorageConditionGroup, attribute storageCondition shall exist "
        "at the time when the DEXT is complete."
    )

    def _make_obj(self) -> DiagnosticStorageConditionGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticStorageConditionGroup(ar_root, "TestStorageConditionGroup")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestStorageConditionGroup"
        assert isinstance(obj, DiagnosticStorageConditionGroup)
        assert isinstance(obj, DiagnosticConditionGroup)
        assert isinstance(obj, DiagnosticCommonElement)
        assert isinstance(obj, ARElement)
        assert obj.getStorageConditionRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim plus the class constraint.
        """
        assert inspect.cleandoc(DiagnosticStorageConditionGroup.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticStorageConditionGroup.__init__.__doc__ is None

    def test_add_get_storage_condition_refs(self):
        """
        Round-trips storageCondition refs; None is a no-op and chaining returns self.
        """
        obj = self._make_obj()

        ref1 = RefType().setValue("/DiagnosticConditions/StorageCondition1")
        ref2 = RefType().setValue("/DiagnosticConditions/StorageCondition2")

        result = obj.addStorageConditionRef(ref1)
        assert result is obj  # method chaining
        obj.addStorageConditionRef(ref2)

        refs = obj.getStorageConditionRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
        assert refs[0].getValue() == "/DiagnosticConditions/StorageCondition1"
        assert refs[1].getValue() == "/DiagnosticConditions/StorageCondition2"

        result = obj.addStorageConditionRef(None)
        assert result is obj  # method chaining with None
        assert len(obj.getStorageConditionRefs()) == 2  # None is a no-op

    def test_create_diagnostic_storage_condition_group(self):
        """
        Test that ARPackage.createDiagnosticStorageConditionGroup appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticStorageConditionGroup("StorageConditionGroup1")

        assert isinstance(obj, DiagnosticStorageConditionGroup)
        assert obj.getShortName() == "StorageConditionGroup1"
        assert ar_root.getReferrableElement("StorageConditionGroup1", DiagnosticStorageConditionGroup) is obj

        duplicate = ar_root.createDiagnosticStorageConditionGroup("StorageConditionGroup1")
        assert duplicate is obj


class TestDiagnosticEvent:
    """
    Test class for DiagnosticEvent functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.149, p.165

    DiagnosticEvent is concrete (XSD complexType DIAGNOSTIC-EVENT abstract="false")
    with nine own Attribute rows in displayed order. The markdown table carries no
    class-level Note row — the class docstring is the XSD complexType documentation
    verbatim.
    """

    CLASS_NOTE = "This element is used to configure DiagnosticEvents."

    ASSOCIATED_EVENT_IDENTIFICATION_NOTE = "This attribute represents the identification number that is associated with the enclosing DiagnosticEvent and allows to identify it when placed into a snapshot record or extended data record storage. This value can be reported as internal data element in snapshot records or extended data records."
    CLEAR_EVENT_ALLOWED_BEHAVIOR_NOTE = "This attribute defines the resulting UDS status byte for the related event, which shall not be cleared according to the ClearEventAllowed callback"
    CONFIRMATION_THRESHOLD_NOTE = 'This attribute defines the number of operation cycles with a failed result before a confirmed DTC is set to 1. The semantic of this attribute is a by "1" increased value compared to the confirmation threshold of the "trip counter" mentioned in ISO 14229-1 in figure D.4. A value of "1" defines the immediate confirmation of the DTC along with the first reported failed. This is also sometimes called "zero trip DTC". A value of "2" defines a DTC confirmation in the operation cycle after the first occurred failed. A value of "2" is typically used in the US for OBD DTC confirmation. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime'
    CONNECTED_INDICATOR_NOTE = "Event specific description of Indicators. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=connectedIndicator.shortName, connectedIndicator.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    EVENT_CLEAR_ALLOWED_NOTE = 'This attribute defines whether the Dem has access to a "ClearEventAllowed" callback.'
    EVENT_KIND_NOTE = "This attribute is used to distinguish between SWC and BSW events."
    PRESTORAGE_FREEZE_FRAME_NOTE = "This attribute describes whether the Prestorage of FreezeFrames is supported by the assigned event or not. true: Prestorage of FreezeFrames is supported fFalse: Prestorage of FreezeFrames is not supported"
    PRESTORED_FREEZEFRAME_STORED_IN_NVM_NOTE = "If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestoredFreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm)"
    RECOVERABLE_IN_SAME_OPERATION_CYCLE_NOTE = "If the attribute is set to true then reporting PASSED will reset the indication of a failed test in the current operation cycle. If the attribute is set to false then reporting PASSED will be ignored and not lead to a reset of the indication of a failed test."

    def _make_obj(self) -> DiagnosticEvent:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEvent(ar_root, "TestEvent")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEvent"
        assert isinstance(obj, DiagnosticEvent)
        assert isinstance(obj, ARElement)
        assert obj.getAssociatedEventIdentification() is None
        assert obj.getClearEventAllowedBehavior() is None
        assert obj.getConfirmationThreshold() is None
        assert obj.getConnectedIndicators() == []
        assert obj.getEventClearAllowed() is None
        assert obj.getEventKind() is None
        assert obj.getPrestorageFreezeFrame() is None
        assert obj.getPrestoredFreezeframeStoredInNvm() is None
        assert obj.getRecoverableInSameOperationCycle() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticEvent.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEvent.__init__.__doc__ is None

    def test_get_set_associated_event_identification(self):
        """
        Round-trips associatedEventIdentification; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger().setValue(3)
        result = obj.setAssociatedEventIdentification(value)
        assert result is obj  # method chaining
        assert obj.getAssociatedEventIdentification() is value
        assert obj.getAssociatedEventIdentification().value == 3

        result = obj.setAssociatedEventIdentification(None)
        assert result is obj  # method chaining with None
        assert obj.getAssociatedEventIdentification() is value  # None is a no-op

    def test_get_set_clear_event_allowed_behavior(self):
        """
        Round-trips clearEventAllowedBehavior; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticClearEventAllowedBehaviorEnum().setValue(DiagnosticClearEventAllowedBehaviorEnum.NO_STATUS_BYTE_CHANGE)
        result = obj.setClearEventAllowedBehavior(value)
        assert result is obj  # method chaining
        assert obj.getClearEventAllowedBehavior() is value
        assert obj.getClearEventAllowedBehavior().getValue() == DiagnosticClearEventAllowedBehaviorEnum.NO_STATUS_BYTE_CHANGE

        result = obj.setClearEventAllowedBehavior(None)
        assert result is obj  # method chaining with None
        assert obj.getClearEventAllowedBehavior() is value  # None is a no-op

    def test_get_set_confirmation_threshold(self):
        """
        Round-trips confirmationThreshold; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger().setValue(2)
        result = obj.setConfirmationThreshold(value)
        assert result is obj  # method chaining
        assert obj.getConfirmationThreshold() is value
        assert obj.getConfirmationThreshold().value == 2

        result = obj.setConfirmationThreshold(None)
        assert result is obj  # method chaining with None
        assert obj.getConfirmationThreshold() is value  # None is a no-op

    def test_add_get_connected_indicators(self):
        """
        Round-trips the connectedIndicator aggregation; None is a no-op and chaining returns self.
        """
        obj = self._make_obj()

        indicator1 = DiagnosticConnectedIndicator()
        indicator2 = DiagnosticConnectedIndicator()

        result = obj.addConnectedIndicator(indicator1)
        assert result is obj  # method chaining
        obj.addConnectedIndicator(indicator2)

        indicators = obj.getConnectedIndicators()
        assert len(indicators) == 2
        assert indicators[0] is indicator1
        assert indicators[1] is indicator2

        result = obj.addConnectedIndicator(None)
        assert result is obj  # method chaining with None
        assert len(obj.getConnectedIndicators()) == 2  # None is a no-op

    def test_get_set_event_clear_allowed(self):
        """
        Round-trips eventClearAllowed; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticEventClearAllowedEnum().setValue(DiagnosticEventClearAllowedEnum.ALWAYS)
        result = obj.setEventClearAllowed(value)
        assert result is obj  # method chaining
        assert obj.getEventClearAllowed() is value
        assert obj.getEventClearAllowed().getValue() == "ALWAYS"

        result = obj.setEventClearAllowed(None)
        assert result is obj  # method chaining with None
        assert obj.getEventClearAllowed() is value  # None is a no-op

    def test_get_set_event_kind(self):
        """
        Round-trips eventKind; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticEventKindEnum().setValue(DiagnosticEventKindEnum.BSW)
        result = obj.setEventKind(value)
        assert result is obj  # method chaining
        assert obj.getEventKind() is value
        assert obj.getEventKind().getValue() == DiagnosticEventKindEnum.BSW

        result = obj.setEventKind(None)
        assert result is obj  # method chaining with None
        assert obj.getEventKind() is value  # None is a no-op

    def test_get_set_prestorage_freeze_frame(self):
        """
        Round-trips prestorageFreezeFrame; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean().setValue(True)
        result = obj.setPrestorageFreezeFrame(value)
        assert result is obj  # method chaining
        assert obj.getPrestorageFreezeFrame() is value
        assert obj.getPrestorageFreezeFrame().value is True

        result = obj.setPrestorageFreezeFrame(None)
        assert result is obj  # method chaining with None
        assert obj.getPrestorageFreezeFrame() is value  # None is a no-op

    def test_get_set_prestored_freezeframe_stored_in_nvm(self):
        """
        Round-trips prestoredFreezeframeStoredInNvm; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean().setValue(False)
        result = obj.setPrestoredFreezeframeStoredInNvm(value)
        assert result is obj  # method chaining
        assert obj.getPrestoredFreezeframeStoredInNvm() is value
        assert obj.getPrestoredFreezeframeStoredInNvm().value is False

        result = obj.setPrestoredFreezeframeStoredInNvm(None)
        assert result is obj  # method chaining with None
        assert obj.getPrestoredFreezeframeStoredInNvm() is value  # None is a no-op

    def test_get_set_recoverable_in_same_operation_cycle(self):
        """
        Round-trips recoverableInSameOperationCycle; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean().setValue(True)
        result = obj.setRecoverableInSameOperationCycle(value)
        assert result is obj  # method chaining
        assert obj.getRecoverableInSameOperationCycle() is value
        assert obj.getRecoverableInSameOperationCycle().value is True

        result = obj.setRecoverableInSameOperationCycle(None)
        assert result is obj  # method chaining with None
        assert obj.getRecoverableInSameOperationCycle() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that every accessor docstring is the spec Note verbatim (setters append the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticEvent.getAssociatedEventIdentification.__doc__) == self.ASSOCIATED_EVENT_IDENTIFICATION_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setAssociatedEventIdentification.__doc__) == (
            self.ASSOCIATED_EVENT_IDENTIFICATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing associatedEventIdentification."
        )
        assert inspect.cleandoc(DiagnosticEvent.getClearEventAllowedBehavior.__doc__) == self.CLEAR_EVENT_ALLOWED_BEHAVIOR_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setClearEventAllowedBehavior.__doc__) == (
            self.CLEAR_EVENT_ALLOWED_BEHAVIOR_NOTE + "\n\nA None value is a no-op and does not overwrite an existing clearEventAllowedBehavior."
        )
        assert inspect.cleandoc(DiagnosticEvent.getConfirmationThreshold.__doc__) == self.CONFIRMATION_THRESHOLD_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setConfirmationThreshold.__doc__) == (
            self.CONFIRMATION_THRESHOLD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing confirmationThreshold."
        )
        assert inspect.cleandoc(DiagnosticEvent.addConnectedIndicator.__doc__) == (self.CONNECTED_INDICATOR_NOTE + "\n\nA None value is a no-op and does not extend the connectedIndicators list.")
        assert inspect.cleandoc(DiagnosticEvent.getConnectedIndicators.__doc__) == self.CONNECTED_INDICATOR_NOTE
        assert inspect.cleandoc(DiagnosticEvent.getEventClearAllowed.__doc__) == self.EVENT_CLEAR_ALLOWED_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setEventClearAllowed.__doc__) == (self.EVENT_CLEAR_ALLOWED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventClearAllowed.")
        assert inspect.cleandoc(DiagnosticEvent.getEventKind.__doc__) == self.EVENT_KIND_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setEventKind.__doc__) == (self.EVENT_KIND_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventKind.")
        assert inspect.cleandoc(DiagnosticEvent.getPrestorageFreezeFrame.__doc__) == self.PRESTORAGE_FREEZE_FRAME_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setPrestorageFreezeFrame.__doc__) == (
            self.PRESTORAGE_FREEZE_FRAME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing prestorageFreezeFrame."
        )
        assert inspect.cleandoc(DiagnosticEvent.getPrestoredFreezeframeStoredInNvm.__doc__) == self.PRESTORED_FREEZEFRAME_STORED_IN_NVM_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setPrestoredFreezeframeStoredInNvm.__doc__) == (
            self.PRESTORED_FREEZEFRAME_STORED_IN_NVM_NOTE + "\n\nA None value is a no-op and does not overwrite an existing prestoredFreezeframeStoredInNvm."
        )
        assert inspect.cleandoc(DiagnosticEvent.getRecoverableInSameOperationCycle.__doc__) == self.RECOVERABLE_IN_SAME_OPERATION_CYCLE_NOTE
        assert inspect.cleandoc(DiagnosticEvent.setRecoverableInSameOperationCycle.__doc__) == (
            self.RECOVERABLE_IN_SAME_OPERATION_CYCLE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing recoverableInSameOperationCycle."
        )

    def test_create_diagnostic_event(self):
        """
        Test that ARPackage.createDiagnosticEvent appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticEvent("Event1")

        assert isinstance(obj, DiagnosticEvent)
        assert obj.getShortName() == "Event1"
        assert ar_root.getReferrableElement("Event1", DiagnosticEvent) is obj

        duplicate = ar_root.createDiagnosticEvent("Event1")
        assert duplicate is obj


class TestDiagnosticExtendedDataRecord:
    """
    Test class for DiagnosticExtendedDataRecord functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.181, p.190

    DiagnosticExtendedDataRecord is concrete (XSD complexType
    DIAGNOSTIC-EXTENDED-DATA-RECORD abstract="false") with five own Attribute
    rows in displayed order. trigger round-trips as the typed
    DiagnosticRecordTriggerEnum (Table 4.182) literal.
    """

    CLASS_NOTE = "Description of an extended data record. Tags: atp.recommendedPackage=DiagnosticExtendedDataRecords"

    CUSTOM_TRIGGER_NOTE = "This attribute shall be taken to verbally describe the nature of the custom trigger."
    RECORD_ELEMENT_NOTE = "Defined DataElements in the extended record element. Stereotypes: atpSplitable Tags: atp.Splitkey=recordElement.bitOffset, recordElement.ident.shortName"
    RECORD_NUMBER_NOTE = "This attribute specifies an unique identifier for an extended data record."
    TRIGGER_NOTE = "This attribute specifies the primary trigger to allocate an event memory entry."
    UPDATE_NOTE = "This attribute defines when an extended data record is captured. true: This extended data record is captured every time. false: This extended data record is only captured for new event memory entries."

    def _make_obj(self) -> DiagnosticExtendedDataRecord:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticExtendedDataRecord(ar_root, "TestExtendedDataRecord")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestExtendedDataRecord"
        assert isinstance(obj, DiagnosticExtendedDataRecord)
        assert isinstance(obj, ARElement)
        assert obj.getCustomTrigger() is None
        assert obj.getRecordElements() == []
        assert obj.getRecordNumber() is None
        assert obj.getTrigger() is None
        assert obj.getUpdate() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticExtendedDataRecord.__init__.__doc__ is None

    def test_get_set_custom_trigger(self):
        """
        Round-trips customTrigger; None is a no-op.
        """
        obj = self._make_obj()

        value = String().setValue("customTriggerDescription")
        result = obj.setCustomTrigger(value)
        assert result is obj  # method chaining
        assert obj.getCustomTrigger() is value
        assert obj.getCustomTrigger().getValue() == "customTriggerDescription"

        result = obj.setCustomTrigger(None)
        assert result is obj  # method chaining with None
        assert obj.getCustomTrigger() is value  # None is a no-op

    def test_add_get_record_elements(self):
        """
        Round-trips the recordElement aggregation; None is a no-op and chaining returns self.
        """
        obj = self._make_obj()

        parameter1 = DiagnosticParameter()
        parameter2 = DiagnosticParameter()

        result = obj.addRecordElement(parameter1)
        assert result is obj  # method chaining
        obj.addRecordElement(parameter2)

        record_elements = obj.getRecordElements()
        assert len(record_elements) == 2
        assert record_elements[0] is parameter1
        assert record_elements[1] is parameter2

        result = obj.addRecordElement(None)
        assert result is obj  # method chaining with None
        assert len(obj.getRecordElements()) == 2  # None is a no-op

    def test_get_set_record_number(self):
        """
        Round-trips recordNumber; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger().setValue(40)
        result = obj.setRecordNumber(value)
        assert result is obj  # method chaining
        assert obj.getRecordNumber() is value
        assert obj.getRecordNumber().value == 40

        result = obj.setRecordNumber(None)
        assert result is obj  # method chaining with None
        assert obj.getRecordNumber() is value  # None is a no-op

    def test_get_set_trigger(self):
        """
        Round-trips trigger; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticRecordTriggerEnum().setValue(DiagnosticRecordTriggerEnum.CONFIRMED)
        result = obj.setTrigger(value)
        assert result is obj  # method chaining
        assert obj.getTrigger() is value
        assert obj.getTrigger().getValue() == "CONFIRMED"

        result = obj.setTrigger(None)
        assert result is obj  # method chaining with None
        assert obj.getTrigger() is value  # None is a no-op

    def test_get_set_update(self):
        """
        Round-trips update; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean().setValue(True)
        result = obj.setUpdate(value)
        assert result is obj  # method chaining
        assert obj.getUpdate() is value
        assert obj.getUpdate().value is True

        result = obj.setUpdate(None)
        assert result is obj  # method chaining with None
        assert obj.getUpdate() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that every accessor docstring is the spec Note verbatim (setters append the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.getCustomTrigger.__doc__) == self.CUSTOM_TRIGGER_NOTE
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.setCustomTrigger.__doc__) == (self.CUSTOM_TRIGGER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing customTrigger.")
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.addRecordElement.__doc__) == (self.RECORD_ELEMENT_NOTE + "\n\nA None value is a no-op and does not extend the recordElements list.")
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.getRecordElements.__doc__) == self.RECORD_ELEMENT_NOTE
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.getRecordNumber.__doc__) == self.RECORD_NUMBER_NOTE
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.setRecordNumber.__doc__) == (self.RECORD_NUMBER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing recordNumber.")
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.getTrigger.__doc__) == self.TRIGGER_NOTE
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.setTrigger.__doc__) == (self.TRIGGER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing trigger.")
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.getUpdate.__doc__) == self.UPDATE_NOTE
        assert inspect.cleandoc(DiagnosticExtendedDataRecord.setUpdate.__doc__) == (self.UPDATE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing update.")

    def test_create_diagnostic_extended_data_record(self):
        """
        Test that ARPackage.createDiagnosticExtendedDataRecord appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticExtendedDataRecord("Record1")

        assert isinstance(obj, DiagnosticExtendedDataRecord)
        assert obj.getShortName() == "Record1"
        assert ar_root.getReferrableElement("Record1", DiagnosticExtendedDataRecord) is obj

        duplicate = ar_root.createDiagnosticExtendedDataRecord("Record1")
        assert duplicate is obj


class TestDiagnosticFimAliasEvent:
    """
    Test class for DiagnosticFimAliasEvent functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.212, p.214

    DiagnosticFimAliasEvent is concrete but its table carries no Attribute rows
    (the XSD group DIAGNOSTIC-FIM-ALIAS-EVENT is an empty sequence) — it is an
    identity-only concrete marker over the abstract base DiagnosticAbstractAliasEvent
    (Table 4.213); round-trip is driven by the concrete sibling
    DiagnosticFimAliasEventGroup (Table 5.35).
    """

    CLASS_NOTE = "This meta-class is used to represent a given event semantics. However, the name of the actual events used in a specific project is sometimes not defined yet, not known or not in the responsibility of the author. Therefore, the DiagnosticFimAliasEvent has a reference to the actual DiagnosticEvent and by this the final connection is created. Tags: atp.recommendedPackage=DiagnosticFimAliasEvents"

    def _make_obj(self) -> DiagnosticFimAliasEvent:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFimAliasEvent(ar_root, "TestFimAliasEvent")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFimAliasEvent"
        assert isinstance(obj, DiagnosticFimAliasEvent)
        assert isinstance(obj, DiagnosticAbstractAliasEvent)
        assert isinstance(obj, ARElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticFimAliasEvent.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFimAliasEvent.__init__.__doc__ is None

    def test_create_diagnostic_fim_alias_event(self):
        """
        Test that ARPackage.createDiagnosticFimAliasEvent appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticFimAliasEvent("FimAliasEvent1")

        assert isinstance(obj, DiagnosticFimAliasEvent)
        assert obj.getShortName() == "FimAliasEvent1"
        assert ar_root.getReferrableElement("FimAliasEvent1", DiagnosticFimAliasEvent) is obj

        duplicate = ar_root.createDiagnosticFimAliasEvent("FimAliasEvent1")
        assert duplicate is obj


class TestDiagnosticFreezeFrame:
    """
    Test class for DiagnosticFreezeFrame functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.183, p.192

    DiagnosticFreezeFrame is concrete (XSD complexType
    DIAGNOSTIC-FREEZE-FRAME abstract="false") with four own Attribute
    rows in displayed order. trigger round-trips as the typed
    DiagnosticRecordTriggerEnum (Table 4.182) literal.
    """

    CLASS_NOTE = "This element describes combinations of DIDs for a non OBD relevant freeze frame. Tags: atp.recommendedPackage=DiagnosticFreezeFrames"

    CUSTOM_TRIGGER_NOTE = "This attribute shall be taken to verbally describe the nature of the custom trigger."
    RECORD_NUMBER_NOTE = "This attribute defines a record number for a freeze frame record. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    TRIGGER_NOTE = "This attribute defines the primary trigger to allocate an event memory entry."
    UPDATE_NOTE = "This attribute defines the approach when the freeze frame record is stored/updated. true: FreezeFrame record is captured every time. false: FreezeFrame record is only captured for new event memory entries."

    def _make_obj(self) -> DiagnosticFreezeFrame:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFreezeFrame(ar_root, "TestFreezeFrame")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFreezeFrame"
        assert isinstance(obj, DiagnosticFreezeFrame)
        assert isinstance(obj, ARElement)
        assert obj.getCustomTrigger() is None
        assert obj.getRecordNumber() is None
        assert obj.getTrigger() is None
        assert obj.getUpdate() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticFreezeFrame.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFreezeFrame.__init__.__doc__ is None

    def test_get_set_custom_trigger(self):
        """
        Round-trips customTrigger; None is a no-op.
        """
        obj = self._make_obj()

        value = String().setValue("custom trigger description")
        result = obj.setCustomTrigger(value)
        assert result is obj  # method chaining
        assert obj.getCustomTrigger() is value
        assert obj.getCustomTrigger().getValue() == "custom trigger description"

        result = obj.setCustomTrigger(None)
        assert result is obj  # method chaining with None
        assert obj.getCustomTrigger() is value  # None is a no-op

    def test_get_set_record_number(self):
        """
        Round-trips recordNumber; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger().setValue(40)
        result = obj.setRecordNumber(value)
        assert result is obj  # method chaining
        assert obj.getRecordNumber() is value
        assert obj.getRecordNumber().value == 40

        result = obj.setRecordNumber(None)
        assert result is obj  # method chaining with None
        assert obj.getRecordNumber() is value  # None is a no-op

    def test_get_set_trigger(self):
        """
        Round-trips trigger; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticRecordTriggerEnum().setValue(DiagnosticRecordTriggerEnum.CONFIRMED)
        result = obj.setTrigger(value)
        assert result is obj  # method chaining
        assert obj.getTrigger() is value
        assert obj.getTrigger().getValue() == "CONFIRMED"

        result = obj.setTrigger(None)
        assert result is obj  # method chaining with None
        assert obj.getTrigger() is value  # None is a no-op

    def test_get_set_update(self):
        """
        Round-trips update; None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean().setValue(True)
        result = obj.setUpdate(value)
        assert result is obj  # method chaining
        assert obj.getUpdate() is value
        assert obj.getUpdate().value is True

        result = obj.setUpdate(None)
        assert result is obj  # method chaining with None
        assert obj.getUpdate() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that every accessor docstring is the spec Note verbatim (setters append the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticFreezeFrame.getCustomTrigger.__doc__) == self.CUSTOM_TRIGGER_NOTE
        assert inspect.cleandoc(DiagnosticFreezeFrame.setCustomTrigger.__doc__) == (self.CUSTOM_TRIGGER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing customTrigger.")
        assert inspect.cleandoc(DiagnosticFreezeFrame.getRecordNumber.__doc__) == self.RECORD_NUMBER_NOTE
        assert inspect.cleandoc(DiagnosticFreezeFrame.setRecordNumber.__doc__) == (self.RECORD_NUMBER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing recordNumber.")
        assert inspect.cleandoc(DiagnosticFreezeFrame.getTrigger.__doc__) == self.TRIGGER_NOTE
        assert inspect.cleandoc(DiagnosticFreezeFrame.setTrigger.__doc__) == (self.TRIGGER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing trigger.")
        assert inspect.cleandoc(DiagnosticFreezeFrame.getUpdate.__doc__) == self.UPDATE_NOTE
        assert inspect.cleandoc(DiagnosticFreezeFrame.setUpdate.__doc__) == (self.UPDATE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing update.")

    def test_create_diagnostic_freeze_frame(self):
        """
        Test that ARPackage.createDiagnosticFreezeFrame appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticFreezeFrame("FreezeFrame1")

        assert isinstance(obj, DiagnosticFreezeFrame)
        assert obj.getShortName() == "FreezeFrame1"
        assert ar_root.getReferrableElement("FreezeFrame1", DiagnosticFreezeFrame) is obj

        duplicate = ar_root.createDiagnosticFreezeFrame("FreezeFrame1")
        assert duplicate is obj


class TestDiagnosticFunctionIdentifier:
    """
    Test class for DiagnosticFunctionIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.214, p.215

    DiagnosticFunctionIdentifier is concrete (XSD complexType
    DIAGNOSTIC-FUNCTION-IDENTIFIER abstract="false") with NO own
    Attribute rows — an identity-only FID marker class; the XSD group
    DIAGNOSTIC-FUNCTION-IDENTIFIER (AUTOSAR_00052.xsd l.37879) is an
    empty xsd:sequence.
    """

    CLASS_NOTE = "This meta-class represents a diagnostic function identifier (a.k.a. FID). Tags: atp.recommendedPackage=DiagnosticFunctionIdentifiers"

    def _make_obj(self) -> DiagnosticFunctionIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticFunctionIdentifier(ar_root, "TestFunctionIdentifier")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestFunctionIdentifier"
        assert isinstance(obj, DiagnosticFunctionIdentifier)
        assert isinstance(obj, ARElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticFunctionIdentifier.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFunctionIdentifier.__init__.__doc__ is None

    def test_create_diagnostic_function_identifier(self):
        """
        Test that ARPackage.createDiagnosticFunctionIdentifier appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticFunctionIdentifier("FID1")

        assert isinstance(obj, DiagnosticFunctionIdentifier)
        assert obj.getShortName() == "FID1"
        assert ar_root.getReferrableElement("FID1", DiagnosticFunctionIdentifier) is obj

        duplicate = ar_root.createDiagnosticFunctionIdentifier("FID1")
        assert duplicate is obj


class TestDiagnosticIndicator:
    """
    Test class for DiagnosticIndicator functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.199, p.203

    DiagnosticIndicator is concrete (XSD complexType
    DIAGNOSTIC-INDICATOR abstract="false") with one own Attribute
    row in displayed order. type (DiagnosticIndicatorTypeEnum,
    Table 4.200) is a synced enum and is exercised as a real enum
    instance.
    """

    CLASS_NOTE = "Definition of an indicator. Tags: atp.recommendedPackage=DiagnosticIndicators"

    TYPE_NOTE = "Defines the type of the indicator. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"

    def _make_obj(self) -> DiagnosticIndicator:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticIndicator(ar_root, "TestIndicator")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestIndicator"
        assert isinstance(obj, DiagnosticIndicator)
        assert isinstance(obj, ARElement)
        assert obj.getType() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticIndicator.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticIndicator.__init__.__doc__ is None

    def test_get_set_type(self):
        """
        Round-trips type; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.MALFUNCTION)
        result = obj.setType(value)
        assert result is obj  # method chaining
        assert obj.getType() is value
        assert obj.getType().getValue() == DiagnosticIndicatorTypeEnum.MALFUNCTION

        result = obj.setType(None)
        assert result is obj  # method chaining with None
        assert obj.getType() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that every accessor docstring is the spec Note verbatim (setters append the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticIndicator.getType.__doc__) == self.TYPE_NOTE
        assert inspect.cleandoc(DiagnosticIndicator.setType.__doc__) == (self.TYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing type.")

    def test_create_diagnostic_indicator(self):
        """
        Test that ARPackage.createDiagnosticIndicator appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticIndicator("Indicator1")

        assert isinstance(obj, DiagnosticIndicator)
        assert obj.getShortName() == "Indicator1"
        assert ar_root.getReferrableElement("Indicator1", DiagnosticIndicator) is obj

        duplicate = ar_root.createDiagnosticIndicator("Indicator1")
        assert duplicate is obj


class TestDiagnosticIumpr:
    """
    Test class for DiagnosticIumpr functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.207, p.210

    DiagnosticIumpr is concrete (XSD complexType
    DIAGNOSTIC-IUMPR abstract="false") with two own Attribute
    rows in displayed order. event (kind ref) is modeled as the typed
    reference eventRef; ratioKind round-trips as the typed
    DiagnosticIumprKindEnum (Table 4.208) literal.
    """

    CLASS_NOTE = "This meta-class represents the ability to model the in-use monitor performance ratio. The latter computes to the number of times a fault could have been found divided by the number of times the vehicle conditions have been properly fulfilled. Tags: atp.recommendedPackage=DiagnosticIumprs"

    EVENT_REF_NOTE = "This reference represents the DiagnosticEvent that corresponds to the IUMPR computation."

    RATIO_KIND_NOTE = "This attribute controls the behavior of how the ratio is calculated."

    def _make_obj(self) -> DiagnosticIumpr:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticIumpr(ar_root, "TestIumpr")

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestIumpr"
        assert isinstance(obj, DiagnosticIumpr)
        assert isinstance(obj, ARElement)
        assert obj.getEventRef() is None
        assert obj.getRatioKind() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticIumpr.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticIumpr.__init__.__doc__ is None

    def test_get_set_event_ref(self):
        """
        Round-trips eventRef; None is a no-op.
        """
        obj = self._make_obj()

        value = RefType().setValue("/AUTOSAR/DiagnosticEvent")
        result = obj.setEventRef(value)
        assert result is obj  # method chaining
        assert obj.getEventRef() is value
        assert obj.getEventRef().getValue() == "/AUTOSAR/DiagnosticEvent"

        result = obj.setEventRef(None)
        assert result is obj  # method chaining with None
        assert obj.getEventRef() is value  # None is a no-op

    def test_get_set_ratio_kind(self):
        """
        Round-trips ratioKind; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticIumprKindEnum().setValue(DiagnosticIumprKindEnum.OBSERVER_BASED)
        result = obj.setRatioKind(value)
        assert result is obj  # method chaining
        assert obj.getRatioKind() is value
        assert obj.getRatioKind().getValue() == DiagnosticIumprKindEnum.OBSERVER_BASED

        result = obj.setRatioKind(None)
        assert result is obj  # method chaining with None
        assert obj.getRatioKind() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Test that every accessor docstring is the spec Note verbatim (setters append the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticIumpr.getEventRef.__doc__) == self.EVENT_REF_NOTE
        assert inspect.cleandoc(DiagnosticIumpr.setEventRef.__doc__) == (self.EVENT_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventRef.")
        assert inspect.cleandoc(DiagnosticIumpr.getRatioKind.__doc__) == self.RATIO_KIND_NOTE
        assert inspect.cleandoc(DiagnosticIumpr.setRatioKind.__doc__) == (self.RATIO_KIND_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ratioKind.")

    def test_create_diagnostic_iumpr(self):
        """
        Test that ARPackage.createDiagnosticIumpr appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticIumpr("Iumpr1")

        assert isinstance(obj, DiagnosticIumpr)
        assert obj.getShortName() == "Iumpr1"
        assert ar_root.getReferrableElement("Iumpr1", DiagnosticIumpr) is obj

        duplicate = ar_root.createDiagnosticIumpr("Iumpr1")
        assert duplicate is obj


class TestDiagnosticIumprDenominatorGroup:
    """
    Test class for DiagnosticIumprDenominatorGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.211, p.211

    DiagnosticIumprDenominatorGroup is concrete (XSD complexType
    DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP abstract="false") with one own
    Attribute row: iumpr (kind ref, multiplicity *) is modeled as the
    plural dedicated typed-list field iumprRefs behind the
    addIumprRef/getIumprRefs accessors (DiagnosticDataIdentifierSet
    dataIdentifierRefs precedent). The referenced type DiagnosticIumpr
    is fully synced on this branch.
    """

    CLASS_NOTE = "This meta-class represents the ability to model a IUMPR denominator groups. Tags: atp.recommendedPackage=DiagnosticIumprDenominatorGroup"

    IUMPR_NOTE = "This reference collects DiagnosticIumpr to a Diagnostic IumprDenominatorGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr"

    def _make_obj(self) -> DiagnosticIumprDenominatorGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticIumprDenominatorGroup(ar_root, "TestDenominatorGroup")

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-IUMPR")
        ref.setValue(value)
        return ref

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestDenominatorGroup"
        assert isinstance(obj, DiagnosticIumprDenominatorGroup)
        assert isinstance(obj, ARElement)
        assert obj.getIumprRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticIumprDenominatorGroup.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticIumprDenominatorGroup.__init__.__doc__ is None

    def test_add_iumpr_ref(self):
        """
        Appends the refs in order; setter-style chaining returns the object.
        """
        obj = self._make_obj()
        ref1 = self._make_ref("/AUTOSAR/DiagnosticIumprDenominatorGroups/Iumpr1")
        ref2 = self._make_ref("/AUTOSAR/DiagnosticIumprDenominatorGroups/Iumpr2")

        result = obj.addIumprRef(ref1)
        assert result is obj  # method chaining
        assert obj.getIumprRefs() == [ref1]

        obj.addIumprRef(ref2)
        assert obj.getIumprRefs() == [ref1, ref2]  # append preserves the ordered list

    def test_add_iumpr_ref_none_no_op(self):
        """
        Test that a None ref is a no-op and does not extend the list.
        """
        obj = self._make_obj()

        result = obj.addIumprRef(None)
        assert result is obj  # method chaining with None
        assert obj.getIumprRefs() == []

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (add + the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticIumprDenominatorGroup.addIumprRef.__doc__) == (self.IUMPR_NOTE + "\n\nA None value is a no-op and does not extend the iumprRefs list.")
        assert inspect.cleandoc(DiagnosticIumprDenominatorGroup.getIumprRefs.__doc__) == self.IUMPR_NOTE

    def test_create_diagnostic_iumpr_denominator_group(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIumprDenominatorGroups")
        element = package.createDiagnosticIumprDenominatorGroup("DenominatorGroup1")

        assert element is not None
        assert isinstance(element, DiagnosticIumprDenominatorGroup)
        assert element.getShortName() == "DenominatorGroup1"
        assert package.getReferrableElement("DenominatorGroup1", DiagnosticIumprDenominatorGroup) is element

        duplicate = package.createDiagnosticIumprDenominatorGroup("DenominatorGroup1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticIumprGroup:
    """
    Test class for DiagnosticIumprGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.209, p.210

    DiagnosticIumprGroup is concrete (XSD complexType DIAGNOSTIC-IUMPR-GROUP
    abstract="false") with two own Attribute rows: iumpr (kind ref,
    multiplicity *) is modeled as the plural dedicated typed-list field
    iumprRefs behind the addIumprRef/getIumprRefs accessors, and
    iumprGroupIdentifier (kind aggr, multiplicity 0..1) as the optional
    typed field behind get/setIumprGroupIdentifier. The referenced type
    DiagnosticIumprGroupIdentifier (Table 4.210) is still an empty stub
    queued later in Group25 — the typed field round-trips the wrapper
    presence until that row syncs.
    """

    CLASS_NOTE = "This meta-class represents the ability to model a IUMPR groups. Tags: atp.recommendedPackage=DiagnosticIumprGroups"

    IUMPR_NOTE = "This reference collects DiagnosticIumpr to a Diagnostic IumprGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr"

    IUMPR_GROUP_IDENTIFIER_NOTE = "This aggregation allows for the variant modeling of the groupIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iumprGroupIdentifier.groupId, iumprGroup Identifier.variationPoint.shortLabel vh.latestBindingTime=postBuild"

    def _make_obj(self) -> DiagnosticIumprGroup:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticIumprGroup(ar_root, "TestIumprGroup")

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-IUMPR")
        ref.setValue(value)
        return ref

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestIumprGroup"
        assert isinstance(obj, DiagnosticIumprGroup)
        assert isinstance(obj, ARElement)
        assert obj.getIumprRefs() == []
        assert obj.getIumprGroupIdentifier() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticIumprGroup.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticIumprGroup.__init__.__doc__ is None

    def test_add_iumpr_ref(self):
        """
        Appends the refs in order; setter-style chaining returns the object.
        """
        obj = self._make_obj()
        ref1 = self._make_ref("/AUTOSAR/DiagnosticIumprGroups/Iumpr1")
        ref2 = self._make_ref("/AUTOSAR/DiagnosticIumprGroups/Iumpr2")

        result = obj.addIumprRef(ref1)
        assert result is obj  # method chaining
        assert obj.getIumprRefs() == [ref1]

        obj.addIumprRef(ref2)
        assert obj.getIumprRefs() == [ref1, ref2]  # append preserves the ordered list

    def test_add_iumpr_ref_none_no_op(self):
        """
        Test that a None ref is a no-op and does not extend the list.
        """
        obj = self._make_obj()

        result = obj.addIumprRef(None)
        assert result is obj  # method chaining with None
        assert obj.getIumprRefs() == []

    def test_get_set_iumpr_group_identifier(self):
        """
        Round-trips the aggregation through the setter/getter; chaining returns the object.
        """
        obj = self._make_obj()
        identifier = DiagnosticIumprGroupIdentifier()

        result = obj.setIumprGroupIdentifier(identifier)
        assert result is obj  # method chaining
        assert obj.getIumprGroupIdentifier() is identifier

    def test_set_iumpr_group_identifier_none_no_op(self):
        """
        Test that a None value is a no-op and does not overwrite an existing iumprGroupIdentifier.
        """
        obj = self._make_obj()
        identifier = DiagnosticIumprGroupIdentifier()
        obj.setIumprGroupIdentifier(identifier)

        result = obj.setIumprGroupIdentifier(None)
        assert result is obj  # method chaining with None
        assert obj.getIumprGroupIdentifier() is identifier

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (add + the None-no-op sentence, get/set pair).
        """
        assert inspect.cleandoc(DiagnosticIumprGroup.addIumprRef.__doc__) == (self.IUMPR_NOTE + "\n\nA None value is a no-op and does not extend the iumprRefs list.")
        assert inspect.cleandoc(DiagnosticIumprGroup.getIumprRefs.__doc__) == self.IUMPR_NOTE
        assert inspect.cleandoc(DiagnosticIumprGroup.getIumprGroupIdentifier.__doc__) == self.IUMPR_GROUP_IDENTIFIER_NOTE
        assert inspect.cleandoc(DiagnosticIumprGroup.setIumprGroupIdentifier.__doc__) == (
            self.IUMPR_GROUP_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing iumprGroupIdentifier."
        )

    def test_create_diagnostic_iumpr_group(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIumprGroups")
        element = package.createDiagnosticIumprGroup("IumprGroup1")

        assert element is not None
        assert isinstance(element, DiagnosticIumprGroup)
        assert element.getShortName() == "IumprGroup1"
        assert package.getReferrableElement("IumprGroup1", DiagnosticIumprGroup) is element

        duplicate = package.createDiagnosticIumprGroup("IumprGroup1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticEcuInstanceProps:
    """
    Test class for DiagnosticEcuInstanceProps functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.205, p.207

    DiagnosticEcuInstanceProps is concrete (XSD complexType
    DIAGNOSTIC-ECU-INSTANCE-PROPS abstract="false") with two own Attribute
    rows: ecuInstance (kind ref, multiplicity *) is modeled as the dedicated
    typed list ecuInstanceRefs of RefType behind addEcuInstanceRef /
    getEcuInstanceRefs (DiagnosticDataIdentifierSet precedent); obdSupport
    (kind attr, multiplicity 0..1) is typed Optional[DiagnosticObdSupportEnum]
    (markdown Type column wins over the XSD element type, Rule 0015).
    obdSupport round-trips as the typed DiagnosticObdSupportEnum (Table 4.206)
    literal.
    """

    CLASS_NOTE = (
        "This meta-class represents the ability to model properties that are specific for a given EcuInstance but on the other hand represent purely diagnostic-related information. "
        "In the spirit of decentralized configuration it is therefore possible to specify the diagnostic-related information related to a given EcuInstance even if the EcuInstance does not yet exist. "
        "Tags: atp.recommendedPackage=DiagnosticEcuInstancePropss"
    )

    ECU_INSTANCE_NOTE = "This represents the actual EcuInstance to which the information contained in the DiagnosticEcuInstance contribute. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance"
    OBD_SUPPORT_NOTE = "This attribute is used to specify the role (if applicable) in which the DiagnosticEcuInstance supports OBD."

    def _make_obj(self) -> DiagnosticEcuInstanceProps:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticEcuInstanceProps(ar_root, "TestEcuInstanceProps")

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("ECU-INSTANCE")
        ref.setValue(value)
        return ref

    def _make_obd_support(self, value: str) -> DiagnosticObdSupportEnum:
        return DiagnosticObdSupportEnum().setValue(value)

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestEcuInstanceProps"
        assert isinstance(obj, DiagnosticEcuInstanceProps)
        assert isinstance(obj, ARElement)
        assert obj.getEcuInstanceRefs() == []
        assert obj.getObdSupport() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticEcuInstanceProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEcuInstanceProps.__init__.__doc__ is None

    def test_add_ecu_instance_ref(self):
        """
        Appends the refs in order; setter-style chaining returns the object.
        """
        obj = self._make_obj()
        ref1 = self._make_ref("/AUTOSAR/EcuInstances/Ecu1")
        ref2 = self._make_ref("/AUTOSAR/EcuInstances/Ecu2")

        result = obj.addEcuInstanceRef(ref1)
        assert result is obj  # method chaining
        assert obj.getEcuInstanceRefs() == [ref1]

        obj.addEcuInstanceRef(ref2)
        assert obj.getEcuInstanceRefs() == [ref1, ref2]  # append preserves the ordered list

    def test_add_ecu_instance_ref_none_no_op(self):
        """
        Test that a None ref is a no-op and does not extend the list.
        """
        obj = self._make_obj()

        result = obj.addEcuInstanceRef(None)
        assert result is obj  # method chaining with None
        assert obj.getEcuInstanceRefs() == []

    def test_get_set_obd_support(self):
        """
        Round-trips the attribute through the setter/getter; chaining returns the object.
        """
        obj = self._make_obj()
        obd_support = DiagnosticObdSupportEnum().setValue(DiagnosticObdSupportEnum.PRIMARY_ECU)

        result = obj.setObdSupport(obd_support)
        assert result is obj  # method chaining
        assert obj.getObdSupport() is obd_support
        assert obj.getObdSupport().getValue() == DiagnosticObdSupportEnum.PRIMARY_ECU

    def test_set_obd_support_none_no_op(self):
        """
        Test that a None value is a no-op and does not overwrite an existing obdSupport.
        """
        obj = self._make_obj()
        obd_support = self._make_obd_support("primaryEcu")
        obj.setObdSupport(obd_support)

        result = obj.setObdSupport(None)
        assert result is obj  # method chaining with None
        assert obj.getObdSupport() is obd_support

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (setters add the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticEcuInstanceProps.addEcuInstanceRef.__doc__) == (self.ECU_INSTANCE_NOTE + "\n\nA None value is a no-op and does not extend the ecuInstanceRefs list.")
        assert inspect.cleandoc(DiagnosticEcuInstanceProps.getEcuInstanceRefs.__doc__) == self.ECU_INSTANCE_NOTE
        assert inspect.cleandoc(DiagnosticEcuInstanceProps.getObdSupport.__doc__) == self.OBD_SUPPORT_NOTE
        assert inspect.cleandoc(DiagnosticEcuInstanceProps.setObdSupport.__doc__) == (self.OBD_SUPPORT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing obdSupport.")

    def test_create_diagnostic_ecu_instance_props(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuInstancePropss")
        element = package.createDiagnosticEcuInstanceProps("EcuInstanceProps1")

        assert element is not None
        assert isinstance(element, DiagnosticEcuInstanceProps)
        assert element.getShortName() == "EcuInstanceProps1"
        assert package.getReferrableElement("EcuInstanceProps1", DiagnosticEcuInstanceProps) is element

        duplicate = package.createDiagnosticEcuInstanceProps("EcuInstanceProps1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticMeasurementIdentifier:
    """
    Test class for DiagnosticMeasurementIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.204, p.206

    DiagnosticMeasurementIdentifier is concrete (XSD complexType
    DIAGNOSTIC-MEASUREMENT-IDENTIFIER abstract="false") with one own
    Attribute row: obdMid (kind attr, multiplicity 0..1) is modeled as the
    optional typed field obdMid behind get/setObdMid. The markdown Type
    column PositiveInteger wins over the XSD element type
    POSITIVE-INTEGER-VALUE-VARIATION-POINT (Rule 0015); the value
    round-trips flattened as the OBD-MID element text (DiagnosticAging
    THRESHOLD precedent).
    """

    CLASS_NOTE = (
        "This meta-class represents the ability to describe a measurement identifier.\n"
        "\n"
        "[constr_10414] Existence of attribute DiagnosticMeasurementIdentifier.obdMid: "
        "For each DiagnosticMeasurementIdentifier, attribute obdMid shall exist at the time when the DEXT is complete."
    )

    OBD_MID_NOTE = "This represents the numerical measurement Id Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"

    def _make_obj(self) -> DiagnosticMeasurementIdentifier:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticMeasurementIdentifier(ar_root, "TestMeasurementIdentifier")

    def _make_obd_mid(self, value: int) -> PositiveInteger:
        obd_mid = PositiveInteger()
        obd_mid.setValue(value)
        return obd_mid

    def test_initialization(self):
        """
        Test that the concrete class instantiates with the most-derived base chain and empty defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMeasurementIdentifier"
        assert isinstance(obj, DiagnosticMeasurementIdentifier)
        assert isinstance(obj, ARElement)
        assert obj.getObdMid() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticMeasurementIdentifier.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMeasurementIdentifier.__init__.__doc__ is None

    def test_get_set_obd_mid(self):
        """
        Round-trips the attribute through the setter/getter; chaining returns the object.
        """
        obj = self._make_obj()
        obd_mid = self._make_obd_mid(300)

        result = obj.setObdMid(obd_mid)
        assert result is obj  # method chaining
        assert obj.getObdMid() is obd_mid
        assert obj.getObdMid().value == 300

    def test_set_obd_mid_none_no_op(self):
        """
        Test that a None value is a no-op and does not overwrite an existing obdMid.
        """
        obj = self._make_obj()
        obd_mid = self._make_obd_mid(300)
        obj.setObdMid(obd_mid)

        result = obj.setObdMid(None)
        assert result is obj  # method chaining with None
        assert obj.getObdMid() is obd_mid

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (get/set pair; setter adds the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticMeasurementIdentifier.getObdMid.__doc__) == self.OBD_MID_NOTE
        assert inspect.cleandoc(DiagnosticMeasurementIdentifier.setObdMid.__doc__) == (self.OBD_MID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing obdMid.")

    def test_create_diagnostic_measurement_identifier(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMeasurementIdentifiers")
        element = package.createDiagnosticMeasurementIdentifier("MeasurementIdentifier1")

        assert element is not None
        assert isinstance(element, DiagnosticMeasurementIdentifier)
        assert element.getShortName() == "MeasurementIdentifier1"
        assert package.getReferrableElement("MeasurementIdentifier1", DiagnosticMeasurementIdentifier) is element

        duplicate = package.createDiagnosticMeasurementIdentifier("MeasurementIdentifier1")
        assert duplicate is element  # duplicate short name returns the existing element


class TestDiagnosticDataIdentifierSet:
    """
    Test class for DiagnosticDataIdentifierSet functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.178, p.187
    """

    CLASS_NOTE = "This represents the ability to define a list of DiagnosticDataIdentifiers that can be reused in different contexts. Tags: atp.recommendedPackage=DiagnosticDataIdentifierSets"
    DATA_IDENTIFIER_NOTE = "Reference to an ordered list of Data Identifiers."

    def _make_obj(self) -> DiagnosticDataIdentifierSet:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticDataIdentifierSet(ar_root, "TestSet")

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-DATA-IDENTIFIER")
        ref.setValue(value)
        return ref

    def test_initialization(self):
        """
        Test that a concrete DiagnosticDataIdentifierSet instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestSet"
        assert isinstance(obj, DiagnosticCommonElement)
        assert obj.getDataIdentifierRefs() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticDataIdentifierSet.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticDataIdentifierSet.__init__.__doc__ is None

    def test_add_data_identifier_ref(self):
        """
        Appends the refs in order; setter-style chaining returns the object.
        """
        obj = self._make_obj()
        ref1 = self._make_ref("/AUTOSAR/DiagnosticDataIdentifiers/DID1")
        ref2 = self._make_ref("/AUTOSAR/DiagnosticDataIdentifiers/DID2")

        result = obj.addDataIdentifierRef(ref1)
        assert result is obj  # method chaining
        assert obj.getDataIdentifierRefs() == [ref1]

        obj.addDataIdentifierRef(ref2)
        assert obj.getDataIdentifierRefs() == [ref1, ref2]  # append preserves the ordered list

    def test_add_data_identifier_ref_none_no_op(self):
        """
        Test that a None ref is a no-op and does not extend the list.
        """
        obj = self._make_obj()

        result = obj.addDataIdentifierRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDataIdentifierRefs() == []

    def test_create_diagnostic_data_identifier_set(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataIdentifierSets")
        element = package.createDiagnosticDataIdentifierSet("Set1")

        assert element is not None
        assert isinstance(element, DiagnosticDataIdentifierSet)
        assert element.getShortName() == "Set1"
        assert package.getReferrableElement("Set1", DiagnosticDataIdentifierSet) is element

        duplicate = package.createDiagnosticDataIdentifierSet("Set1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (add + the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticDataIdentifierSet.addDataIdentifierRef.__doc__) == (
            self.DATA_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not extend the dataIdentifierRefs list."
        )
        assert inspect.cleandoc(DiagnosticDataIdentifierSet.getDataIdentifierRefs.__doc__) == self.DATA_IDENTIFIER_NOTE


class TestDiagnosticOperationCycle:
    """
    Test class for DiagnosticOperationCycle functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.196, p.201

    DiagnosticOperationCycle is an ARElement aggregated by ARPackage.element with a
    single own attribute type (DiagnosticOperationCycleTypeEnum, 0..1, attr) — the
    XSD group (AUTOSAR_00052.xsd l.40289) additionally lists AUTOMATIC-END,
    CYCLE-AUTOSTART and CYCLE-STATUS-STORAGE, but all three carry
    atp.Status="removed" and are not modeled (Rule 0015).
    """

    CLASS_NOTE = "Definition of an operation cycle that is the base of the event qualifying and for Dem scheduling. Tags: atp.recommendedPackage=DiagnosticOperationCycles"
    TYPE_NOTE = "Operation cycles types for the Dem."

    def _make_obj(self) -> DiagnosticOperationCycle:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticOperationCycle(ar_root, "TestOperationCycle")

    def test_initialization(self):
        """
        Test that the class instantiates on the ARElement chain with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestOperationCycle"
        assert isinstance(obj, DiagnosticOperationCycle)
        assert isinstance(obj, ARElement)
        assert obj.getType() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticOperationCycle.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticOperationCycle.__init__.__doc__ is None

    def test_get_set_type(self):
        """
        Round-trips the own type attribute; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticOperationCycleTypeEnum().setValue(DiagnosticOperationCycleTypeEnum.IGNITION)
        result = obj.setType(value)
        assert result is obj  # method chaining
        assert obj.getType() is value
        assert obj.getType().getValue() == "IGNITION"

        result = obj.setType(None)
        assert result is obj  # method chaining with None
        assert obj.getType() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticOperationCycle.getType.__doc__) == self.TYPE_NOTE
        assert inspect.cleandoc(DiagnosticOperationCycle.setType.__doc__) == (self.TYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing type.")

    def test_create_diagnostic_operation_cycle(self):
        """
        Test that ARPackage.createDiagnosticOperationCycle appends a new element and returns the existing one on a duplicate short name.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        obj = ar_root.createDiagnosticOperationCycle("OperationCycle1")

        assert isinstance(obj, DiagnosticOperationCycle)
        assert obj.getShortName() == "OperationCycle1"
        assert ar_root.getReferrableElement("OperationCycle1", DiagnosticOperationCycle) is obj

        duplicate = ar_root.createDiagnosticOperationCycle("OperationCycle1")
        assert duplicate is obj


class TestDiagnosticRequestEmissionRelatedDTCPermanentStatus:
    """
    Test class for DiagnosticRequestEmissionRelatedDTCPermanentStatus functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.147, p.161
    """

    CLASS_NOTE = "This meta-class represents the ability to model an instance of the OBD mode 0x0A service. Tags: atp.recommendedPackage=DiagnosticRequestEmissionRelatedDTCPermanentStatuss"
    CLASS_REF_NOTE = "This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTCPermanentStatus in the given context."

    def _make_obj(self) -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return DiagnosticRequestEmissionRelatedDTCPermanentStatus(ar_root, "TestMode0A")

    def test_is_concrete(self):
        """
        Test that a concrete DiagnosticRequestEmissionRelatedDTCPermanentStatus instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestMode0A"
        assert isinstance(obj, DiagnosticServiceInstance)
        assert obj.getRequestEmissionRelatedDtcClassPermanentStatusRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestEmissionRelatedDTCPermanentStatus.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestEmissionRelatedDTCPermanentStatus.__init__.__doc__ is None

    def test_get_set_request_emission_related_dtc_class_permanent_status_ref(self):
        """
        Round-trips the requestEmissionRelatedDtcClassPermanentStatus ref; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticRequestEmissionRelatedDTCPermanentStatusClasss/Class1")
        result = obj.setRequestEmissionRelatedDtcClassPermanentStatusRef(ref)
        assert result is obj  # method chaining
        assert obj.getRequestEmissionRelatedDtcClassPermanentStatusRef() is ref
        assert obj.getRequestEmissionRelatedDtcClassPermanentStatusRef().getValue() == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCPermanentStatusClasss/Class1"
        assert obj.getRequestEmissionRelatedDtcClassPermanentStatusRef().getDest() == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS"

        result = obj.setRequestEmissionRelatedDtcClassPermanentStatusRef(None)
        assert result is obj  # method chaining with None
        assert obj.getRequestEmissionRelatedDtcClassPermanentStatusRef() is ref  # None is a no-op

    def test_create_diagnostic_request_emission_related_dtc_permanent_status(self):
        """
        Test that the ARPackage create factory creates and reuses the element.
        """
        package = AUTOSAR.getInstance().createARPackage("OBDMode0AServices")
        element = package.createDiagnosticRequestEmissionRelatedDTCPermanentStatus("Mode0AService1")

        assert element is not None
        assert isinstance(element, DiagnosticRequestEmissionRelatedDTCPermanentStatus)
        assert element.getShortName() == "Mode0AService1"
        assert package.getReferrableElement("Mode0AService1", DiagnosticRequestEmissionRelatedDTCPermanentStatus) is element

        duplicate = package.createDiagnosticRequestEmissionRelatedDTCPermanentStatus("Mode0AService1")
        assert duplicate is element  # duplicate short name returns the existing element

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestEmissionRelatedDTCPermanentStatus.getRequestEmissionRelatedDtcClassPermanentStatusRef.__doc__) == self.CLASS_REF_NOTE
        assert inspect.cleandoc(DiagnosticRequestEmissionRelatedDTCPermanentStatus.setRequestEmissionRelatedDtcClassPermanentStatusRef.__doc__) == (
            self.CLASS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing requestEmissionRelatedDtcClassPermanentStatusRef."
        )


class TestPhysicalDimensionMappingSet:
    """
    Test class for PhysicalDimensionMappingSet functionality.

    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.78, p.399
    """

    CLASS_NOTE = "This class represents a container for a list of mappings between PhysicalDimensions. Tags: atp.recommendedPackage=PhysicalDimensionMappingSets"
    PHYSICAL_DIMENSION_MAPPING_NOTE = "This aggregation represents a concrete collections of PhysicalDimensionMappings in the context of one PhysicalDimensionMappingSet."

    def _make_obj(self) -> PhysicalDimensionMappingSet:
        return PhysicalDimensionMappingSet(ARPackage(None, "Pkg"), "Mappings")

    def _make_mapping(self) -> PhysicalDimensionMapping:
        mapping = PhysicalDimensionMapping()
        mapping.setFirstPhysicalDimensionRef(RefType().setDest("PHYSICAL-DIMENSION").setValue("/PhysicalDimensions/Energy"))
        mapping.setSecondPhysicalDimensionRef(RefType().setDest("PHYSICAL-DIMENSION").setValue("/PhysicalDimensions/Torque"))
        return mapping

    def test_is_arelement_subclass(self):
        """
        Test that PhysicalDimensionMappingSet derives from ARElement per the Table 5.78 Base row.
        """
        assert issubclass(PhysicalDimensionMappingSet, ARElement)

    def test_initialization(self):
        """
        Test that a new PhysicalDimensionMappingSet initializes the aggregation to the empty list.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "Mappings"
        assert obj.getPhysicalDimensionMappings() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (incl. the Tags tail).
        """
        assert inspect.cleandoc(PhysicalDimensionMappingSet.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert PhysicalDimensionMappingSet.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 5.78 displayed row order (mutator first per attribute).
        """
        methods = [name for name, value in PhysicalDimensionMappingSet.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "addPhysicalDimensionMapping",
            "getPhysicalDimensionMappings",
        ]

    def test_members_are_pep526_annotated(self):
        """
        Test that the 0..* aggregation is a PEP 526 annotated List[PhysicalDimensionMapping] field.
        """
        source = inspect.getsource(PhysicalDimensionMappingSet.__init__)
        assert "self.physicalDimensionMappings: List[PhysicalDimensionMapping] = []" in source
        assert "# type:" not in source

    def test_inline_comment_is_spec_note_verbatim(self):
        """
        Test that the inline __init__ comment carries the spec Note verbatim.
        """
        source = inspect.getsource(PhysicalDimensionMappingSet.__init__)
        assert "# " + self.PHYSICAL_DIMENSION_MAPPING_NOTE in source

    def test_add_physical_dimension_mapping(self):
        """
        Test that addPhysicalDimensionMapping appends and returns self for chaining.
        """
        obj = self._make_obj()
        mapping = self._make_mapping()

        result = obj.addPhysicalDimensionMapping(mapping)
        assert result is obj
        assert obj.getPhysicalDimensionMappings() == [mapping]
        assert obj.getPhysicalDimensionMappings()[0].getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"

        second = PhysicalDimensionMapping()
        obj.addPhysicalDimensionMapping(second)
        assert obj.getPhysicalDimensionMappings() == [mapping, second]

    def test_add_physical_dimension_mapping_none_noop(self):
        """
        Test that addPhysicalDimensionMapping(None) is a no-op.
        """
        obj = self._make_obj()

        result = obj.addPhysicalDimensionMapping(None)
        assert result is obj
        assert obj.getPhysicalDimensionMappings() == []

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and adder docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(PhysicalDimensionMappingSet.addPhysicalDimensionMapping.__doc__) == (
            self.PHYSICAL_DIMENSION_MAPPING_NOTE + "\n\nA None value is a no-op and does not append a physicalDimensionMapping."
        )
        assert inspect.cleandoc(PhysicalDimensionMappingSet.getPhysicalDimensionMappings.__doc__) == self.PHYSICAL_DIMENSION_MAPPING_NOTE

    def test_arpackage_create_physical_dimension_mapping_set(self):
        """
        Test that ARPackage.createPhysicalDimensionMappingSet appends and returns the existing element on a duplicate short name.
        """
        document = AUTOSAR.getInstance()
        document.clear()
        ar_package = document.createARPackage("Pkg")

        created = ar_package.createPhysicalDimensionMappingSet("Mappings")
        assert isinstance(created, PhysicalDimensionMappingSet)
        assert created.getShortName() == "Mappings"

        duplicate = ar_package.createPhysicalDimensionMappingSet("Mappings")
        assert duplicate is created

    def test_arpackage_get_physical_dimension_mapping_sets(self):
        """
        Test that ARPackage.getPhysicalDimensionMappingSets returns the created sets.
        """
        document = AUTOSAR.getInstance()
        document.clear()
        ar_package = document.createARPackage("Pkg")
        ar_package.createPhysicalDimensionMappingSet("A")
        ar_package.createPhysicalDimensionMappingSet("B")

        sets = ar_package.getPhysicalDimensionMappingSets()
        assert [s.getShortName() for s in sets] == ["A", "B"]


class TestCalibrationParameterValueSet:
    """
    Test class for CalibrationParameterValueSet functionality.

    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.137, p.477
    """

    CLASS_NOTE = "Specification of a constant that can be part of a package, i.e. it can be defined stand-alone. Tags: atp.recommendedPackage=CalibrationParameterValueSets"
    CALIBRATION_PARAMETER_VALUE_NOTE = "This represents single CalibrationParameterValues in the CalibrationParameterValueSet. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=calibrationParameterValue, calibrationParameterValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime"

    def _make_obj(self) -> CalibrationParameterValueSet:
        return CalibrationParameterValueSet(ARPackage(None, "Pkg"), "CalprmValues")

    def _make_value(self) -> CalibrationParameterValue:
        value = CalibrationParameterValue()
        value.setInitializedParameterRef(RefType().setDest("FLAT-INSTANCE-DESCRIPTOR").setValue("/Pkg/FlatInstanceDescriptors/FID1"))
        return value

    def test_is_arelement_subclass(self):
        """
        Test that CalibrationParameterValueSet derives from ARElement per the Table 5.137 Base row.
        """
        assert issubclass(CalibrationParameterValueSet, ARElement)

    def test_initialization(self):
        """
        Test that a new CalibrationParameterValueSet initializes the aggregation to the empty list.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "CalprmValues"
        assert obj.getCalibrationParameterValues() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (incl. the Tags tail).
        """
        assert inspect.cleandoc(CalibrationParameterValueSet.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CalibrationParameterValueSet.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 5.137 displayed row order (mutator first per attribute).
        """
        methods = [name for name, value in CalibrationParameterValueSet.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "addCalibrationParameterValue",
            "getCalibrationParameterValues",
        ]

    def test_members_are_pep526_annotated(self):
        """
        Test that the 0..* aggregation is a PEP 526 annotated List[CalibrationParameterValue] field.
        """
        source = inspect.getsource(CalibrationParameterValueSet.__init__)
        assert "self.calibrationParameterValues: List[CalibrationParameterValue] = []" in source
        assert "# type:" not in source

    def test_inline_comment_is_spec_note_verbatim(self):
        """
        Test that the inline __init__ comment carries the spec Note verbatim (incl. the Stereotypes/Tags tail).
        """
        source = inspect.getsource(CalibrationParameterValueSet.__init__)
        assert "# " + self.CALIBRATION_PARAMETER_VALUE_NOTE in source

    def test_add_calibration_parameter_value(self):
        """
        Test that addCalibrationParameterValue appends and returns self for chaining.
        """
        obj = self._make_obj()
        value = self._make_value()

        result = obj.addCalibrationParameterValue(value)
        assert result is obj
        assert obj.getCalibrationParameterValues() == [value]
        assert obj.getCalibrationParameterValues()[0].getInitializedParameterRef().getValue() == "/Pkg/FlatInstanceDescriptors/FID1"

        second = CalibrationParameterValue()
        obj.addCalibrationParameterValue(second)
        assert obj.getCalibrationParameterValues() == [value, second]

    def test_add_calibration_parameter_value_none_noop(self):
        """
        Test that addCalibrationParameterValue(None) is a no-op.
        """
        obj = self._make_obj()

        result = obj.addCalibrationParameterValue(None)
        assert result is obj
        assert obj.getCalibrationParameterValues() == []

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and adder docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(CalibrationParameterValueSet.addCalibrationParameterValue.__doc__) == (
            self.CALIBRATION_PARAMETER_VALUE_NOTE + "\n\nA None value is a no-op and does not append a calibrationParameterValue."
        )
        assert inspect.cleandoc(CalibrationParameterValueSet.getCalibrationParameterValues.__doc__) == self.CALIBRATION_PARAMETER_VALUE_NOTE

    def test_arpackage_create_calibration_parameter_value_set(self):
        """
        Test that ARPackage.createCalibrationParameterValueSet appends and returns the existing element on a duplicate short name.
        """
        document = AUTOSAR.getInstance()
        document.clear()
        ar_package = document.createARPackage("Pkg")

        created = ar_package.createCalibrationParameterValueSet("CalprmValues")
        assert isinstance(created, CalibrationParameterValueSet)
        assert created.getShortName() == "CalprmValues"

        duplicate = ar_package.createCalibrationParameterValueSet("CalprmValues")
        assert duplicate is created

    def test_arpackage_get_calibration_parameter_value_sets(self):
        """
        Test that ARPackage.getCalibrationParameterValueSets returns the created sets.
        """
        document = AUTOSAR.getInstance()
        document.clear()
        ar_package = document.createARPackage("Pkg")
        ar_package.createCalibrationParameterValueSet("A")
        ar_package.createCalibrationParameterValueSet("B")

        sets = ar_package.getCalibrationParameterValueSets()
        assert [s.getShortName() for s in sets] == ["A", "B"]
