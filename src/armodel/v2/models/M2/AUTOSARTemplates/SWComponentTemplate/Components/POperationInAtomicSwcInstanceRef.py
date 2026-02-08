from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import OperationInAtomicSwcInstanceRef


class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::POperationInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 948, Classic Platform
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
        self._targetProvidedOperation: Optional["ClientServerOperation"] = None

    @property
    def target_provided_operation(self) -> Optional["ClientServerOperation"]:
        """Get targetProvidedOperation (Pythonic accessor)."""
        return self._targetProvidedOperation

    @target_provided_operation.setter
    def target_provided_operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set targetProvidedOperation with validation.

        Args:
            value: The targetProvidedOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetProvidedOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"targetProvidedOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._targetProvidedOperation = value

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

    def setContextPPortPrototype(self, value: "AbstractProvidedPort") -> "POperationInAtomicSwcInstanceRef":
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

    def getTargetProvidedOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for targetProvidedOperation.

        Returns:
            The targetProvidedOperation value

        Note:
            Delegates to target_provided_operation property (CODING_RULE_V2_00017)
        """
        return self.target_provided_operation  # Delegates to property

    def setTargetProvidedOperation(self, value: "ClientServerOperation") -> "POperationInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetProvidedOperation with method chaining.

        Args:
            value: The targetProvidedOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_provided_operation property setter (gets validation automatically)
        """
        self.target_provided_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> "POperationInAtomicSwcInstanceRef":
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

    def with_target_provided_operation(self, value: Optional["ClientServerOperation"]) -> "POperationInAtomicSwcInstanceRef":
        """
        Set targetProvidedOperation and return self for chaining.

        Args:
            value: The targetProvidedOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_provided_operation("value")
        """
        self.target_provided_operation = value  # Use property setter (gets validation)
        return self
