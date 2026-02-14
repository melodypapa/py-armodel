"""
AUTOSAR Package - Dlt

Package: M2::AUTOSARTemplates::SystemTemplate::Dlt
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    DltEcu,
    RefType,
    String,
)


class DltConfig(ARObject):
    """
    This element defines a Dlt configuration for a specific Ecu.

    Package: M2::AUTOSARTemplates::SystemTemplate::Dlt::DltConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 722, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the Ecu representation in the Log And Trace.
        self._dltEcu: Optional["DltEcu"] = None

    @property
    def dlt_ecu(self) -> Optional["DltEcu"]:
        """Get dltEcu (Pythonic accessor)."""
        return self._dltEcu

    @dlt_ecu.setter
    def dlt_ecu(self, value: Optional["DltEcu"]) -> None:
        """
        Set dltEcu with validation.

        Args:
            value: The dltEcu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dltEcu = None
            return

        if not isinstance(value, DltEcu):
            raise TypeError(
                f"dltEcu must be DltEcu or None, got {type(value).__name__}"
            )
        self._dltEcu = value
        self._dltLogChannel: List[DltLogChannel] = []

    @property
    def dlt_log_channel(self) -> List[DltLogChannel]:
        """Get dltLogChannel (Pythonic accessor)."""
        return self._dltLogChannel
        # This attribute defines whether the sessionId is used or.
        self._sessionId: Optional[Boolean] = None

    @property
    def session_id(self) -> Optional[Boolean]:
        """Get sessionId (Pythonic accessor)."""
        return self._sessionId

    @session_id.setter
    def session_id(self, value: Optional[Boolean]) -> None:
        """
        Set sessionId with validation.

        Args:
            value: The sessionId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sessionId = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"sessionId must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._sessionId = value
        # not.
        self._timestamp: Optional[Boolean] = None

    @property
    def timestamp(self) -> Optional[Boolean]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional[Boolean]) -> None:
        """
        Set timestamp with validation.

        Args:
            value: The timestamp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestamp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"timestamp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._timestamp = value

    def with_dlt_log_channel(self, value):
        """
        Set dlt_log_channel and return self for chaining.

        Args:
            value: The dlt_log_channel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_log_channel("value")
        """
        self.dlt_log_channel = value  # Use property setter (gets validation)
        return self

    def with_application(self, value):
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_dlt_message(self, value):
        """
        Set dlt_message and return self for chaining.

        Args:
            value: The dlt_message to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_message("value")
        """
        self.dlt_message = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDltEcu(self) -> DltEcu:
        """
        AUTOSAR-compliant getter for dltEcu.

        Returns:
            The dltEcu value

        Note:
            Delegates to dlt_ecu property (CODING_RULE_V2_00017)
        """
        return self.dlt_ecu  # Delegates to property

    def setDltEcu(self, value: DltEcu) -> DltConfig:
        """
        AUTOSAR-compliant setter for dltEcu with method chaining.

        Args:
            value: The dltEcu to set

        Returns:
            self for method chaining

        Note:
            Delegates to dlt_ecu property setter (gets validation automatically)
        """
        self.dlt_ecu = value  # Delegates to property setter
        return self

    def getDltLogChannel(self) -> List[DltLogChannel]:
        """
        AUTOSAR-compliant getter for dltLogChannel.

        Returns:
            The dltLogChannel value

        Note:
            Delegates to dlt_log_channel property (CODING_RULE_V2_00017)
        """
        return self.dlt_log_channel  # Delegates to property

    def getSessionId(self) -> Boolean:
        """
        AUTOSAR-compliant getter for sessionId.

        Returns:
            The sessionId value

        Note:
            Delegates to session_id property (CODING_RULE_V2_00017)
        """
        return self.session_id  # Delegates to property

    def setSessionId(self, value: Boolean) -> DltConfig:
        """
        AUTOSAR-compliant setter for sessionId with method chaining.

        Args:
            value: The sessionId to set

        Returns:
            self for method chaining

        Note:
            Delegates to session_id property setter (gets validation automatically)
        """
        self.session_id = value  # Delegates to property setter
        return self

    def getTimestamp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for timestamp.

        Returns:
            The timestamp value

        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: Boolean) -> DltConfig:
        """
        AUTOSAR-compliant setter for timestamp with method chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dlt_ecu(self, value: Optional["DltEcu"]) -> DltConfig:
        """
        Set dltEcu and return self for chaining.

        Args:
            value: The dltEcu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_ecu("value")
        """
        self.dlt_ecu = value  # Use property setter (gets validation)
        return self

    def with_session_id(self, value: Optional[Boolean]) -> DltConfig:
        """
        Set sessionId and return self for chaining.

        Args:
            value: The sessionId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_session_id("value")
        """
        self.session_id = value  # Use property setter (gets validation)
        return self

    def with_timestamp(self, value: Optional[Boolean]) -> DltConfig:
        """
        Set timestamp and return self for chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value  # Use property setter (gets validation)
        return self



class DltLogChannel(Identifiable):
    """
    This element contains the settings for the log/trace message output for a
    tuple of ApplicationId and ContextId (verbose mode) or a SessionId
    (non-verbose mode).

    Package: M2::AUTOSARTemplates::SystemTemplate::Dlt::DltLogChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 722, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the Swc that produces the log or trace Please note that this
        # reference shall not be set that the Bsw module produces the associated log
        # messages.
        self._application: List["DltContext"] = []

    @property
    def application(self) -> List["DltContext"]:
        """Get application (Pythonic accessor)."""
        return self._application
        # This attributes defines the default trace status.
        self._defaultTrace: Optional["DltDefaultTraceState"] = None

    @property
    def default_trace(self) -> Optional["DltDefaultTraceState"]:
        """Get defaultTrace (Pythonic accessor)."""
        return self._defaultTrace

    @default_trace.setter
    def default_trace(self, value: Optional["DltDefaultTraceState"]) -> None:
        """
        Set defaultTrace with validation.

        Args:
            value: The defaultTrace to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultTrace = None
            return

        if not isinstance(value, DltDefaultTraceState):
            raise TypeError(
                f"defaultTrace must be DltDefaultTraceState or None, got {type(value).__name__}"
            )
        self._defaultTrace = value
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dltMessage: List["DltMessage"] = []

    @property
    def dlt_message(self) -> List["DltMessage"]:
        """Get dltMessage (Pythonic accessor)."""
        return self._dltMessage
        # This attribute identifies the Channel for usage within the Trace protocol.
        self._logChannelId: Optional[String] = None

    @property
    def log_channel_id(self) -> Optional[String]:
        """Get logChannelId (Pythonic accessor)."""
        return self._logChannelId

    @log_channel_id.setter
    def log_channel_id(self, value: Optional[String]) -> None:
        """
        Set logChannelId with validation.

        Args:
            value: The logChannelId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._logChannelId = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"logChannelId must be String or str or None, got {type(value).__name__}"
            )
        self._logChannelId = value
        self._logTraceDefault: Optional["LogTraceDefaultLog"] = None

    @property
    def log_trace_default(self) -> Optional["LogTraceDefaultLog"]:
        """Get logTraceDefault (Pythonic accessor)."""
        return self._logTraceDefault

    @log_trace_default.setter
    def log_trace_default(self, value: Optional["LogTraceDefaultLog"]) -> None:
        """
        Set logTraceDefault with validation.

        Args:
            value: The logTraceDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._logTraceDefault = None
            return

        if not isinstance(value, LogTraceDefaultLog):
            raise TypeError(
                f"logTraceDefault must be LogTraceDefaultLog or None, got {type(value).__name__}"
            )
        self._logTraceDefault = value
        # If disabled only verbose shall be used.
        self._nonVerbose: Optional[Boolean] = None

    @property
    def non_verbose(self) -> Optional[Boolean]:
        """Get nonVerbose (Pythonic accessor)."""
        return self._nonVerbose

    @non_verbose.setter
    def non_verbose(self, value: Optional[Boolean]) -> None:
        """
        Set nonVerbose with validation.

        Args:
            value: The nonVerbose to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nonVerbose = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nonVerbose must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nonVerbose = value
        self._rxPduTriggering: Optional[RefType] = None

    @property
    def rx_pdu_triggering(self) -> Optional[RefType]:
        """Get rxPduTriggering (Pythonic accessor)."""
        return self._rxPduTriggering

    @rx_pdu_triggering.setter
    def rx_pdu_triggering(self, value: Optional[RefType]) -> None:
        """
        Set rxPduTriggering with validation.

        Args:
            value: The rxPduTriggering to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxPduTriggering = None
            return

        self._rxPduTriggering = value
        # length referenced via DltLogChannel.
        # tx.
        self._segmentation: Optional[Boolean] = None

    @property
    def segmentation(self) -> Optional[Boolean]:
        """Get segmentation (Pythonic accessor)."""
        return self._segmentation

    @segmentation.setter
    def segmentation(self, value: Optional[Boolean]) -> None:
        """
        Set segmentation with validation.

        Args:
            value: The segmentation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._segmentation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"segmentation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._segmentation = value
        self._txPduTriggering: Optional[RefType] = None

    @property
    def tx_pdu_triggering(self) -> Optional[RefType]:
        """Get txPduTriggering (Pythonic accessor)."""
        return self._txPduTriggering

    @tx_pdu_triggering.setter
    def tx_pdu_triggering(self, value: Optional[RefType]) -> None:
        """
        Set txPduTriggering with validation.

        Args:
            value: The txPduTriggering to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txPduTriggering = None
            return

        self._txPduTriggering = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> List["DltContext"]:
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def getDefaultTrace(self) -> "DltDefaultTraceState":
        """
        AUTOSAR-compliant getter for defaultTrace.

        Returns:
            The defaultTrace value

        Note:
            Delegates to default_trace property (CODING_RULE_V2_00017)
        """
        return self.default_trace  # Delegates to property

    def setDefaultTrace(self, value: "DltDefaultTraceState") -> DltLogChannel:
        """
        AUTOSAR-compliant setter for defaultTrace with method chaining.

        Args:
            value: The defaultTrace to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_trace property setter (gets validation automatically)
        """
        self.default_trace = value  # Delegates to property setter
        return self

    def getDltMessage(self) -> List["DltMessage"]:
        """
        AUTOSAR-compliant getter for dltMessage.

        Returns:
            The dltMessage value

        Note:
            Delegates to dlt_message property (CODING_RULE_V2_00017)
        """
        return self.dlt_message  # Delegates to property

    def getLogChannelId(self) -> String:
        """
        AUTOSAR-compliant getter for logChannelId.

        Returns:
            The logChannelId value

        Note:
            Delegates to log_channel_id property (CODING_RULE_V2_00017)
        """
        return self.log_channel_id  # Delegates to property

    def setLogChannelId(self, value: String) -> DltLogChannel:
        """
        AUTOSAR-compliant setter for logChannelId with method chaining.

        Args:
            value: The logChannelId to set

        Returns:
            self for method chaining

        Note:
            Delegates to log_channel_id property setter (gets validation automatically)
        """
        self.log_channel_id = value  # Delegates to property setter
        return self

    def getLogTraceDefault(self) -> "LogTraceDefaultLog":
        """
        AUTOSAR-compliant getter for logTraceDefault.

        Returns:
            The logTraceDefault value

        Note:
            Delegates to log_trace_default property (CODING_RULE_V2_00017)
        """
        return self.log_trace_default  # Delegates to property

    def setLogTraceDefault(self, value: "LogTraceDefaultLog") -> DltLogChannel:
        """
        AUTOSAR-compliant setter for logTraceDefault with method chaining.

        Args:
            value: The logTraceDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to log_trace_default property setter (gets validation automatically)
        """
        self.log_trace_default = value  # Delegates to property setter
        return self

    def getNonVerbose(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nonVerbose.

        Returns:
            The nonVerbose value

        Note:
            Delegates to non_verbose property (CODING_RULE_V2_00017)
        """
        return self.non_verbose  # Delegates to property

    def setNonVerbose(self, value: Boolean) -> DltLogChannel:
        """
        AUTOSAR-compliant setter for nonVerbose with method chaining.

        Args:
            value: The nonVerbose to set

        Returns:
            self for method chaining

        Note:
            Delegates to non_verbose property setter (gets validation automatically)
        """
        self.non_verbose = value  # Delegates to property setter
        return self

    def getRxPduTriggering(self) -> RefType:
        """
        AUTOSAR-compliant getter for rxPduTriggering.

        Returns:
            The rxPduTriggering value

        Note:
            Delegates to rx_pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.rx_pdu_triggering  # Delegates to property

    def setRxPduTriggering(self, value: RefType) -> DltLogChannel:
        """
        AUTOSAR-compliant setter for rxPduTriggering with method chaining.

        Args:
            value: The rxPduTriggering to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_pdu_triggering property setter (gets validation automatically)
        """
        self.rx_pdu_triggering = value  # Delegates to property setter
        return self

    def getSegmentation(self) -> Boolean:
        """
        AUTOSAR-compliant getter for segmentation.

        Returns:
            The segmentation value

        Note:
            Delegates to segmentation property (CODING_RULE_V2_00017)
        """
        return self.segmentation  # Delegates to property

    def setSegmentation(self, value: Boolean) -> DltLogChannel:
        """
        AUTOSAR-compliant setter for segmentation with method chaining.

        Args:
            value: The segmentation to set

        Returns:
            self for method chaining

        Note:
            Delegates to segmentation property setter (gets validation automatically)
        """
        self.segmentation = value  # Delegates to property setter
        return self

    def getTxPduTriggering(self) -> RefType:
        """
        AUTOSAR-compliant getter for txPduTriggering.

        Returns:
            The txPduTriggering value

        Note:
            Delegates to tx_pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.tx_pdu_triggering  # Delegates to property

    def setTxPduTriggering(self, value: RefType) -> DltLogChannel:
        """
        AUTOSAR-compliant setter for txPduTriggering with method chaining.

        Args:
            value: The txPduTriggering to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_pdu_triggering property setter (gets validation automatically)
        """
        self.tx_pdu_triggering = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_trace(self, value: Optional["DltDefaultTraceState"]) -> DltLogChannel:
        """
        Set defaultTrace and return self for chaining.

        Args:
            value: The defaultTrace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_trace("value")
        """
        self.default_trace = value  # Use property setter (gets validation)
        return self

    def with_log_channel_id(self, value: Optional[String]) -> DltLogChannel:
        """
        Set logChannelId and return self for chaining.

        Args:
            value: The logChannelId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_log_channel_id("value")
        """
        self.log_channel_id = value  # Use property setter (gets validation)
        return self

    def with_log_trace_default(self, value: Optional["LogTraceDefaultLog"]) -> DltLogChannel:
        """
        Set logTraceDefault and return self for chaining.

        Args:
            value: The logTraceDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_log_trace_default("value")
        """
        self.log_trace_default = value  # Use property setter (gets validation)
        return self

    def with_non_verbose(self, value: Optional[Boolean]) -> DltLogChannel:
        """
        Set nonVerbose and return self for chaining.

        Args:
            value: The nonVerbose to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_non_verbose("value")
        """
        self.non_verbose = value  # Use property setter (gets validation)
        return self

    def with_rx_pdu_triggering(self, value: Optional[RefType]) -> DltLogChannel:
        """
        Set rxPduTriggering and return self for chaining.

        Args:
            value: The rxPduTriggering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_pdu_triggering("value")
        """
        self.rx_pdu_triggering = value  # Use property setter (gets validation)
        return self

    def with_segmentation(self, value: Optional[Boolean]) -> DltLogChannel:
        """
        Set segmentation and return self for chaining.

        Args:
            value: The segmentation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_segmentation("value")
        """
        self.segmentation = value  # Use property setter (gets validation)
        return self

    def with_tx_pdu_triggering(self, value: Optional[RefType]) -> DltLogChannel:
        """
        Set txPduTriggering and return self for chaining.

        Args:
            value: The txPduTriggering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_pdu_triggering("value")
        """
        self.tx_pdu_triggering = value  # Use property setter (gets validation)
        return self


class DltDefaultTraceStateEnum(AREnum):
    """
    DltDefaultTraceStateEnum enumeration

This enumeration defines the supported values for the Dlt default trace state. Aggregated by DltLogChannel.defaultTraceState

Package: M2::AUTOSARTemplates::SystemTemplate::Dlt
    """
    # The default trace state is disabled
    DefaultTraceStateDisabled = "1"

    # The default trace state is enabled
    DefaultTraceStateEnabled = "0"



class LogTraceDefaultLogLevelEnum(AREnum):
    """
    LogTraceDefaultLogLevelEnum enumeration

This enum defines available log&trace log levels that may be used to define the severity level of a log message. Aggregated by DltLogChannel.logTraceDefaultLogThreshold, DltLogSink.defaultLogThreshold

Package: M2::AUTOSARTemplates::SystemTemplate::Dlt
    """
    # Detailed information for programmers
    debug = "4"

    # Error with impact to correct functionality
    error = "1"

    # Fatal error
    fatal = "0"

    # High level information off logging is turned off
    info = "6"

    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # Verbose debug message
    verbose = "5"

    # Warning if correct behavior cannot be ensured
    warn = "2"
