import inspect

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    MultilanguageReferrable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import (
    DltDefaultTraceStateEnum,
    DltLogChannel,
    LogTraceDefaultLogLevelEnum,
)


class TestDltDefaultTraceStateEnum:
    """Tests for DltDefaultTraceStateEnum (R23-11 SystemTemplate, Table 6.337, p.723)."""

    def test_instantiation(self):
        enum = DltDefaultTraceStateEnum()
        assert isinstance(enum, AREnum)
        assert enum.getValue() == ""

    def test_members(self):
        enum = DltDefaultTraceStateEnum()
        values = enum.getEnumValues()
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED == "DefaultTraceStateDisabled"
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED == "DefaultTraceStateEnabled"
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED in values
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED in values
        assert len(values) == 2

    def test_enum_values_displayed_order(self):
        enum = DltDefaultTraceStateEnum()
        assert enum.getEnumValues() == (
            DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED,
            DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED,
        )

    def test_class_docstring_note(self):
        assert inspect.cleandoc(DltDefaultTraceStateEnum.__doc__) == "This enumeration defines the supported values for the Dlt default trace state."

    def test_set_value_round_trip(self):
        enum = DltDefaultTraceStateEnum()
        assert enum == enum.setValue(DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED)
        assert enum.getValue() == "DefaultTraceStateEnabled"


class TestLogTraceDefaultLogLevelEnum:
    """Tests for LogTraceDefaultLogLevelEnum (R23-11 SystemTemplate, Table 6.338, p.724)."""

    def test_instantiation(self):
        enum = LogTraceDefaultLogLevelEnum()
        assert isinstance(enum, AREnum)
        assert enum.getValue() == ""

    def test_members(self):
        enum = LogTraceDefaultLogLevelEnum()
        values = enum.getEnumValues()
        assert LogTraceDefaultLogLevelEnum.DEBUG == "debug"
        assert LogTraceDefaultLogLevelEnum.ERROR == "error"
        assert LogTraceDefaultLogLevelEnum.FATAL == "fatal"
        assert LogTraceDefaultLogLevelEnum.INFO == "info"
        assert LogTraceDefaultLogLevelEnum.OFF == "off"
        assert LogTraceDefaultLogLevelEnum.VERBOSE == "verbose"
        assert LogTraceDefaultLogLevelEnum.WARN == "warn"
        for member in (
            LogTraceDefaultLogLevelEnum.DEBUG,
            LogTraceDefaultLogLevelEnum.ERROR,
            LogTraceDefaultLogLevelEnum.FATAL,
            LogTraceDefaultLogLevelEnum.INFO,
            LogTraceDefaultLogLevelEnum.OFF,
            LogTraceDefaultLogLevelEnum.VERBOSE,
            LogTraceDefaultLogLevelEnum.WARN,
        ):
            assert member in values
        assert len(values) == 7

    def test_enum_values_displayed_order(self):
        enum = LogTraceDefaultLogLevelEnum()
        assert enum.getEnumValues() == (
            LogTraceDefaultLogLevelEnum.DEBUG,
            LogTraceDefaultLogLevelEnum.ERROR,
            LogTraceDefaultLogLevelEnum.FATAL,
            LogTraceDefaultLogLevelEnum.INFO,
            LogTraceDefaultLogLevelEnum.OFF,
            LogTraceDefaultLogLevelEnum.VERBOSE,
            LogTraceDefaultLogLevelEnum.WARN,
        )

    def test_class_docstring_note(self):
        assert inspect.cleandoc(LogTraceDefaultLogLevelEnum.__doc__) == "This enum defines available log&trace log levels that may be used to define the severity level of a log message."

    def test_set_value_round_trip(self):
        enum = LogTraceDefaultLogLevelEnum()
        assert enum == enum.setValue(LogTraceDefaultLogLevelEnum.VERBOSE)
        assert enum.getValue() == "verbose"


class TestDltLogChannel:
    """Tests for DltLogChannel (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table 6.336, p.723)."""

    MEMBERS = [
        "applicationContextRefs",
        "defaultTraceState",
        "dltMessageRefs",
        "logChannelId",
        "logTraceDefaultLogThreshold",
        "nonVerboseMode",
        "rxPduTriggeringRef",
        "segmentationSupported",
        "txPduTriggeringRef",
    ]

    def _create_channel(self, short_name: str = "dlt_log_channel") -> DltLogChannel:
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        return DltLogChannel(ar_root, short_name)

    def test_inheritance(self):
        assert issubclass(DltLogChannel, ARObject)
        assert issubclass(DltLogChannel, Referrable)
        assert issubclass(DltLogChannel, MultilanguageReferrable)
        assert issubclass(DltLogChannel, Identifiable)

    def test_class_docstring_note(self):
        expected = (
            "This element contains the settings for the log/trace message output for a tuple of ApplicationId and ContextId (verbose mode) or a SessionId (non-verbose mode).\n"
            "\n"
            "[constr_5097] DltLogChannel.txPduTriggering and DltLogChannel.rxPduTriggering shall point to GeneralPurposeIPdus of category DLT: DltLogChannel shall only reference PduTriggerings that are pointing to GeneralPurposeIPdus of category DLT in the roles txPduTriggering and rxPduTriggering.\n"
            "\n"
            "[constr_5306] Restriction of DltLogChannel.logChannelId attribute value: The DltLogChannel.logChannelId attribute value shall be composed of maximum four ASCII characters.\n"
            "\n"
            "[constr_5307] Existence of DltLogChannel.logChannelId: For each DltLogChannel, the attribute logChannelId shall be defined at the time when the System Description is complete.\n"
            "\n"
            "[constr_5308] Existence of DltLogChannel.nonVerboseMode: For each DltLogChannel, the attribute nonVerboseMode shall be defined at the time when the System Description is complete.\n"
            "\n"
            "[constr_5311] Existence of DltLogChannel.logTraceDefaultLogThreshold: For each DltLogChannel, the attribute logTraceDefaultLogThreshold shall be defined at the time when the System Description is complete.\n"
            "\n"
            "[constr_5312] Existence of DltLogChannel.defaultTraceState: For each DltLogChannel, the attribute defaultTraceState shall be defined at the time when the System Description is complete.\n"
            "\n"
            "[constr_5313] Existence of DltLogChannel.txPduTriggering: For each DltLogChannel, the reference to PduTriggering in the role txPduTriggering shall be defined at the time when the System Description is complete.\n"
            "\n"
            "[constr_5314] DltLogChannel txPduTriggering and rxPduTriggering shall be on the same network: The PduTriggerings that are referenced by a DltLogChannel in the role txPduTriggering and rxPduTriggering shall be aggregated by the same PhysicalChannel."
        )
        assert inspect.cleandoc(DltLogChannel.__doc__) == expected

    def test_initialization_defaults(self):
        channel = self._create_channel()
        assert isinstance(channel, ARObject)
        assert isinstance(channel, Referrable)
        assert isinstance(channel, MultilanguageReferrable)
        assert isinstance(channel, Identifiable)
        assert channel.short_name == "dlt_log_channel"
        assert channel.getApplicationContextRefs() == []
        assert channel.getDefaultTraceState() is None
        assert channel.getDltMessageRefs() == []
        assert channel.getLogChannelId() is None
        assert channel.getLogTraceDefaultLogThreshold() is None
        assert channel.getNonVerboseMode() is None
        assert channel.getRxPduTriggeringRef() is None
        assert channel.getSegmentationSupported() is None
        assert channel.getTxPduTriggeringRef() is None

    def test_member_order(self):
        channel = self._create_channel()
        members = [k for k in vars(channel) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_application_context_ref(self):
        channel = self._create_channel()
        ref1 = RefType()
        ref1.setValue("/LogAndTrace/DltContextCollection/Context1")
        assert channel == channel.addApplicationContextRef(ref1)
        assert channel.getApplicationContextRefs() == [ref1]
        ref2 = RefType()
        ref2.setValue("/LogAndTrace/DltContextCollection/Context2")
        channel.addApplicationContextRef(ref2)
        assert channel.getApplicationContextRefs() == [ref1, ref2]
        assert channel.addApplicationContextRef(None) is channel
        assert channel.getApplicationContextRefs() == [ref1, ref2]

    def test_add_dlt_message_ref(self):
        channel = self._create_channel()
        ref1 = RefType()
        ref1.setValue("/LogAndTrace/DltMessageCollection/Message1")
        assert channel == channel.addDltMessageRef(ref1)
        assert channel.getDltMessageRefs() == [ref1]
        ref2 = RefType()
        ref2.setValue("/LogAndTrace/DltMessageCollection/Message2")
        channel.addDltMessageRef(ref2)
        assert channel.getDltMessageRefs() == [ref1, ref2]
        assert channel.addDltMessageRef(None) is channel
        assert channel.getDltMessageRefs() == [ref1, ref2]

    def test_get_set_default_trace_state(self):
        channel = self._create_channel()
        value = DltDefaultTraceStateEnum()
        value.setValue(DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED)
        assert channel == channel.setDefaultTraceState(value)
        assert channel.getDefaultTraceState() is value
        assert channel.getDefaultTraceState().getValue() == "DefaultTraceStateEnabled"
        assert channel.setDefaultTraceState(None) is channel
        assert channel.getDefaultTraceState() is value

    def test_get_set_log_channel_id(self):
        channel = self._create_channel()
        value = String()
        value.setValue("LOG1")
        assert channel == channel.setLogChannelId(value)
        assert channel.getLogChannelId() is value
        assert channel.getLogChannelId().getValue() == "LOG1"
        assert channel.setLogChannelId(None) is channel
        assert channel.getLogChannelId() is value

    def test_get_set_log_trace_default_log_threshold(self):
        channel = self._create_channel()
        value = LogTraceDefaultLogLevelEnum()
        value.setValue(LogTraceDefaultLogLevelEnum.WARN)
        assert channel == channel.setLogTraceDefaultLogThreshold(value)
        assert channel.getLogTraceDefaultLogThreshold() is value
        assert channel.getLogTraceDefaultLogThreshold().getValue() == "warn"
        assert channel.setLogTraceDefaultLogThreshold(None) is channel
        assert channel.getLogTraceDefaultLogThreshold() is value

    def test_get_set_non_verbose_mode(self):
        channel = self._create_channel()
        value = Boolean()
        value.setValue("true")
        assert channel == channel.setNonVerboseMode(value)
        assert channel.getNonVerboseMode() is value
        assert channel.getNonVerboseMode().getValue() is True
        assert channel.setNonVerboseMode(None) is channel
        assert channel.getNonVerboseMode() is value

    def test_get_set_rx_pdu_triggering_ref(self):
        channel = self._create_channel()
        value = RefType()
        value.setValue("/Topology/Cluster/PhysicalChannel/PduTriggering1")
        assert channel == channel.setRxPduTriggeringRef(value)
        assert channel.getRxPduTriggeringRef() is value
        assert channel.getRxPduTriggeringRef().getValue() == "/Topology/Cluster/PhysicalChannel/PduTriggering1"
        assert channel.setRxPduTriggeringRef(None) is channel
        assert channel.getRxPduTriggeringRef() is value

    def test_get_set_segmentation_supported(self):
        channel = self._create_channel()
        value = Boolean()
        value.setValue("false")
        assert channel == channel.setSegmentationSupported(value)
        assert channel.getSegmentationSupported() is value
        assert channel.getSegmentationSupported().getValue() is False
        assert channel.setSegmentationSupported(None) is channel
        assert channel.getSegmentationSupported() is value

    def test_get_set_tx_pdu_triggering_ref(self):
        channel = self._create_channel()
        value = RefType()
        value.setValue("/Topology/Cluster/PhysicalChannel/PduTriggering2")
        assert channel == channel.setTxPduTriggeringRef(value)
        assert channel.getTxPduTriggeringRef() is value
        assert channel.getTxPduTriggeringRef().getValue() == "/Topology/Cluster/PhysicalChannel/PduTriggering2"
        assert channel.setTxPduTriggeringRef(None) is channel
        assert channel.getTxPduTriggeringRef() is value
