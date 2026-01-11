"""
This module contains comprehensive tests for the Composition module in SWComponentTemplate.
Tests cover all classes and methods in the __init__.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    SwComponentPrototype, SwConnector, AssemblySwConnector, DelegationSwConnector, PassThroughSwConnector
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestSwComponentPrototype:
    """Test class for SwComponentPrototype class."""
    
    def test_sw_component_prototype_initialization(self):
        """Test SwComponentPrototype initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_proto = SwComponentPrototype(ar_root, "TestSwComponentPrototype")
        
        assert comp_proto.parent == ar_root
        assert comp_proto.short_name == "TestSwComponentPrototype"
        assert comp_proto.typeTRef is None
        
        # Test typeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        type_ref = RefType()
        type_ref.setValue("/Type/Ref")
        comp_proto.setTypeTRef(type_ref)
        assert comp_proto.getTypeTRef() == type_ref


class TestSwConnector:
    """Test class for SwConnector abstract class."""
    
    def test_sw_connector_initialization(self):
        """Test SwConnector initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        # SwConnector has ABCMeta but no abstract methods, so it can be instantiated
        connector = SwConnector(ar_root, "TestSwConnector")
        
        assert connector.parent == ar_root
        assert connector.short_name == "TestSwConnector"
        assert connector.mappingRef is None


class TestAssemblySwConnector:
    """Test class for AssemblySwConnector class."""
    
    def test_assembly_sw_connector_initialization(self):
        """Test AssemblySwConnector initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = AssemblySwConnector(ar_root, "TestAssemblySwConnector")
        
        assert connector.parent == ar_root
        assert connector.short_name == "TestAssemblySwConnector"
        assert connector.mappingRef is None
        assert connector.providerIRef is None
        assert connector.requesterIRef is None
        
        # Test mappingRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        mapping_ref = RefType()
        mapping_ref.setValue("/Mapping/Ref")
        connector.setMappingRef(mapping_ref)
        assert connector.getMappingRef() == mapping_ref
        
        # Test providerIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import PPortInCompositionInstanceRef
        provider_iref = PPortInCompositionInstanceRef()
        connector.setProviderIRef(provider_iref)
        assert connector.getProviderIRef() == provider_iref
        
        # Test requesterIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import RPortInCompositionInstanceRef
        requester_iref = RPortInCompositionInstanceRef()
        connector.setRequesterIRef(requester_iref)
        assert connector.getRequesterIRef() == requester_iref


class TestDelegationSwConnector:
    """Test class for DelegationSwConnector class."""
    
    def test_delegation_sw_connector_initialization(self):
        """Test DelegationSwConnector initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = DelegationSwConnector(ar_root, "TestDelegationSwConnector")
        
        assert connector.parent == ar_root
        assert connector.short_name == "TestDelegationSwConnector"
        assert connector.mappingRef is None
        assert connector.innerPortIRref is None
        assert connector.outerPortRef is None
        
        # Test mappingRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        mapping_ref = RefType()
        mapping_ref.setValue("/Mapping/Ref")
        connector.setMappingRef(mapping_ref)
        assert connector.getMappingRef() == mapping_ref
        
        # Test innerPortIRref methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import InnerPortGroupInCompositionInstanceRef
        inner_iref = InnerPortGroupInCompositionInstanceRef()
        connector.setInnerPortIRref(inner_iref)
        assert connector.getInnerPortIRref() == inner_iref
        
        # Test outerPortRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        outer_ref = RefType()
        outer_ref.setValue("/Outer/Port/Ref")
        connector.setOuterPortRef(outer_ref)
        assert connector.getOuterPortRef() == outer_ref


class TestPassThroughSwConnector:
    """Test class for PassThroughSwConnector class."""
    
    def test_pass_through_sw_connector_initialization(self):
        """Test PassThroughSwConnector initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        connector = PassThroughSwConnector(ar_root, "TestPassThroughSwConnector")
        
        assert connector.parent == ar_root
        assert connector.short_name == "TestPassThroughSwConnector"
        assert connector.mappingRef is None
        assert connector.providedOuterPortRef is None
        assert connector.requiredOuterPortRef is None
        
        # Test mappingRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        mapping_ref = RefType()
        mapping_ref.setValue("/Mapping/Ref")
        connector.setMappingRef(mapping_ref)
        assert connector.getMappingRef() == mapping_ref
        
        # Test providedOuterPortRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        provided_ref = RefType()
        provided_ref.setValue("/Provided/Port/Ref")
        connector.setProvidedOuterPortRef(provided_ref)
        assert connector.getProvidedOuterPortRef() == provided_ref
        
        # Test requiredOuterPortRef methods
        required_ref = RefType()
        required_ref.setValue("/Required/Port/Ref")
        connector.setRequiredOuterPortRef(required_ref)
        assert connector.getRequiredOuterPortRef() == required_ref