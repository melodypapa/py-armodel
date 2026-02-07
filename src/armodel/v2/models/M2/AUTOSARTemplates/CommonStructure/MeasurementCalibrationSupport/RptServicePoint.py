from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RptServicePoint(Identifiable):
    """
    Description of a Service Point implemented for rapid prototyping.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptServicePoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 206, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Unique ID (Range: 0.
        # 65535) representing the service.
        self._serviceId: Optional["PositiveInteger"] = None

    @property
    def service_id(self) -> Optional["PositiveInteger"]:
        """Get serviceId (Pythonic accessor)."""
        return self._serviceId

    @service_id.setter
    def service_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set serviceId with validation.

        Args:
            value: The serviceId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"serviceId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._serviceId = value
        # Complete symbol of the function implementing the This symbol is used for
        # post-build hooking.
        self._symbol: Optional["CIdentifier"] = None

    @property
    def symbol(self) -> Optional["CIdentifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["CIdentifier"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"symbol must be CIdentifier or None, got {type(value).__name__}"
            )
        self._symbol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getServiceId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for serviceId.

        Returns:
            The serviceId value

        Note:
            Delegates to service_id property (CODING_RULE_V2_00017)
        """
        return self.service_id  # Delegates to property

    def setServiceId(self, value: "PositiveInteger") -> "RptServicePoint":
        """
        AUTOSAR-compliant setter for serviceId with method chaining.

        Args:
            value: The serviceId to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_id property setter (gets validation automatically)
        """
        self.service_id = value  # Delegates to property setter
        return self

    def getSymbol(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "CIdentifier") -> "RptServicePoint":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_service_id(self, value: Optional["PositiveInteger"]) -> "RptServicePoint":
        """
        Set serviceId and return self for chaining.

        Args:
            value: The serviceId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_id("value")
        """
        self.service_id = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["CIdentifier"]) -> "RptServicePoint":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self
