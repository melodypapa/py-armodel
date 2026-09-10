"""
This module contains classes for representing AUTOSAR port API options
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, RefType, TRefType
from typing import List, Optional


class DataTransformationErrorHandlingEnum(AREnum):
    """
    This enumeration defines different ways how a RunnableEntity shall handle transformer errors.
    """

    # DataTransformationErrorHandlingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.43, p.590 (R23-11)
    # Spec verified: R23-11
    # (no methods) — enum value form serialized on PortAPIOption.errorHandling
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # A runnable does not handle transformer errors. Tags: atp.EnumerationLiteralIndex=0
    NO_TRANSFORMER_ERROR_HANDLING = "noTransformerErrorHandling"

    # The runnable implements the handling of transformer errors. Tags: atp.EnumerationLiteralIndex=1
    TRANSFORMER_ERROR_HANDLING = "transformerErrorHandling"

    def __init__(self):
        super().__init__(
            [
                DataTransformationErrorHandlingEnum.NO_TRANSFORMER_ERROR_HANDLING,
                DataTransformationErrorHandlingEnum.TRANSFORMER_ERROR_HANDLING,
            ]
        )


class DataTransformationStatusForwardingEnum(AREnum):
    """
    This enumeration defines different ways how a RunnableEntity shall be able to forward status code into the transformer chain.
    """

    # DataTransformationStatusForwardingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.44, p.591 (R23-11)
    # Spec verified: R23-11
    # (no methods) — enum value form serialized on PortAPIOption.transformerStatusForwarding
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The RunnableEntity is not able to forward a transformer status code. Tags: atp.EnumerationLiteralIndex=0
    NO_TRANSFORMER_STATUS_FORWARDING = "noTransformerStatusForwarding"

    # The RunnableEntity is able to forward a transformer status code. Tags: atp.EnumerationLiteralIndex=1
    TRANSFORMER_STATUS_FORWARDING = "transformerStatusForwarding"

    def __init__(self):
        super().__init__(
            [
                DataTransformationStatusForwardingEnum.NO_TRANSFORMER_STATUS_FORWARDING,
                DataTransformationStatusForwardingEnum.TRANSFORMER_STATUS_FORWARDING,
            ]
        )


class SupportBufferLockingEnum(AREnum):
    """
    This enumeration represents the ability to define the buffer locking behavior.
    """

    # SupportBufferLockingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.48, p.595 (R23-11)
    # Spec verified: R23-11
    # (no methods) — enum value form serialized on CommunicationBufferLocking.supportBufferLocking
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Buffer locking is not supported. Tags: atp.EnumerationLiteralIndex=0
    DOES_NOT_SUPPORT_BUFFER_LOCKING = "doesNotSupportBufferLocking"

    # Buffer locking is supported. Tags: atp.EnumerationLiteralIndex=1
    SUPPORTS_BUFFER_LOCKING = "supportsBufferLocking"

    def __init__(self):
        super().__init__(
            [
                SupportBufferLockingEnum.DOES_NOT_SUPPORT_BUFFER_LOCKING,
                SupportBufferLockingEnum.SUPPORTS_BUFFER_LOCKING,
            ]
        )


class SwcSupportedFeature(ARObject):
    """
    This meta-class represents a abstract base class for features that can be supported by a RunnableEntity.
    """

    # SwcSupportedFeature method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.46, p.594 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is SwcSupportedFeature:
            raise TypeError("SwcSupportedFeature is an abstract class.")
        super().__init__()


class CommunicationBufferLocking(SwcSupportedFeature):
    """
    The aggregation of this meta-class specifies that a RunnableEntity supports locked communication buffers supplied by the RTE. It is able to cope with the error RTE_E_COM_BUSY.
    """

    # CommunicationBufferLocking method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.47, p.595 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSupportBufferLocking    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportBufferLocking    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute is used to indicate the intended buffer locking behavior.
        self.supportBufferLocking: Optional[SupportBufferLockingEnum] = None

    def getSupportBufferLocking(self) -> Optional[SupportBufferLockingEnum]:
        """
        This attribute is used to indicate the intended buffer locking behavior.
        """
        return self.supportBufferLocking

    def setSupportBufferLocking(self, value: Optional[SupportBufferLockingEnum]) -> "CommunicationBufferLocking":
        """
        This attribute is used to indicate the intended buffer locking behavior.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.supportBufferLocking = value
        return self


class PortDefinedArgumentValue(ARObject):
    """
    A PortDefinedArgumentValue is passed to a RunnableEntity dealing with the ClientServerOperations provided by a given PortPrototype. Note that this is restricted to PPortPrototypes of a ClientServer Interface.
    """

    # PortDefinedArgumentValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.45, p.593 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getValue          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValueTypeTRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValueTypeTRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies the actual value.
        self.value: Optional[ValueSpecification] = None

        # The implementation type of this argument value. It should not be composite type or a pointer. Stereotypes: isOfType
        self.valueTypeTRef: Optional[TRefType] = None

    def getValue(self) -> Optional[ValueSpecification]:
        """
        Specifies the actual value.
        """
        return self.value

    def setValue(self, value: Optional[ValueSpecification]) -> "PortDefinedArgumentValue":
        """
        Specifies the actual value.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self

    def getValueTypeTRef(self) -> Optional[TRefType]:
        """
        The implementation type of this argument value. It should not be composite type or a pointer. Stereotypes: isOfType
        """
        return self.valueTypeTRef

    def setValueTypeTRef(self, value: Optional[TRefType]) -> "PortDefinedArgumentValue":
        """
        The implementation type of this argument value. It should not be composite type or a pointer. Stereotypes: isOfType
        A None value is a no-op and does not overwrite an existing value type reference.
        """
        if value is not None:
            self.valueTypeTRef = value
        return self


class PortAPIOption(ARObject, VariationPointCapable):
    """
    Options how to generate the signatures of calls for an AtomicSwComponentType in order to communicate over a PortPrototype (for calls into a RunnableEntity as well as for calls from a Runnable Entity to the PortPrototype).
    """

    # PortAPIOption method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.42, p.590 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEnableTakeAddress            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEnableTakeAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getErrorHandling                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setErrorHandling                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIndirectAPI                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIndirectAPI                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortArgValues                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPortArgValue                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSupportedFeatures            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSupportedFeature             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransformerStatusForwarding [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransformerStatusForwarding [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # If set to true, the software-component is able to use the API reference for deriving a pointer to an object.
        self.enableTakeAddress: Optional[Boolean] = None

        # This specifies whether a RunnableEntity accessing a Port Prototype that is referenced by this PortAPIOption shall specifically handle transformer errors or not.
        self.errorHandling: Optional[DataTransformationErrorHandlingEnum] = None

        # If set to true this attribute specifies an "indirect API" to be generated for the associated port which means that the software-component is able to access the actions on a port via a pointer to an object representing a port. This allows e.g. iterating over ports in a loop. This option has no effect for PPortPrototypes of client/server interfaces.
        self.indirectAPI: Optional[Boolean] = None

        # The option is valid for generated functions related to communication over this port
        self.portRef: Optional[RefType] = None

        # An argument value defined by this port.
        self.portArgValues: List[PortDefinedArgumentValue] = []

        # This collection specifies which features are supported by the RunnableEntitys which access a PortPrototype that it referenced by this PortAPIOption.
        self.supportedFeatures: List[SwcSupportedFeature] = []

        # This attribute specifies whether a RunnableEntity accessing a PortPrototype that is referenced by this Port APIOption shall be able to forward a status code to the transformer chain.
        self.transformerStatusForwarding: Optional[DataTransformationStatusForwardingEnum] = None

    def getEnableTakeAddress(self) -> Optional[Boolean]:
        """
        If set to true, the software-component is able to use the API reference for deriving a pointer to an object.
        """
        return self.enableTakeAddress

    def setEnableTakeAddress(self, value: Optional[Boolean]) -> "PortAPIOption":
        """
        If set to true, the software-component is able to use the API reference for deriving a pointer to an object.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.enableTakeAddress = value
        return self

    def getErrorHandling(self) -> Optional[DataTransformationErrorHandlingEnum]:
        """
        This specifies whether a RunnableEntity accessing a Port Prototype that is referenced by this PortAPIOption shall specifically handle transformer errors or not.
        """
        return self.errorHandling

    def setErrorHandling(self, value: Optional[DataTransformationErrorHandlingEnum]) -> "PortAPIOption":
        """
        This specifies whether a RunnableEntity accessing a Port Prototype that is referenced by this PortAPIOption shall specifically handle transformer errors or not.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.errorHandling = value
        return self

    def getIndirectAPI(self) -> Optional[Boolean]:
        """
        If set to true this attribute specifies an "indirect API" to be generated for the associated port which means that the software-component is able to access the actions on a port via a pointer to an object representing a port. This allows e.g. iterating over ports in a loop. This option has no effect for PPortPrototypes of client/server interfaces.
        """
        return self.indirectAPI

    def setIndirectAPI(self, value: Optional[Boolean]) -> "PortAPIOption":
        """
        If set to true this attribute specifies an "indirect API" to be generated for the associated port which means that the software-component is able to access the actions on a port via a pointer to an object representing a port. This allows e.g. iterating over ports in a loop. This option has no effect for PPortPrototypes of client/server interfaces.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.indirectAPI = value
        return self

    def getPortRef(self) -> Optional[RefType]:
        """
        The option is valid for generated functions related to communication over this port
        """
        return self.portRef

    def setPortRef(self, value: Optional[RefType]) -> "PortAPIOption":
        """
        The option is valid for generated functions related to communication over this port
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.portRef = value
        return self

    def getPortArgValues(self) -> List[PortDefinedArgumentValue]:
        """
        An argument value defined by this port.
        """
        return self.portArgValues

    def addPortArgValue(self, value: Optional[PortDefinedArgumentValue]) -> "PortAPIOption":
        """
        An argument value defined by this port.
        A None value is a no-op and does not append to portArgValues.
        """
        if value is not None:
            self.portArgValues.append(value)
        return self

    def getSupportedFeatures(self) -> List[SwcSupportedFeature]:
        """
        This collection specifies which features are supported by the RunnableEntitys which access a PortPrototype that it referenced by this PortAPIOption.
        """
        return self.supportedFeatures

    def addSupportedFeature(self, value: Optional[SwcSupportedFeature]) -> "PortAPIOption":
        """
        This collection specifies which features are supported by the RunnableEntitys which access a PortPrototype that it referenced by this PortAPIOption.
        A None value is a no-op and does not append to supportedFeatures.
        """
        if value is not None:
            self.supportedFeatures.append(value)
        return self

    def getTransformerStatusForwarding(self) -> Optional[DataTransformationStatusForwardingEnum]:
        """
        This attribute specifies whether a RunnableEntity accessing a PortPrototype that is referenced by this Port APIOption shall be able to forward a status code to the transformer chain.
        """
        return self.transformerStatusForwarding

    def setTransformerStatusForwarding(self, value: Optional[DataTransformationStatusForwardingEnum]) -> "PortAPIOption":
        """
        This attribute specifies whether a RunnableEntity accessing a PortPrototype that is referenced by this Port APIOption shall be able to forward a status code to the transformer chain.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.transformerStatusForwarding = value
        return self
