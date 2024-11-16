#from __future__ import annotations

from abc import ABCMeta
from typing import List

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARLiteral, ARNumerical

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from .M2.MSR.data_dictionary.data_def_properties import SwDataDefProps
from .ar_ref import RefType, TRefType

import re


class ExclusiveArea(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class IncludedModeDeclarationGroupSet(ARObject):
    def __init__(self):
        super().__init__()

        self.mode_declaration_group_refs = []           # type: List[RefType]
        self.prefix = None                              # type: ARLiteral

    def addModeDeclarationGroupRef(self, ref: RefType):
        self.mode_declaration_group_refs.append(ref)
        return self

    def getModeDeclarationGroupRefs(self) -> List[RefType]:
        return self.mode_declaration_group_refs

    def setPrefix(self, prefix: str):
        self.prefix = prefix
        return self
    
    def getPrefix(self) -> ARLiteral:
        return self.prefix
    
class ModeDeclaration(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.value = None                           # type: ARNumerical

    def setValue(self, value):
        self.value = value
        return self

    def getValue(self) -> ARNumerical:
        return self.value

class ExecutableEntity(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ExecutableEntity:
            raise NotImplementedError("ExecutableEntity is an abstract class.")
        
        super().__init__(parent, short_name)
    
        self.activationReason = None                # *
        self.minimumStartInterval = None            # type: ARFloat
        self.reentrancyLevel = None                 # 
        self.canEnterExclusiveAreaRefs = []         # type: List[RefType]  
        self.swAddrMethodRef = None                 # type: RefType

    def getActivationReason(self):
        return self.activationReason

    def setActivationReason(self, value):
        self.activationReason = value
        return self

    def getMinimumStartInterval(self):
        return self.minimumStartInterval

    def setMinimumStartInterval(self, value):
        self.minimumStartInterval = value
        return self

    def getReentrancyLevel(self):
        return self.reentrancyLevel

    def setReentrancyLevel(self, value):
        self.reentrancyLevel = value
        return self

    def getSwAddrMethodRef(self):
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value):
        self.swAddrMethodRef = value
        return self

    @property
    def minimumStartIntervalMs(self) -> int:
        if self.minimumStartInterval is not None:
            return int(self.minimumStartInterval.getValue() * 1000)
        return None

    def addCanEnterExclusiveAreaRef(self, ref: RefType):
        self.canEnterExclusiveAreaRefs.append(ref)

    def getCanEnterExclusiveAreaRefs(self):
        return self.canEnterExclusiveAreaRefs
    
class ModeDeclarationGroupPrototype(Identifiable):
    """
    The ModeDeclarationGroupPrototype specifies a set of Modes (ModeDeclarationGroup) which is provided or required in the given context.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._swCalibrationAccess = None        # type: str
        self.typeTRef = None                    # type: TRefType

    @property
    def sw_calibration_access(self):
        return self._swCalibrationAccess

    @sw_calibration_access.setter
    def sw_calibration_access(self, value):
        if (value not in ("notAccessible", "readOnly", "readWrite")):
            raise ValueError("Invalid SwCalibrationAccess <%s> of ModeDeclarationGroupPrototype <%s>" % (value, self.short_name))
        self._swCalibrationAccess = value

    def getSwCalibrationAccess(self):
        return self.swCalibrationAccess

    def setSwCalibrationAccess(self, value):
        self.swCalibrationAccess = value
        return self

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self

class MemorySection(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self._alignment = None              # type: ARLiteral
        self.size = None
        self.options = []                   # type: List[ARLiteral]
        self.swAddrMethodRef = None         # type: RefType
        self.symbol = None                  # type: ARLiteral

    def getAlignment(self):
        return self.alignment

    def setAlignment(self, value):
        self.alignment = value
        return self

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value
        return self

    def getSwAddrMethodRef(self):
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value):
        self.swAddrMethodRef = value
        return self

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self

    @property
    def alignment(self) -> ARLiteral:
        return self._alignment

    @alignment.setter
    def alignment(self, value: ARLiteral):
        if value is not None and value.getValue() != "":
            match = False
            if value.getValue() in ("UNKNOWN", "UNSPECIFIED", "BOOLEAN", "PTR"):
                self._alignment = value
                match = True
            else:
                m = re.match(r'^\d+', value.value)
                if m:
                    self._alignment = value
                    match = True
                    
            if not match:
                raise ValueError("Invalid alignment <%s> of memory section <%s>" % (value, self.getShortName()))
            
    def addOption(self, option: ARLiteral):
        self.options.append(option)

    def getOptions(self) -> List[ARLiteral]:
        return self.options

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
    
class Trigger(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swImplPolicy = None    # type: str
        self.triggerPeriod = None   # type: float

class ModeRequestTypeMap(ARObject):
    def __init__(self):
        super().__init__()

        self.implementation_data_type_ref = None           # type: RefType
        self.mode_group_ref = None                        # type: RefType

class ModeDeclarationGroup(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._initial_mode_ref = None                      # type: RefType
        self._on_transition_value = None                   # type: ARNumerical

    def createModeDeclaration(self, short_name: str) -> ModeDeclaration:
        if (short_name not in self.elements):
            spec = ModeDeclaration(self, short_name)
            self.elements[short_name] = spec
        return self.elements[short_name]
    
    def getModeDeclarations(self) -> List[ModeDeclaration]:
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclaration), self.elements.values()), key= lambda o:o.short_name))
    
    def setInitialModeRef(self, ref: RefType):
        self._initial_mode_ref = ref
        return self
    
    def getInitialModeRef(self) -> RefType:
        return self._initial_mode_ref

    def setOnTransitionValue(self, value):
        if isinstance(value, int):
            value = ARNumerical()
            value.setValue(value)
        self._on_transition_value = value
        return self
    
    def getOnTransitionValue(self) -> ARNumerical:
        return self._on_transition_value
    
class ModeDeclarationGroupPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swCalibrationAccess = None                 # type: str
        self.type_tref = None                            # type: TRefType