from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DynamicPartAlternative(ARObject):
    """
    One of the Com IPdu alternatives that are transmitted in the Dynamic Part of
    the MultiplexedIPdu. The selectorFieldCode specifies which Com IPdu is
    contained in the DynamicPart within a certain transmission of a multiplexed
    PDU.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::DynamicPartAlternative
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 411, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Dynamic part that shall be used to initialize this IPdu.
        # one "DynamicPartAlternative" in a be the initialDynamicPart.
        self._initialDynamic: Optional["Boolean"] = None

    @property
    def initial_dynamic(self) -> Optional["Boolean"]:
        """Get initialDynamic (Pythonic accessor)."""
        return self._initialDynamic

    @initial_dynamic.setter
    def initial_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set initialDynamic with validation.
        
        Args:
            value: The initialDynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialDynamic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"initialDynamic must be Boolean or None, got {type(value).__name__}"
            )
        self._initialDynamic = value
        # Reference to a Com IPdu which is routed to the IPduM is combined to a
        # multiplexedPdu.
        self._iPdu: Optional["ISignalIPdu"] = None

    @property
    def i_pdu(self) -> Optional["ISignalIPdu"]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional["ISignalIPdu"]) -> None:
        """
        Set iPdu with validation.
        
        Args:
            value: The iPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPdu = None
            return

        if not isinstance(value, ISignalIPdu):
            raise TypeError(
                f"iPdu must be ISignalIPdu or None, got {type(value).__name__}"
            )
        self._iPdu = value
        # The selector field is part of a multiplexed IPdu.
        # It consists contiguous bits.
        # The value of the selector field selects of the multiplexed part of the IPdu.
        self._selectorField: Optional["Integer"] = None

    @property
    def selector_field(self) -> Optional["Integer"]:
        """Get selectorField (Pythonic accessor)."""
        return self._selectorField

    @selector_field.setter
    def selector_field(self, value: Optional["Integer"]) -> None:
        """
        Set selectorField with validation.
        
        Args:
            value: The selectorField to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._selectorField = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"selectorField must be Integer or None, got {type(value).__name__}"
            )
        self._selectorField = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for initialDynamic.
        
        Returns:
            The initialDynamic value
        
        Note:
            Delegates to initial_dynamic property (CODING_RULE_V2_00017)
        """
        return self.initial_dynamic  # Delegates to property

    def setInitialDynamic(self, value: "Boolean") -> "DynamicPartAlternative":
        """
        AUTOSAR-compliant setter for initialDynamic with method chaining.
        
        Args:
            value: The initialDynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to initial_dynamic property setter (gets validation automatically)
        """
        self.initial_dynamic = value  # Delegates to property setter
        return self

    def getIPdu(self) -> "ISignalIPdu":
        """
        AUTOSAR-compliant getter for iPdu.
        
        Returns:
            The iPdu value
        
        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: "ISignalIPdu") -> "DynamicPartAlternative":
        """
        AUTOSAR-compliant setter for iPdu with method chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_pdu property setter (gets validation automatically)
        """
        self.i_pdu = value  # Delegates to property setter
        return self

    def getSelectorField(self) -> "Integer":
        """
        AUTOSAR-compliant getter for selectorField.
        
        Returns:
            The selectorField value
        
        Note:
            Delegates to selector_field property (CODING_RULE_V2_00017)
        """
        return self.selector_field  # Delegates to property

    def setSelectorField(self, value: "Integer") -> "DynamicPartAlternative":
        """
        AUTOSAR-compliant setter for selectorField with method chaining.
        
        Args:
            value: The selectorField to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to selector_field property setter (gets validation automatically)
        """
        self.selector_field = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_dynamic(self, value: Optional["Boolean"]) -> "DynamicPartAlternative":
        """
        Set initialDynamic and return self for chaining.
        
        Args:
            value: The initialDynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_initial_dynamic("value")
        """
        self.initial_dynamic = value  # Use property setter (gets validation)
        return self

    def with_i_pdu(self, value: Optional["ISignalIPdu"]) -> "DynamicPartAlternative":
        """
        Set iPdu and return self for chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_pdu("value")
        """
        self.i_pdu = value  # Use property setter (gets validation)
        return self

    def with_selector_field(self, value: Optional["Integer"]) -> "DynamicPartAlternative":
        """
        Set selectorField and return self for chaining.
        
        Args:
            value: The selectorField to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_selector_field("value")
        """
        self.selector_field = value  # Use property setter (gets validation)
        return self