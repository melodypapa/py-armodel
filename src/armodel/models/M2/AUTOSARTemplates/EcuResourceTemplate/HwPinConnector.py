"""
This module contains classes for representing AUTOSAR hardware pin connectors
in the EcuResourceTemplate module.
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable


class HwPinConnector(Describable):
    """
    Represents a hardware pin connector in AUTOSAR hardware descriptions.
    This class defines connections between hardware pins.

    Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.10, p.22
    Spec verified: R23-11
    Note: Represents connections at the pin level between hardware elements.
    """

    # HwPinConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.10, p.22
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addHwPinRef                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHwPinRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        """
        Initializes the HwPinConnector.
        """
        super().__init__()

        # References to hardware pins that are connected
        self.hwPinRefs: List[RefType] = []

    def addHwPinRef(self, value: RefType):
        """
        Adds a reference to a hardware pin in this connector.

        A None value is a no-op and does not add an hwPinRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwPinRefs.append(value)
        return self

    def getHwPinRefs(self) -> List[RefType]:
        """
        Gets all hardware pin references in this connector.

        Returns:
            The list of hwPinRefs, or an empty list if none are set
        """
        return self.hwPinRefs
