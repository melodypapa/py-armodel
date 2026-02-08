from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Float,
    Integer,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class FlexrayCluster(ARObject):
    """
    FlexRay specific attributes to the physicalCluster

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 80, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The offset of the action point in networks.
        self._actionPointOffset: Optional["Integer"] = None

    @property
    def action_point_offset(self) -> Optional["Integer"]:
        """Get actionPointOffset (Pythonic accessor)."""
        return self._actionPointOffset

    @action_point_offset.setter
    def action_point_offset(self, value: Optional["Integer"]) -> None:
        """
        Set actionPointOffset with validation.

        Args:
            value: The actionPointOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._actionPointOffset = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"actionPointOffset must be Integer or None, got {type(value).__name__}"
            )
        self._actionPointOffset = value
        # Nominal bit time (= 1 / fx:SPEED).
        # gdBit = cSamplesPer gdSampleClockPeriod.
        # Unit: seconds (gdBit).
        self._bit: Optional["TimeValue"] = None

    @property
    def bit(self) -> Optional["TimeValue"]:
        """Get bit (Pythonic accessor)."""
        return self._bit

    @bit.setter
    def bit(self, value: Optional["TimeValue"]) -> None:
        """
        Set bit with validation.

        Args:
            value: The bit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bit = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"bit must be TimeValue or None, got {type(value).__name__}"
            )
        self._bit = value
        # Upper limit of the Collision Avoidance Symbol (CAS) Unit:bitDuration.
        self._casRxLowMax: Optional["Integer"] = None

    @property
    def cas_rx_low_max(self) -> Optional["Integer"]:
        """Get casRxLowMax (Pythonic accessor)."""
        return self._casRxLowMax

    @cas_rx_low_max.setter
    def cas_rx_low_max(self, value: Optional["Integer"]) -> None:
        """
        Set casRxLowMax with validation.

        Args:
            value: The casRxLowMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._casRxLowMax = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"casRxLowMax must be Integer or None, got {type(value).__name__}"
            )
        self._casRxLowMax = value
        # The maximum number of times that a node in this cluster permitted to attempt
        # to start the cluster by initiating.
        self._coldStart: Optional["Integer"] = None

    @property
    def cold_start(self) -> Optional["Integer"]:
        """Get coldStart (Pythonic accessor)."""
        return self._coldStart

    @cold_start.setter
    def cold_start(self, value: Optional["Integer"]) -> None:
        """
        Set coldStart with validation.

        Args:
            value: The coldStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._coldStart = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"coldStart must be Integer or None, got {type(value).__name__}"
            )
        self._coldStart = value
        # Length of the cycle.
        # Unit: seconds.
        self._cycle: Optional["TimeValue"] = None

    @property
    def cycle(self) -> Optional["TimeValue"]:
        """Get cycle (Pythonic accessor)."""
        return self._cycle

    @cycle.setter
    def cycle(self, value: Optional["TimeValue"]) -> None:
        """
        Set cycle with validation.

        Args:
            value: The cycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"cycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._cycle = value
        # Maximum cycle counter value in a given cluster.
        # Remark: 63 for FlexRay Protocol 2.
        # 1 Rev.
        # A compliance.
        self._cycleCountMax: Optional["Integer"] = None

    @property
    def cycle_count_max(self) -> Optional["Integer"]:
        """Get cycleCountMax (Pythonic accessor)."""
        return self._cycleCountMax

    @cycle_count_max.setter
    def cycle_count_max(self, value: Optional["Integer"]) -> None:
        """
        Set cycleCountMax with validation.

        Args:
            value: The cycleCountMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleCountMax = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"cycleCountMax must be Integer or None, got {type(value).__name__}"
            )
        self._cycleCountMax = value
        # Indicates whether NIT error status of each cluster shall be not.
        self._detectNitError: Optional["Boolean"] = None

    @property
    def detect_nit_error(self) -> Optional["Boolean"]:
        """Get detectNitError (Pythonic accessor)."""
        return self._detectNitError

    @detect_nit_error.setter
    def detect_nit_error(self, value: Optional["Boolean"]) -> None:
        """
        Set detectNitError with validation.

        Args:
            value: The detectNitError to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._detectNitError = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"detectNitError must be Boolean or None, got {type(value).__name__}"
            )
        self._detectNitError = value
        # The duration of the dynamic slot idle phase in minislots.
        self._dynamicSlotIdle: Optional["Integer"] = None

    @property
    def dynamic_slot_idle(self) -> Optional["Integer"]:
        """Get dynamicSlotIdle (Pythonic accessor)."""
        return self._dynamicSlotIdle

    @dynamic_slot_idle.setter
    def dynamic_slot_idle(self, value: Optional["Integer"]) -> None:
        """
        Set dynamicSlotIdle with validation.

        Args:
            value: The dynamicSlotIdle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicSlotIdle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"dynamicSlotIdle must be Integer or None, got {type(value).__name__}"
            )
        self._dynamicSlotIdle = value
        # Duration for which the bitstrobing is paused after.
        self._ignoreAfterTx: Optional["Integer"] = None

    @property
    def ignore_after_tx(self) -> Optional["Integer"]:
        """Get ignoreAfterTx (Pythonic accessor)."""
        return self._ignoreAfterTx

    @ignore_after_tx.setter
    def ignore_after_tx(self, value: Optional["Integer"]) -> None:
        """
        Set ignoreAfterTx with validation.

        Args:
            value: The ignoreAfterTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ignoreAfterTx = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"ignoreAfterTx must be Integer or None, got {type(value).__name__}"
            )
        self._ignoreAfterTx = value
        # Upper limit for the start up and wake up listen timeout in of noise.
        # Expressed as a multiple of the pdListenTimeout.
        # Unit microticks.
        self._listenNoise: Optional["Integer"] = None

    @property
    def listen_noise(self) -> Optional["Integer"]:
        """Get listenNoise (Pythonic accessor)."""
        return self._listenNoise

    @listen_noise.setter
    def listen_noise(self, value: Optional["Integer"]) -> None:
        """
        Set listenNoise with validation.

        Args:
            value: The listenNoise to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._listenNoise = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"listenNoise must be Integer or None, got {type(value).__name__}"
            )
        self._listenNoise = value
        # The number of macroticks in a communication cycle.
        self._macroPerCycle: Optional["Integer"] = None

    @property
    def macro_per_cycle(self) -> Optional["Integer"]:
        """Get macroPerCycle (Pythonic accessor)."""
        return self._macroPerCycle

    @macro_per_cycle.setter
    def macro_per_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set macroPerCycle with validation.

        Args:
            value: The macroPerCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macroPerCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"macroPerCycle must be Integer or None, got {type(value).__name__}"
            )
        self._macroPerCycle = value
        # Duration of the cluster wide nominal macrotick, expressed s.
        self._macrotick: Optional["TimeValue"] = None

    @property
    def macrotick(self) -> Optional["TimeValue"]:
        """Get macrotick (Pythonic accessor)."""
        return self._macrotick

    @macrotick.setter
    def macrotick(self, value: Optional["TimeValue"]) -> None:
        """
        Set macrotick with validation.

        Args:
            value: The macrotick to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macrotick = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"macrotick must be TimeValue or None, got {type(value).__name__}"
            )
        self._macrotick = value
        # Threshold concerning vClockCorrectionFailedCounter.
        # the number of consecutive even/odd Cycle pairs missing clock correction terms
                # that will cause the transition from the POC:normal active state to passive
                # state.
        self._maxWithout: Optional["Integer"] = None

    @property
    def max_without(self) -> Optional["Integer"]:
        """Get maxWithout (Pythonic accessor)."""
        return self._maxWithout

    @max_without.setter
    def max_without(self, value: Optional["Integer"]) -> None:
        """
        Set maxWithout with validation.

        Args:
            value: The maxWithout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxWithout = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxWithout must be Integer or None, got {type(value).__name__}"
            )
        self._maxWithout = value
        # The Offset of the action point within a minislot.
        # Unit:.
        self._minislotAction: Optional["Integer"] = None

    @property
    def minislot_action(self) -> Optional["Integer"]:
        """Get minislotAction (Pythonic accessor)."""
        return self._minislotAction

    @minislot_action.setter
    def minislot_action(self, value: Optional["Integer"]) -> None:
        """
        Set minislotAction with validation.

        Args:
            value: The minislotAction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minislotAction = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"minislotAction must be Integer or None, got {type(value).__name__}"
            )
        self._minislotAction = value
        # The duration of a minislot (dynamic segment).
        # Unit:.
        self._minislotDuration: Optional["Integer"] = None

    @property
    def minislot_duration(self) -> Optional["Integer"]:
        """Get minislotDuration (Pythonic accessor)."""
        return self._minislotDuration

    @minislot_duration.setter
    def minislot_duration(self, value: Optional["Integer"]) -> None:
        """
        Set minislotDuration with validation.

        Args:
            value: The minislotDuration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minislotDuration = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"minislotDuration must be Integer or None, got {type(value).__name__}"
            )
        self._minislotDuration = value
        # The duration of the network idle time in macroticks 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._networkIdle: Optional["Integer"] = None

    @property
    def network_idle(self) -> Optional["Integer"]:
        """Get networkIdle (Pythonic accessor)."""
        return self._networkIdle

    @network_idle.setter
    def network_idle(self, value: Optional["Integer"]) -> None:
        """
        Set networkIdle with validation.

        Args:
            value: The networkIdle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkIdle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"networkIdle must be Integer or None, got {type(value).__name__}"
            )
        self._networkIdle = value
        # Length of the Network Management vector in a cluster.
        self._network: Optional["Integer"] = None

    @property
    def network(self) -> Optional["Integer"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["Integer"]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"network must be Integer or None, got {type(value).__name__}"
            )
        self._network = value
        # Number of Minislots in the dynamic segment.
        self._numberOfMinislots: Optional["Integer"] = None

    @property
    def number_of_minislots(self) -> Optional["Integer"]:
        """Get numberOfMinislots (Pythonic accessor)."""
        return self._numberOfMinislots

    @number_of_minislots.setter
    def number_of_minislots(self, value: Optional["Integer"]) -> None:
        """
        Set numberOfMinislots with validation.

        Args:
            value: The numberOfMinislots to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOfMinislots = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"numberOfMinislots must be Integer or None, got {type(value).__name__}"
            )
        self._numberOfMinislots = value
        # The number of static slots in the static segment.
        self._numberOfStaticSlots: Optional["Integer"] = None

    @property
    def number_of_static_slots(self) -> Optional["Integer"]:
        """Get numberOfStaticSlots (Pythonic accessor)."""
        return self._numberOfStaticSlots

    @number_of_static_slots.setter
    def number_of_static_slots(self, value: Optional["Integer"]) -> None:
        """
        Set numberOfStaticSlots with validation.

        Args:
            value: The numberOfStaticSlots to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOfStaticSlots = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"numberOfStaticSlots must be Integer or None, got {type(value).__name__}"
            )
        self._numberOfStaticSlots = value
        # Start of the offset correction phase within the Network Time (NIT), expressed
                # as the number of macroticks start of cycle.
        # Unit: macroticks.
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
        # Globally configured payload length of a static frame.
        # Unit: WORDS.
        self._payloadLength: Optional["Integer"] = None

    @property
    def payload_length(self) -> Optional["Integer"]:
        """Get payloadLength (Pythonic accessor)."""
        return self._payloadLength

    @payload_length.setter
    def payload_length(self, value: Optional["Integer"]) -> None:
        """
        Set payloadLength with validation.

        Args:
            value: The payloadLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._payloadLength = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"payloadLength must be Integer or None, got {type(value).__name__}"
            )
        self._payloadLength = value
        # Additional timespan in macroticks which takes jitter into be able to set the
        # JobListPointer to the next which can be executed in case the FlexRay
        # Execution Function has be resynchronized.
        self._safetyMargin: Optional["Integer"] = None

    @property
    def safety_margin(self) -> Optional["Integer"]:
        """Get safetyMargin (Pythonic accessor)."""
        return self._safetyMargin

    @safety_margin.setter
    def safety_margin(self, value: Optional["Integer"]) -> None:
        """
        Set safetyMargin with validation.

        Args:
            value: The safetyMargin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._safetyMargin = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"safetyMargin must be Integer or None, got {type(value).__name__}"
            )
        self._safetyMargin = value
        # Sample clock period.
        # Unit: seconds.
        self._sampleClockPeriod: Optional["TimeValue"] = None

    @property
    def sample_clock_period(self) -> Optional["TimeValue"]:
        """Get sampleClockPeriod (Pythonic accessor)."""
        return self._sampleClockPeriod

    @sample_clock_period.setter
    def sample_clock_period(self, value: Optional["TimeValue"]) -> None:
        """
        Set sampleClockPeriod with validation.

        Args:
            value: The sampleClockPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sampleClockPeriod = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"sampleClockPeriod must be TimeValue or None, got {type(value).__name__}"
            )
        self._sampleClockPeriod = value
        # The duration of a slot in the static segment.
        # Unit:.
        self._staticSlot: Optional["Integer"] = None

    @property
    def static_slot(self) -> Optional["Integer"]:
        """Get staticSlot (Pythonic accessor)."""
        return self._staticSlot

    @static_slot.setter
    def static_slot(self, value: Optional["Integer"]) -> None:
        """
        Set staticSlot with validation.

        Args:
            value: The staticSlot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._staticSlot = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"staticSlot must be Integer or None, got {type(value).__name__}"
            )
        self._staticSlot = value
        # Number of macroticks the action point offset is from the of the symbol window
        # [Macroticks].
        self._symbolWindow: Optional["Integer"] = None

    @property
    def symbol_window(self) -> Optional["Integer"]:
        """Get symbolWindow (Pythonic accessor)."""
        return self._symbolWindow

    @symbol_window.setter
    def symbol_window(self, value: Optional["Integer"]) -> None:
        """
        Set symbolWindow with validation.

        Args:
            value: The symbolWindow to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolWindow = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"symbolWindow must be Integer or None, got {type(value).__name__}"
            )
        self._symbolWindow = value
        # Maximum number of distinct syncframe identifiers present a given cluster.
        # This parameter maps to FlexRay Rev.
        # A parameter gSyncNodeMax.
        self._syncFrameId: Optional["Integer"] = None

    @property
    def sync_frame_id(self) -> Optional["Integer"]:
        """Get syncFrameId (Pythonic accessor)."""
        return self._syncFrameId

    @sync_frame_id.setter
    def sync_frame_id(self, value: Optional["Integer"]) -> None:
        """
        Set syncFrameId with validation.

        Args:
            value: The syncFrameId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncFrameId = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"syncFrameId must be Integer or None, got {type(value).__name__}"
            )
        self._syncFrameId = value
        # The duration of timer t_TrcvStdbyDelay in seconds.
        # The of this parameter shall be restricted to full Flex (cycle).
        # The transceiver status setting to be delayed by this value.
        # a value or a value of 0 shall imply that the not used.
        self._tranceiver: Optional["Float"] = None

    @property
    def tranceiver(self) -> Optional["Float"]:
        """Get tranceiver (Pythonic accessor)."""
        return self._tranceiver

    @tranceiver.setter
    def tranceiver(self, value: Optional["Float"]) -> None:
        """
        Set tranceiver with validation.

        Args:
            value: The tranceiver to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tranceiver = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"tranceiver must be Float or None, got {type(value).__name__}"
            )
        self._tranceiver = value
        # Number of bits in the Transmission Start Sequence [gd.
        self._transmission: Optional["Integer"] = None

    @property
    def transmission(self) -> Optional["Integer"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["Integer"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"transmission must be Integer or None, got {type(value).__name__}"
            )
        self._transmission = value
        # Number of bits used by the node to test the duration of or HIGH phase of a
                # received wakeup.
        # Unit:bit parameter maps to FlexRay Protocol 2.
        # 1 parameter gdWakeupSymbolRxIdle.
        self._wakeupRxIdle: Optional["Integer"] = None

    @property
    def wakeup_rx_idle(self) -> Optional["Integer"]:
        """Get wakeupRxIdle (Pythonic accessor)."""
        return self._wakeupRxIdle

    @wakeup_rx_idle.setter
    def wakeup_rx_idle(self, value: Optional["Integer"]) -> None:
        """
        Set wakeupRxIdle with validation.

        Args:
            value: The wakeupRxIdle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupRxIdle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"wakeupRxIdle must be Integer or None, got {type(value).__name__}"
            )
        self._wakeupRxIdle = value
        # Number of bits used by the node to test the duration of phase of a received
                # wakeup.
        # Unit:bitDuration parameter maps to FlexRay Protocol 2.
        # 1 parameter gdWakeupSymbolRxLow.
        self._wakeupRxLow: Optional["Integer"] = None

    @property
    def wakeup_rx_low(self) -> Optional["Integer"]:
        """Get wakeupRxLow (Pythonic accessor)."""
        return self._wakeupRxLow

    @wakeup_rx_low.setter
    def wakeup_rx_low(self, value: Optional["Integer"]) -> None:
        """
        Set wakeupRxLow with validation.

        Args:
            value: The wakeupRxLow to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupRxLow = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"wakeupRxLow must be Integer or None, got {type(value).__name__}"
            )
        self._wakeupRxLow = value
        # The size of the window used to detect wakeups [gdBit].
        # This parameter maps to FlexRay Protocol 2.
        # 1 parameter gdWakeupSymbolRxWindow.
        self._wakeupRx: Optional["Integer"] = None

    @property
    def wakeup_rx(self) -> Optional["Integer"]:
        """Get wakeupRx (Pythonic accessor)."""
        return self._wakeupRx

    @wakeup_rx.setter
    def wakeup_rx(self, value: Optional["Integer"]) -> None:
        """
        Set wakeupRx with validation.

        Args:
            value: The wakeupRx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupRx = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"wakeupRx must be Integer or None, got {type(value).__name__}"
            )
        self._wakeupRx = value
        # Number of bits used by the node to transmit the LOW awakeup symbol and the
                # HIGH and LOW a WUDOP.
        # Unit:bitDuration.
        self._wakeupTxActive: Optional["Integer"] = None

    @property
    def wakeup_tx_active(self) -> Optional["Integer"]:
        """Get wakeupTxActive (Pythonic accessor)."""
        return self._wakeupTxActive

    @wakeup_tx_active.setter
    def wakeup_tx_active(self, value: Optional["Integer"]) -> None:
        """
        Set wakeupTxActive with validation.

        Args:
            value: The wakeupTxActive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupTxActive = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"wakeupTxActive must be Integer or None, got {type(value).__name__}"
            )
        self._wakeupTxActive = value
        # Number of bits used by the node to transmit the ’idle’ part wakeup symbol.
        # Unit: gDbit.
        self._wakeupTxIdle: Optional["Integer"] = None

    @property
    def wakeup_tx_idle(self) -> Optional["Integer"]:
        """Get wakeupTxIdle (Pythonic accessor)."""
        return self._wakeupTxIdle

    @wakeup_tx_idle.setter
    def wakeup_tx_idle(self, value: Optional["Integer"]) -> None:
        """
        Set wakeupTxIdle with validation.

        Args:
            value: The wakeupTxIdle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupTxIdle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"wakeupTxIdle must be Integer or None, got {type(value).__name__}"
            )
        self._wakeupTxIdle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActionPointOffset(self) -> "Integer":
        """
        AUTOSAR-compliant getter for actionPointOffset.

        Returns:
            The actionPointOffset value

        Note:
            Delegates to action_point_offset property (CODING_RULE_V2_00017)
        """
        return self.action_point_offset  # Delegates to property

    def setActionPointOffset(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for actionPointOffset with method chaining.

        Args:
            value: The actionPointOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to action_point_offset property setter (gets validation automatically)
        """
        self.action_point_offset = value  # Delegates to property setter
        return self

    def getBit(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for bit.

        Returns:
            The bit value

        Note:
            Delegates to bit property (CODING_RULE_V2_00017)
        """
        return self.bit  # Delegates to property

    def setBit(self, value: "TimeValue") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for bit with method chaining.

        Args:
            value: The bit to set

        Returns:
            self for method chaining

        Note:
            Delegates to bit property setter (gets validation automatically)
        """
        self.bit = value  # Delegates to property setter
        return self

    def getCasRxLowMax(self) -> "Integer":
        """
        AUTOSAR-compliant getter for casRxLowMax.

        Returns:
            The casRxLowMax value

        Note:
            Delegates to cas_rx_low_max property (CODING_RULE_V2_00017)
        """
        return self.cas_rx_low_max  # Delegates to property

    def setCasRxLowMax(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for casRxLowMax with method chaining.

        Args:
            value: The casRxLowMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to cas_rx_low_max property setter (gets validation automatically)
        """
        self.cas_rx_low_max = value  # Delegates to property setter
        return self

    def getColdStart(self) -> "Integer":
        """
        AUTOSAR-compliant getter for coldStart.

        Returns:
            The coldStart value

        Note:
            Delegates to cold_start property (CODING_RULE_V2_00017)
        """
        return self.cold_start  # Delegates to property

    def setColdStart(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for coldStart with method chaining.

        Args:
            value: The coldStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to cold_start property setter (gets validation automatically)
        """
        self.cold_start = value  # Delegates to property setter
        return self

    def getCycle(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for cycle.

        Returns:
            The cycle value

        Note:
            Delegates to cycle property (CODING_RULE_V2_00017)
        """
        return self.cycle  # Delegates to property

    def setCycle(self, value: "TimeValue") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for cycle with method chaining.

        Args:
            value: The cycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle property setter (gets validation automatically)
        """
        self.cycle = value  # Delegates to property setter
        return self

    def getCycleCountMax(self) -> "Integer":
        """
        AUTOSAR-compliant getter for cycleCountMax.

        Returns:
            The cycleCountMax value

        Note:
            Delegates to cycle_count_max property (CODING_RULE_V2_00017)
        """
        return self.cycle_count_max  # Delegates to property

    def setCycleCountMax(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for cycleCountMax with method chaining.

        Args:
            value: The cycleCountMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_count_max property setter (gets validation automatically)
        """
        self.cycle_count_max = value  # Delegates to property setter
        return self

    def getDetectNitError(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for detectNitError.

        Returns:
            The detectNitError value

        Note:
            Delegates to detect_nit_error property (CODING_RULE_V2_00017)
        """
        return self.detect_nit_error  # Delegates to property

    def setDetectNitError(self, value: "Boolean") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for detectNitError with method chaining.

        Args:
            value: The detectNitError to set

        Returns:
            self for method chaining

        Note:
            Delegates to detect_nit_error property setter (gets validation automatically)
        """
        self.detect_nit_error = value  # Delegates to property setter
        return self

    def getDynamicSlotIdle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for dynamicSlotIdle.

        Returns:
            The dynamicSlotIdle value

        Note:
            Delegates to dynamic_slot_idle property (CODING_RULE_V2_00017)
        """
        return self.dynamic_slot_idle  # Delegates to property

    def setDynamicSlotIdle(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for dynamicSlotIdle with method chaining.

        Args:
            value: The dynamicSlotIdle to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_slot_idle property setter (gets validation automatically)
        """
        self.dynamic_slot_idle = value  # Delegates to property setter
        return self

    def getIgnoreAfterTx(self) -> "Integer":
        """
        AUTOSAR-compliant getter for ignoreAfterTx.

        Returns:
            The ignoreAfterTx value

        Note:
            Delegates to ignore_after_tx property (CODING_RULE_V2_00017)
        """
        return self.ignore_after_tx  # Delegates to property

    def setIgnoreAfterTx(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for ignoreAfterTx with method chaining.

        Args:
            value: The ignoreAfterTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to ignore_after_tx property setter (gets validation automatically)
        """
        self.ignore_after_tx = value  # Delegates to property setter
        return self

    def getListenNoise(self) -> "Integer":
        """
        AUTOSAR-compliant getter for listenNoise.

        Returns:
            The listenNoise value

        Note:
            Delegates to listen_noise property (CODING_RULE_V2_00017)
        """
        return self.listen_noise  # Delegates to property

    def setListenNoise(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for listenNoise with method chaining.

        Args:
            value: The listenNoise to set

        Returns:
            self for method chaining

        Note:
            Delegates to listen_noise property setter (gets validation automatically)
        """
        self.listen_noise = value  # Delegates to property setter
        return self

    def getMacroPerCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for macroPerCycle.

        Returns:
            The macroPerCycle value

        Note:
            Delegates to macro_per_cycle property (CODING_RULE_V2_00017)
        """
        return self.macro_per_cycle  # Delegates to property

    def setMacroPerCycle(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for macroPerCycle with method chaining.

        Args:
            value: The macroPerCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to macro_per_cycle property setter (gets validation automatically)
        """
        self.macro_per_cycle = value  # Delegates to property setter
        return self

    def getMacrotick(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for macrotick.

        Returns:
            The macrotick value

        Note:
            Delegates to macrotick property (CODING_RULE_V2_00017)
        """
        return self.macrotick  # Delegates to property

    def setMacrotick(self, value: "TimeValue") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for macrotick with method chaining.

        Args:
            value: The macrotick to set

        Returns:
            self for method chaining

        Note:
            Delegates to macrotick property setter (gets validation automatically)
        """
        self.macrotick = value  # Delegates to property setter
        return self

    def getMaxWithout(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxWithout.

        Returns:
            The maxWithout value

        Note:
            Delegates to max_without property (CODING_RULE_V2_00017)
        """
        return self.max_without  # Delegates to property

    def setMaxWithout(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for maxWithout with method chaining.

        Args:
            value: The maxWithout to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_without property setter (gets validation automatically)
        """
        self.max_without = value  # Delegates to property setter
        return self

    def getMinislotAction(self) -> "Integer":
        """
        AUTOSAR-compliant getter for minislotAction.

        Returns:
            The minislotAction value

        Note:
            Delegates to minislot_action property (CODING_RULE_V2_00017)
        """
        return self.minislot_action  # Delegates to property

    def setMinislotAction(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for minislotAction with method chaining.

        Args:
            value: The minislotAction to set

        Returns:
            self for method chaining

        Note:
            Delegates to minislot_action property setter (gets validation automatically)
        """
        self.minislot_action = value  # Delegates to property setter
        return self

    def getMinislotDuration(self) -> "Integer":
        """
        AUTOSAR-compliant getter for minislotDuration.

        Returns:
            The minislotDuration value

        Note:
            Delegates to minislot_duration property (CODING_RULE_V2_00017)
        """
        return self.minislot_duration  # Delegates to property

    def setMinislotDuration(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for minislotDuration with method chaining.

        Args:
            value: The minislotDuration to set

        Returns:
            self for method chaining

        Note:
            Delegates to minislot_duration property setter (gets validation automatically)
        """
        self.minislot_duration = value  # Delegates to property setter
        return self

    def getNetworkIdle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for networkIdle.

        Returns:
            The networkIdle value

        Note:
            Delegates to network_idle property (CODING_RULE_V2_00017)
        """
        return self.network_idle  # Delegates to property

    def setNetworkIdle(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for networkIdle with method chaining.

        Args:
            value: The networkIdle to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_idle property setter (gets validation automatically)
        """
        self.network_idle = value  # Delegates to property setter
        return self

    def getNetwork(self) -> "Integer":
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    def getNumberOfMinislots(self) -> "Integer":
        """
        AUTOSAR-compliant getter for numberOfMinislots.

        Returns:
            The numberOfMinislots value

        Note:
            Delegates to number_of_minislots property (CODING_RULE_V2_00017)
        """
        return self.number_of_minislots  # Delegates to property

    def setNumberOfMinislots(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for numberOfMinislots with method chaining.

        Args:
            value: The numberOfMinislots to set

        Returns:
            self for method chaining

        Note:
            Delegates to number_of_minislots property setter (gets validation automatically)
        """
        self.number_of_minislots = value  # Delegates to property setter
        return self

    def getNumberOfStaticSlots(self) -> "Integer":
        """
        AUTOSAR-compliant getter for numberOfStaticSlots.

        Returns:
            The numberOfStaticSlots value

        Note:
            Delegates to number_of_static_slots property (CODING_RULE_V2_00017)
        """
        return self.number_of_static_slots  # Delegates to property

    def setNumberOfStaticSlots(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for numberOfStaticSlots with method chaining.

        Args:
            value: The numberOfStaticSlots to set

        Returns:
            self for method chaining

        Note:
            Delegates to number_of_static_slots property setter (gets validation automatically)
        """
        self.number_of_static_slots = value  # Delegates to property setter
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

    def setOffsetCorrection(self, value: "Integer") -> "FlexrayCluster":
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

    def getPayloadLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for payloadLength.

        Returns:
            The payloadLength value

        Note:
            Delegates to payload_length property (CODING_RULE_V2_00017)
        """
        return self.payload_length  # Delegates to property

    def setPayloadLength(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for payloadLength with method chaining.

        Args:
            value: The payloadLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to payload_length property setter (gets validation automatically)
        """
        self.payload_length = value  # Delegates to property setter
        return self

    def getSafetyMargin(self) -> "Integer":
        """
        AUTOSAR-compliant getter for safetyMargin.

        Returns:
            The safetyMargin value

        Note:
            Delegates to safety_margin property (CODING_RULE_V2_00017)
        """
        return self.safety_margin  # Delegates to property

    def setSafetyMargin(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for safetyMargin with method chaining.

        Args:
            value: The safetyMargin to set

        Returns:
            self for method chaining

        Note:
            Delegates to safety_margin property setter (gets validation automatically)
        """
        self.safety_margin = value  # Delegates to property setter
        return self

    def getSampleClockPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for sampleClockPeriod.

        Returns:
            The sampleClockPeriod value

        Note:
            Delegates to sample_clock_period property (CODING_RULE_V2_00017)
        """
        return self.sample_clock_period  # Delegates to property

    def setSampleClockPeriod(self, value: "TimeValue") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for sampleClockPeriod with method chaining.

        Args:
            value: The sampleClockPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to sample_clock_period property setter (gets validation automatically)
        """
        self.sample_clock_period = value  # Delegates to property setter
        return self

    def getStaticSlot(self) -> "Integer":
        """
        AUTOSAR-compliant getter for staticSlot.

        Returns:
            The staticSlot value

        Note:
            Delegates to static_slot property (CODING_RULE_V2_00017)
        """
        return self.static_slot  # Delegates to property

    def setStaticSlot(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for staticSlot with method chaining.

        Args:
            value: The staticSlot to set

        Returns:
            self for method chaining

        Note:
            Delegates to static_slot property setter (gets validation automatically)
        """
        self.static_slot = value  # Delegates to property setter
        return self

    def getSymbolWindow(self) -> "Integer":
        """
        AUTOSAR-compliant getter for symbolWindow.

        Returns:
            The symbolWindow value

        Note:
            Delegates to symbol_window property (CODING_RULE_V2_00017)
        """
        return self.symbol_window  # Delegates to property

    def setSymbolWindow(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for symbolWindow with method chaining.

        Args:
            value: The symbolWindow to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol_window property setter (gets validation automatically)
        """
        self.symbol_window = value  # Delegates to property setter
        return self

    def getSyncFrameId(self) -> "Integer":
        """
        AUTOSAR-compliant getter for syncFrameId.

        Returns:
            The syncFrameId value

        Note:
            Delegates to sync_frame_id property (CODING_RULE_V2_00017)
        """
        return self.sync_frame_id  # Delegates to property

    def setSyncFrameId(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for syncFrameId with method chaining.

        Args:
            value: The syncFrameId to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_frame_id property setter (gets validation automatically)
        """
        self.sync_frame_id = value  # Delegates to property setter
        return self

    def getTranceiver(self) -> "Float":
        """
        AUTOSAR-compliant getter for tranceiver.

        Returns:
            The tranceiver value

        Note:
            Delegates to tranceiver property (CODING_RULE_V2_00017)
        """
        return self.tranceiver  # Delegates to property

    def setTranceiver(self, value: "Float") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for tranceiver with method chaining.

        Args:
            value: The tranceiver to set

        Returns:
            self for method chaining

        Note:
            Delegates to tranceiver property setter (gets validation automatically)
        """
        self.tranceiver = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "Integer":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    def getWakeupRxIdle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for wakeupRxIdle.

        Returns:
            The wakeupRxIdle value

        Note:
            Delegates to wakeup_rx_idle property (CODING_RULE_V2_00017)
        """
        return self.wakeup_rx_idle  # Delegates to property

    def setWakeupRxIdle(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for wakeupRxIdle with method chaining.

        Args:
            value: The wakeupRxIdle to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_rx_idle property setter (gets validation automatically)
        """
        self.wakeup_rx_idle = value  # Delegates to property setter
        return self

    def getWakeupRxLow(self) -> "Integer":
        """
        AUTOSAR-compliant getter for wakeupRxLow.

        Returns:
            The wakeupRxLow value

        Note:
            Delegates to wakeup_rx_low property (CODING_RULE_V2_00017)
        """
        return self.wakeup_rx_low  # Delegates to property

    def setWakeupRxLow(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for wakeupRxLow with method chaining.

        Args:
            value: The wakeupRxLow to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_rx_low property setter (gets validation automatically)
        """
        self.wakeup_rx_low = value  # Delegates to property setter
        return self

    def getWakeupRx(self) -> "Integer":
        """
        AUTOSAR-compliant getter for wakeupRx.

        Returns:
            The wakeupRx value

        Note:
            Delegates to wakeup_rx property (CODING_RULE_V2_00017)
        """
        return self.wakeup_rx  # Delegates to property

    def setWakeupRx(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for wakeupRx with method chaining.

        Args:
            value: The wakeupRx to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_rx property setter (gets validation automatically)
        """
        self.wakeup_rx = value  # Delegates to property setter
        return self

    def getWakeupTxActive(self) -> "Integer":
        """
        AUTOSAR-compliant getter for wakeupTxActive.

        Returns:
            The wakeupTxActive value

        Note:
            Delegates to wakeup_tx_active property (CODING_RULE_V2_00017)
        """
        return self.wakeup_tx_active  # Delegates to property

    def setWakeupTxActive(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for wakeupTxActive with method chaining.

        Args:
            value: The wakeupTxActive to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_tx_active property setter (gets validation automatically)
        """
        self.wakeup_tx_active = value  # Delegates to property setter
        return self

    def getWakeupTxIdle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for wakeupTxIdle.

        Returns:
            The wakeupTxIdle value

        Note:
            Delegates to wakeup_tx_idle property (CODING_RULE_V2_00017)
        """
        return self.wakeup_tx_idle  # Delegates to property

    def setWakeupTxIdle(self, value: "Integer") -> "FlexrayCluster":
        """
        AUTOSAR-compliant setter for wakeupTxIdle with method chaining.

        Args:
            value: The wakeupTxIdle to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_tx_idle property setter (gets validation automatically)
        """
        self.wakeup_tx_idle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_action_point_offset(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set actionPointOffset and return self for chaining.

        Args:
            value: The actionPointOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_action_point_offset("value")
        """
        self.action_point_offset = value  # Use property setter (gets validation)
        return self

    def with_bit(self, value: Optional["TimeValue"]) -> "FlexrayCluster":
        """
        Set bit and return self for chaining.

        Args:
            value: The bit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bit("value")
        """
        self.bit = value  # Use property setter (gets validation)
        return self

    def with_cas_rx_low_max(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set casRxLowMax and return self for chaining.

        Args:
            value: The casRxLowMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cas_rx_low_max("value")
        """
        self.cas_rx_low_max = value  # Use property setter (gets validation)
        return self

    def with_cold_start(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set coldStart and return self for chaining.

        Args:
            value: The coldStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cold_start("value")
        """
        self.cold_start = value  # Use property setter (gets validation)
        return self

    def with_cycle(self, value: Optional["TimeValue"]) -> "FlexrayCluster":
        """
        Set cycle and return self for chaining.

        Args:
            value: The cycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle("value")
        """
        self.cycle = value  # Use property setter (gets validation)
        return self

    def with_cycle_count_max(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set cycleCountMax and return self for chaining.

        Args:
            value: The cycleCountMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_count_max("value")
        """
        self.cycle_count_max = value  # Use property setter (gets validation)
        return self

    def with_detect_nit_error(self, value: Optional["Boolean"]) -> "FlexrayCluster":
        """
        Set detectNitError and return self for chaining.

        Args:
            value: The detectNitError to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_detect_nit_error("value")
        """
        self.detect_nit_error = value  # Use property setter (gets validation)
        return self

    def with_dynamic_slot_idle(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set dynamicSlotIdle and return self for chaining.

        Args:
            value: The dynamicSlotIdle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_slot_idle("value")
        """
        self.dynamic_slot_idle = value  # Use property setter (gets validation)
        return self

    def with_ignore_after_tx(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set ignoreAfterTx and return self for chaining.

        Args:
            value: The ignoreAfterTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ignore_after_tx("value")
        """
        self.ignore_after_tx = value  # Use property setter (gets validation)
        return self

    def with_listen_noise(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set listenNoise and return self for chaining.

        Args:
            value: The listenNoise to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_listen_noise("value")
        """
        self.listen_noise = value  # Use property setter (gets validation)
        return self

    def with_macro_per_cycle(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set macroPerCycle and return self for chaining.

        Args:
            value: The macroPerCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_macro_per_cycle("value")
        """
        self.macro_per_cycle = value  # Use property setter (gets validation)
        return self

    def with_macrotick(self, value: Optional["TimeValue"]) -> "FlexrayCluster":
        """
        Set macrotick and return self for chaining.

        Args:
            value: The macrotick to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_macrotick("value")
        """
        self.macrotick = value  # Use property setter (gets validation)
        return self

    def with_max_without(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set maxWithout and return self for chaining.

        Args:
            value: The maxWithout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_without("value")
        """
        self.max_without = value  # Use property setter (gets validation)
        return self

    def with_minislot_action(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set minislotAction and return self for chaining.

        Args:
            value: The minislotAction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minislot_action("value")
        """
        self.minislot_action = value  # Use property setter (gets validation)
        return self

    def with_minislot_duration(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set minislotDuration and return self for chaining.

        Args:
            value: The minislotDuration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minislot_duration("value")
        """
        self.minislot_duration = value  # Use property setter (gets validation)
        return self

    def with_network_idle(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set networkIdle and return self for chaining.

        Args:
            value: The networkIdle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_idle("value")
        """
        self.network_idle = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_number_of_minislots(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set numberOfMinislots and return self for chaining.

        Args:
            value: The numberOfMinislots to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_number_of_minislots("value")
        """
        self.number_of_minislots = value  # Use property setter (gets validation)
        return self

    def with_number_of_static_slots(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set numberOfStaticSlots and return self for chaining.

        Args:
            value: The numberOfStaticSlots to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_number_of_static_slots("value")
        """
        self.number_of_static_slots = value  # Use property setter (gets validation)
        return self

    def with_offset_correction(self, value: Optional["Integer"]) -> "FlexrayCluster":
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

    def with_payload_length(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set payloadLength and return self for chaining.

        Args:
            value: The payloadLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_payload_length("value")
        """
        self.payload_length = value  # Use property setter (gets validation)
        return self

    def with_safety_margin(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set safetyMargin and return self for chaining.

        Args:
            value: The safetyMargin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_safety_margin("value")
        """
        self.safety_margin = value  # Use property setter (gets validation)
        return self

    def with_sample_clock_period(self, value: Optional["TimeValue"]) -> "FlexrayCluster":
        """
        Set sampleClockPeriod and return self for chaining.

        Args:
            value: The sampleClockPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sample_clock_period("value")
        """
        self.sample_clock_period = value  # Use property setter (gets validation)
        return self

    def with_static_slot(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set staticSlot and return self for chaining.

        Args:
            value: The staticSlot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_static_slot("value")
        """
        self.static_slot = value  # Use property setter (gets validation)
        return self

    def with_symbol_window(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set symbolWindow and return self for chaining.

        Args:
            value: The symbolWindow to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol_window("value")
        """
        self.symbol_window = value  # Use property setter (gets validation)
        return self

    def with_sync_frame_id(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set syncFrameId and return self for chaining.

        Args:
            value: The syncFrameId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_frame_id("value")
        """
        self.sync_frame_id = value  # Use property setter (gets validation)
        return self

    def with_tranceiver(self, value: Optional["Float"]) -> "FlexrayCluster":
        """
        Set tranceiver and return self for chaining.

        Args:
            value: The tranceiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tranceiver("value")
        """
        self.tranceiver = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self

    def with_wakeup_rx_idle(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set wakeupRxIdle and return self for chaining.

        Args:
            value: The wakeupRxIdle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_rx_idle("value")
        """
        self.wakeup_rx_idle = value  # Use property setter (gets validation)
        return self

    def with_wakeup_rx_low(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set wakeupRxLow and return self for chaining.

        Args:
            value: The wakeupRxLow to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_rx_low("value")
        """
        self.wakeup_rx_low = value  # Use property setter (gets validation)
        return self

    def with_wakeup_rx(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set wakeupRx and return self for chaining.

        Args:
            value: The wakeupRx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_rx("value")
        """
        self.wakeup_rx = value  # Use property setter (gets validation)
        return self

    def with_wakeup_tx_active(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set wakeupTxActive and return self for chaining.

        Args:
            value: The wakeupTxActive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_tx_active("value")
        """
        self.wakeup_tx_active = value  # Use property setter (gets validation)
        return self

    def with_wakeup_tx_idle(self, value: Optional["Integer"]) -> "FlexrayCluster":
        """
        Set wakeupTxIdle and return self for chaining.

        Args:
            value: The wakeupTxIdle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_tx_idle("value")
        """
        self.wakeup_tx_idle = value  # Use property setter (gets validation)
        return self
