#from __future__ import annotations

from abc import ABCMeta
from typing import List

from .general_structure import ARObject, ARElement, Identifiable
from .data_dictionary import SwDataDefProps


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

        self.array_size = None    # type: int
        self.array_size_semantics = None  # type: str
        self.is_optional = None    # type: bool
        self.sw_data_def_props = None    # type: SwDataDefProps

    # type : ImplementationDataTypeElement
    def createImplementationDataTypeElement(self, short_name: str):
        if (short_name not in self.elements):
            event = ImplementationDataTypeElement(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    # type：List[ImplementationDataTypeElement]:
    def getImplementationDataTypeElements(self):
        return list(filter(lambda c: isinstance(c, ImplementationDataTypeElement), self.elements.values()))

class ExclusiveArea(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class InternalBehavior(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.exclusive_areas = None     # type: List[ExclusiveArea]

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
