from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CommunicationCluster(ARObject, ABC):
    """
    The CommunicationCluster is the main element to describe the topological
    connection of communicating ECUs. A cluster describes the ensemble of ECUs,
    which are linked by a communication medium of arbitrary topology (bus, star,
    ring, ...). The nodes within the cluster share the same communication
    protocol, which may be event-triggered, time-triggered or a combination of
    both. A CommunicationCluster aggregates one or more physical channels. Tags:
    vh.latestBindingTime=postBuild

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 107, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 57, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationCluster:
            raise TypeError("CommunicationCluster is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Channels speed in bits/s.
        self._baudrate: Optional["PositiveUnlimitedInteger"] = None

    @property
    def baudrate(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get baudrate (Pythonic accessor)."""
        return self._baudrate

    @baudrate.setter
    def baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set baudrate with validation.

        Args:
            value: The baudrate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baudrate = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"baudrate must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._baudrate = value
        # This relationship defines which channel element belongs which cluster.
        # A channel shall be assigned to exactly whereas a cluster may have one or more
                # atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        # atpVariation.
        self._physical: List["PhysicalChannel"] = []

    @property
    def physical(self) -> List["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical
        # The name of the protocol used.
        self._protocolName: Optional["String"] = None

    @property
    def protocol_name(self) -> Optional["String"]:
        """Get protocolName (Pythonic accessor)."""
        return self._protocolName

    @protocol_name.setter
    def protocol_name(self, value: Optional["String"]) -> None:
        """
        Set protocolName with validation.

        Args:
            value: The protocolName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolName = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolName must be String or None, got {type(value).__name__}"
            )
        self._protocolName = value
        # The version of the protocol used.
        self._protocolVersion: Optional["String"] = None

    @property
    def protocol_version(self) -> Optional["String"]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional["String"]) -> None:
        """
        Set protocolVersion with validation.

        Args:
            value: The protocolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolVersion must be String or None, got {type(value).__name__}"
            )
        self._protocolVersion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaudrate(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for baudrate.

        Returns:
            The baudrate value

        Note:
            Delegates to baudrate property (CODING_RULE_V2_00017)
        """
        return self.baudrate  # Delegates to property

    def setBaudrate(self, value: "PositiveUnlimitedInteger") -> "CommunicationCluster":
        """
        AUTOSAR-compliant setter for baudrate with method chaining.

        Args:
            value: The baudrate to set

        Returns:
            self for method chaining

        Note:
            Delegates to baudrate property setter (gets validation automatically)
        """
        self.baudrate = value  # Delegates to property setter
        return self

    def getPhysical(self) -> List["PhysicalChannel"]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def getProtocolName(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolName.

        Returns:
            The protocolName value

        Note:
            Delegates to protocol_name property (CODING_RULE_V2_00017)
        """
        return self.protocol_name  # Delegates to property

    def setProtocolName(self, value: "String") -> "CommunicationCluster":
        """
        AUTOSAR-compliant setter for protocolName with method chaining.

        Args:
            value: The protocolName to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_name property setter (gets validation automatically)
        """
        self.protocol_name = value  # Delegates to property setter
        return self

    def getProtocolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolVersion.

        Returns:
            The protocolVersion value

        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: "String") -> "CommunicationCluster":
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> "CommunicationCluster":
        """
        Set baudrate and return self for chaining.

        Args:
            value: The baudrate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_baudrate("value")
        """
        self.baudrate = value  # Use property setter (gets validation)
        return self

    def with_protocol_name(self, value: Optional["String"]) -> "CommunicationCluster":
        """
        Set protocolName and return self for chaining.

        Args:
            value: The protocolName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_name("value")
        """
        self.protocol_name = value  # Use property setter (gets validation)
        return self

    def with_protocol_version(self, value: Optional["String"]) -> "CommunicationCluster":
        """
        Set protocolVersion and return self for chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self
