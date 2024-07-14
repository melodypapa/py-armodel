from abc import ABCMeta

from .data_dictionary import SwDataDefProps
from .common_structure import ValueSpecification
from .general_structure import AtpFeature, ARObject

class AtpPrototype(AtpFeature, metaclass = ABCMeta):
    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == AtpPrototype:
            raise NotImplementedError("AtpPrototype is an abstract class.")

        super().__init__(parent, short_name)

class DataPrototype(AtpPrototype, metaclass = ABCMeta):
    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == DataPrototype:
            raise NotImplementedError("DataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        self.sw_data_def_props = None   # type: SwDataDefProps

class AutosarDataPrototype(DataPrototype, metaclass = ABCMeta):
    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == AutosarDataPrototype:
            raise NotImplementedError("AutosarDataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        self.type_tref = None           

class VariableDataPrototype(AutosarDataPrototype):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.init_value = None      # type: ValueSpecification

class ApplicationCompositeElementDataPrototype(DataPrototype, metaclass = ABCMeta):
    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == ApplicationCompositeElementDataPrototype:
            raise NotImplementedError("ApplicationCompositeElementDataPrototype is an abstract class.")

        super().__init__(parent, short_name)
        self.type_tref = None           

class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.is_optional = None

class ParameterDataPrototype(AutosarDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.init_value = None      # type: ValueSpecification