"""
This module contains classes for representing AUTOSAR value specification structures
in the CommonStructure module. Value specifications define how values are specified
for initializing data objects in AUTOSAR models, including various forms like
numerical, text, array, record, and application-specific value specifications.
"""

from __future__ import annotations

from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    AREnum as AREnum,
    Identifier,
    Integer,
    PositiveInteger,
    VerbatimString,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


class ValueSpecification(ARObject, ABC):
    """
    Base class for expressions leading to a value which can be used to initialize a data object.
    """

    # ValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.109, p.433
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getShortLabel                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setShortLabel                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is ValueSpecification:
            raise TypeError("ValueSpecification is an abstract class.")

        super().__init__()

        # This can be used to identify particular value specifications for human readers, for example elements of a record type.
        self.shortLabel: Optional[Identifier] = None

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This can be used to identify particular value specifications for human readers, for example elements of a record type.
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "ValueSpecification":
        """
        This can be used to identify particular value specifications for human readers, for example elements of a record type.
        A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self


class CompositeValueSpecification(ValueSpecification, ABC):
    """
    Abstract base class for value specifications that have a composite form.
    This class serves as a base for value specifications that contain multiple elements or components.
    Subclasses include ArrayValueSpecification and RecordValueSpecification.
    """

    # CompositeValueSpecification method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the CompositeValueSpecification base class.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is CompositeValueSpecification:
            raise TypeError("CompositeValueSpecification is an abstract class.")

        super().__init__()


class AbstractRuleBasedValueSpecification(ValueSpecification, ABC):
    """
    This represents an abstract base class for all rule-based value specifications.
    """

    # AbstractRuleBasedValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.128, p.462
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is AbstractRuleBasedValueSpecification:
            raise TypeError("AbstractRuleBasedValueSpecification is an abstract class.")
        super().__init__()


class CompositeRuleBasedValueArgument(AbstractRuleBasedValueSpecification):
    """
    Abstract base class for value specifications that can be used for compound primitive data types.
    This class serves as the base for specialized value specifications that handle complex data types.
    Subclasses include ApplicationRuleBasedValueSpecification and ApplicationValueSpecification.
    """

    # CompositeRuleBasedValueArgument method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        """
        Initializes the CompositeRuleBasedValueArgument base class.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is CompositeRuleBasedValueArgument:
            raise TypeError("CompositeRuleBasedValueArgument is an abstract class.")

        super().__init__()


class ApplicationValueSpecification(CompositeRuleBasedValueArgument, ValueSpecification):
    """
    Represents values for DataPrototypes typed by ApplicationDataTypes, including compound primitives.
    For further details refer to ASAM CDF 2.0. This class corresponds to some extent with
    SW-INSTANCE in ASAM CDF 2.0.
    Base classes: ARObject, CompositeRuleBasedValueArgument, ValueSpecification
    """

    # ApplicationValueSpecification method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getCategory                  [x] impl  [x] docstring  [x] test
    # [x] setCategory                  [x] impl  [x] docstring  [x] test
    # [x] getSwAxisCont                [x] impl  [x] docstring  [x] test
    # [x] setSwAxisCont                [x] impl  [x] docstring  [x] test
    # [x] getSwValueCont               [x] impl  [x] docstring  [x] test
    # [x] setSwValueCont               [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the ApplicationValueSpecification with default values.
        """
        CompositeRuleBasedValueArgument.__init__(self)
        ValueSpecification.__init__(self)

        # Category of this application value specification
        self.category = None
        # Software axis content for this value specification
        self.swAxisCont = []
        # Software value content for this value specification
        self.swValueCont = None

    def getCategory(self):
        """
        Gets the category of this application value specification.

        Returns:
            The category
        """
        return self.category

    def setCategory(self, value):
        """
        Sets the category of this application value specification.
        Only sets the value if it is not None.

        Args:
            value: The category to set

        Returns:
            self for method chaining
        """
        self.category = value
        return self

    def getSwAxisCont(self):
        """
        Gets the software axis content for this value specification.

        Returns:
            The software axis content
        """
        return self.swAxisCont

    def setSwAxisCont(self, value):
        """
        Sets the software axis content for this value specification.
        Only sets the value if it is not None.

        Args:
            value: The software axis content to set

        Returns:
            self for method chaining
        """
        self.swAxisCont = value
        return self

    def getSwValueCont(self):
        """
        Gets the software value content for this value specification.

        Returns:
            The software value content
        """
        return self.swValueCont

    def setSwValueCont(self, value):
        """
        Sets the software value content for this value specification.
        Only sets the value if it is not None.

        Args:
            value: The software value content to set

        Returns:
            self for method chaining
        """
        self.swValueCont = value
        return self


class RecordValueSpecification(CompositeValueSpecification):
    """
    Specifies the values for a record in AUTOSAR models.
    This class contains multiple field value specifications that make up a record structure.
    Base classes: ARObject, CompositeValueSpecification, ValueSpecification
    """

    # RecordValueSpecification method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] addField                     [x] impl  [x] docstring  [x] test
    # [x] getFields                    [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the RecordValueSpecification with default values.
        """
        super().__init__()

        # List of field value specifications in this record
        self.fields = []

    def addField(self, field: ValueSpecification):
        """
        Adds a field value specification to this record.

        Args:
            field: The field value specification to add
        """
        self.fields.append(field)

    def getFields(self) -> List[ValueSpecification]:
        """
        Gets the list of field value specifications in this record.

        Returns:
            List of ValueSpecification instances
        """
        return self.fields


class TextValueSpecification(ValueSpecification):
    """
    Represents a text value specification in AUTOSAR models.
    This class contains a literal text value for initializing data objects.
    """

    # TextValueSpecification method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getValue                     [x] impl  [x] docstring  [x] test
    # [x] setValue                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the TextValueSpecification with default values.
        """
        super().__init__()

        # Text value for this specification
        self.value: ARLiteral = None

    def getValue(self):
        """
        Gets the text value for this specification.

        Returns:
            ARLiteral: The text value
        """
        return self.value

    def setValue(self, value):
        """
        Sets the text value for this specification.
        Only sets the value if it is not None.

        Args:
            value: The text value to set

        Returns:
            self for method chaining
        """
        self.value = value
        return self


class NumericalValueSpecification(ValueSpecification):
    """
    Represents a numerical value specification in AUTOSAR models.
    This class contains a numerical value for initializing data objects.
    """

    # NumericalValueSpecification method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getValue                     [x] impl  [x] docstring  [x] test
    # [x] setValue                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the NumericalValueSpecification with default values.
        """
        super().__init__()

        # Numerical value for this specification
        self.value: ARNumerical = None

    def getValue(self) -> ARNumerical:
        """
        Gets the numerical value for this specification.

        Returns:
            ARNumerical: The numerical value
        """
        return self.value

    def setValue(self, value: ARNumerical):
        """
        Sets the numerical value for this specification.
        Only sets the value if it is not None.

        Args:
            value: The numerical value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


class ArrayValueSpecification(ValueSpecification):
    """
    Represents an array value specification in AUTOSAR models.
    This class contains multiple element value specifications that make up an array structure.
    """

    # ArrayValueSpecification method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getIntendedPartialInitializationCount [x] impl  [x] docstring  [x] test
    # [x] setIntendedPartialInitializationCount [x] impl  [x] docstring  [x] test
    # [x] addElement                   [x] impl  [x] docstring  [x] test
    # [x] getElements                  [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the ArrayValueSpecification with default values.
        """
        super().__init__()

        # List of element value specifications in this array
        self.element: List[ValueSpecification] = []
        # Intended partial initialization count for this array
        self.intendedPartialInitializationCount = None

    def getIntendedPartialInitializationCount(self):
        """
        Gets the intended partial initialization count for this array.

        Returns:
            The intended partial initialization count
        """
        return self.intendedPartialInitializationCount

    def setIntendedPartialInitializationCount(self, value):
        """
        Sets the intended partial initialization count for this array.
        Only sets the value if it is not None.

        Args:
            value: The intended partial initialization count to set

        Returns:
            self for method chaining
        """
        self.intendedPartialInitializationCount = value
        return self

    def addElement(self, element: ValueSpecification):
        """
        Adds an element value specification to this array.

        Args:
            element: The element value specification to add
        """
        self.element.append(element)

    def getElements(self) -> List[ValueSpecification]:
        """
        Gets the list of element value specifications in this array.

        Returns:
            List of ValueSpecification instances
        """
        return self.element


class ConstantSpecification(ARElement):
    """
    Represents a constant specification in AUTOSAR models.
    This class contains a value specification for defining constants in AUTOSAR systems.
    """

    # ConstantSpecification method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getValueSpec                 [x] impl  [x] docstring  [x] test
    # [x] setValueSpec                 [x] impl  [x] docstring  [x] test

    def __init__(self, parent, short_name):
        """
        Initializes the ConstantSpecification with a parent and short name.

        Args:
            parent: The parent ARObject that contains this constant specification
            short_name: The unique short name of this constant specification
        """
        super().__init__(parent, short_name)

        # Value specification for this constant
        self.valueSpec: ValueSpecification = None

    def getValueSpec(self):
        """
        Gets the value specification for this constant.

        Returns:
            ValueSpecification: The value specification
        """
        return self.valueSpec

    def setValueSpec(self, value):
        """
        Sets the value specification for this constant.
        Only sets the value if it is not None.

        Args:
            value: The value specification to set

        Returns:
            self for method chaining
        """
        self.valueSpec = value
        return self


class ConstantReference(ValueSpecification):
    """
    Represents a constant reference in AUTOSAR models.
    This class contains a reference to a constant for use in value specifications.
    """

    # ConstantReference method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getConstantRef               [x] impl  [x] docstring  [x] test
    # [x] setConstantRef               [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the ConstantReference with default values.
        """
        super().__init__()

        # Reference to the constant for this specification
        self.constantRef: RefType = None

    def getConstantRef(self):
        """
        Gets the reference to the constant for this specification.

        Returns:
            RefType: The constant reference
        """
        return self.constantRef

    def setConstantRef(self, value):
        """
        Sets the reference to the constant for this specification.
        Only sets the value if it is not None.

        Args:
            value: The constant reference to set

        Returns:
            self for method chaining
        """
        self.constantRef = value
        return self


class ApplicationRuleBasedValueSpecification(CompositeRuleBasedValueArgument):
    """
    This meta-class represents rule based values for DataPrototypes typed by
    ApplicationDataTypes (ApplicationArrayDataType or a compound
    ApplicationPrimitiveDataType which also boils down to an array-nature).
    """

    # ApplicationRuleBasedValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.6, p.302
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getCategory                  [x] impl  [x] docstring  [x] test
    # [x] setCategory                  [x] impl  [x] docstring  [x] test
    # [x] addSwAxisCont                [x] impl  [x] docstring  [x] test
    # [x] getSwAxisConts               [x] impl  [x] docstring  [x] test
    # [x] getSwValueCont               [x] impl  [x] docstring  [x] test
    # [x] setSwValueCont               [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes an ApplicationRuleBasedValueSpecification instance with default values.
        """
        super().__init__()

        # This represents the category of the RuleBasedValueSpecification.
        # For each ApplicationRuleBasedValueSpecification, attribute category shall exist
        # at the time when the RTE is generated. [constr_1922]
        self.category: Optional[Identifier] = None

        # This represents the axis values of a Compound Primitive Data Type (curve or map).
        # The first swAxisCont describes the x-axis, the second swAxisCont describes the y-axis,
        # the third swAxisCont describes the z-axis. In addition to this, the axis can be
        # denoted in swAxisIndex. The value of ApplicationRuleBasedValueSpecification.swAxisCont.category
        # shall not be set to fixAXIS. [constr_10041]
        self.swAxisConts: List[RuleBasedAxisCont] = []

        # This represents the values of an array or Compound Primitive Data Type.
        self.swValueCont: Optional[RuleBasedValueCont] = None

    def getCategory(self) -> Optional[Identifier]:
        """
        Gets the category of the RuleBasedValueSpecification.
        For each ApplicationRuleBasedValueSpecification, attribute category shall exist
        at the time when the RTE is generated. [constr_1922]

        Returns:
            Optional[Identifier]: The category, or None if not set
        """
        return self.category

    def setCategory(self, value: Optional[Identifier]) -> "ApplicationRuleBasedValueSpecification":
        """
        Sets the category of the RuleBasedValueSpecification.
        For each ApplicationRuleBasedValueSpecification, attribute category shall exist
        at the time when the RTE is generated. [constr_1922]
        A None value is a no-op and does not overwrite an existing category.

        Args:
            value: The category to set

        Returns:
            ApplicationRuleBasedValueSpecification: self for method chaining
        """
        if value is not None:
            self.category = value
        return self

    def addSwAxisCont(self, value: Optional[RuleBasedAxisCont]) -> "ApplicationRuleBasedValueSpecification":
        """
        Adds the axis values of a Compound Primitive Data Type (curve or map).
        The first swAxisCont describes the x-axis, the second swAxisCont describes the y-axis,
        the third swAxisCont describes the z-axis. In addition to this, the axis can be
        denoted in swAxisIndex. The value of ApplicationRuleBasedValueSpecification.swAxisCont.category
        shall not be set to fixAXIS. [constr_10041]
        A None value is a no-op and is not appended.

        Args:
            value: The RuleBasedAxisCont instance to add

        Returns:
            ApplicationRuleBasedValueSpecification: self for method chaining
        """
        if value is not None:
            self.swAxisConts.append(value)
        return self

    def getSwAxisConts(self) -> List[RuleBasedAxisCont]:
        """
        Gets the axis values of this rule-based value specification.
        The first swAxisCont describes the x-axis, the second swAxisCont describes the y-axis,
        the third swAxisCont describes the z-axis. In addition to this, the axis can be
        denoted in swAxisIndex. The value of ApplicationRuleBasedValueSpecification.swAxisCont.category
        shall not be set to fixAXIS. [constr_10041]

        Returns:
            List[RuleBasedAxisCont]: The axis values
        """
        return self.swAxisConts

    def getSwValueCont(self) -> Optional[RuleBasedValueCont]:
        """
        Gets the values of an array or Compound Primitive Data Type.

        Returns:
            Optional[RuleBasedValueCont]: The value content, or None if not set
        """
        return self.swValueCont

    def setSwValueCont(self, value: Optional[RuleBasedValueCont]) -> "ApplicationRuleBasedValueSpecification":
        """
        Sets the values of an array or Compound Primitive Data Type.
        A None value is a no-op and does not overwrite an existing value content.

        Args:
            value: The RuleBasedValueCont instance to set

        Returns:
            ApplicationRuleBasedValueSpecification: self for method chaining
        """
        if value is not None:
            self.swValueCont = value
        return self


class CompositeRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    This meta-class represents rule-based values for DataPrototypes typed by composite AutosarDataTypes.
    """

    # CompositeRuleBasedValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.135, p.471
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addArgument                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getArguments                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addCompoundPrimitiveArgument    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCompoundPrimitiveArguments   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMaxSizeToFill                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxSizeToFill                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRule                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRule                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the collection of aggregated Value Specifications. The last ValueSpecification in the collection shall be taken to execute the filling rule. Tags: xml.sequenceOffset=30
        self.arguments: List[CompositeValueSpecification] = []

        # This represents the collection of aggregated Value Specifications for compound primitive data type. The last ValueSpecification in the collection shall be taken to execute the filling rule. Tags: xml.sequenceOffset=35
        self.compoundPrimitiveArguments: List[CompositeRuleBasedValueArgument] = []

        # If a rule is chosen which does not fill until the end, this determines until which size the rule shall fill the values. Tags: xml.sequenceOffset=40
        self.maxSizeToFill: Optional[PositiveInteger] = None

        # This denotes the name of the rule of the RuleBasedValue Specification. The rule determines the calculation specification according which the arguments are used to calculated the values. Tags: xml.sequenceOffset=20
        self.rule: Optional[Identifier] = None

    def addArgument(self, argument: CompositeValueSpecification) -> "CompositeRuleBasedValueSpecification":
        """
        This represents the collection of aggregated Value Specifications. The last ValueSpecification in the collection shall be taken to execute the filling rule. Tags: xml.sequenceOffset=30
        A None value is a no-op and does not append anything.
        """
        if argument is not None:
            self.arguments.append(argument)
        return self

    def getArguments(self) -> List[CompositeValueSpecification]:
        """
        This represents the collection of aggregated Value Specifications. The last ValueSpecification in the collection shall be taken to execute the filling rule. Tags: xml.sequenceOffset=30
        """
        return self.arguments

    def addCompoundPrimitiveArgument(self, argument: CompositeRuleBasedValueArgument) -> "CompositeRuleBasedValueSpecification":
        """
        This represents the collection of aggregated Value Specifications for compound primitive data type. The last ValueSpecification in the collection shall be taken to execute the filling rule. Tags: xml.sequenceOffset=35
        A None value is a no-op and does not append anything.
        """
        if argument is not None:
            self.compoundPrimitiveArguments.append(argument)
        return self

    def getCompoundPrimitiveArguments(self) -> List[CompositeRuleBasedValueArgument]:
        """
        This represents the collection of aggregated Value Specifications for compound primitive data type. The last ValueSpecification in the collection shall be taken to execute the filling rule. Tags: xml.sequenceOffset=35
        """
        return self.compoundPrimitiveArguments

    def getMaxSizeToFill(self) -> Optional[PositiveInteger]:
        """
        If a rule is chosen which does not fill until the end, this determines until which size the rule shall fill the values. Tags: xml.sequenceOffset=40
        """
        return self.maxSizeToFill

    def setMaxSizeToFill(self, value: Optional[PositiveInteger]) -> "CompositeRuleBasedValueSpecification":
        """
        If a rule is chosen which does not fill until the end, this determines until which size the rule shall fill the values. Tags: xml.sequenceOffset=40
        A None value is a no-op and does not overwrite an existing maxSizeToFill.
        """
        if value is not None:
            self.maxSizeToFill = value
        return self

    def getRule(self) -> Optional[Identifier]:
        """
        This denotes the name of the rule of the RuleBasedValue Specification. The rule determines the calculation specification according which the arguments are used to calculated the values. Tags: xml.sequenceOffset=20
        """
        return self.rule

    def setRule(self, value: Optional[Identifier]) -> "CompositeRuleBasedValueSpecification":
        """
        This denotes the name of the rule of the RuleBasedValue Specification. The rule determines the calculation specification according which the arguments are used to calculated the values. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing rule.
        """
        if value is not None:
            self.rule = value
        return self


class ConstantSpecificationMapping(ARObject):
    """
    This meta-class is used to create an association of two ConstantSpecifications. One Constant Specification is supposed to be defined in the application domain while the other should be defined in the implementation domain. Hence the ConstantSpecificationMapping needs to be used where a ConstantSpecification defined in one domain needs to be associated to a ConstantSpecification in the other domain. This information is crucial for the RTE generator.
    """

    # ConstantSpecificationMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.118, p.443
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getApplConstantRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setApplConstantRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplConstantRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setImplConstantRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # A ConstantSpecification defined in the application domain.
        self.applConstantRef: Optional[RefType] = None

        # A ConstantSpecification defined in the implementation domain.
        self.implConstantRef: Optional[RefType] = None

    def getApplConstantRef(self) -> Optional[RefType]:
        """
        A ConstantSpecification defined in the application domain.

        Returns:
            Optional[RefType]: A ConstantSpecification defined in the application domain., or None if not set
        """
        return self.applConstantRef

    def setApplConstantRef(self, value: Optional[RefType]) -> "ConstantSpecificationMapping":
        """
        A ConstantSpecification defined in the application domain.
        A None value is a no-op and does not overwrite an existing applConstantRef.

        Args:
            value: A ConstantSpecification defined in the application domain. to set

        Returns:
            ConstantSpecificationMapping: self for method chaining
        """
        if value is not None:
            self.applConstantRef = value
        return self

    def getImplConstantRef(self) -> Optional[RefType]:
        """
        A ConstantSpecification defined in the implementation domain.

        Returns:
            Optional[RefType]: A ConstantSpecification defined in the implementation domain., or None if not set
        """
        return self.implConstantRef

    def setImplConstantRef(self, value: Optional[RefType]) -> "ConstantSpecificationMapping":
        """
        A ConstantSpecification defined in the implementation domain.
        A None value is a no-op and does not overwrite an existing implConstantRef.

        Args:
            value: A ConstantSpecification defined in the implementation domain. to set

        Returns:
            ConstantSpecificationMapping: self for method chaining
        """
        if value is not None:
            self.implConstantRef = value
        return self


class ConstantSpecificationMappingSet(ARObject):
    """
    Represents a set of constant specification mappings.
    """

    # ConstantSpecificationMappingSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addMapping                   [x] impl  [ ] docstring  [ ] test
    # [ ] getMappings                  [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()
        self.mappings = []

    def addMapping(self, mapping):
        self.mappings.append(mapping)

    def getMappings(self):
        return self.mappings


class NotAvailableValueSpecification(ValueSpecification):
    """
    This meta-class provides the ability to specify a ValueSpecification to state that the respective element is not available. This ability is needed to support the existence of ApplicationRecordElements where attribute isOptional ist set to the value true.
    """

    # NotAvailableValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.116, p.440
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefaultPattern         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultPattern         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The content of this attribute shall be used to initialize gaps in the memory occupied by a structured data type in the case that an NotAvailableValueSpecification is used. Note that this pattern is only applied during initialization!
        self.defaultPattern: Optional[PositiveInteger] = None

    def getDefaultPattern(self) -> Optional[PositiveInteger]:
        """
        The content of this attribute shall be used to initialize gaps in the memory occupied by a structured data type in the case that an NotAvailableValueSpecification is used. Note that this pattern is only applied during initialization!

        Returns:
            Optional[PositiveInteger]: The content of this attribute shall be used to initialize gaps in the memory occupied by a structured data type in the case that an NotAvailableValueSpecification is used., or None if not set
        """
        return self.defaultPattern

    def setDefaultPattern(self, value: Optional[PositiveInteger]) -> "NotAvailableValueSpecification":
        """
        The content of this attribute shall be used to initialize gaps in the memory occupied by a structured data type in the case that an NotAvailableValueSpecification is used. Note that this pattern is only applied during initialization!
        A None value is a no-op and does not overwrite an existing defaultPattern.

        Args:
            value: The content of this attribute shall be used to initialize gaps in the memory occupied by a structured data type in the case that an NotAvailableValueSpecification is used. to set

        Returns:
            NotAvailableValueSpecification: self for method chaining
        """
        if value is not None:
            self.defaultPattern = value
        return self


class NumericalOrText(ARObject):
    """
    This meta-class represents the ability to yield either a numerical or a string. A typical use case is that
    two or more instances of this meta-class are aggregated with a VariationPoint where some instances yield
    strings while other instances yield numerical depending on the resolution of the binding expression.
    Within the context of one NumericalOrText, either the attribute vf or the attribute vt shall be defined.
    The existence of both attributes at the same time is not permitted. [constr_1243]
    """

    # NumericalOrText method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.42, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getVf                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVf                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVt                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVt                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute represents the ability to provide a numerical value.
        # The latest binding time of the VariationPoint shall be preCompileTime.
        self.vf: Optional[ARNumerical] = None

        # This attribute represents the ability to provide a textual value.
        self.vt: Optional[ARLiteral] = None

    def getVf(self) -> Optional[ARNumerical]:
        """
        This attribute represents the ability to provide a numerical value.
        The latest binding time of the VariationPoint shall be preCompileTime.

        Returns:
            Optional[ARNumerical]: The numerical value, or None if not set
        """
        return self.vf

    def setVf(self, value: Optional[ARNumerical]) -> "NumericalOrText":
        """
        This attribute represents the ability to provide a numerical value.
        The latest binding time of the VariationPoint shall be preCompileTime.
        A None value is a no-op and does not overwrite an existing vf.

        Args:
            value: The numerical value to set

        Returns:
            NumericalOrText: self for method chaining
        """
        if value is not None:
            self.vf = value
        return self

    def getVt(self) -> Optional[ARLiteral]:
        """
        This attribute represents the ability to provide a textual value.

        Returns:
            Optional[ARLiteral]: The textual value, or None if not set
        """
        return self.vt

    def setVt(self, value: Optional[ARLiteral]) -> "NumericalOrText":
        """
        This attribute represents the ability to provide a textual value.
        A None value is a no-op and does not overwrite an existing vt.

        Args:
            value: The textual value to set

        Returns:
            NumericalOrText: self for method chaining
        """
        if value is not None:
            self.vt = value
        return self


class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    This meta-class is used to support a rule-based initialization approach for data types with an array-nature (ImplementationDataType of category ARRAY).
    """

    # NumericalRuleBasedValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.132, p.467
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRuleBasedValues  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRuleBasedValues  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the rule based value specification for the array.
        self.ruleBasedValues: Optional[RuleBasedValueSpecification] = None

    def getRuleBasedValues(self) -> Optional[RuleBasedValueSpecification]:
        """
        This represents the rule based value specification for the array.

        Returns:
            Optional[RuleBasedValueSpecification]: The rule based value specification, or None if not set
        """
        return self.ruleBasedValues

    def setRuleBasedValues(self, value: Optional[RuleBasedValueSpecification]) -> "NumericalRuleBasedValueSpecification":
        """
        This represents the rule based value specification for the array.
        A None value is a no-op and does not overwrite an existing ruleBasedValues.

        Args:
            value: The rule based value specification to set

        Returns:
            NumericalRuleBasedValueSpecification: self for method chaining
        """
        if value is not None:
            self.ruleBasedValues = value
        return self


class ReferenceValueSpecification(ValueSpecification):
    """
    Specifies a reference to a data prototype to be used as an initial value for a pointer in the software.
    """

    # ReferenceValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.115, p.437
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getReferenceValueRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReferenceValueRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The referenced data prototype.
        self.referenceValueRef: Optional[RefType] = None

    def getReferenceValueRef(self) -> Optional[RefType]:
        """
        The referenced data prototype.

        Returns:
            Optional[RefType]: The referenced data prototype, or None if not set
        """
        return self.referenceValueRef

    def setReferenceValueRef(self, value: Optional[RefType]) -> "ReferenceValueSpecification":
        """
        The referenced data prototype.
        A None value is a no-op and does not overwrite an existing referenceValueRef.

        Args:
            value: The referenced data prototype to set

        Returns:
            ReferenceValueSpecification: self for method chaining
        """
        if value is not None:
            self.referenceValueRef = value
        return self


class RuleArguments(ARObject):
    """
    This represents the arguments for a rule-based value specification.
    """

    # RuleArguments method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.57, p.329
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getV                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setV                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVf                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVf                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVt                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVt                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVtf                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVtf                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents a numerical value for the RuleBased ValueSpecification.
        self.v: Optional[ARNumerical] = None

        # This represents a numerical value for the RuleBased ValueSpecification which may subject to variability.
        # The latest binding time of the VariationPoint shall be pre CompileTime.
        self.vf: Optional[ARNumerical] = None

        # This represents a textual value for the RuleBasedValue Specification.
        self.vt: Optional[VerbatimString] = None

        # This aggregation represents the ability to provide a value that is either numerical or text which existence is subject to variability.
        self.vtf: Optional[NumericalOrText] = None

    def getV(self) -> Optional[ARNumerical]:
        """
        This represents a numerical value for the RuleBased ValueSpecification.

        Returns:
            Optional[ARNumerical]: The numerical value, or None if not set
        """
        return self.v

    def setV(self, value: Optional[ARNumerical]) -> "RuleArguments":
        """
        This represents a numerical value for the RuleBased ValueSpecification.
        A None value is a no-op and does not overwrite an existing v.

        Args:
            value: The numerical value to set

        Returns:
            RuleArguments: self for method chaining
        """
        if value is not None:
            self.v = value
        return self

    def getVf(self) -> Optional[ARNumerical]:
        """
        This represents a numerical value for the RuleBased ValueSpecification which may subject to variability.
        The latest binding time of the VariationPoint shall be pre CompileTime.

        Returns:
            Optional[ARNumerical]: The numerical value, or None if not set
        """
        return self.vf

    def setVf(self, value: Optional[ARNumerical]) -> "RuleArguments":
        """
        This represents a numerical value for the RuleBased ValueSpecification which may subject to variability.
        The latest binding time of the VariationPoint shall be pre CompileTime.
        A None value is a no-op and does not overwrite an existing vf.

        Args:
            value: The numerical value to set

        Returns:
            RuleArguments: self for method chaining
        """
        if value is not None:
            self.vf = value
        return self

    def getVt(self) -> Optional[VerbatimString]:
        """
        This represents a textual value for the RuleBasedValue Specification.

        Returns:
            Optional[VerbatimString]: The textual value, or None if not set
        """
        return self.vt

    def setVt(self, value: Optional[VerbatimString]) -> "RuleArguments":
        """
        This represents a textual value for the RuleBasedValue Specification.
        A None value is a no-op and does not overwrite an existing vt.

        Args:
            value: The textual value to set

        Returns:
            RuleArguments: self for method chaining
        """
        if value is not None:
            self.vt = value
        return self

    def getVtf(self) -> Optional[NumericalOrText]:
        """
        This aggregation represents the ability to provide a value that is either numerical or text which existence is subject to variability.

        Returns:
            Optional[NumericalOrText]: The value, or None if not set
        """
        return self.vtf

    def setVtf(self, value: Optional[NumericalOrText]) -> "RuleArguments":
        """
        This aggregation represents the ability to provide a value that is either numerical or text which existence is subject to variability.
        A None value is a no-op and does not overwrite an existing vtf.

        Args:
            value: The value to set

        Returns:
            RuleArguments: self for method chaining
        """
        if value is not None:
            self.vtf = value
        return self


class RuleBasedAxisCont(ARObject):
    """
    This represents the values for the axis of a compound primitive (curve, map). For standard and fix axes, SwAxisCont contains the values of the axis directly. The axis values of SwAxisCont with the category COM_AXIS, RES_AXIS are for display only. For editing and processing, only the values in the related GroupAxis are binding.
    """

    # RuleBasedAxisCont method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.130, p.464
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCategory                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setCategory                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRuleBasedValues           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRuleBasedValues           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwArraysize               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwArraysize               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwAxisIndex               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setSwAxisIndex               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUnitRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnitRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This category specifies the particular axis types: • STD_AXIS • COM_AXIS • RES_AXIS (swArraysize necessary)
        self.category: Optional[CalprmAxisCategoryEnum] = None

        # This represents the rule based value specification for the axis of a compound primitive (curve, map).
        self.ruleBasedValues: Optional[RuleBasedValueSpecification] = None

        # For multidimensional compound primitives (curve, map ...) it is necessary to know the dimensions.They are specified using swArraySize.
        self.swArraysize: Optional[ValueList] = None

        # This property allows to explicitly assign the axis contents to a particular axis. It is specified by numbers where 1 corresponds to the x-axis. It is also possible to derive the axis association from the sequence of the parent.
        self.swAxisIndex: Optional[AxisIndexType] = None

        # This represents the physical unit of the provided values.
        self.unitRef: Optional[RefType] = None

    def getCategory(self) -> Optional[CalprmAxisCategoryEnum]:
        """
        This category specifies the particular axis types: • STD_AXIS • COM_AXIS • RES_AXIS (swArraysize necessary)

        Returns:
            Optional[CalprmAxisCategoryEnum]: The axis category, or None if not set
        """
        return self.category

    def setCategory(self, value: Optional[CalprmAxisCategoryEnum]) -> "RuleBasedAxisCont":
        """
        This category specifies the particular axis types: • STD_AXIS • COM_AXIS • RES_AXIS (swArraysize necessary)
        A None value is a no-op and does not overwrite an existing category.

        Args:
            value: The axis category to set

        Returns:
            RuleBasedAxisCont: self for method chaining
        """
        if value is not None:
            self.category = value
        return self

    def getRuleBasedValues(self) -> Optional[RuleBasedValueSpecification]:
        """
        This represents the rule based value specification for the axis of a compound primitive (curve, map).

        Returns:
            Optional[RuleBasedValueSpecification]: The value specification, or None if not set
        """
        return self.ruleBasedValues

    def setRuleBasedValues(self, value: Optional[RuleBasedValueSpecification]) -> "RuleBasedAxisCont":
        """
        This represents the rule based value specification for the axis of a compound primitive (curve, map).
        A None value is a no-op and does not overwrite an existing ruleBasedValues.

        Args:
            value: The value specification to set

        Returns:
            RuleBasedAxisCont: self for method chaining
        """
        if value is not None:
            self.ruleBasedValues = value
        return self

    def getSwArraysize(self) -> Optional[ValueList]:
        """
        For multidimensional compound primitives (curve, map ...) it is necessary to know the dimensions.They are specified using swArraySize.

        Returns:
            Optional[ValueList]: The array size, or None if not set
        """
        return self.swArraysize

    def setSwArraysize(self, value: Optional[ValueList]) -> "RuleBasedAxisCont":
        """
        For multidimensional compound primitives (curve, map ...) it is necessary to know the dimensions.They are specified using swArraySize.
        A None value is a no-op and does not overwrite an existing swArraysize.

        Args:
            value: The array size to set

        Returns:
            RuleBasedAxisCont: self for method chaining
        """
        if value is not None:
            self.swArraysize = value
        return self

    def getSwAxisIndex(self) -> Optional[AxisIndexType]:
        """
        This property allows to explicitly assign the axis contents to a particular axis. It is specified by numbers where 1 corresponds to the x-axis. It is also possible to derive the axis association from the sequence of the parent.

        Returns:
            Optional[AxisIndexType]: The axis index, or None if not set
        """
        return self.swAxisIndex

    def setSwAxisIndex(self, value: Optional[AxisIndexType]) -> "RuleBasedAxisCont":
        """
        This property allows to explicitly assign the axis contents to a particular axis. It is specified by numbers where 1 corresponds to the x-axis. It is also possible to derive the axis association from the sequence of the parent.
        A None value is a no-op and does not overwrite an existing swAxisIndex.

        Args:
            value: The axis index to set

        Returns:
            RuleBasedAxisCont: self for method chaining
        """
        if value is not None:
            self.swAxisIndex = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """
        This represents the physical unit of the provided values.

        Returns:
            Optional[RefType]: The unit reference, or None if not set
        """
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]) -> "RuleBasedAxisCont":
        """
        This represents the physical unit of the provided values.
        A None value is a no-op and does not overwrite an existing unitRef.

        Args:
            value: The unit reference to set

        Returns:
            RuleBasedAxisCont: self for method chaining
        """
        if value is not None:
            self.unitRef = value
        return self


class RuleBasedValueCont(ARObject):
    """
    This represents the values of a compound primitive (CURVE, MAP, CUBOID, CUBE_4, CUBE_5, VAL_BLK) or an array.
    """

    # RuleBasedValueCont method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.58, p.330
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRuleBasedValues           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRuleBasedValues           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwArraysize               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwArraysize               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUnitRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnitRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the rule based value specification for the array or compound primitive (CURVE, MAP, CUBOID, CUBE_4, CUBE_5, VAL_BLK).
        self.ruleBasedValues: Optional[RuleBasedValueSpecification] = None

        # This attribute defines the size of each dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4, CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK.
        # For each dimension one value has to be defined, e.g. one in case of COM_AXIS and two or more in case of MAP.
        self.swArraysize: Optional[ValueList] = None

        # This represents the physical unit of the provided values.
        self.unitRef: Optional[RefType] = None

    def getRuleBasedValues(self) -> Optional[RuleBasedValueSpecification]:
        """
        This represents the rule based value specification for the array or compound primitive (CURVE, MAP, CUBOID, CUBE_4, CUBE_5, VAL_BLK).

        Returns:
            Optional[RuleBasedValueSpecification]: The value specification, or None if not set
        """
        return self.ruleBasedValues

    def setRuleBasedValues(self, value: Optional[RuleBasedValueSpecification]) -> "RuleBasedValueCont":
        """
        This represents the rule based value specification for the array or compound primitive (CURVE, MAP, CUBOID, CUBE_4, CUBE_5, VAL_BLK).
        A None value is a no-op and does not overwrite an existing ruleBasedValues.

        Args:
            value: The value specification to set

        Returns:
            RuleBasedValueCont: self for method chaining
        """
        if value is not None:
            self.ruleBasedValues = value
        return self

    def getSwArraysize(self) -> Optional[ValueList]:
        """
        This attribute defines the size of each dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4, CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK.
        For each dimension one value has to be defined, e.g. one in case of COM_AXIS and two or more in case of MAP.

        Returns:
            Optional[ValueList]: The array size, or None if not set
        """
        return self.swArraysize

    def setSwArraysize(self, value: Optional[ValueList]) -> "RuleBasedValueCont":
        """
        This attribute defines the size of each dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4, CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK.
        For each dimension one value has to be defined, e.g. one in case of COM_AXIS and two or more in case of MAP.
        A None value is a no-op and does not overwrite an existing swArraysize.

        Args:
            value: The array size to set

        Returns:
            RuleBasedValueCont: self for method chaining
        """
        if value is not None:
            self.swArraysize = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """
        This represents the physical unit of the provided values.

        Returns:
            Optional[RefType]: The unit reference, or None if not set
        """
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]) -> "RuleBasedValueCont":
        """
        This represents the physical unit of the provided values.
        A None value is a no-op and does not overwrite an existing unitRef.

        Args:
            value: The unit reference to set

        Returns:
            RuleBasedValueCont: self for method chaining
        """
        if value is not None:
            self.unitRef = value
        return self


class RuleBasedValueSpecification(ARObject):
    """
    This meta-class is used to support a rule-based initialization approach for data types with an array-nature (ApplicationArrayDataType and ImplementationDataType of category ARRAY) or a compound Application PrimitiveDataType (which also boils down to an array-nature).
    """

    # RuleBasedValueSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.59, p.331
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addArgument                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getArguments                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMaxSizeToFill             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxSizeToFill             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRule                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRule                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the arguments for the RuleBasedValue Specification.
        self.arguments: List[RuleArguments] = []

        # If a rule is chosen which does not fill until the end, this determines until which size the rule shall fill the values.
        self.maxSizeToFill: Optional[Integer] = None

        # This denotes the name of the rule of the RuleBasedValue Specification.
        # The rule determines the calculation specification according which the arguments are used to calculated the values.
        self.rule: Optional[Identifier] = None

    def addArgument(self, argument: RuleArguments) -> "RuleBasedValueSpecification":
        """
        This represents the arguments for the RuleBasedValue Specification.

        Args:
            argument: The argument to add

        Returns:
            RuleBasedValueSpecification: self for method chaining
        """
        if argument is not None:
            self.arguments.append(argument)
        return self

    def getArguments(self) -> List[RuleArguments]:
        """
        This represents the arguments for the RuleBasedValue Specification.

        Returns:
            List[RuleArguments]: The list of arguments
        """
        return self.arguments

    def getMaxSizeToFill(self) -> Optional[Integer]:
        """
        If a rule is chosen which does not fill until the end, this determines until which size the rule shall fill the values.

        Returns:
            Optional[Integer]: The max size to fill, or None if not set
        """
        return self.maxSizeToFill

    def setMaxSizeToFill(self, value: Optional[Integer]) -> "RuleBasedValueSpecification":
        """
        If a rule is chosen which does not fill until the end, this determines until which size the rule shall fill the values.
        A None value is a no-op and does not overwrite an existing maxSizeToFill.

        Args:
            value: The max size to fill

        Returns:
            RuleBasedValueSpecification: self for method chaining
        """
        if value is not None:
            self.maxSizeToFill = value
        return self

    def getRule(self) -> Optional[Identifier]:
        """
        This denotes the name of the rule of the RuleBasedValue Specification.
        The rule determines the calculation specification according which the arguments are used to calculated the values.

        Returns:
            Optional[Identifier]: The rule name, or None if not set
        """
        return self.rule

    def setRule(self, value: Optional[Identifier]) -> "RuleBasedValueSpecification":
        """
        This denotes the name of the rule of the RuleBasedValue Specification.
        The rule determines the calculation specification according which the arguments are used to calculated the values.
        A None value is a no-op and does not overwrite an existing rule.

        Args:
            value: The rule name

        Returns:
            RuleBasedValueSpecification: self for method chaining
        """
        if value is not None:
            self.rule = value
        return self
