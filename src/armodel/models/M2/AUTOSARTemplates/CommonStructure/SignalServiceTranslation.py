from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.DataPrototypeReference import DataPrototypeReference

__all__ = [
    "SignalServiceTranslationControlEnum",
    "SignalServiceTranslationElementProps",
    "SignalServiceTranslationEventProps",
    "SignalServiceTranslationProps",
    "SignalServiceTranslationPropsSet",
]


class SignalServiceTranslationControlEnum(AREnum):
    """
    This enumeration allows to define how the service instance offer/subscribe control shall behave.

    # SignalServiceTranslationControlEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.343, p.744
    # Spec verified: R23-11
    # (no methods; serialized as an enumeration literal on the consuming attribute serviceControl)
    """

    ALL_PARTIAL_NETWORKS_ACTIVE = "allPartialNetworksActive"
    ANY_PARTIAL_NETWORK_ACTIVE = "anyPartialNetworkActive"
    PARTIAL_NETWORK = "partialNetwork"  # atp.Status=obsolete
    SERVICE_DISCOVERY = "serviceDiscovery"
    TRANSLATION_START = "translationStart"

    def __init__(self):
        super().__init__(
            [
                SignalServiceTranslationControlEnum.ALL_PARTIAL_NETWORKS_ACTIVE,
                SignalServiceTranslationControlEnum.ANY_PARTIAL_NETWORK_ACTIVE,
                SignalServiceTranslationControlEnum.PARTIAL_NETWORK,
                SignalServiceTranslationControlEnum.SERVICE_DISCOVERY,
                SignalServiceTranslationControlEnum.TRANSLATION_START,
            ]
        )


class SignalServiceTranslationElementProps(Identifiable):
    """
    Defined translation properties for individual mapped elements.

    # SignalServiceTranslationElementProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.342, p.735
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getElement                  [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
    # [x] setElement                  [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
    # [x] getFilter                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setFilter                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTransmissionTrigger      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTransmissionTrigger      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # element: DataPrototypeReference not yet implemented (Rule 0001.10 placeholder) - reader/writer pending
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the leaf element the SignalService TranslationElementProps apply to.
        # (DataPrototypeReference class is not yet implemented - placeholder)
        self.element: Optional["DataPrototypeReference"] = None

        # Defines an optional filter to be applied during translation.
        self.filter: Optional[DataFilter] = None

        # Defines whether the source element (which is mapped to the referenced element) triggers the sending of the respective payload.
        self.transmissionTrigger: Optional[Boolean] = None

    def getElement(self) -> Optional["DataPrototypeReference"]:
        """
        Reference to the leaf element the SignalService TranslationElementProps apply to.
        """
        return self.element

    def setElement(self, value: Optional["DataPrototypeReference"]):
        """
        Reference to the leaf element the SignalService TranslationElementProps apply to.
        A None value is a no-op and does not overwrite an existing element.
        """
        if value is not None:
            self.element = value
        return self

    def getFilter(self) -> Optional[DataFilter]:
        """
        Defines an optional filter to be applied during translation.
        """
        return self.filter

    def setFilter(self, value: Optional[DataFilter]):
        """
        Defines an optional filter to be applied during translation.
        A None value is a no-op and does not overwrite an existing filter.
        """
        if value is not None:
            self.filter = value
        return self

    def getTransmissionTrigger(self) -> Optional[Boolean]:
        """
        Defines whether the source element (which is mapped to the referenced element) triggers the sending of the respective payload.
        """
        return self.transmissionTrigger

    def setTransmissionTrigger(self, value: Optional[Boolean]):
        """
        Defines whether the source element (which is mapped to the referenced element) triggers the sending of the respective payload.
        A None value is a no-op and does not overwrite an existing transmissionTrigger.
        """
        if value is not None:
            self.transmissionTrigger = value
        return self


class SignalServiceTranslationEventProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the signal/service translation event.

    # SignalServiceTranslationEventProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.341, p.731
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createSignalServiceTranslationElementProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSignalServiceTranslationElementProps        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getSafeTranslation                            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setSafeTranslation                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecureTranslation                          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setSecureTranslation                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTranslationTarget                          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTranslationTarget                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        # Defines properties for a single translated element.
        self.elementProps: List[SignalServiceTranslationElementProps] = []

        # Defined whether the translation shall happen in a safe way.
        self.safeTranslation: Optional[Boolean] = None

        # Defined whether the translation shall happen in a secure way.
        self.secureTranslation: Optional[Boolean] = None

        # Reference to a VariableDataPrototype representing the target of signal/service translation.
        self.translationTarget: Optional[VariableDataPrototypeInSystemInstanceRef] = None

    def createSignalServiceTranslationElementProps(self, short_name: str) -> SignalServiceTranslationElementProps:
        """
        Defines properties for a single translated element.
        """
        element = SignalServiceTranslationElementProps(self, short_name)
        self.addElement(element)
        self.elementProps.append(element)
        return element

    def getSignalServiceTranslationElementProps(self) -> List[SignalServiceTranslationElementProps]:
        """
        Defines properties for a single translated element.
        """
        return self.elementProps

    def getSafeTranslation(self) -> Optional[Boolean]:
        """
        Defined whether the translation shall happen in a safe way.
        """
        return self.safeTranslation

    def setSafeTranslation(self, value: Optional[Boolean]):
        """
        Defined whether the translation shall happen in a safe way.
        A None value is a no-op and does not overwrite an existing safeTranslation.
        """
        if value is not None:
            self.safeTranslation = value
        return self

    def getSecureTranslation(self) -> Optional[Boolean]:
        """
        Defined whether the translation shall happen in a secure way.
        """
        return self.secureTranslation

    def setSecureTranslation(self, value: Optional[Boolean]):
        """
        Defined whether the translation shall happen in a secure way.
        A None value is a no-op and does not overwrite an existing secureTranslation.
        """
        if value is not None:
            self.secureTranslation = value
        return self

    def getTranslationTarget(self) -> Optional[VariableDataPrototypeInSystemInstanceRef]:
        """
        Reference to a VariableDataPrototype representing the target of signal/service translation.
        """
        return self.translationTarget

    def setTranslationTarget(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]):
        """
        Reference to a VariableDataPrototype representing the target of signal/service translation.
        A None value is a no-op and does not overwrite an existing translationTarget.
        """
        if value is not None:
            self.translationTarget = value
        return self


class SignalServiceTranslationProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the signal/service translation service.

    # SignalServiceTranslationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.340, p.730
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addControlConsumedEventGroupRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getControlConsumedEventGroupRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addControlPncRef                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getControlPncRefs                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addControlProvidedEventGroupRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getControlProvidedEventGroupRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getServiceControl                           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setServiceControl                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createSignalServiceTranslationEventProps    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSignalServiceTranslationEventProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the EventGroup which encapsulates the signal-based payload.
        self.controlConsumedEventGroupRefs: List[RefType] = []

        # Reference to the PNCs which control the offer/subscribe behavior of the translated service instance.
        self.controlPncRefs: List[RefType] = []

        # Reference to the provided event group (aka Event Handler) which is automatically available when service Control equals translationStart.
        self.controlProvidedEventGroupRefs: List[RefType] = []

        # Defines how the service instance control shall behave.
        self.serviceControl: Optional[SignalServiceTranslationControlEnum] = None

        # Defines properties for a single translated event.
        self.signalServiceTranslationEventProps: List[SignalServiceTranslationEventProps] = []

    def addControlConsumedEventGroupRef(self, value: RefType):
        """
        Reference to the EventGroup which encapsulates the signal-based payload.
        A None value is a no-op and does not overwrite an existing reference.
        """
        if value is not None:
            self.controlConsumedEventGroupRefs.append(value)
        return self

    def getControlConsumedEventGroupRefs(self) -> List[RefType]:
        """
        Reference to the EventGroup which encapsulates the signal-based payload.
        """
        return self.controlConsumedEventGroupRefs

    def addControlPncRef(self, value: RefType):
        """
        Reference to the PNCs which control the offer/subscribe behavior of the translated service instance.
        A None value is a no-op and does not overwrite an existing reference.
        """
        if value is not None:
            self.controlPncRefs.append(value)
        return self

    def getControlPncRefs(self) -> List[RefType]:
        """
        Reference to the PNCs which control the offer/subscribe behavior of the translated service instance.
        """
        return self.controlPncRefs

    def addControlProvidedEventGroupRef(self, value: RefType):
        """
        Reference to the provided event group (aka Event Handler) which is automatically available when service Control equals translationStart.
        A None value is a no-op and does not overwrite an existing reference.
        """
        if value is not None:
            self.controlProvidedEventGroupRefs.append(value)
        return self

    def getControlProvidedEventGroupRefs(self) -> List[RefType]:
        """
        Reference to the provided event group (aka Event Handler) which is automatically available when service Control equals translationStart.
        """
        return self.controlProvidedEventGroupRefs

    def getServiceControl(self) -> Optional[SignalServiceTranslationControlEnum]:
        """
        Defines how the service instance control shall behave.
        """
        return self.serviceControl

    def setServiceControl(self, value: Optional[SignalServiceTranslationControlEnum]):
        """
        Defines how the service instance control shall behave.
        A None value is a no-op and does not overwrite an existing serviceControl.
        """
        if value is not None:
            self.serviceControl = value
        return self

    def createSignalServiceTranslationEventProps(self, short_name: str) -> SignalServiceTranslationEventProps:
        """
        Defines properties for a single translated event.
        """
        element = SignalServiceTranslationEventProps(self, short_name)
        self.addElement(element)
        self.signalServiceTranslationEventProps.append(element)
        return element

    def getSignalServiceTranslationEventProps(self) -> List[SignalServiceTranslationEventProps]:
        """
        Defines properties for a single translated event.
        """
        return self.signalServiceTranslationEventProps


class SignalServiceTranslationPropsSet(Identifiable):
    """
    Collection of SignalServiceTranslationProps.

    # SignalServiceTranslationPropsSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.339, p.730
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createSignalServiceTranslationProps        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSignalServiceTranslationProps           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        # Collection of SignalServiceTranslationProps.
        self.signalServiceTranslationProps: List[SignalServiceTranslationProps] = []

    def createSignalServiceTranslationProps(self, short_name: str) -> SignalServiceTranslationProps:
        """
        Collection of SignalServiceTranslationProps.
        """
        element = SignalServiceTranslationProps(self, short_name)
        self.addElement(element)
        self.signalServiceTranslationProps.append(element)
        return element

    def getSignalServiceTranslationProps(self) -> List[SignalServiceTranslationProps]:
        """
        Collection of SignalServiceTranslationProps.
        """
        return self.signalServiceTranslationProps
