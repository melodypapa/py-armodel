from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    EcucAbstractExternalReferenceDef,
    String,
)


class EcucInstanceReferenceDef(EcucAbstractExternalReferenceDef):
    """
    Specify a reference to an XML description of an entity described in another
    AUTOSAR template using the INSTANCE REFERENCE semantics.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucInstanceReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 77, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The context in the AUTOSAR Metamodel to which’ this is allowed to point to.
        self._destination: Optional["String"] = None

    @property
    def destination(self) -> Optional["String"]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional["String"]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"destination must be String or None, got {type(value).__name__}"
            )
        self._destination = value
        # The type in the AUTOSAR Metamodel to which’ instance is allowed to point to.
        self._destinationType: Optional["String"] = None

    @property
    def destination_type(self) -> Optional["String"]:
        """Get destinationType (Pythonic accessor)."""
        return self._destinationType

    @destination_type.setter
    def destination_type(self, value: Optional["String"]) -> None:
        """
        Set destinationType with validation.

        Args:
            value: The destinationType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationType = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"destinationType must be String or None, got {type(value).__name__}"
            )
        self._destinationType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> "String":
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: "String") -> "EcucInstanceReferenceDef":
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    def getDestinationType(self) -> "String":
        """
        AUTOSAR-compliant getter for destinationType.

        Returns:
            The destinationType value

        Note:
            Delegates to destination_type property (CODING_RULE_V2_00017)
        """
        return self.destination_type  # Delegates to property

    def setDestinationType(self, value: "String") -> "EcucInstanceReferenceDef":
        """
        AUTOSAR-compliant setter for destinationType with method chaining.

        Args:
            value: The destinationType to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_type property setter (gets validation automatically)
        """
        self.destination_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination(self, value: Optional["String"]) -> "EcucInstanceReferenceDef":
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self

    def with_destination_type(self, value: Optional["String"]) -> "EcucInstanceReferenceDef":
        """
        Set destinationType and return self for chaining.

        Args:
            value: The destinationType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_type("value")
        """
        self.destination_type = value  # Use property setter (gets validation)
        return self
