from typing import List


class BswCompositionTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints for a set
    of BswImplementations representing a BSW composition. A constraint defined
    at this level holds true for all referenced Bsw Implementations. Note, that
    multiple implementations of the same basic software module could be
    involved. TimingDescriptions aggregated by BswCompositionTiming are
    restricted to event chains referring to events which are derived from the
    class TDEventBswInternalBehavior and TDEventBsw. (cid:53) 28 of 277 Document
    ID 411: AUTOSAR_CP_TPS_TimingExtensions Specification of Timing Extensions
    for Classic Platform AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::BswCompositionTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 28, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a BswCompositionTiming.
        # All descriptions and constraints shall within this scope.
        self._implementation: List["BswImplementation"] = []

    @property
    def implementation(self) -> List["BswImplementation"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementation(self) -> List["BswImplementation"]:
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
