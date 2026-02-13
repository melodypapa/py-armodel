"""
AUTOSAR Package - DataMapping

Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (    ApplicationArray,    ApplicationRecord,    SenderRecArray,    SenderRecComposite,    SenderRecRecord,)from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (    DocumentationBlock,    ImplementationData,)from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (    ClientServerOperation,)from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate import (    SystemSignal,)

class DataMapping(ARObject, ABC):
    """
    Mapping of port elements (data elements and parameters) to frames and
    signals.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::DataMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 981, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 217, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataMapping:
            raise TypeError("DataMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
        self._introduction: Optional[DocumentationBlock] = None

    @property
    def introduction(self) -> Optional[DocumentationBlock]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value

    def with_array_element(self, value):
        """
        Set array_element and return self for chaining.

        Args:
            value: The array_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_element("value")
        """
        self.array_element = value  # Use property setter (gets validation)
        return self

    def with_record_element(self, value):
        """
        Set record_element and return self for chaining.

        Args:
            value: The record_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_record_element("value")
        """
        self.record_element = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: DocumentationBlock) -> DataMapping:
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional[DocumentationBlock]) -> DataMapping:
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self



class SenderRecCompositeTypeMapping(ARObject, ABC):
    """
    Two mappings exist for the composite data types: "ArrayTypeMapping" and
    "RecordTypeMapping". In both, a primitive datatype will be mapped to a
    system signal. But it is also possible to combine the arrays and the
    records, so that an "array" could be an element of a "record" and in the
    same manner a "record" could be an element of an "array". Nesting these data
    types is also possible. If an element of a composite data type is again a
    composite one, the "CompositeTypeMapping" element will be used one more time
    (aggregation between the ArrayElementMapping and CompositeType Mapping or
    aggregation between the RecordElementMapping and CompositeTypeMapping).

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecCompositeTypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is SenderRecCompositeTypeMapping:
            raise TypeError("SenderRecCompositeTypeMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SenderRecRecordElementMapping(ARObject):
    """
    Mapping of a primitive record element to a SystemSignal. If the
    VariableDataPrototype that is referenced by
    SenderReceiverToSignalGroupMapping is typed by an ApplicationDataType the
    reference application RecordElement shall be used. If the
    VariableDataPrototype is typed by the ImplementationDataType the reference
    implementationRecordElement shall be used. Either the
    implementationRecordElement or applicationRecordElement reference shall be
    used. If the element is composite, there will be no mapping to the
    SystemSignal (multiplicity 0). In this case the RecordElementMapping element
    will aggregate the complexTypeMapping element. In that way also the
    composite datatypes can be mapped to SystemSignals.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecRecordElementMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 236, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an ApplicationRecordElement in the context of the dataElement or
        # in the context of a composite.
        self._application: Optional[ApplicationRecord] = None

    @property
    def application(self) -> Optional[ApplicationRecord]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional[ApplicationRecord]) -> None:
        """
        Set application with validation.

        Args:
            value: The application to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, ApplicationRecord):
            raise TypeError(
                f"application must be ApplicationRecord or None, got {type(value).__name__}"
            )
        self._application = value
        self._complexType: Optional[SenderRecComposite] = None

    @property
    def complex_type(self) -> Optional[SenderRecComposite]:
        """Get complexType (Pythonic accessor)."""
        return self._complexType

    @complex_type.setter
    def complex_type(self, value: Optional[SenderRecComposite]) -> None:
        """
        Set complexType with validation.

        Args:
            value: The complexType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._complexType = None
            return

        if not isinstance(value, SenderRecComposite):
            raise TypeError(
                f"complexType must be SenderRecComposite or None, got {type(value).__name__}"
            )
        self._complexType = value
        # or in the context of a.
        self._implementation: Optional[ImplementationData] = None

    @property
    def implementation(self) -> Optional[ImplementationData]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional[ImplementationData]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, ImplementationData):
            raise TypeError(
                f"implementation must be ImplementationData or None, got {type(value).__name__}"
            )
        self._implementation = value
        # DataPrototype that is defined in the Port and the physicalProps defined for
        # the System.
        self._senderToSignal: Optional[RefType] = None

    @property
    def sender_to_signal(self) -> Optional[RefType]:
        """Get senderToSignal (Pythonic accessor)."""
        return self._senderToSignal

    @sender_to_signal.setter
    def sender_to_signal(self, value: Optional[RefType]) -> None:
        """
        Set senderToSignal with validation.

        Args:
            value: The senderToSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._senderToSignal = None
            return

        self._senderToSignal = value
        # defined for the SystemSignal and a DataPrototype that is defined in the Port.
        self._signalTo: Optional[RefType] = None

    @property
    def signal_to(self) -> Optional[RefType]:
        """Get signalTo (Pythonic accessor)."""
        return self._signalTo

    @signal_to.setter
    def signal_to(self, value: Optional[RefType]) -> None:
        """
        Set signalTo with validation.

        Args:
            value: The signalTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalTo = None
            return

        self._signalTo = value
        self._systemSignal: Optional[SystemSignal] = None

    @property
    def system_signal(self) -> Optional[SystemSignal]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional[SystemSignal]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> ApplicationRecord:
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: ApplicationRecord) -> SenderRecRecordElementMapping:
        """
        AUTOSAR-compliant setter for application with method chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    def getComplexType(self) -> "SenderRecComposite":
        """
        AUTOSAR-compliant getter for complexType.

        Returns:
            The complexType value

        Note:
            Delegates to complex_type property (CODING_RULE_V2_00017)
        """
        return self.complex_type  # Delegates to property

    def setComplexType(self, value: "SenderRecComposite") -> SenderRecRecordElementMapping:
        """
        AUTOSAR-compliant setter for complexType with method chaining.

        Args:
            value: The complexType to set

        Returns:
            self for method chaining

        Note:
            Delegates to complex_type property setter (gets validation automatically)
        """
        self.complex_type = value  # Delegates to property setter
        return self

    def getImplementation(self) -> "ImplementationData":
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "ImplementationData") -> SenderRecRecordElementMapping:
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getSenderToSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for senderToSignal.

        Returns:
            The senderToSignal value

        Note:
            Delegates to sender_to_signal property (CODING_RULE_V2_00017)
        """
        return self.sender_to_signal  # Delegates to property

    def setSenderToSignal(self, value: RefType) -> SenderRecRecordElementMapping:
        """
        AUTOSAR-compliant setter for senderToSignal with method chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to sender_to_signal property setter (gets validation automatically)
        """
        self.sender_to_signal = value  # Delegates to property setter
        return self

    def getSignalTo(self) -> RefType:
        """
        AUTOSAR-compliant getter for signalTo.

        Returns:
            The signalTo value

        Note:
            Delegates to signal_to property (CODING_RULE_V2_00017)
        """
        return self.signal_to  # Delegates to property

    def setSignalTo(self, value: RefType) -> SenderRecRecordElementMapping:
        """
        AUTOSAR-compliant setter for signalTo with method chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to signal_to property setter (gets validation automatically)
        """
        self.signal_to = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: SystemSignal) -> SenderRecRecordElementMapping:
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional[ApplicationRecord]) -> SenderRecRecordElementMapping:
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_complex_type(self, value: Optional[SenderRecComposite]) -> SenderRecRecordElementMapping:
        """
        Set complexType and return self for chaining.

        Args:
            value: The complexType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_complex_type("value")
        """
        self.complex_type = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value: Optional[ImplementationData]) -> SenderRecRecordElementMapping:
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_sender_to_signal(self, value: Optional[RefType]) -> SenderRecRecordElementMapping:
        """
        Set senderToSignal and return self for chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sender_to_signal("value")
        """
        self.sender_to_signal = value  # Use property setter (gets validation)
        return self

    def with_signal_to(self, value: Optional[RefType]) -> SenderRecRecordElementMapping:
        """
        Set signalTo and return self for chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_to("value")
        """
        self.signal_to = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> SenderRecRecordElementMapping:
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self



class SenderRecArrayElementMapping(ARObject):
    """
    The SenderRecArrayElement may be a primitive one or a composite one. If the
    element is primitive, it will be mapped to the SystemSignal (multiplicity
    1). If the VariableDataPrototype that is referenced by Sender
    ReceiverToSignalGroupMapping is typed by an ApplicationDataType the
    reference to the Application ArrayElement shall be used. If the
    VariableDataPrototype is typed by the ImplementationDataType the reference
    to the ImplementationArrayElement shall be used. If the element is
    composite, there will be no mapping to the SystemSignal (multiplicity 0). In
    this case the ArrayElementMapping element will aggregate the TypeMapping
    element. In that way also the composite datatypes can be mapped to
    SystemSignals. Regardless whether composite or primitive array element is
    mapped the indexed element always needs to be specified.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecArrayElementMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 237, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation will be used if the element is composite.
        self._complexType: Optional[SenderRecComposite] = None

    @property
    def complex_type(self) -> Optional[SenderRecComposite]:
        """Get complexType (Pythonic accessor)."""
        return self._complexType

    @complex_type.setter
    def complex_type(self, value: Optional[SenderRecComposite]) -> None:
        """
        Set complexType with validation.

        Args:
            value: The complexType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._complexType = None
            return

        if not isinstance(value, SenderRecComposite):
            raise TypeError(
                f"complexType must be SenderRecComposite or None, got {type(value).__name__}"
            )
        self._complexType = value
        # context of a composite element.
        self._indexedArray: Optional[IndexedArrayElement] = None

    @property
    def indexed_array(self) -> Optional[IndexedArrayElement]:
        """Get indexedArray (Pythonic accessor)."""
        return self._indexedArray

    @indexed_array.setter
    def indexed_array(self, value: Optional[IndexedArrayElement]) -> None:
        """
        Set indexedArray with validation.

        Args:
            value: The indexedArray to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indexedArray = None
            return

        if not isinstance(value, IndexedArrayElement):
            raise TypeError(
                f"indexedArray must be IndexedArrayElement or None, got {type(value).__name__}"
            )
        self._indexedArray = value
        self._systemSignal: Optional[SystemSignal] = None

    @property
    def system_signal(self) -> Optional[SystemSignal]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional[SystemSignal]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComplexType(self) -> "SenderRecComposite":
        """
        AUTOSAR-compliant getter for complexType.

        Returns:
            The complexType value

        Note:
            Delegates to complex_type property (CODING_RULE_V2_00017)
        """
        return self.complex_type  # Delegates to property

    def setComplexType(self, value: "SenderRecComposite") -> SenderRecArrayElementMapping:
        """
        AUTOSAR-compliant setter for complexType with method chaining.

        Args:
            value: The complexType to set

        Returns:
            self for method chaining

        Note:
            Delegates to complex_type property setter (gets validation automatically)
        """
        self.complex_type = value  # Delegates to property setter
        return self

    def getIndexedArray(self) -> IndexedArrayElement:
        """
        AUTOSAR-compliant getter for indexedArray.

        Returns:
            The indexedArray value

        Note:
            Delegates to indexed_array property (CODING_RULE_V2_00017)
        """
        return self.indexed_array  # Delegates to property

    def setIndexedArray(self, value: IndexedArrayElement) -> SenderRecArrayElementMapping:
        """
        AUTOSAR-compliant setter for indexedArray with method chaining.

        Args:
            value: The indexedArray to set

        Returns:
            self for method chaining

        Note:
            Delegates to indexed_array property setter (gets validation automatically)
        """
        self.indexed_array = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: SystemSignal) -> SenderRecArrayElementMapping:
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_complex_type(self, value: Optional[SenderRecComposite]) -> SenderRecArrayElementMapping:
        """
        Set complexType and return self for chaining.

        Args:
            value: The complexType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_complex_type("value")
        """
        self.complex_type = value  # Use property setter (gets validation)
        return self

    def with_indexed_array(self, value: Optional[IndexedArrayElement]) -> SenderRecArrayElementMapping:
        """
        Set indexedArray and return self for chaining.

        Args:
            value: The indexedArray to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_indexed_array("value")
        """
        self.indexed_array = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> SenderRecArrayElementMapping:
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self



class IndexedArrayElement(ARObject):
    """
    This element represents exactly one indexed element in the array. Either the
    applicationArrayElement or implementationArrayElement reference shall be
    used.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::IndexedArrayElement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 237, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an ApplicationArrayElement in an array.
        self._applicationArray: Optional[ApplicationArray] = None

    @property
    def application_array(self) -> Optional[ApplicationArray]:
        """Get applicationArray (Pythonic accessor)."""
        return self._applicationArray

    @application_array.setter
    def application_array(self, value: Optional[ApplicationArray]) -> None:
        """
        Set applicationArray with validation.

        Args:
            value: The applicationArray to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationArray = None
            return

        if not isinstance(value, ApplicationArray):
            raise TypeError(
                f"applicationArray must be ApplicationArray or None, got {type(value).__name__}"
            )
        self._applicationArray = value
        self._implementation: Optional[ImplementationData] = None

    @property
    def implementation(self) -> Optional[ImplementationData]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional[ImplementationData]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, ImplementationData):
            raise TypeError(
                f"implementation must be ImplementationData or None, got {type(value).__name__}"
            )
        self._implementation = value
        # Starting position is 0.
        self._index: Optional[Integer] = None

    @property
    def index(self) -> Optional[Integer]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional[Integer]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"index must be Integer or int or None, got {type(value).__name__}"
            )
        self._index = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplicationArray(self) -> ApplicationArray:
        """
        AUTOSAR-compliant getter for applicationArray.

        Returns:
            The applicationArray value

        Note:
            Delegates to application_array property (CODING_RULE_V2_00017)
        """
        return self.application_array  # Delegates to property

    def setApplicationArray(self, value: ApplicationArray) -> IndexedArrayElement:
        """
        AUTOSAR-compliant setter for applicationArray with method chaining.

        Args:
            value: The applicationArray to set

        Returns:
            self for method chaining

        Note:
            Delegates to application_array property setter (gets validation automatically)
        """
        self.application_array = value  # Delegates to property setter
        return self

    def getImplementation(self) -> "ImplementationData":
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "ImplementationData") -> IndexedArrayElement:
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getIndex(self) -> Integer:
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: Integer) -> IndexedArrayElement:
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application_array(self, value: Optional[ApplicationArray]) -> IndexedArrayElement:
        """
        Set applicationArray and return self for chaining.

        Args:
            value: The applicationArray to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application_array("value")
        """
        self.application_array = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value: Optional[ImplementationData]) -> IndexedArrayElement:
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_index(self, value: Optional[Integer]) -> IndexedArrayElement:
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self



class SenderReceiverToSignalMapping(DataMapping):
    """
    Mapping of a sender receiver communication data element to a signal.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderReceiverToSignalMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1005, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 229, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: VariableDataPrototypeIn.
        self._dataElementSystemInstanceRef: Optional[RefType] = None

    @property
    def data_element_system_instance_ref(self) -> Optional[RefType]:
        """Get dataElementSystemInstanceRef (Pythonic accessor)."""
        return self._dataElementSystemInstanceRef

    @data_element_system_instance_ref.setter
    def data_element_system_instance_ref(self, value: Optional[RefType]) -> None:
        """
        Set dataElementSystemInstanceRef with validation.

        Args:
            value: The dataElementSystemInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElementSystemInstanceRef = None
            return

        self._dataElementSystemInstanceRef = value
        # DataPrototype that is defined in the Port and the physicalProps defined for
        # the System.
        self._senderToSignal: Optional[RefType] = None

    @property
    def sender_to_signal(self) -> Optional[RefType]:
        """Get senderToSignal (Pythonic accessor)."""
        return self._senderToSignal

    @sender_to_signal.setter
    def sender_to_signal(self, value: Optional[RefType]) -> None:
        """
        Set senderToSignal with validation.

        Args:
            value: The senderToSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._senderToSignal = None
            return

        self._senderToSignal = value
        # defined for the SystemSignal and a DataPrototype that is defined in the Port.
        self._signalTo: Optional[RefType] = None

    @property
    def signal_to(self) -> Optional[RefType]:
        """Get signalTo (Pythonic accessor)."""
        return self._signalTo

    @signal_to.setter
    def signal_to(self, value: Optional[RefType]) -> None:
        """
        Set signalTo with validation.

        Args:
            value: The signalTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalTo = None
            return

        self._signalTo = value
        self._systemSignal: Optional[SystemSignal] = None

    @property
    def system_signal(self) -> Optional[SystemSignal]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional[SystemSignal]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElementSystemInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElementSystemInstanceRef.

        Returns:
            The dataElementSystemInstanceRef value

        Note:
            Delegates to data_element_system_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.data_element_system_instance_ref  # Delegates to property

    def setDataElementSystemInstanceRef(self, value: RefType) -> SenderReceiverToSignalMapping:
        """
        AUTOSAR-compliant setter for dataElementSystemInstanceRef with method chaining.

        Args:
            value: The dataElementSystemInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element_system_instance_ref property setter (gets validation automatically)
        """
        self.data_element_system_instance_ref = value  # Delegates to property setter
        return self

    def getSenderToSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for senderToSignal.

        Returns:
            The senderToSignal value

        Note:
            Delegates to sender_to_signal property (CODING_RULE_V2_00017)
        """
        return self.sender_to_signal  # Delegates to property

    def setSenderToSignal(self, value: RefType) -> SenderReceiverToSignalMapping:
        """
        AUTOSAR-compliant setter for senderToSignal with method chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to sender_to_signal property setter (gets validation automatically)
        """
        self.sender_to_signal = value  # Delegates to property setter
        return self

    def getSignalTo(self) -> RefType:
        """
        AUTOSAR-compliant getter for signalTo.

        Returns:
            The signalTo value

        Note:
            Delegates to signal_to property (CODING_RULE_V2_00017)
        """
        return self.signal_to  # Delegates to property

    def setSignalTo(self, value: RefType) -> SenderReceiverToSignalMapping:
        """
        AUTOSAR-compliant setter for signalTo with method chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to signal_to property setter (gets validation automatically)
        """
        self.signal_to = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: SystemSignal) -> SenderReceiverToSignalMapping:
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element_system_instance_ref(self, value: Optional[RefType]) -> SenderReceiverToSignalMapping:
        """
        Set dataElementSystemInstanceRef and return self for chaining.

        Args:
            value: The dataElementSystemInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element_system_instance_ref("value")
        """
        self.data_element_system_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_sender_to_signal(self, value: Optional[RefType]) -> SenderReceiverToSignalMapping:
        """
        Set senderToSignal and return self for chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sender_to_signal("value")
        """
        self.sender_to_signal = value  # Use property setter (gets validation)
        return self

    def with_signal_to(self, value: Optional[RefType]) -> SenderReceiverToSignalMapping:
        """
        Set signalTo and return self for chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_to("value")
        """
        self.signal_to = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> SenderReceiverToSignalMapping:
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self



class SenderReceiverToSignalGroupMapping(DataMapping):
    """
    Mapping of a sender receiver communication data element with a composite
    datatype to a signal group.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderReceiverToSignalGroupMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 234, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # mapped to a signal group.
        # by: VariableDataPrototypeIn.
        self._dataElement: Optional[RefType] = None

    @property
    def data_element(self) -> Optional[RefType]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional[RefType]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # type.
        self._signalGroup: Optional[RefType] = None

    @property
    def signal_group(self) -> Optional[RefType]:
        """Get signalGroup (Pythonic accessor)."""
        return self._signalGroup

    @signal_group.setter
    def signal_group(self, value: Optional[RefType]) -> None:
        """
        Set signalGroup with validation.

        Args:
            value: The signalGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalGroup = None
            return

        self._signalGroup = value
        # ApplicationRecordElements to Signals of.
        self._typeMapping: Optional[SenderRecComposite] = None

    @property
    def type_mapping(self) -> Optional[SenderRecComposite]:
        """Get typeMapping (Pythonic accessor)."""
        return self._typeMapping

    @type_mapping.setter
    def type_mapping(self, value: Optional[SenderRecComposite]) -> None:
        """
        Set typeMapping with validation.

        Args:
            value: The typeMapping to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeMapping = None
            return

        if not isinstance(value, SenderRecComposite):
            raise TypeError(
                f"typeMapping must be SenderRecComposite or None, got {type(value).__name__}"
            )
        self._typeMapping = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> SenderReceiverToSignalGroupMapping:
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getSignalGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for signalGroup.

        Returns:
            The signalGroup value

        Note:
            Delegates to signal_group property (CODING_RULE_V2_00017)
        """
        return self.signal_group  # Delegates to property

    def setSignalGroup(self, value: RefType) -> SenderReceiverToSignalGroupMapping:
        """
        AUTOSAR-compliant setter for signalGroup with method chaining.

        Args:
            value: The signalGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to signal_group property setter (gets validation automatically)
        """
        self.signal_group = value  # Delegates to property setter
        return self

    def getTypeMapping(self) -> "SenderRecComposite":
        """
        AUTOSAR-compliant getter for typeMapping.

        Returns:
            The typeMapping value

        Note:
            Delegates to type_mapping property (CODING_RULE_V2_00017)
        """
        return self.type_mapping  # Delegates to property

    def setTypeMapping(self, value: "SenderRecComposite") -> SenderReceiverToSignalGroupMapping:
        """
        AUTOSAR-compliant setter for typeMapping with method chaining.

        Args:
            value: The typeMapping to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_mapping property setter (gets validation automatically)
        """
        self.type_mapping = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> SenderReceiverToSignalGroupMapping:
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_signal_group(self, value: Optional[RefType]) -> SenderReceiverToSignalGroupMapping:
        """
        Set signalGroup and return self for chaining.

        Args:
            value: The signalGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_group("value")
        """
        self.signal_group = value  # Use property setter (gets validation)
        return self

    def with_type_mapping(self, value: Optional[SenderRecComposite]) -> SenderReceiverToSignalGroupMapping:
        """
        Set typeMapping and return self for chaining.

        Args:
            value: The typeMapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_mapping("value")
        """
        self.type_mapping = value  # Use property setter (gets validation)
        return self



class ClientServerToSignalMapping(DataMapping):
    """
    This element maps the ClientServerOperation to call- and
    return-SystemSignals.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::ClientServerToSignalMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 242, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the callSignal to which the IN and INOUT mapped.
        self._callSignal: Optional[SystemSignal] = None

    @property
    def call_signal(self) -> Optional[SystemSignal]:
        """Get callSignal (Pythonic accessor)."""
        return self._callSignal

    @call_signal.setter
    def call_signal(self, value: Optional[SystemSignal]) -> None:
        """
        Set callSignal with validation.

        Args:
            value: The callSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._callSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"callSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._callSignal = value
        # by: OperationInSystem.
        self._clientServer: Optional[ClientServerOperation] = None

    @property
    def client_server(self) -> Optional[ClientServerOperation]:
        """Get clientServer (Pythonic accessor)."""
        return self._clientServer

    @client_server.setter
    def client_server(self, value: Optional[ClientServerOperation]) -> None:
        """
        Set clientServer with validation.

        Args:
            value: The clientServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientServer = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"clientServer must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._clientServer = value
        self._returnSignal: Optional[SystemSignal] = None

    @property
    def return_signal(self) -> Optional[SystemSignal]:
        """Get returnSignal (Pythonic accessor)."""
        return self._returnSignal

    @return_signal.setter
    def return_signal(self, value: Optional[SystemSignal]) -> None:
        """
        Set returnSignal with validation.

        Args:
            value: The returnSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._returnSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"returnSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._returnSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCallSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for callSignal.

        Returns:
            The callSignal value

        Note:
            Delegates to call_signal property (CODING_RULE_V2_00017)
        """
        return self.call_signal  # Delegates to property

    def setCallSignal(self, value: SystemSignal) -> ClientServerToSignalMapping:
        """
        AUTOSAR-compliant setter for callSignal with method chaining.

        Args:
            value: The callSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to call_signal property setter (gets validation automatically)
        """
        self.call_signal = value  # Delegates to property setter
        return self

    def getClientServer(self) -> ClientServerOperation:
        """
        AUTOSAR-compliant getter for clientServer.

        Returns:
            The clientServer value

        Note:
            Delegates to client_server property (CODING_RULE_V2_00017)
        """
        return self.client_server  # Delegates to property

    def setClientServer(self, value: ClientServerOperation) -> ClientServerToSignalMapping:
        """
        AUTOSAR-compliant setter for clientServer with method chaining.

        Args:
            value: The clientServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_server property setter (gets validation automatically)
        """
        self.client_server = value  # Delegates to property setter
        return self

    def getReturnSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for returnSignal.

        Returns:
            The returnSignal value

        Note:
            Delegates to return_signal property (CODING_RULE_V2_00017)
        """
        return self.return_signal  # Delegates to property

    def setReturnSignal(self, value: SystemSignal) -> ClientServerToSignalMapping:
        """
        AUTOSAR-compliant setter for returnSignal with method chaining.

        Args:
            value: The returnSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to return_signal property setter (gets validation automatically)
        """
        self.return_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_call_signal(self, value: Optional[SystemSignal]) -> ClientServerToSignalMapping:
        """
        Set callSignal and return self for chaining.

        Args:
            value: The callSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_call_signal("value")
        """
        self.call_signal = value  # Use property setter (gets validation)
        return self

    def with_client_server(self, value: Optional[ClientServerOperation]) -> ClientServerToSignalMapping:
        """
        Set clientServer and return self for chaining.

        Args:
            value: The clientServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server("value")
        """
        self.client_server = value  # Use property setter (gets validation)
        return self

    def with_return_signal(self, value: Optional[SystemSignal]) -> ClientServerToSignalMapping:
        """
        Set returnSignal and return self for chaining.

        Args:
            value: The returnSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_return_signal("value")
        """
        self.return_signal = value  # Use property setter (gets validation)
        return self



class SenderReceiverCompositeElementToSignalMapping(DataMapping):
    """
    Mapping of an Variable Data Prototype which is aggregated within a composite
    datatype to a System Signal (only one element of the composite data type is
    mapped).

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderReceiverCompositeElementToSignalMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 247, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # one element is mapped to a SystemSignal.
        # by: VariableDataPrototypeIn.
        self._dataElement: Optional[RefType] = None

    @property
    def data_element(self) -> Optional[RefType]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional[RefType]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        self._systemSignal: Optional[SystemSignal] = None

    @property
    def system_signal(self) -> Optional[SystemSignal]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional[SystemSignal]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value
        # a SystemSignal.
        self._typeMapping: Optional[SenderRecComposite] = None

    @property
    def type_mapping(self) -> Optional[SenderRecComposite]:
        """Get typeMapping (Pythonic accessor)."""
        return self._typeMapping

    @type_mapping.setter
    def type_mapping(self, value: Optional[SenderRecComposite]) -> None:
        """
        Set typeMapping with validation.

        Args:
            value: The typeMapping to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeMapping = None
            return

        if not isinstance(value, SenderRecComposite):
            raise TypeError(
                f"typeMapping must be SenderRecComposite or None, got {type(value).__name__}"
            )
        self._typeMapping = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> SenderReceiverCompositeElementToSignalMapping:
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: SystemSignal) -> SenderReceiverCompositeElementToSignalMapping:
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    def getTypeMapping(self) -> "SenderRecComposite":
        """
        AUTOSAR-compliant getter for typeMapping.

        Returns:
            The typeMapping value

        Note:
            Delegates to type_mapping property (CODING_RULE_V2_00017)
        """
        return self.type_mapping  # Delegates to property

    def setTypeMapping(self, value: "SenderRecComposite") -> SenderReceiverCompositeElementToSignalMapping:
        """
        AUTOSAR-compliant setter for typeMapping with method chaining.

        Args:
            value: The typeMapping to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_mapping property setter (gets validation automatically)
        """
        self.type_mapping = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> SenderReceiverCompositeElementToSignalMapping:
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> SenderReceiverCompositeElementToSignalMapping:
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self

    def with_type_mapping(self, value: Optional[SenderRecComposite]) -> SenderReceiverCompositeElementToSignalMapping:
        """
        Set typeMapping and return self for chaining.

        Args:
            value: The typeMapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_mapping("value")
        """
        self.type_mapping = value  # Use property setter (gets validation)
        return self



class TriggerToSignalMapping(DataMapping):
    """
    This meta-class represents the ability to map a trigger to a SystemSignal of
    size 0. The Trigger does not transport any other information than its
    existence, therefore the limitation in terms of signal length.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::TriggerToSignalMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 249, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the SystemSignal taken to transport the Trigger network.
        self._systemSignal: Optional[SystemSignal] = None

    @property
    def system_signal(self) -> Optional[SystemSignal]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional[SystemSignal]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value
        # by: TriggerInSystemInstance.
        self._triggerRef: Optional[RefType] = None

    @property
    def trigger_ref(self) -> Optional[RefType]:
        """Get triggerRef (Pythonic accessor)."""
        return self._triggerRef

    @trigger_ref.setter
    def trigger_ref(self, value: Optional[RefType]) -> None:
        """
        Set triggerRef with validation.

        Args:
            value: The triggerRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerRef = None
            return

        self._triggerRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSystemSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: SystemSignal) -> TriggerToSignalMapping:
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    def getTriggerRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for triggerRef.

        Returns:
            The triggerRef value

        Note:
            Delegates to trigger_ref property (CODING_RULE_V2_00017)
        """
        return self.trigger_ref  # Delegates to property

    def setTriggerRef(self, value: RefType) -> TriggerToSignalMapping:
        """
        AUTOSAR-compliant setter for triggerRef with method chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger_ref property setter (gets validation automatically)
        """
        self.trigger_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_system_signal(self, value: Optional[SystemSignal]) -> TriggerToSignalMapping:
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self

    def with_trigger_ref(self, value: Optional[RefType]) -> TriggerToSignalMapping:
        """
        Set triggerRef and return self for chaining.

        Args:
            value: The triggerRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_ref("value")
        """
        self.trigger_ref = value  # Use property setter (gets validation)
        return self



class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """
    If the ApplicationCompositeDataType is an Array, the "ArrayTypeMapping" will
    be used.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecArrayTypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Each ApplicationArrayElement shall be mapped on a SystemSignal.
        self._arrayElement: List[SenderRecArray] = []

    @property
    def array_element(self) -> List[SenderRecArray]:
        """Get arrayElement (Pythonic accessor)."""
        return self._arrayElement
        # This mapping allows for the text-table translation between sending
        # DataPrototype that is defined in the Port and the physicalProps defined for
        # the System.
        self._senderToSignal: Optional[RefType] = None

    @property
    def sender_to_signal(self) -> Optional[RefType]:
        """Get senderToSignal (Pythonic accessor)."""
        return self._senderToSignal

    @sender_to_signal.setter
    def sender_to_signal(self, value: Optional[RefType]) -> None:
        """
        Set senderToSignal with validation.

        Args:
            value: The senderToSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._senderToSignal = None
            return

        self._senderToSignal = value
        # defined for the SystemSignal and a DataPrototype that is defined in the Port.
        self._signalTo: Optional[RefType] = None

    @property
    def signal_to(self) -> Optional[RefType]:
        """Get signalTo (Pythonic accessor)."""
        return self._signalTo

    @signal_to.setter
    def signal_to(self, value: Optional[RefType]) -> None:
        """
        Set signalTo with validation.

        Args:
            value: The signalTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalTo = None
            return

        self._signalTo = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArrayElement(self) -> List[SenderRecArray]:
        """
        AUTOSAR-compliant getter for arrayElement.

        Returns:
            The arrayElement value

        Note:
            Delegates to array_element property (CODING_RULE_V2_00017)
        """
        return self.array_element  # Delegates to property

    def getSenderToSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for senderToSignal.

        Returns:
            The senderToSignal value

        Note:
            Delegates to sender_to_signal property (CODING_RULE_V2_00017)
        """
        return self.sender_to_signal  # Delegates to property

    def setSenderToSignal(self, value: RefType) -> SenderRecArrayTypeMapping:
        """
        AUTOSAR-compliant setter for senderToSignal with method chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to sender_to_signal property setter (gets validation automatically)
        """
        self.sender_to_signal = value  # Delegates to property setter
        return self

    def getSignalTo(self) -> RefType:
        """
        AUTOSAR-compliant getter for signalTo.

        Returns:
            The signalTo value

        Note:
            Delegates to signal_to property (CODING_RULE_V2_00017)
        """
        return self.signal_to  # Delegates to property

    def setSignalTo(self, value: RefType) -> SenderRecArrayTypeMapping:
        """
        AUTOSAR-compliant setter for signalTo with method chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to signal_to property setter (gets validation automatically)
        """
        self.signal_to = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sender_to_signal(self, value: Optional[RefType]) -> SenderRecArrayTypeMapping:
        """
        Set senderToSignal and return self for chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sender_to_signal("value")
        """
        self.sender_to_signal = value  # Use property setter (gets validation)
        return self

    def with_signal_to(self, value: Optional[RefType]) -> SenderRecArrayTypeMapping:
        """
        Set signalTo and return self for chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_to("value")
        """
        self.signal_to = value  # Use property setter (gets validation)
        return self



class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """
    If the ApplicationCompositeDataType is a Record, the "RecordTypeMapping"
    will be used.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecRecordTypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Each ApplicationRecordElement shall be mapped on a SystemSignal.
        self._recordElement: List[SenderRecRecord] = []

    @property
    def record_element(self) -> List[SenderRecRecord]:
        """Get recordElement (Pythonic accessor)."""
        return self._recordElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRecordElement(self) -> List[SenderRecRecord]:
        """
        AUTOSAR-compliant getter for recordElement.

        Returns:
            The recordElement value

        Note:
            Delegates to record_element property (CODING_RULE_V2_00017)
        """
        return self.record_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class DataTypePolicyEnum(AREnum):
    """
    DataTypePolicyEnum enumeration

This class lists the supported DataTypePolicies. Aggregated by ISignal.dataTypePolicy

Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping
    """
    # This literal indicates that this ISignal is used to transport a message as part of a service for Dds.
    ddsService = "6"

    # This literal indicates that this ISignal is used to transport a signal based signal for Dds.
    ddsSignal = "5"

    # In case the System Description doesn’t use a complete Software Component Description (VFB View) this value can be chosen. This supports the inclusion of legacy signals. The aggregation of SwDataDefProps shall be used to configure the "ComSignalDataInvalidValue" and the Data Semantics.
    legacy = "0"

    # Ignore any networkRepresentationProps of this ISignal and use the networkRepresentation from the
    network = "None"

    # ComSpec.
    Representation = "None"

    # Please note that the usage does not imply the existence of the SwDataDefProps in the role network Representation aggregated by the SenderComSpec or ReceiverComSpec if an ImplementationData Type is defined.
    FromComSpec = "1"

    # If this value is chosen the requirements specified in the ComSpec (networkRepresentationFromCom specified by the aggregated swDataDefProps.
    override = "2"

    # This literal indicates that a transformer chain shall be used to communicate the ISignal as UINT8_N over the bus.
    transformingISignal = "4"
