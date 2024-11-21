from abc import ABCMeta
from typing import List

from .....M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical
from .....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype, AutosarDataPrototype
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from .....M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from .....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from .....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpFeature
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class PortInterface(AtpType, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == PortInterface:
            raise NotImplementedError("PortInterface is an abstract class.")
        super().__init__(parent, short_name)

        self.isService = None                       # type: ARBoolean
        self.serviceKind = None                     # type: ARLiteral

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

class DataInterface(PortInterface, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == DataInterface:
            raise NotImplementedError("DataInterface is an abstract class.")
        super().__init__(parent, short_name)

class NvDataInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nvDatas = []       # type: List[VariableDataPrototype]

    def getNvDatas(self):
        return self.nvDatas

    def setNvData(self, value):
        self.nvDatas.append(value)
        return self

class ParameterInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.parameters = []                        # type: List[ParameterDataPrototype]

    def getParameters(self):
        return list(sorted(filter(lambda a : isinstance(a, ParameterDataPrototype), self.elements.values()), key = lambda a: a.short_name))

    def createParameter(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            parameter = ParameterDataPrototype(self, short_name)
            self.elements[short_name] = parameter
            self.parameters.append(parameter)
        return self.elements[short_name]
    
class InvalidationPolicy(ARObject):
    def __init__(self):
        super().__init__()

        self.dataElementRef = None                      # type: RefType
        self.handleInvalid = None                       # type: ARLiteral

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

class SenderReceiverInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.invalidationPolicies = []                # type: List[InvalidationPolicy]
        self.metaDataItemSets = []                    # type: List[MetaDataItemSet]

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
        if (short_name not in self.elements):
            data_element = VariableDataPrototype(self, short_name)
            self.elements[short_name] = data_element
        return self.elements[short_name]

    def getDataElements(self) -> List[VariableDataPrototype]:
        return list(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements.values()))

    def getDataElement(self, short_name) -> VariableDataPrototype:
        if (short_name in self.elements):
            data_element = self.elements[short_name]
            #if (not isinstance(data_element, VariableDataPrototype)):
            #    raise IndexError("%s is not data element." % short_name)
            return data_element
        raise IndexError("data element <%s> can not be found." % short_name)
    
    def createInvalidationPolicy(self) -> InvalidationPolicy:
        policy = InvalidationPolicy(self)
        self.invalidationPolicies.append(policy)
        return policy
    
    def getInvalidationPolicys(self) -> List[InvalidationPolicy]:
        return list(filter(lambda c: isinstance(c, InvalidationPolicy), self.invalidationPolicies))

class ArgumentDataPrototype(AutosarDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.direction = ""
        self.server_argument_impl_policy = ""

class ApplicationError(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.error_code = None                  # type: ARNumerical

class ClientServerOperation(AtpFeature):
    """
        An operation declared within the scope of a client/server interface.
        Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface
        Base: ARObject, AtpClassifier , AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable

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

        self._arguments = []
        self._possible_error_refs = []  # type: List[RefType]

    def addArgumentDataPrototype(self, prototype: ArgumentDataPrototype):
        self._arguments.append(prototype)

    def getArgumentDataPrototypes(self) -> List[ArgumentDataPrototype]:
        return self._arguments

    def addPossibleErrorRef(self, possible_error_ref: RefType):
        self._possible_error_refs.append(possible_error_ref)

    def getPossbileErrorRefs(self) -> List[RefType]:
        return self._possible_error_refs


class ClientServerInterface(PortInterface):
    """
        A client/server interface declares a number of operations that can be invoked on a server by a client.
        Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface
        Base: ARElement, ARObject, AtpBlueprint, AtpBlueprintable, AtpClassifier , AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PortInterface, Referrable

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
        if (short_name not in self.elements):
            operation = ClientServerOperation(self, short_name)
            self.elements[short_name] = operation
        return self.elements[short_name]

    def createApplicationError(self, short_name: str) -> ApplicationError:
        if (short_name not in self.elements):
            error = ApplicationError(self, short_name)
            self.elements[short_name] = error
        return self.elements[short_name]

    def getOperations(self) -> List[ClientServerOperation]:
        return list(filter(lambda c: isinstance(c, ClientServerOperation), self.elements.values()))

    def getPossibleErrors(self) -> List[ApplicationError]:
        return list(filter(lambda c: isinstance(c, ApplicationError), self.elements.values()))
    
class TriggerInterface(PortInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._triggers = []             # type: Trigger

class ModeSwitchInterface(PortInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._modeGroup = []            # type: List[ModeDeclarationGroupPrototype]

    def createModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        prototype = ModeDeclarationGroupPrototype(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = prototype
        return self.elements[short_name]
    
    def getModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, ModeDeclarationGroupPrototype), self.elements.values()), key= lambda o: o.short_name))