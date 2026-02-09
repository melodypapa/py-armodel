from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    PortInCompositionTypeInstanceRef,
)


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 952, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 459, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._context: Optional["SwComponent"] = None

    @property
    def context(self) -> Optional["SwComponent"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["SwComponent"]) -> None:
        """
        Set context with validation.

        Args:
            value: The context to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"context must be SwComponent or None, got {type(value).__name__}"
            )
        self._context = value
        # sequenceOffset=30.
        self._targetRPortPrototype: Optional["AbstractRequiredPort"] = None

    @property
    def target_r_port_prototype(self) -> Optional["AbstractRequiredPort"]:
        """Get targetRPortPrototype (Pythonic accessor)."""
        return self._targetRPortPrototype

    @target_r_port_prototype.setter
    def target_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> None:
        """
        Set targetRPortPrototype with validation.

        Args:
            value: The targetRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"targetRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._targetRPortPrototype = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "SwComponent") -> "RPortInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getTargetRPortPrototype(self) -> "AbstractRequiredPort":
        """
        AUTOSAR-compliant getter for targetRPortPrototype.

        Returns:
            The targetRPortPrototype value

        Note:
            Delegates to target_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.target_r_port_prototype  # Delegates to property

    def setTargetRPortPrototype(self, value: "AbstractRequiredPort") -> "RPortInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetRPortPrototype with method chaining.

        Args:
            value: The targetRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_r_port_prototype property setter (gets validation automatically)
        """
        self.target_r_port_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context(self, value: Optional["SwComponent"]) -> "RPortInCompositionInstanceRef":
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_target_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> "RPortInCompositionInstanceRef":
        """
        Set targetRPortPrototype and return self for chaining.

        Args:
            value: The targetRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_r_port_prototype("value")
        """
        self.target_r_port_prototype = value  # Use property setter (gets validation)
        return self
