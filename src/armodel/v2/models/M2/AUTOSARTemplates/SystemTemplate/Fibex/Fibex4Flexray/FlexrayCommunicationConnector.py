from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector


class FlexrayCommunicationConnector(CommunicationConnector):
    """
    FlexRay specific attributes to the CommunicationConnector

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayCommunicationConnector

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value of this attribute influences the shutdown of the FlexRay NM.
        # FrNm switches to bus sleep seconds after the completion last repetition cycle
                # containing a NM vote.
        self._nmReadySleep: Optional["Float"] = None

    @property
    def nm_ready_sleep(self) -> Optional["Float"]:
        """Get nmReadySleep (Pythonic accessor)."""
        return self._nmReadySleep

    @nm_ready_sleep.setter
    def nm_ready_sleep(self, value: Optional["Float"]) -> None:
        """
        Set nmReadySleep with validation.

        Args:
            value: The nmReadySleep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmReadySleep = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"nmReadySleep must be Float or None, got {type(value).__name__}"
            )
        self._nmReadySleep = value
        # Referenced channel used by the node to send a wakeup (pWakeupChannel).
        self._wakeUp: Optional["Boolean"] = None

    @property
    def wake_up(self) -> Optional["Boolean"]:
        """Get wakeUp (Pythonic accessor)."""
        return self._wakeUp

    @wake_up.setter
    def wake_up(self, value: Optional["Boolean"]) -> None:
        """
        Set wakeUp with validation.

        Args:
            value: The wakeUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeUp = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"wakeUp must be Boolean or None, got {type(value).__name__}"
            )
        self._wakeUp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmReadySleep(self) -> "Float":
        """
        AUTOSAR-compliant getter for nmReadySleep.

        Returns:
            The nmReadySleep value

        Note:
            Delegates to nm_ready_sleep property (CODING_RULE_V2_00017)
        """
        return self.nm_ready_sleep  # Delegates to property

    def setNmReadySleep(self, value: "Float") -> "FlexrayCommunicationConnector":
        """
        AUTOSAR-compliant setter for nmReadySleep with method chaining.

        Args:
            value: The nmReadySleep to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_ready_sleep property setter (gets validation automatically)
        """
        self.nm_ready_sleep = value  # Delegates to property setter
        return self

    def getWakeUp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for wakeUp.

        Returns:
            The wakeUp value

        Note:
            Delegates to wake_up property (CODING_RULE_V2_00017)
        """
        return self.wake_up  # Delegates to property

    def setWakeUp(self, value: "Boolean") -> "FlexrayCommunicationConnector":
        """
        AUTOSAR-compliant setter for wakeUp with method chaining.

        Args:
            value: The wakeUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to wake_up property setter (gets validation automatically)
        """
        self.wake_up = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_ready_sleep(self, value: Optional["Float"]) -> "FlexrayCommunicationConnector":
        """
        Set nmReadySleep and return self for chaining.

        Args:
            value: The nmReadySleep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_ready_sleep("value")
        """
        self.nm_ready_sleep = value  # Use property setter (gets validation)
        return self

    def with_wake_up(self, value: Optional["Boolean"]) -> "FlexrayCommunicationConnector":
        """
        Set wakeUp and return self for chaining.

        Args:
            value: The wakeUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wake_up("value")
        """
        self.wake_up = value  # Use property setter (gets validation)
        return self
