from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PortInCompositionTypeInstanceRef(ARObject, ABC):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 950, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is PortInCompositionTypeInstanceRef:
            raise TypeError("PortInCompositionTypeInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpAbstract Tags: xml.
        # sequenceOffset=20.
        self._abstractContext: Optional["SwComponent"] = None

    @property
    def abstract_context(self) -> Optional["SwComponent"]:
        """Get abstractContext (Pythonic accessor)."""
        return self._abstractContext

    @abstract_context.setter
    def abstract_context(self, value: Optional["SwComponent"]) -> None:
        """
        Set abstractContext with validation.

        Args:
            value: The abstractContext to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._abstractContext = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"abstractContext must be SwComponent or None, got {type(value).__name__}"
            )
        self._abstractContext = value
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
        self._base: Optional["CompositionSw"] = None

    @property
    def base(self) -> Optional["CompositionSw"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["CompositionSw"]) -> None:
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

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"base must be CompositionSw or None, got {type(value).__name__}"
            )
        self._base = value
        # Stereotypes: atpAbstract.
        self._targetPort: RefType = None

    @property
    def target_port(self) -> RefType:
        """Get targetPort (Pythonic accessor)."""
        return self._targetPort

    @target_port.setter
    def target_port(self, value: RefType) -> None:
        """
        Set targetPort with validation.

        Args:
            value: The targetPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetPort = None
            return

        self._targetPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbstractContext(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for abstractContext.

        Returns:
            The abstractContext value

        Note:
            Delegates to abstract_context property (CODING_RULE_V2_00017)
        """
        return self.abstract_context  # Delegates to property

    def setAbstractContext(self, value: "SwComponent") -> "PortInCompositionTypeInstanceRef":
        """
        AUTOSAR-compliant setter for abstractContext with method chaining.

        Args:
            value: The abstractContext to set

        Returns:
            self for method chaining

        Note:
            Delegates to abstract_context property setter (gets validation automatically)
        """
        self.abstract_context = value  # Delegates to property setter
        return self

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> "PortInCompositionTypeInstanceRef":
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

    def getTargetPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetPort.

        Returns:
            The targetPort value

        Note:
            Delegates to target_port property (CODING_RULE_V2_00017)
        """
        return self.target_port  # Delegates to property

    def setTargetPort(self, value: RefType) -> "PortInCompositionTypeInstanceRef":
        """
        AUTOSAR-compliant setter for targetPort with method chaining.

        Args:
            value: The targetPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_port property setter (gets validation automatically)
        """
        self.target_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_abstract_context(self, value: Optional["SwComponent"]) -> "PortInCompositionTypeInstanceRef":
        """
        Set abstractContext and return self for chaining.

        Args:
            value: The abstractContext to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_abstract_context("value")
        """
        self.abstract_context = value  # Use property setter (gets validation)
        return self

    def with_base(self, value: Optional["CompositionSw"]) -> "PortInCompositionTypeInstanceRef":
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

    def with_target_port(self, value: Optional[RefType]) -> "PortInCompositionTypeInstanceRef":
        """
        Set targetPort and return self for chaining.

        Args:
            value: The targetPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_port("value")
        """
        self.target_port = value  # Use property setter (gets validation)
        return self
