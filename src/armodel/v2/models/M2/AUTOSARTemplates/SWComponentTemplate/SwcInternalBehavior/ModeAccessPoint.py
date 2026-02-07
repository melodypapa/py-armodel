from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ModeAccessPoint(ARObject):
    """
    A ModeAccessPoint is required by a RunnableEntity owned by a Mode Manager or
    Mode User. Its semantics implies the ability to access the current mode
    (provided by the RTE) of a ModeDeclaration GroupPrototype’s
    ModeDeclarationGroup.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup::ModeAccessPoint
    
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