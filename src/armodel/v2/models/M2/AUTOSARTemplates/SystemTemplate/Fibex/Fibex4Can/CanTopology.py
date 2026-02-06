# This module contains AUTOSAR System Template classes for CAN topology
# It defines CAN controllers, connectors, and their configuration attributes

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Integer,
    PositiveInteger,
    PositiveUnlimitedInteger,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
    CommunicationController,
)


class CanControllerFdConfiguration(ARObject):
    """
    Defines CAN FD (Flexible Data Rate) configuration parameters for CAN controllers,
    including timing settings, padding values, and bit rate switching properties
    required for CAN FD communication.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self.paddingValue: PositiveInteger = None
        self.propSeg: PositiveInteger = None
        self.sspOffset: PositiveInteger = None
        self.syncJumpWidth: PositiveInteger = None
        self.timeSeg1: PositiveInteger = None
        self.timeSeg2: PositiveInteger = None
        self.txBitRateSwitch: Boolean = None

    def getPaddingValue(self):
        return self.paddingValue

    def setPaddingValue(self, value):
        if value is not None:
            self.paddingValue = value
        return self

    def getPropSeg(self):
        return self.propSeg

    def setPropSeg(self, value):
        if value is not None:
            self.propSeg = value
        return self

    def getSspOffset(self):
        return self.sspOffset

    def setSspOffset(self, value):
        if value is not None:
            self.sspOffset = value
        return self

    def getSyncJumpWidth(self):
        return self.syncJumpWidth

    def setSyncJumpWidth(self, value):
        if value is not None:
            self.syncJumpWidth = value
        return self

    def getTimeSeg1(self):
        return self.timeSeg1

    def setTimeSeg1(self, value):
        if value is not None:
            self.timeSeg1 = value
        return self

    def getTimeSeg2(self):
        return self.timeSeg2

    def setTimeSeg2(self, value):
        if value is not None:
            self.timeSeg2 = value
        return self

    def getTxBitRateSwitch(self):
        return self.txBitRateSwitch

    def setTxBitRateSwitch(self, value):
        if value is not None:
            self.txBitRateSwitch = value
        return self


class CanControllerFdConfigurationRequirements(ARObject):
    """
    Specifies the requirements for CAN FD configuration parameters, defining
    the acceptable ranges and constraints for timing, bit rate, and other
    CAN FD communication properties.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

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
    """
    Abstract base class for CAN communication controllers, defining
    the common properties and behavior for CAN network interfaces
    in the AUTOSAR communication system.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCommunicationController:
            raise TypeError("AbstractCanCommunicationController is an abstract class.")

        super().__init__(parent, short_name)

        self.canControllerAttributes: AbstractCanCommunicationControllerAttributes = None

    def getCanControllerAttributes(self):
        return self.canControllerAttributes

    def setCanControllerAttributes(self, value):
        self.canControllerAttributes = value
        return self


class CanCommunicationController(AbstractCanCommunicationController):
    """
    Represents a CAN communication controller in the system, implementing
    the specific properties and behavior for CAN network communication
    hardware interfaces.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class AbstractCanCommunicationConnector(CommunicationConnector, ABC):
    """
    Abstract base class for CAN communication connectors, providing
    the foundation for connecting CAN controllers to communication
    channels and network segments.
    """
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
