from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DataTransformation,
    PortDefinedArgument,
    SwcSupportedFeature,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)


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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"enableTake must be Boolean or None, got {type(value).__name__}"
            )
        self._enableTake = value
        # This specifies whether a RunnableEntity accessing a Port that is referenced
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
        # If set to true this attribute specifies an "indirect API" to be the
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"indirectAPI must be Boolean or None, got {type(value).__name__}"
            )
        self._indirectAPI = value
        # The option is valid for generated functions related to this port.
        self._port: RefType = None

    @property
    def port(self) -> RefType:
        """Get port (Pythonic accessor)."""
        return self._port

    @port.setter
    def port(self, value: RefType) -> None:
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
        # An argument value defined by this port.
        self._portArgValue: List["PortDefinedArgument"] = []

    @property
    def port_arg_value(self) -> List["PortDefinedArgument"]:
        """Get portArgValue (Pythonic accessor)."""
        return self._portArgValue
        # This collection specifies which features are supported by RunnableEntitys
        # which access a PortPrototype that it this PortAPIOption.
        self._supported: List["SwcSupportedFeature"] = []

    @property
    def supported(self) -> List["SwcSupportedFeature"]:
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

    def setEnableTake(self, value: "Boolean") -> "PortAPIOption":
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

    def setErrorHandling(self, value: "DataTransformation") -> "PortAPIOption":
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

    def setIndirectAPI(self, value: "Boolean") -> "PortAPIOption":
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

    def getPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for port.

        Returns:
            The port value

        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def setPort(self, value: RefType) -> "PortAPIOption":
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

    def getSupported(self) -> List["SwcSupportedFeature"]:
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

    def setTransformer(self, value: "DataTransformation") -> "PortAPIOption":
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

    def with_enable_take(self, value: Optional["Boolean"]) -> "PortAPIOption":
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

    def with_error_handling(self, value: Optional["DataTransformation"]) -> "PortAPIOption":
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

    def with_indirect_api(self, value: Optional["Boolean"]) -> "PortAPIOption":
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

    def with_port(self, value: Optional[RefType]) -> "PortAPIOption":
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

    def with_transformer(self, value: Optional["DataTransformation"]) -> "PortAPIOption":
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
