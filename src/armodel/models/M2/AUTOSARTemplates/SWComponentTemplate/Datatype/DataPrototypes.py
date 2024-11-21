from abc import ABCMeta
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, TRefType
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

        self.swDataDefProps = None          # type: SwDataDefProps

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

        self.typeTRef = None                # type:     TRefType

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self

class VariableDataPrototype(AutosarDataPrototype):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue = None      # type: ValueSpecification

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

        self.typeTRef = None                    # type: RefType

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self


class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arraySizeHandling = None               # type: str
        self.arraySizeSemantics = None              # type: str
        self.indexDataTypeRef = None                # type: RefType
        self.maxNumberOfElements = None             # type: ARNumerical

    def setArraySizeHandling(self, handling: str):
        self.arraySizeHandling = handling
        return self
    
    def setArraySizeSemantics(self, semantics: str):
        self.arraySizeSemantics = semantics
        return self
    
    def setIndexDataTypeRef(self, ref: RefType):
        self.indexDataTypeRef = ref
        return self
    
    def setMaxNumberOfElements(self, number: ARNumerical):
        self.maxNumberOfElements = number
        return self
    
class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.isOptional = None

class ParameterDataPrototype(AutosarDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue = None                       # type: ValueSpecification

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self
