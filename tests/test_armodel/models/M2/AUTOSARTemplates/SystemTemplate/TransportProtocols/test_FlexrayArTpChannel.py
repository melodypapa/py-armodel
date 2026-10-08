import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    FrArTpAckType,
    Integer,
    MaximumMessageLengthType,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpChannel, FlexrayArTpConnection


def _boolean(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _channel() -> FlexrayArTpChannel:
    return FlexrayArTpChannel()


class Test_FlexrayArTpChannel:
    # Table 6.246, p.602 — attribute Notes verbatim from the markdown
    NOTE_ACK_TYPE = "Type of Acknowledgement."
    NOTE_CANCELLATION = "With this switch Tx and Rx Cancellation can be turned on or off."
    NOTE_EXTENDED_ADDRESSING = "Adressing Type of this connection: true: Two Bytes false: One Byte"
    NOTE_MAX_AR = "This attribute defines the maximum number of trying to send a frame when a TIMEOUT AR occurs (depending on whether retry is configured)."
    NOTE_MAX_AS = "This attribute defines the maximum number of trying to send a frame when a TIMEOUT AS occurs (depending on whether retry is configured)."
    NOTE_MAX_BS = "This attribute defines the number of consecutive CFs between two FCs (block size). Valid values are 1 .. 16 when retry is activated, and 0 .. 255 otherwise."
    NOTE_MAX_FC_WAIT = "This attribute defines the maximal number of wait frames to be sent for a pending connection. Range is 0..255."
    NOTE_MAXIMUM_MESSAGE_LENGTH = "This specifies the maximum message length for the particular channel."
    NOTE_MAX_RETRIES = "This attribute defines the maximum number of retries (if retry is configured for the particular channel)."
    NOTE_MINIMUM_MULTICAST_SEPERATION_TIME = (
        "This attribute defines the minimum amount of time between two succeeding CFs of a 1:n segmented transmission in seconds. "
        "Valid values are 0, 100µs, 200µs ... 900µs, 1ms, 2ms .. 127ms. "
        "The value can be changed at runtime using the FrArTp_ChangeParameter interface. "
        "minimumMulticastSeparationTime shall be an integer multiple of the cycle length multiplied with the multiplexing factor, "
        "i.e. minimumMulticastSeparationTime = n * cycle * m, where n is an integer >= 0, cycle is Flexray Cluster.cycle, "
        "and m is the cycle multiplexor of those cycles where PDUs of the PDU pool are scheduled. "
        "Please note: Due to the scheduling strategies of FrTp, minimumMulticastSeparationTime can only be kept to a degree defined "
        "by the maximum temporal distance of the PDUs of a PDU pool within one FlexRay cycle. Range: 0 .. 0.127"
    )
    NOTE_MINIMUM_SEPARATION_TIME = (
        "This attribute defines the minimum amount of time between two succeeding CFs of a 1:1 segmented transmission in seconds. "
        "Valid values are 0, 100µs, 200µs .. 900µs, 1ms, 2ms .. 127ms. "
        "The value can be changed at runtime using the FrArTp_ChangeParameter interface. "
        "The minimumSeparationTime shall be an integer multiple of the cycle length multiplied with the multiplexing factor, "
        "i.e. minimumSeparationTime = n * cycle * m, where n is an integer >=0, cycle is FlexrayCluster.cycle, "
        "and m is the cycle multiplexor of those cycles where PDUs of the PDU pool are scheduled. "
        "Please note: Due to the scheduling strategies of FrTp, minimumSeparationTime can only be kept to a degree defined "
        "by the maximum temporal distance of the PDUs of a PDU pool within one FlexRay cycle."
    )
    NOTE_MULTICAST_SEGMENTATION = "This attribute defines whether segmentation within a 1:n connection is allowed or not."
    NOTE_N_PDU_REFS = (
        "A FlexRayTpChannel references a set of NPdus. These NPdus are logically assembled into a pool of Rx NPdus and another pool of Tx NPdus. "
        "It shall be ensured that a second channel either references all NPdus of such a pool, or none."
    )
    NOTE_TIME_BR = "This attribute defines the time in seconds between receiving the last CF of a block or an FF-x (or SF-x) and sending out an FC or AF."
    NOTE_TIME_CS = (
        "This attribute defines the time in seconds between the sending of two consecutive frames or between a consecutive frame and a flow control "
        "(for Transmit Cancellation) or between reception of an flow control or Acknowledgement Frame and sending of the next consecutive frame "
        "or a flow control (for Transmit Cancellation)."
    )
    NOTE_TIMEOUT_AR = (
        "This attribute states the timeout in seconds between the PDU transmit request of the Transport Layer to the Flex Ray Interface "
        "and the corresponding confirmation of the FlexRay Interface on the receiver side (for FC or AF)."
    )
    NOTE_TIMEOUT_AS = (
        "This attribute states the timeout in seconds between the PDU transmit request for the first PDU of the group used in the current connection "
        "of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the FlexRay Interface "
        "(when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF)."
    )
    NOTE_TIMEOUT_BS = "This attribute defines the timeout in seconds for waiting for an FC or AF on the sender side in a 1:1 connection."
    NOTE_TIMEOUT_CR = (
        "This attribute defines the timeout value in seconds for waiting for a CF or FF-x (in case of retry) after receiving the last CF " "or after sending an FC or AF on the receiver side."
    )
    NOTE_TP_CONNECTION = "Group of connections that can be used in this channel."

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.246, p.602 — class Note verbatim from the markdown + table constraints appended
        note = (
            "A channel is a group of connections sharing several properties. The FlexRay AutosarTransport Layer supports several channels. "
            "These channels can work concurrently, thus each of them requires its own state machine and management data structures and its own PDU-IDs."
        )
        constrs = [
            "[constr_9238] Existence of FlexrayArTpChannel.ackType: For each FlexrayArTpChannel, the attribute ackType shall exist at the time when the System Description is complete.",
            "[constr_9239] Existence of FlexrayArTpChannel.extendedAddressing: For each FlexrayArTpChannel, the attribute extendedAddressing shall exist at the time when the System Description is complete.",
            "[constr_9240] Existence of FlexrayArTpChannel.maximumMessageLength: For each FlexrayArTpChannel, the attribute maximumMessageLength shall exist at the time when the System Description is complete.",
            "[constr_9241] Existence of FlexrayArTpChannel.minimumSeparationTime: For each FlexrayArTpChannel, the attribute minimumSeparationTime shall exist at the time when the System Description is complete.",
            "[constr_9242] Existence of FlexrayArTpChannel.multicastSegmentation: For each FlexrayArTpChannel, the attribute multicastSegmentation shall exist at the time when the System Description is complete.",
            "[constr_9243] Existence of FlexrayArTpChannel.tpConnection: For each FlexrayArTpChannel, the aggregation of FlexrayArTpConnection in the role tpConnection shall exist at least once at the time when the System Description is complete.",
        ]
        expected = note + "\n\n" + "\n\n".join(constrs)
        assert cleandoc(FlexrayArTpChannel.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert FlexrayArTpChannel.__init__.__doc__ is None

    def test_heritage(self):
        channel = _channel()
        assert isinstance(channel, ARObject)

    def test_initialization(self):
        # spec displayed order: ackType, cancellation, extendedAddressing, maxAr, maxAs, maxBs,
        # maxFcWait, maximumMessageLength, maxRetries, minimumMulticastSeperationTime,
        # minimumSeparationTime, multicastSegmentation, nPdu `*`, timeBr, timeCs, timeoutAr,
        # timeoutAs, timeoutBs, timeoutCr, tpConnection `*`
        channel = _channel()
        assert channel.getAckType() is None
        assert channel.getCancellation() is None
        assert channel.getExtendedAddressing() is None
        assert channel.getMaxAr() is None
        assert channel.getMaxAs() is None
        assert channel.getMaxBs() is None
        assert channel.getMaxFcWait() is None
        assert channel.getMaximumMessageLength() is None
        assert channel.getMaxRetries() is None
        assert channel.getMinimumMulticastSeperationTime() is None
        assert channel.getMinimumSeparationTime() is None
        assert channel.getMulticastSegmentation() is None
        assert channel.getNPduRefs() == []
        assert channel.getTimeBr() is None
        assert channel.getTimeCs() is None
        assert channel.getTimeoutAr() is None
        assert channel.getTimeoutAs() is None
        assert channel.getTimeoutBs() is None
        assert channel.getTimeoutCr() is None
        assert channel.getTpConnections() == []

    def test_get_set_ack_type(self):
        channel = _channel()
        value = FrArTpAckType().setValue("ACK-WITH-RT")
        assert channel.setAckType(value) is channel
        assert channel.getAckType() is value
        channel.setAckType(None)
        assert channel.getAckType() is value

    def test_get_set_cancellation(self):
        channel = _channel()
        value = _boolean(True)
        assert channel.setCancellation(value) is channel
        assert channel.getCancellation() is value
        channel.setCancellation(None)
        assert channel.getCancellation() is value

    def test_get_set_extended_addressing(self):
        channel = _channel()
        value = _boolean(True)
        assert channel.setExtendedAddressing(value) is channel
        assert channel.getExtendedAddressing() is value
        channel.setExtendedAddressing(None)
        assert channel.getExtendedAddressing() is value

    def test_get_set_max_ar(self):
        channel = _channel()
        value = _integer(3)
        assert channel.setMaxAr(value) is channel
        assert channel.getMaxAr() is value
        channel.setMaxAr(None)
        assert channel.getMaxAr() is value

    def test_get_set_max_as(self):
        channel = _channel()
        value = _integer(4)
        assert channel.setMaxAs(value) is channel
        assert channel.getMaxAs() is value
        channel.setMaxAs(None)
        assert channel.getMaxAs() is value

    def test_get_set_max_bs(self):
        channel = _channel()
        value = _integer(8)
        assert channel.setMaxBs(value) is channel
        assert channel.getMaxBs() is value
        channel.setMaxBs(None)
        assert channel.getMaxBs() is value

    def test_get_set_max_fc_wait(self):
        channel = _channel()
        value = _positive_integer(2)
        assert channel.setMaxFcWait(value) is channel
        assert channel.getMaxFcWait() is value
        channel.setMaxFcWait(None)
        assert channel.getMaxFcWait() is value

    def test_get_set_maximum_message_length(self):
        channel = _channel()
        value = MaximumMessageLengthType().setValue("MTU-40")
        assert channel.setMaximumMessageLength(value) is channel
        assert channel.getMaximumMessageLength() is value
        channel.setMaximumMessageLength(None)
        assert channel.getMaximumMessageLength() is value

    def test_get_set_max_retries(self):
        channel = _channel()
        value = _integer(1)
        assert channel.setMaxRetries(value) is channel
        assert channel.getMaxRetries() is value
        channel.setMaxRetries(None)
        assert channel.getMaxRetries() is value

    def test_get_set_minimum_multicast_seperation_time(self):
        channel = _channel()
        value = _time(0.0002)
        assert channel.setMinimumMulticastSeperationTime(value) is channel
        assert channel.getMinimumMulticastSeperationTime() is value
        channel.setMinimumMulticastSeperationTime(None)
        assert channel.getMinimumMulticastSeperationTime() is value

    def test_get_set_minimum_separation_time(self):
        channel = _channel()
        value = _time(0.0001)
        assert channel.setMinimumSeparationTime(value) is channel
        assert channel.getMinimumSeparationTime() is value
        channel.setMinimumSeparationTime(None)
        assert channel.getMinimumSeparationTime() is value

    def test_get_set_multicast_segmentation(self):
        channel = _channel()
        value = _boolean(False)
        assert channel.setMulticastSegmentation(value) is channel
        assert channel.getMulticastSegmentation() is value
        channel.setMulticastSegmentation(None)
        assert channel.getMulticastSegmentation() is value

    def test_add_n_pdu_ref(self):
        channel = _channel()
        ref1 = _ref("/NPdus/N1", "N-PDU")
        ref2 = _ref("/NPdus/N2", "N-PDU")
        assert channel.addNPduRef(ref1) is channel
        channel.addNPduRef(ref2)
        assert channel.getNPduRefs() == [ref1, ref2]
        channel.addNPduRef(None)
        assert channel.getNPduRefs() == [ref1, ref2]

    def test_get_set_time_br(self):
        channel = _channel()
        value = _time(0.01)
        assert channel.setTimeBr(value) is channel
        assert channel.getTimeBr() is value
        channel.setTimeBr(None)
        assert channel.getTimeBr() is value

    def test_get_set_time_cs(self):
        channel = _channel()
        value = _time(0.02)
        assert channel.setTimeCs(value) is channel
        assert channel.getTimeCs() is value
        channel.setTimeCs(None)
        assert channel.getTimeCs() is value

    def test_get_set_timeout_ar(self):
        channel = _channel()
        value = _time(0.03)
        assert channel.setTimeoutAr(value) is channel
        assert channel.getTimeoutAr() is value
        channel.setTimeoutAr(None)
        assert channel.getTimeoutAr() is value

    def test_get_set_timeout_as(self):
        channel = _channel()
        value = _time(0.04)
        assert channel.setTimeoutAs(value) is channel
        assert channel.getTimeoutAs() is value
        channel.setTimeoutAs(None)
        assert channel.getTimeoutAs() is value

    def test_get_set_timeout_bs(self):
        channel = _channel()
        value = _time(0.05)
        assert channel.setTimeoutBs(value) is channel
        assert channel.getTimeoutBs() is value
        channel.setTimeoutBs(None)
        assert channel.getTimeoutBs() is value

    def test_get_set_timeout_cr(self):
        channel = _channel()
        value = _time(0.06)
        assert channel.setTimeoutCr(value) is channel
        assert channel.getTimeoutCr() is value
        channel.setTimeoutCr(None)
        assert channel.getTimeoutCr() is value

    def test_add_tp_connection(self):
        channel = _channel()
        connection1 = FlexrayArTpConnection()
        connection2 = FlexrayArTpConnection()
        assert channel.addTpConnection(connection1) is channel
        channel.addTpConnection(connection2)
        assert channel.getTpConnections() == [connection1, connection2]
        channel.addTpConnection(None)
        assert channel.getTpConnections() == [connection1, connection2]

    def test_type_hints_pins(self):
        assert typing.get_type_hints(FlexrayArTpChannel.getAckType).get("return") is not None
        assert typing.get_type_hints(FlexrayArTpChannel.setAckType).get("return") is FlexrayArTpChannel
        assert typing.get_type_hints(FlexrayArTpChannel.getCancellation).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(FlexrayArTpChannel.getExtendedAddressing).get("return") == typing.Optional[Boolean]
        for getter in ["getMaxAr", "getMaxAs", "getMaxBs", "getMaxRetries"]:
            assert typing.get_type_hints(getattr(FlexrayArTpChannel, getter)).get("return") == typing.Optional[Integer]
        assert typing.get_type_hints(FlexrayArTpChannel.getMaxFcWait).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(FlexrayArTpChannel.getMaximumMessageLength).get("return") is not None
        for getter in ["getMinimumMulticastSeperationTime", "getMinimumSeparationTime", "getTimeBr", "getTimeCs", "getTimeoutAr", "getTimeoutAs", "getTimeoutBs", "getTimeoutCr"]:
            assert typing.get_type_hints(getattr(FlexrayArTpChannel, getter)).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(FlexrayArTpChannel.getMulticastSegmentation).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(FlexrayArTpChannel.getNPduRefs).get("return") == typing.List[RefType]
        assert typing.get_type_hints(FlexrayArTpChannel.addNPduRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(FlexrayArTpChannel.addNPduRef).get("return") is FlexrayArTpChannel
        assert typing.get_type_hints(FlexrayArTpChannel.getTpConnections).get("return") == typing.List[FlexrayArTpConnection]
        assert typing.get_type_hints(FlexrayArTpChannel.addTpConnection).get("return") is FlexrayArTpChannel

    def test_docstrings_are_spec_note_verbatim(self):
        cases = [
            ("getAckType", self.NOTE_ACK_TYPE),
            ("getCancellation", self.NOTE_CANCELLATION),
            ("getExtendedAddressing", self.NOTE_EXTENDED_ADDRESSING),
            ("getMaxAr", self.NOTE_MAX_AR),
            ("getMaxAs", self.NOTE_MAX_AS),
            ("getMaxBs", self.NOTE_MAX_BS),
            ("getMaxFcWait", self.NOTE_MAX_FC_WAIT),
            ("getMaximumMessageLength", self.NOTE_MAXIMUM_MESSAGE_LENGTH),
            ("getMaxRetries", self.NOTE_MAX_RETRIES),
            ("getMinimumMulticastSeperationTime", self.NOTE_MINIMUM_MULTICAST_SEPERATION_TIME),
            ("getMinimumSeparationTime", self.NOTE_MINIMUM_SEPARATION_TIME),
            ("getMulticastSegmentation", self.NOTE_MULTICAST_SEGMENTATION),
            ("getNPduRefs", self.NOTE_N_PDU_REFS),
            ("getTimeBr", self.NOTE_TIME_BR),
            ("getTimeCs", self.NOTE_TIME_CS),
            ("getTimeoutAr", self.NOTE_TIMEOUT_AR),
            ("getTimeoutAs", self.NOTE_TIMEOUT_AS),
            ("getTimeoutBs", self.NOTE_TIMEOUT_BS),
            ("getTimeoutCr", self.NOTE_TIMEOUT_CR),
            ("getTpConnections", self.NOTE_TP_CONNECTION),
        ]
        for getter, note in cases:
            assert cleandoc(getattr(FlexrayArTpChannel, getter).__doc__) == note, getter

    def test_variation_point_capable(self):
        channel = _channel()
        assert channel.getVariationPoint() is None
