from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationCompositeDataType,
)


class ApplicationRecordDataType(ApplicationCompositeDataType):
    """
    An application data type which can be decomposed into prototypes of other
    application data types.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 261, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1997, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 34, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies an element of a record.
        # The aggregation of ApplicationRecordElement is subject with the purpose to
                # support the conditional elements inside a ApplicationrecordData atpVariation.
        self._element: List["ApplicationRecord"] = []

    @property
    def element(self) -> List["ApplicationRecord"]:
        """Get element (Pythonic accessor)."""
        return self._element

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> List["ApplicationRecord"]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
