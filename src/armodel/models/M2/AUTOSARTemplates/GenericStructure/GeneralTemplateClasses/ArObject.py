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


class SpecificationScope(ARObject):
    pass


class TextualCondition(AbstractCondition):
    pass


class AbstractGlobalTimeDomainProps(ARObject, VariationPointCapable):
    """
    This abstract class enables a GlobalTimeDomain to specify additional properties.
    """

    # AbstractGlobalTimeDomainProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.2, p.859
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)
    # Table 9.2 has no Attribute rows; the abstract VARIATION-POINT slot is read/written by the
    # reusable readAbstractGlobalTimeDomainProps / writeAbstractGlobalTimeDomainProps helpers
    # that the concrete Can/Eth/Fr GlobalTimeDomainProps readers/writers call.
    # Aggregator dispatch (GlobalTimeDomain.globalTimeDomainProperty) is pending — GlobalTimeDomain
    # is a later-wave class.

    def __init__(self):
        if type(self) is AbstractGlobalTimeDomainProps:
            raise TypeError("AbstractGlobalTimeDomainProps is an abstract class.")

        super().__init__()


class BinaryManifestItemValue(ARObject, ABC):
    """
    This meta-class has the ability to act as an abstract base class for values of binary manifest item.
    """

    # BinaryManifestItemValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.25, p.922
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # Table 11.25 declares no Attribute rows and the XSD BINARY-MANIFEST-ITEM-VALUE group
    # (AUTOSAR_00052.xsd l.8763) has an empty sequence; the reusable readBinaryManifestItemValue /
    # writeBinaryManifestItemValue helpers own the ARObject level of the concrete subclass element
    # (BINARY-MANIFEST-ITEM-NUMERICAL-VALUE / BINARY-MANIFEST-ITEM-POINTER-VALUE) and are called by
    # the BinaryManifestItemNumericalValue / BinaryManifestItemPointerValue readers/writers.
    # Aggregator dispatch (BinaryManifestItem.value / BinaryManifestItem.defaultValue) is pending —
    # BinaryManifestItem is an unsynced later-wave stub.

    def __init__(self):
        if type(self) is BinaryManifestItemValue:
            raise TypeError("BinaryManifestItemValue is an abstract class.")

        super().__init__()


class BusMirrorCanIdRangeMapping(ARObject):
    """
    This element defines a rule for remapping a set of CAN IDs.
    """

    # BusMirrorCanIdRangeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.329, p.702
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDestinationBaseId     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationBaseId     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceCanIdCode       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceCanIdCode       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceCanIdMask       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceCanIdMask       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Base ID merged with the masked parts of the original CAN ID to form the mapped CAN ID.
        self.destinationBaseId: Optional[PositiveInteger] = None

        # Value to match masked original CAN IDs.
        self.sourceCanIdCode: Optional[PositiveInteger] = None

        # Mask applied to original CAN IDs before comparison.
        self.sourceCanIdMask: Optional[PositiveInteger] = None

    def getDestinationBaseId(self) -> Optional[PositiveInteger]:
        """
        Base ID merged with the masked parts of the original CAN ID to form the mapped CAN ID.
        """
        return self.destinationBaseId

    def setDestinationBaseId(self, value: Optional[PositiveInteger]) -> BusMirrorCanIdRangeMapping:
        """
        Base ID merged with the masked parts of the original CAN ID to form the mapped CAN ID.

        A None value is a no-op and does not overwrite an existing destinationBaseId.
        """
        if value is not None:
            self.destinationBaseId = value
        return self

    def getSourceCanIdCode(self) -> Optional[PositiveInteger]:
        """
        Value to match masked original CAN IDs.
        """
        return self.sourceCanIdCode

    def setSourceCanIdCode(self, value: Optional[PositiveInteger]) -> BusMirrorCanIdRangeMapping:
        """
        Value to match masked original CAN IDs.

        A None value is a no-op and does not overwrite an existing sourceCanIdCode.
        """
        if value is not None:
            self.sourceCanIdCode = value
        return self

    def getSourceCanIdMask(self) -> Optional[PositiveInteger]:
        """
        Mask applied to original CAN IDs before comparison.
        """
        return self.sourceCanIdMask

    def setSourceCanIdMask(self, value: Optional[PositiveInteger]) -> BusMirrorCanIdRangeMapping:
        """
        Mask applied to original CAN IDs before comparison.

        A None value is a no-op and does not overwrite an existing sourceCanIdMask.
        """
        if value is not None:
            self.sourceCanIdMask = value
        return self


class BusMirrorCanIdToCanIdMapping(ARObject):
    """
    This element defines a rule for remapping a single CAN ID.
    """

    # BusMirrorCanIdToCanIdMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.330, p.702
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRemappedCanId         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemappedCanId         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSouceCanIdRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSouceCanIdRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the CanId on the targetChannel.
        self.remappedCanId: Optional[PositiveInteger] = None

        # This reference points to the sourceFrame with sourceCan Id on the sourceChannel.
        self.souceCanIdRef: Optional[RefType] = None

    def getRemappedCanId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the CanId on the targetChannel.
        """
        return self.remappedCanId

    def setRemappedCanId(self, value: Optional[PositiveInteger]) -> BusMirrorCanIdToCanIdMapping:
        """
        This attribute defines the CanId on the targetChannel.

        A None value is a no-op and does not overwrite an existing remappedCanId.
        """
        if value is not None:
            self.remappedCanId = value
        return self

    def getSouceCanIdRef(self) -> Optional[RefType]:
        """
        This reference points to the sourceFrame with sourceCan Id on the sourceChannel.
        """
        return self.souceCanIdRef

    def setSouceCanIdRef(self, value: Optional[RefType]) -> BusMirrorCanIdToCanIdMapping:
        """
        This reference points to the sourceFrame with sourceCan Id on the sourceChannel.

        A None value is a no-op and does not overwrite an existing souceCanIdRef.
        """
        if value is not None:
            self.souceCanIdRef = value
        return self


class BusMirrorChannel(ARObject):
    pass


class BusMirrorLinPidToCanIdMapping(ARObject):
    """
    This element defines a rule for remapping a single LIN Frame.
    """

    # BusMirrorLinPidToCanIdMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.331, p.702
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRemappedCanId         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemappedCanId         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceLinPidRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceLinPidRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the CanId on the targetChannel.
        self.remappedCanId: Optional[PositiveInteger] = None

        # This reference points to the sourceFrame with sourceCan Id on the sourceChannel.
        self.sourceLinPidRef: Optional[RefType] = None

    def getRemappedCanId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the CanId on the targetChannel.
        """
        return self.remappedCanId

    def setRemappedCanId(self, value: Optional[PositiveInteger]) -> BusMirrorLinPidToCanIdMapping:
        """
        This attribute defines the CanId on the targetChannel.

        A None value is a no-op and does not overwrite an existing remappedCanId.
        """
        if value is not None:
            self.remappedCanId = value
        return self

    def getSourceLinPidRef(self) -> Optional[RefType]:
        """
        This reference points to the sourceFrame with sourceCan Id on the sourceChannel.
        """
        return self.sourceLinPidRef

    def setSourceLinPidRef(self, value: Optional[RefType]) -> BusMirrorLinPidToCanIdMapping:
        """
        This reference points to the sourceFrame with sourceCan Id on the sourceChannel.

        A None value is a no-op and does not overwrite an existing sourceLinPidRef.
        """
        if value is not None:
            self.sourceLinPidRef = value
        return self


class CpSoftwareClusterCommunicationResourceProps(ARObject, ABC):
    """
    Communication properties for cross cluster communication.
    """

    # CpSoftwareClusterCommunicationResourceProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.9, p.902
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # Table 11.9 declares no Attribute rows and the XSD CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE-PROPS
    # group (AUTOSAR_00052.xsd l.24290) has an empty sequence; the reusable
    # readCpSoftwareClusterCommunicationResourceProps / writeCpSoftwareClusterCommunicationResourceProps
    # helpers own the ARObject level of the concrete subclass element (CLIENT-SERVER-OPERATION-COM-PROPS /
    # DATA-COM-PROPS) and are called by the ClientServerOperationComProps / DataComProps readers/writers.
    # Aggregator dispatch (CpSoftwareClusterCommunicationResource.communicationResourceProps) is
    # pending — CpSoftwareClusterCommunicationResource is an unsynced later-wave class.

    def __init__(self):
        if type(self) is CpSoftwareClusterCommunicationResourceProps:
            raise TypeError("CpSoftwareClusterCommunicationResourceProps is an abstract class.")

        super().__init__()


class DdsCpProvidedServiceInstance(ARObject):
    """
    This meta-class represents the ability to describe the existence and configuration of a provided service instance in a concrete implementation on top of DDS.
    """

    # DdsCpProvidedServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.153, p.473
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLocalUnicastAddressRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLocalUnicastAddressRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinorVersion                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinorVersion                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addProvidedDdsOperation               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProvidedDdsOperations              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addProvidedDdsServiceInstanceEvent    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProvidedDdsServiceInstanceEvents   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getStaticRemoteMulticastAddressRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStaticRemoteMulticastAddressRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addStaticRemoteUnicastAddressRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStaticRemoteUnicastAddressRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # The local address over which the Service is provided. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES
        self.localUnicastAddressRef: Optional[RefType] = None

        # Minor Version of the Service that is provided by this Dds CpProvidedServiceInstance.
        self.minorVersion: Optional[PositiveInteger] = None

        # Collection of provided operations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedDdsOperation, providedDds Operation.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        self.providedDdsOperations: List[DdsCpServiceInstanceOperation] = []

        # Collection of provided events. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedDdsServiceInstanceEvent, provided DdsServiceInstanceEvent.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        self.providedDdsServiceInstanceEvents: List[DdsCpServiceInstanceEvent] = []

        # This reference defines the remote multicast address of Service consumers. This reference shall ONLY be used if the remote multicast address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES
        self.staticRemoteMulticastAddressRef: Optional[RefType] = None

        # This reference defines the remote unicast addresses of Service consumers. This reference shall ONLY be used if the remote unicast address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES
        self.staticRemoteUnicastAddressRefs: List[RefType] = []

    def getLocalUnicastAddressRef(self) -> Optional[RefType]:
        """
        The local address over which the Service is provided. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES
        """
        return self.localUnicastAddressRef

    def setLocalUnicastAddressRef(self, value: Optional[RefType]) -> DdsCpProvidedServiceInstance:
        """
        The local address over which the Service is provided. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES

        A None value is a no-op and does not overwrite an existing localUnicastAddressRef.
        """
        if value is not None:
            self.localUnicastAddressRef = value
        return self

    def getMinorVersion(self) -> Optional[PositiveInteger]:
        """
        Minor Version of the Service that is provided by this Dds CpProvidedServiceInstance.
        """
        return self.minorVersion

    def setMinorVersion(self, value: Optional[PositiveInteger]) -> DdsCpProvidedServiceInstance:
        """
        Minor Version of the Service that is provided by this Dds CpProvidedServiceInstance.

        A None value is a no-op and does not overwrite an existing minorVersion.
        """
        if value is not None:
            self.minorVersion = value
        return self

    def addProvidedDdsOperation(self, value: Optional[DdsCpServiceInstanceOperation]) -> DdsCpProvidedServiceInstance:
        """
        Collection of provided operations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedDdsOperation, providedDds Operation.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not extend the providedDdsOperations list.
        """
        if value is not None:
            self.providedDdsOperations.append(value)
        return self

    def getProvidedDdsOperations(self) -> List[DdsCpServiceInstanceOperation]:
        """
        Collection of provided operations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedDdsOperation, providedDds Operation.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        """
        return self.providedDdsOperations

    def addProvidedDdsServiceInstanceEvent(self, value: Optional[DdsCpServiceInstanceEvent]) -> DdsCpProvidedServiceInstance:
        """
        Collection of provided events. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedDdsServiceInstanceEvent, provided DdsServiceInstanceEvent.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not extend the providedDdsServiceInstanceEvents list.
        """
        if value is not None:
            self.providedDdsServiceInstanceEvents.append(value)
        return self

    def getProvidedDdsServiceInstanceEvents(self) -> List[DdsCpServiceInstanceEvent]:
        """
        Collection of provided events. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedDdsServiceInstanceEvent, provided DdsServiceInstanceEvent.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        """
        return self.providedDdsServiceInstanceEvents

    def getStaticRemoteMulticastAddressRef(self) -> Optional[RefType]:
        """
        This reference defines the remote multicast address of Service consumers. This reference shall ONLY be used if the remote multicast address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES
        """
        return self.staticRemoteMulticastAddressRef

    def setStaticRemoteMulticastAddressRef(self, value: Optional[RefType]) -> DdsCpProvidedServiceInstance:
        """
        This reference defines the remote multicast address of Service consumers. This reference shall ONLY be used if the remote multicast address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES

        A None value is a no-op and does not overwrite an existing staticRemoteMulticastAddressRef.
        """
        if value is not None:
            self.staticRemoteMulticastAddressRef = value
        return self

    def addStaticRemoteUnicastAddressRef(self, value: Optional[RefType]) -> DdsCpProvidedServiceInstance:
        """
        This reference defines the remote unicast addresses of Service consumers. This reference shall ONLY be used if the remote unicast address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES

        A None value is a no-op and does not extend the staticRemoteUnicastAddressRefs list.
        """
        if value is not None:
            self.staticRemoteUnicastAddressRefs.append(value)
        return self

    def getStaticRemoteUnicastAddressRefs(self) -> List[RefType]:
        """
        This reference defines the remote unicast addresses of Service consumers. This reference shall ONLY be used if the remote unicast address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES
        """
        return self.staticRemoteUnicastAddressRefs


class DdsCpServiceInstanceEvent(ARObject, VariationPointCapable):
    """
    This element represents an event as part of the Provided Service Instance. Tags: atp.Status=candidate
    """

    # DdsCpServiceInstanceEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.155, p.475
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDdsEventRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsEventRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsEventQosProfileRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsEventQosProfileRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsEventTopicRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsEventTopicRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) —
    # no spec rows (XSD group DDS-CP-SERVICE-INSTANCE-EVENT carries VARIATION-POINT, Rule 0020).

    def __init__(self):
        super().__init__()

        # Reference to the PduTriggerung used for the upper layer transport of this DdsEvent message. Tags: atp.Status=candidate
        self.ddsEventRef: Optional[RefType] = None

        # Reference to the QOS Profile used for this Event. Tags: atp.Status=candidate
        self.ddsEventQosProfileRef: Optional[RefType] = None

        # Reference to the DDS Topic used for this Event. Tags: atp.Status=candidate
        self.ddsEventTopicRef: Optional[RefType] = None

    def getDdsEventRef(self) -> Optional[RefType]:
        """
        Reference to the PduTriggerung used for the upper layer transport of this DdsEvent message. Tags: atp.Status=candidate
        """
        return self.ddsEventRef

    def setDdsEventRef(self, value: Optional[RefType]) -> DdsCpServiceInstanceEvent:
        """
        Reference to the PduTriggerung used for the upper layer transport of this DdsEvent message. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsEventRef.
        """
        if value is not None:
            self.ddsEventRef = value
        return self

    def getDdsEventQosProfileRef(self) -> Optional[RefType]:
        """
        Reference to the QOS Profile used for this Event. Tags: atp.Status=candidate
        """
        return self.ddsEventQosProfileRef

    def setDdsEventQosProfileRef(self, value: Optional[RefType]) -> DdsCpServiceInstanceEvent:
        """
        Reference to the QOS Profile used for this Event. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsEventQosProfileRef.
        """
        if value is not None:
            self.ddsEventQosProfileRef = value
        return self

    def getDdsEventTopicRef(self) -> Optional[RefType]:
        """
        Reference to the DDS Topic used for this Event. Tags: atp.Status=candidate
        """
        return self.ddsEventTopicRef

    def setDdsEventTopicRef(self, value: Optional[RefType]) -> DdsCpServiceInstanceEvent:
        """
        Reference to the DDS Topic used for this Event. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsEventTopicRef.
        """
        if value is not None:
            self.ddsEventTopicRef = value
        return self


class DdsCpServiceInstanceOperation(ARObject, VariationPointCapable):
    """
    This element represents an operation as part of the Provided Service Instance. Tags: atp.Status=candidate
    """

    # DdsCpServiceInstanceOperation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.156, p.476
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDdsOperationRequestTriggeringRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsOperationRequestTriggeringRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsOperationResponseTriggeringRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsOperationResponseTriggeringRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) —
    # no spec rows (XSD group DDS-CP-SERVICE-INSTANCE-OPERATION carries VARIATION-POINT, Rule 0020).

    def __init__(self):
        super().__init__()

        # Reference to the PduTriggering used for the upper layer transport of this DdsOperation request message. Tags: atp.Status=candidate
        self.ddsOperationRequestTriggeringRef: Optional[RefType] = None

        # Reference to the PduTriggering used for the upper layer transport of this DdsOperation response message. Tags: atp.Status=candidate
        self.ddsOperationResponseTriggeringRef: Optional[RefType] = None

    def getDdsOperationRequestTriggeringRef(self) -> Optional[RefType]:
        """
        Reference to the PduTriggering used for the upper layer transport of this DdsOperation request message. Tags: atp.Status=candidate
        """
        return self.ddsOperationRequestTriggeringRef

    def setDdsOperationRequestTriggeringRef(self, value: Optional[RefType]) -> DdsCpServiceInstanceOperation:
        """
        Reference to the PduTriggering used for the upper layer transport of this DdsOperation request message. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsOperationRequestTriggeringRef.
        """
        if value is not None:
            self.ddsOperationRequestTriggeringRef = value
        return self

    def getDdsOperationResponseTriggeringRef(self) -> Optional[RefType]:
        """
        Reference to the PduTriggering used for the upper layer transport of this DdsOperation response message. Tags: atp.Status=candidate
        """
        return self.ddsOperationResponseTriggeringRef

    def setDdsOperationResponseTriggeringRef(self, value: Optional[RefType]) -> DdsCpServiceInstanceOperation:
        """
        Reference to the PduTriggering used for the upper layer transport of this DdsOperation response message. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ddsOperationResponseTriggeringRef.
        """
        if value is not None:
            self.ddsOperationResponseTriggeringRef = value
        return self


class DdsDeadline(ARObject):
    """
    Describes the DDS DEADLINE QoS policy. Tags: atp.Status=candidate
    """

    # DdsDeadline method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.185, p.532
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDeadlinePeriod   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDeadlinePeriod   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "DEADLINE" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        self.deadlinePeriod: Optional[Float] = None

    def getDeadlinePeriod(self) -> Optional[Float]:
        """
        See "DEADLINE" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        """
        return self.deadlinePeriod

    def setDeadlinePeriod(self, value: Optional[Float]) -> DdsDeadline:
        """
        See "DEADLINE" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing deadlinePeriod.
        """
        if value is not None:
            self.deadlinePeriod = value
        return self


class DdsDestinationOrder(ARObject):
    """
    Describes the DDS DESTINATION_ORDER QoS policy. Tags: atp.Status=candidate
    """

    # DdsDestinationOrder method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.196, p.536
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDestinationOrderKind      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationOrderKind      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "DESTINATION_ORDER" chapter of DDS. Tags: atp.Status=candidate
        self.destinationOrderKind: Optional[DdsDestinationOrderKindEnum] = None

    def getDestinationOrderKind(self) -> Optional[DdsDestinationOrderKindEnum]:
        """
        See "DESTINATION_ORDER" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.destinationOrderKind

    def setDestinationOrderKind(self, value: Optional[DdsDestinationOrderKindEnum]) -> DdsDestinationOrder:
        """
        See "DESTINATION_ORDER" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing destinationOrderKind.
        """
        if value is not None:
            self.destinationOrderKind = value
        return self


class DdsDurability(ARObject):
    """
    Describes the DDS DURABILITY QoS policy. Tags: atp.Status=candidate
    """

    # DdsDurability method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.181, p.530
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDurabilityKind     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityKind     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "DURABILITY" chapter in DDS. Tags: atp.Status=candidate
        self.durabilityKind: Optional[DdsDurabilityKindEnum] = None

    def getDurabilityKind(self) -> Optional[DdsDurabilityKindEnum]:
        """
        See "DURABILITY" chapter in DDS. Tags: atp.Status=candidate
        """
        return self.durabilityKind

    def setDurabilityKind(self, value: Optional[DdsDurabilityKindEnum]) -> DdsDurability:
        """
        See "DURABILITY" chapter in DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityKind.
        """
        if value is not None:
            self.durabilityKind = value
        return self


class DdsDurabilityService(ARObject):
    """
    Describes the DDS DURABILITY_SERVICE QoS policy. Tags: atp.Status=candidate
    """

    # DdsDurabilityService method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.183, p.531
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDurabilityServiceCleanupDelay          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityServiceCleanupDelay          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDurabilityServiceHistoryDepth          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityServiceHistoryDepth          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDurabilityServiceHistoryKind           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityServiceHistoryKind           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDurabilityServiceMaxInstances          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityServiceMaxInstances          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDurabilityServiceMaxSamples            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityServiceMaxSamples            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDurabilityServiceMaxSamplesPerInstance [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDurabilityServiceMaxSamplesPerInstance [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "DURABILITY_SERVICE" chapter in DDS. Time given in seconds. Tags: atp.Status=candidate
        self.durabilityServiceCleanupDelay: Optional[Float] = None

        # See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        self.durabilityServiceHistoryDepth: Optional[PositiveInteger] = None

        # See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        self.durabilityServiceHistoryKind: Optional[DdsDurabilityServiceHistoryKindEnum] = None

        # See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        self.durabilityServiceMaxInstances: Optional[PositiveInteger] = None

        # See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        self.durabilityServiceMaxSamples: Optional[PositiveInteger] = None

        # See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        self.durabilityServiceMaxSamplesPerInstance: Optional[PositiveInteger] = None

    def getDurabilityServiceCleanupDelay(self) -> Optional[Float]:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Time given in seconds. Tags: atp.Status=candidate
        """
        return self.durabilityServiceCleanupDelay

    def setDurabilityServiceCleanupDelay(self, value: Optional[Float]) -> DdsDurabilityService:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Time given in seconds. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityServiceCleanupDelay.
        """
        if value is not None:
            self.durabilityServiceCleanupDelay = value
        return self

    def getDurabilityServiceHistoryDepth(self) -> Optional[PositiveInteger]:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        """
        return self.durabilityServiceHistoryDepth

    def setDurabilityServiceHistoryDepth(self, value: Optional[PositiveInteger]) -> DdsDurabilityService:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityServiceHistoryDepth.
        """
        if value is not None:
            self.durabilityServiceHistoryDepth = value
        return self

    def getDurabilityServiceHistoryKind(self) -> Optional[DdsDurabilityServiceHistoryKindEnum]:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        """
        return self.durabilityServiceHistoryKind

    def setDurabilityServiceHistoryKind(self, value: Optional[DdsDurabilityServiceHistoryKindEnum]) -> DdsDurabilityService:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityServiceHistoryKind.
        """
        if value is not None:
            self.durabilityServiceHistoryKind = value
        return self

    def getDurabilityServiceMaxInstances(self) -> Optional[PositiveInteger]:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        """
        return self.durabilityServiceMaxInstances

    def setDurabilityServiceMaxInstances(self, value: Optional[PositiveInteger]) -> DdsDurabilityService:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityServiceMaxInstances.
        """
        if value is not None:
            self.durabilityServiceMaxInstances = value
        return self

    def getDurabilityServiceMaxSamples(self) -> Optional[PositiveInteger]:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        """
        return self.durabilityServiceMaxSamples

    def setDurabilityServiceMaxSamples(self, value: Optional[PositiveInteger]) -> DdsDurabilityService:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityServiceMaxSamples.
        """
        if value is not None:
            self.durabilityServiceMaxSamples = value
        return self

    def getDurabilityServiceMaxSamplesPerInstance(self) -> Optional[PositiveInteger]:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate
        """
        return self.durabilityServiceMaxSamplesPerInstance

    def setDurabilityServiceMaxSamplesPerInstance(self, value: Optional[PositiveInteger]) -> DdsDurabilityService:
        """
        See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing durabilityServiceMaxSamplesPerInstance.
        """
        if value is not None:
            self.durabilityServiceMaxSamplesPerInstance = value
        return self


class DdsHistory(ARObject):
    """
    Describes the DDS HISTORY QoS policy. Tags: atp.Status=candidate
    """

    # DdsHistory method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.198, p.537
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getHistoryKind            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHistoryKind            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHistoryOrderDepth      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHistoryOrderDepth      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "HISTORY" chapter of DDS. Tags: atp.Status=candidate
        self.historyKind: Optional[DdsHistoryKindEnum] = None

        # See "HISTORY" chapter of DDS. Tags: atp.Status=candidate
        self.historyOrderDepth: Optional[PositiveInteger] = None

    def getHistoryKind(self) -> Optional[DdsHistoryKindEnum]:
        """
        See "HISTORY" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.historyKind

    def setHistoryKind(self, value: Optional[DdsHistoryKindEnum]) -> DdsHistory:
        """
        See "HISTORY" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing historyKind.
        """
        if value is not None:
            self.historyKind = value
        return self

    def getHistoryOrderDepth(self) -> Optional[PositiveInteger]:
        """
        See "HISTORY" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.historyOrderDepth

    def setHistoryOrderDepth(self, value: Optional[PositiveInteger]) -> DdsHistory:
        """
        See "HISTORY" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing historyOrderDepth.
        """
        if value is not None:
            self.historyOrderDepth = value
        return self


class DdsLatencyBudget(ARObject):
    """
    Describes the DDS LATENCY_BUDGET QoS policy. Tags: atp.Status=candidate
    """

    # DdsLatencyBudget method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.186, p.532
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLatencyBudgetDuration   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLatencyBudgetDuration   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "LATENCY_BUDGET" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        self.latencyBudgetDuration: Optional[Float] = None

    def getLatencyBudgetDuration(self) -> Optional[Float]:
        """
        See "LATENCY_BUDGET" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        """
        return self.latencyBudgetDuration

    def setLatencyBudgetDuration(self, value: Optional[Float]) -> DdsLatencyBudget:
        """
        See "LATENCY_BUDGET" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing latencyBudgetDuration.
        """
        if value is not None:
            self.latencyBudgetDuration = value
        return self


class DdsLifespan(ARObject):
    """
    Describes the DDS LIFESPAN QoS policy. Tags: atp.Status=candidate
    """

    # DdsLifespan method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.195, p.536
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLifespanDuration      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLifespanDuration      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "LIFESPAN" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        self.lifespanDuration: Optional[Float] = None

    def getLifespanDuration(self) -> Optional[Float]:
        """
        See "LIFESPAN" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        """
        return self.lifespanDuration

    def setLifespanDuration(self, value: Optional[Float]) -> DdsLifespan:
        """
        See "LIFESPAN" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing lifespanDuration.
        """
        if value is not None:
            self.lifespanDuration = value
        return self


class DdsLiveliness(ARObject):
    """
    Describes the DDS LIVELINESS QoS policy. Tags: atp.Status=candidate
    """

    # DdsLiveliness method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.190, p.534
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLivelinessLeaseDuration      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLivelinessLeaseDuration      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLivenessKind                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLivenessKind                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "LIVELINESS" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        self.livelinessLeaseDuration: Optional[Float] = None

        # See "LIVELINESS" chapter of DDS. Tags: atp.Status=candidate
        self.livenessKind: Optional[DdsLivenessKindEnum] = None

    def getLivelinessLeaseDuration(self) -> Optional[Float]:
        """
        See "LIVELINESS" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        """
        return self.livelinessLeaseDuration

    def setLivelinessLeaseDuration(self, value: Optional[Float]) -> DdsLiveliness:
        """
        See "LIVELINESS" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing livelinessLeaseDuration.
        """
        if value is not None:
            self.livelinessLeaseDuration = value
        return self

    def getLivenessKind(self) -> Optional[DdsLivenessKindEnum]:
        """
        See "LIVELINESS" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.livenessKind

    def setLivenessKind(self, value: Optional[DdsLivenessKindEnum]) -> DdsLiveliness:
        """
        See "LIVELINESS" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing livenessKind.
        """
        if value is not None:
            self.livenessKind = value
        return self


class DdsOwnership(ARObject):
    """
    Describes the DDS OWNERSHIP QoS policy. Tags: atp.Status=candidate
    """

    # DdsOwnership method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.187, p.532
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOwnershipKind    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOwnershipKind    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "OWNERSHIP" chapter of DDS. Tags: atp.Status=candidate
        self.ownershipKind: Optional[DdsOwnershipKindEnum] = None

    def getOwnershipKind(self) -> Optional[DdsOwnershipKindEnum]:
        """
        See "OWNERSHIP" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.ownershipKind

    def setOwnershipKind(self, value: Optional[DdsOwnershipKindEnum]) -> DdsOwnership:
        """
        See "OWNERSHIP" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ownershipKind.
        """
        if value is not None:
            self.ownershipKind = value
        return self


class DdsOwnershipStrength(ARObject):
    """
    Describes the DDS OWNERSHIP_STRENGTH QoS policy. Tags: atp.Status=candidate
    """

    # DdsOwnershipStrength method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.189, p.533
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOwnershipStrength    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOwnershipStrength    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "OWNERSHIP_STRENGTH" chapter of DDS. Tags: atp.Status=candidate
        self.ownershipStrength: Optional[PositiveInteger] = None

    def getOwnershipStrength(self) -> Optional[PositiveInteger]:
        """
        See "OWNERSHIP_STRENGTH" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.ownershipStrength

    def setOwnershipStrength(self, value: Optional[PositiveInteger]) -> DdsOwnershipStrength:
        """
        See "OWNERSHIP_STRENGTH" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ownershipStrength.
        """
        if value is not None:
            self.ownershipStrength = value
        return self


class DdsReliability(ARObject):
    """
    Describes the DDS RELIABILITY QoS policy. Tags: atp.Status=candidate
    """

    # DdsReliability method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.192, p.535
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReliabilityKind            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReliabilityKind            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReliabilityMaxBlockingTime [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReliabilityMaxBlockingTime [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "RELIABILITY" chapter of DDS. Tags: atp.Status=candidate
        self.reliabilityKind: Optional[DdsReliabilityKindEnum] = None

        # See "RELIABILITY" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        self.reliabilityMaxBlockingTime: Optional[Float] = None

    def getReliabilityKind(self) -> Optional[DdsReliabilityKindEnum]:
        """
        See "RELIABILITY" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.reliabilityKind

    def setReliabilityKind(self, value: Optional[DdsReliabilityKindEnum]) -> DdsReliability:
        """
        See "RELIABILITY" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing reliabilityKind.
        """
        if value is not None:
            self.reliabilityKind = value
        return self

    def getReliabilityMaxBlockingTime(self) -> Optional[Float]:
        """
        See "RELIABILITY" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate
        """
        return self.reliabilityMaxBlockingTime

    def setReliabilityMaxBlockingTime(self, value: Optional[Float]) -> DdsReliability:
        """
        See "RELIABILITY" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing reliabilityMaxBlockingTime.
        """
        if value is not None:
            self.reliabilityMaxBlockingTime = value
        return self


class DdsResourceLimits(ARObject):
    """
    Describes the DDS RESOURCE_LIMITS QoS policy. Tags: atp.Status=candidate
    """

    # DdsResourceLimits method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.200, p.538
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxInstances             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxInstances             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxSamples               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxSamples               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxSamplesPerInstance    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxSamplesPerInstance    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "RESOURCE_LIMITS" chapter of DDS.
        self.maxInstances: Optional[PositiveInteger] = None

        # See "RESOURCE_LIMITS" chapter of DDS. Tags: atp.Status=candidate
        self.maxSamples: Optional[PositiveInteger] = None

        # See "RESOURCE_LIMITS" chapter of DDS.
        self.maxSamplesPerInstance: Optional[PositiveInteger] = None

    def getMaxInstances(self) -> Optional[PositiveInteger]:
        """
        See "RESOURCE_LIMITS" chapter of DDS.
        """
        return self.maxInstances

    def setMaxInstances(self, value: Optional[PositiveInteger]) -> DdsResourceLimits:
        """
        See "RESOURCE_LIMITS" chapter of DDS.

        A None value is a no-op and does not overwrite an existing maxInstances.
        """
        if value is not None:
            self.maxInstances = value
        return self

    def getMaxSamples(self) -> Optional[PositiveInteger]:
        """
        See "RESOURCE_LIMITS" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.maxSamples

    def setMaxSamples(self, value: Optional[PositiveInteger]) -> DdsResourceLimits:
        """
        See "RESOURCE_LIMITS" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing maxSamples.
        """
        if value is not None:
            self.maxSamples = value
        return self

    def getMaxSamplesPerInstance(self) -> Optional[PositiveInteger]:
        """
        See "RESOURCE_LIMITS" chapter of DDS.
        """
        return self.maxSamplesPerInstance

    def setMaxSamplesPerInstance(self, value: Optional[PositiveInteger]) -> DdsResourceLimits:
        """
        See "RESOURCE_LIMITS" chapter of DDS.

        A None value is a no-op and does not overwrite an existing maxSamplesPerInstance.
        """
        if value is not None:
            self.maxSamplesPerInstance = value
        return self


class DdsTopicData(ARObject):
    """
    Describes the DDS TOPIC_DATA QoS policy. Tags: atp.Status=candidate
    """

    # DdsTopicData method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.180, p.529
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTopicData   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTopicData   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "TOPIC_DATA" chapter in DDS. Tags: atp.Status=candidate
        self.topicData: Optional[String] = None

    def getTopicData(self) -> Optional[String]:
        """
        See "TOPIC_DATA" chapter in DDS. Tags: atp.Status=candidate
        """
        return self.topicData

    def setTopicData(self, value: Optional[String]) -> DdsTopicData:
        """
        See "TOPIC_DATA" chapter in DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing topicData.
        """
        if value is not None:
            self.topicData = value
        return self


class DdsTransportPriority(ARObject):
    """
    Describes the DDS TRANSPORT_PRIORITY QoS policy. Tags: atp.Status=candidate
    """

    # DdsTransportPriority method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.194, p.535
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTransportPriority      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransportPriority      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # See "TRANSPORT_PRIORITY" chapter of DDS. Tags: atp.Status=candidate
        self.transportPriority: Optional[PositiveInteger] = None

    def getTransportPriority(self) -> Optional[PositiveInteger]:
        """
        See "TRANSPORT_PRIORITY" chapter of DDS. Tags: atp.Status=candidate
        """
        return self.transportPriority

    def setTransportPriority(self, value: Optional[PositiveInteger]) -> DdsTransportPriority:
        """
        See "TRANSPORT_PRIORITY" chapter of DDS. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing transportPriority.
        """
        if value is not None:
            self.transportPriority = value
        return self


class EthGlobalTimeManagedCouplingPort(ARObject):
    """
    Specifies a CouplingPort which is managed by an Ethernet Global Time Domain.
    """

    # EthGlobalTimeManagedCouplingPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.17, p.875
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCouplingPortRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCouplingPortRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getGlobalTimePortRole               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGlobalTimePortRole               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getGlobalTimeTxPeriod               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGlobalTimeTxPeriod               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPdelayLatencyThreshold           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPdelayLatencyThreshold           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPdelayRequestPeriod              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPdelayRequestPeriod              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPdelayRespAndRespFollowUpTimeout [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPdelayRespAndRespFollowUpTimeout [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPdelayResponseEnabled            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPdelayResponseEnabled            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Aggregator dispatch (EthGlobalTimeDomainProps.managedCouplingPort) is pending —
    # EthGlobalTimeDomainProps is a later-wave class; the reusable
    # readEthGlobalTimeManagedCouplingPort / writeEthGlobalTimeManagedCouplingPort helpers own
    # the ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT element (AUTOSAR_00052.xsd l.55634).

    def __init__(self):
        super().__init__()

        # Defines which CouplingPort is managed by this EthGlobalTimeManagedCouplingPort.
        self.couplingPortRef: Optional[RefType] = None

        # This attribute defines the port behavior.
        self.globalTimePortRole: Optional[GlobalTimePortRoleEnum] = None

        # This attribute defines the TX period in seconds
        self.globalTimeTxPeriod: Optional[TimeValue] = None

        # Threshold for calculated Pdelay. If a measured Pdelay exceeds pdelayLatencyThreshold, the measured Pdelay value is discarded.
        self.pdelayLatencyThreshold: Optional[TimeValue] = None

        # Defines the period for the pdelay request messages.
        self.pdelayRequestPeriod: Optional[TimeValue] = None

        # Timeout value for Pdelay_Resp and Pdelay_Resp_Follow_Up after a Pdelay_Req has been transmitted resp. a Pdelay_Resp has been received. A value of 0 or not defining this attribute deactivates this timeout observation.
        self.pdelayRespAndRespFollowUpTimeout: Optional[TimeValue] = None

        # Defines whether PDELAY RESPONSE and PDELAY RESPONSE FOLLOW UP shall be sent on this Coupling Port.
        self.pdelayResponseEnabled: Optional[Boolean] = None

    def getCouplingPortRef(self) -> Optional[RefType]:
        """
        Defines which CouplingPort is managed by this EthGlobalTimeManagedCouplingPort.
        """
        return self.couplingPortRef

    def setCouplingPortRef(self, value: Optional[RefType]) -> EthGlobalTimeManagedCouplingPort:
        """
        Defines which CouplingPort is managed by this EthGlobalTimeManagedCouplingPort.

        A None value is a no-op and does not overwrite an existing couplingPortRef.
        """
        if value is not None:
            self.couplingPortRef = value
        return self

    def getGlobalTimePortRole(self) -> Optional[GlobalTimePortRoleEnum]:
        """
        This attribute defines the port behavior.
        """
        return self.globalTimePortRole

    def setGlobalTimePortRole(self, value: Optional[GlobalTimePortRoleEnum]) -> EthGlobalTimeManagedCouplingPort:
        """
        This attribute defines the port behavior.

        A None value is a no-op and does not overwrite an existing globalTimePortRole.
        """
        if value is not None:
            self.globalTimePortRole = value
        return self

    def getGlobalTimeTxPeriod(self) -> Optional[TimeValue]:
        """
        This attribute defines the TX period in seconds
        """
        return self.globalTimeTxPeriod

    def setGlobalTimeTxPeriod(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        This attribute defines the TX period in seconds

        A None value is a no-op and does not overwrite an existing globalTimeTxPeriod.
        """
        if value is not None:
            self.globalTimeTxPeriod = value
        return self

    def getPdelayLatencyThreshold(self) -> Optional[TimeValue]:
        """
        Threshold for calculated Pdelay. If a measured Pdelay exceeds pdelayLatencyThreshold, the measured Pdelay value is discarded.
        """
        return self.pdelayLatencyThreshold

    def setPdelayLatencyThreshold(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        Threshold for calculated Pdelay. If a measured Pdelay exceeds pdelayLatencyThreshold, the measured Pdelay value is discarded.

        A None value is a no-op and does not overwrite an existing pdelayLatencyThreshold.
        """
        if value is not None:
            self.pdelayLatencyThreshold = value
        return self

    def getPdelayRequestPeriod(self) -> Optional[TimeValue]:
        """
        Defines the period for the pdelay request messages.
        """
        return self.pdelayRequestPeriod

    def setPdelayRequestPeriod(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        Defines the period for the pdelay request messages.

        A None value is a no-op and does not overwrite an existing pdelayRequestPeriod.
        """
        if value is not None:
            self.pdelayRequestPeriod = value
        return self

    def getPdelayRespAndRespFollowUpTimeout(self) -> Optional[TimeValue]:
        """
        Timeout value for Pdelay_Resp and Pdelay_Resp_Follow_Up after a Pdelay_Req has been transmitted resp. a Pdelay_Resp has been received. A value of 0 or not defining this attribute deactivates this timeout observation.
        """
        return self.pdelayRespAndRespFollowUpTimeout

    def setPdelayRespAndRespFollowUpTimeout(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        Timeout value for Pdelay_Resp and Pdelay_Resp_Follow_Up after a Pdelay_Req has been transmitted resp. a Pdelay_Resp has been received. A value of 0 or not defining this attribute deactivates this timeout observation.

        A None value is a no-op and does not overwrite an existing pdelayRespAndRespFollowUpTimeout.
        """
        if value is not None:
            self.pdelayRespAndRespFollowUpTimeout = value
        return self

    def getPdelayResponseEnabled(self) -> Optional[Boolean]:
        """
        Defines whether PDELAY RESPONSE and PDELAY RESPONSE FOLLOW UP shall be sent on this Coupling Port.
        """
        return self.pdelayResponseEnabled

    def setPdelayResponseEnabled(self, value: Optional[Boolean]) -> EthGlobalTimeManagedCouplingPort:
        """
        Defines whether PDELAY RESPONSE and PDELAY RESPONSE FOLLOW UP shall be sent on this Coupling Port.

        A None value is a no-op and does not overwrite an existing pdelayResponseEnabled.
        """
        if value is not None:
            self.pdelayResponseEnabled = value
        return self


class EthTSynCrcFlags(ARObject):
    """
    Defines the fields of the message which shall be taken into account for CRC calculation and verification.
    """

    # EthTSynCrcFlags method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.15, p.868
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCrcCorrectionField         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcCorrectionField         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrcDomainNumber            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcDomainNumber            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrcMessageLength           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcMessageLength           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrcPreciseOriginTimestamp  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcPreciseOriginTimestamp  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrcSequenceId              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcSequenceId              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrcSourcePortIdentity      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcSourcePortIdentity      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Aggregator dispatch (EthGlobalTimeDomainProps.crcFlags) is pending — EthGlobalTimeDomainProps
    # is a later-wave class; the reusable readEthTSynCrcFlags / writeEthTSynCrcFlags helpers own
    # the ETH-T-SYN-CRC-FLAGS element (AUTOSAR_00052.xsd l.55765).

    def __init__(self):
        super().__init__()

        # CorrectionField from the Follow_Up Message Header shall be included in CRC calculation.
        self.crcCorrectionField: Optional[Boolean] = None

        # DomainNumber from the Follow_Up Message Header shall be included in CRC calculation.
        self.crcDomainNumber: Optional[Boolean] = None

        # MessageLength from the Follow_Up Message Header shall be included in CRC calculation.
        self.crcMessageLength: Optional[Boolean] = None

        # PreciseOriginTimestamp from the Follow_Up Message Field shall be included in CRC calculation.
        self.crcPreciseOriginTimestamp: Optional[Boolean] = None

        # SequenceId from the Follow_Up Message Header shall be included in CRC calculation.
        self.crcSequenceId: Optional[Boolean] = None

        # SourcePortIdentity from the Follow_Up Message Header shall be included in CRC calculation.
        self.crcSourcePortIdentity: Optional[Boolean] = None

    def getCrcCorrectionField(self) -> Optional[Boolean]:
        """
        CorrectionField from the Follow_Up Message Header shall be included in CRC calculation.
        """
        return self.crcCorrectionField

    def setCrcCorrectionField(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        CorrectionField from the Follow_Up Message Header shall be included in CRC calculation.

        A None value is a no-op and does not overwrite an existing crcCorrectionField.
        """
        if value is not None:
            self.crcCorrectionField = value
        return self

    def getCrcDomainNumber(self) -> Optional[Boolean]:
        """
        DomainNumber from the Follow_Up Message Header shall be included in CRC calculation.
        """
        return self.crcDomainNumber

    def setCrcDomainNumber(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        DomainNumber from the Follow_Up Message Header shall be included in CRC calculation.

        A None value is a no-op and does not overwrite an existing crcDomainNumber.
        """
        if value is not None:
            self.crcDomainNumber = value
        return self

    def getCrcMessageLength(self) -> Optional[Boolean]:
        """
        MessageLength from the Follow_Up Message Header shall be included in CRC calculation.
        """
        return self.crcMessageLength

    def setCrcMessageLength(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        MessageLength from the Follow_Up Message Header shall be included in CRC calculation.

        A None value is a no-op and does not overwrite an existing crcMessageLength.
        """
        if value is not None:
            self.crcMessageLength = value
        return self

    def getCrcPreciseOriginTimestamp(self) -> Optional[Boolean]:
        """
        PreciseOriginTimestamp from the Follow_Up Message Field shall be included in CRC calculation.
        """
        return self.crcPreciseOriginTimestamp

    def setCrcPreciseOriginTimestamp(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        PreciseOriginTimestamp from the Follow_Up Message Field shall be included in CRC calculation.

        A None value is a no-op and does not overwrite an existing crcPreciseOriginTimestamp.
        """
        if value is not None:
            self.crcPreciseOriginTimestamp = value
        return self

    def getCrcSequenceId(self) -> Optional[Boolean]:
        """
        SequenceId from the Follow_Up Message Header shall be included in CRC calculation.
        """
        return self.crcSequenceId

    def setCrcSequenceId(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        SequenceId from the Follow_Up Message Header shall be included in CRC calculation.

        A None value is a no-op and does not overwrite an existing crcSequenceId.
        """
        if value is not None:
            self.crcSequenceId = value
        return self

    def getCrcSourcePortIdentity(self) -> Optional[Boolean]:
        """
        SourcePortIdentity from the Follow_Up Message Header shall be included in CRC calculation.
        """
        return self.crcSourcePortIdentity

    def setCrcSourcePortIdentity(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        SourcePortIdentity from the Follow_Up Message Header shall be included in CRC calculation.

        A None value is a no-op and does not overwrite an existing crcSourcePortIdentity.
        """
        if value is not None:
            self.crcSourcePortIdentity = value
        return self


class EthTSynSubTlvConfig(ARObject):
    """
    Defines the subTLV fields which shall be included in the time sync message.
    """

    # EthTSynSubTlvConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.12, p.867
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOfsSubTlv         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOfsSubTlv         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStatusSubTlv      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStatusSubTlv      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeSubTlv        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeSubTlv        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUserDataSubTlv    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUserDataSubTlv    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Aggregator dispatch (GlobalTimeEthMaster.subTlvConfig) is pending — GlobalTimeEthMaster
    # is a later-wave class; the reusable readEthTSynSubTlvConfig / writeEthTSynSubTlvConfig
    # helpers own the ETH-T-SYN-SUB-TLV-CONFIG element (AUTOSAR_00052.xsd l.55824).

    def __init__(self):
        super().__init__()

        # Defines whether an AUTOSAR Follow_Up TLV OFS Sub-TLV is used.
        self.ofsSubTlv: Optional[Boolean] = None

        # Defines whether an AUTOSAR Follow_Up TLV Status Sub-TLV is used.
        self.statusSubTlv: Optional[Boolean] = None

        # Defines whether an AUTOSAR Follow_Up TLV Time Sub-TLV is used.
        self.timeSubTlv: Optional[Boolean] = None

        # Defines whether an AUTOSAR Follow_Up TLV UserData Sub-TLV is used.
        self.userDataSubTlv: Optional[Boolean] = None

    def getOfsSubTlv(self) -> Optional[Boolean]:
        """
        Defines whether an AUTOSAR Follow_Up TLV OFS Sub-TLV is used.
        """
        return self.ofsSubTlv

    def setOfsSubTlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Defines whether an AUTOSAR Follow_Up TLV OFS Sub-TLV is used.

        A None value is a no-op and does not overwrite an existing ofsSubTlv.
        """
        if value is not None:
            self.ofsSubTlv = value
        return self

    def getStatusSubTlv(self) -> Optional[Boolean]:
        """
        Defines whether an AUTOSAR Follow_Up TLV Status Sub-TLV is used.
        """
        return self.statusSubTlv

    def setStatusSubTlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Defines whether an AUTOSAR Follow_Up TLV Status Sub-TLV is used.

        A None value is a no-op and does not overwrite an existing statusSubTlv.
        """
        if value is not None:
            self.statusSubTlv = value
        return self

    def getTimeSubTlv(self) -> Optional[Boolean]:
        """
        Defines whether an AUTOSAR Follow_Up TLV Time Sub-TLV is used.
        """
        return self.timeSubTlv

    def setTimeSubTlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Defines whether an AUTOSAR Follow_Up TLV Time Sub-TLV is used.

        A None value is a no-op and does not overwrite an existing timeSubTlv.
        """
        if value is not None:
            self.timeSubTlv = value
        return self

    def getUserDataSubTlv(self) -> Optional[Boolean]:
        """
        Defines whether an AUTOSAR Follow_Up TLV UserData Sub-TLV is used.
        """
        return self.userDataSubTlv

    def setUserDataSubTlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Defines whether an AUTOSAR Follow_Up TLV UserData Sub-TLV is used.

        A None value is a no-op and does not overwrite an existing userDataSubTlv.
        """
        if value is not None:
            self.userDataSubTlv = value
        return self


class GlobalTimeCorrectionProps(ARObject):
    """
    This meta-class defines the attributes for rate and offset correction.
    """

    # GlobalTimeCorrectionProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.7, p.862
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOffsetCorrectionAdaptionInterval       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOffsetCorrectionAdaptionInterval       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOffsetCorrectionJumpThreshold          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOffsetCorrectionJumpThreshold          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRateCorrectionMeasurementDuration      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRateCorrectionMeasurementDuration      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRateCorrectionsPerMeasurementDuration  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRateCorrectionsPerMeasurementDuration  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Aggregator dispatch (GlobalTimeDomain.globalTimeCorrectionProps) is pending — GlobalTimeDomain
    # is a later-wave class; the reusable readGlobalTimeCorrectionProps /
    # writeGlobalTimeCorrectionProps helpers own the GLOBAL-TIME-CORRECTION-PROPS element.

    def __init__(self):
        super().__init__()

        # Defines the interval during which the adaptive rate correction cancels out the rate- and time deviation.
        self.offsetCorrectionAdaptionInterval: Optional[TimeValue] = None

        # Threshold for the correction method. Deviations below this value will be corrected by a linear reduction over a defined timespan. Values equal- and greater than this value will be corrected by immediately setting the correct time- and rate in form of a jump.
        self.offsetCorrectionJumpThreshold: Optional[TimeValue] = None

        # Definition of the time span which is used to calculate the rate deviation.
        self.rateCorrectionMeasurementDuration: Optional[TimeValue] = None

        # Defines the number of simultaneous rate measurements to determine the current rate deviation.
        self.rateCorrectionsPerMeasurementDuration: Optional[PositiveInteger] = None

    def getOffsetCorrectionAdaptionInterval(self) -> Optional[TimeValue]:
        """
        Defines the interval during which the adaptive rate correction cancels out the rate- and time deviation.
        """
        return self.offsetCorrectionAdaptionInterval

    def setOffsetCorrectionAdaptionInterval(self, value: Optional[TimeValue]) -> GlobalTimeCorrectionProps:
        """
        Defines the interval during which the adaptive rate correction cancels out the rate- and time deviation.

        A None value is a no-op and does not overwrite an existing offsetCorrectionAdaptionInterval.
        """
        if value is not None:
            self.offsetCorrectionAdaptionInterval = value
        return self

    def getOffsetCorrectionJumpThreshold(self) -> Optional[TimeValue]:
        """
        Threshold for the correction method. Deviations below this value will be corrected by a linear reduction over a defined timespan. Values equal- and greater than this value will be corrected by immediately setting the correct time- and rate in form of a jump.
        """
        return self.offsetCorrectionJumpThreshold

    def setOffsetCorrectionJumpThreshold(self, value: Optional[TimeValue]) -> GlobalTimeCorrectionProps:
        """
        Threshold for the correction method. Deviations below this value will be corrected by a linear reduction over a defined timespan. Values equal- and greater than this value will be corrected by immediately setting the correct time- and rate in form of a jump.

        A None value is a no-op and does not overwrite an existing offsetCorrectionJumpThreshold.
        """
        if value is not None:
            self.offsetCorrectionJumpThreshold = value
        return self

    def getRateCorrectionMeasurementDuration(self) -> Optional[TimeValue]:
        """
        Definition of the time span which is used to calculate the rate deviation.
        """
        return self.rateCorrectionMeasurementDuration

    def setRateCorrectionMeasurementDuration(self, value: Optional[TimeValue]) -> GlobalTimeCorrectionProps:
        """
        Definition of the time span which is used to calculate the rate deviation.

        A None value is a no-op and does not overwrite an existing rateCorrectionMeasurementDuration.
        """
        if value is not None:
            self.rateCorrectionMeasurementDuration = value
        return self

    def getRateCorrectionsPerMeasurementDuration(self) -> Optional[PositiveInteger]:
        """
        Defines the number of simultaneous rate measurements to determine the current rate deviation.
        """
        return self.rateCorrectionsPerMeasurementDuration

    def setRateCorrectionsPerMeasurementDuration(self, value: Optional[PositiveInteger]) -> GlobalTimeCorrectionProps:
        """
        Defines the number of simultaneous rate measurements to determine the current rate deviation.

        A None value is a no-op and does not overwrite an existing rateCorrectionsPerMeasurementDuration.
        """
        if value is not None:
            self.rateCorrectionsPerMeasurementDuration = value
        return self


class IEEE1722TpAcfBusPart(ARObject, ABC):
    pass


class IEEE1722TpAcfLin(ARObject):
    pass


class IdsmInstance(ARObject):
    pass


class IdsmTrafficLimitation(ARObject):
    pass


class J1939TpConfig(ARObject):
    pass


class J1939TpConnection(ARObject):
    pass


class J1939TpPg(ARObject):
    pass


class NetworkSegmentIdentification(ARObject):
    """
    This meta-class represents the ability to identify the PhysicalChannel on a system scope in a numerical way. One possible application of this approach is the Time Validation.
    """

    # NetworkSegmentIdentification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.3, p.859
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNetworkSegmentId       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNetworkSegmentId       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Aggregator dispatch (GlobalTimeDomain.networkSegmentId) is pending — GlobalTimeDomain
    # is a later-wave class; the reusable readNetworkSegmentIdentification /
    # writeNetworkSegmentIdentification helpers own the NETWORK-SEGMENT-ID element.

    def __init__(self):
        super().__init__()

        # This attribute represents the numerical identifier of a PhysicalChannel on system level scope.
        self.networkSegmentId: Optional[PositiveInteger] = None

    def getNetworkSegmentId(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the numerical identifier of a PhysicalChannel on system level scope.
        """
        return self.networkSegmentId

    def setNetworkSegmentId(self, value: Optional[PositiveInteger]) -> NetworkSegmentIdentification:
        """
        This attribute represents the numerical identifier of a PhysicalChannel on system level scope.

        A None value is a no-op and does not overwrite an existing networkSegmentId.
        """
        if value is not None:
            self.networkSegmentId = value
        return self


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


class SomeipTpConnection(ARObject):
    pass


class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    """
    This meta-class has the ability to provide a numerical value for a binary manifest item.

    [constr_5202] Existence of attribute BinaryManifestItemNumericalValue.value: For each BinaryManifestItemNumericalValue, attribute value shall exist at the time when the definition of binary object metadata is finished.
    """

    # BinaryManifestItemNumericalValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.26, p.922
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getValue  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # The XSD BINARY-MANIFEST-ITEM-NUMERICAL-VALUE group (AUTOSAR_00052.xsd l.8697) orders VALUE;
    # the reader/writer call the base readBinaryManifestItemValue / writeBinaryManifestItemValue
    # helpers exactly once (ARObject level). Aggregator dispatch (BinaryManifestItem.value /
    # BinaryManifestItem.defaultValue) is pending — BinaryManifestItem is an unsynced later-wave
    # stub.

    def __init__(self):
        super().__init__()

        # This attribute specifies the actual numerical value to be used in the binary manifest handle.
        self.value: Optional[Numerical] = None

    def getValue(self) -> Optional[Numerical]:
        """
        This attribute specifies the actual numerical value to be used in the binary manifest handle.
        """
        return self.value

    def setValue(self, value: Optional[Numerical]) -> BinaryManifestItemNumericalValue:
        """
        This attribute specifies the actual numerical value to be used in the binary manifest handle.

        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    """
    This meta-class has the ability to provide a value for a pointer in the context of a binary manifest item.

    [constr_5218] Existence of attribute BinaryManifestItemPointerValue.address: For each BinaryManifestItemPointerValue, attribute address shall exist at the time when the definition of binary object metadata is finished.

    [constr_5203] Existence of attribute BinaryManifestItemPointerValue.symbol: For each BinaryManifestItemPointerValue, attribute symbol shall exist at the time when the definition of binary object meta-data is finished.
    """

    # BinaryManifestItemPointerValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.27, p.922
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAddress [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddress [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSymbol  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSymbol  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # The XSD BINARY-MANIFEST-ITEM-POINTER-VALUE group (AUTOSAR_00052.xsd l.8727) orders ADDRESS,
    # SYMBOL; the reader/writer call the base readBinaryManifestItemValue /
    # writeBinaryManifestItemValue helpers exactly once (ARObject level). Aggregator dispatch
    # (BinaryManifestItem.value / BinaryManifestItem.defaultValue) is pending — BinaryManifestItem
    # is an unsynced later-wave stub.

    def __init__(self):
        super().__init__()

        # This attribute represents the address value of the enclosing pointer value.
        self.address: Optional[Address] = None

        # This attribute represents the symbol associated with the binary manifest handle.
        self.symbol: Optional[SymbolString] = None

    def getAddress(self) -> Optional[Address]:
        """
        This attribute represents the address value of the enclosing pointer value.
        """
        return self.address

    def setAddress(self, value: Optional[Address]) -> BinaryManifestItemPointerValue:
        """
        This attribute represents the address value of the enclosing pointer value.

        A None value is a no-op and does not overwrite an existing address.
        """
        if value is not None:
            self.address = value
        return self

    def getSymbol(self) -> Optional[SymbolString]:
        """
        This attribute represents the symbol associated with the binary manifest handle.
        """
        return self.symbol

    def setSymbol(self, value: Optional[SymbolString]) -> BinaryManifestItemPointerValue:
        """
        This attribute represents the symbol associated with the binary manifest handle.

        A None value is a no-op and does not overwrite an existing symbol.
        """
        if value is not None:
            self.symbol = value
        return self


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """
    Enables the definition of Can Global Time specific properties.
    """

    # CanGlobalTimeDomainProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.10, p.864
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addFupDataIDList    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFupDataIDLists   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addOfnsDataIDList   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOfnsDataIDLists  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addOfsDataIDList    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOfsDataIDLists   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSyncDataIDList   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSyncDataIDLists  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    #
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)
    # The four DataIDList attributes are ordered 0..16 wrapper lists: the XSD CAN-GLOBAL-TIME-DOMAIN-PROPS
    # group (AUTOSAR_00052.xsd l.15163) wraps <FUP/OFNS/OFS/SYNC-DATA-ID-LIST> items in a
    # <...-DATA-ID-LISTS> wrapper emitted only when non-empty. Aggregator dispatch
    # (GlobalTimeDomain.globalTimeDomainProperty) is pending — GlobalTimeDomain is a later-wave
    # class; the reader/writer call the base readAbstractGlobalTimeDomainProps /
    # writeAbstractGlobalTimeDomainProps helpers (VARIATION-POINT precedes the wrapper elements).

    def __init__(self):
        super().__init__()

        # The DataIDList for FUP messages to calculate CRC.
        self.fupDataIDLists: List[PositiveInteger] = []

        # The DataIDList for OFNS messages to calculate CRC.
        self.ofnsDataIDLists: List[PositiveInteger] = []

        # The DataIDList for OFS messages to calculate CRC.
        self.ofsDataIDLists: List[PositiveInteger] = []

        # The DataIDList for SYNC messages to calculate CRC.
        self.syncDataIDLists: List[PositiveInteger] = []

    def addFupDataIDList(self, value: Optional[PositiveInteger]) -> CanGlobalTimeDomainProps:
        """
        The DataIDList for FUP messages to calculate CRC.

        A None value is a no-op and does not append to fupDataIDLists.
        """
        if value is not None:
            self.fupDataIDLists.append(value)
        return self

    def getFupDataIDLists(self) -> List[PositiveInteger]:
        """
        The DataIDList for FUP messages to calculate CRC.
        """
        return self.fupDataIDLists

    def addOfnsDataIDList(self, value: Optional[PositiveInteger]) -> CanGlobalTimeDomainProps:
        """
        The DataIDList for OFNS messages to calculate CRC.

        A None value is a no-op and does not append to ofnsDataIDLists.
        """
        if value is not None:
            self.ofnsDataIDLists.append(value)
        return self

    def getOfnsDataIDLists(self) -> List[PositiveInteger]:
        """
        The DataIDList for OFNS messages to calculate CRC.
        """
        return self.ofnsDataIDLists

    def addOfsDataIDList(self, value: Optional[PositiveInteger]) -> CanGlobalTimeDomainProps:
        """
        The DataIDList for OFS messages to calculate CRC.

        A None value is a no-op and does not append to ofsDataIDLists.
        """
        if value is not None:
            self.ofsDataIDLists.append(value)
        return self

    def getOfsDataIDLists(self) -> List[PositiveInteger]:
        """
        The DataIDList for OFS messages to calculate CRC.
        """
        return self.ofsDataIDLists

    def addSyncDataIDList(self, value: Optional[PositiveInteger]) -> CanGlobalTimeDomainProps:
        """
        The DataIDList for SYNC messages to calculate CRC.

        A None value is a no-op and does not append to syncDataIDLists.
        """
        if value is not None:
            self.syncDataIDLists.append(value)
        return self

    def getSyncDataIDLists(self) -> List[PositiveInteger]:
        """
        The DataIDList for SYNC messages to calculate CRC.
        """
        return self.syncDataIDLists


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """
    Defines additional attributes for the implementation of Client Server communication between software clusters
    """

    # ClientServerOperationComProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.12, p.903
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getQueueLength     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setQueueLength     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # The XSD CLIENT-SERVER-OPERATION-COM-PROPS group (AUTOSAR_00052.xsd l.17582) follows the (empty)
    # CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE-PROPS group; the reader/writer call the base
    # readCpSoftwareClusterCommunicationResourceProps / writeCpSoftwareClusterCommunicationResourceProps
    # helpers exactly once (ARObject level). Aggregator dispatch
    # (CpSoftwareClusterCommunicationResource.communicationResourceProps) is pending —
    # CpSoftwareClusterCommunicationResource is an unsynced later-wave class.

    def __init__(self):
        super().__init__()

        # Length of call request queue on the server side. The queue is implemented by the SwCluC. The value shall be greater or equal to 1. Setting the value of queueLength to 1 implies that incoming requests are rejected while another request that arrived earlier is being processed.
        self.queueLength: Optional[PositiveInteger] = None

    def getQueueLength(self) -> Optional[PositiveInteger]:
        """
        Length of call request queue on the server side. The queue is implemented by the SwCluC. The value shall be greater or equal to 1. Setting the value of queueLength to 1 implies that incoming requests are rejected while another request that arrived earlier is being processed.
        """
        return self.queueLength

    def setQueueLength(self, value: Optional[PositiveInteger]) -> ClientServerOperationComProps:
        """
        Length of call request queue on the server side. The queue is implemented by the SwCluC. The value shall be greater or equal to 1. Setting the value of queueLength to 1 implies that incoming requests are rejected while another request that arrived earlier is being processed.

        A None value is a no-op and does not overwrite an existing queueLength.
        """
        if value is not None:
            self.queueLength = value
        return self


class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    """
    Represents a single resource required or provided by a CP Software Cluster which relates to the port based communication on VFB level.
    """

    # DataComProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.10, p.903
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataConsistencyPolicy     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataConsistencyPolicy     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSendIndication            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSendIndication            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # The XSD DATA-COM-PROPS group (AUTOSAR_00052.xsd l.26787) follows the (empty)
    # CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE-PROPS group; the reader/writer call the base
    # readCpSoftwareClusterCommunicationResourceProps / writeCpSoftwareClusterCommunicationResourceProps
    # helpers exactly once (ARObject level). Aggregator dispatch
    # (CpSoftwareClusterCommunicationResource.communicationResourceProps) is pending —
    # CpSoftwareClusterCommunicationResource is an unsynced later-wave class.

    def __init__(self):
        super().__init__()

        # This attribute defines requirements on the data consistency mechanism in the cross cluster communication. If the attribute is not set, the default value consistencyMechanismRequired applies.
        self.dataConsistencyPolicy: Optional[DataConsistencyPolicyEnum] = None

        # Send indication behavior for last-is-the best data communication.
        self.sendIndication: Optional[SendIndicationEnum] = None

    def getDataConsistencyPolicy(self) -> Optional[DataConsistencyPolicyEnum]:
        """
        This attribute defines requirements on the data consistency mechanism in the cross cluster communication. If the attribute is not set, the default value consistencyMechanismRequired applies.
        """
        return self.dataConsistencyPolicy

    def setDataConsistencyPolicy(self, value: Optional[DataConsistencyPolicyEnum]) -> DataComProps:
        """
        This attribute defines requirements on the data consistency mechanism in the cross cluster communication. If the attribute is not set, the default value consistencyMechanismRequired applies.

        A None value is a no-op and does not overwrite an existing dataConsistencyPolicy.
        """
        if value is not None:
            self.dataConsistencyPolicy = value
        return self

    def getSendIndication(self) -> Optional[SendIndicationEnum]:
        """
        Send indication behavior for last-is-the best data communication.
        """
        return self.sendIndication

    def setSendIndication(self, value: Optional[SendIndicationEnum]) -> DataComProps:
        """
        Send indication behavior for last-is-the best data communication.

        A None value is a no-op and does not overwrite an existing sendIndication.
        """
        if value is not None:
            self.sendIndication = value
        return self


class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """
    Enables the definition of Ethernet Global Time specific properties.

    [constr_9311] Existence of EthGlobalTimeDomainProps.messageCompliance: For each EthGlobalTimeDomainProps, the attribute messageCompliance shall exist at the time when the System Description is complete.
    """

    # EthGlobalTimeDomainProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.14, p.867
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCrcFlags                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcFlags                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDestinationPhysicalAddress [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationPhysicalAddress [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addFupDataIDList              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFupDataIDLists             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addManagedCouplingPort        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getManagedCouplingPorts       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMessageCompliance          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageCompliance          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanPriority               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanPriority               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)
    # The fupDataIDList attribute is an ordered 0..16 wrapper list: the XSD ETH-GLOBAL-TIME-DOMAIN-PROPS
    # group (AUTOSAR_00052.xsd l.55564) wraps <FUP-DATA-ID-LIST> items in a <FUP-DATA-ID-LISTS> wrapper
    # emitted only when non-empty; managedCouplingPort is a 0..* aggregation wrapped in
    # <MANAGED-COUPLING-PORTS>. crcFlags rides in the <CRC-FLAGS> element named by the group (not the
    # ETH-T-SYN-CRC-FLAGS type tag). Aggregator dispatch (GlobalTimeDomain.globalTimeDomainProperty)
    # is pending — GlobalTimeDomain is a later-wave class; the reader/writer call the base
    # readAbstractGlobalTimeDomainProps / writeAbstractGlobalTimeDomainProps helpers (VARIATION-POINT
    # precedes the own elements).

    def __init__(self):
        super().__init__()

        # Defines the fields of the message which shall be taken into account for CRC calculation and verification.
        self.crcFlags: Optional[EthTSynCrcFlags] = None

        # Defines the MAC multicast address the Ethernet time sync messages are communicated on.
        self.destinationPhysicalAddress: Optional[MacAddressString] = None

        # The DataIDList for FUP messages to calculate CRC.
        self.fupDataIDLists: List[PositiveInteger] = []

        # Collection of CouplingPorts which are managed in the scope of this Ethernet GlobalTimeDomain.
        self.managedCouplingPorts: List[EthGlobalTimeManagedCouplingPort] = []

        # Defines the compliance of the Ethernet time sync messages to specific standards.
        self.messageCompliance: Optional[EthGlobalTimeMessageFormatEnum] = None

        # Defines which VLAN priority shall be assigned to a time sync message in case the message is sent using a VLAN tag.
        self.vlanPriority: Optional[PositiveInteger] = None

    def getCrcFlags(self) -> Optional[EthTSynCrcFlags]:
        """
        Defines the fields of the message which shall be taken into account for CRC calculation and verification.
        """
        return self.crcFlags

    def setCrcFlags(self, value: Optional[EthTSynCrcFlags]) -> EthGlobalTimeDomainProps:
        """
        Defines the fields of the message which shall be taken into account for CRC calculation and verification.

        A None value is a no-op and does not overwrite an existing crcFlags.
        """
        if value is not None:
            self.crcFlags = value
        return self

    def getDestinationPhysicalAddress(self) -> Optional[MacAddressString]:
        """
        Defines the MAC multicast address the Ethernet time sync messages are communicated on.
        """
        return self.destinationPhysicalAddress

    def setDestinationPhysicalAddress(self, value: Optional[MacAddressString]) -> EthGlobalTimeDomainProps:
        """
        Defines the MAC multicast address the Ethernet time sync messages are communicated on.

        A None value is a no-op and does not overwrite an existing destinationPhysicalAddress.
        """
        if value is not None:
            self.destinationPhysicalAddress = value
        return self

    def addFupDataIDList(self, value: Optional[PositiveInteger]) -> EthGlobalTimeDomainProps:
        """
        The DataIDList for FUP messages to calculate CRC.

        A None value is a no-op and does not append to fupDataIDLists.
        """
        if value is not None:
            self.fupDataIDLists.append(value)
        return self

    def getFupDataIDLists(self) -> List[PositiveInteger]:
        """
        The DataIDList for FUP messages to calculate CRC.
        """
        return self.fupDataIDLists

    def addManagedCouplingPort(self, value: Optional[EthGlobalTimeManagedCouplingPort]) -> EthGlobalTimeDomainProps:
        """
        Collection of CouplingPorts which are managed in the scope of this Ethernet GlobalTimeDomain.

        A None value is a no-op and does not append to managedCouplingPorts.
        """
        if value is not None:
            self.managedCouplingPorts.append(value)
        return self

    def getManagedCouplingPorts(self) -> List[EthGlobalTimeManagedCouplingPort]:
        """
        Collection of CouplingPorts which are managed in the scope of this Ethernet GlobalTimeDomain.
        """
        return self.managedCouplingPorts

    def getMessageCompliance(self) -> Optional[EthGlobalTimeMessageFormatEnum]:
        """
        Defines the compliance of the Ethernet time sync messages to specific standards.
        """
        return self.messageCompliance

    def setMessageCompliance(self, value: Optional[EthGlobalTimeMessageFormatEnum]) -> EthGlobalTimeDomainProps:
        """
        Defines the compliance of the Ethernet time sync messages to specific standards.

        A None value is a no-op and does not overwrite an existing messageCompliance.
        """
        if value is not None:
            self.messageCompliance = value
        return self

    def getVlanPriority(self) -> Optional[PositiveInteger]:
        """
        Defines which VLAN priority shall be assigned to a time sync message in case the message is sent using a VLAN tag.
        """
        return self.vlanPriority

    def setVlanPriority(self, value: Optional[PositiveInteger]) -> EthGlobalTimeDomainProps:
        """
        Defines which VLAN priority shall be assigned to a time sync message in case the message is sent using a VLAN tag.

        A None value is a no-op and does not overwrite an existing vlanPriority.
        """
        if value is not None:
            self.vlanPriority = value
        return self


class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """
    Enables the definition of Flexray GlobalTime specific properties.
    """

    # FrGlobalTimeDomainProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.22, p.878
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addOfsDataIDList    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOfsDataIDLists   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSyncDataIDList   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSyncDataIDLists  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    #
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)
    # The two DataIDList attributes are ordered 0..16 wrapper lists: the XSD FR-GLOBAL-TIME-DOMAIN-PROPS
    # group (AUTOSAR_00052.xsd l.62914) wraps <OFS/SYNC-DATA-ID-LIST> items in a <...-DATA-ID-LISTS>
    # wrapper emitted only when non-empty. Aggregator dispatch (GlobalTimeDomain.globalTimeDomainProperty)
    # is pending — GlobalTimeDomain is a later-wave class; the reader/writer call the base
    # readAbstractGlobalTimeDomainProps / writeAbstractGlobalTimeDomainProps helpers (VARIATION-POINT
    # precedes the wrapper elements).

    def __init__(self):
        super().__init__()

        # The DataIDList for OFS messages to calculate CRC.
        self.ofsDataIDLists: List[PositiveInteger] = []

        # The DataIDList for SYNC messages to calculate CRC.
        self.syncDataIDLists: List[PositiveInteger] = []

    def addOfsDataIDList(self, value: Optional[PositiveInteger]) -> FrGlobalTimeDomainProps:
        """
        The DataIDList for OFS messages to calculate CRC.

        A None value is a no-op and does not append to ofsDataIDLists.
        """
        if value is not None:
            self.ofsDataIDLists.append(value)
        return self

    def getOfsDataIDLists(self) -> List[PositiveInteger]:
        """
        The DataIDList for OFS messages to calculate CRC.
        """
        return self.ofsDataIDLists

    def addSyncDataIDList(self, value: Optional[PositiveInteger]) -> FrGlobalTimeDomainProps:
        """
        The DataIDList for SYNC messages to calculate CRC.

        A None value is a no-op and does not append to syncDataIDLists.
        """
        if value is not None:
            self.syncDataIDLists.append(value)
        return self

    def getSyncDataIDLists(self) -> List[PositiveInteger]:
        """
        The DataIDList for SYNC messages to calculate CRC.
        """
        return self.syncDataIDLists


# Cycle-breaker (Rule 0005): PrimitiveTypes imports ARObject from this module, so the
# PositiveInteger name needed by DiagnosticAbstractParameter's annotations must be bound
# at the bottom, after every class above is defined. Placed here so get_type_hints can
# resolve the bitOffset/parameterSize annotations at runtime on Python 3.8.
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E402
    Address,
    Boolean,
    ByteOrderEnum,
    DataConsistencyPolicyEnum,
    DdsDestinationOrderKindEnum,
    DdsDurabilityKindEnum,
    DdsDurabilityServiceHistoryKindEnum,
    DdsHistoryKindEnum,
    DdsLivenessKindEnum,
    DdsOwnershipKindEnum,
    DdsReliabilityKindEnum,
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
    EthGlobalTimeMessageFormatEnum,
    Float,
    GlobalTimePortRoleEnum,
    Identifier,
    MacAddressString,
    NameToken,
    Numerical,
    PositiveInteger,
    RefType,
    SendIndicationEnum,
    String,
    SymbolString,
    TimeValue,
)


# BusMirrorChannelMappingCan is defined in SystemTemplate::Fibex::FibexCore (its spec
# Base chain reaches FibexElement there); an eager import from this module would close
# an import-time cycle (FibexCore imports this module for ARObject/PackageableElement),
# so the name is re-exported lazily via PEP 562; `from ArObject import X` and wildcard
# imports keep working because __getattr__ only fires for names missing from module globals.
from importlib import import_module as _import_module  # noqa: E402

_LAZY_IMPORTS = {
    "BusMirrorChannelMappingCan": "armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore",
    "BusMirrorChannelMappingIp": "armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore",
}


def __getattr__(name):
    module_path = _LAZY_IMPORTS.get(name)
    if module_path is None:
        raise AttributeError("module %r has no attribute %r" % (__name__, name))
    value = getattr(_import_module(module_path), name)
    globals()[name] = value
    return value
