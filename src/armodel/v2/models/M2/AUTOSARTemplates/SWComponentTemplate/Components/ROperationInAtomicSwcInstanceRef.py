from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractRequiredPort,
    ClientServerOperation,
    OperationInAtomicSwcInstanceRef,
)


class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::ROperationInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 947, Classic Platform
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
        self._targetRequiredOperation: Optional["ClientServerOperation"] = None

    @property
    def target_required_operation(self) -> Optional["ClientServerOperation"]:
        """Get targetRequiredOperation (Pythonic accessor)."""
        return self._targetRequiredOperation

    @target_required_operation.setter
    def target_required_operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set targetRequiredOperation with validation.

        Args:
            value: The targetRequiredOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetRequiredOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"targetRequiredOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._targetRequiredOperation = value

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

    def setContextRPortPrototype(self, value: "AbstractRequiredPort") -> "ROperationInAtomicSwcInstanceRef":
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

    def getTargetRequiredOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for targetRequiredOperation.

        Returns:
            The targetRequiredOperation value

        Note:
            Delegates to target_required_operation property (CODING_RULE_V2_00017)
        """
        return self.target_required_operation  # Delegates to property

    def setTargetRequiredOperation(self, value: "ClientServerOperation") -> "ROperationInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetRequiredOperation with method chaining.

        Args:
            value: The targetRequiredOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_required_operation property setter (gets validation automatically)
        """
        self.target_required_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> "ROperationInAtomicSwcInstanceRef":
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

    def with_target_required_operation(self, value: Optional["ClientServerOperation"]) -> "ROperationInAtomicSwcInstanceRef":
        """
        Set targetRequiredOperation and return self for chaining.

        Args:
            value: The targetRequiredOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_required_operation("value")
        """
        self.target_required_operation = value  # Use property setter (gets validation)
        return self
