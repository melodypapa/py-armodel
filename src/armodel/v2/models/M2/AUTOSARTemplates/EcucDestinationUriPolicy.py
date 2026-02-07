from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EcucDestinationUriPolicy(ARObject):
    """
    The EcucDestinationUriPolicy describes the EcucContainerDef that will be
    targeted by EcucUriReference Defs. The type of the description is dependent
    of the destinationUriNestingContract attribute.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDestinationUriPolicy

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 83, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Description of the targetContainer in case that the set to targetContainer.
        # In cases the subContainers of the target container here.
        self._container: List["EcucContainerDef"] = []

    @property
    def container(self) -> List["EcucContainerDef"]:
        """Get container (Pythonic accessor)."""
        return self._container
        # This attribute defines how the referenced target Ecuc ContainerDef is
        # described.
        self._destinationUri: Optional["EcucDestinationUri"] = None

    @property
    def destination_uri(self) -> Optional["EcucDestinationUri"]:
        """Get destinationUri (Pythonic accessor)."""
        return self._destinationUri

    @destination_uri.setter
    def destination_uri(self, value: Optional["EcucDestinationUri"]) -> None:
        """
        Set destinationUri with validation.

        Args:
            value: The destinationUri to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationUri = None
            return

        if not isinstance(value, EcucDestinationUri):
            raise TypeError(
                f"destinationUri must be EcucDestinationUri or None, got {type(value).__name__}"
            )
        self._destinationUri = value
        # Description of parameters that are contained in the target.
        self._parameter: List["EcucParameterDef"] = []

    @property
    def parameter(self) -> List["EcucParameterDef"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter
        # Description of references that are contained in the target.
        self._reference: List[RefType] = []

    @property
    def reference(self) -> List[RefType]:
        """Get reference (Pythonic accessor)."""
        return self._reference

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContainer(self) -> List["EcucContainerDef"]:
        """
        AUTOSAR-compliant getter for container.

        Returns:
            The container value

        Note:
            Delegates to container property (CODING_RULE_V2_00017)
        """
        return self.container  # Delegates to property

    def getDestinationUri(self) -> "EcucDestinationUri":
        """
        AUTOSAR-compliant getter for destinationUri.

        Returns:
            The destinationUri value

        Note:
            Delegates to destination_uri property (CODING_RULE_V2_00017)
        """
        return self.destination_uri  # Delegates to property

    def setDestinationUri(self, value: "EcucDestinationUri") -> "EcucDestinationUriPolicy":
        """
        AUTOSAR-compliant setter for destinationUri with method chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_uri property setter (gets validation automatically)
        """
        self.destination_uri = value  # Delegates to property setter
        return self

    def getParameter(self) -> List["EcucParameterDef"]:
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def getReference(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for reference.

        Returns:
            The reference value

        Note:
            Delegates to reference property (CODING_RULE_V2_00017)
        """
        return self.reference  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_uri(self, value: Optional["EcucDestinationUri"]) -> "EcucDestinationUriPolicy":
        """
        Set destinationUri and return self for chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_uri("value")
        """
        self.destination_uri = value  # Use property setter (gets validation)
        return self
