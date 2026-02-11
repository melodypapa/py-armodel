
from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation import (
    GeneralAnnotation,
)

    RefType,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """
    that the "server" in the name of this meta-class is not meant to restrict
    the usage to ClientServer Interfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 156, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In case of a SET operation, the age will be interpreted as in a GET operation
        # (input) it specifies the the signal within the IoHwAbstraction Layer.
        self._age: Optional["MultidimensionalTime"] = None

    @property
    def age(self) -> Optional["MultidimensionalTime"]:
        """Get age (Pythonic accessor)."""
        return self._age

    @age.setter
    def age(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set age with validation.

        Args:
            value: The age to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._age = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"age must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._age = value
        self._argument: RefType = None

    @property
    def argument(self) -> RefType:
        """Get argument (Pythonic accessor)."""
        return self._argument

    @argument.setter
    def argument(self, value: RefType) -> None:
        """
        Set argument with validation.

        Args:
            value: The argument to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._argument = None
            return

        self._argument = value
        # well as the data-elements type, (2ˆdatatypelength - 1).
        self._bswResolution: Optional["Float"] = None

    @property
    def bsw_resolution(self) -> Optional["Float"]:
        """Get bswResolution (Pythonic accessor)."""
        return self._bswResolution

    @bsw_resolution.setter
    def bsw_resolution(self, value: Optional["Float"]) -> None:
        """
        Set bswResolution with validation.

        Args:
            value: The bswResolution to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswResolution = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"bswResolution must be Float or None, got {type(value).__name__}"
            )
        self._bswResolution = value
        self._dataElement: RefType = None

    @property
    def data_element(self) -> RefType:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: RefType) -> None:
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

        self._dataElement = value
        # If it is enabled, IoHwAbstraction layer will monitor the result of the issue
                # an diagnostic signal.
        # This means an additional client-server port has to be can use this
                # information to cross-check each data-element in a SET operation with an
                # additional port is created port monitors a failure in the to be of the
                # IoHwAbstraction referenced port has to be another port of the or Sensor
                # Component.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._failure: RefType = None

    @property
    def failure(self) -> RefType:
        """Get failure (Pythonic accessor)."""
        return self._failure

    @failure.setter
    def failure(self, value: RefType) -> None:
        """
        Set failure with validation.

        Args:
            value: The failure to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._failure = None
            return

        self._failure = value
        # the signal in the IoHw that no modification of the signal has This is the
        # default value debounceData the signal is a mean value waitTimeData the signal
        # is delivered by a GET operation certain amount of time.
        self._filtering: Optional["FilterDebouncingEnum"] = None

    @property
    def filtering(self) -> Optional["FilterDebouncingEnum"]:
        """Get filtering (Pythonic accessor)."""
        return self._filtering

    @filtering.setter
    def filtering(self, value: Optional["FilterDebouncingEnum"]) -> None:
        """
        Set filtering with validation.

        Args:
            value: The filtering to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filtering = None
            return

        if not isinstance(value, FilterDebouncingEnum):
            raise TypeError(
                f"filtering must be FilterDebouncingEnum or None, got {type(value).__name__}"
            )
        self._filtering = value
        # VariableDataPrototype used to generate pulse test sequences using the.
        self._pulseTest: Optional["PulseTestEnum"] = None

    @property
    def pulse_test(self) -> Optional["PulseTestEnum"]:
        """Get pulseTest (Pythonic accessor)."""
        return self._pulseTest

    @pulse_test.setter
    def pulse_test(self, value: Optional["PulseTestEnum"]) -> None:
        """
        Set pulseTest with validation.

        Args:
            value: The pulseTest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pulseTest = None
            return

        if not isinstance(value, PulseTestEnum):
            raise TypeError(
                f"pulseTest must be PulseTestEnum or None, got {type(value).__name__}"
            )
        self._pulseTest = value
        self._trigger: RefType = None

    @property
    def trigger(self) -> RefType:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: RefType) -> None:
        """
        Set trigger with validation.

        Args:
            value: The trigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAge(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for age.

        Returns:
            The age value

        Note:
            Delegates to age property (CODING_RULE_V2_00017)
        """
        return self.age  # Delegates to property

    def setAge(self, value: "MultidimensionalTime") -> IoHwAbstractionServerAnnotation:
        """
        AUTOSAR-compliant setter for age with method chaining.

        Args:
            value: The age to set

        Returns:
            self for method chaining

        Note:
            Delegates to age property setter (gets validation automatically)
        """
        self.age = value  # Delegates to property setter
        return self

    def getArgument(self) -> RefType:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def setArgument(self, value: RefType) -> IoHwAbstractionServerAnnotation:
        """
        AUTOSAR-compliant setter for argument with method chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Note:
            Delegates to argument property setter (gets validation automatically)
        """
        self.argument = value  # Delegates to property setter
        return self

    def getBswResolution(self) -> "Float":
        """
        AUTOSAR-compliant getter for bswResolution.

        Returns:
            The bswResolution value

        Note:
            Delegates to bsw_resolution property (CODING_RULE_V2_00017)
        """
        return self.bsw_resolution  # Delegates to property

    def setBswResolution(self, value: "Float") -> IoHwAbstractionServerAnnotation:
        """
        AUTOSAR-compliant setter for bswResolution with method chaining.

        Args:
            value: The bswResolution to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_resolution property setter (gets validation automatically)
        """
        self.bsw_resolution = value  # Delegates to property setter
        return self

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> IoHwAbstractionServerAnnotation:
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

    def getFailure(self) -> RefType:
        """
        AUTOSAR-compliant getter for failure.

        Returns:
            The failure value

        Note:
            Delegates to failure property (CODING_RULE_V2_00017)
        """
        return self.failure  # Delegates to property

    def setFailure(self, value: RefType) -> IoHwAbstractionServerAnnotation:
        """
        AUTOSAR-compliant setter for failure with method chaining.

        Args:
            value: The failure to set

        Returns:
            self for method chaining

        Note:
            Delegates to failure property setter (gets validation automatically)
        """
        self.failure = value  # Delegates to property setter
        return self

    def getFiltering(self) -> "FilterDebouncingEnum":
        """
        AUTOSAR-compliant getter for filtering.

        Returns:
            The filtering value

        Note:
            Delegates to filtering property (CODING_RULE_V2_00017)
        """
        return self.filtering  # Delegates to property

    def setFiltering(self, value: "FilterDebouncingEnum") -> IoHwAbstractionServerAnnotation:
        """
        AUTOSAR-compliant setter for filtering with method chaining.

        Args:
            value: The filtering to set

        Returns:
            self for method chaining

        Note:
            Delegates to filtering property setter (gets validation automatically)
        """
        self.filtering = value  # Delegates to property setter
        return self

    def getPulseTest(self) -> "PulseTestEnum":
        """
        AUTOSAR-compliant getter for pulseTest.

        Returns:
            The pulseTest value

        Note:
            Delegates to pulse_test property (CODING_RULE_V2_00017)
        """
        return self.pulse_test  # Delegates to property

    def setPulseTest(self, value: "PulseTestEnum") -> IoHwAbstractionServerAnnotation:
        """
        AUTOSAR-compliant setter for pulseTest with method chaining.

        Args:
            value: The pulseTest to set

        Returns:
            self for method chaining

        Note:
            Delegates to pulse_test property setter (gets validation automatically)
        """
        self.pulse_test = value  # Delegates to property setter
        return self

    def getTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: RefType) -> IoHwAbstractionServerAnnotation:
        """
        AUTOSAR-compliant setter for trigger with method chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_age(self, value: Optional["MultidimensionalTime"]) -> IoHwAbstractionServerAnnotation:
        """
        Set age and return self for chaining.

        Args:
            value: The age to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_age("value")
        """
        self.age = value  # Use property setter (gets validation)
        return self

    def with_argument(self, value: Optional[RefType]) -> IoHwAbstractionServerAnnotation:
        """
        Set argument and return self for chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_bsw_resolution(self, value: Optional["Float"]) -> IoHwAbstractionServerAnnotation:
        """
        Set bswResolution and return self for chaining.

        Args:
            value: The bswResolution to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_resolution("value")
        """
        self.bsw_resolution = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional[RefType]) -> IoHwAbstractionServerAnnotation:
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

    def with_failure(self, value: Optional[RefType]) -> IoHwAbstractionServerAnnotation:
        """
        Set failure and return self for chaining.

        Args:
            value: The failure to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_failure("value")
        """
        self.failure = value  # Use property setter (gets validation)
        return self

    def with_filtering(self, value: Optional["FilterDebouncingEnum"]) -> IoHwAbstractionServerAnnotation:
        """
        Set filtering and return self for chaining.

        Args:
            value: The filtering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filtering("value")
        """
        self.filtering = value  # Use property setter (gets validation)
        return self

    def with_pulse_test(self, value: Optional["PulseTestEnum"]) -> IoHwAbstractionServerAnnotation:
        """
        Set pulseTest and return self for chaining.

        Args:
            value: The pulseTest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pulse_test("value")
        """
        self.pulse_test = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional[RefType]) -> IoHwAbstractionServerAnnotation:
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self
