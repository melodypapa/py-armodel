from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ClientServerOperation,
    RootSwComposition,
    System,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class OperationInSystemInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs::OperationInSystemInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1001, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value
        # Tags: xml.
        # sequenceOffset=20.
        self._context: Optional["RootSwComposition"] = None

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
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

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value
        # Tags: xml.
        # sequenceOffset=40.
        self._contextPort: RefType = None

    @property
    def context_port(self) -> RefType:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: RefType) -> None:
        """
        Set contextPort with validation.

        Args:
            value: The contextPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._contextPort = value
        # Tags: xml.
        # sequenceOffset=50.
        self._targetOperation: Optional["ClientServerOperation"] = None

    @property
    def target_operation(self) -> Optional["ClientServerOperation"]:
        """Get targetOperation (Pythonic accessor)."""
        return self._targetOperation

    @target_operation.setter
    def target_operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set targetOperation with validation.

        Args:
            value: The targetOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"targetOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._targetOperation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "OperationInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "OperationInSystemInstanceRef":
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

    def getContextPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextPort.

        Returns:
            The contextPort value

        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: RefType) -> "OperationInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextPort with method chaining.

        Args:
            value: The contextPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_port property setter (gets validation automatically)
        """
        self.context_port = value  # Delegates to property setter
        return self

    def getTargetOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for targetOperation.

        Returns:
            The targetOperation value

        Note:
            Delegates to target_operation property (CODING_RULE_V2_00017)
        """
        return self.target_operation  # Delegates to property

    def setTargetOperation(self, value: "ClientServerOperation") -> "OperationInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for targetOperation with method chaining.

        Args:
            value: The targetOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_operation property setter (gets validation automatically)
        """
        self.target_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["System"]) -> "OperationInSystemInstanceRef":
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_context(self, value: Optional["RootSwComposition"]) -> "OperationInSystemInstanceRef":
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

    def with_context_port(self, value: RefType) -> "OperationInSystemInstanceRef":
        """
        Set contextPort and return self for chaining.

        Args:
            value: The contextPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_port("value")
        """
        self.context_port = value  # Use property setter (gets validation)
        return self

    def with_target_operation(self, value: Optional["ClientServerOperation"]) -> "OperationInSystemInstanceRef":
        """
        Set targetOperation and return self for chaining.

        Args:
            value: The targetOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_operation("value")
        """
        self.target_operation = value  # Use property setter (gets validation)
        return self
