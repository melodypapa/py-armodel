from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DdsLiveliness(ARObject):
    """
    Describes the DDS LIVELINESS QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsLiveliness

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 534, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "LIVELINESS" chapter of DDS.
        # given in seconds.
        self._livelinessLease: Optional["Float"] = None

    @property
    def liveliness_lease(self) -> Optional["Float"]:
        """Get livelinessLease (Pythonic accessor)."""
        return self._livelinessLease

    @liveliness_lease.setter
    def liveliness_lease(self, value: Optional["Float"]) -> None:
        """
        Set livelinessLease with validation.

        Args:
            value: The livelinessLease to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._livelinessLease = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"livelinessLease must be Float or None, got {type(value).__name__}"
            )
        self._livelinessLease = value
        # See "LIVELINESS" chapter of DDS.
        self._livenessKind: Optional["DdsLivenessKindEnum"] = None

    @property
    def liveness_kind(self) -> Optional["DdsLivenessKindEnum"]:
        """Get livenessKind (Pythonic accessor)."""
        return self._livenessKind

    @liveness_kind.setter
    def liveness_kind(self, value: Optional["DdsLivenessKindEnum"]) -> None:
        """
        Set livenessKind with validation.

        Args:
            value: The livenessKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._livenessKind = None
            return

        if not isinstance(value, DdsLivenessKindEnum):
            raise TypeError(
                f"livenessKind must be DdsLivenessKindEnum or None, got {type(value).__name__}"
            )
        self._livenessKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLivelinessLease(self) -> "Float":
        """
        AUTOSAR-compliant getter for livelinessLease.

        Returns:
            The livelinessLease value

        Note:
            Delegates to liveliness_lease property (CODING_RULE_V2_00017)
        """
        return self.liveliness_lease  # Delegates to property

    def setLivelinessLease(self, value: "Float") -> "DdsLiveliness":
        """
        AUTOSAR-compliant setter for livelinessLease with method chaining.

        Args:
            value: The livelinessLease to set

        Returns:
            self for method chaining

        Note:
            Delegates to liveliness_lease property setter (gets validation automatically)
        """
        self.liveliness_lease = value  # Delegates to property setter
        return self

    def getLivenessKind(self) -> "DdsLivenessKindEnum":
        """
        AUTOSAR-compliant getter for livenessKind.

        Returns:
            The livenessKind value

        Note:
            Delegates to liveness_kind property (CODING_RULE_V2_00017)
        """
        return self.liveness_kind  # Delegates to property

    def setLivenessKind(self, value: "DdsLivenessKindEnum") -> "DdsLiveliness":
        """
        AUTOSAR-compliant setter for livenessKind with method chaining.

        Args:
            value: The livenessKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to liveness_kind property setter (gets validation automatically)
        """
        self.liveness_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_liveliness_lease(self, value: Optional["Float"]) -> "DdsLiveliness":
        """
        Set livelinessLease and return self for chaining.

        Args:
            value: The livelinessLease to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_liveliness_lease("value")
        """
        self.liveliness_lease = value  # Use property setter (gets validation)
        return self

    def with_liveness_kind(self, value: Optional["DdsLivenessKindEnum"]) -> "DdsLiveliness":
        """
        Set livenessKind and return self for chaining.

        Args:
            value: The livenessKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_liveness_kind("value")
        """
        self.liveness_kind = value  # Use property setter (gets validation)
        return self
