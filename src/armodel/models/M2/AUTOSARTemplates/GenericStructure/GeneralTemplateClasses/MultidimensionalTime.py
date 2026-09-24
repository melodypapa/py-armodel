"""
This module contains the MultidimensionalTime class for representing
multidimensional time values based on ASAM CSE codes.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CseCodeType, Integer
from typing import Optional


class MultidimensionalTime(ARObject):
    """
    Specifies a time value based on [17] see [TPS_GST_00354].
    """

    # MultidimensionalTime method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.74, p.165
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCseCode          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCseCode          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCseCodeFactor    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCseCodeFactor    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies the time base by means of CSE codes.
        self.cseCode: Optional[CseCodeType] = None

        # The scaling factor for the time value based on the specified CSE code.
        self.cseCodeFactor: Optional[Integer] = None

    def getCseCode(self) -> Optional[CseCodeType]:
        """
        Specifies the time base by means of CSE codes.
        """
        return self.cseCode

    def setCseCode(self, value: Optional[CseCodeType]) -> "MultidimensionalTime":
        """
        Specifies the time base by means of CSE codes. A None value is a no-op and does not overwrite an existing CSE code.
        """
        if value is not None:
            self.cseCode = value
        return self

    def getCseCodeFactor(self) -> Optional[Integer]:
        """
        The scaling factor for the time value based on the specified CSE code.
        """
        return self.cseCodeFactor

    def setCseCodeFactor(self, value: Optional[Integer]) -> "MultidimensionalTime":
        """
        The scaling factor for the time value based on the specified CSE code. A None value is a no-op and does not overwrite an existing scaling factor.
        """
        if value is not None:
            self.cseCodeFactor = value
        return self
