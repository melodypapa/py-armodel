from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwcToSwcSignal(ARObject):
    """
    The SwcToSwcSignal describes the information (data element) that is
    exchanged between two SW Components. On the SWC Level it is possible that a
    SW Component sends one data element from one P-Port to two different SW
    Components (1:n Communication). The SwcToSwcSignal describes exactly the
    information which is exchanged between one P-Port of a SW Component and one
    R-Port of another SW Component.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::SwcToSwcSignal

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # same data element on the RPortPrototype.
        # by: VariableDataPrototypeIn.
        self._dataElement: List[RefType] = []

    @property
    def data_element(self) -> List[RefType]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
