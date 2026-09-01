"""
This module contains tests for the PortInterfaceBlueprintMapping class in the
AUTOSAR CommonStructure.StandardizationTemplate.BlueprintDedicated package.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortInterfaceBlueprint import (
    PortInterfaceBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestPortInterfaceBlueprintMapping:
    """
    Test class for PortInterfaceBlueprintMapping functionality.
    """

    def test_initialization(self):
        obj = PortInterfaceBlueprintMapping()
        assert isinstance(obj, PortInterfaceBlueprintMapping)
        assert obj.getPortInterfaceBlueprintRef() is None
        assert obj.getDerivedPortInterfaceRef() is None

    def test_get_set_port_interface_blueprint_ref(self):
        obj = PortInterfaceBlueprintMapping()
        ref = RefType()
        ref.setDest("PORT-INTERFACE")
        ref.setValue("/Pkg/BlueprintIf")
        obj.setPortInterfaceBlueprintRef(ref)
        assert obj.getPortInterfaceBlueprintRef() is ref
        assert obj.getPortInterfaceBlueprintRef().getDest() == "PORT-INTERFACE"
        assert obj.getPortInterfaceBlueprintRef().getValue() == "/Pkg/BlueprintIf"

    def test_get_set_derived_port_interface_ref(self):
        obj = PortInterfaceBlueprintMapping()
        ref = RefType()
        ref.setDest("PORT-INTERFACE")
        ref.setValue("/Pkg/DerivedIf")
        obj.setDerivedPortInterfaceRef(ref)
        assert obj.getDerivedPortInterfaceRef() is ref
        assert obj.getDerivedPortInterfaceRef().getValue() == "/Pkg/DerivedIf"

    def test_set_ref_none_is_noop(self):
        obj = PortInterfaceBlueprintMapping()
        obj.setPortInterfaceBlueprintRef(None)
        obj.setDerivedPortInterfaceRef(None)
        assert obj.getPortInterfaceBlueprintRef() is None
        assert obj.getDerivedPortInterfaceRef() is None

    def test_set_ref_chaining(self):
        obj = PortInterfaceBlueprintMapping()
        ref = RefType()
        returned = obj.setPortInterfaceBlueprintRef(ref)
        assert returned is obj
        returned = obj.setDerivedPortInterfaceRef(ref)
        assert returned is obj

    def test_is_atp_blueprint_mapping(self):
        obj = PortInterfaceBlueprintMapping()
        assert isinstance(obj, AtpBlueprintMapping)
