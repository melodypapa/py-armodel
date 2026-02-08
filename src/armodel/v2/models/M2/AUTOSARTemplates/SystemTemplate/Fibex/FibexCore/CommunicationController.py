from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CommunicationController(ARObject, ABC):
    """
    The communication controller is a dedicated hardware device by means of
    which hosts are sending frames to and receiving frames from the
    communication medium. Tags: vh.latestBindingTime=postBuild

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 53, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationController:
            raise TypeError("CommunicationController is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether the ECU shall be woken up by this wake up is possible up is
        # not supported wakeUpByControllerSupported is set to TRUE shall be supported
        # by both hardware and.
        self._wakeUpBy: Optional["Boolean"] = None

    @property
    def wake_up_by(self) -> Optional["Boolean"]:
        """Get wakeUpBy (Pythonic accessor)."""
        return self._wakeUpBy

    @wake_up_by.setter
    def wake_up_by(self, value: Optional["Boolean"]) -> None:
        """
        Set wakeUpBy with validation.

        Args:
            value: The wakeUpBy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeUpBy = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"wakeUpBy must be Boolean or None, got {type(value).__name__}"
            )
        self._wakeUpBy = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getWakeUpBy(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for wakeUpBy.

        Returns:
            The wakeUpBy value

        Note:
            Delegates to wake_up_by property (CODING_RULE_V2_00017)
        """
        return self.wake_up_by  # Delegates to property

    def setWakeUpBy(self, value: "Boolean") -> "CommunicationController":
        """
        AUTOSAR-compliant setter for wakeUpBy with method chaining.

        Args:
            value: The wakeUpBy to set

        Returns:
            self for method chaining

        Note:
            Delegates to wake_up_by property setter (gets validation automatically)
        """
        self.wake_up_by = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_wake_up_by(self, value: Optional["Boolean"]) -> "CommunicationController":
        """
        Set wakeUpBy and return self for chaining.

        Args:
            value: The wakeUpBy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wake_up_by("value")
        """
        self.wake_up_by = value  # Use property setter (gets validation)
        return self
