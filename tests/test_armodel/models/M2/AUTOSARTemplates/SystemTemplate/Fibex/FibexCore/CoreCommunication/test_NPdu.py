import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    IPdu,
    NPdu,
    Pdu,
)

CLASS_NOTE = "This is a Pdu of the Transport Layer. The main purpose of the TP Layer is to segment and reassemble IPdus. Tags: atp.recommendedPackage=Pdus"


class TestNPdu:
    """Test cases for NPdu (Table 6.21, p.343)."""

    def test_inheritance(self):
        assert issubclass(NPdu, IPdu)
        assert issubclass(NPdu, Pdu)

    def test_concrete_instantiation(self):
        pdu = NPdu(None, "NPdu1")
        assert pdu.getShortName() == "NPdu1"

    def test_initialization_defaults(self):
        pdu = NPdu(None, "NPdu1")
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
        assert pdu.getContainedIPduProps() is None

    def test_inherited_get_set_has_dynamic_length(self):
        pdu = NPdu(None, "NPdu1")

        value = Boolean()
        value.setValue(True)
        assert pdu.setHasDynamicLength(value) is pdu
        assert pdu.getHasDynamicLength() is value
        assert pdu.getHasDynamicLength().getValue() is True
        pdu.setHasDynamicLength(None)
        assert pdu.getHasDynamicLength() is value

    def test_inherited_get_set_length(self):
        pdu = NPdu(None, "NPdu1")

        length = UnlimitedInteger()
        length.setValue("8")
        assert pdu.setLength(length) is pdu
        assert pdu.getLength() is length
        assert pdu.getLength().getValue() == 8
        pdu.setLength(None)
        assert pdu.getLength() is length

    def test_inherited_get_set_contained_ipdu_props(self):
        pdu = NPdu(None, "NPdu1")

        props = ContainedIPduProps()
        assert pdu.setContainedIPduProps(props) is pdu
        assert pdu.getContainedIPduProps() is props
        pdu.setContainedIPduProps(None)
        assert pdu.getContainedIPduProps() is props

    def test_class_docstring_note(self):
        assert inspect.cleandoc(NPdu.__doc__) == CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert NPdu.__init__.__doc__ is None
