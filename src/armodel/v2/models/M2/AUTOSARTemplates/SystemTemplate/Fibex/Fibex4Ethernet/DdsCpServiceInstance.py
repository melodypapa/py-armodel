from abc import ABC
from typing import Optional


class DdsCpServiceInstance(AbstractServiceInstance, ABC):
    """
    Provided and Consumed Dds Service Instances that are available at the
    ApplicationEndpoint.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 472, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DdsCpServiceInstance:
            raise TypeError("DdsCpServiceInstance is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DdsTopic used as fragment for the topic of field setters.
        self._ddsFieldReply: Optional["DdsCpTopic"] = None

    @property
    def dds_field_reply(self) -> Optional["DdsCpTopic"]:
        """Get ddsFieldReply (Pythonic accessor)."""
        return self._ddsFieldReply

    @dds_field_reply.setter
    def dds_field_reply(self, value: Optional["DdsCpTopic"]) -> None:
        """
        Set ddsFieldReply with validation.

        Args:
            value: The ddsFieldReply to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsFieldReply = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsFieldReply must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsFieldReply = value
        # Reference to the DdsTopic used as fragment for the topic of field getters.
        self._ddsField: Optional["DdsCpTopic"] = None

    @property
    def dds_field(self) -> Optional["DdsCpTopic"]:
        """Get ddsField (Pythonic accessor)."""
        return self._ddsField

    @dds_field.setter
    def dds_field(self, value: Optional["DdsCpTopic"]) -> None:
        """
        Set ddsField with validation.

        Args:
            value: The ddsField to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsField = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsField must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsField = value
        # Reference to the DdsTopic used as fragment for the topic of method requests.
        self._ddsMethod: Optional["DdsCpTopic"] = None

    @property
    def dds_method(self) -> Optional["DdsCpTopic"]:
        """Get ddsMethod (Pythonic accessor)."""
        return self._ddsMethod

    @dds_method.setter
    def dds_method(self, value: Optional["DdsCpTopic"]) -> None:
        """
        Set ddsMethod with validation.

        Args:
            value: The ddsMethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsMethod = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsMethod must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsMethod = value
        # Reference to the QOS Profile used for the service.
        # atp.
        # Status=candidate.
        self._ddsServiceQos: Optional["DdsCpQosProfile"] = None

    @property
    def dds_service_qos(self) -> Optional["DdsCpQosProfile"]:
        """Get ddsServiceQos (Pythonic accessor)."""
        return self._ddsServiceQos

    @dds_service_qos.setter
    def dds_service_qos(self, value: Optional["DdsCpQosProfile"]) -> None:
        """
        Set ddsServiceQos with validation.

        Args:
            value: The ddsServiceQos to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsServiceQos = None
            return

        if not isinstance(value, DdsCpQosProfile):
            raise TypeError(
                f"ddsServiceQos must be DdsCpQosProfile or None, got {type(value).__name__}"
            )
        self._ddsServiceQos = value
        # Identification number that is used by DDS to identify associated with an
        # instance of the.
        self._serviceInstance: Optional["PositiveInteger"] = None

    @property
    def service_instance(self) -> Optional["PositiveInteger"]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    @service_instance.setter
    def service_instance(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set serviceInstance with validation.

        Args:
            value: The serviceInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceInstance = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"serviceInstance must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._serviceInstance = value
        # Unique Identifier that identifies the ServiceInterface in This Identifier is
        # encoded in the USER_DATA QoS DomainParticipant associated with the Service
        # its value is propagated by DDS Discovery.
        self._serviceInterface: Optional["String"] = None

    @property
    def service_interface(self) -> Optional["String"]:
        """Get serviceInterface (Pythonic accessor)."""
        return self._serviceInterface

    @service_interface.setter
    def service_interface(self, value: Optional["String"]) -> None:
        """
        Set serviceInterface with validation.

        Args:
            value: The serviceInterface to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceInterface = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"serviceInterface must be String or None, got {type(value).__name__}"
            )
        self._serviceInterface = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsFieldReply(self) -> "DdsCpTopic":
        """
        AUTOSAR-compliant getter for ddsFieldReply.

        Returns:
            The ddsFieldReply value

        Note:
            Delegates to dds_field_reply property (CODING_RULE_V2_00017)
        """
        return self.dds_field_reply  # Delegates to property

    def setDdsFieldReply(self, value: "DdsCpTopic") -> "DdsCpServiceInstance":
        """
        AUTOSAR-compliant setter for ddsFieldReply with method chaining.

        Args:
            value: The ddsFieldReply to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_field_reply property setter (gets validation automatically)
        """
        self.dds_field_reply = value  # Delegates to property setter
        return self

    def getDdsField(self) -> "DdsCpTopic":
        """
        AUTOSAR-compliant getter for ddsField.

        Returns:
            The ddsField value

        Note:
            Delegates to dds_field property (CODING_RULE_V2_00017)
        """
        return self.dds_field  # Delegates to property

    def setDdsField(self, value: "DdsCpTopic") -> "DdsCpServiceInstance":
        """
        AUTOSAR-compliant setter for ddsField with method chaining.

        Args:
            value: The ddsField to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_field property setter (gets validation automatically)
        """
        self.dds_field = value  # Delegates to property setter
        return self

    def getDdsMethod(self) -> "DdsCpTopic":
        """
        AUTOSAR-compliant getter for ddsMethod.

        Returns:
            The ddsMethod value

        Note:
            Delegates to dds_method property (CODING_RULE_V2_00017)
        """
        return self.dds_method  # Delegates to property

    def setDdsMethod(self, value: "DdsCpTopic") -> "DdsCpServiceInstance":
        """
        AUTOSAR-compliant setter for ddsMethod with method chaining.

        Args:
            value: The ddsMethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_method property setter (gets validation automatically)
        """
        self.dds_method = value  # Delegates to property setter
        return self

    def getDdsServiceQos(self) -> "DdsCpQosProfile":
        """
        AUTOSAR-compliant getter for ddsServiceQos.

        Returns:
            The ddsServiceQos value

        Note:
            Delegates to dds_service_qos property (CODING_RULE_V2_00017)
        """
        return self.dds_service_qos  # Delegates to property

    def setDdsServiceQos(self, value: "DdsCpQosProfile") -> "DdsCpServiceInstance":
        """
        AUTOSAR-compliant setter for ddsServiceQos with method chaining.

        Args:
            value: The ddsServiceQos to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_service_qos property setter (gets validation automatically)
        """
        self.dds_service_qos = value  # Delegates to property setter
        return self

    def getServiceInstance(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for serviceInstance.

        Returns:
            The serviceInstance value

        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    def setServiceInstance(self, value: "PositiveInteger") -> "DdsCpServiceInstance":
        """
        AUTOSAR-compliant setter for serviceInstance with method chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_instance property setter (gets validation automatically)
        """
        self.service_instance = value  # Delegates to property setter
        return self

    def getServiceInterface(self) -> "String":
        """
        AUTOSAR-compliant getter for serviceInterface.

        Returns:
            The serviceInterface value

        Note:
            Delegates to service_interface property (CODING_RULE_V2_00017)
        """
        return self.service_interface  # Delegates to property

    def setServiceInterface(self, value: "String") -> "DdsCpServiceInstance":
        """
        AUTOSAR-compliant setter for serviceInterface with method chaining.

        Args:
            value: The serviceInterface to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_interface property setter (gets validation automatically)
        """
        self.service_interface = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_field_reply(self, value: Optional["DdsCpTopic"]) -> "DdsCpServiceInstance":
        """
        Set ddsFieldReply and return self for chaining.

        Args:
            value: The ddsFieldReply to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_field_reply("value")
        """
        self.dds_field_reply = value  # Use property setter (gets validation)
        return self

    def with_dds_field(self, value: Optional["DdsCpTopic"]) -> "DdsCpServiceInstance":
        """
        Set ddsField and return self for chaining.

        Args:
            value: The ddsField to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_field("value")
        """
        self.dds_field = value  # Use property setter (gets validation)
        return self

    def with_dds_method(self, value: Optional["DdsCpTopic"]) -> "DdsCpServiceInstance":
        """
        Set ddsMethod and return self for chaining.

        Args:
            value: The ddsMethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_method("value")
        """
        self.dds_method = value  # Use property setter (gets validation)
        return self

    def with_dds_service_qos(self, value: Optional["DdsCpQosProfile"]) -> "DdsCpServiceInstance":
        """
        Set ddsServiceQos and return self for chaining.

        Args:
            value: The ddsServiceQos to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_service_qos("value")
        """
        self.dds_service_qos = value  # Use property setter (gets validation)
        return self

    def with_service_instance(self, value: Optional["PositiveInteger"]) -> "DdsCpServiceInstance":
        """
        Set serviceInstance and return self for chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_instance("value")
        """
        self.service_instance = value  # Use property setter (gets validation)
        return self

    def with_service_interface(self, value: Optional["String"]) -> "DdsCpServiceInstance":
        """
        Set serviceInterface and return self for chaining.

        Args:
            value: The serviceInterface to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_interface("value")
        """
        self.service_interface = value  # Use property setter (gets validation)
        return self
