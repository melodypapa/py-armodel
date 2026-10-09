import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    IPdu,
    Pdu,
)

CLASS_NOTE = "The IPdu (Interaction Layer Protocol Data Unit) element is used to sum up all Pdus that are routed by the PduR."
NOTES = {
    "containedIPduProps": "Defines whether this IPdu may be collected inside a ContainerIPdu.",
}


class ConcreteIPdu(IPdu):
    pass


class TestIPdu:
    """Test cases for IPdu (Table 6.18, p.341)."""

    def test_inheritance(self):
        assert issubclass(IPdu, Pdu)

    def test_abstract(self):
        with pytest.raises(TypeError):
            IPdu(None, "IPdu1")

    def test_initialization_defaults(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        assert ipdu.getShortName() == "IPdu1"
        assert ipdu.getContainedIPduProps() is None

    def test_get_set_contained_ipdu_props(self):
        ipdu = ConcreteIPdu(None, "IPdu1")

        props = ContainedIPduProps()
        assert ipdu.setContainedIPduProps(props) is ipdu
        assert ipdu.getContainedIPduProps() is props
        ipdu.setContainedIPduProps(None)
        assert ipdu.getContainedIPduProps() is props

    def test_class_docstring_note(self):
        assert inspect.cleandoc(IPdu.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        pairs = (("getContainedIPduProps", "setContainedIPduProps", "containedIPduProps"),)
        for getter_name, mutator_name, key in pairs:
            getter = getattr(ipdu, getter_name)
            mutator = getattr(ipdu, mutator_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert IPdu.__init__.__doc__ is None
