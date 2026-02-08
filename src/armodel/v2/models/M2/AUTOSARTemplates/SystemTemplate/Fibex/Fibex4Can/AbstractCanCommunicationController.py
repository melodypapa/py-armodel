from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class AbstractCanCommunicationController(ARObject, ABC):
    """
    Abstract class that is used to collect the common TtCAN and CAN Controller
    attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 63, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanCommunicationController:
            raise TypeError("AbstractCanCommunicationController is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CAN Bit Timing configuration.
        self._canControllerControllerAttributes: Optional["AbstractCan"] = None

    @property
    def can_controller_controller_attributes(self) -> Optional["AbstractCan"]:
        """Get canControllerControllerAttributes (Pythonic accessor)."""
        return self._canControllerControllerAttributes

    @can_controller_controller_attributes.setter
    def can_controller_controller_attributes(self, value: Optional["AbstractCan"]) -> None:
        """
        Set canControllerControllerAttributes with validation.

        Args:
            value: The canControllerControllerAttributes to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canControllerControllerAttributes = None
            return

        if not isinstance(value, AbstractCan):
            raise TypeError(
                f"canControllerControllerAttributes must be AbstractCan or None, got {type(value).__name__}"
            )
        self._canControllerControllerAttributes = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanControllerControllerAttributes(self) -> "AbstractCan":
        """
        AUTOSAR-compliant getter for canControllerControllerAttributes.

        Returns:
            The canControllerControllerAttributes value

        Note:
            Delegates to can_controller_controller_attributes property (CODING_RULE_V2_00017)
        """
        return self.can_controller_controller_attributes  # Delegates to property

    def setCanControllerControllerAttributes(self, value: "AbstractCan") -> "AbstractCanCommunicationController":
        """
        AUTOSAR-compliant setter for canControllerControllerAttributes with method chaining.

        Args:
            value: The canControllerControllerAttributes to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_controller_controller_attributes property setter (gets validation automatically)
        """
        self.can_controller_controller_attributes = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_controller_controller_attributes(self, value: Optional["AbstractCan"]) -> "AbstractCanCommunicationController":
        """
        Set canControllerControllerAttributes and return self for chaining.

        Args:
            value: The canControllerControllerAttributes to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_controller_controller_attributes("value")
        """
        self.can_controller_controller_attributes = value  # Use property setter (gets validation)
        return self
