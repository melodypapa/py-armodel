import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatInstanceDescriptor, FlatMap
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class TestFlatInstanceDescriptor:
    def test_initialization(self):
        """Test FlatInstanceDescriptor initialization"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        
        assert flat_instance is not None
        assert flat_instance.getShortName() == "TestInstance"
        assert flat_instance.ecuExtractReferenceIRef is None
        assert flat_instance.role is None
        assert flat_instance.rtePluginProps is None
        assert flat_instance.swDataDefProps is None
        assert flat_instance.upstreamReferenceIRef is None

    def test_get_ecu_extract_reference_iref(self):
        """Test getEcuExtractReferenceIRef method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        assert flat_instance.getEcuExtractReferenceIRef() is None

    def test_set_ecu_extract_reference_iref(self):
        """Test setEcuExtractReferenceIRef method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        test_value = AnyInstanceRef()
        result = flat_instance.setEcuExtractReferenceIRef(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getEcuExtractReferenceIRef() == test_value

    def test_get_role(self):
        """Test getRole method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        assert flat_instance.getRole() is None

    def test_set_role(self):
        """Test setRole method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        test_value = Identifier().setValue("TestRole")
        result = flat_instance.setRole(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getRole() == test_value

    def test_get_rte_plugin_props(self):
        """Test getRtePluginProps method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        assert flat_instance.getRtePluginProps() is None

    def test_set_rte_plugin_props(self):
        """Test setRtePluginProps method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        # Create a mock RtePluginProps object for testing
        class MockRtePluginProps:
            pass
        test_value = MockRtePluginProps()
        result = flat_instance.setRtePluginProps(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getRtePluginProps() == test_value

    def test_get_sw_data_def_props(self):
        """Test getSwDataDefProps method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        assert flat_instance.getSwDataDefProps() is None

    def test_set_sw_data_def_props(self):
        """Test setSwDataDefProps method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        # Import SwDataDefProps to use in test
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        test_value = SwDataDefProps()
        result = flat_instance.setSwDataDefProps(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getSwDataDefProps() == test_value

    def test_get_upstream_reference_iref(self):
        """Test getUpstreamReferenceIRef method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        assert flat_instance.getUpstreamReferenceIRef() is None

    def test_set_upstream_reference_iref(self):
        """Test setUpstreamReferenceIRef method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        test_value = AnyInstanceRef()
        result = flat_instance.setUpstreamReferenceIRef(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getUpstreamReferenceIRef() == test_value

    def test_all_properties(self):
        """Test setting all properties"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")
        
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        ecu_ref = AnyInstanceRef()
        role = Identifier().setValue("TestRole")
        sw_data_def = SwDataDefProps()
        
        flat_instance.setEcuExtractReferenceIRef(ecu_ref)
        flat_instance.setRole(role)
        flat_instance.setSwDataDefProps(sw_data_def)
        flat_instance.setUpstreamReferenceIRef(ecu_ref)
        
        assert flat_instance.getEcuExtractReferenceIRef() == ecu_ref
        assert flat_instance.getRole() == role
        assert flat_instance.getSwDataDefProps() == sw_data_def
        assert flat_instance.getUpstreamReferenceIRef() == ecu_ref


class TestFlatMap:
    def test_initialization(self):
        """Test FlatMap initialization"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")
        
        assert flat_map is not None
        assert flat_map.getShortName() == "TestFlatMap"
        assert flat_map.instances == []

    def test_create_flat_instance_descriptor(self):
        """Test createFlatInstanceDescriptor method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")
        
        instance = flat_map.createFlatInstanceDescriptor("TestInstance")
        assert instance is not None
        assert instance.getShortName() == "TestInstance"
        assert len(flat_map.instances) == 1
        assert flat_map.instances[0] == instance

    def test_create_flat_instance_descriptor_duplicate(self):
        """Test createFlatInstanceDescriptor with duplicate name"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")
        
        instance1 = flat_map.createFlatInstanceDescriptor("TestInstance")
        instance2 = flat_map.createFlatInstanceDescriptor("TestInstance")  # Should return the same instance
        assert instance1 is instance2

    def test_get_instances_empty(self):
        """Test getInstances method with empty list"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")
        
        instances = flat_map.getInstances()
        assert instances == []

    def test_get_instances(self):
        """Test getInstances method with multiple instances"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")
        
        # Create instances in reverse order to test sorting
        flat_map.createFlatInstanceDescriptor("Instance2")
        flat_map.createFlatInstanceDescriptor("Instance1")
        
        instances = flat_map.getInstances()
        assert len(instances) == 2
        assert instances[0].getShortName() == "Instance1"
        assert instances[1].getShortName() == "Instance2"