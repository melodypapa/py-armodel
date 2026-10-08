import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpEcu


def _boolean(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class Test_FlexrayTpEcu:
    # Table 6.244, p.597 — attribute notes from the XSD (the PDF table has no Note column)
    NOTE_CANCELLATION = "With this switch Tx and Rx Cancellation can be turned on or off."
    NOTE_CYCLE_TIME_MAIN_FUNCTION = "The period between successive calls to the Main Function of the AUTOSAR TP. Specified in seconds."
    NOTE_ECU_INSTANCE_REF = "Connection to the ECUInstance in the Topology"
    NOTE_FULL_DUPLEX_ENABLED = "The full duplex mechanisms is enabled if this attribute is set to true. Otherwise half duplex is enabled."

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.244, p.597 — class Note verbatim from the markdown + table constraints appended
        note = "ECU specific TP configuration parameters. Each TpEcu element has a reference to exactly one ECUInstance in the topology."
        constrs = [
            "[constr_9236] Existence of FlexrayTpEcu.ecuInstance: For each FlexrayTpEcu, the reference to EcuInstance in the role ecuInstance shall exist at the time when the System Description is complete.",
            "[constr_9237] Existence of FlexrayTpEcu.fullDuplexEnabled: For each FlexrayTpEcu, the attribute fullDuplexEnabled shall exist at the time when the System Description is complete.",
        ]
        expected = note + "\n\n" + "\n\n".join(constrs)
        assert cleandoc(FlexrayTpEcu.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert FlexrayTpEcu.__init__.__doc__ is None

    def test_heritage(self):
        ecu = FlexrayTpEcu()
        assert isinstance(ecu, ARObject)

    def test_initialization(self):
        # spec displayed order: cancellation, cycleTimeMainFunction, ecuInstance, fullDuplexEnabled
        ecu = FlexrayTpEcu()
        assert ecu.getCancellation() is None
        assert ecu.getCycleTimeMainFunction() is None
        assert ecu.getEcuInstanceRef() is None
        assert ecu.getFullDuplexEnabled() is None

    def test_get_set_cancellation(self):
        ecu = FlexrayTpEcu()
        value = _boolean(True)
        assert ecu.setCancellation(value) is ecu
        assert ecu.getCancellation() is value
        ecu.setCancellation(None)
        assert ecu.getCancellation() is value

    def test_get_set_cycle_time_main_function(self):
        ecu = FlexrayTpEcu()
        value = _time(0.005)
        assert ecu.setCycleTimeMainFunction(value) is ecu
        assert ecu.getCycleTimeMainFunction() is value
        ecu.setCycleTimeMainFunction(None)
        assert ecu.getCycleTimeMainFunction() is value

    def test_get_set_ecu_instance_ref(self):
        ecu = FlexrayTpEcu()
        value = _ref("/Topology/Ecu1", "ECU-INSTANCE")
        assert ecu.setEcuInstanceRef(value) is ecu
        assert ecu.getEcuInstanceRef() is value
        ecu.setEcuInstanceRef(None)
        assert ecu.getEcuInstanceRef() is value

    def test_get_set_full_duplex_enabled(self):
        ecu = FlexrayTpEcu()
        value = _boolean(True)
        assert ecu.setFullDuplexEnabled(value) is ecu
        assert ecu.getFullDuplexEnabled() is value
        ecu.setFullDuplexEnabled(None)
        assert ecu.getFullDuplexEnabled() is value

    def test_type_hints_pins(self):
        assert typing.get_type_hints(FlexrayTpEcu.getCancellation).get("return") == Optional[Boolean]
        assert typing.get_type_hints(FlexrayTpEcu.setCancellation).get("return") is FlexrayTpEcu
        assert typing.get_type_hints(FlexrayTpEcu.getCycleTimeMainFunction).get("return") == Optional[TimeValue]
        assert typing.get_type_hints(FlexrayTpEcu.setCycleTimeMainFunction).get("return") is FlexrayTpEcu
        assert typing.get_type_hints(FlexrayTpEcu.getEcuInstanceRef).get("return") == Optional[RefType]
        assert typing.get_type_hints(FlexrayTpEcu.setEcuInstanceRef).get("return") is FlexrayTpEcu
        assert typing.get_type_hints(FlexrayTpEcu.getFullDuplexEnabled).get("return") == Optional[Boolean]
        assert typing.get_type_hints(FlexrayTpEcu.setFullDuplexEnabled).get("return") is FlexrayTpEcu

    def test_docstrings_are_spec_note_verbatim(self):
        assert cleandoc(FlexrayTpEcu.getCancellation.__doc__) == self.NOTE_CANCELLATION
        assert cleandoc(FlexrayTpEcu.setCancellation.__doc__).split("\n")[0] == self.NOTE_CANCELLATION
        assert cleandoc(FlexrayTpEcu.getCycleTimeMainFunction.__doc__) == self.NOTE_CYCLE_TIME_MAIN_FUNCTION
        assert cleandoc(FlexrayTpEcu.setCycleTimeMainFunction.__doc__).split("\n")[0] == self.NOTE_CYCLE_TIME_MAIN_FUNCTION
        assert cleandoc(FlexrayTpEcu.getEcuInstanceRef.__doc__) == self.NOTE_ECU_INSTANCE_REF
        assert cleandoc(FlexrayTpEcu.setEcuInstanceRef.__doc__).split("\n")[0] == self.NOTE_ECU_INSTANCE_REF
        assert cleandoc(FlexrayTpEcu.getFullDuplexEnabled.__doc__) == self.NOTE_FULL_DUPLEX_ENABLED
        assert cleandoc(FlexrayTpEcu.setFullDuplexEnabled.__doc__).split("\n")[0] == self.NOTE_FULL_DUPLEX_ENABLED

    def test_variation_point_capable(self):
        ecu = FlexrayTpEcu()
        assert ecu.getVariationPoint() is None
