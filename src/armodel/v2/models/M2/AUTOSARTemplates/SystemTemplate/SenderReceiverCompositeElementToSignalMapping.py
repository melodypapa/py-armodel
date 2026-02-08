from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DataMapping,
    SenderRecComposite,
    SystemSignal,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
        self._dataElement: RefType = None

    @property
    def data_element(self) -> RefType:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: RefType) -> None:
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
        # Reference to the SystemSignal to which one primitive of type is mapped.
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
        # The CompositeTypeMapping maps one VariableData of the composite data type to
        # a SystemSignal.
        self._typeMapping: Optional["SenderRecComposite"] = None

    @property
    def type_mapping(self) -> Optional["SenderRecComposite"]:
        """Get typeMapping (Pythonic accessor)."""
        return self._typeMapping

    @type_mapping.setter
    def type_mapping(self, value: Optional["SenderRecComposite"]) -> None:
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

    def setDataElement(self, value: RefType) -> "SenderReceiverCompositeElementToSignalMapping":
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

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "SenderReceiverCompositeElementToSignalMapping":
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

    def setTypeMapping(self, value: "SenderRecComposite") -> "SenderReceiverCompositeElementToSignalMapping":
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

    def with_data_element(self, value: Optional[RefType]) -> "SenderReceiverCompositeElementToSignalMapping":
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

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "SenderReceiverCompositeElementToSignalMapping":
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

    def with_type_mapping(self, value: Optional["SenderRecComposite"]) -> "SenderReceiverCompositeElementToSignalMapping":
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
