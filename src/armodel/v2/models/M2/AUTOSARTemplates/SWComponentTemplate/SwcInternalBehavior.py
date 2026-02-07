from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SwcInternalBehavior(InternalBehavior):
    """
    The SwcInternalBehavior of an AtomicSwComponentType describes the relevant
    aspects of the software-component with respect to the RTE, i.e. the
    RunnableEntities and the RTEEvents they respond to.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::SwcInternalBehavior
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 345, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 518, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2070, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 246, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 472, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 217, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines an AUTOSAR typed memory-block that needs to available for each
                # instance of the SW-component.
        # is typically only useful if supportsMultipleInstantiation to "true" or if the
                # component defines NVRAM permanent blocks.
        # of arTypedPerInstanceMemory is subject with the purpose to support
                # variability in the implementations.
        # Typically different the implementation are requiring different memory
                # objects.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._arTypedPer: List[RefType] = []

    @property
    def ar_typed_per(self) -> List[RefType]:
        """Get arTypedPer (Pythonic accessor)."""
        return self._arTypedPer
        # This is a RTEEvent specified for the particular Swc of RTEEvent is subject to
        # variability with to support the conditional existence of RTE the number of
        # RTE events might vary due conditional existence of PortPrototypes using Data
        # due to different scheduling needs of atpVariation.
        self._event: List["RTEEvent"] = []

    @property
    def event(self) -> List["RTEEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event
        # Options how to generate the ExclusiveArea related APIs.
        # When no SwcExclusiveAreaPolicy is specified for an default values apply.
        # atpVariation.
        self._exclusiveArea: List["SwcExclusiveArea"] = []

    @property
    def exclusive_area(self) -> List["SwcExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea
        # Implement state message semantics for establishing among runnables of the
        # same The aggregation of explicitInterRunnable subject to variability with the
        # purpose to in the software components different algorithms in the requiring
        # different number of memory atpVariation.
        self._explicitInter: List[RefType] = []

    @property
    def explicit_inter(self) -> List[RefType]:
        """Get explicitInter (Pythonic accessor)."""
        return self._explicitInter
        # Implement state message semantics for establishing among runnables of the
        # same The aggregation of implicitInterRunnable subject to variability with the
        # purpose to in the software components different algorithms in the requiring
        # different number of memory atpVariation.
        self._implicitInter: List[RefType] = []

    @property
    def implicit_inter(self) -> List[RefType]:
        """Get implicitInter (Pythonic accessor)."""
        return self._implicitInter
        # The includedDataTypeSet is used by a software for its implementation.
        self._includedData: List[RefType] = []

    @property
    def included_data(self) -> List[RefType]:
        """Get includedData (Pythonic accessor)."""
        return self._includedData
        # This aggregation represents the included Mode DeclarationGroups atpSplitable
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
        # Description Template R23-11.
        self._includedMode: List["IncludedMode"] = []

    @property
    def included_mode(self) -> List["IncludedMode"]:
        """Get includedMode (Pythonic accessor)."""
        return self._includedMode
        # The purpose of this is that within the context of a given SwComponentType
                # some data def properties of individual be modified.
        # The aggregation of subject to variability with the support the conditional
                # existence of Port component local memories like "per
                # "arTypedPerInstanceMemory".
        # atpVariation.
        self._instantiation: List["InstantiationDataDef"] = []

    @property
    def instantiation(self) -> List["InstantiationDataDef"]:
        """Get instantiation (Pythonic accessor)."""
        return self._instantiation
        # Defines parameter(s) or characteristic value(s) that needs to be available
                # for each instance of the is typically only useful if set to "true".
        # The perInstanceParameter is subject to the purpose to support variability in
                # the implementations.
        # Typically different the implementation are requiring different memory
                # objects.
        # atpVariation.
        self._perInstance: List["ParameterData"] = []

    @property
    def per_instance(self) -> List["ParameterData"]:
        """Get perInstance (Pythonic accessor)."""
        return self._perInstance
        # Options for generating the signature of port-related calls runnable to the
                # RTE and vice versa.
        # The PortPrototypes is subject to variability with to support the conditional
                # existence of ports.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._portAPIOption: List["PortAPIOption"] = []

    @property
    def port_api_option(self) -> List["PortAPIOption"]:
        """Get portAPIOption (Pythonic accessor)."""
        return self._portAPIOption
        # This is a RunnableEntity specified for the particular Swc of RunnableEntity
                # is subject to variability purpose to support the conditional existence of the
                # number of RunnableEntities due to the conditional existence of Port
                # DataReceivedEvents or due to different of algorithms.
        # atpVariation.
        self._runnable: List["RunnableEntity"] = []

    @property
    def runnable(self) -> List["RunnableEntity"]:
        """Get runnable (Pythonic accessor)."""
        return self._runnable
        # Defines the requirements on AUTOSAR Services for a particular item.
        # of SwcServiceDependency is subject to the purpose to support the conditional
                # ports as well as the conditional existence of owned by an SwcInternal be
                # located in a different physical file in order that SwcServiceDependency might
                # be later development steps or even by different (e.
        # g OBD expert for Obd related Service Therefore the aggregation is <<atp
                # atpVariation.
        self._service: List["SwcService"] = []

    @property
    def service(self) -> List["SwcService"]:
        """Get service (Pythonic accessor)."""
        return self._service
        # Defines parameter(s) or characteristic value(s) shared between
                # SwComponentPrototypes of the same Sw aggregation of sharedParameter is
                # variability with the purpose to support variability software components
                # implementations.
        # Typically in the implementation are requiring of memory objects.
        # atpVariation.
        self._shared: List["ParameterData"] = []

    @property
    def shared(self) -> List["ParameterData"]:
        """Get shared (Pythonic accessor)."""
        return self._shared
        # Indicate whether the corresponding software-component be multiply
                # instantiated on one ECU.
        # In this case the will result in an appropriate component API on level (with
                # or without instance.
        self._supports: Optional["Boolean"] = None

    @property
    def supports(self) -> Optional["Boolean"]:
        """Get supports (Pythonic accessor)."""
        return self._supports

    @supports.setter
    def supports(self, value: Optional["Boolean"]) -> None:
        """
        Set supports with validation.
        
        Args:
            value: The supports to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supports = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"supports must be Boolean or None, got {type(value).__name__}"
            )
        self._supports = value
        # Proxy of a variation points in the C/C++ implementation.
        # atpSplitable.
        self._variationPoint: List["VariationPointProxy"] = []

    @property
    def variation_point(self) -> List["VariationPointProxy"]:
        """Get variationPoint (Pythonic accessor)."""
        return self._variationPoint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArTypedPer(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for arTypedPer.
        
        Returns:
            The arTypedPer value
        
        Note:
            Delegates to ar_typed_per property (CODING_RULE_V2_00017)
        """
        return self.ar_typed_per  # Delegates to property

    def getEvent(self) -> List["RTEEvent"]:
        """
        AUTOSAR-compliant getter for event.
        
        Returns:
            The event value
        
        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def getExclusiveArea(self) -> List["SwcExclusiveArea"]:
        """
        AUTOSAR-compliant getter for exclusiveArea.
        
        Returns:
            The exclusiveArea value
        
        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def getExplicitInter(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for explicitInter.
        
        Returns:
            The explicitInter value
        
        Note:
            Delegates to explicit_inter property (CODING_RULE_V2_00017)
        """
        return self.explicit_inter  # Delegates to property

    def getImplicitInter(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for implicitInter.
        
        Returns:
            The implicitInter value
        
        Note:
            Delegates to implicit_inter property (CODING_RULE_V2_00017)
        """
        return self.implicit_inter  # Delegates to property

    def getIncludedData(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for includedData.
        
        Returns:
            The includedData value
        
        Note:
            Delegates to included_data property (CODING_RULE_V2_00017)
        """
        return self.included_data  # Delegates to property

    def getIncludedMode(self) -> List["IncludedMode"]:
        """
        AUTOSAR-compliant getter for includedMode.
        
        Returns:
            The includedMode value
        
        Note:
            Delegates to included_mode property (CODING_RULE_V2_00017)
        """
        return self.included_mode  # Delegates to property

    def getInstantiation(self) -> List["InstantiationDataDef"]:
        """
        AUTOSAR-compliant getter for instantiation.
        
        Returns:
            The instantiation value
        
        Note:
            Delegates to instantiation property (CODING_RULE_V2_00017)
        """
        return self.instantiation  # Delegates to property

    def getPerInstance(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for perInstance.
        
        Returns:
            The perInstance value
        
        Note:
            Delegates to per_instance property (CODING_RULE_V2_00017)
        """
        return self.per_instance  # Delegates to property

    def getPortAPIOption(self) -> List["PortAPIOption"]:
        """
        AUTOSAR-compliant getter for portAPIOption.
        
        Returns:
            The portAPIOption value
        
        Note:
            Delegates to port_api_option property (CODING_RULE_V2_00017)
        """
        return self.port_api_option  # Delegates to property

    def getRunnable(self) -> List["RunnableEntity"]:
        """
        AUTOSAR-compliant getter for runnable.
        
        Returns:
            The runnable value
        
        Note:
            Delegates to runnable property (CODING_RULE_V2_00017)
        """
        return self.runnable  # Delegates to property

    def getService(self) -> List["SwcService"]:
        """
        AUTOSAR-compliant getter for service.
        
        Returns:
            The service value
        
        Note:
            Delegates to service property (CODING_RULE_V2_00017)
        """
        return self.service  # Delegates to property

    def getShared(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for shared.
        
        Returns:
            The shared value
        
        Note:
            Delegates to shared property (CODING_RULE_V2_00017)
        """
        return self.shared  # Delegates to property

    def getSupports(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for supports.
        
        Returns:
            The supports value
        
        Note:
            Delegates to supports property (CODING_RULE_V2_00017)
        """
        return self.supports  # Delegates to property

    def setSupports(self, value: "Boolean") -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant setter for supports with method chaining.
        
        Args:
            value: The supports to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to supports property setter (gets validation automatically)
        """
        self.supports = value  # Delegates to property setter
        return self

    def getVariationPoint(self) -> List["VariationPointProxy"]:
        """
        AUTOSAR-compliant getter for variationPoint.
        
        Returns:
            The variationPoint value
        
        Note:
            Delegates to variation_point property (CODING_RULE_V2_00017)
        """
        return self.variation_point  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_supports(self, value: Optional["Boolean"]) -> "SwcInternalBehavior":
        """
        Set supports and return self for chaining.
        
        Args:
            value: The supports to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_supports("value")
        """
        self.supports = value  # Use property setter (gets validation)
        return self