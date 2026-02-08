from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PhysicalChannel,
)


class AbstractCanPhysicalChannel(PhysicalChannel, ABC):
    """
    Abstract class that is used to collect the common TtCAN and CAN
    PhysicalChannel attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 73, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanPhysicalChannel:
            raise TypeError("AbstractCanPhysicalChannel is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
