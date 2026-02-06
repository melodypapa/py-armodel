"""
SWComponentTemplate module for AUTOSAR software component templates.
"""

"""V2 module."""
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    DataLimitKindEnum,
    FilterDebouncingEnum,
    ProcessingKindEnum,
    PulseTestEnum,
    SignalFanEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    CompositeNetworkRepresentation,
    HandleInvalidEnum,
    HandleOutOfRangeEnum,
    HandleOutOfRangeStatusEnum,
    HandleTimeoutEnum,
    ModeSwitchedAckRequest,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    NvProvideComSpec,
    NvRequireComSpec,
    ParameterProvideComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    ReceiverComSpec,
    RPortComSpec,
    SenderComSpec,
    ServerComSpec,
    TransformationComSpecProps,
    TransmissionAcknowledgementRequest,
    TransmissionModeDefinitionEnum,
    UserDefinedTransformationComSpecProps,
)

# Components wildcard import removed to avoid circular import with InternalBehavior
# Import specific classes that don't cause circular imports
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PPortPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    CompositionSwComponentType,
    DelegationSwConnector,
    PassThroughSwConnector,
    SwComponentPrototype,
    SwConnector,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype import (
    ApplicationArrayDataType,
    ApplicationArrayElement,
    ApplicationCompositeDataType,
    ApplicationCompositeElementDataPrototype,
    ApplicationDataType,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    ApplicationRecordElement,
    AutosarDataPrototype,
    AutosarDataType,
    DataPrototype,
    DataTypeMap,
    DataTypeMappingSet,
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndDescription,
    EndToEndProtection,
    EndToEndProtectionISignalIPdu,
    EndToEndProtectionSet,
    EndToEndProtectionVariablePrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ApplicationError,
    ArgumentDataPrototype,
    ClientServerApplicationErrorMapping,
    ClientServerInterface,
    ClientServerInterfaceMapping,
    ClientServerOperation,
    ClientServerOperationMapping,
    DataInterface,
    DataPrototypeMapping,
    InvalidationPolicy,
    MetaDataItem,
    MetaDataItemSet,
    ModeDeclarationMapping,
    ModeDeclarationMappingSet,
    ModeInterfaceMapping,
    ModeSwitchInterface,
    NvDataInterface,
    ParameterInterface,
    PortInterface,
    PortInterfaceMapping,
    PortInterfaceMappingSet,
    SenderReceiverInterface,
    TextTableMapping,
    TriggerInterface,
    TriggerInterfaceMapping,
    VariableAndParameterInterfaceMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    ExternalTriggeringPointIdent,
    IdentCaption,
    ModeAccessPointIdent,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import (
    SwComponentDocumentation,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import (
    SwcImplementation,
)

# SwcInternalBehavior import removed to avoid circular import with InternalBehavior
# from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
    SwComponentType,
)

__all__ = [
    # ApplicationAttributes
    "DataLimitKindEnum",
    "FilterDebouncingEnum",
    "ProcessingKindEnum",
    "PulseTestEnum",
    "SignalFanEnum",
    # Datatype
    "ApplicationArrayDataType",
    "ApplicationArrayElement",
    "ApplicationCompositeDataType",
    "ApplicationCompositeElementDataPrototype",
    "ApplicationDataType",
    "ApplicationPrimitiveDataType",
    "ApplicationRecordDataType",
    "ApplicationRecordElement",
    "AutosarDataPrototype",
    "AutosarDataType",
    "DataPrototype",
    "DataTypeMap",
    "DataTypeMappingSet",
    "ParameterDataPrototype",
    "VariableDataPrototype",
    # Communication
    "ClientComSpec",
    "CompositeNetworkRepresentation",
    "HandleInvalidEnum",
    "HandleOutOfRangeEnum",
    "HandleOutOfRangeStatusEnum",
    "HandleTimeoutEnum",
    "ModeSwitchedAckRequest",
    "ModeSwitchReceiverComSpec",
    "ModeSwitchSenderComSpec",
    "NonqueuedReceiverComSpec",
    "NonqueuedSenderComSpec",
    "NvProvideComSpec",
    "NvRequireComSpec",
    "ParameterProvideComSpec",
    "ParameterRequireComSpec",
    "PPortComSpec",
    "QueuedReceiverComSpec",
    "QueuedSenderComSpec",
    "ReceiverComSpec",
    "RPortComSpec",
    "SenderComSpec",
    "ServerComSpec",
    "TransformationComSpecProps",
    "TransmissionAcknowledgementRequest",
    "TransmissionModeDefinitionEnum",
    "UserDefinedTransformationComSpecProps",
    # Components
    "PPortPrototype",
    # Composition
    "AssemblySwConnector",
    "CompositionSwComponentType",
    "DelegationSwConnector",
    "PassThroughSwConnector",
    "SwComponentPrototype",
    "SwConnector",
    # EndToEndProtection
    "EndToEndDescription",
    "EndToEndProtection",
    "EndToEndProtectionISignalIPdu",
    "EndToEndProtectionSet",
    "EndToEndProtectionVariablePrototype",
    # PortInterface
    "ApplicationError",
    "ArgumentDataPrototype",
    "ClientServerApplicationErrorMapping",
    "ClientServerInterface",
    "ClientServerInterfaceMapping",
    "ClientServerOperation",
    "ClientServerOperationMapping",
    "DataInterface",
    "DataPrototypeMapping",
    "InvalidationPolicy",
    "MetaDataItem",
    "MetaDataItemSet",
    "ModeDeclarationMapping",
    "ModeDeclarationMappingSet",
    "ModeInterfaceMapping",
    "ModeSwitchInterface",
    "NvDataInterface",
    "ParameterInterface",
    "PortInterface",
    "PortInterfaceMapping",
    "PortInterfaceMappingSet",
    "SenderReceiverInterface",
    "TextTableMapping",
    "TriggerInterface",
    "TriggerInterfaceMapping",
    "VariableAndParameterInterfaceMapping",
    # RPTScenario
    "ExternalTriggeringPointIdent",
    "IdentCaption",
    "ModeAccessPointIdent",
    # SoftwareComponentDocumentation
    "SwComponentDocumentation",
    # SwcImplementation
    "SwcImplementation",
    # SwComponentType
    "SwComponentType",
]
