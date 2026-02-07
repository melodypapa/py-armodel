from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):
    """
    This meta-class represents the ability to model specific trouble-code
    related properties for J1939.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeJ1939
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 221, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defined properties associated with the J1939 DTC.
        self._dtcPropsProps: Optional["DiagnosticTroubleCode"] = None

    @property
    def dtc_props_props(self) -> Optional["DiagnosticTroubleCode"]:
        """Get dtcPropsProps (Pythonic accessor)."""
        return self._dtcPropsProps

    @dtc_props_props.setter
    def dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set dtcPropsProps with validation.
        
        Args:
            value: The dtcPropsProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dtcPropsProps = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"dtcPropsProps must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._dtcPropsProps = value
        # This attribute represents the behavior of the Failure Mode 719 Document ID
        # 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._fmi: Optional["PositiveInteger"] = None

    @property
    def fmi(self) -> Optional["PositiveInteger"]:
        """Get fmi (Pythonic accessor)."""
        return self._fmi

    @fmi.setter
    def fmi(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set fmi with validation.
        
        Args:
            value: The fmi to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fmi = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"fmi must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._fmi = value
        # This attribute further specifies the DTC in terms of its.
        self._kind: Optional["DiagnosticTroubleCode"] = None

    @property
    def kind(self) -> Optional["DiagnosticTroubleCode"]:
        """Get kind (Pythonic accessor)."""
        return self._kind

    @kind.setter
    def kind(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set kind with validation.
        
        Args:
            value: The kind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._kind = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"kind must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._kind = value
        # This represents the related DiagnosticJ1939Node.
        self._node: Optional["DiagnosticJ1939Node"] = None

    @property
    def node(self) -> Optional["DiagnosticJ1939Node"]:
        """Get node (Pythonic accessor)."""
        return self._node

    @node.setter
    def node(self, value: Optional["DiagnosticJ1939Node"]) -> None:
        """
        Set node with validation.
        
        Args:
            value: The node to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._node = None
            return

        if not isinstance(value, DiagnosticJ1939Node):
            raise TypeError(
                f"node must be DiagnosticJ1939Node or None, got {type(value).__name__}"
            )
        self._node = value
        # This represents the releated SPN.
        self._spn: Optional["DiagnosticJ1939Spn"] = None

    @property
    def spn(self) -> Optional["DiagnosticJ1939Spn"]:
        """Get spn (Pythonic accessor)."""
        return self._spn

    @spn.setter
    def spn(self, value: Optional["DiagnosticJ1939Spn"]) -> None:
        """
        Set spn with validation.
        
        Args:
            value: The spn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._spn = None
            return

        if not isinstance(value, DiagnosticJ1939Spn):
            raise TypeError(
                f"spn must be DiagnosticJ1939Spn or None, got {type(value).__name__}"
            )
        self._spn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDtcPropsProps(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for dtcPropsProps.
        
        Returns:
            The dtcPropsProps value
        
        Note:
            Delegates to dtc_props_props property (CODING_RULE_V2_00017)
        """
        return self.dtc_props_props  # Delegates to property

    def setDtcPropsProps(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for dtcPropsProps with method chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dtc_props_props property setter (gets validation automatically)
        """
        self.dtc_props_props = value  # Delegates to property setter
        return self

    def getFmi(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for fmi.
        
        Returns:
            The fmi value
        
        Note:
            Delegates to fmi property (CODING_RULE_V2_00017)
        """
        return self.fmi  # Delegates to property

    def setFmi(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for fmi with method chaining.
        
        Args:
            value: The fmi to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to fmi property setter (gets validation automatically)
        """
        self.fmi = value  # Delegates to property setter
        return self

    def getKind(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for kind.
        
        Returns:
            The kind value
        
        Note:
            Delegates to kind property (CODING_RULE_V2_00017)
        """
        return self.kind  # Delegates to property

    def setKind(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for kind with method chaining.
        
        Args:
            value: The kind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to kind property setter (gets validation automatically)
        """
        self.kind = value  # Delegates to property setter
        return self

    def getNode(self) -> "DiagnosticJ1939Node":
        """
        AUTOSAR-compliant getter for node.
        
        Returns:
            The node value
        
        Note:
            Delegates to node property (CODING_RULE_V2_00017)
        """
        return self.node  # Delegates to property

    def setNode(self, value: "DiagnosticJ1939Node") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for node with method chaining.
        
        Args:
            value: The node to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to node property setter (gets validation automatically)
        """
        self.node = value  # Delegates to property setter
        return self

    def getSpn(self) -> "DiagnosticJ1939Spn":
        """
        AUTOSAR-compliant getter for spn.
        
        Returns:
            The spn value
        
        Note:
            Delegates to spn property (CODING_RULE_V2_00017)
        """
        return self.spn  # Delegates to property

    def setSpn(self, value: "DiagnosticJ1939Spn") -> "DiagnosticTroubleCodeJ1939":
        """
        AUTOSAR-compliant setter for spn with method chaining.
        
        Args:
            value: The spn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to spn property setter (gets validation automatically)
        """
        self.spn = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dtc_props_props(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set dtcPropsProps and return self for chaining.
        
        Args:
            value: The dtcPropsProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dtc_props_props("value")
        """
        self.dtc_props_props = value  # Use property setter (gets validation)
        return self

    def with_fmi(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set fmi and return self for chaining.
        
        Args:
            value: The fmi to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_fmi("value")
        """
        self.fmi = value  # Use property setter (gets validation)
        return self

    def with_kind(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set kind and return self for chaining.
        
        Args:
            value: The kind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_kind("value")
        """
        self.kind = value  # Use property setter (gets validation)
        return self

    def with_node(self, value: Optional["DiagnosticJ1939Node"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set node and return self for chaining.
        
        Args:
            value: The node to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_node("value")
        """
        self.node = value  # Use property setter (gets validation)
        return self

    def with_spn(self, value: Optional["DiagnosticJ1939Spn"]) -> "DiagnosticTroubleCodeJ1939":
        """
        Set spn and return self for chaining.
        
        Args:
            value: The spn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_spn("value")
        """
        self.spn = value  # Use property setter (gets validation)
        return self