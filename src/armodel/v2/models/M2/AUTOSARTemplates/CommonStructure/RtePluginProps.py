from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class RtePluginProps(ARObject):
    """
    The properties of a communication graph with respect to the utilization of
    RTE Implementation Plug-in.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::RtePluginProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 971, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This associates a communication graph to a specific RTE Plug-in handling
        # cross Software Cluster.
        self._associated: Optional["EcucContainerValue"] = None

    @property
    def associated(self) -> Optional["EcucContainerValue"]:
        """Get associated (Pythonic accessor)."""
        return self._associated

    @associated.setter
    def associated(self, value: Optional["EcucContainerValue"]) -> None:
        """
        Set associated with validation.

        Args:
            value: The associated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._associated = None
            return

        if not isinstance(value, EcucContainerValue):
            raise TypeError(
                f"associated must be EcucContainerValue or None, got {type(value).__name__}"
            )
        self._associated = value
        # This associates a communication graph to a specific RTE Plug-in handling
        # local Software Cluster communication in a non-cluster ECU.
        self._associatedRte: Optional["EcucContainerValue"] = None

    @property
    def associated_rte(self) -> Optional["EcucContainerValue"]:
        """Get associatedRte (Pythonic accessor)."""
        return self._associatedRte

    @associated_rte.setter
    def associated_rte(self, value: Optional["EcucContainerValue"]) -> None:
        """
        Set associatedRte with validation.

        Args:
            value: The associatedRte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._associatedRte = None
            return

        if not isinstance(value, EcucContainerValue):
            raise TypeError(
                f"associatedRte must be EcucContainerValue or None, got {type(value).__name__}"
            )
        self._associatedRte = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssociated(self) -> "EcucContainerValue":
        """
        AUTOSAR-compliant getter for associated.

        Returns:
            The associated value

        Note:
            Delegates to associated property (CODING_RULE_V2_00017)
        """
        return self.associated  # Delegates to property

    def setAssociated(self, value: "EcucContainerValue") -> "RtePluginProps":
        """
        AUTOSAR-compliant setter for associated with method chaining.

        Args:
            value: The associated to set

        Returns:
            self for method chaining

        Note:
            Delegates to associated property setter (gets validation automatically)
        """
        self.associated = value  # Delegates to property setter
        return self

    def getAssociatedRte(self) -> "EcucContainerValue":
        """
        AUTOSAR-compliant getter for associatedRte.

        Returns:
            The associatedRte value

        Note:
            Delegates to associated_rte property (CODING_RULE_V2_00017)
        """
        return self.associated_rte  # Delegates to property

    def setAssociatedRte(self, value: "EcucContainerValue") -> "RtePluginProps":
        """
        AUTOSAR-compliant setter for associatedRte with method chaining.

        Args:
            value: The associatedRte to set

        Returns:
            self for method chaining

        Note:
            Delegates to associated_rte property setter (gets validation automatically)
        """
        self.associated_rte = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_associated(self, value: Optional["EcucContainerValue"]) -> "RtePluginProps":
        """
        Set associated and return self for chaining.

        Args:
            value: The associated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_associated("value")
        """
        self.associated = value  # Use property setter (gets validation)
        return self

    def with_associated_rte(self, value: Optional["EcucContainerValue"]) -> "RtePluginProps":
        """
        Set associatedRte and return self for chaining.

        Args:
            value: The associatedRte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_associated_rte("value")
        """
        self.associated_rte = value  # Use property setter (gets validation)
        return self
