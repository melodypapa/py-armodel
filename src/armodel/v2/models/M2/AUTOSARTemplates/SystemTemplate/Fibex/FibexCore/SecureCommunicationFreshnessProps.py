from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SecureCommunicationFreshnessProps(Identifiable):
    """
    Freshness properties used to configure SecuredIPdus.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 370, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines a factor that specifies the time for the Freshness
                # Timestamp.
        # It holds a factor that specifies the concrete meaning Freshness Timestamp
                # increment by one on basis of.
        self._freshness: Optional["PositiveInteger"] = None

    @property
    def freshness(self) -> Optional["PositiveInteger"]:
        """Get freshness (Pythonic accessor)."""
        return self._freshness

    @freshness.setter
    def freshness(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set freshness with validation.

        Args:
            value: The freshness to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshness = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"freshness must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._freshness = value
        # This attribute defines the length in bits of the Freshness to be included in
                # the payload of the Secured I-PDU.
        # is specific to the least significant bits of the Counter.
        # If the attribute is 0 no is included in the Secured I-PDU.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._freshnessValue: Optional["PositiveInteger"] = None

    @property
    def freshness_value(self) -> Optional["PositiveInteger"]:
        """Get freshnessValue (Pythonic accessor)."""
        return self._freshnessValue

    @freshness_value.setter
    def freshness_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set freshnessValue with validation.

        Args:
            value: The freshnessValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshnessValue = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"freshnessValue must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._freshnessValue = value
        # This attribute specifies whether the Freshness Value is through individual
        # Freshness Counters or by a value is set to TRUE when Timestamps.
        self._useFreshness: Optional["Boolean"] = None

    @property
    def use_freshness(self) -> Optional["Boolean"]:
        """Get useFreshness (Pythonic accessor)."""
        return self._useFreshness

    @use_freshness.setter
    def use_freshness(self, value: Optional["Boolean"]) -> None:
        """
        Set useFreshness with validation.

        Args:
            value: The useFreshness to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useFreshness = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useFreshness must be Boolean or None, got {type(value).__name__}"
            )
        self._useFreshness = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFreshness(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for freshness.

        Returns:
            The freshness value

        Note:
            Delegates to freshness property (CODING_RULE_V2_00017)
        """
        return self.freshness  # Delegates to property

    def setFreshness(self, value: "PositiveInteger") -> "SecureCommunicationFreshnessProps":
        """
        AUTOSAR-compliant setter for freshness with method chaining.

        Args:
            value: The freshness to set

        Returns:
            self for method chaining

        Note:
            Delegates to freshness property setter (gets validation automatically)
        """
        self.freshness = value  # Delegates to property setter
        return self

    def getFreshnessValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for freshnessValue.

        Returns:
            The freshnessValue value

        Note:
            Delegates to freshness_value property (CODING_RULE_V2_00017)
        """
        return self.freshness_value  # Delegates to property

    def setFreshnessValue(self, value: "PositiveInteger") -> "SecureCommunicationFreshnessProps":
        """
        AUTOSAR-compliant setter for freshnessValue with method chaining.

        Args:
            value: The freshnessValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to freshness_value property setter (gets validation automatically)
        """
        self.freshness_value = value  # Delegates to property setter
        return self

    def getUseFreshness(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useFreshness.

        Returns:
            The useFreshness value

        Note:
            Delegates to use_freshness property (CODING_RULE_V2_00017)
        """
        return self.use_freshness  # Delegates to property

    def setUseFreshness(self, value: "Boolean") -> "SecureCommunicationFreshnessProps":
        """
        AUTOSAR-compliant setter for useFreshness with method chaining.

        Args:
            value: The useFreshness to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_freshness property setter (gets validation automatically)
        """
        self.use_freshness = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_freshness(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationFreshnessProps":
        """
        Set freshness and return self for chaining.

        Args:
            value: The freshness to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_freshness("value")
        """
        self.freshness = value  # Use property setter (gets validation)
        return self

    def with_freshness_value(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationFreshnessProps":
        """
        Set freshnessValue and return self for chaining.

        Args:
            value: The freshnessValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_freshness_value("value")
        """
        self.freshness_value = value  # Use property setter (gets validation)
        return self

    def with_use_freshness(self, value: Optional["Boolean"]) -> "SecureCommunicationFreshnessProps":
        """
        Set useFreshness and return self for chaining.

        Args:
            value: The useFreshness to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_freshness("value")
        """
        self.use_freshness = value  # Use property setter (gets validation)
        return self
