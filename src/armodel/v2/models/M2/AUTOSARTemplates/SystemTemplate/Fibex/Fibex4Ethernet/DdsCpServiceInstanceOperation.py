from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DdsCpServiceInstanceOperation(ARObject):
    """
    This element represents an operation as part of the Provided Service
    Instance.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpServiceInstanceOperation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 475, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the PduTriggering used for the upper layer of this DdsOperation
                # response message.
        # atp.
        # Status=candidate.
        self._ddsOperation: RefType = None

    @property
    def dds_operation(self) -> RefType:
        """Get ddsOperation (Pythonic accessor)."""
        return self._ddsOperation

    @dds_operation.setter
    def dds_operation(self, value: RefType) -> None:
        """
        Set ddsOperation with validation.

        Args:
            value: The ddsOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsOperation = None
            return

        self._ddsOperation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsOperation(self) -> RefType:
        """
        AUTOSAR-compliant getter for ddsOperation.

        Returns:
            The ddsOperation value

        Note:
            Delegates to dds_operation property (CODING_RULE_V2_00017)
        """
        return self.dds_operation  # Delegates to property

    def setDdsOperation(self, value: RefType) -> "DdsCpServiceInstanceOperation":
        """
        AUTOSAR-compliant setter for ddsOperation with method chaining.

        Args:
            value: The ddsOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_operation property setter (gets validation automatically)
        """
        self.dds_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_operation(self, value: Optional[RefType]) -> "DdsCpServiceInstanceOperation":
        """
        Set ddsOperation and return self for chaining.

        Args:
            value: The ddsOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_operation("value")
        """
        self.dds_operation = value  # Use property setter (gets validation)
        return self
