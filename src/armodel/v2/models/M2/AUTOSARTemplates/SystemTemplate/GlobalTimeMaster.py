from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class GlobalTimeMaster(Identifiable, ABC):
    """
    This represents the generic concept of a global time master.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::GlobalTimeMaster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 860, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is GlobalTimeMaster:
            raise TypeError("GlobalTimeMaster is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The GlobalTimeMaster is bound to the Communication Connector.
        self._communication: Optional["Communication"] = None

    @property
    def communication(self) -> Optional["Communication"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["Communication"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"communication must be Communication or None, got {type(value).__name__}"
            )
        self._communication = value
        # Defines whether an Integrity Check Value (ICV) shall be to the sent time sync
        # messages.
        self._icvSecured: Optional["GlobalTimeIcvSupport"] = None

    @property
    def icv_secured(self) -> Optional["GlobalTimeIcvSupport"]:
        """Get icvSecured (Pythonic accessor)."""
        return self._icvSecured

    @icv_secured.setter
    def icv_secured(self, value: Optional["GlobalTimeIcvSupport"]) -> None:
        """
        Set icvSecured with validation.

        Args:
            value: The icvSecured to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icvSecured = None
            return

        if not isinstance(value, GlobalTimeIcvSupport):
            raise TypeError(
                f"icvSecured must be GlobalTimeIcvSupport or None, got {type(value).__name__}"
            )
        self._icvSecured = value
        # Defines the minimum time between an "immediate" and the next periodic
        # message.
        self._immediate: Optional["TimeValue"] = None

    @property
    def immediate(self) -> Optional["TimeValue"]:
        """Get immediate (Pythonic accessor)."""
        return self._immediate

    @immediate.setter
    def immediate(self, value: Optional["TimeValue"]) -> None:
        """
        Set immediate with validation.

        Args:
            value: The immediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._immediate = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"immediate must be TimeValue or None, got {type(value).__name__}"
            )
        self._immediate = value
        # If set to TRUE, the GlobalTimeMaster is supposed to act the root of global
        # time information.
        self._isSystemWide: Optional["Boolean"] = None

    @property
    def is_system_wide(self) -> Optional["Boolean"]:
        """Get isSystemWide (Pythonic accessor)."""
        return self._isSystemWide

    @is_system_wide.setter
    def is_system_wide(self, value: Optional["Boolean"]) -> None:
        """
        Set isSystemWide with validation.

        Args:
            value: The isSystemWide to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isSystemWide = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isSystemWide must be Boolean or None, got {type(value).__name__}"
            )
        self._isSystemWide = value
        # This represents the period.
        # Unit: seconds.
        self._syncPeriod: Optional["TimeValue"] = None

    @property
    def sync_period(self) -> Optional["TimeValue"]:
        """Get syncPeriod (Pythonic accessor)."""
        return self._syncPeriod

    @sync_period.setter
    def sync_period(self, value: Optional["TimeValue"]) -> None:
        """
        Set syncPeriod with validation.

        Args:
            value: The syncPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncPeriod = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"syncPeriod must be TimeValue or None, got {type(value).__name__}"
            )
        self._syncPeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "Communication":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "Communication") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getIcvSecured(self) -> "GlobalTimeIcvSupport":
        """
        AUTOSAR-compliant getter for icvSecured.

        Returns:
            The icvSecured value

        Note:
            Delegates to icv_secured property (CODING_RULE_V2_00017)
        """
        return self.icv_secured  # Delegates to property

    def setIcvSecured(self, value: "GlobalTimeIcvSupport") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for icvSecured with method chaining.

        Args:
            value: The icvSecured to set

        Returns:
            self for method chaining

        Note:
            Delegates to icv_secured property setter (gets validation automatically)
        """
        self.icv_secured = value  # Delegates to property setter
        return self

    def getImmediate(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for immediate.

        Returns:
            The immediate value

        Note:
            Delegates to immediate property (CODING_RULE_V2_00017)
        """
        return self.immediate  # Delegates to property

    def setImmediate(self, value: "TimeValue") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for immediate with method chaining.

        Args:
            value: The immediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to immediate property setter (gets validation automatically)
        """
        self.immediate = value  # Delegates to property setter
        return self

    def getIsSystemWide(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isSystemWide.

        Returns:
            The isSystemWide value

        Note:
            Delegates to is_system_wide property (CODING_RULE_V2_00017)
        """
        return self.is_system_wide  # Delegates to property

    def setIsSystemWide(self, value: "Boolean") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for isSystemWide with method chaining.

        Args:
            value: The isSystemWide to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_system_wide property setter (gets validation automatically)
        """
        self.is_system_wide = value  # Delegates to property setter
        return self

    def getSyncPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for syncPeriod.

        Returns:
            The syncPeriod value

        Note:
            Delegates to sync_period property (CODING_RULE_V2_00017)
        """
        return self.sync_period  # Delegates to property

    def setSyncPeriod(self, value: "TimeValue") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for syncPeriod with method chaining.

        Args:
            value: The syncPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_period property setter (gets validation automatically)
        """
        self.sync_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["Communication"]) -> "GlobalTimeMaster":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

    def with_icv_secured(self, value: Optional["GlobalTimeIcvSupport"]) -> "GlobalTimeMaster":
        """
        Set icvSecured and return self for chaining.

        Args:
            value: The icvSecured to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_icv_secured("value")
        """
        self.icv_secured = value  # Use property setter (gets validation)
        return self

    def with_immediate(self, value: Optional["TimeValue"]) -> "GlobalTimeMaster":
        """
        Set immediate and return self for chaining.

        Args:
            value: The immediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_immediate("value")
        """
        self.immediate = value  # Use property setter (gets validation)
        return self

    def with_is_system_wide(self, value: Optional["Boolean"]) -> "GlobalTimeMaster":
        """
        Set isSystemWide and return self for chaining.

        Args:
            value: The isSystemWide to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_system_wide("value")
        """
        self.is_system_wide = value  # Use property setter (gets validation)
        return self

    def with_sync_period(self, value: Optional["TimeValue"]) -> "GlobalTimeMaster":
        """
        Set syncPeriod and return self for chaining.

        Args:
            value: The syncPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_period("value")
        """
        self.sync_period = value  # Use property setter (gets validation)
        return self
