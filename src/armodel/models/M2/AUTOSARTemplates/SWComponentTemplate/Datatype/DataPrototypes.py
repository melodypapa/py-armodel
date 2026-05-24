"""
This module contains classes for representing AUTOSAR data prototypes
in the SWComponentTemplate module. It includes various types of data
prototypes such as variable, parameter, and composite element prototypes
used in software components.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TRefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype

class DataPrototype(AtpPrototype, ABC):
    """
    Abstract base class for all AUTOSAR data prototypes within software
    components.
    """

    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == DataPrototype:
            raise TypeError("DataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        self.swDataDefProps: SwDataDefProps = None

    def getSwDataDefProps(self):
        """
        Gets the software data definition properties.

        Returns:
            SwDataDefProps: The software data definition properties
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        """
        Sets the software data definition properties.

        Args:
            value: The software data definition properties to set

        Returns:
            self for method chaining
        """
        self.swDataDefProps = value
        return self

class AutosarDataPrototype(DataPrototype, ABC):
    """
    Abstract base class for AUTOSAR data prototypes that have a type
    reference (typeTRef).
    """

    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == AutosarDataPrototype:
            raise TypeError("AutosarDataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        self.typeTRef: TRefType = None

    def getTypeTRef(self):
        """
        Gets the type reference.

        Returns:
            TRefType: The type reference
        """
        return self.typeTRef

    def setTypeTRef(self, value):
        """
        Sets the type reference.

        Args:
            value: The type reference to set

        Returns:
            self for method chaining
        """
        self.typeTRef = value
        return self

class VariableDataPrototype(AutosarDataPrototype):
    """
    A data prototype that represents a variable data element with an
    initial value.
    """

    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue: ValueSpecification = None

    def getInitValue(self):
        """
        Gets the initial value.

        Returns:
            ValueSpecification: The initial value
        """
        return self.initValue

    def setInitValue(self, value):
        """
        Sets the initial value.

        Args:
            value: The initial value to set

        Returns:
            self for method chaining
        """
        self.initValue = value
        return self

class ApplicationCompositeElementDataPrototype(DataPrototype, ABC):
    """
    Abstract base class for data prototypes that represent elements within
    an application composite data type.
    """

    def __init__(self, parent:ARObject, short_name: str):
        if type(self) == ApplicationCompositeElementDataPrototype:
            raise TypeError("ApplicationCompositeElementDataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        self.typeTRef: RefType = None

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self


class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    """
    An element of an application array data type defining the array
    element properties including size handling and index data type.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arraySizeHandling = None
        self.arraySizeSemantics = None
        self.indexDataTypeRef: RefType = None
        self.maxNumberOfElements: PositiveInteger = None

    def getArraySizeHandling(self):
        """
        Gets the array size handling mode.

        Returns:
            The array size handling mode
        """
        return self.arraySizeHandling

    def setArraySizeHandling(self, value):
        """
        Sets the array size handling mode.

        Args:
            value: The array size handling mode to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arraySizeHandling = value
        return self

    def getArraySizeSemantics(self):
        """
        Gets the array size semantics.

        Returns:
            The array size semantics
        """
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value):
        """
        Sets the array size semantics.

        Args:
            value: The array size semantics to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getIndexDataTypeRef(self):
        """
        Gets the index data type reference.

        Returns:
            RefType: The index data type reference
        """
        return self.indexDataTypeRef

    def setIndexDataTypeRef(self, value):
        """
        Sets the index data type reference.

        Args:
            value: The index data type reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.indexDataTypeRef = value
        return self

    def getMaxNumberOfElements(self):
        """
        Gets the maximum number of array elements.

        Returns:
            PositiveInteger: The maximum number of elements
        """
        return self.maxNumberOfElements

    def setMaxNumberOfElements(self, value):
        """
        Sets the maximum number of array elements.

        Args:
            value: The maximum number of elements to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxNumberOfElements = value
        return self

class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    """
    An element of an application record data type defining a field within
    the record structure.
    """

    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.isOptional = None

    def getIsOptional(self):
        """
        Gets whether this record element is optional.

        Returns:
            Whether the element is optional
        """
        return self.isOptional

    def setIsOptional(self, value):
        """
        Sets whether this record element is optional.

        Args:
            value: The optional flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.isOptional = value
        return self


class ParameterDataPrototype(AutosarDataPrototype):
    """
    A data prototype that represents a parameter data element with an
    initial value.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue: ValueSpecification = None

    def getInitValue(self):
        """
        Gets the initial value.

        Returns:
            ValueSpecification: The initial value
        """
        return self.initValue

    def setInitValue(self, value):
        """
        Sets the initial value.

        Args:
            value: The initial value to set

        Returns:
            self for method chaining
        """
        self.initValue = value
        return self
