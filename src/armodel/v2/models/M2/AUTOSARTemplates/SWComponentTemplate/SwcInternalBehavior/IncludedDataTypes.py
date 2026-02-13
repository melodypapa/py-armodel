"""
AUTOSAR Package - IncludedDataTypes

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::IncludedDataTypes
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class IncludedDataTypeSet(ARObject):
    """
    An includedDataTypeSet declares that a set of AutosarDataType is used by a
    basic software module or a software component for its implementation and the
    AutosarDataType becomes part of the contract. This information is required
    if the AutosarDataType is not used for any DataPrototype owned by this
    software component or if the enumeration literals, lowerLimit and upperLimit
    constants shall be generated with a literalPrefix. The optional
    literalPrefix is used to add a common prefix on enumeration literals,
    lowerLimit and upper Limit constants created by the RTE.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::IncludedDataTypes::IncludedDataTypeSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 600, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AutosarDataType belonging to the includedDataTypeSet.
        self._dataType: List[AutosarDataType] = []

    @property
    def data_type(self) -> List[AutosarDataType]:
        """Get dataType (Pythonic accessor)."""
        return self._dataType
        # LiteralPrefix defines a common prefix for all AutosarData the
        # includedDataTypeSet to be added on lowerLimit and upperLimit constants the
        # RTE.
        self._literalPrefix: Optional["Identifier"] = None

    @property
    def literal_prefix(self) -> Optional["Identifier"]:
        """Get literalPrefix (Pythonic accessor)."""
        return self._literalPrefix

    @literal_prefix.setter
    def literal_prefix(self, value: Optional["Identifier"]) -> None:
        """
        Set literalPrefix with validation.

        Args:
            value: The literalPrefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._literalPrefix = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"literalPrefix must be Identifier or str or None, got {type(value).__name__}"
            )
        self._literalPrefix = value

    def with_data_type(self, value):
        """
        Set data_type and return self for chaining.

        Args:
            value: The data_type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_type("value")
        """
        self.data_type = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataType(self) -> List[AutosarDataType]:
        """
        AUTOSAR-compliant getter for dataType.

        Returns:
            The dataType value

        Note:
            Delegates to data_type property (CODING_RULE_V2_00017)
        """
        return self.data_type  # Delegates to property

    def getLiteralPrefix(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for literalPrefix.

        Returns:
            The literalPrefix value

        Note:
            Delegates to literal_prefix property (CODING_RULE_V2_00017)
        """
        return self.literal_prefix  # Delegates to property

    def setLiteralPrefix(self, value: "Identifier") -> IncludedDataTypeSet:
        """
        AUTOSAR-compliant setter for literalPrefix with method chaining.

        Args:
            value: The literalPrefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to literal_prefix property setter (gets validation automatically)
        """
        self.literal_prefix = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_literal_prefix(self, value: Optional["Identifier"]) -> IncludedDataTypeSet:
        """
        Set literalPrefix and return self for chaining.

        Args:
            value: The literalPrefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_literal_prefix("value")
        """
        self.literal_prefix = value  # Use property setter (gets validation)
        return self
