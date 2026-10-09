import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Pdu

CLASS_NOTE = "Collection of all Pdus that can be routed through a bus interface."
CLASS_CONSTRAINTS = (
    "[constr_5249] Existence of Pdu.length: For each Pdu, the attribute length shall exist at the time when the System Description is complete.",
    "[constr_5321] Value range of Pdu.length: The value of Pdu.length shall be in the range of 0..4294967295 Bytes.",
    "[constr_3448] Restriction for usage of Pdu.hasDynamicLength: The Pdu.hasDynamicLength attribute is only relevant for UserDefinedPdus, UserDefinedIPdus, J1939DcmIPdus.",
)
NOTES = {
    "hasDynamicLength": ("This attribute defines whether the Pdu has dynamic length (true) or not (false). Please note that the usage of this attribute is restricted by [constr_3448]."),
    "length": (
        "Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the "
        "maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this "
        "parameter was defined in bits. The Pdu length of zero bytes is allowed."
    ),
}


class ConcretePdu(Pdu):
    pass


class TestPdu:
    """Test cases for Pdu (Table 6.17, p.340)."""

    def test_inheritance(self):
        assert issubclass(Pdu, FibexElement)

    def test_abstract(self):
        with pytest.raises(TypeError):
            Pdu(None, "Pdu1")

    def test_initialization_defaults(self):
        pdu = ConcretePdu(None, "Pdu1")
        assert pdu.getShortName() == "Pdu1"
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None

    def test_get_set_has_dynamic_length(self):
        pdu = ConcretePdu(None, "Pdu1")

        value = Boolean()
        value.setValue(True)
        assert pdu.setHasDynamicLength(value) is pdu
        assert pdu.getHasDynamicLength() is value
        assert pdu.getHasDynamicLength().getValue() is True
        pdu.setHasDynamicLength(None)
        assert pdu.getHasDynamicLength() is value

    def test_get_set_length(self):
        pdu = ConcretePdu(None, "Pdu1")

        length = UnlimitedInteger()
        length.setValue("8")
        assert pdu.setLength(length) is pdu
        assert pdu.getLength() is length
        assert pdu.getLength().getValue() == 8
        pdu.setLength(None)
        assert pdu.getLength() is length

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Pdu.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        pdu = ConcretePdu(None, "Pdu1")
        pairs = (
            ("getHasDynamicLength", "setHasDynamicLength", "hasDynamicLength"),
            ("getLength", "setLength", "length"),
        )
        for getter_name, mutator_name, key in pairs:
            getter = getattr(pdu, getter_name)
            mutator = getattr(pdu, mutator_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert Pdu.__init__.__doc__ is None
