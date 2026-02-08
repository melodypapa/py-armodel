from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DoIpEntity,
    TimeSynchronization,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class InfrastructureServices(ARObject):
    """
    Defines the network infrastructure services provided or consumed.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::InfrastructureServices

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 469, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether a infrastructure service that runs on the is a DoIP-Entity.
        self._doIpEntity: Optional["DoIpEntity"] = None

    @property
    def do_ip_entity(self) -> Optional["DoIpEntity"]:
        """Get doIpEntity (Pythonic accessor)."""
        return self._doIpEntity

    @do_ip_entity.setter
    def do_ip_entity(self, value: Optional["DoIpEntity"]) -> None:
        """
        Set doIpEntity with validation.

        Args:
            value: The doIpEntity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpEntity = None
            return

        if not isinstance(value, DoIpEntity):
            raise TypeError(
                f"doIpEntity must be DoIpEntity or None, got {type(value).__name__}"
            )
        self._doIpEntity = value
        # Defines the servers / clients in a time synchronised.
        self._time: Optional["TimeSynchronization"] = None

    @property
    def time(self) -> Optional["TimeSynchronization"]:
        """Get time (Pythonic accessor)."""
        return self._time

    @time.setter
    def time(self, value: Optional["TimeSynchronization"]) -> None:
        """
        Set time with validation.

        Args:
            value: The time to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._time = None
            return

        if not isinstance(value, TimeSynchronization):
            raise TypeError(
                f"time must be TimeSynchronization or None, got {type(value).__name__}"
            )
        self._time = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpEntity(self) -> "DoIpEntity":
        """
        AUTOSAR-compliant getter for doIpEntity.

        Returns:
            The doIpEntity value

        Note:
            Delegates to do_ip_entity property (CODING_RULE_V2_00017)
        """
        return self.do_ip_entity  # Delegates to property

    def setDoIpEntity(self, value: "DoIpEntity") -> "InfrastructureServices":
        """
        AUTOSAR-compliant setter for doIpEntity with method chaining.

        Args:
            value: The doIpEntity to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_entity property setter (gets validation automatically)
        """
        self.do_ip_entity = value  # Delegates to property setter
        return self

    def getTime(self) -> "TimeSynchronization":
        """
        AUTOSAR-compliant getter for time.

        Returns:
            The time value

        Note:
            Delegates to time property (CODING_RULE_V2_00017)
        """
        return self.time  # Delegates to property

    def setTime(self, value: "TimeSynchronization") -> "InfrastructureServices":
        """
        AUTOSAR-compliant setter for time with method chaining.

        Args:
            value: The time to set

        Returns:
            self for method chaining

        Note:
            Delegates to time property setter (gets validation automatically)
        """
        self.time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_do_ip_entity(self, value: Optional["DoIpEntity"]) -> "InfrastructureServices":
        """
        Set doIpEntity and return self for chaining.

        Args:
            value: The doIpEntity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_entity("value")
        """
        self.do_ip_entity = value  # Use property setter (gets validation)
        return self

    def with_time(self, value: Optional["TimeSynchronization"]) -> "InfrastructureServices":
        """
        Set time and return self for chaining.

        Args:
            value: The time to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time("value")
        """
        self.time = value  # Use property setter (gets validation)
        return self
