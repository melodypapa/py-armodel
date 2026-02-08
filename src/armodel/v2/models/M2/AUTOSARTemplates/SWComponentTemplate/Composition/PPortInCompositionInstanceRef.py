from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import PortInCompositionTypeInstanceRef


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs::PPortInCompositionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 951, Classic Platform
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
        # Tags: xml.
        # sequenceOffset=30.
        self._targetPPortPrototype: Optional["AbstractProvidedPort"] = None

    @property
    def target_p_port_prototype(self) -> Optional["AbstractProvidedPort"]:
        """Get targetPPortPrototype (Pythonic accessor)."""
        return self._targetPPortPrototype

    @target_p_port_prototype.setter
    def target_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> None:
        """
        Set targetPPortPrototype with validation.

        Args:
            value: The targetPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"targetPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._targetPPortPrototype = value

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

    def setContext(self, value: "SwComponent") -> "PPortInCompositionInstanceRef":
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

    def getTargetPPortPrototype(self) -> "AbstractProvidedPort":
        """
        AUTOSAR-compliant getter for targetPPortPrototype.

        Returns:
            The targetPPortPrototype value

        Note:
            Delegates to target_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.target_p_port_prototype  # Delegates to property

    def setTargetPPortPrototype(self, value: "AbstractProvidedPort") -> "PPortInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetPPortPrototype with method chaining.

        Args:
            value: The targetPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_p_port_prototype property setter (gets validation automatically)
        """
        self.target_p_port_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context(self, value: Optional["SwComponent"]) -> "PPortInCompositionInstanceRef":
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

    def with_target_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> "PPortInCompositionInstanceRef":
        """
        Set targetPPortPrototype and return self for chaining.

        Args:
            value: The targetPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_p_port_prototype("value")
        """
        self.target_p_port_prototype = value  # Use property setter (gets validation)
        return self
