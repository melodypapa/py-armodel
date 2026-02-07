from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class AbstractCanCommunicationControllerAttributes(ARObject, ABC):
    """
    For the configuration of the CanController parameters two different
    approaches can be used: 1. Providing exact values which are taken by the ECU
    developer (CanControllerConfiguration). 2. Providing ranges of values which
    are taken as requirements and have to be respected by the ECU developer
    (CanControllerConfigurationRequirements).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::AbstractCanCommunicationControllerAttributes

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 64, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanCommunicationControllerAttributes:
            raise TypeError("AbstractCanCommunicationControllerAttributes is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Additional CanFD ranges of the bit timing related configuration of a CanFD
                # controller.
        # If this element exists controller supports CanFD frames and the ECU take
                # these ranges as requirements for the the CanFD controller.
        self._canControllerFd: Optional["CanControllerFd"] = None

    @property
    def can_controller_fd(self) -> Optional["CanControllerFd"]:
        """Get canControllerFd (Pythonic accessor)."""
        return self._canControllerFd

    @can_controller_fd.setter
    def can_controller_fd(self, value: Optional["CanControllerFd"]) -> None:
        """
        Set canControllerFd with validation.

        Args:
            value: The canControllerFd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canControllerFd = None
            return

        if not isinstance(value, CanControllerFd):
            raise TypeError(
                f"canControllerFd must be CanControllerFd or None, got {type(value).__name__}"
            )
        self._canControllerFd = value
        # Additional CanXL ranges of the bit timing related configuration of a CanXL
                # controller.
        # If this element exists controller supports CanXL frames and the ECU take
                # these ranges as requirements for the the CanXL controller.
        self._canControllerXl: Optional["CanControllerXl"] = None

    @property
    def can_controller_xl(self) -> Optional["CanControllerXl"]:
        """Get canControllerXl (Pythonic accessor)."""
        return self._canControllerXl

    @can_controller_xl.setter
    def can_controller_xl(self, value: Optional["CanControllerXl"]) -> None:
        """
        Set canControllerXl with validation.

        Args:
            value: The canControllerXl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canControllerXl = None
            return

        if not isinstance(value, CanControllerXl):
            raise TypeError(
                f"canControllerXl must be CanControllerXl or None, got {type(value).__name__}"
            )
        self._canControllerXl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanControllerFd(self) -> "CanControllerFd":
        """
        AUTOSAR-compliant getter for canControllerFd.

        Returns:
            The canControllerFd value

        Note:
            Delegates to can_controller_fd property (CODING_RULE_V2_00017)
        """
        return self.can_controller_fd  # Delegates to property

    def setCanControllerFd(self, value: "CanControllerFd") -> "AbstractCanCommunicationControllerAttributes":
        """
        AUTOSAR-compliant setter for canControllerFd with method chaining.

        Args:
            value: The canControllerFd to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_controller_fd property setter (gets validation automatically)
        """
        self.can_controller_fd = value  # Delegates to property setter
        return self

    def getCanControllerXl(self) -> "CanControllerXl":
        """
        AUTOSAR-compliant getter for canControllerXl.

        Returns:
            The canControllerXl value

        Note:
            Delegates to can_controller_xl property (CODING_RULE_V2_00017)
        """
        return self.can_controller_xl  # Delegates to property

    def setCanControllerXl(self, value: "CanControllerXl") -> "AbstractCanCommunicationControllerAttributes":
        """
        AUTOSAR-compliant setter for canControllerXl with method chaining.

        Args:
            value: The canControllerXl to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_controller_xl property setter (gets validation automatically)
        """
        self.can_controller_xl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_controller_fd(self, value: Optional["CanControllerFd"]) -> "AbstractCanCommunicationControllerAttributes":
        """
        Set canControllerFd and return self for chaining.

        Args:
            value: The canControllerFd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_controller_fd("value")
        """
        self.can_controller_fd = value  # Use property setter (gets validation)
        return self

    def with_can_controller_xl(self, value: Optional["CanControllerXl"]) -> "AbstractCanCommunicationControllerAttributes":
        """
        Set canControllerXl and return self for chaining.

        Args:
            value: The canControllerXl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_controller_xl("value")
        """
        self.can_controller_xl = value  # Use property setter (gets validation)
        return self
