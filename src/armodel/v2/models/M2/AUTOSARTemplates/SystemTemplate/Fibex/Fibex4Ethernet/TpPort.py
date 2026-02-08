from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class TpPort(ARObject):
    """
    Dynamic or direct assignment of a PortNumber.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 461, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates whether the source port is dynamically.
        self._dynamically: Optional["Boolean"] = None

    @property
    def dynamically(self) -> Optional["Boolean"]:
        """Get dynamically (Pythonic accessor)."""
        return self._dynamically

    @dynamically.setter
    def dynamically(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamically with validation.

        Args:
            value: The dynamically to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamically = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"dynamically must be Boolean or None, got {type(value).__name__}"
            )
        self._dynamically = value
        # Port Number.
        self._portNumber: Optional["PositiveInteger"] = None

    @property
    def port_number(self) -> Optional["PositiveInteger"]:
        """Get portNumber (Pythonic accessor)."""
        return self._portNumber

    @port_number.setter
    def port_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set portNumber with validation.

        Args:
            value: The portNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portNumber = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"portNumber must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._portNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamically(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamically.

        Returns:
            The dynamically value

        Note:
            Delegates to dynamically property (CODING_RULE_V2_00017)
        """
        return self.dynamically  # Delegates to property

    def setDynamically(self, value: "Boolean") -> "TpPort":
        """
        AUTOSAR-compliant setter for dynamically with method chaining.

        Args:
            value: The dynamically to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamically property setter (gets validation automatically)
        """
        self.dynamically = value  # Delegates to property setter
        return self

    def getPortNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for portNumber.

        Returns:
            The portNumber value

        Note:
            Delegates to port_number property (CODING_RULE_V2_00017)
        """
        return self.port_number  # Delegates to property

    def setPortNumber(self, value: "PositiveInteger") -> "TpPort":
        """
        AUTOSAR-compliant setter for portNumber with method chaining.

        Args:
            value: The portNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_number property setter (gets validation automatically)
        """
        self.port_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamically(self, value: Optional["Boolean"]) -> "TpPort":
        """
        Set dynamically and return self for chaining.

        Args:
            value: The dynamically to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamically("value")
        """
        self.dynamically = value  # Use property setter (gets validation)
        return self

    def with_port_number(self, value: Optional["PositiveInteger"]) -> "TpPort":
        """
        Set portNumber and return self for chaining.

        Args:
            value: The portNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_number("value")
        """
        self.port_number = value  # Use property setter (gets validation)
        return self
