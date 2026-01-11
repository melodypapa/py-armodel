"""
This module contains comprehensive tests for the ARPackage.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, ReferenceBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, ReferrableSubtypesEnum, Identifier, Boolean


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
        Test get/set methods for BaseIsThisPackage flag.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getBaseIsThisPackage() is None

        # Test setting BaseIsThisPackage
        result = obj.setBaseIsThisPackage(Boolean().setValue(True))
        assert result is obj  # Verify method chaining
        assert obj.getBaseIsThisPackage().value is True

    def test_get_set_package_ref(self):
        """
        Test get/set methods for package references.
        """
        obj = ReferenceBase()

        # Test initial value
        assert obj.getPackageRef() is None

        # Test setting package ref list
        ref1 = RefType().setValue("/Package1")
        ref2 = RefType().setValue("/Package2")
        ref_list = [ref1, ref2]
        result = obj.setPackageRef(ref_list)
        assert result is obj  # Verify method chaining
        assert obj.getPackageRef() == ref_list

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
        sub_package = ARPackage(package, "SubPackage")
        package.arPackages["SubPackage"] = sub_package

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
        sub_package = ARPackage(package, "SubPackage")
        package.arPackages["SubPackage"] = sub_package

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

        isignal = package.createISignal("ISignal")
        assert isignal.getShortName() == "ISignal"

        system_signal = package.createSystemSignal("SystemSignal")
        assert system_signal.getShortName() == "SystemSignal"

        system_signal_group = package.createSystemSignalGroup("SystemSignalGroup")
        assert system_signal_group.getShortName() == "SystemSignalGroup"

        isignal_ipdu = package.createISignalIPdu("ISignalIPdu")
        assert isignal_ipdu.getShortName() == "ISignalIPdu"

        ecuc_val_collection = package.createEcucValueCollection("EcucValueCollection")
        assert ecuc_val_collection.getShortName() == "EcucValueCollection"

        ecuc_module_config = package.createEcucModuleConfigurationValues("EcucModuleConfigValues")
        assert ecuc_module_config.getShortName() == "EcucModuleConfigValues"

        ecuc_module_def = package.createEcucModuleDef("EcucModuleDef")
        assert ecuc_module_def.getShortName() == "EcucModuleDef"

        phys_dimension = package.createPhysicalDimension("PhysicalDimension")
        assert phys_dimension.getShortName() == "PhysicalDimension"

        isignal_group = package.createISignalGroup("ISignalGroup")
        assert isignal_group.getShortName() == "ISignalGroup"

        isignal_ipdu_group = package.createISignalIPduGroup("ISignalIPduGroup")
        assert isignal_ipdu_group.getShortName() == "ISignalIPduGroup"

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

        doip_tp_config = package.createDoIpTpConfig("DoIpTpConfig")
        assert doip_tp_config.getShortName() == "DoIpTpConfig"

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
        app_prim_dt = package.createApplicationPrimitiveDataType("AppPrimDT")
        impl_dt = package.createImplementationDataType("ImplDT")
        swc = package.createApplicationSwComponentType("AppSwc")
        sri = package.createSenderReceiverInterface("SRI")

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