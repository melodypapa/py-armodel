from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswModuleEntity


class BswInterruptEntity(BswModuleEntity):
    """
    BSW module entity, which is designed to be triggered by an interrupt.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInterruptEntity

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 75, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 212, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Category of the interrupt.
        self._interruptCategory: Optional["BswInterruptCategory"] = None

    @property
    def interrupt_category(self) -> Optional["BswInterruptCategory"]:
        """Get interruptCategory (Pythonic accessor)."""
        return self._interruptCategory

    @interrupt_category.setter
    def interrupt_category(self, value: Optional["BswInterruptCategory"]) -> None:
        """
        Set interruptCategory with validation.

        Args:
            value: The interruptCategory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interruptCategory = None
            return

        if not isinstance(value, BswInterruptCategory):
            raise TypeError(
                f"interruptCategory must be BswInterruptCategory or None, got {type(value).__name__}"
            )
        self._interruptCategory = value
        # Allows a textual documentation of the intended interrupt.
        self._interruptSource: Optional["String"] = None

    @property
    def interrupt_source(self) -> Optional["String"]:
        """Get interruptSource (Pythonic accessor)."""
        return self._interruptSource

    @interrupt_source.setter
    def interrupt_source(self, value: Optional["String"]) -> None:
        """
        Set interruptSource with validation.

        Args:
            value: The interruptSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interruptSource = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"interruptSource must be String or None, got {type(value).__name__}"
            )
        self._interruptSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInterruptCategory(self) -> "BswInterruptCategory":
        """
        AUTOSAR-compliant getter for interruptCategory.

        Returns:
            The interruptCategory value

        Note:
            Delegates to interrupt_category property (CODING_RULE_V2_00017)
        """
        return self.interrupt_category  # Delegates to property

    def setInterruptCategory(self, value: "BswInterruptCategory") -> "BswInterruptEntity":
        """
        AUTOSAR-compliant setter for interruptCategory with method chaining.

        Args:
            value: The interruptCategory to set

        Returns:
            self for method chaining

        Note:
            Delegates to interrupt_category property setter (gets validation automatically)
        """
        self.interrupt_category = value  # Delegates to property setter
        return self

    def getInterruptSource(self) -> "String":
        """
        AUTOSAR-compliant getter for interruptSource.

        Returns:
            The interruptSource value

        Note:
            Delegates to interrupt_source property (CODING_RULE_V2_00017)
        """
        return self.interrupt_source  # Delegates to property

    def setInterruptSource(self, value: "String") -> "BswInterruptEntity":
        """
        AUTOSAR-compliant setter for interruptSource with method chaining.

        Args:
            value: The interruptSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to interrupt_source property setter (gets validation automatically)
        """
        self.interrupt_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_interrupt_category(self, value: Optional["BswInterruptCategory"]) -> "BswInterruptEntity":
        """
        Set interruptCategory and return self for chaining.

        Args:
            value: The interruptCategory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interrupt_category("value")
        """
        self.interrupt_category = value  # Use property setter (gets validation)
        return self

    def with_interrupt_source(self, value: Optional["String"]) -> "BswInterruptEntity":
        """
        Set interruptSource and return self for chaining.

        Args:
            value: The interruptSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interrupt_source("value")
        """
        self.interrupt_source = value  # Use property setter (gets validation)
        return self
