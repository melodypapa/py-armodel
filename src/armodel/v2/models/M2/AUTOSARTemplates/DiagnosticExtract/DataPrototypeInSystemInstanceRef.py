from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DataPrototypeInSystemInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs::DataPrototypeInSystemInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 368, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the base of the InstanceRef.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
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

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value
        # Tags: xml.
        # sequenceOffset=30.
        self._context: List["SwComponent"] = []

    @property
    def context(self) -> List["SwComponent"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # Tags: xml.
        # sequenceOffset=50.
        self._contextData: List["ApplicationComposite"] = []

    @property
    def context_data(self) -> List["ApplicationComposite"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # This represents the PortPrototype that is contained in the.
        self._contextPort: RefType = None

    @property
    def context_port(self) -> RefType:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: RefType) -> None:
        """
        Set contextPort with validation.

        Args:
            value: The contextPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPort = None
            return

        self._contextPort = value
        # Tags: xml.
        # sequenceOffset=20.
        self._contextRoot: Optional["RootSwComposition"] = None

    @property
    def context_root(self) -> Optional["RootSwComposition"]:
        """Get contextRoot (Pythonic accessor)."""
        return self._contextRoot

    @context_root.setter
    def context_root(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set contextRoot with validation.

        Args:
            value: The contextRoot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRoot = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"contextRoot must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._contextRoot = value
        # Tags: xml.
        # sequenceOffset=45.
        self._rootDataPrototype: RefType = None

    @property
    def root_data_prototype(self) -> RefType:
        """Get rootDataPrototype (Pythonic accessor)."""
        return self._rootDataPrototype

    @root_data_prototype.setter
    def root_data_prototype(self, value: RefType) -> None:
        """
        Set rootDataPrototype with validation.

        Args:
            value: The rootDataPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootDataPrototype = None
            return

        self._rootDataPrototype = value
        # This represents the target of the InstanceRef xml.
        # sequenceOffset=60.
        self._targetData: RefType = None

    @property
    def target_data(self) -> RefType:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: RefType) -> None:
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

        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "DataPrototypeInSystemInstanceRef":
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

    def getContext(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getContextData(self) -> List["ApplicationComposite"]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getContextPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextPort.

        Returns:
            The contextPort value

        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: RefType) -> "DataPrototypeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextPort with method chaining.

        Args:
            value: The contextPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_port property setter (gets validation automatically)
        """
        self.context_port = value  # Delegates to property setter
        return self

    def getContextRoot(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for contextRoot.

        Returns:
            The contextRoot value

        Note:
            Delegates to context_root property (CODING_RULE_V2_00017)
        """
        return self.context_root  # Delegates to property

    def setContextRoot(self, value: "RootSwComposition") -> "DataPrototypeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextRoot with method chaining.

        Args:
            value: The contextRoot to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_root property setter (gets validation automatically)
        """
        self.context_root = value  # Delegates to property setter
        return self

    def getRootDataPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootDataPrototype.

        Returns:
            The rootDataPrototype value

        Note:
            Delegates to root_data_prototype property (CODING_RULE_V2_00017)
        """
        return self.root_data_prototype  # Delegates to property

    def setRootDataPrototype(self, value: RefType) -> "DataPrototypeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for rootDataPrototype with method chaining.

        Args:
            value: The rootDataPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_data_prototype property setter (gets validation automatically)
        """
        self.root_data_prototype = value  # Delegates to property setter
        return self

    def getTargetData(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetData.

        Returns:
            The targetData value

        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: RefType) -> "DataPrototypeInSystemInstanceRef":
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

    def with_base(self, value: Optional["System"]) -> "DataPrototypeInSystemInstanceRef":
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

    def with_context_port(self, value: Optional[RefType]) -> "DataPrototypeInSystemInstanceRef":
        """
        Set contextPort and return self for chaining.

        Args:
            value: The contextPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_port("value")
        """
        self.context_port = value  # Use property setter (gets validation)
        return self

    def with_context_root(self, value: Optional["RootSwComposition"]) -> "DataPrototypeInSystemInstanceRef":
        """
        Set contextRoot and return self for chaining.

        Args:
            value: The contextRoot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_root("value")
        """
        self.context_root = value  # Use property setter (gets validation)
        return self

    def with_root_data_prototype(self, value: Optional[RefType]) -> "DataPrototypeInSystemInstanceRef":
        """
        Set rootDataPrototype and return self for chaining.

        Args:
            value: The rootDataPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_data_prototype("value")
        """
        self.root_data_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional[RefType]) -> "DataPrototypeInSystemInstanceRef":
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
