from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TextTableMapping(ARObject):
    """
    Defines the mapping of two DataPrototypes typed by AutosarDataTypes that
    refer to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or
    BITFIELD_TEXTTABLE.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 145, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 230, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute can be used to support the mapping of bit to bit field,
        # boolean values to bit fields, and vice attribute defines the bit mask for the
        # second the TextTableMapping.
        self._bitfieldTextTable: Optional["PositiveInteger"] = None

    @property
    def bitfield_text_table(self) -> Optional["PositiveInteger"]:
        """Get bitfieldTextTable (Pythonic accessor)."""
        return self._bitfieldTextTable

    @bitfield_text_table.setter
    def bitfield_text_table(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bitfieldTextTable with validation.

        Args:
            value: The bitfieldTextTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitfieldTextTable = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bitfieldTextTable must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._bitfieldTextTable = value
        # If identicalMapping is set == true the values of the two DataPrototypes do
        # not need any conversion of.
        self._identical: Optional["Boolean"] = None

    @property
    def identical(self) -> Optional["Boolean"]:
        """Get identical (Pythonic accessor)."""
        return self._identical

    @identical.setter
    def identical(self, value: Optional["Boolean"]) -> None:
        """
        Set identical with validation.

        Args:
            value: The identical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identical = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"identical must be Boolean or None, got {type(value).__name__}"
            )
        self._identical = value
        # Specifies the conversion direction for which the TextTable is applicable.
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
        # Defines a pair of values which are translated into each.
        self._valuePair: List["TextTableValuePair"] = []

    @property
    def value_pair(self) -> List["TextTableValuePair"]:
        """Get valuePair (Pythonic accessor)."""
        return self._valuePair

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitfieldTextTable(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bitfieldTextTable.

        Returns:
            The bitfieldTextTable value

        Note:
            Delegates to bitfield_text_table property (CODING_RULE_V2_00017)
        """
        return self.bitfield_text_table  # Delegates to property

    def setBitfieldTextTable(self, value: "PositiveInteger") -> "TextTableMapping":
        """
        AUTOSAR-compliant setter for bitfieldTextTable with method chaining.

        Args:
            value: The bitfieldTextTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to bitfield_text_table property setter (gets validation automatically)
        """
        self.bitfield_text_table = value  # Delegates to property setter
        return self

    def getIdentical(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for identical.

        Returns:
            The identical value

        Note:
            Delegates to identical property (CODING_RULE_V2_00017)
        """
        return self.identical  # Delegates to property

    def setIdentical(self, value: "Boolean") -> "TextTableMapping":
        """
        AUTOSAR-compliant setter for identical with method chaining.

        Args:
            value: The identical to set

        Returns:
            self for method chaining

        Note:
            Delegates to identical property setter (gets validation automatically)
        """
        self.identical = value  # Delegates to property setter
        return self

    def getMapping(self) -> RefType:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    def setMapping(self, value: RefType) -> "TextTableMapping":
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

    def getValuePair(self) -> List["TextTableValuePair"]:
        """
        AUTOSAR-compliant getter for valuePair.

        Returns:
            The valuePair value

        Note:
            Delegates to value_pair property (CODING_RULE_V2_00017)
        """
        return self.value_pair  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bitfield_text_table(self, value: Optional["PositiveInteger"]) -> "TextTableMapping":
        """
        Set bitfieldTextTable and return self for chaining.

        Args:
            value: The bitfieldTextTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bitfield_text_table("value")
        """
        self.bitfield_text_table = value  # Use property setter (gets validation)
        return self

    def with_identical(self, value: Optional["Boolean"]) -> "TextTableMapping":
        """
        Set identical and return self for chaining.

        Args:
            value: The identical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identical("value")
        """
        self.identical = value  # Use property setter (gets validation)
        return self

    def with_mapping(self, value: Optional[RefType]) -> "TextTableMapping":
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
