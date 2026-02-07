from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DdsReliability(ARObject):
    """
    Describes the DDS RELIABILITY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsReliability

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 534, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "RELIABILITY" chapter of DDS.
        self._reliabilityKind: Optional["DdsReliabilityKindEnum"] = None

    @property
    def reliability_kind(self) -> Optional["DdsReliabilityKindEnum"]:
        """Get reliabilityKind (Pythonic accessor)."""
        return self._reliabilityKind

    @reliability_kind.setter
    def reliability_kind(self, value: Optional["DdsReliabilityKindEnum"]) -> None:
        """
        Set reliabilityKind with validation.

        Args:
            value: The reliabilityKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reliabilityKind = None
            return

        if not isinstance(value, DdsReliabilityKindEnum):
            raise TypeError(
                f"reliabilityKind must be DdsReliabilityKindEnum or None, got {type(value).__name__}"
            )
        self._reliabilityKind = value
        # See "RELIABILITY" chapter of DDS.
        # given in seconds.
        self._reliabilityMax: Optional["Float"] = None

    @property
    def reliability_max(self) -> Optional["Float"]:
        """Get reliabilityMax (Pythonic accessor)."""
        return self._reliabilityMax

    @reliability_max.setter
    def reliability_max(self, value: Optional["Float"]) -> None:
        """
        Set reliabilityMax with validation.

        Args:
            value: The reliabilityMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reliabilityMax = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"reliabilityMax must be Float or None, got {type(value).__name__}"
            )
        self._reliabilityMax = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReliabilityKind(self) -> "DdsReliabilityKindEnum":
        """
        AUTOSAR-compliant getter for reliabilityKind.

        Returns:
            The reliabilityKind value

        Note:
            Delegates to reliability_kind property (CODING_RULE_V2_00017)
        """
        return self.reliability_kind  # Delegates to property

    def setReliabilityKind(self, value: "DdsReliabilityKindEnum") -> "DdsReliability":
        """
        AUTOSAR-compliant setter for reliabilityKind with method chaining.

        Args:
            value: The reliabilityKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to reliability_kind property setter (gets validation automatically)
        """
        self.reliability_kind = value  # Delegates to property setter
        return self

    def getReliabilityMax(self) -> "Float":
        """
        AUTOSAR-compliant getter for reliabilityMax.

        Returns:
            The reliabilityMax value

        Note:
            Delegates to reliability_max property (CODING_RULE_V2_00017)
        """
        return self.reliability_max  # Delegates to property

    def setReliabilityMax(self, value: "Float") -> "DdsReliability":
        """
        AUTOSAR-compliant setter for reliabilityMax with method chaining.

        Args:
            value: The reliabilityMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to reliability_max property setter (gets validation automatically)
        """
        self.reliability_max = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_reliability_kind(self, value: Optional["DdsReliabilityKindEnum"]) -> "DdsReliability":
        """
        Set reliabilityKind and return self for chaining.

        Args:
            value: The reliabilityKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reliability_kind("value")
        """
        self.reliability_kind = value  # Use property setter (gets validation)
        return self

    def with_reliability_max(self, value: Optional["Float"]) -> "DdsReliability":
        """
        Set reliabilityMax and return self for chaining.

        Args:
            value: The reliabilityMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reliability_max("value")
        """
        self.reliability_max = value  # Use property setter (gets validation)
        return self
