from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CommunicationCluster,
    EthernetPhysical,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticComControlSpecificChannel(ARObject):
    """
    This represents the ability to add further attributes to the definition of a
    specific channel that is subject to the diagnostic service "communication
    control".

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl::DiagnosticComControlSpecificChannel

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
