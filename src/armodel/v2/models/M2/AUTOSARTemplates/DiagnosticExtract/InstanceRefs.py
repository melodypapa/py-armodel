"""
AUTOSAR Package - InstanceRefs

Package: M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
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
        self._contextPort: Optional["RefType"] = None

    @property
    def context_port(self) -> Optional["RefType"]:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: Optional["RefType"]) -> None:
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
        # sequenceOffset=45.
        self._rootDataPrototype: Optional["RefType"] = None

    @property
    def root_data_prototype(self) -> Optional["RefType"]:
        """Get rootDataPrototype (Pythonic accessor)."""
        return self._rootDataPrototype

    @root_data_prototype.setter
    def root_data_prototype(self, value: Optional["RefType"]) -> None:
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
        # sequenceOffset=60.
        self._targetData: Optional["RefType"] = None

    @property
    def target_data(self) -> Optional["RefType"]:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: Optional["RefType"]) -> None:
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

    def with_context_sw(self, value):
        """
        Set context_sw and return self for chaining.

        Args:
            value: The context_sw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_sw("value")
        """
        self.context_sw = value  # Use property setter (gets validation)
        return self

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

    def getContextPort(self) -> "RefType":
        """
        AUTOSAR-compliant getter for contextPort.

        Returns:
            The contextPort value

        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: "RefType") -> "DataPrototypeInSystemInstanceRef":
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

    def getRootDataPrototype(self) -> "RefType":
        """
        AUTOSAR-compliant getter for rootDataPrototype.

        Returns:
            The rootDataPrototype value

        Note:
            Delegates to root_data_prototype property (CODING_RULE_V2_00017)
        """
        return self.root_data_prototype  # Delegates to property

    def setRootDataPrototype(self, value: "RefType") -> "DataPrototypeInSystemInstanceRef":
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

    def getTargetData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetData.

        Returns:
            The targetData value

        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: "RefType") -> "DataPrototypeInSystemInstanceRef":
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



class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs::SwcServiceDependencyInSystemInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 369, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._contextRootSw: Optional["RootSwComposition"] = None

    @property
    def context_root_sw(self) -> Optional["RootSwComposition"]:
        """Get contextRootSw (Pythonic accessor)."""
        return self._contextRootSw

    @context_root_sw.setter
    def context_root_sw(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set contextRootSw with validation.

        Args:
            value: The contextRootSw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRootSw = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"contextRootSw must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._contextRootSw = value
        # R23-11.
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        self._targetSwc: Optional["SwcService"] = None

    @property
    def target_swc(self) -> Optional["SwcService"]:
        """Get targetSwc (Pythonic accessor)."""
        return self._targetSwc

    @target_swc.setter
    def target_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set targetSwc with validation.

        Args:
            value: The targetSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"targetSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._targetSwc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextRootSw(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for contextRootSw.

        Returns:
            The contextRootSw value

        Note:
            Delegates to context_root_sw property (CODING_RULE_V2_00017)
        """
        return self.context_root_sw  # Delegates to property

    def setContextRootSw(self, value: "RootSwComposition") -> "SwcServiceDependencyInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextRootSw with method chaining.

        Args:
            value: The contextRootSw to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_root_sw property setter (gets validation automatically)
        """
        self.context_root_sw = value  # Delegates to property setter
        return self

    def getContextSw(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextSw.

        Returns:
            The contextSw value

        Note:
            Delegates to context_sw property (CODING_RULE_V2_00017)
        """
        return self.context_sw  # Delegates to property

    def getTargetSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for targetSwc.

        Returns:
            The targetSwc value

        Note:
            Delegates to target_swc property (CODING_RULE_V2_00017)
        """
        return self.target_swc  # Delegates to property

    def setTargetSwc(self, value: "SwcService") -> "SwcServiceDependencyInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for targetSwc with method chaining.

        Args:
            value: The targetSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_swc property setter (gets validation automatically)
        """
        self.target_swc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_root_sw(self, value: Optional["RootSwComposition"]) -> "SwcServiceDependencyInSystemInstanceRef":
        """
        Set contextRootSw and return self for chaining.

        Args:
            value: The contextRootSw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_root_sw("value")
        """
        self.context_root_sw = value  # Use property setter (gets validation)
        return self

    def with_target_swc(self, value: Optional["SwcService"]) -> "SwcServiceDependencyInSystemInstanceRef":
        """
        Set targetSwc and return self for chaining.

        Args:
            value: The targetSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_swc("value")
        """
        self.target_swc = value  # Use property setter (gets validation)
        return self



class PModeInSystemInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs::PModeInSystemInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 370, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
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
        # sequenceOffset=20.
        self._context: Optional["RootSwComposition"] = None

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set context with validation.

        Args:
            value: The context to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value
        # sequenceOffset=50.
        self._contextModeGroup: Optional["RefType"] = None

    @property
    def context_mode_group(self) -> Optional["RefType"]:
        """Get contextModeGroup (Pythonic accessor)."""
        return self._contextModeGroup

    @context_mode_group.setter
    def context_mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set contextModeGroup with validation.

        Args:
            value: The contextModeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextModeGroup = None
            return

        self._contextModeGroup = value
        # sequenceOffset=40.
        self._contextPPortPrototype: Optional["AbstractProvidedPort"] = None

    @property
    def context_p_port_prototype(self) -> Optional["AbstractProvidedPort"]:
        """Get contextPPortPrototype (Pythonic accessor)."""
        return self._contextPPortPrototype

    @context_p_port_prototype.setter
    def context_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> None:
        """
        Set contextPPortPrototype with validation.

        Args:
            value: The contextPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"contextPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._contextPPortPrototype = value
        # sequenceOffset=60.
        self._targetMode: Optional["ModeDeclaration"] = None

    @property
    def target_mode(self) -> Optional["ModeDeclaration"]:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set targetMode with validation.

        Args:
            value: The targetMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"targetMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._targetMode = value

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

    def setBase(self, value: "System") -> "PModeInSystemInstanceRef":
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

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "PModeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getContextModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for contextModeGroup.

        Returns:
            The contextModeGroup value

        Note:
            Delegates to context_mode_group property (CODING_RULE_V2_00017)
        """
        return self.context_mode_group  # Delegates to property

    def setContextModeGroup(self, value: "RefType") -> "PModeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextModeGroup with method chaining.

        Args:
            value: The contextModeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_mode_group property setter (gets validation automatically)
        """
        self.context_mode_group = value  # Delegates to property setter
        return self

    def getContextPPortPrototype(self) -> "AbstractProvidedPort":
        """
        AUTOSAR-compliant getter for contextPPortPrototype.

        Returns:
            The contextPPortPrototype value

        Note:
            Delegates to context_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_p_port_prototype  # Delegates to property

    def setContextPPortPrototype(self, value: "AbstractProvidedPort") -> "PModeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextPPortPrototype with method chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_p_port_prototype property setter (gets validation automatically)
        """
        self.context_p_port_prototype = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for targetMode.

        Returns:
            The targetMode value

        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: "ModeDeclaration") -> "PModeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for targetMode with method chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["System"]) -> "PModeInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "PModeInSystemInstanceRef":
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context_mode_group(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        """
        Set contextModeGroup and return self for chaining.

        Args:
            value: The contextModeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_mode_group("value")
        """
        self.context_mode_group = value  # Use property setter (gets validation)
        return self

    def with_context_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> "PModeInSystemInstanceRef":
        """
        Set contextPPortPrototype and return self for chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_p_port_prototype("value")
        """
        self.context_p_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional["ModeDeclaration"]) -> "PModeInSystemInstanceRef":
        """
        Set targetMode and return self for chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self
