import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, GeneralPurposeConnection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

CLASS_NOTE = "This meta-class allows to describe the relationship between several PduTriggerings that are defined on the same PhysicalChannel, e.g. to create a link between Rx and Tx Pdu that are used for request/ response. Tags: atp.recommendedPackage=GeneralPurposeConnections"
CLASS_CONSTRAINTS = (
    "[constr_3384] PduTriggerings referenced by GeneralPurposeConnection shall be defined on the same PhysicalChannel: The PduTriggerings that are referenced by the GeneralPurposeConnection in the role pduTriggering shall be defined on the same PhysicalChannel.",
    "[constr_3383] Standardized values for the attribute category of meta-class GeneralPurposeConnection: The following values of the attribute category of metaclass GeneralPurposeConnection are reserved by the AUTOSAR standard: XcpChannel.",
    "[constr_3385] XcpChannel is allowed to reference exactly two PduTriggerings: In case that the category of meta-class GeneralPurposeConnection is set to the value XcpChannel the GeneralPurposeConnection is allowed to reference exactly two PduTriggerings in the role pduTriggering.",
    "[constr_3386] XcpChannel is only allowed to reference PduTriggerings of GeneralPurposeIPdus with category XCP: In case that the category of metaclass GeneralPurposeConnection is set to the value XcpChannel the GeneralPurposeConnection is allowed to reference PduTriggerings of GeneralPurposeIPdus with category XCP.",
)
PDU_TRIGGERING_REFS_NOTE = "Reference to PduTriggerings that are connected to each other by a GeneralPurposeConnection."


class TestGeneralPurposeConnection:
    """Test cases for GeneralPurposeConnection (Table 6.58, p.388)."""

    def test_inheritance(self):
        assert issubclass(GeneralPurposeConnection, ARElement)

    def test_concrete_instantiation(self):
        connection = GeneralPurposeConnection(None, "GeneralPurposeConnection1")
        assert connection.getShortName() == "GeneralPurposeConnection1"

    def test_initialization_defaults(self):
        connection = GeneralPurposeConnection(None, "GeneralPurposeConnection1")
        assert connection.getPduTriggeringRefs() == []

    def test_add_get_pdu_triggering_refs(self):
        connection = GeneralPurposeConnection(None, "GeneralPurposeConnection1")

        ref1 = RefType().setDest("PDU-TRIGGERING-SUBTYPES-ENUM").setValue("/PduTriggerings/RequestTriggering")
        ref2 = RefType().setDest("PDU-TRIGGERING-SUBTYPES-ENUM").setValue("/PduTriggerings/ResponseTriggering")
        assert connection.addPduTriggeringRef(ref1) is connection
        connection.addPduTriggeringRef(ref2)
        assert connection.getPduTriggeringRefs() == [ref1, ref2]

        connection.addPduTriggeringRef(None)
        assert connection.getPduTriggeringRefs() == [ref1, ref2]

    def test_annotation_pins(self):
        getter_hints = typing.get_type_hints(GeneralPurposeConnection.getPduTriggeringRefs)
        assert getter_hints.get("return") == typing.List[RefType]
        add_hints = typing.get_type_hints(GeneralPurposeConnection.addPduTriggeringRef)
        assert add_hints.get("value") == typing.Optional[RefType]
        assert add_hints.get("return") is GeneralPurposeConnection

    def test_class_docstring_note(self):
        assert inspect.cleandoc(GeneralPurposeConnection.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        assert inspect.cleandoc(GeneralPurposeConnection.getPduTriggeringRefs.__doc__) == PDU_TRIGGERING_REFS_NOTE
        assert inspect.cleandoc(GeneralPurposeConnection.addPduTriggeringRef.__doc__).split("\n")[0] == PDU_TRIGGERING_REFS_NOTE

    def test_init_has_no_docstring(self):
        assert GeneralPurposeConnection.__init__.__doc__ is None
