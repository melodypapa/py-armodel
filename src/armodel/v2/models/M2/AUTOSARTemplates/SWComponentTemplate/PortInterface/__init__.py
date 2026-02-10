"""
AUTOSAR Package - PortInterface

Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    AutosarDataPrototype,
)


class ArgumentDataPrototype(AutosarDataPrototype):
    """
    An argument of an operation, much like a data element, but also carries
    direction information and is owned by a particular ClientServerOperation.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ArgumentDataPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 303, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 300, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 102, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1998, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 29, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 160, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the direction of the argument.
        self._direction: Optional["ArgumentDirection"] = None

    @property
    def direction(self) -> Optional["ArgumentDirection"]:
        """Get direction (Pythonic accessor)."""
        return self._direction

    @direction.setter
    def direction(self, value: Optional["ArgumentDirection"]) -> None:
        """
        Set direction with validation.

        Args:
            value: The direction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._direction = None
            return

        if not isinstance(value, ArgumentDirection):
            raise TypeError(
                f"direction must be ArgumentDirection or None, got {type(value).__name__}"
            )
        self._direction = value
        # This defines how the argument type of the servers RunnableEntity is
                # implemented.
        # attribute is not defined this has the same semantics the attribute is set to
                # the value useArgumentType for and structures.
        self._serverArgument: Optional["ServerArgumentImpl"] = None

    @property
    def server_argument(self) -> Optional["ServerArgumentImpl"]:
        """Get serverArgument (Pythonic accessor)."""
        return self._serverArgument

    @server_argument.setter
    def server_argument(self, value: Optional["ServerArgumentImpl"]) -> None:
        """
        Set serverArgument with validation.

        Args:
            value: The serverArgument to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serverArgument = None
            return

        if not isinstance(value, ServerArgumentImpl):
            raise TypeError(
                f"serverArgument must be ServerArgumentImpl or None, got {type(value).__name__}"
            )
        self._serverArgument = value

    def with_argument(self, value):
        """
        Set argument and return self for chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_possible_error(self, value):
        """
        Set possible_error and return self for chaining.

        Args:
            value: The possible_error to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_possible_error("value")
        """
        self.possible_error = value  # Use property setter (gets validation)
        return self

    def with_port_interface(self, value):
        """
        Set port_interface and return self for chaining.

        Args:
            value: The port_interface to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_interface("value")
        """
        self.port_interface = value  # Use property setter (gets validation)
        return self

    def with_sub_element(self, value):
        """
        Set sub_element and return self for chaining.

        Args:
            value: The sub_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_element("value")
        """
        self.sub_element = value  # Use property setter (gets validation)
        return self

    def with_argument(self, value):
        """
        Set argument and return self for chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value):
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_first_mode(self, value):
        """
        Set first_mode and return self for chaining.

        Args:
            value: The first_mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_mode("value")
        """
        self.first_mode = value  # Use property setter (gets validation)
        return self

    def with_value_pair(self, value):
        """
        Set value_pair and return self for chaining.

        Args:
            value: The value_pair to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_pair("value")
        """
        self.value_pair = value  # Use property setter (gets validation)
        return self

    def with_operation(self, value):
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_possible_error(self, value):
        """
        Set possible_error and return self for chaining.

        Args:
            value: The possible_error to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_possible_error("value")
        """
        self.possible_error = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value):
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self

    def with_data_mapping(self, value):
        """
        Set data_mapping and return self for chaining.

        Args:
            value: The data_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_mapping("value")
        """
        self.data_mapping = value  # Use property setter (gets validation)
        return self

    def with_error_mapping(self, value):
        """
        Set error_mapping and return self for chaining.

        Args:
            value: The error_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_mapping("value")
        """
        self.error_mapping = value  # Use property setter (gets validation)
        return self

    def with_operation(self, value):
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_trigger_mapping(self, value):
        """
        Set trigger_mapping and return self for chaining.

        Args:
            value: The trigger_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_mapping("value")
        """
        self.trigger_mapping = value  # Use property setter (gets validation)
        return self

    def with_invalidation_policy(self, value):
        """
        Set invalidation_policy and return self for chaining.

        Args:
            value: The invalidation_policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_invalidation_policy("value")
        """
        self.invalidation_policy = value  # Use property setter (gets validation)
        return self

    def with_nv_data(self, value):
        """
        Set nv_data and return self for chaining.

        Args:
            value: The nv_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nv_data("value")
        """
        self.nv_data = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirection(self) -> "ArgumentDirection":
        """
        AUTOSAR-compliant getter for direction.

        Returns:
            The direction value

        Note:
            Delegates to direction property (CODING_RULE_V2_00017)
        """
        return self.direction  # Delegates to property

    def setDirection(self, value: "ArgumentDirection") -> "ArgumentDataPrototype":
        """
        AUTOSAR-compliant setter for direction with method chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Note:
            Delegates to direction property setter (gets validation automatically)
        """
        self.direction = value  # Delegates to property setter
        return self

    def getServerArgument(self) -> "ServerArgumentImpl":
        """
        AUTOSAR-compliant getter for serverArgument.

        Returns:
            The serverArgument value

        Note:
            Delegates to server_argument property (CODING_RULE_V2_00017)
        """
        return self.server_argument  # Delegates to property

    def setServerArgument(self, value: "ServerArgumentImpl") -> "ArgumentDataPrototype":
        """
        AUTOSAR-compliant setter for serverArgument with method chaining.

        Args:
            value: The serverArgument to set

        Returns:
            self for method chaining

        Note:
            Delegates to server_argument property setter (gets validation automatically)
        """
        self.server_argument = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direction(self, value: Optional["ArgumentDirection"]) -> "ArgumentDataPrototype":
        """
        Set direction and return self for chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direction("value")
        """
        self.direction = value  # Use property setter (gets validation)
        return self

    def with_server_argument(self, value: Optional["ServerArgumentImpl"]) -> "ArgumentDataPrototype":
        """
        Set serverArgument and return self for chaining.

        Args:
            value: The serverArgument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_server_argument("value")
        """
        self.server_argument = value  # Use property setter (gets validation)
        return self



class ClientServerOperation(Identifiable):
    """
    An operation declared within the scope of a client/server interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ClientServerOperation

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 309, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 306, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 102, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2008, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 218, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 28, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 433, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 174, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An argument of this ClientServerOperation atpSplitable; atpVariation.
        self._argument: List["RefType"] = []

    @property
    def argument(self) -> List["RefType"]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # This attribute shall only be used in the implementation of to support the
                # case where input and are allocated in a shared buffer and overwrite input
                # arguments by operations to output arguments.
        # can happen during sliced execution or while are arrays (call by reference).
        # The means that the ClientServerOperation is aware usage of a shared buffer
                # and takes precautions to overwrite of input arguments.
        # attribute does not exist or is set to false the Client not have to consider
                # the usage of a.
        self._diagArgIntegrity: Optional["Boolean"] = None

    @property
    def diag_arg_integrity(self) -> Optional["Boolean"]:
        """Get diagArgIntegrity (Pythonic accessor)."""
        return self._diagArgIntegrity

    @diag_arg_integrity.setter
    def diag_arg_integrity(self, value: Optional["Boolean"]) -> None:
        """
        Set diagArgIntegrity with validation.

        Args:
            value: The diagArgIntegrity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagArgIntegrity = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"diagArgIntegrity must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._diagArgIntegrity = value
        # Possible errors that may by raised by the referring.
        self._possibleError: List["ApplicationError"] = []

    @property
    def possible_error(self) -> List["ApplicationError"]:
        """Get possibleError (Pythonic accessor)."""
        return self._possibleError

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getDiagArgIntegrity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for diagArgIntegrity.

        Returns:
            The diagArgIntegrity value

        Note:
            Delegates to diag_arg_integrity property (CODING_RULE_V2_00017)
        """
        return self.diag_arg_integrity  # Delegates to property

    def setDiagArgIntegrity(self, value: "Boolean") -> "ClientServerOperation":
        """
        AUTOSAR-compliant setter for diagArgIntegrity with method chaining.

        Args:
            value: The diagArgIntegrity to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag_arg_integrity property setter (gets validation automatically)
        """
        self.diag_arg_integrity = value  # Delegates to property setter
        return self

    def getPossibleError(self) -> List["ApplicationError"]:
        """
        AUTOSAR-compliant getter for possibleError.

        Returns:
            The possibleError value

        Note:
            Delegates to possible_error property (CODING_RULE_V2_00017)
        """
        return self.possible_error  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag_arg_integrity(self, value: Optional["Boolean"]) -> "ClientServerOperation":
        """
        Set diagArgIntegrity and return self for chaining.

        Args:
            value: The diagArgIntegrity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag_arg_integrity("value")
        """
        self.diag_arg_integrity = value  # Use property setter (gets validation)
        return self



class PortInterface(ARElement, ABC):
    """
    Abstract base class for an interface that is either provided or required by
    a port of a software component.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 326, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 87, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2046, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 27, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 457, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 200, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PortInterface:
            raise TypeError("PortInterface is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This flag is set if the PortInterface is to be used for an or or or
                # ServiceSwComponentType (namely an AUTOSAR on the same ECU.
        # Otherwise the flag is.
        self._isService: Optional["Boolean"] = None

    @property
    def is_service(self) -> Optional["Boolean"]:
        """Get isService (Pythonic accessor)."""
        return self._isService

    @is_service.setter
    def is_service(self, value: Optional["Boolean"]) -> None:
        """
        Set isService with validation.

        Args:
            value: The isService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isService = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isService must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isService = value
        # This attribute provides further details about the nature of service.
        self._serviceKind: Optional["ServiceProviderEnum"] = None

    @property
    def service_kind(self) -> Optional["ServiceProviderEnum"]:
        """Get serviceKind (Pythonic accessor)."""
        return self._serviceKind

    @service_kind.setter
    def service_kind(self, value: Optional["ServiceProviderEnum"]) -> None:
        """
        Set serviceKind with validation.

        Args:
            value: The serviceKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceKind = None
            return

        if not isinstance(value, ServiceProviderEnum):
            raise TypeError(
                f"serviceKind must be ServiceProviderEnum or None, got {type(value).__name__}"
            )
        self._serviceKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIsService(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isService.

        Returns:
            The isService value

        Note:
            Delegates to is_service property (CODING_RULE_V2_00017)
        """
        return self.is_service  # Delegates to property

    def setIsService(self, value: "Boolean") -> "PortInterface":
        """
        AUTOSAR-compliant setter for isService with method chaining.

        Args:
            value: The isService to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_service property setter (gets validation automatically)
        """
        self.is_service = value  # Delegates to property setter
        return self

    def getServiceKind(self) -> "ServiceProviderEnum":
        """
        AUTOSAR-compliant getter for serviceKind.

        Returns:
            The serviceKind value

        Note:
            Delegates to service_kind property (CODING_RULE_V2_00017)
        """
        return self.service_kind  # Delegates to property

    def setServiceKind(self, value: "ServiceProviderEnum") -> "PortInterface":
        """
        AUTOSAR-compliant setter for serviceKind with method chaining.

        Args:
            value: The serviceKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_kind property setter (gets validation automatically)
        """
        self.service_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_service(self, value: Optional["Boolean"]) -> "PortInterface":
        """
        Set isService and return self for chaining.

        Args:
            value: The isService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_service("value")
        """
        self.is_service = value  # Use property setter (gets validation)
        return self

    def with_service_kind(self, value: Optional["ServiceProviderEnum"]) -> "PortInterface":
        """
        Set serviceKind and return self for chaining.

        Args:
            value: The serviceKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_kind("value")
        """
        self.service_kind = value  # Use property setter (gets validation)
        return self



class InvalidationPolicy(ARObject):
    """
    Specifies whether the component can actively invalidate a particular
    dataElement. If no invalidationPolicy points to a dataElement this is
    considered to yield the identical result as if the handleInvalid attribute
    was set to dontInvalidate.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::InvalidationPolicy

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 97, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the dataElement for which the Invalidation.
        self._dataElement: Optional["RefType"] = None

    @property
    def data_element(self) -> Optional["RefType"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["RefType"]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # This attribute controls how invalidation is applied to the.
        self._handleInvalid: Optional["HandleInvalidEnum"] = None

    @property
    def handle_invalid(self) -> Optional["HandleInvalidEnum"]:
        """Get handleInvalid (Pythonic accessor)."""
        return self._handleInvalid

    @handle_invalid.setter
    def handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> None:
        """
        Set handleInvalid with validation.

        Args:
            value: The handleInvalid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleInvalid = None
            return

        if not isinstance(value, HandleInvalidEnum):
            raise TypeError(
                f"handleInvalid must be HandleInvalidEnum or None, got {type(value).__name__}"
            )
        self._handleInvalid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "RefType") -> "InvalidationPolicy":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getHandleInvalid(self) -> "HandleInvalidEnum":
        """
        AUTOSAR-compliant getter for handleInvalid.

        Returns:
            The handleInvalid value

        Note:
            Delegates to handle_invalid property (CODING_RULE_V2_00017)
        """
        return self.handle_invalid  # Delegates to property

    def setHandleInvalid(self, value: "HandleInvalidEnum") -> "InvalidationPolicy":
        """
        AUTOSAR-compliant setter for handleInvalid with method chaining.

        Args:
            value: The handleInvalid to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_invalid property setter (gets validation automatically)
        """
        self.handle_invalid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> "InvalidationPolicy":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> "InvalidationPolicy":
        """
        Set handleInvalid and return self for chaining.

        Args:
            value: The handleInvalid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_invalid("value")
        """
        self.handle_invalid = value  # Use property setter (gets validation)
        return self



class MetaDataItem(ARObject):
    """
    This meta-class represents a single meta-data item.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::MetaDataItem

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 98, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2037, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute determines the length of the MetaDataItem.
        self._length: Optional["PositiveInteger"] = None

    @property
    def length(self) -> Optional["PositiveInteger"]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set length with validation.

        Args:
            value: The length to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"length must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._length = value
        # This aggregation contributes the specification of the meta-data item type.
        self._metaDataItem: Optional["TextValueSpecification"] = None

    @property
    def meta_data_item(self) -> Optional["TextValueSpecification"]:
        """Get metaDataItem (Pythonic accessor)."""
        return self._metaDataItem

    @meta_data_item.setter
    def meta_data_item(self, value: Optional["TextValueSpecification"]) -> None:
        """
        Set metaDataItem with validation.

        Args:
            value: The metaDataItem to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._metaDataItem = None
            return

        if not isinstance(value, TextValueSpecification):
            raise TypeError(
                f"metaDataItem must be TextValueSpecification or None, got {type(value).__name__}"
            )
        self._metaDataItem = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for length.

        Returns:
            The length value

        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: "PositiveInteger") -> "MetaDataItem":
        """
        AUTOSAR-compliant setter for length with method chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    def getMetaDataItem(self) -> "TextValueSpecification":
        """
        AUTOSAR-compliant getter for metaDataItem.

        Returns:
            The metaDataItem value

        Note:
            Delegates to meta_data_item property (CODING_RULE_V2_00017)
        """
        return self.meta_data_item  # Delegates to property

    def setMetaDataItem(self, value: "TextValueSpecification") -> "MetaDataItem":
        """
        AUTOSAR-compliant setter for metaDataItem with method chaining.

        Args:
            value: The metaDataItem to set

        Returns:
            self for method chaining

        Note:
            Delegates to meta_data_item property setter (gets validation automatically)
        """
        self.meta_data_item = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_length(self, value: Optional["PositiveInteger"]) -> "MetaDataItem":
        """
        Set length and return self for chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self

    def with_meta_data_item(self, value: Optional["TextValueSpecification"]) -> "MetaDataItem":
        """
        Set metaDataItem and return self for chaining.

        Args:
            value: The metaDataItem to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_meta_data_item("value")
        """
        self.meta_data_item = value  # Use property setter (gets validation)
        return self



class MetaDataItemSet(ARObject):
    """
    This meta-class represents the ability to define a set of meta-data items to
    be used in SenderReceiver Interfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::MetaDataItemSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 99, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2037, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the dataElement for which the of meta-data items is
        # defined.
        self._dataElement: List["RefType"] = []

    @property
    def data_element(self) -> List["RefType"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # This aggregation represents the ordered definition of items.
        self._metaDataItem: List["MetaDataItem"] = []

    @property
    def meta_data_item(self) -> List["MetaDataItem"]:
        """Get metaDataItem (Pythonic accessor)."""
        return self._metaDataItem

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def getMetaDataItem(self) -> List["MetaDataItem"]:
        """
        AUTOSAR-compliant getter for metaDataItem.

        Returns:
            The metaDataItem value

        Note:
            Delegates to meta_data_item property (CODING_RULE_V2_00017)
        """
        return self.meta_data_item  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ApplicationError(Identifiable):
    """
    This is a user-defined error that is associated with an element of an
    AUTOSAR interface. It is specific for the particular functionality or
    service provided by the AUTOSAR software component.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ApplicationError

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 108, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1996, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The RTE generator is forced to assign this value to the symbol.
        # Note that for error codes are predefined (see RTE specification).
        self._errorCode: Optional["Integer"] = None

    @property
    def error_code(self) -> Optional["Integer"]:
        """Get errorCode (Pythonic accessor)."""
        return self._errorCode

    @error_code.setter
    def error_code(self, value: Optional["Integer"]) -> None:
        """
        Set errorCode with validation.

        Args:
            value: The errorCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._errorCode = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"errorCode must be Integer or int or None, got {type(value).__name__}"
            )
        self._errorCode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getErrorCode(self) -> "Integer":
        """
        AUTOSAR-compliant getter for errorCode.

        Returns:
            The errorCode value

        Note:
            Delegates to error_code property (CODING_RULE_V2_00017)
        """
        return self.error_code  # Delegates to property

    def setErrorCode(self, value: "Integer") -> "ApplicationError":
        """
        AUTOSAR-compliant setter for errorCode with method chaining.

        Args:
            value: The errorCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to error_code property setter (gets validation automatically)
        """
        self.error_code = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_error_code(self, value: Optional["Integer"]) -> "ApplicationError":
        """
        Set errorCode and return self for chaining.

        Args:
            value: The errorCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_code("value")
        """
        self.error_code = value  # Use property setter (gets validation)
        return self



class PortInterfaceMappingSet(ARElement):
    """
    Specifies a set of (one or more) PortInterfaceMappings.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::PortInterfaceMappingSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 119, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 201, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies one PortInterfaceMapping to support the of Ports typed by two
                # different PortInterfaces elements having unequal names and/or (resolution or
                # range).
        # atpVariation.
        self._portInterface: List["RefType"] = []

    @property
    def port_interface(self) -> List["RefType"]:
        """Get portInterface (Pythonic accessor)."""
        return self._portInterface

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPortInterface(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for portInterface.

        Returns:
            The portInterface value

        Note:
            Delegates to port_interface property (CODING_RULE_V2_00017)
        """
        return self.port_interface  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class PortInterfaceMapping(Identifiable, ABC):
    """
    Specifies one PortInterfaceMapping to support the connection of Ports typed
    by two different Port Interfaces with PortInterface elements having unequal
    names and/or unequal semantic (resolution or range).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::PortInterfaceMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 119, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2046, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 200, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PortInterfaceMapping:
            raise TypeError("PortInterfaceMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataPrototypeMapping(ARObject):
    """
    Defines the mapping of two particular VariableDataPrototypes,
    ParameterDataPrototypes or Argument DataPrototypes with non-equal
    shortNames, non-equal structure (specific condition is described by
    [constr_1187]), and/or non-equal semantic (resolution or range) in context
    of two different Sender ReceiverInterface, NvDataInterface or
    ParameterInterface or Operations. If the semantic is unequal, the following
    rules apply: The textTableMapping is only applicable if the referred
    DataPrototypes are typed by AutosarDataType referring to CompuMethods of
    category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE. In the
    case that the DataPrototypes are typed by AutosarDataType either referring
    to CompuMethods of category LINEAR, IDENTICAL or referring to no CompuMethod
    (which is similar as IDENTICAL) the linear conversion factor is calculated
    out of the factorSiToUnit and offsetSiToUnit attributes of the referred
    Units and the CompuRationalCoeffs of a compuInternalToPhys of the referred
    CompuMethods.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::DataPrototypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 125, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2014, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # First to be mapped DataPrototype in context of a Sender NvDataInterface,
        # ParameterInterface.
        self._firstData: Optional["RefType"] = None

    @property
    def first_data(self) -> Optional["RefType"]:
        """Get firstData (Pythonic accessor)."""
        return self._firstData

    @first_data.setter
    def first_data(self, value: Optional["RefType"]) -> None:
        """
        Set firstData with validation.

        Args:
            value: The firstData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstData = None
            return

        self._firstData = value
        # This reference defines the need to execute the Data <Mip>_<transformerId>
                # functions of the chain when communicating from the Data the Data also
                # specifies the reverse Data functions of chain (i.
        # e.
        # from the DataPrototype the DataPrototype the referenced Data symmetric, i.
        # e.
        # attribute Data set to.
        self._firstToSecond: Optional["DataTransformation"] = None

    @property
    def first_to_second(self) -> Optional["DataTransformation"]:
        """Get firstToSecond (Pythonic accessor)."""
        return self._firstToSecond

    @first_to_second.setter
    def first_to_second(self, value: Optional["DataTransformation"]) -> None:
        """
        Set firstToSecond with validation.

        Args:
            value: The firstToSecond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstToSecond = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"firstToSecond must be DataTransformation or None, got {type(value).__name__}"
            )
        self._firstToSecond = value
        # Second to be mapped DataPrototype in context of a NvDataInterface, Parameter
        # Operation.
        self._secondData: Optional["RefType"] = None

    @property
    def second_data(self) -> Optional["RefType"]:
        """Get secondData (Pythonic accessor)."""
        return self._secondData

    @second_data.setter
    def second_data(self, value: Optional["RefType"]) -> None:
        """
        Set secondData with validation.

        Args:
            value: The secondData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondData = None
            return

        self._secondData = value
        # This defines the need to execute the reverse Data <Mip>_Inv_<transformerId>
        # functions of transformation chain when communicating from the the Data.
        self._secondToFirst: Optional["DataTransformation"] = None

    @property
    def second_to_first(self) -> Optional["DataTransformation"]:
        """Get secondToFirst (Pythonic accessor)."""
        return self._secondToFirst

    @second_to_first.setter
    def second_to_first(self, value: Optional["DataTransformation"]) -> None:
        """
        Set secondToFirst with validation.

        Args:
            value: The secondToFirst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondToFirst = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"secondToFirst must be DataTransformation or None, got {type(value).__name__}"
            )
        self._secondToFirst = value
        # This represents the owned SubelementMapping.
        # atpSplitable.
        self._subElement: List["RefType"] = []

    @property
    def sub_element(self) -> List["RefType"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement
        self._textTable: "RefType" = None

    @property
    def text_table(self) -> "RefType":
        """Get textTable (Pythonic accessor)."""
        return self._textTable

    @text_table.setter
    def text_table(self, value: "RefType") -> None:
        """
        Set textTable with validation.

        Args:
            value: The textTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._textTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for firstData.

        Returns:
            The firstData value

        Note:
            Delegates to first_data property (CODING_RULE_V2_00017)
        """
        return self.first_data  # Delegates to property

    def setFirstData(self, value: "RefType") -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for firstData with method chaining.

        Args:
            value: The firstData to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_data property setter (gets validation automatically)
        """
        self.first_data = value  # Delegates to property setter
        return self

    def getFirstToSecond(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for firstToSecond.

        Returns:
            The firstToSecond value

        Note:
            Delegates to first_to_second property (CODING_RULE_V2_00017)
        """
        return self.first_to_second  # Delegates to property

    def setFirstToSecond(self, value: "DataTransformation") -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for firstToSecond with method chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_to_second property setter (gets validation automatically)
        """
        self.first_to_second = value  # Delegates to property setter
        return self

    def getSecondData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for secondData.

        Returns:
            The secondData value

        Note:
            Delegates to second_data property (CODING_RULE_V2_00017)
        """
        return self.second_data  # Delegates to property

    def setSecondData(self, value: "RefType") -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for secondData with method chaining.

        Args:
            value: The secondData to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_data property setter (gets validation automatically)
        """
        self.second_data = value  # Delegates to property setter
        return self

    def getSecondToFirst(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for secondToFirst.

        Returns:
            The secondToFirst value

        Note:
            Delegates to second_to_first property (CODING_RULE_V2_00017)
        """
        return self.second_to_first  # Delegates to property

    def setSecondToFirst(self, value: "DataTransformation") -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for secondToFirst with method chaining.

        Args:
            value: The secondToFirst to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_to_first property setter (gets validation automatically)
        """
        self.second_to_first = value  # Delegates to property setter
        return self

    def getSubElement(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    def getTextTable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for textTable.

        Returns:
            The textTable value

        Note:
            Delegates to text_table property (CODING_RULE_V2_00017)
        """
        return self.text_table  # Delegates to property

    def setTextTable(self, value: "RefType") -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for textTable with method chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to text_table property setter (gets validation automatically)
        """
        self.text_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_data(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        Set firstData and return self for chaining.

        Args:
            value: The firstData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_data("value")
        """
        self.first_data = value  # Use property setter (gets validation)
        return self

    def with_first_to_second(self, value: Optional["DataTransformation"]) -> "DataPrototypeMapping":
        """
        Set firstToSecond and return self for chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_to_second("value")
        """
        self.first_to_second = value  # Use property setter (gets validation)
        return self

    def with_second_data(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        Set secondData and return self for chaining.

        Args:
            value: The secondData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_data("value")
        """
        self.second_data = value  # Use property setter (gets validation)
        return self

    def with_second_to_first(self, value: Optional["DataTransformation"]) -> "DataPrototypeMapping":
        """
        Set secondToFirst and return self for chaining.

        Args:
            value: The secondToFirst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_to_first("value")
        """
        self.second_to_first = value  # Use property setter (gets validation)
        return self

    def with_text_table(self, value: RefType) -> "DataPrototypeMapping":
        """
        Set textTable and return self for chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_text_table("value")
        """
        self.text_table = value  # Use property setter (gets validation)
        return self



class ClientServerOperationMapping(ARObject):
    """
    Defines the mapping of two particular ClientServerOperations in context of
    two different ClientServer Interfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ClientServerOperationMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 129, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the mapping of two particular ArgumentData with unequal names or
        # unequal semantic range) in context of Operations.
        self._argument: List["RefType"] = []

    @property
    def argument(self) -> List["RefType"]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # First to-be-mapped ClientServerOperation of a Client.
        self._firstOperation: Optional["ClientServerOperation"] = None

    @property
    def first_operation(self) -> Optional["ClientServerOperation"]:
        """Get firstOperation (Pythonic accessor)."""
        return self._firstOperation

    @first_operation.setter
    def first_operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set firstOperation with validation.

        Args:
            value: The firstOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"firstOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._firstOperation = value
        # This reference indicates that a DataTransformation is in the context of the
        # ClientServerOperation.
        self._firstToSecond: Optional["DataTransformation"] = None

    @property
    def first_to_second(self) -> Optional["DataTransformation"]:
        """Get firstToSecond (Pythonic accessor)."""
        return self._firstToSecond

    @first_to_second.setter
    def first_to_second(self, value: Optional["DataTransformation"]) -> None:
        """
        Set firstToSecond with validation.

        Args:
            value: The firstToSecond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstToSecond = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"firstToSecond must be DataTransformation or None, got {type(value).__name__}"
            )
        self._firstToSecond = value
        # Second to-be-mapped ClientServerOperation of a Client.
        self._second: Optional["ClientServerOperation"] = None

    @property
    def second(self) -> Optional["ClientServerOperation"]:
        """Get second (Pythonic accessor)."""
        return self._second

    @second.setter
    def second(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set second with validation.

        Args:
            value: The second to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._second = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"second must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._second = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getFirstOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for firstOperation.

        Returns:
            The firstOperation value

        Note:
            Delegates to first_operation property (CODING_RULE_V2_00017)
        """
        return self.first_operation  # Delegates to property

    def setFirstOperation(self, value: "ClientServerOperation") -> "ClientServerOperationMapping":
        """
        AUTOSAR-compliant setter for firstOperation with method chaining.

        Args:
            value: The firstOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_operation property setter (gets validation automatically)
        """
        self.first_operation = value  # Delegates to property setter
        return self

    def getFirstToSecond(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for firstToSecond.

        Returns:
            The firstToSecond value

        Note:
            Delegates to first_to_second property (CODING_RULE_V2_00017)
        """
        return self.first_to_second  # Delegates to property

    def setFirstToSecond(self, value: "DataTransformation") -> "ClientServerOperationMapping":
        """
        AUTOSAR-compliant setter for firstToSecond with method chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_to_second property setter (gets validation automatically)
        """
        self.first_to_second = value  # Delegates to property setter
        return self

    def getSecond(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for second.

        Returns:
            The second value

        Note:
            Delegates to second property (CODING_RULE_V2_00017)
        """
        return self.second  # Delegates to property

    def setSecond(self, value: "ClientServerOperation") -> "ClientServerOperationMapping":
        """
        AUTOSAR-compliant setter for second with method chaining.

        Args:
            value: The second to set

        Returns:
            self for method chaining

        Note:
            Delegates to second property setter (gets validation automatically)
        """
        self.second = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_operation(self, value: Optional["ClientServerOperation"]) -> "ClientServerOperationMapping":
        """
        Set firstOperation and return self for chaining.

        Args:
            value: The firstOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_operation("value")
        """
        self.first_operation = value  # Use property setter (gets validation)
        return self

    def with_first_to_second(self, value: Optional["DataTransformation"]) -> "ClientServerOperationMapping":
        """
        Set firstToSecond and return self for chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_to_second("value")
        """
        self.first_to_second = value  # Use property setter (gets validation)
        return self

    def with_second(self, value: Optional["ClientServerOperation"]) -> "ClientServerOperationMapping":
        """
        Set second and return self for chaining.

        Args:
            value: The second to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second("value")
        """
        self.second = value  # Use property setter (gets validation)
        return self



class ClientServerApplicationErrorMapping(ARObject):
    """
    This meta-class represents the ability to map ApplicationErrors onto each
    other.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ClientServerApplicationErrorMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 129, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first ApplicationError in the context of
        # ClientServerApplicationErrorMapping.
        self._firstApplication: Optional["ApplicationError"] = None

    @property
    def first_application(self) -> Optional["ApplicationError"]:
        """Get firstApplication (Pythonic accessor)."""
        return self._firstApplication

    @first_application.setter
    def first_application(self, value: Optional["ApplicationError"]) -> None:
        """
        Set firstApplication with validation.

        Args:
            value: The firstApplication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstApplication = None
            return

        if not isinstance(value, ApplicationError):
            raise TypeError(
                f"firstApplication must be ApplicationError or None, got {type(value).__name__}"
            )
        self._firstApplication = value
        # This represents the second ApplicationError in the of the
        # ClientServerApplicationErrorMapping.
        self._second: Optional["ApplicationError"] = None

    @property
    def second(self) -> Optional["ApplicationError"]:
        """Get second (Pythonic accessor)."""
        return self._second

    @second.setter
    def second(self, value: Optional["ApplicationError"]) -> None:
        """
        Set second with validation.

        Args:
            value: The second to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._second = None
            return

        if not isinstance(value, ApplicationError):
            raise TypeError(
                f"second must be ApplicationError or None, got {type(value).__name__}"
            )
        self._second = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstApplication(self) -> "ApplicationError":
        """
        AUTOSAR-compliant getter for firstApplication.

        Returns:
            The firstApplication value

        Note:
            Delegates to first_application property (CODING_RULE_V2_00017)
        """
        return self.first_application  # Delegates to property

    def setFirstApplication(self, value: "ApplicationError") -> "ClientServerApplicationErrorMapping":
        """
        AUTOSAR-compliant setter for firstApplication with method chaining.

        Args:
            value: The firstApplication to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_application property setter (gets validation automatically)
        """
        self.first_application = value  # Delegates to property setter
        return self

    def getSecond(self) -> "ApplicationError":
        """
        AUTOSAR-compliant getter for second.

        Returns:
            The second value

        Note:
            Delegates to second property (CODING_RULE_V2_00017)
        """
        return self.second  # Delegates to property

    def setSecond(self, value: "ApplicationError") -> "ClientServerApplicationErrorMapping":
        """
        AUTOSAR-compliant setter for second with method chaining.

        Args:
            value: The second to set

        Returns:
            self for method chaining

        Note:
            Delegates to second property setter (gets validation automatically)
        """
        self.second = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_application(self, value: Optional["ApplicationError"]) -> "ClientServerApplicationErrorMapping":
        """
        Set firstApplication and return self for chaining.

        Args:
            value: The firstApplication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_application("value")
        """
        self.first_application = value  # Use property setter (gets validation)
        return self

    def with_second(self, value: Optional["ApplicationError"]) -> "ClientServerApplicationErrorMapping":
        """
        Set second and return self for chaining.

        Args:
            value: The second to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second("value")
        """
        self.second = value  # Use property setter (gets validation)
        return self



class ModeDeclarationMappingSet(ARElement):
    """
    This meta-class implements a container for ModeDeclarationGroupMappings

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ModeDeclarationMappingSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 132, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of ModeDeclaration Mappings owned by the
        # enclosing ModeDeclaration.
        self._mode: List["ModeDeclaration"] = []

    @property
    def mode(self) -> List["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ModeDeclarationMapping(Identifiable):
    """
    This meta-class implements a concrete mapping of two ModeDeclarations.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ModeDeclarationMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 132, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first ModeDeclaration of the Mode reference has the
                # multiplicity 1 to support use cases where e.
        # g.
        # one mode of the is mapped to several modes of the mode.
        self._firstMode: List["ModeDeclaration"] = []

    @property
    def first_mode(self) -> List["ModeDeclaration"]:
        """Get firstMode (Pythonic accessor)."""
        return self._firstMode
        # This represents the second ModeDeclaration of the Mode.
        self._secondMode: Optional["ModeDeclaration"] = None

    @property
    def second_mode(self) -> Optional["ModeDeclaration"]:
        """Get secondMode (Pythonic accessor)."""
        return self._secondMode

    @second_mode.setter
    def second_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set secondMode with validation.

        Args:
            value: The secondMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"secondMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._secondMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstMode(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for firstMode.

        Returns:
            The firstMode value

        Note:
            Delegates to first_mode property (CODING_RULE_V2_00017)
        """
        return self.first_mode  # Delegates to property

    def getSecondMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for secondMode.

        Returns:
            The secondMode value

        Note:
            Delegates to second_mode property (CODING_RULE_V2_00017)
        """
        return self.second_mode  # Delegates to property

    def setSecondMode(self, value: "ModeDeclaration") -> "ModeDeclarationMapping":
        """
        AUTOSAR-compliant setter for secondMode with method chaining.

        Args:
            value: The secondMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_mode property setter (gets validation automatically)
        """
        self.second_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_second_mode(self, value: Optional["ModeDeclaration"]) -> "ModeDeclarationMapping":
        """
        Set secondMode and return self for chaining.

        Args:
            value: The secondMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_mode("value")
        """
        self.second_mode = value  # Use property setter (gets validation)
        return self



class SubElementMapping(ARObject):
    """
    This meta-class allows for the definition of mappings of elements of a
    composite data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::SubElementMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 137, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first element referenced in the scope mapping.
        # atpVariation.
        self._firstElement: Optional["RefType"] = None

    @property
    def first_element(self) -> Optional["RefType"]:
        """Get firstElement (Pythonic accessor)."""
        return self._firstElement

    @first_element.setter
    def first_element(self, value: Optional["RefType"]) -> None:
        """
        Set firstElement with validation.

        Args:
            value: The firstElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstElement = None
            return

        self._firstElement = value
        # This represents the second element referenced in the the mapping.
        # atpVariation.
        self._secondElement: Optional["RefType"] = None

    @property
    def second_element(self) -> Optional["RefType"]:
        """Get secondElement (Pythonic accessor)."""
        return self._secondElement

    @second_element.setter
    def second_element(self, value: Optional["RefType"]) -> None:
        """
        Set secondElement with validation.

        Args:
            value: The secondElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondElement = None
            return

        self._secondElement = value
        # of a composite data type.
        self._textTable: "RefType" = None

    @property
    def text_table(self) -> "RefType":
        """Get textTable (Pythonic accessor)."""
        return self._textTable

    @text_table.setter
    def text_table(self, value: "RefType") -> None:
        """
        Set textTable with validation.

        Args:
            value: The textTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._textTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for firstElement.

        Returns:
            The firstElement value

        Note:
            Delegates to first_element property (CODING_RULE_V2_00017)
        """
        return self.first_element  # Delegates to property

    def setFirstElement(self, value: "RefType") -> "SubElementMapping":
        """
        AUTOSAR-compliant setter for firstElement with method chaining.

        Args:
            value: The firstElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_element property setter (gets validation automatically)
        """
        self.first_element = value  # Delegates to property setter
        return self

    def getSecondElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for secondElement.

        Returns:
            The secondElement value

        Note:
            Delegates to second_element property (CODING_RULE_V2_00017)
        """
        return self.second_element  # Delegates to property

    def setSecondElement(self, value: "RefType") -> "SubElementMapping":
        """
        AUTOSAR-compliant setter for secondElement with method chaining.

        Args:
            value: The secondElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_element property setter (gets validation automatically)
        """
        self.second_element = value  # Delegates to property setter
        return self

    def getTextTable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for textTable.

        Returns:
            The textTable value

        Note:
            Delegates to text_table property (CODING_RULE_V2_00017)
        """
        return self.text_table  # Delegates to property

    def setTextTable(self, value: "RefType") -> "SubElementMapping":
        """
        AUTOSAR-compliant setter for textTable with method chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to text_table property setter (gets validation automatically)
        """
        self.text_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_element(self, value: Optional[RefType]) -> "SubElementMapping":
        """
        Set firstElement and return self for chaining.

        Args:
            value: The firstElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_element("value")
        """
        self.first_element = value  # Use property setter (gets validation)
        return self

    def with_second_element(self, value: Optional[RefType]) -> "SubElementMapping":
        """
        Set secondElement and return self for chaining.

        Args:
            value: The secondElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_element("value")
        """
        self.second_element = value  # Use property setter (gets validation)
        return self

    def with_text_table(self, value: RefType) -> "SubElementMapping":
        """
        Set textTable and return self for chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_text_table("value")
        """
        self.text_table = value  # Use property setter (gets validation)
        return self



class SubElementRef(ARObject, ABC):
    """
    This meta-class provides the ability to reference elements of composite data
    type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::SubElementRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 138, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is SubElementRef:
            raise TypeError("SubElementRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TextTableMapping(ARObject):
    """
    Defines the mapping of two DataPrototypes typed by AutosarDataTypes that
    refer to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or
    BITFIELD_TEXTTABLE.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::TextTableMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 145, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 230, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute can be used to support the mapping of bit to bit field,
        # boolean values to bit fields, and vice attribute defines the bit mask for the
        # second the TextTableMapping.
        self._bitfieldTextTable: Optional["PositiveInteger"] = None

    @property
    def bitfield_text_table(self) -> Optional["PositiveInteger"]:
        """Get bitfieldTextTable (Pythonic accessor)."""
        return self._bitfieldTextTable

    @bitfield_text_table.setter
    def bitfield_text_table(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bitfieldTextTable with validation.

        Args:
            value: The bitfieldTextTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitfieldTextTable = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bitfieldTextTable must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._bitfieldTextTable = value
        # If identicalMapping is set == true the values of the two DataPrototypes do
        # not need any conversion of.
        self._identical: Optional["Boolean"] = None

    @property
    def identical(self) -> Optional["Boolean"]:
        """Get identical (Pythonic accessor)."""
        return self._identical

    @identical.setter
    def identical(self, value: Optional["Boolean"]) -> None:
        """
        Set identical with validation.

        Args:
            value: The identical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identical = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"identical must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._identical = value
        # Specifies the conversion direction for which the TextTable is applicable.
        self._mapping: Optional["RefType"] = None

    @property
    def mapping(self) -> Optional["RefType"]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping

    @mapping.setter
    def mapping(self, value: Optional["RefType"]) -> None:
        """
        Set mapping with validation.

        Args:
            value: The mapping to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mapping = None
            return

        self._mapping = value
        # Defines a pair of values which are translated into each.
        self._valuePair: List["TextTableValuePair"] = []

    @property
    def value_pair(self) -> List["TextTableValuePair"]:
        """Get valuePair (Pythonic accessor)."""
        return self._valuePair

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitfieldTextTable(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bitfieldTextTable.

        Returns:
            The bitfieldTextTable value

        Note:
            Delegates to bitfield_text_table property (CODING_RULE_V2_00017)
        """
        return self.bitfield_text_table  # Delegates to property

    def setBitfieldTextTable(self, value: "PositiveInteger") -> "TextTableMapping":
        """
        AUTOSAR-compliant setter for bitfieldTextTable with method chaining.

        Args:
            value: The bitfieldTextTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to bitfield_text_table property setter (gets validation automatically)
        """
        self.bitfield_text_table = value  # Delegates to property setter
        return self

    def getIdentical(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for identical.

        Returns:
            The identical value

        Note:
            Delegates to identical property (CODING_RULE_V2_00017)
        """
        return self.identical  # Delegates to property

    def setIdentical(self, value: "Boolean") -> "TextTableMapping":
        """
        AUTOSAR-compliant setter for identical with method chaining.

        Args:
            value: The identical to set

        Returns:
            self for method chaining

        Note:
            Delegates to identical property setter (gets validation automatically)
        """
        self.identical = value  # Delegates to property setter
        return self

    def getMapping(self) -> "RefType":
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    def setMapping(self, value: "RefType") -> "TextTableMapping":
        """
        AUTOSAR-compliant setter for mapping with method chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapping property setter (gets validation automatically)
        """
        self.mapping = value  # Delegates to property setter
        return self

    def getValuePair(self) -> List["TextTableValuePair"]:
        """
        AUTOSAR-compliant getter for valuePair.

        Returns:
            The valuePair value

        Note:
            Delegates to value_pair property (CODING_RULE_V2_00017)
        """
        return self.value_pair  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bitfield_text_table(self, value: Optional["PositiveInteger"]) -> "TextTableMapping":
        """
        Set bitfieldTextTable and return self for chaining.

        Args:
            value: The bitfieldTextTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bitfield_text_table("value")
        """
        self.bitfield_text_table = value  # Use property setter (gets validation)
        return self

    def with_identical(self, value: Optional["Boolean"]) -> "TextTableMapping":
        """
        Set identical and return self for chaining.

        Args:
            value: The identical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identical("value")
        """
        self.identical = value  # Use property setter (gets validation)
        return self

    def with_mapping(self, value: Optional[RefType]) -> "TextTableMapping":
        """
        Set mapping and return self for chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping("value")
        """
        self.mapping = value  # Use property setter (gets validation)
        return self



class TextTableValuePair(ARObject):
    """
    Defines a pair of text values which are translated into each other.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::TextTableValuePair

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 146, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Value of first DataPrototype provided similar to a which is intended to be a
                # Primitive data element.
        # Note that the is a variant, it can be computed by a.
        self._firstValue: Optional["Numerical"] = None

    @property
    def first_value(self) -> Optional["Numerical"]:
        """Get firstValue (Pythonic accessor)."""
        return self._firstValue

    @first_value.setter
    def first_value(self, value: Optional["Numerical"]) -> None:
        """
        Set firstValue with validation.

        Args:
            value: The firstValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstValue = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"firstValue must be Numerical or None, got {type(value).__name__}"
            )
        self._firstValue = value
        # Value of second DataPrototype provided similar to a which is intended to be a
                # Primitive data element.
        # Note that the is a variant, it can be computed by a.
        self._secondValue: Optional["Numerical"] = None

    @property
    def second_value(self) -> Optional["Numerical"]:
        """Get secondValue (Pythonic accessor)."""
        return self._secondValue

    @second_value.setter
    def second_value(self, value: Optional["Numerical"]) -> None:
        """
        Set secondValue with validation.

        Args:
            value: The secondValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondValue = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"secondValue must be Numerical or None, got {type(value).__name__}"
            )
        self._secondValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for firstValue.

        Returns:
            The firstValue value

        Note:
            Delegates to first_value property (CODING_RULE_V2_00017)
        """
        return self.first_value  # Delegates to property

    def setFirstValue(self, value: "Numerical") -> "TextTableValuePair":
        """
        AUTOSAR-compliant setter for firstValue with method chaining.

        Args:
            value: The firstValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_value property setter (gets validation automatically)
        """
        self.first_value = value  # Delegates to property setter
        return self

    def getSecondValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for secondValue.

        Returns:
            The secondValue value

        Note:
            Delegates to second_value property (CODING_RULE_V2_00017)
        """
        return self.second_value  # Delegates to property

    def setSecondValue(self, value: "Numerical") -> "TextTableValuePair":
        """
        AUTOSAR-compliant setter for secondValue with method chaining.

        Args:
            value: The secondValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_value property setter (gets validation automatically)
        """
        self.second_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_value(self, value: Optional["Numerical"]) -> "TextTableValuePair":
        """
        Set firstValue and return self for chaining.

        Args:
            value: The firstValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_value("value")
        """
        self.first_value = value  # Use property setter (gets validation)
        return self

    def with_second_value(self, value: Optional["Numerical"]) -> "TextTableValuePair":
        """
        Set secondValue and return self for chaining.

        Args:
            value: The secondValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_value("value")
        """
        self.second_value = value  # Use property setter (gets validation)
        return self



class ClientServerInterface(PortInterface):
    """
    A client/server interface declares a number of operations that can be
    invoked on a server by a client.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ClientServerInterface

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 308, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 235, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 101, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2007, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 432, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ClientServerOperation(s) of this ClientServerInterface.
        # atpVariation.
        self._operation: List["ClientServerOperation"] = []

    @property
    def operation(self) -> List["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation
        # Application errors that are defined as part of this interface.
        self._possibleError: List["ApplicationError"] = []

    @property
    def possible_error(self) -> List["ApplicationError"]:
        """Get possibleError (Pythonic accessor)."""
        return self._possibleError

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> List["ClientServerOperation"]:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def getPossibleError(self) -> List["ApplicationError"]:
        """
        AUTOSAR-compliant getter for possibleError.

        Returns:
            The possibleError value

        Note:
            Delegates to possible_error property (CODING_RULE_V2_00017)
        """
        return self.possible_error  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataInterface(PortInterface, ABC):
    """
    The purpose of this meta-class is to act as an abstract base class for
    subclasses that share the semantics of being concerned about data (as
    opposed to e.g. operations).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::DataInterface

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 87, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DataInterface:
            raise TypeError("DataInterface is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TriggerInterface(PortInterface):
    """
    A trigger interface declares a number of triggers that can be sent by an
    trigger source.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::TriggerInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 109, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2076, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Trigger of this trigger interface.
        self._trigger: List["RefType"] = []

    @property
    def trigger(self) -> List["RefType"]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrigger(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ModeSwitchInterface(PortInterface):
    """
    A mode switch interface declares a ModeDeclarationGroupPrototype to be sent
    and received.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ModeSwitchInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 113, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2039, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The ModeDeclarationGroupPrototype of this mode.
        self._modeGroup: Optional["RefType"] = None

    @property
    def mode_group(self) -> Optional["RefType"]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: "RefType") -> "ModeSwitchInterface":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group(self, value: Optional[RefType]) -> "ModeSwitchInterface":
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self



class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of VariableDataPrototypes or ParameterDataPrototypes in
    context of two different SenderReceiverInterfaces, NvDataInterfaces or
    ParameterInterfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::VariableAndParameterInterfaceMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 124, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2077, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the mapping of two particular VariableData ParameterDataPrototypes
        # with unequal unequal semantic (resolution or range) in two different
        # SenderReceiverInterfaces, Nv ParameterInterfaces.
        self._dataMapping: List["RefType"] = []

    @property
    def data_mapping(self) -> List["RefType"]:
        """Get dataMapping (Pythonic accessor)."""
        return self._dataMapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataMapping(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dataMapping.

        Returns:
            The dataMapping value

        Note:
            Delegates to data_mapping property (CODING_RULE_V2_00017)
        """
        return self.data_mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ClientServerInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of ClientServerOperations in context of two different
    ClientServerInterfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ClientServerInterfaceMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 128, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Map two different ApplicationErrors defined in the context two different
        # ClientServerInterfaces.
        self._errorMapping: List["ClientServerApplication"] = []

    @property
    def error_mapping(self) -> List["ClientServerApplication"]:
        """Get errorMapping (Pythonic accessor)."""
        return self._errorMapping
        # Mapping of two ClientServerOperations in two different
        # ClientServerInterfaces.
        self._operation: List["ClientServerOperation"] = []

    @property
    def operation(self) -> List["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getErrorMapping(self) -> List["ClientServerApplication"]:
        """
        AUTOSAR-compliant getter for errorMapping.

        Returns:
            The errorMapping value

        Note:
            Delegates to error_mapping property (CODING_RULE_V2_00017)
        """
        return self.error_mapping  # Delegates to property

    def getOperation(self) -> List["ClientServerOperation"]:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ModeInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of ModeDeclarationGroupPrototypes in context of two
    different ModeInterfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ModeInterfaceMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 130, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Mapping of two ModeDeclarationGroupPrototypes in two ModeInterfaces.
        self._modeMapping: Optional["RefType"] = None

    @property
    def mode_mapping(self) -> Optional["RefType"]:
        """Get modeMapping (Pythonic accessor)."""
        return self._modeMapping

    @mode_mapping.setter
    def mode_mapping(self, value: Optional["RefType"]) -> None:
        """
        Set modeMapping with validation.

        Args:
            value: The modeMapping to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeMapping = None
            return

        self._modeMapping = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeMapping(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeMapping.

        Returns:
            The modeMapping value

        Note:
            Delegates to mode_mapping property (CODING_RULE_V2_00017)
        """
        return self.mode_mapping  # Delegates to property

    def setModeMapping(self, value: "RefType") -> "ModeInterfaceMapping":
        """
        AUTOSAR-compliant setter for modeMapping with method chaining.

        Args:
            value: The modeMapping to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_mapping property setter (gets validation automatically)
        """
        self.mode_mapping = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_mapping(self, value: Optional[RefType]) -> "ModeInterfaceMapping":
        """
        Set modeMapping and return self for chaining.

        Args:
            value: The modeMapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_mapping("value")
        """
        self.mode_mapping = value  # Use property setter (gets validation)
        return self



class TriggerInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of unequal named Triggers in context of two different
    TriggerInterfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::TriggerInterfaceMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 134, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Mapping of two Trigger in two different TriggerInterface.
        self._triggerMapping: List["RefType"] = []

    @property
    def trigger_mapping(self) -> List["RefType"]:
        """Get triggerMapping (Pythonic accessor)."""
        return self._triggerMapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTriggerMapping(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for triggerMapping.

        Returns:
            The triggerMapping value

        Note:
            Delegates to trigger_mapping property (CODING_RULE_V2_00017)
        """
        return self.trigger_mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ImplementationDataTypeSubElementRef(SubElementRef):
    """
    This meta-class represents the specialization of SubElementMapping with
    respect to Implementation DataTypes.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ImplementationDataTypeSubElementRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 138, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the referenced implementationDataType Element.
        self._implementation: Optional["ArVariableIn"] = None

    @property
    def implementation(self) -> Optional["ArVariableIn"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["ArVariableIn"]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, ArVariableIn):
            raise TypeError(
                f"implementation must be ArVariableIn or None, got {type(value).__name__}"
            )
        self._implementation = value
        # This represents the referenced ImplementationDataType Element.
        self._parameter: Optional["ArParameterIn"] = None

    @property
    def parameter(self) -> Optional["ArParameterIn"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["ArParameterIn"]) -> None:
        """
        Set parameter with validation.

        Args:
            value: The parameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, ArParameterIn):
            raise TypeError(
                f"parameter must be ArParameterIn or None, got {type(value).__name__}"
            )
        self._parameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementation(self) -> "ArVariableIn":
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "ArVariableIn") -> "ImplementationDataTypeSubElementRef":
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getParameter(self) -> "ArParameterIn":
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "ArParameterIn") -> "ImplementationDataTypeSubElementRef":
        """
        AUTOSAR-compliant setter for parameter with method chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implementation(self, value: Optional["ArVariableIn"]) -> "ImplementationDataTypeSubElementRef":
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["ArParameterIn"]) -> "ImplementationDataTypeSubElementRef":
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self



class ApplicationCompositeDataTypeSubElementRef(SubElementRef):
    """
    This meta-class represents the specialization of SubElementMapping with
    respect to Application CompositeDataTypes.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ApplicationCompositeDataTypeSubElementRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 138, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # DataPrototype.
        # implemented by: ApplicationComposite.
        self._application: Optional["ApplicationComposite"] = None

    @property
    def application(self) -> Optional["ApplicationComposite"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationComposite"]) -> None:
        """
        Set application with validation.

        Args:
            value: The application to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, ApplicationComposite):
            raise TypeError(
                f"application must be ApplicationComposite or None, got {type(value).__name__}"
            )
        self._application = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> "ApplicationComposite":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationComposite") -> "ApplicationCompositeDataTypeSubElementRef":
        """
        AUTOSAR-compliant setter for application with method chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional["ApplicationComposite"]) -> "ApplicationCompositeDataTypeSubElementRef":
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self



class SenderReceiverInterface(DataInterface):
    """
    A sender/receiver interface declares a number of data elements to be sent
    and received.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::SenderReceiverInterface

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 335, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 329, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 94, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2054, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 244, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 208, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The data elements of this SenderReceiverInterface.
        self._dataElement: List["RefType"] = []

    @property
    def data_element(self) -> List["RefType"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # InvalidationPolicy for a particular dataElement.
        self._invalidationPolicy: List["InvalidationPolicy"] = []

    @property
    def invalidation_policy(self) -> List["InvalidationPolicy"]:
        """Get invalidationPolicy (Pythonic accessor)."""
        return self._invalidationPolicy
        # This aggregation defines fixed sets of meta-data items with dataElements of
        # the enclosing Sender.
        self._metaDataItem: List["RefType"] = []

    @property
    def meta_data_item(self) -> List["RefType"]:
        """Get metaDataItem (Pythonic accessor)."""
        return self._metaDataItem

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def getInvalidationPolicy(self) -> List["InvalidationPolicy"]:
        """
        AUTOSAR-compliant getter for invalidationPolicy.

        Returns:
            The invalidationPolicy value

        Note:
            Delegates to invalidation_policy property (CODING_RULE_V2_00017)
        """
        return self.invalidation_policy  # Delegates to property

    def getMetaDataItem(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for metaDataItem.

        Returns:
            The metaDataItem value

        Note:
            Delegates to meta_data_item property (CODING_RULE_V2_00017)
        """
        return self.meta_data_item  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NvDataInterface(DataInterface):
    """
    A non volatile data interface declares a number of VariableDataPrototypes to
    be exchanged between non volatile block components and atomic software
    components.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::NvDataInterface

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 324, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 664, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2041, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 457, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The VariableDataPrototype of this nv data interface.
        self._nvData: List["RefType"] = []

    @property
    def nv_data(self) -> List["RefType"]:
        """Get nvData (Pythonic accessor)."""
        return self._nvData

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNvData(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for nvData.

        Returns:
            The nvData value

        Note:
            Delegates to nv_data property (CODING_RULE_V2_00017)
        """
        return self.nv_data  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ParameterInterface(DataInterface):
    """
    A parameter interface declares a number of parameter and characteristic
    values to be exchanged between parameter components and software components.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ParameterInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 41, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2042, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The ParameterDataPrototype of this ParameterInterface.
        self._parameter: List["ParameterData"] = []

    @property
    def parameter(self) -> List["ParameterData"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParameter(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class ServerArgumentImplPolicyEnum(AREnum):
    """
    ServerArgumentImplPolicyEnum enumeration

This defines how the argument type of the servers RunnableEntity is implemented. Aggregated by ArgumentDataPrototype.serverArgumentImplPolicy

Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface
    """
    # The argument type of the RunnableEntity is derived from the AutosarDataType of the Argument
    useArgumentType = "0"

    # The argument type of the RunnableEntity is void.
    useVoid = "2"



class MappingDirectionEnum(AREnum):
    """
    MappingDirectionEnum enumeration

Specifies the conversion direction for which the mapping is applicable. Aggregated by TextTableMapping.mappingDirection

Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface
    """
    # The TextTableMapping is applicable in both directions.
    bidirectional = "0"

    # The TextTableMapping is applicable in the direction from firstDataPrototype / firstOperationArgument referring into the PortInterface of the PPortPrototype to secondDataPrototype / secondOperation Argument referring into the PortInterface of the RPortPrototype.
    firstToSecond = "1"

    # The TextTableMapping is applicable in the direction from secondDataPrototype / secondOperation Argument referring into the PortInterface of the PPortPrototype to firstDataPrototype / firstOperation Argument referring into the PortInterface of the RPortPrototype.
    secondToFirst = "2"


__all__ = [
    "ArgumentDataPrototype",
    "ClientServerOperation",
    "PortInterface",
    "InvalidationPolicy",
    "MetaDataItem",
    "MetaDataItemSet",
    "ApplicationError",
    "PortInterfaceMappingSet",
    "PortInterfaceMapping",
    "DataPrototypeMapping",
    "ClientServerOperationMapping",
    "ClientServerApplicationErrorMapping",
    "ModeDeclarationMappingSet",
    "ModeDeclarationMapping",
    "SubElementMapping",
    "SubElementRef",
    "TextTableMapping",
    "TextTableValuePair",
    "ClientServerInterface",
    "DataInterface",
    "TriggerInterface",
    "ModeSwitchInterface",
    "VariableAndParameterInterfaceMapping",
    "ClientServerInterfaceMapping",
    "ModeInterfaceMapping",
    "TriggerInterfaceMapping",
    "ImplementationDataTypeSubElementRef",
    "ApplicationCompositeDataTypeSubElementRef",
    "SenderReceiverInterface",
    "NvDataInterface",
    "ParameterInterface",
    "ServerArgumentImplPolicyEnum",
    "MappingDirectionEnum",
]
