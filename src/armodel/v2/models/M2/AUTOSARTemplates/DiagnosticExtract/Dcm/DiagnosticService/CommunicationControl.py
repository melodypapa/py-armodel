from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)


class DiagnosticComControl(DiagnosticServiceInstance):
    """
    This represents an instance of the "Communication Control" diagnostic
    service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 108, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticComControl in the.
        self._comControl: Optional["DiagnosticComControl"] = None

    @property
    def com_control(self) -> Optional["DiagnosticComControl"]:
        """Get comControl (Pythonic accessor)."""
        return self._comControl

    @com_control.setter
    def com_control(self, value: Optional["DiagnosticComControl"]) -> None:
        """
        Set comControl with validation.

        Args:
            value: The comControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._comControl = None
            return

        if not isinstance(value, DiagnosticComControl):
            raise TypeError(
                f"comControl must be DiagnosticComControl or None, got {type(value).__name__}"
            )
        self._comControl = value
        # This attribute shall be used to define a custom number if none of the
        # standardized values of shall be used.
        self._customSub: Optional["PositiveInteger"] = None

    @property
    def custom_sub(self) -> Optional["PositiveInteger"]:
        """Get customSub (Pythonic accessor)."""
        return self._customSub

    @custom_sub.setter
    def custom_sub(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set customSub with validation.

        Args:
            value: The customSub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customSub = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"customSub must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._customSub = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComControl(self) -> "DiagnosticComControl":
        """
        AUTOSAR-compliant getter for comControl.

        Returns:
            The comControl value

        Note:
            Delegates to com_control property (CODING_RULE_V2_00017)
        """
        return self.com_control  # Delegates to property

    def setComControl(self, value: "DiagnosticComControl") -> "DiagnosticComControl":
        """
        AUTOSAR-compliant setter for comControl with method chaining.

        Args:
            value: The comControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to com_control property setter (gets validation automatically)
        """
        self.com_control = value  # Delegates to property setter
        return self

    def getCustomSub(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for customSub.

        Returns:
            The customSub value

        Note:
            Delegates to custom_sub property (CODING_RULE_V2_00017)
        """
        return self.custom_sub  # Delegates to property

    def setCustomSub(self, value: "PositiveInteger") -> "DiagnosticComControl":
        """
        AUTOSAR-compliant setter for customSub with method chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom_sub property setter (gets validation automatically)
        """
        self.custom_sub = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_com_control(self, value: Optional["DiagnosticComControl"]) -> "DiagnosticComControl":
        """
        Set comControl and return self for chaining.

        Args:
            value: The comControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com_control("value")
        """
        self.com_control = value  # Use property setter (gets validation)
        return self

    def with_custom_sub(self, value: Optional["PositiveInteger"]) -> "DiagnosticComControl":
        """
        Set customSub and return self for chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_sub("value")
        """
        self.custom_sub = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticComControlSpecificChannel(ARObject):
    """
    This represents the ability to add further attributes to the definition of a
    specific channel that is subject to the diagnostic service "communication
    control".

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 109, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the affected CommunicationCluster in the.
        self._specificChannel: Optional["CommunicationCluster"] = None

    @property
    def specific_channel(self) -> Optional["CommunicationCluster"]:
        """Get specificChannel (Pythonic accessor)."""
        return self._specificChannel

    @specific_channel.setter
    def specific_channel(self, value: Optional["CommunicationCluster"]) -> None:
        """
        Set specificChannel with validation.

        Args:
            value: The specificChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._specificChannel = None
            return

        if not isinstance(value, CommunicationCluster):
            raise TypeError(
                f"specificChannel must be CommunicationCluster or None, got {type(value).__name__}"
            )
        self._specificChannel = value
        # This represents the affected specific EthernetPhysical Channel.
        self._specificPhysical: Optional["EthernetPhysical"] = None

    @property
    def specific_physical(self) -> Optional["EthernetPhysical"]:
        """Get specificPhysical (Pythonic accessor)."""
        return self._specificPhysical

    @specific_physical.setter
    def specific_physical(self, value: Optional["EthernetPhysical"]) -> None:
        """
        Set specificPhysical with validation.

        Args:
            value: The specificPhysical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._specificPhysical = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"specificPhysical must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._specificPhysical = value
        # This represents the applicable subnet number (which is number ranging from 1.
        # 14).
        self._subnetNumber: Optional["PositiveInteger"] = None

    @property
    def subnet_number(self) -> Optional["PositiveInteger"]:
        """Get subnetNumber (Pythonic accessor)."""
        return self._subnetNumber

    @subnet_number.setter
    def subnet_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set subnetNumber with validation.

        Args:
            value: The subnetNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subnetNumber = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"subnetNumber must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._subnetNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSpecificChannel(self) -> "CommunicationCluster":
        """
        AUTOSAR-compliant getter for specificChannel.

        Returns:
            The specificChannel value

        Note:
            Delegates to specific_channel property (CODING_RULE_V2_00017)
        """
        return self.specific_channel  # Delegates to property

    def setSpecificChannel(self, value: "CommunicationCluster") -> "DiagnosticComControlSpecificChannel":
        """
        AUTOSAR-compliant setter for specificChannel with method chaining.

        Args:
            value: The specificChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to specific_channel property setter (gets validation automatically)
        """
        self.specific_channel = value  # Delegates to property setter
        return self

    def getSpecificPhysical(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for specificPhysical.

        Returns:
            The specificPhysical value

        Note:
            Delegates to specific_physical property (CODING_RULE_V2_00017)
        """
        return self.specific_physical  # Delegates to property

    def setSpecificPhysical(self, value: "EthernetPhysical") -> "DiagnosticComControlSpecificChannel":
        """
        AUTOSAR-compliant setter for specificPhysical with method chaining.

        Args:
            value: The specificPhysical to set

        Returns:
            self for method chaining

        Note:
            Delegates to specific_physical property setter (gets validation automatically)
        """
        self.specific_physical = value  # Delegates to property setter
        return self

    def getSubnetNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for subnetNumber.

        Returns:
            The subnetNumber value

        Note:
            Delegates to subnet_number property (CODING_RULE_V2_00017)
        """
        return self.subnet_number  # Delegates to property

    def setSubnetNumber(self, value: "PositiveInteger") -> "DiagnosticComControlSpecificChannel":
        """
        AUTOSAR-compliant setter for subnetNumber with method chaining.

        Args:
            value: The subnetNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to subnet_number property setter (gets validation automatically)
        """
        self.subnet_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_specific_channel(self, value: Optional["CommunicationCluster"]) -> "DiagnosticComControlSpecificChannel":
        """
        Set specificChannel and return self for chaining.

        Args:
            value: The specificChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_specific_channel("value")
        """
        self.specific_channel = value  # Use property setter (gets validation)
        return self

    def with_specific_physical(self, value: Optional["EthernetPhysical"]) -> "DiagnosticComControlSpecificChannel":
        """
        Set specificPhysical and return self for chaining.

        Args:
            value: The specificPhysical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_specific_physical("value")
        """
        self.specific_physical = value  # Use property setter (gets validation)
        return self

    def with_subnet_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticComControlSpecificChannel":
        """
        Set subnetNumber and return self for chaining.

        Args:
            value: The subnetNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_subnet_number("value")
        """
        self.subnet_number = value  # Use property setter (gets validation)
        return self

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the
    "Communication Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 109, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the semantics that all available be affected.
        # It is still necessary to refer to because there could CommunicationClusters
                # in the System Extract not subject to the service "communication to the
                # applicable CommunicationClusters it made sure that only the affected
                # Communication accessed.
        self._allChannels: List["CommunicationCluster"] = []

    @property
    def all_channels(self) -> List["CommunicationCluster"]:
        """Get allChannels (Pythonic accessor)."""
        return self._allChannels
        # This reference represents the semantics that all available channels shall be
                # affected.
        # It is still necessary to refer to because there could VLANs (and thus private
                # EthernetPhysical the System Extract that are not subject to "communication
                # control".
        # to the applicable EthernetPhysicalChannels it made sure that only the
                # affected EthernetPhysical accessed.
        self._allPhysical: List["EthernetPhysical"] = []

    @property
    def all_physical(self) -> List["EthernetPhysical"]:
        """Get allPhysical (Pythonic accessor)."""
        return self._allPhysical
        # This represents the ability to add additional attributes to case that only
        # specific channels are supposed to be.
        self._specificChannel: List["DiagnosticComControl"] = []

    @property
    def specific_channel(self) -> List["DiagnosticComControl"]:
        """Get specificChannel (Pythonic accessor)."""
        return self._specificChannel
        # This attribute represents the ability to add further attributes to the
        # definition of a specific sub-node channel subject to the diagnostic service
        # "communication.
        self._subNode: List["DiagnosticComControl"] = []

    @property
    def sub_node(self) -> List["DiagnosticComControl"]:
        """Get subNode (Pythonic accessor)."""
        return self._subNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllChannels(self) -> List["CommunicationCluster"]:
        """
        AUTOSAR-compliant getter for allChannels.

        Returns:
            The allChannels value

        Note:
            Delegates to all_channels property (CODING_RULE_V2_00017)
        """
        return self.all_channels  # Delegates to property

    def getAllPhysical(self) -> List["EthernetPhysical"]:
        """
        AUTOSAR-compliant getter for allPhysical.

        Returns:
            The allPhysical value

        Note:
            Delegates to all_physical property (CODING_RULE_V2_00017)
        """
        return self.all_physical  # Delegates to property

    def getSpecificChannel(self) -> List["DiagnosticComControl"]:
        """
        AUTOSAR-compliant getter for specificChannel.

        Returns:
            The specificChannel value

        Note:
            Delegates to specific_channel property (CODING_RULE_V2_00017)
        """
        return self.specific_channel  # Delegates to property

    def getSubNode(self) -> List["DiagnosticComControl"]:
        """
        AUTOSAR-compliant getter for subNode.

        Returns:
            The subNode value

        Note:
            Delegates to sub_node property (CODING_RULE_V2_00017)
        """
        return self.sub_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticComControlSubNodeChannel(ARObject):
    """
    This represents the ability to add further attributes to the definition of a
    specific sub-node channel that is subject to the diagnostic service
    "communication control".

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 110, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the affected sub-node EthernetPhysical Channel.
        self._subNode: Optional["EthernetPhysical"] = None

    @property
    def sub_node(self) -> Optional["EthernetPhysical"]:
        """Get subNode (Pythonic accessor)."""
        return self._subNode

    @sub_node.setter
    def sub_node(self, value: Optional["EthernetPhysical"]) -> None:
        """
        Set subNode with validation.

        Args:
            value: The subNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subNode = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"subNode must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._subNode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSubNode(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for subNode.

        Returns:
            The subNode value

        Note:
            Delegates to sub_node property (CODING_RULE_V2_00017)
        """
        return self.sub_node  # Delegates to property

    def setSubNode(self, value: "EthernetPhysical") -> "DiagnosticComControlSubNodeChannel":
        """
        AUTOSAR-compliant setter for subNode with method chaining.

        Args:
            value: The subNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub_node property setter (gets validation automatically)
        """
        self.sub_node = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sub_node(self, value: Optional["EthernetPhysical"]) -> "DiagnosticComControlSubNodeChannel":
        """
        Set subNode and return self for chaining.

        Args:
            value: The subNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_node("value")
        """
        self.sub_node = value  # Use property setter (gets validation)
        return self
