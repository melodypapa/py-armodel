from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    RefType,
    String,
)


class DltDefaultTraceStateEnum(AREnum):
    """
    This enumeration defines the supported values for the Dlt default trace state.
    """

    # DltDefaultTraceStateEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.337, p.723 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DltLogChannel.defaultTraceState (Steps 5/6 N/A: standalone AREnum)

    # The default trace state is disabled Tags: atp.EnumerationLiteralIndex=1
    DEFAULT_TRACE_STATE_DISABLED = "DefaultTraceStateDisabled"

    # The default trace state is enabled Tags: atp.EnumerationLiteralIndex=0
    DEFAULT_TRACE_STATE_ENABLED = "DefaultTraceStateEnabled"

    def __init__(self):
        super().__init__(
            (
                DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED,
                DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED,
            )
        )


class LogTraceDefaultLogLevelEnum(AREnum):
    """
    This enum defines available log&trace log levels that may be used to define the severity level of a log message.
    """

    # LogTraceDefaultLogLevelEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.338, p.724 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DltLogChannel.logTraceDefaultLogThreshold (Steps 5/6 N/A: standalone AREnum)

    # Detailed information for programmers Tags: atp.EnumerationLiteralIndex=4
    DEBUG = "debug"

    # Error with impact to correct functionality Tags: atp.EnumerationLiteralIndex=1
    ERROR = "error"

    # Fatal error Tags: atp.EnumerationLiteralIndex=0
    FATAL = "fatal"

    # High level information Tags: atp.EnumerationLiteralIndex=3
    INFO = "info"

    # logging is turned off Tags: atp.EnumerationLiteralIndex=6
    OFF = "off"

    # Verbose debug message Tags: atp.EnumerationLiteralIndex=5
    VERBOSE = "verbose"

    # Warning if correct behavior cannot be ensured Tags: atp.EnumerationLiteralIndex=2
    WARN = "warn"

    def __init__(self):
        super().__init__(
            (
                LogTraceDefaultLogLevelEnum.DEBUG,
                LogTraceDefaultLogLevelEnum.ERROR,
                LogTraceDefaultLogLevelEnum.FATAL,
                LogTraceDefaultLogLevelEnum.INFO,
                LogTraceDefaultLogLevelEnum.OFF,
                LogTraceDefaultLogLevelEnum.VERBOSE,
                LogTraceDefaultLogLevelEnum.WARN,
            )
        )


class DltLogChannel(Identifiable):
    """
    This element contains the settings for the log/trace message output for a tuple of ApplicationId and ContextId (verbose mode) or a SessionId (non-verbose mode).

    [constr_5097] DltLogChannel.txPduTriggering and DltLogChannel.rxPduTriggering shall point to GeneralPurposeIPdus of category DLT: DltLogChannel shall only reference PduTriggerings that are pointing to GeneralPurposeIPdus of category DLT in the roles txPduTriggering and rxPduTriggering.

    [constr_5306] Restriction of DltLogChannel.logChannelId attribute value: The DltLogChannel.logChannelId attribute value shall be composed of maximum four ASCII characters.

    [constr_5307] Existence of DltLogChannel.logChannelId: For each DltLogChannel, the attribute logChannelId shall be defined at the time when the System Description is complete.

    [constr_5308] Existence of DltLogChannel.nonVerboseMode: For each DltLogChannel, the attribute nonVerboseMode shall be defined at the time when the System Description is complete.

    [constr_5311] Existence of DltLogChannel.logTraceDefaultLogThreshold: For each DltLogChannel, the attribute logTraceDefaultLogThreshold shall be defined at the time when the System Description is complete.

    [constr_5312] Existence of DltLogChannel.defaultTraceState: For each DltLogChannel, the attribute defaultTraceState shall be defined at the time when the System Description is complete.

    [constr_5313] Existence of DltLogChannel.txPduTriggering: For each DltLogChannel, the reference to PduTriggering in the role txPduTriggering shall be defined at the time when the System Description is complete.

    [constr_5314] DltLogChannel txPduTriggering and rxPduTriggering shall be on the same network: The PduTriggerings that are referenced by a DltLogChannel in the role txPduTriggering and rxPduTriggering shall be aggregated by the same PhysicalChannel.
    """

    # DltLogChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.336, p.723 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addApplicationContextRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getApplicationContextRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDefaultTraceState                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultTraceState                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDltMessageRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDltMessageRefs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getLogChannelId                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLogChannelId                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLogTraceDefaultLogThreshold       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLogTraceDefaultLogThreshold       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNonVerboseMode                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNonVerboseMode                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRxPduTriggeringRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRxPduTriggeringRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSegmentationSupported             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSegmentationSupported             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTxPduTriggeringRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTxPduTriggeringRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the Swc that produces the log or trace message. Please note that this reference shall not be set in case that the Bsw module produces the associated log or trace messages.
        self.applicationContextRefs: List[RefType] = []

        # This attributes defines the default trace status.
        self.defaultTraceState: Optional[DltDefaultTraceStateEnum] = None

        # Reference to DltMessages that can be transported over the DltLogChannel in the DltPdu.
        self.dltMessageRefs: List[RefType] = []

        # This attribute identifies the Channel for usage within the Log And Trace protocol.
        self.logChannelId: Optional[String] = None

        # This attribute allows to set a log level Threshold for Log Level filtering.
        self.logTraceDefaultLogThreshold: Optional[LogTraceDefaultLogLevelEnum] = None

        # This attribute defines whether this channel supports non-Verbose Dlt messages. If disabled only verbose mode messages shall be used.
        self.nonVerboseMode: Optional[Boolean] = None

        # Reference to DltPdu that is received by the DltLogChannel
        self.rxPduTriggeringRef: Optional[RefType] = None

        # If enabled, segmentation will be used if a DLT message is larger than Pdu.length referenced via DltLogChannel.txPduTriggering.
        self.segmentationSupported: Optional[Boolean] = None

        # Reference to DltPdu that is transmitted by the DltLogChannel.
        self.txPduTriggeringRef: Optional[RefType] = None

    def addApplicationContextRef(self, value: Optional[RefType]) -> "DltLogChannel":
        """
        Reference to the Swc that produces the log or trace message. Please note that this reference shall not be set in case that the Bsw module produces the associated log or trace messages.

        A None value is a no-op and does not append a new applicationContextRef.
        """
        if value is not None:
            self.applicationContextRefs.append(value)
        return self

    def getApplicationContextRefs(self) -> List[RefType]:
        """
        Reference to the Swc that produces the log or trace message. Please note that this reference shall not be set in case that the Bsw module produces the associated log or trace messages.
        """
        return self.applicationContextRefs

    def getDefaultTraceState(self) -> Optional[DltDefaultTraceStateEnum]:
        """
        This attributes defines the default trace status.
        """
        return self.defaultTraceState

    def setDefaultTraceState(self, value: Optional[DltDefaultTraceStateEnum]) -> "DltLogChannel":
        """
        This attributes defines the default trace status.

        A None value is a no-op and does not overwrite an existing defaultTraceState.
        """
        if value is not None:
            self.defaultTraceState = value
        return self

    def addDltMessageRef(self, value: Optional[RefType]) -> "DltLogChannel":
        """
        Reference to DltMessages that can be transported over the DltLogChannel in the DltPdu.

        A None value is a no-op and does not append a new dltMessageRef.
        """
        if value is not None:
            self.dltMessageRefs.append(value)
        return self

    def getDltMessageRefs(self) -> List[RefType]:
        """
        Reference to DltMessages that can be transported over the DltLogChannel in the DltPdu.
        """
        return self.dltMessageRefs

    def getLogChannelId(self) -> Optional[String]:
        """
        This attribute identifies the Channel for usage within the Log And Trace protocol.
        """
        return self.logChannelId

    def setLogChannelId(self, value: Optional[String]) -> "DltLogChannel":
        """
        This attribute identifies the Channel for usage within the Log And Trace protocol.

        A None value is a no-op and does not overwrite an existing logChannelId.
        """
        if value is not None:
            self.logChannelId = value
        return self

    def getLogTraceDefaultLogThreshold(self) -> Optional[LogTraceDefaultLogLevelEnum]:
        """
        This attribute allows to set a log level Threshold for Log Level filtering.
        """
        return self.logTraceDefaultLogThreshold

    def setLogTraceDefaultLogThreshold(self, value: Optional[LogTraceDefaultLogLevelEnum]) -> "DltLogChannel":
        """
        This attribute allows to set a log level Threshold for Log Level filtering.

        A None value is a no-op and does not overwrite an existing logTraceDefaultLogThreshold.
        """
        if value is not None:
            self.logTraceDefaultLogThreshold = value
        return self

    def getNonVerboseMode(self) -> Optional[Boolean]:
        """
        This attribute defines whether this channel supports non-Verbose Dlt messages. If disabled only verbose mode messages shall be used.
        """
        return self.nonVerboseMode

    def setNonVerboseMode(self, value: Optional[Boolean]) -> "DltLogChannel":
        """
        This attribute defines whether this channel supports non-Verbose Dlt messages. If disabled only verbose mode messages shall be used.

        A None value is a no-op and does not overwrite an existing nonVerboseMode.
        """
        if value is not None:
            self.nonVerboseMode = value
        return self

    def getRxPduTriggeringRef(self) -> Optional[RefType]:
        """
        Reference to DltPdu that is received by the DltLogChannel
        """
        return self.rxPduTriggeringRef

    def setRxPduTriggeringRef(self, value: Optional[RefType]) -> "DltLogChannel":
        """
        Reference to DltPdu that is received by the DltLogChannel

        A None value is a no-op and does not overwrite an existing rxPduTriggeringRef.
        """
        if value is not None:
            self.rxPduTriggeringRef = value
        return self

    def getSegmentationSupported(self) -> Optional[Boolean]:
        """
        If enabled, segmentation will be used if a DLT message is larger than Pdu.length referenced via DltLogChannel.txPduTriggering.
        """
        return self.segmentationSupported

    def setSegmentationSupported(self, value: Optional[Boolean]) -> "DltLogChannel":
        """
        If enabled, segmentation will be used if a DLT message is larger than Pdu.length referenced via DltLogChannel.txPduTriggering.

        A None value is a no-op and does not overwrite an existing segmentationSupported.
        """
        if value is not None:
            self.segmentationSupported = value
        return self

    def getTxPduTriggeringRef(self) -> Optional[RefType]:
        """
        Reference to DltPdu that is transmitted by the DltLogChannel.
        """
        return self.txPduTriggeringRef

    def setTxPduTriggeringRef(self, value: Optional[RefType]) -> "DltLogChannel":
        """
        Reference to DltPdu that is transmitted by the DltLogChannel.

        A None value is a no-op and does not overwrite an existing txPduTriggeringRef.
        """
        if value is not None:
            self.txPduTriggeringRef = value
        return self


class DltConfig(ARObject):
    """
    This element defines a Dlt configuration for a specific Ecu.

    [constr_5309] Existence of DltConfig.sessionIdSupport: For each DltConfig, the attribute sessionIdSupport shall be defined at the time when the System Description is complete.

    [constr_5310] Existence of DltConfig.timestampSupport: For each DltConfig, the attribute timestampSupport shall be defined at the time when the System Description is complete.
    """

    # DltConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.335, p.722 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDltEcuRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDltEcuRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDltLogChannel    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDltLogChannels      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSessionIdSupport    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSessionIdSupport    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimestampSupport    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimestampSupport    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the Ecu representation in the Log And Trace Extract.
        self.dltEcuRef: Optional[RefType] = None

        # Describes the DltLogChannels that are configured for the log/trace message output
        self.dltLogChannels: List[DltLogChannel] = []

        # This attribute defines whether the sessionId is used or not.
        self.sessionIdSupport: Optional[Boolean] = None

        # This attribute defines whether a timestamp shall be added to the Dlt messages or not.
        self.timestampSupport: Optional[Boolean] = None

    def getDltEcuRef(self) -> Optional[RefType]:
        """
        Reference to the Ecu representation in the Log And Trace Extract.
        """
        return self.dltEcuRef

    def setDltEcuRef(self, value: Optional[RefType]) -> "DltConfig":
        """
        Reference to the Ecu representation in the Log And Trace Extract.

        A None value is a no-op and does not overwrite an existing dltEcuRef.
        """
        if value is not None:
            self.dltEcuRef = value
        return self

    def createDltLogChannel(self, short_name: str) -> DltLogChannel:
        """
        Describes the DltLogChannels that are configured for the log/trace message output
        """
        for channel in self.dltLogChannels:
            if channel.getShortName() == short_name:
                return channel
        channel = DltLogChannel(self, short_name)
        self.dltLogChannels.append(channel)
        return channel

    def getDltLogChannels(self) -> List[DltLogChannel]:
        """
        Describes the DltLogChannels that are configured for the log/trace message output
        """
        return self.dltLogChannels

    def getSessionIdSupport(self) -> Optional[Boolean]:
        """
        This attribute defines whether the sessionId is used or not.
        """
        return self.sessionIdSupport

    def setSessionIdSupport(self, value: Optional[Boolean]) -> "DltConfig":
        """
        This attribute defines whether the sessionId is used or not.

        A None value is a no-op and does not overwrite an existing sessionIdSupport.
        """
        if value is not None:
            self.sessionIdSupport = value
        return self

    def getTimestampSupport(self) -> Optional[Boolean]:
        """
        This attribute defines whether a timestamp shall be added to the Dlt messages or not.
        """
        return self.timestampSupport

    def setTimestampSupport(self, value: Optional[Boolean]) -> "DltConfig":
        """
        This attribute defines whether a timestamp shall be added to the Dlt messages or not.

        A None value is a no-op and does not overwrite an existing timestampSupport.
        """
        if value is not None:
            self.timestampSupport = value
        return self
