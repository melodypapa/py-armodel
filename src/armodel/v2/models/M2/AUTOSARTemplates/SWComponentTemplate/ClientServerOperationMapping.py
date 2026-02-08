from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ClientServerOperation,
    DataTransformation,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ClientServerOperationMapping(ARObject):
    """
    Defines the mapping of two particular ClientServerOperations in context of
    two different ClientServer Interfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ClientServerOperationMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 129, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the mapping of two particular ArgumentData with unequal names or
        # unequal semantic range) in context of Operations.
        self._argument: List[RefType] = []

    @property
    def argument(self) -> List[RefType]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # First to-be-mapped ClientServerOperation of a Client.
        self._firstOperation: Optional["ClientServerOperation"] = None

    @property
    def first_operation(self) -> Optional["ClientServerOperation"]:
        """Get firstOperation (Pythonic accessor)."""
        return self._firstOperation

    @first_operation.setter
    def first_operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set firstOperation with validation.

        Args:
            value: The firstOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"firstOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._firstOperation = value
        # This reference indicates that a DataTransformation is in the context of the
        # ClientServerOperation.
        self._firstToSecond: Optional["DataTransformation"] = None

    @property
    def first_to_second(self) -> Optional["DataTransformation"]:
        """Get firstToSecond (Pythonic accessor)."""
        return self._firstToSecond

    @first_to_second.setter
    def first_to_second(self, value: Optional["DataTransformation"]) -> None:
        """
        Set firstToSecond with validation.

        Args:
            value: The firstToSecond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstToSecond = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"firstToSecond must be DataTransformation or None, got {type(value).__name__}"
            )
        self._firstToSecond = value
        # Second to-be-mapped ClientServerOperation of a Client.
        self._second: Optional["ClientServerOperation"] = None

    @property
    def second(self) -> Optional["ClientServerOperation"]:
        """Get second (Pythonic accessor)."""
        return self._second

    @second.setter
    def second(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set second with validation.

        Args:
            value: The second to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._second = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"second must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._second = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getFirstOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for firstOperation.

        Returns:
            The firstOperation value

        Note:
            Delegates to first_operation property (CODING_RULE_V2_00017)
        """
        return self.first_operation  # Delegates to property

    def setFirstOperation(self, value: "ClientServerOperation") -> "ClientServerOperationMapping":
        """
        AUTOSAR-compliant setter for firstOperation with method chaining.

        Args:
            value: The firstOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_operation property setter (gets validation automatically)
        """
        self.first_operation = value  # Delegates to property setter
        return self

    def getFirstToSecond(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for firstToSecond.

        Returns:
            The firstToSecond value

        Note:
            Delegates to first_to_second property (CODING_RULE_V2_00017)
        """
        return self.first_to_second  # Delegates to property

    def setFirstToSecond(self, value: "DataTransformation") -> "ClientServerOperationMapping":
        """
        AUTOSAR-compliant setter for firstToSecond with method chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_to_second property setter (gets validation automatically)
        """
        self.first_to_second = value  # Delegates to property setter
        return self

    def getSecond(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for second.

        Returns:
            The second value

        Note:
            Delegates to second property (CODING_RULE_V2_00017)
        """
        return self.second  # Delegates to property

    def setSecond(self, value: "ClientServerOperation") -> "ClientServerOperationMapping":
        """
        AUTOSAR-compliant setter for second with method chaining.

        Args:
            value: The second to set

        Returns:
            self for method chaining

        Note:
            Delegates to second property setter (gets validation automatically)
        """
        self.second = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_operation(self, value: Optional["ClientServerOperation"]) -> "ClientServerOperationMapping":
        """
        Set firstOperation and return self for chaining.

        Args:
            value: The firstOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_operation("value")
        """
        self.first_operation = value  # Use property setter (gets validation)
        return self

    def with_first_to_second(self, value: Optional["DataTransformation"]) -> "ClientServerOperationMapping":
        """
        Set firstToSecond and return self for chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_to_second("value")
        """
        self.first_to_second = value  # Use property setter (gets validation)
        return self

    def with_second(self, value: Optional["ClientServerOperation"]) -> "ClientServerOperationMapping":
        """
        Set second and return self for chaining.

        Args:
            value: The second to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second("value")
        """
        self.second = value  # Use property setter (gets validation)
        return self
