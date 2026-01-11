"""
This module contains classes for representing AUTOSAR data prototypes
in the SWComponentTemplate module. It includes various types of data
prototypes such as variable, parameter, and composite element prototypes
used in software components.
"""

from abc import ABCMeta
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, PositiveInteger, TRefType
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from .....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from .....M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from .....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpFeature

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

        self.swDataDefProps: SwDataDefProps = None

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self
    
class AutosarDataPrototype(DataPrototype, metaclass = ABCMeta):
    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == AutosarDataPrototype:
            raise NotImplementedError("AutosarDataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        self.typeTRef: TRefType = None

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self

class VariableDataPrototype(AutosarDataPrototype):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue: ValueSpecification = None

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

class ApplicationCompositeElementDataPrototype(DataPrototype, metaclass = ABCMeta):
    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == ApplicationCompositeElementDataPrototype:
            raise NotImplementedError("ApplicationCompositeElementDataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        self.typeTRef: RefType = None

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self


class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arraySizeHandling = None
        self.arraySizeSemantics = None
        self.indexDataTypeRef: RefType = None
        self.maxNumberOfElements: PositiveInteger = None

    def getArraySizeHandling(self):
        return self.arraySizeHandling

    def setArraySizeHandling(self, value):
        if value is not None:
            self.arraySizeHandling = value
        return self

    def getArraySizeSemantics(self):
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value):
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getIndexDataTypeRef(self):
        return self.indexDataTypeRef

    def setIndexDataTypeRef(self, value):
        if value is not None:
            self.indexDataTypeRef = value
        return self

    def getMaxNumberOfElements(self):
        return self.maxNumberOfElements

    def setMaxNumberOfElements(self, value):
        if value is not None:
            self.maxNumberOfElements = value
        return self
    
class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.isOptional = None

    def getIsOptional(self):
        return self.isOptional

    def setIsOptional(self, value):
        if value is not None:
            self.isOptional = value
        return self


class ParameterDataPrototype(AutosarDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue: ValueSpecification = None

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self
