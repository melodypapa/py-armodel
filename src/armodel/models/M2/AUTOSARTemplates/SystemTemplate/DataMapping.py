# This module contains AUTOSAR System Template classes for data mapping between sender/receiver interfaces and signals
# It includes classes for mapping data elements between software component ports and system signals

from __future__ import annotations

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class DataMapping(ARObject, VariationPointCapable, ABC):
    """
    Mapping of port elements (data elements and parameters) to frames and signals.
    """

    # DataMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.22, p.217 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_SystemTemplate.pdf, Table 5.14, p.142 (R4.3.1)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationDirection [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setCommunicationDirection [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getEventGroupRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addEventGroupRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getEventHandlerRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addEventHandlerRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getIntroduction           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceInstanceRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addServiceInstanceRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self):
        if type(self) is DataMapping:
            raise TypeError("DataMapping is an abstract class.")

        super().__init__()

        # This attribute controls the direction into which the mapped SystemSignal is communicated with respect to the kind of PortPrototype used as the context element of the DataMapping.
        self.communicationDirection: Optional[CommunicationDirectionType] = None

        # Via this reference a connection between the VFB View and the Ethernet EventGroups can be created.
        self.eventGroupRefs: List[RefType] = []

        # Via this reference a connection between the VFB View and the Ethernet EventHandlers can be created.
        self.eventHandlerRefs: List[RefType] = []

        # This represents introductory documentation about the data mapping.
        self.introduction: Optional[DocumentationBlock] = None

        # Via this reference a connection between the VFB View and the Ethernet Services can be created.
        self.serviceInstanceRefs: List[RefType] = []

    def getCommunicationDirection(self) -> Optional[CommunicationDirectionType]:
        """
        This attribute controls the direction into which the mapped SystemSignal is communicated with respect to the kind of PortPrototype used as the context element of the DataMapping.
        """
        return self.communicationDirection

    def setCommunicationDirection(self, value: Optional[CommunicationDirectionType]) -> DataMapping:
        """
        This attribute controls the direction into which the mapped SystemSignal is communicated with respect to the kind of PortPrototype used as the context element of the DataMapping.
        A None value is a no-op and does not overwrite an existing communicationDirection.
        """
        if value is not None:
            self.communicationDirection = value
        return self

    def getEventGroupRefs(self) -> List[RefType]:
        """
        Via this reference a connection between the VFB View and the Ethernet EventGroups can be created.
        """
        return self.eventGroupRefs

    def addEventGroupRef(self, value: Optional[RefType]) -> DataMapping:
        """
        Via this reference a connection between the VFB View and the Ethernet EventGroups can be created.
        A None value is a no-op and does not extend the eventGroupRefs list.
        """
        if value is not None:
            self.eventGroupRefs.append(value)
        return self

    def getEventHandlerRefs(self) -> List[RefType]:
        """
        Via this reference a connection between the VFB View and the Ethernet EventHandlers can be created.
        """
        return self.eventHandlerRefs

    def addEventHandlerRef(self, value: Optional[RefType]) -> DataMapping:
        """
        Via this reference a connection between the VFB View and the Ethernet EventHandlers can be created.
        A None value is a no-op and does not extend the eventHandlerRefs list.
        """
        if value is not None:
            self.eventHandlerRefs.append(value)
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents introductory documentation about the data mapping.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> DataMapping:
        """
        This represents introductory documentation about the data mapping.
        A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self

    def getServiceInstanceRefs(self) -> List[RefType]:
        """
        Via this reference a connection between the VFB View and the Ethernet Services can be created.
        """
        return self.serviceInstanceRefs

    def addServiceInstanceRef(self, value: Optional[RefType]) -> DataMapping:
        """
        Via this reference a connection between the VFB View and the Ethernet Services can be created.
        A None value is a no-op and does not extend the serviceInstanceRefs list.
        """
        if value is not None:
            self.serviceInstanceRefs.append(value)
        return self


class SenderReceiverToSignalMapping(DataMapping):
    """
    Mapping of a sender receiver communication data element to a signal.

    [constr_5466] Existence of SenderReceiverToSignalMapping.dataElement: For each SenderReceiverToSignalMapping, the reference to VariableDataPrototype in the role dataElement shall exist at the time when the Ecu Extract is complete.

    [constr_5467] Existence of SenderReceiverToSignalMapping.systemSignal: For each SenderReceiverToSignalMapping, the reference to SystemSignal in the role systemSignal shall exist at the time when the Ecu Extract is complete.
    """

    # SenderReceiverToSignalMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.24, p.229
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElementIRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementIRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSenderToSignalTextTableMapping   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSenderToSignalTextTableMapping   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignalToReceiverTextTableMapping [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSignalToReceiverTextTableMapping [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSystemSignalRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSystemSignalRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the data element. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        self.dataElementIRef: Optional[VariableDataPrototypeInSystemInstanceRef] = None

        # This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal.
        self.senderToSignalTextTableMapping: Optional[TextTableMapping] = None

        # This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype.
        self.signalToReceiverTextTableMapping: Optional[TextTableMapping] = None

        # Reference to the system signal used to carry the data element.
        self.systemSignalRef: Optional[RefType] = None

    def getDataElementIRef(self) -> Optional[VariableDataPrototypeInSystemInstanceRef]:
        """
        Reference to the data element. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        """
        return self.dataElementIRef

    def setDataElementIRef(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]) -> SenderReceiverToSignalMapping:
        """
        Reference to the data element. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing dataElementIRef.
        """
        if value is not None:
            self.dataElementIRef = value
        return self

    def getSenderToSignalTextTableMapping(self) -> Optional[TextTableMapping]:
        """
        This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal.
        """
        return self.senderToSignalTextTableMapping

    def setSenderToSignalTextTableMapping(self, value: Optional[TextTableMapping]) -> SenderReceiverToSignalMapping:
        """
        This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal.
        A None value is a no-op and does not overwrite an existing senderToSignalTextTableMapping.
        """
        if value is not None:
            self.senderToSignalTextTableMapping = value
        return self

    def getSignalToReceiverTextTableMapping(self) -> Optional[TextTableMapping]:
        """
        This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype.
        """
        return self.signalToReceiverTextTableMapping

    def setSignalToReceiverTextTableMapping(self, value: Optional[TextTableMapping]) -> SenderReceiverToSignalMapping:
        """
        This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype.
        A None value is a no-op and does not overwrite an existing signalToReceiverTextTableMapping.
        """
        if value is not None:
            self.signalToReceiverTextTableMapping = value
        return self

    def getSystemSignalRef(self) -> Optional[RefType]:
        """
        Reference to the system signal used to carry the data element.
        """
        return self.systemSignalRef

    def setSystemSignalRef(self, value: Optional[RefType]) -> SenderReceiverToSignalMapping:
        """
        Reference to the system signal used to carry the data element.
        A None value is a no-op and does not overwrite an existing systemSignalRef.
        """
        if value is not None:
            self.systemSignalRef = value
        return self


class SenderRecCompositeTypeMapping(ARObject, ABC):
    """Two mappings exist for the composite data types: "ArrayTypeMapping" and "RecordTypeMapping". In both, a primitive datatype will be mapped to a system signal. But it is also possible to combine the arrays and the records, so that an "array" could be an element of a "record" and in the same manner a "record" could be an element of an "array". Nesting these data types is also possible. If an element of a composite data type is again a composite one, the "CompositeTypeMapping" element will be used one more time (aggregation between the ArrayElementMapping and CompositeTypeMapping or aggregation between the RecordElementMapping and CompositeTypeMapping)."""

    # SenderRecCompositeTypeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.27, p.235
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is SenderRecCompositeTypeMapping:
            raise TypeError("SenderRecCompositeTypeMapping is an abstract class.")

        super().__init__()


class SenderRecRecordElementMapping(ARObject):
    """
    Mapping of a primitive record element to a SystemSignal. If the VariableDataPrototype that is referenced by SenderReceiverToSignalGroupMapping is typed by an ApplicationDataType the reference application RecordElement shall be used. If the VariableDataPrototype is typed by the ImplementationDataType the reference implementationRecordElement shall be used. Either the implementationRecordElement or applicationRecordElement reference shall be used. If the element is composite, there will be no mapping to the SystemSignal (multiplicity 0). In this case the RecordElementMapping element will aggregate the complexTypeMapping element. In that way also the composite datatypes can be mapped to SystemSignals.
    """

    # SenderRecRecordElementMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.30, p.236
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationRecordElementRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationRecordElementRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComplexTypeMapping                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComplexTypeMapping                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImplementationRecordElementRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImplementationRecordElementRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSenderToSignalTextTableMapping    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSenderToSignalTextTableMapping    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignalToReceiverTextTableMapping  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSignalToReceiverTextTableMapping  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSystemSignalRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSystemSignalRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to an ApplicationRecordElement in the context of the dataElement or in the context of a composite element.
        self.applicationRecordElementRef: Optional[RefType] = None

        # This aggregation will be used if the element is composite.
        self.complexTypeMapping: Optional[SenderRecCompositeTypeMapping] = None

        # Reference to an ImplementationRecordElement in the context of the dataElement or in the context of a composite element.
        self.implementationRecordElementRef: Optional[RefType] = None

        # This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal.
        self.senderToSignalTextTableMapping: Optional[TextTableMapping] = None

        # This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype.
        self.signalToReceiverTextTableMapping: Optional[TextTableMapping] = None

        # Reference to the system signal used to carry the primitive ApplicationRecordElement.
        self.systemSignalRef: Optional[RefType] = None

    def getApplicationRecordElementRef(self) -> Optional[RefType]:
        """
        Reference to an ApplicationRecordElement in the context of the dataElement or in the context of a composite element.
        """
        return self.applicationRecordElementRef

    def setApplicationRecordElementRef(self, value: Optional[RefType]) -> SenderRecRecordElementMapping:
        """
        Reference to an ApplicationRecordElement in the context of the dataElement or in the context of a composite element.
        A None value is a no-op and does not overwrite an existing applicationRecordElementRef.
        """
        if value is not None:
            self.applicationRecordElementRef = value
        return self

    def getComplexTypeMapping(self) -> Optional[SenderRecCompositeTypeMapping]:
        """
        This aggregation will be used if the element is composite.
        """
        return self.complexTypeMapping

    def setComplexTypeMapping(self, value: Optional[SenderRecCompositeTypeMapping]) -> SenderRecRecordElementMapping:
        """
        This aggregation will be used if the element is composite.
        A None value is a no-op and does not overwrite an existing complexTypeMapping.
        """
        if value is not None:
            self.complexTypeMapping = value
        return self

    def getImplementationRecordElementRef(self) -> Optional[RefType]:
        """
        Reference to an ImplementationRecordElement in the context of the dataElement or in the context of a composite element.
        """
        return self.implementationRecordElementRef

    def setImplementationRecordElementRef(self, value: Optional[RefType]) -> SenderRecRecordElementMapping:
        """
        Reference to an ImplementationRecordElement in the context of the dataElement or in the context of a composite element.
        A None value is a no-op and does not overwrite an existing implementationRecordElementRef.
        """
        if value is not None:
            self.implementationRecordElementRef = value
        return self

    def getSenderToSignalTextTableMapping(self) -> Optional[TextTableMapping]:
        """
        This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal.
        """
        return self.senderToSignalTextTableMapping

    def setSenderToSignalTextTableMapping(self, value: Optional[TextTableMapping]) -> SenderRecRecordElementMapping:
        """
        This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal.
        A None value is a no-op and does not overwrite an existing senderToSignalTextTableMapping.
        """
        if value is not None:
            self.senderToSignalTextTableMapping = value
        return self

    def getSignalToReceiverTextTableMapping(self) -> Optional[TextTableMapping]:
        """
        This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype.
        """
        return self.signalToReceiverTextTableMapping

    def setSignalToReceiverTextTableMapping(self, value: Optional[TextTableMapping]) -> SenderRecRecordElementMapping:
        """
        This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype.
        A None value is a no-op and does not overwrite an existing signalToReceiverTextTableMapping.
        """
        if value is not None:
            self.signalToReceiverTextTableMapping = value
        return self

    def getSystemSignalRef(self) -> Optional[RefType]:
        """
        Reference to the system signal used to carry the primitive ApplicationRecordElement.
        """
        return self.systemSignalRef

    def setSystemSignalRef(self, value: Optional[RefType]) -> SenderRecRecordElementMapping:
        """
        Reference to the system signal used to carry the primitive ApplicationRecordElement.
        A None value is a no-op and does not overwrite an existing systemSignalRef.
        """
        if value is not None:
            self.systemSignalRef = value
        return self


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """If the ApplicationCompositeDataType is a Record, the "RecordTypeMapping" will be used."""

    # SenderRecRecordTypeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.29, p.236
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRecordElementMappings     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addRecordElementMapping      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Each ApplicationRecordElement shall be mapped on a SystemSignal.
        self.recordElementMappings: List[SenderRecRecordElementMapping] = []

    def getRecordElementMappings(self) -> List[SenderRecRecordElementMapping]:
        """
        Each ApplicationRecordElement shall be mapped on a SystemSignal.
        """
        return self.recordElementMappings

    def addRecordElementMapping(self, value: Optional[SenderRecRecordElementMapping]) -> SenderRecRecordTypeMapping:
        """
        Each ApplicationRecordElement shall be mapped on a SystemSignal.
        A None value is a no-op and does not extend the recordElementMappings list.
        """
        if value is not None:
            self.recordElementMappings.append(value)
        return self


class IndexedArrayElement(ARObject):
    """
    This element represents exactly one indexed element in the array. Either the applicationArrayElement or implementationArrayElement reference shall be used.

    [constr_5471] Existence of SenderRecArrayElementMapping.indexedArrayElement: For each SenderRecArrayElementMapping, the aggregation in the role indexedArrayElement shall exist at the time when the Ecu Extract is complete.

    [constr_5472] Existence of IndexedArrayElement.index: For each IndexedArrayElement, the attribute index shall exist at the time when the Ecu Extract is complete.

    [constr_3231] Usage of IndexedArrayElement.applicationArrayElement: IndexedArrayElement.applicationArrayElement shall only be used if the referenced context element (VariableDataPrototype that is referenced by the SenderReceiverToSignalGroupMapping.dataElement) is typed by an ApplicationDataType.

    [constr_3245] Usage of IndexedArrayElement.implementationArrayElement: IndexedArrayElement.implementationArrayElement shall only be used if the referenced context element (VariableDataPrototype that is referenced by the SenderReceiverToSignalGroupMapping.dataElement) is typed by an ImplementationDataType.
    """

    # IndexedArrayElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.32, p.237
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationArrayElementRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationArrayElementRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImplementationArrayElementRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImplementationArrayElementRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIndex                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIndex                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to an ApplicationArrayElement in an array.
        self.applicationArrayElementRef: Optional[RefType] = None

        # Reference to an ImplementationDataTypeElement in an array.
        self.implementationArrayElementRef: Optional[RefType] = None

        # Position of an element in an array. Starting position is 0.
        self.index: Optional[Integer] = None

    def getApplicationArrayElementRef(self) -> Optional[RefType]:
        """
        Reference to an ApplicationArrayElement in an array.
        """
        return self.applicationArrayElementRef

    def setApplicationArrayElementRef(self, value: Optional[RefType]) -> IndexedArrayElement:
        """
        Reference to an ApplicationArrayElement in an array.
        A None value is a no-op and does not overwrite an existing applicationArrayElementRef.
        """
        if value is not None:
            self.applicationArrayElementRef = value
        return self

    def getImplementationArrayElementRef(self) -> Optional[RefType]:
        """
        Reference to an ImplementationDataTypeElement in an array.
        """
        return self.implementationArrayElementRef

    def setImplementationArrayElementRef(self, value: Optional[RefType]) -> IndexedArrayElement:
        """
        Reference to an ImplementationDataTypeElement in an array.
        A None value is a no-op and does not overwrite an existing implementationArrayElementRef.
        """
        if value is not None:
            self.implementationArrayElementRef = value
        return self

    def getIndex(self) -> Optional[Integer]:
        """
        Position of an element in an array. Starting position is 0.
        """
        return self.index

    def setIndex(self, value: Optional[Integer]) -> IndexedArrayElement:
        """
        Position of an element in an array. Starting position is 0.
        A None value is a no-op and does not overwrite an existing index.
        """
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
    # Spec verified: R23-11
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

    def addArrayElementMapping(self, value: Optional[SenderRecArrayElementMapping]) -> SenderRecArrayTypeMapping:
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

    def setSenderToSignalTextTableMapping(self, value: Optional[TextTableMapping]) -> SenderRecArrayTypeMapping:
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

    def setSignalToReceiverTextTableMapping(self, value: Optional[TextTableMapping]) -> SenderRecArrayTypeMapping:
        """
        This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the PortPrototype.
        A None value is a no-op and does not overwrite an existing signalToReceiverTextTableMapping.
        """
        if value is not None:
            self.signalToReceiverTextTableMapping = value
        return self


class SenderReceiverToSignalGroupMapping(DataMapping):
    """
    Mapping of a sender receiver communication data element with a composite datatype to a signal group.

    [constr_5468] Existence of SenderReceiverToSignalGroupMapping.dataElement: For each SenderReceiverToSignalGroupMapping, the reference to VariableDataPrototype in the role dataElement shall exist at the time when the Ecu Extract is complete.

    [constr_5469] Existence of SenderReceiverToSignalGroupMapping.signalGroup: For each SenderReceiverToSignalGroupMapping, the reference to SystemSignalGroup in the role signalGroup shall exist at the time when the Ecu Extract is complete.

    [constr_5470] Existence of SenderReceiverToSignalGroupMapping.typeMapping: For each SenderReceiverToSignalGroupMapping, the aggregation of SenderRecCompositeTypeMapping in the role typeMapping shall exist at the time when the Ecu Extract is complete.
    """

    # SenderReceiverToSignalGroupMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.26, p.234
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElementIRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignalGroupRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSignalGroupRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTypeMapping      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTypeMapping      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to a data element with a composite datatype which is mapped to a signal group. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        self.dataElementIRef: Optional[VariableDataPrototypeInSystemInstanceRef] = None

        # Reference to the signal group, which contain all primitive datatypes of the composite type
        self.signalGroupRef: Optional[RefType] = None

        # The CompositeTypeMapping maps the ApplicationArrayElements and ApplicationRecordElements to Signals of the SignalGroup.
        self.typeMapping: Optional[SenderRecCompositeTypeMapping] = None

    def getDataElementIRef(self) -> Optional[VariableDataPrototypeInSystemInstanceRef]:
        """
        Reference to a data element with a composite datatype which is mapped to a signal group. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        """
        return self.dataElementIRef

    def setDataElementIRef(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]) -> SenderReceiverToSignalGroupMapping:
        """
        Reference to a data element with a composite datatype which is mapped to a signal group. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing dataElementIRef.
        """
        if value is not None:
            self.dataElementIRef = value
        return self

    def getSignalGroupRef(self) -> Optional[RefType]:
        """
        Reference to the signal group, which contain all primitive datatypes of the composite type
        """
        return self.signalGroupRef

    def setSignalGroupRef(self, value: Optional[RefType]) -> SenderReceiverToSignalGroupMapping:
        """
        Reference to the signal group, which contain all primitive datatypes of the composite type
        A None value is a no-op and does not overwrite an existing signalGroupRef.
        """
        if value is not None:
            self.signalGroupRef = value
        return self

    def getTypeMapping(self) -> Optional[SenderRecCompositeTypeMapping]:
        """
        The CompositeTypeMapping maps the ApplicationArrayElements and ApplicationRecordElements to Signals of the SignalGroup.
        """
        return self.typeMapping

    def setTypeMapping(self, value: Optional[SenderRecCompositeTypeMapping]) -> SenderReceiverToSignalGroupMapping:
        """
        The CompositeTypeMapping maps the ApplicationArrayElements and ApplicationRecordElements to Signals of the SignalGroup.
        A None value is a no-op and does not overwrite an existing typeMapping.
        """
        if value is not None:
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


class ClientServerToSignalMapping(DataMapping):
    pass


class SenderReceiverCompositeElementToSignalMapping(DataMapping):
    pass
