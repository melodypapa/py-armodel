from abc import ABCMeta
from typing import List

from .ar_object import ARBoolean, ARLiteral, ARNumerical
from .common_structure import ModeDeclarationGroupPrototype, Trigger
from .datatype import AtpType
from .general_structure import ARObject, Identifiable, AtpFeature
from .data_prototype import VariableDataPrototype, AutosarDataPrototype, ParameterDataPrototype
from .ar_ref import RefType

class PortInterface(AtpType, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == PortInterface:
            raise NotImplementedError("PortInterface is an abstract class.")
        super().__init__(parent, short_name)

        self.is_service = None                   # type: ARBoolean
        self.serviceKind = None                 # type: ARLiteral

class DataInterface(PortInterface, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == DataInterface:
            raise NotImplementedError("DataInterface is an abstract class.")
        super().__init__(parent, short_name)


class NvDataInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ParameterInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createParameter(self, short_name) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            parameter = ParameterDataPrototype(self, short_name)
            self.elements[short_name] = parameter
        return self.elements[short_name]
    
    def getParameters(self) -> List[ParameterDataPrototype]:
        return list(filter(lambda c: isinstance(c, ParameterDataPrototype), self.elements.values()))
    
    def getParameter(self, short_name) -> ParameterDataPrototype:
        if (short_name in self.elements):
            parameter = self.elements[short_name]
            if (not isinstance(parameter, ParameterDataPrototype)):
                raise IndexError("%s is not parameter." % short_name)
            return parameter
        raise IndexError("parameter <%s> can not be found." % short_name)


class InvalidationPolicy(ARObject):
    def __init__(self, parent: ARObject):
        self.parent = parent
        self.policy = None

        self.data_element_ref = None            # type: RefType
        self.handle_invalid = ""                # type: ARLiteral

class SenderReceiverInterface(DataInterface):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.invalidation_polivys = []          # type: List[InvalidationPolicy]

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
        self.invalidation_polivys.append(policy)
        return policy
    
    def getInvalidationPolicys(self) -> List[InvalidationPolicy]:
        return list(filter(lambda c: isinstance(c, InvalidationPolicy), self.invalidation_polivys))

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