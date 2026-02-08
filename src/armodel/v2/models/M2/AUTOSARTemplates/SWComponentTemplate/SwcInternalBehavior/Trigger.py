"""
AUTOSAR Package - Trigger

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)




class ExternalTriggeringPoint(ARObject):
    """
    If a RunnableEntity owns an ExternalTriggeringPoint it is entitled to raise
    an ExternalTriggerOccurred Event.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger::ExternalTriggeringPoint
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 315, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 584, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The aggregation in the role ident provides the ability to the
                # ExternalTriggeringPoint identifiable.
        # semantical point of view, the ExternalTriggering considered a first-class
                # Identifiable and therefore in the role ident shall always exist (until it
                # possible to let ModeAccessPoint directly inherit.
        self._ident: Optional["RefType"] = None

    @property
    def ident(self) -> Optional["RefType"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["RefType"]) -> None:
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

        self._ident = value
        # by: PTriggerInAtomicSwc.
        self._triggerTypeInstanceRef: Optional["RefType"] = None

    @property
    def trigger_type_instance_ref(self) -> Optional["RefType"]:
        """Get triggerTypeInstanceRef (Pythonic accessor)."""
        return self._triggerTypeInstanceRef

    @trigger_type_instance_ref.setter
    def trigger_type_instance_ref(self, value: Optional["RefType"]) -> None:
        """
        Set triggerTypeInstanceRef with validation.
        
        Args:
            value: The triggerTypeInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerTypeInstanceRef = None
            return

        self._triggerTypeInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdent(self) -> "RefType":
        """
        AUTOSAR-compliant getter for ident.
        
        Returns:
            The ident value
        
        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "RefType") -> "ExternalTriggeringPoint":
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

    def getTriggerTypeInstanceRef(self) -> "RefType":
        """
        AUTOSAR-compliant getter for triggerTypeInstanceRef.
        
        Returns:
            The triggerTypeInstanceRef value
        
        Note:
            Delegates to trigger_type_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.trigger_type_instance_ref  # Delegates to property

    def setTriggerTypeInstanceRef(self, value: "RefType") -> "ExternalTriggeringPoint":
        """
        AUTOSAR-compliant setter for triggerTypeInstanceRef with method chaining.
        
        Args:
            value: The triggerTypeInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trigger_type_instance_ref property setter (gets validation automatically)
        """
        self.trigger_type_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional[RefType]) -> "ExternalTriggeringPoint":
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

    def with_trigger_type_instance_ref(self, value: Optional[RefType]) -> "ExternalTriggeringPoint":
        """
        Set triggerTypeInstanceRef and return self for chaining.
        
        Args:
            value: The triggerTypeInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trigger_type_instance_ref("value")
        """
        self.trigger_type_instance_ref = value  # Use property setter (gets validation)
        return self



class InternalTriggeringPoint(AbstractAccessPoint):
    """
    If a RunnableEntity owns an InternalTriggeringPoint it is entitled to
    trigger the execution of Runnable Entities of the corresponding
    software-component.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger::InternalTriggeringPoint
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 322, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 561, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute, when set to value queued, allows for a of Triggers.
        self._swImplPolicy: Optional["SwImplPolicyEnum"] = None

    @property
    def sw_impl_policy(self) -> Optional["SwImplPolicyEnum"]:
        """Get swImplPolicy (Pythonic accessor)."""
        return self._swImplPolicy

    @sw_impl_policy.setter
    def sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> None:
        """
        Set swImplPolicy with validation.
        
        Args:
            value: The swImplPolicy to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swImplPolicy = None
            return

        if not isinstance(value, SwImplPolicyEnum):
            raise TypeError(
                f"swImplPolicy must be SwImplPolicyEnum or None, got {type(value).__name__}"
            )
        self._swImplPolicy = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwImplPolicy(self) -> "SwImplPolicyEnum":
        """
        AUTOSAR-compliant getter for swImplPolicy.
        
        Returns:
            The swImplPolicy value
        
        Note:
            Delegates to sw_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.sw_impl_policy  # Delegates to property

    def setSwImplPolicy(self, value: "SwImplPolicyEnum") -> "InternalTriggeringPoint":
        """
        AUTOSAR-compliant setter for swImplPolicy with method chaining.
        
        Args:
            value: The swImplPolicy to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_impl_policy property setter (gets validation automatically)
        """
        self.sw_impl_policy = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> "InternalTriggeringPoint":
        """
        Set swImplPolicy and return self for chaining.
        
        Args:
            value: The swImplPolicy to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_impl_policy("value")
        """
        self.sw_impl_policy = value  # Use property setter (gets validation)
        return self