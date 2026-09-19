"""
This module contains tests for the ComManagementMapping class
in the AUTOSAR SystemTemplate module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ComManagementMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import PortGroupInSystemInstanceRef

SPEC_NOTE = "Describes a mapping between one or several Mode Management PortGroups and communication channels."


def _port_group_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest("PORT-GROUP")
    return ref


GROUP_NOTE = "IPduGroup participating in a Mode Management PortGroup."
PORT_GROUP_NOTE = (
    "Mode Management PortGroup to be mapped onto a communication channel. This reference is optional in case that the "
    "System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy systems."
)
PHYSICAL_CHANNEL_NOTE = "This reference maps the Mode Management PortGroup partial network to communication channels."


class TestComManagementMapping:
    def test_initialization(self):
        """Test that the concrete ComManagementMapping is an Identifiable wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mapping = ComManagementMapping(ar_root, "TestComManagementMapping")

        assert isinstance(mapping, Identifiable)
        assert isinstance(mapping, VariationPointCapable)
        assert mapping.getShortName() == "TestComManagementMapping"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 5.46)"""
        assert ComManagementMapping.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert ComManagementMapping.__init__.__doc__ is None

    def test_attribute_docstrings_are_spec_notes(self):
        """Test that the adder and getter docstrings carry the attribute Notes verbatim (Table 5.46)"""
        assert ComManagementMapping.addComManagementGroupRef.__doc__.strip().startswith(GROUP_NOTE)
        assert ComManagementMapping.getComManagementGroupRefs.__doc__.strip() == GROUP_NOTE
        assert ComManagementMapping.addComManagementPortGroupIRef.__doc__.strip().startswith(PORT_GROUP_NOTE)
        assert ComManagementMapping.getComManagementPortGroupIRefs.__doc__.strip() == PORT_GROUP_NOTE
        assert ComManagementMapping.addPhysicalChannelRef.__doc__.strip().startswith(PHYSICAL_CHANNEL_NOTE)
        assert ComManagementMapping.getPhysicalChannelRefs.__doc__.strip() == PHYSICAL_CHANNEL_NOTE

    def test_get_set_com_management_group_refs(self):
        """Test comManagementGroupRefs default, add chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mapping = ComManagementMapping(ar_root, "TestGroupRefs")

        assert mapping.getComManagementGroupRefs() == []

        ref = RefType()
        ref.setValue("/Systems/ISignalIPduGroup")
        ref.setDest("I-SIGNAL-I-PDU-GROUP")
        assert mapping == mapping.addComManagementGroupRef(ref)
        assert mapping.getComManagementGroupRefs() == [ref]

        assert mapping == mapping.addComManagementGroupRef(None)
        assert mapping.getComManagementGroupRefs() == [ref]

        getter_hints = typing.get_type_hints(ComManagementMapping.getComManagementGroupRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = typing.get_type_hints(ComManagementMapping.addComManagementGroupRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is ComManagementMapping

    def test_get_set_com_management_port_group_irefs(self):
        """Test comManagementPortGroupIRefs default, add chaining, None no-op and typing (Kind iref -> PortGroupInSystemInstanceRef list)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mapping = ComManagementMapping(ar_root, "TestPortGroupIRefs")

        assert mapping.getComManagementPortGroupIRefs() == []

        iref1 = PortGroupInSystemInstanceRef()
        iref1.setTargetRef(_port_group_ref("/Systems/RootComp/PortGroup1"))
        iref2 = PortGroupInSystemInstanceRef()
        iref2.setTargetRef(_port_group_ref("/Systems/RootComp/PortGroup2"))
        assert mapping == mapping.addComManagementPortGroupIRef(iref1)
        assert mapping == mapping.addComManagementPortGroupIRef(iref2)
        assert mapping.getComManagementPortGroupIRefs() == [iref1, iref2]

        assert mapping == mapping.addComManagementPortGroupIRef(None)
        assert mapping.getComManagementPortGroupIRefs() == [iref1, iref2]

        getter_hints = typing.get_type_hints(ComManagementMapping.getComManagementPortGroupIRefs)
        assert getter_hints.get("return") == typing.List[PortGroupInSystemInstanceRef]

        adder_hints = typing.get_type_hints(ComManagementMapping.addComManagementPortGroupIRef)
        assert adder_hints.get("value") == typing.Optional[PortGroupInSystemInstanceRef]
        assert adder_hints.get("return") is ComManagementMapping

    def test_get_set_physical_channel_refs(self):
        """Test physicalChannelRefs spec-many list shape: default, add chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mapping = ComManagementMapping(ar_root, "TestPhysicalChannelRefs")

        assert mapping.getPhysicalChannelRefs() == []

        ref = RefType()
        ref.setValue("/CanSystem/CLUSTERS/CanNetwork/CHANNELS/CanChannel")
        ref.setDest("CAN-COMMUNICATION-CONNECTOR")
        assert mapping == mapping.addPhysicalChannelRef(ref)
        assert mapping.getPhysicalChannelRefs() == [ref]

        ref_2 = RefType()
        ref_2.setValue("/CanSystem/CLUSTERS/CanNetwork/CHANNELS/CanChannel2")
        ref_2.setDest("CAN-COMMUNICATION-CONNECTOR")
        assert mapping == mapping.addPhysicalChannelRef(ref_2)
        assert mapping.getPhysicalChannelRefs() == [ref, ref_2]

        assert mapping == mapping.addPhysicalChannelRef(None)
        assert mapping.getPhysicalChannelRefs() == [ref, ref_2]

        getter_hints = typing.get_type_hints(ComManagementMapping.getPhysicalChannelRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = typing.get_type_hints(ComManagementMapping.addPhysicalChannelRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is ComManagementMapping
