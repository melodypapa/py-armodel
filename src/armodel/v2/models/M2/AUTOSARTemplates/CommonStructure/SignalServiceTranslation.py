"""
AUTOSAR Package - SignalServiceTranslation

Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SignalServiceTranslationProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the
    signal/service translation service.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation::SignalServiceTranslationProps

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
        self._control: List["RefType"] = []

    @property
    def control(self) -> List["RefType"]:
        """Get control (Pythonic accessor)."""
        return self._control
        # Reference to the PNCs which control the offer/subscribe the translated
        # service instance.
        self._controlPnc: List["RefType"] = []

    @property
    def control_pnc(self) -> List["RefType"]:
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
        self._signalServiceEventProps: List["SignalService"] = []

    @property
    def signal_service_event_props(self) -> List["SignalService"]:
        """Get signalServiceEventProps (Pythonic accessor)."""
        return self._signalServiceEventProps

    def with_control(self, value):
        """
        Set control and return self for chaining.

        Args:
            value: The control to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_control("value")
        """
        self.control = value  # Use property setter (gets validation)
        return self

    def with_control_pnc(self, value):
        """
        Set control_pnc and return self for chaining.

        Args:
            value: The control_pnc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_control_pnc("value")
        """
        self.control_pnc = value  # Use property setter (gets validation)
        return self

    def with_control_provided(self, value):
        """
        Set control_provided and return self for chaining.

        Args:
            value: The control_provided to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_control_provided("value")
        """
        self.control_provided = value  # Use property setter (gets validation)
        return self

    def with_signal_service_event_props(self, value):
        """
        Set signal_service_event_props and return self for chaining.

        Args:
            value: The signal_service_event_props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_service_event_props("value")
        """
        self.signal_service_event_props = value  # Use property setter (gets validation)
        return self

    def with_signal_service_props(self, value):
        """
        Set signal_service_props and return self for chaining.

        Args:
            value: The signal_service_props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_service_props("value")
        """
        self.signal_service_props = value  # Use property setter (gets validation)
        return self

    def with_element_props(self, value):
        """
        Set element_props and return self for chaining.

        Args:
            value: The element_props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element_props("value")
        """
        self.element_props = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getControl(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for control.

        Returns:
            The control value

        Note:
            Delegates to control property (CODING_RULE_V2_00017)
        """
        return self.control  # Delegates to property

    def getControlPnc(self) -> List["RefType"]:
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



class SignalServiceTranslationPropsSet(ARElement):
    """
    Collection of SignalServiceTranslationProps.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation::SignalServiceTranslationPropsSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 730, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of SignalServiceTranslationProps.
        self._signalServiceProps: List["SignalService"] = []

    @property
    def signal_service_props(self) -> List["SignalService"]:
        """Get signalServiceProps (Pythonic accessor)."""
        return self._signalServiceProps

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignalServiceProps(self) -> List["SignalService"]:
        """
        AUTOSAR-compliant getter for signalServiceProps.

        Returns:
            The signalServiceProps value

        Note:
            Delegates to signal_service_props property (CODING_RULE_V2_00017)
        """
        return self.signal_service_props  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SignalServiceTranslationEventProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the
    signal/service translation event.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation::SignalServiceTranslationEventProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 731, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines properties for a single translated element.
        self._elementProps: List["SignalService"] = []

    @property
    def element_props(self) -> List["SignalService"]:
        """Get elementProps (Pythonic accessor)."""
        return self._elementProps
        # Defined whether the translation shall happen in a safe.
        self._safeTranslation: Optional["Boolean"] = None

    @property
    def safe_translation(self) -> Optional["Boolean"]:
        """Get safeTranslation (Pythonic accessor)."""
        return self._safeTranslation

    @safe_translation.setter
    def safe_translation(self, value: Optional["Boolean"]) -> None:
        """
        Set safeTranslation with validation.

        Args:
            value: The safeTranslation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._safeTranslation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"safeTranslation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._safeTranslation = value
        self._secure: Optional["Boolean"] = None

    @property
    def secure(self) -> Optional["Boolean"]:
        """Get secure (Pythonic accessor)."""
        return self._secure

    @secure.setter
    def secure(self, value: Optional["Boolean"]) -> None:
        """
        Set secure with validation.

        Args:
            value: The secure to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secure = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"secure must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._secure = value
        # by: VariableDataPrototypeIn.
        self._translation: Optional["RefType"] = None

    @property
    def translation(self) -> Optional["RefType"]:
        """Get translation (Pythonic accessor)."""
        return self._translation

    @translation.setter
    def translation(self, value: Optional["RefType"]) -> None:
        """
        Set translation with validation.

        Args:
            value: The translation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._translation = None
            return

        self._translation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElementProps(self) -> List["SignalService"]:
        """
        AUTOSAR-compliant getter for elementProps.

        Returns:
            The elementProps value

        Note:
            Delegates to element_props property (CODING_RULE_V2_00017)
        """
        return self.element_props  # Delegates to property

    def getSafeTranslation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for safeTranslation.

        Returns:
            The safeTranslation value

        Note:
            Delegates to safe_translation property (CODING_RULE_V2_00017)
        """
        return self.safe_translation  # Delegates to property

    def setSafeTranslation(self, value: "Boolean") -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for safeTranslation with method chaining.

        Args:
            value: The safeTranslation to set

        Returns:
            self for method chaining

        Note:
            Delegates to safe_translation property setter (gets validation automatically)
        """
        self.safe_translation = value  # Delegates to property setter
        return self

    def getSecure(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for secure.

        Returns:
            The secure value

        Note:
            Delegates to secure property (CODING_RULE_V2_00017)
        """
        return self.secure  # Delegates to property

    def setSecure(self, value: "Boolean") -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for secure with method chaining.

        Args:
            value: The secure to set

        Returns:
            self for method chaining

        Note:
            Delegates to secure property setter (gets validation automatically)
        """
        self.secure = value  # Delegates to property setter
        return self

    def getTranslation(self) -> "RefType":
        """
        AUTOSAR-compliant getter for translation.

        Returns:
            The translation value

        Note:
            Delegates to translation property (CODING_RULE_V2_00017)
        """
        return self.translation  # Delegates to property

    def setTranslation(self, value: "RefType") -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for translation with method chaining.

        Args:
            value: The translation to set

        Returns:
            self for method chaining

        Note:
            Delegates to translation property setter (gets validation automatically)
        """
        self.translation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_safe_translation(self, value: Optional["Boolean"]) -> "SignalServiceTranslationEventProps":
        """
        Set safeTranslation and return self for chaining.

        Args:
            value: The safeTranslation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_safe_translation("value")
        """
        self.safe_translation = value  # Use property setter (gets validation)
        return self

    def with_secure(self, value: Optional["Boolean"]) -> "SignalServiceTranslationEventProps":
        """
        Set secure and return self for chaining.

        Args:
            value: The secure to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_secure("value")
        """
        self.secure = value  # Use property setter (gets validation)
        return self

    def with_translation(self, value: Optional[RefType]) -> "SignalServiceTranslationEventProps":
        """
        Set translation and return self for chaining.

        Args:
            value: The translation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_translation("value")
        """
        self.translation = value  # Use property setter (gets validation)
        return self



class SignalServiceTranslationElementProps(Identifiable):
    """
    Defined translation properties for individual mapped elements.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation::SignalServiceTranslationElementProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 735, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the leaf element the SignalService apply to.
        self._element: Optional["RefType"] = None

    @property
    def element(self) -> Optional["RefType"]:
        """Get element (Pythonic accessor)."""
        return self._element

    @element.setter
    def element(self, value: Optional["RefType"]) -> None:
        """
        Set element with validation.

        Args:
            value: The element to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._element = None
            return

        self._element = value
        self._filter: Optional["DataFilter"] = None

    @property
    def filter(self) -> Optional["DataFilter"]:
        """Get filter (Pythonic accessor)."""
        return self._filter

    @filter.setter
    def filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set filter with validation.

        Args:
            value: The filter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"filter must be DataFilter or None, got {type(value).__name__}"
            )
        self._filter = value
        # triggers the sending of the.
        self._transmission: Optional["Boolean"] = None

    @property
    def transmission(self) -> Optional["Boolean"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["Boolean"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"transmission must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def setElement(self, value: "RefType") -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for element with method chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Note:
            Delegates to element property setter (gets validation automatically)
        """
        self.element = value  # Delegates to property setter
        return self

    def getFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for filter.

        Returns:
            The filter value

        Note:
            Delegates to filter property (CODING_RULE_V2_00017)
        """
        return self.filter  # Delegates to property

    def setFilter(self, value: "DataFilter") -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for filter with method chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter property setter (gets validation automatically)
        """
        self.filter = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "Boolean") -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_element(self, value: Optional[RefType]) -> "SignalServiceTranslationElementProps":
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self

    def with_filter(self, value: Optional["DataFilter"]) -> "SignalServiceTranslationElementProps":
        """
        Set filter and return self for chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter("value")
        """
        self.filter = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["Boolean"]) -> "SignalServiceTranslationElementProps":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self


class SignalServiceTranslationControlEnum(AREnum):
    """
    SignalServiceTranslationControlEnum enumeration

This enumeration allows to define how the service instance offer/subscribe control shall behave. Aggregated by SignalServiceTranslationProps.serviceControl

Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation
    """
    # Defines the start of service control when all specified partial networks are active.
    allPartialNetworksActive = "3"

    # Defines the start of service control when any specified partial network is active.
    anyPartialNetworkActive = "4"

    # Defines the start of service control when specific partial networks are active.
    partialNetwork = "1"

    # Defines the start of service control when other service is available.
    serviceDiscovery = "2"

    # Defines the start of service control at translation start.
    translationStart = "0"
