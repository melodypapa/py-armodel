"""
AUTOSAR Package - BswBehavior

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    PositiveInteger,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ImplementationProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    AbstractEvent,
    ExecutableEntity,
    InternalBehavior,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceDependency,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class BswInternalBehavior(InternalBehavior):
    """
    Specifies the behavior of a BSW module or a BSW cluster w.r.t. the code
    entities visible by the BSW Scheduler. It is possible to have several
    different BswInternalBehaviors referring to the same BswModule Description.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInternalBehavior

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
        self._arTypedPer: List["RefType"] = []

    @property
    def ar_typed_per(self) -> List["RefType"]:
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
        self._entity: List[BswModuleEntity] = []

    @property
    def entity(self) -> List[BswModuleEntity]:
        """Get entity (Pythonic accessor)."""
        return self._entity
        # An event required by this module behavior.
        # atpVariation.
        self._event: List[BswEvent] = []

    @property
    def event(self) -> List[BswEvent]:
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
        self._includedData: List["RefType"] = []

    @property
    def included_data(self) -> List["RefType"]:
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
        self._internal: List["RefType"] = []

    @property
    def internal(self) -> List["RefType"]:
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
        self._modeSender: List[BswModeSenderPolicy] = []

    @property
    def mode_sender(self) -> List[BswModeSenderPolicy]:
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
        self._releasedTrigger: List["RefType"] = []

    @property
    def released_trigger(self) -> List["RefType"]:
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
        self._triggerDirect: List["RefType"] = []

    @property
    def trigger_direct(self) -> List["RefType"]:
        """Get triggerDirect (Pythonic accessor)."""
        return self._triggerDirect
        # Proxy of a variation points in the C/C++ implementation.
        # atpSplitable.
        self._variationPoint: List["VariationPointProxy"] = []

    @property
    def variation_point(self) -> List["VariationPointProxy"]:
        """Get variationPoint (Pythonic accessor)."""
        return self._variationPoint

    def with_ar_typed_per(self, value):
        """
        Set ar_typed_per and return self for chaining.

        Args:
            value: The ar_typed_per to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ar_typed_per("value")
        """
        self.ar_typed_per = value  # Use property setter (gets validation)
        return self

    def with_bsw_per_instance(self, value):
        """
        Set bsw_per_instance and return self for chaining.

        Args:
            value: The bsw_per_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_per_instance("value")
        """
        self.bsw_per_instance = value  # Use property setter (gets validation)
        return self

    def with_client_policy(self, value):
        """
        Set client_policy and return self for chaining.

        Args:
            value: The client_policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_policy("value")
        """
        self.client_policy = value  # Use property setter (gets validation)
        return self

    def with_distinguished(self, value):
        """
        Set distinguished and return self for chaining.

        Args:
            value: The distinguished to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_distinguished("value")
        """
        self.distinguished = value  # Use property setter (gets validation)
        return self

    def with_entity(self, value):
        """
        Set entity and return self for chaining.

        Args:
            value: The entity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entity("value")
        """
        self.entity = value  # Use property setter (gets validation)
        return self

    def with_event(self, value):
        """
        Set event and return self for chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_included_data(self, value):
        """
        Set included_data and return self for chaining.

        Args:
            value: The included_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_included_data("value")
        """
        self.included_data = value  # Use property setter (gets validation)
        return self

    def with_included_mode(self, value):
        """
        Set included_mode and return self for chaining.

        Args:
            value: The included_mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_included_mode("value")
        """
        self.included_mode = value  # Use property setter (gets validation)
        return self

    def with_internal(self, value):
        """
        Set internal and return self for chaining.

        Args:
            value: The internal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal("value")
        """
        self.internal = value  # Use property setter (gets validation)
        return self

    def with_mode_receiver(self, value):
        """
        Set mode_receiver and return self for chaining.

        Args:
            value: The mode_receiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_receiver("value")
        """
        self.mode_receiver = value  # Use property setter (gets validation)
        return self

    def with_mode_sender(self, value):
        """
        Set mode_sender and return self for chaining.

        Args:
            value: The mode_sender to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_sender("value")
        """
        self.mode_sender = value  # Use property setter (gets validation)
        return self

    def with_parameter_policy(self, value):
        """
        Set parameter_policy and return self for chaining.

        Args:
            value: The parameter_policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter_policy("value")
        """
        self.parameter_policy = value  # Use property setter (gets validation)
        return self

    def with_per_instance(self, value):
        """
        Set per_instance and return self for chaining.

        Args:
            value: The per_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_per_instance("value")
        """
        self.per_instance = value  # Use property setter (gets validation)
        return self

    def with_reception_policy(self, value):
        """
        Set reception_policy and return self for chaining.

        Args:
            value: The reception_policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reception_policy("value")
        """
        self.reception_policy = value  # Use property setter (gets validation)
        return self

    def with_released_trigger(self, value):
        """
        Set released_trigger and return self for chaining.

        Args:
            value: The released_trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_released_trigger("value")
        """
        self.released_trigger = value  # Use property setter (gets validation)
        return self

    def with_send_policy(self, value):
        """
        Set send_policy and return self for chaining.

        Args:
            value: The send_policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_send_policy("value")
        """
        self.send_policy = value  # Use property setter (gets validation)
        return self

    def with_service(self, value):
        """
        Set service and return self for chaining.

        Args:
            value: The service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service("value")
        """
        self.service = value  # Use property setter (gets validation)
        return self

    def with_trigger_direct(self, value):
        """
        Set trigger_direct and return self for chaining.

        Args:
            value: The trigger_direct to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_direct("value")
        """
        self.trigger_direct = value  # Use property setter (gets validation)
        return self

    def with_variation_point(self, value):
        """
        Set variation_point and return self for chaining.

        Args:
            value: The variation_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variation_point("value")
        """
        self.variation_point = value  # Use property setter (gets validation)
        return self

    def with_accessed_mode(self, value):
        """
        Set accessed_mode and return self for chaining.

        Args:
            value: The accessed_mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accessed_mode("value")
        """
        self.accessed_mode = value  # Use property setter (gets validation)
        return self

    def with_activation_point(self, value):
        """
        Set activation_point and return self for chaining.

        Args:
            value: The activation_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_activation_point("value")
        """
        self.activation_point = value  # Use property setter (gets validation)
        return self

    def with_call_point(self, value):
        """
        Set call_point and return self for chaining.

        Args:
            value: The call_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_call_point("value")
        """
        self.call_point = value  # Use property setter (gets validation)
        return self

    def with_data_receive(self, value):
        """
        Set data_receive and return self for chaining.

        Args:
            value: The data_receive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_receive("value")
        """
        self.data_receive = value  # Use property setter (gets validation)
        return self

    def with_data_send_point(self, value):
        """
        Set data_send_point and return self for chaining.

        Args:
            value: The data_send_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_send_point("value")
        """
        self.data_send_point = value  # Use property setter (gets validation)
        return self

    def with_issued_trigger(self, value):
        """
        Set issued_trigger and return self for chaining.

        Args:
            value: The issued_trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_issued_trigger("value")
        """
        self.issued_trigger = value  # Use property setter (gets validation)
        return self

    def with_managed_mode(self, value):
        """
        Set managed_mode and return self for chaining.

        Args:
            value: The managed_mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_managed_mode("value")
        """
        self.managed_mode = value  # Use property setter (gets validation)
        return self

    def with_context(self, value):
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context(self, value):
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context(self, value):
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_disabled_in_mode_description_instance_ref(self, value):
        """
        Set disabled_in_mode_description_instance_ref and return self for chaining.

        Args:
            value: The disabled_in_mode_description_instance_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_disabled_in_mode_description_instance_ref("value")
        """
        self.disabled_in_mode_description_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_assigned_data(self, value):
        """
        Set assigned_data and return self for chaining.

        Args:
            value: The assigned_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_data("value")
        """
        self.assigned_data = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArTypedPer(self) -> List["RefType"]:
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

    def getEntity(self) -> List[BswModuleEntity]:
        """
        AUTOSAR-compliant getter for entity.

        Returns:
            The entity value

        Note:
            Delegates to entity property (CODING_RULE_V2_00017)
        """
        return self.entity  # Delegates to property

    def getEvent(self) -> List[BswEvent]:
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

    def getIncludedData(self) -> List["RefType"]:
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

    def getInternal(self) -> List["RefType"]:
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

    def getModeSender(self) -> List[BswModeSenderPolicy]:
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

    def getReleasedTrigger(self) -> List["RefType"]:
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

    def getTriggerDirect(self) -> List["RefType"]:
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



class BswModuleEntity(ExecutableEntity, ABC):
    """
    Specifies the smallest code fragment which can be described for a BSW module
    or cluster within AUTOSAR.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModuleEntity

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 70, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 215, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 429, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is BswModuleEntity:
            raise TypeError("BswModuleEntity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A mode group which is accessed via API call by this entity.
        # It shall be a ModeDeclarationGroupPrototype this module or cluster.
        # atpVariation.
        self._accessedMode: List["RefType"] = []

    @property
    def accessed_mode(self) -> List["RefType"]:
        """Get accessedMode (Pythonic accessor)."""
        return self._accessedMode
        # Activation point used by the module entity to activate one more internal
                # triggers.
        # atpVariation.
        self._activationPoint: List["RefType"] = []

    @property
    def activation_point(self) -> List["RefType"]:
        """Get activationPoint (Pythonic accessor)."""
        return self._activationPoint
        # A call point used in the code of this entity.
        # of this association is especially targeted at It is possible to have one
                # variant calling AUTOSAR debug module and another one which atpVariation.
        self._callPoint: List[BswModuleCallPoint] = []

    @property
    def call_point(self) -> List[BswModuleCallPoint]:
        """Get callPoint (Pythonic accessor)."""
        return self._callPoint
        # The data is received via the BSW Scheduler.
        # atpSplitable; atpVariation.
        self._dataReceive: List[BswVariableAccess] = []

    @property
    def data_receive(self) -> List[BswVariableAccess]:
        """Get dataReceive (Pythonic accessor)."""
        return self._dataReceive
        # The data is sent via the BSW Scheduler.
        # atpVariation.
        self._dataSendPoint: List[BswVariableAccess] = []

    @property
    def data_send_point(self) -> List[BswVariableAccess]:
        """Get dataSendPoint (Pythonic accessor)."""
        return self._dataSendPoint
        # The entry which is implemented by this module entity.
        self._implemented: Optional["BswModuleEntry"] = None

    @property
    def implemented(self) -> Optional["BswModuleEntry"]:
        """Get implemented (Pythonic accessor)."""
        return self._implemented

    @implemented.setter
    def implemented(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set implemented with validation.

        Args:
            value: The implemented to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implemented = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"implemented must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._implemented = value
        # be a BswTrigger released (i.
        # e.
        # owned) by this cluster.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._issuedTrigger: List["RefType"] = []

    @property
    def issued_trigger(self) -> List["RefType"]:
        """Get issuedTrigger (Pythonic accessor)."""
        return self._issuedTrigger
        # A mode group which is managed by this entity.
        # It shall be a ModeDeclarationGroupPrototype provided by this cluster.
        # atpVariation.
        self._managedMode: List["RefType"] = []

    @property
    def managed_mode(self) -> List["RefType"]:
        """Get managedMode (Pythonic accessor)."""
        return self._managedMode
        # A prefix to be used in generated names for the Bsw ModuleScheduler in the
                # context of this BswModuleEntity, entry point prototypes, macros for dealing
                # areas, header file names.
        # defined in the SWS RTE.
        # supersedes default rules for the prefix of those.
        self._schedulerName: Optional["BswSchedulerName"] = None

    @property
    def scheduler_name(self) -> Optional["BswSchedulerName"]:
        """Get schedulerName (Pythonic accessor)."""
        return self._schedulerName

    @scheduler_name.setter
    def scheduler_name(self, value: Optional["BswSchedulerName"]) -> None:
        """
        Set schedulerName with validation.

        Args:
            value: The schedulerName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._schedulerName = None
            return

        if not isinstance(value, BswSchedulerName):
            raise TypeError(
                f"schedulerName must be BswSchedulerName or None, got {type(value).__name__}"
            )
        self._schedulerName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedMode(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for accessedMode.

        Returns:
            The accessedMode value

        Note:
            Delegates to accessed_mode property (CODING_RULE_V2_00017)
        """
        return self.accessed_mode  # Delegates to property

    def getActivationPoint(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for activationPoint.

        Returns:
            The activationPoint value

        Note:
            Delegates to activation_point property (CODING_RULE_V2_00017)
        """
        return self.activation_point  # Delegates to property

    def getCallPoint(self) -> List[BswModuleCallPoint]:
        """
        AUTOSAR-compliant getter for callPoint.

        Returns:
            The callPoint value

        Note:
            Delegates to call_point property (CODING_RULE_V2_00017)
        """
        return self.call_point  # Delegates to property

    def getDataReceive(self) -> List[BswVariableAccess]:
        """
        AUTOSAR-compliant getter for dataReceive.

        Returns:
            The dataReceive value

        Note:
            Delegates to data_receive property (CODING_RULE_V2_00017)
        """
        return self.data_receive  # Delegates to property

    def getDataSendPoint(self) -> List[BswVariableAccess]:
        """
        AUTOSAR-compliant getter for dataSendPoint.

        Returns:
            The dataSendPoint value

        Note:
            Delegates to data_send_point property (CODING_RULE_V2_00017)
        """
        return self.data_send_point  # Delegates to property

    def getImplemented(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for implemented.

        Returns:
            The implemented value

        Note:
            Delegates to implemented property (CODING_RULE_V2_00017)
        """
        return self.implemented  # Delegates to property

    def setImplemented(self, value: "BswModuleEntry") -> BswModuleEntity:
        """
        AUTOSAR-compliant setter for implemented with method chaining.

        Args:
            value: The implemented to set

        Returns:
            self for method chaining

        Note:
            Delegates to implemented property setter (gets validation automatically)
        """
        self.implemented = value  # Delegates to property setter
        return self

    def getIssuedTrigger(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for issuedTrigger.

        Returns:
            The issuedTrigger value

        Note:
            Delegates to issued_trigger property (CODING_RULE_V2_00017)
        """
        return self.issued_trigger  # Delegates to property

    def getManagedMode(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for managedMode.

        Returns:
            The managedMode value

        Note:
            Delegates to managed_mode property (CODING_RULE_V2_00017)
        """
        return self.managed_mode  # Delegates to property

    def getSchedulerName(self) -> "BswSchedulerName":
        """
        AUTOSAR-compliant getter for schedulerName.

        Returns:
            The schedulerName value

        Note:
            Delegates to scheduler_name property (CODING_RULE_V2_00017)
        """
        return self.scheduler_name  # Delegates to property

    def setSchedulerName(self, value: "BswSchedulerName") -> BswModuleEntity:
        """
        AUTOSAR-compliant setter for schedulerName with method chaining.

        Args:
            value: The schedulerName to set

        Returns:
            self for method chaining

        Note:
            Delegates to scheduler_name property setter (gets validation automatically)
        """
        self.scheduler_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implemented(self, value: Optional["BswModuleEntry"]) -> BswModuleEntity:
        """
        Set implemented and return self for chaining.

        Args:
            value: The implemented to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implemented("value")
        """
        self.implemented = value  # Use property setter (gets validation)
        return self

    def with_scheduler_name(self, value: Optional["BswSchedulerName"]) -> BswModuleEntity:
        """
        Set schedulerName and return self for chaining.

        Args:
            value: The schedulerName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scheduler_name("value")
        """
        self.scheduler_name = value  # Use property setter (gets validation)
        return self



class BswModuleCallPoint(Referrable, ABC):
    """
    Represents a point at which a BswModuleEntity handles a procedure call into
    a BswModuleEntry, either directly or via the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModuleCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 77, Classic
      Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswModuleCallPoint:
            raise TypeError("BswModuleCallPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The existence of this reference indicates that the call point is used only in
        # the context of the referred Bsw.
        self._context: List["BswDistinguished"] = []

    @property
    def context(self) -> List["BswDistinguished"]:
        """Get context (Pythonic accessor)."""
        return self._context

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> List["BswDistinguished"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswVariableAccess(Referrable):
    """
    The presence of a BswVariableAccess implies that a BswModuleEntity needs
    access to a VariableData Prototype via the BSW Scheduler. The kind of access
    is specified by the role in which the class is used.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswVariableAccess

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 81, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The data accessed via the BSW Scheduler.
        self._accessedVariable: Optional["RefType"] = None

    @property
    def accessed_variable(self) -> Optional["RefType"]:
        """Get accessedVariable (Pythonic accessor)."""
        return self._accessedVariable

    @accessed_variable.setter
    def accessed_variable(self, value: Optional["RefType"]) -> None:
        """
        Set accessedVariable with validation.

        Args:
            value: The accessedVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessedVariable = None
            return

        self._accessedVariable = value
        # sent only in the context of the referred.
        self._context: List["BswDistinguished"] = []

    @property
    def context(self) -> List["BswDistinguished"]:
        """Get context (Pythonic accessor)."""
        return self._context

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedVariable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for accessedVariable.

        Returns:
            The accessedVariable value

        Note:
            Delegates to accessed_variable property (CODING_RULE_V2_00017)
        """
        return self.accessed_variable  # Delegates to property

    def setAccessedVariable(self, value: "RefType") -> BswVariableAccess:
        """
        AUTOSAR-compliant setter for accessedVariable with method chaining.

        Args:
            value: The accessedVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to accessed_variable property setter (gets validation automatically)
        """
        self.accessed_variable = value  # Delegates to property setter
        return self

    def getContext(self) -> List["BswDistinguished"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accessed_variable(self, value: Optional[RefType]) -> BswVariableAccess:
        """
        Set accessedVariable and return self for chaining.

        Args:
            value: The accessedVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accessed_variable("value")
        """
        self.accessed_variable = value  # Use property setter (gets validation)
        return self



class BswExclusiveAreaPolicy(ARObject):
    """
    The ExclusiveArea for which the BSW Scheduler using this policy.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswExclusiveAreaPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 82, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies for this ExclusiveArea if either one common set and Exit APIs for
                # the whole BSW module is the SchM or if the set of Enter and Exit expected per
                # BswModuleEntity.
        # The default value.
        self._apiPrinciple: Optional["ApiPrincipleEnum"] = None

    @property
    def api_principle(self) -> Optional["ApiPrincipleEnum"]:
        """Get apiPrinciple (Pythonic accessor)."""
        return self._apiPrinciple

    @api_principle.setter
    def api_principle(self, value: Optional["ApiPrincipleEnum"]) -> None:
        """
        Set apiPrinciple with validation.

        Args:
            value: The apiPrinciple to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._apiPrinciple = None
            return

        if not isinstance(value, ApiPrincipleEnum):
            raise TypeError(
                f"apiPrinciple must be ApiPrincipleEnum or None, got {type(value).__name__}"
            )
        self._apiPrinciple = value
        self._exclusiveArea: Optional["ExclusiveArea"] = None

    @property
    def exclusive_area(self) -> Optional["ExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea

    @exclusive_area.setter
    def exclusive_area(self, value: Optional["ExclusiveArea"]) -> None:
        """
        Set exclusiveArea with validation.

        Args:
            value: The exclusiveArea to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exclusiveArea = None
            return

        if not isinstance(value, ExclusiveArea):
            raise TypeError(
                f"exclusiveArea must be ExclusiveArea or None, got {type(value).__name__}"
            )
        self._exclusiveArea = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApiPrinciple(self) -> "ApiPrincipleEnum":
        """
        AUTOSAR-compliant getter for apiPrinciple.

        Returns:
            The apiPrinciple value

        Note:
            Delegates to api_principle property (CODING_RULE_V2_00017)
        """
        return self.api_principle  # Delegates to property

    def setApiPrinciple(self, value: "ApiPrincipleEnum") -> BswExclusiveAreaPolicy:
        """
        AUTOSAR-compliant setter for apiPrinciple with method chaining.

        Args:
            value: The apiPrinciple to set

        Returns:
            self for method chaining

        Note:
            Delegates to api_principle property setter (gets validation automatically)
        """
        self.api_principle = value  # Delegates to property setter
        return self

    def getExclusiveArea(self) -> "ExclusiveArea":
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def setExclusiveArea(self, value: "ExclusiveArea") -> BswExclusiveAreaPolicy:
        """
        AUTOSAR-compliant setter for exclusiveArea with method chaining.

        Args:
            value: The exclusiveArea to set

        Returns:
            self for method chaining

        Note:
            Delegates to exclusive_area property setter (gets validation automatically)
        """
        self.exclusive_area = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_api_principle(self, value: Optional["ApiPrincipleEnum"]) -> BswExclusiveAreaPolicy:
        """
        Set apiPrinciple and return self for chaining.

        Args:
            value: The apiPrinciple to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_api_principle("value")
        """
        self.api_principle = value  # Use property setter (gets validation)
        return self

    def with_exclusive_area(self, value: Optional["ExclusiveArea"]) -> BswExclusiveAreaPolicy:
        """
        Set exclusiveArea and return self for chaining.

        Args:
            value: The exclusiveArea to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exclusive_area("value")
        """
        self.exclusive_area = value  # Use property setter (gets validation)
        return self



class BswSchedulerNamePrefix(ImplementationProps):
    """
    A prefix to be used in names of generated code artifacts which make up the
    interface of a BSW module to the BswScheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswSchedulerNamePrefix

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 86, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswEvent(AbstractEvent, ABC):
    """
    Base class of various kinds of events which are used to trigger a
    BswModuleEntity of this BSW module or cluster. The event is local to the BSW
    module or cluster. The short name of the meta-class instance is intended as
    an input to configure the required API of the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 87, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 206, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswEvent:
            raise TypeError("BswEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The existence of this reference indicates that the usage of the event is
        # limited to the context of the referred Bsw.
        self._context: List["BswDistinguished"] = []

    @property
    def context(self) -> List["BswDistinguished"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # by: ModeInBswModule.
        self._disabledInModeDescriptionInstanceRef: List["ModeDeclaration"] = []

    @property
    def disabled_in_mode_description_instance_ref(self) -> List["ModeDeclaration"]:
        """Get disabledInModeDescriptionInstanceRef (Pythonic accessor)."""
        return self._disabledInModeDescriptionInstanceRef
        # The entity which is started by the event.
        self._startsOnEvent: Optional[BswModuleEntity] = None

    @property
    def starts_on_event(self) -> Optional[BswModuleEntity]:
        """Get startsOnEvent (Pythonic accessor)."""
        return self._startsOnEvent

    @starts_on_event.setter
    def starts_on_event(self, value: Optional[BswModuleEntity]) -> None:
        """
        Set startsOnEvent with validation.

        Args:
            value: The startsOnEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startsOnEvent = None
            return

        if not isinstance(value, BswModuleEntity):
            raise TypeError(
                f"startsOnEvent must be BswModuleEntity or None, got {type(value).__name__}"
            )
        self._startsOnEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> List["BswDistinguished"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getDisabledInModeDescriptionInstanceRef(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for disabledInModeDescriptionInstanceRef.

        Returns:
            The disabledInModeDescriptionInstanceRef value

        Note:
            Delegates to disabled_in_mode_description_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.disabled_in_mode_description_instance_ref  # Delegates to property

    def getStartsOnEvent(self) -> BswModuleEntity:
        """
        AUTOSAR-compliant getter for startsOnEvent.

        Returns:
            The startsOnEvent value

        Note:
            Delegates to starts_on_event property (CODING_RULE_V2_00017)
        """
        return self.starts_on_event  # Delegates to property

    def setStartsOnEvent(self, value: BswModuleEntity) -> BswEvent:
        """
        AUTOSAR-compliant setter for startsOnEvent with method chaining.

        Args:
            value: The startsOnEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to starts_on_event property setter (gets validation automatically)
        """
        self.starts_on_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_starts_on_event(self, value: Optional[BswModuleEntity]) -> BswEvent:
        """
        Set startsOnEvent and return self for chaining.

        Args:
            value: The startsOnEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_starts_on_event("value")
        """
        self.starts_on_event = value  # Use property setter (gets validation)
        return self



class BswInternalTriggeringPoint(Identifiable):
    """
    Represents the activation point for one or more
    BswInternalTriggerOccurredEvents.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInternalTriggeringPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 91, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute, when set to value queued, specifies a of the internal trigger
        # event.
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

    def setSwImplPolicy(self, value: "SwImplPolicyEnum") -> BswInternalTriggeringPoint:
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

    def with_sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> BswInternalTriggeringPoint:
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



class BswTriggerDirectImplementation(ARObject):
    """
    Specifies a released trigger to be directly implemented via OS calls, for
    example in a Complex Driver module.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswTriggerDirectImplementation

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 102, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The name of the OS category 2 ISR, which is controlled referred trigger.
        # This means, that the module category 2 ISR (e.
        # g.
        # according hardware enabling of ISR).
        # Instead of calling an SchM API to raise the appropriate events in modules
                # receiving the trigger, this ISR the triggered ExecutableEntitys.
        # The is required by the integrator to map the Bsw RTEEvents to this ISR.
        self._cat2Isr: Optional["Identifier"] = None

    @property
    def cat2_isr(self) -> Optional["Identifier"]:
        """Get cat2Isr (Pythonic accessor)."""
        return self._cat2Isr

    @cat2_isr.setter
    def cat2_isr(self, value: Optional["Identifier"]) -> None:
        """
        Set cat2Isr with validation.

        Args:
            value: The cat2Isr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cat2Isr = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"cat2Isr must be Identifier or str or None, got {type(value).__name__}"
            )
        self._cat2Isr = value
        # The trigger which is directly mastered by this module.
        # be several different BswTriggerDirect the same Trigger.
        # This may e.
        # g.
        # due to memory partitioning.
        self._masteredTrigger: Optional["RefType"] = None

    @property
    def mastered_trigger(self) -> Optional["RefType"]:
        """Get masteredTrigger (Pythonic accessor)."""
        return self._masteredTrigger

    @mastered_trigger.setter
    def mastered_trigger(self, value: Optional["RefType"]) -> None:
        """
        Set masteredTrigger with validation.

        Args:
            value: The masteredTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._masteredTrigger = None
            return

        self._masteredTrigger = value
                # module uses the to directly activate an OS task instead of API of the
                # BswScheduler.
        # The task name is the RTE generator resp.
        # BswScheduler to appropriate events in components or modules trigger.
        self._task: Optional["Identifier"] = None

    @property
    def task(self) -> Optional["Identifier"]:
        """Get task (Pythonic accessor)."""
        return self._task

    @task.setter
    def task(self, value: Optional["Identifier"]) -> None:
        """
        Set task with validation.

        Args:
            value: The task to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._task = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"task must be Identifier or str or None, got {type(value).__name__}"
            )
        self._task = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCat2Isr(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for cat2Isr.

        Returns:
            The cat2Isr value

        Note:
            Delegates to cat2_isr property (CODING_RULE_V2_00017)
        """
        return self.cat2_isr  # Delegates to property

    def setCat2Isr(self, value: "Identifier") -> BswTriggerDirectImplementation:
        """
        AUTOSAR-compliant setter for cat2Isr with method chaining.

        Args:
            value: The cat2Isr to set

        Returns:
            self for method chaining

        Note:
            Delegates to cat2_isr property setter (gets validation automatically)
        """
        self.cat2_isr = value  # Delegates to property setter
        return self

    def getMasteredTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for masteredTrigger.

        Returns:
            The masteredTrigger value

        Note:
            Delegates to mastered_trigger property (CODING_RULE_V2_00017)
        """
        return self.mastered_trigger  # Delegates to property

    def setMasteredTrigger(self, value: "RefType") -> BswTriggerDirectImplementation:
        """
        AUTOSAR-compliant setter for masteredTrigger with method chaining.

        Args:
            value: The masteredTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to mastered_trigger property setter (gets validation automatically)
        """
        self.mastered_trigger = value  # Delegates to property setter
        return self

    def getTask(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for task.

        Returns:
            The task value

        Note:
            Delegates to task property (CODING_RULE_V2_00017)
        """
        return self.task  # Delegates to property

    def setTask(self, value: "Identifier") -> BswTriggerDirectImplementation:
        """
        AUTOSAR-compliant setter for task with method chaining.

        Args:
            value: The task to set

        Returns:
            self for method chaining

        Note:
            Delegates to task property setter (gets validation automatically)
        """
        self.task = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cat2_isr(self, value: Optional["Identifier"]) -> BswTriggerDirectImplementation:
        """
        Set cat2Isr and return self for chaining.

        Args:
            value: The cat2Isr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cat2_isr("value")
        """
        self.cat2_isr = value  # Use property setter (gets validation)
        return self

    def with_mastered_trigger(self, value: Optional[RefType]) -> BswTriggerDirectImplementation:
        """
        Set masteredTrigger and return self for chaining.

        Args:
            value: The masteredTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mastered_trigger("value")
        """
        self.mastered_trigger = value  # Use property setter (gets validation)
        return self

    def with_task(self, value: Optional["Identifier"]) -> BswTriggerDirectImplementation:
        """
        Set task and return self for chaining.

        Args:
            value: The task to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_task("value")
        """
        self.task = value  # Use property setter (gets validation)
        return self



class BswModeSenderPolicy(ARObject):
    """
    Specifies the details for the sending of a mode switch for the referred mode
    group.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeSenderPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 102, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Request for acknowledgement.
        self._ackRequestRequest: Optional["BswModeSwitchAck"] = None

    @property
    def ack_request_request(self) -> Optional["BswModeSwitchAck"]:
        """Get ackRequestRequest (Pythonic accessor)."""
        return self._ackRequestRequest

    @ack_request_request.setter
    def ack_request_request(self, value: Optional["BswModeSwitchAck"]) -> None:
        """
        Set ackRequestRequest with validation.

        Args:
            value: The ackRequestRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ackRequestRequest = None
            return

        if not isinstance(value, BswModeSwitchAck):
            raise TypeError(
                f"ackRequestRequest must be BswModeSwitchAck or None, got {type(value).__name__}"
            )
        self._ackRequestRequest = value
                # the previous mode and the next set to TRUE the enhanced mode API is be
                # generated.
        # For more details please refer SWS_RTE.
        self._enhancedMode: Optional["Boolean"] = None

    @property
    def enhanced_mode(self) -> Optional["Boolean"]:
        """Get enhancedMode (Pythonic accessor)."""
        return self._enhancedMode

    @enhanced_mode.setter
    def enhanced_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set enhancedMode with validation.

        Args:
            value: The enhancedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enhancedMode = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enhancedMode must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enhancedMode = value
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._providedMode: Optional["RefType"] = None

    @property
    def provided_mode(self) -> Optional["RefType"]:
        """Get providedMode (Pythonic accessor)."""
        return self._providedMode

    @provided_mode.setter
    def provided_mode(self, value: Optional["RefType"]) -> None:
        """
        Set providedMode with validation.

        Args:
            value: The providedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedMode = None
            return

        self._providedMode = value
        # The queue is the RTE resp.
        # BswScheduler.
        # The value greater or equal to 0.
        # Setting the value of queue 0 implies non-queued communication.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"queueLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAckRequestRequest(self) -> "BswModeSwitchAck":
        """
        AUTOSAR-compliant getter for ackRequestRequest.

        Returns:
            The ackRequestRequest value

        Note:
            Delegates to ack_request_request property (CODING_RULE_V2_00017)
        """
        return self.ack_request_request  # Delegates to property

    def setAckRequestRequest(self, value: "BswModeSwitchAck") -> BswModeSenderPolicy:
        """
        AUTOSAR-compliant setter for ackRequestRequest with method chaining.

        Args:
            value: The ackRequestRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to ack_request_request property setter (gets validation automatically)
        """
        self.ack_request_request = value  # Delegates to property setter
        return self

    def getEnhancedMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enhancedMode.

        Returns:
            The enhancedMode value

        Note:
            Delegates to enhanced_mode property (CODING_RULE_V2_00017)
        """
        return self.enhanced_mode  # Delegates to property

    def setEnhancedMode(self, value: "Boolean") -> BswModeSenderPolicy:
        """
        AUTOSAR-compliant setter for enhancedMode with method chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to enhanced_mode property setter (gets validation automatically)
        """
        self.enhanced_mode = value  # Delegates to property setter
        return self

    def getProvidedMode(self) -> "RefType":
        """
        AUTOSAR-compliant getter for providedMode.

        Returns:
            The providedMode value

        Note:
            Delegates to provided_mode property (CODING_RULE_V2_00017)
        """
        return self.provided_mode  # Delegates to property

    def setProvidedMode(self, value: "RefType") -> BswModeSenderPolicy:
        """
        AUTOSAR-compliant setter for providedMode with method chaining.

        Args:
            value: The providedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to provided_mode property setter (gets validation automatically)
        """
        self.provided_mode = value  # Delegates to property setter
        return self

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> BswModeSenderPolicy:
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ack_request_request(self, value: Optional["BswModeSwitchAck"]) -> BswModeSenderPolicy:
        """
        Set ackRequestRequest and return self for chaining.

        Args:
            value: The ackRequestRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ack_request_request("value")
        """
        self.ack_request_request = value  # Use property setter (gets validation)
        return self

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> BswModeSenderPolicy:
        """
        Set enhancedMode and return self for chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enhanced_mode("value")
        """
        self.enhanced_mode = value  # Use property setter (gets validation)
        return self

    def with_provided_mode(self, value: Optional[RefType]) -> BswModeSenderPolicy:
        """
        Set providedMode and return self for chaining.

        Args:
            value: The providedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_mode("value")
        """
        self.provided_mode = value  # Use property setter (gets validation)
        return self

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> BswModeSenderPolicy:
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self



class BswModeSwitchAckRequest(ARObject):
    """
    Requests acknowledgements that a mode switch has been processed successfully

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeSwitchAckRequest

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 103, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Number of seconds before an error is reported.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> BswModeSwitchAckRequest:
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timeout(self, value: Optional["TimeValue"]) -> BswModeSwitchAckRequest:
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self



class BswModeReceiverPolicy(ARObject):
    """
    Specifies the details for the reception of a mode switch for the referred
    mode group.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeReceiverPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 103, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This controls the creation of the enhanced mode API that information about
                # the previous mode and the next set to TRUE the enhanced mode API is be
                # generated.
        # For more details please refer SWS_RTE.
        self._enhancedMode: Optional["Boolean"] = None

    @property
    def enhanced_mode(self) -> Optional["Boolean"]:
        """Get enhancedMode (Pythonic accessor)."""
        return self._enhancedMode

    @enhanced_mode.setter
    def enhanced_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set enhancedMode with validation.

        Args:
            value: The enhancedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enhancedMode = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enhancedMode must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enhancedMode = value
        self._requiredMode: Optional["RefType"] = None

    @property
    def required_mode(self) -> Optional["RefType"]:
        """Get requiredMode (Pythonic accessor)."""
        return self._requiredMode

    @required_mode.setter
    def required_mode(self, value: Optional["RefType"]) -> None:
        """
        Set requiredMode with validation.

        Args:
            value: The requiredMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiredMode = None
            return

        self._requiredMode = value
        # switch (true) or not (false).
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"supports must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._supports = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnhancedMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enhancedMode.

        Returns:
            The enhancedMode value

        Note:
            Delegates to enhanced_mode property (CODING_RULE_V2_00017)
        """
        return self.enhanced_mode  # Delegates to property

    def setEnhancedMode(self, value: "Boolean") -> BswModeReceiverPolicy:
        """
        AUTOSAR-compliant setter for enhancedMode with method chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to enhanced_mode property setter (gets validation automatically)
        """
        self.enhanced_mode = value  # Delegates to property setter
        return self

    def getRequiredMode(self) -> "RefType":
        """
        AUTOSAR-compliant getter for requiredMode.

        Returns:
            The requiredMode value

        Note:
            Delegates to required_mode property (CODING_RULE_V2_00017)
        """
        return self.required_mode  # Delegates to property

    def setRequiredMode(self, value: "RefType") -> BswModeReceiverPolicy:
        """
        AUTOSAR-compliant setter for requiredMode with method chaining.

        Args:
            value: The requiredMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to required_mode property setter (gets validation automatically)
        """
        self.required_mode = value  # Delegates to property setter
        return self

    def getSupports(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for supports.

        Returns:
            The supports value

        Note:
            Delegates to supports property (CODING_RULE_V2_00017)
        """
        return self.supports  # Delegates to property

    def setSupports(self, value: "Boolean") -> BswModeReceiverPolicy:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> BswModeReceiverPolicy:
        """
        Set enhancedMode and return self for chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enhanced_mode("value")
        """
        self.enhanced_mode = value  # Use property setter (gets validation)
        return self

    def with_required_mode(self, value: Optional[RefType]) -> BswModeReceiverPolicy:
        """
        Set requiredMode and return self for chaining.

        Args:
            value: The requiredMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_mode("value")
        """
        self.required_mode = value  # Use property setter (gets validation)
        return self

    def with_supports(self, value: Optional["Boolean"]) -> BswModeReceiverPolicy:
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



class BswDataReceptionPolicy(ARObject, ABC):
    """
    Specifies the reception policy for the referred data in sender-receiver
    communication over the BSW Scheduler. To be used for inter-partition and/or
    inter-core communication.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswDataReceptionPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 104, Classic
      Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswDataReceptionPolicy:
            raise TypeError("BswDataReceptionPolicy is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The data received over the BSW Scheduler using this.
        self._receivedData: Optional["RefType"] = None

    @property
    def received_data(self) -> Optional["RefType"]:
        """Get receivedData (Pythonic accessor)."""
        return self._receivedData

    @received_data.setter
    def received_data(self, value: Optional["RefType"]) -> None:
        """
        Set receivedData with validation.

        Args:
            value: The receivedData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._receivedData = None
            return

        self._receivedData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReceivedData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for receivedData.

        Returns:
            The receivedData value

        Note:
            Delegates to received_data property (CODING_RULE_V2_00017)
        """
        return self.received_data  # Delegates to property

    def setReceivedData(self, value: "RefType") -> BswDataReceptionPolicy:
        """
        AUTOSAR-compliant setter for receivedData with method chaining.

        Args:
            value: The receivedData to set

        Returns:
            self for method chaining

        Note:
            Delegates to received_data property setter (gets validation automatically)
        """
        self.received_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_received_data(self, value: Optional[RefType]) -> BswDataReceptionPolicy:
        """
        Set receivedData and return self for chaining.

        Args:
            value: The receivedData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_received_data("value")
        """
        self.received_data = value  # Use property setter (gets validation)
        return self



class BswDistinguishedPartition(Referrable):
    """
    Each instance of this meta-class represents an abstract partition in which
    context the code of the enclosing BswModuleBehavior can be executed. The
    intended use case is to distinguish between several partitions in order to
    implement different behavior per partition, for example to behave either as
    a master or satellite in a multicore ECU with shared BSW code.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswDistinguishedPartition

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 118, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswServiceDependency(ServiceDependency):
    """
    Specialization of ServiceDependency in the context of an
    BswInternalBehavior. It allows to associate BswModuleEntries and data
    defined for a BSW module or cluster to a given ServiceNeeds element.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswServiceDependency

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 225, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 225, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 978, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the role of an associated data object (owned by module or cluster) in
        # the context of the ServiceNeeds atpVariation.
        self._assignedData: List["RoleBasedData"] = []

    @property
    def assigned_data(self) -> List["RoleBasedData"]:
        """Get assignedData (Pythonic accessor)."""
        return self._assignedData
        # Defines the role of an associated BswModuleEntry in the context of the
                # ServiceNeeds element.
        # atpVariation.
        self._assignedEntry: List["RoleBasedBswModule"] = []

    @property
    def assigned_entry(self) -> List["RoleBasedBswModule"]:
        """Get assignedEntry (Pythonic accessor)."""
        return self._assignedEntry
        # This adds the ability to become referrable to BswService.
        self._ident: Optional["BswService"] = None

    @property
    def ident(self) -> Optional["BswService"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["BswService"]) -> None:
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

        if not isinstance(value, BswService):
            raise TypeError(
                f"ident must be BswService or None, got {type(value).__name__}"
            )
        self._ident = value
        self._serviceNeeds: Optional["ServiceNeeds"] = None

    @property
    def service_needs(self) -> Optional["ServiceNeeds"]:
        """Get serviceNeeds (Pythonic accessor)."""
        return self._serviceNeeds

    @service_needs.setter
    def service_needs(self, value: Optional["ServiceNeeds"]) -> None:
        """
        Set serviceNeeds with validation.

        Args:
            value: The serviceNeeds to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceNeeds = None
            return

        if not isinstance(value, ServiceNeeds):
            raise TypeError(
                f"serviceNeeds must be ServiceNeeds or None, got {type(value).__name__}"
            )
        self._serviceNeeds = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedData(self) -> List["RoleBasedData"]:
        """
        AUTOSAR-compliant getter for assignedData.

        Returns:
            The assignedData value

        Note:
            Delegates to assigned_data property (CODING_RULE_V2_00017)
        """
        return self.assigned_data  # Delegates to property

    def getAssignedEntry(self) -> List["RoleBasedBswModule"]:
        """
        AUTOSAR-compliant getter for assignedEntry.

        Returns:
            The assignedEntry value

        Note:
            Delegates to assigned_entry property (CODING_RULE_V2_00017)
        """
        return self.assigned_entry  # Delegates to property

    def getIdent(self) -> "BswService":
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "BswService") -> BswServiceDependency:
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

    def getServiceNeeds(self) -> "ServiceNeeds":
        """
        AUTOSAR-compliant getter for serviceNeeds.

        Returns:
            The serviceNeeds value

        Note:
            Delegates to service_needs property (CODING_RULE_V2_00017)
        """
        return self.service_needs  # Delegates to property

    def setServiceNeeds(self, value: "ServiceNeeds") -> BswServiceDependency:
        """
        AUTOSAR-compliant setter for serviceNeeds with method chaining.

        Args:
            value: The serviceNeeds to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_needs property setter (gets validation automatically)
        """
        self.service_needs = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional["BswService"]) -> BswServiceDependency:
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

    def with_service_needs(self, value: Optional["ServiceNeeds"]) -> BswServiceDependency:
        """
        Set serviceNeeds and return self for chaining.

        Args:
            value: The serviceNeeds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_needs("value")
        """
        self.service_needs = value  # Use property setter (gets validation)
        return self



class RoleBasedBswModuleEntryAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular BswModuleEntry
    (usually a configurable callback). With this assignment, the role of the
    callback is mapped to a specific ServiceNeeds element, so that a tool is
    able to create appropriate configuration values for the module that
    implements the AUTOSAR Service.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::RoleBasedBswModuleEntryAssignment

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 226, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The assigned entry.
        # It should be an implementedEntry or the module or cluster that requires the.
        self._assignedEntry: Optional["BswModuleEntry"] = None

    @property
    def assigned_entry(self) -> Optional["BswModuleEntry"]:
        """Get assignedEntry (Pythonic accessor)."""
        return self._assignedEntry

    @assigned_entry.setter
    def assigned_entry(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set assignedEntry with validation.

        Args:
            value: The assignedEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedEntry = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"assignedEntry must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._assignedEntry = value
                # required (for example) kind of callbacks may be associated same ServiceNeeds
                # (e.
        # g.
        # end-notification vs.
        # shall be the role name of a configurable (usually a callback) as standardized
                # in the of the related AUTOSAR Service.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedEntry(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for assignedEntry.

        Returns:
            The assignedEntry value

        Note:
            Delegates to assigned_entry property (CODING_RULE_V2_00017)
        """
        return self.assigned_entry  # Delegates to property

    def setAssignedEntry(self, value: "BswModuleEntry") -> RoleBasedBswModuleEntryAssignment:
        """
        AUTOSAR-compliant setter for assignedEntry with method chaining.

        Args:
            value: The assignedEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_entry property setter (gets validation automatically)
        """
        self.assigned_entry = value  # Delegates to property setter
        return self

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> RoleBasedBswModuleEntryAssignment:
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned_entry(self, value: Optional["BswModuleEntry"]) -> RoleBasedBswModuleEntryAssignment:
        """
        Set assignedEntry and return self for chaining.

        Args:
            value: The assignedEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_entry("value")
        """
        self.assigned_entry = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["Identifier"]) -> RoleBasedBswModuleEntryAssignment:
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self



class BswCalledEntity(BswModuleEntity):
    """
    BSW module entity which is designed to be called from another BSW module or
    cluster.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswCalledEntity

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 74, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 972, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswSchedulableEntity(BswModuleEntity):
    """
    BSW module entity, which is designed for control by the BSW Scheduler. It
    may for example implement a so-called "main" function.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswSchedulableEntity

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 75, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 978, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswInterruptEntity(BswModuleEntity):
    """
    BSW module entity, which is designed to be triggered by an interrupt.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInterruptEntity

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 75, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 212, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Category of the interrupt.
        self._interruptCategory: Optional[BswInterruptCategory] = None

    @property
    def interrupt_category(self) -> Optional[BswInterruptCategory]:
        """Get interruptCategory (Pythonic accessor)."""
        return self._interruptCategory

    @interrupt_category.setter
    def interrupt_category(self, value: Optional[BswInterruptCategory]) -> None:
        """
        Set interruptCategory with validation.

        Args:
            value: The interruptCategory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interruptCategory = None
            return

        if not isinstance(value, BswInterruptCategory):
            raise TypeError(
                f"interruptCategory must be BswInterruptCategory or None, got {type(value).__name__}"
            )
        self._interruptCategory = value
        self._interruptSource: Optional["String"] = None

    @property
    def interrupt_source(self) -> Optional["String"]:
        """Get interruptSource (Pythonic accessor)."""
        return self._interruptSource

    @interrupt_source.setter
    def interrupt_source(self, value: Optional["String"]) -> None:
        """
        Set interruptSource with validation.

        Args:
            value: The interruptSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interruptSource = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"interruptSource must be String or str or None, got {type(value).__name__}"
            )
        self._interruptSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInterruptCategory(self) -> BswInterruptCategory:
        """
        AUTOSAR-compliant getter for interruptCategory.

        Returns:
            The interruptCategory value

        Note:
            Delegates to interrupt_category property (CODING_RULE_V2_00017)
        """
        return self.interrupt_category  # Delegates to property

    def setInterruptCategory(self, value: BswInterruptCategory) -> BswInterruptEntity:
        """
        AUTOSAR-compliant setter for interruptCategory with method chaining.

        Args:
            value: The interruptCategory to set

        Returns:
            self for method chaining

        Note:
            Delegates to interrupt_category property setter (gets validation automatically)
        """
        self.interrupt_category = value  # Delegates to property setter
        return self

    def getInterruptSource(self) -> "String":
        """
        AUTOSAR-compliant getter for interruptSource.

        Returns:
            The interruptSource value

        Note:
            Delegates to interrupt_source property (CODING_RULE_V2_00017)
        """
        return self.interrupt_source  # Delegates to property

    def setInterruptSource(self, value: "String") -> BswInterruptEntity:
        """
        AUTOSAR-compliant setter for interruptSource with method chaining.

        Args:
            value: The interruptSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to interrupt_source property setter (gets validation automatically)
        """
        self.interrupt_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_interrupt_category(self, value: Optional[BswInterruptCategory]) -> BswInterruptEntity:
        """
        Set interruptCategory and return self for chaining.

        Args:
            value: The interruptCategory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interrupt_category("value")
        """
        self.interrupt_category = value  # Use property setter (gets validation)
        return self

    def with_interrupt_source(self, value: Optional["String"]) -> BswInterruptEntity:
        """
        Set interruptSource and return self for chaining.

        Args:
            value: The interruptSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interrupt_source("value")
        """
        self.interrupt_source = value  # Use property setter (gets validation)
        return self



class BswDirectCallPoint(BswModuleCallPoint):
    """
    Represents a concrete point in the code from where a BswModuleEntry is
    called directly, i.e. not via the BSW Scheduler. This information can be
    used to analyze call tree and resource locking scenarios. It is not needed
    to configure the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswDirectCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 78, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The BswModuleEntry called at this point.
        self._calledEntry: Optional["BswModuleEntry"] = None

    @property
    def called_entry(self) -> Optional["BswModuleEntry"]:
        """Get calledEntry (Pythonic accessor)."""
        return self._calledEntry

    @called_entry.setter
    def called_entry(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set calledEntry with validation.

        Args:
            value: The calledEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledEntry = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"calledEntry must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._calledEntry = value
        # or more ExclusiveAreas that are nested the given order.
        self._calledFrom: Optional["ExclusiveAreaNesting"] = None

    @property
    def called_from(self) -> Optional["ExclusiveAreaNesting"]:
        """Get calledFrom (Pythonic accessor)."""
        return self._calledFrom

    @called_from.setter
    def called_from(self, value: Optional["ExclusiveAreaNesting"]) -> None:
        """
        Set calledFrom with validation.

        Args:
            value: The calledFrom to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledFrom = None
            return

        if not isinstance(value, ExclusiveAreaNesting):
            raise TypeError(
                f"calledFrom must be ExclusiveAreaNesting or None, got {type(value).__name__}"
            )
        self._calledFrom = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalledEntry(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for calledEntry.

        Returns:
            The calledEntry value

        Note:
            Delegates to called_entry property (CODING_RULE_V2_00017)
        """
        return self.called_entry  # Delegates to property

    def setCalledEntry(self, value: "BswModuleEntry") -> BswDirectCallPoint:
        """
        AUTOSAR-compliant setter for calledEntry with method chaining.

        Args:
            value: The calledEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_entry property setter (gets validation automatically)
        """
        self.called_entry = value  # Delegates to property setter
        return self

    def getCalledFrom(self) -> "ExclusiveAreaNesting":
        """
        AUTOSAR-compliant getter for calledFrom.

        Returns:
            The calledFrom value

        Note:
            Delegates to called_from property (CODING_RULE_V2_00017)
        """
        return self.called_from  # Delegates to property

    def setCalledFrom(self, value: "ExclusiveAreaNesting") -> BswDirectCallPoint:
        """
        AUTOSAR-compliant setter for calledFrom with method chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_from property setter (gets validation automatically)
        """
        self.called_from = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_entry(self, value: Optional["BswModuleEntry"]) -> BswDirectCallPoint:
        """
        Set calledEntry and return self for chaining.

        Args:
            value: The calledEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_entry("value")
        """
        self.called_entry = value  # Use property setter (gets validation)
        return self

    def with_called_from(self, value: Optional["ExclusiveAreaNesting"]) -> BswDirectCallPoint:
        """
        Set calledFrom and return self for chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_from("value")
        """
        self.called_from = value  # Use property setter (gets validation)
        return self



class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents a synchronous procedure call point via the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswSynchronousServerCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 79, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The entry to be called.
        self._calledEntryEntry: Optional["BswModuleClientServer"] = None

    @property
    def called_entry_entry(self) -> Optional["BswModuleClientServer"]:
        """Get calledEntryEntry (Pythonic accessor)."""
        return self._calledEntryEntry

    @called_entry_entry.setter
    def called_entry_entry(self, value: Optional["BswModuleClientServer"]) -> None:
        """
        Set calledEntryEntry with validation.

        Args:
            value: The calledEntryEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledEntryEntry = None
            return

        if not isinstance(value, BswModuleClientServer):
            raise TypeError(
                f"calledEntryEntry must be BswModuleClientServer or None, got {type(value).__name__}"
            )
        self._calledEntryEntry = value
        # or more ExclusiveAreas that are nested the given order.
        self._calledFrom: Optional["ExclusiveAreaNesting"] = None

    @property
    def called_from(self) -> Optional["ExclusiveAreaNesting"]:
        """Get calledFrom (Pythonic accessor)."""
        return self._calledFrom

    @called_from.setter
    def called_from(self, value: Optional["ExclusiveAreaNesting"]) -> None:
        """
        Set calledFrom with validation.

        Args:
            value: The calledFrom to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledFrom = None
            return

        if not isinstance(value, ExclusiveAreaNesting):
            raise TypeError(
                f"calledFrom must be ExclusiveAreaNesting or None, got {type(value).__name__}"
            )
        self._calledFrom = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalledEntryEntry(self) -> "BswModuleClientServer":
        """
        AUTOSAR-compliant getter for calledEntryEntry.

        Returns:
            The calledEntryEntry value

        Note:
            Delegates to called_entry_entry property (CODING_RULE_V2_00017)
        """
        return self.called_entry_entry  # Delegates to property

    def setCalledEntryEntry(self, value: "BswModuleClientServer") -> BswSynchronousServerCallPoint:
        """
        AUTOSAR-compliant setter for calledEntryEntry with method chaining.

        Args:
            value: The calledEntryEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_entry_entry property setter (gets validation automatically)
        """
        self.called_entry_entry = value  # Delegates to property setter
        return self

    def getCalledFrom(self) -> "ExclusiveAreaNesting":
        """
        AUTOSAR-compliant getter for calledFrom.

        Returns:
            The calledFrom value

        Note:
            Delegates to called_from property (CODING_RULE_V2_00017)
        """
        return self.called_from  # Delegates to property

    def setCalledFrom(self, value: "ExclusiveAreaNesting") -> BswSynchronousServerCallPoint:
        """
        AUTOSAR-compliant setter for calledFrom with method chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_from property setter (gets validation automatically)
        """
        self.called_from = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_entry_entry(self, value: Optional["BswModuleClientServer"]) -> BswSynchronousServerCallPoint:
        """
        Set calledEntryEntry and return self for chaining.

        Args:
            value: The calledEntryEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_entry_entry("value")
        """
        self.called_entry_entry = value  # Use property setter (gets validation)
        return self

    def with_called_from(self, value: Optional["ExclusiveAreaNesting"]) -> BswSynchronousServerCallPoint:
        """
        Set calledFrom and return self for chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_from("value")
        """
        self.called_from = value  # Use property setter (gets validation)
        return self



class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents an asynchronous procedure call point via the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswAsynchronousServerCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 80, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The entry to be called.
        self._calledEntryEntry: Optional["BswModuleClientServer"] = None

    @property
    def called_entry_entry(self) -> Optional["BswModuleClientServer"]:
        """Get calledEntryEntry (Pythonic accessor)."""
        return self._calledEntryEntry

    @called_entry_entry.setter
    def called_entry_entry(self, value: Optional["BswModuleClientServer"]) -> None:
        """
        Set calledEntryEntry with validation.

        Args:
            value: The calledEntryEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledEntryEntry = None
            return

        if not isinstance(value, BswModuleClientServer):
            raise TypeError(
                f"calledEntryEntry must be BswModuleClientServer or None, got {type(value).__name__}"
            )
        self._calledEntryEntry = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalledEntryEntry(self) -> "BswModuleClientServer":
        """
        AUTOSAR-compliant getter for calledEntryEntry.

        Returns:
            The calledEntryEntry value

        Note:
            Delegates to called_entry_entry property (CODING_RULE_V2_00017)
        """
        return self.called_entry_entry  # Delegates to property

    def setCalledEntryEntry(self, value: "BswModuleClientServer") -> BswAsynchronousServerCallPoint:
        """
        AUTOSAR-compliant setter for calledEntryEntry with method chaining.

        Args:
            value: The calledEntryEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_entry_entry property setter (gets validation automatically)
        """
        self.called_entry_entry = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_entry_entry(self, value: Optional["BswModuleClientServer"]) -> BswAsynchronousServerCallPoint:
        """
        Set calledEntryEntry and return self for chaining.

        Args:
            value: The calledEntryEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_entry_entry("value")
        """
        self.called_entry_entry = value  # Use property setter (gets validation)
        return self



class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """
    The callback point for an BswAsynchronousServerCallPoint i.e. the point at
    which the result can be retrieved from the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswAsynchronousServerCallResultPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 80, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The call point invoking the call to which the result belongs.
        self._asynchronous: Optional["BswAsynchronous"] = None

    @property
    def asynchronous(self) -> Optional["BswAsynchronous"]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, value: Optional["BswAsynchronous"]) -> None:
        """
        Set asynchronous with validation.

        Args:
            value: The asynchronous to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._asynchronous = None
            return

        if not isinstance(value, BswAsynchronous):
            raise TypeError(
                f"asynchronous must be BswAsynchronous or None, got {type(value).__name__}"
            )
        self._asynchronous = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAsynchronous(self) -> "BswAsynchronous":
        """
        AUTOSAR-compliant getter for asynchronous.

        Returns:
            The asynchronous value

        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def setAsynchronous(self, value: "BswAsynchronous") -> BswAsynchronousServerCallResultPoint:
        """
        AUTOSAR-compliant setter for asynchronous with method chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Note:
            Delegates to asynchronous property setter (gets validation automatically)
        """
        self.asynchronous = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_asynchronous(self, value: Optional["BswAsynchronous"]) -> BswAsynchronousServerCallResultPoint:
        """
        Set asynchronous and return self for chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_asynchronous("value")
        """
        self.asynchronous = value  # Use property setter (gets validation)
        return self



class BswScheduleEvent(BswEvent, ABC):
    """
    BswEvent that is able to start a BswSchedulabeEntity.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswScheduleEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 88, Classic
      Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswScheduleEvent:
            raise TypeError("BswScheduleEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswInterruptEvent(BswEvent):
    """
    This meta-class represents an event triggered by an interrupt.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInterruptEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 88, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswOperationInvokedEvent(BswEvent):
    """
    this event is not needed in case of direct function calls.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswOperationInvokedEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 97, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The providedClientServerEntry invoked by this event.
        self._entry: Optional["BswModuleClientServer"] = None

    @property
    def entry(self) -> Optional["BswModuleClientServer"]:
        """Get entry (Pythonic accessor)."""
        return self._entry

    @entry.setter
    def entry(self, value: Optional["BswModuleClientServer"]) -> None:
        """
        Set entry with validation.

        Args:
            value: The entry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._entry = None
            return

        if not isinstance(value, BswModuleClientServer):
            raise TypeError(
                f"entry must be BswModuleClientServer or None, got {type(value).__name__}"
            )
        self._entry = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntry(self) -> "BswModuleClientServer":
        """
        AUTOSAR-compliant getter for entry.

        Returns:
            The entry value

        Note:
            Delegates to entry property (CODING_RULE_V2_00017)
        """
        return self.entry  # Delegates to property

    def setEntry(self, value: "BswModuleClientServer") -> BswOperationInvokedEvent:
        """
        AUTOSAR-compliant setter for entry with method chaining.

        Args:
            value: The entry to set

        Returns:
            self for method chaining

        Note:
            Delegates to entry property setter (gets validation automatically)
        """
        self.entry = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_entry(self, value: Optional["BswModuleClientServer"]) -> BswOperationInvokedEvent:
        """
        Set entry and return self for chaining.

        Args:
            value: The entry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entry("value")
        """
        self.entry = value  # Use property setter (gets validation)
        return self



class BswQueuedDataReceptionPolicy(BswDataReceptionPolicy):
    """
    Reception policy attributes specific for queued receiving.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswQueuedDataReceptionPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 105, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Length of queue for received events.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"queueLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> BswQueuedDataReceptionPolicy:
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> BswQueuedDataReceptionPolicy:
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self



class BswTimingEvent(BswScheduleEvent):
    """
    A recurring BswEvent driven by a time period.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswTimingEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 88, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 217, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Requirement for the time period (in seconds) by which is triggered.
        self._period: Optional["TimeValue"] = None

    @property
    def period(self) -> Optional["TimeValue"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["TimeValue"]) -> None:
        """
        Set period with validation.

        Args:
            value: The period to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"period must be TimeValue or None, got {type(value).__name__}"
            )
        self._period = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "TimeValue") -> BswTimingEvent:
        """
        AUTOSAR-compliant setter for period with method chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_period(self, value: Optional["TimeValue"]) -> BswTimingEvent:
        """
        Set period and return self for chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self



class BswBackgroundEvent(BswScheduleEvent):
    """
    A recurring BswEvent which is used to perform background activities. It is
    similar to a BswTimingEvent but has no fixed time period and is activated
    only with low priority.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswBackgroundEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 89, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswOsTaskExecutionEvent(BswScheduleEvent):
    """
    This BswEvent is supposed to execute BswSchedulableEntitys which have to
    react on the execution of specific OsTasks. Therefore, this event is
    unconditionally raised whenever the OsTask on which it is mapped is
    executed. The main use case for this event is scheduling of Runnables of
    Complex Drivers which have to react on task executions.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswOsTaskExecutionEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 89, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """
    A BswEvent, which can happen sporadically. The event is activated by
    explicit calls from the module to the BSW Scheduler. The main purpose for
    such an event is to cause a context switch, e.g. from an ISR context into a
    task context. Activation and switching are handled within the same module or
    cluster only.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInternalTriggerOccurredEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 91, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The activation point is the source of this event.
        self._eventSourcePoint: Optional["RefType"] = None

    @property
    def event_source_point(self) -> Optional["RefType"]:
        """Get eventSourcePoint (Pythonic accessor)."""
        return self._eventSourcePoint

    @event_source_point.setter
    def event_source_point(self, value: Optional["RefType"]) -> None:
        """
        Set eventSourcePoint with validation.

        Args:
            value: The eventSourcePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSourcePoint = None
            return

        self._eventSourcePoint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSourcePoint(self) -> "RefType":
        """
        AUTOSAR-compliant getter for eventSourcePoint.

        Returns:
            The eventSourcePoint value

        Note:
            Delegates to event_source_point property (CODING_RULE_V2_00017)
        """
        return self.event_source_point  # Delegates to property

    def setEventSourcePoint(self, value: "RefType") -> BswInternalTriggerOccurredEvent:
        """
        AUTOSAR-compliant setter for eventSourcePoint with method chaining.

        Args:
            value: The eventSourcePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_source_point property setter (gets validation automatically)
        """
        self.event_source_point = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source_point(self, value: Optional[RefType]) -> BswInternalTriggerOccurredEvent:
        """
        Set eventSourcePoint and return self for chaining.

        Args:
            value: The eventSourcePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_source_point("value")
        """
        self.event_source_point = value  # Use property setter (gets validation)
        return self



class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    """
    A BswEvent resulting from a trigger released by another module or cluster.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswExternalTriggerOccurredEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 91, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The trigger associated with this event.
        # The trigger is this module.
        self._trigger: Optional["RefType"] = None

    @property
    def trigger(self) -> Optional["RefType"]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: Optional["RefType"]) -> None:
        """
        Set trigger with validation.

        Args:
            value: The trigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: "RefType") -> BswExternalTriggerOccurredEvent:
        """
        AUTOSAR-compliant setter for trigger with method chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_trigger(self, value: Optional[RefType]) -> BswExternalTriggerOccurredEvent:
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self



class BswModeSwitchEvent(BswScheduleEvent):
    """
    A BswEvent resulting from a mode switch.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeSwitchEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 94, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Kind of activation w.
        # r.
        # t.
        # to the referred mode.
        # ModeDeclaration 0.
        # 2 iref Reference to one or two Modes that initiate the Mode by:
                # ModeInBswModule.
        self._activation: Optional["ModeActivationKind"] = None

    @property
    def activation(self) -> Optional["ModeActivationKind"]:
        """Get activation (Pythonic accessor)."""
        return self._activation

    @activation.setter
    def activation(self, value: Optional["ModeActivationKind"]) -> None:
        """
        Set activation with validation.

        Args:
            value: The activation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._activation = None
            return

        if not isinstance(value, ModeActivationKind):
            raise TypeError(
                f"activation must be ModeActivationKind or None, got {type(value).__name__}"
            )
        self._activation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActivation(self) -> "ModeActivationKind":
        """
        AUTOSAR-compliant getter for activation.

        Returns:
            The activation value

        Note:
            Delegates to activation property (CODING_RULE_V2_00017)
        """
        return self.activation  # Delegates to property

    def setActivation(self, value: "ModeActivationKind") -> BswModeSwitchEvent:
        """
        AUTOSAR-compliant setter for activation with method chaining.

        Args:
            value: The activation to set

        Returns:
            self for method chaining

        Note:
            Delegates to activation property setter (gets validation automatically)
        """
        self.activation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_activation(self, value: Optional["ModeActivationKind"]) -> BswModeSwitchEvent:
        """
        Set activation and return self for chaining.

        Args:
            value: The activation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_activation("value")
        """
        self.activation = value  # Use property setter (gets validation)
        return self



class BswModeSwitchedAckEvent(BswScheduleEvent):
    """
    The event is raised after a switch of the referenced mode group has been
    acknowledged or an error occurs. The referenced mode group shall be provided
    by this module.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeSwitchedAckEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 95, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A mode group provided by this module.
        # The of a switch of this group raises this.
        self._modeGroup: Optional["RefType"] = None

    @property
    def mode_group(self) -> Optional["RefType"]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: "RefType") -> BswModeSwitchedAckEvent:
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group(self, value: Optional[RefType]) -> BswModeSwitchedAckEvent:
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self



class BswModeManagerErrorEvent(BswScheduleEvent):
    """
    This represents the ability to react on errors occurring during mode
    handling.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeManagerErrorEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 95, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the ModeDeclarationGroupPrototype for the error behavior of
        # the mode manager applies.
        self._modeGroup: Optional["RefType"] = None

    @property
    def mode_group(self) -> Optional["RefType"]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: "RefType") -> BswModeManagerErrorEvent:
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group(self, value: Optional[RefType]) -> BswModeManagerErrorEvent:
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self



class BswAsynchronousServerCallReturnsEvent(BswScheduleEvent):
    """
    This is the "callback" event for asynchronous Client-Server-Communication
    via the BSW Scheduler which is thrown after completion of the asynchronous
    Client-Server call. Its eventSource specifies the call point to be used for
    retrieving the result.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswAsynchronousServerCallReturnsEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 98, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The call point to be used for retrieving the result.
        self._eventSource: Optional["BswAsynchronous"] = None

    @property
    def event_source(self) -> Optional["BswAsynchronous"]:
        """Get eventSource (Pythonic accessor)."""
        return self._eventSource

    @event_source.setter
    def event_source(self, value: Optional["BswAsynchronous"]) -> None:
        """
        Set eventSource with validation.

        Args:
            value: The eventSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSource = None
            return

        if not isinstance(value, BswAsynchronous):
            raise TypeError(
                f"eventSource must be BswAsynchronous or None, got {type(value).__name__}"
            )
        self._eventSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSource(self) -> "BswAsynchronous":
        """
        AUTOSAR-compliant getter for eventSource.

        Returns:
            The eventSource value

        Note:
            Delegates to event_source property (CODING_RULE_V2_00017)
        """
        return self.event_source  # Delegates to property

    def setEventSource(self, value: "BswAsynchronous") -> BswAsynchronousServerCallReturnsEvent:
        """
        AUTOSAR-compliant setter for eventSource with method chaining.

        Args:
            value: The eventSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_source property setter (gets validation automatically)
        """
        self.event_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source(self, value: Optional["BswAsynchronous"]) -> BswAsynchronousServerCallReturnsEvent:
        """
        Set eventSource and return self for chaining.

        Args:
            value: The eventSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_source("value")
        """
        self.event_source = value  # Use property setter (gets validation)
        return self



class BswDataReceivedEvent(BswScheduleEvent):
    """
    This event is thrown on reception of the referenced data via
    Sender-Receiver-Communication over the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswDataReceivedEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 99, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The received data.
        self._data: Optional["RefType"] = None

    @property
    def data(self) -> Optional["RefType"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["RefType"]) -> None:
        """
        Set data with validation.

        Args:
            value: The data to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        self._data = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for data.

        Returns:
            The data value

        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "RefType") -> BswDataReceivedEvent:
        """
        AUTOSAR-compliant setter for data with method chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional[RefType]) -> BswDataReceivedEvent:
        """
        Set data and return self for chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self


class BswInterruptCategory(AREnum):
    """
    BswInterruptCategory enumeration

Category of the interrupt service Aggregated by BswInterruptEntity.interruptCategory

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior
    """
    # Cat1 interrupt routines are not controlled by the OS and are only allowed to make a very limited selection of OS calls to enable and disable all interrupts. The BswInterruptEntity is implemented by the interrupt service routine, which is directly called from the interrupt vector (not via the OS).
    cat1 = "0"

    # Cat2 interrupt routines are controlled by the OS and they are allowed to make OS calls. The Bsw InterruptEntity is implemented by the interrupt handler, which is called from the OS.
    cat2 = "1"
