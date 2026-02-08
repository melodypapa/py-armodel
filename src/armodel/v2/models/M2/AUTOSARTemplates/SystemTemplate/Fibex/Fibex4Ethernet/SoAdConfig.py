from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SoAdConfig(ARObject):
    """
    SoAd Configuration for one specific Physical Channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 451, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of SocketConnectionBundles.
        # Stereotypes: atpSplitable; atpVariation 2090 Document ID 63:
                # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._connection: List["SocketConnection"] = []

    @property
    def connection(self) -> List["SocketConnection"]:
        """Get connection (Pythonic accessor)."""
        return self._connection
        # Collection of SoAdAddresses.
        # atpVariation.
        self._socketAddress: List["SocketAddress"] = []

    @property
    def socket_address(self) -> List["SocketAddress"]:
        """Get socketAddress (Pythonic accessor)."""
        return self._socketAddress

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnection(self) -> List["SocketConnection"]:
        """
        AUTOSAR-compliant getter for connection.

        Returns:
            The connection value

        Note:
            Delegates to connection property (CODING_RULE_V2_00017)
        """
        return self.connection  # Delegates to property

    def getSocketAddress(self) -> List["SocketAddress"]:
        """
        AUTOSAR-compliant getter for socketAddress.

        Returns:
            The socketAddress value

        Note:
            Delegates to socket_address property (CODING_RULE_V2_00017)
        """
        return self.socket_address  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
