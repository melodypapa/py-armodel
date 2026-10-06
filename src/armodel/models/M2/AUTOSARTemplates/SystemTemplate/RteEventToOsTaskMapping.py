# This module contains AUTOSAR System Template classes for RTE event to OS task mapping
# It defines mappings between application and ECU task proxies for real-time execution

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInCompositionInstanceRef


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """
    This meta-class is used to map an OsTaskProxy that was created in the context of a SwComponent to an OsTaskProxy that was created in the context of an Ecu.
    """

    # AppOsTaskProxyToEcuTaskProxyMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.17, p.209
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAppTaskProxyRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAppTaskProxyRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuTaskProxyRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuTaskProxyRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOffset           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOffset           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to an OsTaskProxy that is created in the context of a SwComponent.
        self.appTaskProxyRef: Optional[RefType] = None

        # Reference to an OsTaskProxy that is created in the context of an EcuInstance.
        self.ecuTaskProxyRef: Optional[RefType] = None

        # This attribute is used to describe the position of the app TaskProxy in an ecuTaskProxy as a relative value, i.e. the values show only the relative position of the appTask Proxy in the ecuTaskProxy.
        self.offset: Optional[Integer] = None

    def getAppTaskProxyRef(self) -> Optional[RefType]:
        """
        Reference to an OsTaskProxy that is created in the context of a SwComponent.
        """
        return self.appTaskProxyRef

    def setAppTaskProxyRef(self, value: Optional[RefType]) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """
        Reference to an OsTaskProxy that is created in the context of a SwComponent.

        A None value is a no-op and does not overwrite an existing appTaskProxyRef.
        """
        if value is not None:
            self.appTaskProxyRef = value
        return self

    def getEcuTaskProxyRef(self) -> Optional[RefType]:
        """
        Reference to an OsTaskProxy that is created in the context of an EcuInstance.
        """
        return self.ecuTaskProxyRef

    def setEcuTaskProxyRef(self, value: Optional[RefType]) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """
        Reference to an OsTaskProxy that is created in the context of an EcuInstance.

        A None value is a no-op and does not overwrite an existing ecuTaskProxyRef.
        """
        if value is not None:
            self.ecuTaskProxyRef = value
        return self

    def getOffset(self) -> Optional[Integer]:
        """
        This attribute is used to describe the position of the app TaskProxy in an ecuTaskProxy as a relative value, i.e. the values show only the relative position of the appTask Proxy in the ecuTaskProxy.
        """
        return self.offset

    def setOffset(self, value: Optional[Integer]) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """
        This attribute is used to describe the position of the app TaskProxy in an ecuTaskProxy as a relative value, i.e. the values show only the relative position of the appTask Proxy in the ecuTaskProxy.

        A None value is a no-op and does not overwrite an existing offset.
        """
        if value is not None:
            self.offset = value
        return self


class RteEventInCompositionToOsTaskProxyMapping(Identifiable):
    """
    This meta-class is used to map an RteEvent to an OsTaskProxy in the context of a SwComposition. Several RteEventInCompositionToOsTaskProxyMappings can be used to define a pairing constraint that describes which RteEvents shall be mapped together into an OsTask. Optionally the relative position of the RteEvents in the OsTask can be defined in the mapping.
    """

    # RteEventInCompositionToOsTaskProxyMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.18, p.212
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOffset         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOffset         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOsTaskProxyRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOsTaskProxyRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRteEventIRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRteEventIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This attribute is used to describe the position of the Rte Event in the OsTask as a relative value, i.e. the values show only the relative position of the RteEvent in the Os Task.
        self.offset: Optional[PositiveInteger] = None

        # Reference to OsTaskProxy to which the RteEvent is mapped.
        self.osTaskProxyRef: Optional[RefType] = None

        # Reference to RteEvent that is mapped to the OsTask Proxy. InstanceRef implemented by: RteEventInComposition InstanceRef
        self.rteEventIRef: Optional[RteEventInCompositionInstanceRef] = None

    def getOffset(self) -> Optional[PositiveInteger]:
        """
        This attribute is used to describe the position of the Rte Event in the OsTask as a relative value, i.e. the values show only the relative position of the RteEvent in the Os Task.
        """
        return self.offset

    def setOffset(self, value: Optional[PositiveInteger]) -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        This attribute is used to describe the position of the Rte Event in the OsTask as a relative value, i.e. the values show only the relative position of the RteEvent in the Os Task.

        A None value is a no-op and does not overwrite an existing offset.
        """
        if value is not None:
            self.offset = value
        return self

    def getOsTaskProxyRef(self) -> Optional[RefType]:
        """
        Reference to OsTaskProxy to which the RteEvent is mapped.
        """
        return self.osTaskProxyRef

    def setOsTaskProxyRef(self, value: Optional[RefType]) -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        Reference to OsTaskProxy to which the RteEvent is mapped.

        A None value is a no-op and does not overwrite an existing osTaskProxyRef.
        """
        if value is not None:
            self.osTaskProxyRef = value
        return self

    def getRteEventIRef(self) -> Optional[RteEventInCompositionInstanceRef]:
        """
        Reference to RteEvent that is mapped to the OsTask Proxy. InstanceRef implemented by: RteEventInComposition InstanceRef
        """
        return self.rteEventIRef

    def setRteEventIRef(self, value: Optional[RteEventInCompositionInstanceRef]) -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        Reference to RteEvent that is mapped to the OsTask Proxy. InstanceRef implemented by: RteEventInComposition InstanceRef

        A None value is a no-op and does not overwrite an existing rteEventIRef.
        """
        if value is not None:
            self.rteEventIRef = value
        return self


class RteEventInCompositionSeparation(Identifiable):
    """
    This meta-class is used to define a separation constraint in the context of a SwComposition. The referenced RteEvents are not allowed to be mapped into the same OsTask.
    """

    # RteEventInCompositionSeparation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.19, p.212
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRteEventIRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRteEventIRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to RteEvents that are not allowed to be mapped into the same OsTask. InstanceRef implemented by: RteEventInComposition InstanceRef
        self.rteEventIRefs: List[RteEventInCompositionInstanceRef] = []

    def addRteEventIRef(self, value: Optional[RteEventInCompositionInstanceRef]) -> "RteEventInCompositionSeparation":
        """
        Reference to RteEvents that are not allowed to be mapped into the same OsTask. InstanceRef implemented by: RteEventInComposition InstanceRef

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.rteEventIRefs.append(value)
        return self

    def getRteEventIRefs(self) -> List[RteEventInCompositionInstanceRef]:
        """
        Reference to RteEvents that are not allowed to be mapped into the same OsTask. InstanceRef implemented by: RteEventInComposition InstanceRef
        """
        return self.rteEventIRefs


class OsTaskPreemptabilityEnum(AREnum):
    """
    Enumeration that defines the possible preemptability values for OsTask.
    """

    # OsTaskPreemptabilityEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.16, p.209
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on OsTaskProxy.preemptability (Steps 5/6 N/A: standalone AREnum)

    # Task is preemptable. Tags: atp.EnumerationLiteralIndex=1
    FULL = "FULL"

    # Task is not preemptable. Tags: atp.EnumerationLiteralIndex=0
    NONE = "NONE"

    def __init__(self):
        super().__init__(
            [
                OsTaskPreemptabilityEnum.FULL,
                OsTaskPreemptabilityEnum.NONE,
            ]
        )


class OsTaskProxy(ARElement):
    """This meta-class represents a proxy for an OsTask in the System Description. Tags: atp.recommendedPackage=OsTaskProxies"""

    # OsTaskProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.15, p.208 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPeriod          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPeriod          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPreemptability  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPreemptability  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPriority        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # Aggregated by ARPackage.element (XSD L5379) → ARPackage.createOsTaskProxy factory.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute specifies the period in seconds of this task in case of a cyclically activated task. Please note that this attribute is informative and not directly relevant for the AUTOSAR OS. But the attribute value can be mapped into the OS configuration to support configuration work flows using a fixed set of OsTasks.
        self.period: Optional[TimeValue] = None

        # This attribute defines the preemptability of the task.
        self.preemptability: Optional[OsTaskPreemptabilityEnum] = None

        # This attribute defines the priority of a task as a relative value, i.e. the values show only the relative ordering of the tasks.
        self.priority: Optional[PositiveInteger] = None

    def getPeriod(self) -> Optional[TimeValue]:
        """This attribute specifies the period in seconds of this task in case of a cyclically activated task. Please note that this attribute is informative and not directly relevant for the AUTOSAR OS. But the attribute value can be mapped into the OS configuration to support configuration work flows using a fixed set of OsTasks."""
        return self.period

    def setPeriod(self, value: Optional[TimeValue]) -> "OsTaskProxy":
        """This attribute specifies the period in seconds of this task in case of a cyclically activated task. Please note that this attribute is informative and not directly relevant for the AUTOSAR OS. But the attribute value can be mapped into the OS configuration to support configuration work flows using a fixed set of OsTasks.

        A None value is a no-op and does not overwrite an existing period.
        """
        if value is not None:
            self.period = value
        return self

    def getPreemptability(self) -> Optional[OsTaskPreemptabilityEnum]:
        """This attribute defines the preemptability of the task."""
        return self.preemptability

    def setPreemptability(self, value: Optional[OsTaskPreemptabilityEnum]) -> "OsTaskProxy":
        """This attribute defines the preemptability of the task.

        A None value is a no-op and does not overwrite an existing preemptability.
        """
        if value is not None:
            self.preemptability = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """This attribute defines the priority of a task as a relative value, i.e. the values show only the relative ordering of the tasks."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> "OsTaskProxy":
        """This attribute defines the priority of a task as a relative value, i.e. the values show only the relative ordering of the tasks.

        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self
