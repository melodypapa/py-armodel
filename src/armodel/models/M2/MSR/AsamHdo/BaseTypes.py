from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    BaseTypeEncodingString,
    ByteOrderEnum,
    NativeDeclarationString,
    PositiveInteger,
)


class BaseTypeDefinition(ARObject, ABC):
    """
    This meta-class represents the ability to define a basetype.
    """

    # BaseTypeDefinition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.23, p.290
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is BaseTypeDefinition:
            raise TypeError("BaseTypeDefinition is an abstract class.")
        super().__init__()


class BaseTypeDirectDefinition(BaseTypeDefinition):
    """
    This BaseType is defined directly (as opposite to a derived BaseType)
    """

    # BaseTypeDirectDefinition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.24, p.290
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseTypeEncoding       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseTypeEncoding       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBaseTypeSize           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseTypeSize           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getByteOrder              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setByteOrder              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMemAlignment           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMemAlignment           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNativeDeclaration      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNativeDeclaration      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This specifies, how an object of the current BaseType is encoded, e.g. in an ECU within a message sequence.
        self.baseTypeEncoding: Optional[BaseTypeEncodingString] = None

        # Describes the length of the data type specified in the container in bits.
        self.baseTypeSize: Optional[PositiveInteger] = None

        # This attribute specifies the byte order of the base type.
        self.byteOrder: Optional[ByteOrderEnum] = None

        # This attribute describes the alignment of the memory object in bits. E.g. "8" specifies, that the object in question is aligned to a byte while "32" specifies that it is aligned four byte. If the value is set to "0" the meaning shall be interpreted as "unspecified".
        self.memAlignment: Optional[PositiveInteger] = None

        # This attribute describes the declaration of such a base type in the native programming language, primarily in the Programming language C. This can then be used by a code generator to include the necessary declarations into a header file.
        self.nativeDeclaration: Optional[NativeDeclarationString] = None

    def getBaseTypeEncoding(self) -> Optional[BaseTypeEncodingString]:
        """
        This specifies, how an object of the current BaseType is encoded, e.g. in an ECU within a message sequence.
        """
        return self.baseTypeEncoding

    def setBaseTypeEncoding(self, value: Optional[BaseTypeEncodingString]) -> "BaseTypeDirectDefinition":
        """
        This specifies, how an object of the current BaseType is encoded, e.g. in an ECU within a message sequence.

        A None value is a no-op and does not overwrite an existing baseTypeEncoding.
        """
        if value is not None:
            self.baseTypeEncoding = value
        return self

    def getBaseTypeSize(self) -> Optional[PositiveInteger]:
        """
        Describes the length of the data type specified in the container in bits.
        """
        return self.baseTypeSize

    def setBaseTypeSize(self, value: Optional[PositiveInteger]) -> "BaseTypeDirectDefinition":
        """
        Describes the length of the data type specified in the container in bits.

        A None value is a no-op and does not overwrite an existing baseTypeSize.
        """
        if value is not None:
            self.baseTypeSize = value
        return self

    def getByteOrder(self) -> Optional[ByteOrderEnum]:
        """
        This attribute specifies the byte order of the base type.
        """
        return self.byteOrder

    def setByteOrder(self, value: Optional[ByteOrderEnum]) -> "BaseTypeDirectDefinition":
        """
        This attribute specifies the byte order of the base type.

        A None value is a no-op and does not overwrite an existing byteOrder.
        """
        if value is not None:
            self.byteOrder = value
        return self

    def getMemAlignment(self) -> Optional[PositiveInteger]:
        """
        This attribute describes the alignment of the memory object in bits. E.g. "8" specifies, that the object in question is aligned to a byte while "32" specifies that it is aligned four byte. If the value is set to "0" the meaning shall be interpreted as "unspecified".
        """
        return self.memAlignment

    def setMemAlignment(self, value: Optional[PositiveInteger]) -> "BaseTypeDirectDefinition":
        """
        This attribute describes the alignment of the memory object in bits. E.g. "8" specifies, that the object in question is aligned to a byte while "32" specifies that it is aligned four byte. If the value is set to "0" the meaning shall be interpreted as "unspecified".

        A None value is a no-op and does not overwrite an existing memAlignment.
        """
        if value is not None:
            self.memAlignment = value
        return self

    def getNativeDeclaration(self) -> Optional[NativeDeclarationString]:
        """
        This attribute describes the declaration of such a base type in the native programming language, primarily in the Programming language C. This can then be used by a code generator to include the necessary declarations into a header file. For example BaseType with shortName: "MyUnsignedInt" native Declaration: "unsigned short" Results in typedef unsigned short MyUnsignedInt; If the attribute is not defined the referring Implementation DataTypes will not be generated as a typedef by RTE. If a nativeDeclaration type is given it shall fulfill the characteristic given by basetypeEncoding and baseType Size. This is required to ensure the consistent handling and interpretation by software components, RTE, COM and MCM systems.
        """
        return self.nativeDeclaration

    def setNativeDeclaration(self, value: Optional[NativeDeclarationString]) -> "BaseTypeDirectDefinition":
        """
        This attribute describes the declaration of such a base type in the native programming language, primarily in the Programming language C. This can then be used by a code generator to include the necessary declarations into a header file. For example BaseType with shortName: "MyUnsignedInt" native Declaration: "unsigned short" Results in typedef unsigned short MyUnsignedInt; If the attribute is not defined the referring Implementation DataTypes will not be generated as a typedef by RTE. If a nativeDeclaration type is given it shall fulfill the characteristic given by basetypeEncoding and baseType Size. This is required to ensure the consistent handling and interpretation by software components, RTE, COM and MCM systems.

        A None value is a no-op and does not overwrite an existing nativeDeclaration.
        """
        if value is not None:
            self.nativeDeclaration = value
        return self


class BaseType(ARElement, ABC):
    """
    This abstract meta-class represents the ability to specify a platform dependent base type.
    """

    # BaseType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.26, p.291
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseTypeDefinition     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseTypeDefinition     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BaseType:
            raise TypeError("BaseType is an abstract class.")

        super().__init__(parent, short_name)

        # This is the actual definition of the base type.
        self.baseTypeDefinition: BaseTypeDirectDefinition = BaseTypeDirectDefinition()

    def getBaseTypeDefinition(self) -> BaseTypeDirectDefinition:
        """
        This is the actual definition of the base type.
        """
        return self.baseTypeDefinition

    def setBaseTypeDefinition(self, value: Optional[BaseTypeDirectDefinition]) -> "BaseType":
        """
        This is the actual definition of the base type.

        A None value is a no-op and does not overwrite an existing baseTypeDefinition.
        """
        if value is not None:
            self.baseTypeDefinition = value
        return self


class SwBaseType(BaseType):
    """
    This meta-class represents a base type used within ECU software.
    """

    # SwBaseType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.22, p.290
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
