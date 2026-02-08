from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SignalServiceTranslationProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the
    signal/service translation service.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 336, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1005, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 730, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the EventGroup which encapsulates the payload.
        self._control: List[RefType] = []

    @property
    def control(self) -> List[RefType]:
        """Get control (Pythonic accessor)."""
        return self._control
        # Reference to the PNCs which control the offer/subscribe the translated
        # service instance.
        self._controlPnc: List[RefType] = []

    @property
    def control_pnc(self) -> List[RefType]:
        """Get controlPnc (Pythonic accessor)."""
        return self._controlPnc
        # Reference to the provided event group (aka Event which is automatically
        # available when service translationStart.
        self._controlProvided: List["EventHandler"] = []

    @property
    def control_provided(self) -> List["EventHandler"]:
        """Get controlProvided (Pythonic accessor)."""
        return self._controlProvided
        # Defines how the service instance control shall behave.
        self._serviceControl: Optional["SignalService"] = None

    @property
    def service_control(self) -> Optional["SignalService"]:
        """Get serviceControl (Pythonic accessor)."""
        return self._serviceControl

    @service_control.setter
    def service_control(self, value: Optional["SignalService"]) -> None:
        """
        Set serviceControl with validation.

        Args:
            value: The serviceControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceControl = None
            return

        if not isinstance(value, SignalService):
            raise TypeError(
                f"serviceControl must be SignalService or None, got {type(value).__name__}"
            )
        self._serviceControl = value
        # Defines properties for a single translated event.
        self._signalServiceEventProps: List["SignalService"] = []

    @property
    def signal_service_event_props(self) -> List["SignalService"]:
        """Get signalServiceEventProps (Pythonic accessor)."""
        return self._signalServiceEventProps

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getControl(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for control.

        Returns:
            The control value

        Note:
            Delegates to control property (CODING_RULE_V2_00017)
        """
        return self.control  # Delegates to property

    def getControlPnc(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for controlPnc.

        Returns:
            The controlPnc value

        Note:
            Delegates to control_pnc property (CODING_RULE_V2_00017)
        """
        return self.control_pnc  # Delegates to property

    def getControlProvided(self) -> List["EventHandler"]:
        """
        AUTOSAR-compliant getter for controlProvided.

        Returns:
            The controlProvided value

        Note:
            Delegates to control_provided property (CODING_RULE_V2_00017)
        """
        return self.control_provided  # Delegates to property

    def getServiceControl(self) -> "SignalService":
        """
        AUTOSAR-compliant getter for serviceControl.

        Returns:
            The serviceControl value

        Note:
            Delegates to service_control property (CODING_RULE_V2_00017)
        """
        return self.service_control  # Delegates to property

    def setServiceControl(self, value: "SignalService") -> "SignalServiceTranslationProps":
        """
        AUTOSAR-compliant setter for serviceControl with method chaining.

        Args:
            value: The serviceControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_control property setter (gets validation automatically)
        """
        self.service_control = value  # Delegates to property setter
        return self

    def getSignalServiceEventProps(self) -> List["SignalService"]:
        """
        AUTOSAR-compliant getter for signalServiceEventProps.

        Returns:
            The signalServiceEventProps value

        Note:
            Delegates to signal_service_event_props property (CODING_RULE_V2_00017)
        """
        return self.signal_service_event_props  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_service_control(self, value: Optional["SignalService"]) -> "SignalServiceTranslationProps":
        """
        Set serviceControl and return self for chaining.

        Args:
            value: The serviceControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_control("value")
        """
        self.service_control = value  # Use property setter (gets validation)
        return self
