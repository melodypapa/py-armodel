from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticDataElement,
    DiagnosticMapping,
    NameToken,
)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    """
    This represents the ability to define the nature of a data access for a
    DiagnosticDataElement in the Dem.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping::DiagnosticDemProvidedDataMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 255, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the DiagnosticDataElement for which the further qualified by
        # the DiagnosticDemProvided.
        self._dataElement: Optional["DiagnosticDataElement"] = None

    @property
    def data_element(self) -> Optional["DiagnosticDataElement"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"dataElement must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._dataElement = value
        # This represents the ability to further specify the access Dem.
        self._dataProvider: Optional["NameToken"] = None

    @property
    def data_provider(self) -> Optional["NameToken"]:
        """Get dataProvider (Pythonic accessor)."""
        return self._dataProvider

    @data_provider.setter
    def data_provider(self, value: Optional["NameToken"]) -> None:
        """
        Set dataProvider with validation.

        Args:
            value: The dataProvider to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataProvider = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"dataProvider must be NameToken or None, got {type(value).__name__}"
            )
        self._dataProvider = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticDemProvidedDataMapping":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getDataProvider(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for dataProvider.

        Returns:
            The dataProvider value

        Note:
            Delegates to data_provider property (CODING_RULE_V2_00017)
        """
        return self.data_provider  # Delegates to property

    def setDataProvider(self, value: "NameToken") -> "DiagnosticDemProvidedDataMapping":
        """
        AUTOSAR-compliant setter for dataProvider with method chaining.

        Args:
            value: The dataProvider to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_provider property setter (gets validation automatically)
        """
        self.data_provider = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticDemProvidedDataMapping":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_data_provider(self, value: Optional["NameToken"]) -> "DiagnosticDemProvidedDataMapping":
        """
        Set dataProvider and return self for chaining.

        Args:
            value: The dataProvider to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_provider("value")
        """
        self.data_provider = value  # Use property setter (gets validation)
        return self
