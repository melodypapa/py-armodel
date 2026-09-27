import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
    FibexElement,
    ISignalIPduGroup,
)

CLASS_NOTE = (
    "The AUTOSAR COM Layer is able to start and to stop sending and receiving configurable groups of I-Pdus "
    "during runtime. An ISignalIPduGroup contains either ISignalIPdus or ISignalIPduGroups. "
    "Tags: atp.recommendedPackage=ISignaliPduGroup"
)
NOTES = {
    "communicationDirection": "This attribute determines in which direction IPdus that are contained in this IPduGroup will be transmitted (communication direction can be either In or Out).",
    "communicationMode": (
        "This attribute defines the use-case for this ISignalIPduGroup (e.g. diagnostic, debugging etc.). For example, "
        "in a diagnostic mode all IPdus - which are not involved in diagnostic - are disabled. The use cases are not "
        "limited to a fixed enumeration and can be specified as a string."
    ),
    "containedISignalIPduGroupRefs": "An I-Pdu group can be included in other I-Pdu groups. Contained I-Pdu groups shall not be referenced by the EcuInstance.",
    "iSignalIPduRefs": (
        "Reference to a set of Signal I-Pdus, which are contained in the ISignal I-Pdu Group. atpVariation: The content "
        "of a ISignal I-Pdu group can vary (->vehicle modes). Stereotypes: atpSplitable; atpVariation Tags: "
        "atp.Splitkey=iSignalIPdu.iSignalIPdu, iSignalIPdu.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    ),
    "nmPduRefs": (
        "Reference to a set of NmPdus with NmUserData, which are contained in the ISignalIPduGroup. Stereotypes: "
        "atpSplitable; atpVariation Tags: atp.Splitkey=nmPdu.nmPdu, nmPdu.variationPoint.shortLabel "
        "vh.latestBindingTime=postBuild"
    ),
}


class TestISignalIPduGroup:
    """Test cases for ISignalIPduGroup (Table 6.32, p.351)."""

    def test_inheritance(self):
        assert issubclass(ISignalIPduGroup, FibexElement)

    def test_initialization_defaults(self):
        group = ISignalIPduGroup(None, "Group")
        assert group.getCommunicationDirection() is None
        assert group.getCommunicationMode() is None
        assert group.getContainedISignalIPduGroupRefs() == []
        assert group.getISignalIPduRefs() == []
        assert group.getNmPduRefs() == []

    def test_get_set_round_trip_and_none_noop(self):
        group = ISignalIPduGroup(None, "Group")

        direction = CommunicationDirectionType().setValue(CommunicationDirectionType.IN)
        assert group.setCommunicationDirection(direction) is group
        assert group.getCommunicationDirection() is direction
        group.setCommunicationDirection(None)
        assert group.getCommunicationDirection() is direction

        assert group.setCommunicationMode("diagnostic") is group
        assert group.getCommunicationMode() == "diagnostic"
        group.setCommunicationMode(None)
        assert group.getCommunicationMode() == "diagnostic"

    def test_add_refs_append_and_none_noop(self):
        group = ISignalIPduGroup(None, "Group")
        ref = RefType()
        ref.value = "/groups/sub"
        assert group.addContainedISignalIPduGroupRef(ref) is group
        assert group.getContainedISignalIPduGroupRefs() == [ref]
        group.addContainedISignalIPduGroupRef(None)
        assert len(group.getContainedISignalIPduGroupRefs()) == 1

        pdu_ref = RefType()
        pdu_ref.value = "/pdus/p1"
        assert group.addISignalIPduRef(pdu_ref) is group
        assert group.getISignalIPduRefs() == [pdu_ref]
        group.addISignalIPduRef(None)
        assert len(group.getISignalIPduRefs()) == 1

        nm_ref = RefType()
        nm_ref.value = "/pdus/nm1"
        assert group.addNmPduRef(nm_ref) is group
        assert group.getNmPduRefs() == [nm_ref]
        group.addNmPduRef(None)
        assert len(group.getNmPduRefs()) == 1

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalIPduGroup.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        group = ISignalIPduGroup(None, "Group")
        pairs = (
            ("getCommunicationDirection", "setCommunicationDirection", "communicationDirection"),
            ("getCommunicationMode", "setCommunicationMode", "communicationMode"),
            ("getContainedISignalIPduGroupRefs", "addContainedISignalIPduGroupRef", "containedISignalIPduGroupRefs"),
            ("getISignalIPduRefs", "addISignalIPduRef", "iSignalIPduRefs"),
            ("getNmPduRefs", "addNmPduRef", "nmPduRefs"),
        )
        for getter_name, setter_name, key in pairs:
            getter = getattr(group, getter_name)
            setter = getattr(group, setter_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(setter.__doc__).split("\n")[0] == NOTES[key], key
