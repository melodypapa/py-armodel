"""
This module contains classes for representing AUTOSAR included data types
in software component internal behavior templates.
"""

from typing import List

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    RefType,
)


class IncludedDataTypeSet(ARObject):
    def __init__(self):
        super().__init__()

        self.data_type_refs = []            # type: List[RefType]
        self.literal_prefix = None          # type: ARLiteral

    def addDataTypeRef(self, ref_type: RefType):
        self.data_type_refs.append(ref_type)

    def getDataTypeRefs(self) -> List[RefType]:
        return self.data_type_refs

    @property
    def literalPrefix(self) -> ARLiteral:
        return self.literal_prefix

    @literalPrefix.setter
    def literalPrefix(self, value: ARLiteral):
        self.literal_prefix = value

    def getLiteralPrefix(self) -> ARLiteral:
        return self.literal_prefix
