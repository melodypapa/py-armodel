from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    VariableInAtomicSwcInstanceRef,
)

    RefType,
)


class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 943, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextRPortPrototype: Optional["AbstractRequiredPort"] = None

    @property
    def context_r_port_prototype(self) -> Optional["AbstractRequiredPort"]:
        """Get contextRPortPrototype (Pythonic accessor)."""
        return self._contextRPortPrototype

    @context_r_port_prototype.setter
    def context_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> None:
        """
        Set contextRPortPrototype with validation.

        Args:
            value: The contextRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"contextRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._contextRPortPrototype = value
        # sequenceOffset=30.
        self._targetDataElement: RefType = None

    @property
    def target_data_element(self) -> RefType:
        """Get targetDataElement (Pythonic accessor)."""
        return self._targetDataElement

    @target_data_element.setter
    def target_data_element(self, value: RefType) -> None:
        """
        Set targetDataElement with validation.

        Args:
            value: The targetDataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetDataElement = None
            return

        self._targetDataElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextRPortPrototype(self) -> "AbstractRequiredPort":
        """
        AUTOSAR-compliant getter for contextRPortPrototype.

        Returns:
            The contextRPortPrototype value

        Note:
            Delegates to context_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_r_port_prototype  # Delegates to property

    def setContextRPortPrototype(self, value: "AbstractRequiredPort") -> "RVariableInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextRPortPrototype with method chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_r_port_prototype property setter (gets validation automatically)
        """
        self.context_r_port_prototype = value  # Delegates to property setter
        return self

    def getTargetDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetDataElement.

        Returns:
            The targetDataElement value

        Note:
            Delegates to target_data_element property (CODING_RULE_V2_00017)
        """
        return self.target_data_element  # Delegates to property

    def setTargetDataElement(self, value: RefType) -> "RVariableInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetDataElement with method chaining.

        Args:
            value: The targetDataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data_element property setter (gets validation automatically)
        """
        self.target_data_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> "RVariableInAtomicSwcInstanceRef":
        """
        Set contextRPortPrototype and return self for chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_r_port_prototype("value")
        """
        self.context_r_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_data_element(self, value: Optional[RefType]) -> "RVariableInAtomicSwcInstanceRef":
        """
        Set targetDataElement and return self for chaining.

        Args:
            value: The targetDataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data_element("value")
        """
        self.target_data_element = value  # Use property setter (gets validation)
        return self
