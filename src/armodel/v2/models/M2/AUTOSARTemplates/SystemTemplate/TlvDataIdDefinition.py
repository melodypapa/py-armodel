from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TlvDataIdDefinition(ARObject):
    """
    This meta-class represents the ability to define the tlvDataId.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 830, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the definition of the value of the.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # This reference assigns a tlvDataId to a given argument of.
        self._tlvArgument: RefType = None

    @property
    def tlv_argument(self) -> RefType:
        """Get tlvArgument (Pythonic accessor)."""
        return self._tlvArgument

    @tlv_argument.setter
    def tlv_argument(self, value: RefType) -> None:
        """
        Set tlvArgument with validation.

        Args:
            value: The tlvArgument to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlvArgument = None
            return

        self._tlvArgument = value
        # This reference associates the definition of a TLV data id with a given
        # AbstractImplementationDataTypeElement.
        self._tlv: Optional["AbstractImplementation"] = None

    @property
    def tlv(self) -> Optional["AbstractImplementation"]:
        """Get tlv (Pythonic accessor)."""
        return self._tlv

    @tlv.setter
    def tlv(self, value: Optional["AbstractImplementation"]) -> None:
        """
        Set tlv with validation.

        Args:
            value: The tlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlv = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"tlv must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._tlv = value
        # This reference associates the definition of a TLV data id with a given
        # ApplicationRecordElement.
        self._tlvRecord: Optional["ApplicationRecord"] = None

    @property
    def tlv_record(self) -> Optional["ApplicationRecord"]:
        """Get tlvRecord (Pythonic accessor)."""
        return self._tlvRecord

    @tlv_record.setter
    def tlv_record(self, value: Optional["ApplicationRecord"]) -> None:
        """
        Set tlvRecord with validation.

        Args:
            value: The tlvRecord to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlvRecord = None
            return

        if not isinstance(value, ApplicationRecord):
            raise TypeError(
                f"tlvRecord must be ApplicationRecord or None, got {type(value).__name__}"
            )
        self._tlvRecord = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "TlvDataIdDefinition":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getTlvArgument(self) -> RefType:
        """
        AUTOSAR-compliant getter for tlvArgument.

        Returns:
            The tlvArgument value

        Note:
            Delegates to tlv_argument property (CODING_RULE_V2_00017)
        """
        return self.tlv_argument  # Delegates to property

    def setTlvArgument(self, value: RefType) -> "TlvDataIdDefinition":
        """
        AUTOSAR-compliant setter for tlvArgument with method chaining.

        Args:
            value: The tlvArgument to set

        Returns:
            self for method chaining

        Note:
            Delegates to tlv_argument property setter (gets validation automatically)
        """
        self.tlv_argument = value  # Delegates to property setter
        return self

    def getTlv(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for tlv.

        Returns:
            The tlv value

        Note:
            Delegates to tlv property (CODING_RULE_V2_00017)
        """
        return self.tlv  # Delegates to property

    def setTlv(self, value: "AbstractImplementation") -> "TlvDataIdDefinition":
        """
        AUTOSAR-compliant setter for tlv with method chaining.

        Args:
            value: The tlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to tlv property setter (gets validation automatically)
        """
        self.tlv = value  # Delegates to property setter
        return self

    def getTlvRecord(self) -> "ApplicationRecord":
        """
        AUTOSAR-compliant getter for tlvRecord.

        Returns:
            The tlvRecord value

        Note:
            Delegates to tlv_record property (CODING_RULE_V2_00017)
        """
        return self.tlv_record  # Delegates to property

    def setTlvRecord(self, value: "ApplicationRecord") -> "TlvDataIdDefinition":
        """
        AUTOSAR-compliant setter for tlvRecord with method chaining.

        Args:
            value: The tlvRecord to set

        Returns:
            self for method chaining

        Note:
            Delegates to tlv_record property setter (gets validation automatically)
        """
        self.tlv_record = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "TlvDataIdDefinition":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_tlv_argument(self, value: Optional[RefType]) -> "TlvDataIdDefinition":
        """
        Set tlvArgument and return self for chaining.

        Args:
            value: The tlvArgument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tlv_argument("value")
        """
        self.tlv_argument = value  # Use property setter (gets validation)
        return self

    def with_tlv(self, value: Optional["AbstractImplementation"]) -> "TlvDataIdDefinition":
        """
        Set tlv and return self for chaining.

        Args:
            value: The tlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tlv("value")
        """
        self.tlv = value  # Use property setter (gets validation)
        return self

    def with_tlv_record(self, value: Optional["ApplicationRecord"]) -> "TlvDataIdDefinition":
        """
        Set tlvRecord and return self for chaining.

        Args:
            value: The tlvRecord to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tlv_record("value")
        """
        self.tlv_record = value  # Use property setter (gets validation)
        return self
