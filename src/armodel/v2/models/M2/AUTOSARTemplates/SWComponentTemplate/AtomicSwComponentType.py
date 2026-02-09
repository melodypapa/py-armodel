from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    SwComponentType,
)


class AtomicSwComponentType(SwComponentType, ABC):
    """
    An atomic software component is atomic in the sense that it cannot be
    further decomposed and distributed across multiple ECUs.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 304, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 300, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 70, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2000, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 205, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 43, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 161, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtomicSwComponentType:
            raise TypeError("AtomicSwComponentType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The SwcInternalBehaviors owned by an AtomicSw be located in a different
                # physical file.
        # aggregation is <<atpSplitable>>.
        # atpVariation.
        self._internalBehavior: Optional["SwcInternalBehavior"] = None

    @property
    def internal_behavior(self) -> Optional["SwcInternalBehavior"]:
        """Get internalBehavior (Pythonic accessor)."""
        return self._internalBehavior

    @internal_behavior.setter
    def internal_behavior(self, value: Optional["SwcInternalBehavior"]) -> None:
        """
        Set internalBehavior with validation.

        Args:
            value: The internalBehavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._internalBehavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"internalBehavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._internalBehavior = value
        self._symbolProps: Optional["SymbolProps"] = None

    @property
    def symbol_props(self) -> Optional["SymbolProps"]:
        """Get symbolProps (Pythonic accessor)."""
        return self._symbolProps

    @symbol_props.setter
    def symbol_props(self, value: Optional["SymbolProps"]) -> None:
        """
        Set symbolProps with validation.

        Args:
            value: The symbolProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolProps = None
            return

        if not isinstance(value, SymbolProps):
            raise TypeError(
                f"symbolProps must be SymbolProps or None, got {type(value).__name__}"
            )
        self._symbolProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInternalBehavior(self) -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant getter for internalBehavior.

        Returns:
            The internalBehavior value

        Note:
            Delegates to internal_behavior property (CODING_RULE_V2_00017)
        """
        return self.internal_behavior  # Delegates to property

    def setInternalBehavior(self, value: "SwcInternalBehavior") -> "AtomicSwComponentType":
        """
        AUTOSAR-compliant setter for internalBehavior with method chaining.

        Args:
            value: The internalBehavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to internal_behavior property setter (gets validation automatically)
        """
        self.internal_behavior = value  # Delegates to property setter
        return self

    def getSymbolProps(self) -> "SymbolProps":
        """
        AUTOSAR-compliant getter for symbolProps.

        Returns:
            The symbolProps value

        Note:
            Delegates to symbol_props property (CODING_RULE_V2_00017)
        """
        return self.symbol_props  # Delegates to property

    def setSymbolProps(self, value: "SymbolProps") -> "AtomicSwComponentType":
        """
        AUTOSAR-compliant setter for symbolProps with method chaining.

        Args:
            value: The symbolProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol_props property setter (gets validation automatically)
        """
        self.symbol_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_internal_behavior(self, value: Optional["SwcInternalBehavior"]) -> "AtomicSwComponentType":
        """
        Set internalBehavior and return self for chaining.

        Args:
            value: The internalBehavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal_behavior("value")
        """
        self.internal_behavior = value  # Use property setter (gets validation)
        return self

    def with_symbol_props(self, value: Optional["SymbolProps"]) -> "AtomicSwComponentType":
        """
        Set symbolProps and return self for chaining.

        Args:
            value: The symbolProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol_props("value")
        """
        self.symbol_props = value  # Use property setter (gets validation)
        return self
