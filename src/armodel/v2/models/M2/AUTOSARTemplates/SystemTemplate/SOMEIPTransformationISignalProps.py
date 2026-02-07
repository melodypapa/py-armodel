from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SOMEIPTransformationISignalProps(ARObject):
    """
    The class SOMEIPTransformationISignalProps specifies ISignal specific
    configuration properties for SOME/IP transformer attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::SOMEIPTransformationISignalProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 778, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates that Strings in the SOME/IP shall NOT be serialized
                # according to the SOME/ specification for Strings.
        # attribute is set to true, BOM and null-termination be added in the
                # serialization for Strings in the this attribute is set to false (or not set)
                # BOM shall be added in the serialization for the payload according to the
                # SOME/IP Strings.
        # attribute is not future safe, and will be an upcoming AUTOSAR release!".
        self._implements: Optional["Boolean"] = None

    @property
    def implements(self) -> Optional["Boolean"]:
        """Get implements (Pythonic accessor)."""
        return self._implements

    @implements.setter
    def implements(self, value: Optional["Boolean"]) -> None:
        """
        Set implements with validation.
        
        Args:
            value: The implements to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implements = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"implements must be Boolean or None, got {type(value).__name__}"
            )
        self._implements = value
        # The interface version the SOME/IP transformer shall use.
        self._interfaceVersion: Optional["PositiveInteger"] = None

    @property
    def interface_version(self) -> Optional["PositiveInteger"]:
        """Get interfaceVersion (Pythonic accessor)."""
        return self._interfaceVersion

    @interface_version.setter
    def interface_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set interfaceVersion with validation.
        
        Args:
            value: The interfaceVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interfaceVersion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"interfaceVersion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._interfaceVersion = value
        # This attribute shall be used to determine the wire type in context of using
        # the TLV encoding.
        self._isDynamic: Optional["Boolean"] = None

    @property
    def is_dynamic(self) -> Optional["Boolean"]:
        """Get isDynamic (Pythonic accessor)."""
        return self._isDynamic

    @is_dynamic.setter
    def is_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set isDynamic with validation.
        
        Args:
            value: The isDynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isDynamic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isDynamic must be Boolean or None, got {type(value).__name__}"
            )
        self._isDynamic = value
        # The Message Type which shall be placed into the SOME/ header.
        self._messageType: Optional["SOMEIPMessageType"] = None

    @property
    def message_type(self) -> Optional["SOMEIPMessageType"]:
        """Get messageType (Pythonic accessor)."""
        return self._messageType

    @message_type.setter
    def message_type(self, value: Optional["SOMEIPMessageType"]) -> None:
        """
        Set messageType with validation.
        
        Args:
            value: The messageType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageType = None
            return

        if not isinstance(value, SOMEIPMessageType):
            raise TypeError(
                f"messageType must be SOMEIPMessageType or None, got {type(value).__name__}"
            )
        self._messageType = value
        # The size of all length fields (in Bytes) of fixed-size arrays dynamic size
                # arrays in the SOME/IP message.
        # This valid for all available occurrences of fixed-size dynamic size arrays in
                # the SOME/IP message.
        self._sizeOfArray: Optional["PositiveInteger"] = None

    @property
    def size_of_array(self) -> Optional["PositiveInteger"]:
        """Get sizeOfArray (Pythonic accessor)."""
        return self._sizeOfArray

    @size_of_array.setter
    def size_of_array(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfArray with validation.
        
        Args:
            value: The sizeOfArray to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfArray = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfArray must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfArray = value
        # The size of all length fields (in Bytes) of dynamic length in the SOME/IP
                # message.
        # This attribute is valid for occurrences of strings in the SOME/IP.
        self._sizeOfString: Optional["PositiveInteger"] = None

    @property
    def size_of_string(self) -> Optional["PositiveInteger"]:
        """Get sizeOfString (Pythonic accessor)."""
        return self._sizeOfString

    @size_of_string.setter
    def size_of_string(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfString with validation.
        
        Args:
            value: The sizeOfString to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfString = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfString must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfString = value
        # The size of all length fields (in Bytes) of structs in the message.
        # This attribute is valid for all available structures in the SOME/IP message.
        # For fine granular modeling on the level of Data
                # DataPrototypeTransformationProps shall.
        self._sizeOfStruct: Optional["PositiveInteger"] = None

    @property
    def size_of_struct(self) -> Optional["PositiveInteger"]:
        """Get sizeOfStruct (Pythonic accessor)."""
        return self._sizeOfStruct

    @size_of_struct.setter
    def size_of_struct(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfStruct with validation.
        
        Args:
            value: The sizeOfStruct to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfStruct = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfStruct must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfStruct = value
        # The size of all length fields (in Bytes) of unions in the message.
        # This attribute is valid for all available Unions in the SOME/IP message.
        # For a granular modeling on the level of Data DataPrototypeTransformationProps
                # shall.
        self._sizeOfUnion: Optional["PositiveInteger"] = None

    @property
    def size_of_union(self) -> Optional["PositiveInteger"]:
        """Get sizeOfUnion (Pythonic accessor)."""
        return self._sizeOfUnion

    @size_of_union.setter
    def size_of_union(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfUnion with validation.
        
        Args:
            value: The sizeOfUnion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfUnion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfUnion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfUnion = value
        # This reference identifies the TlvDataIdDefinitions relevant the enclosing
        # SOMEIPTransformationISignalProps.
        self._tlvDataId: List[RefType] = []

    @property
    def tlv_data_id(self) -> List[RefType]:
        """Get tlvDataId (Pythonic accessor)."""
        return self._tlvDataId

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplements(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for implements.
        
        Returns:
            The implements value
        
        Note:
            Delegates to implements property (CODING_RULE_V2_00017)
        """
        return self.implements  # Delegates to property

    def setImplements(self, value: "Boolean") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for implements with method chaining.
        
        Args:
            value: The implements to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to implements property setter (gets validation automatically)
        """
        self.implements = value  # Delegates to property setter
        return self

    def getInterfaceVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for interfaceVersion.
        
        Returns:
            The interfaceVersion value
        
        Note:
            Delegates to interface_version property (CODING_RULE_V2_00017)
        """
        return self.interface_version  # Delegates to property

    def setInterfaceVersion(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for interfaceVersion with method chaining.
        
        Args:
            value: The interfaceVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to interface_version property setter (gets validation automatically)
        """
        self.interface_version = value  # Delegates to property setter
        return self

    def getIsDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isDynamic.
        
        Returns:
            The isDynamic value
        
        Note:
            Delegates to is_dynamic property (CODING_RULE_V2_00017)
        """
        return self.is_dynamic  # Delegates to property

    def setIsDynamic(self, value: "Boolean") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for isDynamic with method chaining.
        
        Args:
            value: The isDynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to is_dynamic property setter (gets validation automatically)
        """
        self.is_dynamic = value  # Delegates to property setter
        return self

    def getMessageType(self) -> "SOMEIPMessageType":
        """
        AUTOSAR-compliant getter for messageType.
        
        Returns:
            The messageType value
        
        Note:
            Delegates to message_type property (CODING_RULE_V2_00017)
        """
        return self.message_type  # Delegates to property

    def setMessageType(self, value: "SOMEIPMessageType") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for messageType with method chaining.
        
        Args:
            value: The messageType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_type property setter (gets validation automatically)
        """
        self.message_type = value  # Delegates to property setter
        return self

    def getSizeOfArray(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfArray.
        
        Returns:
            The sizeOfArray value
        
        Note:
            Delegates to size_of_array property (CODING_RULE_V2_00017)
        """
        return self.size_of_array  # Delegates to property

    def setSizeOfArray(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfArray with method chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_array property setter (gets validation automatically)
        """
        self.size_of_array = value  # Delegates to property setter
        return self

    def getSizeOfString(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfString.
        
        Returns:
            The sizeOfString value
        
        Note:
            Delegates to size_of_string property (CODING_RULE_V2_00017)
        """
        return self.size_of_string  # Delegates to property

    def setSizeOfString(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfString with method chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_string property setter (gets validation automatically)
        """
        self.size_of_string = value  # Delegates to property setter
        return self

    def getSizeOfStruct(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfStruct.
        
        Returns:
            The sizeOfStruct value
        
        Note:
            Delegates to size_of_struct property (CODING_RULE_V2_00017)
        """
        return self.size_of_struct  # Delegates to property

    def setSizeOfStruct(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfStruct with method chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_struct property setter (gets validation automatically)
        """
        self.size_of_struct = value  # Delegates to property setter
        return self

    def getSizeOfUnion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfUnion.
        
        Returns:
            The sizeOfUnion value
        
        Note:
            Delegates to size_of_union property (CODING_RULE_V2_00017)
        """
        return self.size_of_union  # Delegates to property

    def setSizeOfUnion(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfUnion with method chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_union property setter (gets validation automatically)
        """
        self.size_of_union = value  # Delegates to property setter
        return self

    def getTlvDataId(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for tlvDataId.
        
        Returns:
            The tlvDataId value
        
        Note:
            Delegates to tlv_data_id property (CODING_RULE_V2_00017)
        """
        return self.tlv_data_id  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implements(self, value: Optional["Boolean"]) -> "SOMEIPTransformationISignalProps":
        """
        Set implements and return self for chaining.
        
        Args:
            value: The implements to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_implements("value")
        """
        self.implements = value  # Use property setter (gets validation)
        return self

    def with_interface_version(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set interfaceVersion and return self for chaining.
        
        Args:
            value: The interfaceVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_interface_version("value")
        """
        self.interface_version = value  # Use property setter (gets validation)
        return self

    def with_is_dynamic(self, value: Optional["Boolean"]) -> "SOMEIPTransformationISignalProps":
        """
        Set isDynamic and return self for chaining.
        
        Args:
            value: The isDynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_is_dynamic("value")
        """
        self.is_dynamic = value  # Use property setter (gets validation)
        return self

    def with_message_type(self, value: Optional["SOMEIPMessageType"]) -> "SOMEIPTransformationISignalProps":
        """
        Set messageType and return self for chaining.
        
        Args:
            value: The messageType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_type("value")
        """
        self.message_type = value  # Use property setter (gets validation)
        return self

    def with_size_of_array(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfArray and return self for chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_array("value")
        """
        self.size_of_array = value  # Use property setter (gets validation)
        return self

    def with_size_of_string(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfString and return self for chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_string("value")
        """
        self.size_of_string = value  # Use property setter (gets validation)
        return self

    def with_size_of_struct(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfStruct and return self for chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_struct("value")
        """
        self.size_of_struct = value  # Use property setter (gets validation)
        return self

    def with_size_of_union(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfUnion and return self for chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_union("value")
        """
        self.size_of_union = value  # Use property setter (gets validation)
        return self