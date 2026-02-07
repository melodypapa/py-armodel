from typing import List


class LogAndTraceMessageCollectionSet(ARElement):
    """
    Collection of DltMessages

    Package: M2::AUTOSARTemplates::LogAndTraceExtract::LogAndTraceMessageCollectionSet

    Sources:
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 12, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of DltMessages in the DltMessageCollection atpVariation.
        self._dltMessage: List["DltMessage"] = []

    @property
    def dlt_message(self) -> List["DltMessage"]:
        """Get dltMessage (Pythonic accessor)."""
        return self._dltMessage

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDltMessage(self) -> List["DltMessage"]:
        """
        AUTOSAR-compliant getter for dltMessage.

        Returns:
            The dltMessage value

        Note:
            Delegates to dlt_message property (CODING_RULE_V2_00017)
        """
        return self.dlt_message  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
