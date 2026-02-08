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


class ArVariableInImplementationDataInstanceRef(ARObject):
    """
    that this class follows the pattern of an InstanceRef but is not implemented
    based on the abstract classes because the ImplementationDataType isn’t
    either, especially because ImplementationDataType Element isn’t derived from
    AtpPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 322, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a context in case there are subelements with explicit types.
        # The reference has to be ordered to reflect the nested structure.
        self._contextData: List["AbstractImplementation"] = []

    @property
    def context_data(self) -> List["AbstractImplementation"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # This is the port providing/receiving the root of the variable.
        self._portPrototype: RefType = None

    @property
    def port_prototype(self) -> RefType:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: RefType) -> None:
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
        # This refers to the VariableDataPrototype typed by the in which the target can
        # be found.
        self._rootVariable: RefType = None

    @property
    def root_variable(self) -> RefType:
        """Get rootVariable (Pythonic accessor)."""
        return self._rootVariable

    @root_variable.setter
    def root_variable(self, value: RefType) -> None:
        """
        Set rootVariable with validation.

        Args:
            value: The rootVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootVariable = None
            return

        self._rootVariable = value
        # This reference points to the target ImplementationData TypeElement.
        self._targetData: Optional["AbstractImplementation"] = None

    @property
    def target_data(self) -> Optional["AbstractImplementation"]:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: Optional["AbstractImplementation"]) -> None:
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

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"targetData must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextData(self) -> List["AbstractImplementation"]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getPortPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: RefType) -> "ArVariableInImplementationDataInstanceRef":
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

    def getRootVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootVariable.

        Returns:
            The rootVariable value

        Note:
            Delegates to root_variable property (CODING_RULE_V2_00017)
        """
        return self.root_variable  # Delegates to property

    def setRootVariable(self, value: RefType) -> "ArVariableInImplementationDataInstanceRef":
        """
        AUTOSAR-compliant setter for rootVariable with method chaining.

        Args:
            value: The rootVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_variable property setter (gets validation automatically)
        """
        self.root_variable = value  # Delegates to property setter
        return self

    def getTargetData(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for targetData.

        Returns:
            The targetData value

        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: "AbstractImplementation") -> "ArVariableInImplementationDataInstanceRef":
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

    def with_port_prototype(self, value: Optional[RefType]) -> "ArVariableInImplementationDataInstanceRef":
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

    def with_root_variable(self, value: Optional[RefType]) -> "ArVariableInImplementationDataInstanceRef":
        """
        Set rootVariable and return self for chaining.

        Args:
            value: The rootVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_variable("value")
        """
        self.root_variable = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional["AbstractImplementation"]) -> "ArVariableInImplementationDataInstanceRef":
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
