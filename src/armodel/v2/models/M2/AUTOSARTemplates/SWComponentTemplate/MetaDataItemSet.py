from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class MetaDataItemSet(ARObject):
    """
    This meta-class represents the ability to define a set of meta-data items to
    be used in SenderReceiver Interfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 99, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2037, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the dataElement for which the of meta-data items is
        # defined.
        self._dataElement: List[RefType] = []

    @property
    def data_element(self) -> List[RefType]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # This aggregation represents the ordered definition of items.
        self._metaDataItem: List["MetaDataItem"] = []

    @property
    def meta_data_item(self) -> List["MetaDataItem"]:
        """Get metaDataItem (Pythonic accessor)."""
        return self._metaDataItem

    def with_data_element(self, value):
        """
        Set data_element and return self for chaining.

        Args:
            value: The data_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_meta_data_item(self, value):
        """
        Set meta_data_item and return self for chaining.

        Args:
            value: The meta_data_item to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_meta_data_item("value")
        """
        self.meta_data_item = value  # Use property setter (gets validation)
        return self

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

    def getMetaDataItem(self) -> List["MetaDataItem"]:
        """
        AUTOSAR-compliant getter for metaDataItem.

        Returns:
            The metaDataItem value

        Note:
            Delegates to meta_data_item property (CODING_RULE_V2_00017)
        """
        return self.meta_data_item  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
