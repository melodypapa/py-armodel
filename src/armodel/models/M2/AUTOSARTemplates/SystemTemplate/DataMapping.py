# This module contains AUTOSAR System Template classes for data mapping between sender/receiver interfaces and signals
# It includes classes for mapping data elements between software component ports and system signals

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType


class DataMapping(ARObject, VariationPointCapable, ABC):
    """
    Abstract base class for data mapping elements that define relationships between
    AUTOSAR software component data elements and system-level communication signals.
    This class serves as the foundation for various types of data mappings used in
    system design to connect component interfaces with communication infrastructure.
    """

    # DataMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] setIntroduction              [x] impl  [ ] docstring  [ ] test

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

    # SenderReceiverToSignalMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationDirection    [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationDirection    [x] impl  [ ] docstring  [ ] test
    # [ ] getDataElementIRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setDataElementIRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getSenderToSignalTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] setSenderToSignalTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSignalToReceiverTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] setSignalToReceiverTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemSignalRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setSystemSignalRef           [x] impl  [ ] docstring  [ ] test

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
    """Two mappings exist for the composite data types: "ArrayTypeMapping" and "RecordTypeMapping". In both, a primitive datatype will be mapped to a system signal. But it is also possible to combine the arrays and the records, so that an "array" could be an element of a "record" and in the same manner a "record" could be an element of an "array". Nesting these data types is also possible. If an element of a composite data type is again a composite one, the "CompositeTypeMapping" element will be used one more time (aggregation between the ArrayElementMapping and CompositeTypeMapping or aggregation between the RecordElementMapping and CompositeTypeMapping)."""

    # SenderRecCompositeTypeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.27, p.235
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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

    # SenderRecRecordElementMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getApplicationRecordElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] setApplicationRecordElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] getComplexTypeMapping        [x] impl  [ ] docstring  [ ] test
    # [ ] setComplexTypeMapping        [x] impl  [ ] docstring  [ ] test
    # [ ] getImplementationRecordElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] setImplementationRecordElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] getSenderToSignalTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] setSenderToSignalTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSignalToReceiverTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] setSignalToReceiverTextTableMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemSignalRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setSystemSignalRef           [x] impl  [ ] docstring  [ ] test

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

    # SenderRecRecordTypeMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getRecordElementMappings     [x] impl  [ ] docstring  [ ] test
    # [ ] addRecordElementMapping      [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.recordElementMappings = []  # type: List[SenderRecRecordElementMapping]

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

    # IndexedArrayElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getApplicationArrayElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] setApplicationArrayElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] getImplementationArrayElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] setImplementationArrayElementRef [x] impl  [ ] docstring  [ ] test
    # [ ] getIndex                     [x] impl  [ ] docstring  [ ] test
    # [ ] setIndex                     [x] impl  [ ] docstring  [ ] test

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

    # SenderRecArrayElementMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getComplexTypeMapping        [x] impl  [ ] docstring  [ ] test
    # [ ] setComplexTypeMapping        [x] impl  [ ] docstring  [ ] test
    # [ ] getIndexedArrayElement       [x] impl  [ ] docstring  [ ] test
    # [ ] setIndexedArrayElement       [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemSignalRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setSystemSignalRef           [x] impl  [ ] docstring  [ ] test

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
    """If the ApplicationCompositeDataType is an Array, the "ArrayTypeMapping" will be used."""

    # SenderRecArrayTypeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.28, p.235
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArrayElementMappings              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addArrayElementMapping               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSenderToSignalTextTableMapping    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSenderToSignalTextTableMapping    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignalToReceiverTextTableMapping  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSignalToReceiverTextTableMapping  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Each ApplicationArrayElement shall be mapped on a SystemSignal.
        self.arrayElementMappings: List[SenderRecArrayElementMapping] = []

        # This mapping allows for the text-table translation between the sending DataPrototype that is defined in the PortPrototype and the physicalProps defined for the SystemSignal.
        self.senderToSignalTextTableMapping: Optional[TextTableMapping] = None

        # This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the PortPrototype.
        self.signalToReceiverTextTableMapping: Optional[TextTableMapping] = None

    def getArrayElementMappings(self) -> List[SenderRecArrayElementMapping]:
        """
        Each ApplicationArrayElement shall be mapped on a SystemSignal.
        """
        return self.arrayElementMappings

    def addArrayElementMapping(self, value: Optional[SenderRecArrayElementMapping]) -> "SenderRecArrayTypeMapping":
        """
        Each ApplicationArrayElement shall be mapped on a SystemSignal.
        A None value is a no-op and does not extend the arrayElementMappings list.
        """
        if value is not None:
            self.arrayElementMappings.append(value)
        return self

    def getSenderToSignalTextTableMapping(self) -> Optional[TextTableMapping]:
        """
        This mapping allows for the text-table translation between the sending DataPrototype that is defined in the PortPrototype and the physicalProps defined for the SystemSignal.
        """
        return self.senderToSignalTextTableMapping

    def setSenderToSignalTextTableMapping(self, value: Optional[TextTableMapping]) -> "SenderRecArrayTypeMapping":
        """
        This mapping allows for the text-table translation between the sending DataPrototype that is defined in the PortPrototype and the physicalProps defined for the SystemSignal.
        A None value is a no-op and does not overwrite an existing senderToSignalTextTableMapping.
        """
        if value is not None:
            self.senderToSignalTextTableMapping = value
        return self

    def getSignalToReceiverTextTableMapping(self) -> Optional[TextTableMapping]:
        """
        This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the PortPrototype.
        """
        return self.signalToReceiverTextTableMapping

    def setSignalToReceiverTextTableMapping(self, value: Optional[TextTableMapping]) -> "SenderRecArrayTypeMapping":
        """
        This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the PortPrototype.
        A None value is a no-op and does not overwrite an existing signalToReceiverTextTableMapping.
        """
        if value is not None:
            self.signalToReceiverTextTableMapping = value
        return self


class SenderReceiverToSignalGroupMapping(DataMapping):
    """
    Maps sender/receiver interface data to system signal groups, enabling
    communication with multiple related signals as a single entity, with
    support for complex type mappings of grouped data structures.
    """

    # SenderReceiverToSignalGroupMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataElementIRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setDataElementIRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getSignalGroupRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setSignalGroupRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTypeMapping               [x] impl  [ ] docstring  [ ] test
    # [ ] setTypeMapping               [x] impl  [ ] docstring  [ ] test

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


class DataTypePolicyEnum(AREnum):
    """
    This class lists the supported DataTypePolicies.
    """

    # DataTypePolicyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.8, p.322
    # Spec verified: R23-11
    # (no methods)

    # This literal indicates that this ISignal is used to transport a message as part of a service for Dds. Tags: atp.EnumerationLiteralIndex=6 atp.Status=candidate
    DDS_SERVICE = "ddsService"

    # This literal indicates that this ISignal is used to transport a signal based signal for Dds. Tags: atp.EnumerationLiteralIndex=5 atp.Status=candidate
    DDS_SIGNAL = "ddsSignal"

    # In case the System Description doesn't use a complete Software Component Description (VFB View) this value can be chosen. This supports the inclusion of legacy signals. The aggregation of SwDataDefProps shall be used to configure the "ComSignalDataInvalidValue" and the Data Semantics. Tags: atp.EnumerationLiteralIndex=0
    LEGACY = "legacy"

    # Ignore any networkRepresentationProps of this ISignal and use the networkRepresentation from the ComSpec. Please note that the usage does not imply the existence of the SwDataDefProps in the role networkRepresentation aggregated by the SenderComSpec or ReceiverComSpec if an ImplementationDataType is defined. Tags: atp.EnumerationLiteralIndex=1
    NETWORK_REPRESENTATION_FROM_COM_SPEC = "networkRepresentationFromComSpec"

    # If this value is chosen the requirements specified in the ComSpec (networkRepresentationFromComSpec) are not fullfilled by the aggregated SwDataDefProps. In this case the networkRepresentation is specified by the aggregated swDataDefProps. Tags: atp.EnumerationLiteralIndex=2
    OVERRIDE = "override"

    # This literal indicates that a transformer chain shall be used to communicate the ISignal as UINT8_N over the bus. Tags: atp.EnumerationLiteralIndex=4
    TRANSFORMING_I_SIGNAL = "transformingISignal"

    def __init__(self):
        super().__init__(
            (
                DataTypePolicyEnum.DDS_SERVICE,
                DataTypePolicyEnum.DDS_SIGNAL,
                DataTypePolicyEnum.LEGACY,
                DataTypePolicyEnum.NETWORK_REPRESENTATION_FROM_COM_SPEC,
                DataTypePolicyEnum.OVERRIDE,
                DataTypePolicyEnum.TRANSFORMING_I_SIGNAL,
            )
        )
