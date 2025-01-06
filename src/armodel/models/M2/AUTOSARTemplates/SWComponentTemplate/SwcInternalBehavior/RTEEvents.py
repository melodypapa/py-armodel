from .....M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RVariableInAtomicSwcInstanceRef, RModeInAtomicSwcInstanceRef
from .....M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import POperationInAtomicSwcInstanceRef
from .....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from typing import List

class RTEEvent(AbstractEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.disabledModeIRefs = []                                     # type: List[RModeInAtomicSwcInstanceRef]
        self.startOnEventRef = None                                     # type: RefType

    def getDisabledModeIRefs(self):
        return self.disabledModeIRefs

    def addDisabledModeIRef(self, value):
        self.disabledModeIRefs.append(value)
        return self

    def getStartOnEventRef(self):
        return self.startOnEventRef

    def setStartOnEventRef(self, value):
        self.startOnEventRef = value
        return self

class AsynchronousServerCallReturnsEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef = None                                      # type: RefType

    def getEventSourceRef(self):
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        self.eventSourceRef = value
        return self


class DataSendCompletedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef = None                                      # type: RefType

    def getEventSourceRef(self):
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        self.eventSourceRef = value
        return self

class DataWriteCompletedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef = None                                      # type: RefType

    def getEventSourceRef(self):
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        self.eventSourceRef = value
        return self

class DataReceivedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataIRef = None                   # type: RVariableInAtomicSwcInstanceRef

    def getDataIRef(self):
        return self.dataIRef

    def setDataIRef(self, value):
        self.dataIRef = value
        return self


class SwcModeSwitchEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.activation = None              # type: ModeActivationKind
        self.modeIRefs = []                 # type: List[RModeInAtomicSwcInstanceRef]

    def getActivation(self):
        return self.activation

    def setActivation(self, value):
        self.activation = value
        return self

    def getModeIRefs(self):
        return self.modeIRefs

    def addModeIRef(self, value):
        self.modeIRefs.append(value)
        return self

class DataReceiveErrorEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataIRef = None            

    def getDataIRef(self):
        return self.dataIRef

    def setDataIRef(self, value):
        self.dataIRef = value
        return self

class OperationInvokedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.operationIRef = None                                   # type: POperationInAtomicSwcInstanceRef

    def getOperationIRef(self):
        return self.operationIRef

    def setOperationIRef(self, value):
        if value is not None:
            self.operationIRef = value
        return self

class InitEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class TimingEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.offset = None                              # type: TimeValue
        self.period = None                              # type: TimeValue

    @property
    def periodMs(self):
        if (self.period < 0.001):
            return self.period * 1000
        else:
            return (int)(self.period * 1000)
        
    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        if value is not None:
            self.offset = value
        return self

    def getPeriod(self):
        return self.period

    def setPeriod(self, value):
        if value is not None:
            self.period = value
        return self

class InternalTriggerOccurredEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef = None                                  # type: RefType

    def getEventSourceRef(self):
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        if value is not None:
            self.eventSourceRef = value
        return self

class BackgroundEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class ModeSwitchedAckEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef = None                                  # type: RefType

    def getEventSourceRef(self):
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        if value is not None:
            self.eventSourceRef = value
        return self
