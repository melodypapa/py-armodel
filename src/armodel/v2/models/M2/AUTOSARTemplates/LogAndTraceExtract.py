"""
AUTOSAR Package - LogAndTraceExtract

Package: M2::AUTOSARTemplates::LogAndTraceExtract
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DltArgument(Identifiable):
    """
    This element defines an Argument in a DltMessage.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::DltArgument

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 983, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 13, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation is used to describe subElements of a Dlt that defines a
        # Structure.
        self._dltArgument: List[DltArgument] = []

    @property
    def dlt_argument(self) -> List[DltArgument]:
        """Get dltArgument (Pythonic accessor)."""
        return self._dltArgument
        # Describes the DltArgument length in case of Arrays and number of BaseTypes.
        self._length: Optional[PositiveInteger] = None

    @property
    def length(self) -> Optional[PositiveInteger]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional[PositiveInteger]) -> None:
        """
        Set length with validation.

        Args:
            value: The length to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"length must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._length = value
        self._network: Optional[SwDataDefProps] = None

    @property
    def network(self) -> Optional[SwDataDefProps]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional[SwDataDefProps]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"network must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._network = value
        # argument can be omitted from the a DLT message.
        self._optional: Optional[Boolean] = None

    @property
    def optional(self) -> Optional[Boolean]:
        """Get optional (Pythonic accessor)."""
        return self._optional

    @optional.setter
    def optional(self, value: Optional[Boolean]) -> None:
        """
        Set optional with validation.

        Args:
            value: The optional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._optional = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"optional must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._optional = value
        self._predefinedText: Optional[Boolean] = None

    @property
    def predefined_text(self) -> Optional[Boolean]:
        """Get predefinedText (Pythonic accessor)."""
        return self._predefinedText

    @predefined_text.setter
    def predefined_text(self, value: Optional[Boolean]) -> None:
        """
        Set predefinedText with validation.

        Args:
            value: The predefinedText to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._predefinedText = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"predefinedText must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._predefinedText = value
        # runtime) or not.
        self._variableLength: Optional[Boolean] = None

    @property
    def variable_length(self) -> Optional[Boolean]:
        """Get variableLength (Pythonic accessor)."""
        return self._variableLength

    @variable_length.setter
    def variable_length(self, value: Optional[Boolean]) -> None:
        """
        Set variableLength with validation.

        Args:
            value: The variableLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableLength = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"variableLength must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._variableLength = value

    def with_dlt_argument(self, value):
        """
        Set dlt_argument and return self for chaining.

        Args:
            value: The dlt_argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_argument("value")
        """
        self.dlt_argument = value  # Use property setter (gets validation)
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

    def with_dlt_argument(self, value):
        """
        Set dlt_argument and return self for chaining.

        Args:
            value: The dlt_argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_argument("value")
        """
        self.dlt_argument = value  # Use property setter (gets validation)
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

    def getDltArgument(self) -> List[DltArgument]:
        """
        AUTOSAR-compliant getter for dltArgument.

        Returns:
            The dltArgument value

        Note:
            Delegates to dlt_argument property (CODING_RULE_V2_00017)
        """
        return self.dlt_argument  # Delegates to property

    def getLength(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for length.

        Returns:
            The length value

        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: PositiveInteger) -> DltArgument:
        """
        AUTOSAR-compliant setter for length with method chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    def getNetwork(self) -> SwDataDefProps:
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: SwDataDefProps) -> DltArgument:
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    def getOptional(self) -> Boolean:
        """
        AUTOSAR-compliant getter for optional.

        Returns:
            The optional value

        Note:
            Delegates to optional property (CODING_RULE_V2_00017)
        """
        return self.optional  # Delegates to property

    def setOptional(self, value: Boolean) -> DltArgument:
        """
        AUTOSAR-compliant setter for optional with method chaining.

        Args:
            value: The optional to set

        Returns:
            self for method chaining

        Note:
            Delegates to optional property setter (gets validation automatically)
        """
        self.optional = value  # Delegates to property setter
        return self

    def getPredefinedText(self) -> Boolean:
        """
        AUTOSAR-compliant getter for predefinedText.

        Returns:
            The predefinedText value

        Note:
            Delegates to predefined_text property (CODING_RULE_V2_00017)
        """
        return self.predefined_text  # Delegates to property

    def setPredefinedText(self, value: Boolean) -> DltArgument:
        """
        AUTOSAR-compliant setter for predefinedText with method chaining.

        Args:
            value: The predefinedText to set

        Returns:
            self for method chaining

        Note:
            Delegates to predefined_text property setter (gets validation automatically)
        """
        self.predefined_text = value  # Delegates to property setter
        return self

    def getVariableLength(self) -> Boolean:
        """
        AUTOSAR-compliant getter for variableLength.

        Returns:
            The variableLength value

        Note:
            Delegates to variable_length property (CODING_RULE_V2_00017)
        """
        return self.variable_length  # Delegates to property

    def setVariableLength(self, value: Boolean) -> DltArgument:
        """
        AUTOSAR-compliant setter for variableLength with method chaining.

        Args:
            value: The variableLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable_length property setter (gets validation automatically)
        """
        self.variable_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_length(self, value: Optional[PositiveInteger]) -> DltArgument:
        """
        Set length and return self for chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional[SwDataDefProps]) -> DltArgument:
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_optional(self, value: Optional[Boolean]) -> DltArgument:
        """
        Set optional and return self for chaining.

        Args:
            value: The optional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_optional("value")
        """
        self.optional = value  # Use property setter (gets validation)
        return self

    def with_predefined_text(self, value: Optional[Boolean]) -> DltArgument:
        """
        Set predefinedText and return self for chaining.

        Args:
            value: The predefinedText to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_predefined_text("value")
        """
        self.predefined_text = value  # Use property setter (gets validation)
        return self

    def with_variable_length(self, value: Optional[Boolean]) -> DltArgument:
        """
        Set variableLength and return self for chaining.

        Args:
            value: The variableLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_length("value")
        """
        self.variable_length = value  # Use property setter (gets validation)
        return self



class DltApplication(Identifiable):
    """
    This meta-class represents the application from which the log and trace
    message originates.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::DltApplication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2017, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 8, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute can be used to describe the applicationId is used in the log
        # and trace message in more detail.
        self._application: Optional[String] = None

    @property
    def application(self) -> Optional[String]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional[String]) -> None:
        """
        Set application with validation.

        Args:
            value: The application to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"application must be String or str or None, got {type(value).__name__}"
            )
        self._application = value
        self._applicationId: Optional[String] = None

    @property
    def application_id(self) -> Optional[String]:
        """Get applicationId (Pythonic accessor)."""
        return self._applicationId

    @application_id.setter
    def application_id(self, value: Optional[String]) -> None:
        """
        Set applicationId with validation.

        Args:
            value: The applicationId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationId = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"applicationId must be String or str or None, got {type(value).__name__}"
            )
        self._applicationId = value
        # atpVariation.
        self._context: List[DltContext] = []

    @property
    def context(self) -> List[DltContext]:
        """Get context (Pythonic accessor)."""
        return self._context

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> String:
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: String) -> DltApplication:
        """
        AUTOSAR-compliant setter for application with method chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    def getApplicationId(self) -> String:
        """
        AUTOSAR-compliant getter for applicationId.

        Returns:
            The applicationId value

        Note:
            Delegates to application_id property (CODING_RULE_V2_00017)
        """
        return self.application_id  # Delegates to property

    def setApplicationId(self, value: String) -> DltApplication:
        """
        AUTOSAR-compliant setter for applicationId with method chaining.

        Args:
            value: The applicationId to set

        Returns:
            self for method chaining

        Note:
            Delegates to application_id property setter (gets validation automatically)
        """
        self.application_id = value  # Delegates to property setter
        return self

    def getContext(self) -> List[DltContext]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional[String]) -> DltApplication:
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

    def with_application_id(self, value: Optional[String]) -> DltApplication:
        """
        Set applicationId and return self for chaining.

        Args:
            value: The applicationId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application_id("value")
        """
        self.application_id = value  # Use property setter (gets validation)
        return self



class DltContext(ARElement):
    """
    This meta-class represents the Context that groups Log and Trace Messages
    that are generated by an application.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::DltContext

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2017, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 9, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute can be used to describe the contextId that is in the log and
        # trace message in more detail.
        self._context: Optional[String] = None

    @property
    def context(self) -> Optional[String]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional[String]) -> None:
        """
        Set context with validation.

        Args:
            value: The context to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"context must be String or str or None, got {type(value).__name__}"
            )
        self._context = value
                # distinguish functionality.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._contextId: Optional[String] = None

    @property
    def context_id(self) -> Optional[String]:
        """Get contextId (Pythonic accessor)."""
        return self._contextId

    @context_id.setter
    def context_id(self, value: Optional[String]) -> None:
        """
        Set contextId with validation.

        Args:
            value: The contextId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextId = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"contextId must be String or str or None, got {type(value).__name__}"
            )
        self._contextId = value
        self._dltMessage: List[DltMessage] = []

    @property
    def dlt_message(self) -> List[DltMessage]:
        """Get dltMessage (Pythonic accessor)."""
        return self._dltMessage

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> String:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: String) -> DltContext:
        """
        AUTOSAR-compliant setter for context with method chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getContextId(self) -> String:
        """
        AUTOSAR-compliant getter for contextId.

        Returns:
            The contextId value

        Note:
            Delegates to context_id property (CODING_RULE_V2_00017)
        """
        return self.context_id  # Delegates to property

    def setContextId(self, value: String) -> DltContext:
        """
        AUTOSAR-compliant setter for contextId with method chaining.

        Args:
            value: The contextId to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_id property setter (gets validation automatically)
        """
        self.context_id = value  # Delegates to property setter
        return self

    def getDltMessage(self) -> List[DltMessage]:
        """
        AUTOSAR-compliant getter for dltMessage.

        Returns:
            The dltMessage value

        Note:
            Delegates to dlt_message property (CODING_RULE_V2_00017)
        """
        return self.dlt_message  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context(self, value: Optional[String]) -> DltContext:
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context_id(self, value: Optional[String]) -> DltContext:
        """
        Set contextId and return self for chaining.

        Args:
            value: The contextId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_id("value")
        """
        self.context_id = value  # Use property setter (gets validation)
        return self



class DltEcu(ARElement):
    """
    This element represents an Ecu or Machine that produces logging and tracing
    information.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::DltEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2018, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 8, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Application on DltEcu that provides log or trace data.
        # atpVariation.
        self._application: List[DltApplication] = []

    @property
    def application(self) -> List[DltApplication]:
        """Get application (Pythonic accessor)."""
        return self._application
        # This attribute defines the name of the ECU for use within protocol.
        self._ecuId: Optional[String] = None

    @property
    def ecu_id(self) -> Optional[String]:
        """Get ecuId (Pythonic accessor)."""
        return self._ecuId

    @ecu_id.setter
    def ecu_id(self, value: Optional[String]) -> None:
        """
        Set ecuId with validation.

        Args:
            value: The ecuId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuId = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"ecuId must be String or str or None, got {type(value).__name__}"
            )
        self._ecuId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> List[DltApplication]:
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def getEcuId(self) -> String:
        """
        AUTOSAR-compliant getter for ecuId.

        Returns:
            The ecuId value

        Note:
            Delegates to ecu_id property (CODING_RULE_V2_00017)
        """
        return self.ecu_id  # Delegates to property

    def setEcuId(self, value: String) -> DltEcu:
        """
        AUTOSAR-compliant setter for ecuId with method chaining.

        Args:
            value: The ecuId to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_id property setter (gets validation automatically)
        """
        self.ecu_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_id(self, value: Optional[String]) -> DltEcu:
        """
        Set ecuId and return self for chaining.

        Args:
            value: The ecuId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_id("value")
        """
        self.ecu_id = value  # Use property setter (gets validation)
        return self



class DltMessage(Identifiable):
    """
    This element defines a DltMessage.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::DltMessage

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2018, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 12, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Ordered collection of DltArguments in the DltMessage.
        self._dltArgument: List[DltArgument] = []

    @property
    def dlt_argument(self) -> List[DltArgument]:
        """Get dltArgument (Pythonic accessor)."""
        return self._dltArgument
        # This attribute defines the unique Id for the DltMessage.
        self._messageId: Optional[PositiveInteger] = None

    @property
    def message_id(self) -> Optional[PositiveInteger]:
        """Get messageId (Pythonic accessor)."""
        return self._messageId

    @message_id.setter
    def message_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set messageId with validation.

        Args:
            value: The messageId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"messageId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._messageId = value
        # was called.
        self._messageLine: Optional[PositiveInteger] = None

    @property
    def message_line(self) -> Optional[PositiveInteger]:
        """Get messageLine (Pythonic accessor)."""
        return self._messageLine

    @message_line.setter
    def message_line(self, value: Optional[PositiveInteger]) -> None:
        """
        Set messageLine with validation.

        Args:
            value: The messageLine to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageLine = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"messageLine must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._messageLine = value
        self._messageSource: Optional[String] = None

    @property
    def message_source(self) -> Optional[String]:
        """Get messageSource (Pythonic accessor)."""
        return self._messageSource

    @message_source.setter
    def message_source(self, value: Optional[String]) -> None:
        """
        Set messageSource with validation.

        Args:
            value: The messageSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageSource = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"messageSource must be String or str or None, got {type(value).__name__}"
            )
        self._messageSource = value
        self._messageTypeInfo: Optional[String] = None

    @property
    def message_type_info(self) -> Optional[String]:
        """Get messageTypeInfo (Pythonic accessor)."""
        return self._messageTypeInfo

    @message_type_info.setter
    def message_type_info(self, value: Optional[String]) -> None:
        """
        Set messageTypeInfo with validation.

        Args:
            value: The messageTypeInfo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageTypeInfo = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"messageTypeInfo must be String or str or None, got {type(value).__name__}"
            )
        self._messageTypeInfo = value
        # to it.
        self._privacyLevel: Optional[PrivacyLevel] = None

    @property
    def privacy_level(self) -> Optional[PrivacyLevel]:
        """Get privacyLevel (Pythonic accessor)."""
        return self._privacyLevel

    @privacy_level.setter
    def privacy_level(self, value: Optional[PrivacyLevel]) -> None:
        """
        Set privacyLevel with validation.

        Args:
            value: The privacyLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._privacyLevel = None
            return

        if not isinstance(value, PrivacyLevel):
            raise TypeError(
                f"privacyLevel must be PrivacyLevel or None, got {type(value).__name__}"
            )
        self._privacyLevel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDltArgument(self) -> List[DltArgument]:
        """
        AUTOSAR-compliant getter for dltArgument.

        Returns:
            The dltArgument value

        Note:
            Delegates to dlt_argument property (CODING_RULE_V2_00017)
        """
        return self.dlt_argument  # Delegates to property

    def getMessageId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for messageId.

        Returns:
            The messageId value

        Note:
            Delegates to message_id property (CODING_RULE_V2_00017)
        """
        return self.message_id  # Delegates to property

    def setMessageId(self, value: PositiveInteger) -> DltMessage:
        """
        AUTOSAR-compliant setter for messageId with method chaining.

        Args:
            value: The messageId to set

        Returns:
            self for method chaining

        Note:
            Delegates to message_id property setter (gets validation automatically)
        """
        self.message_id = value  # Delegates to property setter
        return self

    def getMessageLine(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for messageLine.

        Returns:
            The messageLine value

        Note:
            Delegates to message_line property (CODING_RULE_V2_00017)
        """
        return self.message_line  # Delegates to property

    def setMessageLine(self, value: PositiveInteger) -> DltMessage:
        """
        AUTOSAR-compliant setter for messageLine with method chaining.

        Args:
            value: The messageLine to set

        Returns:
            self for method chaining

        Note:
            Delegates to message_line property setter (gets validation automatically)
        """
        self.message_line = value  # Delegates to property setter
        return self

    def getMessageSource(self) -> String:
        """
        AUTOSAR-compliant getter for messageSource.

        Returns:
            The messageSource value

        Note:
            Delegates to message_source property (CODING_RULE_V2_00017)
        """
        return self.message_source  # Delegates to property

    def setMessageSource(self, value: String) -> DltMessage:
        """
        AUTOSAR-compliant setter for messageSource with method chaining.

        Args:
            value: The messageSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to message_source property setter (gets validation automatically)
        """
        self.message_source = value  # Delegates to property setter
        return self

    def getMessageTypeInfo(self) -> String:
        """
        AUTOSAR-compliant getter for messageTypeInfo.

        Returns:
            The messageTypeInfo value

        Note:
            Delegates to message_type_info property (CODING_RULE_V2_00017)
        """
        return self.message_type_info  # Delegates to property

    def setMessageTypeInfo(self, value: String) -> DltMessage:
        """
        AUTOSAR-compliant setter for messageTypeInfo with method chaining.

        Args:
            value: The messageTypeInfo to set

        Returns:
            self for method chaining

        Note:
            Delegates to message_type_info property setter (gets validation automatically)
        """
        self.message_type_info = value  # Delegates to property setter
        return self

    def getPrivacyLevel(self) -> PrivacyLevel:
        """
        AUTOSAR-compliant getter for privacyLevel.

        Returns:
            The privacyLevel value

        Note:
            Delegates to privacy_level property (CODING_RULE_V2_00017)
        """
        return self.privacy_level  # Delegates to property

    def setPrivacyLevel(self, value: PrivacyLevel) -> DltMessage:
        """
        AUTOSAR-compliant setter for privacyLevel with method chaining.

        Args:
            value: The privacyLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to privacy_level property setter (gets validation automatically)
        """
        self.privacy_level = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_message_id(self, value: Optional[PositiveInteger]) -> DltMessage:
        """
        Set messageId and return self for chaining.

        Args:
            value: The messageId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message_id("value")
        """
        self.message_id = value  # Use property setter (gets validation)
        return self

    def with_message_line(self, value: Optional[PositiveInteger]) -> DltMessage:
        """
        Set messageLine and return self for chaining.

        Args:
            value: The messageLine to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message_line("value")
        """
        self.message_line = value  # Use property setter (gets validation)
        return self

    def with_message_source(self, value: Optional[String]) -> DltMessage:
        """
        Set messageSource and return self for chaining.

        Args:
            value: The messageSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message_source("value")
        """
        self.message_source = value  # Use property setter (gets validation)
        return self

    def with_message_type_info(self, value: Optional[String]) -> DltMessage:
        """
        Set messageTypeInfo and return self for chaining.

        Args:
            value: The messageTypeInfo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message_type_info("value")
        """
        self.message_type_info = value  # Use property setter (gets validation)
        return self

    def with_privacy_level(self, value: Optional[PrivacyLevel]) -> DltMessage:
        """
        Set privacyLevel and return self for chaining.

        Args:
            value: The privacyLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_privacy_level("value")
        """
        self.privacy_level = value  # Use property setter (gets validation)
        return self



class LogAndTraceMessageCollectionSet(ARElement):
    """
    Collection of DltMessages

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::LogAndTraceMessageCollectionSet

    Sources:
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 12, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of DltMessages in the DltMessageCollection atpVariation.
        self._dltMessage: List[DltMessage] = []

    @property
    def dlt_message(self) -> List[DltMessage]:
        """Get dltMessage (Pythonic accessor)."""
        return self._dltMessage

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDltMessage(self) -> List[DltMessage]:
        """
        AUTOSAR-compliant getter for dltMessage.

        Returns:
            The dltMessage value

        Note:
            Delegates to dlt_message property (CODING_RULE_V2_00017)
        """
        return self.dlt_message  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class PrivacyLevel(ARObject):
    """
    This meta-class defines the Privacy Level for a Log and Trace content.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::PrivacyLevel

    Sources:
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 18, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to CompuMethod of category TEXTTABLE the supported user-defined
        # privacy levels.
        self._compuMethod: Optional[CompuMethod] = None

    @property
    def compu_method(self) -> Optional[CompuMethod]:
        """Get compuMethod (Pythonic accessor)."""
        return self._compuMethod

    @compu_method.setter
    def compu_method(self, value: Optional[CompuMethod]) -> None:
        """
        Set compuMethod with validation.

        Args:
            value: The compuMethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuMethod = None
            return

        if not isinstance(value, CompuMethod):
            raise TypeError(
                f"compuMethod must be CompuMethod or None, got {type(value).__name__}"
            )
        self._compuMethod = value
        self._privacyLevel: Optional[PositiveInteger] = None

    @property
    def privacy_level(self) -> Optional[PositiveInteger]:
        """Get privacyLevel (Pythonic accessor)."""
        return self._privacyLevel

    @privacy_level.setter
    def privacy_level(self, value: Optional[PositiveInteger]) -> None:
        """
        Set privacyLevel with validation.

        Args:
            value: The privacyLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._privacyLevel = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"privacyLevel must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._privacyLevel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuMethod(self) -> CompuMethod:
        """
        AUTOSAR-compliant getter for compuMethod.

        Returns:
            The compuMethod value

        Note:
            Delegates to compu_method property (CODING_RULE_V2_00017)
        """
        return self.compu_method  # Delegates to property

    def setCompuMethod(self, value: CompuMethod) -> PrivacyLevel:
        """
        AUTOSAR-compliant setter for compuMethod with method chaining.

        Args:
            value: The compuMethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_method property setter (gets validation automatically)
        """
        self.compu_method = value  # Delegates to property setter
        return self

    def getPrivacyLevel(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for privacyLevel.

        Returns:
            The privacyLevel value

        Note:
            Delegates to privacy_level property (CODING_RULE_V2_00017)
        """
        return self.privacy_level  # Delegates to property

    def setPrivacyLevel(self, value: PositiveInteger) -> PrivacyLevel:
        """
        AUTOSAR-compliant setter for privacyLevel with method chaining.

        Args:
            value: The privacyLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to privacy_level property setter (gets validation automatically)
        """
        self.privacy_level = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_method(self, value: Optional[CompuMethod]) -> PrivacyLevel:
        """
        Set compuMethod and return self for chaining.

        Args:
            value: The compuMethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_method("value")
        """
        self.compu_method = value  # Use property setter (gets validation)
        return self

    def with_privacy_level(self, value: Optional[PositiveInteger]) -> PrivacyLevel:
        """
        Set privacyLevel and return self for chaining.

        Args:
            value: The privacyLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_privacy_level("value")
        """
        self.privacy_level = value  # Use property setter (gets validation)
        return self
