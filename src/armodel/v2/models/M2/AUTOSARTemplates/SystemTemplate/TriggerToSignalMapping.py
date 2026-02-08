from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TriggerToSignalMapping(DataMapping):
    """
    This meta-class represents the ability to map a trigger to a SystemSignal of
    size 0. The Trigger does not transport any other information than its
    existence, therefore the limitation in terms of signal length.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::TriggerToSignalMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 249, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the SystemSignal taken to transport the Trigger network.
        self._systemSignal: Optional["SystemSignal"] = None

    @property
    def system_signal(self) -> Optional["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["SystemSignal"]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value
        # to a remote ECU.
        # by: TriggerInSystemInstance.
        self._triggerRef: RefType = None

    @property
    def trigger_ref(self) -> RefType:
        """Get triggerRef (Pythonic accessor)."""
        return self._triggerRef

    @trigger_ref.setter
    def trigger_ref(self, value: RefType) -> None:
        """
        Set triggerRef with validation.

        Args:
            value: The triggerRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerRef = None
            return

        self._triggerRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "TriggerToSignalMapping":
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    def getTriggerRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for triggerRef.

        Returns:
            The triggerRef value

        Note:
            Delegates to trigger_ref property (CODING_RULE_V2_00017)
        """
        return self.trigger_ref  # Delegates to property

    def setTriggerRef(self, value: RefType) -> "TriggerToSignalMapping":
        """
        AUTOSAR-compliant setter for triggerRef with method chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger_ref property setter (gets validation automatically)
        """
        self.trigger_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "TriggerToSignalMapping":
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self

    def with_trigger_ref(self, value: Optional[RefType]) -> "TriggerToSignalMapping":
        """
        Set triggerRef and return self for chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_ref("value")
        """
        self.trigger_ref = value  # Use property setter (gets validation)
        return self
