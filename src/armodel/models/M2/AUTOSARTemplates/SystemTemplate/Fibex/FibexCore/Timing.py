from typing import List
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType, TimeValue

class ModeDrivenTransmissionModeCondition(ARObject):
    def __init__(self):
        super().__init__()

        self.modeDeclarationRef = None                          # type: RefType

    def getModeDeclarationRef(self):
        return self.modeDeclarationRef

    def setModeDeclarationRef(self, value):
        self.modeDeclarationRef = value
        return self

class TransmissionModeCondition(ARObject):
    def __init__(self):
        super().__init__()

        self.dataFilter = None                                  # type: DataFilter
        self.iSignalInIPduRef = None                            # type: RefType

    def getDataFilter(self):
        return self.dataFilter

    def setDataFilter(self, value):
        self.dataFilter = value
        return self

    def getISignalInIPduRef(self):
        return self.iSignalInIPduRef

    def setISignalInIPduRef(self, value):
        self.iSignalInIPduRef = value
        return self


class TimeRangeType(ARObject):
    def __init__(self):
        super().__init__()

        # type: TimeRangeTypeTolerance
        self.tolerance = None
        self.value = None                                       # type: TimeValue

    def getTolerance(self):
        return self.tolerance

    def setTolerance(self, value):
        self.tolerance = value
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self


class CyclicTiming(Describable):
    def __init__(self):
        super().__init__()

        self.timeOffset = None                                  # type: TimeRangeType
        self.timePeriod = None                                  # type: TimeRangeType

    def getTimeOffset(self):
        return self.timeOffset

    def setTimeOffset(self, value):
        self.timeOffset = value
        return self

    def getTimePeriod(self):
        return self.timePeriod

    def setTimePeriod(self, value):
        self.timePeriod = value
        return self


class EventControlledTiming(Describable):
    def __init__(self):
        super().__init__()

        self.numberOfRepetitions = None                         # type: Integer
        self.repetitionPeriod = None                            # type: TimeRangeType

    def getNumberOfRepetitions(self):
        return self.numberOfRepetitions

    def setNumberOfRepetitions(self, value):
        self.numberOfRepetitions = value
        return self

    def getRepetitionPeriod(self):
        return self.repetitionPeriod

    def setRepetitionPeriod(self, value):
        self.repetitionPeriod = value
        return self


class TransmissionModeTiming(ARObject):
    def __init__(self):
        super().__init__()

        self.cyclicTiming = None                                # type: CyclicTiming
        self.eventControlledTiming = None                       # type: EventControlledTiming

    def getCyclicTiming(self):
        return self.cyclicTiming

    def setCyclicTiming(self, value):
        self.cyclicTiming = value
        return self

    def getEventControlledTiming(self):
        return self.eventControlledTiming

    def setEventControlledTiming(self, value):
        self.eventControlledTiming = value
        return self

class TransmissionModeDeclaration(ARObject):
    def __init__(self):
        super().__init__()

        self.modeDrivenFalseConditions = []                         # type: List[ModeDrivenTransmissionModeCondition]
        self.modeDrivenTrueConditions = []                          # type: List[ModeDrivenTransmissionModeCondition]
        self.transmissionModeConditions = []                        # typeL List[TransmissionModeCondition]
        self.transmissionModeFalseTiming = None                     # type: TransmissionModeTiming
        self.transmissionModeTrueTiming = None                      # type: TransmissionModeTiming

    def getModeDrivenFalseConditions(self):
        return self.modeDrivenFalseConditions

    def addModeDrivenFalseCondition(self, value):
        self.modeDrivenFalseConditions.append(value)
        return self

    def getModeDrivenTrueConditions(self):
        return self.modeDrivenTrueConditions

    def addModeDrivenTrueCondition(self, value):
        self.modeDrivenTrueConditions.append(value)
        return self

    def getTransmissionModeConditions(self):
        return self.transmissionModeConditions

    def addTransmissionModeCondition(self, value):
        self.transmissionModeConditions.append(value)
        return self

    def getTransmissionModeFalseTiming(self):
        return self.transmissionModeFalseTiming

    def setTransmissionModeFalseTiming(self, value):
        self.transmissionModeFalseTiming = value
        return self

    def getTransmissionModeTrueTiming(self):
        return self.transmissionModeTrueTiming

    def setTransmissionModeTrueTiming(self, value):
        self.transmissionModeTrueTiming = value
        return self
