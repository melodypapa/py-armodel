from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """
    This class represents a RootDataPrototype that is typed by an
    ApplicationDataType or Implementation DataType or a DataTypeElement that is
    aggregated within a composite application data type (record or array).

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataPrototypeInPortInterfaceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 787, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # context of a SenderReceiverInterface.
        # implemented by: DataPrototypeInSender.
        self._dataPrototypeIn: RefType = None

    @property
    def data_prototype_in(self) -> RefType:
        """Get dataPrototypeIn (Pythonic accessor)."""
        return self._dataPrototypeIn

    @data_prototype_in.setter
    def data_prototype_in(self, value: RefType) -> None:
        """
        Set dataPrototypeIn with validation.

        Args:
            value: The dataPrototypeIn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPrototypeIn = None
            return

        self._dataPrototypeIn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataPrototypeIn(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataPrototypeIn.

        Returns:
            The dataPrototypeIn value

        Note:
            Delegates to data_prototype_in property (CODING_RULE_V2_00017)
        """
        return self.data_prototype_in  # Delegates to property

    def setDataPrototypeIn(self, value: RefType) -> "DataPrototypeInPortInterfaceRef":
        """
        AUTOSAR-compliant setter for dataPrototypeIn with method chaining.

        Args:
            value: The dataPrototypeIn to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_prototype_in property setter (gets validation automatically)
        """
        self.data_prototype_in = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_prototype_in(self, value: Optional[RefType]) -> "DataPrototypeInPortInterfaceRef":
        """
        Set dataPrototypeIn and return self for chaining.

        Args:
            value: The dataPrototypeIn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_prototype_in("value")
        """
        self.data_prototype_in = value  # Use property setter (gets validation)
        return self
