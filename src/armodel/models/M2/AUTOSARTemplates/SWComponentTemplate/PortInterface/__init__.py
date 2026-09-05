"""
This module contains classes for representing AUTOSAR port interfaces
in the SWComponentTemplate module. It includes various types of port
interfaces such as sender/receiver, client/server, mode switch, and
parameter interfaces, as well as mapping classes for interface mappings.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from typing import List, Optional, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype, ModeDeclarationGroupPrototypeMapping
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger, TriggerMapping

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceProviderEnum
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleInvalidEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement, AtpType
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ArgumentDirectionEnum,
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AutosarDataPrototype, ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef


class PortInterface(AtpType, ABC):
    """Abstract base class for an interface that is either provided or required by a port of a software component."""

    # PortInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.18, p.87
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIsService   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIsService   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getServiceKind [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setServiceKind [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PortInterface:
            raise TypeError("PortInterface is an abstract class.")
        super().__init__(parent, short_name)

        # This flag is set if the PortInterface is to be used for communication between an
        # ApplicationSwComponentType or ServiceProxySwComponentType or SensorActuatorSwComponentType or
        # ComplexDeviceDriverSwComponentType or ServiceSwComponentType or EcuAbstractionSwComponentType and a
        # ServiceSwComponentType (namely an AUTOSAR Service) located on the same ECU. Otherwise the flag is not set.
        self.isService: Optional[Boolean] = None

        # This attribute provides further details about the nature of the applied service.
        self.serviceKind: Optional["ServiceProviderEnum"] = None

    def getIsService(self) -> Optional[Boolean]:
        """
        Gets the isService flag of this PortInterface.

        This flag is set if the PortInterface is to be used for communication between an ApplicationSwComponentType or
        ServiceProxySwComponentType or SensorActuatorSwComponentType or ComplexDeviceDriverSwComponentType or
        ServiceSwComponentType or EcuAbstractionSwComponentType and a ServiceSwComponentType (namely an AUTOSAR Service)
        located on the same ECU. Otherwise the flag is not set.

        Returns:
            Optional[Boolean]: The isService flag, or None if not set
        """
        return self.isService

    def setIsService(self, value: Optional[Boolean]) -> "PortInterface":
        """
        Sets the isService flag of this PortInterface.

        This flag is set if the PortInterface is to be used for communication between an ApplicationSwComponentType or
        ServiceProxySwComponentType or SensorActuatorSwComponentType or ComplexDeviceDriverSwComponentType or
        ServiceSwComponentType or EcuAbstractionSwComponentType and a ServiceSwComponentType (namely an AUTOSAR Service)
        located on the same ECU. Otherwise the flag is not set.
        A None value is a no-op and does not overwrite an existing isService.

        Args:
            value: The isService flag to set

        Returns:
            PortInterface: self for method chaining
        """
        if value is not None:
            self.isService = value
        return self

    def getServiceKind(self) -> Optional["ServiceProviderEnum"]:
        """
        Gets the serviceKind of this PortInterface.

        This attribute provides further details about the nature of the applied service.

        Returns:
            Optional[ServiceProviderEnum]: The serviceKind, or None if not set
        """
        return self.serviceKind

    def setServiceKind(self, value: Optional["ServiceProviderEnum"]) -> "PortInterface":
        """
        Sets the serviceKind of this PortInterface.

        This attribute provides further details about the nature of the applied service.
        A None value is a no-op and does not overwrite an existing serviceKind.

        Args:
            value: The serviceKind to set

        Returns:
            PortInterface: self for method chaining
        """
        if value is not None:
            self.serviceKind = value
        return self


class DataInterface(PortInterface, ABC):
    """The purpose of this meta-class is to act as an abstract base class for subclasses that share the semantics of being concerned about data (as opposed to e.g. operations)."""

    # DataInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.19, p.87 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DataInterface:
            raise TypeError("DataInterface is an abstract class.")
        super().__init__(parent, short_name)


class NvDataInterface(DataInterface):
    """A non volatile data interface declares a number of VariableDataPrototypes to be exchanged between non volatile block components and atomic software components."""

    # NvDataInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.5, p.664 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNvDatas     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createNvData   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNvData      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        # The VariableDataPrototype of this nv data interface.
        self.nvDatas: List[VariableDataPrototype] = []

    def getNvDatas(self) -> List[VariableDataPrototype]:
        """The VariableDataPrototype of this nv data interface."""
        return self.nvDatas

    def createNvData(self, short_name: str) -> VariableDataPrototype:
        """The VariableDataPrototype of this nv data interface."""
        if self.IsElementExists(short_name, VariableDataPrototype):
            return self.getElement(short_name, VariableDataPrototype)
        prototype = VariableDataPrototype(self, short_name)
        self.addElement(prototype)
        self.nvDatas.append(prototype)
        return prototype

    def getNvData(self, short_name: str) -> VariableDataPrototype:
        """The VariableDataPrototype of this nv data interface."""
        return self.getElement(short_name, VariableDataPrototype)


class ParameterInterface(DataInterface):
    """A parameter interface declares a number of parameter and characteristic values to be exchanged between parameter components and software components."""

    # ParameterInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 2.2, p.41 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getParameters                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createParameterDataPrototype [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The ParameterDataPrototype of this ParameterInterface.
        self.parameters: List[ParameterDataPrototype] = []

    def getParameters(self) -> List[ParameterDataPrototype]:
        """The ParameterDataPrototype of this ParameterInterface."""
        return self.parameters

    def createParameterDataPrototype(self, short_name: str) -> ParameterDataPrototype:
        """The ParameterDataPrototype of this ParameterInterface."""
        if self.IsElementExists(short_name, ParameterDataPrototype):
            return self.getElement(short_name, ParameterDataPrototype)
        prototype = ParameterDataPrototype(self, short_name)
        self.addElement(prototype)
        self.parameters.append(prototype)
        return prototype


class InvalidationPolicy(ARObject):
    """Specifies whether the component can actively invalidate a particular dataElement. If no invalidationPolicy points to a dataElement this is considered to yield the identical result as if the handleInvalid attribute was set to dontInvalidate."""

    # InvalidationPolicy method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.2, p.97 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElementRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHandleInvalid     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHandleInvalid     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the dataElement for which the InvalidationPolicy applies.
        self.dataElementRef: Optional[RefType] = None

        # This attribute controls how invalidation is applied to the dataElement.
        self.handleInvalid: Optional["HandleInvalidEnum"] = None

    def getDataElementRef(self) -> Optional[RefType]:
        """
        Reference to the dataElement for which the InvalidationPolicy applies.
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> "InvalidationPolicy":
        """
        Reference to the dataElement for which the InvalidationPolicy applies. A None value is a no-op and is not set.
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getHandleInvalid(self) -> Optional["HandleInvalidEnum"]:
        """
        This attribute controls how invalidation is applied to the dataElement.
        """
        return self.handleInvalid

    def setHandleInvalid(self, value: Optional["HandleInvalidEnum"]) -> "InvalidationPolicy":
        """
        This attribute controls how invalidation is applied to the dataElement. A None value is a no-op and is not set.
        """
        if value is not None:
            self.handleInvalid = value
        return self


class MetaDataItem(ARObject):
    """
    This meta-class represents a single meta-data item.
    """

    # MetaDataItem method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.4, p.98 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLength            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLength            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMetaDataItemType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMetaDataItemType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute determines the length of the MetaDataItem at run-time.
        self.length: Optional[PositiveInteger] = None

        # This aggregation contributes the specification of the concrete meta-data item type.
        self.metaDataItemType: Optional[TextValueSpecification] = None

    def getLength(self) -> Optional[PositiveInteger]:
        """
        This attribute determines the length of the MetaDataItem at run-time.
        """
        return self.length

    def setLength(self, value: Optional[PositiveInteger]) -> "MetaDataItem":
        """
        This attribute determines the length of the MetaDataItem at run-time. A None value is a no-op and does not overwrite an existing length.
        """
        if value is not None:
            self.length = value
        return self

    def getMetaDataItemType(self) -> Optional[TextValueSpecification]:
        """
        This aggregation contributes the specification of the concrete meta-data item type.
        """
        return self.metaDataItemType

    def setMetaDataItemType(self, value: Optional[TextValueSpecification]) -> "MetaDataItem":
        """
        This aggregation contributes the specification of the concrete meta-data item type. A None value is a no-op and does not overwrite an existing metaDataItemType.
        """
        if value is not None:
            self.metaDataItemType = value
        return self


class MetaDataItemSet(ARObject):
    """
    This meta-class represents the ability to define a set of meta-data items to be used in SenderReceiver Interfaces.
    """

    # MetaDataItemSet method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.5, p.99 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElementRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDataElementRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMetaDataItems    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addMetaDataItem     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This reference identifies the dataElement for which the ordered list of meta-data items is defined.
        self.dataElementRefs: List[RefType] = []

        # This aggregation represents the ordered definition of meta-data items.
        self.metaDataItems: List[MetaDataItem] = []

    def getDataElementRefs(self) -> List[RefType]:
        """
        This reference identifies the dataElement for which the ordered list of meta-data items is defined.
        """
        return self.dataElementRefs

    def addDataElementRef(self, value: RefType):
        """
        This reference identifies the dataElement for which the ordered list of meta-data items is defined.
        """
        self.dataElementRefs.append(value)
        return self

    def getMetaDataItems(self) -> List[MetaDataItem]:
        """
        This aggregation represents the ordered definition of meta-data items.
        """
        return self.metaDataItems

    def addMetaDataItem(self, value: MetaDataItem):
        """
        This aggregation represents the ordered definition of meta-data items.
        """
        self.metaDataItems.append(value)
        return self


class SenderReceiverInterface(DataInterface):
    """A sender/receiver interface declares a number of data elements to be sent and received."""

    # SenderReceiverInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.1, p.94 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createDataElement         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElements           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDataElement            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addInvalidationPolicy     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createInvalidationPolicy  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInvalidationPolicies   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addMetaDataItemSet        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMetaDataItemSets       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The data elements of this SenderReceiverInterface.
        self.dataElements: List[VariableDataPrototype] = []

        # InvalidationPolicy for a particular dataElement
        self.invalidationPolicies: List[InvalidationPolicy] = []

        # This aggregation defines fixed sets of meta-data items associated with dataElements of the enclosing Sender ReceiverInterface
        self.metaDataItemSets: List[MetaDataItemSet] = []

    def createDataElement(self, short_name: str) -> VariableDataPrototype:
        """
        The data elements of this SenderReceiverInterface.
        """
        if not self.IsElementExists(short_name, VariableDataPrototype):
            data_element = VariableDataPrototype(self, short_name)
            self.addElement(data_element)
            self.dataElements.append(data_element)
        return self.getElement(short_name, VariableDataPrototype)

    def getDataElements(self) -> List[VariableDataPrototype]:
        """
        The data elements of this SenderReceiverInterface.
        """
        return self.dataElements

    def getDataElement(self, short_name: str) -> VariableDataPrototype:
        """
        The data elements of this SenderReceiverInterface.
        """
        return self.getElement(short_name, VariableDataPrototype)

    def addInvalidationPolicy(self, value: InvalidationPolicy) -> "SenderReceiverInterface":
        """
        InvalidationPolicy for a particular dataElement
        """
        if value is not None:
            self.invalidationPolicies.append(value)
        return self

    def createInvalidationPolicy(self) -> InvalidationPolicy:
        """
        InvalidationPolicy for a particular dataElement
        """
        policy = InvalidationPolicy()
        self.invalidationPolicies.append(policy)
        return policy

    def getInvalidationPolicies(self) -> List[InvalidationPolicy]:
        """
        InvalidationPolicy for a particular dataElement
        """
        return self.invalidationPolicies

    def addMetaDataItemSet(self, value: MetaDataItemSet) -> "SenderReceiverInterface":
        """
        This aggregation defines fixed sets of meta-data items associated with dataElements of the enclosing Sender ReceiverInterface
        """
        if value is not None:
            self.metaDataItemSets.append(value)
        return self

    def getMetaDataItemSets(self) -> List[MetaDataItemSet]:
        """
        This aggregation defines fixed sets of meta-data items associated with dataElements of the enclosing Sender ReceiverInterface
        """
        return self.metaDataItemSets


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


class ArgumentDataPrototype(AutosarDataPrototype, VariationPointCapable):
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
    """
    This is a user-defined error that is associated with an element of an AUTOSAR interface. It is specific for the particular functionality or service provided by the AUTOSAR software component.
    """

    # ApplicationError method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.11, p.108
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getErrorCode      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setErrorCode      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The RTE generator is forced to assign this value to the corresponding error symbol. Note that for error codes certain ranges are predefined (see RTE specification).
        self.errorCode: Optional[Integer] = None

    def getErrorCode(self) -> Optional[Integer]:
        """
        Gets the error code that the RTE generator is forced to assign to the corresponding error symbol.
        Note that for error codes certain ranges are predefined (see RTE specification).

        Returns:
            Integer representing the error code, or None if not set
        """
        return self.errorCode

    def setErrorCode(self, value: Optional[Integer]) -> "ApplicationError":
        """
        Sets the error code that the RTE generator is forced to assign to the corresponding error symbol.
        Note that for error codes certain ranges are predefined (see RTE specification).
        A None value is a no-op and does not overwrite an existing error code.

        Args:
            value: The error code Integer to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.errorCode = value
        return self


class ClientServerOperation(AtpStructureElement, VariationPointCapable):
    """
    An operation declared within the scope of a client/server interface.
    """

    # ClientServerOperation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.7, p.102
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] createArgumentDataPrototype  [x] impl  [x] docstring  [x] test
    # [x] getArguments                 [x] impl  [x] docstring  [x] test
    # [x] getDiagArgIntegrity          [x] impl  [x] docstring  [x] test
    # [x] setDiagArgIntegrity          [x] impl  [x] docstring  [x] test
    # [x] addPossibleErrorRef          [x] impl  [x] docstring  [x] test
    # [x] getPossibleErrorRefs         [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Constructs a ClientServerOperation.

        Args:
            parent: The parent ARObject
            short_name: The short name of the operation
        """
        super().__init__(parent, short_name)

        # An argument of this ClientServerOperation
        self.arguments: List[ArgumentDataPrototype] = []

        # This attribute shall only be used in the implementation of diagnostic routines to support
        # the case where input and output arguments are allocated in a shared buffer and might
        # unintentionally overwrite input arguments by tentative write operations to output
        # arguments. The value true means that the ClientServerOperation is aware of the usage of a
        # shared buffer and takes precautions to avoid unintentional overwrite of input arguments.
        # [constr_1724]
        self.diagArgIntegrity: Optional[Boolean] = None

        # Possible errors that may by raised by the referring operation.
        self.possibleErrorRefs: List[RefType] = []

    def createArgumentDataPrototype(self, short_name: str) -> ArgumentDataPrototype:
        """
        Creates an ArgumentDataPrototype of this ClientServerOperation with the given short name,
        or returns the existing one if it already exists.

        An argument of this ClientServerOperation.

        Args:
            short_name: The short name for the new ArgumentDataPrototype

        Returns:
            The created (or existing) ArgumentDataPrototype
        """
        if not self.IsElementExists(short_name, ArgumentDataPrototype):
            prototype = ArgumentDataPrototype(self, short_name)
            self.addElement(prototype)
            self.arguments.append(prototype)
        return self.getElement(short_name, ArgumentDataPrototype)

    def getArguments(self) -> List[ArgumentDataPrototype]:
        """
        Gets the ArgumentDataPrototype objects of this ClientServerOperation.

        An argument of this ClientServerOperation.

        Returns:
            The list of ArgumentDataPrototype instances
        """
        return self.arguments

    def getDiagArgIntegrity(self) -> Optional[Boolean]:
        """
        Returns the diagArgIntegrity flag of this ClientServerOperation.

        This attribute shall only be used in the implementation of diagnostic routines to support the
        case where input and output arguments are allocated in a shared buffer and might
        unintentionally overwrite input arguments by tentative write operations to output arguments.
        The value true means that the ClientServerOperation is aware of the usage of a shared buffer
        and takes precautions to avoid unintentional overwrite of input arguments. [constr_1724]

        Returns:
            Optional[Boolean]: The diagArgIntegrity flag, or None if not set
        """
        return self.diagArgIntegrity

    def setDiagArgIntegrity(self, value: Optional[Boolean]) -> "ClientServerOperation":
        """
        Sets the diagArgIntegrity flag of this ClientServerOperation.

        This attribute shall only be used in the implementation of diagnostic routines to support the
        case where input and output arguments are allocated in a shared buffer and might
        unintentionally overwrite input arguments by tentative write operations to output arguments.
        The value true means that the ClientServerOperation is aware of the usage of a shared buffer
        and takes precautions to avoid unintentional overwrite of input arguments. [constr_1724]
        A None value is a no-op and does not overwrite an existing diagArgIntegrity.

        Args:
            value: The diagArgIntegrity flag to set

        Returns:
            ClientServerOperation: self for method chaining
        """
        if value is not None:
            self.diagArgIntegrity = value
        return self

    def addPossibleErrorRef(self, value: Optional[RefType]) -> "ClientServerOperation":
        """
        Adds a possible error to this ClientServerOperation.

        Possible errors that may by raised by the referring operation.

        Args:
            value: The possible error reference to add

        Returns:
            ClientServerOperation: self for method chaining
        """
        if value is not None:
            self.possibleErrorRefs.append(value)
        return self

    def getPossibleErrorRefs(self) -> List[RefType]:
        """
        Gets the possible errors that may be raised by this ClientServerOperation.

        Possible errors that may by raised by the referring operation.

        Returns:
            The list of possible error references
        """
        return self.possibleErrorRefs


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
    # [x] getOperations                [x] impl  [x] docstring  [x] test
    # [x] createApplicationError       [x] impl  [x] docstring  [x] test
    # [x] getPossibleErrors            [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # ClientServerOperation(s) of this ClientServerInterface.
        self.operations: List[ClientServerOperation] = []

        # Application errors that are defined as part of this interface.
        self.possibleErrors: List[ApplicationError] = []

    def createOperation(self, short_name: str) -> ClientServerOperation:
        """
        Creates a ClientServerOperation of this ClientServerInterface with the
        given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new ClientServerOperation

        Returns:
            The created (or existing) ClientServerOperation
        """
        if not self.IsElementExists(short_name, ClientServerOperation):
            operation = ClientServerOperation(self, short_name)
            self.addElement(operation)
            self.operations.append(operation)
        return self.getElement(short_name, ClientServerOperation)

    def getOperations(self) -> List[ClientServerOperation]:
        """
        Gets the ClientServerOperation(s) of this ClientServerInterface.

        Returns:
            The list of ClientServerOperation instances
        """
        return self.operations

    def createApplicationError(self, short_name: str) -> ApplicationError:
        """
        Creates an ApplicationError of this ClientServerInterface with the
        given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new ApplicationError

        Returns:
            The created (or existing) ApplicationError
        """
        if not self.IsElementExists(short_name, ApplicationError):
            error = ApplicationError(self, short_name)
            self.addElement(error)
            self.possibleErrors.append(error)
        return self.getElement(short_name, ApplicationError)

    def getPossibleErrors(self) -> List[ApplicationError]:
        """
        Gets the Application errors that are defined as part of this interface.

        Returns:
            The list of ApplicationError instances
        """
        return self.possibleErrors


class TriggerInterface(PortInterface):
    """A trigger interface declares a number of triggers that can be sent by an trigger source."""

    # TriggerInterface method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.12, p.109 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createTrigger  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTriggers    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The Trigger of this trigger interface.
        self.triggers: List[Trigger] = []

    def createTrigger(self, short_name: str) -> Trigger:
        """The Trigger of this trigger interface."""
        if not self.IsElementExists(short_name, Trigger):
            trigger = Trigger(self, short_name)
            self.addElement(trigger)
            self.triggers.append(trigger)
        return self.getElement(short_name, Trigger)

    def getTriggers(self) -> List[Trigger]:
        """The Trigger of this trigger interface."""
        return self.triggers


class ModeSwitchInterface(PortInterface):
    """
    A mode switch interface declares a ModeDeclarationGroupPrototype to be sent and received. Tags: atp.recommendedPackage=PortInterfaces
    """

    # ModeSwitchInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.16, p.113
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createModeGroup    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeGroup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The ModeDeclarationGroupPrototype of this mode interface.
        self.modeGroup: Optional[ModeDeclarationGroupPrototype] = None

    def createModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """
        Creates the ModeDeclarationGroupPrototype of this mode interface.
        Returns the existing prototype when the short name already exists.

        The ModeDeclarationGroupPrototype of this mode interface.

        Args:
            short_name: The short name of the ModeDeclarationGroupPrototype

        Returns:
            The created or existing ModeDeclarationGroupPrototype
        """
        if not self.IsElementExists(short_name, ModeDeclarationGroupPrototype):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
        mode_group = self.getElement(short_name, ModeDeclarationGroupPrototype)
        self.modeGroup = mode_group
        return mode_group

    def getModeGroup(self) -> Optional[ModeDeclarationGroupPrototype]:
        """
        Gets the ModeDeclarationGroupPrototype of this mode interface.

        The ModeDeclarationGroupPrototype of this mode interface.

        Returns:
            The ModeDeclarationGroupPrototype, or None if not set
        """
        return self.modeGroup


class PortInterfaceMapping(AtpBlueprintable, VariationPointCapable, ABC):
    """
    Specifies one PortInterfaceMapping to support the connection of Ports typed by two different Port Interfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
    """

    # PortInterfaceMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.20, p.119 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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


class SubElementMapping(ARObject):
    """
    This meta-class allows for the definition of mappings of elements of a composite data type.
    """

    # SubElementMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.32, p.137
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFirstElement      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFirstElement      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondElement     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondElement     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addTextTableMapping  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTextTableMappings [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This represents the first element referenced in the scope of the mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=firstElement, firstElement.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.firstElement: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef] = None

        # This represents the second element referenced in the scope of the mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=secondElement, secondElement.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.secondElement: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef] = None

        # This allows for the text-table translation of individual elements of a composite data type.
        self.textTableMappings: List["TextTableMapping"] = []

    def getFirstElement(self) -> Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]:
        """
        Gets the first element referenced in the scope of the mapping.

        This represents the first element referenced in the scope of the mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=firstElement, firstElement.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            ApplicationCompositeElementInPortInterfaceInstanceRef, or None if not set
        """
        return self.firstElement

    def setFirstElement(self, value: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]) -> "SubElementMapping":
        """
        Sets the first element referenced in the scope of the mapping.
        A None value is a no-op and does not overwrite an existing first element.

        This represents the first element referenced in the scope of the mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=firstElement, firstElement.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            value: The ApplicationCompositeElementInPortInterfaceInstanceRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.firstElement = value
        return self

    def getSecondElement(self) -> Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]:
        """
        Gets the second element referenced in the scope of the mapping.

        This represents the second element referenced in the scope of the mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=secondElement, secondElement.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            ApplicationCompositeElementInPortInterfaceInstanceRef, or None if not set
        """
        return self.secondElement

    def setSecondElement(self, value: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]) -> "SubElementMapping":
        """
        Sets the second element referenced in the scope of the mapping.
        A None value is a no-op and does not overwrite an existing second element.

        This represents the second element referenced in the scope of the mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=secondElement, secondElement.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            value: The ApplicationCompositeElementInPortInterfaceInstanceRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.secondElement = value
        return self

    def addTextTableMapping(self, value: Optional["TextTableMapping"]) -> "SubElementMapping":
        """
        Adds a TextTableMapping allowing for the text-table translation of individual elements of a composite data type.
        A None value is a no-op and does not append anything.

        This allows for the text-table translation of individual elements of a composite data type.

        Args:
            value: The TextTableMapping to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.textTableMappings.append(value)
        return self

    def getTextTableMappings(self) -> List["TextTableMapping"]:
        """
        Gets the TextTableMappings allowing for the text-table translation of individual elements of a composite data type.

        This allows for the text-table translation of individual elements of a composite data type.

        Returns:
            List of TextTableMapping instances
        """
        return self.textTableMappings


class DataPrototypeMapping(ARObject):
    """
    Defines the mapping of two particular VariableDataPrototypes, ParameterDataPrototypes or Argument DataPrototypes with non-equal shortNames, non-equal structure (specific condition is described by [constr_1187]), and/or non-equal semantic (resolution or range) in context of two different Sender ReceiverInterface, NvDataInterface or ParameterInterface or Operations. If the semantic is unequal, the following rules apply: The textTableMapping is only applicable if the referred DataPrototypes are typed by AutosarDataType referring to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE. In the case that the DataPrototypes are typed by AutosarDataType either referring to CompuMethods of category LINEAR, IDENTICAL or referring to no CompuMethod (which is similar as IDENTICAL) the linear conversion factor is calculated out of the factorSiToUnit and offsetSiToUnit attributes of the referred Units and the CompuRationalCoeffs of a compuInternalToPhys of the referred CompuMethods.
    """

    # DataPrototypeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.22, p.125
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFirstDataPrototypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFirstDataPrototypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFirstToSecondDataTransformationRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFirstToSecondDataTransformationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondDataPrototypeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondDataPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondToFirstDataTransformationRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondToFirstDataTransformationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addSubElementMapping         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSubElementMappings        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTextTableMapping          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTextTableMappings         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # First to be mapped DataPrototype in context of a Sender ReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        self.firstDataPrototypeRef: Optional[RefType] = None

        # This reference defines the need to execute the Data Transformation <Mip>_<transformerId> functions of the transformation chain when communicating from the Data PrototypeMapping.firstDataPrototype to the Data PrototypeMapping.secondDataPrototype. This reference also specifies the reverse Data Transformation <Mip>_Inv_<transformerId> functions of the transformation chain (i.e. from the DataPrototype Mapping.secondDataPrototype to the DataPrototype Mapping.firstDataPrototype) if the referenced Data Transformation is symmetric, i.e. attribute Data Transformation.dataTransformationKind is set to symmetric.
        self.firstToSecondDataTransformationRef: Optional[RefType] = None

        # Second to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, Parameter Interface or Operation.
        self.secondDataPrototypeRef: Optional[RefType] = None

        # This defines the need to execute the reverse Data Transformation <Mip>_Inv_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.secondDataPrototype to the Data PrototypeMapping.firstDataPrototype.
        self.secondToFirstDataTransformationRef: Optional[RefType] = None

        # This represents the owned SubelementMapping.
        self.subElementMappings: List[SubElementMapping] = []

        # Applied TextTableMapping(s)
        self.textTableMappings: List["TextTableMapping"] = []

    def getFirstDataPrototypeRef(self) -> Optional[RefType]:
        """
        First to be mapped DataPrototype in context of a Sender ReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        """
        return self.firstDataPrototypeRef

    def setFirstDataPrototypeRef(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        First to be mapped DataPrototype in context of a Sender ReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        A None value is a no-op and does not overwrite an existing firstDataPrototypeRef.
        """
        if value is not None:
            self.firstDataPrototypeRef = value
        return self

    def getFirstToSecondDataTransformationRef(self) -> Optional[RefType]:
        """
        This reference defines the need to execute the Data Transformation <Mip>_<transformerId> functions of the transformation chain when communicating from the Data PrototypeMapping.firstDataPrototype to the Data PrototypeMapping.secondDataPrototype. This reference also specifies the reverse Data Transformation <Mip>_Inv_<transformerId> functions of the transformation chain (i.e. from the DataPrototype Mapping.secondDataPrototype to the DataPrototype Mapping.firstDataPrototype) if the referenced Data Transformation is symmetric, i.e. attribute Data Transformation.dataTransformationKind is set to symmetric.
        """
        return self.firstToSecondDataTransformationRef

    def setFirstToSecondDataTransformationRef(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        This reference defines the need to execute the Data Transformation <Mip>_<transformerId> functions of the transformation chain when communicating from the Data PrototypeMapping.firstDataPrototype to the Data PrototypeMapping.secondDataPrototype. This reference also specifies the reverse Data Transformation <Mip>_Inv_<transformerId> functions of the transformation chain (i.e. from the DataPrototype Mapping.secondDataPrototype to the DataPrototype Mapping.firstDataPrototype) if the referenced Data Transformation is symmetric, i.e. attribute Data Transformation.dataTransformationKind is set to symmetric.
        A None value is a no-op and does not overwrite an existing firstToSecondDataTransformationRef.
        """
        if value is not None:
            self.firstToSecondDataTransformationRef = value
        return self

    def getSecondDataPrototypeRef(self) -> Optional[RefType]:
        """
        Second to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, Parameter Interface or Operation.
        """
        return self.secondDataPrototypeRef

    def setSecondDataPrototypeRef(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        Second to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, Parameter Interface or Operation.
        A None value is a no-op and does not overwrite an existing secondDataPrototypeRef.
        """
        if value is not None:
            self.secondDataPrototypeRef = value
        return self

    def getSecondToFirstDataTransformationRef(self) -> Optional[RefType]:
        """
        This defines the need to execute the reverse Data Transformation <Mip>_Inv_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.secondDataPrototype to the Data PrototypeMapping.firstDataPrototype.
        """
        return self.secondToFirstDataTransformationRef

    def setSecondToFirstDataTransformationRef(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        This defines the need to execute the reverse Data Transformation <Mip>_Inv_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.secondDataPrototype to the Data PrototypeMapping.firstDataPrototype.
        A None value is a no-op and does not overwrite an existing secondToFirstDataTransformationRef.
        """
        if value is not None:
            self.secondToFirstDataTransformationRef = value
        return self

    def addSubElementMapping(self, value: Optional[SubElementMapping]) -> "DataPrototypeMapping":
        """
        This represents the owned SubelementMapping.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.subElementMappings.append(value)
        return self

    def getSubElementMappings(self) -> List[SubElementMapping]:
        """
        This represents the owned SubelementMapping.
        """
        return self.subElementMappings

    def addTextTableMapping(self, value: Optional["TextTableMapping"]) -> "DataPrototypeMapping":
        """
        Applied TextTableMapping(s)
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.textTableMappings.append(value)
        return self

    def getTextTableMappings(self) -> List["TextTableMapping"]:
        """
        Applied TextTableMapping(s)
        """
        return self.textTableMappings


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
    """
    Defines the mapping of unequal named Triggers in context of two different TriggerInterfaces.
    """

    # TriggerInterfaceMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.30, p.134 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTriggerMappings            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTriggerMapping             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Mapping of two Trigger in two different TriggerInterface
        self.triggerMappings: List[TriggerMapping] = []

    def getTriggerMappings(self) -> List[TriggerMapping]:
        """
        Mapping of two Trigger in two different TriggerInterface
        """
        return self.triggerMappings

    def addTriggerMapping(self, value: Optional[TriggerMapping]) -> "TriggerInterfaceMapping":
        """
        Mapping of two Trigger in two different TriggerInterface
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.triggerMappings.append(value)
        return self


class ModeDeclarationMapping(AtpStructureElement):
    """
    This meta-class implements a concrete mapping of two ModeDeclarations.
    """

    # ModeDeclarationMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.29, p.132
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFirstModeRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addFirstModeRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondModeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondModeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the first ModeDeclaration of the Mode DeclarationMapping. This reference has the multiplicity 1 .. * to support use cases where e.g. one mode of the mode user is mapped to several modes of the mode manager.
        self.firstModeRefs: List[RefType] = []

        # This represents the second ModeDeclaration of the Mode DeclarationMapping.
        self.secondModeRef: Optional[RefType] = None

    def getFirstModeRefs(self) -> List[RefType]:
        """
        This represents the first ModeDeclaration of the Mode DeclarationMapping. This reference has the multiplicity 1 .. * to support use cases where e.g. one mode of the mode user is mapped to several modes of the mode manager.
        """
        return self.firstModeRefs

    def addFirstModeRef(self, value: Optional[RefType]) -> "ModeDeclarationMapping":
        """
        This represents the first ModeDeclaration of the Mode DeclarationMapping. This reference has the multiplicity 1 .. * to support use cases where e.g. one mode of the mode user is mapped to several modes of the mode manager.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.firstModeRefs.append(value)
        return self

    def getSecondModeRef(self) -> Optional[RefType]:
        """
        This represents the second ModeDeclaration of the Mode DeclarationMapping.
        """
        return self.secondModeRef

    def setSecondModeRef(self, value: Optional[RefType]) -> "ModeDeclarationMapping":
        """
        This represents the second ModeDeclaration of the Mode DeclarationMapping.
        A None value is a no-op and does not overwrite an existing secondModeRef.
        """
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
        if not self.IsElementExists(short_name, ModeDeclarationMapping):
            mapping = ModeDeclarationMapping(self, short_name)
            self.addElement(mapping)
            self.modeDeclarationMappings.append(mapping)
        return self.getElement(short_name, ModeDeclarationMapping)


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement  # noqa: E402


class PortInterfaceMappingSet(ARElement):
    """
    Specifies a set of (one or more) PortInterfaceMappings.
    """

    # PortInterfaceMappingSet method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.19, p.119 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPortInterfaceMappings                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createVariableAndParameterInterfaceMapping [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createClientServerInterfaceMapping         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createModeInterfaceMapping                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createTriggerInterfaceMapping              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        self.portInterfaceMappings: List[PortInterfaceMapping] = []

    def getPortInterfaceMappings(self) -> List[PortInterfaceMapping]:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        return self.portInterfaceMappings

    def createVariableAndParameterInterfaceMapping(self, short_name: str) -> VariableAndParameterInterfaceMapping:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        if not self.IsElementExists(short_name, VariableAndParameterInterfaceMapping):
            mapping = VariableAndParameterInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name, VariableAndParameterInterfaceMapping)

    def createClientServerInterfaceMapping(self, short_name: str) -> ClientServerInterfaceMapping:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        if not self.IsElementExists(short_name, ClientServerInterfaceMapping):
            mapping = ClientServerInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name, ClientServerInterfaceMapping)

    def createModeInterfaceMapping(self, short_name: str) -> ModeInterfaceMapping:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        if not self.IsElementExists(short_name, ModeInterfaceMapping):
            mapping = ModeInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name, ModeInterfaceMapping)

    def createTriggerInterfaceMapping(self, short_name: str) -> TriggerInterfaceMapping:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        if not self.IsElementExists(short_name, TriggerInterfaceMapping):
            mapping = TriggerInterfaceMapping(self, short_name)
            self.addElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return self.getElement(short_name, TriggerInterfaceMapping)


class TextTableMapping(ARObject):
    """
    Defines the mapping of two DataPrototypes typed by AutosarDataTypes that refer to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE.
    """

    # TextTableMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.36, p.145
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBitfieldTextTableMaskFirst [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBitfieldTextTableMaskFirst [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBitfieldTextTableMaskSecond [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBitfieldTextTableMaskSecond [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIdenticalMapping          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIdenticalMapping          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMappingDirection          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMappingDirection          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addValuePair                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValuePairs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the first element of the TextTableMapping. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.bitfieldTextTableMaskFirst: Optional[PositiveInteger] = None

        # This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the second element of the TextTableMapping. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.bitfieldTextTableMaskSecond: Optional[PositiveInteger] = None

        # If identicalMapping is set == true the values of the two referenced DataPrototypes do not need any conversion of the values.
        self.identicalMapping: Optional[Boolean] = None

        # Specifies the conversion direction for which the TextTableMapping is applicable.
        self.mappingDirection = None

        # Defines a pair of values which are translated into each other.
        self.valuePairs: List = []

    def getBitfieldTextTableMaskFirst(self) -> Optional[PositiveInteger]:
        """
        Gets the bit mask for the first element of the TextTableMapping.

        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the first element of the TextTableMapping. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        Returns:
            PositiveInteger, or None if not set
        """
        return self.bitfieldTextTableMaskFirst

    def setBitfieldTextTableMaskFirst(self, value: Optional[PositiveInteger]) -> "TextTableMapping":
        """
        Sets the bit mask for the first element of the TextTableMapping.
        A None value is a no-op and does not overwrite an existing bit mask.

        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the first element of the TextTableMapping. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        Args:
            value: The bit mask to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bitfieldTextTableMaskFirst = value
        return self

    def getBitfieldTextTableMaskSecond(self) -> Optional[PositiveInteger]:
        """
        Gets the bit mask for the second element of the TextTableMapping.

        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the second element of the TextTableMapping. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        Returns:
            PositiveInteger, or None if not set
        """
        return self.bitfieldTextTableMaskSecond

    def setBitfieldTextTableMaskSecond(self, value: Optional[PositiveInteger]) -> "TextTableMapping":
        """
        Sets the bit mask for the second element of the TextTableMapping.
        A None value is a no-op and does not overwrite an existing bit mask.

        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the second element of the TextTableMapping. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        Args:
            value: The bit mask to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bitfieldTextTableMaskSecond = value
        return self

    def getIdenticalMapping(self) -> Optional[Boolean]:
        """
        Gets whether the values of the two referenced DataPrototypes need any conversion of the values.

        If identicalMapping is set == true the values of the two referenced DataPrototypes do not need any conversion of the values.

        Returns:
            Boolean, or None if not set
        """
        return self.identicalMapping

    def setIdenticalMapping(self, value: Optional[Boolean]) -> "TextTableMapping":
        """
        Sets whether the values of the two referenced DataPrototypes need any conversion of the values.
        A None value is a no-op and does not overwrite an existing identicalMapping.

        If identicalMapping is set == true the values of the two referenced DataPrototypes do not need any conversion of the values.

        Args:
            value: The identicalMapping flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.identicalMapping = value
        return self

    def getMappingDirection(self):
        """
        Gets the conversion direction for which the TextTableMapping is applicable.

        Specifies the conversion direction for which the TextTableMapping is applicable.

        Returns:
            The mapping direction, or None if not set
        """
        return self.mappingDirection

    def setMappingDirection(self, value):
        """
        Sets the conversion direction for which the TextTableMapping is applicable.
        A None value is a no-op and does not overwrite an existing mapping direction.

        Specifies the conversion direction for which the TextTableMapping is applicable.

        Args:
            value: The mapping direction to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mappingDirection = value
        return self

    def addValuePair(self, value):
        """
        Adds a pair of values which are translated into each other.
        A None value is a no-op and does not append anything.

        Defines a pair of values which are translated into each other.

        Args:
            value: The TextTableValuePair to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.valuePairs.append(value)
        return self

    def getValuePairs(self) -> List:
        """
        Gets the pairs of values which are translated into each other.

        Defines a pair of values which are translated into each other.

        Returns:
            List of TextTableValuePair instances
        """
        return self.valuePairs
