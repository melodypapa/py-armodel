from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwitchStreamFilterRule(Identifiable):
    """
    SwitchStreamIdentification
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamFilterRule
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 136, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of a filter rule on the data link layer.
        # Tags: atp.
        # Status=candidate.
        self._dataLinkLayer: Optional["StreamFilterRuleData"] = None

    @property
    def data_link_layer(self) -> Optional["StreamFilterRuleData"]:
        """Get dataLinkLayer (Pythonic accessor)."""
        return self._dataLinkLayer

    @data_link_layer.setter
    def data_link_layer(self, value: Optional["StreamFilterRuleData"]) -> None:
        """
        Set dataLinkLayer with validation.
        
        Args:
            value: The dataLinkLayer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLinkLayer = None
            return

        if not isinstance(value, StreamFilterRuleData):
            raise TypeError(
                f"dataLinkLayer must be StreamFilterRuleData or None, got {type(value).__name__}"
            )
        self._dataLinkLayer = value
        # Definition of a filter rule for IEEE1722Tp.
        # Tags: atp.
        # Status=candidate.
        self._ieee1722Tp: Optional["StreamFilterIEEE1722"] = None

    @property
    def ieee1722_tp(self) -> Optional["StreamFilterIEEE1722"]:
        """Get ieee1722Tp (Pythonic accessor)."""
        return self._ieee1722Tp

    @ieee1722_tp.setter
    def ieee1722_tp(self, value: Optional["StreamFilterIEEE1722"]) -> None:
        """
        Set ieee1722Tp with validation.
        
        Args:
            value: The ieee1722Tp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ieee1722Tp = None
            return

        if not isinstance(value, StreamFilterIEEE1722):
            raise TypeError(
                f"ieee1722Tp must be StreamFilterIEEE1722 or None, got {type(value).__name__}"
            )
        self._ieee1722Tp = value
        # Definition of a filter rule IP and TP.
        self._ipTpRule: Optional["StreamFilterRuleIpTp"] = None

    @property
    def ip_tp_rule(self) -> Optional["StreamFilterRuleIpTp"]:
        """Get ipTpRule (Pythonic accessor)."""
        return self._ipTpRule

    @ip_tp_rule.setter
    def ip_tp_rule(self, value: Optional["StreamFilterRuleIpTp"]) -> None:
        """
        Set ipTpRule with validation.
        
        Args:
            value: The ipTpRule to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipTpRule = None
            return

        if not isinstance(value, StreamFilterRuleIpTp):
            raise TypeError(
                f"ipTpRule must be StreamFilterRuleIpTp or None, got {type(value).__name__}"
            )
        self._ipTpRule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLinkLayer(self) -> "StreamFilterRuleData":
        """
        AUTOSAR-compliant getter for dataLinkLayer.
        
        Returns:
            The dataLinkLayer value
        
        Note:
            Delegates to data_link_layer property (CODING_RULE_V2_00017)
        """
        return self.data_link_layer  # Delegates to property

    def setDataLinkLayer(self, value: "StreamFilterRuleData") -> "SwitchStreamFilterRule":
        """
        AUTOSAR-compliant setter for dataLinkLayer with method chaining.
        
        Args:
            value: The dataLinkLayer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_link_layer property setter (gets validation automatically)
        """
        self.data_link_layer = value  # Delegates to property setter
        return self

    def getIeee1722Tp(self) -> "StreamFilterIEEE1722":
        """
        AUTOSAR-compliant getter for ieee1722Tp.
        
        Returns:
            The ieee1722Tp value
        
        Note:
            Delegates to ieee1722_tp property (CODING_RULE_V2_00017)
        """
        return self.ieee1722_tp  # Delegates to property

    def setIeee1722Tp(self, value: "StreamFilterIEEE1722") -> "SwitchStreamFilterRule":
        """
        AUTOSAR-compliant setter for ieee1722Tp with method chaining.
        
        Args:
            value: The ieee1722Tp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ieee1722_tp property setter (gets validation automatically)
        """
        self.ieee1722_tp = value  # Delegates to property setter
        return self

    def getIpTpRule(self) -> "StreamFilterRuleIpTp":
        """
        AUTOSAR-compliant getter for ipTpRule.
        
        Returns:
            The ipTpRule value
        
        Note:
            Delegates to ip_tp_rule property (CODING_RULE_V2_00017)
        """
        return self.ip_tp_rule  # Delegates to property

    def setIpTpRule(self, value: "StreamFilterRuleIpTp") -> "SwitchStreamFilterRule":
        """
        AUTOSAR-compliant setter for ipTpRule with method chaining.
        
        Args:
            value: The ipTpRule to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ip_tp_rule property setter (gets validation automatically)
        """
        self.ip_tp_rule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_link_layer(self, value: Optional["StreamFilterRuleData"]) -> "SwitchStreamFilterRule":
        """
        Set dataLinkLayer and return self for chaining.
        
        Args:
            value: The dataLinkLayer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_link_layer("value")
        """
        self.data_link_layer = value  # Use property setter (gets validation)
        return self

    def with_ieee1722_tp(self, value: Optional["StreamFilterIEEE1722"]) -> "SwitchStreamFilterRule":
        """
        Set ieee1722Tp and return self for chaining.
        
        Args:
            value: The ieee1722Tp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ieee1722_tp("value")
        """
        self.ieee1722_tp = value  # Use property setter (gets validation)
        return self

    def with_ip_tp_rule(self, value: Optional["StreamFilterRuleIpTp"]) -> "SwitchStreamFilterRule":
        """
        Set ipTpRule and return self for chaining.
        
        Args:
            value: The ipTpRule to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ip_tp_rule("value")
        """
        self.ip_tp_rule = value  # Use property setter (gets validation)
        return self