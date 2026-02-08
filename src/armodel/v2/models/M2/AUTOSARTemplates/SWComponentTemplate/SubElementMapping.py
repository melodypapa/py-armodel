from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SubElementMapping(ARObject):
    """
    This meta-class allows for the definition of mappings of elements of a
    composite data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 137, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first element referenced in the scope mapping.
        # atpVariation.
        self._firstElement: RefType = None

    @property
    def first_element(self) -> RefType:
        """Get firstElement (Pythonic accessor)."""
        return self._firstElement

    @first_element.setter
    def first_element(self, value: RefType) -> None:
        """
        Set firstElement with validation.

        Args:
            value: The firstElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstElement = None
            return

        self._firstElement = value
        # This represents the second element referenced in the the mapping.
        # atpVariation.
        self._secondElement: RefType = None

    @property
    def second_element(self) -> RefType:
        """Get secondElement (Pythonic accessor)."""
        return self._secondElement

    @second_element.setter
    def second_element(self, value: RefType) -> None:
        """
        Set secondElement with validation.

        Args:
            value: The secondElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondElement = None
            return

        self._secondElement = value
        # of a composite data type.
        self._textTable: RefType = None

    @property
    def text_table(self) -> RefType:
        """Get textTable (Pythonic accessor)."""
        return self._textTable

    @text_table.setter
    def text_table(self, value: RefType) -> None:
        """
        Set textTable with validation.

        Args:
            value: The textTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._textTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for firstElement.

        Returns:
            The firstElement value

        Note:
            Delegates to first_element property (CODING_RULE_V2_00017)
        """
        return self.first_element  # Delegates to property

    def setFirstElement(self, value: RefType) -> "SubElementMapping":
        """
        AUTOSAR-compliant setter for firstElement with method chaining.

        Args:
            value: The firstElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_element property setter (gets validation automatically)
        """
        self.first_element = value  # Delegates to property setter
        return self

    def getSecondElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for secondElement.

        Returns:
            The secondElement value

        Note:
            Delegates to second_element property (CODING_RULE_V2_00017)
        """
        return self.second_element  # Delegates to property

    def setSecondElement(self, value: RefType) -> "SubElementMapping":
        """
        AUTOSAR-compliant setter for secondElement with method chaining.

        Args:
            value: The secondElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_element property setter (gets validation automatically)
        """
        self.second_element = value  # Delegates to property setter
        return self

    def getTextTable(self) -> RefType:
        """
        AUTOSAR-compliant getter for textTable.

        Returns:
            The textTable value

        Note:
            Delegates to text_table property (CODING_RULE_V2_00017)
        """
        return self.text_table  # Delegates to property

    def setTextTable(self, value: RefType) -> "SubElementMapping":
        """
        AUTOSAR-compliant setter for textTable with method chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to text_table property setter (gets validation automatically)
        """
        self.text_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_element(self, value: Optional[RefType]) -> "SubElementMapping":
        """
        Set firstElement and return self for chaining.

        Args:
            value: The firstElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_element("value")
        """
        self.first_element = value  # Use property setter (gets validation)
        return self

    def with_second_element(self, value: Optional[RefType]) -> "SubElementMapping":
        """
        Set secondElement and return self for chaining.

        Args:
            value: The secondElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_element("value")
        """
        self.second_element = value  # Use property setter (gets validation)
        return self

    def with_text_table(self, value: RefType) -> "SubElementMapping":
        """
        Set textTable and return self for chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_text_table("value")
        """
        self.text_table = value  # Use property setter (gets validation)
        return self
