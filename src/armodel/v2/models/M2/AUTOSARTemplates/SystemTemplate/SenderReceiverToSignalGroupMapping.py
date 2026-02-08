from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping

    RefType,
)


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
        # Reference to the signal group, which contain all primitive the composite
        # type.
        self._signalGroup: RefType = None

    @property
    def signal_group(self) -> RefType:
        """Get signalGroup (Pythonic accessor)."""
        return self._signalGroup

    @signal_group.setter
    def signal_group(self, value: RefType) -> None:
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
        # The CompositeTypeMapping maps the ApplicationArray and
        # ApplicationRecordElements to Signals of.
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

    def setDataElement(self, value: RefType) -> "SenderReceiverToSignalGroupMapping":
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

    def setSignalGroup(self, value: RefType) -> "SenderReceiverToSignalGroupMapping":
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

    def setTypeMapping(self, value: "SenderRecComposite") -> "SenderReceiverToSignalGroupMapping":
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

    def with_data_element(self, value: Optional[RefType]) -> "SenderReceiverToSignalGroupMapping":
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

    def with_signal_group(self, value: Optional[RefType]) -> "SenderReceiverToSignalGroupMapping":
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

    def with_type_mapping(self, value: Optional["SenderRecComposite"]) -> "SenderReceiverToSignalGroupMapping":
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
