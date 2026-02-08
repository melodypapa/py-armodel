from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ModeGroupInAtomicSwcInstanceRef

    RefType,
)


class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::PModeGroupInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 949, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextPPortPrototype: Optional["AbstractProvidedPort"] = None

    @property
    def context_p_port_prototype(self) -> Optional["AbstractProvidedPort"]:
        """Get contextPPortPrototype (Pythonic accessor)."""
        return self._contextPPortPrototype

    @context_p_port_prototype.setter
    def context_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> None:
        """
        Set contextPPortPrototype with validation.

        Args:
            value: The contextPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"contextPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._contextPPortPrototype = value
        # Tags: xml.
        # sequenceOffset=30.
        self._targetMode: RefType = None

    @property
    def target_mode(self) -> RefType:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: RefType) -> None:
        """
        Set targetMode with validation.

        Args:
            value: The targetMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        self._targetMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextPPortPrototype(self) -> "AbstractProvidedPort":
        """
        AUTOSAR-compliant getter for contextPPortPrototype.

        Returns:
            The contextPPortPrototype value

        Note:
            Delegates to context_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_p_port_prototype  # Delegates to property

    def setContextPPortPrototype(self, value: "AbstractProvidedPort") -> "PModeGroupInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextPPortPrototype with method chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_p_port_prototype property setter (gets validation automatically)
        """
        self.context_p_port_prototype = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetMode.

        Returns:
            The targetMode value

        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: RefType) -> "PModeGroupInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetMode with method chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> "PModeGroupInAtomicSwcInstanceRef":
        """
        Set contextPPortPrototype and return self for chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_p_port_prototype("value")
        """
        self.context_p_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional[RefType]) -> "PModeGroupInAtomicSwcInstanceRef":
        """
        Set targetMode and return self for chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self
