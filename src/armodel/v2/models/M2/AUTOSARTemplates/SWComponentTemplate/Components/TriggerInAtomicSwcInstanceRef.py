from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TriggerInAtomicSwcInstanceRef(ARObject, ABC):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::TriggerInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 944, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is TriggerInAtomicSwcInstanceRef:
            raise TypeError("TriggerInAtomicSwcInstanceRef is an abstract class.")
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
        # Stereotypes: atpAbstract.
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
        # Stereotypes: atpAbstract.
        self._target: RefType = None

    @property
    def target(self) -> RefType:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: RefType) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        self._target = value

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

    def setBase(self, value: "AtomicSwComponent") -> "TriggerInAtomicSwcInstanceRef":
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

    def getContextPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextPort.

        Returns:
            The contextPort value

        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: RefType) -> "TriggerInAtomicSwcInstanceRef":
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

    def getTarget(self) -> RefType:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: RefType) -> "TriggerInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for target with method chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["AtomicSwComponent"]) -> "TriggerInAtomicSwcInstanceRef":
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

    def with_context_port(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
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

    def with_target(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
        """
        Set target and return self for chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self
