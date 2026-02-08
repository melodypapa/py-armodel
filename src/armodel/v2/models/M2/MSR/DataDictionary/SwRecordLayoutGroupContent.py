from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwRecordLayoutGroupContent(ARObject):
    """
    This is the contents of a RecordLayout which is inserted for every
    iteration. Note that since this is atp Mixed, multiple properties can be
    inserted for each iteration.

    Package: M2::MSR::DataDictionary::RecordLayout::SwRecordLayoutGroupContent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 424, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Particular Value specification for this record layout group.
        # xml.
        # sequenceOffset=120.
        self._swRecord: Optional["SwRecordLayoutV"] = None

    @property
    def sw_record(self) -> Optional["SwRecordLayoutV"]:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: Optional["SwRecordLayoutV"]) -> None:
        """
        Set swRecord with validation.

        Args:
            value: The swRecord to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swRecord = None
            return

        if not isinstance(value, SwRecordLayoutV):
            raise TypeError(
                f"swRecord must be SwRecordLayoutV or None, got {type(value).__name__}"
            )
        self._swRecord = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwRecord(self) -> "SwRecordLayoutV":
        """
        AUTOSAR-compliant getter for swRecord.

        Returns:
            The swRecord value

        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: "SwRecordLayoutV") -> "SwRecordLayoutGroupContent":
        """
        AUTOSAR-compliant setter for swRecord with method chaining.

        Args:
            value: The swRecord to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_record property setter (gets validation automatically)
        """
        self.sw_record = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_record(self, value: Optional["SwRecordLayoutV"]) -> "SwRecordLayoutGroupContent":
        """
        Set swRecord and return self for chaining.

        Args:
            value: The swRecord to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_record("value")
        """
        self.sw_record = value  # Use property setter (gets validation)
        return self
