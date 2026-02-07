from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TransmissionModeCondition(ARObject):
    """
    Possibility to attach a condition to each signal within an I-PDU. If at
    least one condition evaluates to true, TRANSMISSION MODE True shall be used
    for this I-Pdu. In all other cases, the TRANSMISSION MODE FALSE shall be
    used.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TransmissionModeCondition
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 392, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Possibilities to define conditions.
        self._dataFilter: Optional["DataFilter"] = None

    @property
    def data_filter(self) -> Optional["DataFilter"]:
        """Get dataFilter (Pythonic accessor)."""
        return self._dataFilter

    @data_filter.setter
    def data_filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set dataFilter with validation.
        
        Args:
            value: The dataFilter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFilter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"dataFilter must be DataFilter or None, got {type(value).__name__}"
            )
        self._dataFilter = value
        # Reference to a signal to which a condition is attached.
        self._iSignalInIPdu: RefType = None

    @property
    def i_signal_in_i_pdu(self) -> RefType:
        """Get iSignalInIPdu (Pythonic accessor)."""
        return self._iSignalInIPdu

    @i_signal_in_i_pdu.setter
    def i_signal_in_i_pdu(self, value: RefType) -> None:
        """
        Set iSignalInIPdu with validation.
        
        Args:
            value: The iSignalInIPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalInIPdu = None
            return

        self._iSignalInIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for dataFilter.
        
        Returns:
            The dataFilter value
        
        Note:
            Delegates to data_filter property (CODING_RULE_V2_00017)
        """
        return self.data_filter  # Delegates to property

    def setDataFilter(self, value: "DataFilter") -> "TransmissionModeCondition":
        """
        AUTOSAR-compliant setter for dataFilter with method chaining.
        
        Args:
            value: The dataFilter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_filter property setter (gets validation automatically)
        """
        self.data_filter = value  # Delegates to property setter
        return self

    def getISignalInIPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for iSignalInIPdu.
        
        Returns:
            The iSignalInIPdu value
        
        Note:
            Delegates to i_signal_in_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_in_i_pdu  # Delegates to property

    def setISignalInIPdu(self, value: RefType) -> "TransmissionModeCondition":
        """
        AUTOSAR-compliant setter for iSignalInIPdu with method chaining.
        
        Args:
            value: The iSignalInIPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal_in_i_pdu property setter (gets validation automatically)
        """
        self.i_signal_in_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_filter(self, value: Optional["DataFilter"]) -> "TransmissionModeCondition":
        """
        Set dataFilter and return self for chaining.
        
        Args:
            value: The dataFilter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_filter("value")
        """
        self.data_filter = value  # Use property setter (gets validation)
        return self

    def with_i_signal_in_i_pdu(self, value: Optional[RefType]) -> "TransmissionModeCondition":
        """
        Set iSignalInIPdu and return self for chaining.
        
        Args:
            value: The iSignalInIPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal_in_i_pdu("value")
        """
        self.i_signal_in_i_pdu = value  # Use property setter (gets validation)
        return self