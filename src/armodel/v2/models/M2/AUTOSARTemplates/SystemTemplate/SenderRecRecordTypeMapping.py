from typing import List


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """
    If the ApplicationCompositeDataType is a Record, the "RecordTypeMapping"
    will be used.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecRecordTypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Each ApplicationRecordElement shall be mapped on a SystemSignal.
        self._recordElement: List["SenderRecRecord"] = []

    @property
    def record_element(self) -> List["SenderRecRecord"]:
        """Get recordElement (Pythonic accessor)."""
        return self._recordElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRecordElement(self) -> List["SenderRecRecord"]:
        """
        AUTOSAR-compliant getter for recordElement.

        Returns:
            The recordElement value

        Note:
            Delegates to record_element property (CODING_RULE_V2_00017)
        """
        return self.record_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
