from typing import List

from .ar_object import ARFloat, ARLiteral
from .calibration import SwCalprmAxisSet
from .annotation import Annotation
from .general_structure import ARObject, Identifiable
from .ar_ref import RefType



class SwDataDefPropsConditional(ARObject):
    def __init__(self):
        super().__init__()

class SwDataDefProps(ARObject):
    def __init__(self):
        super().__init__()

        self._annotations = []                              # type: List[Annotation]
        self.baseTypeRef = None                             # type: RefType
        self.compuMethodRef = None                          # type: RefType
        self.dataConstrRef = None                           # type: RefType
        self.implementationDataTypeRef = None               # type: RefType
        self.swImplPolicy = None                            # type: str
        self.swCalibrationAccess = None                     # type: str
        self.swCalprmAxisSet = None                         # type: SwCalprmAxisSet
        self.sw_pointer_target_props = None                 # type: SwPointerTargetProps
        self.swRecordLayoutRef = None                       # type: RefType
        self.valueAxisDataTypeRef = None                    # type: RefType
        self.unitRef = None                                 # type: RefType
        self.conditional = SwDataDefPropsConditional()      # type: SwDataDefPropsConditional

    def addAnnotation(self, annotation: Annotation):
        self._annotations.append(annotation)

    def getAnnotations(self) -> List[Annotation]:
        return self._annotations
    
    def setUnitRef(self, ref: RefType):
        self.unitRef = ref
        return self

class SwPointerTargetProps(ARObject):
    def __init__(self):
        super().__init__()

        self.function_pointer_signature = None      # type: RefType
        self.sw_data_def_props = None               # type: SwDataDefProps
        self.target_category = None

class SwAddrMethod(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.memoryAllocationKeywordPolicy = None   # type: MemoryAllocationKeywordPolicyType
        self.option = []                            # type: str
        self.sectionInitializationPolicy = None     # type: SectionInitializationPolicyType
        self.sectionType = None                     # type: MemorySectionType
    