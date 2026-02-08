from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PortPrototype(Identifiable, ABC):
    """
    Base class for the ports of an AUTOSAR software component. The aggregation
    of PortPrototypes is subject to variability with the purpose to support the
    conditional existence of ports.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 326, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 326, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 304, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 62, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 66, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2047, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 236, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (Page 30, Foundation R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 48, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 76, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 458, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 33, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 65, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 201, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PortPrototype:
            raise TypeError("PortPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Annotation of this PortPrototype with respect to client/ communication.
        self._clientServer: List["ClientServerAnnotation"] = []

    @property
    def client_server(self) -> List["ClientServerAnnotation"]:
        """Get clientServer (Pythonic accessor)."""
        return self._clientServer
        # Annotations on this delegated port.
        self._delegatedPort: Optional["DelegatedPort"] = None

    @property
    def delegated_port(self) -> Optional["DelegatedPort"]:
        """Get delegatedPort (Pythonic accessor)."""
        return self._delegatedPort

    @delegated_port.setter
    def delegated_port(self, value: Optional["DelegatedPort"]) -> None:
        """
        Set delegatedPort with validation.

        Args:
            value: The delegatedPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._delegatedPort = None
            return

        if not isinstance(value, DelegatedPort):
            raise TypeError(
                f"delegatedPort must be DelegatedPort or None, got {type(value).__name__}"
            )
        self._delegatedPort = value
        # Annotations on this IO Hardware Abstraction port.
        self._ioHwAbstractionAnnotation: List["IoHwAbstractionServer"] = []

    @property
    def io_hw_abstraction_annotation(self) -> List["IoHwAbstractionServer"]:
        """Get ioHwAbstractionAnnotation (Pythonic accessor)."""
        return self._ioHwAbstractionAnnotation
        # Annotations on this mode port.
        self._modePortAnnotation: List["ModePortAnnotation"] = []

    @property
    def mode_port_annotation(self) -> List["ModePortAnnotation"]:
        """Get modePortAnnotation (Pythonic accessor)."""
        return self._modePortAnnotation
        # Annotations on this non voilatile data port.
        self._nvDataPortAnnotation: List["NvDataPortAnnotation"] = []

    @property
    def nv_data_port_annotation(self) -> List["NvDataPortAnnotation"]:
        """Get nvDataPortAnnotation (Pythonic accessor)."""
        return self._nvDataPortAnnotation
        # Annotations on this parameter port.
        self._parameterPort: List["ParameterPort"] = []

    @property
    def parameter_port(self) -> List["ParameterPort"]:
        """Get parameterPort (Pythonic accessor)."""
        return self._parameterPort
        # Collection of annotations of this ports sender/receiver communication.
        self._senderReceiver: List["SenderReceiver"] = []

    @property
    def sender_receiver(self) -> List["SenderReceiver"]:
        """Get senderReceiver (Pythonic accessor)."""
        return self._senderReceiver
        # Annotations on this trigger port.
        self._triggerPortAnnotation: List[RefType] = []

    @property
    def trigger_port_annotation(self) -> List[RefType]:
        """Get triggerPortAnnotation (Pythonic accessor)."""
        return self._triggerPortAnnotation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientServer(self) -> List["ClientServerAnnotation"]:
        """
        AUTOSAR-compliant getter for clientServer.

        Returns:
            The clientServer value

        Note:
            Delegates to client_server property (CODING_RULE_V2_00017)
        """
        return self.client_server  # Delegates to property

    def getDelegatedPort(self) -> "DelegatedPort":
        """
        AUTOSAR-compliant getter for delegatedPort.

        Returns:
            The delegatedPort value

        Note:
            Delegates to delegated_port property (CODING_RULE_V2_00017)
        """
        return self.delegated_port  # Delegates to property

    def setDelegatedPort(self, value: "DelegatedPort") -> "PortPrototype":
        """
        AUTOSAR-compliant setter for delegatedPort with method chaining.

        Args:
            value: The delegatedPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to delegated_port property setter (gets validation automatically)
        """
        self.delegated_port = value  # Delegates to property setter
        return self

    def getIoHwAbstractionAnnotation(self) -> List["IoHwAbstractionServer"]:
        """
        AUTOSAR-compliant getter for ioHwAbstractionAnnotation.

        Returns:
            The ioHwAbstractionAnnotation value

        Note:
            Delegates to io_hw_abstraction_annotation property (CODING_RULE_V2_00017)
        """
        return self.io_hw_abstraction_annotation  # Delegates to property

    def getModePortAnnotation(self) -> List["ModePortAnnotation"]:
        """
        AUTOSAR-compliant getter for modePortAnnotation.

        Returns:
            The modePortAnnotation value

        Note:
            Delegates to mode_port_annotation property (CODING_RULE_V2_00017)
        """
        return self.mode_port_annotation  # Delegates to property

    def getNvDataPortAnnotation(self) -> List["NvDataPortAnnotation"]:
        """
        AUTOSAR-compliant getter for nvDataPortAnnotation.

        Returns:
            The nvDataPortAnnotation value

        Note:
            Delegates to nv_data_port_annotation property (CODING_RULE_V2_00017)
        """
        return self.nv_data_port_annotation  # Delegates to property

    def getParameterPort(self) -> List["ParameterPort"]:
        """
        AUTOSAR-compliant getter for parameterPort.

        Returns:
            The parameterPort value

        Note:
            Delegates to parameter_port property (CODING_RULE_V2_00017)
        """
        return self.parameter_port  # Delegates to property

    def getSenderReceiver(self) -> List["SenderReceiver"]:
        """
        AUTOSAR-compliant getter for senderReceiver.

        Returns:
            The senderReceiver value

        Note:
            Delegates to sender_receiver property (CODING_RULE_V2_00017)
        """
        return self.sender_receiver  # Delegates to property

    def getTriggerPortAnnotation(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for triggerPortAnnotation.

        Returns:
            The triggerPortAnnotation value

        Note:
            Delegates to trigger_port_annotation property (CODING_RULE_V2_00017)
        """
        return self.trigger_port_annotation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_delegated_port(self, value: Optional["DelegatedPort"]) -> "PortPrototype":
        """
        Set delegatedPort and return self for chaining.

        Args:
            value: The delegatedPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_delegated_port("value")
        """
        self.delegated_port = value  # Use property setter (gets validation)
        return self
