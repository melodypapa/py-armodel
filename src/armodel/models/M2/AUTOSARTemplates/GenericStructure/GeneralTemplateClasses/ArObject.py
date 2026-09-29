"""
Abstract base class of all AUTOSAR objects.
"""

from abc import ABC
from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
        DateTime,
        String,
    )


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

        self.parent: Optional["ARObject"] = None

        # Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum.
        self.checksum: Optional["String"] = None

        # Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        self.timestamp: Optional["DateTime"] = None

    def getChecksum(self) -> Optional["String"]:
        """
        Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum.
        """
        return self.checksum

    def setChecksum(self, value: Optional["String"]) -> "ARObject":
        """
        Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum. A None value is a no-op and does not overwrite an existing checksum.
        """
        if value is not None:
            self.checksum = value
        return self

    def getTimestamp(self) -> Optional["DateTime"]:
        """
        Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        """
        return self.timestamp

    def setTimestamp(self, value: Optional["DateTime"]) -> "ARObject":
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


class AbstractValueRestriction(ARObject, ABC):
    pass


class AbstractVariationRestriction(ARObject, ABC):
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
    pass


class DiagnosticClearResetEmissionRelatedInfo(ARObject):
    pass


class DiagnosticComControlSpecificChannel(ARObject):
    pass


class DiagnosticComControlSubNodeChannel(ARObject):
    pass


class DiagnosticCommonProps(ARObject):
    pass


class DiagnosticConnectedIndicator(ARObject):
    pass


class DiagnosticContributionSet(ARObject):
    pass


class DiagnosticControlDTCSetting(ARObject):
    pass


class DiagnosticControlEnableMaskBit(ARObject):
    pass


class DiagnosticEnableConditionPortMapping(ARObject):
    pass


class DiagnosticEnvModeCondition(ARObject):
    pass


class DiagnosticEventWindow(ARObject):
    pass


class DiagnosticFimFunctionMapping(ARObject):
    pass


class DiagnosticFunctionIdentifierInhibit(ARObject):
    pass


class DiagnosticInhibitSourceEventMapping(ARObject):
    pass


class DiagnosticIumprGroupIdentifier(ARObject):
    pass


class DiagnosticMemoryDestination(ARObject, ABC):
    pass


class DiagnosticMemoryDestinationUserDefined(ARObject):
    pass


class DiagnosticParameter(DiagnosticAbstractParameter):
    pass


class DiagnosticParameterElementAccess(ARObject):
    pass


class DiagnosticParameterSupportInfo(ARObject):
    pass


class DiagnosticPeriodicRate(ARObject):
    pass


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


class List(ARObject):
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
    pass


class RptHook(ARObject):
    pass


class RptProfile(ARObject):
    pass


class SdgElementWithGid(ARObject, ABC):
    pass


class SpecificationScope(ARObject):
    pass


class SwAxisCont(ARObject):
    pass


class SwcModeManagerErrorEvent(ARObject):
    pass


class TextualCondition(AbstractCondition):
    pass


class ValueRestrictionWithSeverity(AbstractValueRestriction):
    pass


class VariationRestrictionWithSeverity(AbstractVariationRestriction):
    pass
