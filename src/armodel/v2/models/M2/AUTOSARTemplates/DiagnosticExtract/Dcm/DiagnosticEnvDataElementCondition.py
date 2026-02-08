from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition import DiagnosticEnvCompareCondition

    RefType,
)


class DiagnosticEnvDataElementCondition(DiagnosticEnvCompareCondition):
    """
    This meta-class represents the ability to formulate a diagnostic environment
    condition based on the value of a data element owned by the application
    software.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvDataElementCondition

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 85, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the definition of the compare which the value
        # taken from the application be compared.
        self._compareValue: Optional["ValueSpecification"] = None

    @property
    def compare_value(self) -> Optional["ValueSpecification"]:
        """Get compareValue (Pythonic accessor)."""
        return self._compareValue

    @compare_value.setter
    def compare_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set compareValue with validation.

        Args:
            value: The compareValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compareValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"compareValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._compareValue = value
        # by the application software on the platform.
        # by: DataPrototypeInSystem.
        self._dataPrototype: RefType = None

    @property
    def data_prototype(self) -> RefType:
        """Get dataPrototype (Pythonic accessor)."""
        return self._dataPrototype

    @data_prototype.setter
    def data_prototype(self, value: RefType) -> None:
        """
        Set dataPrototype with validation.

        Args:
            value: The dataPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPrototype = None
            return

        self._dataPrototype = value
        # Via this aggregation it is possible to describe the of the data that is
        # obtained from the application environmental condition.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.

        Args:
            value: The swDataDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompareValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for compareValue.

        Returns:
            The compareValue value

        Note:
            Delegates to compare_value property (CODING_RULE_V2_00017)
        """
        return self.compare_value  # Delegates to property

    def setCompareValue(self, value: "ValueSpecification") -> "DiagnosticEnvDataElementCondition":
        """
        AUTOSAR-compliant setter for compareValue with method chaining.

        Args:
            value: The compareValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to compare_value property setter (gets validation automatically)
        """
        self.compare_value = value  # Delegates to property setter
        return self

    def getDataPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataPrototype.

        Returns:
            The dataPrototype value

        Note:
            Delegates to data_prototype property (CODING_RULE_V2_00017)
        """
        return self.data_prototype  # Delegates to property

    def setDataPrototype(self, value: RefType) -> "DiagnosticEnvDataElementCondition":
        """
        AUTOSAR-compliant setter for dataPrototype with method chaining.

        Args:
            value: The dataPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_prototype property setter (gets validation automatically)
        """
        self.data_prototype = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "DiagnosticEnvDataElementCondition":
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compare_value(self, value: Optional["ValueSpecification"]) -> "DiagnosticEnvDataElementCondition":
        """
        Set compareValue and return self for chaining.

        Args:
            value: The compareValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compare_value("value")
        """
        self.compare_value = value  # Use property setter (gets validation)
        return self

    def with_data_prototype(self, value: Optional[RefType]) -> "DiagnosticEnvDataElementCondition":
        """
        Set dataPrototype and return self for chaining.

        Args:
            value: The dataPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_prototype("value")
        """
        self.data_prototype = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "DiagnosticEnvDataElementCondition":
        """
        Set swDataDef and return self for chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self
