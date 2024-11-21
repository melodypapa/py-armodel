from abc import ABCMeta
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DataMapping(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == ARObject:
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

        self.dataElementIRef = None
        self.senderToSignalTextTableMapping = None
        self.signalToReceiverTextTableMapping = None
        self.systemSignalRef = None

    def getDataElementIRef(self):
        return self.dataElementIRef

    def setDataElementIRef(self, value):
        self.dataElementIRef = value
        return self

    def getSenderToSignalTextTableMapping(self):
        return self.senderToSignalTextTableMapping

    def setSenderToSignalTextTableMapping(self, value):
        self.senderToSignalTextTableMapping = value
        return self

    def getSignalToReceiverTextTableMapping(self):
        return self.signalToReceiverTextTableMapping

    def setSignalToReceiverTextTableMapping(self, value):
        self.signalToReceiverTextTableMapping = value
        return self

    def getSystemSignalRef(self):
        return self.systemSignalRef

    def setSystemSignalRef(self, value):
        self.systemSignalRef = value
        return self

class SenderReceiverToSignalGroupMapping(DataMapping):
    def __init__(self):
        super().__init__()

        self.dataElementIRef = None                         # type: RefType
        self.signalGroupRef = None                          # type: RefType
        self.typeMapping = None

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

