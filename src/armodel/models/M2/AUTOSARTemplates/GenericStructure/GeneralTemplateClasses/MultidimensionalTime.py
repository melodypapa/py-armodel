"""
This module contains the MultidimensionalTime class for representing
multidimensional time values based on ASAM CSE codes.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String
from typing import Optional, Union


class MultidimensionalTime(ARObject):
    """
    This is used to specify a multidimensional time value based on ASAM CSE codes. It is
    specified by a code which defined the basis of the time and a scaling factor which
    finally determines the time value.
    """

    # MultidimensionalTime method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.22, p.164
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

        # The CSE code specifying the time base. Modeled as String since the
        # dedicated CseCodeType is not modeled in this library.
        self.cseCode: Optional[String] = None

        # The scaling factor for the time value based on the specified CSE code.
        self.cseCodeFactor: Optional[Integer] = None

    def getCseCode(self) -> Optional[String]:
        """
        Gets the CSE code specifying the time base.

        Returns:
            String representing the CSE code, or None if not set
        """
        return self.cseCode

    def setCseCode(self, value: Optional[Union[String, str]]) -> "MultidimensionalTime":
        """
        Sets the CSE code specifying the time base.

        Args:
            value: The CSE code to set

        Returns:
            self for method chaining
        """
        if isinstance(value, str):
            self.cseCode = String().setValue(value)
        else:
            self.cseCode = value
        return self

    def getCseCodeFactor(self) -> Optional[Integer]:
        """
        Gets the scaling factor for the time value based on the specified CSE code.

        Returns:
            Integer representing the scaling factor, or None if not set
        """
        return self.cseCodeFactor

    def setCseCodeFactor(self, value: Optional[Union[Integer, int]]) -> "MultidimensionalTime":
        """
        Sets the scaling factor for the time value based on the specified CSE code.

        Args:
            value: The scaling factor to set

        Returns:
            self for method chaining
        """
        if isinstance(value, int) and not isinstance(value, Integer):
            self.cseCodeFactor = Integer().setValue(value)
        else:
            self.cseCodeFactor = value
        return self
