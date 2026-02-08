from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DltArgument,
    PrivacyLevel,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


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
        self._dltArgument: List["DltArgument"] = []

    @property
    def dlt_argument(self) -> List["DltArgument"]:
        """Get dltArgument (Pythonic accessor)."""
        return self._dltArgument
        # This attribute defines the unique Id for the DltMessage.
        self._messageId: Optional["PositiveInteger"] = None

    @property
    def message_id(self) -> Optional["PositiveInteger"]:
        """Get messageId (Pythonic accessor)."""
        return self._messageId

    @message_id.setter
    def message_id(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"messageId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._messageId = value
        # This attribute describes the position in the source file in this log message
        # was called.
        self._messageLine: Optional["PositiveInteger"] = None

    @property
    def message_line(self) -> Optional["PositiveInteger"]:
        """Get messageLine (Pythonic accessor)."""
        return self._messageLine

    @message_line.setter
    def message_line(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"messageLine must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._messageLine = value
        # This attribute describes the source file in which this log was called.
        self._messageSource: Optional["String"] = None

    @property
    def message_source(self) -> Optional["String"]:
        """Get messageSource (Pythonic accessor)."""
        return self._messageSource

    @message_source.setter
    def message_source(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"messageSource must be String or None, got {type(value).__name__}"
            )
        self._messageSource = value
        # This attribute describes the message Type.
        self._messageTypeInfo: Optional["String"] = None

    @property
    def message_type_info(self) -> Optional["String"]:
        """Get messageTypeInfo (Pythonic accessor)."""
        return self._messageTypeInfo

    @message_type_info.setter
    def message_type_info(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"messageTypeInfo must be String or None, got {type(value).__name__}"
            )
        self._messageTypeInfo = value
        # The Privacy Level helps to identify the Log and Trace the degree of privacy
        # to it.
        self._privacyLevel: Optional["PrivacyLevel"] = None

    @property
    def privacy_level(self) -> Optional["PrivacyLevel"]:
        """Get privacyLevel (Pythonic accessor)."""
        return self._privacyLevel

    @privacy_level.setter
    def privacy_level(self, value: Optional["PrivacyLevel"]) -> None:
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

    def getDltArgument(self) -> List["DltArgument"]:
        """
        AUTOSAR-compliant getter for dltArgument.

        Returns:
            The dltArgument value

        Note:
            Delegates to dlt_argument property (CODING_RULE_V2_00017)
        """
        return self.dlt_argument  # Delegates to property

    def getMessageId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for messageId.

        Returns:
            The messageId value

        Note:
            Delegates to message_id property (CODING_RULE_V2_00017)
        """
        return self.message_id  # Delegates to property

    def setMessageId(self, value: "PositiveInteger") -> "DltMessage":
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

    def getMessageLine(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for messageLine.

        Returns:
            The messageLine value

        Note:
            Delegates to message_line property (CODING_RULE_V2_00017)
        """
        return self.message_line  # Delegates to property

    def setMessageLine(self, value: "PositiveInteger") -> "DltMessage":
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

    def getMessageSource(self) -> "String":
        """
        AUTOSAR-compliant getter for messageSource.

        Returns:
            The messageSource value

        Note:
            Delegates to message_source property (CODING_RULE_V2_00017)
        """
        return self.message_source  # Delegates to property

    def setMessageSource(self, value: "String") -> "DltMessage":
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

    def getMessageTypeInfo(self) -> "String":
        """
        AUTOSAR-compliant getter for messageTypeInfo.

        Returns:
            The messageTypeInfo value

        Note:
            Delegates to message_type_info property (CODING_RULE_V2_00017)
        """
        return self.message_type_info  # Delegates to property

    def setMessageTypeInfo(self, value: "String") -> "DltMessage":
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

    def getPrivacyLevel(self) -> "PrivacyLevel":
        """
        AUTOSAR-compliant getter for privacyLevel.

        Returns:
            The privacyLevel value

        Note:
            Delegates to privacy_level property (CODING_RULE_V2_00017)
        """
        return self.privacy_level  # Delegates to property

    def setPrivacyLevel(self, value: "PrivacyLevel") -> "DltMessage":
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

    def with_message_id(self, value: Optional["PositiveInteger"]) -> "DltMessage":
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

    def with_message_line(self, value: Optional["PositiveInteger"]) -> "DltMessage":
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

    def with_message_source(self, value: Optional["String"]) -> "DltMessage":
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

    def with_message_type_info(self, value: Optional["String"]) -> "DltMessage":
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

    def with_privacy_level(self, value: Optional["PrivacyLevel"]) -> "DltMessage":
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
