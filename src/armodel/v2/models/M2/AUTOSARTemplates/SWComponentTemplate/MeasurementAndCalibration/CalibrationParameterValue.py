from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CalibrationParameterValue(ARObject):
    """
    further that in this case an explicit mapping of ValueSpecification is not
    implemented because calibration parameters are delivered back after the
    calibration phase.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::CalibrationParameter

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 478, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2007, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the initial value specification structured according
        # ApplicationDataType.
        self._applInitValue: Optional["ValueSpecification"] = None

    @property
    def appl_init_value(self) -> Optional["ValueSpecification"]:
        """Get applInitValue (Pythonic accessor)."""
        return self._applInitValue

    @appl_init_value.setter
    def appl_init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set applInitValue with validation.

        Args:
            value: The applInitValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applInitValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"applInitValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._applInitValue = value
        # This is the initial value specification structured according
        # ImplementationDataType.
        self._implInitValue: Optional["ValueSpecification"] = None

    @property
    def impl_init_value(self) -> Optional["ValueSpecification"]:
        """Get implInitValue (Pythonic accessor)."""
        return self._implInitValue

    @impl_init_value.setter
    def impl_init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set implInitValue with validation.

        Args:
            value: The implInitValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implInitValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"implInitValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._implInitValue = value
        # This represents the parameter that is initialized by the.
        self._initialized: Optional["FlatInstanceDescriptor"] = None

    @property
    def initialized(self) -> Optional["FlatInstanceDescriptor"]:
        """Get initialized (Pythonic accessor)."""
        return self._initialized

    @initialized.setter
    def initialized(self, value: Optional["FlatInstanceDescriptor"]) -> None:
        """
        Set initialized with validation.

        Args:
            value: The initialized to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialized = None
            return

        if not isinstance(value, FlatInstanceDescriptor):
            raise TypeError(
                f"initialized must be FlatInstanceDescriptor or None, got {type(value).__name__}"
            )
        self._initialized = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for applInitValue.

        Returns:
            The applInitValue value

        Note:
            Delegates to appl_init_value property (CODING_RULE_V2_00017)
        """
        return self.appl_init_value  # Delegates to property

    def setApplInitValue(self, value: "ValueSpecification") -> "CalibrationParameterValue":
        """
        AUTOSAR-compliant setter for applInitValue with method chaining.

        Args:
            value: The applInitValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to appl_init_value property setter (gets validation automatically)
        """
        self.appl_init_value = value  # Delegates to property setter
        return self

    def getImplInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for implInitValue.

        Returns:
            The implInitValue value

        Note:
            Delegates to impl_init_value property (CODING_RULE_V2_00017)
        """
        return self.impl_init_value  # Delegates to property

    def setImplInitValue(self, value: "ValueSpecification") -> "CalibrationParameterValue":
        """
        AUTOSAR-compliant setter for implInitValue with method chaining.

        Args:
            value: The implInitValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to impl_init_value property setter (gets validation automatically)
        """
        self.impl_init_value = value  # Delegates to property setter
        return self

    def getInitialized(self) -> "FlatInstanceDescriptor":
        """
        AUTOSAR-compliant getter for initialized.

        Returns:
            The initialized value

        Note:
            Delegates to initialized property (CODING_RULE_V2_00017)
        """
        return self.initialized  # Delegates to property

    def setInitialized(self, value: "FlatInstanceDescriptor") -> "CalibrationParameterValue":
        """
        AUTOSAR-compliant setter for initialized with method chaining.

        Args:
            value: The initialized to set

        Returns:
            self for method chaining

        Note:
            Delegates to initialized property setter (gets validation automatically)
        """
        self.initialized = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_appl_init_value(self, value: Optional["ValueSpecification"]) -> "CalibrationParameterValue":
        """
        Set applInitValue and return self for chaining.

        Args:
            value: The applInitValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_appl_init_value("value")
        """
        self.appl_init_value = value  # Use property setter (gets validation)
        return self

    def with_impl_init_value(self, value: Optional["ValueSpecification"]) -> "CalibrationParameterValue":
        """
        Set implInitValue and return self for chaining.

        Args:
            value: The implInitValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_impl_init_value("value")
        """
        self.impl_init_value = value  # Use property setter (gets validation)
        return self

    def with_initialized(self, value: Optional["FlatInstanceDescriptor"]) -> "CalibrationParameterValue":
        """
        Set initialized and return self for chaining.

        Args:
            value: The initialized to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initialized("value")
        """
        self.initialized = value  # Use property setter (gets validation)
        return self
