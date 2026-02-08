from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior


class BswInternalBehavior(InternalBehavior):
    """
    Specifies the behavior of a BSW module or a BSW cluster w.r.t. the code
    entities visible by the BSW Scheduler. It is possible to have several
    different BswInternalBehaviors referring to the same BswModule Description.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 65, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 649, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2003, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 208, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 165, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines an AUTOSAR typed memory-block that needs to available for each
        # instance of the Basic Software The aggregation of arTypedPerInstanceMemory to
        # variability with the purpose to support the Basic Software Module’s different
        # algorithms in the requiring different number of memory atpVariation.
        self._arTypedPer: List[RefType] = []

    @property
    def ar_typed_per(self) -> List[RefType]:
        """Get arTypedPer (Pythonic accessor)."""
        return self._arTypedPer
        # Policy for a arTypedPerInstanceMemory The policy selects the options of the
        # Schedule Manager API atpVariation 381 Document ID 89:
        # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._bswPerInstance: List["BswPerInstance"] = []

    @property
    def bsw_per_instance(self) -> List["BswPerInstance"]:
        """Get bswPerInstance (Pythonic accessor)."""
        return self._bswPerInstance
        # Policy for a requiredClientServerEntry.
        # The policy selects of the Schedule Manager API generation.
        # atpVariation.
        self._clientPolicy: List["BswClientPolicy"] = []

    @property
    def client_policy(self) -> List["BswClientPolicy"]:
        """Get clientPolicy (Pythonic accessor)."""
        return self._clientPolicy
        # Indicates an abstract partition context in which the enclosing
                # BswModuleEntity can be executed.
        # atpVariation.
        self._distinguished: List["BswDistinguished"] = []

    @property
    def distinguished(self) -> List["BswDistinguished"]:
        """Get distinguished (Pythonic accessor)."""
        return self._distinguished
        # A code entity for which the behavior is described atpVariation.
        self._entity: List["BswModuleEntity"] = []

    @property
    def entity(self) -> List["BswModuleEntity"]:
        """Get entity (Pythonic accessor)."""
        return self._entity
        # An event required by this module behavior.
        # atpVariation.
        self._event: List["BswEvent"] = []

    @property
    def event(self) -> List["BswEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event
        # Policy for an ExclusiveArea in this BswInternalBehavior.
        # The policy selects the options of the Schedule Manager atpVariation.
        self._exclusiveArea: List["BswExclusiveArea"] = []

    @property
    def exclusive_area(self) -> List["BswExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea
        # The includedDataTypeSet is used by a basic software for its implementation.
        self._includedData: List[RefType] = []

    @property
    def included_data(self) -> List[RefType]:
        """Get includedData (Pythonic accessor)."""
        return self._includedData
        # This aggregation represents the included Mode DeclarationGroups atpSplitable.
        self._includedMode: List["IncludedMode"] = []

    @property
    def included_mode(self) -> List["IncludedMode"]:
        """Get includedMode (Pythonic accessor)."""
        return self._includedMode
        # Policy for an internalTriggeringPoint in this BswInternal Behavior.
        # The policy selects the options of the Schedule API generation.
        # atpVariation.
        self._internal: List[RefType] = []

    @property
    def internal(self) -> List[RefType]:
        """Get internal (Pythonic accessor)."""
        return self._internal
        # Implementation policy for the reception of mode switches.
        # Stereotypes: atpSplitable; atpVariation.
        self._modeReceiver: List["BswModeReceiver"] = []

    @property
    def mode_receiver(self) -> List["BswModeReceiver"]:
        """Get modeReceiver (Pythonic accessor)."""
        return self._modeReceiver
        # Implementation policy for providing a mode group.
        # atpSplitable; atpVariation.
        self._modeSender: List["BswModeSenderPolicy"] = []

    @property
    def mode_sender(self) -> List["BswModeSenderPolicy"]:
        """Get modeSender (Pythonic accessor)."""
        return self._modeSender
        # Policy for a perInstanceParameter in this BswInternal policy selects the
                # options of the Schedule generation.
        # atpVariation.
        self._parameterPolicy: List["BswParameterPolicy"] = []

    @property
    def parameter_policy(self) -> List["BswParameterPolicy"]:
        """Get parameterPolicy (Pythonic accessor)."""
        return self._parameterPolicy
        # Describes a read only memory object containing characteristic value(s) needed
                # by this BswInternal role name perInstanceParameter is chosen to the similar
                # role in the context of SwcInternal to constantMemory, this object is not
                # allocated the module’s code, but by the BSW Scheduler is accessed from the
                # BSW module via the BSW The main use case is the support of of calibration
                # data.
        # is subject to variability with the purpose implementation variants.
        # atpVariation.
        self._perInstance: List["ParameterData"] = []

    @property
    def per_instance(self) -> List["ParameterData"]:
        """Get perInstance (Pythonic accessor)."""
        return self._perInstance
        # Data reception policy for inter-partition and/or inter-core atpVariation 381
        # Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
        # Description Template R23-11.
        self._receptionPolicy: List["BswDataReception"] = []

    @property
    def reception_policy(self) -> List["BswDataReception"]:
        """Get receptionPolicy (Pythonic accessor)."""
        return self._receptionPolicy
        # Policy for a releasedTrigger.
        # The policy selects the options of the Schedule Manager API generation.
        # atpVariation.
        self._releasedTrigger: List[RefType] = []

    @property
    def released_trigger(self) -> List[RefType]:
        """Get releasedTrigger (Pythonic accessor)."""
        return self._releasedTrigger
        # Optional definition of one or more prefixes to be used for the BswScheduler.
        # atpVariation.
        self._schedulerName: List["BswSchedulerName"] = []

    @property
    def scheduler_name(self) -> List["BswSchedulerName"]:
        """Get schedulerName (Pythonic accessor)."""
        return self._schedulerName
        # Policy for a providedData.
        # The policy selects the options Schedule Manager API generation.
        # atpVariation.
        self._sendPolicy: List["BswDataSendPolicy"] = []

    @property
    def send_policy(self) -> List["BswDataSendPolicy"]:
        """Get sendPolicy (Pythonic accessor)."""
        return self._sendPolicy
        # Defines the requirements on AUTOSAR Services for a particular item.
        # is subject to variability with the purpose the conditional existence of
                # ServiceNeeds.
        # is splitable in order to support that be provided in later development
                # atpVariation.
        self._service: List["BswService"] = []

    @property
    def service(self) -> List["BswService"]:
        """Get service (Pythonic accessor)."""
        return self._service
        # Specifies a trigger to be directly implemented via OS calls.
        # atpVariation.
        self._triggerDirect: List[RefType] = []

    @property
    def trigger_direct(self) -> List[RefType]:
        """Get triggerDirect (Pythonic accessor)."""
        return self._triggerDirect
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

    def getBswPerInstance(self) -> List["BswPerInstance"]:
        """
        AUTOSAR-compliant getter for bswPerInstance.

        Returns:
            The bswPerInstance value

        Note:
            Delegates to bsw_per_instance property (CODING_RULE_V2_00017)
        """
        return self.bsw_per_instance  # Delegates to property

    def getClientPolicy(self) -> List["BswClientPolicy"]:
        """
        AUTOSAR-compliant getter for clientPolicy.

        Returns:
            The clientPolicy value

        Note:
            Delegates to client_policy property (CODING_RULE_V2_00017)
        """
        return self.client_policy  # Delegates to property

    def getDistinguished(self) -> List["BswDistinguished"]:
        """
        AUTOSAR-compliant getter for distinguished.

        Returns:
            The distinguished value

        Note:
            Delegates to distinguished property (CODING_RULE_V2_00017)
        """
        return self.distinguished  # Delegates to property

    def getEntity(self) -> List["BswModuleEntity"]:
        """
        AUTOSAR-compliant getter for entity.

        Returns:
            The entity value

        Note:
            Delegates to entity property (CODING_RULE_V2_00017)
        """
        return self.entity  # Delegates to property

    def getEvent(self) -> List["BswEvent"]:
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def getExclusiveArea(self) -> List["BswExclusiveArea"]:
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

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

    def getInternal(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for internal.

        Returns:
            The internal value

        Note:
            Delegates to internal property (CODING_RULE_V2_00017)
        """
        return self.internal  # Delegates to property

    def getModeReceiver(self) -> List["BswModeReceiver"]:
        """
        AUTOSAR-compliant getter for modeReceiver.

        Returns:
            The modeReceiver value

        Note:
            Delegates to mode_receiver property (CODING_RULE_V2_00017)
        """
        return self.mode_receiver  # Delegates to property

    def getModeSender(self) -> List["BswModeSenderPolicy"]:
        """
        AUTOSAR-compliant getter for modeSender.

        Returns:
            The modeSender value

        Note:
            Delegates to mode_sender property (CODING_RULE_V2_00017)
        """
        return self.mode_sender  # Delegates to property

    def getParameterPolicy(self) -> List["BswParameterPolicy"]:
        """
        AUTOSAR-compliant getter for parameterPolicy.

        Returns:
            The parameterPolicy value

        Note:
            Delegates to parameter_policy property (CODING_RULE_V2_00017)
        """
        return self.parameter_policy  # Delegates to property

    def getPerInstance(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for perInstance.

        Returns:
            The perInstance value

        Note:
            Delegates to per_instance property (CODING_RULE_V2_00017)
        """
        return self.per_instance  # Delegates to property

    def getReceptionPolicy(self) -> List["BswDataReception"]:
        """
        AUTOSAR-compliant getter for receptionPolicy.

        Returns:
            The receptionPolicy value

        Note:
            Delegates to reception_policy property (CODING_RULE_V2_00017)
        """
        return self.reception_policy  # Delegates to property

    def getReleasedTrigger(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for releasedTrigger.

        Returns:
            The releasedTrigger value

        Note:
            Delegates to released_trigger property (CODING_RULE_V2_00017)
        """
        return self.released_trigger  # Delegates to property

    def getSchedulerName(self) -> List["BswSchedulerName"]:
        """
        AUTOSAR-compliant getter for schedulerName.

        Returns:
            The schedulerName value

        Note:
            Delegates to scheduler_name property (CODING_RULE_V2_00017)
        """
        return self.scheduler_name  # Delegates to property

    def getSendPolicy(self) -> List["BswDataSendPolicy"]:
        """
        AUTOSAR-compliant getter for sendPolicy.

        Returns:
            The sendPolicy value

        Note:
            Delegates to send_policy property (CODING_RULE_V2_00017)
        """
        return self.send_policy  # Delegates to property

    def getService(self) -> List["BswService"]:
        """
        AUTOSAR-compliant getter for service.

        Returns:
            The service value

        Note:
            Delegates to service property (CODING_RULE_V2_00017)
        """
        return self.service  # Delegates to property

    def getTriggerDirect(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for triggerDirect.

        Returns:
            The triggerDirect value

        Note:
            Delegates to trigger_direct property (CODING_RULE_V2_00017)
        """
        return self.trigger_direct  # Delegates to property

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
