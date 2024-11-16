from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ...GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from typing import List

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