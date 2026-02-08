# This module contains AUTOSAR System Template classes for data mapping between sender/receiver interfaces and signals
# It includes classes for mapping data elements between software component ports and system signals

from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    TextTableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    VariableDataPrototypeInSystemInstanceRef,
)


class DataMapping(ARObject, ABC):
    """
    Abstract base class for data mapping elements that define relationships between
    AUTOSAR software component data elements and system-level communication signals.
    This class serves as the foundation for various types of data mappings used in
    system design to connect component interfaces with communication infrastructure.
    """
    def __init__(self):
        if type(self) is DataMapping:
            raise TypeError("DataMapping is an abstract class.")

        super().__init__()

        self.introduction = None

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        self.introduction = value
        return self


class SenderReceiverToSignalMapping(DataMapping):
    """
    Maps data elements from sender/receiver interfaces to system signals.
    This class establishes the connection between variable data prototypes
    in system instance references and their corresponding system signal
    representations, including text table mappings for data transformation.
    """
    def __init__(self):
        super().__init__()

        self.communicationDirection: CommunicationDirectionType = None
        self.dataElementIRef: VariableDataPrototypeInSystemInstanceRef = None
        self.senderToSignalTextTableMapping: TextTableMapping = None
        self.signalToReceiverTextTableMapping: TextTableMapping = None
        self.systemSignalRef: RefType = None

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


class SenderRecCompositeTypeMapping(ARObject, ABC):
    """
    Abstract base class for composite type mappings between sender/receiver
    interfaces and system-level signals. This class handles complex data
    structures such as records and arrays in data mapping scenarios.
    """
    def __init__(self):
        if type(self) is SenderRecCompositeTypeMapping:
            raise TypeError("SenderRecCompositeTypeMapping is an abstract class.")

        super().__init__()


class SenderRecRecordElementMapping(ARObject):
    """
    Defines mapping for individual elements within a record structure,
    connecting application record elements to implementation record elements
    and their corresponding system signals, with optional text table mappings
    for data transformation.
    """
    def __init__(self):
        super().__init__()

        self.applicationRecordElementRef: RefType = None
        self.complexTypeMapping: SenderRecCompositeTypeMapping = None
        self.implementationRecordElementRef: RefType = None
        self.senderToSignalTextTableMapping: TextTableMapping = None
        self.signalToReceiverTextTableMapping: TextTableMapping = None
        self.systemSignalRef: RefType = None

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
    """
    Maps record data types between sender/receiver interfaces and system signals,
    containing multiple record element mappings that define how each field in
    the record structure is connected to system-level communication elements.
    """
    def __init__(self):
        super().__init__()

        self.recordElementMappings = []                                   # type: List[SenderRecRecordElementMapping]

    def getRecordElementMappings(self):
        return self.recordElementMappings

    def addRecordElementMapping(self, value):
        if value is not None:
            self.recordElementMappings.append(value)
        return self


class IndexedArrayElement(ARObject):
    """
    Represents an element in an array with a specific index, connecting
    application array elements to implementation array elements in the
    mapping between component interfaces and system signals.
    """
    def __init__(self):
        super().__init__()

        self.applicationArrayElementRef: RefType = None
        self.implementationArrayElementRef: RefType = None
        self.index: Integer = None

    def getApplicationArrayElementRef(self):
        return self.applicationArrayElementRef

    def setApplicationArrayElementRef(self, value):
        if value is not None:
            self.applicationArrayElementRef = value
        return self

    def getImplementationArrayElementRef(self):
        return self.implementationArrayElementRef

    def setImplementationArrayElementRef(self, value):
        if value is not None:
            self.implementationArrayElementRef = value
        return self

    def getIndex(self):
        return self.index

    def setIndex(self, value):
        if value is not None:
            self.index = value
        return self


class SenderRecArrayElementMapping(ARObject):
    """
    Maps individual elements of an array data type between sender/receiver
    interfaces and system signals, including complex type mapping for
    nested data structures and indexed array elements.
    """
    def __init__(self):
        super().__init__()

        self.complexTypeMapping: SenderRecCompositeTypeMapping = None
        self.indexedArrayElement: IndexedArrayElement = None
        self.systemSignalRef: RefType = None

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
    """
    Maps array data types between sender/receiver interfaces and system signals,
    containing multiple array element mappings and text table mappings for
    transforming array data during communication.
    """
    def __init__(self):
        super().__init__()

        self.arrayElementMappings: List[SenderRecArrayElementMapping] = []
        self.senderToSignal: TextTableMapping = None
        self.signalToReceiverTextTableMapping: TextTableMapping = None

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
    """
    Maps sender/receiver interface data to system signal groups, enabling
    communication with multiple related signals as a single entity, with
    support for complex type mappings of grouped data structures.
    """
    def __init__(self):
        super().__init__()

        self.dataElementIRef: VariableDataPrototypeInSystemInstanceRef = None
        self.signalGroupRef: RefType = None
        self.typeMapping: SenderRecCompositeTypeMapping = None

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
