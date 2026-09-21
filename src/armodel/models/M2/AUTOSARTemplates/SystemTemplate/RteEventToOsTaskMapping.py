# This module contains AUTOSAR System Template classes for RTE event to OS task mapping
# It defines mappings between application and ECU task proxies for real-time execution

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, RefType, TimeValue


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """
    Represents a mapping between application OS task proxies and ECU task proxies
    in the Runtime Environment (RTE), defining how application-level tasks are
    connected to ECU-level tasks for real-time execution coordination.
    """

    # AppOsTaskProxyToEcuTaskProxyMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAppTaskProxyRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setAppTaskProxyRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuTaskProxyRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuTaskProxyRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getOffset                    [x] impl  [ ] docstring  [ ] test
    # [ ] setOffset                    [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.appTaskProxyRef: RefType = None
        self.ecuTaskProxyRef: RefType = None
        self.offset: Optional[int] = None

    def getAppTaskProxyRef(self):
        return self.appTaskProxyRef

    def setAppTaskProxyRef(self, value):
        if value is not None:
            self.appTaskProxyRef = value
        return self

    def getEcuTaskProxyRef(self):
        return self.ecuTaskProxyRef

    def setEcuTaskProxyRef(self, value):
        if value is not None:
            self.ecuTaskProxyRef = value
        return self

    def getOffset(self) -> Optional[int]:
        return self.offset

    def setOffset(self, value: Optional[int]) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        if value is not None:
            self.offset = value
        return self


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
    FULL = "full"

    # Task is not preemptable. Tags: atp.EnumerationLiteralIndex=0
    NONE = "none"

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
