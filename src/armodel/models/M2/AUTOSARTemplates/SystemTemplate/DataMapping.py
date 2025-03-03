from abc import ABCMeta
from typing import List

from ....M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from ....M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationDirectionType


class DataMapping(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is DataMapping:
            raise NotImplementedError("DataMapping is an abstract class.")
        
        super().__init__()

        self.introduction = None

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        self.introduction = value
        return self


class SenderReceiverToSignalMapping(DataMapping):
    def __init__(self):
        super().__init__()

        self.communicationDirection = None                          # type: CommunicationDirectionType
        self.dataElementIRef = None                                 # type: VariableDataPrototypeInSystemInstanceRef
        self.senderToSignalTextTableMapping = None                  # type: TextTableMapping
        self.signalToReceiverTextTableMapping = None                # type: TextTableMapping
        self.systemSignalRef = None                                 # type: RefType

    def getCommunicationDirection(self):
        return self.communicationDirection

    def setCommunicationDirection(self, value: CommunicationDirectionType):
        self.communicationDirection = value
        return self

    def getDataElementIRef(self):
        return self.dataElementIRef

    def setDataElementIRef(self, value: VariableDataPrototypeInSystemInstanceRef):
        self.dataElementIRef = value
        return self

    def getSenderToSignalTextTableMapping(self):
        return self.senderToSignalTextTableMapping

    def setSenderToSignalTextTableMapping(self, value: TextTableMapping):
        self.senderToSignalTextTableMapping = value
        return self

    def getSignalToReceiverTextTableMapping(self):
        return self.signalToReceiverTextTableMapping

    def setSignalToReceiverTextTableMapping(self, value: TextTableMapping):
        self.signalToReceiverTextTableMapping = value
        return self

    def getSystemSignalRef(self):
        return self.systemSignalRef

    def setSystemSignalRef(self, value: RefType):
        self.systemSignalRef = value
        return self


class SenderRecCompositeTypeMapping(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is SenderRecCompositeTypeMapping:
            raise NotImplementedError("SenderRecCompositeTypeMapping is an abstract class.")
        
        super().__init__()


class SenderRecRecordElementMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.applicationRecordElementRef = None                     # type: RefType
        self.complexTypeMapping = None                              # type: SenderRecCompositeTypeMapping
        self.implementationRecordElementRef = None                  # type: RefType
        self.senderToSignalTextTableMapping = None                  # type: TextTableMapping
        self.signalToReceiverTextTableMapping = None                # type: TextTableMapping
        self.systemSignalRef = None                                 # type: RefType

    def getApplicationRecordElementRef(self):
        return self.applicationRecordElementRef

    def setApplicationRecordElementRef(self, value):
        if value is not None:
            self.applicationRecordElementRef = value
        return self

    def getComplexTypeMapping(self):
        return self.complexTypeMapping

    def setComplexTypeMapping(self, value):
        if value is not None:
            self.complexTypeMapping = value
        return self

    def getImplementationRecordElementRef(self):
        return self.implementationRecordElementRef

    def setImplementationRecordElementRef(self, value):
        if value is not None:
            self.implementationRecordElementRef = value
        return self

    def getSenderToSignalTextTableMapping(self):
        return self.senderToSignalTextTableMapping

    def setSenderToSignalTextTableMapping(self, value):
        if value is not None:
            self.senderToSignalTextTableMapping = value
        return self

    def getSignalToReceiverTextTableMapping(self):
        return self.signalToReceiverTextTableMapping

    def setSignalToReceiverTextTableMapping(self, value):
        if value is not None:
            self.signalToReceiverTextTableMapping = value
        return self

    def getSystemSignalRef(self):
        return self.systemSignalRef

    def setSystemSignalRef(self, value):
        if value is not None:
            self.systemSignalRef = value
        return self


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    def __init__(self):
        super().__init__()

        self.recordElementMappings = []                     # type: List[SenderRecRecordElementMapping]

    def getRecordElementMappings(self):
        return self.recordElementMappings

    def addRecordElementMapping(self, value):
        if value is not None:
            self.recordElementMappings.append(value)
        return self


class IndexedArrayElement(ARObject):
    def __init__(self):
        super().__init__()

        self.applicationArrayElementRef = None              # type: RefType
        self.implementationArrayElementRef = None           # type: RefType
        self.index = None                                   # type: Integer
        

class SenderRecArrayElementMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.complexTypeMapping = None                      # type: SenderRecCompositeTypeMapping
        self.indexedArrayElement = None                     # type: IndexedArrayElement
        self.systemSignalRef = None                         # type: RefType

    def getComplexTypeMapping(self):
        return self.complexTypeMapping

    def setComplexTypeMapping(self, value):
        if value is not None:
            self.complexTypeMapping = value
        return self

    def getIndexedArrayElement(self):
        return self.indexedArrayElement

    def setIndexedArrayElement(self, value):
        if value is not None:
            self.indexedArrayElement = value
        return self

    def getSystemSignalRef(self):
        return self.systemSignalRef

    def setSystemSignalRef(self, value):
        if value is not None:
            self.systemSignalRef = value
        return self


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    def __init__(self):
        super().__init__()

        self.arrayElementMappings = []                      # type: List[SenderRecArrayElementMapping]
        self.senderToSignal = None                          # type: TextTableMapping
        self.signalToReceiverTextTableMapping = None        # type: TextTableMapping

    def getArrayElementMappings(self):
        return self.arrayElementMappings

    def setArrayElementMappings(self, value):
        if value is not None:
            self.arrayElementMappings = value
        return self

    def getSenderToSignal(self):
        return self.senderToSignal

    def setSenderToSignal(self, value):
        if value is not None:
            self.senderToSignal = value
        return self

    def getSignalToReceiverTextTableMapping(self):
        return self.signalToReceiverTextTableMapping

    def setSignalToReceiverTextTableMapping(self, value):
        if value is not None:
            self.signalToReceiverTextTableMapping = value
        return self


class SenderReceiverToSignalGroupMapping(DataMapping):
    def __init__(self):
        super().__init__()

        self.dataElementIRef = None                         # type: VariableDataPrototypeInSystemInstanceRef
        self.signalGroupRef = None                          # type: RefType
        self.typeMapping = None                             # type: SenderRecCompositeTypeMapping

    def getDataElementIRef(self):
        return self.dataElementIRef

    def setDataElementIRef(self, value):
        self.dataElementIRef = value
        return self

    def getSignalGroupRef(self):
        return self.signalGroupRef

    def setSignalGroupRef(self, value):
        self.signalGroupRef = value
        return self

    def getTypeMapping(self):
        return self.typeMapping

    def setTypeMapping(self, value):
        self.typeMapping = value
        return self
