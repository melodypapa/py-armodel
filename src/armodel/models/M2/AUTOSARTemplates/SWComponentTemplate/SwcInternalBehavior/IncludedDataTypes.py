"""
This module contains classes for representing AUTOSAR included data types
in software component internal behavior templates.
"""

from __future__ import annotations
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class IncludedDataTypeSet(ARObject):
    """
    An includedDataTypeSet declares that a set of AutosarDataType is used by a basic software module or a software component for its implementation and the AutosarDataType becomes part of the contract. This information is required if the AutosarDataType is not used for any DataPrototype owned by this software component or if the enumeration literals, lowerLimit and upperLimit constants shall be generated with a literalPrefix. The optional literalPrefix is used to add a common prefix on enumeration literals, lowerLimit and upper Limit constants created by the RTE.
    """

    # IncludedDataTypeSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.50, p.600
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDataTypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataTypeRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getLiteralPrefix  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLiteralPrefix  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # AutosarDataType belonging to the includedDataTypeSet
        self.dataTypeRefs: List[RefType] = []

        # LiteralPrefix defines a common prefix for all AutosarData Types of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE.
        self.literalPrefix: Optional[Identifier] = None

    def addDataTypeRef(self, value: Optional[RefType]) -> IncludedDataTypeSet:
        """AutosarDataType belonging to the includedDataTypeSet A None value is a no-op and does not append to dataTypeRefs."""
        if value is not None:
            self.dataTypeRefs.append(value)
        return self

    def getDataTypeRefs(self) -> List[RefType]:
        """AutosarDataType belonging to the includedDataTypeSet"""
        return self.dataTypeRefs

    def getLiteralPrefix(self) -> Optional[Identifier]:
        """LiteralPrefix defines a common prefix for all AutosarData Types of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE."""
        return self.literalPrefix

    def setLiteralPrefix(self, value: Optional[Identifier]) -> IncludedDataTypeSet:
        """LiteralPrefix defines a common prefix for all AutosarData Types of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE. A None value is a no-op and does not overwrite an existing literalPrefix."""
        if value is not None:
            self.literalPrefix = value
        return self
