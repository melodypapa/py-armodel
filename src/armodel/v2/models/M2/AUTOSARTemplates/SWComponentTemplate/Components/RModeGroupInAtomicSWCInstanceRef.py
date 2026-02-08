from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ModeGroupInAtomicSwcInstanceRef

    RefType,
)


class RModeGroupInAtomicSWCInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::RModeGroupInAtomicSWCInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 948, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextRPortPrototype: Optional["AbstractRequiredPort"] = None

    @property
    def context_r_port_prototype(self) -> Optional["AbstractRequiredPort"]:
        """Get contextRPortPrototype (Pythonic accessor)."""
        return self._contextRPortPrototype

    @context_r_port_prototype.setter
    def context_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> None:
        """
        Set contextRPortPrototype with validation.

        Args:
            value: The contextRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"contextRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._contextRPortPrototype = value
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

    def getContextRPortPrototype(self) -> "AbstractRequiredPort":
        """
        AUTOSAR-compliant getter for contextRPortPrototype.

        Returns:
            The contextRPortPrototype value

        Note:
            Delegates to context_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_r_port_prototype  # Delegates to property

    def setContextRPortPrototype(self, value: "AbstractRequiredPort") -> "RModeGroupInAtomicSWCInstanceRef":
        """
        AUTOSAR-compliant setter for contextRPortPrototype with method chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_r_port_prototype property setter (gets validation automatically)
        """
        self.context_r_port_prototype = value  # Delegates to property setter
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

    def setTargetMode(self, value: RefType) -> "RModeGroupInAtomicSWCInstanceRef":
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

    def with_context_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> "RModeGroupInAtomicSWCInstanceRef":
        """
        Set contextRPortPrototype and return self for chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_r_port_prototype("value")
        """
        self.context_r_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional[RefType]) -> "RModeGroupInAtomicSWCInstanceRef":
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
