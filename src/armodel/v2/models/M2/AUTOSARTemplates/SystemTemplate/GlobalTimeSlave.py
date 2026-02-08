from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class GlobalTimeSlave(Identifiable, ABC):
    """
    This represents the generic concept of a global time slave.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 860, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is GlobalTimeSlave:
            raise TypeError("GlobalTimeSlave is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The GlobalTimeSlave is bound to the Communication Connector.
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
        # Rx timeout for the follow-up message.
        self._followUpTimeoutValue: Optional["TimeValue"] = None

    @property
    def follow_up_timeout_value(self) -> Optional["TimeValue"]:
        """Get followUpTimeoutValue (Pythonic accessor)."""
        return self._followUpTimeoutValue

    @follow_up_timeout_value.setter
    def follow_up_timeout_value(self, value: Optional["TimeValue"]) -> None:
        """
        Set followUpTimeoutValue with validation.

        Args:
            value: The followUpTimeoutValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._followUpTimeoutValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"followUpTimeoutValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._followUpTimeoutValue = value
        # Defines how an Integrity Check Value (ICV) shall be at the receiver.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._icvVerification: Optional["GlobalTimeIcv"] = None

    @property
    def icv_verification(self) -> Optional["GlobalTimeIcv"]:
        """Get icvVerification (Pythonic accessor)."""
        return self._icvVerification

    @icv_verification.setter
    def icv_verification(self, value: Optional["GlobalTimeIcv"]) -> None:
        """
        Set icvVerification with validation.

        Args:
            value: The icvVerification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icvVerification = None
            return

        if not isinstance(value, GlobalTimeIcv):
            raise TypeError(
                f"icvVerification must be GlobalTimeIcv or None, got {type(value).__name__}"
            )
        self._icvVerification = value
        # Defines the maximum allowed positive difference the current Local Time Base
        # value and a newly Time Base value.
        self._timeLeapFuture: Optional["TimeValue"] = None

    @property
    def time_leap_future(self) -> Optional["TimeValue"]:
        """Get timeLeapFuture (Pythonic accessor)."""
        return self._timeLeapFuture

    @time_leap_future.setter
    def time_leap_future(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeLeapFuture with validation.

        Args:
            value: The timeLeapFuture to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeLeapFuture = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeLeapFuture must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeLeapFuture = value
        # Defines the required number of updates to the Time Base the time difference
        # to the previous received value remain within the bounds of timeLeapFuture
        # timeLeapPastThreshold until that Time.
        self._timeLeap: Optional["PositiveInteger"] = None

    @property
    def time_leap(self) -> Optional["PositiveInteger"]:
        """Get timeLeap (Pythonic accessor)."""
        return self._timeLeap

    @time_leap.setter
    def time_leap(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set timeLeap with validation.

        Args:
            value: The timeLeap to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeLeap = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"timeLeap must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._timeLeap = value
        # Defines the maximum allowed negative difference the current Local Time Base
        # value and a newly Time Base value.
        self._timeLeapPast: Optional["TimeValue"] = None

    @property
    def time_leap_past(self) -> Optional["TimeValue"]:
        """Get timeLeapPast (Pythonic accessor)."""
        return self._timeLeapPast

    @time_leap_past.setter
    def time_leap_past(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeLeapPast with validation.

        Args:
            value: The timeLeapPast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeLeapPast = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeLeapPast must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeLeapPast = value

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

    def setCommunication(self, value: "Communication") -> "GlobalTimeSlave":
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

    def getFollowUpTimeoutValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for followUpTimeoutValue.

        Returns:
            The followUpTimeoutValue value

        Note:
            Delegates to follow_up_timeout_value property (CODING_RULE_V2_00017)
        """
        return self.follow_up_timeout_value  # Delegates to property

    def setFollowUpTimeoutValue(self, value: "TimeValue") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for followUpTimeoutValue with method chaining.

        Args:
            value: The followUpTimeoutValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to follow_up_timeout_value property setter (gets validation automatically)
        """
        self.follow_up_timeout_value = value  # Delegates to property setter
        return self

    def getIcvVerification(self) -> "GlobalTimeIcv":
        """
        AUTOSAR-compliant getter for icvVerification.

        Returns:
            The icvVerification value

        Note:
            Delegates to icv_verification property (CODING_RULE_V2_00017)
        """
        return self.icv_verification  # Delegates to property

    def setIcvVerification(self, value: "GlobalTimeIcv") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for icvVerification with method chaining.

        Args:
            value: The icvVerification to set

        Returns:
            self for method chaining

        Note:
            Delegates to icv_verification property setter (gets validation automatically)
        """
        self.icv_verification = value  # Delegates to property setter
        return self

    def getTimeLeapFuture(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeLeapFuture.

        Returns:
            The timeLeapFuture value

        Note:
            Delegates to time_leap_future property (CODING_RULE_V2_00017)
        """
        return self.time_leap_future  # Delegates to property

    def setTimeLeapFuture(self, value: "TimeValue") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for timeLeapFuture with method chaining.

        Args:
            value: The timeLeapFuture to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_leap_future property setter (gets validation automatically)
        """
        self.time_leap_future = value  # Delegates to property setter
        return self

    def getTimeLeap(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for timeLeap.

        Returns:
            The timeLeap value

        Note:
            Delegates to time_leap property (CODING_RULE_V2_00017)
        """
        return self.time_leap  # Delegates to property

    def setTimeLeap(self, value: "PositiveInteger") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for timeLeap with method chaining.

        Args:
            value: The timeLeap to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_leap property setter (gets validation automatically)
        """
        self.time_leap = value  # Delegates to property setter
        return self

    def getTimeLeapPast(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeLeapPast.

        Returns:
            The timeLeapPast value

        Note:
            Delegates to time_leap_past property (CODING_RULE_V2_00017)
        """
        return self.time_leap_past  # Delegates to property

    def setTimeLeapPast(self, value: "TimeValue") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for timeLeapPast with method chaining.

        Args:
            value: The timeLeapPast to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_leap_past property setter (gets validation automatically)
        """
        self.time_leap_past = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["Communication"]) -> "GlobalTimeSlave":
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

    def with_follow_up_timeout_value(self, value: Optional["TimeValue"]) -> "GlobalTimeSlave":
        """
        Set followUpTimeoutValue and return self for chaining.

        Args:
            value: The followUpTimeoutValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_follow_up_timeout_value("value")
        """
        self.follow_up_timeout_value = value  # Use property setter (gets validation)
        return self

    def with_icv_verification(self, value: Optional["GlobalTimeIcv"]) -> "GlobalTimeSlave":
        """
        Set icvVerification and return self for chaining.

        Args:
            value: The icvVerification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_icv_verification("value")
        """
        self.icv_verification = value  # Use property setter (gets validation)
        return self

    def with_time_leap_future(self, value: Optional["TimeValue"]) -> "GlobalTimeSlave":
        """
        Set timeLeapFuture and return self for chaining.

        Args:
            value: The timeLeapFuture to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_leap_future("value")
        """
        self.time_leap_future = value  # Use property setter (gets validation)
        return self

    def with_time_leap(self, value: Optional["PositiveInteger"]) -> "GlobalTimeSlave":
        """
        Set timeLeap and return self for chaining.

        Args:
            value: The timeLeap to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_leap("value")
        """
        self.time_leap = value  # Use property setter (gets validation)
        return self

    def with_time_leap_past(self, value: Optional["TimeValue"]) -> "GlobalTimeSlave":
        """
        Set timeLeapPast and return self for chaining.

        Args:
            value: The timeLeapPast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_leap_past("value")
        """
        self.time_leap_past = value  # Use property setter (gets validation)
        return self
