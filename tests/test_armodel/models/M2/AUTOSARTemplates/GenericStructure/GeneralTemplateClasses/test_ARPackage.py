"""
This module contains comprehensive tests for the ARPackage.py file
in the AUTOSAR GenericStructure module.
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import LifeCycleState
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticCommonProps, DiagnosticParameter, DiagnosticSupportInfoByte
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
    ARPackage,
    CpSwClusterToDiagEventMapping,
    DiagnosticAbstractDataIdentifier,
    DiagnosticAuthentication,
    DiagnosticAuthenticationConfiguration,
    DiagnosticAuthRole,
    DiagnosticAuthTransmitCertificate,
    DiagnosticComControl,
    DiagnosticContributionSet,
    DiagnosticControlDTCSetting,
    DiagnosticCustomServiceInstance,
    DiagnosticDataByIdentifier,
    DiagnosticDataIdentifier,
    DiagnosticDeAuthentication,
    DiagnosticDynamicDataIdentifier,
    DiagnosticEcuReset,
    DiagnosticMapping,
    DiagnosticProofOfOwnership,
    DiagnosticProtocol,
    DiagnosticReadDataByIdentifier,
    DiagnosticSecurityAccess,
    DiagnosticSessionControl,
    DiagnosticVerifyCertificateBidirectional,
    DiagnosticVerifyCertificateUnidirectional,
    DiagnosticWriteDataByIdentifier,
    LifeCycleStateDefinitionGroup,
    PackageableElement,
    ReferenceBase,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticAuthTransmitCertificateEvaluation, Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
    Boolean,
    Identifier,
    NameToken,
    PositiveInteger,
    ReferrableSubtypesEnum,
    RefType,
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
        assert package.getElement("NonExistent") is None

        # Add a sub-package
        sub_package = package.createARPackage("SubPackage")

        # Should be able to get the sub-package
        result = package.getElement("SubPackage")
        assert result == sub_package

        # Should return None for non-existent type
        result = package.getElement("SubPackage", type=str)  # Wrong type
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
        scope.setValue("descendant")
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
        scope.setValue("descendant")
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
        assert package.getElement("Svc1", DiagnosticCustomServiceInstance) is instance

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
        assert package.getElement("Role1", DiagnosticAuthRole) is auth_role

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
        assert package.getElement("SessionCtrl1", DiagnosticSessionControl) is session_control

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
        assert package.getElement("SecAccess1", DiagnosticSecurityAccess) is security_access

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
        assert package.getElement("AuthCfg1", DiagnosticAuthenticationConfiguration) is configuration

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
        assert package.getElement("VerifyBidir1", DiagnosticVerifyCertificateBidirectional) is verification

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
        assert package.getElement("VerifyUnidir1", DiagnosticVerifyCertificateUnidirectional) is verification

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
        assert package.getElement("DeAuth1", DiagnosticDeAuthentication) is de_authentication

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
        assert package.getElement("Proof1", DiagnosticProofOfOwnership) is proof_of_ownership

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
        assert package.getElement("Certificate1", DiagnosticAuthTransmitCertificate) is certificate

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
        assert package.getElement("EcuReset1", DiagnosticEcuReset) is ecu_reset

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
        assert package.getElement("ComControl1", DiagnosticComControl) is com_control

        duplicate = package.createDiagnosticComControl("ComControl1")
        assert duplicate is com_control  # duplicate short name returns the existing element


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
        assert package.getElement("ControlDTCSetting1", DiagnosticControlDTCSetting) is control_dtc_setting

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
        assert package.getElement("ReadDataByIdentifier1", DiagnosticReadDataByIdentifier) is read_did

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
        assert package.getElement("WriteDataByIdentifier1", DiagnosticWriteDataByIdentifier) is write_did

        duplicate = package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")
        assert duplicate is write_did  # duplicate short name returns the existing element
