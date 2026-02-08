from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConnection

    RefType,
)


class IEEE1722TpAvConnection(IEEE1722TpConnection, ABC):
    """
    AV IEEE1722Tp connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 639, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpAvConnection:
            raise TypeError("IEEE1722TpAvConnection is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the time offset that is added to the current time at in order to get
        # the "presentation time" (in content shall be presented at the.
        self._maxTransitTime: Optional["TimeValue"] = None

    @property
    def max_transit_time(self) -> Optional["TimeValue"]:
        """Get maxTransitTime (Pythonic accessor)."""
        return self._maxTransitTime

    @max_transit_time.setter
    def max_transit_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxTransitTime with validation.

        Args:
            value: The maxTransitTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxTransitTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxTransitTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxTransitTime = value
        # Reference to the upper layer Sdu used for the transport of of the IEEE1722Tp.
        self._sdu: List[RefType] = []

    @property
    def sdu(self) -> List[RefType]:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxTransitTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxTransitTime.

        Returns:
            The maxTransitTime value

        Note:
            Delegates to max_transit_time property (CODING_RULE_V2_00017)
        """
        return self.max_transit_time  # Delegates to property

    def setMaxTransitTime(self, value: "TimeValue") -> "IEEE1722TpAvConnection":
        """
        AUTOSAR-compliant setter for maxTransitTime with method chaining.

        Args:
            value: The maxTransitTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_transit_time property setter (gets validation automatically)
        """
        self.max_transit_time = value  # Delegates to property setter
        return self

    def getSdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for sdu.

        Returns:
            The sdu value

        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_transit_time(self, value: Optional["TimeValue"]) -> "IEEE1722TpAvConnection":
        """
        Set maxTransitTime and return self for chaining.

        Args:
            value: The maxTransitTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_transit_time("value")
        """
        self.max_transit_time = value  # Use property setter (gets validation)
        return self
