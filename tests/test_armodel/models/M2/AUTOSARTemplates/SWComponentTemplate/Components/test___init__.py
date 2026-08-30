"""
This module contains tests for the SwComponentType class in the
AUTOSAR SWComponentTemplate module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PortGroup,
    PPortPrototype,
    PRPortPrototype,
    RPortPrototype,
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import ConsistencyNeeds
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import (
    SwComponentDocumentation,
)


class TestSwComponentType:
    """
    Test class for SwComponentType functionality.
    """

    def _create_concrete(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteSwComponentType(SwComponentType):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        return ConcreteSwComponentType(ar_root, "TestSwComponentType")

    def test_abstract_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = SwComponentType(ar_root, "TestSwComponentType")
            assert False, "SwComponentType should not be instantiable"
        except TypeError:
            pass

    def test_initialization(self):
        obj = self._create_concrete()
        assert obj.getShortName() == "TestSwComponentType"
        assert obj.getConsistencyNeeds() == []
        assert obj.getPorts() == []
        assert obj.getPortGroups() == []
        assert obj.getSwcMappingConstraintsRefs() == []
        assert obj.getSwComponentDocumentation() is None
        assert obj.getUnitGroupRefs() == []

    def test_create_get_consistency_needs(self):
        obj = self._create_concrete()
        consistency_needs = obj.createConsistencyNeeds("ConsistencyNeeds")
        assert isinstance(consistency_needs, ConsistencyNeeds)
        assert consistency_needs in obj.getConsistencyNeeds()
        assert obj.createConsistencyNeeds("ConsistencyNeeds") == consistency_needs

    def test_get_set_swComponentDocumentation(self):
        obj = self._create_concrete()
        documentation = SwComponentDocumentation()
        assert obj.setSwComponentDocumentation(documentation) is obj
        assert obj.getSwComponentDocumentation() == documentation
        obj.setSwComponentDocumentation(None)
        assert obj.getSwComponentDocumentation() == documentation

    def test_create_PPortPrototype(self):
        obj = self._create_concrete()
        port = obj.createPPortPrototype("PPort")
        assert isinstance(port, PPortPrototype)
        assert port in obj.getPorts()
        assert port in obj.getPPortPrototypes()
        assert obj.createPPortPrototype("PPort") == port

    def test_create_RPortPrototype(self):
        obj = self._create_concrete()
        port = obj.createRPortPrototype("RPort")
        assert isinstance(port, RPortPrototype)
        assert port in obj.getPorts()
        assert port in obj.getRPortPrototypes()
        assert obj.createRPortPrototype("RPort") == port

    def test_create_PRPortPrototype(self):
        obj = self._create_concrete()
        port = obj.createPRPortPrototype("PRPort")
        assert isinstance(port, PRPortPrototype)
        assert port in obj.getPorts()
        assert port in obj.getPRPortPrototypes()
        assert obj.createPRPortPrototype("PRPort") == port

    def test_get_port_prototypes(self):
        obj = self._create_concrete()
        obj.createPPortPrototype("PPort")
        obj.createRPortPrototype("RPort")
        obj.createPRPortPrototype("PRPort")
        assert len(obj.getPortPrototypes()) == 3
        assert len(obj.getPPortPrototypes()) == 1
        assert len(obj.getRPortPrototypes()) == 1
        assert len(obj.getPRPortPrototypes()) == 1

    def test_create_PortGroup(self):
        obj = self._create_concrete()
        port_group = obj.createPortGroup("PortGroup")
        assert isinstance(port_group, PortGroup)
        assert port_group in obj.getPortGroups()
        assert obj.createPortGroup("PortGroup") == port_group

    def test_add_get_swcMappingConstraintRefs(self):
        obj = self._create_concrete()
        ref = RefType()
        ref.setValue("/SwComponentMappingConstraints")
        assert obj.addSwcMappingConstraintRef(ref) is obj
        assert ref in obj.getSwcMappingConstraintsRefs()
        obj.addSwcMappingConstraintRef(None)
        assert len(obj.getSwcMappingConstraintsRefs()) == 1

    def test_add_get_unitGroupRefs(self):
        obj = self._create_concrete()
        ref = RefType()
        ref.setValue("/UnitGroup")
        assert obj.addUnitGroupRef(ref) is obj
        assert ref in obj.getUnitGroupRefs()
        obj.addUnitGroupRef(None)
        assert len(obj.getUnitGroupRefs()) == 1
