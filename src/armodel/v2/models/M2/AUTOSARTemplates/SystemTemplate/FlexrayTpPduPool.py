from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FlexrayTpPduPool(Identifiable):
    """
    FlexrayTpPduPool is a set of N-PDUs which are defined for FrTp sending or
    receiving purpose.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpPduPool

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 596, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to NPdus that are part of the PduPool.
        self._nPdu: List["NPdu"] = []

    @property
    def n_pdu(self) -> List["NPdu"]:
        """Get nPdu (Pythonic accessor)."""
        return self._nPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNPdu(self) -> List["NPdu"]:
        """
        AUTOSAR-compliant getter for nPdu.

        Returns:
            The nPdu value

        Note:
            Delegates to n_pdu property (CODING_RULE_V2_00017)
        """
        return self.n_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
