from abc import ABCMeta
from typing import List

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from .ar_ref import RefType
from .common_structure import ExclusiveArea
from .M2.AUTOSARTemplates.sw_component_template.data_type.data_prototypes import ParameterDataPrototype
from .general_structure import Identifiable

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

class InternalBehavior(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == InternalBehavior:
            raise NotImplementedError("InternalBehavior is an abstract class.")
        super().__init__(parent, short_name)

        self.data_type_mapping_refs = []        # type: List[RefType]                       
        self.constant_memories = []             # type: List[ParameterDataPrototype]

    def addDataTypeMappingRef(self, ref: RefType):
        self.data_type_mapping_refs.append(ref)

    def getDataTypeMappingRefs(self) -> List[RefType]:
        return self.data_type_mapping_refs
    
    def createExclusiveArea(self, short_name: str) -> ExclusiveArea:
        if (short_name not in self.elements):
            event = ExclusiveArea(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getExclusiveAreas(self) -> List[ExclusiveArea]:
        return list(filter(lambda c: isinstance(c, ExclusiveArea), self.elements.values()))
    
    def createConstantMemory(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            prototype = ParameterDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.constant_memories.append(prototype)
        return self.elements[short_name]

    def getConstantMemorys(self) -> List[ParameterDataPrototype]:
        return self.constant_memories
