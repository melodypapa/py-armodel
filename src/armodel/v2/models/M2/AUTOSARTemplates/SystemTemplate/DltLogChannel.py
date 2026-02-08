from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DltLogChannel(Identifiable):
    """
    This element contains the settings for the log/trace message output for a
    tuple of ApplicationId and ContextId (verbose mode) or a SessionId
    (non-verbose mode).

    Package: M2::AUTOSARTemplates::SystemTemplate::Dlt

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
        # Reference to DltMessages that can be transported over in the DltPdu.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dltMessage: List["DltMessage"] = []

    @property
    def dlt_message(self) -> List["DltMessage"]:
        """Get dltMessage (Pythonic accessor)."""
        return self._dltMessage
        # This attribute identifies the Channel for usage within the Trace protocol.
        self._logChannelId: Optional["String"] = None

    @property
    def log_channel_id(self) -> Optional["String"]:
        """Get logChannelId (Pythonic accessor)."""
        return self._logChannelId

    @log_channel_id.setter
    def log_channel_id(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"logChannelId must be String or None, got {type(value).__name__}"
            )
        self._logChannelId = value
        # This attribute allows to set a log level Threshold for Log Level filtering.
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
        # This attribute defines whether this channel supports Dlt messages.
        # If disabled only verbose shall be used.
        self._nonVerbose: Optional["Boolean"] = None

    @property
    def non_verbose(self) -> Optional["Boolean"]:
        """Get nonVerbose (Pythonic accessor)."""
        return self._nonVerbose

    @non_verbose.setter
    def non_verbose(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nonVerbose must be Boolean or None, got {type(value).__name__}"
            )
        self._nonVerbose = value
        # Reference to DltPdu that is received by the DltLog.
        self._rxPduTriggering: RefType = None

    @property
    def rx_pdu_triggering(self) -> RefType:
        """Get rxPduTriggering (Pythonic accessor)."""
        return self._rxPduTriggering

    @rx_pdu_triggering.setter
    def rx_pdu_triggering(self, value: RefType) -> None:
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
        # If enabled, segmentation will be used if a DLT message is than Pdu.
        # length referenced via DltLogChannel.
        # tx.
        self._segmentation: Optional["Boolean"] = None

    @property
    def segmentation(self) -> Optional["Boolean"]:
        """Get segmentation (Pythonic accessor)."""
        return self._segmentation

    @segmentation.setter
    def segmentation(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"segmentation must be Boolean or None, got {type(value).__name__}"
            )
        self._segmentation = value
        # Reference to DltPdu that is transmitted by the DltLog.
        self._txPduTriggering: RefType = None

    @property
    def tx_pdu_triggering(self) -> RefType:
        """Get txPduTriggering (Pythonic accessor)."""
        return self._txPduTriggering

    @tx_pdu_triggering.setter
    def tx_pdu_triggering(self, value: RefType) -> None:
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

    def setDefaultTrace(self, value: "DltDefaultTraceState") -> "DltLogChannel":
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

    def getLogChannelId(self) -> "String":
        """
        AUTOSAR-compliant getter for logChannelId.

        Returns:
            The logChannelId value

        Note:
            Delegates to log_channel_id property (CODING_RULE_V2_00017)
        """
        return self.log_channel_id  # Delegates to property

    def setLogChannelId(self, value: "String") -> "DltLogChannel":
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

    def setLogTraceDefault(self, value: "LogTraceDefaultLog") -> "DltLogChannel":
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

    def getNonVerbose(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nonVerbose.

        Returns:
            The nonVerbose value

        Note:
            Delegates to non_verbose property (CODING_RULE_V2_00017)
        """
        return self.non_verbose  # Delegates to property

    def setNonVerbose(self, value: "Boolean") -> "DltLogChannel":
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

    def setRxPduTriggering(self, value: RefType) -> "DltLogChannel":
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

    def getSegmentation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for segmentation.

        Returns:
            The segmentation value

        Note:
            Delegates to segmentation property (CODING_RULE_V2_00017)
        """
        return self.segmentation  # Delegates to property

    def setSegmentation(self, value: "Boolean") -> "DltLogChannel":
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

    def setTxPduTriggering(self, value: RefType) -> "DltLogChannel":
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

    def with_default_trace(self, value: Optional["DltDefaultTraceState"]) -> "DltLogChannel":
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

    def with_log_channel_id(self, value: Optional["String"]) -> "DltLogChannel":
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

    def with_log_trace_default(self, value: Optional["LogTraceDefaultLog"]) -> "DltLogChannel":
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

    def with_non_verbose(self, value: Optional["Boolean"]) -> "DltLogChannel":
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

    def with_rx_pdu_triggering(self, value: Optional[RefType]) -> "DltLogChannel":
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

    def with_segmentation(self, value: Optional["Boolean"]) -> "DltLogChannel":
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

    def with_tx_pdu_triggering(self, value: Optional[RefType]) -> "DltLogChannel":
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
