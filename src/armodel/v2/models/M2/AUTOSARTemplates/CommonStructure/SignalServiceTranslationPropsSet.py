from typing import List


class SignalServiceTranslationPropsSet(ARElement):
    """
    Collection of SignalServiceTranslationProps.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation::SignalServiceTranslationPropsSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 730, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of SignalServiceTranslationProps.
        self._signalServiceProps: List["SignalService"] = []

    @property
    def signal_service_props(self) -> List["SignalService"]:
        """Get signalServiceProps (Pythonic accessor)."""
        return self._signalServiceProps

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignalServiceProps(self) -> List["SignalService"]:
        """
        AUTOSAR-compliant getter for signalServiceProps.

        Returns:
            The signalServiceProps value

        Note:
            Delegates to signal_service_props property (CODING_RULE_V2_00017)
        """
        return self.signal_service_props  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
