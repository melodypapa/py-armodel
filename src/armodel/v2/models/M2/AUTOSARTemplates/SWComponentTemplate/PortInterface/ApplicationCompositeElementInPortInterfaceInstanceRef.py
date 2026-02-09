from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ApplicationCompositeElementInPortInterfaceInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::InstanceRefs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 952, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the SenderReceiverInterface that acts as in this InstanceRef
        # definition.
        self._base: Optional["DataInterface"] = None

    @property
    def base(self) -> Optional["DataInterface"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["DataInterface"]) -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, DataInterface):
            raise TypeError(
                f"base must be DataInterface or None, got {type(value).__name__}"
            )
        self._base = value
        # sequenceOffset=20 1228 Document ID 62:
                # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._contextData: List["ApplicationComposite"] = []

    @property
    def context_data(self) -> List["ApplicationComposite"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # This refers to the dataPrototype which is typed by the in which which the
        # target can be.
        self._rootData: RefType = None

    @property
    def root_data(self) -> RefType:
        """Get rootData (Pythonic accessor)."""
        return self._rootData

    @root_data.setter
    def root_data(self, value: RefType) -> None:
        """
        Set rootData with validation.

        Args:
            value: The rootData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootData = None
            return

        self._rootData = value
        self._targetData: Optional["ApplicationComposite"] = None

    @property
    def target_data(self) -> Optional["ApplicationComposite"]:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: Optional["ApplicationComposite"]) -> None:
        """
        Set targetData with validation.

        Args:
            value: The targetData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetData = None
            return

        if not isinstance(value, ApplicationComposite):
            raise TypeError(
                f"targetData must be ApplicationComposite or None, got {type(value).__name__}"
            )
        self._targetData = value

    def with_context_data(self, value):
        """
        Set context_data and return self for chaining.

        Args:
            value: The context_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "DataInterface":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "DataInterface") -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
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

    def getRootData(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootData.

        Returns:
            The rootData value

        Note:
            Delegates to root_data property (CODING_RULE_V2_00017)
        """
        return self.root_data  # Delegates to property

    def setRootData(self, value: RefType) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for rootData with method chaining.

        Args:
            value: The rootData to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_data property setter (gets validation automatically)
        """
        self.root_data = value  # Delegates to property setter
        return self

    def getTargetData(self) -> "ApplicationComposite":
        """
        AUTOSAR-compliant getter for targetData.

        Returns:
            The targetData value

        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: "ApplicationComposite") -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for targetData with method chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data property setter (gets validation automatically)
        """
        self.target_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["DataInterface"]) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_root_data(self, value: Optional[RefType]) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        Set rootData and return self for chaining.

        Args:
            value: The rootData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_data("value")
        """
        self.root_data = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional["ApplicationComposite"]) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        Set targetData and return self for chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data("value")
        """
        self.target_data = value  # Use property setter (gets validation)
        return self
