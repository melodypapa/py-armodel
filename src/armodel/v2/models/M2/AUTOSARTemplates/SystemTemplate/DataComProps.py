from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    """
    Represents a single resource required or provided by a CP Software Cluster
    which relates to the port based communication on VFB level.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::DataComProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 903, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines requirements on the data consistency mechanism in the
        # cross cluster If the attribute is not set, the default value.
        self._data: Optional["DataConsistencyPolicy"] = None

    @property
    def data(self) -> Optional["DataConsistencyPolicy"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["DataConsistencyPolicy"]) -> None:
        """
        Set data with validation.
        
        Args:
            value: The data to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        if not isinstance(value, DataConsistencyPolicy):
            raise TypeError(
                f"data must be DataConsistencyPolicy or None, got {type(value).__name__}"
            )
        self._data = value
        # Send indication behavior for last-is-the best data.
        self._sendIndication: Optional["SendIndicationEnum"] = None

    @property
    def send_indication(self) -> Optional["SendIndicationEnum"]:
        """Get sendIndication (Pythonic accessor)."""
        return self._sendIndication

    @send_indication.setter
    def send_indication(self, value: Optional["SendIndicationEnum"]) -> None:
        """
        Set sendIndication with validation.
        
        Args:
            value: The sendIndication to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sendIndication = None
            return

        if not isinstance(value, SendIndicationEnum):
            raise TypeError(
                f"sendIndication must be SendIndicationEnum or None, got {type(value).__name__}"
            )
        self._sendIndication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "DataConsistencyPolicy":
        """
        AUTOSAR-compliant getter for data.
        
        Returns:
            The data value
        
        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "DataConsistencyPolicy") -> "DataComProps":
        """
        AUTOSAR-compliant setter for data with method chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    def getSendIndication(self) -> "SendIndicationEnum":
        """
        AUTOSAR-compliant getter for sendIndication.
        
        Returns:
            The sendIndication value
        
        Note:
            Delegates to send_indication property (CODING_RULE_V2_00017)
        """
        return self.send_indication  # Delegates to property

    def setSendIndication(self, value: "SendIndicationEnum") -> "DataComProps":
        """
        AUTOSAR-compliant setter for sendIndication with method chaining.
        
        Args:
            value: The sendIndication to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to send_indication property setter (gets validation automatically)
        """
        self.send_indication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional["DataConsistencyPolicy"]) -> "DataComProps":
        """
        Set data and return self for chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self

    def with_send_indication(self, value: Optional["SendIndicationEnum"]) -> "DataComProps":
        """
        Set sendIndication and return self for chaining.
        
        Args:
            value: The sendIndication to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_send_indication("value")
        """
        self.send_indication = value  # Use property setter (gets validation)
        return self