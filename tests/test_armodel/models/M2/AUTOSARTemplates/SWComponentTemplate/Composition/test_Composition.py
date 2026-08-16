"""
This module contains tests for the Composition subdirectory in SWComponentTemplate.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    CompositionSwComponentType,
    DelegationSwConnector,
    InstantiationRTEEventProps,
    InstantiationTimingEventProps,
    PassThroughSwConnector,
    SwComponentPrototype,
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import InstanceEventInCompositionInstanceRef


class Test_M2_AUTOSARTemplates_SWComponentTemplate_Composition:
    """Test class for Composition module classes."""

    def test_SwComponentPrototype(self):
        """Test SwComponentPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        component_prototype = SwComponentPrototype(ar_root, "TestComponentPrototype")

        assert component_prototype.parent == ar_root
        assert component_prototype.short_name == "TestComponentPrototype"
        assert component_prototype.typeTRef is None

        # Test setters and getters
        ref = RefType()
        component_prototype.setTypeTRef(ref)
        assert component_prototype.getTypeTRef() == ref

    def test_SwConnector_abstract(self):
        """Test that SwConnector is abstract."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        # Create a concrete subclass to test the abstract class
        class TestSwConnector(SwConnector):
            def __init__(self, parent: ARObject, short_name: str):
                super().__init__(parent, short_name)

        test_connector = TestSwConnector(ar_root, "TestSwConnector")
        assert test_connector is not None
        assert test_connector.short_name == "TestSwConnector"
        assert isinstance(test_connector, SwConnector)

    def test_SwConnector_initialization(self):
        """Test SwConnector initialization defaults via a concrete subclass."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = AssemblySwConnector(ar_root, "TestSwConnector")

        assert connector.getMappingRef() is None

    def test_SwConnector_get_set_MappingRef(self):
        """Test mappingRef getter and setter with round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = AssemblySwConnector(ar_root, "TestSwConnector")

        ref = RefType()
        ref.setDest("PORT-INTERFACE-MAPPING")
        ref.setValue("/Mapping/IfMap")
        result = connector.setMappingRef(ref)
        assert result is connector
        assert connector.getMappingRef() == ref

        connector.setMappingRef(None)
        assert connector.getMappingRef() == ref

    def test_AssemblySwConnector(self):
        """Test AssemblySwConnector class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        assembly_connector = AssemblySwConnector(ar_root, "TestAssemblySwConnector")

        assert assembly_connector.parent == ar_root
        assert assembly_connector.short_name == "TestAssemblySwConnector"
        assert assembly_connector.mappingRef is None
        assert assembly_connector.providerIRef is None
        assert assembly_connector.requesterIRef is None

        # Test setters and getters
        ref = RefType()
        assembly_connector.setMappingRef(ref)
        assert assembly_connector.getMappingRef() == ref

    def test_DelegationSwConnector(self):
        """Test DelegationSwConnector class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        delegation_connector = DelegationSwConnector(ar_root, "TestDelegationSwConnector")

        assert delegation_connector.parent == ar_root
        assert delegation_connector.short_name == "TestDelegationSwConnector"
        assert delegation_connector.mappingRef is None
        assert delegation_connector.innerPortIRref is None
        assert delegation_connector.outerPortRef is None

        # Test setters and getters
        ref = RefType()
        delegation_connector.setMappingRef(ref)
        assert delegation_connector.getMappingRef() == ref

    def test_PassThroughSwConnector(self):
        """Test PassThroughSwConnector class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        pass_through_connector = PassThroughSwConnector(ar_root, "TestPassThroughSwConnector")

        assert pass_through_connector.parent == ar_root
        assert pass_through_connector.short_name == "TestPassThroughSwConnector"
        assert pass_through_connector.mappingRef is None
        assert pass_through_connector.providedOuterPortRef is None
        assert pass_through_connector.requiredOuterPortRef is None

        # Test setters and getters
        ref = RefType()
        pass_through_connector.setMappingRef(ref)
        assert pass_through_connector.getMappingRef() == ref

    def test_PassThroughSwConnector_initialization(self):
        """Test PassThroughSwConnector initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = PassThroughSwConnector(ar_root, "TestPassThroughSwConnector")

        assert connector.getMappingRef() is None
        assert connector.getProvidedOuterPortRef() is None
        assert connector.getRequiredOuterPortRef() is None

    def test_PassThroughSwConnector_get_set_ProvidedOuterPortRef(self):
        """Test providedOuterPortRef getter and setter with round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = PassThroughSwConnector(ar_root, "TestPassThroughSwConnector")

        ref = RefType()
        ref.setDest("P-PORT-PROTOTYPE")
        ref.setValue("/Composition/PPort")
        result = connector.setProvidedOuterPortRef(ref)
        assert result is connector
        assert connector.getProvidedOuterPortRef() == ref

        connector.setProvidedOuterPortRef(None)
        assert connector.getProvidedOuterPortRef() == ref

    def test_PassThroughSwConnector_get_set_RequiredOuterPortRef(self):
        """Test requiredOuterPortRef getter and setter with round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = PassThroughSwConnector(ar_root, "TestPassThroughSwConnector")

        ref = RefType()
        ref.setDest("R-PORT-PROTOTYPE")
        ref.setValue("/Composition/RPort")
        result = connector.setRequiredOuterPortRef(ref)
        assert result is connector
        assert connector.getRequiredOuterPortRef() == ref

        connector.setRequiredOuterPortRef(None)
        assert connector.getRequiredOuterPortRef() == ref


class TestInstantiationRTEEventProps:
    """Test class for InstantiationRTEEventProps abstract class."""

    def test_instantiation_rte_event_props_abstract(self):
        """Test that InstantiationRTEEventProps is an abstract class."""
        import pytest

        with pytest.raises(TypeError):
            InstantiationRTEEventProps()

    def test_get_set_refined_event_iref(self):
        """Test refinedEventIRef getter and setter."""
        props = InstantiationTimingEventProps()

        assert props.getRefinedEventIRef() is None

        refined_event = InstanceEventInCompositionInstanceRef()
        props.setRefinedEventIRef(refined_event)
        assert props.getRefinedEventIRef() == refined_event

        props.setRefinedEventIRef(None)
        assert props.getRefinedEventIRef() == refined_event

    def test_get_set_short_label(self):
        """Test shortLabel getter and setter."""
        props = InstantiationTimingEventProps()

        assert props.getShortLabel() is None

        short_label = Identifier()
        short_label.setValue("Label")
        props.setShortLabel(short_label)
        assert props.getShortLabel() == short_label

        props.setShortLabel(None)
        assert props.getShortLabel() == short_label


class TestInstantiationTimingEventProps:
    """Test class for InstantiationTimingEventProps class."""

    def test_initialization(self):
        """Test InstantiationTimingEventProps initialization and defaults."""
        props = InstantiationTimingEventProps()

        assert props.getRefinedEventIRef() is None
        assert props.getShortLabel() is None
        assert props.getPeriod() is None

    def test_get_set_period(self):
        """Test period getter and setter."""
        props = InstantiationTimingEventProps()

        period = TimeValue()
        period.setValue("0.01")
        props.setPeriod(period)
        assert props.getPeriod() == period

        props.setPeriod(None)
        assert props.getPeriod() == period


class TestCompositionSwComponentType:
    """Test class for CompositionSwComponentType class."""

    def test_initialization(self):
        """Test CompositionSwComponentType initialization and defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        assert composition.getComponents() == []
        assert composition.getSwConnectors() == []
        assert composition.getConstantValueMappingRefs() == []
        assert composition.getDataTypeMappingRefs() == []
        assert composition.getInstantiationRTEEventProps() == []
        assert composition.getPhysicalDimensionMappingRef() is None

    def test_create_sw_component_prototype(self):
        """Test createSwComponentPrototype method."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        prototype = composition.createSwComponentPrototype("Cmp1")
        assert isinstance(prototype, SwComponentPrototype)
        assert prototype.short_name == "Cmp1"
        assert composition.getComponents() == [prototype]

        prototype_again = composition.createSwComponentPrototype("Cmp1")
        assert prototype_again is prototype

    def test_create_connectors(self):
        """Test createAssemblySwConnector, createDelegationSwConnector and createPassThroughSwConnector."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        assembly = composition.createAssemblySwConnector("AsmConn")
        delegation = composition.createDelegationSwConnector("DelConn")
        pass_through = composition.createPassThroughSwConnector("PassConn")

        assert isinstance(assembly, AssemblySwConnector)
        assert isinstance(delegation, DelegationSwConnector)
        assert isinstance(pass_through, PassThroughSwConnector)
        assert len(composition.getSwConnectors()) == 3
        assert composition.getAssemblySwConnectors() == [assembly]
        assert composition.getDelegationSwConnectors() == [delegation]
        assert composition.getPassThroughSwConnectors() == [pass_through]

        assert composition.createAssemblySwConnector("AsmConn") is assembly
        assert len(composition.getSwConnectors()) == 3

    def test_remove_all_connectors(self):
        """Test removeAllAssemblySwConnector, removeAllDelegationSwConnector and removeAllPassThroughSwConnector."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        composition.createAssemblySwConnector("AsmConn")
        composition.createDelegationSwConnector("DelConn")
        composition.createPassThroughSwConnector("PassConn")

        composition.removeAllAssemblySwConnector()
        assert len(composition.getSwConnectors()) == 2

        composition.removeAllDelegationSwConnector()
        assert len(composition.getSwConnectors()) == 1

        composition.removeAllPassThroughSwConnector()
        assert len(composition.getSwConnectors()) == 0

    def test_remove_element_connector(self):
        """Test that removeElement removes a connector from the connectors list."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        assembly = composition.createAssemblySwConnector("AsmConn")
        composition.createDelegationSwConnector("DelConn")

        composition.removeElement("AsmConn")
        assert assembly not in composition.getSwConnectors()
        assert len(composition.getSwConnectors()) == 1

    def test_add_get_constant_value_mapping_refs(self):
        """Test addConstantValueMappingRef and getConstantValueMappingRefs methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        ref1 = RefType()
        ref1.setDest("CONSTANT-SPECIFICATION-MAPPING-SET")
        ref1.setValue("/Mapping/Set1")
        composition.addConstantValueMappingRef(ref1)
        assert composition.getConstantValueMappingRefs() == [ref1]

        ref2 = RefType()
        ref2.setDest("CONSTANT-SPECIFICATION-MAPPING-SET")
        ref2.setValue("/Mapping/Set2")
        composition.addConstantValueMappingRef(ref2)
        assert composition.getConstantValueMappingRefs() == [ref1, ref2]

        composition.addConstantValueMappingRef(None)
        assert composition.getConstantValueMappingRefs() == [ref1, ref2]

    def test_add_get_data_type_mapping_refs(self):
        """Test addDataTypeMappingRef and getDataTypeMappingRefs methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        ref1 = RefType()
        ref1.setDest("DATA-TYPE-MAPPING-SET")
        ref1.setValue("/Mapping/Set1")
        composition.addDataTypeMappingRef(ref1)
        assert composition.getDataTypeMappingRefs() == [ref1]

        ref2 = RefType()
        ref2.setDest("DATA-TYPE-MAPPING-SET")
        ref2.setValue("/Mapping/Set2")
        composition.addDataTypeMappingRef(ref2)
        assert composition.getDataTypeMappingRefs() == [ref1, ref2]

        composition.addDataTypeMappingRef(None)
        assert composition.getDataTypeMappingRefs() == [ref1, ref2]

    def test_add_get_instantiation_rte_event_props(self):
        """Test addInstantiationRTEEventProps and getInstantiationRTEEventProps methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        props1 = InstantiationTimingEventProps()
        props1.setPeriod(TimeValue())
        composition.addInstantiationRTEEventProps(props1)
        assert composition.getInstantiationRTEEventProps() == [props1]

        props2 = InstantiationTimingEventProps()
        composition.addInstantiationRTEEventProps(props2)
        assert composition.getInstantiationRTEEventProps() == [props1, props2]

        composition.addInstantiationRTEEventProps(None)
        assert composition.getInstantiationRTEEventProps() == [props1, props2]

    def test_set_get_physical_dimension_mapping_ref(self):
        """Test setPhysicalDimensionMappingRef and getPhysicalDimensionMappingRef methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition = CompositionSwComponentType(ar_root, "TestComposition")

        ref = RefType()
        ref.setDest("PHYSICAL-DIMENSION-MAPPING-SET")
        ref.setValue("/Mapping/DimSet")
        composition.setPhysicalDimensionMappingRef(ref)
        assert composition.getPhysicalDimensionMappingRef() == ref

        composition.setPhysicalDimensionMappingRef(None)
        assert composition.getPhysicalDimensionMappingRef() == ref
