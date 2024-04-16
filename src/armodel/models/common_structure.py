#from __future__ import annotations

from abc import ABCMeta
from typing import List

from .general_structure import ARObject, ARElement, Identifiable
from .data_dictionary import SwDataDefProps
from .ar_ref import RefType

import re

class ValueSpecification(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ValueSpecification:
            raise NotImplementedError("ValueSpecification is an abstract class.")
        super().__init__()

        self.short_label = None


class ConstantSpecification(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.value_spec = None  # type: ValueSpecification

class ConstantReference(ValueSpecification):
    def __init__(self):
        super().__init__()

        self.constant_ref = None

class AbstractImplementationDataTypeElement(Identifiable):
    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    ARRAY_SIZE_SEMANTICS_FIXED_SIZE = "FIXED-SIZE"
    ARRAY_SIZE_SEMANTICS_VARIABLE_SIZE = "VARIABLE_SIZE"

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.array_size = None              # type: int
        self.array_size_semantics = None    # type: str
        self.is_optional = None             # type: bool
        self.sw_data_def_props = None       # type: SwDataDefProps
    
    def createImplementationDataTypeElement(self, short_name: str): # type: (...) -> ImplementationDataTypeElement
        if (short_name not in self.elements):
            event = ImplementationDataTypeElement(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]
    
    def getImplementationDataTypeElements(self):                    # type：(...) -> List[ImplementationDataTypeElement]:
        return list(filter(lambda c: isinstance(c, ImplementationDataTypeElement), self.elements.values()))

class ExclusiveArea(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class InternalBehavior(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == InternalBehavior:
            raise NotImplementedError("InternalBehavior is an abstract class.")
        super().__init__(parent, short_name)

        self._data_type_mapping_refs = []      # type: List[RefType]

    def addDataTypeMappingRef(self, ref: RefType):
        self._data_type_mapping_refs.append(ref)

    def getDataTypeMappingRefs(self) -> List[RefType]:
        return self._data_type_mapping_refs

    def createExclusiveArea(self, short_name: str) -> ExclusiveArea:
        if (short_name not in self.elements):
            event = ExclusiveArea(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getExclusiveAreas(self) -> List[ExclusiveArea]:
        return list(filter(lambda c: isinstance(c, ExclusiveArea), self.elements.values()))

class ModeDeclaration(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.value = 0

class ExecutableEntity(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ExecutableEntity:
            raise NotImplementedError("ExecutableEntity is an abstract class.")
        super().__init__(parent, short_name)
    
        self.activation_reason = None           # *
        self.minimum_start_interval = 0.0       # 0..1
        self.reentrancy_level = None            # 
        self.can_enter_exclusive_area_refs = [] # type: List[RefType]  

    @property
    def minimum_start_interval_ms(self) -> int:
        return int(self.minimum_start_interval * 1000)

    def addCanEnterExclusiveAreaRef(self, ref: RefType):
        self.can_enter_exclusive_area_refs.append(ref)

    def getCanEnterExclusiveAreaRefs(self):
        return self.can_enter_exclusive_area_refs
    
class ModeDeclarationGroupPrototype(Identifiable):
    """
    The ModeDeclarationGroupPrototype specifies a set of Modes (ModeDeclarationGroup) which is provided or required in the given context.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self._sw_calibration_access = ""    # 0..1
        self.type_tref = None                    # tref 0..1

    @property
    def sw_calibration_access(self):
        return self._sw_calibration_access

    @sw_calibration_access.setter
    def sw_calibration_access(self, value):
        if (value not in ("notAccessible", "readOnly", "readWrite")):
            raise ValueError("Invalid SwCalibrationAccess <%s> of ModeDeclarationGroupPrototype <%s>" % (value, self.short_name))
        self._sw_calibration_access = value

class MemorySection(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self._alignment = None
        self.sw_addr_method_ref = None  # type: RefType

    @property
    def alignment(self) -> str:
        return self._alignment

    @alignment.setter
    def alignment(self, value:str):
        match = False
        if value in ("UNKNOWN", "UNSPECIFIED", "BOOLEAN", "PTR"):
            self._alignment = value
            match = True
        else:
            m = re.match(r'^\d+', value)
            if m:
                self._alignment = value
                match = True
                
        if not match:
            raise ValueError("Invalid alignment <%s> of memory section <%s>" % (value, self.short_name))
        

class ResourceConsumption(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createMemorySection(self, short_name: str) -> MemorySection:
        if (short_name not in self.elements):
            entry = MemorySection(self, short_name)
            self.elements[short_name] = entry
        return self.elements[short_name]

    def getMemorySections(self) -> List[MemorySection]:
        return list(filter(lambda a : isinstance(a, MemorySection), self.elements.values()))

    def getMemorySection(self, short_name: str) -> MemorySection:
        return next(filter(lambda o: isinstance(o, MemorySection) and (o.short_name == short_name), self.elements.values()), None)