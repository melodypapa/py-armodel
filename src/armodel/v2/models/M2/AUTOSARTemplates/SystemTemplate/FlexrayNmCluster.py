from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmCluster


class FlexrayNmCluster(NmCluster):
    """
    FlexRay specific NM cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::FlexrayNmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 678, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If set to true this attribute enables the support of CarWake bit evaluation
        # in received NmPdus.
        self._nmCarWakeUp: Optional["Boolean"] = None

    @property
    def nm_car_wake_up(self) -> Optional["Boolean"]:
        """Get nmCarWakeUp (Pythonic accessor)."""
        return self._nmCarWakeUp

    @nm_car_wake_up.setter
    def nm_car_wake_up(self, value: Optional["Boolean"]) -> None:
        """
        Set nmCarWakeUp with validation.

        Args:
            value: The nmCarWakeUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCarWakeUp = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmCarWakeUp must be Boolean or None, got {type(value).__name__}"
            )
        self._nmCarWakeUp = value
        # Number of FlexRay Communication Cycles needed to Nm Data PDUs of all FlexRay
        # Nm Ecus of.
        self._nmDataCycle: Optional["Integer"] = None

    @property
    def nm_data_cycle(self) -> Optional["Integer"]:
        """Get nmDataCycle (Pythonic accessor)."""
        return self._nmDataCycle

    @nm_data_cycle.setter
    def nm_data_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set nmDataCycle with validation.

        Args:
            value: The nmDataCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmDataCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"nmDataCycle must be Integer or None, got {type(value).__name__}"
            )
        self._nmDataCycle = value
        # Defines the processing cycle of the main function of FrNm.
        self._nmMain: Optional["TimeValue"] = None

    @property
    def nm_main(self) -> Optional["TimeValue"]:
        """Get nmMain (Pythonic accessor)."""
        return self._nmMain

    @nm_main.setter
    def nm_main(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmMain with validation.

        Args:
            value: The nmMain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMain = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMain must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMain = value
        # Timeout for Remote Sleep Indication in seconds.
        # It the time how long it shall take to recognize that all nodes are ready to
                # sleep.
        self._nmRemote: Optional["TimeValue"] = None

    @property
    def nm_remote(self) -> Optional["TimeValue"]:
        """Get nmRemote (Pythonic accessor)."""
        return self._nmRemote

    @nm_remote.setter
    def nm_remote(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmRemote with validation.

        Args:
            value: The nmRemote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRemote = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRemote must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRemote = value
        # Timeout for Repeat Message State in seconds.
        # Defines time how long the NM shall stay in the Repeat.
        self._nmRepeat: Optional["TimeValue"] = None

    @property
    def nm_repeat(self) -> Optional["TimeValue"]:
        """Get nmRepeat (Pythonic accessor)."""
        return self._nmRepeat

    @nm_repeat.setter
    def nm_repeat(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmRepeat with validation.

        Args:
            value: The nmRepeat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepeat = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRepeat must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRepeat = value
        # Number of FlexRay Communication Cycles used to the transmission of the Nm
                # vote Pdus of all Flex of this FlexRayNmCluster.
        # This value shall integral multiple of nmVotingCycle.
        self._nmRepetition: Optional["Integer"] = None

    @property
    def nm_repetition(self) -> Optional["Integer"]:
        """Get nmRepetition (Pythonic accessor)."""
        return self._nmRepetition

    @nm_repetition.setter
    def nm_repetition(self, value: Optional["Integer"]) -> None:
        """
        Set nmRepetition with validation.

        Args:
            value: The nmRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepetition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"nmRepetition must be Integer or None, got {type(value).__name__}"
            )
        self._nmRepetition = value
        # Number of FlexRay CommunicationCycles needed to Nm vote of Pdus of all
        # FlexRay NmEcus of.
        self._nmVotingCycle: Optional["Integer"] = None

    @property
    def nm_voting_cycle(self) -> Optional["Integer"]:
        """Get nmVotingCycle (Pythonic accessor)."""
        return self._nmVotingCycle

    @nm_voting_cycle.setter
    def nm_voting_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set nmVotingCycle with validation.

        Args:
            value: The nmVotingCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmVotingCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"nmVotingCycle must be Integer or None, got {type(value).__name__}"
            )
        self._nmVotingCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmCarWakeUp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmCarWakeUp.

        Returns:
            The nmCarWakeUp value

        Note:
            Delegates to nm_car_wake_up property (CODING_RULE_V2_00017)
        """
        return self.nm_car_wake_up  # Delegates to property

    def setNmCarWakeUp(self, value: "Boolean") -> "FlexrayNmCluster":
        """
        AUTOSAR-compliant setter for nmCarWakeUp with method chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_car_wake_up property setter (gets validation automatically)
        """
        self.nm_car_wake_up = value  # Delegates to property setter
        return self

    def getNmDataCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for nmDataCycle.

        Returns:
            The nmDataCycle value

        Note:
            Delegates to nm_data_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_data_cycle  # Delegates to property

    def setNmDataCycle(self, value: "Integer") -> "FlexrayNmCluster":
        """
        AUTOSAR-compliant setter for nmDataCycle with method chaining.

        Args:
            value: The nmDataCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_data_cycle property setter (gets validation automatically)
        """
        self.nm_data_cycle = value  # Delegates to property setter
        return self

    def getNmMain(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmMain.

        Returns:
            The nmMain value

        Note:
            Delegates to nm_main property (CODING_RULE_V2_00017)
        """
        return self.nm_main  # Delegates to property

    def setNmMain(self, value: "TimeValue") -> "FlexrayNmCluster":
        """
        AUTOSAR-compliant setter for nmMain with method chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_main property setter (gets validation automatically)
        """
        self.nm_main = value  # Delegates to property setter
        return self

    def getNmRemote(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmRemote.

        Returns:
            The nmRemote value

        Note:
            Delegates to nm_remote property (CODING_RULE_V2_00017)
        """
        return self.nm_remote  # Delegates to property

    def setNmRemote(self, value: "TimeValue") -> "FlexrayNmCluster":
        """
        AUTOSAR-compliant setter for nmRemote with method chaining.

        Args:
            value: The nmRemote to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_remote property setter (gets validation automatically)
        """
        self.nm_remote = value  # Delegates to property setter
        return self

    def getNmRepeat(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmRepeat.

        Returns:
            The nmRepeat value

        Note:
            Delegates to nm_repeat property (CODING_RULE_V2_00017)
        """
        return self.nm_repeat  # Delegates to property

    def setNmRepeat(self, value: "TimeValue") -> "FlexrayNmCluster":
        """
        AUTOSAR-compliant setter for nmRepeat with method chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repeat property setter (gets validation automatically)
        """
        self.nm_repeat = value  # Delegates to property setter
        return self

    def getNmRepetition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for nmRepetition.

        Returns:
            The nmRepetition value

        Note:
            Delegates to nm_repetition property (CODING_RULE_V2_00017)
        """
        return self.nm_repetition  # Delegates to property

    def setNmRepetition(self, value: "Integer") -> "FlexrayNmCluster":
        """
        AUTOSAR-compliant setter for nmRepetition with method chaining.

        Args:
            value: The nmRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repetition property setter (gets validation automatically)
        """
        self.nm_repetition = value  # Delegates to property setter
        return self

    def getNmVotingCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for nmVotingCycle.

        Returns:
            The nmVotingCycle value

        Note:
            Delegates to nm_voting_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_voting_cycle  # Delegates to property

    def setNmVotingCycle(self, value: "Integer") -> "FlexrayNmCluster":
        """
        AUTOSAR-compliant setter for nmVotingCycle with method chaining.

        Args:
            value: The nmVotingCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_voting_cycle property setter (gets validation automatically)
        """
        self.nm_voting_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_car_wake_up(self, value: Optional["Boolean"]) -> "FlexrayNmCluster":
        """
        Set nmCarWakeUp and return self for chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_car_wake_up("value")
        """
        self.nm_car_wake_up = value  # Use property setter (gets validation)
        return self

    def with_nm_data_cycle(self, value: Optional["Integer"]) -> "FlexrayNmCluster":
        """
        Set nmDataCycle and return self for chaining.

        Args:
            value: The nmDataCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_data_cycle("value")
        """
        self.nm_data_cycle = value  # Use property setter (gets validation)
        return self

    def with_nm_main(self, value: Optional["TimeValue"]) -> "FlexrayNmCluster":
        """
        Set nmMain and return self for chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_main("value")
        """
        self.nm_main = value  # Use property setter (gets validation)
        return self

    def with_nm_remote(self, value: Optional["TimeValue"]) -> "FlexrayNmCluster":
        """
        Set nmRemote and return self for chaining.

        Args:
            value: The nmRemote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_remote("value")
        """
        self.nm_remote = value  # Use property setter (gets validation)
        return self

    def with_nm_repeat(self, value: Optional["TimeValue"]) -> "FlexrayNmCluster":
        """
        Set nmRepeat and return self for chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repeat("value")
        """
        self.nm_repeat = value  # Use property setter (gets validation)
        return self

    def with_nm_repetition(self, value: Optional["Integer"]) -> "FlexrayNmCluster":
        """
        Set nmRepetition and return self for chaining.

        Args:
            value: The nmRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repetition("value")
        """
        self.nm_repetition = value  # Use property setter (gets validation)
        return self

    def with_nm_voting_cycle(self, value: Optional["Integer"]) -> "FlexrayNmCluster":
        """
        Set nmVotingCycle and return self for chaining.

        Args:
            value: The nmVotingCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_voting_cycle("value")
        """
        self.nm_voting_cycle = value  # Use property setter (gets validation)
        return self
