"""
This module contains classes for representing AUTOSAR port interfaces
in the SWComponentTemplate module. It includes various types of port
interfaces such as sender/receiver, client/server, mode switch, and
parameter interfaces, as well as mapping classes for interface mappings.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype, ModeDeclarationGroupPrototypeMapping
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger, TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable, AtpStructureElement, AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    AREnum,
    ArgumentDirectionEnum,
    ARLiteral,
    ARNumerical,
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AutosarDataPrototype, ParameterDataPrototype, VariableDataPrototype


class PortInterface(AtpType, ABC):
    # PortInterface method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIsService                 [x] impl  [ ] docstring  [ ] test
    # [ ] setIsService                 [x] impl  [ ] docstring  [ ] test
    # [ ] getServiceKind               [x] impl  [ ] docstring  [ ] test
    # [ ] setServiceKind               [x] impl  [ ] docstring  [ ] test

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
    # DataInterface method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DataInterface:
            raise TypeError("DataInterface is an abstract class.")
        super().__init__(parent, short_name)


class NvDataInterface(DataInterface):
    """Class NvDataInterface.

    Package M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Note: A non volatile data interface declares a number of
    VariableDataPrototypes to be exchanged between non volatile block
    components and atomic software components.

    Tags: atp.recommendedPackage=PortInterfaces

    Base ARElement, ARObject, AtpBlueprint, AtpBlueprintable,
    AtpClassifier, AtpType, CollectableElement, DataInterface,
    Identifiable, MultilanguageReferrable, PackageableElement,
    PortInterface, Referrable

    Attribute:
        nvData (VariableDataPrototype, 1..*, aggr)
        The VariableDataPrototype of this nv data interface.
    """

    # NvDataInterface method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getNvDatas                   [x] impl  [x] docstring  [ ] test
    # [ ] createNvData                 [x] impl  [x] docstring  [ ] test
    # [ ] getNvData                    [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def getNvDatas(self):
        """Get nvData VariableDataPrototype list."""
        return list(
            filter(
                lambda c: isinstance(c, VariableDataPrototype),
                self.elements,
            )
        )

    def createNvData(self, short_name: str) -> VariableDataPrototype:
        """Create one nvData VariableDataPrototype and aggregate it."""
        if not self.IsElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
        return self.getElement(short_name, VariableDataPrototype)

    def getNvData(self, short_name: str) -> VariableDataPrototype:
        """Get one nvData VariableDataPrototype by short name."""
        return self.getElement(short_name, VariableDataPrototype)


class ParameterInterface(DataInterface):
    # ParameterInterface method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getParameters                [x] impl  [ ] docstring  [ ] test
    # [ ] createParameterDataPrototype [x] impl  [ ] docstring  [ ] test

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
    # InvalidationPolicy method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataElementRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setDataElementRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getHandleInvalid             [x] impl  [ ] docstring  [ ] test
    # [ ] setHandleInvalid             [x] impl  [ ] docstring  [ ] test

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
    # MetaDataItem method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getLength                    [x] impl  [ ] docstring  [ ] test
    # [ ] setLength                    [x] impl  [ ] docstring  [ ] test
    # [ ] getMetaDataItemType          [x] impl  [ ] docstring  [ ] test
    # [ ] setMetaDataItemType          [x] impl  [ ] docstring  [ ] test

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
    # MetaDataItemSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataElementRefs           [x] impl  [ ] docstring  [ ] test
    # [ ] addDataElementRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getMetaDataItems             [x] impl  [ ] docstring  [ ] test
    # [ ] addMetaDataItem              [x] impl  [ ] docstring  [ ] test

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
    # SenderReceiverInterface method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInvalidationPolicies      [x] impl  [ ] docstring  [ ] test
    # [ ] addInvalidationPolicy        [x] impl  [ ] docstring  [ ] test
    # [ ] getMetaDataItemSets          [x] impl  [ ] docstring  [ ] test
    # [ ] addMetaDataItemSet           [x] impl  [ ] docstring  [ ] test
    # [ ] createDataElement            [x] impl  [ ] docstring  [ ] test
    # [ ] getDataElements              [x] impl  [ ] docstring  [ ] test
    # [ ] getDataElement               [x] impl  [ ] docstring  [ ] test
    # [ ] createInvalidationPolicy     [x] impl  [ ] docstring  [ ] test
    # [ ] getInvalidationPolicys       [x] impl  [ ] docstring  [ ] test

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
        if not self.IsElementExists(short_name):
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


class ServerArgumentImplPolicyEnum(AREnum):
    """
    This defines how the argument type of the servers RunnableEntity is implemented.
    """

    # ServerArgumentImplPolicyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.10, p.105
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The argument type of the RunnableEntity is derived from the AutosarDataType of the
    # Argument Prototype. Tags: atp.EnumerationLiteralIndex=0
    USE_ARGUMENT_TYPE = "useArgumentType"

    # The argument type of the RunnableEntity is void. Tags: atp.EnumerationLiteralIndex=2
    USE_VOID = "useVoid"

    def __init__(self):
        """
        Initializes a ServerArgumentImplPolicyEnum instance with the spec-defined literals.
        """
        super().__init__((ServerArgumentImplPolicyEnum.USE_ARGUMENT_TYPE, ServerArgumentImplPolicyEnum.USE_VOID))


class ArgumentDataPrototype(AutosarDataPrototype):
    """
    An argument of an operation, much like a data element, but also carries direction
    information and is owned by a particular ClientServerOperation.
    The overriding value of attribute swImplPolicy of an ArgumentDataPrototype shall be
    standard. [constr_2047]
    """

    # ArgumentDataPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.7, p.303
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getDirection                 [x] impl  [x] docstring  [x] test
    # [x] setDirection                 [x] impl  [x] docstring  [x] test
    # [x] getServerArgumentImplPolicy  [x] impl  [x] docstring  [x] test
    # [x] setServerArgumentImplPolicy  [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes an ArgumentDataPrototype instance with an argument direction and a server
        argument implementation policy.
        """
        super().__init__(parent, short_name)

        # This attribute specifies the direction of the argument prototype.
        # For each ArgumentDataPrototype, attribute direction shall be defined at the time
        # when the contract phase generation is executed. [constr_1869]
        self.direction: Optional[ArgumentDirectionEnum] = None

        # This defines how the argument type of the servers RunnableEntity is implemented.
        # If the attribute is not defined this has the same semantics as if the attribute is set
        # to the value useArgumentType for primitive arguments and structures.
        # The value of the attribute ArgumentDataPrototype.serverArgumentImplPolicy shall not be
        # set to useVoid for an ArgumentDataPrototype of direction in that is typed by an
        # AutosarDataType that boils down to a primitive C data type. [constr_1286]
        self.serverArgumentImplPolicy: Optional[ServerArgumentImplPolicyEnum] = None

    def getDirection(self) -> Optional[ArgumentDirectionEnum]:
        """
        Gets the direction of the argument prototype.
        This attribute specifies the direction of the argument prototype.
        For each ArgumentDataPrototype, attribute direction shall be defined at the time
        when the contract phase generation is executed. [constr_1869]

        Returns:
            Optional[ArgumentDirectionEnum]: The direction, or None if not set
        """
        return self.direction

    def setDirection(self, value: Optional[ArgumentDirectionEnum]) -> "ArgumentDataPrototype":
        """
        Sets the direction of the argument prototype.
        This attribute specifies the direction of the argument prototype.
        For each ArgumentDataPrototype, attribute direction shall be defined at the time
        when the contract phase generation is executed. [constr_1869]
        A None value is a no-op and does not overwrite an existing direction.

        Args:
            value: The direction to set

        Returns:
            ArgumentDataPrototype: self for method chaining
        """
        if value is not None:
            self.direction = value
        return self

    def getServerArgumentImplPolicy(self) -> Optional[ServerArgumentImplPolicyEnum]:
        """
        Gets the server argument implementation policy.
        This defines how the argument type of the servers RunnableEntity is implemented.
        If the attribute is not defined this has the same semantics as if the attribute is set
        to the value useArgumentType for primitive arguments and structures.
        The value of the attribute ArgumentDataPrototype.serverArgumentImplPolicy shall not be
        set to useVoid for an ArgumentDataPrototype of direction in that is typed by an
        AutosarDataType that boils down to a primitive C data type. [constr_1286]

        Returns:
            Optional[ServerArgumentImplPolicyEnum]: The policy, or None if not set
        """
        return self.serverArgumentImplPolicy

    def setServerArgumentImplPolicy(self, value: Optional[ServerArgumentImplPolicyEnum]) -> "ArgumentDataPrototype":
        """
        Sets the server argument implementation policy.
        This defines how the argument type of the servers RunnableEntity is implemented.
        If the attribute is not defined this has the same semantics as if the attribute is set
        to the value useArgumentType for primitive arguments and structures.
        The value of the attribute ArgumentDataPrototype.serverArgumentImplPolicy shall not be
        set to useVoid for an ArgumentDataPrototype of direction in that is typed by an
        AutosarDataType that boils down to a primitive C data type. [constr_1286]
        A None value is a no-op and does not overwrite an existing policy.

        Args:
            value: The policy to set

        Returns:
            ArgumentDataPrototype: self for method chaining
        """
        if value is not None:
            self.serverArgumentImplPolicy = value
        return self


class ApplicationError(Identifiable):
    # ApplicationError method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

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

    # ClientServerOperation method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getArguments                 [x] impl  [ ] docstring  [ ] test
    # [ ] createArgumentDataPrototype  [x] impl  [ ] docstring  [ ] test
    # [ ] getPossibleErrorRefs         [x] impl  [ ] docstring  [ ] test
    # [ ] addPossibleErrorRef          [x] impl  [ ] docstring  [ ] test

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
    A client/server interface declares a number of operations that can be
    invoked on a server by a client.
    """

    # ClientServerInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.6, p.101
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] createOperation              [x] impl  [x] docstring  [x] test
    # [x] createApplicationError       [x] impl  [x] docstring  [x] test
    # [x] getOperations                [x] impl  [x] docstring  [x] test
    # [x] getPossibleErrors            [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createOperation(self, short_name: str) -> ClientServerOperation:
        """
        Creates a ClientServerOperation of this ClientServerInterface with the
        given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new ClientServerOperation

        Returns:
            The created (or existing) ClientServerOperation
        """
        if not self.IsElementExists(short_name):
            operation = ClientServerOperation(self, short_name)
            self.addElement(operation)
        return self.getElement(short_name, ClientServerOperation)

    def createApplicationError(self, short_name: str) -> ApplicationError:
        """
        Creates an ApplicationError of this ClientServerInterface with the
        given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new ApplicationError

        Returns:
            The created (or existing) ApplicationError
        """
        if not self.IsElementExists(short_name):
            error = ApplicationError(self, short_name)
            self.addElement(error)
        return self.getElement(short_name, ApplicationError)

    def getOperations(self) -> List[ClientServerOperation]:
        """
        Gets the ClientServerOperation(s) of this ClientServerInterface.

        Returns:
            The list of ClientServerOperation instances
        """
        return list(filter(lambda c: isinstance(c, ClientServerOperation), self.elements))

    def getPossibleErrors(self) -> List[ApplicationError]:
        """
        Gets the Application errors that are defined as part of this interface.

        Returns:
            The list of ApplicationError instances
        """
        return list(filter(lambda c: isinstance(c, ApplicationError), self.elements))


class TriggerInterface(PortInterface):
    # TriggerInterface method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._triggers: List[Trigger] = []


class ModeSwitchInterface(PortInterface):
    # ModeSwitchInterface method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] createModeGroup              [x] impl  [ ] docstring  [ ] test
    # [ ] getModeGroups                [x] impl  [ ] docstring  [ ] test

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
    # PortInterfaceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PortInterfaceMapping:
            raise TypeError("PortInterfaceMapping is an abstract class.")
        super().__init__(parent, short_name)


class ClientServerApplicationErrorMapping(ARObject):
    # ClientServerApplicationErrorMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstApplicationErrorRef  [x] impl  [ ] docstring  [ ] test
    # [ ] setFirstApplicationErrorRef  [x] impl  [ ] docstring  [ ] test
    # [ ] getSecondApplicationErrorRef [x] impl  [ ] docstring  [ ] test
    # [ ] setSecondApplicationErrorRef [x] impl  [ ] docstring  [ ] test

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
    # ClientServerOperationMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getArgumentMappings          [x] impl  [ ] docstring  [ ] test
    # [ ] addArgumentMapping           [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstOperationRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setFirstOperationRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstToSecondDataTransformationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setFirstToSecondDataTransformationRef [x] impl  [ ] docstring  [ ] test
    # [ ] getSecondOperationRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setSecondOperationRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.argumentMappings: List["DataPrototypeMapping"] = []
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
    # DataPrototypeMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstDataPrototypeRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setFirstDataPrototypeRef     [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstToSecondDataTransformationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setFirstToSecondDataTransformationRef [x] impl  [ ] docstring  [ ] test
    # [ ] getSecondDataPrototypeRef    [x] impl  [ ] docstring  [ ] test
    # [ ] setSecondDataPrototypeRef    [x] impl  [ ] docstring  [ ] test
    # [ ] getSecondToFirstDataTransformationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setSecondToFirstDataTransformationRef [x] impl  [ ] docstring  [ ] test
    # [ ] getSubElementMappings        [x] impl  [ ] docstring  [ ] test
    # [ ] setSubElementMappings        [x] impl  [ ] docstring  [ ] test
    # [ ] getTextTableMappings         [x] impl  [ ] docstring  [ ] test
    # [ ] setTextTableMappings         [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.firstDataPrototypeRef: RefType = None
        self.firstToSecondDataTransformationRef: RefType = None
        self.secondDataPrototypeRef: RefType = None
        self.secondToFirstDataTransformationRef: RefType = None
        self.subElementMappings = []
        self.textTableMappings: List["TextTableMapping"] = []

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
    # ClientServerInterfaceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getErrorMappings             [x] impl  [ ] docstring  [ ] test
    # [ ] addErrorMapping              [x] impl  [ ] docstring  [ ] test
    # [ ] getOperationMappings         [x] impl  [ ] docstring  [ ] test
    # [ ] addOperationMapping          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.errorMappings: List["ClientServerApplicationErrorMapping"] = []
        self.operationMappings: List["ClientServerOperationMapping"] = []

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
    # VariableAndParameterInterfaceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataMappings              [x] impl  [ ] docstring  [ ] test
    # [ ] addDataMapping               [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataMappings: List["DataPrototypeMapping"] = []

    def getDataMappings(self):
        return self.dataMappings

    def addDataMapping(self, value):
        self.dataMappings.append(value)
        return self


class ModeInterfaceMapping(PortInterfaceMapping):
    # ModeInterfaceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getModeMapping               [x] impl  [ ] docstring  [ ] test
    # [ ] setModeMapping               [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.modeMapping: "ModeDeclarationGroupPrototypeMapping" = None

    def getModeMapping(self):
        return self.modeMapping

    def setModeMapping(self, value):
        if value is not None:
            self.modeMapping = value
        return self


class TriggerInterfaceMapping(PortInterfaceMapping):
    # TriggerInterfaceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTriggerMapping            [x] impl  [ ] docstring  [ ] test
    # [ ] setTriggerMapping            [x] impl  [ ] docstring  [ ] test

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
    # ModeDeclarationMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstModeRefs             [x] impl  [ ] docstring  [ ] test
    # [ ] addFirstModeRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getSecondModeRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setSecondModeRef             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.firstModeRefs: List[RefType] = []
        self.secondModeRef: RefType = []

    def getFirstModeRefs(self) -> List[RefType]:
        return self.firstModeRefs

    def addFirstModeRef(self, value: "RefType"):
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
    # ModeDeclarationMappingSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getModeDeclarationMappings   [x] impl  [ ] docstring  [ ] test
    # [ ] createModeDeclarationMapping [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.modeDeclarationMappings: List[ModeDeclarationMapping] = []

    def getModeDeclarationMappings(self) -> List[ModeDeclarationMapping]:
        return self.modeDeclarationMappings

    def createModeDeclarationMapping(self, short_name: str) -> ModeDeclarationMapping:
        if not self.IsElementExists(short_name):
            mapping = ModeDeclarationMapping(self, short_name)
            self.addElement(mapping)
            self.modeDeclarationMappings.append(mapping)
        return self.getElement(short_name)


class PortInterfaceMappingSet(AtpBlueprintable):
    # PortInterfaceMappingSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getPortInterfaceMappings     [x] impl  [ ] docstring  [ ] test
    # [ ] createVariableAndParameterInterfaceMapping [x] impl  [ ] docstring  [ ] test
    # [ ] createClientServerInterfaceMapping [x] impl  [ ] docstring  [ ] test
    # [ ] createModeInterfaceMapping   [x] impl  [ ] docstring  [ ] test
    # [ ] createTriggerInterfaceMapping [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.portInterfaceMappings = []  # type: List[PortInterfaceMapping]

    def getPortInterfaceMappings(self):
        return self.portInterfaceMappings

    def createVariableAndParameterInterfaceMapping(self, short_name: str):
        if not self.IsElementExists(short_name):
            mapping = VariableAndParameterInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)

    def createClientServerInterfaceMapping(self, short_name: str):
        if not self.IsElementExists(short_name):
            mapping = ClientServerInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)

    def createModeInterfaceMapping(self, short_name: str):
        if not self.IsElementExists(short_name):
            mapping = ModeInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)

    def createTriggerInterfaceMapping(self, short_name: str):
        if not self.IsElementExists(short_name):
            mapping = TriggerInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name)


class TextTableMapping(ARObject):
    # TextTableMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBitfieldTextTableMaskFirst [x] impl  [ ] docstring  [ ] test
    # [ ] setBitfieldTextTableMaskFirst [x] impl  [ ] docstring  [ ] test
    # [ ] getBitfieldTextTableMaskSecond [x] impl  [ ] docstring  [ ] test
    # [ ] setBitfieldTextTableMaskSecond [x] impl  [ ] docstring  [ ] test
    # [ ] getIdenticalMapping          [x] impl  [ ] docstring  [ ] test
    # [ ] setIdenticalMapping          [x] impl  [ ] docstring  [ ] test
    # [ ] getMappingDirection          [x] impl  [ ] docstring  [ ] test
    # [ ] setMappingDirection          [x] impl  [ ] docstring  [ ] test
    # [ ] getValuePairs                [x] impl  [ ] docstring  [ ] test
    # [ ] setValuePairs                [x] impl  [ ] docstring  [ ] test

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
