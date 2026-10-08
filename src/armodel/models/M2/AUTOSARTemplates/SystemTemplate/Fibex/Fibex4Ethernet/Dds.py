from __future__ import annotations

from typing import List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpDomain, DdsCpQosProfile
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class DdsCpConfig(ARElement):
    """
    Collection of DDS definitions. Tags: atp.Status=candidate atp.recommendedPackage=DdsCpConfigs
    """

    # DdsCpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.175, p.526
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createDdsDomain        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsDomains          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDdsQosProfile    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsQosProfiles      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of DDS Domain definitions. Tags: atp.Status=candidate
        self.ddsDomains: List[DdsCpDomain] = []

        # Collection of DDS QOS Profiles. Tags: atp.Status=candidate
        self.ddsQosProfiles: List[DdsCpQosProfile] = []

    def createDdsDomain(self, short_name: str) -> DdsCpDomain:
        """
        Collection of DDS Domain definitions. Tags: atp.Status=candidate
        """
        if not self.IsReferrableElementExists(short_name, DdsCpDomain):
            domain = DdsCpDomain(self, short_name)
            self.addReferrableElement(domain)
            self.ddsDomains.append(domain)
        return cast(DdsCpDomain, self.getReferrableElement(short_name, DdsCpDomain))

    def getDdsDomains(self) -> List[DdsCpDomain]:
        """
        Collection of DDS Domain definitions. Tags: atp.Status=candidate
        """
        return self.ddsDomains

    def createDdsQosProfile(self, short_name: str) -> DdsCpQosProfile:
        """
        Collection of DDS QOS Profiles. Tags: atp.Status=candidate
        """
        if not self.IsReferrableElementExists(short_name, DdsCpQosProfile):
            profile = DdsCpQosProfile(self, short_name)
            self.addReferrableElement(profile)
            self.ddsQosProfiles.append(profile)
        return cast(DdsCpQosProfile, self.getReferrableElement(short_name, DdsCpQosProfile))

    def getDdsQosProfiles(self) -> List[DdsCpQosProfile]:
        """
        Collection of DDS QOS Profiles. Tags: atp.Status=candidate
        """
        return self.ddsQosProfiles


class DdsCpISignalToDdsTopicMapping(ARObject):
    """
    Mapping of an ISignal to a DdsTopic. Tags: atp.Status=candidate
    """

    # DdsCpISignalToDdsTopicMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.53, p.293 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDdsTopicRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsTopicRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getISignalRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setISignalRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the DdsTopic. Tags: atp.Status=candidate
        self.ddsTopicRef: Optional[RefType] = None

        # Reference to the ISignal. Tags: atp.Status=candidate
        self.iSignalRef: Optional[RefType] = None

    def getDdsTopicRef(self) -> Optional[RefType]:
        """
        Reference to the DdsTopic. Tags: atp.Status=candidate
        """
        return self.ddsTopicRef

    def setDdsTopicRef(self, value: Optional[RefType]) -> DdsCpISignalToDdsTopicMapping:
        """
        Reference to the DdsTopic. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing ddsTopicRef.
        """
        if value is not None:
            self.ddsTopicRef = value
        return self

    def getISignalRef(self) -> Optional[RefType]:
        """
        Reference to the ISignal. Tags: atp.Status=candidate
        """
        return self.iSignalRef

    def setISignalRef(self, value: Optional[RefType]) -> DdsCpISignalToDdsTopicMapping:
        """
        Reference to the ISignal. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing iSignalRef.
        """
        if value is not None:
            self.iSignalRef = value
        return self
