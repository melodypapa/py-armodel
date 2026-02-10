"""
AUTOSAR Package - InstanceRefs

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::InstanceRefs
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ParameterInAtomicSWCTypeInstanceRef(ARObject):
    """
    This class implements an instance reference which can be applied for
    variables as well as for parameters.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::InstanceRefs::ParameterInAtomicSWCTypeInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 319, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
        self._base: Optional["AtomicSwComponent"] = None

    @property
    def base(self) -> Optional["AtomicSwComponent"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["AtomicSwComponent"]) -> None:
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

        if not isinstance(value, AtomicSwComponent):
            raise TypeError(
                f"base must be AtomicSwComponent or None, got {type(value).__name__}"
            )
        self._base = value
        # Tags: xml.
        # sequenceOffset=40 (ordered).
        self._contextData: List["ApplicationComposite"] = []

    @property
    def context_data(self) -> List["ApplicationComposite"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # This is the port providing the variable or the entry point to structure.
        self._portPrototype: Optional["RefType"] = None

    @property
    def port_prototype(self) -> Optional["RefType"]:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: Optional["RefType"]) -> None:
        """
        Set portPrototype with validation.

        Args:
            value: The portPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portPrototype = None
            return

        self._portPrototype = value
        self._rootParameter: Optional["RefType"] = None

    @property
    def root_parameter(self) -> Optional["RefType"]:
        """Get rootParameter (Pythonic accessor)."""
        return self._rootParameter

    @root_parameter.setter
    def root_parameter(self, value: Optional["RefType"]) -> None:
        """
        Set rootParameter with validation.

        Args:
            value: The rootParameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootParameter = None
            return

        self._rootParameter = value
        # Note that this must nested in ParameterDataPrototype.
        # The target must of ParameterDataPrototype, Application.
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

    def getBase(self) -> "AtomicSwComponent":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "AtomicSwComponent") -> "ParameterInAtomicSWCTypeInstanceRef":
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

    def getPortPrototype(self) -> "RefType":
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: "RefType") -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        AUTOSAR-compliant setter for portPrototype with method chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_prototype property setter (gets validation automatically)
        """
        self.port_prototype = value  # Delegates to property setter
        return self

    def getRootParameter(self) -> "RefType":
        """
        AUTOSAR-compliant getter for rootParameter.

        Returns:
            The rootParameter value

        Note:
            Delegates to root_parameter property (CODING_RULE_V2_00017)
        """
        return self.root_parameter  # Delegates to property

    def setRootParameter(self, value: "RefType") -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        AUTOSAR-compliant setter for rootParameter with method chaining.

        Args:
            value: The rootParameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_parameter property setter (gets validation automatically)
        """
        self.root_parameter = value  # Delegates to property setter
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

    def setTargetData(self, value: "RefType") -> "ParameterInAtomicSWCTypeInstanceRef":
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

    def with_base(self, value: Optional["AtomicSwComponent"]) -> "ParameterInAtomicSWCTypeInstanceRef":
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

    def with_port_prototype(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        Set portPrototype and return self for chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_prototype("value")
        """
        self.port_prototype = value  # Use property setter (gets validation)
        return self

    def with_root_parameter(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        Set rootParameter and return self for chaining.

        Args:
            value: The rootParameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_parameter("value")
        """
        self.root_parameter = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
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



class VariableInAtomicSWCTypeInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::InstanceRefs::VariableInAtomicSWCTypeInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 953, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
        self._base: Optional["AtomicSwComponent"] = None

    @property
    def base(self) -> Optional["AtomicSwComponent"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["AtomicSwComponent"]) -> None:
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

        if not isinstance(value, AtomicSwComponent):
            raise TypeError(
                f"base must be AtomicSwComponent or None, got {type(value).__name__}"
            )
        self._base = value
        # Tags: xml.
        # sequenceOffset=40 (ordered).
        self._contextData: List["ApplicationComposite"] = []

    @property
    def context_data(self) -> List["ApplicationComposite"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # This is the port providing the parameter or the entry point parameter
        # structure.
        self._portPrototype: Optional["RefType"] = None

    @property
    def port_prototype(self) -> Optional["RefType"]:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: Optional["RefType"]) -> None:
        """
        Set portPrototype with validation.

        Args:
            value: The portPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portPrototype = None
            return

        self._portPrototype = value
        # sequenceOffset=30 1228 Document ID 62:
                # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._rootVariableDataPrototype: Optional["RefType"] = None

    @property
    def root_variable_data_prototype(self) -> Optional["RefType"]:
        """Get rootVariableDataPrototype (Pythonic accessor)."""
        return self._rootVariableDataPrototype

    @root_variable_data_prototype.setter
    def root_variable_data_prototype(self, value: Optional["RefType"]) -> None:
        """
        Set rootVariableDataPrototype with validation.

        Args:
            value: The rootVariableDataPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootVariableDataPrototype = None
            return

        self._rootVariableDataPrototype = value
        # Note that it shall be of ApplicationCompositeElementDataPrototype of.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "AtomicSwComponent":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "AtomicSwComponent") -> "VariableInAtomicSWCTypeInstanceRef":
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

    def getPortPrototype(self) -> "RefType":
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: "RefType") -> "VariableInAtomicSWCTypeInstanceRef":
        """
        AUTOSAR-compliant setter for portPrototype with method chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_prototype property setter (gets validation automatically)
        """
        self.port_prototype = value  # Delegates to property setter
        return self

    def getRootVariableDataPrototype(self) -> "RefType":
        """
        AUTOSAR-compliant getter for rootVariableDataPrototype.

        Returns:
            The rootVariableDataPrototype value

        Note:
            Delegates to root_variable_data_prototype property (CODING_RULE_V2_00017)
        """
        return self.root_variable_data_prototype  # Delegates to property

    def setRootVariableDataPrototype(self, value: "RefType") -> "VariableInAtomicSWCTypeInstanceRef":
        """
        AUTOSAR-compliant setter for rootVariableDataPrototype with method chaining.

        Args:
            value: The rootVariableDataPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_variable_data_prototype property setter (gets validation automatically)
        """
        self.root_variable_data_prototype = value  # Delegates to property setter
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

    def setTargetData(self, value: "RefType") -> "VariableInAtomicSWCTypeInstanceRef":
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

    def with_base(self, value: Optional["AtomicSwComponent"]) -> "VariableInAtomicSWCTypeInstanceRef":
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

    def with_port_prototype(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
        """
        Set portPrototype and return self for chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_prototype("value")
        """
        self.port_prototype = value  # Use property setter (gets validation)
        return self

    def with_root_variable_data_prototype(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
        """
        Set rootVariableDataPrototype and return self for chaining.

        Args:
            value: The rootVariableDataPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_variable_data_prototype("value")
        """
        self.root_variable_data_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
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
