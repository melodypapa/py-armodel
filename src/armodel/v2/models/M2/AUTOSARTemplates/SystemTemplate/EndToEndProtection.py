"""
AUTOSAR Package - EndToEndProtection

Package: M2::AUTOSARTemplates::SystemTemplate::EndToEndProtection
"""


from __future__ import annotations

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)


class EndToEndProtectionISignalIPdu(ARObject):
    """
    It is possible to protect the inter-ECU data exchange of safety-related
    ISignalGroups at the level of COM IPdus using protection mechanisms provided
    by E2E Library. For each ISignalGroup to be protected, a separate
    EndToEndProtectionISignalIPdu element shall be created within the
    EndToEndProtectionSet. The EndToEndProtectionISignalIPdu element refers to
    the ISignalGroup that is to be protected and to the ISignalIPdu that
    transmits the protected ISignalGroup. The information how the referenced
    ISignalGroup shall be protected (through which E2E Profile and with which
    E2E settings) is defined in the EndToEnd Description element.

    Package: M2::AUTOSARTemplates::SystemTemplate::EndToEndProtection::EndToEndProtectionISignalIPdu

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 987, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 384, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the beginning offset (in bits) of the of the Signal
                # Group (including CRC, application signal group) in the IPdu.
        # This mandatory and the dataOffset shall always be.
        self._dataOffset: Optional[Integer] = None

    @property
    def data_offset(self) -> Optional[Integer]:
        """Get dataOffset (Pythonic accessor)."""
        return self._dataOffset

    @data_offset.setter
    def data_offset(self, value: Optional[Integer]) -> None:
        """
        Set dataOffset with validation.

        Args:
            value: The dataOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataOffset = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"dataOffset must be Integer or int or None, got {type(value).__name__}"
            )
        self._dataOffset = value
        self._iSignalGroup: Optional[RefType] = None

    @property
    def i_signal_group(self) -> Optional[RefType]:
        """Get iSignalGroup (Pythonic accessor)."""
        return self._iSignalGroup

    @i_signal_group.setter
    def i_signal_group(self, value: Optional[RefType]) -> None:
        """
        Set iSignalGroup with validation.

        Args:
            value: The iSignalGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalGroup = None
            return

        self._iSignalGroup = value
        self._iSignalIPdu: Optional["ISignalIPdu"] = None

    @property
    def i_signal_i_pdu(self) -> Optional["ISignalIPdu"]:
        """Get iSignalIPdu (Pythonic accessor)."""
        return self._iSignalIPdu

    @i_signal_i_pdu.setter
    def i_signal_i_pdu(self, value: Optional["ISignalIPdu"]) -> None:
        """
        Set iSignalIPdu with validation.

        Args:
            value: The iSignalIPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalIPdu = None
            return

        if not isinstance(value, ISignalIPdu):
            raise TypeError(
                f"iSignalIPdu must be ISignalIPdu or None, got {type(value).__name__}"
            )
        self._iSignalIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataOffset(self) -> Integer:
        """
        AUTOSAR-compliant getter for dataOffset.

        Returns:
            The dataOffset value

        Note:
            Delegates to data_offset property (CODING_RULE_V2_00017)
        """
        return self.data_offset  # Delegates to property

    def setDataOffset(self, value: Integer) -> EndToEndProtectionISignalIPdu:
        """
        AUTOSAR-compliant setter for dataOffset with method chaining.

        Args:
            value: The dataOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_offset property setter (gets validation automatically)
        """
        self.data_offset = value  # Delegates to property setter
        return self

    def getISignalGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for iSignalGroup.

        Returns:
            The iSignalGroup value

        Note:
            Delegates to i_signal_group property (CODING_RULE_V2_00017)
        """
        return self.i_signal_group  # Delegates to property

    def setISignalGroup(self, value: RefType) -> EndToEndProtectionISignalIPdu:
        """
        AUTOSAR-compliant setter for iSignalGroup with method chaining.

        Args:
            value: The iSignalGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal_group property setter (gets validation automatically)
        """
        self.i_signal_group = value  # Delegates to property setter
        return self

    def getISignalIPdu(self) -> "ISignalIPdu":
        """
        AUTOSAR-compliant getter for iSignalIPdu.

        Returns:
            The iSignalIPdu value

        Note:
            Delegates to i_signal_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_i_pdu  # Delegates to property

    def setISignalIPdu(self, value: "ISignalIPdu") -> EndToEndProtectionISignalIPdu:
        """
        AUTOSAR-compliant setter for iSignalIPdu with method chaining.

        Args:
            value: The iSignalIPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal_i_pdu property setter (gets validation automatically)
        """
        self.i_signal_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_offset(self, value: Optional[Integer]) -> EndToEndProtectionISignalIPdu:
        """
        Set dataOffset and return self for chaining.

        Args:
            value: The dataOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_offset("value")
        """
        self.data_offset = value  # Use property setter (gets validation)
        return self

    def with_i_signal_group(self, value: Optional[RefType]) -> EndToEndProtectionISignalIPdu:
        """
        Set iSignalGroup and return self for chaining.

        Args:
            value: The iSignalGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_group("value")
        """
        self.i_signal_group = value  # Use property setter (gets validation)
        return self

    def with_i_signal_i_pdu(self, value: Optional["ISignalIPdu"]) -> EndToEndProtectionISignalIPdu:
        """
        Set iSignalIPdu and return self for chaining.

        Args:
            value: The iSignalIPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_i_pdu("value")
        """
        self.i_signal_i_pdu = value  # Use property setter (gets validation)
        return self
