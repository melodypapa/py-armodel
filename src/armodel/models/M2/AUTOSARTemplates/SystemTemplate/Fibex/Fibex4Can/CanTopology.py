# This module contains AUTOSAR System Template classes for CAN topology
# It defines CAN controllers, connectors, and their configuration attributes

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController


class CanControllerFdConfiguration(ARObject):
    """Bit timing related configuration of a CAN controller for payload and CRC of a CAN FD frame."""

    # CanControllerFdConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.16, p.66
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPaddingValue              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPaddingValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPropSeg                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPropSeg                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSspOffset                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSspOffset                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSyncJumpWidth             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSyncJumpWidth             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSeg1                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeSeg1                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSeg2                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeSeg2                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTxBitRateSwitch           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTxBitRateSwitch           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the value which is used to pad unused data in CAN FD frames which are bigger than 8 byte if the length of a Pdu which was requested to be sent does not match the allowed DLC values of CAN FD.
        self.paddingValue: Optional[PositiveInteger] = None

        # Specifies propagation delay in time quantas.
        self.propSeg: Optional[PositiveInteger] = None

        # Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled.
        self.sspOffset: Optional[PositiveInteger] = None

        # Specifies the synchronization jump width for the controller in time quantas.
        self.syncJumpWidth: Optional[PositiveInteger] = None

        # Specifies phase segment 1 in time quantas.
        self.timeSeg1: Optional[PositiveInteger] = None

        # Specifies phase segment 2 in time quantas.
        self.timeSeg2: Optional[PositiveInteger] = None

        # Specifies if the bit rate switching shall be used for transmissions. TRUE: CAN FD frames shall be sent with bit rate switching. FALSE: CAN FD frames shall be sent without bit rate switching.
        self.txBitRateSwitch: Optional[Boolean] = None

    def getPaddingValue(self) -> Optional[PositiveInteger]:
        """
        Specifies the value which is used to pad unused data in CAN FD frames which are bigger than 8 byte if the length of a Pdu which was requested to be sent does not match the allowed DLC values of CAN FD.
        """
        return self.paddingValue

    def setPaddingValue(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfiguration":
        """
        Specifies the value which is used to pad unused data in CAN FD frames which are bigger than 8 byte if the length of a Pdu which was requested to be sent does not match the allowed DLC values of CAN FD.
        A None value is a no-op and does not overwrite an existing paddingValue.
        """
        if value is not None:
            self.paddingValue = value
        return self

    def getPropSeg(self) -> Optional[PositiveInteger]:
        """
        Specifies propagation delay in time quantas.
        """
        return self.propSeg

    def setPropSeg(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfiguration":
        """
        Specifies propagation delay in time quantas.
        A None value is a no-op and does not overwrite an existing propSeg.
        """
        if value is not None:
            self.propSeg = value
        return self

    def getSspOffset(self) -> Optional[PositiveInteger]:
        """
        Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled.
        """
        return self.sspOffset

    def setSspOffset(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfiguration":
        """
        Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled.
        A None value is a no-op and does not overwrite an existing sspOffset.
        """
        if value is not None:
            self.sspOffset = value
        return self

    def getSyncJumpWidth(self) -> Optional[PositiveInteger]:
        """
        Specifies the synchronization jump width for the controller in time quantas.
        """
        return self.syncJumpWidth

    def setSyncJumpWidth(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfiguration":
        """
        Specifies the synchronization jump width for the controller in time quantas.
        A None value is a no-op and does not overwrite an existing syncJumpWidth.
        """
        if value is not None:
            self.syncJumpWidth = value
        return self

    def getTimeSeg1(self) -> Optional[PositiveInteger]:
        """
        Specifies phase segment 1 in time quantas.
        """
        return self.timeSeg1

    def setTimeSeg1(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfiguration":
        """
        Specifies phase segment 1 in time quantas.
        A None value is a no-op and does not overwrite an existing timeSeg1.
        """
        if value is not None:
            self.timeSeg1 = value
        return self

    def getTimeSeg2(self) -> Optional[PositiveInteger]:
        """
        Specifies phase segment 2 in time quantas.
        """
        return self.timeSeg2

    def setTimeSeg2(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfiguration":
        """
        Specifies phase segment 2 in time quantas.
        A None value is a no-op and does not overwrite an existing timeSeg2.
        """
        if value is not None:
            self.timeSeg2 = value
        return self

    def getTxBitRateSwitch(self) -> Optional[Boolean]:
        """
        Specifies if the bit rate switching shall be used for transmissions. TRUE: CAN FD frames shall be sent with bit rate switching. FALSE: CAN FD frames shall be sent without bit rate switching.
        """
        return self.txBitRateSwitch

    def setTxBitRateSwitch(self, value: Optional[Boolean]) -> "CanControllerFdConfiguration":
        """
        Specifies if the bit rate switching shall be used for transmissions. TRUE: CAN FD frames shall be sent with bit rate switching. FALSE: CAN FD frames shall be sent without bit rate switching.
        A None value is a no-op and does not overwrite an existing txBitRateSwitch.
        """
        if value is not None:
            self.txBitRateSwitch = value
        return self


class CanControllerFdConfigurationRequirements(ARObject):
    """
    Specifies the requirements for CAN FD configuration parameters, defining
    the acceptable ranges and constraints for timing, bit rate, and other
    CAN FD communication properties.
    """

    # CanControllerFdConfigurationRequirements method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxSyncJumpWidth          [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxSyncJumpWidth          [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxTrcvDelayCompensationOffset [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxTrcvDelayCompensationOffset [x] impl  [ ] docstring  [ ] test
    # [ ] getMinNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] setMinNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] getMinSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] setMinSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] getMinSyncJumpWidth          [x] impl  [ ] docstring  [ ] test
    # [ ] setMinSyncJumpWidth          [x] impl  [ ] docstring  [ ] test
    # [ ] getMinTrcvDelayCompensationOffset [x] impl  [ ] docstring  [ ] test
    # [ ] setMinTrcvDelayCompensationOffset [x] impl  [ ] docstring  [ ] test
    # [ ] getPaddingValue              [x] impl  [ ] docstring  [ ] test
    # [ ] setPaddingValue              [x] impl  [ ] docstring  [ ] test
    # [ ] getTxBitRateSwitch           [x] impl  [ ] docstring  [ ] test
    # [ ] setTxBitRateSwitch           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.maxNumberOfTimeQuantaPerBit: Integer = None
        self.maxSamplePoint: Float = None
        self.maxSyncJumpWidth: Float = None
        self.maxTrcvDelayCompensationOffset: TimeValue = None
        self.minNumberOfTimeQuantaPerBit: Integer = None
        self.minSamplePoint: Float = None
        self.minSyncJumpWidth: Float = None
        self.minTrcvDelayCompensationOffset: TimeValue = None
        self.paddingValue: PositiveInteger = None
        self.txBitRateSwitch: Boolean = None

    def getMaxNumberOfTimeQuantaPerBit(self):
        return self.maxNumberOfTimeQuantaPerBit

    def setMaxNumberOfTimeQuantaPerBit(self, value):
        if value is not None:
            self.maxNumberOfTimeQuantaPerBit = value
        return self

    def getMaxSamplePoint(self):
        return self.maxSamplePoint

    def setMaxSamplePoint(self, value):
        if value is not None:
            self.maxSamplePoint = value
        return self

    def getMaxSyncJumpWidth(self):
        return self.maxSyncJumpWidth

    def setMaxSyncJumpWidth(self, value):
        if value is not None:
            self.maxSyncJumpWidth = value
        return self

    def getMaxTrcvDelayCompensationOffset(self):
        return self.maxTrcvDelayCompensationOffset

    def setMaxTrcvDelayCompensationOffset(self, value):
        if value is not None:
            self.maxTrcvDelayCompensationOffset = value
        return self

    def getMinNumberOfTimeQuantaPerBit(self):
        return self.minNumberOfTimeQuantaPerBit

    def setMinNumberOfTimeQuantaPerBit(self, value):
        if value is not None:
            self.minNumberOfTimeQuantaPerBit = value
        return self

    def getMinSamplePoint(self):
        return self.minSamplePoint

    def setMinSamplePoint(self, value):
        if value is not None:
            self.minSamplePoint = value
        return self

    def getMinSyncJumpWidth(self):
        return self.minSyncJumpWidth

    def setMinSyncJumpWidth(self, value):
        if value is not None:
            self.minSyncJumpWidth = value
        return self

    def getMinTrcvDelayCompensationOffset(self):
        return self.minTrcvDelayCompensationOffset

    def setMinTrcvDelayCompensationOffset(self, value):
        if value is not None:
            self.minTrcvDelayCompensationOffset = value
        return self

    def getPaddingValue(self):
        return self.paddingValue

    def setPaddingValue(self, value):
        if value is not None:
            self.paddingValue = value
        return self

    def getTxBitRateSwitch(self):
        return self.txBitRateSwitch

    def setTxBitRateSwitch(self, value):
        if value is not None:
            self.txBitRateSwitch = value
        return self


class CanControllerXlConfiguration(ARObject):
    """This meta-class represents the CAN XL-specific controller attributes."""

    # CanControllerXlConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.18, p.71
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getErrorSignalingEnabled     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setErrorSignalingEnabled     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPropSeg                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPropSeg                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPwmL                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPwmL                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPwmO                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPwmO                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPwmS                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPwmS                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSspOffset                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSspOffset                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSyncJumpWidth             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSyncJumpWidth             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSeg1                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeSeg1                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSeg2                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeSeg2                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTrcvPwmModeEnabled        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTrcvPwmModeEnabled        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled.
        self.errorSignalingEnabled: Optional[Boolean] = None

        # Specifies propagation delay in time quantas.
        self.propSeg: Optional[PositiveInteger] = None

        # Specifies the PWM long phase length.
        self.pwmL: Optional[PositiveInteger] = None

        # Specifies the PWM time offset.
        self.pwmO: Optional[PositiveInteger] = None

        # Specifies the PWM short phase length.
        self.pwmS: Optional[PositiveInteger] = None

        # Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled.
        self.sspOffset: Optional[PositiveInteger] = None

        # Specifies the synchronization jump width for the controller in time quantas.
        self.syncJumpWidth: Optional[PositiveInteger] = None

        # Specifies phase segment 1 in time quantas.
        self.timeSeg1: Optional[PositiveInteger] = None

        # Specifies phase segment 2 in time quantas.
        self.timeSeg2: Optional[PositiveInteger] = None

        # Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode.
        self.trcvPwmModeEnabled: Optional[Boolean] = None

    def getErrorSignalingEnabled(self) -> Optional[Boolean]:
        """Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled."""
        return self.errorSignalingEnabled

    def setErrorSignalingEnabled(self, value: Optional[Boolean]) -> "CanControllerXlConfiguration":
        """Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled.
        A None value is a no-op and does not overwrite an existing errorSignalingEnabled."""
        if value is not None:
            self.errorSignalingEnabled = value
        return self

    def getPropSeg(self) -> Optional[PositiveInteger]:
        """Specifies propagation delay in time quantas."""
        return self.propSeg

    def setPropSeg(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies propagation delay in time quantas.
        A None value is a no-op and does not overwrite an existing propSeg."""
        if value is not None:
            self.propSeg = value
        return self

    def getPwmL(self) -> Optional[PositiveInteger]:
        """Specifies the PWM long phase length."""
        return self.pwmL

    def setPwmL(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies the PWM long phase length.
        A None value is a no-op and does not overwrite an existing pwmL."""
        if value is not None:
            self.pwmL = value
        return self

    def getPwmO(self) -> Optional[PositiveInteger]:
        """Specifies the PWM time offset."""
        return self.pwmO

    def setPwmO(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies the PWM time offset.
        A None value is a no-op and does not overwrite an existing pwmO."""
        if value is not None:
            self.pwmO = value
        return self

    def getPwmS(self) -> Optional[PositiveInteger]:
        """Specifies the PWM short phase length."""
        return self.pwmS

    def setPwmS(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies the PWM short phase length.
        A None value is a no-op and does not overwrite an existing pwmS."""
        if value is not None:
            self.pwmS = value
        return self

    def getSspOffset(self) -> Optional[PositiveInteger]:
        """Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled."""
        return self.sspOffset

    def setSspOffset(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled.
        A None value is a no-op and does not overwrite an existing sspOffset."""
        if value is not None:
            self.sspOffset = value
        return self

    def getSyncJumpWidth(self) -> Optional[PositiveInteger]:
        """Specifies the synchronization jump width for the controller in time quantas."""
        return self.syncJumpWidth

    def setSyncJumpWidth(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies the synchronization jump width for the controller in time quantas.
        A None value is a no-op and does not overwrite an existing syncJumpWidth."""
        if value is not None:
            self.syncJumpWidth = value
        return self

    def getTimeSeg1(self) -> Optional[PositiveInteger]:
        """Specifies phase segment 1 in time quantas."""
        return self.timeSeg1

    def setTimeSeg1(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies phase segment 1 in time quantas.
        A None value is a no-op and does not overwrite an existing timeSeg1."""
        if value is not None:
            self.timeSeg1 = value
        return self

    def getTimeSeg2(self) -> Optional[PositiveInteger]:
        """Specifies phase segment 2 in time quantas."""
        return self.timeSeg2

    def setTimeSeg2(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfiguration":
        """Specifies phase segment 2 in time quantas.
        A None value is a no-op and does not overwrite an existing timeSeg2."""
        if value is not None:
            self.timeSeg2 = value
        return self

    def getTrcvPwmModeEnabled(self) -> Optional[Boolean]:
        """Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode."""
        return self.trcvPwmModeEnabled

    def setTrcvPwmModeEnabled(self, value: Optional[Boolean]) -> "CanControllerXlConfiguration":
        """Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode.
        A None value is a no-op and does not overwrite an existing trcvPwmModeEnabled."""
        if value is not None:
            self.trcvPwmModeEnabled = value
        return self


class CanControllerXlConfigurationRequirements(ARObject):
    """This element allows the specification of ranges for the CAN XL configuration parameters. These ranges are taken as requirements and have to be respected by the ECU developer."""

    # CanControllerXlConfigurationRequirements method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.19, p.72
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getErrorSignalingEnabled           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setErrorSignalingEnabled           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxNumberOfTimeQuantaPerBit     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxNumberOfTimeQuantaPerBit     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxPwmL                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxPwmL                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxPwmO                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxPwmO                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxPwmS                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxPwmS                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxSamplePoint                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxSamplePoint                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxSyncJumpWidth                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxSyncJumpWidth                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxTrcvDelayCompensationOffset  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxTrcvDelayCompensationOffset  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinNumberOfTimeQuantaPerBit     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinNumberOfTimeQuantaPerBit     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinPwmL                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinPwmL                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinPwmO                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinPwmO                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinPwmS                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinPwmS                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinSamplePoint                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinSamplePoint                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinSyncJumpWidth                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinSyncJumpWidth                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinTrcvDelayCompensationOffset  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinTrcvDelayCompensationOffset  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTrcvPwmModeEnabled              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTrcvPwmModeEnabled              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled.
        self.errorSignalingEnabled: Optional[Boolean] = None

        # Maximum number of time quanta in the bit time.
        self.maxNumberOfTimeQuantaPerBit: Optional[Integer] = None

        # Specifies the maximum PWM long phase length.
        self.maxPwmL: Optional[PositiveInteger] = None

        # Specifies the minimum PWM time offset.
        self.maxPwmO: Optional[PositiveInteger] = None

        # Specifies the maximum PWM short phase length.
        self.maxPwmS: Optional[PositiveInteger] = None

        # The max. value of the sample point as a percentage of the total bit time.
        self.maxSamplePoint: Optional[Float] = None

        # The max. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors.
        self.maxSyncJumpWidth: Optional[Float] = None

        # Specifies the maximum Transceiver Delay Compensation Offset in seconds. If not specified Transceiver Delay Compensation is disabled.
        self.maxTrcvDelayCompensationOffset: Optional[TimeValue] = None

        # Minimum number of time quantas in the bit time.
        self.minNumberOfTimeQuantaPerBit: Optional[Integer] = None

        # Specifies the minimum PWM long phase length.
        self.minPwmL: Optional[PositiveInteger] = None

        # Specifies the maximum PWM time offset.
        self.minPwmO: Optional[PositiveInteger] = None

        # Specifies the minimum PWM short phase length.
        self.minPwmS: Optional[PositiveInteger] = None

        # The min. value of the sample point as a percentage of the total bit time.
        self.minSamplePoint: Optional[Float] = None

        # The min. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors.
        self.minSyncJumpWidth: Optional[Float] = None

        # Specifies the minimum Transceiver Delay Compensation Offset in seconds. If not specified Transmitter Delay Compensation is disabled.
        self.minTrcvDelayCompensationOffset: Optional[TimeValue] = None

        # Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode.
        self.trcvPwmModeEnabled: Optional[Boolean] = None

    def getErrorSignalingEnabled(self) -> Optional[Boolean]:
        """Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled."""
        return self.errorSignalingEnabled

    def setErrorSignalingEnabled(self, value: Optional[Boolean]) -> "CanControllerXlConfigurationRequirements":
        """Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled.
        A None value is a no-op and does not overwrite an existing errorSignalingEnabled."""
        if value is not None:
            self.errorSignalingEnabled = value
        return self

    def getMaxNumberOfTimeQuantaPerBit(self) -> Optional[Integer]:
        """Maximum number of time quanta in the bit time."""
        return self.maxNumberOfTimeQuantaPerBit

    def setMaxNumberOfTimeQuantaPerBit(self, value: Optional[Integer]) -> "CanControllerXlConfigurationRequirements":
        """Maximum number of time quanta in the bit time.
        A None value is a no-op and does not overwrite an existing maxNumberOfTimeQuantaPerBit."""
        if value is not None:
            self.maxNumberOfTimeQuantaPerBit = value
        return self

    def getMaxPwmL(self) -> Optional[PositiveInteger]:
        """Specifies the maximum PWM long phase length."""
        return self.maxPwmL

    def setMaxPwmL(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the maximum PWM long phase length.
        A None value is a no-op and does not overwrite an existing maxPwmL."""
        if value is not None:
            self.maxPwmL = value
        return self

    def getMaxPwmO(self) -> Optional[PositiveInteger]:
        """Specifies the minimum PWM time offset."""
        return self.maxPwmO

    def setMaxPwmO(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the minimum PWM time offset.
        A None value is a no-op and does not overwrite an existing maxPwmO."""
        if value is not None:
            self.maxPwmO = value
        return self

    def getMaxPwmS(self) -> Optional[PositiveInteger]:
        """Specifies the maximum PWM short phase length."""
        return self.maxPwmS

    def setMaxPwmS(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the maximum PWM short phase length.
        A None value is a no-op and does not overwrite an existing maxPwmS."""
        if value is not None:
            self.maxPwmS = value
        return self

    def getMaxSamplePoint(self) -> Optional[Float]:
        """The max. value of the sample point as a percentage of the total bit time."""
        return self.maxSamplePoint

    def setMaxSamplePoint(self, value: Optional[Float]) -> "CanControllerXlConfigurationRequirements":
        """The max. value of the sample point as a percentage of the total bit time.
        A None value is a no-op and does not overwrite an existing maxSamplePoint."""
        if value is not None:
            self.maxSamplePoint = value
        return self

    def getMaxSyncJumpWidth(self) -> Optional[Float]:
        """The max. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."""
        return self.maxSyncJumpWidth

    def setMaxSyncJumpWidth(self, value: Optional[Float]) -> "CanControllerXlConfigurationRequirements":
        """The max. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors.
        A None value is a no-op and does not overwrite an existing maxSyncJumpWidth."""
        if value is not None:
            self.maxSyncJumpWidth = value
        return self

    def getMaxTrcvDelayCompensationOffset(self) -> Optional[TimeValue]:
        """Specifies the maximum Transceiver Delay Compensation Offset in seconds. If not specified Transceiver Delay Compensation is disabled."""
        return self.maxTrcvDelayCompensationOffset

    def setMaxTrcvDelayCompensationOffset(self, value: Optional[TimeValue]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the maximum Transceiver Delay Compensation Offset in seconds. If not specified Transceiver Delay Compensation is disabled.
        A None value is a no-op and does not overwrite an existing maxTrcvDelayCompensationOffset."""
        if value is not None:
            self.maxTrcvDelayCompensationOffset = value
        return self

    def getMinNumberOfTimeQuantaPerBit(self) -> Optional[Integer]:
        """Minimum number of time quantas in the bit time."""
        return self.minNumberOfTimeQuantaPerBit

    def setMinNumberOfTimeQuantaPerBit(self, value: Optional[Integer]) -> "CanControllerXlConfigurationRequirements":
        """Minimum number of time quantas in the bit time.
        A None value is a no-op and does not overwrite an existing minNumberOfTimeQuantaPerBit."""
        if value is not None:
            self.minNumberOfTimeQuantaPerBit = value
        return self

    def getMinPwmL(self) -> Optional[PositiveInteger]:
        """Specifies the minimum PWM long phase length."""
        return self.minPwmL

    def setMinPwmL(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the minimum PWM long phase length.
        A None value is a no-op and does not overwrite an existing minPwmL."""
        if value is not None:
            self.minPwmL = value
        return self

    def getMinPwmO(self) -> Optional[PositiveInteger]:
        """Specifies the maximum PWM time offset."""
        return self.minPwmO

    def setMinPwmO(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the maximum PWM time offset.
        A None value is a no-op and does not overwrite an existing minPwmO."""
        if value is not None:
            self.minPwmO = value
        return self

    def getMinPwmS(self) -> Optional[PositiveInteger]:
        """Specifies the minimum PWM short phase length."""
        return self.minPwmS

    def setMinPwmS(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the minimum PWM short phase length.
        A None value is a no-op and does not overwrite an existing minPwmS."""
        if value is not None:
            self.minPwmS = value
        return self

    def getMinSamplePoint(self) -> Optional[Float]:
        """The min. value of the sample point as a percentage of the total bit time."""
        return self.minSamplePoint

    def setMinSamplePoint(self, value: Optional[Float]) -> "CanControllerXlConfigurationRequirements":
        """The min. value of the sample point as a percentage of the total bit time.
        A None value is a no-op and does not overwrite an existing minSamplePoint."""
        if value is not None:
            self.minSamplePoint = value
        return self

    def getMinSyncJumpWidth(self) -> Optional[Float]:
        """The min. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."""
        return self.minSyncJumpWidth

    def setMinSyncJumpWidth(self, value: Optional[Float]) -> "CanControllerXlConfigurationRequirements":
        """The min. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors.
        A None value is a no-op and does not overwrite an existing minSyncJumpWidth."""
        if value is not None:
            self.minSyncJumpWidth = value
        return self

    def getMinTrcvDelayCompensationOffset(self) -> Optional[TimeValue]:
        """Specifies the minimum Transceiver Delay Compensation Offset in seconds. If not specified Transmitter Delay Compensation is disabled."""
        return self.minTrcvDelayCompensationOffset

    def setMinTrcvDelayCompensationOffset(self, value: Optional[TimeValue]) -> "CanControllerXlConfigurationRequirements":
        """Specifies the minimum Transceiver Delay Compensation Offset in seconds. If not specified Transmitter Delay Compensation is disabled.
        A None value is a no-op and does not overwrite an existing minTrcvDelayCompensationOffset."""
        if value is not None:
            self.minTrcvDelayCompensationOffset = value
        return self

    def getTrcvPwmModeEnabled(self) -> Optional[Boolean]:
        """Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode."""
        return self.trcvPwmModeEnabled

    def setTrcvPwmModeEnabled(self, value: Optional[Boolean]) -> "CanControllerXlConfigurationRequirements":
        """Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode.
        A None value is a no-op and does not overwrite an existing trcvPwmModeEnabled."""
        if value is not None:
            self.trcvPwmModeEnabled = value
        return self


class AbstractCanCommunicationControllerAttributes(ARObject, ABC):
    """For the configuration of the CanController parameters two different approaches can be used: 1. Providing exact values which are taken by the ECU developer (CanControllerConfiguration). 2. Providing ranges of values which are taken as requirements and have to be respected by the ECU developer (CanControllerConfigurationRequirements)."""

    # AbstractCanCommunicationControllerAttributes method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.13, p.64
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCanControllerFdAttributes      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanControllerFdAttributes      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanControllerFdRequirements    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanControllerFdRequirements    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanControllerXlAttributes      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanControllerXlAttributes      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanControllerXlRequirements     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanControllerXlRequirements     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is AbstractCanCommunicationControllerAttributes:
            raise TypeError("AbstractCanCommunicationControllerAttributes is an abstract class.")

        super().__init__()

        # Bit timing related configuration of a CAN controller for payload and CRC of a CanFD frame. If this element exists the controller supports CanFD frames and the ECU developer shall take these values for the configuration of the CanFD controller.
        self.canControllerFdAttributes: Optional[CanControllerFdConfiguration] = None

        # Additional CanFD ranges of the bit timing related configuration of a CanFD controller. If this element exists the controller supports CanFD frames and the ECU developer shall take these ranges as requirements for the configuration of the CanFD controller.
        self.canControllerFdRequirements: Optional[CanControllerFdConfigurationRequirements] = None

        # Bit timing related configuration of a CAN controller for payload and CRC of a CanXL frame. If this element exists the controller supports CanXL frames and the ECU developer shall take these values for the configuration of the CanXL controller.
        self.canControllerXlAttributes: Optional[CanControllerXlConfiguration] = None

        # Additional CanXL ranges of the bit timing related configuration of a CanXL controller. If this element exists the controller supports CanXL frames and the ECU developer shall take these ranges as requirements for the configuration of the CanXL controller.
        self.canControllerXlRequirements: Optional[CanControllerXlConfigurationRequirements] = None

    def getCanControllerFdAttributes(self) -> Optional[CanControllerFdConfiguration]:
        """Bit timing related configuration of a CAN controller for payload and CRC of a CanFD frame. If this element exists the controller supports CanFD frames and the ECU developer shall take these values for the configuration of the CanFD controller."""
        return self.canControllerFdAttributes

    def setCanControllerFdAttributes(self, value: Optional[CanControllerFdConfiguration]) -> "AbstractCanCommunicationControllerAttributes":
        """Bit timing related configuration of a CAN controller for payload and CRC of a CanFD frame. If this element exists the controller supports CanFD frames and the ECU developer shall take these values for the configuration of the CanFD controller.
        A None value is a no-op and does not overwrite an existing canControllerFdAttributes."""
        if value is not None:
            self.canControllerFdAttributes = value
        return self

    def getCanControllerFdRequirements(self) -> Optional[CanControllerFdConfigurationRequirements]:
        """Additional CanFD ranges of the bit timing related configuration of a CanFD controller. If this element exists the controller supports CanFD frames and the ECU developer shall take these ranges as requirements for the configuration of the CanFD controller."""
        return self.canControllerFdRequirements

    def setCanControllerFdRequirements(self, value: Optional[CanControllerFdConfigurationRequirements]) -> "AbstractCanCommunicationControllerAttributes":
        """Additional CanFD ranges of the bit timing related configuration of a CanFD controller. If this element exists the controller supports CanFD frames and the ECU developer shall take these ranges as requirements for the configuration of the CanFD controller.
        A None value is a no-op and does not overwrite an existing canControllerFdRequirements."""
        if value is not None:
            self.canControllerFdRequirements = value
        return self

    def getCanControllerXlAttributes(self) -> Optional[CanControllerXlConfiguration]:
        """Bit timing related configuration of a CAN controller for payload and CRC of a CanXL frame. If this element exists the controller supports CanXL frames and the ECU developer shall take these values for the configuration of the CanXL controller."""
        return self.canControllerXlAttributes

    def setCanControllerXlAttributes(self, value: Optional[CanControllerXlConfiguration]) -> "AbstractCanCommunicationControllerAttributes":
        """Bit timing related configuration of a CAN controller for payload and CRC of a CanXL frame. If this element exists the controller supports CanXL frames and the ECU developer shall take these values for the configuration of the CanXL controller.
        A None value is a no-op and does not overwrite an existing canControllerXlAttributes."""
        if value is not None:
            self.canControllerXlAttributes = value
        return self

    def getCanControllerXlRequirements(self) -> Optional[CanControllerXlConfigurationRequirements]:
        """Additional CanXL ranges of the bit timing related configuration of a CanXL controller. If this element exists the controller supports CanXL frames and the ECU developer shall take these ranges as requirements for the configuration of the CanXL controller."""
        return self.canControllerXlRequirements

    def setCanControllerXlRequirements(self, value: Optional[CanControllerXlConfigurationRequirements]) -> "AbstractCanCommunicationControllerAttributes":
        """Additional CanXL ranges of the bit timing related configuration of a CanXL controller. If this element exists the controller supports CanXL frames and the ECU developer shall take these ranges as requirements for the configuration of the CanXL controller.
        A None value is a no-op and does not overwrite an existing canControllerXlRequirements."""
        if value is not None:
            self.canControllerXlRequirements = value
        return self


class CanControllerConfigurationRequirements(AbstractCanCommunicationControllerAttributes):
    """
    Defines configuration requirements for CAN controllers, specifying
    the timing and communication parameters that must be supported
    by the CAN communication hardware.
    """

    # CanControllerConfigurationRequirements method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxSyncJumpWidth          [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxSyncJumpWidth          [x] impl  [ ] docstring  [ ] test
    # [ ] getMinNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] setMinNumberOfTimeQuantaPerBit [x] impl  [ ] docstring  [ ] test
    # [ ] getMinSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] setMinSamplePoint            [x] impl  [ ] docstring  [ ] test
    # [ ] getMinSyncJumpWidth          [x] impl  [ ] docstring  [ ] test
    # [ ] setMinSyncJumpWidth          [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.maxNumberOfTimeQuantaPerBit: Integer = None
        self.maxSamplePoint: Float = None
        self.maxSyncJumpWidth: Float = None
        self.minNumberOfTimeQuantaPerBit: Integer = None
        self.minSamplePoint: Float = None
        self.minSyncJumpWidth: Float = None

    def getMaxNumberOfTimeQuantaPerBit(self):
        return self.maxNumberOfTimeQuantaPerBit

    def setMaxNumberOfTimeQuantaPerBit(self, value):
        self.maxNumberOfTimeQuantaPerBit = value
        return self

    def getMaxSamplePoint(self):
        return self.maxSamplePoint

    def setMaxSamplePoint(self, value):
        self.maxSamplePoint = value
        return self

    def getMaxSyncJumpWidth(self):
        return self.maxSyncJumpWidth

    def setMaxSyncJumpWidth(self, value):
        self.maxSyncJumpWidth = value
        return self

    def getMinNumberOfTimeQuantaPerBit(self):
        return self.minNumberOfTimeQuantaPerBit

    def setMinNumberOfTimeQuantaPerBit(self, value):
        self.minNumberOfTimeQuantaPerBit = value
        return self

    def getMinSamplePoint(self):
        return self.minSamplePoint

    def setMinSamplePoint(self, value):
        self.minSamplePoint = value
        return self

    def getMinSyncJumpWidth(self):
        return self.minSyncJumpWidth

    def setMinSyncJumpWidth(self, value):
        self.minSyncJumpWidth = value
        return self


class AbstractCanCommunicationController(CommunicationController, ABC):
    """Abstract class that is used to collect the common TtCAN and CAN Controller attributes."""

    # AbstractCanCommunicationController method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.12, p.63
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCanControllerAttributes   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanControllerAttributes   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCommunicationController:
            raise TypeError("AbstractCanCommunicationController is an abstract class.")

        super().__init__(parent, short_name)

        # CAN Bit Timing configuration
        self.canControllerAttributes: Optional[AbstractCanCommunicationControllerAttributes] = None

    def getCanControllerAttributes(self) -> Optional[AbstractCanCommunicationControllerAttributes]:
        """
        CAN Bit Timing configuration
        """
        return self.canControllerAttributes

    def setCanControllerAttributes(self, value: Optional[AbstractCanCommunicationControllerAttributes]) -> "AbstractCanCommunicationController":
        """
        CAN Bit Timing configuration
        A None value is a no-op and does not overwrite an existing canControllerAttributes.
        """
        if value is not None:
            self.canControllerAttributes = value
        return self


class CanCommunicationController(AbstractCanCommunicationController):
    """CAN bus specific communication port attributes."""

    # CanCommunicationController method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.11, p.63
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class AbstractCanCommunicationConnector(CommunicationConnector, ABC):
    """
    Abstract class that is used to collect the common TtCAN and CAN CommunicationConnector attributes.
    """

    # AbstractCanCommunicationConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.22, p.73
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # (no own attributes; reader/writer coverage via CAN-COMMUNICATION-CONNECTOR dispatch of subclasses)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCommunicationConnector:
            raise TypeError("AbstractCanCommunicationConnector is an abstract class.")

        super().__init__(parent, short_name)


class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """
    Represents a CAN communication connector that links CAN controllers
    to communication channels, enabling network connectivity and defining
    power state management properties for CAN communication.
    """

    # CanCommunicationConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getPncWakeupCanId            [x] impl  [ ] docstring  [ ] test
    # [ ] setPncWakeupCanId            [x] impl  [ ] docstring  [ ] test
    # [ ] getPncWakeupCanIdExtended    [x] impl  [ ] docstring  [ ] test
    # [ ] setPncWakeupCanIdExtended    [x] impl  [ ] docstring  [ ] test
    # [ ] getPncWakeupCanIdMask        [x] impl  [ ] docstring  [ ] test
    # [ ] setPncWakeupCanIdMask        [x] impl  [ ] docstring  [ ] test
    # [ ] getPncWakeupDataMask         [x] impl  [ ] docstring  [ ] test
    # [ ] setPncWakeupDataMask         [x] impl  [ ] docstring  [ ] test
    # [ ] getPncWakeupDlc              [x] impl  [ ] docstring  [ ] test
    # [ ] setPncWakeupDlc              [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.pncWakeupCanId: PositiveInteger = None
        self.pncWakeupCanIdExtended: Boolean = None
        self.pncWakeupCanIdMask: PositiveInteger = None
        self.pncWakeupDataMask: PositiveUnlimitedInteger = None
        self.pncWakeupDlc: PositiveInteger = None

    def getPncWakeupCanId(self):
        return self.pncWakeupCanId

    def setPncWakeupCanId(self, value):
        if value is not None:
            self.pncWakeupCanId = value
        return self

    def getPncWakeupCanIdExtended(self):
        return self.pncWakeupCanIdExtended

    def setPncWakeupCanIdExtended(self, value):
        if value is not None:
            self.pncWakeupCanIdExtended = value
        return self

    def getPncWakeupCanIdMask(self):
        return self.pncWakeupCanIdMask

    def setPncWakeupCanIdMask(self, value):
        if value is not None:
            self.pncWakeupCanIdMask = value
        return self

    def getPncWakeupDataMask(self):
        return self.pncWakeupDataMask

    def setPncWakeupDataMask(self, value):
        if value is not None:
            self.pncWakeupDataMask = value
        return self

    def getPncWakeupDlc(self):
        return self.pncWakeupDlc

    def setPncWakeupDlc(self, value):
        if value is not None:
            self.pncWakeupDlc = value
        return self
