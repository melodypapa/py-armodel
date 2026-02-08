from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DataFilter
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)


class SignalServiceTranslationElementProps(Identifiable):
    """
    Defined translation properties for individual mapped elements.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation::SignalServiceTranslationElementProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 735, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the leaf element the SignalService apply to.
        self._element: RefType = None

    @property
    def element(self) -> RefType:
        """Get element (Pythonic accessor)."""
        return self._element

    @element.setter
    def element(self, value: RefType) -> None:
        """
        Set element with validation.

        Args:
            value: The element to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._element = None
            return

        self._element = value
        # Defines an optional filter to be applied during translation.
        self._filter: Optional["DataFilter"] = None

    @property
    def filter(self) -> Optional["DataFilter"]:
        """Get filter (Pythonic accessor)."""
        return self._filter

    @filter.setter
    def filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set filter with validation.

        Args:
            value: The filter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"filter must be DataFilter or None, got {type(value).__name__}"
            )
        self._filter = value
        # Defines whether the source element (which is mapped to referenced element)
        # triggers the sending of the.
        self._transmission: Optional["Boolean"] = None

    @property
    def transmission(self) -> Optional["Boolean"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["Boolean"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"transmission must be Boolean or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def setElement(self, value: RefType) -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for element with method chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Note:
            Delegates to element property setter (gets validation automatically)
        """
        self.element = value  # Delegates to property setter
        return self

    def getFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for filter.

        Returns:
            The filter value

        Note:
            Delegates to filter property (CODING_RULE_V2_00017)
        """
        return self.filter  # Delegates to property

    def setFilter(self, value: "DataFilter") -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for filter with method chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter property setter (gets validation automatically)
        """
        self.filter = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "Boolean") -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_element(self, value: Optional[RefType]) -> "SignalServiceTranslationElementProps":
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self

    def with_filter(self, value: Optional["DataFilter"]) -> "SignalServiceTranslationElementProps":
        """
        Set filter and return self for chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter("value")
        """
        self.filter = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["Boolean"]) -> "SignalServiceTranslationElementProps":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self
