from typing import List


class TDCpSoftwareClusterMappingSet(ARElement):
    """
    This is used to gather of classic platform software cluster mappings.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster::TDCpSoftwareClusterMappingSet

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maps a temporal resource to a mapping between a providing CP software cluster
        # and requesting CP software atpVariation.
        self._tdCpSoftware: List["TDCpSoftwareCluster"] = []

    @property
    def td_cp_software(self) -> List["TDCpSoftwareCluster"]:
        """Get tdCpSoftware (Pythonic accessor)."""
        return self._tdCpSoftware

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTdCpSoftware(self) -> List["TDCpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for tdCpSoftware.

        Returns:
            The tdCpSoftware value

        Note:
            Delegates to td_cp_software property (CODING_RULE_V2_00017)
        """
        return self.td_cp_software  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
