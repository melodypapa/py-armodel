from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ApplicationRecord,
    ImplementationData,
    SenderRecComposite,
    SystemSignal,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
        self._application: Optional["ApplicationRecord"] = None

    @property
    def application(self) -> Optional["ApplicationRecord"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationRecord"]) -> None:
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
        # This aggregation will be used if the element is composite.
        self._complexType: Optional["SenderRecComposite"] = None

    @property
    def complex_type(self) -> Optional["SenderRecComposite"]:
        """Get complexType (Pythonic accessor)."""
        return self._complexType

    @complex_type.setter
    def complex_type(self, value: Optional["SenderRecComposite"]) -> None:
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
        # Reference to an ImplementationRecordElement in the context of the dataElement
        # or in the context of a.
        self._implementation: Optional["ImplementationData"] = None

    @property
    def implementation(self) -> Optional["ImplementationData"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["ImplementationData"]) -> None:
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
        # This mapping allows for the text-table translation between sending
        # DataPrototype that is defined in the Port and the physicalProps defined for
        # the System.
        self._senderToSignal: RefType = None

    @property
    def sender_to_signal(self) -> RefType:
        """Get senderToSignal (Pythonic accessor)."""
        return self._senderToSignal

    @sender_to_signal.setter
    def sender_to_signal(self, value: RefType) -> None:
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
        # This mapping allows for the text-table translation between physicalProps
        # defined for the SystemSignal and a DataPrototype that is defined in the Port.
        self._signalTo: RefType = None

    @property
    def signal_to(self) -> RefType:
        """Get signalTo (Pythonic accessor)."""
        return self._signalTo

    @signal_to.setter
    def signal_to(self, value: RefType) -> None:
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
        # Reference to the system signal used to carry the primitive.
        self._systemSignal: Optional["SystemSignal"] = None

    @property
    def system_signal(self) -> Optional["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["SystemSignal"]) -> None:
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

    def getApplication(self) -> "ApplicationRecord":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationRecord") -> "SenderRecRecordElementMapping":
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

    def setComplexType(self, value: "SenderRecComposite") -> "SenderRecRecordElementMapping":
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

    def setImplementation(self, value: "ImplementationData") -> "SenderRecRecordElementMapping":
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

    def setSenderToSignal(self, value: RefType) -> "SenderRecRecordElementMapping":
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

    def setSignalTo(self, value: RefType) -> "SenderRecRecordElementMapping":
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

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "SenderRecRecordElementMapping":
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

    def with_application(self, value: Optional["ApplicationRecord"]) -> "SenderRecRecordElementMapping":
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

    def with_complex_type(self, value: Optional["SenderRecComposite"]) -> "SenderRecRecordElementMapping":
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

    def with_implementation(self, value: Optional["ImplementationData"]) -> "SenderRecRecordElementMapping":
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

    def with_sender_to_signal(self, value: Optional[RefType]) -> "SenderRecRecordElementMapping":
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

    def with_signal_to(self, value: Optional[RefType]) -> "SenderRecRecordElementMapping":
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

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "SenderRecRecordElementMapping":
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
