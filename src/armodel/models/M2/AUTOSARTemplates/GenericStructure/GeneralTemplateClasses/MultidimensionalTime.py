"""
This module contains the MultidimensionalTime class for representing
multidimensional time values based on ASAM CSE codes.
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CseCodeType, Integer


class MultidimensionalTime(ARObject):
    """
    Specifies a time value based on [20] see [TPS_GST_00354].

    This is used to specify a multidimensional time value based on ASAM CSE codes. It is
    specified by a code which defined the basis of the time and a scaling factor which
    finally determines the time value.

    If for example the cseCode is 100 and the cseCodeFactor is 360, it represents 360
    angular degrees. If the cseCode is 0 and the cseCodeFactor is 50 it represents 50
    microseconds.
    """

    # MultidimensionalTime method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.22, p.164
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getCseCode                   [x] impl  [x] docstring  [x] test
    # [x] setCseCode                   [x] impl  [x] docstring  [x] test
    # [x] getCseCodeFactor             [x] impl  [x] docstring  [x] test
    # [x] setCseCodeFactor             [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the MultidimensionalTime.
        """
        super().__init__()

        # Specifies the time base by means of CSE codes. [constr_10338]
        self.cseCode: Optional[CseCodeType] = None

        # The scaling factor for the time value based on the specified CSE code. [constr_10339]
        self.cseCodeFactor: Optional[Integer] = None

    def getCseCode(self) -> Optional[CseCodeType]:
        """
        Gets the CSE code specifying the time base.

        The CSE code determines the basis of the time value. [constr_10338]

        Returns:
            CseCodeType representing the CSE code, or None if not set
        """
        return self.cseCode

    def setCseCode(self, value: Optional[CseCodeType]) -> "MultidimensionalTime":
        """
        Sets the CSE code specifying the time base.

        A None value is a no-op and does not overwrite an existing CSE code. [constr_10338]

        Args:
            value: The CSE code to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.cseCode = value
        return self

    def getCseCodeFactor(self) -> Optional[Integer]:
        """
        Gets the scaling factor for the time value based on the specified CSE code.

        The scaling factor finally determines the time value. [constr_10339]

        Returns:
            Integer representing the scaling factor, or None if not set
        """
        return self.cseCodeFactor

    def setCseCodeFactor(self, value: Optional[Integer]) -> "MultidimensionalTime":
        """
        Sets the scaling factor for the time value based on the specified CSE code.

        A None value is a no-op and does not overwrite an existing scaling factor. [constr_10339]

        Args:
            value: The scaling factor to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.cseCodeFactor = value
        return self
