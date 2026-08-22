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
    """
    Defines CAN XL (eXtended Length) configuration parameters for CAN controllers,
    including timing settings, payload length configurations, and other
    CAN XL communication properties.
    """

    # CanControllerXlConfiguration method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getArbitrationPhaseSeg1      [x] impl  [ ] docstring  [ ] test
    # [ ] setArbitrationPhaseSeg1      [x] impl  [ ] docstring  [ ] test
    # [ ] getArbitrationPhaseSeg2      [x] impl  [ ] docstring  [ ] test
    # [ ] setArbitrationPhaseSeg2      [x] impl  [ ] docstring  [ ] test
    # [ ] getArbitrationSJW            [x] impl  [ ] docstring  [ ] test
    # [ ] setArbitrationSJW            [x] impl  [ ] docstring  [ ] test
    # [ ] getDataPhaseSeg1             [x] impl  [ ] docstring  [ ] test
    # [ ] setDataPhaseSeg1             [x] impl  [ ] docstring  [ ] test
    # [ ] getDataPhaseSeg2             [x] impl  [ ] docstring  [ ] test
    # [ ] setDataPhaseSeg2             [x] impl  [ ] docstring  [ ] test
    # [ ] getDataSJW                   [x] impl  [ ] docstring  [ ] test
    # [ ] setDataSJW                   [x] impl  [ ] docstring  [ ] test
    # [ ] getMinArbitrationBitTime     [x] impl  [ ] docstring  [ ] test
    # [ ] setMinArbitrationBitTime     [x] impl  [ ] docstring  [ ] test
    # [ ] getMinDataBitTime            [x] impl  [ ] docstring  [ ] test
    # [ ] setMinDataBitTime            [x] impl  [ ] docstring  [ ] test
    # [ ] getPaddingValue              [x] impl  [ ] docstring  [ ] test
    # [ ] setPaddingValue              [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSeg1Arbitration       [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSeg1Arbitration       [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSeg1Data              [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSeg1Data              [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSeg2Arbitration       [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSeg2Arbitration       [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSeg2Data              [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSeg2Data              [x] impl  [ ] docstring  [ ] test
    # [ ] getXlBitRateSwitch           [x] impl  [ ] docstring  [ ] test
    # [ ] setXlBitRateSwitch           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.arbitrationPhaseSeg1: PositiveInteger = None
        self.arbitrationPhaseSeg2: PositiveInteger = None
        self.arbitrationSJW: PositiveInteger = None
        self.dataPhaseSeg1: PositiveInteger = None
        self.dataPhaseSeg2: PositiveInteger = None
        self.dataSJW: PositiveInteger = None
        self.minArbitrationBitTime: TimeValue = None
        self.minDataBitTime: TimeValue = None
        self.paddingValue: PositiveInteger = None
        self.timeSeg1Arbitration: PositiveInteger = None
        self.timeSeg1Data: PositiveInteger = None
        self.timeSeg2Arbitration: PositiveInteger = None
        self.timeSeg2Data: PositiveInteger = None
        self.xlBitRateSwitch: Boolean = None

    def getArbitrationPhaseSeg1(self):
        return self.arbitrationPhaseSeg1

    def setArbitrationPhaseSeg1(self, value):
        if value is not None:
            self.arbitrationPhaseSeg1 = value
        return self

    def getArbitrationPhaseSeg2(self):
        return self.arbitrationPhaseSeg2

    def setArbitrationPhaseSeg2(self, value):
        if value is not None:
            self.arbitrationPhaseSeg2 = value
        return self

    def getArbitrationSJW(self):
        return self.arbitrationSJW

    def setArbitrationSJW(self, value):
        if value is not None:
            self.arbitrationSJW = value
        return self

    def getDataPhaseSeg1(self):
        return self.dataPhaseSeg1

    def setDataPhaseSeg1(self, value):
        if value is not None:
            self.dataPhaseSeg1 = value
        return self

    def getDataPhaseSeg2(self):
        return self.dataPhaseSeg2

    def setDataPhaseSeg2(self, value):
        if value is not None:
            self.dataPhaseSeg2 = value
        return self

    def getDataSJW(self):
        return self.dataSJW

    def setDataSJW(self, value):
        if value is not None:
            self.dataSJW = value
        return self

    def getMinArbitrationBitTime(self):
        return self.minArbitrationBitTime

    def setMinArbitrationBitTime(self, value):
        if value is not None:
            self.minArbitrationBitTime = value
        return self

    def getMinDataBitTime(self):
        return self.minDataBitTime

    def setMinDataBitTime(self, value):
        if value is not None:
            self.minDataBitTime = value
        return self

    def getPaddingValue(self):
        return self.paddingValue

    def setPaddingValue(self, value):
        if value is not None:
            self.paddingValue = value
        return self

    def getTimeSeg1Arbitration(self):
        return self.timeSeg1Arbitration

    def setTimeSeg1Arbitration(self, value):
        if value is not None:
            self.timeSeg1Arbitration = value
        return self

    def getTimeSeg1Data(self):
        return self.timeSeg1Data

    def setTimeSeg1Data(self, value):
        if value is not None:
            self.timeSeg1Data = value
        return self

    def getTimeSeg2Arbitration(self):
        return self.timeSeg2Arbitration

    def setTimeSeg2Arbitration(self, value):
        if value is not None:
            self.timeSeg2Arbitration = value
        return self

    def getTimeSeg2Data(self):
        return self.timeSeg2Data

    def setTimeSeg2Data(self, value):
        if value is not None:
            self.timeSeg2Data = value
        return self

    def getXlBitRateSwitch(self):
        return self.xlBitRateSwitch

    def setXlBitRateSwitch(self, value):
        if value is not None:
            self.xlBitRateSwitch = value
        return self


class CanControllerXlConfigurationRequirements(ARObject):
    """
    Specifies the requirements for CAN XL configuration parameters, defining
    the acceptable ranges and constraints for timing, bit rate, and other
    CAN XL communication properties.
    """

    # CanControllerXlConfigurationRequirements method parity checklist:
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
    # [ ] getXlBitRateSwitch           [x] impl  [ ] docstring  [ ] test
    # [ ] setXlBitRateSwitch           [x] impl  [ ] docstring  [ ] test

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
        self.xlBitRateSwitch: Boolean = None

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

    def getXlBitRateSwitch(self):
        return self.xlBitRateSwitch

    def setXlBitRateSwitch(self, value):
        if value is not None:
            self.xlBitRateSwitch = value
        return self


class AbstractCanCommunicationControllerAttributes(ARObject, ABC):
    """
    Abstract base class for CAN communication controller attributes,
    providing a common foundation for both FD and XL configuration
    properties of CAN controllers.
    """

    # AbstractCanCommunicationControllerAttributes method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCanControllerFdAttributes [x] impl  [ ] docstring  [ ] test
    # [ ] setCanControllerFdAttributes [x] impl  [ ] docstring  [ ] test
    # [ ] getCanControllerFdRequirements [x] impl  [ ] docstring  [ ] test
    # [ ] setCanControllerFdRequirements [x] impl  [ ] docstring  [ ] test
    # [ ] getCanControllerXlAttributes [x] impl  [ ] docstring  [ ] test
    # [ ] setCanControllerXlAttributes [x] impl  [ ] docstring  [ ] test
    # [ ] getCanControllerXlRequirements [x] impl  [ ] docstring  [ ] test
    # [ ] setCanControllerXlRequirements [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is AbstractCanCommunicationControllerAttributes:
            raise TypeError("AbstractCanCommunicationControllerAttributes is an abstract class.")

        super().__init__()

        self.canControllerFdAttributes: CanControllerFdConfiguration = None
        self.canControllerFdRequirements: CanControllerFdConfigurationRequirements = None
        self.canControllerXlAttributes: CanControllerXlConfiguration = None
        self.canControllerXlRequirements: CanControllerXlConfigurationRequirements = None

    def getCanControllerFdAttributes(self):
        return self.canControllerFdAttributes

    def setCanControllerFdAttributes(self, value):
        self.canControllerFdAttributes = value
        return self

    def getCanControllerFdRequirements(self):
        return self.canControllerFdRequirements

    def setCanControllerFdRequirements(self, value):
        self.canControllerFdRequirements = value
        return self

    def getCanControllerXlAttributes(self):
        return self.canControllerXlAttributes

    def setCanControllerXlAttributes(self, value):
        self.canControllerXlAttributes = value
        return self

    def getCanControllerXlRequirements(self):
        return self.canControllerXlRequirements

    def setCanControllerXlRequirements(self, value):
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
    Abstract base class for CAN communication connectors, providing
    the foundation for connecting CAN controllers to communication
    channels and network segments.
    """

    # AbstractCanCommunicationConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

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
