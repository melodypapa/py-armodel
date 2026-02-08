from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DdsCpTopic,
    ISignal,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DdsCpISignalToDdsTopicMapping(ARObject):
    """
    Mapping of an ISignal to a DdsTopic.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpISignalToDdsTopicMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 293, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DdsTopic.
        self._ddsTopic: Optional["DdsCpTopic"] = None

    @property
    def dds_topic(self) -> Optional["DdsCpTopic"]:
        """Get ddsTopic (Pythonic accessor)."""
        return self._ddsTopic

    @dds_topic.setter
    def dds_topic(self, value: Optional["DdsCpTopic"]) -> None:
        """
        Set ddsTopic with validation.

        Args:
            value: The ddsTopic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsTopic = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsTopic must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsTopic = value
        # Reference to the ISignal.
        self._iSignal: Optional["ISignal"] = None

    @property
    def i_signal(self) -> Optional["ISignal"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional["ISignal"]) -> None:
        """
        Set iSignal with validation.

        Args:
            value: The iSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsTopic(self) -> "DdsCpTopic":
        """
        AUTOSAR-compliant getter for ddsTopic.

        Returns:
            The ddsTopic value

        Note:
            Delegates to dds_topic property (CODING_RULE_V2_00017)
        """
        return self.dds_topic  # Delegates to property

    def setDdsTopic(self, value: "DdsCpTopic") -> "DdsCpISignalToDdsTopicMapping":
        """
        AUTOSAR-compliant setter for ddsTopic with method chaining.

        Args:
            value: The ddsTopic to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_topic property setter (gets validation automatically)
        """
        self.dds_topic = value  # Delegates to property setter
        return self

    def getISignal(self) -> "ISignal":
        """
        AUTOSAR-compliant getter for iSignal.

        Returns:
            The iSignal value

        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: "ISignal") -> "DdsCpISignalToDdsTopicMapping":
        """
        AUTOSAR-compliant setter for iSignal with method chaining.

        Args:
            value: The iSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_topic(self, value: Optional["DdsCpTopic"]) -> "DdsCpISignalToDdsTopicMapping":
        """
        Set ddsTopic and return self for chaining.

        Args:
            value: The ddsTopic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_topic("value")
        """
        self.dds_topic = value  # Use property setter (gets validation)
        return self

    def with_i_signal(self, value: Optional["ISignal"]) -> "DdsCpISignalToDdsTopicMapping":
        """
        Set iSignal and return self for chaining.

        Args:
            value: The iSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self
