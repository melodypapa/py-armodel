from abc import ABCMeta
from typing import List

from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical
from armodel.models.general_structure import ARElement
from ....ar_object import ARLiteral

class ValueSpecification(ARObject, metaclass = ABCMeta):
    '''
    Base class for expressions leading to a value which can be used to initialize a data object.
    
    Base        : ARObject
    Subclasses  : AbstractRuleBasedValueSpecification, ApplicationValueSpecification, CompositeValueSpecification,
                  ConstantReference, NotAvailableValueSpecification, NumericalValueSpecification, ReferenceValueSpecification, 
                  TextValueSpecification
    '''
    def __init__(self):
        if type(self) == ValueSpecification:
            raise NotImplementedError("ValueSpecification is an abstract class.")
        
        super().__init__()

        self.shortLabel = None

    def getShortLabel(self):
        return self.shortLabel

    def setShortLabel(self, value):
        self.shortLabel = value
        return self
    
class CompositeValueSpecification(ValueSpecification, metaclass = ABCMeta):
    '''
    This abstract meta-class acts a base class for ValueSpecifications that have a composite form.

    Base        : ARObject, ValueSpecification
    Subclasses  : ArrayValueSpecification, RecordValueSpecification
    '''            
    def __init__(self):
        if type(self) == CompositeValueSpecification:
            raise NotImplementedError("CompositeValueSpecification is an abstract class.")
        
        super().__init__()    

class CompositeRuleBasedValueArgument(ARObject, metaclass = ABCMeta):
    '''
    This meta-class has the ability to serve as the abstract base class for ValueSpecifications that can be
    used for compound primitive data types.

    Base        : ARObject
    Subclasses  : ApplicationRuleBasedValueSpecification, ApplicationValueSpecification
    '''
    def __init__(self):
        if type(self) == CompositeRuleBasedValueArgument:
            raise NotImplementedError("CompositeRuleBasedValueArgument is an abstract class.")
        
        super().__init__()

class ApplicationValueSpecification(CompositeRuleBasedValueArgument, ValueSpecification):
    '''
    This meta-class represents values for DataPrototypes typed by ApplicationDataTypes (this includes in
    particular compound primitives).
    For further details refer to ASAM CDF 2.0. This meta-class corresponds to some extent with
    SW-INSTANCE in ASAM CDF 2.0.

    Base ARObject, CompositeRuleBasedValueArgument, ValueSpecification    
    '''
    def __init__(self):
        
        CompositeRuleBasedValueArgument.__init__(self)
        ValueSpecification.__init__(self)

        self.category = None
        self.swAxisCont = []
        self.swValueCont = None

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        self.category = value
        return self

    def getSwAxisCont(self):
        return self.swAxisCont

    def setSwAxisCont(self, value):
        self.swAxisCont = value
        return self

    def getSwValueCont(self):
        return self.swValueCont

    def setSwValueCont(self, value):
        self.swValueCont = value
        return self


class RecordValueSpecification(CompositeValueSpecification):
    '''
    Specifies the values for a record.
    
    Base : ARObject, CompositeValueSpecification, ValueSpecification
    '''
    def __init__(self):
        super().__init__()

        self.fields = []

    def addField(self, field: ValueSpecification):
        self.fields.append(field)

    def getFields(self) -> List[ValueSpecification]:
        return self.fields
    
class TextValueSpecification(ValueSpecification):
    def __init__(self):
        super().__init__()

        self.value = None               # type: ARLiteral

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self


class NumericalValueSpecification(ValueSpecification):
    def __init__(self):
        super().__init__()

        self.value = None               # type: ARNumerical  

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self


class ArrayValueSpecification(ValueSpecification):
    def __init__(self):
        super().__init__()

        self.element = []                                   # type: List[ValueSpecification]
        self.intendedPartialInitializationCount = None

    def getIntendedPartialInitializationCount(self):
        return self.intendedPartialInitializationCount

    def setIntendedPartialInitializationCount(self, value):
        self.intendedPartialInitializationCount = value
        return self

    def addElement(self, element: ValueSpecification):
        self.element.append(element)

    def getElements(self) -> List[ValueSpecification]:
        return self.element

class ConstantSpecification(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.valueSpec = None                  # type: ValueSpecification

    def getValueSpec(self):
        return self.valueSpec

    def setValueSpec(self, value):
        self.valueSpec = value
        return self


class ConstantReference(ValueSpecification):
    def __init__(self):
        super().__init__()

        self.constantRef = None                 # type: RefType

    def getConstantRef(self):
        return self.constantRef

    def setConstantRef(self, value):
        self.constantRef = value
        return self
