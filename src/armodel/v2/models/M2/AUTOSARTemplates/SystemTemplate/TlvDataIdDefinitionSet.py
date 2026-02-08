from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class TlvDataIdDefinitionSet(ARElement):
    """
    This meta-class acts as a container of TlvDataIdDefinitions to be used in a
    given context

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TlvDataIdDefinitionSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 830, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the collection of TlVDataTid aggregated by the
        # TlvDataIdDefinitionSet.
        self._tlvDataId: List["TlvDataIdDefinition"] = []

    @property
    def tlv_data_id(self) -> List["TlvDataIdDefinition"]:
        """Get tlvDataId (Pythonic accessor)."""
        return self._tlvDataId

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTlvDataId(self) -> List["TlvDataIdDefinition"]:
        """
        AUTOSAR-compliant getter for tlvDataId.

        Returns:
            The tlvDataId value

        Note:
            Delegates to tlv_data_id property (CODING_RULE_V2_00017)
        """
        return self.tlv_data_id  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
