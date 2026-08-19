"""
This module contains classes for representing AUTOSAR included data types
in software component internal behavior templates.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType


class IncludedDataTypeSet(ARObject):
    """
    An includedDataTypeSet declares that a set of AutosarDataType is used by a basic software module or a software component for its implementation and the AutosarDataType becomes part of the contract. This information is required if the AutosarDataType is not used for any DataPrototype owned by this software component or if the enumeration literals, lowerLimit and upperLimit constants shall be generated with a literalPrefix. The optional literalPrefix is used to add a common prefix on enumeration literals, lowerLimit and upper Limit constants created by the RTE.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.50, p.600
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addDataTypeRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataTypeRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getLiteralPrefix     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLiteralPrefix     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # AutosarDataType belonging to the includedDataTypeSet.
        self.dataTypeRefs: List[RefType] = []

        # LiteralPrefix defines a common prefix for all AutosarDataTypes of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE.
        self.literalPrefix: Optional[ARLiteral] = None

    def addDataTypeRef(self, value: RefType) -> "IncludedDataTypeSet":
        """
        Adds a data type reference to the set.
        A None value is a no-op and does not append anything.

        AutosarDataType belonging to the includedDataTypeSet.

        Args:
            value: The data type reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataTypeRefs.append(value)
        return self

    def getDataTypeRefs(self) -> List[RefType]:
        """
        Gets the list of data type references.

        AutosarDataType belonging to the includedDataTypeSet.

        Returns:
            List[RefType]: The list of data type references
        """
        return self.dataTypeRefs

    def getLiteralPrefix(self) -> Optional[ARLiteral]:
        """
        Gets the literal prefix for the included data types.

        LiteralPrefix defines a common prefix for all AutosarDataTypes of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE.

        Returns:
            Optional[ARLiteral]: The literal prefix, or None if not set
        """
        return self.literalPrefix

    def setLiteralPrefix(self, value: Optional[ARLiteral]) -> "IncludedDataTypeSet":
        """
        Sets the literal prefix for the included data types.
        A None value is a no-op and does not overwrite an existing literal prefix.

        LiteralPrefix defines a common prefix for all AutosarDataTypes of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE.

        Args:
            value: The literal prefix to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.literalPrefix = value
        return self
