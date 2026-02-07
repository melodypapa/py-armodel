from typing import Optional


class MeasuredStackUsage(StackUsage):
    """
    The stack usage has been measured.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage::MeasuredStackUsage

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 150, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The average stack usage measured.
        # Unit: byte.
        self._averageMemoryConsumption: Optional["PositiveInteger"] = None

    @property
    def average_memory_consumption(self) -> Optional["PositiveInteger"]:
        """Get averageMemoryConsumption (Pythonic accessor)."""
        return self._averageMemoryConsumption

    @average_memory_consumption.setter
    def average_memory_consumption(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set averageMemoryConsumption with validation.

        Args:
            value: The averageMemoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._averageMemoryConsumption = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"averageMemoryConsumption must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._averageMemoryConsumption = value
        # The maximum stack usage measured.
        # Unit: byte.
        self._maximumMemoryConsumption: Optional["PositiveInteger"] = None

    @property
    def maximum_memory_consumption(self) -> Optional["PositiveInteger"]:
        """Get maximumMemoryConsumption (Pythonic accessor)."""
        return self._maximumMemoryConsumption

    @maximum_memory_consumption.setter
    def maximum_memory_consumption(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maximumMemoryConsumption with validation.

        Args:
            value: The maximumMemoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumMemoryConsumption = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maximumMemoryConsumption must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maximumMemoryConsumption = value
        # The minimum stack usage measured.
        # Unit: byte.
        self._minimumMemoryConsumption: Optional["PositiveInteger"] = None

    @property
    def minimum_memory_consumption(self) -> Optional["PositiveInteger"]:
        """Get minimumMemoryConsumption (Pythonic accessor)."""
        return self._minimumMemoryConsumption

    @minimum_memory_consumption.setter
    def minimum_memory_consumption(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minimumMemoryConsumption with validation.

        Args:
            value: The minimumMemoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumMemoryConsumption = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minimumMemoryConsumption must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minimumMemoryConsumption = value
        # Description of the test pattern used to acquire the.
        self._testPattern: Optional["String"] = None

    @property
    def test_pattern(self) -> Optional["String"]:
        """Get testPattern (Pythonic accessor)."""
        return self._testPattern

    @test_pattern.setter
    def test_pattern(self, value: Optional["String"]) -> None:
        """
        Set testPattern with validation.

        Args:
            value: The testPattern to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._testPattern = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"testPattern must be String or None, got {type(value).__name__}"
            )
        self._testPattern = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAverageMemoryConsumption(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for averageMemoryConsumption.

        Returns:
            The averageMemoryConsumption value

        Note:
            Delegates to average_memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.average_memory_consumption  # Delegates to property

    def setAverageMemoryConsumption(self, value: "PositiveInteger") -> "MeasuredStackUsage":
        """
        AUTOSAR-compliant setter for averageMemoryConsumption with method chaining.

        Args:
            value: The averageMemoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to average_memory_consumption property setter (gets validation automatically)
        """
        self.average_memory_consumption = value  # Delegates to property setter
        return self

    def getMaximumMemoryConsumption(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maximumMemoryConsumption.

        Returns:
            The maximumMemoryConsumption value

        Note:
            Delegates to maximum_memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.maximum_memory_consumption  # Delegates to property

    def setMaximumMemoryConsumption(self, value: "PositiveInteger") -> "MeasuredStackUsage":
        """
        AUTOSAR-compliant setter for maximumMemoryConsumption with method chaining.

        Args:
            value: The maximumMemoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum_memory_consumption property setter (gets validation automatically)
        """
        self.maximum_memory_consumption = value  # Delegates to property setter
        return self

    def getMinimumMemoryConsumption(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minimumMemoryConsumption.

        Returns:
            The minimumMemoryConsumption value

        Note:
            Delegates to minimum_memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.minimum_memory_consumption  # Delegates to property

    def setMinimumMemoryConsumption(self, value: "PositiveInteger") -> "MeasuredStackUsage":
        """
        AUTOSAR-compliant setter for minimumMemoryConsumption with method chaining.

        Args:
            value: The minimumMemoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_memory_consumption property setter (gets validation automatically)
        """
        self.minimum_memory_consumption = value  # Delegates to property setter
        return self

    def getTestPattern(self) -> "String":
        """
        AUTOSAR-compliant getter for testPattern.

        Returns:
            The testPattern value

        Note:
            Delegates to test_pattern property (CODING_RULE_V2_00017)
        """
        return self.test_pattern  # Delegates to property

    def setTestPattern(self, value: "String") -> "MeasuredStackUsage":
        """
        AUTOSAR-compliant setter for testPattern with method chaining.

        Args:
            value: The testPattern to set

        Returns:
            self for method chaining

        Note:
            Delegates to test_pattern property setter (gets validation automatically)
        """
        self.test_pattern = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_average_memory_consumption(self, value: Optional["PositiveInteger"]) -> "MeasuredStackUsage":
        """
        Set averageMemoryConsumption and return self for chaining.

        Args:
            value: The averageMemoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_average_memory_consumption("value")
        """
        self.average_memory_consumption = value  # Use property setter (gets validation)
        return self

    def with_maximum_memory_consumption(self, value: Optional["PositiveInteger"]) -> "MeasuredStackUsage":
        """
        Set maximumMemoryConsumption and return self for chaining.

        Args:
            value: The maximumMemoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum_memory_consumption("value")
        """
        self.maximum_memory_consumption = value  # Use property setter (gets validation)
        return self

    def with_minimum_memory_consumption(self, value: Optional["PositiveInteger"]) -> "MeasuredStackUsage":
        """
        Set minimumMemoryConsumption and return self for chaining.

        Args:
            value: The minimumMemoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_memory_consumption("value")
        """
        self.minimum_memory_consumption = value  # Use property setter (gets validation)
        return self

    def with_test_pattern(self, value: Optional["String"]) -> "MeasuredStackUsage":
        """
        Set testPattern and return self for chaining.

        Args:
            value: The testPattern to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_test_pattern("value")
        """
        self.test_pattern = value  # Use property setter (gets validation)
        return self
