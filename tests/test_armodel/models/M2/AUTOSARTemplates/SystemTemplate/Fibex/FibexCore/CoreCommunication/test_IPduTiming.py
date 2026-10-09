import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import IPduTiming
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import TransmissionModeDeclaration

CLASS_NOTE = "AUTOSAR COM provides the possibility to define two different TRANSMISSION MODES for each IPdu. The Transmission Mode of an IPdu that is valid at a specific point in time is selected using the values of the signals that are mapped to this IPdu. For each IPdu a Transmission Mode Selector is defined. The Transmission Mode Selector is calculated by evaluating the conditions for a subset of signals (class TransmissionModeCondition in the System Template). The Transmission Mode Selector is defined to be true, if at least one Condition evaluates to true and is defined to be false, if all Conditions evaluate to false."
NOTES = {
    "minimumDelay": "Minimum Delay in seconds between successive transmissions of this I-PDU, independent of the Transmission Mode.",
    "transmissionModeDeclaration": "AUTOSAR COM allows configuring statically two different transmission modes for each I-PDU (True and False). The Transmission Mode Selector evaluates the conditions for a subset of signals and decides the transmission mode. It is possible to switch between the transmission modes during runtime.",
}


class TestIPduTiming:
    """Test cases for IPduTiming (Table 6.30, p.348)."""

    def test_inheritance(self):
        assert issubclass(IPduTiming, Describable)
        assert issubclass(IPduTiming, VariationPointCapable)

    def test_concrete_instantiation(self):
        timing = IPduTiming()
        assert type(timing) is IPduTiming

    def test_initialization_defaults(self):
        timing = IPduTiming()
        assert timing.getMinimumDelay() is None
        assert timing.getTransmissionModeDeclaration() is None
        assert timing.getVariationPoint() is None

    def test_get_set_minimum_delay(self):
        timing = IPduTiming()

        value = TimeValue()
        value.setValue("0.005")
        assert timing.setMinimumDelay(value) is timing
        assert timing.getMinimumDelay() is value
        assert timing.getMinimumDelay().getValue() == 0.005
        timing.setMinimumDelay(None)
        assert timing.getMinimumDelay() is value

    def test_get_set_transmission_mode_declaration(self):
        timing = IPduTiming()

        value = TransmissionModeDeclaration()
        condition = value.addTransmissionModeCondition
        assert callable(condition)
        assert timing.setTransmissionModeDeclaration(value) is timing
        assert timing.getTransmissionModeDeclaration() is value
        timing.setTransmissionModeDeclaration(None)
        assert timing.getTransmissionModeDeclaration() is value

    def test_describable_base_accessors(self):
        timing = IPduTiming()
        assert timing.getAdminData() is None
        assert timing.getCategory() is None
        assert timing.getDesc() is None
        assert timing.getIntroduction() is None

    def test_annotation_pins(self):
        pairs = [
            ("getMinimumDelay", "setMinimumDelay", TimeValue),
            ("getTransmissionModeDeclaration", "setTransmissionModeDeclaration", TransmissionModeDeclaration),
        ]
        for getter_name, setter_name, member_type in pairs:
            getter_hints = typing.get_type_hints(getattr(IPduTiming, getter_name))
            assert getter_hints.get("return") == typing.Optional[member_type], getter_name
            setter_hints = typing.get_type_hints(getattr(IPduTiming, setter_name))
            assert setter_hints.get("value") == typing.Optional[member_type], setter_name
            assert setter_hints.get("return") is IPduTiming, setter_name

    def test_class_docstring_note(self):
        assert inspect.cleandoc(IPduTiming.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        timing = IPduTiming()
        for attr, note in NOTES.items():
            getter = getattr(timing, "get%s%s" % (attr[0].upper(), attr[1:]))
            setter = getattr(timing, "set%s%s" % (attr[0].upper(), attr[1:]))
            assert inspect.cleandoc(getter.__doc__) == note, attr
            assert inspect.cleandoc(setter.__doc__).split("\n")[0] == note, attr
            assert "A None value is a no-op and does not overwrite an existing %s." % attr in inspect.cleandoc(setter.__doc__), attr

    def test_init_has_no_docstring(self):
        assert IPduTiming.__init__.__doc__ is None
