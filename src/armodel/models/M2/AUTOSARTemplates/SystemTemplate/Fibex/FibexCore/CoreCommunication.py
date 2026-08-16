from __future__ import annotations

from abc import ABC
from typing import List, Optional, TYPE_CHECKING
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable, Describable, PackageableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARLiteral, ARNumerical, ARPositiveInteger, Boolean, ByteOrderEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, PositiveInteger, RefType, ARBoolean, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue, UnlimitedInteger
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import TransmissionModeDeclaration

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataTypePolicyEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationISignalProps


class FibexElement(PackageableElement, ABC):
    """
    ASAM FIBEX elements specifying Communication and Topology.
    """

    # FibexElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.64, p.2026
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is FibexElement:
            raise TypeError("FibexElement is an abstract class.")

        super().__init__(parent, short_name)


class PduToFrameMapping(Identifiable):
    """
    Defines the mapping between Protocol Data Units (PDUs) and frames,
    specifying how PDUs are embedded within frames including byte order,
    start position, and update indication bit position.
    """

    # PduToFrameMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getPackingByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] setPackingByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] getPduRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] setPduRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] getStartPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] setStartPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] getUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test
    # [ ] setUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.packingByteOrder: ARLiteral = None
        self.pduRef: RefType = None
        self.startPosition: ARNumerical = None
        self.updateIndicationBitPosition: ARNumerical = None

    def getPackingByteOrder(self):
        return self.packingByteOrder

    def setPackingByteOrder(self, value):
        self.packingByteOrder = value
        return self

    def getPduRef(self):
        return self.pduRef

    def setPduRef(self, value):
        self.pduRef = value
        return self

    def getStartPosition(self):
        return self.startPosition

    def setStartPosition(self, value):
        self.startPosition = value
        return self

    def getUpdateIndicationBitPosition(self):
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value):
        self.updateIndicationBitPosition = value
        return self


class Frame(FibexElement, ABC):
    """
    Abstract base class for communication frames in the AUTOSAR system,
    defining common properties for different types of communication
    frames including frame length and PDU to frame mappings.
    """

    # Frame method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFrameLength               [x] impl  [ ] docstring  [ ] test
    # [ ] setFrameLength               [x] impl  [ ] docstring  [ ] test
    # [ ] createPduToFrameMapping      [x] impl  [ ] docstring  [ ] test
    # [ ] getPduToFrameMappings        [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Frame:
            raise TypeError("Frame is an abstract class.")

        super().__init__(parent, short_name)

        self.frameLength = None
        self.pduToFrameMappings: List[PduToFrameMapping] = []

    def getFrameLength(self):
        return self.frameLength

    def setFrameLength(self, value):
        self.frameLength = value
        return self

    def createPduToFrameMapping(self, short_name: str) -> PduToFrameMapping:
        if not self.IsElementExists(short_name):
            mapping = PduToFrameMapping(self, short_name)
            self.addElement(mapping)
            self.pduToFrameMappings.append(mapping)
        return self.getElement(short_name, PduToFrameMapping)

    def getPduToFrameMappings(self) -> List[PduToFrameMapping]:
        return list(sorted(filter(lambda a: isinstance(a, PduToFrameMapping), self.elements), key=lambda o: o.short_name))


class ContainedIPduProps(ARObject):
    """
    Defines properties for contained Interaction Protocol Data Units (IPDUs),
    specifying collection semantics, header IDs, offset, timeout,
    trigger, and update indication bit position properties.
    """

    # ContainedIPduProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCollectionSemantics       [x] impl  [ ] docstring  [ ] test
    # [ ] setCollectionSemantics       [x] impl  [ ] docstring  [ ] test
    # [ ] getHeaderIdLongHeader        [x] impl  [ ] docstring  [ ] test
    # [ ] setHeaderIdLongHeader        [x] impl  [ ] docstring  [ ] test
    # [ ] getHeaderIdShortHeader       [x] impl  [ ] docstring  [ ] test
    # [ ] setHeaderIdShortHeader       [x] impl  [ ] docstring  [ ] test
    # [ ] getOffset                    [x] impl  [ ] docstring  [ ] test
    # [ ] setOffset                    [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeout                   [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeout                   [x] impl  [ ] docstring  [ ] test
    # [ ] getTrigger                   [x] impl  [ ] docstring  [ ] test
    # [ ] setTrigger                   [x] impl  [ ] docstring  [ ] test
    # [ ] getUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test
    # [ ] setUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.collectionSemantics: ARLiteral = None
        self.headerIdLongHeader: ARPositiveInteger = None
        self.headerIdShortHeader: ARPositiveInteger = None
        self.offset: ARNumerical = None
        self.timeout: ARNumerical = None
        self.trigger: ARLiteral = None
        self.updateIndicationBitPosition: ARNumerical = None

    def getCollectionSemantics(self):
        return self.collectionSemantics

    def setCollectionSemantics(self, value):
        self.collectionSemantics = value
        return self

    def getHeaderIdLongHeader(self):
        return self.headerIdLongHeader

    def setHeaderIdLongHeader(self, value):
        self.headerIdLongHeader = value
        return self

    def getHeaderIdShortHeader(self):
        return self.headerIdShortHeader

    def setHeaderIdShortHeader(self, value):
        self.headerIdShortHeader = value
        return self

    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        self.offset = value
        return self

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        self.timeout = value
        return self

    def getTrigger(self):
        return self.trigger

    def setTrigger(self, value):
        self.trigger = value
        return self

    def getUpdateIndicationBitPosition(self):
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value):
        self.updateIndicationBitPosition = value
        return self


class ISignalGroup(FibexElement):
    """
    Defines a group of interaction signals in the communication system,
    specifying relationships between individual signals and system-level
    signal groups with transformation properties.
    """

    # ISignalGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getComBasedSignalGroupTransformationRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addComBasedSignalGroupTransformationRef [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalRefs               [x] impl  [ ] docstring  [ ] test
    # [ ] addISignalRef                [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemSignalGroupRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setSystemSignalGroupRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getTransformationISignalProps [x] impl  [ ] docstring  [ ] test
    # [ ] setTransformationISignalProps [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.comBasedSignalGroupTransformationRefs: List[RefType] = []
        self.iSignalRefs: List[RefType] = []
        self.systemSignalGroupRef = None
        self.transformationISignalProps = None

    def getComBasedSignalGroupTransformationRefs(self):
        return self.comBasedSignalGroupTransformationRefs

    def addComBasedSignalGroupTransformationRef(self, value):
        if value is not None:
            self.comBasedSignalGroupTransformationRefs.append(value)
        return self

    def getISignalRefs(self):
        return self.iSignalRefs

    def addISignalRef(self, value):
        self.iSignalRefs.append(value)
        return self

    def getSystemSignalGroupRef(self):
        return self.systemSignalGroupRef

    def setSystemSignalGroupRef(self, value):
        self.systemSignalGroupRef = value
        return self

    def getTransformationISignalProps(self):
        return self.transformationISignalProps

    def setTransformationISignalProps(self, value):
        self.transformationISignalProps = value
        return self


class ISignalIPduGroup(FibexElement):
    """
    Defines a group of Interaction Protocol Data Units (IPDUs) based on interaction signals,
    specifying communication direction, mode, and references to contained
    IPDU groups and individual IPDUs.
    """

    # ISignalIPduGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationDirection    [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationDirection    [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationMode         [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationMode         [x] impl  [ ] docstring  [ ] test
    # [ ] getContainedISignalIPduGroupRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addContainedISignalIPduGroupRef [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalIPduRefs           [x] impl  [ ] docstring  [ ] test
    # [ ] addISignalIPduRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getNmPduRefs                 [x] impl  [ ] docstring  [ ] test
    # [ ] addNmPduRef                  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.communicationDirection = None
        self.communicationMode = None
        self.containedISignalIPduGroupRefs = []
        self.iSignalIPduRefs = []
        self.nmPduRefs = []

    def getCommunicationDirection(self):
        return self.communicationDirection

    def setCommunicationDirection(self, value):
        self.communicationDirection = value
        return self

    def getCommunicationMode(self):
        return self.communicationMode

    def setCommunicationMode(self, value):
        self.communicationMode = value
        return self

    def getContainedISignalIPduGroupRefs(self):
        return self.containedISignalIPduGroupRefs

    def addContainedISignalIPduGroupRef(self, value):
        self.containedISignalIPduGroupRefs.append(value)
        return self

    def getISignalIPduRefs(self):
        return self.iSignalIPduRefs

    def addISignalIPduRef(self, value):
        self.iSignalIPduRefs.append(value)
        return self

    def getNmPduRefs(self):
        return self.nmPduRefs

    def addNmPduRef(self, value):
        self.nmPduRefs.append(value)
        return self


class Pdu(FibexElement, ABC):
    """
    Collection of all Pdus that can be routed through a bus interface.
    """

    # Pdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.17, p.340
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setHasDynamicLength          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHasDynamicLength          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLength                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLength                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Pdu:
            raise TypeError("Pdu is an abstract class.")

        super().__init__(parent, short_name)

        # This attribute defines whether the Pdu has dynamic length (true) or not (false). Please note that the usage of this attribute is restricted by [constr_3448].
        self.hasDynamicLength: Boolean = None

        # Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this parameter was defined in bits. The Pdu length of zero bytes is allowed.
        self.length: UnlimitedInteger = None

    def setHasDynamicLength(self, value: Optional[Boolean]) -> "Pdu":
        """
        This attribute defines whether the Pdu has dynamic length (true) or not (false). Please note that the usage of this attribute is restricted by [constr_3448].
        A None value is a no-op and does not overwrite an existing hasDynamicLength.
        """
        if value is not None:
            self.hasDynamicLength = value
        return self

    def getHasDynamicLength(self) -> Optional[Boolean]:
        """
        This attribute defines whether the Pdu has dynamic length (true) or not (false). Please note that the usage of this attribute is restricted by [constr_3448].
        """
        return self.hasDynamicLength

    def setLength(self, value: Optional[UnlimitedInteger]) -> "Pdu":
        """
        Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this parameter was defined in bits. The Pdu length of zero bytes is allowed.
        A None value is a no-op and does not overwrite an existing length.
        """
        if value is not None:
            self.length = value
        return self

    def getLength(self) -> Optional[UnlimitedInteger]:
        """
        Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this parameter was defined in bits. The Pdu length of zero bytes is allowed.
        """
        return self.length


class IPdu(Pdu, ABC):
    """
    Abstract base class for Interaction Protocol Data Units (IPDUs),
    extending the PDU class with contained IPDU properties for
    interaction-based communication.
    """

    # IPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContainedIPduProps        [x] impl  [ ] docstring  [ ] test
    # [ ] setContainedIPduProps        [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IPdu:
            raise TypeError("IPdu is an abstract class.")

        super().__init__(parent, short_name)

        self.containedIPduProps: ContainedIPduProps = None

    def getContainedIPduProps(self):
        return self.containedIPduProps

    def setContainedIPduProps(self, value):
        if value is not None:
            self.containedIPduProps = value
        return self


class SecureCommunicationProps(ARObject):
    """
    This meta-class contains configuration settings that are specific for an individual SecuredIPdu.
    """

    # SecureCommunicationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.44, p.369
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAuthDataFreshnessLength             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthDataFreshnessLength             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthDataFreshnessStartPosition      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthDataFreshnessStartPosition      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthenticationBuildAttempts         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthenticationBuildAttempts         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthenticationRetries               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthenticationRetries               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataId                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataId                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessValueId                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessValueId                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMessageLinkLength                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMessageLinkLength                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMessageLinkPosition                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMessageLinkPosition                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondaryFreshnessValueId           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondaryFreshnessValueId           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecuredAreaLength                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecuredAreaLength                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecuredAreaOffset                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecuredAreaOffset                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the SecureCommunicationProps.
        """
        super().__init__()

        # This attribute defines the length in bits of the authentic PDU data that is passed to the SWC that verifies and generates the Freshness.
        self.authDataFreshnessLength: Optional[PositiveInteger] = None

        # This value determines the start position in bits of the Authentic PDU that shall be passed on to the SWC that verifies and generates the Freshness. The bit counting is done according to TPS_SYST_01068.
        self.authDataFreshnessStartPosition: Optional[PositiveInteger] = None

        # This attribute specifies the number of authentication build attempts.
        self.authenticationBuildAttempts: Optional[PositiveInteger] = None

        # This attribute defines the additional number of authentication attempts that are to be carried out when the generation of the authentication information failed for a given SecuredIPdu. If zero is set than only one authentication attempt is done.
        self.authenticationRetries: Optional[PositiveInteger] = None

        # This attribute defines a numerical identifier for the Secured I-PDU.
        self.dataId: Optional[PositiveInteger] = None

        # This attribute defines the Id of the Freshness Value. The Freshness Value might be a normal counter or a time value.
        self.freshnessValueId: Optional[PositiveInteger] = None

        # SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the length in bits of the messageLinker.
        self.messageLinkLength: Optional[PositiveInteger] = None

        # SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the startPosition in bits of the messageLinker.
        self.messageLinkPosition: Optional[PositiveInteger] = None

        # This attribute defines the Id of the Secondary Freshness Value. The Secondary Freshness Value might be a normal counter or a time value. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        self.secondaryFreshnessValueId: Optional[PositiveInteger] = None

        # This attribute defines the length in bytes of the area within the payload Pdu which will be secured.
        self.securedAreaLength: Optional[PositiveInteger] = None

        # This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured.
        self.securedAreaOffset: Optional[PositiveInteger] = None

    def getAuthDataFreshnessLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bits of the authentic PDU data that is passed to the SWC that verifies and generates the Freshness.
        """
        return self.authDataFreshnessLength

    def setAuthDataFreshnessLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the length in bits of the authentic PDU data that is passed to the SWC that verifies and generates the Freshness.
        A None value is a no-op and does not overwrite an existing authDataFreshnessLength.
        """
        if value is not None:
            self.authDataFreshnessLength = value
        return self

    def getAuthDataFreshnessStartPosition(self) -> Optional[PositiveInteger]:
        """
        This value determines the start position in bits of the Authentic PDU that shall be passed on to the SWC that verifies and generates the Freshness. The bit counting is done according to TPS_SYST_01068.
        """
        return self.authDataFreshnessStartPosition

    def setAuthDataFreshnessStartPosition(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This value determines the start position in bits of the Authentic PDU that shall be passed on to the SWC that verifies and generates the Freshness. The bit counting is done according to TPS_SYST_01068.
        A None value is a no-op and does not overwrite an existing authDataFreshnessStartPosition.
        """
        if value is not None:
            self.authDataFreshnessStartPosition = value
        return self

    def getAuthenticationBuildAttempts(self) -> Optional[PositiveInteger]:
        """
        This attribute specifies the number of authentication build attempts.
        """
        return self.authenticationBuildAttempts

    def setAuthenticationBuildAttempts(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute specifies the number of authentication build attempts.
        A None value is a no-op and does not overwrite an existing authenticationBuildAttempts.
        """
        if value is not None:
            self.authenticationBuildAttempts = value
        return self

    def getAuthenticationRetries(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the additional number of authentication attempts that are to be carried out when the generation of the authentication information failed for a given SecuredIPdu. If zero is set than only one authentication attempt is done.
        """
        return self.authenticationRetries

    def setAuthenticationRetries(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the additional number of authentication attempts that are to be carried out when the generation of the authentication information failed for a given SecuredIPdu. If zero is set than only one authentication attempt is done.
        A None value is a no-op and does not overwrite an existing authenticationRetries.
        """
        if value is not None:
            self.authenticationRetries = value
        return self

    def getDataId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines a numerical identifier for the Secured I-PDU.
        """
        return self.dataId

    def setDataId(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines a numerical identifier for the Secured I-PDU.
        A None value is a no-op and does not overwrite an existing dataId.
        """
        if value is not None:
            self.dataId = value
        return self

    def getFreshnessValueId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the Id of the Freshness Value. The Freshness Value might be a normal counter or a time value.
        """
        return self.freshnessValueId

    def setFreshnessValueId(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the Id of the Freshness Value. The Freshness Value might be a normal counter or a time value.
        A None value is a no-op and does not overwrite an existing freshnessValueId.
        """
        if value is not None:
            self.freshnessValueId = value
        return self

    def getMessageLinkLength(self) -> Optional[PositiveInteger]:
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the length in bits of the messageLinker.
        """
        return self.messageLinkLength

    def setMessageLinkLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the length in bits of the messageLinker.
        A None value is a no-op and does not overwrite an existing messageLinkLength.
        """
        if value is not None:
            self.messageLinkLength = value
        return self

    def getMessageLinkPosition(self) -> Optional[PositiveInteger]:
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the startPosition in bits of the messageLinker.
        """
        return self.messageLinkPosition

    def setMessageLinkPosition(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the startPosition in bits of the messageLinker.
        A None value is a no-op and does not overwrite an existing messageLinkPosition.
        """
        if value is not None:
            self.messageLinkPosition = value
        return self

    def getSecondaryFreshnessValueId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the Id of the Secondary Freshness Value. The Secondary Freshness Value might be a normal counter or a time value. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        """
        return self.secondaryFreshnessValueId

    def setSecondaryFreshnessValueId(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the Id of the Secondary Freshness Value. The Secondary Freshness Value might be a normal counter or a time value. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        A None value is a no-op and does not overwrite an existing secondaryFreshnessValueId.
        """
        if value is not None:
            self.secondaryFreshnessValueId = value
        return self

    def getSecuredAreaLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bytes of the area within the payload Pdu which will be secured.
        """
        return self.securedAreaLength

    def setSecuredAreaLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the length in bytes of the area within the payload Pdu which will be secured.
        A None value is a no-op and does not overwrite an existing securedAreaLength.
        """
        if value is not None:
            self.securedAreaLength = value
        return self

    def getSecuredAreaOffset(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured.
        """
        return self.securedAreaOffset

    def setSecuredAreaOffset(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured.
        A None value is a no-op and does not overwrite an existing securedAreaOffset.
        """
        if value is not None:
            self.securedAreaOffset = value
        return self


class SecuredIPdu(IPdu):
    """
    Represents a secured Interaction Protocol Data Unit (IPDU) with
    authentication, integrity protection, and other security properties
    for protected communication.
    """

    # SecuredIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAuthenticationPropsRef    [x] impl  [ ] docstring  [ ] test
    # [ ] setAuthenticationPropsRef    [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicRuntimeLengthHandling [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicRuntimeLengthHandling [x] impl  [ ] docstring  [ ] test
    # [ ] getFreshnessPropsRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setFreshnessPropsRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getPayloadRef                [x] impl  [ ] docstring  [ ] test
    # [ ] setPayloadRef                [x] impl  [ ] docstring  [ ] test
    # [ ] getSecureCommunicationProps  [x] impl  [ ] docstring  [ ] test
    # [ ] setSecureCommunicationProps  [x] impl  [ ] docstring  [ ] test
    # [ ] getUseAsCryptographicIPdu    [x] impl  [ ] docstring  [ ] test
    # [ ] setUseAsCryptographicIPdu    [x] impl  [ ] docstring  [ ] test
    # [ ] getUseSecuredPduHeader       [x] impl  [ ] docstring  [ ] test
    # [ ] setUseSecuredPduHeader       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.authenticationPropsRef: RefType = None
        self.dynamicRuntimeLengthHandling: Boolean = None
        self.freshnessPropsRef: RefType = None
        self.payloadRef: RefType = None
        self.secureCommunicationProps: SecureCommunicationProps = None
        self.useAsCryptographicIPdu: Boolean = None
        self.useSecuredPduHeader = None

    def getAuthenticationPropsRef(self):
        return self.authenticationPropsRef

    def setAuthenticationPropsRef(self, value):
        if value is not None:
            self.authenticationPropsRef = value
        return self

    def getDynamicRuntimeLengthHandling(self):
        return self.dynamicRuntimeLengthHandling

    def setDynamicRuntimeLengthHandling(self, value):
        if value is not None:
            self.dynamicRuntimeLengthHandling = value
        return self

    def getFreshnessPropsRef(self):
        return self.freshnessPropsRef

    def setFreshnessPropsRef(self, value):
        if value is not None:
            self.freshnessPropsRef = value
        return self

    def getPayloadRef(self):
        return self.payloadRef

    def setPayloadRef(self, value):
        if value is not None:
            self.payloadRef = value
        return self

    def getSecureCommunicationProps(self):
        return self.secureCommunicationProps

    def setSecureCommunicationProps(self, value):
        if value is not None:
            self.secureCommunicationProps = value
        return self

    def getUseAsCryptographicIPdu(self):
        return self.useAsCryptographicIPdu

    def setUseAsCryptographicIPdu(self, value):
        if value is not None:
            self.useAsCryptographicIPdu = value
        return self

    def getUseSecuredPduHeader(self):
        return self.useSecuredPduHeader

    def setUseSecuredPduHeader(self, value):
        if value is not None:
            self.useSecuredPduHeader = value
        return self


class ISignalToIPduMapping(Identifiable):
    """
    Defines the mapping between interaction signals and Interaction Protocol Data Units (IPDUs),
    specifying signal references, byte order, start position, transfer
    properties, and update indication bit position.
    """

    # ISignalToIPduMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalRef                [x] impl  [ ] docstring  [ ] test
    # [ ] setISignalRef                [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalGroupRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setISignalGroupRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getPackingByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] setPackingByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] getStartPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] setStartPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] getTransferProperty          [x] impl  [ ] docstring  [ ] test
    # [ ] setTransferProperty          [x] impl  [ ] docstring  [ ] test
    # [ ] getUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test
    # [ ] setUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iSignalRef: RefType = None
        self.iSignalGroupRef: RefType = None
        self.packingByteOrder: ByteOrderEnum = None
        self.startPosition: UnlimitedInteger = None
        self.transferProperty = None
        self.updateIndicationBitPosition: UnlimitedInteger = None

    def getISignalRef(self):
        return self.iSignalRef

    def setISignalRef(self, value):
        self.iSignalRef = value
        return self

    def getISignalGroupRef(self):
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value):
        self.iSignalGroupRef = value
        return self

    def getPackingByteOrder(self):
        return self.packingByteOrder

    def setPackingByteOrder(self, value):
        self.packingByteOrder = value
        return self

    def getStartPosition(self):
        return self.startPosition

    def setStartPosition(self, value):
        self.startPosition = value
        return self

    def getTransferProperty(self):
        return self.transferProperty

    def setTransferProperty(self, value):
        self.transferProperty = value
        return self

    def getUpdateIndicationBitPosition(self):
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value):
        self.updateIndicationBitPosition = value
        return self


class NmPdu(Pdu):
    """
    Represents a Network Management Protocol Data Unit (PDU) used for
    network management communication including node monitoring,
    wake-up, and sleep state management.
    """

    # NmPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalToIPduMappings     [x] impl  [ ] docstring  [ ] test
    # [ ] createISignalToIPduMapping   [x] impl  [ ] docstring  [ ] test
    # [ ] getNmDataInformation         [x] impl  [ ] docstring  [ ] test
    # [ ] setNmDataInformation         [x] impl  [ ] docstring  [ ] test
    # [ ] getNmVoteInformation         [x] impl  [ ] docstring  [ ] test
    # [ ] setNmVoteInformation         [x] impl  [ ] docstring  [ ] test
    # [ ] getUnusedBitPattern          [x] impl  [ ] docstring  [ ] test
    # [ ] setUnusedBitPattern          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.iSignalToIPduMappings: List[ISignalToIPduMapping] = []
        self.nmDataInformation: Boolean = None
        self.nmVoteInformation: Boolean = None
        self.unusedBitPattern: Integer = None

    def getISignalToIPduMappings(self):
        return self.iSignalToIPduMappings

    def createISignalToIPduMapping(self, short_name: str) -> ISignalToIPduMapping:
        if not self.IsElementExists(short_name):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToIPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getNmDataInformation(self):
        return self.nmDataInformation

    def setNmDataInformation(self, value):
        if value is not None:
            self.nmDataInformation = value
        return self

    def getNmVoteInformation(self):
        return self.nmVoteInformation

    def setNmVoteInformation(self, value):
        if value is not None:
            self.nmVoteInformation = value
        return self

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        if value is not None:
            self.unusedBitPattern = value
        return self


class NPdu(IPdu):
    """
    Represents a Network Protocol Data Unit (PDU) used for network-level
    communication in the AUTOSAR communication system.
    """

    # NPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DcmIPdu(IPdu):
    """
    Represents a Diagnostic Communication Management Interaction Protocol Data Unit (IPDU)
    used for diagnostic communication in the AUTOSAR system.
    """

    # DcmIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDiagPduType               [x] impl  [ ] docstring  [ ] test
    # [ ] setDiagPduType               [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.diagPduType: ARLiteral = None

    def getDiagPduType(self):
        return self.diagPduType

    def setDiagPduType(self, value):
        self.diagPduType = value
        return self


class IPduTiming(Describable):
    """
    Defines timing properties for Interaction Protocol Data Units (IPDUs),
    specifying minimum delay and transmission mode declaration for
    timed communication.
    """

    # IPduTiming method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getMinimumDelay              [x] impl  [ ] docstring  [ ] test
    # [ ] setMinimumDelay              [x] impl  [ ] docstring  [ ] test
    # [ ] getTransmissionModeDeclaration [x] impl  [ ] docstring  [ ] test
    # [ ] setTransmissionModeDeclaration [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.minimumDelay: TimeValue = None
        self.transmissionModeDeclaration: TransmissionModeDeclaration = None

    def getMinimumDelay(self):
        return self.minimumDelay

    def setMinimumDelay(self, value):
        self.minimumDelay = value
        return self

    def getTransmissionModeDeclaration(self):
        return self.transmissionModeDeclaration

    def setTransmissionModeDeclaration(self, value):
        self.transmissionModeDeclaration = value
        return self


class ISignalIPdu(IPdu):
    """
    Represents an Interaction Protocol Data Unit (IPDU) based on interaction signals,
    defining timing specifications, signal-to-PDU mappings, and unused
    bit patterns for signal-based communication.
    """

    # ISignalIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduTimingSpecification   [x] impl  [ ] docstring  [ ] test
    # [ ] setIPduTimingSpecification   [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalToPduMappings      [x] impl  [ ] docstring  [ ] test
    # [ ] createISignalToPduMappings   [x] impl  [ ] docstring  [ ] test
    # [ ] getUnusedBitPattern          [x] impl  [ ] docstring  [ ] test
    # [ ] setUnusedBitPattern          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iPduTimingSpecification: IPduTiming = None
        self.iSignalToPduMappings: List[ISignalToIPduMapping] = []
        self.unusedBitPattern: Integer = None

    def getIPduTimingSpecification(self):
        return self.iPduTimingSpecification

    def setIPduTimingSpecification(self, value):
        self.iPduTimingSpecification = value
        return self

    def getISignalToPduMappings(self):
        return self.iSignalToPduMappings

    def createISignalToPduMappings(self, short_name: str) -> ISignalToIPduMapping:
        if not self.IsElementExists(short_name):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        self.unusedBitPattern = value
        return self


class ISignalTypeEnum(AREnum):
    """
    This enumeration defines ISignal types that are used for derivation of the ComSignalType in the COM configuration.
    """

    # ISignalTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.9, p.322
    # Spec verified: R23-11
    # (no methods)

    # ISignal shall be interpreted as an array (UINT8_N, UINT8_DYN) Tags: atp.EnumerationLiteralIndex=0
    ARRAY = "array"

    # ISignal shall be interpreted as a primitive type (e.g. UINT_8, SINT_32) Tags: atp.EnumerationLiteralIndex=1
    PRIMITIVE = "primitive"

    def __init__(self):
        super().__init__(
            (
                ISignalTypeEnum.ARRAY,
                ISignalTypeEnum.PRIMITIVE,
            )
        )


class ISignalProps(ARObject):
    """
    Additional ISignal properties that may be stored in different files.
    """

    # ISignalProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.10, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHandleOutOfRange                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHandleOutOfRange                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the ISignalProps.
        """
        super().__init__()

        # This attribute defines the outOfRangeHandling for received and sent signals.
        self.handleOutOfRange: Optional[HandleOutOfRangeEnum] = None

    def getHandleOutOfRange(self) -> Optional[HandleOutOfRangeEnum]:
        """
        This attribute defines the outOfRangeHandling for received and sent signals.
        """
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value: Optional[HandleOutOfRangeEnum]) -> "ISignalProps":
        """
        This attribute defines the outOfRangeHandling for received and sent signals.
        A None value is a no-op and does not overwrite an existing handleOutOfRange.
        """
        if value is not None:
            self.handleOutOfRange = value
        return self


class ISignal(FibexElement):
    """
    Signal of the Interaction Layer. The RTE supports a "signal fan-out" where the same System Signal is sent in different SignalIPdus to multiple receivers. To support the RTE "signal fan-out" each SignalIPdu contains ISignals. If the same System Signal is to be mapped into several SignalIPdus there is one ISignal needed for each ISignalToIPduMapping. ISignals describe the Interface between the Precompile configured RTE and the potentially Postbuild configured Com Stack (see ECUC Parameter Mapping). In case of the SystemSignalGroup an ISignal shall be created for each SystemSignal contained in the SystemSignalGroup.
    """

    # ISignal method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.7, p.321
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataTransformationRef                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataTransformationRef                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataTypePolicy                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataTypePolicy                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInitValue                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInitValue                                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalProps                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalProps                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalType                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalType                                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLength                                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLength                                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkRepresentationProps                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkRepresentationProps                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSystemSignalRef                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSystemSignalRef                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutSubstitutionValue                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutSubstitutionValue                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addTransformationISignalProps                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformationISignalProps                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ISignal.
        """
        super().__init__(parent, short_name)

        # Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignal.
        self.dataTransformationRef: Optional[RefType] = None

        # With the aggregation of SwDataDefProps an ISignal specifies how it is represented on the network. This representation follows a particular policy. Note that this causes some redundancy which is intended and can be used to support flexible development methodology as well as subsequent integrity checks. If the policy "networkRepresentationFromComSpec" is chosen the network representation from the ComSpec that is aggregated by the PortPrototype shall be used. If the "override" policy is chosen the requirements specified in the PortInterface and in the ComSpec are not fulfilled by the networkRepresentationProps. In case the System Description doesn't use a complete Software Component Description (VFB View) the "legacy" policy can be chosen.
        self.dataTypePolicy: Optional[DataTypePolicyEnum] = None

        # Optional definition of a ISignal's initValue in case the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. This value can be used to configure the Signal's "Init Value". If a full DataMapping exist for the SystemSignal this information may be available from a configured SenderComSpec and ReceiverComSpec. In this case the initvalues in SenderComSpec and/or ReceiverComSpec override this optional value specification. Further restrictions apply from the RTE specification.
        self.initValue: Optional[ValueSpecification] = None

        # Additional optional ISignal properties that may be stored in different files.
        self.iSignalProps: Optional[ISignalProps] = None

        # This attribute defines whether this iSignal is an array that results in a UINT8_N / UINT8_DYN ComSignalType in the COM configuration or a primitive type.
        self.iSignalType: Optional[ISignalTypeEnum] = None

        # Size of the signal in bits. The size needs to be derived from the mapped VariableDataPrototype according to the mapping of primitive DataTypes to BaseTypes as used in the RTE. Indicates maximum size for dynamic length signals. The ISignal length of zero bits is allowed.
        self.length: Optional[UnlimitedInteger] = None

        # Specification of the actual network representation. The usage of SwDataDefProps for this purpose is restricted to the attributes compuMethod and baseType. The optional baseType attributes "memAllignment" and "byteOrder" shall not be used. The attribute "dataTypePolicy" in the SystemTemplate element defines whether this network representation shall be ignored and the information shall be taken over from the network representation of the ComSpec. If "override" is chosen by the system integrator the network representation can violate against the requirements defined in the PortInterface and in the network representation of the ComSpec. In case that the System Description doesn't use a complete Software Component Description (VFB View) this element is used to configure "ComSignalDataInvalidValue" and the Data Semantics.
        self.networkRepresentationProps: Optional[SwDataDefProps] = None

        # Reference to the System Signal that is supposed to be transmitted in the ISignal.
        self.systemSignalRef: Optional[RefType] = None

        # Defines and enables the ComTimeoutSubstituition for this ISignal.
        self.timeoutSubstitutionValue: Optional[ValueSpecification] = None

        # A transformer chain consists of an ordered list of transformers. The ISignal specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignals are described in the TransformationTechnology class.
        self.transformationISignalProps: List[TransformationISignalProps] = []

    def getDataTransformationRef(self) -> Optional[RefType]:
        """
        Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignal.
        """
        return self.dataTransformationRef

    def setDataTransformationRef(self, value: Optional[RefType]) -> "ISignal":
        """
        Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignal.
        A None value is a no-op and does not overwrite an existing dataTransformationRef.
        """
        if value is not None:
            self.dataTransformationRef = value
        return self

    def getDataTypePolicy(self) -> Optional[DataTypePolicyEnum]:
        """
        With the aggregation of SwDataDefProps an ISignal specifies how it is represented on the network. This representation follows a particular policy. Note that this causes some redundancy which is intended and can be used to support flexible development methodology as well as subsequent integrity checks. If the policy "networkRepresentationFromComSpec" is chosen the network representation from the ComSpec that is aggregated by the PortPrototype shall be used. If the "override" policy is chosen the requirements specified in the PortInterface and in the ComSpec are not fulfilled by the networkRepresentationProps. In case the System Description doesn't use a complete Software Component Description (VFB View) the "legacy" policy can be chosen.
        """
        return self.dataTypePolicy

    def setDataTypePolicy(self, value: Optional[DataTypePolicyEnum]) -> "ISignal":
        """
        With the aggregation of SwDataDefProps an ISignal specifies how it is represented on the network. This representation follows a particular policy. Note that this causes some redundancy which is intended and can be used to support flexible development methodology as well as subsequent integrity checks. If the policy "networkRepresentationFromComSpec" is chosen the network representation from the ComSpec that is aggregated by the PortPrototype shall be used. If the "override" policy is chosen the requirements specified in the PortInterface and in the ComSpec are not fulfilled by the networkRepresentationProps. In case the System Description doesn't use a complete Software Component Description (VFB View) the "legacy" policy can be chosen.
        A None value is a no-op and does not overwrite an existing dataTypePolicy.
        """
        if value is not None:
            self.dataTypePolicy = value
        return self

    def getInitValue(self) -> Optional[ValueSpecification]:
        """
        Optional definition of a ISignal's initValue in case the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. This value can be used to configure the Signal's "Init Value". If a full DataMapping exist for the SystemSignal this information may be available from a configured SenderComSpec and ReceiverComSpec. In this case the initvalues in SenderComSpec and/or ReceiverComSpec override this optional value specification. Further restrictions apply from the RTE specification.
        """
        return self.initValue

    def setInitValue(self, value: Optional[ValueSpecification]) -> "ISignal":
        """
        Optional definition of a ISignal's initValue in case the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. This value can be used to configure the Signal's "Init Value". If a full DataMapping exist for the SystemSignal this information may be available from a configured SenderComSpec and ReceiverComSpec. In this case the initvalues in SenderComSpec and/or ReceiverComSpec override this optional value specification. Further restrictions apply from the RTE specification.
        A None value is a no-op and does not overwrite an existing initValue.
        """
        if value is not None:
            self.initValue = value
        return self

    def getISignalProps(self) -> Optional[ISignalProps]:
        """
        Additional optional ISignal properties that may be stored in different files.
        """
        return self.iSignalProps

    def setISignalProps(self, value: Optional[ISignalProps]) -> "ISignal":
        """
        Additional optional ISignal properties that may be stored in different files.
        A None value is a no-op and does not overwrite an existing iSignalProps.
        """
        if value is not None:
            self.iSignalProps = value
        return self

    def getISignalType(self) -> Optional[ISignalTypeEnum]:
        """
        This attribute defines whether this iSignal is an array that results in a UINT8_N / UINT8_DYN ComSignalType in the COM configuration or a primitive type.
        """
        return self.iSignalType

    def setISignalType(self, value: Optional[ISignalTypeEnum]) -> "ISignal":
        """
        This attribute defines whether this iSignal is an array that results in a UINT8_N / UINT8_DYN ComSignalType in the COM configuration or a primitive type.
        A None value is a no-op and does not overwrite an existing iSignalType.
        """
        if value is not None:
            self.iSignalType = value
        return self

    def getLength(self) -> Optional[UnlimitedInteger]:
        """
        Size of the signal in bits. The size needs to be derived from the mapped VariableDataPrototype according to the mapping of primitive DataTypes to BaseTypes as used in the RTE. Indicates maximum size for dynamic length signals. The ISignal length of zero bits is allowed.
        """
        return self.length

    def setLength(self, value: Optional[UnlimitedInteger]) -> "ISignal":
        """
        Size of the signal in bits. The size needs to be derived from the mapped VariableDataPrototype according to the mapping of primitive DataTypes to BaseTypes as used in the RTE. Indicates maximum size for dynamic length signals. The ISignal length of zero bits is allowed.
        A None value is a no-op and does not overwrite an existing length.
        """
        if value is not None:
            self.length = value
        return self

    def getNetworkRepresentationProps(self) -> Optional[SwDataDefProps]:
        """
        Specification of the actual network representation. The usage of SwDataDefProps for this purpose is restricted to the attributes compuMethod and baseType. The optional baseType attributes "memAllignment" and "byteOrder" shall not be used. The attribute "dataTypePolicy" in the SystemTemplate element defines whether this network representation shall be ignored and the information shall be taken over from the network representation of the ComSpec. If "override" is chosen by the system integrator the network representation can violate against the requirements defined in the PortInterface and in the network representation of the ComSpec. In case that the System Description doesn't use a complete Software Component Description (VFB View) this element is used to configure "ComSignalDataInvalidValue" and the Data Semantics.
        """
        return self.networkRepresentationProps

    def setNetworkRepresentationProps(self, value: Optional[SwDataDefProps]) -> "ISignal":
        """
        Specification of the actual network representation. The usage of SwDataDefProps for this purpose is restricted to the attributes compuMethod and baseType. The optional baseType attributes "memAllignment" and "byteOrder" shall not be used. The attribute "dataTypePolicy" in the SystemTemplate element defines whether this network representation shall be ignored and the information shall be taken over from the network representation of the ComSpec. If "override" is chosen by the system integrator the network representation can violate against the requirements defined in the PortInterface and in the network representation of the ComSpec. In case that the System Description doesn't use a complete Software Component Description (VFB View) this element is used to configure "ComSignalDataInvalidValue" and the Data Semantics.
        A None value is a no-op and does not overwrite an existing networkRepresentationProps.
        """
        if value is not None:
            self.networkRepresentationProps = value
        return self

    def getSystemSignalRef(self) -> Optional[RefType]:
        """
        Reference to the System Signal that is supposed to be transmitted in the ISignal.
        """
        return self.systemSignalRef

    def setSystemSignalRef(self, value: Optional[RefType]) -> "ISignal":
        """
        Reference to the System Signal that is supposed to be transmitted in the ISignal.
        A None value is a no-op and does not overwrite an existing systemSignalRef.
        """
        if value is not None:
            self.systemSignalRef = value
        return self

    def getTimeoutSubstitutionValue(self) -> Optional[ValueSpecification]:
        """
        Defines and enables the ComTimeoutSubstituition for this ISignal.
        """
        return self.timeoutSubstitutionValue

    def setTimeoutSubstitutionValue(self, value: Optional[ValueSpecification]) -> "ISignal":
        """
        Defines and enables the ComTimeoutSubstituition for this ISignal.
        A None value is a no-op and does not overwrite an existing timeoutSubstitutionValue.
        """
        if value is not None:
            self.timeoutSubstitutionValue = value
        return self

    def addTransformationISignalProps(self, value: Optional[TransformationISignalProps]) -> "ISignal":
        """
        A transformer chain consists of an ordered list of transformers. The ISignal specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignals are described in the TransformationTechnology class.
        """
        if value is not None:
            self.transformationISignalProps.append(value)
        return self

    def getTransformationISignalProps(self) -> List[TransformationISignalProps]:
        """
        A transformer chain consists of an ordered list of transformers. The ISignal specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignals are described in the TransformationTechnology class.
        """
        return self.transformationISignalProps


class PduTriggering(Identifiable):
    """
    Defines the triggering mechanism for Protocol Data Units (PDUs),
    specifying PDU references, port references, and trigger conditions
    for PDU transmission and reception.
    """

    # PduTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduPortRefs              [x] impl  [ ] docstring  [ ] test
    # [ ] addIPduPortRef               [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalTriggeringRefs     [x] impl  [ ] docstring  [ ] test
    # [ ] addISignalTriggeringRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getSecOcCryptoMappingRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setSecOcCryptoMappingRef     [x] impl  [ ] docstring  [ ] test
    # [ ] getTriggerIPduSendConditions [x] impl  [ ] docstring  [ ] test
    # [ ] addTriggerIPduSendCondition  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iPduRef: RefType = None
        self.iPduPortRefs: List[RefType] = []
        self.iSignalTriggeringRefs: List[RefType] = []
        self.secOcCryptoMappingRef: RefType = None
        self.triggerIPduSendConditions = []  # type: List

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        self.iPduRef = value
        return self

    def getIPduPortRefs(self):
        return self.iPduPortRefs

    def addIPduPortRef(self, value):
        self.iPduPortRefs.append(value)
        return self

    def getISignalTriggeringRefs(self):
        # return sorted(self.iSignalTriggeringRefs, key = lambda i: i.getShortValue())
        return self.iSignalTriggeringRefs

    def addISignalTriggeringRef(self, value):
        self.iSignalTriggeringRefs.append(value)
        return self

    def getSecOcCryptoMappingRef(self):
        return self.secOcCryptoMappingRef

    def setSecOcCryptoMappingRef(self, value):
        self.secOcCryptoMappingRef = value
        return self

    def getTriggerIPduSendConditions(self):
        return self.triggerIPduSendConditions

    def addTriggerIPduSendCondition(self, value):
        self.triggerIPduSendConditions.append(value)
        return self


class FrameTriggering(Identifiable, ABC):
    """
    Abstract base class for frame triggering mechanisms, defining
    common properties for triggering frame transmission and reception
    including frame references and port references.
    """

    # FrameTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFrameRef                  [x] impl  [ ] docstring  [ ] test
    # [ ] setFrameRef                  [x] impl  [ ] docstring  [ ] test
    # [ ] getFramePortRefs             [x] impl  [ ] docstring  [ ] test
    # [ ] addFramePortRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getPduTriggeringRefs         [x] impl  [ ] docstring  [ ] test
    # [ ] addPduTriggeringRef          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        if type(self) is FrameTriggering:
            raise TypeError("FrameTriggering is an abstract class.")

        super().__init__(parent, short_name)

        self.frameRef: RefType = None
        self.framePortRefs: List[RefType] = []
        self.pduTriggeringRefs: List[RefType] = []

    def getFrameRef(self) -> RefType:
        return self.frameRef

    def setFrameRef(self, value: RefType):
        self.frameRef = value
        return self

    def getFramePortRefs(self) -> List[RefType]:
        return self.framePortRefs

    def addFramePortRef(self, value: RefType):
        self.framePortRefs.append(value)
        return self

    def getPduTriggeringRefs(self) -> RefType:
        return self.pduTriggeringRefs

    def addPduTriggeringRef(self, value: RefType):
        self.pduTriggeringRefs.append(value)
        return self


class SystemSignal(ARElement):
    """
    Represents a system signal in the AUTOSAR system, defining
    dynamic length properties and physical properties for
    system-level signal communication.
    """

    # SystemSignal method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicLength             [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicLength             [x] impl  [ ] docstring  [ ] test
    # [ ] getPhysicalProps             [x] impl  [ ] docstring  [ ] test
    # [ ] setPhysicalProps             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dynamicLength: ARBoolean = None
        self.physicalProps: SwDataDefProps = None

    def getDynamicLength(self):
        return self.dynamicLength

    def setDynamicLength(self, value):
        self.dynamicLength = value
        return self

    def getPhysicalProps(self):
        return self.physicalProps

    def setPhysicalProps(self, value):
        self.physicalProps = value
        return self


class SystemSignalGroup(ARElement):
    """
    Represents a group of system signals, defining relationships
    between individual system signals and transforming signal references
    for grouped signal communication.
    """

    # SystemSignalGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemSignalRefs          [x] impl  [ ] docstring  [ ] test
    # [ ] addSystemSignalRefs          [x] impl  [ ] docstring  [ ] test
    # [ ] getTransformingSystemSignalRef [x] impl  [ ] docstring  [ ] test
    # [ ] setTransformingSystemSignalRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.systemSignalRefs: List[RefType] = []
        self.transformingSystemSignalRef: RefType = None

    def getSystemSignalRefs(self):
        return self.systemSignalRefs

    def addSystemSignalRefs(self, value: RefType):
        self.systemSignalRefs.append(value)
        return self

    def getTransformingSystemSignalRef(self):
        return self.transformingSystemSignalRef

    def setTransformingSystemSignalRef(self, value):
        self.transformingSystemSignalRef = value
        return self


class ISignalTriggering(Identifiable):
    """
    Defines triggering properties for interaction signals, specifying
    signal references, group references, and port references for
    signal-based communication triggering.
    """

    # ISignalTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalRef                [x] impl  [ ] docstring  [ ] test
    # [ ] setISignalRef                [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalGroupRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setISignalGroupRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalPortRefs           [x] impl  [ ] docstring  [ ] test
    # [ ] addISignalPortRef            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iSignalRef: RefType = None
        self.iSignalGroupRef: RefType = None
        self.iSignalPortRefs: List[RefType] = []

    def getISignalRef(self):
        return self.iSignalRef

    def setISignalRef(self, value):
        self.iSignalRef = value
        return self

    def getISignalGroupRef(self):
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value):
        self.iSignalGroupRef = value
        return self

    def getISignalPortRefs(self):
        return self.iSignalPortRefs

    def addISignalPortRef(self, value):
        self.iSignalPortRefs.append(value)
        return self


class SegmentPosition(ARObject):
    """
    Defines the position of a segment within a communication element,
    specifying byte order, length, and position properties for
    segmented communication.
    """

    # SegmentPosition method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] setSegmentByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentLength             [x] impl  [ ] docstring  [ ] test
    # [ ] setSegmentLength             [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentPosition           [x] impl  [ ] docstring  [ ] test
    # [ ] setSegmentPosition           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.segmentByteOrder: ByteOrderEnum = None
        self.segmentLength: Integer = None
        self.segmentPosition: Integer = None

    def getSegmentByteOrder(self):
        return self.segmentByteOrder

    def setSegmentByteOrder(self, value):
        if value is not None:
            self.segmentByteOrder = value
        return self

    def getSegmentLength(self):
        return self.segmentLength

    def setSegmentLength(self, value):
        if value is not None:
            self.segmentLength = value
        return self

    def getSegmentPosition(self):
        return self.segmentPosition

    def setSegmentPosition(self, value):
        if value is not None:
            self.segmentPosition = value
        return self


class MultiplexedPart(ARObject, ABC):
    """
    Abstract base class for multiplexed communication parts, defining
    common properties for dynamic and static multiplexed communication
    segments including segment positions.
    """

    # MultiplexedPart method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentPositions          [x] impl  [ ] docstring  [ ] test
    # [ ] addSegmentPosition           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is MultiplexedPart:
            raise TypeError("MultiplexedPart is an abstract class.")

        super().__init__()

        self.segmentPositions = []  # type: List[SegmentPosition]

    def getSegmentPositions(self):
        return self.segmentPositions

    def addSegmentPosition(self, value):
        if value is not None:
            self.segmentPositions.append(value)
        return self


class StaticPart(MultiplexedPart):
    """
    Defines a static part of multiplexed communication, specifying
    Interaction Protocol Data Unit (IPDU) references for fixed
    segments in multiplexed communication.
    """

    # StaticPart method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setIPduRef                   [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.iPduRef = None  # type: RefType

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        if value is not None:
            self.iPduRef = value
        return self


class DynamicPartAlternative(ARObject):
    """
    Defines an alternative for dynamic parts in multiplexed communication,
    specifying selector field codes, initial dynamic part properties,
    and Interaction Protocol Data Unit (IPDU) references.
    """

    # DynamicPartAlternative method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialDynamicPart        [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialDynamicPart        [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldCode         [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldCode         [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.initialDynamicPart = None  # type: Boolean
        self.iPduRef = None  # type: RefType
        self.selectorFieldCode = None  # type: Integer

    def getInitialDynamicPart(self):
        return self.initialDynamicPart

    def setInitialDynamicPart(self, value):
        if value is not None:
            self.initialDynamicPart = value
        return self

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        if value is not None:
            self.iPduRef = value
        return self

    def getSelectorFieldCode(self):
        return self.selectorFieldCode

    def setSelectorFieldCode(self, value):
        if value is not None:
            self.selectorFieldCode = value
        return self


class DynamicPart(MultiplexedPart):
    """
    Defines a dynamic part of multiplexed communication, specifying
    alternatives for variable segments in multiplexed communication
    based on selector field values.
    """

    # DynamicPart method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicPartAlternatives   [x] impl  [ ] docstring  [ ] test
    # [ ] addDynamicPartAlternative    [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.dynamicPartAlternatives = []  # type: List[DynamicPartAlternative]

    def getDynamicPartAlternatives(self):
        return self.dynamicPartAlternatives

    def addDynamicPartAlternative(self, value):
        if value is not None:
            self.dynamicPartAlternatives.append(value)
        return self


class MultiplexedIPdu(IPdu):
    """
    Represents a multiplexed Interaction Protocol Data Unit (IPDU)
    with dynamic and static parts, defining selector field properties
    and trigger modes for multiplexed communication.
    """

    # MultiplexedIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicPart               [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicPart               [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldByteOrder    [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldByteOrder    [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldLength       [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldLength       [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldStartPosition [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldStartPosition [x] impl  [ ] docstring  [ ] test
    # [ ] getStaticPart                [x] impl  [ ] docstring  [ ] test
    # [ ] setStaticPart                [x] impl  [ ] docstring  [ ] test
    # [ ] getTriggerMode               [x] impl  [ ] docstring  [ ] test
    # [ ] setTriggerMode               [x] impl  [ ] docstring  [ ] test
    # [ ] getUnusedBitPattern          [x] impl  [ ] docstring  [ ] test
    # [ ] setUnusedBitPattern          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dynamicPart = None  # type: DynamicPart
        self.selectorFieldByteOrder = None  # type: ByteOrderEnum
        self.selectorFieldLength = None  # type: Integer
        self.selectorFieldStartPosition = None  # type: Integer
        self.staticPart = None  # type: StaticPart
        self.triggerMode = None  # type: TriggerMode
        self.unusedBitPattern = None  # type: Integer

    def getDynamicPart(self):
        return self.dynamicPart

    def setDynamicPart(self, value):
        if value is not None:
            self.dynamicPart = value
        return self

    def getSelectorFieldByteOrder(self):
        return self.selectorFieldByteOrder

    def setSelectorFieldByteOrder(self, value):
        if value is not None:
            self.selectorFieldByteOrder = value
        return self

    def getSelectorFieldLength(self):
        return self.selectorFieldLength

    def setSelectorFieldLength(self, value):
        if value is not None:
            self.selectorFieldLength = value
        return self

    def getSelectorFieldStartPosition(self):
        return self.selectorFieldStartPosition

    def setSelectorFieldStartPosition(self, value):
        if value is not None:
            self.selectorFieldStartPosition = value
        return self

    def getStaticPart(self):
        return self.staticPart

    def setStaticPart(self, value):
        if value is not None:
            self.staticPart = value
        return self

    def getTriggerMode(self):
        return self.triggerMode

    def setTriggerMode(self, value):
        if value is not None:
            self.triggerMode = value
        return self

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        if value is not None:
            self.unusedBitPattern = value
        return self


class GeneralPurposePdu(Pdu):
    """
    Represents a general-purpose Protocol Data Unit (PDU) for flexible
    communication patterns that don't fit into specific PDU categories.
    """

    # GeneralPurposePdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class GeneralPurposeIPdu(IPdu):
    """
    Represents a general-purpose Interaction Protocol Data Unit (IPDU) for flexible
    interaction-based communication patterns that don't fit into specific IPDU categories.
    """

    # GeneralPurposeIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SecureCommunicationPropsSet(FibexElement):
    """
    Collection of properties used to configure SecuredIPdus.
    """

    # SecureCommunicationPropsSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.45, p.370
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createSecureCommunicationAuthenticationProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthenticationProps                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSecureCommunicationFreshnessProps          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessProps                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SecureCommunicationPropsSet.
        """
        super().__init__(parent, short_name)

        # Authentication properties used to configure Secured IPdus.
        self.authenticationProps: List[SecureCommunicationAuthenticationProps] = []

        # Freshness properties used to configure SecuredIPdus.
        self.freshnessProps: List[SecureCommunicationFreshnessProps] = []

    def createSecureCommunicationAuthenticationProps(self, short_name: str) -> SecureCommunicationAuthenticationProps:
        """
        Authentication properties used to configure Secured IPdus.
        """
        if not self.IsElementExists(short_name, SecureCommunicationAuthenticationProps):
            props = SecureCommunicationAuthenticationProps(self, short_name)
            self.addElement(props)
            self.authenticationProps.append(props)
        return self.getElement(short_name, SecureCommunicationAuthenticationProps)

    def getAuthenticationProps(self) -> List[SecureCommunicationAuthenticationProps]:
        """
        Authentication properties used to configure Secured IPdus.
        """
        return self.authenticationProps

    def createSecureCommunicationFreshnessProps(self, short_name: str) -> SecureCommunicationFreshnessProps:
        """
        Freshness properties used to configure SecuredIPdus.
        """
        if not self.IsElementExists(short_name, SecureCommunicationFreshnessProps):
            props = SecureCommunicationFreshnessProps(self, short_name)
            self.addElement(props)
            self.freshnessProps.append(props)
        return self.getElement(short_name, SecureCommunicationFreshnessProps)

    def getFreshnessProps(self) -> List[SecureCommunicationFreshnessProps]:
        """
        Freshness properties used to configure SecuredIPdus.
        """
        return self.freshnessProps


class UserDefinedPdu(Pdu):
    """
    Allows to describe PDU-based communication over Complex Communication Drivers.

    If a new BSW module is added above the BusIf (e.g. a new Nm module) then this
    Pdu element shall be used to describe the communication.

    Requirements:
        atp.recommendedPackage=Pdus

    Attributes:
        cddType: Optional attribute that defines the CDD (Complex Device Driver)
            that transmits or receives the UserDefinedPdu. If several CDDs are
            defined this attribute is used to distinguish between them.
    """

    # UserDefinedPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCddType                   [x] impl  [ ] docstring  [ ] test
    # [ ] setCddType                   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.cddType: String = None

    def getCddType(self):
        return self.cddType

    def setCddType(self, value):
        self.cddType = value
        return self


class UserDefinedIPdu(IPdu):
    """
    Represents a user-defined Interaction Protocol Data Unit (IPDU) that allows for custom
    interaction-based communication patterns defined by the user rather than following standard IPDU types.
    """

    # UserDefinedIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCddType                   [x] impl  [ ] docstring  [ ] test
    # [ ] setCddType                   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.cddType: ARLiteral = None

    def getCddType(self):
        return self.cddType

    def setCddType(self, value):
        self.cddType = value
        return self


class SecureCommunicationAuthenticationProps(Identifiable):
    """
    Authentication properties used to configure SecuredIPdus.
    """

    # SecureCommunicationAuthenticationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.47, p.371
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAuthInfoTxLength            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthInfoTxLength            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SecureCommunicationAuthenticationProps.
        """
        super().__init__(parent, short_name)

        # This attribute defines the length in bits of the authentication code to be included in the payload of the authenticated Pdu.
        self.authInfoTxLength: Optional[PositiveInteger] = None

    def getAuthInfoTxLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bits of the authentication code to be included in the payload of the authenticated Pdu.
        """
        return self.authInfoTxLength

    def setAuthInfoTxLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationAuthenticationProps":
        """
        This attribute defines the length in bits of the authentication code to be included in the payload of the authenticated Pdu.
        A None value is a no-op and does not overwrite an existing authInfoTxLength.
        """
        if value is not None:
            self.authInfoTxLength = value
        return self


class SecureCommunicationFreshnessProps(Identifiable):
    """
    Freshness properties used to configure SecuredIPdus.
    """

    # SecureCommunicationFreshnessProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.46, p.371
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFreshnessCounterSyncAttempts            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessCounterSyncAttempts            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessTimestampTimePeriodFactor      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessTimestampTimePeriodFactor      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessValueLength                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessValueLength                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessValueTxLength                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessValueTxLength                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUseFreshnessTimestamp                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUseFreshnessTimestamp                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SecureCommunicationFreshnessProps.
        """
        super().__init__(parent, short_name)

        # This attribute defines the number of Freshness Counter re-synchronization attempts when a verification failed for a Secured I-PDU. If the value is zero, there will be no additional verification attempt to synchronize with a potentially better fitting Freshness Counter value. This attribute is only applicable if useFreshnessTimestamp is FALSE.
        self.freshnessCounterSyncAttempts: Optional[PositiveInteger] = None

        # This attribute defines a factor that specifies the time period for the Freshness Timestamp. It holds a multiplication factor that specifies the concrete meaning of a Freshness Timestamp increment by one on basis of microseconds.
        self.freshnessTimestampTimePeriodFactor: Optional[PositiveInteger] = None

        # This attribute defines the complete length in bits of the Freshness Value. As long as the key doesn't change the counter shall not overflow. The length of the counter shall be determined based on the expected life time of the corresponding key and frequency of usage of the counter.
        self.freshnessValueLength: Optional[PositiveInteger] = None

        # This attribute defines the length in bits of the Freshness Value to be included in the payload of the Secured I-PDU. This length is specific to the least significant bits of the complete Freshness Counter. If the attribute is 0 no Freshness Value is included in the Secured I-PDU.
        self.freshnessValueTxLength: Optional[PositiveInteger] = None

        # This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. The value is set to TRUE when Timestamps are used.
        self.useFreshnessTimestamp: Optional[Boolean] = None

    def getFreshnessCounterSyncAttempts(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the number of Freshness Counter re-synchronization attempts when a verification failed for a Secured I-PDU. If the value is zero, there will be no additional verification attempt to synchronize with a potentially better fitting Freshness Counter value. This attribute is only applicable if useFreshnessTimestamp is FALSE.
        """
        return self.freshnessCounterSyncAttempts

    def setFreshnessCounterSyncAttempts(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines the number of Freshness Counter re-synchronization attempts when a verification failed for a Secured I-PDU. If the value is zero, there will be no additional verification attempt to synchronize with a potentially better fitting Freshness Counter value. This attribute is only applicable if useFreshnessTimestamp is FALSE.
        A None value is a no-op and does not overwrite an existing freshnessCounterSyncAttempts.
        """
        if value is not None:
            self.freshnessCounterSyncAttempts = value
        return self

    def getFreshnessTimestampTimePeriodFactor(self) -> Optional[PositiveInteger]:
        """
        This attribute defines a factor that specifies the time period for the Freshness Timestamp. It holds a multiplication factor that specifies the concrete meaning of a Freshness Timestamp increment by one on basis of microseconds.
        """
        return self.freshnessTimestampTimePeriodFactor

    def setFreshnessTimestampTimePeriodFactor(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines a factor that specifies the time period for the Freshness Timestamp. It holds a multiplication factor that specifies the concrete meaning of a Freshness Timestamp increment by one on basis of microseconds.
        A None value is a no-op and does not overwrite an existing freshnessTimestampTimePeriodFactor.
        """
        if value is not None:
            self.freshnessTimestampTimePeriodFactor = value
        return self

    def getFreshnessValueLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the complete length in bits of the Freshness Value. As long as the key doesn't change the counter shall not overflow. The length of the counter shall be determined based on the expected life time of the corresponding key and frequency of usage of the counter.
        """
        return self.freshnessValueLength

    def setFreshnessValueLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines the complete length in bits of the Freshness Value. As long as the key doesn't change the counter shall not overflow. The length of the counter shall be determined based on the expected life time of the corresponding key and frequency of usage of the counter.
        A None value is a no-op and does not overwrite an existing freshnessValueLength.
        """
        if value is not None:
            self.freshnessValueLength = value
        return self

    def getFreshnessValueTxLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bits of the Freshness Value to be included in the payload of the Secured I-PDU. This length is specific to the least significant bits of the complete Freshness Counter. If the attribute is 0 no Freshness Value is included in the Secured I-PDU.
        """
        return self.freshnessValueTxLength

    def setFreshnessValueTxLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines the length in bits of the Freshness Value to be included in the payload of the Secured I-PDU. This length is specific to the least significant bits of the complete Freshness Counter. If the attribute is 0 no Freshness Value is included in the Secured I-PDU.
        A None value is a no-op and does not overwrite an existing freshnessValueTxLength.
        """
        if value is not None:
            self.freshnessValueTxLength = value
        return self

    def getUseFreshnessTimestamp(self) -> Optional[Boolean]:
        """
        This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. The value is set to TRUE when Timestamps are used.
        """
        return self.useFreshnessTimestamp

    def setUseFreshnessTimestamp(self, value: Optional[Boolean]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. The value is set to TRUE when Timestamps are used.
        A None value is a no-op and does not overwrite an existing useFreshnessTimestamp.
        """
        if value is not None:
            self.useFreshnessTimestamp = value
        return self
