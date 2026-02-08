from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

    RefType,
)


class Gateway(FibexElement):
    """
    A gateway is an ECU that is connected to two or more clusters (channels, but
    not redundant), and performs a frame, Pdu or signal mapping between them.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::Gateway

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 837, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to one ECU instance that implements the.
        self._ecu: Optional["EcuInstance"] = None

    @property
    def ecu(self) -> Optional["EcuInstance"]:
        """Get ecu (Pythonic accessor)."""
        return self._ecu

    @ecu.setter
    def ecu(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecu with validation.

        Args:
            value: The ecu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecu = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecu must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecu = value
        # Frame Gateway: The entire source frame is mapped as it the target frame (what
                # in general is only possible a common platform).
        # In this case source and should be the identical object.
        # frames are variable in clusters, the mapping needs to be variable, too.
        # atpVariation.
        self._frameMapping: List[RefType] = []

    @property
    def frame_mapping(self) -> List[RefType]:
        """Get frameMapping (Pythonic accessor)."""
        return self._frameMapping
        # IPdu Gateway: Arranges those IPdus that are transferred gateway from one
                # channel to the other in pairs and mapping between them.
        # PDUs are variable in clusters, the gateway needs to be variable, too.
        # atpVariation.
        self._iPduMapping: List[RefType] = []

    @property
    def i_pdu_mapping(self) -> List[RefType]:
        """Get iPduMapping (Pythonic accessor)."""
        return self._iPduMapping
        # Signal Gateway: Arranges those signals that are the gateway from one channel
                # to the other and defines the mapping between them.
        # signals are variable in clusters, the mapping needs to be variable, too.
        # atpVariation.
        self._signalMapping: List[RefType] = []

    @property
    def signal_mapping(self) -> List[RefType]:
        """Get signalMapping (Pythonic accessor)."""
        return self._signalMapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcu(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecu.

        Returns:
            The ecu value

        Note:
            Delegates to ecu property (CODING_RULE_V2_00017)
        """
        return self.ecu  # Delegates to property

    def setEcu(self, value: "EcuInstance") -> "Gateway":
        """
        AUTOSAR-compliant setter for ecu with method chaining.

        Args:
            value: The ecu to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu property setter (gets validation automatically)
        """
        self.ecu = value  # Delegates to property setter
        return self

    def getFrameMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for frameMapping.

        Returns:
            The frameMapping value

        Note:
            Delegates to frame_mapping property (CODING_RULE_V2_00017)
        """
        return self.frame_mapping  # Delegates to property

    def getIPduMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for iPduMapping.

        Returns:
            The iPduMapping value

        Note:
            Delegates to i_pdu_mapping property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_mapping  # Delegates to property

    def getSignalMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for signalMapping.

        Returns:
            The signalMapping value

        Note:
            Delegates to signal_mapping property (CODING_RULE_V2_00017)
        """
        return self.signal_mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu(self, value: Optional["EcuInstance"]) -> "Gateway":
        """
        Set ecu and return self for chaining.

        Args:
            value: The ecu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu("value")
        """
        self.ecu = value  # Use property setter (gets validation)
        return self
