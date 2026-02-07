from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class ISignalIPduGroup(FibexElement):
    """
    The AUTOSAR COM Layer is able to start and to stop sending and receiving
    configurable groups of I-Pdus during runtime. An ISignalIPduGroup contains
    either ISignalIPdus or ISignalIPduGroups.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalIPduGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 316, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 350, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the use-case for this ISignalIPdu (e.
        # g.
        # diagnostic, debugging etc.
        # ).
        # For example, in a all IPdus - which are not involved in are disabled.
        # The use cases are not limited to enumeration and can be specified as a
                # string.
        self._communication: Optional["String"] = None

    @property
    def communication(self) -> Optional["String"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["String"]) -> None:
        """
        Set communication with validation.
        
        Args:
            value: The communication to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"communication must be String or None, got {type(value).__name__}"
            )
        self._communication = value
        # An I-Pdu group can be included in other I-Pdu groups.
        # I-Pdu groups shall not be referenced by the.
        self._contained: List[RefType] = []

    @property
    def contained(self) -> List[RefType]:
        """Get contained (Pythonic accessor)."""
        return self._contained
        # Reference to a set of Signal I-Pdus, which are contained ISignal I-Pdu Group.
        # content of a ISignal I-Pdu group can modes).
        # atpVariation.
        self._iSignalIPdu: List["ISignalIPdu"] = []

    @property
    def i_signal_i_pdu(self) -> List["ISignalIPdu"]:
        """Get iSignalIPdu (Pythonic accessor)."""
        return self._iSignalIPdu
        # Reference to a set of NmPdus with NmUserData, which in the ISignalIPduGroup.
        # atpVariation.
        self._nmPdu: List["NmPdu"] = []

    @property
    def nm_pdu(self) -> List["NmPdu"]:
        """Get nmPdu (Pythonic accessor)."""
        return self._nmPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "String":
        """
        AUTOSAR-compliant getter for communication.
        
        Returns:
            The communication value
        
        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "String") -> "ISignalIPduGroup":
        """
        AUTOSAR-compliant setter for communication with method chaining.
        
        Args:
            value: The communication to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getContained(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for contained.
        
        Returns:
            The contained value
        
        Note:
            Delegates to contained property (CODING_RULE_V2_00017)
        """
        return self.contained  # Delegates to property

    def getISignalIPdu(self) -> List["ISignalIPdu"]:
        """
        AUTOSAR-compliant getter for iSignalIPdu.
        
        Returns:
            The iSignalIPdu value
        
        Note:
            Delegates to i_signal_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_i_pdu  # Delegates to property

    def getNmPdu(self) -> List["NmPdu"]:
        """
        AUTOSAR-compliant getter for nmPdu.
        
        Returns:
            The nmPdu value
        
        Note:
            Delegates to nm_pdu property (CODING_RULE_V2_00017)
        """
        return self.nm_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["String"]) -> "ISignalIPduGroup":
        """
        Set communication and return self for chaining.
        
        Args:
            value: The communication to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self