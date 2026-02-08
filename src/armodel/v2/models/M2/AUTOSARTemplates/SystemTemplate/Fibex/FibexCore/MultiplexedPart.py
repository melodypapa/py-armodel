from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import SegmentPosition
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class MultiplexedPart(ARObject, ABC):
    """
    The StaticPart and the DynamicPart have common properties. Both can be
    separated in multiple segments within the multiplexed PDU.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::MultiplexedPart

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 411, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is MultiplexedPart:
            raise TypeError("MultiplexedPart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The StaticPart and the DynamicPart can be separated in segments within the
                # multiplexed PDU.
        # Therefore and the DynamicPart can contain multiple.
        self._segment: List["SegmentPosition"] = []

    @property
    def segment(self) -> List["SegmentPosition"]:
        """Get segment (Pythonic accessor)."""
        return self._segment

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSegment(self) -> List["SegmentPosition"]:
        """
        AUTOSAR-compliant getter for segment.

        Returns:
            The segment value

        Note:
            Delegates to segment property (CODING_RULE_V2_00017)
        """
        return self.segment  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
