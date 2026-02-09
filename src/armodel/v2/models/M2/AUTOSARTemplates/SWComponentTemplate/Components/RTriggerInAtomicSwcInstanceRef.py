from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    TriggerInAtomicSwcInstanceRef,
)

    RefType,
)


class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 945, Classic Platform
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
        # sequenceOffset=30.
        self._targetTrigger: RefType = None

    @property
    def target_trigger(self) -> RefType:
        """Get targetTrigger (Pythonic accessor)."""
        return self._targetTrigger

    @target_trigger.setter
    def target_trigger(self, value: RefType) -> None:
        """
        Set targetTrigger with validation.

        Args:
            value: The targetTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetTrigger = None
            return

        self._targetTrigger = value

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

    def setContextRPortPrototype(self, value: "AbstractRequiredPort") -> "RTriggerInAtomicSwcInstanceRef":
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

    def getTargetTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetTrigger.

        Returns:
            The targetTrigger value

        Note:
            Delegates to target_trigger property (CODING_RULE_V2_00017)
        """
        return self.target_trigger  # Delegates to property

    def setTargetTrigger(self, value: RefType) -> "RTriggerInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetTrigger with method chaining.

        Args:
            value: The targetTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_trigger property setter (gets validation automatically)
        """
        self.target_trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> "RTriggerInAtomicSwcInstanceRef":
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

    def with_target_trigger(self, value: Optional[RefType]) -> "RTriggerInAtomicSwcInstanceRef":
        """
        Set targetTrigger and return self for chaining.

        Args:
            value: The targetTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_trigger("value")
        """
        self.target_trigger = value  # Use property setter (gets validation)
        return self
