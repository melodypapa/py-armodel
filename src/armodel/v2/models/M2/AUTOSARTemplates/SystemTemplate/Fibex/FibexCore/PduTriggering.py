from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class PduTriggering(Identifiable):
    """
    The PduTriggering describes on which channel the IPdu is transmitted. The
    Pdu routing by the PduR is only allowed for subclasses of IPdu. Depending on
    its relation to entities such channels and clusters it can be unambiguously
    deduced whether a fan-out is handled by the Pdu router or the Bus Interface.
    If the fan-out is specified between different clusters it shall be handled
    by the Pdu Router. If the fan-out is specified between different channels of
    the same cluster it shall be handled by the Bus Interface.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::PduTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 303, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 348, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 234, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the Pdu for which the PduTriggering is I-Pdu can be triggered on
                # different channels The Pdu routing by the PduR is only subclasses of IPdu.
        # the reference to the Pdu element the PduTriggering element is also used the
                # sending and receiving connections to Ecu.
        self._iPdu: Optional["Pdu"] = None

    @property
    def i_pdu(self) -> Optional["Pdu"]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional["Pdu"]) -> None:
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

        if not isinstance(value, Pdu):
            raise TypeError(
                f"iPdu must be Pdu or None, got {type(value).__name__}"
            )
        self._iPdu = value
        # References to the IPduPort on every ECU of the system and/or receives the
                # I-PDU.
        # both the sender and the receiver side included when the system is completely
                # defined.
        self._iPduPort: List["IPduPort"] = []

    @property
    def i_pdu_port(self) -> List["IPduPort"]:
        """Get iPduPort (Pythonic accessor)."""
        return self._iPduPort
        # This reference provides the relationship to the ISignal that are implemented
                # by the PduTriggering.
        # is optional since no ISignalTriggering can for DCM and Multiplexed Pdus.
        # atpVariation 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU
                # Configuration R23-11.
        self._iSignal: List[RefType] = []

    @property
    def i_signal(self) -> List[RefType]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal
        # This reference identifies the crypto profile applicable to the usage (send,
        # receive) of the also referenced Secured reference is only applicable if the
        # references a SecuredIPdu in the role i.
        self._secOcCrypto: Optional["SecOcCryptoService"] = None

    @property
    def sec_oc_crypto(self) -> Optional["SecOcCryptoService"]:
        """Get secOcCrypto (Pythonic accessor)."""
        return self._secOcCrypto

    @sec_oc_crypto.setter
    def sec_oc_crypto(self, value: Optional["SecOcCryptoService"]) -> None:
        """
        Set secOcCrypto with validation.
        
        Args:
            value: The secOcCrypto to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secOcCrypto = None
            return

        if not isinstance(value, SecOcCryptoService):
            raise TypeError(
                f"secOcCrypto must be SecOcCryptoService or None, got {type(value).__name__}"
            )
        self._secOcCrypto = value
        # Defines the trigger for the Com_TriggerIPDUSend API call.
        # Only if all defined TriggerIPduSendConditions true (AND associated) the
                # Com_Trigger shall be called.
        self._triggerIPduSend: List[RefType] = []

    @property
    def trigger_i_pdu_send(self) -> List[RefType]:
        """Get triggerIPduSend (Pythonic accessor)."""
        return self._triggerIPduSend

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPdu(self) -> "Pdu":
        """
        AUTOSAR-compliant getter for iPdu.
        
        Returns:
            The iPdu value
        
        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: "Pdu") -> "PduTriggering":
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

    def getIPduPort(self) -> List["IPduPort"]:
        """
        AUTOSAR-compliant getter for iPduPort.
        
        Returns:
            The iPduPort value
        
        Note:
            Delegates to i_pdu_port property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_port  # Delegates to property

    def getISignal(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def getSecOcCrypto(self) -> "SecOcCryptoService":
        """
        AUTOSAR-compliant getter for secOcCrypto.
        
        Returns:
            The secOcCrypto value
        
        Note:
            Delegates to sec_oc_crypto property (CODING_RULE_V2_00017)
        """
        return self.sec_oc_crypto  # Delegates to property

    def setSecOcCrypto(self, value: "SecOcCryptoService") -> "PduTriggering":
        """
        AUTOSAR-compliant setter for secOcCrypto with method chaining.
        
        Args:
            value: The secOcCrypto to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sec_oc_crypto property setter (gets validation automatically)
        """
        self.sec_oc_crypto = value  # Delegates to property setter
        return self

    def getTriggerIPduSend(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for triggerIPduSend.
        
        Returns:
            The triggerIPduSend value
        
        Note:
            Delegates to trigger_i_pdu_send property (CODING_RULE_V2_00017)
        """
        return self.trigger_i_pdu_send  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu(self, value: Optional["Pdu"]) -> "PduTriggering":
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

    def with_sec_oc_crypto(self, value: Optional["SecOcCryptoService"]) -> "PduTriggering":
        """
        Set secOcCrypto and return self for chaining.
        
        Args:
            value: The secOcCrypto to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sec_oc_crypto("value")
        """
        self.sec_oc_crypto = value  # Use property setter (gets validation)
        return self