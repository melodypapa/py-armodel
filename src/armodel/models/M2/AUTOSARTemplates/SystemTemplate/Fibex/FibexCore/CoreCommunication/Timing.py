from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter


class ModeDrivenTransmissionModeCondition(ARObject):
    """
    The condition defined by this class evaluates to true if one of the referenced modeDeclarations (OR associated) is active. All referenced modeDeclarations shall be from the same ModeDeclarationGroup. The condition is used to define which TransmissionMode shall be activated using Com_SwitchIpduTxMode.

    [constr_9187] Existence of ModeDrivenTransmissionModeCondition.modeDeclaration: For each ModeDrivenTransmissionModeCondition, the reference to ModeDeclaration in the role modeDeclaration shall exist at the time when the System Description is complete.
    """

    # ModeDrivenTransmissionModeCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.61, p.393 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getModeDeclarationRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addModeDeclarationRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to one modeDeclaration which is OR associated in the context of the ModeDrivenTransmissionModeCondition.
        self.modeDeclarationRefs: List[RefType] = []

    def getModeDeclarationRefs(self) -> List[RefType]:
        """
        Reference to one modeDeclaration which is OR associated in the context of the ModeDrivenTransmissionModeCondition.
        """
        return self.modeDeclarationRefs

    def addModeDeclarationRef(self, value: Optional[RefType]) -> "ModeDrivenTransmissionModeCondition":
        """
        Reference to one modeDeclaration which is OR associated in the context of the ModeDrivenTransmissionModeCondition.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.modeDeclarationRefs.append(value)
        return self


class TransmissionModeCondition(ARObject):
    """
    Possibility to attach a condition to each signal within an I-PDU. If at least one condition evaluates to true, TRANSMISSION MODE True shall be used for this I-Pdu. In all other cases, the TRANSMISSION MODE FALSE shall be used.
    """

    # TransmissionModeCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.60, p.392 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataFilter          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataFilter          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getISignalInIPduRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setISignalInIPduRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Possibilities to define conditions
        self.dataFilter: Optional[DataFilter] = None

        # Reference to a signal to which a condition is attached.
        self.iSignalInIPduRef: Optional[RefType] = None

    def getDataFilter(self) -> Optional[DataFilter]:
        """
        Possibilities to define conditions
        """
        return self.dataFilter

    def setDataFilter(self, value: Optional[DataFilter]) -> "TransmissionModeCondition":
        """
        Possibilities to define conditions
        A None value is a no-op and does not overwrite an existing dataFilter.
        """
        if value is not None:
            self.dataFilter = value
        return self

    def getISignalInIPduRef(self) -> Optional[RefType]:
        """
        Reference to a signal to which a condition is attached.
        """
        return self.iSignalInIPduRef

    def setISignalInIPduRef(self, value: Optional[RefType]) -> "TransmissionModeCondition":
        """
        Reference to a signal to which a condition is attached.
        A None value is a no-op and does not overwrite an existing iSignalInIPduRef.
        """
        if value is not None:
            self.iSignalInIPduRef = value
        return self


class TimeRangeTypeTolerance(ARObject):
    """
    Maximum allowable deviation
    """

    # TimeRangeTypeTolerance method parity checklist:
    # Spec: XSD group TIME-RANGE-TYPE-TOLERANCE, AUTOSAR_00052.xsd line 122919 (XSD-only; empty group, no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class TimeRangeType(ARObject):
    """
    The timeRange can be specified with the value attribute. Optionally a tolerance can be defined.
    """

    # TimeRangeType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.67, p.398 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTolerance           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTolerance           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValue               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Optional specification of a tolerance.
        self.tolerance: Optional[TimeRangeTypeTolerance] = None

        # Average value of a date (in seconds)
        self.value: Optional[TimeValue] = None

    def getTolerance(self) -> Optional[TimeRangeTypeTolerance]:
        """
        Optional specification of a tolerance.
        """
        return self.tolerance

    def setTolerance(self, value: Optional[TimeRangeTypeTolerance]) -> "TimeRangeType":
        """
        Optional specification of a tolerance.
        A None value is a no-op and does not overwrite an existing tolerance.
        """
        if value is not None:
            self.tolerance = value
        return self

    def getValue(self) -> Optional[TimeValue]:
        """
        Average value of a date (in seconds)
        """
        return self.value

    def setValue(self, value: Optional[TimeValue]) -> "TimeRangeType":
        """
        Average value of a date (in seconds)
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class CyclicTiming(Describable):
    """
    Specification of a cyclic sending behavior.
    """

    # CyclicTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.65, p.396 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTimeOffset          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeOffset          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimePeriod          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimePeriod          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute specifies the time until first transmission of this I-PDU. This attribute defines the time between Com_ IpduGroupStart and the first transmission of the cyclic part of this transmission request for this I-PDU.
        self.timeOffset: Optional[TimeRangeType] = None

        # Period of the repetition of cyclic transmissions.
        self.timePeriod: Optional[TimeRangeType] = None

    def getTimeOffset(self) -> Optional[TimeRangeType]:
        """
        This attribute specifies the time until first transmission of this I-PDU. This attribute defines the time between Com_ IpduGroupStart and the first transmission of the cyclic part of this transmission request for this I-PDU.
        """
        return self.timeOffset

    def setTimeOffset(self, value: Optional[TimeRangeType]) -> "CyclicTiming":
        """
        This attribute specifies the time until first transmission of this I-PDU. This attribute defines the time between Com_ IpduGroupStart and the first transmission of the cyclic part of this transmission request for this I-PDU.
        A None value is a no-op and does not overwrite an existing timeOffset.
        """
        if value is not None:
            self.timeOffset = value
        return self

    def getTimePeriod(self) -> Optional[TimeRangeType]:
        """
        Period of the repetition of cyclic transmissions.
        """
        return self.timePeriod

    def setTimePeriod(self, value: Optional[TimeRangeType]) -> "CyclicTiming":
        """
        Period of the repetition of cyclic transmissions.
        A None value is a no-op and does not overwrite an existing timePeriod.
        """
        if value is not None:
            self.timePeriod = value
        return self


class EventControlledTiming(Describable):
    """
    Specification of a event driven sending behavior. The PDU is sent n (numberOfRepeat + 1) times separated by the repetitionPeriod. If numberOfRepeats = 0, then the Pdu is sent just once.
    """

    # EventControlledTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.66, p.397 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNumberOfRepetitions [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNumberOfRepetitions [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRepetitionPeriod    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRepetitionPeriod    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Defines the number of repetitions for the Direct/N-Times transmission mode and the event driven part of Mixed transmission mode.
        self.numberOfRepetitions: Optional[Integer] = None

        # The repetitionPeriod specifies the time in seconds that elapses before the pdu can be sent the next time (Minimum repeat gap between two pdus). The repetition Period is optional in case that no repetitions are configured.
        self.repetitionPeriod: Optional[TimeRangeType] = None

    def getNumberOfRepetitions(self) -> Optional[Integer]:
        """
        Defines the number of repetitions for the Direct/N-Times transmission mode and the event driven part of Mixed transmission mode.
        """
        return self.numberOfRepetitions

    def setNumberOfRepetitions(self, value: Optional[Integer]) -> "EventControlledTiming":
        """
        Defines the number of repetitions for the Direct/N-Times transmission mode and the event driven part of Mixed transmission mode.
        A None value is a no-op and does not overwrite an existing numberOfRepetitions.
        """
        if value is not None:
            self.numberOfRepetitions = value
        return self

    def getRepetitionPeriod(self) -> Optional[TimeRangeType]:
        """
        The repetitionPeriod specifies the time in seconds that elapses before the pdu can be sent the next time (Minimum repeat gap between two pdus). The repetition Period is optional in case that no repetitions are configured.
        """
        return self.repetitionPeriod

    def setRepetitionPeriod(self, value: Optional[TimeRangeType]) -> "EventControlledTiming":
        """
        The repetitionPeriod specifies the time in seconds that elapses before the pdu can be sent the next time (Minimum repeat gap between two pdus). The repetition Period is optional in case that no repetitions are configured.
        A None value is a no-op and does not overwrite an existing repetitionPeriod.
        """
        if value is not None:
            self.repetitionPeriod = value
        return self


class TransmissionModeTiming(ARObject):
    """
    If the COM Transmission Mode is false the timing is aggregated by the TransmissionModeTiming element in the role of transmissionModeFalseTiming. If the COM Transmission Mode is true the timing is aggregated by the TransmissionModeTiming element in the role of transmissionModeTrueTiming. COM supports the following Transmission Modes: • Periodic (Cyclic Timing) • Direct /n-times (EventControlledTiming) • Mixed (Cyclic and EventControlledTiming are assigned)
    """

    # TransmissionModeTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.62, p.393 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCyclicTiming        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCyclicTiming        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEventControlledTiming [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventControlledTiming [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Periodic Transmission Mode.
        self.cyclicTiming: Optional[CyclicTiming] = None

        # Direct Transmission Mode.
        self.eventControlledTiming: Optional[EventControlledTiming] = None

    def getCyclicTiming(self) -> Optional[CyclicTiming]:
        """
        Periodic Transmission Mode.
        """
        return self.cyclicTiming

    def setCyclicTiming(self, value: Optional[CyclicTiming]) -> "TransmissionModeTiming":
        """
        Periodic Transmission Mode.
        A None value is a no-op and does not overwrite an existing cyclicTiming.
        """
        if value is not None:
            self.cyclicTiming = value
        return self

    def getEventControlledTiming(self) -> Optional[EventControlledTiming]:
        """
        Direct Transmission Mode.
        """
        return self.eventControlledTiming

    def setEventControlledTiming(self, value: Optional[EventControlledTiming]) -> "TransmissionModeTiming":
        """
        Direct Transmission Mode.
        A None value is a no-op and does not overwrite an existing eventControlledTiming.
        """
        if value is not None:
            self.eventControlledTiming = value
        return self


class TransmissionModeDeclaration(ARObject):
    """
    AUTOSAR COM provides the possibility to define two different TRANSMISSION MODES (True and False) for each I-PDU. As TransmissionMode selector the signal content can be evaluated via transmissionModeCondition (implemented directly in the COM module) or mode conditions can be defined with the modeDrivenTrue Condition or modeDrivenFalseCondition (evaluated by BswM and invoking Com_SwitchIpduTxMode COM API). If modeDrivenTrueCondition and modeDrivenFalseCondition are defined they shall never evaluate to true both at the same time. The mixing of Transmission Mode Switch via API and signal value is not allowed.
    """

    # TransmissionModeDeclaration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.59, p.392 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getModeDrivenFalseCondition [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModeDrivenFalseCondition [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeDrivenTrueCondition [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModeDrivenTrueCondition [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransmissionModeCondition [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmissionModeCondition [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransmissionModeFalseTiming [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmissionModeFalseTiming [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransmissionModeTrueTiming [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmissionModeTrueTiming [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven FalseConditions evaluate to true (AND associated) the transmissionModeFalseTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time.
        self.modeDrivenFalseConditions: List[ModeDrivenTransmissionModeCondition] = []

        # Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven TrueConditions evaluate to true (AND associated) the transmissionModeTrueTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time.
        self.modeDrivenTrueConditions: List[ModeDrivenTransmissionModeCondition] = []

        # The Transmission Mode Selector evaluates the conditions for a subset of signals and decides which transmission mode should be used. In case only one transmission mode is used there is no need for the "TransmissionMode Condition" and its sub-structure. In case the transmission mode shall be switched using the COM-API "Com_Switch IpduTxMode" there is no need for the "TransmissionMode Condition" and its sub-structure.
        self.transmissionModeConditions: List[TransmissionModeCondition] = []

        # Timing Specification if the COM Transmission Mode is false. The Transmission Mode Selector is defined to be false, if all Conditions evaluate to false.
        self.transmissionModeFalseTiming: Optional[TransmissionModeTiming] = None

        # Timing Specification if the COM Transmission Mode is true. The Transmission Mode Selector is defined to be true, if at least one Condition evaluates to true.
        self.transmissionModeTrueTiming: Optional[TransmissionModeTiming] = None

    def getModeDrivenFalseConditions(self) -> List[ModeDrivenTransmissionModeCondition]:
        """
        Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven FalseConditions evaluate to true (AND associated) the transmissionModeFalseTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time.
        """
        return self.modeDrivenFalseConditions

    def addModeDrivenFalseCondition(self, value: Optional[ModeDrivenTransmissionModeCondition]) -> "TransmissionModeDeclaration":
        """
        Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven FalseConditions evaluate to true (AND associated) the transmissionModeFalseTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time.
        A None value is a no-op and is not appended.
        """
        if value is not None:
            self.modeDrivenFalseConditions.append(value)
        return self

    def getModeDrivenTrueConditions(self) -> List[ModeDrivenTransmissionModeCondition]:
        """
        Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven TrueConditions evaluate to true (AND associated) the transmissionModeTrueTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time.
        """
        return self.modeDrivenTrueConditions

    def addModeDrivenTrueCondition(self, value: Optional[ModeDrivenTransmissionModeCondition]) -> "TransmissionModeDeclaration":
        """
        Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven TrueConditions evaluate to true (AND associated) the transmissionModeTrueTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time.
        A None value is a no-op and is not appended.
        """
        if value is not None:
            self.modeDrivenTrueConditions.append(value)
        return self

    def getTransmissionModeConditions(self) -> List[TransmissionModeCondition]:
        """
        The Transmission Mode Selector evaluates the conditions for a subset of signals and decides which transmission mode should be used. In case only one transmission mode is used there is no need for the "TransmissionMode Condition" and its sub-structure. In case the transmission mode shall be switched using the COM-API "Com_Switch IpduTxMode" there is no need for the "TransmissionMode Condition" and its sub-structure.
        """
        return self.transmissionModeConditions

    def addTransmissionModeCondition(self, value: Optional[TransmissionModeCondition]) -> "TransmissionModeDeclaration":
        """
        The Transmission Mode Selector evaluates the conditions for a subset of signals and decides which transmission mode should be used. In case only one transmission mode is used there is no need for the "TransmissionMode Condition" and its sub-structure. In case the transmission mode shall be switched using the COM-API "Com_Switch IpduTxMode" there is no need for the "TransmissionMode Condition" and its sub-structure.
        A None value is a no-op and is not appended.
        """
        if value is not None:
            self.transmissionModeConditions.append(value)
        return self

    def getTransmissionModeFalseTiming(self) -> Optional[TransmissionModeTiming]:
        """
        Timing Specification if the COM Transmission Mode is false. The Transmission Mode Selector is defined to be false, if all Conditions evaluate to false.
        """
        return self.transmissionModeFalseTiming

    def setTransmissionModeFalseTiming(self, value: Optional[TransmissionModeTiming]) -> "TransmissionModeDeclaration":
        """
        Timing Specification if the COM Transmission Mode is false. The Transmission Mode Selector is defined to be false, if all Conditions evaluate to false.
        A None value is a no-op and does not overwrite an existing transmissionModeFalseTiming.
        """
        if value is not None:
            self.transmissionModeFalseTiming = value
        return self

    def getTransmissionModeTrueTiming(self) -> Optional[TransmissionModeTiming]:
        """
        Timing Specification if the COM Transmission Mode is true. The Transmission Mode Selector is defined to be true, if at least one Condition evaluates to true.
        """
        return self.transmissionModeTrueTiming

    def setTransmissionModeTrueTiming(self, value: Optional[TransmissionModeTiming]) -> "TransmissionModeDeclaration":
        """
        Timing Specification if the COM Transmission Mode is true. The Transmission Mode Selector is defined to be true, if at least one Condition evaluates to true.
        A None value is a no-op and does not overwrite an existing transmissionModeTrueTiming.
        """
        if value is not None:
            self.transmissionModeTrueTiming = value
        return self


class TriggerIPduSendCondition(ARObject):
    """
    The condition defined by this class evaluates to true if one of the referenced modeDeclarations (OR associated) is active. The condition is used to define when the Pdu is triggered with the Com_Trigger IPDUSend API call.
    """

    # TriggerIPduSendCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.70, p.399 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getModeDeclarations    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addModeDeclarationRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to one modeDeclaration which is OR associated in the context of the TriggerIPduSend Condition.
        self.modeDeclarationRefs: List[RefType] = []

    def getModeDeclarationRefs(self) -> List[RefType]:
        """
        Reference to one modeDeclaration which is OR associated in the context of the TriggerIPduSend Condition.
        """
        return self.modeDeclarationRefs

    def addModeDeclarationRef(self, value: Optional[RefType]) -> "TriggerIPduSendCondition":
        """
        Reference to one modeDeclaration which is OR associated in the context of the TriggerIPduSend Condition.
        A None value is a no-op and is not appended.
        """
        if value is not None:
            self.modeDeclarationRefs.append(value)
        return self


class AbsoluteTolerance(TimeRangeTypeTolerance):
    """
    Maximum allowable deviation
    """

    # AbsoluteTolerance method parity checklist:
    # Spec: XSD group ABSOLUTE-TOLERANCE, AUTOSAR_00052.xsd line 37 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAbsolute  [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAbsolute  [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Maximum allowable deviation in duration (in seconds).
        self.absolute: Optional[TimeValue] = None

    def getAbsolute(self) -> Optional[TimeValue]:
        return self.absolute

    def setAbsolute(self, value: Optional[TimeValue]) -> "AbsoluteTolerance":
        if value is not None:
            self.absolute = value
        return self


class RelativeTolerance(TimeRangeTypeTolerance):
    """
    Maximum allowable deviation
    """

    # RelativeTolerance method parity checklist:
    # Spec: XSD group RELATIVE-TOLERANCE, AUTOSAR_00052.xsd line 98240 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRelative  [x] impl  [—] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRelative  [x] impl  [—] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Maximum allowable deviation in percent (percent of the corresponding TimeValue).
        self.relative: Optional[Integer] = None

    def getRelative(self) -> Optional[Integer]:
        return self.relative

    def setRelative(self, value: Optional[Integer]) -> "RelativeTolerance":
        if value is not None:
            self.relative = value
        return self
