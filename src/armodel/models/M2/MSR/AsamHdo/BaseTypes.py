from abc import ABCMeta
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, ByteOrderEnum

class BaseTypeDefinition(ARObject):
    """
    Abstract base class for base type definitions.
    Base: ARObject
    """
    def __init__(self):
        super().__init__()


class BaseTypeDirectDefinition(BaseTypeDefinition):
    """
    Direct definition of a base type with encoding, size, and memory alignment specifications.
    Base: BaseTypeDefinition
    """
    def __init__(self):
        super().__init__()

        self.baseTypeEncoding: str = None
        self.baseTypeSize: ARNumerical = None
        self.byteOrder: ByteOrderEnum = None
        self.memAlignment: ARNumerical = None
        self.nativeDeclaration: str = None

    def getBaseTypeEncoding(self):
        return self.baseTypeEncoding

    def setBaseTypeEncoding(self, value):
        self.baseTypeEncoding = value
        return self

    def getBaseTypeSize(self):
        return self.baseTypeSize

    def setBaseTypeSize(self, value):
        self.baseTypeSize = value
        return self

    def getByteOrder(self):
        return self.byteOrder

    def setByteOrder(self, value):
        self.byteOrder = value
        return self

    def getMemAlignment(self):
        return self.memAlignment

    def setMemAlignment(self, value):
        self.memAlignment = value
        return self

    def getNativeDeclaration(self):
        return self.nativeDeclaration

    def setNativeDeclaration(self, value):
        self.nativeDeclaration = value
        return self



class BaseType(ARElement, metaclass=ABCMeta):
    """
    Abstract base class for base types.
    Base: ARElement
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BaseType:
            raise NotImplementedError("BaseType is an abstract class.")

        super().__init__(parent, short_name)

        self.baseTypeDefinition: BaseTypeDirectDefinition = BaseTypeDirectDefinition()

    def getBaseTypeDefinition(self) -> BaseTypeDirectDefinition:
        return self.baseTypeDefinition

    def setBaseTypeDefinition(self, value: BaseTypeDirectDefinition):
        self.baseTypeDefinition = value
        return self

class SwBaseType(BaseType):
    """
    Software base type representing primitive data types in software.
    Base: BaseType
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
