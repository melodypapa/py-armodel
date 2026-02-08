from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class DdsCpConfig(ARElement):
    """
    Collection of DDS definitions. (cid:53) 525 of 2090 Document ID 63:
    AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 525, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of DDS Domain definitions.
        self._ddsDomain: List["DdsCpDomain"] = []

    @property
    def dds_domain(self) -> List["DdsCpDomain"]:
        """Get ddsDomain (Pythonic accessor)."""
        return self._ddsDomain
        # Collection of DDS QOS Profiles.
        self._ddsQosProfile: List["DdsCpQosProfile"] = []

    @property
    def dds_qos_profile(self) -> List["DdsCpQosProfile"]:
        """Get ddsQosProfile (Pythonic accessor)."""
        return self._ddsQosProfile

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsDomain(self) -> List["DdsCpDomain"]:
        """
        AUTOSAR-compliant getter for ddsDomain.

        Returns:
            The ddsDomain value

        Note:
            Delegates to dds_domain property (CODING_RULE_V2_00017)
        """
        return self.dds_domain  # Delegates to property

    def getDdsQosProfile(self) -> List["DdsCpQosProfile"]:
        """
        AUTOSAR-compliant getter for ddsQosProfile.

        Returns:
            The ddsQosProfile value

        Note:
            Delegates to dds_qos_profile property (CODING_RULE_V2_00017)
        """
        return self.dds_qos_profile  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
