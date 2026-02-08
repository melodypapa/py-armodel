from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EthernetCluster(ARObject):
    """
    Ethernet-specific cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 103, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Switch off delay for CouplingPorts in seconds.
        # It denotes delay of switching off couplingPorts after the request off a
                # couplingPort was issued.
        # (e.
        # g.
        # switch off of ports).
        self._couplingPort: Optional["TimeValue"] = None

    @property
    def coupling_port(self) -> Optional["TimeValue"]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort

    @coupling_port.setter
    def coupling_port(self, value: Optional["TimeValue"]) -> None:
        """
        Set couplingPort with validation.

        Args:
            value: The couplingPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingPort = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"couplingPort must be TimeValue or None, got {type(value).__name__}"
            )
        self._couplingPort = value
        # MacMulticastGroup that is defined for the Subnet.
        self._macMulticast: List[RefType] = []

    @property
    def mac_multicast(self) -> List[RefType]:
        """Get macMulticast (Pythonic accessor)."""
        return self._macMulticast

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCouplingPort(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def setCouplingPort(self, value: "TimeValue") -> "EthernetCluster":
        """
        AUTOSAR-compliant setter for couplingPort with method chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_port property setter (gets validation automatically)
        """
        self.coupling_port = value  # Delegates to property setter
        return self

    def getMacMulticast(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for macMulticast.

        Returns:
            The macMulticast value

        Note:
            Delegates to mac_multicast property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_coupling_port(self, value: Optional["TimeValue"]) -> "EthernetCluster":
        """
        Set couplingPort and return self for chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_port("value")
        """
        self.coupling_port = value  # Use property setter (gets validation)
        return self
