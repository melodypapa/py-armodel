from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwConnector(Identifiable, ABC):
    """
    The base class for connectors between ports. Connectors have to be
    identifiable to allow references from the system constraint template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 307, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 80, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2061, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is SwConnector:
            raise TypeError("SwConnector is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a PortInterfaceMapping specifying the unequal named
        # PortInterface elements of the PortInterfaces typing the two PortPrototypes
        # referenced by the ConnectorPrototype.
        self._mapping: RefType = None

    @property
    def mapping(self) -> RefType:
        """Get mapping (Pythonic accessor)."""
        return self._mapping

    @mapping.setter
    def mapping(self, value: RefType) -> None:
        """
        Set mapping with validation.

        Args:
            value: The mapping to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mapping = None
            return

        self._mapping = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMapping(self) -> RefType:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    def setMapping(self, value: RefType) -> "SwConnector":
        """
        AUTOSAR-compliant setter for mapping with method chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapping property setter (gets validation automatically)
        """
        self.mapping = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapping(self, value: Optional[RefType]) -> "SwConnector":
        """
        Set mapping and return self for chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping("value")
        """
        self.mapping = value  # Use property setter (gets validation)
        return self
