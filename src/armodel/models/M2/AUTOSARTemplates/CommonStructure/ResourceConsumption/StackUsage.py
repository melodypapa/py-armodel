"""
This module contains classes for representing stack usage in AUTOSAR resource consumption models.
It includes abstract base classes and concrete implementations for different types of stack usage analysis.
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from typing import Optional


class StackUsage(Identifiable, VariationPointCapable, ABC):
    """
    Describes the stack memory usage of a software.
    """

    # StackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.9, p.149
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getExecutableEntityRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExecutableEntityRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHardwareConfiguration  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHardwareConfiguration  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHwElementRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHwElementRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSoftwareContext        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSoftwareContext        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is StackUsage:
            raise TypeError("StackUsage is an abstract class.")

        super().__init__(parent, short_name)

        # The executable entity for which this stack usage is described.
        self.executableEntityRef: Optional[RefType] = None

        # Contains information about the hardware context this stack usage is describing.
        self.hardwareConfiguration: Optional[HardwareConfiguration] = None

        # Specifies for which hardware element (e.g. ECU) this stack usage is given.
        self.hwElementRef: Optional[RefType] = None

        # Contains details about the software context this stack usage is provided for.
        self.softwareContext: Optional[SoftwareContext] = None

    def getExecutableEntityRef(self) -> Optional[RefType]:
        """
        The executable entity for which this stack usage is described.
        """
        return self.executableEntityRef

    def setExecutableEntityRef(self, value: Optional[RefType]) -> StackUsage:
        """
        The executable entity for which this stack usage is described.
        A None value is a no-op and does not overwrite an existing executableEntityRef.
        """
        if value is not None:
            self.executableEntityRef = value
        return self

    def getHardwareConfiguration(self) -> Optional[HardwareConfiguration]:
        """
        Contains information about the hardware context this stack usage is describing.
        """
        return self.hardwareConfiguration

    def setHardwareConfiguration(self, value: Optional[HardwareConfiguration]) -> StackUsage:
        """
        Contains information about the hardware context this stack usage is describing.
        A None value is a no-op and does not overwrite an existing hardwareConfiguration.
        """
        if value is not None:
            self.hardwareConfiguration = value
        return self

    def getHwElementRef(self) -> Optional[RefType]:
        """
        Specifies for which hardware element (e.g. ECU) this stack usage is given.
        """
        return self.hwElementRef

    def setHwElementRef(self, value: Optional[RefType]) -> StackUsage:
        """
        Specifies for which hardware element (e.g. ECU) this stack usage is given.
        A None value is a no-op and does not overwrite an existing hwElementRef.
        """
        if value is not None:
            self.hwElementRef = value
        return self

    def getSoftwareContext(self) -> Optional[SoftwareContext]:
        """
        Contains details about the software context this stack usage is provided for.
        """
        return self.softwareContext

    def setSoftwareContext(self, value: Optional[SoftwareContext]) -> StackUsage:
        """
        Contains details about the software context this stack usage is provided for.
        A None value is a no-op and does not overwrite an existing softwareContext.
        """
        if value is not None:
            self.softwareContext = value
        return self


# Runtime cycle-breaker: ResourceConsumption.__init__ defines HardwareConfiguration /
# SoftwareContext and imports this module, so this import must run after every class
# above is defined; the parent package defines both classes before importing this
# module (Rule 0005).
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, SoftwareContext  # noqa: E402


class MeasuredStackUsage(StackUsage):
    """
    The stack usage has been measured.
    """

    # MeasuredStackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.11, p.150
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAverageMemoryConsumption  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAverageMemoryConsumption  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaximumMemoryConsumption  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumMemoryConsumption  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinimumMemoryConsumption  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinimumMemoryConsumption  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTestPattern               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTestPattern               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The average stack usage measured. Unit: byte.
        self.averageMemoryConsumption: Optional[PositiveInteger] = None

        # The maximum stack usage measured. Unit: byte.
        self.maximumMemoryConsumption: Optional[PositiveInteger] = None

        # The minimum stack usage measured. Unit: byte.
        self.minimumMemoryConsumption: Optional[PositiveInteger] = None

        # Description of the test pattern used to acquire the measured values.
        self.testPattern: Optional[String] = None

    def getAverageMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        The average stack usage measured. Unit: byte.
        """
        return self.averageMemoryConsumption

    def setAverageMemoryConsumption(self, value: Optional[PositiveInteger]) -> MeasuredStackUsage:
        """
        The average stack usage measured. Unit: byte.
        A None value is a no-op and does not overwrite an existing averageMemoryConsumption.
        """
        if value is not None:
            self.averageMemoryConsumption = value
        return self

    def getMaximumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        The maximum stack usage measured. Unit: byte.
        """
        return self.maximumMemoryConsumption

    def setMaximumMemoryConsumption(self, value: Optional[PositiveInteger]) -> MeasuredStackUsage:
        """
        The maximum stack usage measured. Unit: byte.
        A None value is a no-op and does not overwrite an existing maximumMemoryConsumption.
        """
        if value is not None:
            self.maximumMemoryConsumption = value
        return self

    def getMinimumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        The minimum stack usage measured. Unit: byte.
        """
        return self.minimumMemoryConsumption

    def setMinimumMemoryConsumption(self, value: Optional[PositiveInteger]) -> MeasuredStackUsage:
        """
        The minimum stack usage measured. Unit: byte.
        A None value is a no-op and does not overwrite an existing minimumMemoryConsumption.
        """
        if value is not None:
            self.minimumMemoryConsumption = value
        return self

    def getTestPattern(self) -> Optional[String]:
        """
        Description of the test pattern used to acquire the measured values.
        """
        return self.testPattern

    def setTestPattern(self, value: Optional[String]) -> MeasuredStackUsage:
        """
        Description of the test pattern used to acquire the measured values.
        A None value is a no-op and does not overwrite an existing testPattern.
        """
        if value is not None:
            self.testPattern = value
        return self


class RoughEstimateStackUsage(StackUsage):
    """
    Rough estimation of the stack usage.
    """

    # RoughEstimateStackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.12, p.151
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMemoryConsumption  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMemoryConsumption  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Rough estimate of the stack usage. Unit: byte.
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Rough estimate of the stack usage. Unit: byte.
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> RoughEstimateStackUsage:
        """
        Rough estimate of the stack usage. Unit: byte.
        A None value is a no-op and does not overwrite an existing memoryConsumption.
        """
        if value is not None:
            self.memoryConsumption = value
        return self


class WorstCaseStackUsage(StackUsage):
    """
    Provides a formal worst case stack usage.
    """

    # WorstCaseStackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.10, p.150
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMemoryConsumption  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMemoryConsumption  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Worst case stack consumption. Unit: byte.
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Worst case stack consumption. Unit: byte.
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> WorstCaseStackUsage:
        """
        Worst case stack consumption. Unit: byte.
        A None value is a no-op and does not overwrite an existing memoryConsumption.
        """
        if value is not None:
            self.memoryConsumption = value
        return self
