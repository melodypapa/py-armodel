from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DiagnosticAbstractParameter(ARObject, ABC):
    """
    This meta-class represents an abstract base class for modeling a diagnostic
    parameter.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticAbstractParameter

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 37, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticAbstractParameter:
            raise TypeError("DiagnosticAbstractParameter is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the bitOffset of the DiagnosticParameter.
        # of the bitOffset shall always be interpreted as the start of the enclosing
                # DiagnosticData or Diagnostic.
        self._bitOffset: Optional["PositiveInteger"] = None

    @property
    def bit_offset(self) -> Optional["PositiveInteger"]:
        """Get bitOffset (Pythonic accessor)."""
        return self._bitOffset

    @bit_offset.setter
    def bit_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bitOffset with validation.

        Args:
            value: The bitOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitOffset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bitOffset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._bitOffset = value
        # This represents the related dataElement of the Diagnostic atpVariation.
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
        # This attribute allows for the specification of the parameter information is
                # relevant if there is a gap between parameter and the following diagnostic the
                # tail of the telegram).
        # The unit is bit and shall be multiples of 8.
        self._parameterSize: Optional["PositiveInteger"] = None

    @property
    def parameter_size(self) -> Optional["PositiveInteger"]:
        """Get parameterSize (Pythonic accessor)."""
        return self._parameterSize

    @parameter_size.setter
    def parameter_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set parameterSize with validation.

        Args:
            value: The parameterSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameterSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"parameterSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._parameterSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bitOffset.

        Returns:
            The bitOffset value

        Note:
            Delegates to bit_offset property (CODING_RULE_V2_00017)
        """
        return self.bit_offset  # Delegates to property

    def setBitOffset(self, value: "PositiveInteger") -> "DiagnosticAbstractParameter":
        """
        AUTOSAR-compliant setter for bitOffset with method chaining.

        Args:
            value: The bitOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to bit_offset property setter (gets validation automatically)
        """
        self.bit_offset = value  # Delegates to property setter
        return self

    def getDataElement(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticAbstractParameter":
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

    def getParameterSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for parameterSize.

        Returns:
            The parameterSize value

        Note:
            Delegates to parameter_size property (CODING_RULE_V2_00017)
        """
        return self.parameter_size  # Delegates to property

    def setParameterSize(self, value: "PositiveInteger") -> "DiagnosticAbstractParameter":
        """
        AUTOSAR-compliant setter for parameterSize with method chaining.

        Args:
            value: The parameterSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter_size property setter (gets validation automatically)
        """
        self.parameter_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_offset(self, value: Optional["PositiveInteger"]) -> "DiagnosticAbstractParameter":
        """
        Set bitOffset and return self for chaining.

        Args:
            value: The bitOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bit_offset("value")
        """
        self.bit_offset = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticAbstractParameter":
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

    def with_parameter_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticAbstractParameter":
        """
        Set parameterSize and return self for chaining.

        Args:
            value: The parameterSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter_size("value")
        """
        self.parameter_size = value  # Use property setter (gets validation)
        return self
