"""
This module contains classes for representing AUTOSAR port interfaces
in the SWComponentTemplate module. It includes various types of port
interfaces such as sender/receiver, client/server, mode switch, and
parameter interfaces, as well as mapping classes for interface mappings.
"""

from __future__ import annotations


from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from typing import List, Optional, TYPE_CHECKING, cast

from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype, ModeDeclarationGroupPrototypeMapping
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger, TriggerMapping

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceProviderEnum

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleInvalidEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement, AtpType
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ArParameterInImplementationDataInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ArgumentDirectionEnum,
    Boolean,
    Integer,
    Numerical,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AutosarDataPrototype, ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef


class PortInterface(AtpType, ABC):
    """Abstract base class for an interface that is either provided or required by a port of a software component."""

    # PortInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.18, p.87 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIsService   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIsService   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceKind [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceKind [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PortInterface:
            raise TypeError("PortInterface is an abstract class.")
        super().__init__(parent, short_name)

        # This flag is set if the PortInterface is to be used for communication between an • ApplicationSwComponentType or • ServiceProxySwComponentType or • SensorActuatorSwComponentType or • ComplexDeviceDriverSwComponentType • ServiceSwComponentType • EcuAbstractionSwComponentType and a ServiceSwComponentType (namely an AUTOSAR Service) located on the same ECU. Otherwise the flag is not set.
        self.isService: Optional[Boolean] = None

        # This attribute provides further details about the nature of the applied service.
        self.serviceKind: Optional[ServiceProviderEnum] = None

    def getIsService(self) -> Optional[Boolean]:
        """
        This flag is set if the PortInterface is to be used for communication between an • ApplicationSwComponentType or • ServiceProxySwComponentType or • SensorActuatorSwComponentType or • ComplexDeviceDriverSwComponentType • ServiceSwComponentType • EcuAbstractionSwComponentType and a ServiceSwComponentType (namely an AUTOSAR Service) located on the same ECU. Otherwise the flag is not set.
        """
        return self.isService

    def setIsService(self, value: Optional[Boolean]) -> PortInterface:
        """
        This flag is set if the PortInterface is to be used for communication between an • ApplicationSwComponentType or • ServiceProxySwComponentType or • SensorActuatorSwComponentType or • ComplexDeviceDriverSwComponentType • ServiceSwComponentType • EcuAbstractionSwComponentType and a ServiceSwComponentType (namely an AUTOSAR Service) located on the same ECU. Otherwise the flag is not set.
        A None value is a no-op and does not overwrite an existing isService.
        """
        if value is not None:
            self.isService = value
        return self

    def getServiceKind(self) -> Optional[ServiceProviderEnum]:
        """
        This attribute provides further details about the nature of the applied service.
        """
        return self.serviceKind

    def setServiceKind(self, value: Optional[ServiceProviderEnum]) -> PortInterface:
        """
        This attribute provides further details about the nature of the applied service.
        A None value is a no-op and does not overwrite an existing serviceKind.
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
        if self.IsReferrableElementExists(short_name, VariableDataPrototype):
            return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))
        prototype = VariableDataPrototype(self, short_name)
        self.addReferrableElement(prototype)
        self.nvDatas.append(prototype)
        return prototype

    def getNvData(self, short_name: str) -> VariableDataPrototype:
        """The VariableDataPrototype of this nv data interface."""
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))


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
        if self.IsReferrableElementExists(short_name, ParameterDataPrototype):
            return cast(ParameterDataPrototype, self.getReferrableElement(short_name, ParameterDataPrototype))
        prototype = ParameterDataPrototype(self, short_name)
        self.addReferrableElement(prototype)
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
        self.handleInvalid: Optional[HandleInvalidEnum] = None

    def getDataElementRef(self) -> Optional[RefType]:
        """
        Reference to the dataElement for which the InvalidationPolicy applies.
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> InvalidationPolicy:
        """
        Reference to the dataElement for which the InvalidationPolicy applies. A None value is a no-op and is not set.
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getHandleInvalid(self) -> Optional[HandleInvalidEnum]:
        """
        This attribute controls how invalidation is applied to the dataElement.
        """
        return self.handleInvalid

    def setHandleInvalid(self, value: Optional[HandleInvalidEnum]) -> InvalidationPolicy:
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

    def setLength(self, value: Optional[PositiveInteger]) -> MetaDataItem:
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

    def setMetaDataItemType(self, value: Optional[TextValueSpecification]) -> MetaDataItem:
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
        if not self.IsReferrableElementExists(short_name, VariableDataPrototype):
            data_element = VariableDataPrototype(self, short_name)
            self.addReferrableElement(data_element)
            self.dataElements.append(data_element)
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))

    def getDataElements(self) -> List[VariableDataPrototype]:
        """
        The data elements of this SenderReceiverInterface.
        """
        return self.dataElements

    def getDataElement(self, short_name: str) -> VariableDataPrototype:
        """
        The data elements of this SenderReceiverInterface.
        """
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))

    def addInvalidationPolicy(self, value: InvalidationPolicy) -> SenderReceiverInterface:
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

    def addMetaDataItemSet(self, value: MetaDataItemSet) -> SenderReceiverInterface:
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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.10, p.105 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # The argument type of the RunnableEntity is derived from the AutosarDataType of the Argument Prototype. Tags: atp.EnumerationLiteralIndex=0
    USE_ARGUMENT_TYPE = "useArgumentType"

    # The argument type of the RunnableEntity is void. Tags: atp.EnumerationLiteralIndex=2
    USE_VOID = "useVoid"

    def __init__(self):
        super().__init__((ServerArgumentImplPolicyEnum.USE_ARGUMENT_TYPE, ServerArgumentImplPolicyEnum.USE_VOID))


class ArgumentDataPrototype(AutosarDataPrototype, VariationPointCapable):
    """
    An argument of an operation, much like a data element, but also carries direction information and is owned by a particular ClientServerOperation.
    """

    # ArgumentDataPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.8, p.103 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDirection                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setDirection                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getServerArgumentImplPolicy [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setServerArgumentImplPolicy [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute specifies the direction of the argument prototype.
        self.direction: Optional[ArgumentDirectionEnum] = None

        # This defines how the argument type of the servers RunnableEntity is implemented. If the attribute is not defined this has the same semantics as if the attribute is set to the value useArgumentType for primitive arguments and structures.
        self.serverArgumentImplPolicy: Optional[ServerArgumentImplPolicyEnum] = None

    def getDirection(self) -> Optional[ArgumentDirectionEnum]:
        """
        This attribute specifies the direction of the argument prototype.
        """
        return self.direction

    def setDirection(self, value: Optional[ArgumentDirectionEnum]) -> ArgumentDataPrototype:
        """
        This attribute specifies the direction of the argument prototype.
        A None value is a no-op and does not overwrite an existing direction.
        """
        if value is not None:
            self.direction = value
        return self

    def getServerArgumentImplPolicy(self) -> Optional[ServerArgumentImplPolicyEnum]:
        """
        This defines how the argument type of the servers RunnableEntity is implemented. If the attribute is not defined this has the same semantics as if the attribute is set to the value useArgumentType for primitive arguments and structures.
        """
        return self.serverArgumentImplPolicy

    def setServerArgumentImplPolicy(self, value: Optional[ServerArgumentImplPolicyEnum]) -> ArgumentDataPrototype:
        """
        This defines how the argument type of the servers RunnableEntity is implemented. If the attribute is not defined this has the same semantics as if the attribute is set to the value useArgumentType for primitive arguments and structures.
        A None value is a no-op and does not overwrite an existing serverArgumentImplPolicy.
        """
        if value is not None:
            self.serverArgumentImplPolicy = value
        return self


class ApplicationError(Identifiable):
    """
    This is a user-defined error that is associated with an element of an AUTOSAR interface. It is specific for the particular functionality or service provided by the AUTOSAR software component.
    """

    # ApplicationError method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.11, p.108 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getErrorCode  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setErrorCode  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The RTE generator is forced to assign this value to the corresponding error symbol. Note that for error codes certain ranges are predefined (see RTE specification).
        self.errorCode: Optional[Integer] = None

    def getErrorCode(self) -> Optional[Integer]:
        """
        The RTE generator is forced to assign this value to the corresponding error symbol. Note that for error codes certain ranges are predefined (see RTE specification).
        """
        return self.errorCode

    def setErrorCode(self, value: Optional[Integer]) -> ApplicationError:
        """
        The RTE generator is forced to assign this value to the corresponding error symbol. Note that for error codes certain ranges are predefined (see RTE specification).
        A None value is a no-op and does not overwrite an existing error code.
        """
        if value is not None:
            self.errorCode = value
        return self


class ClientServerOperation(AtpStructureElement, VariationPointCapable):
    """
    An operation declared within the scope of a client/server interface.
    """

    # ClientServerOperation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.7, p.102 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createArgumentDataPrototype  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArguments                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDiagArgIntegrity          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagArgIntegrity          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPossibleErrorRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPossibleErrorRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # An argument of this ClientServerOperation
        self.arguments: List[ArgumentDataPrototype] = []

        # This attribute shall only be used in the implementation of diagnostic routines to support the case where input and output arguments are allocated in a shared buffer and might unintentionally overwrite input arguments by tentative write operations to output arguments. This situation can happen during sliced execution or while output parameters are arrays (call by reference). The value true means that the ClientServerOperation is aware of the usage of a shared buffer and takes precautions to avoid unintentional overwrite of input arguments. If the attribute does not exist or is set to false the Client ServerOperation does not have to consider the usage of a shared buffer.
        self.diagArgIntegrity: Optional[Boolean] = None

        # Possible errors that may by raised by the referring operation.
        self.possibleErrorRefs: List[RefType] = []

    def createArgumentDataPrototype(self, short_name: str) -> ArgumentDataPrototype:
        """
        An argument of this ClientServerOperation
        """
        if not self.IsReferrableElementExists(short_name, ArgumentDataPrototype):
            prototype = ArgumentDataPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.arguments.append(prototype)
        return cast(ArgumentDataPrototype, self.getReferrableElement(short_name, ArgumentDataPrototype))

    def getArguments(self) -> List[ArgumentDataPrototype]:
        """
        An argument of this ClientServerOperation
        """
        return self.arguments

    def getDiagArgIntegrity(self) -> Optional[Boolean]:
        """
        This attribute shall only be used in the implementation of diagnostic routines to support the case where input and output arguments are allocated in a shared buffer and might unintentionally overwrite input arguments by tentative write operations to output arguments. This situation can happen during sliced execution or while output parameters are arrays (call by reference). The value true means that the ClientServerOperation is aware of the usage of a shared buffer and takes precautions to avoid unintentional overwrite of input arguments. If the attribute does not exist or is set to false the Client ServerOperation does not have to consider the usage of a shared buffer.
        """
        return self.diagArgIntegrity

    def setDiagArgIntegrity(self, value: Optional[Boolean]) -> ClientServerOperation:
        """
        This attribute shall only be used in the implementation of diagnostic routines to support the case where input and output arguments are allocated in a shared buffer and might unintentionally overwrite input arguments by tentative write operations to output arguments. This situation can happen during sliced execution or while output parameters are arrays (call by reference). The value true means that the ClientServerOperation is aware of the usage of a shared buffer and takes precautions to avoid unintentional overwrite of input arguments. If the attribute does not exist or is set to false the Client ServerOperation does not have to consider the usage of a shared buffer.
        A None value is a no-op and does not overwrite an existing diagArgIntegrity.
        """
        if value is not None:
            self.diagArgIntegrity = value
        return self

    def addPossibleErrorRef(self, value: Optional[RefType]) -> ClientServerOperation:
        """
        Possible errors that may by raised by the referring operation.
        A None value is a no-op and does not append to possibleErrorRefs.
        """
        if value is not None:
            self.possibleErrorRefs.append(value)
        return self

    def getPossibleErrorRefs(self) -> List[RefType]:
        """
        Possible errors that may by raised by the referring operation.
        """
        return self.possibleErrorRefs


class ClientServerInterface(PortInterface):
    """
    A client/server interface declares a number of operations that can be invoked on a server by a client.
    """

    # ClientServerInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.6, p.101 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createOperation        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOperations          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createApplicationError [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPossibleErrors      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # ClientServerOperation(s) of this ClientServerInterface.
        self.operations: List[ClientServerOperation] = []

        # Application errors that are defined as part of this interface.
        self.possibleErrors: List[ApplicationError] = []

    def createOperation(self, short_name: str) -> ClientServerOperation:
        """
        ClientServerOperation(s) of this ClientServerInterface.
        """
        if not self.IsReferrableElementExists(short_name, ClientServerOperation):
            operation = ClientServerOperation(self, short_name)
            self.addReferrableElement(operation)
            self.operations.append(operation)
        return cast(ClientServerOperation, self.getReferrableElement(short_name, ClientServerOperation))

    def getOperations(self) -> List[ClientServerOperation]:
        """
        ClientServerOperation(s) of this ClientServerInterface.
        """
        return self.operations

    def createApplicationError(self, short_name: str) -> ApplicationError:
        """
        Application errors that are defined as part of this interface.
        """
        if not self.IsReferrableElementExists(short_name, ApplicationError):
            error = ApplicationError(self, short_name)
            self.addReferrableElement(error)
            self.possibleErrors.append(error)
        return cast(ApplicationError, self.getReferrableElement(short_name, ApplicationError))

    def getPossibleErrors(self) -> List[ApplicationError]:
        """
        Application errors that are defined as part of this interface.
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
        if not self.IsReferrableElementExists(short_name, Trigger):
            trigger = Trigger(self, short_name)
            self.addReferrableElement(trigger)
            self.triggers.append(trigger)
        return cast(Trigger, self.getReferrableElement(short_name, Trigger))

    def getTriggers(self) -> List[Trigger]:
        """The Trigger of this trigger interface."""
        return self.triggers


class ModeSwitchInterface(PortInterface):
    """A mode switch interface declares a ModeDeclarationGroupPrototype to be sent and received."""

    # ModeSwitchInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.16, p.113 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createModeGroup  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeGroup     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The ModeDeclarationGroupPrototype of this mode interface.
        self.modeGroup: Optional[ModeDeclarationGroupPrototype] = None

    def createModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """The ModeDeclarationGroupPrototype of this mode interface."""
        if not self.IsReferrableElementExists(short_name, ModeDeclarationGroupPrototype):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addReferrableElement(prototype)
        mode_group = cast(ModeDeclarationGroupPrototype, self.getReferrableElement(short_name, ModeDeclarationGroupPrototype))
        self.modeGroup = mode_group
        return mode_group

    def getModeGroup(self) -> Optional[ModeDeclarationGroupPrototype]:
        """The ModeDeclarationGroupPrototype of this mode interface."""
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
    """
    This meta-class represents the ability to map ApplicationErrors onto each other.

    [constr_1238] Scope of mapped ApplicationErrors in the context of a ClientServerOperationMapping: All ApplicationErrors referenced by a ClientServerApplicationErrorMapping in the role firstApplicationError shall belong to exactly one ClientServerInterface. All ApplicationErrors referenced by a ClientServerApplicationErrorMapping in the role secondApplicationError shall belong to exactly one other ClientServerInterface. This rule shall be imposed at the time when the RTE is generated.
    """

    # ClientServerApplicationErrorMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.25, p.129
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstApplicationErrorRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstApplicationErrorRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondApplicationErrorRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondApplicationErrorRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the first ApplicationError in the context of the ClientServerApplicationErrorMapping.
        self.firstApplicationErrorRef: Optional[RefType] = None

        # This represents the second ApplicationError in the context of the ClientServerApplicationErrorMapping.
        self.secondApplicationErrorRef: Optional[RefType] = None

    def getFirstApplicationErrorRef(self) -> Optional[RefType]:
        """
        This represents the first ApplicationError in the context of the ClientServerApplicationErrorMapping.

        Returns:
            Optional[RefType]: The first application error reference
        """
        return self.firstApplicationErrorRef

    def setFirstApplicationErrorRef(self, value: Optional[RefType]) -> ClientServerApplicationErrorMapping:
        """
        This represents the first ApplicationError in the context of the ClientServerApplicationErrorMapping.
        A None value is a no-op and does not overwrite an existing firstApplicationErrorRef.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.firstApplicationErrorRef = value
        return self

    def getSecondApplicationErrorRef(self) -> Optional[RefType]:
        """
        This represents the second ApplicationError in the context of the ClientServerApplicationErrorMapping.

        Returns:
            Optional[RefType]: The second application error reference
        """
        return self.secondApplicationErrorRef

    def setSecondApplicationErrorRef(self, value: Optional[RefType]) -> ClientServerApplicationErrorMapping:
        """
        This represents the second ApplicationError in the context of the ClientServerApplicationErrorMapping.
        A None value is a no-op and does not overwrite an existing secondApplicationErrorRef.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.secondApplicationErrorRef = value
        return self


class SubElementRef(ARObject, ABC):
    """
    This meta-class provides the ability to reference elements of composite data type.
    """

    # SubElementRef method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.33, p.138 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is SubElementRef:
            raise TypeError("SubElementRef is an abstract class.")

        super().__init__()


class ApplicationCompositeDataTypeSubElementRef(SubElementRef):
    """
    This meta-class represents the specialization of SubElementMapping with respect to ApplicationCompositeDataTypes.
    """

    # ApplicationCompositeDataTypeSubElementRef method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.35, p.138 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationCompositeElementIRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationCompositeElementIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the referenced ApplicationCompositeDataPrototype. InstanceRef implemented by: ApplicationCompositeElementInPortInterfaceInstanceRef
        self.applicationCompositeElementIRef: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef] = None

    def getApplicationCompositeElementIRef(self) -> Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]:
        """
        This represents the referenced ApplicationCompositeDataPrototype. InstanceRef implemented by: ApplicationCompositeElementInPortInterfaceInstanceRef
        """
        return self.applicationCompositeElementIRef

    def setApplicationCompositeElementIRef(self, value: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]) -> ApplicationCompositeDataTypeSubElementRef:
        """
        This represents the referenced ApplicationCompositeDataPrototype. InstanceRef implemented by: ApplicationCompositeElementInPortInterfaceInstanceRef
        A None value is a no-op and does not overwrite an existing applicationCompositeElementIRef.
        """
        if value is not None:
            self.applicationCompositeElementIRef = value
        return self


class MappingDirectionEnum(AREnum):
    """
    Specifies the conversion direction for which the mapping is applicable.
    """

    # MappingDirectionEnum method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.37, p.146 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The TextTableMapping is applicable in both directions. Tags: atp.EnumerationLiteralIndex=0
    BIDIRECTIONAL = "bidirectional"

    # The TextTableMapping is applicable in the direction from firstDataPrototype / firstOperationArgument referring into the PortInterface of the PPortPrototype to secondDataPrototype / secondOperationArgument referring into the PortInterface of the RPortPrototype. Tags: atp.EnumerationLiteralIndex=1
    FIRST_TO_SECOND = "firstToSecond"

    # The TextTableMapping is applicable in the direction from secondDataPrototype / secondOperationArgument referring into the PortInterface of the PPortPrototype to firstDataPrototype / firstOperationArgument referring into the PortInterface of the RPortPrototype. Tags: atp.EnumerationLiteralIndex=2
    SECOND_TO_FIRST = "secondToFirst"

    def __init__(self):
        super().__init__((MappingDirectionEnum.BIDIRECTIONAL, MappingDirectionEnum.FIRST_TO_SECOND, MappingDirectionEnum.SECOND_TO_FIRST))


class TextTableValuePair(ARObject):
    """
    Defines a pair of text values which are translated into each other.
    """

    # TextTableValuePair method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.38, p.146 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstValue   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstValue   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondValue  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondValue  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Value of first DataPrototype provided similar to a numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula.
        self.firstValue: Optional[Numerical] = None

        # Value of second DataPrototype provided similar to a numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula.
        self.secondValue: Optional[Numerical] = None

    def getFirstValue(self) -> Optional[Numerical]:
        """
        Value of first DataPrototype provided similar to a numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula.
        """
        return self.firstValue

    def setFirstValue(self, value: Optional[Numerical]) -> TextTableValuePair:
        """
        Value of first DataPrototype provided similar to a numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula.
        A None value is a no-op and does not overwrite an existing firstValue.
        """
        if value is not None:
            self.firstValue = value
        return self

    def getSecondValue(self) -> Optional[Numerical]:
        """
        Value of second DataPrototype provided similar to a numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula.
        """
        return self.secondValue

    def setSecondValue(self, value: Optional[Numerical]) -> TextTableValuePair:
        """
        Value of second DataPrototype provided similar to a numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula.
        A None value is a no-op and does not overwrite an existing secondValue.
        """
        if value is not None:
            self.secondValue = value
        return self


class TextTableMapping(ARObject):
    """
    Defines the mapping of two DataPrototypes typed by AutosarDataTypes that refer to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE.
    """

    # TextTableMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.36, p.145 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBitfieldTextTableMaskFirst  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitfieldTextTableMaskFirst  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBitfieldTextTableMaskSecond [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitfieldTextTableMaskSecond [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIdenticalMapping            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIdenticalMapping            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappingDirection            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappingDirection            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addValuePair                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValuePairs                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the first element of the TextTableMapping.
        self.bitfieldTextTableMaskFirst: Optional[PositiveInteger] = None

        # This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the second element of the TextTableMapping.
        self.bitfieldTextTableMaskSecond: Optional[PositiveInteger] = None

        # If identicalMapping is set == true the values of the two referenced DataPrototypes do not need any conversion of the values.
        self.identicalMapping: Optional[Boolean] = None

        # Specifies the conversion direction for which the TextTableMapping is applicable.
        self.mappingDirection: Optional[MappingDirectionEnum] = None

        # Defines a pair of values which are translated into each other.
        self.valuePairs: List[TextTableValuePair] = []

    def getBitfieldTextTableMaskFirst(self) -> Optional[PositiveInteger]:
        """
        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the first element of the TextTableMapping.
        """
        return self.bitfieldTextTableMaskFirst

    def setBitfieldTextTableMaskFirst(self, value: Optional[PositiveInteger]) -> TextTableMapping:
        """
        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the first element of the TextTableMapping.
        A None value is a no-op and does not overwrite an existing bitfieldTextTableMaskFirst.
        """
        if value is not None:
            self.bitfieldTextTableMaskFirst = value
        return self

    def getBitfieldTextTableMaskSecond(self) -> Optional[PositiveInteger]:
        """
        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the second element of the TextTableMapping.
        """
        return self.bitfieldTextTableMaskSecond

    def setBitfieldTextTableMaskSecond(self, value: Optional[PositiveInteger]) -> TextTableMapping:
        """
        This attribute can be used to support the mapping of bit field to bit field, boolean values to bit fields, and vice versa. The attribute defines the bit mask for the second element of the TextTableMapping.
        A None value is a no-op and does not overwrite an existing bitfieldTextTableMaskSecond.
        """
        if value is not None:
            self.bitfieldTextTableMaskSecond = value
        return self

    def getIdenticalMapping(self) -> Optional[Boolean]:
        """
        If identicalMapping is set == true the values of the two referenced DataPrototypes do not need any conversion of the values.
        """
        return self.identicalMapping

    def setIdenticalMapping(self, value: Optional[Boolean]) -> TextTableMapping:
        """
        If identicalMapping is set == true the values of the two referenced DataPrototypes do not need any conversion of the values.
        A None value is a no-op and does not overwrite an existing identicalMapping.
        """
        if value is not None:
            self.identicalMapping = value
        return self

    def getMappingDirection(self) -> Optional[MappingDirectionEnum]:
        """
        Specifies the conversion direction for which the TextTableMapping is applicable.
        """
        return self.mappingDirection

    def setMappingDirection(self, value: Optional[MappingDirectionEnum]) -> TextTableMapping:
        """
        Specifies the conversion direction for which the TextTableMapping is applicable.
        A None value is a no-op and does not overwrite an existing mappingDirection.
        """
        if value is not None:
            self.mappingDirection = value
        return self

    def addValuePair(self, value: Optional[TextTableValuePair]) -> TextTableMapping:
        """
        Defines a pair of values which are translated into each other.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.valuePairs.append(value)
        return self

    def getValuePairs(self) -> List[TextTableValuePair]:
        """
        Defines a pair of values which are translated into each other.
        """
        return self.valuePairs


class SubElementMapping(ARObject):
    """
    This meta-class allows for the definition of mappings of elements of a composite data type.
    """

    # SubElementMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.32, p.137 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (textTableMapping multiplicity 0..2 per Table 4.32 — modeled as a list; bound documented here)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstElement      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstElement      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondElement     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondElement     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addTextTableMapping  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTextTableMappings [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the first element referenced in the scope of the mapping.
        self.firstElement: Optional[SubElementRef] = None

        # This represents the second element referenced in the scope of the mapping.
        self.secondElement: Optional[SubElementRef] = None

        # This allows for the text-table translation of individual elements of a composite data type.
        self.textTableMappings: List[TextTableMapping] = []

    def getFirstElement(self) -> Optional[SubElementRef]:
        """
        This represents the first element referenced in the scope of the mapping.
        """
        return self.firstElement

    def setFirstElement(self, value: Optional[SubElementRef]) -> SubElementMapping:
        """
        This represents the first element referenced in the scope of the mapping.
        A None value is a no-op and does not overwrite an existing firstElement.
        """
        if value is not None:
            self.firstElement = value
        return self

    def getSecondElement(self) -> Optional[SubElementRef]:
        """
        This represents the second element referenced in the scope of the mapping.
        """
        return self.secondElement

    def setSecondElement(self, value: Optional[SubElementRef]) -> SubElementMapping:
        """
        This represents the second element referenced in the scope of the mapping.
        A None value is a no-op and does not overwrite an existing secondElement.
        """
        if value is not None:
            self.secondElement = value
        return self

    def addTextTableMapping(self, value: Optional[TextTableMapping]) -> SubElementMapping:
        """
        This allows for the text-table translation of individual elements of a composite data type.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.textTableMappings.append(value)
        return self

    def getTextTableMappings(self) -> List[TextTableMapping]:
        """
        This allows for the text-table translation of individual elements of a composite data type.
        """
        return self.textTableMappings


class DataPrototypeMapping(ARObject):
    """
    Defines the mapping of two particular VariableDataPrototypes, ParameterDataPrototypes or ArgumentDataPrototypes with non-equal shortNames, non-equal structure (specific condition is described by [constr_1187]), and/or non-equal semantic (resolution or range) in context of two different SenderReceiverInterface, NvDataInterface or ParameterInterface or Operations. If the semantic is unequal, the following rules apply: The textTableMapping is only applicable if the referred DataPrototypes are typed by AutosarDataType referring to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE. In the case that the DataPrototypes are typed by AutosarDataType either referring to CompuMethods of category LINEAR, IDENTICAL or referring to no CompuMethod (which is similar as IDENTICAL) the linear conversion factor is calculated out of the factorSiToUnit and offsetSiToUnit attributes of the referred Units and the CompuRationalCoeffs of a compuInternalToPhys of the referred CompuMethods.
    """

    # DataPrototypeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.22, p.125 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstDataPrototypeRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstDataPrototypeRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirstToSecondDataTransformationRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstToSecondDataTransformationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondDataPrototypeRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondDataPrototypeRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondToFirstDataTransformationRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondToFirstDataTransformationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSubElementMapping                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubElementMappings                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTextTableMapping                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTextTableMappings                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # First to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        self.firstDataPrototypeRef: Optional[RefType] = None

        # This reference defines the need to execute the DataTransformation <Mip>_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.firstDataPrototype to the DataPrototypeMapping.secondDataPrototype. This reference also specifies the reverse DataTransformation <Mip>_Inv_<transformerId> functions of the transformation chain (i.e. from the DataPrototypeMapping.secondDataPrototype to the DataPrototypeMapping.firstDataPrototype) if the referenced DataTransformation is symmetric, i.e. attribute DataTransformation.dataTransformationKind is set to symmetric.
        self.firstToSecondDataTransformationRef: Optional[RefType] = None

        # Second to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        self.secondDataPrototypeRef: Optional[RefType] = None

        # This defines the need to execute the reverse DataTransformation <Mip>_Inv_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.secondDataPrototype to the DataPrototypeMapping.firstDataPrototype.
        self.secondToFirstDataTransformationRef: Optional[RefType] = None

        # This represents the owned SubelementMapping.
        self.subElementMappings: List[SubElementMapping] = []

        # Applied TextTableMapping(s)
        self.textTableMappings: List[TextTableMapping] = []

    def getFirstDataPrototypeRef(self) -> Optional[RefType]:
        """
        First to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        """
        return self.firstDataPrototypeRef

    def setFirstDataPrototypeRef(self, value: Optional[RefType]) -> DataPrototypeMapping:
        """
        First to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        A None value is a no-op and does not overwrite an existing firstDataPrototypeRef.
        """
        if value is not None:
            self.firstDataPrototypeRef = value
        return self

    def getFirstToSecondDataTransformationRef(self) -> Optional[RefType]:
        """
        This reference defines the need to execute the DataTransformation <Mip>_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.firstDataPrototype to the DataPrototypeMapping.secondDataPrototype. This reference also specifies the reverse DataTransformation <Mip>_Inv_<transformerId> functions of the transformation chain (i.e. from the DataPrototypeMapping.secondDataPrototype to the DataPrototypeMapping.firstDataPrototype) if the referenced DataTransformation is symmetric, i.e. attribute DataTransformation.dataTransformationKind is set to symmetric.
        """
        return self.firstToSecondDataTransformationRef

    def setFirstToSecondDataTransformationRef(self, value: Optional[RefType]) -> DataPrototypeMapping:
        """
        This reference defines the need to execute the DataTransformation <Mip>_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.firstDataPrototype to the DataPrototypeMapping.secondDataPrototype. This reference also specifies the reverse DataTransformation <Mip>_Inv_<transformerId> functions of the transformation chain (i.e. from the DataPrototypeMapping.secondDataPrototype to the DataPrototypeMapping.firstDataPrototype) if the referenced DataTransformation is symmetric, i.e. attribute DataTransformation.dataTransformationKind is set to symmetric.
        A None value is a no-op and does not overwrite an existing firstToSecondDataTransformationRef.
        """
        if value is not None:
            self.firstToSecondDataTransformationRef = value
        return self

    def getSecondDataPrototypeRef(self) -> Optional[RefType]:
        """
        Second to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        """
        return self.secondDataPrototypeRef

    def setSecondDataPrototypeRef(self, value: Optional[RefType]) -> DataPrototypeMapping:
        """
        Second to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation.
        A None value is a no-op and does not overwrite an existing secondDataPrototypeRef.
        """
        if value is not None:
            self.secondDataPrototypeRef = value
        return self

    def getSecondToFirstDataTransformationRef(self) -> Optional[RefType]:
        """
        This defines the need to execute the reverse DataTransformation <Mip>_Inv_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.secondDataPrototype to the DataPrototypeMapping.firstDataPrototype.
        """
        return self.secondToFirstDataTransformationRef

    def setSecondToFirstDataTransformationRef(self, value: Optional[RefType]) -> DataPrototypeMapping:
        """
        This defines the need to execute the reverse DataTransformation <Mip>_Inv_<transformerId> functions of the transformation chain when communicating from the DataPrototypeMapping.secondDataPrototype to the DataPrototypeMapping.firstDataPrototype.
        A None value is a no-op and does not overwrite an existing secondToFirstDataTransformationRef.
        """
        if value is not None:
            self.secondToFirstDataTransformationRef = value
        return self

    def addSubElementMapping(self, value: Optional[SubElementMapping]) -> DataPrototypeMapping:
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

    def addTextTableMapping(self, value: Optional[TextTableMapping]) -> DataPrototypeMapping:
        """
        Applied TextTableMapping(s)
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.textTableMappings.append(value)
        return self

    def getTextTableMappings(self) -> List[TextTableMapping]:
        """
        Applied TextTableMapping(s)
        """
        return self.textTableMappings


class ClientServerOperationMapping(ARObject):
    """
    Defines the mapping of two particular ClientServerOperations in context of two different ClientServerInterfaces.

    [constr_1237] Scope of mapped ClientServerOperations in the context of a ClientServerOperationMapping: All ClientServerOperations referenced by a ClientServerOperationMapping in the role firstOperation shall belong to exactly one ClientServerInterface. All ClientServerOperations referenced by a ClientServerOperationMapping in the role secondOperation shall belong to exactly one other ClientServerInterface. This rule shall be imposed at the time when the RTE is generated.

    [constr_1240] Consistency of ArgumentDataPrototypes within the context of a ClientServerOperationMapping: Unless a ClientServerOperationMapping.firstToSecondDataTransformation exists, for each argument owned by a ClientServerOperationMapping.firstOperation and a ClientServerOperationMapping.secondOperation, a reference in the role ClientServerOperationMapping.argumentMapping.firstDataPrototype or ClientServerOperationMapping.argumentMapping.secondDataPrototype shall exist at the time when the RTE is generated, originated by one of the ClientServerOperationMapping.argumentMappings owned by the mentioned ClientServerOperationMapping.

    [constr_1268] ArgumentDataPrototype.direction shall be preserved in a ClientServerOperationMapping: Within the context of a ClientServerOperationMapping, the value of the argument ArgumentDataPrototype.direction of two mapped ArgumentDataPrototype shall be identical at the time when the RTE is generated.

    [constr_1269] Number of arguments shall be preserved in a ClientServerOperationMapping: Within the context of a ClientServerOperationMapping, the number of arguments of firstOperation and secondOperation shall be identical at the time when the RTE is generated.

    [constr_1270] ArgumentDataPrototype shall be mapped only once in a ClientServerOperationMapping: Within the context of a ClientServerOperationMapping, each argument shall only be referenced once in the role firstDataPrototype or secondDataPrototype at the time when the RTE is generated.

    [constr_1875] Existence of reference ClientServerOperationMapping.firstOperation: For each ClientServerOperationMapping, the reference in the role firstOperation shall exist at the time when the RTE is generated.

    [constr_1876] Existence of reference ClientServerOperationMapping.secondOperation: For each ClientServerOperationMapping, the reference in the role secondOperation shall exist at the time when the RTE is generated.
    """

    # ClientServerOperationMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.24, p.129
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addArgumentMapping                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArgumentMappings                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getFirstOperationRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstOperationRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirstToSecondDataTransformationRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstToSecondDataTransformationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondOperationRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondOperationRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Defines the mapping of two particular ArgumentDataPrototypes with unequal names or unequal semantic (resolution or range) in context of Operations.
        self.argumentMappings: List[DataPrototypeMapping] = []

        # First to-be-mapped ClientServerOperation of a ClientServerInterface.
        self.firstOperationRef: Optional[RefType] = None

        # This reference indicates that a DataTransformation is intended in the context of the ClientServerOperationMapping.
        self.firstToSecondDataTransformationRef: Optional[RefType] = None

        # Second to-be-mapped ClientServerOperation of a ClientServerInterface.
        self.secondOperationRef: Optional[RefType] = None

    def addArgumentMapping(self, value: Optional[DataPrototypeMapping]) -> ClientServerOperationMapping:
        """
        Defines the mapping of two particular ArgumentDataPrototypes with unequal names or unequal semantic (resolution or range) in context of Operations.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.argumentMappings.append(value)
        return self

    def getArgumentMappings(self) -> List[DataPrototypeMapping]:
        """
        Defines the mapping of two particular ArgumentDataPrototypes with unequal names or unequal semantic (resolution or range) in context of Operations.
        """
        return self.argumentMappings

    def getFirstOperationRef(self) -> Optional[RefType]:
        """
        First to-be-mapped ClientServerOperation of a ClientServerInterface.
        """
        return self.firstOperationRef

    def setFirstOperationRef(self, value: Optional[RefType]) -> ClientServerOperationMapping:
        """
        First to-be-mapped ClientServerOperation of a ClientServerInterface.
        A None value is a no-op and does not overwrite an existing firstOperationRef.
        """
        if value is not None:
            self.firstOperationRef = value
        return self

    def getFirstToSecondDataTransformationRef(self) -> Optional[RefType]:
        """
        This reference indicates that a DataTransformation is intended in the context of the ClientServerOperationMapping.
        """
        return self.firstToSecondDataTransformationRef

    def setFirstToSecondDataTransformationRef(self, value: Optional[RefType]) -> ClientServerOperationMapping:
        """
        This reference indicates that a DataTransformation is intended in the context of the ClientServerOperationMapping.
        A None value is a no-op and does not overwrite an existing firstToSecondDataTransformationRef.
        """
        if value is not None:
            self.firstToSecondDataTransformationRef = value
        return self

    def getSecondOperationRef(self) -> Optional[RefType]:
        """
        Second to-be-mapped ClientServerOperation of a ClientServerInterface.
        """
        return self.secondOperationRef

    def setSecondOperationRef(self, value: Optional[RefType]) -> ClientServerOperationMapping:
        """
        Second to-be-mapped ClientServerOperation of a ClientServerInterface.
        A None value is a no-op and does not overwrite an existing secondOperationRef.
        """
        if value is not None:
            self.secondOperationRef = value
        return self


class ClientServerInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of ClientServerOperations in context of two different ClientServerInterfaces.
    """

    # ClientServerInterfaceMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.23, p.128 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getErrorMappings       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addErrorMapping        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOperationMappings   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addOperationMapping    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Map two different ApplicationErrors defined in the context of two different ClientServerInterfaces.
        self.errorMappings: List[ClientServerApplicationErrorMapping] = []

        # Mapping of two ClientServerOperations in two different ClientServerInterfaces Stereotypes: atpSplitable Tags: atp.Splitkey=operationMapping
        self.operationMappings: List[ClientServerOperationMapping] = []

    def getErrorMappings(self) -> List[ClientServerApplicationErrorMapping]:
        """
        Map two different ApplicationErrors defined in the context of two different ClientServerInterfaces.
        """
        return self.errorMappings

    def addErrorMapping(self, value: Optional[ClientServerApplicationErrorMapping]) -> ClientServerInterfaceMapping:
        """
        Map two different ApplicationErrors defined in the context of two different ClientServerInterfaces. A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.errorMappings.append(value)
        return self

    def getOperationMappings(self) -> List[ClientServerOperationMapping]:
        """
        Mapping of two ClientServerOperations in two different ClientServerInterfaces Stereotypes: atpSplitable Tags: atp.Splitkey=operationMapping
        """
        return self.operationMappings

    def addOperationMapping(self, value: Optional[ClientServerOperationMapping]) -> ClientServerInterfaceMapping:
        """
        Mapping of two ClientServerOperations in two different ClientServerInterfaces Stereotypes: atpSplitable Tags: atp.Splitkey=operationMapping. A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.operationMappings.append(value)
        return self


class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of VariableDataPrototypes or ParameterDataPrototypes in context of two different SenderReceiverInterfaces, NvDataInterfaces or ParameterInterfaces.
    """

    # VariableAndParameterInterfaceMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.21, p.125 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataMappings    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDataMapping     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the mapping of two particular VariableDataPrototypes or ParameterDataPrototypes with unequal names and/or unequal semantic (resolution or range) in context of two different SenderReceiverInterfaces, NvDataInterfaces or ParameterInterfaces Stereotypes: atpSplitable Tags: atp.Splitkey=dataMapping
        self.dataMappings: List[DataPrototypeMapping] = []

    def getDataMappings(self) -> List[DataPrototypeMapping]:
        """
        Defines the mapping of two particular VariableDataPrototypes or ParameterDataPrototypes with unequal names and/or unequal semantic (resolution or range) in context of two different SenderReceiverInterfaces, NvDataInterfaces or ParameterInterfaces Stereotypes: atpSplitable Tags: atp.Splitkey=dataMapping
        """
        return self.dataMappings

    def addDataMapping(self, value: Optional[DataPrototypeMapping]) -> VariableAndParameterInterfaceMapping:
        """
        Defines the mapping of two particular VariableDataPrototypes or ParameterDataPrototypes with unequal names and/or unequal semantic (resolution or range) in context of two different SenderReceiverInterfaces, NvDataInterfaces or ParameterInterfaces Stereotypes: atpSplitable Tags: atp.Splitkey=dataMapping. A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.dataMappings.append(value)
        return self


class ModeInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of ModeDeclarationGroupPrototypes in context of two different ModeInterfaces.
    """

    # ModeInterfaceMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.26, p.130 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getModeMapping  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModeMapping  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Mapping of two ModeDeclarationGroupPrototypes in two different ModeInterfaces
        self.modeMapping: Optional[ModeDeclarationGroupPrototypeMapping] = None

    def getModeMapping(self) -> Optional[ModeDeclarationGroupPrototypeMapping]:
        """
        Mapping of two ModeDeclarationGroupPrototypes in two different ModeInterfaces
        """
        return self.modeMapping

    def setModeMapping(self, value: Optional[ModeDeclarationGroupPrototypeMapping]) -> ModeInterfaceMapping:
        """
        Mapping of two ModeDeclarationGroupPrototypes in two different ModeInterfaces. A None value is a no-op and does not overwrite an existing modeMapping.
        """
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

    def addTriggerMapping(self, value: Optional[TriggerMapping]) -> TriggerInterfaceMapping:
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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.29, p.132 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstModeRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addFirstModeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondModeRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondModeRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the first ModeDeclaration of the ModeDeclarationMapping. This reference has the multiplicity 1 .. * to support use cases where e.g. one mode of the mode user is mapped to several modes of the mode manager.
        self.firstModeRefs: List[RefType] = []

        # This represents the second ModeDeclaration of the ModeDeclarationMapping.
        self.secondModeRef: Optional[RefType] = None

    def getFirstModeRefs(self) -> List[RefType]:
        """
        This represents the first ModeDeclaration of the ModeDeclarationMapping. This reference has the multiplicity 1 .. * to support use cases where e.g. one mode of the mode user is mapped to several modes of the mode manager.
        """
        return self.firstModeRefs

    def addFirstModeRef(self, value: Optional[RefType]) -> ModeDeclarationMapping:
        """
        This represents the first ModeDeclaration of the ModeDeclarationMapping. This reference has the multiplicity 1 .. * to support use cases where e.g. one mode of the mode user is mapped to several modes of the mode manager.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.firstModeRefs.append(value)
        return self

    def getSecondModeRef(self) -> Optional[RefType]:
        """
        This represents the second ModeDeclaration of the ModeDeclarationMapping.
        """
        return self.secondModeRef

    def setSecondModeRef(self, value: Optional[RefType]) -> ModeDeclarationMapping:
        """
        This represents the second ModeDeclaration of the ModeDeclarationMapping.
        A None value is a no-op and does not overwrite an existing secondModeRef.
        """
        if value is not None:
            self.secondModeRef = value
        return self


class ModeDeclarationMappingSet(AtpType):
    """
    This meta-class implements a container for ModeDeclarationGroupMappings
    """

    # ModeDeclarationMappingSet method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.28, p.132 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getModeDeclarationMappings   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createModeDeclarationMapping [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # reader/writer: dedicated helpers readModeDeclarationMappingSet/writeModeDeclarationMappingSet
    # (readARElement/writeARElement; element <MODE-DECLARATION-MAPPING-SET> of type
    # MODE-DECLARATION-MAPPING-SET, XSD AUTOSAR_00052.xsd l.82399, own group l.82378)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the collection of ModeDeclaration Mappings owned by the enclosing ModeDeclaration MappingSet.
        self.modeDeclarationMappings: List[ModeDeclarationMapping] = []

    def getModeDeclarationMappings(self) -> List[ModeDeclarationMapping]:
        """
        This represents the collection of ModeDeclaration Mappings owned by the enclosing ModeDeclaration MappingSet.
        """
        return self.modeDeclarationMappings

    def createModeDeclarationMapping(self, short_name: str) -> ModeDeclarationMapping:
        """
        This represents the collection of ModeDeclaration Mappings owned by the enclosing ModeDeclaration MappingSet.

        A duplicate short name with the same type returns the existing ModeDeclarationMapping.
        """
        if not self.IsReferrableElementExists(short_name, ModeDeclarationMapping):
            mapping = ModeDeclarationMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.modeDeclarationMappings.append(mapping)
        return cast(ModeDeclarationMapping, self.getReferrableElement(short_name, ModeDeclarationMapping))


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
        if not self.IsReferrableElementExists(short_name, VariableAndParameterInterfaceMapping):
            mapping = VariableAndParameterInterfaceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return cast(VariableAndParameterInterfaceMapping, self.getReferrableElement(short_name, VariableAndParameterInterfaceMapping))

    def createClientServerInterfaceMapping(self, short_name: str) -> ClientServerInterfaceMapping:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        if not self.IsReferrableElementExists(short_name, ClientServerInterfaceMapping):
            mapping = ClientServerInterfaceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return cast(ClientServerInterfaceMapping, self.getReferrableElement(short_name, ClientServerInterfaceMapping))

    def createModeInterfaceMapping(self, short_name: str) -> ModeInterfaceMapping:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        if not self.IsReferrableElementExists(short_name, ModeInterfaceMapping):
            mapping = ModeInterfaceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return cast(ModeInterfaceMapping, self.getReferrableElement(short_name, ModeInterfaceMapping))

    def createTriggerInterfaceMapping(self, short_name: str) -> TriggerInterfaceMapping:
        """
        Specifies one PortInterfaceMapping to support the connection of Ports typed by two different PortInterfaces with PortInterface elements having unequal names and/or unequal semantic (resolution or range).
        """
        if not self.IsReferrableElementExists(short_name, TriggerInterfaceMapping):
            mapping = TriggerInterfaceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.portInterfaceMappings.append(mapping)
        return cast(TriggerInterfaceMapping, self.getReferrableElement(short_name, TriggerInterfaceMapping))


from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ArVariableInImplementationDataInstanceRef  # noqa: E402


class ImplementationDataTypeSubElementRef(SubElementRef):
    """This meta-class represents the specialization of SubElementMapping with respect to ImplementationDataTypes."""

    # ImplementationDataTypeSubElementRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.34, p.138 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getImplementationDataTypeElement            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImplementationDataTypeElement            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParameterImplementationDataTypeElement   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParameterImplementationDataTypeElement   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the referenced implementationDataTypeElement.
        self.implementationDataTypeElement: Optional[ArVariableInImplementationDataInstanceRef] = None

        # This represents the referenced ImplementationDataTypeElement.
        self.parameterImplementationDataTypeElement: Optional[ArParameterInImplementationDataInstanceRef] = None

    def getImplementationDataTypeElement(self) -> Optional[ArVariableInImplementationDataInstanceRef]:
        """This represents the referenced implementationDataTypeElement."""
        return self.implementationDataTypeElement

    def setImplementationDataTypeElement(self, value: Optional[ArVariableInImplementationDataInstanceRef]) -> ImplementationDataTypeSubElementRef:
        """
        This represents the referenced implementationDataTypeElement.
        A None value is a no-op and does not overwrite an existing implementationDataTypeElement.
        """
        if value is not None:
            self.implementationDataTypeElement = value
        return self

    def getParameterImplementationDataTypeElement(self) -> Optional[ArParameterInImplementationDataInstanceRef]:
        """This represents the referenced ImplementationDataTypeElement."""
        return self.parameterImplementationDataTypeElement

    def setParameterImplementationDataTypeElement(self, value: Optional[ArParameterInImplementationDataInstanceRef]) -> ImplementationDataTypeSubElementRef:
        """
        This represents the referenced ImplementationDataTypeElement.
        A None value is a no-op and does not overwrite an existing parameterImplementationDataTypeElement.
        """
        if value is not None:
            self.parameterImplementationDataTypeElement = value
        return self
