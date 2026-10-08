import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConnectionControl, TpAckType


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


class Test_FlexrayTpConnectionControl:
    # Table 6.240, p.593 — attribute Notes verbatim from the markdown
    NOTE_ACK_TYPE = "This parameter defines the type of acknowledgement which is used for the specific channel."
    NOTE_MAX_FC_WAIT = 'This attribute defines the maximum number of Flow Control N-PDUs with FlowState "WAIT".'
    NOTE_MAX_NUMBER_OF_NPDU_PER_CYCLE = "This parameter limits the number of N-Pdus the sender is allowed to transmit within a FlexRay cycle."
    NOTE_MAX_RETRIES = "This parameter defines the maximum number of retries (if retry is configured for the particular channel)."
    NOTE_SEPARATION_CYCLE_EXPONENT = 'Exponent to calculate the minimum number of "Separation Cycles" the sender has to wait for the next transmission of an FrTp N-Pdu.'
    NOTE_TIME_BR = "Time (in seconds) until transmission of the next Flow Control N-PDU."
    NOTE_TIME_BUFFER = (
        "This parameter defines the time of waiting for the next try to get a Tx or Rx buffer. "
        "This parameter is equivalent to the temporal distance between two FC.WT N-Pdus in case the buffer request returns busy."
    )
    NOTE_TIME_CS = "Time (in seconds) until transmission of the next ConsecutiveFrame NPdu / LastFrame NPdu."
    NOTE_TIMEOUT_AR = (
        "This parameter states the timeout between the PDU transmit request of the Transport Layer to the FlexRay Interface "
        "and the corresponding confirmation of the Flex Ray Interface on the receiver side (for FC or AF). Specified in seconds."
    )
    NOTE_TIMEOUT_AS = (
        "This attribute states the timeout between the PDU transmit request for the first PDU of the group used in the current connection "
        "of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the Flex Ray Interface "
        "(when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF or FC "
        "(in case of Transmit Cancellation)). Specified in seconds."
    )
    NOTE_TIMEOUT_BS = "This parameter defines the timeout in seconds for waiting for an FC or AF on the sender side in a 1:1 connection."
    NOTE_TIMEOUT_CR = (
        "This parameter defines the timeout value in seconds for waiting for a CF or FF-x (in case of retry) after receiving the last CF "
        "or after sending an FC or AF on the receiver side. Specified in seconds."
    )

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.240, p.593 — class Note verbatim from the markdown
        assert cleandoc(FlexrayTpConnectionControl.__doc__) == "Configuration parameters to control a FlexRay TP connection."

    def test_init_has_no_docstring(self):
        assert FlexrayTpConnectionControl.__init__.__doc__ is None

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        assert isinstance(control, Identifiable)

    def test_initialization(self):
        # spec displayed order: ackType, maxFcWait, maxNumberOfNpduPerCycle, maxRetries,
        # separationCycleExponent, timeBr, timeBuffer, timeCs, timeoutAr, timeoutAs, timeoutBs, timeoutCr
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        assert control.getAckType() is None
        assert control.getMaxFcWait() is None
        assert control.getMaxNumberOfNpduPerCycle() is None
        assert control.getMaxRetries() is None
        assert control.getSeparationCycleExponent() is None
        assert control.getTimeBr() is None
        assert control.getTimeBuffer() is None
        assert control.getTimeCs() is None
        assert control.getTimeoutAr() is None
        assert control.getTimeoutAs() is None
        assert control.getTimeoutBs() is None
        assert control.getTimeoutCr() is None

    def test_get_set_ack_type(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = TpAckType().setValue(TpAckType.ENUM_ACK_WITH_RT)
        assert control.setAckType(value) is control
        assert control.getAckType() is value
        control.setAckType(None)
        assert control.getAckType() is value

    def test_get_set_max_fc_wait(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _integer(5)
        assert control.setMaxFcWait(value) is control
        assert control.getMaxFcWait() is value
        control.setMaxFcWait(None)
        assert control.getMaxFcWait() is value

    def test_get_set_max_number_of_npdu_per_cycle(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _integer(2)
        assert control.setMaxNumberOfNpduPerCycle(value) is control
        assert control.getMaxNumberOfNpduPerCycle() is value
        control.setMaxNumberOfNpduPerCycle(None)
        assert control.getMaxNumberOfNpduPerCycle() is value

    def test_get_set_max_retries(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _integer(3)
        assert control.setMaxRetries(value) is control
        assert control.getMaxRetries() is value
        control.setMaxRetries(None)
        assert control.getMaxRetries() is value

    def test_get_set_separation_cycle_exponent(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _integer(1)
        assert control.setSeparationCycleExponent(value) is control
        assert control.getSeparationCycleExponent() is value
        control.setSeparationCycleExponent(None)
        assert control.getSeparationCycleExponent() is value

    def test_get_set_time_br(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _time(0.01)
        assert control.setTimeBr(value) is control
        assert control.getTimeBr() is value
        control.setTimeBr(None)
        assert control.getTimeBr() is value

    def test_get_set_time_buffer(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _time(0.02)
        assert control.setTimeBuffer(value) is control
        assert control.getTimeBuffer() is value
        control.setTimeBuffer(None)
        assert control.getTimeBuffer() is value

    def test_get_set_time_cs(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _time(0.03)
        assert control.setTimeCs(value) is control
        assert control.getTimeCs() is value
        control.setTimeCs(None)
        assert control.getTimeCs() is value

    def test_get_set_timeout_ar(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _time(0.04)
        assert control.setTimeoutAr(value) is control
        assert control.getTimeoutAr() is value
        control.setTimeoutAr(None)
        assert control.getTimeoutAr() is value

    def test_get_set_timeout_as(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _time(0.05)
        assert control.setTimeoutAs(value) is control
        assert control.getTimeoutAs() is value
        control.setTimeoutAs(None)
        assert control.getTimeoutAs() is value

    def test_get_set_timeout_bs(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _time(0.06)
        assert control.setTimeoutBs(value) is control
        assert control.getTimeoutBs() is value
        control.setTimeoutBs(None)
        assert control.getTimeoutBs() is value

    def test_get_set_timeout_cr(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        value = _time(0.07)
        assert control.setTimeoutCr(value) is control
        assert control.getTimeoutCr() is value
        control.setTimeoutCr(None)
        assert control.getTimeoutCr() is value

    def test_type_hints_pins(self):
        for getter, setter in [
            ("getMaxFcWait", "setMaxFcWait"),
            ("getMaxNumberOfNpduPerCycle", "setMaxNumberOfNpduPerCycle"),
            ("getMaxRetries", "setMaxRetries"),
            ("getSeparationCycleExponent", "setSeparationCycleExponent"),
        ]:
            assert typing.get_type_hints(getattr(FlexrayTpConnectionControl, getter)).get("return") == Optional[Integer]
            assert typing.get_type_hints(getattr(FlexrayTpConnectionControl, setter)).get("value") == Optional[Integer]
            assert typing.get_type_hints(getattr(FlexrayTpConnectionControl, setter)).get("return") is FlexrayTpConnectionControl
        for getter, setter in [
            ("getTimeBr", "setTimeBr"),
            ("getTimeBuffer", "setTimeBuffer"),
            ("getTimeCs", "setTimeCs"),
            ("getTimeoutAr", "setTimeoutAr"),
            ("getTimeoutAs", "setTimeoutAs"),
            ("getTimeoutBs", "setTimeoutBs"),
            ("getTimeoutCr", "setTimeoutCr"),
        ]:
            assert typing.get_type_hints(getattr(FlexrayTpConnectionControl, getter)).get("return") == Optional[TimeValue]
            assert typing.get_type_hints(getattr(FlexrayTpConnectionControl, setter)).get("value") == Optional[TimeValue]
            assert typing.get_type_hints(getattr(FlexrayTpConnectionControl, setter)).get("return") is FlexrayTpConnectionControl
        assert typing.get_type_hints(FlexrayTpConnectionControl.getAckType).get("return") == Optional[TpAckType]
        assert typing.get_type_hints(FlexrayTpConnectionControl.setAckType).get("value") == Optional[TpAckType]
        assert typing.get_type_hints(FlexrayTpConnectionControl.setAckType).get("return") is FlexrayTpConnectionControl

    def test_docstrings_are_spec_note_verbatim(self):
        for getter, note in [
            ("getAckType", self.NOTE_ACK_TYPE),
            ("getMaxFcWait", self.NOTE_MAX_FC_WAIT),
            ("getMaxNumberOfNpduPerCycle", self.NOTE_MAX_NUMBER_OF_NPDU_PER_CYCLE),
            ("getMaxRetries", self.NOTE_MAX_RETRIES),
            ("getSeparationCycleExponent", self.NOTE_SEPARATION_CYCLE_EXPONENT),
            ("getTimeBr", self.NOTE_TIME_BR),
            ("getTimeBuffer", self.NOTE_TIME_BUFFER),
            ("getTimeCs", self.NOTE_TIME_CS),
            ("getTimeoutAr", self.NOTE_TIMEOUT_AR),
            ("getTimeoutAs", self.NOTE_TIMEOUT_AS),
            ("getTimeoutBs", self.NOTE_TIMEOUT_BS),
            ("getTimeoutCr", self.NOTE_TIMEOUT_CR),
        ]:
            assert cleandoc(getattr(FlexrayTpConnectionControl, getter).__doc__) == note
            setter = getter.replace("get", "set", 1)
            assert cleandoc(getattr(FlexrayTpConnectionControl, setter).__doc__).split("\n")[0] == note


class TestTpAckType:
    # XSD-only class (AUTOSAR_00052.xsd line 144716) — no own table in the R23-11 corpus

    def test_instantiability(self):
        enum = TpAckType()
        assert enum is not None

    def test_literal_values_follow_xsd_facets(self):
        assert TpAckType.ENUM_ACK_WITH_RT == "ACK-WITH-RT"
        assert TpAckType.ENUM_NO_ACK == "NO-ACK"

    def test_set_value_round_trip(self):
        enum = TpAckType()
        enum.setValue(TpAckType.ENUM_NO_ACK)
        assert enum.getValue() == "NO-ACK"
