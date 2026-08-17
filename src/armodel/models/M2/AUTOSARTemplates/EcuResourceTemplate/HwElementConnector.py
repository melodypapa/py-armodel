"""
This module contains classes for representing AUTOSAR hardware element connectors
in the EcuResourceTemplate module.
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable


class HwElementConnector(Describable):
    """
    This meta-class represents the ability to connect two hardware elements. The details of the connection can be refined by hwPinGroupConnection.
    """

    # HwElementConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUResourceTemplate.pdf, Table 2.8, p.21
    # Deviation: source attributes (hwElementRef, hwPinRef) do not match spec
    #   Table 2.8 (hwElement x2, hwPinConnection aggr, hwPinGroupConnection ref);
    #   HwPinConnector/HwPinGroupConnector classes not yet modeled. No stamp.
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHwElementRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setHwElementRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHwPinRef                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setHwPinRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        self.hwElementRef: Optional[RefType] = None
        self.hwPinRef: Optional[RefType] = None

    def getHwElementRef(self) -> Optional[RefType]:
        """
        Gets the reference to the connected hardware element.

        Returns:
            RefType representing the hardware element reference, or None if not set
        """
        return self.hwElementRef

    def setHwElementRef(self, value: RefType):
        """
        Sets the reference to the connected hardware element.
        Only sets the value if it is not None.

        Args:
            value: The hardware element reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwElementRef = value
        return self

    def getHwPinRef(self) -> Optional[RefType]:
        """
        Gets the reference to the connected hardware pin.

        Returns:
            RefType representing the hardware pin reference, or None if not set
        """
        return self.hwPinRef

    def setHwPinRef(self, value: RefType):
        """
        Sets the reference to the connected hardware pin.
        Only sets the value if it is not None.

        Args:
            value: The hardware pin reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwPinRef = value
        return self
