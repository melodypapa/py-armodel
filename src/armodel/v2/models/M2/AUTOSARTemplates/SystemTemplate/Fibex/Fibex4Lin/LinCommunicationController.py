from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import String
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class LinCommunicationController(ARObject, ABC):
    """
    LIN bus specific communication controller attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinCommunicationController

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 93, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is LinCommunicationController:
            raise TypeError("LinCommunicationController is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Version specifier for a communication protocol.
        self._protocolVersion: Optional["String"] = None

    @property
    def protocol_version(self) -> Optional["String"]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional["String"]) -> None:
        """
        Set protocolVersion with validation.

        Args:
            value: The protocolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolVersion must be String or None, got {type(value).__name__}"
            )
        self._protocolVersion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProtocolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolVersion.

        Returns:
            The protocolVersion value

        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: "String") -> "LinCommunicationController":
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_protocol_version(self, value: Optional["String"]) -> "LinCommunicationController":
        """
        Set protocolVersion and return self for chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self
