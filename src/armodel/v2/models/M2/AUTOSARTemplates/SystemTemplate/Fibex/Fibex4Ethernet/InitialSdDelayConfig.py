from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class InitialSdDelayConfig(ARObject):
    """
    This element is used to configure the offer behavior of the server and the
    find behavior on the client.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::InitialSdDelayConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 514, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Max Value in seconds to delay randomly the first offer (if by SdServerConfig)
        # or the transmission of a (if aggregated by SdClientConfig).
        self._initialDelayMax: Optional["TimeValue"] = None

    @property
    def initial_delay_max(self) -> Optional["TimeValue"]:
        """Get initialDelayMax (Pythonic accessor)."""
        return self._initialDelayMax

    @initial_delay_max.setter
    def initial_delay_max(self, value: Optional["TimeValue"]) -> None:
        """
        Set initialDelayMax with validation.

        Args:
            value: The initialDelayMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialDelayMax = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"initialDelayMax must be TimeValue or None, got {type(value).__name__}"
            )
        self._initialDelayMax = value
        # Min Value in seconds to delay randomly the first offer or transmission of a
        # find message (if aggregated by Sd.
        self._initialDelayMin: Optional["TimeValue"] = None

    @property
    def initial_delay_min(self) -> Optional["TimeValue"]:
        """Get initialDelayMin (Pythonic accessor)."""
        return self._initialDelayMin

    @initial_delay_min.setter
    def initial_delay_min(self, value: Optional["TimeValue"]) -> None:
        """
        Set initialDelayMin with validation.

        Args:
            value: The initialDelayMin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialDelayMin = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"initialDelayMin must be TimeValue or None, got {type(value).__name__}"
            )
        self._initialDelayMin = value
        # Describes the maximum amount of offer repetitions (if by SdServerConfig) or
        # the maximum amount repetitions (if aggregated by SdClientConfig).
        self._initial: Optional["PositiveInteger"] = None

    @property
    def initial(self) -> Optional["PositiveInteger"]:
        """Get initial (Pythonic accessor)."""
        return self._initial

    @initial.setter
    def initial(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set initial with validation.

        Args:
            value: The initial to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initial = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"initial must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._initial = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialDelayMax(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for initialDelayMax.

        Returns:
            The initialDelayMax value

        Note:
            Delegates to initial_delay_max property (CODING_RULE_V2_00017)
        """
        return self.initial_delay_max  # Delegates to property

    def setInitialDelayMax(self, value: "TimeValue") -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant setter for initialDelayMax with method chaining.

        Args:
            value: The initialDelayMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_delay_max property setter (gets validation automatically)
        """
        self.initial_delay_max = value  # Delegates to property setter
        return self

    def getInitialDelayMin(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for initialDelayMin.

        Returns:
            The initialDelayMin value

        Note:
            Delegates to initial_delay_min property (CODING_RULE_V2_00017)
        """
        return self.initial_delay_min  # Delegates to property

    def setInitialDelayMin(self, value: "TimeValue") -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant setter for initialDelayMin with method chaining.

        Args:
            value: The initialDelayMin to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_delay_min property setter (gets validation automatically)
        """
        self.initial_delay_min = value  # Delegates to property setter
        return self

    def getInitial(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for initial.

        Returns:
            The initial value

        Note:
            Delegates to initial property (CODING_RULE_V2_00017)
        """
        return self.initial  # Delegates to property

    def setInitial(self, value: "PositiveInteger") -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant setter for initial with method chaining.

        Args:
            value: The initial to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial property setter (gets validation automatically)
        """
        self.initial = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_delay_max(self, value: Optional["TimeValue"]) -> "InitialSdDelayConfig":
        """
        Set initialDelayMax and return self for chaining.

        Args:
            value: The initialDelayMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_delay_max("value")
        """
        self.initial_delay_max = value  # Use property setter (gets validation)
        return self

    def with_initial_delay_min(self, value: Optional["TimeValue"]) -> "InitialSdDelayConfig":
        """
        Set initialDelayMin and return self for chaining.

        Args:
            value: The initialDelayMin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_delay_min("value")
        """
        self.initial_delay_min = value  # Use property setter (gets validation)
        return self

    def with_initial(self, value: Optional["PositiveInteger"]) -> "InitialSdDelayConfig":
        """
        Set initial and return self for chaining.

        Args:
            value: The initial to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial("value")
        """
        self.initial = value  # Use property setter (gets validation)
        return self
