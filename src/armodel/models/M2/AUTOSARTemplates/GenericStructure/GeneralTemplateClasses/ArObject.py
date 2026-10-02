"""
Abstract base class of all AUTOSAR objects.
"""

from __future__ import annotations


from abc import ABC
from typing import TYPE_CHECKING, Dict, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
        DateTime,
        String,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import DiagnosticParameterIdent
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDataElement, DiagnosticDebounceAlgorithmProps


class ARObject(ABC):
    """
    Abstract base class of all AUTOSAR meta-classes
    (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 6.1).
    """

    # ARObject method parity checklist:
    # Spec verified: R23-11
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 6.1, p.192
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setChecksum   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getChecksum   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimestamp  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimestamp  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    #
    # Internal members (no spec counterpart, cf. CollectableElement decision):
    #   parent     — structural link to the owning object
    #   getTagName — parser helper for namespace-stripped tag names

    def __init__(self):
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")

        self.parent: Optional[ARObject] = None

        # Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum.
        self.checksum: Optional[String] = None

        # Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        self.timestamp: Optional[DateTime] = None

    def getChecksum(self) -> Optional[String]:
        """
        Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum.
        """
        return self.checksum

    def setChecksum(self, value: Optional[String]) -> ARObject:
        """
        Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum. A None value is a no-op and does not overwrite an existing checksum.
        """
        if value is not None:
            self.checksum = value
        return self

    def getTimestamp(self) -> Optional[DateTime]:
        """
        Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        """
        return self.timestamp

    def setTimestamp(self, value: Optional[DateTime]) -> ARObject:
        """
        Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp. A None value is a no-op and does not overwrite an existing timestamp.
        """
        if value is not None:
            self.timestamp = value
        return self

    def getTagName(self, tag: str, nsmap: Dict) -> str:
        """
        Gets the tag name without namespace prefix.

        Args:
            tag: The full tag name with namespace prefix
            nsmap: The namespace map dictionary

        Returns:
            The tag name without namespace prefix
        """
        return tag.replace("{%s}" % nsmap["xmlns"], "")


class AbstractCondition(ARObject, ABC):
    pass


class AbstractMultiplicityRestriction(ARObject, ABC):
    pass


class AttributeCondition(AbstractCondition, ABC):
    pass


class AggregationCondition(AttributeCondition):
    pass


class ArParameterInImplementationDataInstanceRef(ARObject):
    pass


class Baseline(ARObject):
    pass


class CalibrationParameterValue(ARObject):
    pass


class ClassTailoring(ARObject, ABC):
    pass


class ClientServerOperationBlueprintMapping(ARObject):
    pass


class DiagnosticAbstractParameter(ARObject, ABC):
    """
    This meta-class represents an abstract base class for modeling a diagnostic parameter.

    [constr_1790] Existence of attribute DiagnosticAbstractParameter.bitOffset: For each DiagnosticParameter, attribute bitOffset shall exist at the time when the DEXT is complete.
    [constr_1470] Value of DiagnosticAbstractParameter.bitOffset: The value of DiagnosticAbstractParameter.bitOffset shall only be set to a multiple of 8 at the time when the DEXT is complete.
    """

    # DiagnosticAbstractParameter method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.8, p.37
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBitOffset       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitOffset       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDataElement  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElement     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getParameterSize   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParameterSize   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Subclasses: DiagnosticParameter (Table 4.5), DiagnosticParameterElement
    # (Table 4.6). PDF Mult of dataElement is 0..1 — the XSD resolves the
    # atpVariation/atpSplitable stereotypes into the DATA-ELEMENTS wrapper with an
    # unbounded choice (single-field model stays PDF-correct, Rule 0001.4); the
    # wrapper is absorbed by the reusable read/write helpers (Rule 0001.7).
    # __init__ calls ARObject.__init__ directly (Referrable precedent): cooperative
    # super() would dispatch to Identifiable.__init__(parent, short_name) under the
    # DiagnosticParameterElement(DiagnosticAbstractParameter, Identifiable) MRO and
    # fail on missing arguments.

    def __init__(self):
        if type(self) is DiagnosticAbstractParameter:
            raise TypeError("DiagnosticAbstractParameter is an abstract class.")

        ARObject.__init__(self)

        # This represents the bitOffset of the DiagnosticParameter. The value of the bitOffset shall always be interpreted as relative to the start of the enclosing DiagnosticData Identifier, DiagnosticParameterIdentifier, or Diagnostic RoutineSubfunction.
        self.bitOffset: Optional[PositiveInteger] = None

        # This represents the related dataElement of the Diagnostic Parameter
        self.dataElement: Optional[DiagnosticDataElement] = None

        # This attribute allows for the specification of the parameter size. This information is relevant if there is a gap between one diagnostic parameter and the following diagnostic parameter (or the tail of the telegram). The unit is bit and the values shall be multiples of 8.
        self.parameterSize: Optional[PositiveInteger] = None

    def getBitOffset(self) -> Optional[PositiveInteger]:
        """
        This represents the bitOffset of the DiagnosticParameter. The value of the bitOffset shall always be interpreted as relative to the start of the enclosing DiagnosticData Identifier, DiagnosticParameterIdentifier, or Diagnostic RoutineSubfunction.
        """
        return self.bitOffset

    def setBitOffset(self, value: Optional[PositiveInteger]) -> DiagnosticAbstractParameter:
        """
        This represents the bitOffset of the DiagnosticParameter. The value of the bitOffset shall always be interpreted as relative to the start of the enclosing DiagnosticData Identifier, DiagnosticParameterIdentifier, or Diagnostic RoutineSubfunction.
        A None value is a no-op and does not overwrite an existing bitOffset.
        """
        if value is not None:
            self.bitOffset = value
        return self

    def createDataElement(self, short_name: str) -> DiagnosticDataElement:
        """
        This represents the related dataElement of the Diagnostic Parameter
        The existing data element is returned when the short name already exists (no duplicate creation).
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDataElement

        if self.dataElement is None or self.dataElement.getShortName() != short_name:
            self.dataElement = DiagnosticDataElement(self, short_name)
        return self.dataElement

    def getDataElement(self) -> Optional[DiagnosticDataElement]:
        """
        This represents the related dataElement of the Diagnostic Parameter
        """
        return self.dataElement

    def getParameterSize(self) -> Optional[PositiveInteger]:
        """
        This attribute allows for the specification of the parameter size. This information is relevant if there is a gap between one diagnostic parameter and the following diagnostic parameter (or the tail of the telegram). The unit is bit and the values shall be multiples of 8.
        """
        return self.parameterSize

    def setParameterSize(self, value: Optional[PositiveInteger]) -> DiagnosticAbstractParameter:
        """
        This attribute allows for the specification of the parameter size. This information is relevant if there is a gap between one diagnostic parameter and the following diagnostic parameter (or the tail of the telegram). The unit is bit and the values shall be multiples of 8.
        A None value is a no-op and does not overwrite an existing parameterSize.
        """
        if value is not None:
            self.parameterSize = value
        return self


class DiagnosticClearResetEmissionRelatedInfo(ARObject):
    pass


class DiagnosticComControlSpecificChannel(ARObject):
    """
    This represents the ability to add further attributes to the definition of a specific channel that is subject to the diagnostic service "communication control".
    """

    # DiagnosticComControlSpecificChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.65, p.109
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSpecificChannel         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSpecificChannel         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSpecificPhysicalChannel [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSpecificPhysicalChannel [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubnetNumber            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSubnetNumber            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the affected CommunicationCluster in the role specificChannel
        self.specificChannel: Optional[RefType] = None

        # This represents the affected specific EthernetPhysicalChannel.
        self.specificPhysicalChannel: Optional[RefType] = None

        # This represents the applicable subnet number (which is an arbitrary number ranging from 1..14)
        self.subnetNumber: Optional[PositiveInteger] = None

    def getSpecificChannel(self) -> Optional[RefType]:
        """
        This represents the affected CommunicationCluster in the role specificChannel
        """
        return self.specificChannel

    def setSpecificChannel(self, value: Optional[RefType]) -> DiagnosticComControlSpecificChannel:
        """
        This represents the affected CommunicationCluster in the role specificChannel

        A None value is a no-op and does not overwrite an existing specificChannel.
        """
        if value is not None:
            self.specificChannel = value
        return self

    def getSpecificPhysicalChannel(self) -> Optional[RefType]:
        """
        This represents the affected specific EthernetPhysicalChannel.
        """
        return self.specificPhysicalChannel

    def setSpecificPhysicalChannel(self, value: Optional[RefType]) -> DiagnosticComControlSpecificChannel:
        """
        This represents the affected specific EthernetPhysicalChannel.

        A None value is a no-op and does not overwrite an existing specificPhysicalChannel.
        """
        if value is not None:
            self.specificPhysicalChannel = value
        return self

    def getSubnetNumber(self) -> Optional[PositiveInteger]:
        """
        This represents the applicable subnet number (which is an arbitrary number ranging from 1..14)
        """
        return self.subnetNumber

    def setSubnetNumber(self, value: Optional[PositiveInteger]) -> DiagnosticComControlSpecificChannel:
        """
        This represents the applicable subnet number (which is an arbitrary number ranging from 1..14)

        A None value is a no-op and does not overwrite an existing subnetNumber.
        """
        if value is not None:
            self.subnetNumber = value
        return self


class DiagnosticComControlSubNodeChannel(ARObject):
    """
    This represents the ability to add further attributes to the definition of a specific sub-node channel that is subject to the diagnostic service "communication control".
    """

    # DiagnosticComControlSubNodeChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.67, p.110
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSubNodeChannel             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSubNodeChannel             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubNodeNumber              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSubNodeNumber              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubNodePhysicalChannel     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSubNodePhysicalChannel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the affected CommunicationCluster in the role subNodeChannel
        self.subNodeChannel: Optional[RefType] = None

        # This represents the applicable subNode number. The value corresponds to the request message parameter nodeIdentificationNumber of diagnostic service CommunicationControl (0x28).
        self.subNodeNumber: Optional[PositiveInteger] = None

        # This represents the affected sub-node EthernetPhysicalChannel.
        self.subNodePhysicalChannel: Optional[RefType] = None

    def getSubNodeChannel(self) -> Optional[RefType]:
        """
        This represents the affected CommunicationCluster in the role subNodeChannel
        """
        return self.subNodeChannel

    def setSubNodeChannel(self, value: Optional[RefType]) -> DiagnosticComControlSubNodeChannel:
        """
        This represents the affected CommunicationCluster in the role subNodeChannel

        A None value is a no-op and does not overwrite an existing subNodeChannel.
        """
        if value is not None:
            self.subNodeChannel = value
        return self

    def getSubNodeNumber(self) -> Optional[PositiveInteger]:
        """
        This represents the applicable subNode number. The value corresponds to the request message parameter nodeIdentificationNumber of diagnostic service CommunicationControl (0x28).
        """
        return self.subNodeNumber

    def setSubNodeNumber(self, value: Optional[PositiveInteger]) -> DiagnosticComControlSubNodeChannel:
        """
        This represents the applicable subNode number. The value corresponds to the request message parameter nodeIdentificationNumber of diagnostic service CommunicationControl (0x28).

        A None value is a no-op and does not overwrite an existing subNodeNumber.
        """
        if value is not None:
            self.subNodeNumber = value
        return self

    def getSubNodePhysicalChannel(self) -> Optional[RefType]:
        """
        This represents the affected sub-node EthernetPhysicalChannel.
        """
        return self.subNodePhysicalChannel

    def setSubNodePhysicalChannel(self, value: Optional[RefType]) -> DiagnosticComControlSubNodeChannel:
        """
        This represents the affected sub-node EthernetPhysicalChannel.

        A None value is a no-op and does not overwrite an existing subNodePhysicalChannel.
        """
        if value is not None:
            self.subNodePhysicalChannel = value
        return self


class DiagnosticCommonProps(ARObject):
    """
    This meta-class aggregates a number of common properties that are shared among a diagnostic extract.

    [constr_10042] Existence of attribute DiagnosticCommonProps.defaultEndianness: One of the following conditions shall be fulfilled at the time when the DEXT is complete: DiagnosticCommonProps.defaultEndianness exists. The attribute DiagnosticParameter.dataElement.swDataDefProps.baseType.baseTypeDefinition.baseTypeEncoding exist for all DiagnosticParameters defined in the context of the DiagnosticContributionSet.
    [constr_10043] Existence of attribute DiagnosticCommonProps.resetConfirmedBitOnOverflow: Attribute DiagnosticCommonProps.resetConfirmedBitOnOverflow shall exist at the time when the DEXT is complete.
    [constr_10044] Existence of attribute DiagnosticCommonProps.occurrenceCounterProcessing: If, in the context of a DiagnosticContributionSet, a DiagnosticDemProvidedDataMapping exists where attribute DiagnosticDemProvidedDataMapping.dataProvider is set to the value DEM_OCCCTR, then attribute DiagnosticCommonProps.occurrenceCounterProcessing shall exist at the time when the DEXT is complete.
    [constr_10089] Existence of attribute DiagnosticCommonProps.eventCombinationReportingBehavior: Attribute DiagnosticCommonProps.eventCombinationReportingBehavior is always optional and shall be set to the value DiagnosticEventCombinationReportingBehaviorEnum.reportingInChronlogicalOrderOldestFirst only if attribute DiagnosticCommonProps.typeOfEventCombinationSupported is set to the value DiagnosticEventCombinationBehaviorEnum.eventCombinationOnRetrieval. If it is missing, then the reporting order is not specified. This rule shall be imposed at the time when the DEXT is complete.
    [constr_10419] Existence of the attribute DiagnosticCommonProps.resetPendingBitOnOverflow: Attribute DiagnosticCommonProps.resetPendingBitOnOverflow shall exist at the time when the DEXT is complete.
    """

    # DiagnosticCommonProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.19, p.65
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAuthenticationTimeout                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAuthenticationTimeout                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDebounceAlgorithmProps                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDebounceAlgorithmProps                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDefaultEndianness                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultEndianness                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEventCombinationReportingBehavior                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventCombinationReportingBehavior                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumberOfRequestCorrectlyReceivedResponsePending [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumberOfRequestCorrectlyReceivedResponsePending [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOccurrenceCounterProcessing                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOccurrenceCounterProcessing                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResetConfirmedBitOnOverflow                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResetConfirmedBitOnOverflow                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResetPendingBitOnOverflow                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResetPendingBitOnOverflow                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponseOnAllRequestSids                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseOnAllRequestSids                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponseOnSecondDeclinedRequest                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseOnSecondDeclinedRequest                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTypeOfEventCombinationSupported                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTypeOfEventCombinationSupported                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the time (in seconds) that the authentication state is maintained in default-session if there is no communication from the authenticated client.
        self.authenticationTimeout: Optional[TimeValue] = None

        # Defines the used debounce algorithms relevant in the context of the enclosing DiagnosticCommonProps. Usually, there is a variety of debouncing algorithms to take into account and therefore the multiplicity of this aggregation is set to 0..*.
        self.debounceAlgorithmProps: List[DiagnosticDebounceAlgorithmProps] = []

        # Defines the default endianness of the data belonging to a DID or RID which is applicable if the DiagnosticDataElement does not define the endianness via the swDataDefProps.baseType attribute.
        self.defaultEndianness: Optional[ByteOrderEnum] = None

        # In case of EventCombination on Retrieval, this attribute specifies if a specific order of reporting is to be maintained.
        self.eventCombinationReportingBehavior: Optional[DiagnosticEventCombinationReportingBehaviorEnum] = None

        # Maximum number of negative responses with response code 0x78 (requestCorrectlyReceived-ResponsePending) allowed per request. DCM will send a negative response with response code 0x10 (generalReject), in case the limit value gets reached. Value 0xFF means that no limit number of NRC 0x78 response apply.
        self.maxNumberOfRequestCorrectlyReceivedResponsePending: Optional[PositiveInteger] = None

        # This attribute defines the consideration of the fault confirmation process for the occurrence counter.
        self.occurrenceCounterProcessing: Optional[DiagnosticOccurrenceCounterProcessingEnum] = None

        # This attribute defines, whether the confirmed bit is reset or not while an event memory entry will be displaced.
        self.resetConfirmedBitOnOverflow: Optional[Boolean] = None

        # This attribute defines, whether the pending bit is reset or not while an event memory entry will be displaced. In order to be compliant to ISO 14229-1 [1], this parameter needs to be set to "false".
        self.resetPendingBitOnOverflow: Optional[Boolean] = None

        # If set to FALSE the DCM will not respond to diagnostic request that contains a service ID which is in the range from 0x40 to 0x7F or in the range from 0xC0 to 0xFF (Response IDs).
        self.responseOnAllRequestSids: Optional[Boolean] = None

        # Defines the reaction upon a second request (ClientB) that can not be processed (e.g. due to priority assessment). TRUE: when the second request (Client B) can not be processed, it shall be answered with NRC21 BusyRepeat Request. FALSE: when the second request (Client B) can not be processed, it shall not be responded.
        self.responseOnSecondDeclinedRequest: Optional[Boolean] = None

        # Select type of Event Combination support.
        self.typeOfEventCombinationSupported: Optional[DiagnosticEventCombinationBehaviorEnum] = None

    def getAuthenticationTimeout(self) -> Optional[TimeValue]:
        """
        This attribute defines the time (in seconds) that the authentication state is maintained in default-session if there is no communication from the authenticated client.
        """
        return self.authenticationTimeout

    def setAuthenticationTimeout(self, value: Optional[TimeValue]) -> DiagnosticCommonProps:
        """
        This attribute defines the time (in seconds) that the authentication state is maintained in default-session if there is no communication from the authenticated client.
        A None value is a no-op and does not overwrite an existing authenticationTimeout.
        """
        if value is not None:
            self.authenticationTimeout = value
        return self

    def createDebounceAlgorithmProps(self, short_name: str) -> DiagnosticDebounceAlgorithmProps:
        """
        Defines the used debounce algorithms relevant in the context of the enclosing DiagnosticCommonProps. Usually, there is a variety of debouncing algorithms to take into account and therefore the multiplicity of this aggregation is set to 0..*.
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDebounceAlgorithmProps

        for props in self.debounceAlgorithmProps:
            if props.getShortName() == short_name:
                return props
        props = DiagnosticDebounceAlgorithmProps(self, short_name)
        self.debounceAlgorithmProps.append(props)
        return props

    def getDebounceAlgorithmProps(self) -> List[DiagnosticDebounceAlgorithmProps]:
        """
        Defines the used debounce algorithms relevant in the context of the enclosing DiagnosticCommonProps. Usually, there is a variety of debouncing algorithms to take into account and therefore the multiplicity of this aggregation is set to 0..*.
        """
        return self.debounceAlgorithmProps

    def getDefaultEndianness(self) -> Optional[ByteOrderEnum]:
        """
        Defines the default endianness of the data belonging to a DID or RID which is applicable if the DiagnosticDataElement does not define the endianness via the swDataDefProps.baseType attribute.
        """
        return self.defaultEndianness

    def setDefaultEndianness(self, value: Optional[ByteOrderEnum]) -> DiagnosticCommonProps:
        """
        Defines the default endianness of the data belonging to a DID or RID which is applicable if the DiagnosticDataElement does not define the endianness via the swDataDefProps.baseType attribute.
        A None value is a no-op and does not overwrite an existing defaultEndianness.
        """
        if value is not None:
            self.defaultEndianness = value
        return self

    def getEventCombinationReportingBehavior(self) -> Optional[DiagnosticEventCombinationReportingBehaviorEnum]:
        """
        In case of EventCombination on Retrieval, this attribute specifies if a specific order of reporting is to be maintained.
        """
        return self.eventCombinationReportingBehavior

    def setEventCombinationReportingBehavior(self, value: Optional[DiagnosticEventCombinationReportingBehaviorEnum]) -> DiagnosticCommonProps:
        """
        In case of EventCombination on Retrieval, this attribute specifies if a specific order of reporting is to be maintained.
        A None value is a no-op and does not overwrite an existing eventCombinationReportingBehavior.
        """
        if value is not None:
            self.eventCombinationReportingBehavior = value
        return self

    def getMaxNumberOfRequestCorrectlyReceivedResponsePending(self) -> Optional[PositiveInteger]:
        """
        Maximum number of negative responses with response code 0x78 (requestCorrectlyReceived-ResponsePending) allowed per request. DCM will send a negative response with response code 0x10 (generalReject), in case the limit value gets reached. Value 0xFF means that no limit number of NRC 0x78 response apply.
        """
        return self.maxNumberOfRequestCorrectlyReceivedResponsePending

    def setMaxNumberOfRequestCorrectlyReceivedResponsePending(self, value: Optional[PositiveInteger]) -> DiagnosticCommonProps:
        """
        Maximum number of negative responses with response code 0x78 (requestCorrectlyReceived-ResponsePending) allowed per request. DCM will send a negative response with response code 0x10 (generalReject), in case the limit value gets reached. Value 0xFF means that no limit number of NRC 0x78 response apply.
        A None value is a no-op and does not overwrite an existing maxNumberOfRequestCorrectlyReceivedResponsePending.
        """
        if value is not None:
            self.maxNumberOfRequestCorrectlyReceivedResponsePending = value
        return self

    def getOccurrenceCounterProcessing(self) -> Optional[DiagnosticOccurrenceCounterProcessingEnum]:
        """
        This attribute defines the consideration of the fault confirmation process for the occurrence counter.
        """
        return self.occurrenceCounterProcessing

    def setOccurrenceCounterProcessing(self, value: Optional[DiagnosticOccurrenceCounterProcessingEnum]) -> DiagnosticCommonProps:
        """
        This attribute defines the consideration of the fault confirmation process for the occurrence counter.
        A None value is a no-op and does not overwrite an existing occurrenceCounterProcessing.
        """
        if value is not None:
            self.occurrenceCounterProcessing = value
        return self

    def getResetConfirmedBitOnOverflow(self) -> Optional[Boolean]:
        """
        This attribute defines, whether the confirmed bit is reset or not while an event memory entry will be displaced.
        """
        return self.resetConfirmedBitOnOverflow

    def setResetConfirmedBitOnOverflow(self, value: Optional[Boolean]) -> DiagnosticCommonProps:
        """
        This attribute defines, whether the confirmed bit is reset or not while an event memory entry will be displaced.
        A None value is a no-op and does not overwrite an existing resetConfirmedBitOnOverflow.
        """
        if value is not None:
            self.resetConfirmedBitOnOverflow = value
        return self

    def getResetPendingBitOnOverflow(self) -> Optional[Boolean]:
        """
        This attribute defines, whether the pending bit is reset or not while an event memory entry will be displaced. In order to be compliant to ISO 14229-1 [1], this parameter needs to be set to "false".
        """
        return self.resetPendingBitOnOverflow

    def setResetPendingBitOnOverflow(self, value: Optional[Boolean]) -> DiagnosticCommonProps:
        """
        This attribute defines, whether the pending bit is reset or not while an event memory entry will be displaced. In order to be compliant to ISO 14229-1 [1], this parameter needs to be set to "false".
        A None value is a no-op and does not overwrite an existing resetPendingBitOnOverflow.
        """
        if value is not None:
            self.resetPendingBitOnOverflow = value
        return self

    def getResponseOnAllRequestSids(self) -> Optional[Boolean]:
        """
        If set to FALSE the DCM will not respond to diagnostic request that contains a service ID which is in the range from 0x40 to 0x7F or in the range from 0xC0 to 0xFF (Response IDs).
        """
        return self.responseOnAllRequestSids

    def setResponseOnAllRequestSids(self, value: Optional[Boolean]) -> DiagnosticCommonProps:
        """
        If set to FALSE the DCM will not respond to diagnostic request that contains a service ID which is in the range from 0x40 to 0x7F or in the range from 0xC0 to 0xFF (Response IDs).
        A None value is a no-op and does not overwrite an existing responseOnAllRequestSids.
        """
        if value is not None:
            self.responseOnAllRequestSids = value
        return self

    def getResponseOnSecondDeclinedRequest(self) -> Optional[Boolean]:
        """
        Defines the reaction upon a second request (ClientB) that can not be processed (e.g. due to priority assessment). TRUE: when the second request (Client B) can not be processed, it shall be answered with NRC21 BusyRepeat Request. FALSE: when the second request (Client B) can not be processed, it shall not be responded.
        """
        return self.responseOnSecondDeclinedRequest

    def setResponseOnSecondDeclinedRequest(self, value: Optional[Boolean]) -> DiagnosticCommonProps:
        """
        Defines the reaction upon a second request (ClientB) that can not be processed (e.g. due to priority assessment). TRUE: when the second request (Client B) can not be processed, it shall be answered with NRC21 BusyRepeat Request. FALSE: when the second request (Client B) can not be processed, it shall not be responded.
        A None value is a no-op and does not overwrite an existing responseOnSecondDeclinedRequest.
        """
        if value is not None:
            self.responseOnSecondDeclinedRequest = value
        return self

    def getTypeOfEventCombinationSupported(self) -> Optional[DiagnosticEventCombinationBehaviorEnum]:
        """
        Select type of Event Combination support.
        """
        return self.typeOfEventCombinationSupported

    def setTypeOfEventCombinationSupported(self, value: Optional[DiagnosticEventCombinationBehaviorEnum]) -> DiagnosticCommonProps:
        """
        Select type of Event Combination support.
        A None value is a no-op and does not overwrite an existing typeOfEventCombinationSupported.
        """
        if value is not None:
            self.typeOfEventCombinationSupported = value
        return self


class DiagnosticConnectedIndicator(ARObject):
    pass


class DiagnosticControlEnableMaskBit(ARObject):
    """This meta-class has the ability to represent one bit in the control enable mask record."""

    # DiagnosticControlEnableMaskBit method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.83, p.119
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBitNumber               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitNumber               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addControlledDataElement   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getControlledDataElements  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute represents the bit number of the bit in the control mask record. Bit number 0 is the most significant bit (MSB) in the first byte of the CEMR in the network presentation.
        self.bitNumber: Optional[PositiveInteger] = None

        # This reference represents the collection of DiagnosticDataElements that are controlled by this bit of the control mask record.
        self.controlledDataElement: List[RefType] = []

    def getBitNumber(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the bit number of the bit in the control mask record. Bit number 0 is the most significant bit (MSB) in the first byte of the CEMR in the network presentation.
        """
        return self.bitNumber

    def setBitNumber(self, value: Optional[PositiveInteger]) -> DiagnosticControlEnableMaskBit:
        """
        This attribute represents the bit number of the bit in the control mask record. Bit number 0 is the most significant bit (MSB) in the first byte of the CEMR in the network presentation.

        A None value is a no-op and does not overwrite an existing bitNumber.
        """
        if value is not None:
            self.bitNumber = value
        return self

    def addControlledDataElement(self, value: Optional[RefType]) -> DiagnosticControlEnableMaskBit:
        """
        This reference represents the collection of DiagnosticDataElements that are controlled by this bit of the control mask record.

        A None value is a no-op and does not append a controlledDataElement.
        """
        if value is not None:
            self.controlledDataElement.append(value)
        return self

    def getControlledDataElements(self) -> List[RefType]:
        """
        This reference represents the collection of DiagnosticDataElements that are controlled by this bit of the control mask record.
        """
        return self.controlledDataElement


class DiagnosticEnableConditionPortMapping(ARObject):
    pass


class DiagnosticEnvModeCondition(ARObject):
    pass


class DiagnosticEventWindow(ARObject):
    """This represents the ability to define the characteristics of the applicable event window"""

    # DiagnosticEventWindow method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.103, p.133
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventWindowTime   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventWindowTime   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute clarifies the validity of the eventWindow
        self.eventWindowTime: Optional[DiagnosticEventWindowTimeEnum] = None

    def getEventWindowTime(self) -> Optional[DiagnosticEventWindowTimeEnum]:
        """
        This attribute clarifies the validity of the eventWindow
        """
        return self.eventWindowTime

    def setEventWindowTime(self, value: Optional[DiagnosticEventWindowTimeEnum]) -> DiagnosticEventWindow:
        """
        This attribute clarifies the validity of the eventWindow

        A None value is a no-op and does not overwrite an existing eventWindowTime.
        """
        if value is not None:
            self.eventWindowTime = value
        return self


class DiagnosticFimFunctionMapping(ARObject):
    pass


class DiagnosticFunctionIdentifierInhibit(ARObject):
    pass


class DiagnosticIumprGroupIdentifier(ARObject):
    pass


class DiagnosticMemoryDestination(ARObject, ABC):
    pass


class DiagnosticMemoryDestinationUserDefined(ARObject):
    pass


class DiagnosticParameter(DiagnosticAbstractParameter, VariationPointCapable):
    """
    This meta-class represents the ability to describe information relevant for the execution of a specific diagnostic service, i.e. it can be taken to parameterize the service.
    """

    # DiagnosticParameter method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.5, p.36
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createIdent     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIdent        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSupportInfo  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportInfo  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)

    def __init__(self):
        super().__init__()

        # The aggregation in the role ident provides the ability to make the DiagnosticAbstractParameter identifiable. From the semantical point of view, the AbstractDiagnostic Parameter is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let AbstractDiagnostic Parameter directly inherit from Identifiable). Stereotypes: atpIdentityContributor
        self.ident: Optional[DiagnosticParameterIdent] = None

        # This attribute represents the ability to define which bit of the support info byte is representing this part of the PID.
        self.supportInfo: Optional[DiagnosticParameterSupportInfo] = None

    def createIdent(self, short_name: str) -> DiagnosticParameterIdent:
        """
        The aggregation in the role ident provides the ability to make the DiagnosticAbstractParameter identifiable. From the semantical point of view, the AbstractDiagnostic Parameter is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let AbstractDiagnostic Parameter directly inherit from Identifiable).
        The existing ident is returned when the short name already exists (no duplicate creation).
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import DiagnosticParameterIdent

        if self.ident is None or self.ident.getShortName() != short_name:
            self.ident = DiagnosticParameterIdent(self, short_name)
        return self.ident

    def getIdent(self) -> Optional[DiagnosticParameterIdent]:
        """
        The aggregation in the role ident provides the ability to make the DiagnosticAbstractParameter identifiable. From the semantical point of view, the AbstractDiagnostic Parameter is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let AbstractDiagnostic Parameter directly inherit from Identifiable).
        """
        return self.ident

    def getSupportInfo(self) -> Optional[DiagnosticParameterSupportInfo]:
        """
        This attribute represents the ability to define which bit of the support info byte is representing this part of the PID.
        """
        return self.supportInfo

    def setSupportInfo(self, value: Optional[DiagnosticParameterSupportInfo]) -> DiagnosticParameter:
        """
        This attribute represents the ability to define which bit of the support info byte is representing this part of the PID.
        A None value is a no-op and does not overwrite an existing supportInfo.
        """
        if value is not None:
            self.supportInfo = value
        return self


class DiagnosticParameterElementAccess(ARObject):
    pass


class DiagnosticParameterSupportInfo(ARObject):
    pass


class DiagnosticPeriodicRate(ARObject):
    """This represents the ability to define a periodic rate for the specification of the "read data by periodic ID" diagnostic service."""

    # DiagnosticPeriodicRate method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.99, p.131
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPeriod                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPeriod                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPeriodicRateCategory      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPeriodicRateCategory      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the period of the DiagnosticPeriodicRate in seconds.
        self.period: Optional[TimeValue] = None

        # This attribute represents the category of the periodic rate.
        self.periodicRateCategory: Optional[DiagnosticPeriodicRateCategoryEnum] = None

    def getPeriod(self) -> Optional[TimeValue]:
        """
        This represents the period of the DiagnosticPeriodicRate in seconds.
        """
        return self.period

    def setPeriod(self, value: Optional[TimeValue]) -> DiagnosticPeriodicRate:
        """
        This represents the period of the DiagnosticPeriodicRate in seconds.

        A None value is a no-op and does not overwrite an existing period.
        """
        if value is not None:
            self.period = value
        return self

    def getPeriodicRateCategory(self) -> Optional[DiagnosticPeriodicRateCategoryEnum]:
        """
        This attribute represents the category of the periodic rate.
        """
        return self.periodicRateCategory

    def setPeriodicRateCategory(self, value: Optional[DiagnosticPeriodicRateCategoryEnum]) -> DiagnosticPeriodicRate:
        """
        This attribute represents the category of the periodic rate.

        A None value is a no-op and does not overwrite an existing periodicRateCategory.
        """
        if value is not None:
            self.periodicRateCategory = value
        return self


class DiagnosticReadMemoryByAddress(ARObject):
    pass


class DiagnosticRequestCurrentPowertrainData(ARObject):
    pass


class DiagnosticRequestDownloadClass(ARObject):
    pass


class DiagnosticRequestEmissionRelatedDTC(ARObject):
    pass


class DiagnosticRequestOnBoardMonitoringTestResultsClass(ARObject):
    pass


class DiagnosticServiceMappingDiagTarget(ARObject, ABC):
    pass


class DiagnosticServiceSwMapping(ARObject):
    pass


class DiagnosticSupportInfoByte(ARObject):
    pass


class DiagnosticTestIdentifier(ARObject):
    pass


class DiagnosticTroubleCodeJ1939(ARObject):
    pass


class DiagnosticTroubleCodeObd(ARObject):
    pass


class DiagnosticTroubleCodeProps(ARObject):
    pass


class DiagnosticTroubleCodeUds(ARObject):
    pass


class DiagnosticWriteMemoryByAddress(ARObject):
    pass


class EventObdReadinessGroup(ARObject):
    pass


class FMAttributeValue(ARObject):
    pass


class FMFeatureDecomposition(ARObject):
    pass


class InvertCondition(AbstractCondition):
    pass


class MultiplicityRestrictionWithSeverity(AbstractMultiplicityRestriction):
    pass


class PhysicalDimensionMapping(ARObject):
    pass


class PrimitiveAttributeCondition(AttributeCondition):
    pass


class ReferenceCondition(AttributeCondition):
    pass


class RestrictionWithSeverity(ARObject, ABC):
    pass


class RoleBasedResourceDependency(ARObject):
    """This class specifies a dependency between CpSoftwareClusterResources."""

    # RoleBasedResourceDependency method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.45, p.272
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getResourceRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResourceRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRole           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to resource for which the dependency is depicted.
        self.resourceRef: Optional[RefType] = None

        # This is attributes characterizes the kind of dependency
        self.role: Optional[Identifier] = None

    def getResourceRef(self) -> Optional[RefType]:
        """
        Reference to resource for which the dependency is depicted.
        """
        return self.resourceRef

    def setResourceRef(self, value: Optional[RefType]) -> RoleBasedResourceDependency:
        """
        Reference to resource for which the dependency is depicted.
        A None value is a no-op and does not overwrite an existing resourceRef.
        """
        if value is not None:
            self.resourceRef = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        This is attributes characterizes the kind of dependency
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> RoleBasedResourceDependency:
        """
        This is attributes characterizes the kind of dependency
        A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self


class RptHook(ARObject):
    pass


class RptProfile(ARObject):
    pass


class SpecificationScope(ARObject):
    pass


class SwAxisCont(ARObject):
    pass


class SwcModeManagerErrorEvent(ARObject):
    pass


class TextualCondition(AbstractCondition):
    pass


class AbstractGlobalTimeDomainProps(ARObject, ABC):
    pass


class BinaryManifestAddressableObject(ARObject, ABC):
    pass


class BinaryManifestItemValue(ARObject, ABC):
    pass


class BinaryManifestResource(ARObject, ABC):
    pass


class BusMirrorCanIdRangeMapping(ARObject):
    pass


class BusMirrorCanIdToCanIdMapping(ARObject):
    pass


class BusMirrorChannel(ARObject):
    pass


class BusMirrorChannelMappingCan(ARObject):
    pass


class BusMirrorChannelMappingIp(ARObject):
    pass


class BusMirrorLinPidToCanIdMapping(ARObject):
    pass


class CommonSignalPath(ARObject):
    pass


class ContainerIPdu(ARObject):
    pass


class CouplingElement(ARObject):
    pass


class CpSoftwareClusterCommunicationResourceProps(ARObject, ABC):
    pass


class DdsCpISignalToDdsTopicMapping(ARObject):
    pass


class DdsCpProvidedServiceInstance(ARObject):
    pass


class DdsCpQosProfile(ARObject):
    pass


class DdsCpServiceInstanceEvent(ARObject):
    pass


class DdsCpServiceInstanceOperation(ARObject):
    pass


class DdsCpTopic(ARObject):
    pass


class DdsDeadline(ARObject):
    pass


class DdsDestinationOrder(ARObject):
    pass


class DdsDurability(ARObject):
    pass


class DdsDurabilityService(ARObject):
    pass


class DdsHistory(ARObject):
    pass


class DdsLatencyBudget(ARObject):
    pass


class DdsLifespan(ARObject):
    pass


class DdsLiveliness(ARObject):
    pass


class DdsOwnership(ARObject):
    pass


class DdsOwnershipStrength(ARObject):
    pass


class DdsReliability(ARObject):
    pass


class DdsResourceLimits(ARObject):
    pass


class DdsTopicData(ARObject):
    pass


class DdsTransportPriority(ARObject):
    pass


class Dhcpv6Props(ARObject):
    pass


class EcuResourceEstimation(ARObject):
    pass


class EthGlobalTimeManagedCouplingPort(ARObject):
    pass


class EthTSynCrcFlags(ARObject):
    pass


class EthTSynSubTlvConfig(ARObject):
    pass


class EthernetWakeupSleepOnDatalineConfig(ARObject):
    pass


class FlexrayArTpChannel(ARObject):
    pass


class FlexrayTpEcu(ARObject):
    pass


class ForbiddenSignalPath(ARObject):
    pass


class GlobalTimeCorrectionProps(ARObject):
    pass


class GlobalTimeSlave(ARObject, ABC):
    pass


class IEEE1722TpAcfBusPart(ARObject, ABC):
    pass


class IEEE1722TpAcfLin(ARObject):
    pass


class IEEE1722TpConfig(ARObject):
    pass


class IdsmInstance(ARObject):
    pass


class IdsmTrafficLimitation(ARObject):
    pass


class Ipv4ArpProps(ARObject):
    pass


class Ipv4AutoIpProps(ARObject):
    pass


class Ipv4FragmentationProps(ARObject):
    pass


class Ipv4Props(ARObject):
    pass


class Ipv6FragmentationProps(ARObject):
    pass


class Ipv6NdpProps(ARObject):
    pass


class Ipv6Props(ARObject):
    pass


class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    pass


class J1939TpConfig(ARObject):
    pass


class J1939TpConnection(ARObject):
    pass


class J1939TpPg(ARObject):
    pass


class MappingConstraint(ARObject, ABC):
    pass


class NetworkSegmentIdentification(ARObject):
    pass


class NmCoordinator(ARObject):
    pass


class PermissibleSignalPath(ARObject):
    pass


class PncMapping(ARObject):
    pass


class RteEventInCompositionToOsTaskProxyMapping(ARObject):
    pass


class RteEventInSystemToOsTaskProxyMapping(ARObject):
    pass


class SecurityEventAggregationFilter(ARObject):
    pass


class SecurityEventContextMapping(ARObject, ABC):
    pass


class SecurityEventContextMappingCommConnector(ARObject):
    pass


class SecurityEventContextProps(ARObject):
    pass


class SecurityEventFilterChain(ARObject):
    pass


class SecurityEventStateFilter(ARObject):
    pass


class SeparateSignalPath(ARObject):
    pass


class SomeipSdServerServiceInstanceConfig(ARObject):
    pass


class SomeipTpConnection(ARObject):
    pass


class StreamFilterIEEE1722Tp(ARObject):
    pass


class StreamFilterIpv4Address(ARObject):
    pass


class StreamFilterIpv6Address(ARObject):
    pass


class StreamFilterMACAddress(ARObject):
    pass


class StreamFilterPortRange(ARObject):
    pass


class StreamFilterRuleDataLinkLayer(ARObject):
    pass


class StreamFilterRuleIpTp(ARObject):
    pass


class SwcToSwcOperationArguments(ARObject):
    pass


class SwcToSwcSignal(ARObject):
    pass


class SystemTiming(ARObject):
    pass


class TDCpSoftwareClusterMappingSet(ARObject):
    pass


class TransformationProps(ARObject, ABC):
    pass


class TriggerToSignalMapping(ARObject):
    pass


class TtcanCommunicationController(ARObject):
    pass


class UserDefinedCommunicationConnector(ARObject):
    pass


class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    pass


class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    pass


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    pass


class ComponentClustering(MappingConstraint):
    pass


class ComponentSeparation(MappingConstraint):
    pass


class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    pass


class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass


class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass


# Cycle-breaker (Rule 0005): PrimitiveTypes imports ARObject from this module, so the
# PositiveInteger name needed by DiagnosticAbstractParameter's annotations must be bound
# at the bottom, after every class above is defined. Placed here so get_type_hints can
# resolve the bitOffset/parameterSize annotations at runtime on Python 3.8.
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E402
    Boolean,
    ByteOrderEnum,
    DiagnosticEventCombinationBehaviorEnum,
    DiagnosticEventCombinationReportingBehaviorEnum,
    DiagnosticEventWindowTimeEnum,
    DiagnosticOccurrenceCounterProcessingEnum,
    DiagnosticPeriodicRateCategoryEnum,
    Identifier,
    PositiveInteger,
    RefType,
    TimeValue,
)
