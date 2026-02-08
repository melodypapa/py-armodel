from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


class SocketConnectionIpduIdentifierSet(FibexElement):
    """
    Collection of PduIdentifiers used for transmission over a Socket Connection
    with the header option.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SocketConnectionIpduIdentifierSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 490, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of IPduIdentifiers that are transmitted over.
        self._iPduIdentifier: List["SoConIPduIdentifier"] = []

    @property
    def i_pdu_identifier(self) -> List["SoConIPduIdentifier"]:
        """Get iPduIdentifier (Pythonic accessor)."""
        return self._iPduIdentifier

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduIdentifier(self) -> List["SoConIPduIdentifier"]:
        """
        AUTOSAR-compliant getter for iPduIdentifier.

        Returns:
            The iPduIdentifier value

        Note:
            Delegates to i_pdu_identifier property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_identifier  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
