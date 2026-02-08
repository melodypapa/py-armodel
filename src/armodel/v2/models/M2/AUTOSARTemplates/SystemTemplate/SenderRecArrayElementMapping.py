from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


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
        # Reference to an indexed array element in the context of dataElement or in the
        # context of a composite element.
        self._indexedArray: Optional["IndexedArrayElement"] = None

    @property
    def indexed_array(self) -> Optional["IndexedArrayElement"]:
        """Get indexedArray (Pythonic accessor)."""
        return self._indexedArray

    @indexed_array.setter
    def indexed_array(self, value: Optional["IndexedArrayElement"]) -> None:
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

    def getComplexType(self) -> "SenderRecComposite":
        """
        AUTOSAR-compliant getter for complexType.

        Returns:
            The complexType value

        Note:
            Delegates to complex_type property (CODING_RULE_V2_00017)
        """
        return self.complex_type  # Delegates to property

    def setComplexType(self, value: "SenderRecComposite") -> "SenderRecArrayElementMapping":
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

    def getIndexedArray(self) -> "IndexedArrayElement":
        """
        AUTOSAR-compliant getter for indexedArray.

        Returns:
            The indexedArray value

        Note:
            Delegates to indexed_array property (CODING_RULE_V2_00017)
        """
        return self.indexed_array  # Delegates to property

    def setIndexedArray(self, value: "IndexedArrayElement") -> "SenderRecArrayElementMapping":
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

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "SenderRecArrayElementMapping":
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

    def with_complex_type(self, value: Optional["SenderRecComposite"]) -> "SenderRecArrayElementMapping":
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

    def with_indexed_array(self, value: Optional["IndexedArrayElement"]) -> "SenderRecArrayElementMapping":
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

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "SenderRecArrayElementMapping":
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
