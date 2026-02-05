"""
This module contains classes for representing AUTOSAR port interfaces
in the SWComponentTemplate module. It includes various types of port
interfaces such as sender/receiver, client/server, mode switch, and
parameter interfaces, as well as mapping classes for interface mappings.
"""

from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger, TriggerMapping
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement, AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, ArgumentDirectionEnum, Boolean
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype, AutosarDataPrototype
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype, ModeDeclarationGroupPrototypeMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class PortInterface(AtpType, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PortInterface:
            raise TypeError("PortInterface is an abstract class.")
        super().__init__(parent, short_name)

        self.isService: ARBoolean = None
        self.serviceKind: ARLiteral = None

    def getIsService(self):
        return self.isService

    def setIsService(self, value):
        self.isService = value
        return self

    def getServiceKind(self):
        return self.serviceKind

    def setServiceKind(self, value):
        self.serviceKind = value
        return self


class DataInterface(PortInterface, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DataInterface:
            raise TypeError("DataInterface is an abstract class.")
        super().__init__(parent, short_name)


class NvDataInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nvDatas: List[VariableDataPrototype] = []

    def getNvDatas(self):
        return self.nvDatas

    def setNvData(self, value):
        self.nvDatas.append(value)
        return self


class ParameterInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.parameters: List[ParameterDataPrototype] = []

    def getParameters(self):
        return self.parameters

    def createParameterDataPrototype(self, short_name: str) -> ParameterDataPrototype:
        prototype = ParameterDataPrototype(self, short_name)
        self.addElement(prototype)
        self.parameters.append(prototype)
        return prototype


class InvalidationPolicy(ARObject):
    def __init__(self):
        super().__init__()

        self.dataElementRef: RefType = None
        self.handleInvalid: ARLiteral = None

    def getDataElementRef(self):
        return self.dataElementRef

    def setDataElementRef(self, value):
        self.dataElementRef = value
        return self

    def getHandleInvalid(self):
        return self.handleInvalid

    def setHandleInvalid(self, value):
        self.handleInvalid = value
        return self


class MetaDataItem(ARObject):
    def __init__(self):
        super().__init__()

        self.length: PositiveInteger = None
        self.metaDataItemType: TextValueSpecification = None

    def getLength(self):
        return self.length

    def setLength(self, value):
        self.length = value
        return self

    def getMetaDataItemType(self):
        return self.metaDataItemType

    def setMetaDataItemType(self, value):
        self.metaDataItemType = value
        return self


class MetaDataItemSet(ARObject):
    def __init__(self):
        super().__init__()

        self.dataElementRefs: List[RefType] = []
        self.metaDataItems: List[MetaDataItem] = []

    def getDataElementRefs(self):
        return self.dataElementRefs

    def addDataElementRef(self, value):
        self.dataElementRefs.append(value)
        return self

    def getMetaDataItems(self):
        return self.metaDataItems

    def addMetaDataItem(self, value):
        self.metaDataItems.append(value)
        return self


class SenderReceiverInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.invalidationPolicies: List[InvalidationPolicy] = []
        self.metaDataItemSets: List[MetaDataItemSet] = []

    def getInvalidationPolicies(self):
        return self.invalidationPolicies

    def addInvalidationPolicy(self, value):
        self.invalidationPolicies.append(value)
        return self

    def getMetaDataItemSets(self):
        return self.metaDataItemSets

    def addMetaDataItemSet(self, value):
        self.metaDataItemSets.append(value)
        return self

    def createDataElement(self, short_name) -> VariableDataPrototype:
        if (not self.IsElementExists(short_name)):
            data_element = VariableDataPrototype(self, short_name)
            self.addElement(data_element)
        return self.getElement(short_name, VariableDataPrototype)

    def getDataElements(self) -> List[VariableDataPrototype]:
        return list(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements))

    def getDataElement(self, short_name) -> VariableDataPrototype:
        return self.getElement(short_name, VariableDataPrototype)
    
    def createInvalidationPolicy(self) -> InvalidationPolicy:
        policy = InvalidationPolicy()
        self.invalidationPolicies.append(policy)
        return policy
    
    def getInvalidationPolicys(self) -> List[InvalidationPolicy]:
        return list(filter(lambda c: isinstance(c, InvalidationPolicy), self.invalidationPolicies))


class ArgumentDataPrototype(AutosarDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.direction: ArgumentDirectionEnum = None
        self.serverArgumentImplPolicy = None

    def getDirection(self):
        return self.direction

    def setDirection(self, value):
        if value is not None:
            self.direction = value
        return self

    def getServerArgumentImplPolicy(self):
        return self.serverArgumentImplPolicy

    def setServerArgumentImplPolicy(self, value):
        if value is not None:
            self.serverArgumentImplPolicy = value
        return self


class ApplicationError(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.error_code: ARNumerical = None


class ClientServerOperation(AtpStructureElement):
    """
        An operation declared within the scope of a client/server interface.
        Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface
        Base: ARObject, AtpClassifier , AtpBlueprintable, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable

        Attributes:
        -----------
        _argument: ArgumentDataPrototype (optional)
            An argument of this ClientServerOperation

        _possibleError: RefType -> ApplicationError (optional)
            Possible errors that may by raised by the referring operation

        Methods:
        --------
        addArgumentDataPrototype    add the argument
        getArgumentDataPrototypes   get the arguments
        addPossibleErrorRef         add the possible error
        getPossbileErrorRefs        get the possible errors

    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arguments: List[ArgumentDataPrototype] = []
        self.possibleErrorRefs: List[RefType] = []

    def getArguments(self):
        return self.arguments

    def createArgumentDataPrototype(self, short_name):
        if not self.IsElementExists(short_name):
            prototype = ArgumentDataPrototype(self, short_name)
            self.addElement(prototype)
            self.arguments.append(prototype)
        return self.getElement(short_name)

    def getPossibleErrorRefs(self):
        return self.possibleErrorRefs

    def addPossibleErrorRef(self, value):
        if value is not None:
            self.possibleErrorRefs.append(value)
        return self


class ClientServerInterface(PortInterface):
    """
        A client/server interface declares a number of operations that can be invoked on a server by a client.
        Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface
        Base: ARElement, ARObject, AtpBlueprint, AtpBlueprintable, AtpClassifier , AtpType, CollectableElement, Identifiable, MultilanguageReferrable,
              PackageableElement, PortInterface, Referrable

        Methods:
        --------
        createOperation             create ClientServerOperation(s) of this ClientServerInterface.
        createApplicationError      create Application errors that are defined as part of this interface
        getOperations               get all ClientServerOperation(s) of this ClientServerInterface
        getPossibleErrors           get all Application error(s) of this ClientServerInterface

    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createOperation(self, short_name: str) -> ClientServerOperation:
        if (not self.IsElementExists(short_name)):
            operation = ClientServerOperation(self, short_name)
            self.addElement(operation)
        return self.getElement(short_name, ClientServerOperation)

    def createApplicationError(self, short_name: str) -> ApplicationError:
        if (not self.IsElementExists(short_name)):
            error = ApplicationError(self, short_name)
            self.addElement(error)
        return self.getElement(short_name, ApplicationError)

    def getOperations(self) -> List[ClientServerOperation]:
        return list(filter(lambda c: isinstance(c, ClientServerOperation), self.elements))

    def getPossibleErrors(self) -> List[ApplicationError]:
        return list(filter(lambda c: isinstance(c, ApplicationError), self.elements))


class TriggerInterface(PortInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._triggers: List[Trigger] = []


class ModeSwitchInterface(PortInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._modeGroup: List[ModeDeclarationGroupPrototype] = []

    def createModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if not self.IsElementExists(short_name):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
        return self.getElement(short_name, ModeDeclarationGroupPrototype)
    
    def getModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, ModeDeclarationGroupPrototype), self.elements), key=lambda o: o.short_name))


class PortInterfaceMapping(AtpBlueprintable, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PortInterfaceMapping:
            raise TypeError("PortInterfaceMapping is an abstract class.")
        super().__init__(parent, short_name)


class ClientServerApplicationErrorMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.firstApplicationErrorRef: RefType = None
        self.secondApplicationErrorRef: RefType = None

    def getFirstApplicationErrorRef(self):
        return self.firstApplicationErrorRef

    def setFirstApplicationErrorRef(self, value):
        self.firstApplicationErrorRef = value
        return self

    def getSecondApplicationErrorRef(self):
        return self.secondApplicationErrorRef

    def setSecondApplicationErrorRef(self, value):
        self.secondApplicationErrorRef = value
        return self


class ClientServerOperationMapping(ARObject):
    def __init__(self):
        super().__init__()
        
        self.argumentMappings: List['DataPrototypeMapping'] = []
        self.firstOperationRef: RefType = None
        self.firstToSecondDataTransformationRef: RefType = None
        self.secondOperationRef: RefType = None

    def getArgumentMappings(self):
        return self.argumentMappings

    def addArgumentMapping(self, value):
        self.argumentMappings.append(value)
        return self

    def getFirstOperationRef(self):
        return self.firstOperationRef

    def setFirstOperationRef(self, value):
        self.firstOperationRef = value
        return self

    def getFirstToSecondDataTransformationRef(self):
        return self.firstToSecondDataTransformationRef

    def setFirstToSecondDataTransformationRef(self, value):
        self.firstToSecondDataTransformationRef = value
        return self

    def getSecondOperationRef(self):
        return self.secondOperationRef

    def setSecondOperationRef(self, value):
        self.secondOperationRef = value
        return self
    

class DataPrototypeMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.firstDataPrototypeRef: RefType = None
        self.firstToSecondDataTransformationRef: RefType = None
        self.secondDataPrototypeRef: RefType = None
        self.secondToFirstDataTransformationRef: RefType = None
        self.subElementMappings = []
        self.textTableMappings: List['TextTableMapping'] = []

    def getFirstDataPrototypeRef(self):
        return self.firstDataPrototypeRef

    def setFirstDataPrototypeRef(self, value):
        self.firstDataPrototypeRef = value
        return self

    def getFirstToSecondDataTransformationRef(self):
        return self.firstToSecondDataTransformationRef

    def setFirstToSecondDataTransformationRef(self, value):
        self.firstToSecondDataTransformationRef = value
        return self

    def getSecondDataPrototypeRef(self):
        return self.secondDataPrototypeRef

    def setSecondDataPrototypeRef(self, value):
        self.secondDataPrototypeRef = value
        return self

    def getSecondToFirstDataTransformationRef(self):
        return self.secondToFirstDataTransformationRef

    def setSecondToFirstDataTransformationRef(self, value):
        self.secondToFirstDataTransformationRef = value
        return self

    def getSubElementMappings(self):
        return self.subElementMappings

    def setSubElementMappings(self, value):
        self.subElementMappings = value
        return self

    def getTextTableMappings(self):
        return self.textTableMappings

    def setTextTableMappings(self, value):
        self.textTableMappings = value
        return self


class ClientServerInterfaceMapping(PortInterfaceMapping):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.errorMappings: List['ClientServerApplicationErrorMapping'] = []
        self.operationMappings: List['ClientServerOperationMapping'] = []

    def getErrorMappings(self):
        return self.errorMappings

    def addErrorMapping(self, value):
        if value is not None:
            self.errorMappings.append(value)
        return self

    def getOperationMappings(self):
        return self.operationMappings

    def addOperationMapping(self, value):
        if value is not None:
            self.operationMappings.append(value)
        return self


class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataMappings: List['DataPrototypeMapping'] = []

    def getDataMappings(self):
        return self.dataMappings

    def addDataMapping(self, value):
        self.dataMappings.append(value)
        return self


class ModeInterfaceMapping(PortInterfaceMapping):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.modeMapping: 'ModeDeclarationGroupPrototypeMapping' = None

    def getModeMapping(self):
        return self.modeMapping

    def setModeMapping(self, value):
        if value is not None:
            self.modeMapping = value
        return self


class TriggerInterfaceMapping(PortInterfaceMapping):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.triggerMapping: List[TriggerMapping] = []

    def getTriggerMapping(self) -> List[TriggerMapping]:
        return self.triggerMapping

    def setTriggerMapping(self, value: List[TriggerMapping]):
        if value is not None:
            self.triggerMapping = value
        return self


class ModeDeclarationMapping(AtpStructureElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.firstModeRefs: List[RefType] = []
        self.secondModeRef: RefType = []

    def getFirstModeRefs(self) -> List[RefType]:
        return self.firstModeRefs

    def addFirstModeRef(self, value: 'RefType'):
        if value is not None:
            self.firstModeRefs.append(value)
        return self

    def getSecondModeRef(self) -> RefType:
        return self.secondModeRef

    def setSecondModeRef(self, value: RefType):
        if value is not None:
            self.secondModeRef = value
        return self


class ModeDeclarationMappingSet(AtpType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.modeDeclarationMappings: List[ModeDeclarationMapping] = []

    def getModeDeclarationMappings(self) -> List[ModeDeclarationMapping]:
        return self.modeDeclarationMappings

    def createModeDeclarationMapping(self, short_name: str) -> ModeDeclarationMapping:
        if (not self.IsElementExists(short_name)):
            mapping = ModeDeclarationMapping(self, short_name)
            self.addElement(mapping)
            self.modeDeclarationMappings.append(mapping)
        return self.getElement(short_name)


class PortInterfaceMappingSet(AtpBlueprintable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.portInterfaceMappings = []                 # type: List[PortInterfaceMapping]

    def getPortInterfaceMappings(self):
        return self.portInterfaceMappings

    def createVariableAndParameterInterfaceMapping(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            mapping = VariableAndParameterInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)
    
    def createClientServerInterfaceMapping(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            mapping = ClientServerInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)
    
    def createModeInterfaceMapping(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            mapping = ModeInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)
    
    def createTriggerInterfaceMapping(self, short_name: str):
        if (not self.IsElementExists(short_name)):
            mapping = TriggerInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)


class TextTableMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.bitfieldTextTableMaskFirst: PositiveInteger = None
        self.bitfieldTextTableMaskSecond: PositiveInteger = None
        self.identicalMapping: Boolean = None
        self.mappingDirection = None
        self.valuePairs = []

    def getBitfieldTextTableMaskFirst(self):
        return self.bitfieldTextTableMaskFirst

    def setBitfieldTextTableMaskFirst(self, value):
        if value is not None:
            self.bitfieldTextTableMaskFirst = value
        return self

    def getBitfieldTextTableMaskSecond(self):
        return self.bitfieldTextTableMaskSecond

    def setBitfieldTextTableMaskSecond(self, value):
        if value is not None:
            self.bitfieldTextTableMaskSecond = value
        return self

    def getIdenticalMapping(self):
        return self.identicalMapping

    def setIdenticalMapping(self, value):
        if value is not None:
            self.identicalMapping = value
        return self

    def getMappingDirection(self):
        return self.mappingDirection

    def setMappingDirection(self, value):
        if value is not None:
            self.mappingDirection = value
        return self

    def getValuePairs(self):
        return self.valuePairs

    def setValuePairs(self, value):
        if value is not None:
            self.valuePairs = value
        return self
