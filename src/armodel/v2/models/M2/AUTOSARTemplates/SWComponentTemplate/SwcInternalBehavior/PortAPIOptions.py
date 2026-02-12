"""
AUTOSAR Package - PortAPIOptions

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class PortDefinedArgumentValue(ARObject):
    """
    A PortDefinedArgumentValue is passed to a RunnableEntity dealing with the
    ClientServerOperations provided by a given PortPrototype. Note that this is
    restricted to PPortPrototypes of a ClientServer Interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions::PortDefinedArgumentValue

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 326, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 593, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 199, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the actual value.
        self._value: Optional["ValueSpecification"] = None

    @property
    def value(self) -> Optional["ValueSpecification"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"value must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._value = value
        self._valueType: Optional["ImplementationData"] = None

    @property
    def value_type(self) -> Optional["ImplementationData"]:
        """Get valueType (Pythonic accessor)."""
        return self._valueType

    @value_type.setter
    def value_type(self, value: Optional["ImplementationData"]) -> None:
        """
        Set valueType with validation.

        Args:
            value: The valueType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valueType = None
            return

        if not isinstance(value, ImplementationData):
            raise TypeError(
                f"valueType must be ImplementationData or None, got {type(value).__name__}"
            )
        self._valueType = value

    def with_port_arg_value(self, value):
        """
        Set port_arg_value and return self for chaining.

        Args:
            value: The port_arg_value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_arg_value("value")
        """
        self.port_arg_value = value  # Use property setter (gets validation)
        return self

    def with_supported(self, value):
        """
        Set supported and return self for chaining.

        Args:
            value: The supported to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supported("value")
        """
        self.supported = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "ValueSpecification") -> PortDefinedArgumentValue:
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    def getValueType(self) -> "ImplementationData":
        """
        AUTOSAR-compliant getter for valueType.

        Returns:
            The valueType value

        Note:
            Delegates to value_type property (CODING_RULE_V2_00017)
        """
        return self.value_type  # Delegates to property

    def setValueType(self, value: "ImplementationData") -> PortDefinedArgumentValue:
        """
        AUTOSAR-compliant setter for valueType with method chaining.

        Args:
            value: The valueType to set

        Returns:
            self for method chaining

        Note:
            Delegates to value_type property setter (gets validation automatically)
        """
        self.value_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["ValueSpecification"]) -> PortDefinedArgumentValue:
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_value_type(self, value: Optional["ImplementationData"]) -> PortDefinedArgumentValue:
        """
        Set valueType and return self for chaining.

        Args:
            value: The valueType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_type("value")
        """
        self.value_type = value  # Use property setter (gets validation)
        return self



class PortAPIOption(ARObject):
    """
    Options how to generate the signatures of calls for an AtomicSwComponentType
    in order to communicate over a PortPrototype (for calls into a
    RunnableEntity as well as for calls from a Runnable Entity to the
    PortPrototype).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions::PortAPIOption

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 589, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2045, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If set to true, the software-component is able to use the reference for
        # deriving a pointer to an object.
        self._enableTake: Optional["Boolean"] = None

    @property
    def enable_take(self) -> Optional["Boolean"]:
        """Get enableTake (Pythonic accessor)."""
        return self._enableTake

    @enable_take.setter
    def enable_take(self, value: Optional["Boolean"]) -> None:
        """
        Set enableTake with validation.

        Args:
            value: The enableTake to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableTake = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enableTake must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enableTake = value
        # by this PortAPIOption shall transformer errors or not.
        self._errorHandling: Optional["DataTransformation"] = None

    @property
    def error_handling(self) -> Optional["DataTransformation"]:
        """Get errorHandling (Pythonic accessor)."""
        return self._errorHandling

    @error_handling.setter
    def error_handling(self, value: Optional["DataTransformation"]) -> None:
        """
        Set errorHandling with validation.

        Args:
            value: The errorHandling to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._errorHandling = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"errorHandling must be DataTransformation or None, got {type(value).__name__}"
            )
        self._errorHandling = value
                # associated port which means that the able to access the actions on a a
                # pointer to an object representing a port.
        # This iterating over ports in a loop.
        # This option has for PPortPrototypes of client/server interfaces.
        self._indirectAPI: Optional["Boolean"] = None

    @property
    def indirect_api(self) -> Optional["Boolean"]:
        """Get indirectAPI (Pythonic accessor)."""
        return self._indirectAPI

    @indirect_api.setter
    def indirect_api(self, value: Optional["Boolean"]) -> None:
        """
        Set indirectAPI with validation.

        Args:
            value: The indirectAPI to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indirectAPI = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"indirectAPI must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._indirectAPI = value
        self._port: Optional["RefType"] = None

    @property
    def port(self) -> Optional["RefType"]:
        """Get port (Pythonic accessor)."""
        return self._port

    @port.setter
    def port(self, value: Optional["RefType"]) -> None:
        """
        Set port with validation.

        Args:
            value: The port to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._port = None
            return

        self._port = value
        self._portArgValue: List["PortDefinedArgument"] = []

    @property
    def port_arg_value(self) -> List["PortDefinedArgument"]:
        """Get portArgValue (Pythonic accessor)."""
        return self._portArgValue
        # This collection specifies which features are supported by RunnableEntitys
        # which access a PortPrototype that it this PortAPIOption.
        self._supported: List[SwcSupportedFeature] = []

    @property
    def supported(self) -> List[SwcSupportedFeature]:
        """Get supported (Pythonic accessor)."""
        return self._supported
        # This attribute specifies whether a RunnableEntity accessing a PortPrototype
        # that is referenced by this Port shall be able to forward a status code to
        # the.
        self._transformer: Optional["DataTransformation"] = None

    @property
    def transformer(self) -> Optional["DataTransformation"]:
        """Get transformer (Pythonic accessor)."""
        return self._transformer

    @transformer.setter
    def transformer(self, value: Optional["DataTransformation"]) -> None:
        """
        Set transformer with validation.

        Args:
            value: The transformer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transformer = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"transformer must be DataTransformation or None, got {type(value).__name__}"
            )
        self._transformer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnableTake(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enableTake.

        Returns:
            The enableTake value

        Note:
            Delegates to enable_take property (CODING_RULE_V2_00017)
        """
        return self.enable_take  # Delegates to property

    def setEnableTake(self, value: "Boolean") -> PortAPIOption:
        """
        AUTOSAR-compliant setter for enableTake with method chaining.

        Args:
            value: The enableTake to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_take property setter (gets validation automatically)
        """
        self.enable_take = value  # Delegates to property setter
        return self

    def getErrorHandling(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for errorHandling.

        Returns:
            The errorHandling value

        Note:
            Delegates to error_handling property (CODING_RULE_V2_00017)
        """
        return self.error_handling  # Delegates to property

    def setErrorHandling(self, value: "DataTransformation") -> PortAPIOption:
        """
        AUTOSAR-compliant setter for errorHandling with method chaining.

        Args:
            value: The errorHandling to set

        Returns:
            self for method chaining

        Note:
            Delegates to error_handling property setter (gets validation automatically)
        """
        self.error_handling = value  # Delegates to property setter
        return self

    def getIndirectAPI(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for indirectAPI.

        Returns:
            The indirectAPI value

        Note:
            Delegates to indirect_api property (CODING_RULE_V2_00017)
        """
        return self.indirect_api  # Delegates to property

    def setIndirectAPI(self, value: "Boolean") -> PortAPIOption:
        """
        AUTOSAR-compliant setter for indirectAPI with method chaining.

        Args:
            value: The indirectAPI to set

        Returns:
            self for method chaining

        Note:
            Delegates to indirect_api property setter (gets validation automatically)
        """
        self.indirect_api = value  # Delegates to property setter
        return self

    def getPort(self) -> "RefType":
        """
        AUTOSAR-compliant getter for port.

        Returns:
            The port value

        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def setPort(self, value: "RefType") -> PortAPIOption:
        """
        AUTOSAR-compliant setter for port with method chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Note:
            Delegates to port property setter (gets validation automatically)
        """
        self.port = value  # Delegates to property setter
        return self

    def getPortArgValue(self) -> List["PortDefinedArgument"]:
        """
        AUTOSAR-compliant getter for portArgValue.

        Returns:
            The portArgValue value

        Note:
            Delegates to port_arg_value property (CODING_RULE_V2_00017)
        """
        return self.port_arg_value  # Delegates to property

    def getSupported(self) -> List[SwcSupportedFeature]:
        """
        AUTOSAR-compliant getter for supported.

        Returns:
            The supported value

        Note:
            Delegates to supported property (CODING_RULE_V2_00017)
        """
        return self.supported  # Delegates to property

    def getTransformer(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for transformer.

        Returns:
            The transformer value

        Note:
            Delegates to transformer property (CODING_RULE_V2_00017)
        """
        return self.transformer  # Delegates to property

    def setTransformer(self, value: "DataTransformation") -> PortAPIOption:
        """
        AUTOSAR-compliant setter for transformer with method chaining.

        Args:
            value: The transformer to set

        Returns:
            self for method chaining

        Note:
            Delegates to transformer property setter (gets validation automatically)
        """
        self.transformer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enable_take(self, value: Optional["Boolean"]) -> PortAPIOption:
        """
        Set enableTake and return self for chaining.

        Args:
            value: The enableTake to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_take("value")
        """
        self.enable_take = value  # Use property setter (gets validation)
        return self

    def with_error_handling(self, value: Optional["DataTransformation"]) -> PortAPIOption:
        """
        Set errorHandling and return self for chaining.

        Args:
            value: The errorHandling to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_handling("value")
        """
        self.error_handling = value  # Use property setter (gets validation)
        return self

    def with_indirect_api(self, value: Optional["Boolean"]) -> PortAPIOption:
        """
        Set indirectAPI and return self for chaining.

        Args:
            value: The indirectAPI to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_indirect_api("value")
        """
        self.indirect_api = value  # Use property setter (gets validation)
        return self

    def with_port(self, value: Optional[RefType]) -> PortAPIOption:
        """
        Set port and return self for chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port("value")
        """
        self.port = value  # Use property setter (gets validation)
        return self

    def with_transformer(self, value: Optional["DataTransformation"]) -> PortAPIOption:
        """
        Set transformer and return self for chaining.

        Args:
            value: The transformer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformer("value")
        """
        self.transformer = value  # Use property setter (gets validation)
        return self



class SwcSupportedFeature(ARObject, ABC):
    """
    This meta-class represents a abstract base class for features that can be
    supported by a RunnableEntity.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions::SwcSupportedFeature

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 594, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is SwcSupportedFeature:
            raise TypeError("SwcSupportedFeature is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CommunicationBufferLocking(SwcSupportedFeature):
    """
    The aggregation of this meta-class specifies that a RunnableEntity supports
    locked communication buffers supplied by the RTE. It is able to cope with
    the error RTE_E_COM_BUSY.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions::CommunicationBufferLocking

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 595, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to indicate the intended buffer locking behavior.
        self._supportBuffer: Optional["SupportBufferLocking"] = None

    @property
    def support_buffer(self) -> Optional["SupportBufferLocking"]:
        """Get supportBuffer (Pythonic accessor)."""
        return self._supportBuffer

    @support_buffer.setter
    def support_buffer(self, value: Optional["SupportBufferLocking"]) -> None:
        """
        Set supportBuffer with validation.

        Args:
            value: The supportBuffer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportBuffer = None
            return

        if not isinstance(value, SupportBufferLocking):
            raise TypeError(
                f"supportBuffer must be SupportBufferLocking or None, got {type(value).__name__}"
            )
        self._supportBuffer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSupportBuffer(self) -> "SupportBufferLocking":
        """
        AUTOSAR-compliant getter for supportBuffer.

        Returns:
            The supportBuffer value

        Note:
            Delegates to support_buffer property (CODING_RULE_V2_00017)
        """
        return self.support_buffer  # Delegates to property

    def setSupportBuffer(self, value: "SupportBufferLocking") -> CommunicationBufferLocking:
        """
        AUTOSAR-compliant setter for supportBuffer with method chaining.

        Args:
            value: The supportBuffer to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_buffer property setter (gets validation automatically)
        """
        self.support_buffer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_support_buffer(self, value: Optional["SupportBufferLocking"]) -> CommunicationBufferLocking:
        """
        Set supportBuffer and return self for chaining.

        Args:
            value: The supportBuffer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_buffer("value")
        """
        self.support_buffer = value  # Use property setter (gets validation)
        return self


class DataTransformationErrorHandlingEnum(AREnum):
    """
    DataTransformationErrorHandlingEnum enumeration

This enumeration defines different ways how a RunnableEntity shall handle transformer errors. Aggregated by PortAPIOption.errorHandling

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions
    """
    # A runnable does not handle transformer errors.
    noTransformerErrorHandling = "0"

    # The runnable implements the handling of transformer errors.
    transformerErrorHandling = "1"



class DataTransformationStatusForwardingEnum(AREnum):
    """
    DataTransformationStatusForwardingEnum enumeration

This enumeration defines different ways how a RunnableEntity shall be able to forward status code into the transformer chain. Aggregated by PortAPIOption.transformerStatusForwarding

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions
    """
    # The RunnableEntity is not able to forward a transformer status code.
    noTransformerStatusForwarding = "0"

    # The RunnableEntity is able to forward a transformer status code.
    transformerStatusForwarding = "1"



class SupportBufferLockingEnum(AREnum):
    """
    SupportBufferLockingEnum enumeration

This enumeration represents the ability to define the buffer locking behavior. Aggregated by CommunicationBufferLocking.supportBufferLocking

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions
    """
    # Buffer locking is not supported.
    doesNotSupportBufferLocking = "0"

    # Buffer locking is supported.
    supportsBufferLocking = "1"
