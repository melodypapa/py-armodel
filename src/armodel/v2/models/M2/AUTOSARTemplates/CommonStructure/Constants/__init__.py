"""
This module contains classes for representing AUTOSAR value specification structures
in the CommonStructure module. Value specifications define how values are specified
for initializing data objects in AUTOSAR models, including various forms like
numerical, text, array, record, and application-specific value specifications.
"""




from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARNumerical,
    RefType,
)

__all__ = [
    'AbstractRuleBasedValueSpecification',
    'ApplicationRuleBasedValueSpecification',
    'ApplicationValueSpecification',
    'ArrayValueSpecification',
    'CompositeRuleBasedValueArgument',
    'CompositeRuleBasedValueSpecification',
    'CompositeValueSpecification',
    'ConstantReference',
    'ConstantSpecification',
    'ConstantSpecificationMapping',
    'ConstantSpecificationMappingSet',
    'NotAvailableValueSpecification',
    'NumericalOrText',
    'NumericalRuleBasedValueSpecification',
    'NumericalValueSpecification',
    'RecordValueSpecification',
    'ReferenceValueSpecification',
    'RuleArguments',
    'RuleBasedAxisCont',
    'RuleBasedValueCont',
    'RuleBasedValueSpecification',
    'TextValueSpecification',
    'ValueSpecification',
]


class ValueSpecification(ARObject, ABC):
    """
    Abstract base class for expressions leading to a value which can be used to initialize a data object.
    This class serves as the base for all value specification types in AUTOSAR models.
    Subclasses include AbstractRuleBasedValueSpecification, ApplicationValueSpecification, CompositeValueSpecification,
    ConstantReference, NotAvailableValueSpecification, NumericalValueSpecification, ReferenceValueSpecification,
    and TextValueSpecification.
    """

    def __init__(self):
        """
        Initializes the ValueSpecification base class.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is ValueSpecification:
            raise TypeError("ValueSpecification is an abstract class.")

        super().__init__()

        # Short label for this value specification
        self.shortLabel = None

    def getShortLabel(self):
        """
        Gets the short label for this value specification.

        Returns:
            The short label
        """
        return self.shortLabel

    def setShortLabel(self, value):
        """
        Sets the short label for this value specification.
        Only sets the value if it is not None.

        Args:
            value: The short label to set

        Returns:
            self for method chaining
        """
        self.shortLabel = value
        return self


class CompositeValueSpecification(ValueSpecification, ABC):
    """
    Abstract base class for value specifications that have a composite form.
    This class serves as a base for value specifications that contain multiple elements or components.
    Subclasses include ArrayValueSpecification and RecordValueSpecification.
    """

    def __init__(self):
        """
        Initializes the CompositeValueSpecification base class.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is CompositeValueSpecification:
            raise TypeError("CompositeValueSpecification is an abstract class.")

        super().__init__()


class CompositeRuleBasedValueArgument(ARObject, ABC):
    """
    Abstract base class for value specifications that can be used for compound primitive data types.
    This class serves as the base for specialized value specifications that handle complex data types.
    Subclasses include ApplicationRuleBasedValueSpecification and ApplicationValueSpecification.
    """

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

class AbstractRuleBasedValueSpecification(ValueSpecification, ABC):
    """
    Abstract base class for rule-based value specifications.
    This class serves as the base for specifications that use rules to determine values.
    """

    def __init__(self):
        if type(self) is AbstractRuleBasedValueSpecification:
            raise TypeError("AbstractRuleBasedValueSpecification is an abstract class.")
        super().__init__()


class ApplicationRuleBasedValueSpecification(CompositeRuleBasedValueArgument):
    """
    Represents application-specific rule-based value specifications.
    """

    def __init__(self):
        super().__init__()
        self.category = None

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        self.category = value
        return self


class CompositeRuleBasedValueSpecification(CompositeValueSpecification):
    """
    Represents composite rule-based value specifications.
    """

    def __init__(self):
        super().__init__()
        self.ruleArguments = []

    def addRuleArgument(self, argument):
        self.ruleArguments.append(argument)

    def getRuleArguments(self):
        return self.ruleArguments


class ConstantSpecificationMapping(ARObject):
    """
    Represents a mapping between constant specifications.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()
        self.sourceRef: RefType = None
        self.targetRef: RefType = None

    def getSourceRef(self):
        return self.sourceRef

    def setSourceRef(self, value):
        self.sourceRef = value
        return self

    def getTargetRef(self):
        return self.targetRef

    def setTargetRef(self, value):
        self.targetRef = value
        return self


class ConstantSpecificationMappingSet(ARObject):
    """
    Represents a set of constant specification mappings.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()
        self.mappings = []

    def addMapping(self, mapping):
        self.mappings.append(mapping)

    def getMappings(self):
        return self.mappings


class NotAvailableValueSpecification(ValueSpecification):
    """
    Represents a value specification that indicates a value is not available.
    """

    def __init__(self):
        super().__init__()
        self.reason: str = None

    def getReason(self):
        return self.reason

    def setReason(self, value):
        self.reason = value
        return self


class NumericalOrText(ARObject):
    """
    Represents a value that can be either numerical or text.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()
        self.numericalValue: ARNumerical = None
        self.textValue: ARLiteral = None

    def getNumericalValue(self):
        return self.numericalValue

    def setNumericalValue(self, value):
        self.numericalValue = value
        return self

    def getTextValue(self):
        return self.textValue

    def setTextValue(self, value):
        self.textValue = value
        return self


class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    Represents numerical rule-based value specifications.
    """

    def __init__(self):
        super().__init__()
        self.expression: str = None

    def getExpression(self):
        return self.expression

    def setExpression(self, value):
        self.expression = value
        return self


class ReferenceValueSpecification(ValueSpecification):
    """
    Represents a reference to another value specification.
    """

    def __init__(self):
        super().__init__()
        self.valueSpecRef: RefType = None

    def getValueSpecRef(self):
        return self.valueSpecRef

    def setValueSpecRef(self, value):
        self.valueSpecRef = value
        return self


class RuleArguments(ARObject):
    """
    Represents arguments for rule-based value specifications.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()
        self.arguments = []

    def addArgument(self, argument):
        self.arguments.append(argument)

    def getArguments(self):
        return self.arguments


class RuleBasedAxisCont(ARObject):
    """
    Represents rule-based axis content.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()
        self.axisId: str = None

    def getAxisId(self):
        return self.axisId

    def setAxisId(self, value):
        self.axisId = value
        return self


class RuleBasedValueCont(ARObject):
    """
    Represents rule-based value content.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()
        self.value: str = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self


class RuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    Represents general rule-based value specifications.
    """

    def __init__(self):
        super().__init__()
        self.rule: str = None

    def getRule(self):
        return self.rule

    def setRule(self, value):
        self.rule = value
        return self
