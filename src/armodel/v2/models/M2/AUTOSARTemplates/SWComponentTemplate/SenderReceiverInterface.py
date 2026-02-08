from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import DataInterface

    RefType,
)


class SenderReceiverInterface(DataInterface):
    """
    A sender/receiver interface declares a number of data elements to be sent
    and received.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::SenderReceiverInterface

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 335, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 329, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 94, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2054, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 244, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 208, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The data elements of this SenderReceiverInterface.
        self._dataElement: List[RefType] = []

    @property
    def data_element(self) -> List[RefType]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # InvalidationPolicy for a particular dataElement.
        self._invalidationPolicy: List["InvalidationPolicy"] = []

    @property
    def invalidation_policy(self) -> List["InvalidationPolicy"]:
        """Get invalidationPolicy (Pythonic accessor)."""
        return self._invalidationPolicy
        # This aggregation defines fixed sets of meta-data items with dataElements of
        # the enclosing Sender.
        self._metaDataItem: List[RefType] = []

    @property
    def meta_data_item(self) -> List[RefType]:
        """Get metaDataItem (Pythonic accessor)."""
        return self._metaDataItem

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def getInvalidationPolicy(self) -> List["InvalidationPolicy"]:
        """
        AUTOSAR-compliant getter for invalidationPolicy.

        Returns:
            The invalidationPolicy value

        Note:
            Delegates to invalidation_policy property (CODING_RULE_V2_00017)
        """
        return self.invalidation_policy  # Delegates to property

    def getMetaDataItem(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for metaDataItem.

        Returns:
            The metaDataItem value

        Note:
            Delegates to meta_data_item property (CODING_RULE_V2_00017)
        """
        return self.meta_data_item  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
