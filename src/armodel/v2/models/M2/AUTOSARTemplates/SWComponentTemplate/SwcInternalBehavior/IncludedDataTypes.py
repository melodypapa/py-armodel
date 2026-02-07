"""
This module contains classes for representing AUTOSAR included data types
in software component internal behavior templates.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    RefType,
)


class IncludedDataTypeSet(ARObject):

    def __init__(self) -> None:
        super().__init__()

        self.data_type_refs = []            # type: List[RefType]
        self.literal_prefix: Union[ARLiteral, None] = None

    def addDataTypeRef(self, ref_type: RefType) -> None:
        self.data_type_refs.append(ref_type)

    def getDataTypeRefs(self) -> List[RefType]:
        return self.data_type_refs

    @property
    def literalPrefix(self) -> Union[ARLiteral, None]:
        return self.literal_prefix

    @literalPrefix.setter
    def literalPrefix(self, value: ARLiteral) -> None:
        self.literal_prefix = value

    def getLiteralPrefix(self) -> Union[ARLiteral, None]:
        return self.literal_prefix
