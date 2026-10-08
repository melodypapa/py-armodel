"""
This module contains the CP software cluster timing mapping classes
(spec package CommonStructure::Timing::TimingCpSoftwareCluster).
"""

from typing import List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable


class TDCpSoftwareClusterMapping(Identifiable, VariationPointCapable):
    """
    This is used to specify a mapping between a software cluster that provides temporal and dynamic resources and the software clusters that need these resources.
    """

    # TDCpSoftwareClusterMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 4.6, p.157
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getProviderRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProviderRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addRequestorRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequestorRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getTimingDescriptionRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimingDescriptionRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is the software cluster that provides the temporal and dynamic resource.
        self.providerRef: Optional[RefType] = None

        # This is the software cluster that requests the temporal and dynamic resource.
        self.requestorRefs: List[RefType] = []

        # The timing description representing the temporal and dynamic resource.
        self.timingDescriptionRef: Optional[RefType] = None

    def getProviderRef(self) -> Optional[RefType]:
        """
        This is the software cluster that provides the temporal and dynamic resource.
        """
        return self.providerRef

    def setProviderRef(self, value: Optional[RefType]) -> "TDCpSoftwareClusterMapping":
        """
        This is the software cluster that provides the temporal and dynamic resource.

        A None value is a no-op and does not overwrite an existing providerRef.
        """
        if value is not None:
            self.providerRef = value
        return self

    def addRequestorRef(self, value: Optional[RefType]) -> "TDCpSoftwareClusterMapping":
        """
        This is the software cluster that requests the temporal and dynamic resource.
        """
        if value is not None:
            self.requestorRefs.append(value)
        return self

    def getRequestorRefs(self) -> List[RefType]:
        """
        This is the software cluster that requests the temporal and dynamic resource.
        """
        return self.requestorRefs

    def getTimingDescriptionRef(self) -> Optional[RefType]:
        """
        The timing description representing the temporal and dynamic resource.
        """
        return self.timingDescriptionRef

    def setTimingDescriptionRef(self, value: Optional[RefType]) -> "TDCpSoftwareClusterMapping":
        """
        The timing description representing the temporal and dynamic resource.

        A None value is a no-op and does not overwrite an existing timingDescriptionRef.
        """
        if value is not None:
            self.timingDescriptionRef = value
        return self


class TDCpSoftwareClusterResourceMapping(Identifiable, VariationPointCapable):
    """
    This is used to assign an unequivocal global resource identification to a temporal and dynamic resource.
    """

    # TDCpSoftwareClusterResourceMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 4.7, p.158
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getResourceRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResourceRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimingDescriptionRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimingDescriptionRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The specific resource identification assigned to the temporal and dynamic resource.
        self.resourceRef: Optional[RefType] = None

        # The timing description representing the temporal and dynamic resource.
        self.timingDescriptionRef: Optional[RefType] = None

    def getResourceRef(self) -> Optional[RefType]:
        """
        The specific resource identification assigned to the temporal and dynamic resource.
        """
        return self.resourceRef

    def setResourceRef(self, value: Optional[RefType]) -> "TDCpSoftwareClusterResourceMapping":
        """
        The specific resource identification assigned to the temporal and dynamic resource.

        A None value is a no-op and does not overwrite an existing resourceRef.
        """
        if value is not None:
            self.resourceRef = value
        return self

    def getTimingDescriptionRef(self) -> Optional[RefType]:
        """
        The timing description representing the temporal and dynamic resource.
        """
        return self.timingDescriptionRef

    def setTimingDescriptionRef(self, value: Optional[RefType]) -> "TDCpSoftwareClusterResourceMapping":
        """
        The timing description representing the temporal and dynamic resource.

        A None value is a no-op and does not overwrite an existing timingDescriptionRef.
        """
        if value is not None:
            self.timingDescriptionRef = value
        return self


class TDCpSoftwareClusterMappingSet(ARElement):
    """
    This is used to gather of classic platform software cluster mappings. Tags: atp.recommendedPackage=TimingExtensions
    """

    # TDCpSoftwareClusterMappingSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 4.5, p.157
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createTdCpSoftwareClusterResourceToTdMapping    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTdCpSoftwareClusterResourceToTdMappings      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createTdCpSoftwareClusterToTdMapping            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTdCpSoftwareClusterToTdMappings              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Maps a CP software cluster resource to a temporal resource. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterResourceToTdMapping.shortName, tdCpSoftwareClusterResourceToTdMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.tdCpSoftwareClusterResourceToTdMappings: List[TDCpSoftwareClusterResourceMapping] = []

        # Maps a temporal resource to a mapping between a providing CP software cluster and requesting CP software clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterToTdMapping.short Name, tdCpSoftwareClusterToTdMapping.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tdCpSoftwareClusterToTdMappings: List[TDCpSoftwareClusterMapping] = []

    def createTdCpSoftwareClusterResourceToTdMapping(self, short_name: str) -> TDCpSoftwareClusterResourceMapping:
        """
        Maps a CP software cluster resource to a temporal resource. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterResourceToTdMapping.shortName, tdCpSoftwareClusterResourceToTdMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, TDCpSoftwareClusterResourceMapping):
            mapping = TDCpSoftwareClusterResourceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.tdCpSoftwareClusterResourceToTdMappings.append(mapping)
        return cast(TDCpSoftwareClusterResourceMapping, self.getReferrableElement(short_name, TDCpSoftwareClusterResourceMapping))

    def getTdCpSoftwareClusterResourceToTdMappings(self) -> List[TDCpSoftwareClusterResourceMapping]:
        """
        Maps a CP software cluster resource to a temporal resource. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterResourceToTdMapping.shortName, tdCpSoftwareClusterResourceToTdMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tdCpSoftwareClusterResourceToTdMappings

    def createTdCpSoftwareClusterToTdMapping(self, short_name: str) -> TDCpSoftwareClusterMapping:
        """
        Maps a temporal resource to a mapping between a providing CP software cluster and requesting CP software clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterToTdMapping.short Name, tdCpSoftwareClusterToTdMapping.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, TDCpSoftwareClusterMapping):
            mapping = TDCpSoftwareClusterMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.tdCpSoftwareClusterToTdMappings.append(mapping)
        return cast(TDCpSoftwareClusterMapping, self.getReferrableElement(short_name, TDCpSoftwareClusterMapping))

    def getTdCpSoftwareClusterToTdMappings(self) -> List[TDCpSoftwareClusterMapping]:
        """
        Maps a temporal resource to a mapping between a providing CP software cluster and requesting CP software clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterToTdMapping.short Name, tdCpSoftwareClusterToTdMapping.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tdCpSoftwareClusterToTdMappings
