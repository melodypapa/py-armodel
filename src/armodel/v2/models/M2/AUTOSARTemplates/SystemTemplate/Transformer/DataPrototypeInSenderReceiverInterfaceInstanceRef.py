from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ApplicationComposite,
    DataPrototypeInPortInterfaceInstanceRef,
    SenderReceiver,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DataPrototypeInSenderReceiverInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::DataPrototypeInSenderReceiverInterfaceInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 788, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._baseInterface: Optional["SenderReceiver"] = None

    @property
    def base_interface(self) -> Optional["SenderReceiver"]:
        """Get baseInterface (Pythonic accessor)."""
        return self._baseInterface

    @base_interface.setter
    def base_interface(self, value: Optional["SenderReceiver"]) -> None:
        """
        Set baseInterface with validation.

        Args:
            value: The baseInterface to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseInterface = None
            return

        if not isinstance(value, SenderReceiver):
            raise TypeError(
                f"baseInterface must be SenderReceiver or None, got {type(value).__name__}"
            )
        self._baseInterface = value
        # Tags: xml.
        # sequenceOffset=20.
        self._contextData: List["ApplicationComposite"] = []

    @property
    def context_data(self) -> List["ApplicationComposite"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # Tags: xml.
        # sequenceOffset=10.
        self._rootDataPrototypeInSr: RefType = None

    @property
    def root_data_prototype_in_sr(self) -> RefType:
        """Get rootDataPrototypeInSr (Pythonic accessor)."""
        return self._rootDataPrototypeInSr

    @root_data_prototype_in_sr.setter
    def root_data_prototype_in_sr(self, value: RefType) -> None:
        """
        Set rootDataPrototypeInSr with validation.

        Args:
            value: The rootDataPrototypeInSr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootDataPrototypeInSr = None
            return

        self._rootDataPrototypeInSr = value
        # Tags: xml.
        # sequenceOffset=30.
        self._targetDataPrototypeInSr: RefType = None

    @property
    def target_data_prototype_in_sr(self) -> RefType:
        """Get targetDataPrototypeInSr (Pythonic accessor)."""
        return self._targetDataPrototypeInSr

    @target_data_prototype_in_sr.setter
    def target_data_prototype_in_sr(self, value: RefType) -> None:
        """
        Set targetDataPrototypeInSr with validation.

        Args:
            value: The targetDataPrototypeInSr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetDataPrototypeInSr = None
            return

        self._targetDataPrototypeInSr = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseInterface(self) -> "SenderReceiver":
        """
        AUTOSAR-compliant getter for baseInterface.

        Returns:
            The baseInterface value

        Note:
            Delegates to base_interface property (CODING_RULE_V2_00017)
        """
        return self.base_interface  # Delegates to property

    def setBaseInterface(self, value: "SenderReceiver") -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for baseInterface with method chaining.

        Args:
            value: The baseInterface to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_interface property setter (gets validation automatically)
        """
        self.base_interface = value  # Delegates to property setter
        return self

    def getContextData(self) -> List["ApplicationComposite"]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getRootDataPrototypeInSr(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootDataPrototypeInSr.

        Returns:
            The rootDataPrototypeInSr value

        Note:
            Delegates to root_data_prototype_in_sr property (CODING_RULE_V2_00017)
        """
        return self.root_data_prototype_in_sr  # Delegates to property

    def setRootDataPrototypeInSr(self, value: RefType) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for rootDataPrototypeInSr with method chaining.

        Args:
            value: The rootDataPrototypeInSr to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_data_prototype_in_sr property setter (gets validation automatically)
        """
        self.root_data_prototype_in_sr = value  # Delegates to property setter
        return self

    def getTargetDataPrototypeInSr(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetDataPrototypeInSr.

        Returns:
            The targetDataPrototypeInSr value

        Note:
            Delegates to target_data_prototype_in_sr property (CODING_RULE_V2_00017)
        """
        return self.target_data_prototype_in_sr  # Delegates to property

    def setTargetDataPrototypeInSr(self, value: RefType) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for targetDataPrototypeInSr with method chaining.

        Args:
            value: The targetDataPrototypeInSr to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data_prototype_in_sr property setter (gets validation automatically)
        """
        self.target_data_prototype_in_sr = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_interface(self, value: Optional["SenderReceiver"]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Set baseInterface and return self for chaining.

        Args:
            value: The baseInterface to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_interface("value")
        """
        self.base_interface = value  # Use property setter (gets validation)
        return self

    def with_root_data_prototype_in_sr(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Set rootDataPrototypeInSr and return self for chaining.

        Args:
            value: The rootDataPrototypeInSr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_data_prototype_in_sr("value")
        """
        self.root_data_prototype_in_sr = value  # Use property setter (gets validation)
        return self

    def with_target_data_prototype_in_sr(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Set targetDataPrototypeInSr and return self for chaining.

        Args:
            value: The targetDataPrototypeInSr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data_prototype_in_sr("value")
        """
        self.target_data_prototype_in_sr = value  # Use property setter (gets validation)
        return self
