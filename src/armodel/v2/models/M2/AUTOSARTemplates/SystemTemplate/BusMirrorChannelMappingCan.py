from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BusMirrorCanIdRange,
    BusMirrorCanIdToCanId,
    BusMirrorChannelMapping,
    BusMirrorLinPidToCan,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN or LIN sourceChannel
    and a CAN targetChannel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror::BusMirrorChannelMappingCan

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 700, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Rules for remapping of a set of CAN IDs.
        self._canIdRange: List["BusMirrorCanIdRange"] = []

    @property
    def can_id_range(self) -> List["BusMirrorCanIdRange"]:
        """Get canIdRange (Pythonic accessor)."""
        return self._canIdRange
        # Rules for remapping of single CanIds.
        self._canIdToCanId: List["BusMirrorCanIdToCanId"] = []

    @property
    def can_id_to_can_id(self) -> List["BusMirrorCanIdToCanId"]:
        """Get canIdToCanId (Pythonic accessor)."""
        return self._canIdToCanId
        # Rules for remapping of single LIN Frames.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._linPidToCanId: List["BusMirrorLinPidToCan"] = []

    @property
    def lin_pid_to_can_id(self) -> List["BusMirrorLinPidToCan"]:
        """Get linPidToCanId (Pythonic accessor)."""
        return self._linPidToCanId
        # Base ID merged with the LIN frame ID to form the CAN required when a
        # BusMirrorChannel that refers to a the role channel is referenced in
        # sourceChannel.
        self._mirrorSourceLin: Optional["PositiveInteger"] = None

    @property
    def mirror_source_lin(self) -> Optional["PositiveInteger"]:
        """Get mirrorSourceLin (Pythonic accessor)."""
        return self._mirrorSourceLin

    @mirror_source_lin.setter
    def mirror_source_lin(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set mirrorSourceLin with validation.

        Args:
            value: The mirrorSourceLin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mirrorSourceLin = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"mirrorSourceLin must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._mirrorSourceLin = value
        # CAN ID of the CAN status frame.
        # configured, a status frame will be sent on the CAN that contains the state of
                # all active source.
        self._mirrorStatus: Optional["PositiveInteger"] = None

    @property
    def mirror_status(self) -> Optional["PositiveInteger"]:
        """Get mirrorStatus (Pythonic accessor)."""
        return self._mirrorStatus

    @mirror_status.setter
    def mirror_status(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set mirrorStatus with validation.

        Args:
            value: The mirrorStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mirrorStatus = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"mirrorStatus must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._mirrorStatus = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanIdRange(self) -> List["BusMirrorCanIdRange"]:
        """
        AUTOSAR-compliant getter for canIdRange.

        Returns:
            The canIdRange value

        Note:
            Delegates to can_id_range property (CODING_RULE_V2_00017)
        """
        return self.can_id_range  # Delegates to property

    def getCanIdToCanId(self) -> List["BusMirrorCanIdToCanId"]:
        """
        AUTOSAR-compliant getter for canIdToCanId.

        Returns:
            The canIdToCanId value

        Note:
            Delegates to can_id_to_can_id property (CODING_RULE_V2_00017)
        """
        return self.can_id_to_can_id  # Delegates to property

    def getLinPidToCanId(self) -> List["BusMirrorLinPidToCan"]:
        """
        AUTOSAR-compliant getter for linPidToCanId.

        Returns:
            The linPidToCanId value

        Note:
            Delegates to lin_pid_to_can_id property (CODING_RULE_V2_00017)
        """
        return self.lin_pid_to_can_id  # Delegates to property

    def getMirrorSourceLin(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for mirrorSourceLin.

        Returns:
            The mirrorSourceLin value

        Note:
            Delegates to mirror_source_lin property (CODING_RULE_V2_00017)
        """
        return self.mirror_source_lin  # Delegates to property

    def setMirrorSourceLin(self, value: "PositiveInteger") -> "BusMirrorChannelMappingCan":
        """
        AUTOSAR-compliant setter for mirrorSourceLin with method chaining.

        Args:
            value: The mirrorSourceLin to set

        Returns:
            self for method chaining

        Note:
            Delegates to mirror_source_lin property setter (gets validation automatically)
        """
        self.mirror_source_lin = value  # Delegates to property setter
        return self

    def getMirrorStatus(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for mirrorStatus.

        Returns:
            The mirrorStatus value

        Note:
            Delegates to mirror_status property (CODING_RULE_V2_00017)
        """
        return self.mirror_status  # Delegates to property

    def setMirrorStatus(self, value: "PositiveInteger") -> "BusMirrorChannelMappingCan":
        """
        AUTOSAR-compliant setter for mirrorStatus with method chaining.

        Args:
            value: The mirrorStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to mirror_status property setter (gets validation automatically)
        """
        self.mirror_status = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mirror_source_lin(self, value: Optional["PositiveInteger"]) -> "BusMirrorChannelMappingCan":
        """
        Set mirrorSourceLin and return self for chaining.

        Args:
            value: The mirrorSourceLin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mirror_source_lin("value")
        """
        self.mirror_source_lin = value  # Use property setter (gets validation)
        return self

    def with_mirror_status(self, value: Optional["PositiveInteger"]) -> "BusMirrorChannelMappingCan":
        """
        Set mirrorStatus and return self for chaining.

        Args:
            value: The mirrorStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mirror_status("value")
        """
        self.mirror_status = value  # Use property setter (gets validation)
        return self
