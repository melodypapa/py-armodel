from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class CommunicationConnector(Identifiable, ABC):
    """
    The connection between the referencing ECU and the referenced channel via
    the referenced controller. Connectors are used to describe the bus
    interfaces of the ECUs and to specify the sending/receiving behavior. Each
    CommunicationConnector has a reference to exactly one
    communicationController. Note: Several CommunicationConnectors can be
    assigned to one PhysicalChannel in the scope of one ECU Instance.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology::CommunicationConnector
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 54, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 57, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationConnector:
            raise TypeError("CommunicationConnector is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the communication controller.
        # The and referenced be aggregated by the can be referenced by elements.
        # This is the FlexRay Bus.
        # FlexRay communicates physical channels.
        # But only one controller in an responsible for both channels.
        # Thus, two channel A and for channel B) shall the same controller.
        self._commController: Optional["Communication"] = None

    @property
    def comm_controller(self) -> Optional["Communication"]:
        """Get commController (Pythonic accessor)."""
        return self._commController

    @comm_controller.setter
    def comm_controller(self, value: Optional["Communication"]) -> None:
        """
        Set commController with validation.
        
        Args:
            value: The commController to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._commController = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"commController must be Communication or None, got {type(value).__name__}"
            )
        self._commController = value
        # If this parameter is available and set to true then a wakeup source shall be
        # created for the Physical this CommunicationConnector.
        self._createEcu: Optional["Boolean"] = None

    @property
    def create_ecu(self) -> Optional["Boolean"]:
        """Get createEcu (Pythonic accessor)."""
        return self._createEcu

    @create_ecu.setter
    def create_ecu(self, value: Optional["Boolean"]) -> None:
        """
        Set createEcu with validation.
        
        Args:
            value: The createEcu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._createEcu = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"createEcu must be Boolean or None, got {type(value).__name__}"
            )
        self._createEcu = value
        # Defines if this EcuInstance shall implement the dynamic functionality on this
        # and its respective Physical.
        self._dynamicPncTo: Optional["Boolean"] = None

    @property
    def dynamic_pnc_to(self) -> Optional["Boolean"]:
        """Get dynamicPncTo (Pythonic accessor)."""
        return self._dynamicPncTo

    @dynamic_pnc_to.setter
    def dynamic_pnc_to(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamicPncTo with validation.
        
        Args:
            value: The dynamicPncTo to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicPncTo = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"dynamicPncTo must be Boolean or None, got {type(value).__name__}"
            )
        self._dynamicPncTo = value
        # An ECUs reception or send ports.
        # If signals/PDUs/frames are variable, the shall be variable, too.
        # atpVariation.
        self._ecuCommPort: List["CommConnectorPort"] = []

    @property
    def ecu_comm_port(self) -> List["CommConnectorPort"]:
        """Get ecuCommPort (Pythonic accessor)."""
        return self._ecuCommPort
        # Bit mask for NM-Pdu Payload used to configure the NM filter mask for the
        # Network Management.
        self._pncFilterArray: List["PositiveInteger"] = []

    @property
    def pnc_filter_array(self) -> List["PositiveInteger"]:
        """Get pncFilterArray (Pythonic accessor)."""
        return self._pncFilterArray
        # Defines if this EcuInstance shall implement the Pnc functionality on this
                # CommunicationConnector respective PhysicalChannel.
        # Several Ecu the same PhysicalChannel can have the enabled, but only one of
                # them the pncGatewayType "active".
        self._pncGateway: Optional["PncGatewayTypeEnum"] = None

    @property
    def pnc_gateway(self) -> Optional["PncGatewayTypeEnum"]:
        """Get pncGateway (Pythonic accessor)."""
        return self._pncGateway

    @pnc_gateway.setter
    def pnc_gateway(self, value: Optional["PncGatewayTypeEnum"]) -> None:
        """
        Set pncGateway with validation.
        
        Args:
            value: The pncGateway to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncGateway = None
            return

        if not isinstance(value, PncGatewayTypeEnum):
            raise TypeError(
                f"pncGateway must be PncGatewayTypeEnum or None, got {type(value).__name__}"
            )
        self._pncGateway = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommController(self) -> "Communication":
        """
        AUTOSAR-compliant getter for commController.
        
        Returns:
            The commController value
        
        Note:
            Delegates to comm_controller property (CODING_RULE_V2_00017)
        """
        return self.comm_controller  # Delegates to property

    def setCommController(self, value: "Communication") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for commController with method chaining.
        
        Args:
            value: The commController to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to comm_controller property setter (gets validation automatically)
        """
        self.comm_controller = value  # Delegates to property setter
        return self

    def getCreateEcu(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for createEcu.
        
        Returns:
            The createEcu value
        
        Note:
            Delegates to create_ecu property (CODING_RULE_V2_00017)
        """
        return self.create_ecu  # Delegates to property

    def setCreateEcu(self, value: "Boolean") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for createEcu with method chaining.
        
        Args:
            value: The createEcu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to create_ecu property setter (gets validation automatically)
        """
        self.create_ecu = value  # Delegates to property setter
        return self

    def getDynamicPncTo(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamicPncTo.
        
        Returns:
            The dynamicPncTo value
        
        Note:
            Delegates to dynamic_pnc_to property (CODING_RULE_V2_00017)
        """
        return self.dynamic_pnc_to  # Delegates to property

    def setDynamicPncTo(self, value: "Boolean") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for dynamicPncTo with method chaining.
        
        Args:
            value: The dynamicPncTo to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dynamic_pnc_to property setter (gets validation automatically)
        """
        self.dynamic_pnc_to = value  # Delegates to property setter
        return self

    def getEcuCommPort(self) -> List["CommConnectorPort"]:
        """
        AUTOSAR-compliant getter for ecuCommPort.
        
        Returns:
            The ecuCommPort value
        
        Note:
            Delegates to ecu_comm_port property (CODING_RULE_V2_00017)
        """
        return self.ecu_comm_port  # Delegates to property

    def getPncFilterArray(self) -> List["PositiveInteger"]:
        """
        AUTOSAR-compliant getter for pncFilterArray.
        
        Returns:
            The pncFilterArray value
        
        Note:
            Delegates to pnc_filter_array property (CODING_RULE_V2_00017)
        """
        return self.pnc_filter_array  # Delegates to property

    def getPncGateway(self) -> "PncGatewayTypeEnum":
        """
        AUTOSAR-compliant getter for pncGateway.
        
        Returns:
            The pncGateway value
        
        Note:
            Delegates to pnc_gateway property (CODING_RULE_V2_00017)
        """
        return self.pnc_gateway  # Delegates to property

    def setPncGateway(self, value: "PncGatewayTypeEnum") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for pncGateway with method chaining.
        
        Args:
            value: The pncGateway to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pnc_gateway property setter (gets validation automatically)
        """
        self.pnc_gateway = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_comm_controller(self, value: Optional["Communication"]) -> "CommunicationConnector":
        """
        Set commController and return self for chaining.
        
        Args:
            value: The commController to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_comm_controller("value")
        """
        self.comm_controller = value  # Use property setter (gets validation)
        return self

    def with_create_ecu(self, value: Optional["Boolean"]) -> "CommunicationConnector":
        """
        Set createEcu and return self for chaining.
        
        Args:
            value: The createEcu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_create_ecu("value")
        """
        self.create_ecu = value  # Use property setter (gets validation)
        return self

    def with_dynamic_pnc_to(self, value: Optional["Boolean"]) -> "CommunicationConnector":
        """
        Set dynamicPncTo and return self for chaining.
        
        Args:
            value: The dynamicPncTo to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dynamic_pnc_to("value")
        """
        self.dynamic_pnc_to = value  # Use property setter (gets validation)
        return self

    def with_pnc_gateway(self, value: Optional["PncGatewayTypeEnum"]) -> "CommunicationConnector":
        """
        Set pncGateway and return self for chaining.
        
        Args:
            value: The pncGateway to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pnc_gateway("value")
        """
        self.pnc_gateway = value  # Use property setter (gets validation)
        return self