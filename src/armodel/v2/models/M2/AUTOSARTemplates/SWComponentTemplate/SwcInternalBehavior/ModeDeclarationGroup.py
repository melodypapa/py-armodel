from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeAccessPoint(ARObject):
    """
    A ModeAccessPoint is required by a RunnableEntity owned by a Mode Manager or
    Mode User. Its semantics implies the ability to access the current mode
    (provided by the RTE) of a ModeDeclaration GroupPrototype’s
    ModeDeclarationGroup.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 323, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 634, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The aggregation in the role ident provides the ability to ModeAccessPoint
                # identifiable.
        # semantical point of view, the ModeAccessPoint a first-class Identifiable and
                # therefore the the role ident shall always exist (until it possible to let
                # ModeAccessPoint directly inherit.
        self._ident: Optional["ModeAccessPointIdent"] = None

    @property
    def ident(self) -> Optional["ModeAccessPointIdent"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["ModeAccessPointIdent"]) -> None:
        """
        Set ident with validation.

        Args:
            value: The ident to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ident = None
            return

        if not isinstance(value, ModeAccessPointIdent):
            raise TypeError(
                f"ident must be ModeAccessPointIdent or None, got {type(value).__name__}"
            )
        self._ident = value
        # by: ModeGroupInAtomicSwc.
        self._modeGroupInstanceRef: RefType = None

    @property
    def mode_group_instance_ref(self) -> RefType:
        """Get modeGroupInstanceRef (Pythonic accessor)."""
        return self._modeGroupInstanceRef

    @mode_group_instance_ref.setter
    def mode_group_instance_ref(self, value: RefType) -> None:
        """
        Set modeGroupInstanceRef with validation.

        Args:
            value: The modeGroupInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroupInstanceRef = None
            return

        self._modeGroupInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdent(self) -> "ModeAccessPointIdent":
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "ModeAccessPointIdent") -> "ModeAccessPoint":
        """
        AUTOSAR-compliant setter for ident with method chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Note:
            Delegates to ident property setter (gets validation automatically)
        """
        self.ident = value  # Delegates to property setter
        return self

    def getModeGroupInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroupInstanceRef.

        Returns:
            The modeGroupInstanceRef value

        Note:
            Delegates to mode_group_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.mode_group_instance_ref  # Delegates to property

    def setModeGroupInstanceRef(self, value: RefType) -> "ModeAccessPoint":
        """
        AUTOSAR-compliant setter for modeGroupInstanceRef with method chaining.

        Args:
            value: The modeGroupInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group_instance_ref property setter (gets validation automatically)
        """
        self.mode_group_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional["ModeAccessPointIdent"]) -> "ModeAccessPoint":
        """
        Set ident and return self for chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ident("value")
        """
        self.ident = value  # Use property setter (gets validation)
        return self

    def with_mode_group_instance_ref(self, value: Optional[RefType]) -> "ModeAccessPoint":
        """
        Set modeGroupInstanceRef and return self for chaining.

        Args:
            value: The modeGroupInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group_instance_ref("value")
        """
        self.mode_group_instance_ref = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint

    RefType,
)


class ModeSwitchPoint(AbstractAccessPoint):
    """
    A ModeSwitchPoint is required by a RunnableEntity owned a Mode Manager. Its
    semantics implies the ability to initiate a mode switch.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 323, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 633, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: PModeGroupInAtomic.
        self._modeGroupSwcInstanceRef: RefType = None

    @property
    def mode_group_swc_instance_ref(self) -> RefType:
        """Get modeGroupSwcInstanceRef (Pythonic accessor)."""
        return self._modeGroupSwcInstanceRef

    @mode_group_swc_instance_ref.setter
    def mode_group_swc_instance_ref(self, value: RefType) -> None:
        """
        Set modeGroupSwcInstanceRef with validation.

        Args:
            value: The modeGroupSwcInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroupSwcInstanceRef = None
            return

        self._modeGroupSwcInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroupSwcInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroupSwcInstanceRef.

        Returns:
            The modeGroupSwcInstanceRef value

        Note:
            Delegates to mode_group_swc_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.mode_group_swc_instance_ref  # Delegates to property

    def setModeGroupSwcInstanceRef(self, value: RefType) -> "ModeSwitchPoint":
        """
        AUTOSAR-compliant setter for modeGroupSwcInstanceRef with method chaining.

        Args:
            value: The modeGroupSwcInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group_swc_instance_ref property setter (gets validation automatically)
        """
        self.mode_group_swc_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group_swc_instance_ref(self, value: Optional[RefType]) -> "ModeSwitchPoint":
        """
        Set modeGroupSwcInstanceRef and return self for chaining.

        Args:
            value: The modeGroupSwcInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group_swc_instance_ref("value")
        """
        self.mode_group_swc_instance_ref = value  # Use property setter (gets validation)
        return self

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


class IncludedModeDeclarationGroupSet(ARObject):
    """
    An IncludedModeDeclarationGroupSet declares that a set of
    ModeDeclarationGroups used by the software component for its implementation
    and consequently these ModeDeclarationGroups become part of the contract.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 601, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the referenced ModeDeclarationGroup.
        self._mode: List[RefType] = []

    @property
    def mode(self) -> List[RefType]:
        """Get mode (Pythonic accessor)."""
        return self._mode
        # The prefix shall be used by the RTE generator as a prefix creation of symbols
        # related to the referenced RTE_TRANSITION_<Mode.
        self._prefix: Optional["Identifier"] = None

    @property
    def prefix(self) -> Optional["Identifier"]:
        """Get prefix (Pythonic accessor)."""
        return self._prefix

    @prefix.setter
    def prefix(self, value: Optional["Identifier"]) -> None:
        """
        Set prefix with validation.

        Args:
            value: The prefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._prefix = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"prefix must be Identifier or None, got {type(value).__name__}"
            )
        self._prefix = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def getPrefix(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for prefix.

        Returns:
            The prefix value

        Note:
            Delegates to prefix property (CODING_RULE_V2_00017)
        """
        return self.prefix  # Delegates to property

    def setPrefix(self, value: "Identifier") -> "IncludedModeDeclarationGroupSet":
        """
        AUTOSAR-compliant setter for prefix with method chaining.

        Args:
            value: The prefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to prefix property setter (gets validation automatically)
        """
        self.prefix = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_prefix(self, value: Optional["Identifier"]) -> "IncludedModeDeclarationGroupSet":
        """
        Set prefix and return self for chaining.

        Args:
            value: The prefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prefix("value")
        """
        self.prefix = value  # Use property setter (gets validation)
        return self
