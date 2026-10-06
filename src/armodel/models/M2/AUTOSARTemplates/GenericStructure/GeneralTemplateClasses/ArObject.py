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
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import DiagnosticParameterIdent
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDataElement, DiagnosticDebounceAlgorithmProps, DiagnosticFunctionInhibitSource


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


class Baseline(ARObject):
    pass


class CalibrationParameterValue(ARObject, VariationPointCapable):
    """
    Specifies instance specific calibration parameter values used to initialize the memory objects implementing calibration parameters in the generated RTE code. RTE generator will use the implInitValue to override the initial values specified for the DataPrototypes of a component type. The applInitValue is used to exchange init values with the component vendor not publishing the transformation algorithm between ApplicationDataTypes and ImplementationDataTypes or defining an instance specific initialization of components which are only defined with ApplicationDataTypes. Note: If both representations of init values are available these need to represent the same content. Note further that in this case an explicit mapping of ValueSpecification is not implemented because calibration parameters are delivered back after the calibration phase.

    [constr_1933] Existence of CalibrationParameterValue.initializedParameter: For each CalibrationParameterValue, the reference to meta-class ConstantSpecification in the role initializedParameter shall exist at the time when the contract phase generation is executed.
    """

    # CalibrationParameterValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.138, p.478
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplInitValue             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplInitValue             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImplInitValue             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImplInitValue             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInitializedParameterRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInitializedParameterRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)

    def __init__(self):
        super().__init__()

        # This is the initial value specification structured according to the ApplicationDataType
        self.applInitValue: Optional[ValueSpecification] = None

        # This is the initial value specification structured according to the ImplementationDataType
        self.implInitValue: Optional[ValueSpecification] = None

        # This represents the parameter that is initialized by the CalibrationParameterValue.
        self.initializedParameterRef: Optional[RefType] = None

    def getApplInitValue(self) -> Optional[ValueSpecification]:
        """
        This is the initial value specification structured according to the ApplicationDataType
        """
        return self.applInitValue

    def setApplInitValue(self, value: Optional[ValueSpecification]) -> CalibrationParameterValue:
        """
        This is the initial value specification structured according to the ApplicationDataType

        A None value is a no-op and does not overwrite an existing applInitValue.
        """
        if value is not None:
            self.applInitValue = value
        return self

    def getImplInitValue(self) -> Optional[ValueSpecification]:
        """
        This is the initial value specification structured according to the ImplementationDataType
        """
        return self.implInitValue

    def setImplInitValue(self, value: Optional[ValueSpecification]) -> CalibrationParameterValue:
        """
        This is the initial value specification structured according to the ImplementationDataType

        A None value is a no-op and does not overwrite an existing implInitValue.
        """
        if value is not None:
            self.implInitValue = value
        return self

    def getInitializedParameterRef(self) -> Optional[RefType]:
        """
        This represents the parameter that is initialized by the CalibrationParameterValue.
        """
        return self.initializedParameterRef

    def setInitializedParameterRef(self, value: Optional[RefType]) -> CalibrationParameterValue:
        """
        This represents the parameter that is initialized by the CalibrationParameterValue.

        A None value is a no-op and does not overwrite an existing initializedParameterRef.
        """
        if value is not None:
            self.initializedParameterRef = value
        return self


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
    """Description of indicators that are defined per DiagnosticEvent."""

    # DiagnosticConnectedIndicator method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.152, p.167
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBehavior                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBehavior                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHealingCycleRef                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHealingCycleRef                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHealingCycleCounterThreshold            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHealingCycleCounterThreshold            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIndicatorRef                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIndicatorRef                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIndicatorFailureCycleCounterThreshold   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIndicatorFailureCycleCounterThreshold   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Behavior of the linked indicator.
        self.behavior: Optional[DiagnosticConnectedIndicatorBehaviorEnum] = None

        # The deactivation of indicators per event is defined as healing of a diagnostic event. The operation cycle in which the warning indicator will be switched off is defined here.
        self.healingCycleRef: Optional[RefType] = None

        # This attribute defines the number of healing cycles for the WarningIndicatorOffCriteria Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.healingCycleCounterThreshold: Optional[PositiveInteger] = None

        # Reference to the used indicator.
        self.indicatorRef: Optional[RefType] = None

        # This attribute defines the number of failure cycles for the WarningIndicatorOnCriteria. Please note that this attribute is not relevant for the Adaptive Platform.
        self.indicatorFailureCycleCounterThreshold: Optional[PositiveInteger] = None

    def getBehavior(self) -> Optional[DiagnosticConnectedIndicatorBehaviorEnum]:
        """
        Behavior of the linked indicator.
        """
        return self.behavior

    def setBehavior(self, value: Optional[DiagnosticConnectedIndicatorBehaviorEnum]) -> DiagnosticConnectedIndicator:
        """
        Behavior of the linked indicator.

        A None value is a no-op and does not overwrite an existing behavior.
        """
        if value is not None:
            self.behavior = value
        return self

    def getHealingCycleRef(self) -> Optional[RefType]:
        """
        The deactivation of indicators per event is defined as healing of a diagnostic event. The operation cycle in which the warning indicator will be switched off is defined here.
        """
        return self.healingCycleRef

    def setHealingCycleRef(self, value: Optional[RefType]) -> DiagnosticConnectedIndicator:
        """
        The deactivation of indicators per event is defined as healing of a diagnostic event. The operation cycle in which the warning indicator will be switched off is defined here.

        A None value is a no-op and does not overwrite an existing healingCycleRef.
        """
        if value is not None:
            self.healingCycleRef = value
        return self

    def getHealingCycleCounterThreshold(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the number of healing cycles for the WarningIndicatorOffCriteria Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.healingCycleCounterThreshold

    def setHealingCycleCounterThreshold(self, value: Optional[PositiveInteger]) -> DiagnosticConnectedIndicator:
        """
        This attribute defines the number of healing cycles for the WarningIndicatorOffCriteria Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing healingCycleCounterThreshold.
        """
        if value is not None:
            self.healingCycleCounterThreshold = value
        return self

    def getIndicatorRef(self) -> Optional[RefType]:
        """
        Reference to the used indicator.
        """
        return self.indicatorRef

    def setIndicatorRef(self, value: Optional[RefType]) -> DiagnosticConnectedIndicator:
        """
        Reference to the used indicator.

        A None value is a no-op and does not overwrite an existing indicatorRef.
        """
        if value is not None:
            self.indicatorRef = value
        return self

    def getIndicatorFailureCycleCounterThreshold(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the number of failure cycles for the WarningIndicatorOnCriteria. Please note that this attribute is not relevant for the Adaptive Platform.
        """
        return self.indicatorFailureCycleCounterThreshold

    def setIndicatorFailureCycleCounterThreshold(self, value: Optional[PositiveInteger]) -> DiagnosticConnectedIndicator:
        """
        This attribute defines the number of failure cycles for the WarningIndicatorOnCriteria. Please note that this attribute is not relevant for the Adaptive Platform.

        A None value is a no-op and does not overwrite an existing indicatorFailureCycleCounterThreshold.
        """
        if value is not None:
            self.indicatorFailureCycleCounterThreshold = value
        return self


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
    """This meta-class represents the ability to define the inhibition of a specific function identifier within the Fim configuration. Tags: atp.recommendedPackage=DiagnosticFunctionIdentifierInhibits"""

    # DiagnosticFunctionIdentifierInhibit method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.215, p.216
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFunctionIdentifierRef  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setFunctionIdentifierRef  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInhibitionMask         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setInhibitionMask         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addInhibitSource          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInhibitSources         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — the XSD carries DIAGNOSTIC-FUNCTION-IDENTIFIER-INHIBIT only
    # via ARPackage.element (AUTOSAR_00052.xsd l.5124), whose ELEMENTS loop requires a Referrable child; the
    # future consumer wires it (cf. DiagnosticConnectedIndicator Base note, commit b2e6b6341).

    def __init__(self):
        super().__init__()

        # This represents the corresponding function identifier.
        self.functionIdentifierRef: Optional[RefType] = None

        # This represents the value of the inhibition mask behavior.
        self.inhibitionMask: Optional[DiagnosticInhibitionMaskEnum] = None

        # This represents a collection of DiagnosticFunctionInhibitSource that contribute to the configuration of the enclosing DiagnosticFunctionIdentiferInhibit.
        self.inhibitSources: List[DiagnosticFunctionInhibitSource] = []

    def getFunctionIdentifierRef(self) -> Optional[RefType]:
        """
        This represents the corresponding function identifier.
        """
        return self.functionIdentifierRef

    def setFunctionIdentifierRef(self, value: Optional[RefType]) -> DiagnosticFunctionIdentifierInhibit:
        """
        This represents the corresponding function identifier.

        A None value is a no-op and does not overwrite an existing functionIdentifierRef.
        """
        if value is not None:
            self.functionIdentifierRef = value
        return self

    def getInhibitionMask(self) -> Optional[DiagnosticInhibitionMaskEnum]:
        """
        This represents the value of the inhibition mask behavior.
        """
        return self.inhibitionMask

    def setInhibitionMask(self, value: Optional[DiagnosticInhibitionMaskEnum]) -> DiagnosticFunctionIdentifierInhibit:
        """
        This represents the value of the inhibition mask behavior.

        A None value is a no-op and does not overwrite an existing inhibitionMask.
        """
        if value is not None:
            self.inhibitionMask = value
        return self

    def addInhibitSource(self, value: Optional[DiagnosticFunctionInhibitSource]) -> DiagnosticFunctionIdentifierInhibit:
        """
        This represents a collection of DiagnosticFunctionInhibitSource that contribute to the configuration of the enclosing DiagnosticFunctionIdentiferInhibit.

        A None value is a no-op and does not append an inhibitSource.
        """
        if value is not None:
            self.inhibitSources.append(value)
        return self

    def getInhibitSources(self) -> List[DiagnosticFunctionInhibitSource]:
        """
        This represents a collection of DiagnosticFunctionInhibitSource that contribute to the configuration of the enclosing DiagnosticFunctionIdentiferInhibit.
        """
        return self.inhibitSources


class DiagnosticIumprGroupIdentifier(ARObject):
    """This meta-class provides the ability to the define the group identifier for an IumprGroup."""

    # DiagnosticIumprGroupIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.210, p.211
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getGroupId  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGroupId  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute shall be taken to define an identifier for the IUMPR group. Please note that the value of this identifier is driven by regulations outside the scope of AUTOSAR and can therefore not be limited to the set of characters suitable for a shortName. Stereotypes: atpIdentityContributor
        self.groupId: Optional[NameToken] = None

    def getGroupId(self) -> Optional[NameToken]:
        """
        This attribute shall be taken to define an identifier for the IUMPR group. Please note that the value of this identifier is driven by regulations outside the scope of AUTOSAR and can therefore not be limited to the set of characters suitable for a shortName. Stereotypes: atpIdentityContributor
        """
        return self.groupId

    def setGroupId(self, value: Optional[NameToken]) -> DiagnosticIumprGroupIdentifier:
        """
        This attribute shall be taken to define an identifier for the IUMPR group. Please note that the value of this identifier is driven by regulations outside the scope of AUTOSAR and can therefore not be limited to the set of characters suitable for a shortName. Stereotypes: atpIdentityContributor

        A None value is a no-op and does not overwrite an existing groupId.
        """
        if value is not None:
            self.groupId = value
        return self


class DiagnosticMemoryDestination(ARObject, ABC):
    """This abstract meta-class represents a possible memory destination for a diagnostic event."""

    # DiagnosticMemoryDestination method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.167, p.182
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAgingRequiresTestedCycle                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAgingRequiresTestedCycle                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClearDtcLimitation                                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClearDtcLimitation                                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDtcStatusAvailabilityMask                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDtcStatusAvailabilityMask                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEventDisplacementStrategy                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventDisplacementStrategy                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumberOfEventEntries                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumberOfEventEntries                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMemoryEntryStorageTrigger                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMemoryEntryStorageTrigger                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStatusBitHandlingTestFailedSinceLastClear          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStatusBitHandlingTestFailedSinceLastClear          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStatusBitStorageTestFailed                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStatusBitStorageTestFailed                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTypeOfFreezeFrameRecordNumeration                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTypeOfFreezeFrameRecordNumeration                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is DiagnosticMemoryDestination:
            raise TypeError("DiagnosticMemoryDestination is an abstract class.")
        super().__init__()

        # Defines whether the aging cycle counter is processed every aging cycles or else only tested aging cycle are considered. If the attribute is set to TRUE: only tested aging cycle are considered for aging cycle counter. If the attribute is set to FALSE: aging cycle counter is processed every aging cycle. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.
        self.agingRequiresTestedCycle: Optional[Boolean] = None

        # Defines the scope of the DEM_ClearDTC Api. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.
        self.clearDtcLimitation: Optional[DiagnosticClearDtcLimitationEnum] = None

        # Mask for the supported DTC status bits by the Dem.
        self.dtcStatusAvailabilityMask: Optional[PositiveInteger] = None

        # This attribute defines, whether support for event displacement is enabled or not, and which displacement strategy is followed.
        self.eventDisplacementStrategy: Optional[DiagnosticEventDisplacementStrategyEnum] = None

        # This attribute fixes the maximum number of event entries in the fault memory.
        self.maxNumberOfEventEntries: Optional[PositiveInteger] = None

        # Describes the trigger to allocate an event memory entry.
        self.memoryEntryStorageTrigger: Optional[DiagnosticMemoryEntryStorageTriggerEnum] = None

        # This attribute defines, whether the aging and displacement mechanism shall be applied to the "TestFailedSinceLastClear" status bits. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.
        self.statusBitHandlingTestFailedSinceLastClear: Optional[DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum] = None

        # This parameter is used to activate/deactivate the permanent storage of the "TestFailed" status bits. true: storage activated false: storage deactivated
        self.statusBitStorageTestFailed: Optional[Boolean] = None

        # This attribute defines the type of assigning freeze frame record numbers for event-specific freeze frame records.
        self.typeOfFreezeFrameRecordNumeration: Optional[DiagnosticTypeOfFreezeFrameRecordNumerationEnum] = None

    def getAgingRequiresTestedCycle(self) -> Optional[Boolean]:
        """
        Defines whether the aging cycle counter is processed every aging cycles or else only tested aging cycle are considered. If the attribute is set to TRUE: only tested aging cycle are considered for aging cycle counter. If the attribute is set to FALSE: aging cycle counter is processed every aging cycle. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.
        """
        return self.agingRequiresTestedCycle

    def setAgingRequiresTestedCycle(self, value: Optional[Boolean]) -> DiagnosticMemoryDestination:
        """
        Defines whether the aging cycle counter is processed every aging cycles or else only tested aging cycle are considered. If the attribute is set to TRUE: only tested aging cycle are considered for aging cycle counter. If the attribute is set to FALSE: aging cycle counter is processed every aging cycle. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.

        A None value is a no-op and does not overwrite an existing agingRequiresTestedCycle.
        """
        if value is not None:
            self.agingRequiresTestedCycle = value
        return self

    def getClearDtcLimitation(self) -> Optional[DiagnosticClearDtcLimitationEnum]:
        """
        Defines the scope of the DEM_ClearDTC Api. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.
        """
        return self.clearDtcLimitation

    def setClearDtcLimitation(self, value: Optional[DiagnosticClearDtcLimitationEnum]) -> DiagnosticMemoryDestination:
        """
        Defines the scope of the DEM_ClearDTC Api. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.

        A None value is a no-op and does not overwrite an existing clearDtcLimitation.
        """
        if value is not None:
            self.clearDtcLimitation = value
        return self

    def getDtcStatusAvailabilityMask(self) -> Optional[PositiveInteger]:
        """
        Mask for the supported DTC status bits by the Dem.
        """
        return self.dtcStatusAvailabilityMask

    def setDtcStatusAvailabilityMask(self, value: Optional[PositiveInteger]) -> DiagnosticMemoryDestination:
        """
        Mask for the supported DTC status bits by the Dem.

        A None value is a no-op and does not overwrite an existing dtcStatusAvailabilityMask.
        """
        if value is not None:
            self.dtcStatusAvailabilityMask = value
        return self

    def getEventDisplacementStrategy(self) -> Optional[DiagnosticEventDisplacementStrategyEnum]:
        """
        This attribute defines, whether support for event displacement is enabled or not, and which displacement strategy is followed.
        """
        return self.eventDisplacementStrategy

    def setEventDisplacementStrategy(self, value: Optional[DiagnosticEventDisplacementStrategyEnum]) -> DiagnosticMemoryDestination:
        """
        This attribute defines, whether support for event displacement is enabled or not, and which displacement strategy is followed.

        A None value is a no-op and does not overwrite an existing eventDisplacementStrategy.
        """
        if value is not None:
            self.eventDisplacementStrategy = value
        return self

    def getMaxNumberOfEventEntries(self) -> Optional[PositiveInteger]:
        """
        This attribute fixes the maximum number of event entries in the fault memory.
        """
        return self.maxNumberOfEventEntries

    def setMaxNumberOfEventEntries(self, value: Optional[PositiveInteger]) -> DiagnosticMemoryDestination:
        """
        This attribute fixes the maximum number of event entries in the fault memory.

        A None value is a no-op and does not overwrite an existing maxNumberOfEventEntries.
        """
        if value is not None:
            self.maxNumberOfEventEntries = value
        return self

    def getMemoryEntryStorageTrigger(self) -> Optional[DiagnosticMemoryEntryStorageTriggerEnum]:
        """
        Describes the trigger to allocate an event memory entry.
        """
        return self.memoryEntryStorageTrigger

    def setMemoryEntryStorageTrigger(self, value: Optional[DiagnosticMemoryEntryStorageTriggerEnum]) -> DiagnosticMemoryDestination:
        """
        Describes the trigger to allocate an event memory entry.

        A None value is a no-op and does not overwrite an existing memoryEntryStorageTrigger.
        """
        if value is not None:
            self.memoryEntryStorageTrigger = value
        return self

    def getStatusBitHandlingTestFailedSinceLastClear(self) -> Optional[DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum]:
        """
        This attribute defines, whether the aging and displacement mechanism shall be applied to the "TestFailedSinceLastClear" status bits. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.
        """
        return self.statusBitHandlingTestFailedSinceLastClear

    def setStatusBitHandlingTestFailedSinceLastClear(self, value: Optional[DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum]) -> DiagnosticMemoryDestination:
        """
        This attribute defines, whether the aging and displacement mechanism shall be applied to the "TestFailedSinceLastClear" status bits. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.

        A None value is a no-op and does not overwrite an existing statusBitHandlingTestFailedSinceLastClear.
        """
        if value is not None:
            self.statusBitHandlingTestFailedSinceLastClear = value
        return self

    def getStatusBitStorageTestFailed(self) -> Optional[Boolean]:
        """
        This parameter is used to activate/deactivate the permanent storage of the "TestFailed" status bits. true: storage activated false: storage deactivated
        """
        return self.statusBitStorageTestFailed

    def setStatusBitStorageTestFailed(self, value: Optional[Boolean]) -> DiagnosticMemoryDestination:
        """
        This parameter is used to activate/deactivate the permanent storage of the "TestFailed" status bits. true: storage activated false: storage deactivated

        A None value is a no-op and does not overwrite an existing statusBitStorageTestFailed.
        """
        if value is not None:
            self.statusBitStorageTestFailed = value
        return self

    def getTypeOfFreezeFrameRecordNumeration(self) -> Optional[DiagnosticTypeOfFreezeFrameRecordNumerationEnum]:
        """
        This attribute defines the type of assigning freeze frame record numbers for event-specific freeze frame records.
        """
        return self.typeOfFreezeFrameRecordNumeration

    def setTypeOfFreezeFrameRecordNumeration(self, value: Optional[DiagnosticTypeOfFreezeFrameRecordNumerationEnum]) -> DiagnosticMemoryDestination:
        """
        This attribute defines the type of assigning freeze frame record numbers for event-specific freeze frame records.

        A None value is a no-op and does not overwrite an existing typeOfFreezeFrameRecordNumeration.
        """
        if value is not None:
            self.typeOfFreezeFrameRecordNumeration = value
        return self


class DiagnosticMemoryDestinationUserDefined(DiagnosticMemoryDestination):
    """This represents a user-defined memory for a diagnostic event. Tags: atp.recommendedPackage=DiagnosticMemoryDestinations"""

    # DiagnosticMemoryDestinationUserDefined method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.174, p.185
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAuthRoleRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAuthRoleRefs  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMemoryId      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setMemoryId      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — the XSD carries DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED only
    # via ARPackage.element (AUTOSAR_00052.xsd l.5149), whose ELEMENTS loop requires a Referrable child; the confirmed
    # queue row homes the class ARObject-family in ArObject.py (concrete branch of the abstract DiagnosticMemoryDestination,
    # not Identifiable — cf. DiagnosticFunctionIdentifierInhibit), so no ARPackage factory/dispatch can reach it —
    # the future consumer wires it. The XSD's own group also carries AUTHENTICATION-ROLE-REF with atp.Status="removed"
    # (AUTOSAR_00052.xsd l.39720) — not modeled (Rule 0015).

    def __init__(self):
        super().__init__()

        # This reference identifies the collection of applicable DiagnosticAuthRole Stereotypes: atpSplitable Tags: atp.Splitkey=authRole
        self.authRoleRefs: List[RefType] = []

        # This represents the identifier of the user-defined memory.
        self.memoryId: Optional[PositiveInteger] = None

    def addAuthRoleRef(self, ref: Optional[RefType]) -> DiagnosticMemoryDestinationUserDefined:
        """
        This reference identifies the collection of applicable DiagnosticAuthRole Stereotypes: atpSplitable Tags: atp.Splitkey=authRole

        A None value is a no-op and does not extend the authRoleRefs list.
        """
        if ref is not None:
            self.authRoleRefs.append(ref)
        return self

    def getAuthRoleRefs(self) -> List[RefType]:
        """
        This reference identifies the collection of applicable DiagnosticAuthRole Stereotypes: atpSplitable Tags: atp.Splitkey=authRole
        """
        return self.authRoleRefs

    def getMemoryId(self) -> Optional[PositiveInteger]:
        """
        This represents the identifier of the user-defined memory.
        """
        return self.memoryId

    def setMemoryId(self, value: Optional[PositiveInteger]) -> DiagnosticMemoryDestinationUserDefined:
        """
        This represents the identifier of the user-defined memory.

        A None value is a no-op and does not overwrite an existing memoryId.
        """
        if value is not None:
            self.memoryId = value
        return self


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


class DiagnosticParameterSupportInfo(ARObject):
    """This represents a way to define which bit of the supportInfo is representing this part of the PID"""

    # DiagnosticParameterSupportInfo method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.128, p.149
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSupportInfoBit     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportInfoBit     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # defines the bit in the SupportInfo byte, which represents the PID DataElement pidSize / position / size. Unit: byte.
        self.supportInfoBit: Optional[PositiveInteger] = None

    def getSupportInfoBit(self) -> Optional[PositiveInteger]:
        """
        defines the bit in the SupportInfo byte, which represents the PID DataElement pidSize / position / size. Unit: byte.
        """
        return self.supportInfoBit

    def setSupportInfoBit(self, value: Optional[PositiveInteger]) -> DiagnosticParameterSupportInfo:
        """
        defines the bit in the SupportInfo byte, which represents the PID DataElement pidSize / position / size. Unit: byte.

        A None value is a no-op and does not overwrite an existing supportInfoBit.
        """
        if value is not None:
            self.supportInfoBit = value
        return self


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


class DiagnosticSupportInfoByte(ARObject):
    """This meta-class defines the support information (typically byte A) to declare the usability of the Data Elements within the so-called packeted PIDs (e.g. PID$68)."""

    # DiagnosticSupportInfoByte method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.129, p.150
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPosition  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPosition  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSize      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSize      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the position of the supportInfo in the PID. Unit: byte.
        self.position: Optional[PositiveInteger] = None

        # This represents the size of the supportInfo within the PID. Unit: byte.
        self.size: Optional[PositiveInteger] = None

    def getPosition(self) -> Optional[PositiveInteger]:
        """
        This represents the position of the supportInfo in the PID. Unit: byte.
        """
        return self.position

    def setPosition(self, value: Optional[PositiveInteger]) -> DiagnosticSupportInfoByte:
        """
        This represents the position of the supportInfo in the PID. Unit: byte.

        A None value is a no-op and does not overwrite an existing position.
        """
        if value is not None:
            self.position = value
        return self

    def getSize(self) -> Optional[PositiveInteger]:
        """
        This represents the size of the supportInfo within the PID. Unit: byte.
        """
        return self.size

    def setSize(self, value: Optional[PositiveInteger]) -> DiagnosticSupportInfoByte:
        """
        This represents the size of the supportInfo within the PID. Unit: byte.

        A None value is a no-op and does not overwrite an existing size.
        """
        if value is not None:
            self.size = value
        return self


class DiagnosticTestIdentifier(ARObject):
    """This meta-class represents the ability to create a diagnostic test identifier."""

    # DiagnosticTestIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.203, p.205
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getId         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setId         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getUasId      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setUasId      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — the XSD carries DIAGNOSTIC-TEST-IDENTIFIER only as
    # TEST-IDENTIFIER inside the DIAGNOSTIC-TEST-RESULT group (AUTOSAR_00052.xsd l.45989), whose only class
    # consumer DiagnosticTestResult is an unsynced stub; the future consumer wires it (cf.
    # DiagnosticFunctionIdentifierInhibit, commit 27e01b079).

    def __init__(self):
        super().__init__()

        # This represents the numerical id associated with the diagnostic test identifier. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.id: Optional[PositiveInteger] = None

        # This represents the unit and scaling Id of the diagnostic test result. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.uasId: Optional[PositiveInteger] = None

    def getId(self) -> Optional[PositiveInteger]:
        """
        This represents the numerical id associated with the diagnostic test identifier. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> DiagnosticTestIdentifier:
        """
        This represents the numerical id associated with the diagnostic test identifier. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self

    def getUasId(self) -> Optional[PositiveInteger]:
        """
        This represents the unit and scaling Id of the diagnostic test result. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.uasId

    def setUasId(self, value: Optional[PositiveInteger]) -> DiagnosticTestIdentifier:
        """
        This represents the unit and scaling Id of the diagnostic test result. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing uasId.
        """
        if value is not None:
            self.uasId = value
        return self


class DiagnosticTroubleCodeObd(ARObject):
    """This element is used to define OBD-relevant DTCs. Tags: atp.recommendedPackage=DiagnosticTroubleCodes"""

    # DiagnosticTroubleCodeObd method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.159, p.175
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getConsiderPtoStatus    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setConsiderPtoStatus    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDtcPropsRef          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setDtcPropsRef          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventReadinessGroup  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setEventReadinessGroup  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getObdDtcValue          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setObdDtcValue          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — DIAGNOSTIC-TROUBLE-CODE-OBD appears in the ARPackage
    # ELEMENTS choice only (AUTOSAR_00052.xsd l.5250; no other parent aggregation in the XSD), whose loop
    # requires a Referrable child (createXxx(short_name) + addReferrableElement); the confirmed queue row
    # homes the class ARObject-family in ArObject.py (not Identifiable), so no factory/dispatch can reach
    # it — the future consumer wires it (cf. DiagnosticMemoryDestinationUserDefined,
    # DiagnosticFunctionIdentifierInhibit, commit 27e01b079).

    def __init__(self):
        super().__init__()

        # This attribute describes the affection of the event by the Dem PTO handling.
        #
        # true: the event is affected by the Dem PTO handling.
        #
        # false: the event is not affected by the Dem PTO handling.
        self.considerPtoStatus: Optional[Boolean] = None

        # Defined properties associated with the DemDTC.
        self.dtcPropsRef: Optional[RefType] = None

        # This aggregation allows for the variant definition of the attribute eventObdReadinessGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=eventReadinessGroup.eventObdReadiness Group, eventReadinessGroup.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.eventReadinessGroup: Optional[EventObdReadinessGroup] = None

        # Unique Diagnostic Trouble Code value for OBD. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.obdDtcValue: Optional[PositiveInteger] = None

    def getConsiderPtoStatus(self) -> Optional[Boolean]:
        """
        This attribute describes the affection of the event by the Dem PTO handling.

        true: the event is affected by the Dem PTO handling.

        false: the event is not affected by the Dem PTO handling.
        """
        return self.considerPtoStatus

    def setConsiderPtoStatus(self, value: Optional[Boolean]) -> DiagnosticTroubleCodeObd:
        """
        This attribute describes the affection of the event by the Dem PTO handling.

        true: the event is affected by the Dem PTO handling.

        false: the event is not affected by the Dem PTO handling.

        A None value is a no-op and does not overwrite an existing considerPtoStatus.
        """
        if value is not None:
            self.considerPtoStatus = value
        return self

    def getDtcPropsRef(self) -> Optional[RefType]:
        """
        Defined properties associated with the DemDTC.
        """
        return self.dtcPropsRef

    def setDtcPropsRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeObd:
        """
        Defined properties associated with the DemDTC.

        A None value is a no-op and does not overwrite an existing dtcProps reference.
        """
        if value is not None:
            self.dtcPropsRef = value
        return self

    def getEventReadinessGroup(self) -> Optional[EventObdReadinessGroup]:
        """
        This aggregation allows for the variant definition of the attribute eventObdReadinessGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=eventReadinessGroup.eventObdReadiness Group, eventReadinessGroup.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.eventReadinessGroup

    def setEventReadinessGroup(self, value: Optional[EventObdReadinessGroup]) -> DiagnosticTroubleCodeObd:
        """
        This aggregation allows for the variant definition of the attribute eventObdReadinessGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=eventReadinessGroup.eventObdReadiness Group, eventReadinessGroup.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not overwrite an existing eventReadinessGroup.
        """
        if value is not None:
            self.eventReadinessGroup = value
        return self

    def getObdDtcValue(self) -> Optional[PositiveInteger]:
        """
        Unique Diagnostic Trouble Code value for OBD. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.obdDtcValue

    def setObdDtcValue(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeObd:
        """
        Unique Diagnostic Trouble Code value for OBD. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing obdDtcValue.
        """
        if value is not None:
            self.obdDtcValue = value
        return self


class DiagnosticTroubleCodeProps(ARObject):
    """This element defines common Dtc properties that can be reused by different non OBD-relevant DTCs. Tags: atp.recommendedPackage=DiagnosticTroubleCodePropss"""

    # DiagnosticTroubleCodeProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.175, p.186
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAgingRef                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAgingRef                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticMemoryRef                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setDiagnosticMemoryRef                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addExtendedDataRecordRef                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getExtendedDataRecordRefs                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addFreezeFrameRef                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFreezeFrameRefs                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getImmediateNvDataStorage                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setImmediateNvDataStorage                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLegislatedFreezeFrameContentUdsObdRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setLegislatedFreezeFrameContentUdsObdRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxNumberFreezeFrameRecords             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setMaxNumberFreezeFrameRecords             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPriority                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setPriority                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSignificance                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setSignificance                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSnapshotRecordContentRef                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setSnapshotRecordContentRef                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — DIAGNOSTIC-TROUBLE-CODE-PROPS appears in the ARPackage
    # ELEMENTS choice only (AUTOSAR_00052.xsd l.5251; no other parent aggregation in the XSD), whose loop
    # requires a Referrable child (createXxx(short_name) + addReferrableElement); the confirmed queue row
    # homes the class ARObject-family in ArObject.py (not Identifiable), so no factory/dispatch can reach
    # it — the future consumer wires it (cf. DiagnosticTroubleCodeObd, DiagnosticMemoryDestinationUserDefined,
    # DiagnosticFunctionIdentifierInhibit, commit 27e01b079). The XSD group also carries AGING-ALLOWED,
    # ENVIRONMENT-CAPTURE-TO-REPORTING, FDC-THRESHOLD-STORAGE-VALUE, FREEZE-FRAME-CONTENT-REF,
    # FREEZE-FRAME-CONTENT-WWH-OBD-REF, LEGISLATED-FREEZE-FRAME-CONTENT-WWH-OBDS and MEMORY-DESTINATION-REFS
    # with atp.Status="removed" (AUTOSAR_00052.xsd l.46452-46546) — not modeled (Rule 0015).

    def __init__(self):
        super().__init__()

        # Reference to an aging algorithm in case that an aging/ unlearning of the event is allowed. Stereotypes: atpSplitable Tags: atp.Splitkey=aging
        self.agingRef: Optional[RefType] = None

        # Reference to the applicable DiagnosticMemory Destination. Stereotypes: atpSplitable Tags: atp.Splitkey=diagnosticMemory
        self.diagnosticMemoryRef: Optional[RefType] = None

        # Defines the links to an extended data class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=extendedDataRecord.diagnosticExtended DataRecord, extendedDataRecord.variationPoint.short Label vh.latestBindingTime=preCompileTime
        self.extendedDataRecordRefs: List[RefType] = []

        # Define the links to a freeze frame class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=freezeFrame.diagnosticFreezeFrame, freeze Frame.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.freezeFrameRefs: List[RefType] = []

        # Change description for Class immediateNvDataStorage in table "Table A.111: DiagnosticTroubleCodeProps": Switch to enable immediate storage triggering of an according event memory entry persistently to NVRAM. true: immediate non-volatile storage triggering on first occurrence and shutdown. false: immediate non-volatile storage triggering on shutdown.
        self.immediateNvDataStorage: Optional[Boolean] = None

        # This reference identifies the layout of legislated freeze frames used for emission related diagnostics over the UDS protocol such as OBDonUDS or WWH-OBD. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=legislatedFreezeFrameContentUds Obd.diagnosticDataIdentifierSet, legislatedFreezeFrame ContentUdsObd.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.legislatedFreezeFrameContentUdsObdRef: Optional[RefType] = None

        # This attribute defines the number of according freeze frame records, which can maximal be stored for this event. Therefore all these freeze frame records have the same freeze frame class.
        self.maxNumberFreezeFrameRecords: Optional[PositiveInteger] = None

        # Priority of the event, in view of full event buffer. A lower value means higher priority. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.priority: Optional[PositiveInteger] = None

        # Significance of the event, which indicates additional information concerning fault classification and resolution.
        self.significance: Optional[DiagnosticSignificanceEnum] = None

        # This represents the freeze frame layout as a set of DIDs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=snapshotRecordContent.diagnosticData IdentifierSet, snapshotRecordContent.variationPoint.short Label vh.latestBindingTime=preCompileTime
        self.snapshotRecordContentRef: Optional[RefType] = None

    def getAgingRef(self) -> Optional[RefType]:
        """
        Reference to an aging algorithm in case that an aging/ unlearning of the event is allowed. Stereotypes: atpSplitable Tags: atp.Splitkey=aging
        """
        return self.agingRef

    def setAgingRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeProps:
        """
        Reference to an aging algorithm in case that an aging/ unlearning of the event is allowed. Stereotypes: atpSplitable Tags: atp.Splitkey=aging

        A None value is a no-op and does not overwrite an existing aging reference.
        """
        if value is not None:
            self.agingRef = value
        return self

    def getDiagnosticMemoryRef(self) -> Optional[RefType]:
        """
        Reference to the applicable DiagnosticMemory Destination. Stereotypes: atpSplitable Tags: atp.Splitkey=diagnosticMemory
        """
        return self.diagnosticMemoryRef

    def setDiagnosticMemoryRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeProps:
        """
        Reference to the applicable DiagnosticMemory Destination. Stereotypes: atpSplitable Tags: atp.Splitkey=diagnosticMemory

        A None value is a no-op and does not overwrite an existing diagnosticMemory reference.
        """
        if value is not None:
            self.diagnosticMemoryRef = value
        return self

    def addExtendedDataRecordRef(self, ref: Optional[RefType]) -> DiagnosticTroubleCodeProps:
        """
        Defines the links to an extended data class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=extendedDataRecord.diagnosticExtended DataRecord, extendedDataRecord.variationPoint.short Label vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not extend the extendedDataRecordRefs list.
        """
        if ref is not None:
            self.extendedDataRecordRefs.append(ref)
        return self

    def getExtendedDataRecordRefs(self) -> List[RefType]:
        """
        Defines the links to an extended data class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=extendedDataRecord.diagnosticExtended DataRecord, extendedDataRecord.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return self.extendedDataRecordRefs

    def addFreezeFrameRef(self, ref: Optional[RefType]) -> DiagnosticTroubleCodeProps:
        """
        Define the links to a freeze frame class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=freezeFrame.diagnosticFreezeFrame, freeze Frame.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not extend the freezeFrameRefs list.
        """
        if ref is not None:
            self.freezeFrameRefs.append(ref)
        return self

    def getFreezeFrameRefs(self) -> List[RefType]:
        """
        Define the links to a freeze frame class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=freezeFrame.diagnosticFreezeFrame, freeze Frame.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.freezeFrameRefs

    def getImmediateNvDataStorage(self) -> Optional[Boolean]:
        """
        Change description for Class immediateNvDataStorage in table "Table A.111: DiagnosticTroubleCodeProps": Switch to enable immediate storage triggering of an according event memory entry persistently to NVRAM. true: immediate non-volatile storage triggering on first occurrence and shutdown. false: immediate non-volatile storage triggering on shutdown.
        """
        return self.immediateNvDataStorage

    def setImmediateNvDataStorage(self, value: Optional[Boolean]) -> DiagnosticTroubleCodeProps:
        """
        Change description for Class immediateNvDataStorage in table "Table A.111: DiagnosticTroubleCodeProps": Switch to enable immediate storage triggering of an according event memory entry persistently to NVRAM. true: immediate non-volatile storage triggering on first occurrence and shutdown. false: immediate non-volatile storage triggering on shutdown.

        A None value is a no-op and does not overwrite an existing immediateNvDataStorage.
        """
        if value is not None:
            self.immediateNvDataStorage = value
        return self

    def getLegislatedFreezeFrameContentUdsObdRef(self) -> Optional[RefType]:
        """
        This reference identifies the layout of legislated freeze frames used for emission related diagnostics over the UDS protocol such as OBDonUDS or WWH-OBD. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=legislatedFreezeFrameContentUds Obd.diagnosticDataIdentifierSet, legislatedFreezeFrame ContentUdsObd.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.legislatedFreezeFrameContentUdsObdRef

    def setLegislatedFreezeFrameContentUdsObdRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeProps:
        """
        This reference identifies the layout of legislated freeze frames used for emission related diagnostics over the UDS protocol such as OBDonUDS or WWH-OBD. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=legislatedFreezeFrameContentUds Obd.diagnosticDataIdentifierSet, legislatedFreezeFrame ContentUdsObd.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing legislatedFreezeFrameContentUdsObd reference.
        """
        if value is not None:
            self.legislatedFreezeFrameContentUdsObdRef = value
        return self

    def getMaxNumberFreezeFrameRecords(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the number of according freeze frame records, which can maximal be stored for this event. Therefore all these freeze frame records have the same freeze frame class.
        """
        return self.maxNumberFreezeFrameRecords

    def setMaxNumberFreezeFrameRecords(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeProps:
        """
        This attribute defines the number of according freeze frame records, which can maximal be stored for this event. Therefore all these freeze frame records have the same freeze frame class.

        A None value is a no-op and does not overwrite an existing maxNumberFreezeFrameRecords.
        """
        if value is not None:
            self.maxNumberFreezeFrameRecords = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """
        Priority of the event, in view of full event buffer. A lower value means higher priority. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeProps:
        """
        Priority of the event, in view of full event buffer. A lower value means higher priority. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getSignificance(self) -> Optional[DiagnosticSignificanceEnum]:
        """
        Significance of the event, which indicates additional information concerning fault classification and resolution.
        """
        return self.significance

    def setSignificance(self, value: Optional[DiagnosticSignificanceEnum]) -> DiagnosticTroubleCodeProps:
        """
        Significance of the event, which indicates additional information concerning fault classification and resolution.

        A None value is a no-op and does not overwrite an existing significance.
        """
        if value is not None:
            self.significance = value
        return self

    def getSnapshotRecordContentRef(self) -> Optional[RefType]:
        """
        This represents the freeze frame layout as a set of DIDs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=snapshotRecordContent.diagnosticData IdentifierSet, snapshotRecordContent.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return self.snapshotRecordContentRef

    def setSnapshotRecordContentRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeProps:
        """
        This represents the freeze frame layout as a set of DIDs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=snapshotRecordContent.diagnosticData IdentifierSet, snapshotRecordContent.variationPoint.short Label vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing snapshotRecordContent reference.
        """
        if value is not None:
            self.snapshotRecordContentRef = value
        return self


class DiagnosticTroubleCodeUds(ARObject):
    """This element is used to describe non OBD-relevant DTCs. Tags: atp.recommendedPackage=DiagnosticTroubleCodes"""

    # DiagnosticTroubleCodeUds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.158, p.174
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getConsiderPtoStatus      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setConsiderPtoStatus      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDtcPropsRef            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setDtcPropsRef            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventReadinessGroup    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setEventReadinessGroup    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFunctionalUnit         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setFunctionalUnit         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getObdDtcValue3Byte       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setObdDtcValue3Byte       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSeverity               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setSeverity               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getUdsDtcValue            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setUdsDtcValue            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getWwhObdDtcClass         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setWwhObdDtcClass         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — DIAGNOSTIC-TROUBLE-CODE-UDS appears in the ARPackage
    # ELEMENTS choice only (AUTOSAR_00052.xsd l.5252; no other parent aggregation in the XSD), whose loop
    # requires a Referrable child (createXxx(short_name) + addReferrableElement); the confirmed queue row
    # homes the class ARObject-family in ArObject.py (not Identifiable), so no factory/dispatch can reach
    # it — the future consumer wires it (cf. DiagnosticTroubleCodeObd, DiagnosticTroubleCodeProps,
    # DiagnosticMemoryDestinationUserDefined, commit 27e01b079). The XSD group also carries
    # EVENT-OBD-READINESS-GROUP (NMTOKEN, atp.Status="removed", AUTOSAR_00052.xsd l.46742-46749), absent
    # from the markdown table — not modeled (Rule 0015).

    def __init__(self):
        super().__init__()

        # This attribute describes the affection of the event by the Dem PTO handling.
        #
        # true: the event is affected by the Dem PTO handling.
        #
        # false: the event is not affected by the Dem PTO handling.
        self.considerPtoStatus: Optional[Boolean] = None

        # Defined properties associated with the DemDTC.
        self.dtcPropsRef: Optional[RefType] = None

        # This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs. The upper multiplicity of this role has been increased to * due to resolving an atpVariation stereotype. The previous value was 1.
        self.eventReadinessGroup: Optional[EventObdReadinessGroup] = None

        # This attribute specifies a 1-byte value which identifies the corresponding basic vehicle / system function which reports the DTC. This parameter is necessary for the report of severity information. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.functionalUnit: Optional[PositiveInteger] = None

        # 3 Byte OBD DTC value based on the definition from SAE J2012. The existence of this attribute is only required if separated UDS and OBD DTC values are used for SAE J1979-2. If this attribute does not exist, then UDS DTC values are used with J1979-2. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.obdDtcValue3Byte: Optional[PositiveInteger] = None

        # DTC severity according to ISO 14229-1. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.severity: Optional[DiagnosticUdsSeverityEnum] = None

        # Unique Diagnostic Trouble Code value for UDS. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.udsDtcValue: Optional[PositiveInteger] = None

        # This attribute is used to identify (if applicable) the corresponding severity class of an WWH-OBD DTC. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.wwhObdDtcClass: Optional[DiagnosticWwhObdDtcClassEnum] = None

    def getConsiderPtoStatus(self) -> Optional[Boolean]:
        """
        This attribute describes the affection of the event by the Dem PTO handling.

        true: the event is affected by the Dem PTO handling.

        false: the event is not affected by the Dem PTO handling.
        """
        return self.considerPtoStatus

    def setConsiderPtoStatus(self, value: Optional[Boolean]) -> DiagnosticTroubleCodeUds:
        """
        This attribute describes the affection of the event by the Dem PTO handling.

        true: the event is affected by the Dem PTO handling.

        false: the event is not affected by the Dem PTO handling.

        A None value is a no-op and does not overwrite an existing considerPtoStatus.
        """
        if value is not None:
            self.considerPtoStatus = value
        return self

    def getDtcPropsRef(self) -> Optional[RefType]:
        """
        Defined properties associated with the DemDTC.
        """
        return self.dtcPropsRef

    def setDtcPropsRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeUds:
        """
        Defined properties associated with the DemDTC.

        A None value is a no-op and does not overwrite an existing dtcProps reference.
        """
        if value is not None:
            self.dtcPropsRef = value
        return self

    def getEventReadinessGroup(self) -> Optional[EventObdReadinessGroup]:
        """
        This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs. The upper multiplicity of this role has been increased to * due to resolving an atpVariation stereotype. The previous value was 1.
        """
        return self.eventReadinessGroup

    def setEventReadinessGroup(self, value: Optional[EventObdReadinessGroup]) -> DiagnosticTroubleCodeUds:
        """
        This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs. The upper multiplicity of this role has been increased to * due to resolving an atpVariation stereotype. The previous value was 1.

        A None value is a no-op and does not overwrite an existing eventReadinessGroup.
        """
        if value is not None:
            self.eventReadinessGroup = value
        return self

    def getFunctionalUnit(self) -> Optional[PositiveInteger]:
        """
        This attribute specifies a 1-byte value which identifies the corresponding basic vehicle / system function which reports the DTC. This parameter is necessary for the report of severity information. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.functionalUnit

    def setFunctionalUnit(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeUds:
        """
        This attribute specifies a 1-byte value which identifies the corresponding basic vehicle / system function which reports the DTC. This parameter is necessary for the report of severity information. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing functionalUnit.
        """
        if value is not None:
            self.functionalUnit = value
        return self

    def getObdDtcValue3Byte(self) -> Optional[PositiveInteger]:
        """
        3 Byte OBD DTC value based on the definition from SAE J2012. The existence of this attribute is only required if separated UDS and OBD DTC values are used for SAE J1979-2. If this attribute does not exist, then UDS DTC values are used with J1979-2. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.obdDtcValue3Byte

    def setObdDtcValue3Byte(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeUds:
        """
        3 Byte OBD DTC value based on the definition from SAE J2012. The existence of this attribute is only required if separated UDS and OBD DTC values are used for SAE J1979-2. If this attribute does not exist, then UDS DTC values are used with J1979-2. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing obdDtcValue3Byte.
        """
        if value is not None:
            self.obdDtcValue3Byte = value
        return self

    def getSeverity(self) -> Optional[DiagnosticUdsSeverityEnum]:
        """
        DTC severity according to ISO 14229-1. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.severity

    def setSeverity(self, value: Optional[DiagnosticUdsSeverityEnum]) -> DiagnosticTroubleCodeUds:
        """
        DTC severity according to ISO 14229-1. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing severity.
        """
        if value is not None:
            self.severity = value
        return self

    def getUdsDtcValue(self) -> Optional[PositiveInteger]:
        """
        Unique Diagnostic Trouble Code value for UDS. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.udsDtcValue

    def setUdsDtcValue(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeUds:
        """
        Unique Diagnostic Trouble Code value for UDS. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing udsDtcValue.
        """
        if value is not None:
            self.udsDtcValue = value
        return self

    def getWwhObdDtcClass(self) -> Optional[DiagnosticWwhObdDtcClassEnum]:
        """
        This attribute is used to identify (if applicable) the corresponding severity class of an WWH-OBD DTC. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.wwhObdDtcClass

    def setWwhObdDtcClass(self, value: Optional[DiagnosticWwhObdDtcClassEnum]) -> DiagnosticTroubleCodeUds:
        """
        This attribute is used to identify (if applicable) the corresponding severity class of an WWH-OBD DTC. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing wwhObdDtcClass.
        """
        if value is not None:
            self.wwhObdDtcClass = value
        return self


class EventObdReadinessGroup(ARObject):
    """This meta-class represents the ability to define the value of attribute eventObdReadinessGroup. It is only introduced to allow for a variant modeling of this attribute."""

    # EventObdReadinessGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.160, p.176
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventObdReadinessGroup  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setEventObdReadinessGroup  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # reader/writer [—] = Steps 5/6 N/A this pass — EVENT-OBD-READINESS-GROUP is aggregated only by
    # DiagnosticTroubleCodeObd.eventReadinessGroup and DiagnosticTroubleCodeUds.eventReadinessGroup
    # (AUTOSAR_00052.xsd l.46400 / l.46756, each through an optional EVENT-READINESS-GROUPS wrapper
    # holding an unbounded EVENT-OBD-READINESS-GROUP choice); both consuming parents are ARObject-family
    # homes in ArObject.py (not Identifiable), so no factory/dispatch can reach them — the future
    # consumer wires the wrapper structure (cf. DiagnosticTroubleCodeUds, DiagnosticTroubleCodeObd,
    # commit 27e01b079). The XSD group also carries VARIATION-POINT (AUTOSAR_00052.xsd l.57557-57567,
    # xml.sequenceOffset="10000"), absent from the markdown table — not modeled (Rule 0015).

    def __init__(self):
        super().__init__()

        # This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs.
        self.eventObdReadinessGroup: Optional[NameToken] = None

    def getEventObdReadinessGroup(self) -> Optional[NameToken]:
        """
        This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs.
        """
        return self.eventObdReadinessGroup

    def setEventObdReadinessGroup(self, value: Optional[NameToken]) -> EventObdReadinessGroup:
        """
        This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs.

        A None value is a no-op and does not overwrite an existing eventObdReadinessGroup.
        """
        if value is not None:
            self.eventObdReadinessGroup = value
        return self


class FMAttributeValue(ARObject):
    pass


class FMFeatureDecomposition(ARObject):
    pass


class InvertCondition(AbstractCondition):
    pass


class MultiplicityRestrictionWithSeverity(AbstractMultiplicityRestriction):
    pass


class PhysicalDimensionMapping(ARObject):
    """This class represents a specific mapping between two PhysicalDimensions."""

    # PhysicalDimensionMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.77, p.399
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstPhysicalDimensionRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstPhysicalDimensionRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondPhysicalDimensionRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondPhysicalDimensionRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping.
        self.firstPhysicalDimensionRef: Optional[RefType] = None

        # This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping.
        self.secondPhysicalDimensionRef: Optional[RefType] = None

    def getFirstPhysicalDimensionRef(self) -> Optional[RefType]:
        """
        This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping.
        """
        return self.firstPhysicalDimensionRef

    def setFirstPhysicalDimensionRef(self, value: Optional[RefType]) -> PhysicalDimensionMapping:
        """
        This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping.

        A None value is a no-op and does not overwrite an existing firstPhysicalDimensionRef.
        """
        if value is not None:
            self.firstPhysicalDimensionRef = value
        return self

    def getSecondPhysicalDimensionRef(self) -> Optional[RefType]:
        """
        This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping.
        """
        return self.secondPhysicalDimensionRef

    def setSecondPhysicalDimensionRef(self, value: Optional[RefType]) -> PhysicalDimensionMapping:
        """
        This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping.

        A None value is a no-op and does not overwrite an existing secondPhysicalDimensionRef.
        """
        if value is not None:
            self.secondPhysicalDimensionRef = value
        return self


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


class StreamFilterIpv6Address(ARObject):
    pass


class StreamFilterPortRange(ARObject):
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
    DiagnosticClearDtcLimitationEnum,
    DiagnosticConnectedIndicatorBehaviorEnum,
    DiagnosticEventCombinationBehaviorEnum,
    DiagnosticEventCombinationReportingBehaviorEnum,
    DiagnosticEventDisplacementStrategyEnum,
    DiagnosticEventWindowTimeEnum,
    DiagnosticInhibitionMaskEnum,
    DiagnosticMemoryEntryStorageTriggerEnum,
    DiagnosticOccurrenceCounterProcessingEnum,
    DiagnosticPeriodicRateCategoryEnum,
    DiagnosticSignificanceEnum,
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
    DiagnosticTypeOfFreezeFrameRecordNumerationEnum,
    DiagnosticUdsSeverityEnum,
    DiagnosticWwhObdDtcClassEnum,
    Identifier,
    NameToken,
    PositiveInteger,
    RefType,
    TimeValue,
)
