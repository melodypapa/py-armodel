from typing import List
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter

class ModeDrivenTransmissionModeCondition(ARObject):
    """
    The condition defined by this class evaluates to true if one of the
    referenced modeDeclarations (OR associated) is active.
    """
    # ModeDrivenTransmissionModeCondition method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getModeDeclarationRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setModeDeclarationRef        [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.modeDeclarationRef: RefType = None

    def getModeDeclarationRef(self):
        return self.modeDeclarationRef

    def setModeDeclarationRef(self, value):
        self.modeDeclarationRef = value
        return self

class TransmissionModeCondition(ARObject):
    """
    Possibility to attach a condition to each signal within an I-PDU.
    If at least one condition evaluates to true, TRANSMISSION MODE True
    shall be used for this I-Pdu.
    """
    # TransmissionModeCondition method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataFilter                [x] impl  [ ] docstring  [ ] test
    # [ ] setDataFilter                [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalInIPduRef          [x] impl  [ ] docstring  [ ] test
    # [ ] setISignalInIPduRef          [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.dataFilter: DataFilter = None
        self.iSignalInIPduRef: RefType = None

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
    """
    The timeRange can be specified with the value attribute. Optionally a
    tolerance can be defined.
    """
    # TimeRangeType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTolerance                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTolerance                 [x] impl  [ ] docstring  [ ] test
    # [ ] getValue                     [x] impl  [ ] docstring  [ ] test
    # [ ] setValue                     [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.tolerance = None
        self.value: TimeValue = None

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
    """
    Specification of a cyclic sending behavior.
    """
    # CyclicTiming method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeOffset                [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeOffset                [x] impl  [ ] docstring  [ ] test
    # [ ] getTimePeriod                [x] impl  [ ] docstring  [ ] test
    # [ ] setTimePeriod                [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.timeOffset: TimeRangeType = None
        self.timePeriod: TimeRangeType = None

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
    """
    Specification of an event-driven sending behavior. The PDU is sent
    n (numberOfRepeat + 1) times separated by the repetitionPeriod.
    """
    # EventControlledTiming method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getNumberOfRepetitions       [x] impl  [ ] docstring  [ ] test
    # [ ] setNumberOfRepetitions       [x] impl  [ ] docstring  [ ] test
    # [ ] getRepetitionPeriod          [x] impl  [ ] docstring  [ ] test
    # [ ] setRepetitionPeriod          [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.numberOfRepetitions: Integer = None
        self.repetitionPeriod: TimeRangeType = None

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
    """
    Defines the timing behavior for a transmission mode. If the COM
    Transmission Mode is false, the timing is defined by
    transmissionModeFalseTiming; if true, by transmissionModeTrueTiming.
    """
    # TransmissionModeTiming method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCyclicTiming              [x] impl  [ ] docstring  [ ] test
    # [ ] setCyclicTiming              [x] impl  [ ] docstring  [ ] test
    # [ ] getEventControlledTiming     [x] impl  [ ] docstring  [ ] test
    # [ ] setEventControlledTiming     [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.cyclicTiming: CyclicTiming = None
        self.eventControlledTiming: EventControlledTiming = None

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
    """
    Defines two different TRANSMISSION MODES (True and False) for each
    I-PDU, selected by signal content evaluation or mode conditions.
    """
    # TransmissionModeDeclaration method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getModeDrivenFalseConditions [x] impl  [ ] docstring  [ ] test
    # [ ] addModeDrivenFalseCondition  [x] impl  [ ] docstring  [ ] test
    # [ ] getModeDrivenTrueConditions  [x] impl  [ ] docstring  [ ] test
    # [ ] addModeDrivenTrueCondition   [x] impl  [ ] docstring  [ ] test
    # [ ] getTransmissionModeConditions [x] impl  [ ] docstring  [ ] test
    # [ ] addTransmissionModeCondition [x] impl  [ ] docstring  [ ] test
    # [ ] getTransmissionModeFalseTiming [x] impl  [ ] docstring  [ ] test
    # [ ] setTransmissionModeFalseTiming [x] impl  [ ] docstring  [ ] test
    # [ ] getTransmissionModeTrueTiming [x] impl  [ ] docstring  [ ] test
    # [ ] setTransmissionModeTrueTiming [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.modeDrivenFalseConditions: List[ModeDrivenTransmissionModeCondition] = []
        self.modeDrivenTrueConditions: List[ModeDrivenTransmissionModeCondition] = []
        self.transmissionModeConditions: List[TransmissionModeCondition] = []
        self.transmissionModeFalseTiming: TransmissionModeTiming = None
        self.transmissionModeTrueTiming: TransmissionModeTiming = None

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
