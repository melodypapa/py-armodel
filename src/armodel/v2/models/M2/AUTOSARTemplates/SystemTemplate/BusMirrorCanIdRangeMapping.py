from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BusMirrorCanIdRangeMapping(ARObject):
    """
    This element defines a rule for remapping a set of CAN IDs.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror::BusMirrorCanIdRangeMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 702, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Base ID merged with the masked parts of the original ID to form the mapped
        # CAN ID.
        self._destinationBase: Optional["PositiveInteger"] = None

    @property
    def destination_base(self) -> Optional["PositiveInteger"]:
        """Get destinationBase (Pythonic accessor)."""
        return self._destinationBase

    @destination_base.setter
    def destination_base(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set destinationBase with validation.

        Args:
            value: The destinationBase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationBase = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"destinationBase must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._destinationBase = value
        # Value to match masked original CAN IDs.
        self._sourceCanIdCode: Optional["PositiveInteger"] = None

    @property
    def source_can_id_code(self) -> Optional["PositiveInteger"]:
        """Get sourceCanIdCode (Pythonic accessor)."""
        return self._sourceCanIdCode

    @source_can_id_code.setter
    def source_can_id_code(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sourceCanIdCode with validation.

        Args:
            value: The sourceCanIdCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceCanIdCode = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sourceCanIdCode must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sourceCanIdCode = value
        # Mask applied to original CAN IDs before comparison.
        self._sourceCanId: Optional["PositiveInteger"] = None

    @property
    def source_can_id(self) -> Optional["PositiveInteger"]:
        """Get sourceCanId (Pythonic accessor)."""
        return self._sourceCanId

    @source_can_id.setter
    def source_can_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sourceCanId with validation.

        Args:
            value: The sourceCanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceCanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sourceCanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sourceCanId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationBase(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for destinationBase.

        Returns:
            The destinationBase value

        Note:
            Delegates to destination_base property (CODING_RULE_V2_00017)
        """
        return self.destination_base  # Delegates to property

    def setDestinationBase(self, value: "PositiveInteger") -> "BusMirrorCanIdRangeMapping":
        """
        AUTOSAR-compliant setter for destinationBase with method chaining.

        Args:
            value: The destinationBase to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_base property setter (gets validation automatically)
        """
        self.destination_base = value  # Delegates to property setter
        return self

    def getSourceCanIdCode(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sourceCanIdCode.

        Returns:
            The sourceCanIdCode value

        Note:
            Delegates to source_can_id_code property (CODING_RULE_V2_00017)
        """
        return self.source_can_id_code  # Delegates to property

    def setSourceCanIdCode(self, value: "PositiveInteger") -> "BusMirrorCanIdRangeMapping":
        """
        AUTOSAR-compliant setter for sourceCanIdCode with method chaining.

        Args:
            value: The sourceCanIdCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_can_id_code property setter (gets validation automatically)
        """
        self.source_can_id_code = value  # Delegates to property setter
        return self

    def getSourceCanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sourceCanId.

        Returns:
            The sourceCanId value

        Note:
            Delegates to source_can_id property (CODING_RULE_V2_00017)
        """
        return self.source_can_id  # Delegates to property

    def setSourceCanId(self, value: "PositiveInteger") -> "BusMirrorCanIdRangeMapping":
        """
        AUTOSAR-compliant setter for sourceCanId with method chaining.

        Args:
            value: The sourceCanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_can_id property setter (gets validation automatically)
        """
        self.source_can_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_base(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdRangeMapping":
        """
        Set destinationBase and return self for chaining.

        Args:
            value: The destinationBase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_base("value")
        """
        self.destination_base = value  # Use property setter (gets validation)
        return self

    def with_source_can_id_code(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdRangeMapping":
        """
        Set sourceCanIdCode and return self for chaining.

        Args:
            value: The sourceCanIdCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_can_id_code("value")
        """
        self.source_can_id_code = value  # Use property setter (gets validation)
        return self

    def with_source_can_id(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdRangeMapping":
        """
        Set sourceCanId and return self for chaining.

        Args:
            value: The sourceCanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_can_id("value")
        """
        self.source_can_id = value  # Use property setter (gets validation)
        return self
