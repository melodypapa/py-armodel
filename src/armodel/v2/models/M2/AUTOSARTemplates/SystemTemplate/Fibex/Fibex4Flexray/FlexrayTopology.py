"""
AUTOSAR Package - FlexrayTopology

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Integer,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
    PhysicalChannel,
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
        self._actionPointOffset: Optional[Integer] = None

    @property
    def action_point_offset(self) -> Optional[Integer]:
        """Get actionPointOffset (Pythonic accessor)."""
        return self._actionPointOffset

    @action_point_offset.setter
    def action_point_offset(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"actionPointOffset must be Integer or int or None, got {type(value).__name__}"
            )
        self._actionPointOffset = value
        # gdBit = cSamplesPer gdSampleClockPeriod.
        # Unit: seconds (gdBit).
        self._bit: Optional[TimeValue] = None

    @property
    def bit(self) -> Optional[TimeValue]:
        """Get bit (Pythonic accessor)."""
        return self._bit

    @bit.setter
    def bit(self, value: Optional[TimeValue]) -> None:
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
        self._casRxLowMax: Optional[Integer] = None

    @property
    def cas_rx_low_max(self) -> Optional[Integer]:
        """Get casRxLowMax (Pythonic accessor)."""
        return self._casRxLowMax

    @cas_rx_low_max.setter
    def cas_rx_low_max(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"casRxLowMax must be Integer or int or None, got {type(value).__name__}"
            )
        self._casRxLowMax = value
        # to start the cluster by initiating.
        self._coldStart: Optional[Integer] = None

    @property
    def cold_start(self) -> Optional[Integer]:
        """Get coldStart (Pythonic accessor)."""
        return self._coldStart

    @cold_start.setter
    def cold_start(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"coldStart must be Integer or int or None, got {type(value).__name__}"
            )
        self._coldStart = value
        # Unit: seconds.
        self._cycle: Optional[TimeValue] = None

    @property
    def cycle(self) -> Optional[TimeValue]:
        """Get cycle (Pythonic accessor)."""
        return self._cycle

    @cycle.setter
    def cycle(self, value: Optional[TimeValue]) -> None:
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
        # Remark: 63 for FlexRay Protocol 2.
        # 1 Rev.
        # A compliance.
        self._cycleCountMax: Optional[Integer] = None

    @property
    def cycle_count_max(self) -> Optional[Integer]:
        """Get cycleCountMax (Pythonic accessor)."""
        return self._cycleCountMax

    @cycle_count_max.setter
    def cycle_count_max(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"cycleCountMax must be Integer or int or None, got {type(value).__name__}"
            )
        self._cycleCountMax = value
        self._detectNitError: Optional[Boolean] = None

    @property
    def detect_nit_error(self) -> Optional[Boolean]:
        """Get detectNitError (Pythonic accessor)."""
        return self._detectNitError

    @detect_nit_error.setter
    def detect_nit_error(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"detectNitError must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._detectNitError = value
        self._dynamicSlotIdle: Optional[Integer] = None

    @property
    def dynamic_slot_idle(self) -> Optional[Integer]:
        """Get dynamicSlotIdle (Pythonic accessor)."""
        return self._dynamicSlotIdle

    @dynamic_slot_idle.setter
    def dynamic_slot_idle(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"dynamicSlotIdle must be Integer or int or None, got {type(value).__name__}"
            )
        self._dynamicSlotIdle = value
        self._ignoreAfterTx: Optional[Integer] = None

    @property
    def ignore_after_tx(self) -> Optional[Integer]:
        """Get ignoreAfterTx (Pythonic accessor)."""
        return self._ignoreAfterTx

    @ignore_after_tx.setter
    def ignore_after_tx(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"ignoreAfterTx must be Integer or int or None, got {type(value).__name__}"
            )
        self._ignoreAfterTx = value
        # Expressed as a multiple of the pdListenTimeout.
        # Unit microticks.
        self._listenNoise: Optional[Integer] = None

    @property
    def listen_noise(self) -> Optional[Integer]:
        """Get listenNoise (Pythonic accessor)."""
        return self._listenNoise

    @listen_noise.setter
    def listen_noise(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"listenNoise must be Integer or int or None, got {type(value).__name__}"
            )
        self._listenNoise = value
        self._macroPerCycle: Optional[Integer] = None

    @property
    def macro_per_cycle(self) -> Optional[Integer]:
        """Get macroPerCycle (Pythonic accessor)."""
        return self._macroPerCycle

    @macro_per_cycle.setter
    def macro_per_cycle(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"macroPerCycle must be Integer or int or None, got {type(value).__name__}"
            )
        self._macroPerCycle = value
        self._macrotick: Optional[TimeValue] = None

    @property
    def macrotick(self) -> Optional[TimeValue]:
        """Get macrotick (Pythonic accessor)."""
        return self._macrotick

    @macrotick.setter
    def macrotick(self, value: Optional[TimeValue]) -> None:
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
        # the number of consecutive even/odd Cycle pairs missing clock correction terms
                # that will cause the transition from the POC:normal active state to passive
                # state.
        self._maxWithout: Optional[Integer] = None

    @property
    def max_without(self) -> Optional[Integer]:
        """Get maxWithout (Pythonic accessor)."""
        return self._maxWithout

    @max_without.setter
    def max_without(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxWithout must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxWithout = value
        # Unit:.
        self._minislotAction: Optional[Integer] = None

    @property
    def minislot_action(self) -> Optional[Integer]:
        """Get minislotAction (Pythonic accessor)."""
        return self._minislotAction

    @minislot_action.setter
    def minislot_action(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"minislotAction must be Integer or int or None, got {type(value).__name__}"
            )
        self._minislotAction = value
        # Unit:.
        self._minislotDuration: Optional[Integer] = None

    @property
    def minislot_duration(self) -> Optional[Integer]:
        """Get minislotDuration (Pythonic accessor)."""
        return self._minislotDuration

    @minislot_duration.setter
    def minislot_duration(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"minislotDuration must be Integer or int or None, got {type(value).__name__}"
            )
        self._minislotDuration = value
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._networkIdle: Optional[Integer] = None

    @property
    def network_idle(self) -> Optional[Integer]:
        """Get networkIdle (Pythonic accessor)."""
        return self._networkIdle

    @network_idle.setter
    def network_idle(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"networkIdle must be Integer or int or None, got {type(value).__name__}"
            )
        self._networkIdle = value
        self._network: Optional[Integer] = None

    @property
    def network(self) -> Optional[Integer]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"network must be Integer or int or None, got {type(value).__name__}"
            )
        self._network = value
        self._numberOfMinislots: Optional[Integer] = None

    @property
    def number_of_minislots(self) -> Optional[Integer]:
        """Get numberOfMinislots (Pythonic accessor)."""
        return self._numberOfMinislots

    @number_of_minislots.setter
    def number_of_minislots(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"numberOfMinislots must be Integer or int or None, got {type(value).__name__}"
            )
        self._numberOfMinislots = value
        self._numberOfStaticSlots: Optional[Integer] = None

    @property
    def number_of_static_slots(self) -> Optional[Integer]:
        """Get numberOfStaticSlots (Pythonic accessor)."""
        return self._numberOfStaticSlots

    @number_of_static_slots.setter
    def number_of_static_slots(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"numberOfStaticSlots must be Integer or int or None, got {type(value).__name__}"
            )
        self._numberOfStaticSlots = value
                # as the number of macroticks start of cycle.
        # Unit: macroticks.
        self._offsetCorrection: Optional[Integer] = None

    @property
    def offset_correction(self) -> Optional[Integer]:
        """Get offsetCorrection (Pythonic accessor)."""
        return self._offsetCorrection

    @offset_correction.setter
    def offset_correction(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"offsetCorrection must be Integer or int or None, got {type(value).__name__}"
            )
        self._offsetCorrection = value
        # Unit: WORDS.
        self._payloadLength: Optional[Integer] = None

    @property
    def payload_length(self) -> Optional[Integer]:
        """Get payloadLength (Pythonic accessor)."""
        return self._payloadLength

    @payload_length.setter
    def payload_length(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"payloadLength must be Integer or int or None, got {type(value).__name__}"
            )
        self._payloadLength = value
        # JobListPointer to the next which can be executed in case the FlexRay
        # Execution Function has be resynchronized.
        self._safetyMargin: Optional[Integer] = None

    @property
    def safety_margin(self) -> Optional[Integer]:
        """Get safetyMargin (Pythonic accessor)."""
        return self._safetyMargin

    @safety_margin.setter
    def safety_margin(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"safetyMargin must be Integer or int or None, got {type(value).__name__}"
            )
        self._safetyMargin = value
        # Unit: seconds.
        self._sampleClockPeriod: Optional[TimeValue] = None

    @property
    def sample_clock_period(self) -> Optional[TimeValue]:
        """Get sampleClockPeriod (Pythonic accessor)."""
        return self._sampleClockPeriod

    @sample_clock_period.setter
    def sample_clock_period(self, value: Optional[TimeValue]) -> None:
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
        # Unit:.
        self._staticSlot: Optional[Integer] = None

    @property
    def static_slot(self) -> Optional[Integer]:
        """Get staticSlot (Pythonic accessor)."""
        return self._staticSlot

    @static_slot.setter
    def static_slot(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"staticSlot must be Integer or int or None, got {type(value).__name__}"
            )
        self._staticSlot = value
        # [Macroticks].
        self._symbolWindow: Optional[Integer] = None

    @property
    def symbol_window(self) -> Optional[Integer]:
        """Get symbolWindow (Pythonic accessor)."""
        return self._symbolWindow

    @symbol_window.setter
    def symbol_window(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"symbolWindow must be Integer or int or None, got {type(value).__name__}"
            )
        self._symbolWindow = value
        # This parameter maps to FlexRay Rev.
        # A parameter gSyncNodeMax.
        self._syncFrameId: Optional[Integer] = None

    @property
    def sync_frame_id(self) -> Optional[Integer]:
        """Get syncFrameId (Pythonic accessor)."""
        return self._syncFrameId

    @sync_frame_id.setter
    def sync_frame_id(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"syncFrameId must be Integer or int or None, got {type(value).__name__}"
            )
        self._syncFrameId = value
        # The of this parameter shall be restricted to full Flex (cycle).
        # The transceiver status setting to be delayed by this value.
        # a value or a value of 0 shall imply that the not used.
        self._tranceiver: Optional[Float] = None

    @property
    def tranceiver(self) -> Optional[Float]:
        """Get tranceiver (Pythonic accessor)."""
        return self._tranceiver

    @tranceiver.setter
    def tranceiver(self, value: Optional[Float]) -> None:
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

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"tranceiver must be Float or float or None, got {type(value).__name__}"
            )
        self._tranceiver = value
        self._transmission: Optional[Integer] = None

    @property
    def transmission(self) -> Optional[Integer]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"transmission must be Integer or int or None, got {type(value).__name__}"
            )
        self._transmission = value
                # received wakeup.
        # Unit:bit parameter maps to FlexRay Protocol 2.
        # 1 parameter gdWakeupSymbolRxIdle.
        self._wakeupRxIdle: Optional[Integer] = None

    @property
    def wakeup_rx_idle(self) -> Optional[Integer]:
        """Get wakeupRxIdle (Pythonic accessor)."""
        return self._wakeupRxIdle

    @wakeup_rx_idle.setter
    def wakeup_rx_idle(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"wakeupRxIdle must be Integer or int or None, got {type(value).__name__}"
            )
        self._wakeupRxIdle = value
                # wakeup.
        # Unit:bitDuration parameter maps to FlexRay Protocol 2.
        # 1 parameter gdWakeupSymbolRxLow.
        self._wakeupRxLow: Optional[Integer] = None

    @property
    def wakeup_rx_low(self) -> Optional[Integer]:
        """Get wakeupRxLow (Pythonic accessor)."""
        return self._wakeupRxLow

    @wakeup_rx_low.setter
    def wakeup_rx_low(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"wakeupRxLow must be Integer or int or None, got {type(value).__name__}"
            )
        self._wakeupRxLow = value
        # This parameter maps to FlexRay Protocol 2.
        # 1 parameter gdWakeupSymbolRxWindow.
        self._wakeupRx: Optional[Integer] = None

    @property
    def wakeup_rx(self) -> Optional[Integer]:
        """Get wakeupRx (Pythonic accessor)."""
        return self._wakeupRx

    @wakeup_rx.setter
    def wakeup_rx(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"wakeupRx must be Integer or int or None, got {type(value).__name__}"
            )
        self._wakeupRx = value
                # HIGH and LOW a WUDOP.
        # Unit:bitDuration.
        self._wakeupTxActive: Optional[Integer] = None

    @property
    def wakeup_tx_active(self) -> Optional[Integer]:
        """Get wakeupTxActive (Pythonic accessor)."""
        return self._wakeupTxActive

    @wakeup_tx_active.setter
    def wakeup_tx_active(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"wakeupTxActive must be Integer or int or None, got {type(value).__name__}"
            )
        self._wakeupTxActive = value
        # Unit: gDbit.
        self._wakeupTxIdle: Optional[Integer] = None

    @property
    def wakeup_tx_idle(self) -> Optional[Integer]:
        """Get wakeupTxIdle (Pythonic accessor)."""
        return self._wakeupTxIdle

    @wakeup_tx_idle.setter
    def wakeup_tx_idle(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"wakeupTxIdle must be Integer or int or None, got {type(value).__name__}"
            )
        self._wakeupTxIdle = value

    def with_flexray_fifo(self, value):
        """
        Set flexray_fifo and return self for chaining.

        Args:
            value: The flexray_fifo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flexray_fifo("value")
        """
        self.flexray_fifo = value  # Use property setter (gets validation)
        return self

    def with_fifo_range(self, value):
        """
        Set fifo_range and return self for chaining.

        Args:
            value: The fifo_range to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fifo_range("value")
        """
        self.fifo_range = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActionPointOffset(self) -> Integer:
        """
        AUTOSAR-compliant getter for actionPointOffset.

        Returns:
            The actionPointOffset value

        Note:
            Delegates to action_point_offset property (CODING_RULE_V2_00017)
        """
        return self.action_point_offset  # Delegates to property

    def setActionPointOffset(self, value: Integer) -> FlexrayCluster:
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

    def getBit(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for bit.

        Returns:
            The bit value

        Note:
            Delegates to bit property (CODING_RULE_V2_00017)
        """
        return self.bit  # Delegates to property

    def setBit(self, value: TimeValue) -> FlexrayCluster:
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

    def getCasRxLowMax(self) -> Integer:
        """
        AUTOSAR-compliant getter for casRxLowMax.

        Returns:
            The casRxLowMax value

        Note:
            Delegates to cas_rx_low_max property (CODING_RULE_V2_00017)
        """
        return self.cas_rx_low_max  # Delegates to property

    def setCasRxLowMax(self, value: Integer) -> FlexrayCluster:
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

    def getColdStart(self) -> Integer:
        """
        AUTOSAR-compliant getter for coldStart.

        Returns:
            The coldStart value

        Note:
            Delegates to cold_start property (CODING_RULE_V2_00017)
        """
        return self.cold_start  # Delegates to property

    def setColdStart(self, value: Integer) -> FlexrayCluster:
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

    def getCycle(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for cycle.

        Returns:
            The cycle value

        Note:
            Delegates to cycle property (CODING_RULE_V2_00017)
        """
        return self.cycle  # Delegates to property

    def setCycle(self, value: TimeValue) -> FlexrayCluster:
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

    def getCycleCountMax(self) -> Integer:
        """
        AUTOSAR-compliant getter for cycleCountMax.

        Returns:
            The cycleCountMax value

        Note:
            Delegates to cycle_count_max property (CODING_RULE_V2_00017)
        """
        return self.cycle_count_max  # Delegates to property

    def setCycleCountMax(self, value: Integer) -> FlexrayCluster:
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

    def getDetectNitError(self) -> Boolean:
        """
        AUTOSAR-compliant getter for detectNitError.

        Returns:
            The detectNitError value

        Note:
            Delegates to detect_nit_error property (CODING_RULE_V2_00017)
        """
        return self.detect_nit_error  # Delegates to property

    def setDetectNitError(self, value: Boolean) -> FlexrayCluster:
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

    def getDynamicSlotIdle(self) -> Integer:
        """
        AUTOSAR-compliant getter for dynamicSlotIdle.

        Returns:
            The dynamicSlotIdle value

        Note:
            Delegates to dynamic_slot_idle property (CODING_RULE_V2_00017)
        """
        return self.dynamic_slot_idle  # Delegates to property

    def setDynamicSlotIdle(self, value: Integer) -> FlexrayCluster:
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

    def getIgnoreAfterTx(self) -> Integer:
        """
        AUTOSAR-compliant getter for ignoreAfterTx.

        Returns:
            The ignoreAfterTx value

        Note:
            Delegates to ignore_after_tx property (CODING_RULE_V2_00017)
        """
        return self.ignore_after_tx  # Delegates to property

    def setIgnoreAfterTx(self, value: Integer) -> FlexrayCluster:
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

    def getListenNoise(self) -> Integer:
        """
        AUTOSAR-compliant getter for listenNoise.

        Returns:
            The listenNoise value

        Note:
            Delegates to listen_noise property (CODING_RULE_V2_00017)
        """
        return self.listen_noise  # Delegates to property

    def setListenNoise(self, value: Integer) -> FlexrayCluster:
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

    def getMacroPerCycle(self) -> Integer:
        """
        AUTOSAR-compliant getter for macroPerCycle.

        Returns:
            The macroPerCycle value

        Note:
            Delegates to macro_per_cycle property (CODING_RULE_V2_00017)
        """
        return self.macro_per_cycle  # Delegates to property

    def setMacroPerCycle(self, value: Integer) -> FlexrayCluster:
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

    def getMacrotick(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for macrotick.

        Returns:
            The macrotick value

        Note:
            Delegates to macrotick property (CODING_RULE_V2_00017)
        """
        return self.macrotick  # Delegates to property

    def setMacrotick(self, value: TimeValue) -> FlexrayCluster:
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

    def getMaxWithout(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxWithout.

        Returns:
            The maxWithout value

        Note:
            Delegates to max_without property (CODING_RULE_V2_00017)
        """
        return self.max_without  # Delegates to property

    def setMaxWithout(self, value: Integer) -> FlexrayCluster:
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

    def getMinislotAction(self) -> Integer:
        """
        AUTOSAR-compliant getter for minislotAction.

        Returns:
            The minislotAction value

        Note:
            Delegates to minislot_action property (CODING_RULE_V2_00017)
        """
        return self.minislot_action  # Delegates to property

    def setMinislotAction(self, value: Integer) -> FlexrayCluster:
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

    def getMinislotDuration(self) -> Integer:
        """
        AUTOSAR-compliant getter for minislotDuration.

        Returns:
            The minislotDuration value

        Note:
            Delegates to minislot_duration property (CODING_RULE_V2_00017)
        """
        return self.minislot_duration  # Delegates to property

    def setMinislotDuration(self, value: Integer) -> FlexrayCluster:
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

    def getNetworkIdle(self) -> Integer:
        """
        AUTOSAR-compliant getter for networkIdle.

        Returns:
            The networkIdle value

        Note:
            Delegates to network_idle property (CODING_RULE_V2_00017)
        """
        return self.network_idle  # Delegates to property

    def setNetworkIdle(self, value: Integer) -> FlexrayCluster:
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

    def getNetwork(self) -> Integer:
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: Integer) -> FlexrayCluster:
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

    def getNumberOfMinislots(self) -> Integer:
        """
        AUTOSAR-compliant getter for numberOfMinislots.

        Returns:
            The numberOfMinislots value

        Note:
            Delegates to number_of_minislots property (CODING_RULE_V2_00017)
        """
        return self.number_of_minislots  # Delegates to property

    def setNumberOfMinislots(self, value: Integer) -> FlexrayCluster:
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

    def getNumberOfStaticSlots(self) -> Integer:
        """
        AUTOSAR-compliant getter for numberOfStaticSlots.

        Returns:
            The numberOfStaticSlots value

        Note:
            Delegates to number_of_static_slots property (CODING_RULE_V2_00017)
        """
        return self.number_of_static_slots  # Delegates to property

    def setNumberOfStaticSlots(self, value: Integer) -> FlexrayCluster:
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

    def getOffsetCorrection(self) -> Integer:
        """
        AUTOSAR-compliant getter for offsetCorrection.

        Returns:
            The offsetCorrection value

        Note:
            Delegates to offset_correction property (CODING_RULE_V2_00017)
        """
        return self.offset_correction  # Delegates to property

    def setOffsetCorrection(self, value: Integer) -> FlexrayCluster:
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

    def getPayloadLength(self) -> Integer:
        """
        AUTOSAR-compliant getter for payloadLength.

        Returns:
            The payloadLength value

        Note:
            Delegates to payload_length property (CODING_RULE_V2_00017)
        """
        return self.payload_length  # Delegates to property

    def setPayloadLength(self, value: Integer) -> FlexrayCluster:
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

    def getSafetyMargin(self) -> Integer:
        """
        AUTOSAR-compliant getter for safetyMargin.

        Returns:
            The safetyMargin value

        Note:
            Delegates to safety_margin property (CODING_RULE_V2_00017)
        """
        return self.safety_margin  # Delegates to property

    def setSafetyMargin(self, value: Integer) -> FlexrayCluster:
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

    def getSampleClockPeriod(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for sampleClockPeriod.

        Returns:
            The sampleClockPeriod value

        Note:
            Delegates to sample_clock_period property (CODING_RULE_V2_00017)
        """
        return self.sample_clock_period  # Delegates to property

    def setSampleClockPeriod(self, value: TimeValue) -> FlexrayCluster:
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

    def getStaticSlot(self) -> Integer:
        """
        AUTOSAR-compliant getter for staticSlot.

        Returns:
            The staticSlot value

        Note:
            Delegates to static_slot property (CODING_RULE_V2_00017)
        """
        return self.static_slot  # Delegates to property

    def setStaticSlot(self, value: Integer) -> FlexrayCluster:
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

    def getSymbolWindow(self) -> Integer:
        """
        AUTOSAR-compliant getter for symbolWindow.

        Returns:
            The symbolWindow value

        Note:
            Delegates to symbol_window property (CODING_RULE_V2_00017)
        """
        return self.symbol_window  # Delegates to property

    def setSymbolWindow(self, value: Integer) -> FlexrayCluster:
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

    def getSyncFrameId(self) -> Integer:
        """
        AUTOSAR-compliant getter for syncFrameId.

        Returns:
            The syncFrameId value

        Note:
            Delegates to sync_frame_id property (CODING_RULE_V2_00017)
        """
        return self.sync_frame_id  # Delegates to property

    def setSyncFrameId(self, value: Integer) -> FlexrayCluster:
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

    def getTranceiver(self) -> Float:
        """
        AUTOSAR-compliant getter for tranceiver.

        Returns:
            The tranceiver value

        Note:
            Delegates to tranceiver property (CODING_RULE_V2_00017)
        """
        return self.tranceiver  # Delegates to property

    def setTranceiver(self, value: Float) -> FlexrayCluster:
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

    def getTransmission(self) -> Integer:
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: Integer) -> FlexrayCluster:
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

    def getWakeupRxIdle(self) -> Integer:
        """
        AUTOSAR-compliant getter for wakeupRxIdle.

        Returns:
            The wakeupRxIdle value

        Note:
            Delegates to wakeup_rx_idle property (CODING_RULE_V2_00017)
        """
        return self.wakeup_rx_idle  # Delegates to property

    def setWakeupRxIdle(self, value: Integer) -> FlexrayCluster:
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

    def getWakeupRxLow(self) -> Integer:
        """
        AUTOSAR-compliant getter for wakeupRxLow.

        Returns:
            The wakeupRxLow value

        Note:
            Delegates to wakeup_rx_low property (CODING_RULE_V2_00017)
        """
        return self.wakeup_rx_low  # Delegates to property

    def setWakeupRxLow(self, value: Integer) -> FlexrayCluster:
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

    def getWakeupRx(self) -> Integer:
        """
        AUTOSAR-compliant getter for wakeupRx.

        Returns:
            The wakeupRx value

        Note:
            Delegates to wakeup_rx property (CODING_RULE_V2_00017)
        """
        return self.wakeup_rx  # Delegates to property

    def setWakeupRx(self, value: Integer) -> FlexrayCluster:
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

    def getWakeupTxActive(self) -> Integer:
        """
        AUTOSAR-compliant getter for wakeupTxActive.

        Returns:
            The wakeupTxActive value

        Note:
            Delegates to wakeup_tx_active property (CODING_RULE_V2_00017)
        """
        return self.wakeup_tx_active  # Delegates to property

    def setWakeupTxActive(self, value: Integer) -> FlexrayCluster:
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

    def getWakeupTxIdle(self) -> Integer:
        """
        AUTOSAR-compliant getter for wakeupTxIdle.

        Returns:
            The wakeupTxIdle value

        Note:
            Delegates to wakeup_tx_idle property (CODING_RULE_V2_00017)
        """
        return self.wakeup_tx_idle  # Delegates to property

    def setWakeupTxIdle(self, value: Integer) -> FlexrayCluster:
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

    def with_action_point_offset(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_bit(self, value: Optional[TimeValue]) -> FlexrayCluster:
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

    def with_cas_rx_low_max(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_cold_start(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_cycle(self, value: Optional[TimeValue]) -> FlexrayCluster:
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

    def with_cycle_count_max(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_detect_nit_error(self, value: Optional[Boolean]) -> FlexrayCluster:
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

    def with_dynamic_slot_idle(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_ignore_after_tx(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_listen_noise(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_macro_per_cycle(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_macrotick(self, value: Optional[TimeValue]) -> FlexrayCluster:
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

    def with_max_without(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_minislot_action(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_minislot_duration(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_network_idle(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_network(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_number_of_minislots(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_number_of_static_slots(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_offset_correction(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_payload_length(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_safety_margin(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_sample_clock_period(self, value: Optional[TimeValue]) -> FlexrayCluster:
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

    def with_static_slot(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_symbol_window(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_sync_frame_id(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_tranceiver(self, value: Optional[Float]) -> FlexrayCluster:
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

    def with_transmission(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_wakeup_rx_idle(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_wakeup_rx_low(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_wakeup_rx(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_wakeup_tx_active(self, value: Optional[Integer]) -> FlexrayCluster:
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

    def with_wakeup_tx_idle(self, value: Optional[Integer]) -> FlexrayCluster:
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



class FlexrayCommunicationController(ARObject):
    """
    FlexRay bus specific communication port attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayCommunicationController

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
        self._accepted: Optional[Integer] = None

    @property
    def accepted(self) -> Optional[Integer]:
        """Get accepted (Pythonic accessor)."""
        return self._accepted

    @accepted.setter
    def accepted(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"accepted must be Integer or int or None, got {type(value).__name__}"
            )
        self._accepted = value
                # synchronization errors.
        # If set to true, Controller is allowed to transition to set to false, the
                # Communication Controller transition to the POC:halt state but will enter or
                # the normal POC (passive State).
        self._allowHaltDueTo: Optional[Boolean] = None

    @property
    def allow_halt_due_to(self) -> Optional[Boolean]:
        """Get allowHaltDueTo (Pythonic accessor)."""
        return self._allowHaltDueTo

    @allow_halt_due_to.setter
    def allow_halt_due_to(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"allowHaltDueTo must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._allowHaltDueTo = value
        # terms before the will be allowed to transition POC:normal passive state to
        # POC:normal active set to 0, the Communication Controller is not transition
        # from POC:norm.
        self._allowPassiveTo: Optional[Integer] = None

    @property
    def allow_passive_to(self) -> Optional[Integer]:
        """Get allowPassiveTo (Pythonic accessor)."""
        return self._allowPassiveTo

    @allow_passive_to.setter
    def allow_passive_to(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"allowPassiveTo must be Integer or int or None, got {type(value).__name__}"
            )
        self._allowPassiveTo = value
        self._clusterDrift: Optional[Integer] = None

    @property
    def cluster_drift(self) -> Optional[Integer]:
        """Get clusterDrift (Pythonic accessor)."""
        return self._clusterDrift

    @cluster_drift.setter
    def cluster_drift(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"clusterDrift must be Integer or int or None, got {type(value).__name__}"
            )
        self._clusterDrift = value
        # point and secondary time Unit: Microticks (pDecodingCorrection).
        self._decoding: Optional[Integer] = None

    @property
    def decoding(self) -> Optional[Integer]:
        """Get decoding (Pythonic accessor)."""
        return self._decoding

    @decoding.setter
    def decoding(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"decoding must be Integer or int or None, got {type(value).__name__}"
            )
        self._decoding = value
        # Unit: Microticks.
        # This optional parameter shall filled out if channel B is used.
        self._delay: Optional[Integer] = None

    @property
    def delay(self) -> Optional[Integer]:
        """Get delay (Pythonic accessor)."""
        return self._delay

    @delay.setter
    def delay(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"delay must be Integer or int or None, got {type(value).__name__}"
            )
        self._delay = value
        # Triggered External Sync cluster) or locally.
        self._externalSync: Optional[Boolean] = None

    @property
    def external_sync(self) -> Optional[Boolean]:
        """Get externalSync (Pythonic accessor)."""
        return self._externalSync

    @external_sync.setter
    def external_sync(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"externalSync must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._externalSync = value
        # external offset correction, node-local microticks.
        self._externOffset: Optional[Integer] = None

    @property
    def extern_offset(self) -> Optional[Integer]:
        """Get externOffset (Pythonic accessor)."""
        return self._externOffset

    @extern_offset.setter
    def extern_offset(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"externOffset must be Integer or int or None, got {type(value).__name__}"
            )
        self._externOffset = value
        # external rate correction, node-local microticks.
        self._externRate: Optional[Integer] = None

    @property
    def extern_rate(self) -> Optional[Integer]:
        """Get externRate (Pythonic accessor)."""
        return self._externRate

    @extern_rate.setter
    def extern_rate(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"externRate must be Integer or int or None, got {type(value).__name__}"
            )
        self._externRate = value
        # when synchronization with Gateway Source node is lost (pFallBackInternal or
        # will instead go to POC:ready (pFallBackInternal.
        self._fallBackInternal: Optional[Boolean] = None

    @property
    def fall_back_internal(self) -> Optional[Boolean]:
        """Get fallBackInternal (Pythonic accessor)."""
        return self._fallBackInternal

    @fall_back_internal.setter
    def fall_back_internal(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"fallBackInternal must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._fallBackInternal = value
        # criteria to the FIFO.
        self._flexrayFifo: List["FlexrayFifo"] = []

    @property
    def flexray_fifo(self) -> List["FlexrayFifo"]:
        """Get flexrayFifo (Pythonic accessor)."""
        return self._flexrayFifo
        # ID of the slot used to transmit the startup frame, sync designated single
                # slot frame.
        # If the attributes or keySlot set to true the key slot value is.
        self._keySlotID: Optional[PositiveInteger] = None

    @property
    def key_slot_id(self) -> Optional[PositiveInteger]:
        """Get keySlotID (Pythonic accessor)."""
        return self._keySlotID

    @key_slot_id.setter
    def key_slot_id(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"keySlotID must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._keySlotID = value
        # startup.
        self._keySlotOnly: Optional[Boolean] = None

    @property
    def key_slot_only(self) -> Optional[Boolean]:
        """Get keySlotOnly (Pythonic accessor)."""
        return self._keySlotOnly

    @key_slot_only.setter
    def key_slot_only(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"keySlotOnly must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._keySlotOnly = value
        self._keySlotUsedFor: Optional[Boolean] = None

    @property
    def key_slot_used_for(self) -> Optional[Boolean]:
        """Get keySlotUsedFor (Pythonic accessor)."""
        return self._keySlotUsedFor

    @key_slot_used_for.setter
    def key_slot_used_for(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"keySlotUsedFor must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._keySlotUsedFor = value
        # segment for the respective node.
        self._latestTX: Optional[Integer] = None

    @property
    def latest_tx(self) -> Optional[Integer]:
        """Get latestTX (Pythonic accessor)."""
        return self._latestTX

    @latest_tx.setter
    def latest_tx(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"latestTX must be Integer or int or None, got {type(value).__name__}"
            )
        self._latestTX = value
                # parameter, the real of this value should be the same for all the cluster.
        # Unit: Microticks.
        self._listenTimeout: Optional[Integer] = None

    @property
    def listen_timeout(self) -> Optional[Integer]:
        """Get listenTimeout (Pythonic accessor)."""
        return self._listenTimeout

    @listen_timeout.setter
    def listen_timeout(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"listenTimeout must be Integer or int or None, got {type(value).__name__}"
            )
        self._listenTimeout = value
                # macrotick boundary of the reference point based on the nominal
                # (pMacroInitialOffset).
        # This optional only be filled out if channel B is used.
        self._macroInitial: Optional[Integer] = None

    @property
    def macro_initial(self) -> Optional[Integer]:
        """Get macroInitial (Pythonic accessor)."""
        return self._macroInitial

    @macro_initial.setter
    def macro_initial(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"macroInitial must be Integer or int or None, got {type(value).__name__}"
            )
        self._macroInitial = value
        self._maximum: Optional[Integer] = None

    @property
    def maximum(self) -> Optional[Integer]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maximum must be Integer or int or None, got {type(value).__name__}"
            )
        self._maximum = value
                # gMacroInitialOffset and the reference point.
        # The parameter depends and therefore it has to be set each channel.
        # This optional parameter be filled out if channel B is used.
        self._microInitial: Optional[Integer] = None

    @property
    def micro_initial(self) -> Optional[Integer]:
        """Get microInitial (Pythonic accessor)."""
        return self._microInitial

    @micro_initial.setter
    def micro_initial(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"microInitial must be Integer or int or None, got {type(value).__name__}"
            )
        self._microInitial = value
        self._microPerCycle: Optional[Integer] = None

    @property
    def micro_per_cycle(self) -> Optional[Integer]:
        """Get microPerCycle (Pythonic accessor)."""
        return self._microPerCycle

    @micro_per_cycle.setter
    def micro_per_cycle(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"microPerCycle must be Integer or int or None, got {type(value).__name__}"
            )
        self._microPerCycle = value
        # This attribute can be derived from and gdSampleClockPeriod.
        # Unit:.
        self._microtick: Optional[TimeValue] = None

    @property
    def microtick(self) -> Optional[TimeValue]:
        """Get microtick (Pythonic accessor)."""
        return self._microtick

    @microtick.setter
    def microtick(self, value: Optional[TimeValue]) -> None:
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
                # place.
        # If set to update shall take place after the NIT.
        # If set to update shall take place after the end of the static.
        self._nmVectorEarly: Optional[Boolean] = None

    @property
    def nm_vector_early(self) -> Optional[Boolean]:
        """Get nmVectorEarly (Pythonic accessor)."""
        return self._nmVectorEarly

    @nm_vector_early.setter
    def nm_vector_early(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmVectorEarly must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmVectorEarly = value
        # (pOffsetCorrectionOut).
        self._offsetCorrection: Optional[Integer] = None

    @property
    def offset_correction(self) -> Optional[Integer]:
        """Get offsetCorrection (Pythonic accessor)."""
        return self._offsetCorrection

    @offset_correction.setter
    def offset_correction(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"offsetCorrection must be Integer or int or None, got {type(value).__name__}"
            )
        self._offsetCorrection = value
                # offset between two nodes unsynchronized clocks for one Unit:Microticks
                # (pRateCorrection parameter maps to FlexRay Protocol 2.
        # 1 parameter pdMaxDrift.
        self._rateCorrection: Optional[Integer] = None

    @property
    def rate_correction(self) -> Optional[Integer]:
        """Get rateCorrection (Pythonic accessor)."""
        return self._rateCorrection

    @rate_correction.setter
    def rate_correction(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"rateCorrection must be Integer or int or None, got {type(value).__name__}"
            )
        self._rateCorrection = value
        self._samplesPerMicrotick: Optional[Integer] = None

    @property
    def samples_per_microtick(self) -> Optional[Integer]:
        """Get samplesPerMicrotick (Pythonic accessor)."""
        return self._samplesPerMicrotick

    @samples_per_microtick.setter
    def samples_per_microtick(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"samplesPerMicrotick must be Integer or int or None, got {type(value).__name__}"
            )
        self._samplesPerMicrotick = value
                # Time Triggered Local Master TT-E Time Triggered External Sync mode.
        # If this set to zero the node does not have a second.
        self._secondKeySlot: Optional[PositiveInteger] = None

    @property
    def second_key_slot(self) -> Optional[PositiveInteger]:
        """Get secondKeySlot (Pythonic accessor)."""
        return self._secondKeySlot

    @second_key_slot.setter
    def second_key_slot(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"secondKeySlot must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._secondKeySlot = value
        # External Sync or TT-L Time Master Sync cluster.
        self._twoKeySlot: Optional[Boolean] = None

    @property
    def two_key_slot(self) -> Optional[Boolean]:
        """Get twoKeySlot (Pythonic accessor)."""
        return self._twoKeySlot

    @two_key_slot.setter
    def two_key_slot(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"twoKeySlot must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._twoKeySlot = value
        # of this Node in the.
        self._wakeUpPattern: Optional[Integer] = None

    @property
    def wake_up_pattern(self) -> Optional[Integer]:
        """Get wakeUpPattern (Pythonic accessor)."""
        return self._wakeUpPattern

    @wake_up_pattern.setter
    def wake_up_pattern(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"wakeUpPattern must be Integer or int or None, got {type(value).__name__}"
            )
        self._wakeUpPattern = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccepted(self) -> Integer:
        """
        AUTOSAR-compliant getter for accepted.

        Returns:
            The accepted value

        Note:
            Delegates to accepted property (CODING_RULE_V2_00017)
        """
        return self.accepted  # Delegates to property

    def setAccepted(self, value: Integer) -> FlexrayCommunicationController:
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

    def getAllowHaltDueTo(self) -> Boolean:
        """
        AUTOSAR-compliant getter for allowHaltDueTo.

        Returns:
            The allowHaltDueTo value

        Note:
            Delegates to allow_halt_due_to property (CODING_RULE_V2_00017)
        """
        return self.allow_halt_due_to  # Delegates to property

    def setAllowHaltDueTo(self, value: Boolean) -> FlexrayCommunicationController:
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

    def getAllowPassiveTo(self) -> Integer:
        """
        AUTOSAR-compliant getter for allowPassiveTo.

        Returns:
            The allowPassiveTo value

        Note:
            Delegates to allow_passive_to property (CODING_RULE_V2_00017)
        """
        return self.allow_passive_to  # Delegates to property

    def setAllowPassiveTo(self, value: Integer) -> FlexrayCommunicationController:
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

    def getClusterDrift(self) -> Integer:
        """
        AUTOSAR-compliant getter for clusterDrift.

        Returns:
            The clusterDrift value

        Note:
            Delegates to cluster_drift property (CODING_RULE_V2_00017)
        """
        return self.cluster_drift  # Delegates to property

    def setClusterDrift(self, value: Integer) -> FlexrayCommunicationController:
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

    def getDecoding(self) -> Integer:
        """
        AUTOSAR-compliant getter for decoding.

        Returns:
            The decoding value

        Note:
            Delegates to decoding property (CODING_RULE_V2_00017)
        """
        return self.decoding  # Delegates to property

    def setDecoding(self, value: Integer) -> FlexrayCommunicationController:
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

    def getDelay(self) -> Integer:
        """
        AUTOSAR-compliant getter for delay.

        Returns:
            The delay value

        Note:
            Delegates to delay property (CODING_RULE_V2_00017)
        """
        return self.delay  # Delegates to property

    def setDelay(self, value: Integer) -> FlexrayCommunicationController:
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

    def getExternalSync(self) -> Boolean:
        """
        AUTOSAR-compliant getter for externalSync.

        Returns:
            The externalSync value

        Note:
            Delegates to external_sync property (CODING_RULE_V2_00017)
        """
        return self.external_sync  # Delegates to property

    def setExternalSync(self, value: Boolean) -> FlexrayCommunicationController:
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

    def getExternOffset(self) -> Integer:
        """
        AUTOSAR-compliant getter for externOffset.

        Returns:
            The externOffset value

        Note:
            Delegates to extern_offset property (CODING_RULE_V2_00017)
        """
        return self.extern_offset  # Delegates to property

    def setExternOffset(self, value: Integer) -> FlexrayCommunicationController:
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

    def getExternRate(self) -> Integer:
        """
        AUTOSAR-compliant getter for externRate.

        Returns:
            The externRate value

        Note:
            Delegates to extern_rate property (CODING_RULE_V2_00017)
        """
        return self.extern_rate  # Delegates to property

    def setExternRate(self, value: Integer) -> FlexrayCommunicationController:
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

    def getFallBackInternal(self) -> Boolean:
        """
        AUTOSAR-compliant getter for fallBackInternal.

        Returns:
            The fallBackInternal value

        Note:
            Delegates to fall_back_internal property (CODING_RULE_V2_00017)
        """
        return self.fall_back_internal  # Delegates to property

    def setFallBackInternal(self, value: Boolean) -> FlexrayCommunicationController:
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

    def getKeySlotID(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for keySlotID.

        Returns:
            The keySlotID value

        Note:
            Delegates to key_slot_id property (CODING_RULE_V2_00017)
        """
        return self.key_slot_id  # Delegates to property

    def setKeySlotID(self, value: PositiveInteger) -> FlexrayCommunicationController:
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

    def getKeySlotOnly(self) -> Boolean:
        """
        AUTOSAR-compliant getter for keySlotOnly.

        Returns:
            The keySlotOnly value

        Note:
            Delegates to key_slot_only property (CODING_RULE_V2_00017)
        """
        return self.key_slot_only  # Delegates to property

    def setKeySlotOnly(self, value: Boolean) -> FlexrayCommunicationController:
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

    def getKeySlotUsedFor(self) -> Boolean:
        """
        AUTOSAR-compliant getter for keySlotUsedFor.

        Returns:
            The keySlotUsedFor value

        Note:
            Delegates to key_slot_used_for property (CODING_RULE_V2_00017)
        """
        return self.key_slot_used_for  # Delegates to property

    def setKeySlotUsedFor(self, value: Boolean) -> FlexrayCommunicationController:
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

    def getLatestTX(self) -> Integer:
        """
        AUTOSAR-compliant getter for latestTX.

        Returns:
            The latestTX value

        Note:
            Delegates to latest_tx property (CODING_RULE_V2_00017)
        """
        return self.latest_tx  # Delegates to property

    def setLatestTX(self, value: Integer) -> FlexrayCommunicationController:
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

    def getListenTimeout(self) -> Integer:
        """
        AUTOSAR-compliant getter for listenTimeout.

        Returns:
            The listenTimeout value

        Note:
            Delegates to listen_timeout property (CODING_RULE_V2_00017)
        """
        return self.listen_timeout  # Delegates to property

    def setListenTimeout(self, value: Integer) -> FlexrayCommunicationController:
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

    def getMacroInitial(self) -> Integer:
        """
        AUTOSAR-compliant getter for macroInitial.

        Returns:
            The macroInitial value

        Note:
            Delegates to macro_initial property (CODING_RULE_V2_00017)
        """
        return self.macro_initial  # Delegates to property

    def setMacroInitial(self, value: Integer) -> FlexrayCommunicationController:
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

    def getMaximum(self) -> Integer:
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: Integer) -> FlexrayCommunicationController:
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

    def getMicroInitial(self) -> Integer:
        """
        AUTOSAR-compliant getter for microInitial.

        Returns:
            The microInitial value

        Note:
            Delegates to micro_initial property (CODING_RULE_V2_00017)
        """
        return self.micro_initial  # Delegates to property

    def setMicroInitial(self, value: Integer) -> FlexrayCommunicationController:
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

    def getMicroPerCycle(self) -> Integer:
        """
        AUTOSAR-compliant getter for microPerCycle.

        Returns:
            The microPerCycle value

        Note:
            Delegates to micro_per_cycle property (CODING_RULE_V2_00017)
        """
        return self.micro_per_cycle  # Delegates to property

    def setMicroPerCycle(self, value: Integer) -> FlexrayCommunicationController:
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

    def getMicrotick(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for microtick.

        Returns:
            The microtick value

        Note:
            Delegates to microtick property (CODING_RULE_V2_00017)
        """
        return self.microtick  # Delegates to property

    def setMicrotick(self, value: TimeValue) -> FlexrayCommunicationController:
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

    def getNmVectorEarly(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmVectorEarly.

        Returns:
            The nmVectorEarly value

        Note:
            Delegates to nm_vector_early property (CODING_RULE_V2_00017)
        """
        return self.nm_vector_early  # Delegates to property

    def setNmVectorEarly(self, value: Boolean) -> FlexrayCommunicationController:
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

    def getOffsetCorrection(self) -> Integer:
        """
        AUTOSAR-compliant getter for offsetCorrection.

        Returns:
            The offsetCorrection value

        Note:
            Delegates to offset_correction property (CODING_RULE_V2_00017)
        """
        return self.offset_correction  # Delegates to property

    def setOffsetCorrection(self, value: Integer) -> FlexrayCommunicationController:
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

    def getRateCorrection(self) -> Integer:
        """
        AUTOSAR-compliant getter for rateCorrection.

        Returns:
            The rateCorrection value

        Note:
            Delegates to rate_correction property (CODING_RULE_V2_00017)
        """
        return self.rate_correction  # Delegates to property

    def setRateCorrection(self, value: Integer) -> FlexrayCommunicationController:
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

    def getSamplesPerMicrotick(self) -> Integer:
        """
        AUTOSAR-compliant getter for samplesPerMicrotick.

        Returns:
            The samplesPerMicrotick value

        Note:
            Delegates to samples_per_microtick property (CODING_RULE_V2_00017)
        """
        return self.samples_per_microtick  # Delegates to property

    def setSamplesPerMicrotick(self, value: Integer) -> FlexrayCommunicationController:
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

    def getSecondKeySlot(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for secondKeySlot.

        Returns:
            The secondKeySlot value

        Note:
            Delegates to second_key_slot property (CODING_RULE_V2_00017)
        """
        return self.second_key_slot  # Delegates to property

    def setSecondKeySlot(self, value: PositiveInteger) -> FlexrayCommunicationController:
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

    def getTwoKeySlot(self) -> Boolean:
        """
        AUTOSAR-compliant getter for twoKeySlot.

        Returns:
            The twoKeySlot value

        Note:
            Delegates to two_key_slot property (CODING_RULE_V2_00017)
        """
        return self.two_key_slot  # Delegates to property

    def setTwoKeySlot(self, value: Boolean) -> FlexrayCommunicationController:
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

    def getWakeUpPattern(self) -> Integer:
        """
        AUTOSAR-compliant getter for wakeUpPattern.

        Returns:
            The wakeUpPattern value

        Note:
            Delegates to wake_up_pattern property (CODING_RULE_V2_00017)
        """
        return self.wake_up_pattern  # Delegates to property

    def setWakeUpPattern(self, value: Integer) -> FlexrayCommunicationController:
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

    def with_accepted(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_allow_halt_due_to(self, value: Optional[Boolean]) -> FlexrayCommunicationController:
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

    def with_allow_passive_to(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_cluster_drift(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_decoding(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_delay(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_external_sync(self, value: Optional[Boolean]) -> FlexrayCommunicationController:
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

    def with_extern_offset(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_extern_rate(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_fall_back_internal(self, value: Optional[Boolean]) -> FlexrayCommunicationController:
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

    def with_key_slot_id(self, value: Optional[PositiveInteger]) -> FlexrayCommunicationController:
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

    def with_key_slot_only(self, value: Optional[Boolean]) -> FlexrayCommunicationController:
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

    def with_key_slot_used_for(self, value: Optional[Boolean]) -> FlexrayCommunicationController:
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

    def with_latest_tx(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_listen_timeout(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_macro_initial(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_maximum(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_micro_initial(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_micro_per_cycle(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_microtick(self, value: Optional[TimeValue]) -> FlexrayCommunicationController:
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

    def with_nm_vector_early(self, value: Optional[Boolean]) -> FlexrayCommunicationController:
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

    def with_offset_correction(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_rate_correction(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_samples_per_microtick(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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

    def with_second_key_slot(self, value: Optional[PositiveInteger]) -> FlexrayCommunicationController:
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

    def with_two_key_slot(self, value: Optional[Boolean]) -> FlexrayCommunicationController:
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

    def with_wake_up_pattern(self, value: Optional[Integer]) -> FlexrayCommunicationController:
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



class FlexrayFifoConfiguration(ARObject):
    """
    One First In First Out (FIFO) queued receive structure, defining the
    admittance criteria to the FIFO, and mandating the ability to admit messages
    into the FIFO based on Message Id filtering criteria.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayFifoConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 87, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Boolean configuration which determines whether or not received in the dynamic
        # segment that don’t message ID will be admitted into the FIFO.
        self._admitWithout: Optional[Boolean] = None

    @property
    def admit_without(self) -> Optional[Boolean]:
        """Get admitWithout (Pythonic accessor)."""
        return self._admitWithout

    @admit_without.setter
    def admit_without(self, value: Optional[Boolean]) -> None:
        """
        Set admitWithout with validation.

        Args:
            value: The admitWithout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._admitWithout = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"admitWithout must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._admitWithout = value
        self._baseCycle: Optional[Integer] = None

    @property
    def base_cycle(self) -> Optional[Integer]:
        """Get baseCycle (Pythonic accessor)."""
        return self._baseCycle

    @base_cycle.setter
    def base_cycle(self, value: Optional[Integer]) -> None:
        """
        Set baseCycle with validation.

        Args:
            value: The baseCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseCycle = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"baseCycle must be Integer or int or None, got {type(value).__name__}"
            )
        self._baseCycle = value
        self._channel: Optional[FlexrayPhysicalChannel] = None

    @property
    def channel(self) -> Optional[FlexrayPhysicalChannel]:
        """Get channel (Pythonic accessor)."""
        return self._channel

    @channel.setter
    def channel(self, value: Optional[FlexrayPhysicalChannel]) -> None:
        """
        Set channel with validation.

        Args:
            value: The channel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channel = None
            return

        if not isinstance(value, FlexrayPhysicalChannel):
            raise TypeError(
                f"channel must be FlexrayPhysicalChannel or None, got {type(value).__name__}"
            )
        self._channel = value
        self._cycleRepetition: Optional[Integer] = None

    @property
    def cycle_repetition(self) -> Optional[Integer]:
        """Get cycleRepetition (Pythonic accessor)."""
        return self._cycleRepetition

    @cycle_repetition.setter
    def cycle_repetition(self, value: Optional[Integer]) -> None:
        """
        Set cycleRepetition with validation.

        Args:
            value: The cycleRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleRepetition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"cycleRepetition must be Integer or int or None, got {type(value).__name__}"
            )
        self._cycleRepetition = value
        self._fifoDepth: Optional[Integer] = None

    @property
    def fifo_depth(self) -> Optional[Integer]:
        """Get fifoDepth (Pythonic accessor)."""
        return self._fifoDepth

    @fifo_depth.setter
    def fifo_depth(self, value: Optional[Integer]) -> None:
        """
        Set fifoDepth with validation.

        Args:
            value: The fifoDepth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fifoDepth = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"fifoDepth must be Integer or int or None, got {type(value).__name__}"
            )
        self._fifoDepth = value
        self._fifoRange: List[FlexrayFifoRange] = []

    @property
    def fifo_range(self) -> List[FlexrayFifoRange]:
        """Get fifoRange (Pythonic accessor)."""
        return self._fifoRange
        # FIFO message identifier acceptance criteria (Mask filter).
        self._msgIdMask: Optional[Integer] = None

    @property
    def msg_id_mask(self) -> Optional[Integer]:
        """Get msgIdMask (Pythonic accessor)."""
        return self._msgIdMask

    @msg_id_mask.setter
    def msg_id_mask(self, value: Optional[Integer]) -> None:
        """
        Set msgIdMask with validation.

        Args:
            value: The msgIdMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._msgIdMask = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"msgIdMask must be Integer or int or None, got {type(value).__name__}"
            )
        self._msgIdMask = value
        self._msgIdMatch: Optional[Integer] = None

    @property
    def msg_id_match(self) -> Optional[Integer]:
        """Get msgIdMatch (Pythonic accessor)."""
        return self._msgIdMatch

    @msg_id_match.setter
    def msg_id_match(self, value: Optional[Integer]) -> None:
        """
        Set msgIdMatch with validation.

        Args:
            value: The msgIdMatch to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._msgIdMatch = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"msgIdMatch must be Integer or int or None, got {type(value).__name__}"
            )
        self._msgIdMatch = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdmitWithout(self) -> Boolean:
        """
        AUTOSAR-compliant getter for admitWithout.

        Returns:
            The admitWithout value

        Note:
            Delegates to admit_without property (CODING_RULE_V2_00017)
        """
        return self.admit_without  # Delegates to property

    def setAdmitWithout(self, value: Boolean) -> FlexrayFifoConfiguration:
        """
        AUTOSAR-compliant setter for admitWithout with method chaining.

        Args:
            value: The admitWithout to set

        Returns:
            self for method chaining

        Note:
            Delegates to admit_without property setter (gets validation automatically)
        """
        self.admit_without = value  # Delegates to property setter
        return self

    def getBaseCycle(self) -> Integer:
        """
        AUTOSAR-compliant getter for baseCycle.

        Returns:
            The baseCycle value

        Note:
            Delegates to base_cycle property (CODING_RULE_V2_00017)
        """
        return self.base_cycle  # Delegates to property

    def setBaseCycle(self, value: Integer) -> FlexrayFifoConfiguration:
        """
        AUTOSAR-compliant setter for baseCycle with method chaining.

        Args:
            value: The baseCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_cycle property setter (gets validation automatically)
        """
        self.base_cycle = value  # Delegates to property setter
        return self

    def getChannel(self) -> FlexrayPhysicalChannel:
        """
        AUTOSAR-compliant getter for channel.

        Returns:
            The channel value

        Note:
            Delegates to channel property (CODING_RULE_V2_00017)
        """
        return self.channel  # Delegates to property

    def setChannel(self, value: FlexrayPhysicalChannel) -> FlexrayFifoConfiguration:
        """
        AUTOSAR-compliant setter for channel with method chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel property setter (gets validation automatically)
        """
        self.channel = value  # Delegates to property setter
        return self

    def getCycleRepetition(self) -> Integer:
        """
        AUTOSAR-compliant getter for cycleRepetition.

        Returns:
            The cycleRepetition value

        Note:
            Delegates to cycle_repetition property (CODING_RULE_V2_00017)
        """
        return self.cycle_repetition  # Delegates to property

    def setCycleRepetition(self, value: Integer) -> FlexrayFifoConfiguration:
        """
        AUTOSAR-compliant setter for cycleRepetition with method chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_repetition property setter (gets validation automatically)
        """
        self.cycle_repetition = value  # Delegates to property setter
        return self

    def getFifoDepth(self) -> Integer:
        """
        AUTOSAR-compliant getter for fifoDepth.

        Returns:
            The fifoDepth value

        Note:
            Delegates to fifo_depth property (CODING_RULE_V2_00017)
        """
        return self.fifo_depth  # Delegates to property

    def setFifoDepth(self, value: Integer) -> FlexrayFifoConfiguration:
        """
        AUTOSAR-compliant setter for fifoDepth with method chaining.

        Args:
            value: The fifoDepth to set

        Returns:
            self for method chaining

        Note:
            Delegates to fifo_depth property setter (gets validation automatically)
        """
        self.fifo_depth = value  # Delegates to property setter
        return self

    def getFifoRange(self) -> List[FlexrayFifoRange]:
        """
        AUTOSAR-compliant getter for fifoRange.

        Returns:
            The fifoRange value

        Note:
            Delegates to fifo_range property (CODING_RULE_V2_00017)
        """
        return self.fifo_range  # Delegates to property

    def getMsgIdMask(self) -> Integer:
        """
        AUTOSAR-compliant getter for msgIdMask.

        Returns:
            The msgIdMask value

        Note:
            Delegates to msg_id_mask property (CODING_RULE_V2_00017)
        """
        return self.msg_id_mask  # Delegates to property

    def setMsgIdMask(self, value: Integer) -> FlexrayFifoConfiguration:
        """
        AUTOSAR-compliant setter for msgIdMask with method chaining.

        Args:
            value: The msgIdMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to msg_id_mask property setter (gets validation automatically)
        """
        self.msg_id_mask = value  # Delegates to property setter
        return self

    def getMsgIdMatch(self) -> Integer:
        """
        AUTOSAR-compliant getter for msgIdMatch.

        Returns:
            The msgIdMatch value

        Note:
            Delegates to msg_id_match property (CODING_RULE_V2_00017)
        """
        return self.msg_id_match  # Delegates to property

    def setMsgIdMatch(self, value: Integer) -> FlexrayFifoConfiguration:
        """
        AUTOSAR-compliant setter for msgIdMatch with method chaining.

        Args:
            value: The msgIdMatch to set

        Returns:
            self for method chaining

        Note:
            Delegates to msg_id_match property setter (gets validation automatically)
        """
        self.msg_id_match = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_admit_without(self, value: Optional[Boolean]) -> FlexrayFifoConfiguration:
        """
        Set admitWithout and return self for chaining.

        Args:
            value: The admitWithout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_admit_without("value")
        """
        self.admit_without = value  # Use property setter (gets validation)
        return self

    def with_base_cycle(self, value: Optional[Integer]) -> FlexrayFifoConfiguration:
        """
        Set baseCycle and return self for chaining.

        Args:
            value: The baseCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_cycle("value")
        """
        self.base_cycle = value  # Use property setter (gets validation)
        return self

    def with_channel(self, value: Optional[FlexrayPhysicalChannel]) -> FlexrayFifoConfiguration:
        """
        Set channel and return self for chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel("value")
        """
        self.channel = value  # Use property setter (gets validation)
        return self

    def with_cycle_repetition(self, value: Optional[Integer]) -> FlexrayFifoConfiguration:
        """
        Set cycleRepetition and return self for chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_repetition("value")
        """
        self.cycle_repetition = value  # Use property setter (gets validation)
        return self

    def with_fifo_depth(self, value: Optional[Integer]) -> FlexrayFifoConfiguration:
        """
        Set fifoDepth and return self for chaining.

        Args:
            value: The fifoDepth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fifo_depth("value")
        """
        self.fifo_depth = value  # Use property setter (gets validation)
        return self

    def with_msg_id_mask(self, value: Optional[Integer]) -> FlexrayFifoConfiguration:
        """
        Set msgIdMask and return self for chaining.

        Args:
            value: The msgIdMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msg_id_mask("value")
        """
        self.msg_id_mask = value  # Use property setter (gets validation)
        return self

    def with_msg_id_match(self, value: Optional[Integer]) -> FlexrayFifoConfiguration:
        """
        Set msgIdMatch and return self for chaining.

        Args:
            value: The msgIdMatch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msg_id_match("value")
        """
        self.msg_id_match = value  # Use property setter (gets validation)
        return self



class FlexrayFifoRange(ARObject):
    """
    FIFO Frame Id range acceptance criteria.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayFifoRange

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 87, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Max Range.
        self._rangeMax: Optional[Integer] = None

    @property
    def range_max(self) -> Optional[Integer]:
        """Get rangeMax (Pythonic accessor)."""
        return self._rangeMax

    @range_max.setter
    def range_max(self, value: Optional[Integer]) -> None:
        """
        Set rangeMax with validation.

        Args:
            value: The rangeMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rangeMax = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"rangeMax must be Integer or int or None, got {type(value).__name__}"
            )
        self._rangeMax = value
        self._rangeMin: Optional[Integer] = None

    @property
    def range_min(self) -> Optional[Integer]:
        """Get rangeMin (Pythonic accessor)."""
        return self._rangeMin

    @range_min.setter
    def range_min(self, value: Optional[Integer]) -> None:
        """
        Set rangeMin with validation.

        Args:
            value: The rangeMin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rangeMin = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"rangeMin must be Integer or int or None, got {type(value).__name__}"
            )
        self._rangeMin = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRangeMax(self) -> Integer:
        """
        AUTOSAR-compliant getter for rangeMax.

        Returns:
            The rangeMax value

        Note:
            Delegates to range_max property (CODING_RULE_V2_00017)
        """
        return self.range_max  # Delegates to property

    def setRangeMax(self, value: Integer) -> FlexrayFifoRange:
        """
        AUTOSAR-compliant setter for rangeMax with method chaining.

        Args:
            value: The rangeMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to range_max property setter (gets validation automatically)
        """
        self.range_max = value  # Delegates to property setter
        return self

    def getRangeMin(self) -> Integer:
        """
        AUTOSAR-compliant getter for rangeMin.

        Returns:
            The rangeMin value

        Note:
            Delegates to range_min property (CODING_RULE_V2_00017)
        """
        return self.range_min  # Delegates to property

    def setRangeMin(self, value: Integer) -> FlexrayFifoRange:
        """
        AUTOSAR-compliant setter for rangeMin with method chaining.

        Args:
            value: The rangeMin to set

        Returns:
            self for method chaining

        Note:
            Delegates to range_min property setter (gets validation automatically)
        """
        self.range_min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_range_max(self, value: Optional[Integer]) -> FlexrayFifoRange:
        """
        Set rangeMax and return self for chaining.

        Args:
            value: The rangeMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_range_max("value")
        """
        self.range_max = value  # Use property setter (gets validation)
        return self

    def with_range_min(self, value: Optional[Integer]) -> FlexrayFifoRange:
        """
        Set rangeMin and return self for chaining.

        Args:
            value: The rangeMin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_range_min("value")
        """
        self.range_min = value  # Use property setter (gets validation)
        return self



class FlexrayCommunicationConnector(CommunicationConnector):
    """
    FlexRay specific attributes to the CommunicationConnector

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayCommunicationConnector

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value of this attribute influences the shutdown of the FlexRay NM.
        # FrNm switches to bus sleep seconds after the completion last repetition cycle
                # containing a NM vote.
        self._nmReadySleep: Optional[Float] = None

    @property
    def nm_ready_sleep(self) -> Optional[Float]:
        """Get nmReadySleep (Pythonic accessor)."""
        return self._nmReadySleep

    @nm_ready_sleep.setter
    def nm_ready_sleep(self, value: Optional[Float]) -> None:
        """
        Set nmReadySleep with validation.

        Args:
            value: The nmReadySleep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmReadySleep = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"nmReadySleep must be Float or float or None, got {type(value).__name__}"
            )
        self._nmReadySleep = value
        self._wakeUp: Optional[Boolean] = None

    @property
    def wake_up(self) -> Optional[Boolean]:
        """Get wakeUp (Pythonic accessor)."""
        return self._wakeUp

    @wake_up.setter
    def wake_up(self, value: Optional[Boolean]) -> None:
        """
        Set wakeUp with validation.

        Args:
            value: The wakeUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeUp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"wakeUp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._wakeUp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmReadySleep(self) -> Float:
        """
        AUTOSAR-compliant getter for nmReadySleep.

        Returns:
            The nmReadySleep value

        Note:
            Delegates to nm_ready_sleep property (CODING_RULE_V2_00017)
        """
        return self.nm_ready_sleep  # Delegates to property

    def setNmReadySleep(self, value: Float) -> FlexrayCommunicationConnector:
        """
        AUTOSAR-compliant setter for nmReadySleep with method chaining.

        Args:
            value: The nmReadySleep to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_ready_sleep property setter (gets validation automatically)
        """
        self.nm_ready_sleep = value  # Delegates to property setter
        return self

    def getWakeUp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for wakeUp.

        Returns:
            The wakeUp value

        Note:
            Delegates to wake_up property (CODING_RULE_V2_00017)
        """
        return self.wake_up  # Delegates to property

    def setWakeUp(self, value: Boolean) -> FlexrayCommunicationConnector:
        """
        AUTOSAR-compliant setter for wakeUp with method chaining.

        Args:
            value: The wakeUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to wake_up property setter (gets validation automatically)
        """
        self.wake_up = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_ready_sleep(self, value: Optional[Float]) -> FlexrayCommunicationConnector:
        """
        Set nmReadySleep and return self for chaining.

        Args:
            value: The nmReadySleep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_ready_sleep("value")
        """
        self.nm_ready_sleep = value  # Use property setter (gets validation)
        return self

    def with_wake_up(self, value: Optional[Boolean]) -> FlexrayCommunicationConnector:
        """
        Set wakeUp and return self for chaining.

        Args:
            value: The wakeUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wake_up("value")
        """
        self.wake_up = value  # Use property setter (gets validation)
        return self



class FlexrayPhysicalChannel(PhysicalChannel):
    """
    FlexRay specific attributes to the physicalChannel

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayPhysicalChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Name of the channel (Channel A or Channel B).
        self._channelName: Optional[FlexrayChannelName] = None

    @property
    def channel_name(self) -> Optional[FlexrayChannelName]:
        """Get channelName (Pythonic accessor)."""
        return self._channelName

    @channel_name.setter
    def channel_name(self, value: Optional[FlexrayChannelName]) -> None:
        """
        Set channelName with validation.

        Args:
            value: The channelName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channelName = None
            return

        if not isinstance(value, FlexrayChannelName):
            raise TypeError(
                f"channelName must be FlexrayChannelName or None, got {type(value).__name__}"
            )
        self._channelName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChannelName(self) -> FlexrayChannelName:
        """
        AUTOSAR-compliant getter for channelName.

        Returns:
            The channelName value

        Note:
            Delegates to channel_name property (CODING_RULE_V2_00017)
        """
        return self.channel_name  # Delegates to property

    def setChannelName(self, value: FlexrayChannelName) -> FlexrayPhysicalChannel:
        """
        AUTOSAR-compliant setter for channelName with method chaining.

        Args:
            value: The channelName to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel_name property setter (gets validation automatically)
        """
        self.channel_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_channel_name(self, value: Optional[FlexrayChannelName]) -> FlexrayPhysicalChannel:
        """
        Set channelName and return self for chaining.

        Args:
            value: The channelName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel_name("value")
        """
        self.channel_name = value  # Use property setter (gets validation)
        return self


class FlexrayChannelName(AREnum):
    """
    FlexrayChannelName enumeration

Name of the channel. Aggregated by FlexrayPhysicalChannel.channelName

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology
    """
    # Channel A
    channelA = "0"

    # Channel B
    channelB = "1"
