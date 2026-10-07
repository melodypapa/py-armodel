from __future__ import annotations

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import PortGroupInSystemInstanceRef


class PncMappingIdent(Referrable):
    """
    This meta-class is created to add the ability to become the target of a reference to the non-Referrable PncMapping.
    """

    # PncMappingIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.95, p.NN/A (R23-11 markdown appendix; page not extractable from the R23-11 PDF)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class PncMapping(Describable, VariationPointCapable):
    """
    Describes a mapping between one or several Virtual Function Clusters onto Partial Network Clusters. A Virtual Function Cluster is realized by a PortGroup. A Partial Network Cluster is realized by one or more IPduGroups.
    """

    # PncMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.45, p.266
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDynamicPncMappingPduGroupRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDynamicPncMappingPduGroupRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createIdent                                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIdent                                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPhysicalChannelRef                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPhysicalChannelRefs                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPncConsumedProvidedServiceInstanceGroupRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncConsumedProvidedServiceInstanceGroupRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPncGroupRef                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncGroupRefs                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPncIdentifier                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncIdentifier                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPncPdurGroupRef                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncPdurGroupRefs                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPncWakeupEnable                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncWakeupEnable                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addRelevantForDynamicPncMappingRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRelevantForDynamicPncMappingRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getShortLabel                                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortLabel                                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addVfcIRef                                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVfcIRefs                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addWakeupFrameRef                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupFrameRefs                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to an ISignalIPduGroup that allows mapping of this PNC without statically mapping this PNC directly to a channel. This is needed to describe dynamic PNCs that can be learned only at run-time and which have also a relation to an ISignalIPduGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=dynamicPncMappingPduGroup atp.Status=draft
        self.dynamicPncMappingPduGroupRefs: List[RefType] = []

        # This adds the ability to become referrable to PncMapping.
        self.ident: Optional[PncMappingIdent] = None

        # This reference maps the partial network to a communication channel. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalChannel
        self.physicalChannelRefs: List[RefType] = []

        # ConsumedProvidedServiceInstanceGroup used in a Partial Network Cluster. This reference is optional, since this could be used for starting and stopping Consumed ProvidedServiceInstanceGroup according the requested partial network, but is not necessarily needed. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pncConsumedProvidedServiceInstanceGroup.consumedProvidedServiceInstanceGroup, pnc ConsumedProvidedServiceInstanceGroup.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.pncConsumedProvidedServiceInstanceGroupRefs: List[RefType] = []

        # IPduGroup participating in a Partial Network Cluster. This reference is optional in case an ecu extract has only indirect pnc access, i.e. ecu is not directly connected to a network which supports partial network. Stereotypes: atpSplitable Tags: atp.Splitkey=pncGroup
        self.pncGroupRefs: List[RefType] = []

        # Identifer of the Partial Network Cluster. This number represents the absolute bit position of this Partial Network Cluster in the NM Pdu.
        self.pncIdentifier: Optional[PositiveInteger] = None

        # This reference maps the Partial Network Cluster to a set of PdurIpduGroups. Stereotypes: atpSplitable Tags: atp.Splitkey=pncPdurGroup
        self.pncPdurGroupRefs: List[RefType] = []

        # If this parameter is available and set to true then this PNC will be woken up as soon as a channel wakeup occurs on a channel where this PNC is assigned to. This is ensured by adding this PNC to the corresponding channel wakeup sources during upstream mapping.
        self.pncWakeupEnable: Optional[Boolean] = None

        # Reference to a PNC Gateway ECU for PNCs which do not have a static channel mapping. This is needed to describe dynamic PNCs that can be learned only at run-time and which have no relation to an ISignalIPdu Group. Stereotypes: atpSplitable Tags: atp.Splitkey=relevantForDynamicPncMapping atp.Status=draft
        self.relevantForDynamicPncMappingRefs: List[RefType] = []

        # This attribute specifies an identifying shortName for the PncMapping. It shall be unique in the System scope.
        self.shortLabel: Optional[Identifier] = None

        # Virtual Function Cluster to be mapped onto a Partial Network Cluster. This reference is optional in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy systems. InstanceRef implemented by: PortGroupInSystemInstanceRef
        self.vfcIRefs: List[PortGroupInSystemInstanceRef] = []

        # Reference to collection of FrameTriggerings that are used for the wakeup of this PNC (Application Frames or Nm Frames can be used). This reference is only valid if this EcuExtract represents an ECU which has direct PNC access, i.e. ECU is directly connected to a network which supports partial network. Stereotypes: atpSplitable Tags: atp.Splitkey=wakeupFrame
        self.wakeupFrameRefs: List[RefType] = []

    def addDynamicPncMappingPduGroupRef(self, value: Optional[RefType]) -> PncMapping:
        """
        Reference to an ISignalIPduGroup that allows mapping of this PNC without statically mapping this PNC directly to a channel. This is needed to describe dynamic PNCs that can be learned only at run-time and which have also a relation to an ISignalIPduGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=dynamicPncMappingPduGroup atp.Status=draft

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.dynamicPncMappingPduGroupRefs.append(value)
        return self

    def getDynamicPncMappingPduGroupRefs(self) -> List[RefType]:
        """
        Reference to an ISignalIPduGroup that allows mapping of this PNC without statically mapping this PNC directly to a channel. This is needed to describe dynamic PNCs that can be learned only at run-time and which have also a relation to an ISignalIPduGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=dynamicPncMappingPduGroup atp.Status=draft
        """
        return self.dynamicPncMappingPduGroupRefs

    def createIdent(self, short_name: str) -> PncMappingIdent:
        """
        This adds the ability to become referrable to PncMapping.
        """
        if self.ident is None:
            self.ident = PncMappingIdent(self, short_name)
        return self.ident

    def getIdent(self) -> Optional[PncMappingIdent]:
        """
        This adds the ability to become referrable to PncMapping.
        """
        return self.ident

    def addPhysicalChannelRef(self, value: Optional[RefType]) -> PncMapping:
        """
        This reference maps the partial network to a communication channel. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalChannel

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.physicalChannelRefs.append(value)
        return self

    def getPhysicalChannelRefs(self) -> List[RefType]:
        """
        This reference maps the partial network to a communication channel. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalChannel
        """
        return self.physicalChannelRefs

    def addPncConsumedProvidedServiceInstanceGroupRef(self, value: Optional[RefType]) -> PncMapping:
        """
        ConsumedProvidedServiceInstanceGroup used in a Partial Network Cluster. This reference is optional, since this could be used for starting and stopping Consumed ProvidedServiceInstanceGroup according the requested partial network, but is not necessarily needed. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pncConsumedProvidedServiceInstanceGroup.consumedProvidedServiceInstanceGroup, pnc ConsumedProvidedServiceInstanceGroup.variation Point.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.pncConsumedProvidedServiceInstanceGroupRefs.append(value)
        return self

    def getPncConsumedProvidedServiceInstanceGroupRefs(self) -> List[RefType]:
        """
        ConsumedProvidedServiceInstanceGroup used in a Partial Network Cluster. This reference is optional, since this could be used for starting and stopping Consumed ProvidedServiceInstanceGroup according the requested partial network, but is not necessarily needed. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pncConsumedProvidedServiceInstanceGroup.consumedProvidedServiceInstanceGroup, pnc ConsumedProvidedServiceInstanceGroup.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.pncConsumedProvidedServiceInstanceGroupRefs

    def addPncGroupRef(self, value: Optional[RefType]) -> PncMapping:
        """
        IPduGroup participating in a Partial Network Cluster. This reference is optional in case an ecu extract has only indirect pnc access, i.e. ecu is not directly connected to a network which supports partial network. Stereotypes: atpSplitable Tags: atp.Splitkey=pncGroup

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.pncGroupRefs.append(value)
        return self

    def getPncGroupRefs(self) -> List[RefType]:
        """
        IPduGroup participating in a Partial Network Cluster. This reference is optional in case an ecu extract has only indirect pnc access, i.e. ecu is not directly connected to a network which supports partial network. Stereotypes: atpSplitable Tags: atp.Splitkey=pncGroup
        """
        return self.pncGroupRefs

    def getPncIdentifier(self) -> Optional[PositiveInteger]:
        """
        Identifer of the Partial Network Cluster. This number represents the absolute bit position of this Partial Network Cluster in the NM Pdu.
        """
        return self.pncIdentifier

    def setPncIdentifier(self, value: Optional[PositiveInteger]) -> PncMapping:
        """
        Identifer of the Partial Network Cluster. This number represents the absolute bit position of this Partial Network Cluster in the NM Pdu.

        A None value is a no-op and does not overwrite an existing pncIdentifier.
        """
        if value is not None:
            self.pncIdentifier = value
        return self

    def addPncPdurGroupRef(self, value: Optional[RefType]) -> PncMapping:
        """
        This reference maps the Partial Network Cluster to a set of PdurIpduGroups. Stereotypes: atpSplitable Tags: atp.Splitkey=pncPdurGroup

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.pncPdurGroupRefs.append(value)
        return self

    def getPncPdurGroupRefs(self) -> List[RefType]:
        """
        This reference maps the Partial Network Cluster to a set of PdurIpduGroups. Stereotypes: atpSplitable Tags: atp.Splitkey=pncPdurGroup
        """
        return self.pncPdurGroupRefs

    def getPncWakeupEnable(self) -> Optional[Boolean]:
        """
        If this parameter is available and set to true then this PNC will be woken up as soon as a channel wakeup occurs on a channel where this PNC is assigned to. This is ensured by adding this PNC to the corresponding channel wakeup sources during upstream mapping.
        """
        return self.pncWakeupEnable

    def setPncWakeupEnable(self, value: Optional[Boolean]) -> PncMapping:
        """
        If this parameter is available and set to true then this PNC will be woken up as soon as a channel wakeup occurs on a channel where this PNC is assigned to. This is ensured by adding this PNC to the corresponding channel wakeup sources during upstream mapping.

        A None value is a no-op and does not overwrite an existing pncWakeupEnable.
        """
        if value is not None:
            self.pncWakeupEnable = value
        return self

    def addRelevantForDynamicPncMappingRef(self, value: Optional[RefType]) -> PncMapping:
        """
        Reference to a PNC Gateway ECU for PNCs which do not have a static channel mapping. This is needed to describe dynamic PNCs that can be learned only at run-time and which have no relation to an ISignalIPdu Group. Stereotypes: atpSplitable Tags: atp.Splitkey=relevantForDynamicPncMapping atp.Status=draft

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.relevantForDynamicPncMappingRefs.append(value)
        return self

    def getRelevantForDynamicPncMappingRefs(self) -> List[RefType]:
        """
        Reference to a PNC Gateway ECU for PNCs which do not have a static channel mapping. This is needed to describe dynamic PNCs that can be learned only at run-time and which have no relation to an ISignalIPdu Group. Stereotypes: atpSplitable Tags: atp.Splitkey=relevantForDynamicPncMapping atp.Status=draft
        """
        return self.relevantForDynamicPncMappingRefs

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This attribute specifies an identifying shortName for the PncMapping. It shall be unique in the System scope.
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> PncMapping:
        """
        This attribute specifies an identifying shortName for the PncMapping. It shall be unique in the System scope.

        A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self

    def addVfcIRef(self, value: Optional[PortGroupInSystemInstanceRef]) -> PncMapping:
        """
        Virtual Function Cluster to be mapped onto a Partial Network Cluster. This reference is optional in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy systems. InstanceRef implemented by: PortGroupInSystemInstanceRef

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.vfcIRefs.append(value)
        return self

    def getVfcIRefs(self) -> List[PortGroupInSystemInstanceRef]:
        """
        Virtual Function Cluster to be mapped onto a Partial Network Cluster. This reference is optional in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy systems. InstanceRef implemented by: PortGroupInSystemInstanceRef
        """
        return self.vfcIRefs

    def addWakeupFrameRef(self, value: Optional[RefType]) -> PncMapping:
        """
        Reference to collection of FrameTriggerings that are used for the wakeup of this PNC (Application Frames or Nm Frames can be used). This reference is only valid if this EcuExtract represents an ECU which has direct PNC access, i.e. ECU is directly connected to a network which supports partial network. Stereotypes: atpSplitable Tags: atp.Splitkey=wakeupFrame

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.wakeupFrameRefs.append(value)
        return self

    def getWakeupFrameRefs(self) -> List[RefType]:
        """
        Reference to collection of FrameTriggerings that are used for the wakeup of this PNC (Application Frames or Nm Frames can be used). This reference is only valid if this EcuExtract represents an ECU which has direct PNC access, i.e. ECU is directly connected to a network which supports partial network. Stereotypes: atpSplitable Tags: atp.Splitkey=wakeupFrame
        """
        return self.wakeupFrameRefs
