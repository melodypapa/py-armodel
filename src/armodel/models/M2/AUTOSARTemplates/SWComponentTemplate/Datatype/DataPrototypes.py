"""
This module contains classes for representing AUTOSAR data prototypes
in the SWComponentTemplate module. It includes various types of data
prototypes such as variable, parameter, and composite element prototypes
used in software components.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TRefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ArraySizeHandlingEnum


class DataPrototype(AtpPrototype, ABC):
    """
    Base class for prototypical roles of any data type.
    """

    # DataPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.28, p.306
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSwDataDefProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwDataDefProps       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DataPrototype:
            raise TypeError("DataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        # This property allows to specify data definition properties which apply on data prototype level. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps
        self.swDataDefProps: Optional[SwDataDefProps] = None

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        This property allows to specify data definition properties which apply on data prototype level.

        Returns:
            Optional[SwDataDefProps]: The swDataDefProps
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "DataPrototype":
        """
        This property allows to specify data definition properties which apply on data prototype level. A None value is a no-op and does not overwrite an existing swDataDefProps.

        Args:
            value: The swDataDefProps to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swDataDefProps = value
        return self


class AutosarDataPrototype(DataPrototype, ABC):
    """
    Base class for prototypical roles of an AutosarDataType.
    """

    # AutosarDataPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.29, p.306
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTypeTRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTypeTRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AutosarDataPrototype:
            raise TypeError("AutosarDataPrototype is an abstract class.")

        super().__init__(parent, short_name)

        # This represents the corresponding data type. Stereotypes: isOfType
        self.typeTRef: Optional[TRefType] = None

    def getTypeTRef(self) -> Optional[TRefType]:
        """
        This represents the corresponding data type.

        Returns:
            Optional[TRefType]: The typeTRef
        """
        return self.typeTRef

    def setTypeTRef(self, value: Optional[TRefType]) -> "AutosarDataPrototype":
        """
        This represents the corresponding data type. A None value is a no-op and does not overwrite an existing typeTRef.

        Args:
            value: The typeTRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.typeTRef = value
        return self


class VariableDataPrototype(AutosarDataPrototype):
    """
    A data prototype that represents a variable data element with an
    initial value.
    """

    # VariableDataPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitValue                 [x] impl  [x] docstring  [ ] test
    # [ ] setInitValue                 [x] impl  [x] docstring  [ ] test

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


class ApplicationCompositeElementDataPrototype(DataPrototype, ABC):
    """
    Abstract base class for data prototypes that represent elements within
    an application composite data type.
    """

    # ApplicationCompositeElementDataPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTypeTRef                  [x] impl  [ ] docstring  [ ] test
    # [ ] setTypeTRef                  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ApplicationCompositeElementDataPrototype:
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
    Describes the properties of the elements of an application array data type.
    """

    # ApplicationArrayElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.9, p.252
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArraySizeHandling    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArraySizeHandling    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getArraySizeSemantics   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArraySizeSemantics   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIndexDataTypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIndexDataTypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxNumberOfElements  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxNumberOfElements  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The way how the size of the array is handled.
        self.arraySizeHandling: Optional[ArraySizeHandlingEnum] = None

        # This attribute controls how the information about the array size shall be interpreted.
        self.arraySizeSemantics: Optional[ArraySizeSemanticsEnum] = None

        # This reference can be taken to assign a CompuMethod of category TEXTTABLE to the array. The texttable entries associate a textual value to an index number such that the element with that index number is represented by a symbolic name.
        self.indexDataTypeRef: Optional[RefType] = None

        # The maximum number of elements that the array can contain. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.maxNumberOfElements: Optional[PositiveInteger] = None

    def getArraySizeHandling(self) -> Optional[ArraySizeHandlingEnum]:
        """
        The way how the size of the array is handled.

        Returns:
            Optional[ArraySizeHandlingEnum]: The arraySizeHandling
        """
        return self.arraySizeHandling

    def setArraySizeHandling(self, value: Optional[ArraySizeHandlingEnum]) -> "ApplicationArrayElement":
        """
        The way how the size of the array is handled. A None value is a no-op and does not overwrite an existing arraySizeHandling.

        Args:
            value: The arraySizeHandling to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arraySizeHandling = value
        return self

    def getArraySizeSemantics(self) -> Optional[ArraySizeSemanticsEnum]:
        """
        This attribute controls how the information about the array size shall be interpreted.

        Returns:
            Optional[ArraySizeSemanticsEnum]: The arraySizeSemantics
        """
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value: Optional[ArraySizeSemanticsEnum]) -> "ApplicationArrayElement":
        """
        This attribute controls how the information about the array size shall be interpreted. A None value is a no-op and does not overwrite an existing arraySizeSemantics.

        Args:
            value: The arraySizeSemantics to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getIndexDataTypeRef(self) -> Optional[RefType]:
        """
        This reference can be taken to assign a CompuMethod of category TEXTTABLE to the array. The texttable entries associate a textual value to an index number such that the element with that index number is represented by a symbolic name.

        Returns:
            Optional[RefType]: The indexDataType reference
        """
        return self.indexDataTypeRef

    def setIndexDataTypeRef(self, value: Optional[RefType]) -> "ApplicationArrayElement":
        """
        This reference can be taken to assign a CompuMethod of category TEXTTABLE to the array. The texttable entries associate a textual value to an index number such that the element with that index number is represented by a symbolic name. A None value is a no-op and does not overwrite an existing indexDataTypeRef.

        Args:
            value: The indexDataType reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.indexDataTypeRef = value
        return self

    def getMaxNumberOfElements(self) -> Optional[PositiveInteger]:
        """
        The maximum number of elements that the array can contain.

        Returns:
            Optional[PositiveInteger]: The maxNumberOfElements
        """
        return self.maxNumberOfElements

    def setMaxNumberOfElements(self, value: Optional[PositiveInteger]) -> "ApplicationArrayElement":
        """
        The maximum number of elements that the array can contain. A None value is a no-op and does not overwrite an existing maxNumberOfElements.

        Args:
            value: The maxNumberOfElements to set

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

    # ApplicationRecordElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIsOptional                [x] impl  [x] docstring  [ ] test
    # [ ] setIsOptional                [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
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
    A ParameterDataPrototype represents a formalized generic piece of information that is typically immutable by the application software layer, but mutable by measurement and calibration tools. ParameterDataPrototype is used in various contexts and the specific context gives the otherwise generic ParameterDataPrototype a dedicated semantics.
    """

    # ParameterDataPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.32, p.310
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getInitValue            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInitValue            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies initial value(s) of the ParameterDataPrototype
        self.initValue: Optional[ValueSpecification] = None

    def getInitValue(self) -> Optional[ValueSpecification]:
        """
        Specifies initial value(s) of the ParameterDataPrototype

        Returns:
            Optional[ValueSpecification]: The initValue
        """
        return self.initValue

    def setInitValue(self, value: Optional[ValueSpecification]) -> "ParameterDataPrototype":
        """
        Specifies initial value(s) of the ParameterDataPrototype A None value is a no-op and does not overwrite an existing initValue.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.initValue = value
        return self
