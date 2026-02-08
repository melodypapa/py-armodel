from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractDoIpLogic,
    Integer,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DoIpLogicAddress(Identifiable):
    """
    The logical DoIP address.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::DoIpLogicAddress

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 555, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The logical DoIP address.
        self._address: Optional["Integer"] = None

    @property
    def address(self) -> Optional["Integer"]:
        """Get address (Pythonic accessor)."""
        return self._address

    @address.setter
    def address(self, value: Optional["Integer"]) -> None:
        """
        Set address with validation.

        Args:
            value: The address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._address = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"address must be Integer or None, got {type(value).__name__}"
            )
        self._address = value
        # Collection of additional LogicAddress properties.
        self._doIpLogic: Optional["AbstractDoIpLogic"] = None

    @property
    def do_ip_logic(self) -> Optional["AbstractDoIpLogic"]:
        """Get doIpLogic (Pythonic accessor)."""
        return self._doIpLogic

    @do_ip_logic.setter
    def do_ip_logic(self, value: Optional["AbstractDoIpLogic"]) -> None:
        """
        Set doIpLogic with validation.

        Args:
            value: The doIpLogic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpLogic = None
            return

        if not isinstance(value, AbstractDoIpLogic):
            raise TypeError(
                f"doIpLogic must be AbstractDoIpLogic or None, got {type(value).__name__}"
            )
        self._doIpLogic = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddress(self) -> "Integer":
        """
        AUTOSAR-compliant getter for address.

        Returns:
            The address value

        Note:
            Delegates to address property (CODING_RULE_V2_00017)
        """
        return self.address  # Delegates to property

    def setAddress(self, value: "Integer") -> "DoIpLogicAddress":
        """
        AUTOSAR-compliant setter for address with method chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Note:
            Delegates to address property setter (gets validation automatically)
        """
        self.address = value  # Delegates to property setter
        return self

    def getDoIpLogic(self) -> "AbstractDoIpLogic":
        """
        AUTOSAR-compliant getter for doIpLogic.

        Returns:
            The doIpLogic value

        Note:
            Delegates to do_ip_logic property (CODING_RULE_V2_00017)
        """
        return self.do_ip_logic  # Delegates to property

    def setDoIpLogic(self, value: "AbstractDoIpLogic") -> "DoIpLogicAddress":
        """
        AUTOSAR-compliant setter for doIpLogic with method chaining.

        Args:
            value: The doIpLogic to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_logic property setter (gets validation automatically)
        """
        self.do_ip_logic = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address(self, value: Optional["Integer"]) -> "DoIpLogicAddress":
        """
        Set address and return self for chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address("value")
        """
        self.address = value  # Use property setter (gets validation)
        return self

    def with_do_ip_logic(self, value: Optional["AbstractDoIpLogic"]) -> "DoIpLogicAddress":
        """
        Set doIpLogic and return self for chaining.

        Args:
            value: The doIpLogic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_logic("value")
        """
        self.do_ip_logic = value  # Use property setter (gets validation)
        return self
