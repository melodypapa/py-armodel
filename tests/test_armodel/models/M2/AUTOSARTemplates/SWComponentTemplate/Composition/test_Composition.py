"""
This module contains tests for the Composition subdirectory in SWComponentTemplate.
"""
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    DelegationSwConnector,
    PassThroughSwConnector,
    SwComponentPrototype,
    SwConnector,
)


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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
            ARObject,
        )
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
