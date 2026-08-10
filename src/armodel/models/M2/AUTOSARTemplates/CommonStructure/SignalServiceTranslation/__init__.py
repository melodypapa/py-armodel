from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef

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

    * allPartialNetworksActive
        Defines the start of service control when all specified partial networks are active.
    * anyPartialNetworkActive
        Defines the start of service control when any specified partial network is active.
    * partialNetwork
        Defines the start of service control when specific partial networks are active. This literal is obsolete.
    * serviceDiscovery
        Defines the start of service control when other service is available.
    * translationStart
        Defines the start of service control at translation start.

    # SignalServiceTranslationControlEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.343, p.744
    # Spec verified: R23-11
    # (no methods)
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
    # [ ] __init__                   [x] impl  [x] docstring  [x] test
    # [ ] getElement                 [x] impl  [x] docstring  [x] test
    # [ ] setElement                 [x] impl  [x] docstring  [x] test
    # [ ] getFilter                  [x] impl  [x] docstring  [x] test
    # [ ] setFilter                  [x] impl  [x] docstring  [x] test
    # [ ] getTransmissionTrigger     [x] impl  [x] docstring  [x] test
    # [ ] setTransmissionTrigger     [x] impl  [x] docstring  [x] test
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        # DataPrototypeReference class is not yet implemented - placeholder (TODO)
        self.element: Optional["DataPrototypeReference"] = None
        self.filter: Optional[DataFilter] = None
        self.transmissionTrigger: Optional[Boolean] = None

    def getElement(self) -> Optional["DataPrototypeReference"]:
        return self.element

    def setElement(self, value: Optional["DataPrototypeReference"]):
        if value is not None:
            self.element = value
        return self

    def getFilter(self) -> Optional[DataFilter]:
        return self.filter

    def setFilter(self, value: Optional[DataFilter]):
        if value is not None:
            self.filter = value
        return self

    def getTransmissionTrigger(self) -> Optional[Boolean]:
        return self.transmissionTrigger

    def setTransmissionTrigger(self, value: Optional[Boolean]):
        if value is not None:
            self.transmissionTrigger = value
        return self


class SignalServiceTranslationEventProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the signal/service translation event.

    # SignalServiceTranslationEventProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.341, p.731
    # Spec verified: R23-11
    # [x] __init__                              [x] impl  [x] docstring  [x] test
    # [x] createSignalServiceTranslationElementProps    [x] impl  [x] docstring  [x] test
    # [x] getSignalServiceTranslationElementProps       [x] impl  [x] docstring  [x] test
    # [x] getSafeTranslation                    [x] impl  [x] docstring  [x] test
    # [x] setSafeTranslation                    [x] impl  [x] docstring  [x] test
    # [x] getSecureTranslation                  [x] impl  [x] docstring  [x] test
    # [x] setSecureTranslation                  [x] impl  [x] docstring  [x] test
    # [x] getTranslationTarget                  [x] impl  [x] docstring  [x] test
    # [x] setTranslationTarget                  [x] impl  [x] docstring  [x] test
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        self.elementProps: List[SignalServiceTranslationElementProps] = []
        self.safeTranslation: Optional[Boolean] = None
        self.secureTranslation: Optional[Boolean] = None
        self.translationTarget: Optional[VariableDataPrototypeInSystemInstanceRef] = None

    def createSignalServiceTranslationElementProps(self, short_name: str) -> SignalServiceTranslationElementProps:
        element = SignalServiceTranslationElementProps(self, short_name)
        self.addElement(element)
        self.elementProps.append(element)
        return element

    def getSignalServiceTranslationElementProps(self) -> List[SignalServiceTranslationElementProps]:
        return self.elementProps

    def getSafeTranslation(self) -> Optional[Boolean]:
        return self.safeTranslation

    def setSafeTranslation(self, value: Optional[Boolean]):
        if value is not None:
            self.safeTranslation = value
        return self

    def getSecureTranslation(self) -> Optional[Boolean]:
        return self.secureTranslation

    def setSecureTranslation(self, value: Optional[Boolean]):
        if value is not None:
            self.secureTranslation = value
        return self

    def getTranslationTarget(self) -> Optional[VariableDataPrototypeInSystemInstanceRef]:
        return self.translationTarget

    def setTranslationTarget(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]):
        if value is not None:
            self.translationTarget = value
        return self


class SignalServiceTranslationProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the signal/service translation service.

    # SignalServiceTranslationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.340, p.731
    # Spec verified: R23-11
    # [x] __init__                           [x] impl  [x] docstring  [x] test
    # [x] addControlConsumedEventGroupRef    [x] impl  [x] docstring  [x] test
    # [x] getControlConsumedEventGroupRefs   [x] impl  [x] docstring  [x] test
    # [x] addControlPncRef                   [x] impl  [x] docstring  [x] test
    # [x] getControlPncRefs                  [x] impl  [x] docstring  [x] test
    # [x] addControlProvidedEventGroupRef    [x] impl  [x] docstring  [x] test
    # [x] getControlProvidedEventGroupRefs   [x] impl  [x] docstring  [x] test
    # [x] getServiceControl                  [x] impl  [x] docstring  [x] test
    # [x] setServiceControl                  [x] impl  [x] docstring  [x] test
    # [x] createSignalServiceTranslationEventProps    [x] impl  [x] docstring  [x] test
    # [x] getSignalServiceTranslationEventProps       [x] impl  [x] docstring  [x] test
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        self.controlConsumedEventGroupRefs: List[RefType] = []
        self.controlPncRefs: List[RefType] = []
        self.controlProvidedEventGroupRefs: List[RefType] = []
        self.serviceControl: Optional[SignalServiceTranslationControlEnum] = None
        self.signalServiceTranslationEventProps: List[SignalServiceTranslationEventProps] = []

    def addControlConsumedEventGroupRef(self, value: RefType):
        if value is not None:
            self.controlConsumedEventGroupRefs.append(value)
        return self

    def getControlConsumedEventGroupRefs(self) -> List[RefType]:
        return self.controlConsumedEventGroupRefs

    def addControlPncRef(self, value: RefType):
        if value is not None:
            self.controlPncRefs.append(value)
        return self

    def getControlPncRefs(self) -> List[RefType]:
        return self.controlPncRefs

    def addControlProvidedEventGroupRef(self, value: RefType):
        if value is not None:
            self.controlProvidedEventGroupRefs.append(value)
        return self

    def getControlProvidedEventGroupRefs(self) -> List[RefType]:
        return self.controlProvidedEventGroupRefs

    def getServiceControl(self) -> Optional[SignalServiceTranslationControlEnum]:
        return self.serviceControl

    def setServiceControl(self, value: Optional[SignalServiceTranslationControlEnum]):
        if value is not None:
            self.serviceControl = value
        return self

    def createSignalServiceTranslationEventProps(self, short_name: str) -> SignalServiceTranslationEventProps:
        element = SignalServiceTranslationEventProps(self, short_name)
        self.addElement(element)
        self.signalServiceTranslationEventProps.append(element)
        return element

    def getSignalServiceTranslationEventProps(self) -> List[SignalServiceTranslationEventProps]:
        return self.signalServiceTranslationEventProps


class SignalServiceTranslationPropsSet(Identifiable):
    """
    This element allows to define the properties which are applicable for the signal/service translation service.

    # SignalServiceTranslationPropsSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.339, p.730
    # Spec verified: R23-11
    # [x] __init__                              [x] impl  [x] docstring  [x] test
    # [x] createSignalServiceTranslationProps   [x] impl  [x] docstring  [x] test
    # [x] getSignalServiceTranslationProps      [x] impl  [x] docstring  [x] test
    """

    def __init__(self, parent: Identifiable, short_name: str):
        super().__init__(parent, short_name)

        self.signalServiceTranslationProps: List[SignalServiceTranslationProps] = []

    def createSignalServiceTranslationProps(self, short_name: str) -> SignalServiceTranslationProps:
        element = SignalServiceTranslationProps(self, short_name)
        self.addElement(element)
        self.signalServiceTranslationProps.append(element)
        return element

    def getSignalServiceTranslationProps(self) -> List[SignalServiceTranslationProps]:
        return self.signalServiceTranslationProps
