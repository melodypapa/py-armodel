import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PackageableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SoAdRoutingGroup
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import EventGroupControlTypeEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


SPEC_CLASS_NOTE = (
    "Routing of Pdus in the SoAd can be activated or deactivated. "
    "The ShortName of this element shall contain the RoutingGroupId. "
    "Tags: atp.Status=obsolete atp.recommendedPackage=SoAdRoutingGroups"
)

SPEC_ATTRIBUTE_NOTE = (
    "This attribute defines the type of a RoutingGroup. There are RoutingGroups that activate "
    "the data path for unicast or multicast events of an event group. And there are RoutingGroups "
    "that activate the data path for initial events that are triggered, namely events that are "
    "sent out on the server side after a client got subscribed. Please note that this attribute is "
    "only valid for event communication (Sender Receiver communication) and shall be omitted in "
    "MethodActivationRoutingGroups."
)


class TestSoAdRoutingGroup:
    """Test cases for SoAdRoutingGroup (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.115, p.2057)."""

    def test_initialization(self):
        parent = MockParent()
        group = SoAdRoutingGroup(parent, "RG1")

        assert group.getShortName() == "RG1"
        assert group.getParent() is parent
        assert group.eventGroupControlType is None
        assert isinstance(group, FibexElement)
        assert isinstance(group, PackageableElement)
        assert isinstance(group, Identifiable)
        assert isinstance(group, Referrable)
        assert isinstance(group, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        group = SoAdRoutingGroup(MockParent(), "RG1")

        assert group.__doc__ == SPEC_CLASS_NOTE

    def test_get_set_eventGroupControlType(self):
        group = SoAdRoutingGroup(MockParent(), "RG1")

        control_type = EventGroupControlTypeEnum().setValue(EventGroupControlTypeEnum.ACTIVATION_AND_TRIGGER_UNICAST)
        result = group.setEventGroupControlType(control_type)
        assert result is group
        assert group.getEventGroupControlType() is control_type

        group.setEventGroupControlType(None)
        assert group.getEventGroupControlType() is control_type

    def test_get_set_eventGroupControlType_docstrings_are_spec_note_verbatim(self):
        group = SoAdRoutingGroup(MockParent(), "RG1")

        assert group.getEventGroupControlType.__doc__ == SPEC_ATTRIBUTE_NOTE
        assert group.setEventGroupControlType.__doc__ == ("\n        " + SPEC_ATTRIBUTE_NOTE + "\n        A None value is a no-op and does not overwrite an existing eventGroupControlType.\n        ")

    def test_type_hints_resolve_to_spec_types(self):
        getter_hints = typing.get_type_hints(SoAdRoutingGroup.getEventGroupControlType)
        assert getter_hints["return"] == typing.Optional[EventGroupControlTypeEnum]

        setter_hints = typing.get_type_hints(SoAdRoutingGroup.setEventGroupControlType)
        assert setter_hints["value"] == typing.Optional[EventGroupControlTypeEnum]
        assert setter_hints["return"] is SoAdRoutingGroup
