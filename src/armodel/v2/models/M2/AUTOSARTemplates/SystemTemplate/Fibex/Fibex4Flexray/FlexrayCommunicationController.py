from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class FlexrayCommunicationController(ARObject):
    """
    FlexRay bus specific communication port attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 84, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 446, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Expanded range of measured clock deviation allowed for frames during
                # integration.
        # Unit:microtick.
        self._accepted: Optional["Integer"] = None

    @property
    def accepted(self) -> Optional["Integer"]:
        """Get accepted (Pythonic accessor)."""
        return self._accepted

    @accepted.setter
    def accepted(self, value: Optional["Integer"]) -> None:
        """
        Set accepted with validation.

        Args:
            value: The accepted to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accepted = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"accepted must be Integer or None, got {type(value).__name__}"
            )
        self._accepted = value
        # Boolean flag that controls the transition to the POC:halt due to a clock
                # synchronization errors.
        # If set to true, Controller is allowed to transition to set to false, the
                # Communication Controller transition to the POC:halt state but will enter or
                # the normal POC (passive State).
        self._allowHaltDueTo: Optional["Boolean"] = None

    @property
    def allow_halt_due_to(self) -> Optional["Boolean"]:
        """Get allowHaltDueTo (Pythonic accessor)."""
        return self._allowHaltDueTo

    @allow_halt_due_to.setter
    def allow_halt_due_to(self, value: Optional["Boolean"]) -> None:
        """
        Set allowHaltDueTo with validation.

        Args:
            value: The allowHaltDueTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allowHaltDueTo = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"allowHaltDueTo must be Boolean or None, got {type(value).__name__}"
            )
        self._allowHaltDueTo = value
        # Number of consecutive even/odd cycle pairs that shall valid clock correction
        # terms before the will be allowed to transition POC:normal passive state to
        # POC:normal active set to 0, the Communication Controller is not transition
        # from POC:norm.
        self._allowPassiveTo: Optional["Integer"] = None

    @property
    def allow_passive_to(self) -> Optional["Integer"]:
        """Get allowPassiveTo (Pythonic accessor)."""
        return self._allowPassiveTo

    @allow_passive_to.setter
    def allow_passive_to(self, value: Optional["Integer"]) -> None:
        """
        Set allowPassiveTo with validation.

        Args:
            value: The allowPassiveTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allowPassiveTo = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"allowPassiveTo must be Integer or None, got {type(value).__name__}"
            )
        self._allowPassiveTo = value
        # The cluster drift damping factor used in clock rate correction in microticks.
        self._clusterDrift: Optional["Integer"] = None

    @property
    def cluster_drift(self) -> Optional["Integer"]:
        """Get clusterDrift (Pythonic accessor)."""
        return self._clusterDrift

    @cluster_drift.setter
    def cluster_drift(self, value: Optional["Integer"]) -> None:
        """
        Set clusterDrift with validation.

        Args:
            value: The clusterDrift to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clusterDrift = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"clusterDrift must be Integer or None, got {type(value).__name__}"
            )
        self._clusterDrift = value
        # Value used by the receiver to calculate the difference primary time reference
        # point and secondary time Unit: Microticks (pDecodingCorrection).
        self._decoding: Optional["Integer"] = None

    @property
    def decoding(self) -> Optional["Integer"]:
        """Get decoding (Pythonic accessor)."""
        return self._decoding

    @decoding.setter
    def decoding(self, value: Optional["Integer"]) -> None:
        """
        Set decoding with validation.

        Args:
            value: The decoding to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._decoding = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"decoding must be Integer or None, got {type(value).__name__}"
            )
        self._decoding = value
        # Value used to compensate for reception delays on B.
        # Unit: Microticks.
        # This optional parameter shall filled out if channel B is used.
        self._delay: Optional["Integer"] = None

    @property
    def delay(self) -> Optional["Integer"]:
        """Get delay (Pythonic accessor)."""
        return self._delay

    @delay.setter
    def delay(self, value: Optional["Integer"]) -> None:
        """
        Set delay with validation.

        Args:
            value: The delay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._delay = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"delay must be Integer or None, got {type(value).__name__}"
            )
        self._delay = value
        # Flag indicating whether the node is externally as Time Gateway Sink in an
        # Triggered External Sync cluster) or locally.
        self._externalSync: Optional["Boolean"] = None

    @property
    def external_sync(self) -> Optional["Boolean"]:
        """Get externalSync (Pythonic accessor)."""
        return self._externalSync

    @external_sync.setter
    def external_sync(self, value: Optional["Boolean"]) -> None:
        """
        Set externalSync with validation.

        Args:
            value: The externalSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._externalSync = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"externalSync must be Boolean or None, got {type(value).__name__}"
            )
        self._externalSync = value
        # Fixed amount added or subtracted to the calculated offset term to facilitate
        # external offset correction, node-local microticks.
        self._externOffset: Optional["Integer"] = None

    @property
    def extern_offset(self) -> Optional["Integer"]:
        """Get externOffset (Pythonic accessor)."""
        return self._externOffset

    @extern_offset.setter
    def extern_offset(self, value: Optional["Integer"]) -> None:
        """
        Set externOffset with validation.

        Args:
            value: The externOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._externOffset = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"externOffset must be Integer or None, got {type(value).__name__}"
            )
        self._externOffset = value
        # Fixed amount added or subtracted to the calculated rate term to facilitate
        # external rate correction, node-local microticks.
        self._externRate: Optional["Integer"] = None

    @property
    def extern_rate(self) -> Optional["Integer"]:
        """Get externRate (Pythonic accessor)."""
        return self._externRate

    @extern_rate.setter
    def extern_rate(self, value: Optional["Integer"]) -> None:
        """
        Set externRate with validation.

        Args:
            value: The externRate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._externRate = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"externRate must be Integer or None, got {type(value).__name__}"
            )
        self._externRate = value
        # Flag indicating whether a Time Gateway Sink node will local clock operation
        # when synchronization with Gateway Source node is lost (pFallBackInternal or
        # will instead go to POC:ready (pFallBackInternal.
        self._fallBackInternal: Optional["Boolean"] = None

    @property
    def fall_back_internal(self) -> Optional["Boolean"]:
        """Get fallBackInternal (Pythonic accessor)."""
        return self._fallBackInternal

    @fall_back_internal.setter
    def fall_back_internal(self, value: Optional["Boolean"]) -> None:
        """
        Set fallBackInternal with validation.

        Args:
            value: The fallBackInternal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fallBackInternal = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"fallBackInternal must be Boolean or None, got {type(value).__name__}"
            )
        self._fallBackInternal = value
        # One First In First Out (FIFO) queued receive structure, the admittance
        # criteria to the FIFO.
        self._flexrayFifo: List["FlexrayFifo"] = []

    @property
    def flexray_fifo(self) -> List["FlexrayFifo"]:
        """Get flexrayFifo (Pythonic accessor)."""
        return self._flexrayFifo
        # ID of the slot used to transmit the startup frame, sync designated single
                # slot frame.
        # If the attributes or keySlot set to true the key slot value is.
        self._keySlotID: Optional["PositiveInteger"] = None

    @property
    def key_slot_id(self) -> Optional["PositiveInteger"]:
        """Get keySlotID (Pythonic accessor)."""
        return self._keySlotID

    @key_slot_id.setter
    def key_slot_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set keySlotID with validation.

        Args:
            value: The keySlotID to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySlotID = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"keySlotID must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._keySlotID = value
        # Flag indicating whether or not the node shall enter key only mode following
        # startup.
        self._keySlotOnly: Optional["Boolean"] = None

    @property
    def key_slot_only(self) -> Optional["Boolean"]:
        """Get keySlotOnly (Pythonic accessor)."""
        return self._keySlotOnly

    @key_slot_only.setter
    def key_slot_only(self, value: Optional["Boolean"]) -> None:
        """
        Set keySlotOnly with validation.

        Args:
            value: The keySlotOnly to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySlotOnly = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"keySlotOnly must be Boolean or None, got {type(value).__name__}"
            )
        self._keySlotOnly = value
        # Flag indicating whether the Key Slot is used to transmit a frame.
        self._keySlotUsedFor: Optional["Boolean"] = None

    @property
    def key_slot_used_for(self) -> Optional["Boolean"]:
        """Get keySlotUsedFor (Pythonic accessor)."""
        return self._keySlotUsedFor

    @key_slot_used_for.setter
    def key_slot_used_for(self, value: Optional["Boolean"]) -> None:
        """
        Set keySlotUsedFor with validation.

        Args:
            value: The keySlotUsedFor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySlotUsedFor = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"keySlotUsedFor must be Boolean or None, got {type(value).__name__}"
            )
        self._keySlotUsedFor = value
        # The number of the last minislot in which a transmission in the dynamic
        # segment for the respective node.
        self._latestTX: Optional["Integer"] = None

    @property
    def latest_tx(self) -> Optional["Integer"]:
        """Get latestTX (Pythonic accessor)."""
        return self._latestTX

    @latest_tx.setter
    def latest_tx(self, value: Optional["Integer"]) -> None:
        """
        Set latestTX with validation.

        Args:
            value: The latestTX to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._latestTX = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"latestTX must be Integer or None, got {type(value).__name__}"
            )
        self._latestTX = value
        # Value for the startup listen timeout and wakeup listen this is a node local
                # parameter, the real of this value should be the same for all the cluster.
        # Unit: Microticks.
        self._listenTimeout: Optional["Integer"] = None

    @property
    def listen_timeout(self) -> Optional["Integer"]:
        """Get listenTimeout (Pythonic accessor)."""
        return self._listenTimeout

    @listen_timeout.setter
    def listen_timeout(self, value: Optional["Integer"]) -> None:
        """
        Set listenTimeout with validation.

        Args:
            value: The listenTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._listenTimeout = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"listenTimeout must be Integer or None, got {type(value).__name__}"
            )
        self._listenTimeout = value
        # Integer number of macroticks between the static slot and the closest
                # macrotick boundary of the reference point based on the nominal
                # (pMacroInitialOffset).
        # This optional only be filled out if channel B is used.
        self._macroInitial: Optional["Integer"] = None

    @property
    def macro_initial(self) -> Optional["Integer"]:
        """Get macroInitial (Pythonic accessor)."""
        return self._macroInitial

    @macro_initial.setter
    def macro_initial(self, value: Optional["Integer"]) -> None:
        """
        Set macroInitial with validation.

        Args:
            value: The macroInitial to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macroInitial = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"macroInitial must be Integer or None, got {type(value).__name__}"
            )
        self._macroInitial = value
        # Maximum payload length for the dynamic channel of a in 16 bit WORDS.
        self._maximum: Optional["Integer"] = None

    @property
    def maximum(self) -> Optional["Integer"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["Integer"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maximum must be Integer or None, got {type(value).__name__}"
            )
        self._maximum = value
        # Number of microticks between the closest macrotick described by
                # gMacroInitialOffset and the reference point.
        # The parameter depends and therefore it has to be set each channel.
        # This optional parameter be filled out if channel B is used.
        self._microInitial: Optional["Integer"] = None

    @property
    def micro_initial(self) -> Optional["Integer"]:
        """Get microInitial (Pythonic accessor)."""
        return self._microInitial

    @micro_initial.setter
    def micro_initial(self, value: Optional["Integer"]) -> None:
        """
        Set microInitial with validation.

        Args:
            value: The microInitial to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._microInitial = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"microInitial must be Integer or None, got {type(value).__name__}"
            )
        self._microInitial = value
        # The nominal number of microticks in a communication.
        self._microPerCycle: Optional["Integer"] = None

    @property
    def micro_per_cycle(self) -> Optional["Integer"]:
        """Get microPerCycle (Pythonic accessor)."""
        return self._microPerCycle

    @micro_per_cycle.setter
    def micro_per_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set microPerCycle with validation.

        Args:
            value: The microPerCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._microPerCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"microPerCycle must be Integer or None, got {type(value).__name__}"
            )
        self._microPerCycle = value
        # Duration of a microtick.
        # This attribute can be derived from and gdSampleClockPeriod.
        # Unit:.
        self._microtick: Optional["TimeValue"] = None

    @property
    def microtick(self) -> Optional["TimeValue"]:
        """Get microtick (Pythonic accessor)."""
        return self._microtick

    @microtick.setter
    def microtick(self, value: Optional["TimeValue"]) -> None:
        """
        Set microtick with validation.

        Args:
            value: The microtick to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._microtick = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"microtick must be TimeValue or None, got {type(value).__name__}"
            )
        self._microtick = value
        # Flag indicating when the update of the Network Vector in the CHI shall take
                # place.
        # If set to update shall take place after the NIT.
        # If set to update shall take place after the end of the static.
        self._nmVectorEarly: Optional["Boolean"] = None

    @property
    def nm_vector_early(self) -> Optional["Boolean"]:
        """Get nmVectorEarly (Pythonic accessor)."""
        return self._nmVectorEarly

    @nm_vector_early.setter
    def nm_vector_early(self, value: Optional["Boolean"]) -> None:
        """
        Set nmVectorEarly with validation.

        Args:
            value: The nmVectorEarly to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmVectorEarly = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmVectorEarly must be Boolean or None, got {type(value).__name__}"
            )
        self._nmVectorEarly = value
        # Magnitude of the maximum permissible offset correction Unit:microtick
        # (pOffsetCorrectionOut).
        self._offsetCorrection: Optional["Integer"] = None

    @property
    def offset_correction(self) -> Optional["Integer"]:
        """Get offsetCorrection (Pythonic accessor)."""
        return self._offsetCorrection

    @offset_correction.setter
    def offset_correction(self, value: Optional["Integer"]) -> None:
        """
        Set offsetCorrection with validation.

        Args:
            value: The offsetCorrection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offsetCorrection = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"offsetCorrection must be Integer or None, got {type(value).__name__}"
            )
        self._offsetCorrection = value
        # Magnitude of the maximum permissible rate correction and the maximum drift
                # offset between two nodes unsynchronized clocks for one Unit:Microticks
                # (pRateCorrection parameter maps to FlexRay Protocol 2.
        # 1 parameter pdMaxDrift.
        self._rateCorrection: Optional["Integer"] = None

    @property
    def rate_correction(self) -> Optional["Integer"]:
        """Get rateCorrection (Pythonic accessor)."""
        return self._rateCorrection

    @rate_correction.setter
    def rate_correction(self, value: Optional["Integer"]) -> None:
        """
        Set rateCorrection with validation.

        Args:
            value: The rateCorrection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateCorrection = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"rateCorrection must be Integer or None, got {type(value).__name__}"
            )
        self._rateCorrection = value
        # Number of samples per microtick.
        self._samplesPerMicrotick: Optional["Integer"] = None

    @property
    def samples_per_microtick(self) -> Optional["Integer"]:
        """Get samplesPerMicrotick (Pythonic accessor)."""
        return self._samplesPerMicrotick

    @samples_per_microtick.setter
    def samples_per_microtick(self, value: Optional["Integer"]) -> None:
        """
        Set samplesPerMicrotick with validation.

        Args:
            value: The samplesPerMicrotick to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._samplesPerMicrotick = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"samplesPerMicrotick must be Integer or None, got {type(value).__name__}"
            )
        self._samplesPerMicrotick = value
        # ID of the second Key slot, in which a second startup shall be sent in TT-L
                # Time Triggered Local Master TT-E Time Triggered External Sync mode.
        # If this set to zero the node does not have a second.
        self._secondKeySlot: Optional["PositiveInteger"] = None

    @property
    def second_key_slot(self) -> Optional["PositiveInteger"]:
        """Get secondKeySlot (Pythonic accessor)."""
        return self._secondKeySlot

    @second_key_slot.setter
    def second_key_slot(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set secondKeySlot with validation.

        Args:
            value: The secondKeySlot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondKeySlot = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"secondKeySlot must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._secondKeySlot = value
        # Flag indicating whether node operates as a startup node a TT-E Time Triggered
        # External Sync or TT-L Time Master Sync cluster.
        self._twoKeySlot: Optional["Boolean"] = None

    @property
    def two_key_slot(self) -> Optional["Boolean"]:
        """Get twoKeySlot (Pythonic accessor)."""
        return self._twoKeySlot

    @two_key_slot.setter
    def two_key_slot(self, value: Optional["Boolean"]) -> None:
        """
        Set twoKeySlot with validation.

        Args:
            value: The twoKeySlot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._twoKeySlot = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"twoKeySlot must be Boolean or None, got {type(value).__name__}"
            )
        self._twoKeySlot = value
        # Number of repetitions of the Tx-wakeup symbol to be sent CC_WakeupSend state
        # of this Node in the.
        self._wakeUpPattern: Optional["Integer"] = None

    @property
    def wake_up_pattern(self) -> Optional["Integer"]:
        """Get wakeUpPattern (Pythonic accessor)."""
        return self._wakeUpPattern

    @wake_up_pattern.setter
    def wake_up_pattern(self, value: Optional["Integer"]) -> None:
        """
        Set wakeUpPattern with validation.

        Args:
            value: The wakeUpPattern to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeUpPattern = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"wakeUpPattern must be Integer or None, got {type(value).__name__}"
            )
        self._wakeUpPattern = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccepted(self) -> "Integer":
        """
        AUTOSAR-compliant getter for accepted.

        Returns:
            The accepted value

        Note:
            Delegates to accepted property (CODING_RULE_V2_00017)
        """
        return self.accepted  # Delegates to property

    def setAccepted(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for accepted with method chaining.

        Args:
            value: The accepted to set

        Returns:
            self for method chaining

        Note:
            Delegates to accepted property setter (gets validation automatically)
        """
        self.accepted = value  # Delegates to property setter
        return self

    def getAllowHaltDueTo(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for allowHaltDueTo.

        Returns:
            The allowHaltDueTo value

        Note:
            Delegates to allow_halt_due_to property (CODING_RULE_V2_00017)
        """
        return self.allow_halt_due_to  # Delegates to property

    def setAllowHaltDueTo(self, value: "Boolean") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for allowHaltDueTo with method chaining.

        Args:
            value: The allowHaltDueTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to allow_halt_due_to property setter (gets validation automatically)
        """
        self.allow_halt_due_to = value  # Delegates to property setter
        return self

    def getAllowPassiveTo(self) -> "Integer":
        """
        AUTOSAR-compliant getter for allowPassiveTo.

        Returns:
            The allowPassiveTo value

        Note:
            Delegates to allow_passive_to property (CODING_RULE_V2_00017)
        """
        return self.allow_passive_to  # Delegates to property

    def setAllowPassiveTo(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for allowPassiveTo with method chaining.

        Args:
            value: The allowPassiveTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to allow_passive_to property setter (gets validation automatically)
        """
        self.allow_passive_to = value  # Delegates to property setter
        return self

    def getClusterDrift(self) -> "Integer":
        """
        AUTOSAR-compliant getter for clusterDrift.

        Returns:
            The clusterDrift value

        Note:
            Delegates to cluster_drift property (CODING_RULE_V2_00017)
        """
        return self.cluster_drift  # Delegates to property

    def setClusterDrift(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for clusterDrift with method chaining.

        Args:
            value: The clusterDrift to set

        Returns:
            self for method chaining

        Note:
            Delegates to cluster_drift property setter (gets validation automatically)
        """
        self.cluster_drift = value  # Delegates to property setter
        return self

    def getDecoding(self) -> "Integer":
        """
        AUTOSAR-compliant getter for decoding.

        Returns:
            The decoding value

        Note:
            Delegates to decoding property (CODING_RULE_V2_00017)
        """
        return self.decoding  # Delegates to property

    def setDecoding(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for decoding with method chaining.

        Args:
            value: The decoding to set

        Returns:
            self for method chaining

        Note:
            Delegates to decoding property setter (gets validation automatically)
        """
        self.decoding = value  # Delegates to property setter
        return self

    def getDelay(self) -> "Integer":
        """
        AUTOSAR-compliant getter for delay.

        Returns:
            The delay value

        Note:
            Delegates to delay property (CODING_RULE_V2_00017)
        """
        return self.delay  # Delegates to property

    def setDelay(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for delay with method chaining.

        Args:
            value: The delay to set

        Returns:
            self for method chaining

        Note:
            Delegates to delay property setter (gets validation automatically)
        """
        self.delay = value  # Delegates to property setter
        return self

    def getExternalSync(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for externalSync.

        Returns:
            The externalSync value

        Note:
            Delegates to external_sync property (CODING_RULE_V2_00017)
        """
        return self.external_sync  # Delegates to property

    def setExternalSync(self, value: "Boolean") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for externalSync with method chaining.

        Args:
            value: The externalSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to external_sync property setter (gets validation automatically)
        """
        self.external_sync = value  # Delegates to property setter
        return self

    def getExternOffset(self) -> "Integer":
        """
        AUTOSAR-compliant getter for externOffset.

        Returns:
            The externOffset value

        Note:
            Delegates to extern_offset property (CODING_RULE_V2_00017)
        """
        return self.extern_offset  # Delegates to property

    def setExternOffset(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for externOffset with method chaining.

        Args:
            value: The externOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to extern_offset property setter (gets validation automatically)
        """
        self.extern_offset = value  # Delegates to property setter
        return self

    def getExternRate(self) -> "Integer":
        """
        AUTOSAR-compliant getter for externRate.

        Returns:
            The externRate value

        Note:
            Delegates to extern_rate property (CODING_RULE_V2_00017)
        """
        return self.extern_rate  # Delegates to property

    def setExternRate(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for externRate with method chaining.

        Args:
            value: The externRate to set

        Returns:
            self for method chaining

        Note:
            Delegates to extern_rate property setter (gets validation automatically)
        """
        self.extern_rate = value  # Delegates to property setter
        return self

    def getFallBackInternal(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for fallBackInternal.

        Returns:
            The fallBackInternal value

        Note:
            Delegates to fall_back_internal property (CODING_RULE_V2_00017)
        """
        return self.fall_back_internal  # Delegates to property

    def setFallBackInternal(self, value: "Boolean") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for fallBackInternal with method chaining.

        Args:
            value: The fallBackInternal to set

        Returns:
            self for method chaining

        Note:
            Delegates to fall_back_internal property setter (gets validation automatically)
        """
        self.fall_back_internal = value  # Delegates to property setter
        return self

    def getFlexrayFifo(self) -> List["FlexrayFifo"]:
        """
        AUTOSAR-compliant getter for flexrayFifo.

        Returns:
            The flexrayFifo value

        Note:
            Delegates to flexray_fifo property (CODING_RULE_V2_00017)
        """
        return self.flexray_fifo  # Delegates to property

    def getKeySlotID(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for keySlotID.

        Returns:
            The keySlotID value

        Note:
            Delegates to key_slot_id property (CODING_RULE_V2_00017)
        """
        return self.key_slot_id  # Delegates to property

    def setKeySlotID(self, value: "PositiveInteger") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for keySlotID with method chaining.

        Args:
            value: The keySlotID to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_slot_id property setter (gets validation automatically)
        """
        self.key_slot_id = value  # Delegates to property setter
        return self

    def getKeySlotOnly(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for keySlotOnly.

        Returns:
            The keySlotOnly value

        Note:
            Delegates to key_slot_only property (CODING_RULE_V2_00017)
        """
        return self.key_slot_only  # Delegates to property

    def setKeySlotOnly(self, value: "Boolean") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for keySlotOnly with method chaining.

        Args:
            value: The keySlotOnly to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_slot_only property setter (gets validation automatically)
        """
        self.key_slot_only = value  # Delegates to property setter
        return self

    def getKeySlotUsedFor(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for keySlotUsedFor.

        Returns:
            The keySlotUsedFor value

        Note:
            Delegates to key_slot_used_for property (CODING_RULE_V2_00017)
        """
        return self.key_slot_used_for  # Delegates to property

    def setKeySlotUsedFor(self, value: "Boolean") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for keySlotUsedFor with method chaining.

        Args:
            value: The keySlotUsedFor to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_slot_used_for property setter (gets validation automatically)
        """
        self.key_slot_used_for = value  # Delegates to property setter
        return self

    def getLatestTX(self) -> "Integer":
        """
        AUTOSAR-compliant getter for latestTX.

        Returns:
            The latestTX value

        Note:
            Delegates to latest_tx property (CODING_RULE_V2_00017)
        """
        return self.latest_tx  # Delegates to property

    def setLatestTX(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for latestTX with method chaining.

        Args:
            value: The latestTX to set

        Returns:
            self for method chaining

        Note:
            Delegates to latest_tx property setter (gets validation automatically)
        """
        self.latest_tx = value  # Delegates to property setter
        return self

    def getListenTimeout(self) -> "Integer":
        """
        AUTOSAR-compliant getter for listenTimeout.

        Returns:
            The listenTimeout value

        Note:
            Delegates to listen_timeout property (CODING_RULE_V2_00017)
        """
        return self.listen_timeout  # Delegates to property

    def setListenTimeout(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for listenTimeout with method chaining.

        Args:
            value: The listenTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to listen_timeout property setter (gets validation automatically)
        """
        self.listen_timeout = value  # Delegates to property setter
        return self

    def getMacroInitial(self) -> "Integer":
        """
        AUTOSAR-compliant getter for macroInitial.

        Returns:
            The macroInitial value

        Note:
            Delegates to macro_initial property (CODING_RULE_V2_00017)
        """
        return self.macro_initial  # Delegates to property

    def setMacroInitial(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for macroInitial with method chaining.

        Args:
            value: The macroInitial to set

        Returns:
            self for method chaining

        Note:
            Delegates to macro_initial property setter (gets validation automatically)
        """
        self.macro_initial = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getMicroInitial(self) -> "Integer":
        """
        AUTOSAR-compliant getter for microInitial.

        Returns:
            The microInitial value

        Note:
            Delegates to micro_initial property (CODING_RULE_V2_00017)
        """
        return self.micro_initial  # Delegates to property

    def setMicroInitial(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for microInitial with method chaining.

        Args:
            value: The microInitial to set

        Returns:
            self for method chaining

        Note:
            Delegates to micro_initial property setter (gets validation automatically)
        """
        self.micro_initial = value  # Delegates to property setter
        return self

    def getMicroPerCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for microPerCycle.

        Returns:
            The microPerCycle value

        Note:
            Delegates to micro_per_cycle property (CODING_RULE_V2_00017)
        """
        return self.micro_per_cycle  # Delegates to property

    def setMicroPerCycle(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for microPerCycle with method chaining.

        Args:
            value: The microPerCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to micro_per_cycle property setter (gets validation automatically)
        """
        self.micro_per_cycle = value  # Delegates to property setter
        return self

    def getMicrotick(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for microtick.

        Returns:
            The microtick value

        Note:
            Delegates to microtick property (CODING_RULE_V2_00017)
        """
        return self.microtick  # Delegates to property

    def setMicrotick(self, value: "TimeValue") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for microtick with method chaining.

        Args:
            value: The microtick to set

        Returns:
            self for method chaining

        Note:
            Delegates to microtick property setter (gets validation automatically)
        """
        self.microtick = value  # Delegates to property setter
        return self

    def getNmVectorEarly(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmVectorEarly.

        Returns:
            The nmVectorEarly value

        Note:
            Delegates to nm_vector_early property (CODING_RULE_V2_00017)
        """
        return self.nm_vector_early  # Delegates to property

    def setNmVectorEarly(self, value: "Boolean") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for nmVectorEarly with method chaining.

        Args:
            value: The nmVectorEarly to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_vector_early property setter (gets validation automatically)
        """
        self.nm_vector_early = value  # Delegates to property setter
        return self

    def getOffsetCorrection(self) -> "Integer":
        """
        AUTOSAR-compliant getter for offsetCorrection.

        Returns:
            The offsetCorrection value

        Note:
            Delegates to offset_correction property (CODING_RULE_V2_00017)
        """
        return self.offset_correction  # Delegates to property

    def setOffsetCorrection(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for offsetCorrection with method chaining.

        Args:
            value: The offsetCorrection to set

        Returns:
            self for method chaining

        Note:
            Delegates to offset_correction property setter (gets validation automatically)
        """
        self.offset_correction = value  # Delegates to property setter
        return self

    def getRateCorrection(self) -> "Integer":
        """
        AUTOSAR-compliant getter for rateCorrection.

        Returns:
            The rateCorrection value

        Note:
            Delegates to rate_correction property (CODING_RULE_V2_00017)
        """
        return self.rate_correction  # Delegates to property

    def setRateCorrection(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for rateCorrection with method chaining.

        Args:
            value: The rateCorrection to set

        Returns:
            self for method chaining

        Note:
            Delegates to rate_correction property setter (gets validation automatically)
        """
        self.rate_correction = value  # Delegates to property setter
        return self

    def getSamplesPerMicrotick(self) -> "Integer":
        """
        AUTOSAR-compliant getter for samplesPerMicrotick.

        Returns:
            The samplesPerMicrotick value

        Note:
            Delegates to samples_per_microtick property (CODING_RULE_V2_00017)
        """
        return self.samples_per_microtick  # Delegates to property

    def setSamplesPerMicrotick(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for samplesPerMicrotick with method chaining.

        Args:
            value: The samplesPerMicrotick to set

        Returns:
            self for method chaining

        Note:
            Delegates to samples_per_microtick property setter (gets validation automatically)
        """
        self.samples_per_microtick = value  # Delegates to property setter
        return self

    def getSecondKeySlot(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for secondKeySlot.

        Returns:
            The secondKeySlot value

        Note:
            Delegates to second_key_slot property (CODING_RULE_V2_00017)
        """
        return self.second_key_slot  # Delegates to property

    def setSecondKeySlot(self, value: "PositiveInteger") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for secondKeySlot with method chaining.

        Args:
            value: The secondKeySlot to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_key_slot property setter (gets validation automatically)
        """
        self.second_key_slot = value  # Delegates to property setter
        return self

    def getTwoKeySlot(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for twoKeySlot.

        Returns:
            The twoKeySlot value

        Note:
            Delegates to two_key_slot property (CODING_RULE_V2_00017)
        """
        return self.two_key_slot  # Delegates to property

    def setTwoKeySlot(self, value: "Boolean") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for twoKeySlot with method chaining.

        Args:
            value: The twoKeySlot to set

        Returns:
            self for method chaining

        Note:
            Delegates to two_key_slot property setter (gets validation automatically)
        """
        self.two_key_slot = value  # Delegates to property setter
        return self

    def getWakeUpPattern(self) -> "Integer":
        """
        AUTOSAR-compliant getter for wakeUpPattern.

        Returns:
            The wakeUpPattern value

        Note:
            Delegates to wake_up_pattern property (CODING_RULE_V2_00017)
        """
        return self.wake_up_pattern  # Delegates to property

    def setWakeUpPattern(self, value: "Integer") -> "FlexrayCommunicationController":
        """
        AUTOSAR-compliant setter for wakeUpPattern with method chaining.

        Args:
            value: The wakeUpPattern to set

        Returns:
            self for method chaining

        Note:
            Delegates to wake_up_pattern property setter (gets validation automatically)
        """
        self.wake_up_pattern = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accepted(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set accepted and return self for chaining.

        Args:
            value: The accepted to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accepted("value")
        """
        self.accepted = value  # Use property setter (gets validation)
        return self

    def with_allow_halt_due_to(self, value: Optional["Boolean"]) -> "FlexrayCommunicationController":
        """
        Set allowHaltDueTo and return self for chaining.

        Args:
            value: The allowHaltDueTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allow_halt_due_to("value")
        """
        self.allow_halt_due_to = value  # Use property setter (gets validation)
        return self

    def with_allow_passive_to(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set allowPassiveTo and return self for chaining.

        Args:
            value: The allowPassiveTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allow_passive_to("value")
        """
        self.allow_passive_to = value  # Use property setter (gets validation)
        return self

    def with_cluster_drift(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set clusterDrift and return self for chaining.

        Args:
            value: The clusterDrift to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cluster_drift("value")
        """
        self.cluster_drift = value  # Use property setter (gets validation)
        return self

    def with_decoding(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set decoding and return self for chaining.

        Args:
            value: The decoding to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_decoding("value")
        """
        self.decoding = value  # Use property setter (gets validation)
        return self

    def with_delay(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set delay and return self for chaining.

        Args:
            value: The delay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_delay("value")
        """
        self.delay = value  # Use property setter (gets validation)
        return self

    def with_external_sync(self, value: Optional["Boolean"]) -> "FlexrayCommunicationController":
        """
        Set externalSync and return self for chaining.

        Args:
            value: The externalSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_external_sync("value")
        """
        self.external_sync = value  # Use property setter (gets validation)
        return self

    def with_extern_offset(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set externOffset and return self for chaining.

        Args:
            value: The externOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_extern_offset("value")
        """
        self.extern_offset = value  # Use property setter (gets validation)
        return self

    def with_extern_rate(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set externRate and return self for chaining.

        Args:
            value: The externRate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_extern_rate("value")
        """
        self.extern_rate = value  # Use property setter (gets validation)
        return self

    def with_fall_back_internal(self, value: Optional["Boolean"]) -> "FlexrayCommunicationController":
        """
        Set fallBackInternal and return self for chaining.

        Args:
            value: The fallBackInternal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fall_back_internal("value")
        """
        self.fall_back_internal = value  # Use property setter (gets validation)
        return self

    def with_key_slot_id(self, value: Optional["PositiveInteger"]) -> "FlexrayCommunicationController":
        """
        Set keySlotID and return self for chaining.

        Args:
            value: The keySlotID to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_slot_id("value")
        """
        self.key_slot_id = value  # Use property setter (gets validation)
        return self

    def with_key_slot_only(self, value: Optional["Boolean"]) -> "FlexrayCommunicationController":
        """
        Set keySlotOnly and return self for chaining.

        Args:
            value: The keySlotOnly to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_slot_only("value")
        """
        self.key_slot_only = value  # Use property setter (gets validation)
        return self

    def with_key_slot_used_for(self, value: Optional["Boolean"]) -> "FlexrayCommunicationController":
        """
        Set keySlotUsedFor and return self for chaining.

        Args:
            value: The keySlotUsedFor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_slot_used_for("value")
        """
        self.key_slot_used_for = value  # Use property setter (gets validation)
        return self

    def with_latest_tx(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set latestTX and return self for chaining.

        Args:
            value: The latestTX to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_latest_tx("value")
        """
        self.latest_tx = value  # Use property setter (gets validation)
        return self

    def with_listen_timeout(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set listenTimeout and return self for chaining.

        Args:
            value: The listenTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_listen_timeout("value")
        """
        self.listen_timeout = value  # Use property setter (gets validation)
        return self

    def with_macro_initial(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set macroInitial and return self for chaining.

        Args:
            value: The macroInitial to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_macro_initial("value")
        """
        self.macro_initial = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_micro_initial(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set microInitial and return self for chaining.

        Args:
            value: The microInitial to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_micro_initial("value")
        """
        self.micro_initial = value  # Use property setter (gets validation)
        return self

    def with_micro_per_cycle(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set microPerCycle and return self for chaining.

        Args:
            value: The microPerCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_micro_per_cycle("value")
        """
        self.micro_per_cycle = value  # Use property setter (gets validation)
        return self

    def with_microtick(self, value: Optional["TimeValue"]) -> "FlexrayCommunicationController":
        """
        Set microtick and return self for chaining.

        Args:
            value: The microtick to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_microtick("value")
        """
        self.microtick = value  # Use property setter (gets validation)
        return self

    def with_nm_vector_early(self, value: Optional["Boolean"]) -> "FlexrayCommunicationController":
        """
        Set nmVectorEarly and return self for chaining.

        Args:
            value: The nmVectorEarly to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_vector_early("value")
        """
        self.nm_vector_early = value  # Use property setter (gets validation)
        return self

    def with_offset_correction(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set offsetCorrection and return self for chaining.

        Args:
            value: The offsetCorrection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset_correction("value")
        """
        self.offset_correction = value  # Use property setter (gets validation)
        return self

    def with_rate_correction(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set rateCorrection and return self for chaining.

        Args:
            value: The rateCorrection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rate_correction("value")
        """
        self.rate_correction = value  # Use property setter (gets validation)
        return self

    def with_samples_per_microtick(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set samplesPerMicrotick and return self for chaining.

        Args:
            value: The samplesPerMicrotick to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_samples_per_microtick("value")
        """
        self.samples_per_microtick = value  # Use property setter (gets validation)
        return self

    def with_second_key_slot(self, value: Optional["PositiveInteger"]) -> "FlexrayCommunicationController":
        """
        Set secondKeySlot and return self for chaining.

        Args:
            value: The secondKeySlot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_key_slot("value")
        """
        self.second_key_slot = value  # Use property setter (gets validation)
        return self

    def with_two_key_slot(self, value: Optional["Boolean"]) -> "FlexrayCommunicationController":
        """
        Set twoKeySlot and return self for chaining.

        Args:
            value: The twoKeySlot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_two_key_slot("value")
        """
        self.two_key_slot = value  # Use property setter (gets validation)
        return self

    def with_wake_up_pattern(self, value: Optional["Integer"]) -> "FlexrayCommunicationController":
        """
        Set wakeUpPattern and return self for chaining.

        Args:
            value: The wakeUpPattern to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wake_up_pattern("value")
        """
        self.wake_up_pattern = value  # Use property setter (gets validation)
        return self
