from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SenderReceiverAnnotation(GeneralAnnotation, ABC):
    """
    Annotation of the data elements in a port that realizes a sender/receiver
    interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::SenderReceiverAnnotation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 152, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is SenderReceiverAnnotation:
            raise TypeError("SenderReceiverAnnotation is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Flag whether this data element was not measured directly was calculated from
        # possibly several other calculated values.
        self._computed: Optional["Boolean"] = None

    @property
    def computed(self) -> Optional["Boolean"]:
        """Get computed (Pythonic accessor)."""
        return self._computed

    @computed.setter
    def computed(self, value: Optional["Boolean"]) -> None:
        """
        Set computed with validation.

        Args:
            value: The computed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._computed = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"computed must be Boolean or None, got {type(value).__name__}"
            )
        self._computed = value
        # The instance of VariableDataPrototype annotated.
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
        # This min or max has not to be mismatched with the min- for data-value in a
                # compu-method.
        # For example, shows when the result of the calculation a RunnableEntity owned
                # by one AtomicSw transmitted to another AtomicSw RunnableEntity will use this
                # value limit, e.
        # g.
        # the max.
        # power which can be used by that the current min.
        # slip.
        self._limitKind: Optional["DataLimitKindEnum"] = None

    @property
    def limit_kind(self) -> Optional["DataLimitKindEnum"]:
        """Get limitKind (Pythonic accessor)."""
        return self._limitKind

    @limit_kind.setter
    def limit_kind(self, value: Optional["DataLimitKindEnum"]) -> None:
        """
        Set limitKind with validation.

        Args:
            value: The limitKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._limitKind = None
            return

        if not isinstance(value, DataLimitKindEnum):
            raise TypeError(
                f"limitKind must be DataLimitKindEnum or None, got {type(value).__name__}"
            )
        self._limitKind = value
        # This attribute controls how data is processed according to values of
        # ProcessingKindEnum.
        self._processingKind: Optional["ProcessingKindEnum"] = None

    @property
    def processing_kind(self) -> Optional["ProcessingKindEnum"]:
        """Get processingKind (Pythonic accessor)."""
        return self._processingKind

    @processing_kind.setter
    def processing_kind(self, value: Optional["ProcessingKindEnum"]) -> None:
        """
        Set processingKind with validation.

        Args:
            value: The processingKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processingKind = None
            return

        if not isinstance(value, ProcessingKindEnum):
            raise TypeError(
                f"processingKind must be ProcessingKindEnum or None, got {type(value).__name__}"
            )
        self._processingKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComputed(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for computed.

        Returns:
            The computed value

        Note:
            Delegates to computed property (CODING_RULE_V2_00017)
        """
        return self.computed  # Delegates to property

    def setComputed(self, value: "Boolean") -> "SenderReceiverAnnotation":
        """
        AUTOSAR-compliant setter for computed with method chaining.

        Args:
            value: The computed to set

        Returns:
            self for method chaining

        Note:
            Delegates to computed property setter (gets validation automatically)
        """
        self.computed = value  # Delegates to property setter
        return self

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> "SenderReceiverAnnotation":
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

    def getLimitKind(self) -> "DataLimitKindEnum":
        """
        AUTOSAR-compliant getter for limitKind.

        Returns:
            The limitKind value

        Note:
            Delegates to limit_kind property (CODING_RULE_V2_00017)
        """
        return self.limit_kind  # Delegates to property

    def setLimitKind(self, value: "DataLimitKindEnum") -> "SenderReceiverAnnotation":
        """
        AUTOSAR-compliant setter for limitKind with method chaining.

        Args:
            value: The limitKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to limit_kind property setter (gets validation automatically)
        """
        self.limit_kind = value  # Delegates to property setter
        return self

    def getProcessingKind(self) -> "ProcessingKindEnum":
        """
        AUTOSAR-compliant getter for processingKind.

        Returns:
            The processingKind value

        Note:
            Delegates to processing_kind property (CODING_RULE_V2_00017)
        """
        return self.processing_kind  # Delegates to property

    def setProcessingKind(self, value: "ProcessingKindEnum") -> "SenderReceiverAnnotation":
        """
        AUTOSAR-compliant setter for processingKind with method chaining.

        Args:
            value: The processingKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to processing_kind property setter (gets validation automatically)
        """
        self.processing_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_computed(self, value: Optional["Boolean"]) -> "SenderReceiverAnnotation":
        """
        Set computed and return self for chaining.

        Args:
            value: The computed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_computed("value")
        """
        self.computed = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional[RefType]) -> "SenderReceiverAnnotation":
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

    def with_limit_kind(self, value: Optional["DataLimitKindEnum"]) -> "SenderReceiverAnnotation":
        """
        Set limitKind and return self for chaining.

        Args:
            value: The limitKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_limit_kind("value")
        """
        self.limit_kind = value  # Use property setter (gets validation)
        return self

    def with_processing_kind(self, value: Optional["ProcessingKindEnum"]) -> "SenderReceiverAnnotation":
        """
        Set processingKind and return self for chaining.

        Args:
            value: The processingKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_processing_kind("value")
        """
        self.processing_kind = value  # Use property setter (gets validation)
        return self
