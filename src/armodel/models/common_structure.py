#from __future__ import annotations

from abc import ABCMeta
from typing import List

from .general_structure import ARObject, ARElement, Identifiable
from .data_dictionary import SwDataDefProps


class ValueSpecification(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ValueSpecification:
            raise NotImplementedError(
                "ValueSpecification is an abstract class.")
        super().__init__()

        self.short_label = None


class ConstantSpecification(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.value_spec = None  # type: ValueSpecification


class ConstantReference(ValueSpecification):
    def __init__(self):
        super().__init__()

        self. constant_ref = None


class AbstractImplementationDataTypeElement(Identifiable):
    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)


class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.array_size = None    # type: int
        self.is_optional = None    # type: bool
        self.sw_data_def_props = None    # type: SwDataDefProps

    # def createImplementationDataTypeElement(self, short_name: str)-> ImplementationDataTypeElement:    # type :
    
    def createImplementationDataTypeElement(self, short_name: str): # type : ImplementationDataTypeElement
        if (short_name not in self.elements):
            event = ImplementationDataTypeElement(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getImplementationDataTypeElements(self): # type：List[ImplementationDataTypeElement]:
        return list(filter(lambda c: isinstance(c, ImplementationDataTypeElement), self.elements.values()))
