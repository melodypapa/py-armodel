from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DdsResourceLimits(ARObject):
    """
    Describes the DDS RESOURCE_LIMITS QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsResourceLimits

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 537, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "RESOURCE_LIMITS" chapter of DDS.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxInstances: Optional["PositiveInteger"] = None

    @property
    def max_instances(self) -> Optional["PositiveInteger"]:
        """Get maxInstances (Pythonic accessor)."""
        return self._maxInstances

    @max_instances.setter
    def max_instances(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxInstances with validation.

        Args:
            value: The maxInstances to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxInstances = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxInstances must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxInstances = value
        # See "RESOURCE_LIMITS" chapter of DDS.
        self._maxSamples: Optional["PositiveInteger"] = None

    @property
    def max_samples(self) -> Optional["PositiveInteger"]:
        """Get maxSamples (Pythonic accessor)."""
        return self._maxSamples

    @max_samples.setter
    def max_samples(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSamples with validation.

        Args:
            value: The maxSamples to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSamples = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxSamples must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxSamples = value
        # See "RESOURCE_LIMITS" chapter of DDS.
        self._maxSamplesPerInstance: Optional["PositiveInteger"] = None

    @property
    def max_samples_per_instance(self) -> Optional["PositiveInteger"]:
        """Get maxSamplesPerInstance (Pythonic accessor)."""
        return self._maxSamplesPerInstance

    @max_samples_per_instance.setter
    def max_samples_per_instance(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSamplesPerInstance with validation.

        Args:
            value: The maxSamplesPerInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSamplesPerInstance = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxSamplesPerInstance must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxSamplesPerInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxInstances(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxInstances.

        Returns:
            The maxInstances value

        Note:
            Delegates to max_instances property (CODING_RULE_V2_00017)
        """
        return self.max_instances  # Delegates to property

    def setMaxInstances(self, value: "PositiveInteger") -> "DdsResourceLimits":
        """
        AUTOSAR-compliant setter for maxInstances with method chaining.

        Args:
            value: The maxInstances to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_instances property setter (gets validation automatically)
        """
        self.max_instances = value  # Delegates to property setter
        return self

    def getMaxSamples(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSamples.

        Returns:
            The maxSamples value

        Note:
            Delegates to max_samples property (CODING_RULE_V2_00017)
        """
        return self.max_samples  # Delegates to property

    def setMaxSamples(self, value: "PositiveInteger") -> "DdsResourceLimits":
        """
        AUTOSAR-compliant setter for maxSamples with method chaining.

        Args:
            value: The maxSamples to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_samples property setter (gets validation automatically)
        """
        self.max_samples = value  # Delegates to property setter
        return self

    def getMaxSamplesPerInstance(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSamplesPerInstance.

        Returns:
            The maxSamplesPerInstance value

        Note:
            Delegates to max_samples_per_instance property (CODING_RULE_V2_00017)
        """
        return self.max_samples_per_instance  # Delegates to property

    def setMaxSamplesPerInstance(self, value: "PositiveInteger") -> "DdsResourceLimits":
        """
        AUTOSAR-compliant setter for maxSamplesPerInstance with method chaining.

        Args:
            value: The maxSamplesPerInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_samples_per_instance property setter (gets validation automatically)
        """
        self.max_samples_per_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_instances(self, value: Optional["PositiveInteger"]) -> "DdsResourceLimits":
        """
        Set maxInstances and return self for chaining.

        Args:
            value: The maxInstances to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_instances("value")
        """
        self.max_instances = value  # Use property setter (gets validation)
        return self

    def with_max_samples(self, value: Optional["PositiveInteger"]) -> "DdsResourceLimits":
        """
        Set maxSamples and return self for chaining.

        Args:
            value: The maxSamples to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_samples("value")
        """
        self.max_samples = value  # Use property setter (gets validation)
        return self

    def with_max_samples_per_instance(self, value: Optional["PositiveInteger"]) -> "DdsResourceLimits":
        """
        Set maxSamplesPerInstance and return self for chaining.

        Args:
            value: The maxSamplesPerInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_samples_per_instance("value")
        """
        self.max_samples_per_instance = value  # Use property setter (gets validation)
        return self
