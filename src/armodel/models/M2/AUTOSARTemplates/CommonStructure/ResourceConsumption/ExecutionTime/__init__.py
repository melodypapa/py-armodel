"""
This module defines execution time resource consumption classes in AUTOSAR.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, SoftwareContext


class ExecutionTime(Identifiable, ABC):
    """
    Base class for several means how to describe the ExecutionTime of software.
    The required context information is provided through this class.
    """

    # ExecutionTime method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.17, p.159
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaRef          [x] impl  [x] docstring  [x] test
    # [x] setExclusiveAreaRef          [x] impl  [x] docstring  [x] test
    # [x] getExecutableEntityRef       [x] impl  [x] docstring  [x] test
    # [x] setExecutableEntityRef       [x] impl  [x] docstring  [x] test
    # [x] getHardwareConfiguration     [x] impl  [x] docstring  [x] test
    # [x] setHardwareConfiguration     [x] impl  [x] docstring  [x] test
    # [x] getHwElementRef              [x] impl  [x] docstring  [x] test
    # [x] setHwElementRef              [x] impl  [x] docstring  [x] test
    # [x] addIncludedLibraryRef        [x] impl  [x] docstring  [x] test
    # [x] getIncludedLibraryRefs       [x] impl  [x] docstring  [x] test
    # [x] addMemorySectionLocation     [x] impl  [x] docstring  [x] test
    # [x] getMemorySectionLocations    [x] impl  [x] docstring  [x] test
    # [x] getSoftwareContext           [x] impl  [x] docstring  [x] test
    # [x] setSoftwareContext           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ExecutionTime with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this execution time
            short_name: The unique short name of this execution time
        """
        if type(self) is ExecutionTime:
            raise TypeError("ExecutionTime is an abstract class.")

        super().__init__(parent, short_name)

        # Reference to the ExclusiveArea this execution time is provided for.
        self.exclusiveAreaRef: Optional[RefType] = None

        # The executable entity for which this execution time is described.
        self.executableEntityRef: Optional[RefType] = None

        # Provides information on the HardwareConfiguration used to specify this
        # ExecutionTime. [constr_10313] The attribute shall exist at the time when
        # the configuration of the BSW module is finished.
        self.hardwareConfiguration: Optional[HardwareConfiguration] = None

        # The hardware element (e.g. type of ECU) for which the execution time is specified.
        self.hwElementRef: Optional[RefType] = None

        # If this dependency is specified, the execution time of the library code is
        # included in the execution time data for the runnable.
        self.includedLibraryRefs: List[RefType] = []

        # Provides information on the MemorySectionLocation which is involved in the
        # ExecutionTime description.
        self.memorySectionLocations: List["MemorySectionLocation"] = []

        # Provides information on the detailed SoftwareContext used to provide the
        # ExecutionTime description. [constr_10314] The attribute shall exist at the
        # time when the configuration of the BSW module is finished.
        self.softwareContext: Optional[SoftwareContext] = None

    def getExclusiveAreaRef(self) -> Optional[RefType]:
        """
        Gets the reference to the ExclusiveArea this execution time is provided for.

        Returns:
            RefType referencing the exclusive area, or None if not set
        """
        return self.exclusiveAreaRef

    def setExclusiveAreaRef(self, value: Optional[RefType]) -> "ExecutionTime":
        """
        Sets the reference to the ExclusiveArea this execution time is provided for.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The exclusive area reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exclusiveAreaRef = value
        return self

    def getExecutableEntityRef(self) -> Optional[RefType]:
        """
        Gets the reference to the executable entity for which this execution time is described.

        Returns:
            RefType referencing the executable entity, or None if not set
        """
        return self.executableEntityRef

    def setExecutableEntityRef(self, value: Optional[RefType]) -> "ExecutionTime":
        """
        Sets the reference to the executable entity for which this execution time is described.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The executable entity reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.executableEntityRef = value
        return self

    def getHardwareConfiguration(self) -> Optional[HardwareConfiguration]:
        """
        Gets the information on the HardwareConfiguration used to specify this
        ExecutionTime. [constr_10313]

        Returns:
            HardwareConfiguration instance, or None if not set
        """
        return self.hardwareConfiguration

    def setHardwareConfiguration(self, value: Optional[HardwareConfiguration]) -> "ExecutionTime":
        """
        Sets the information on the HardwareConfiguration used to specify this
        ExecutionTime. [constr_10313] The attribute shall exist at the time when the
        configuration of the BSW module is finished.
        A None value is a no-op and does not overwrite an existing configuration.

        Args:
            value: The hardware configuration to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hardwareConfiguration = value
        return self

    def getHwElementRef(self) -> Optional[RefType]:
        """
        Gets the reference to the hardware element for which the execution time is specified.

        Returns:
            RefType referencing the hardware element, or None if not set
        """
        return self.hwElementRef

    def setHwElementRef(self, value: Optional[RefType]) -> "ExecutionTime":
        """
        Sets the reference to the hardware element (e.g. type of ECU) for which the
        execution time is specified.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The hardware element reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwElementRef = value
        return self

    def addIncludedLibraryRef(self, value: Optional[RefType]) -> "ExecutionTime":
        """
        Adds a reference to a DependencyOnArtifact. If this dependency is specified,
        the execution time of the library code is included in the execution time data
        for the runnable.

        Args:
            value: The included library reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.includedLibraryRefs.append(value)
        return self

    def getIncludedLibraryRefs(self) -> List[RefType]:
        """
        Gets the references to the DependencyOnArtifact instances whose library code is
        included in the execution time data for the runnable.

        Returns:
            List of RefType references to included libraries
        """
        return self.includedLibraryRefs

    def addMemorySectionLocation(self, value: Optional["MemorySectionLocation"]) -> "ExecutionTime":
        """
        Adds a MemorySectionLocation which is involved in the ExecutionTime description.

        Args:
            value: The memory section location to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.memorySectionLocations.append(value)
        return self

    def getMemorySectionLocations(self) -> List["MemorySectionLocation"]:
        """
        Gets the MemorySectionLocations which are involved in the ExecutionTime description.

        Returns:
            List of MemorySectionLocation instances
        """
        return self.memorySectionLocations

    def getSoftwareContext(self) -> Optional[SoftwareContext]:
        """
        Gets the information on the detailed SoftwareContext used to provide the
        ExecutionTime description. [constr_10314]

        Returns:
            SoftwareContext instance, or None if not set
        """
        return self.softwareContext

    def setSoftwareContext(self, value: Optional[SoftwareContext]) -> "ExecutionTime":
        """
        Sets the information on the detailed SoftwareContext used to provide the
        ExecutionTime description. [constr_10314] The attribute shall exist at the time
        when the configuration of the BSW module is finished.
        A None value is a no-op and does not overwrite an existing context.

        Args:
            value: The software context to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.softwareContext = value
        return self


class MemorySectionLocation(ARObject):
    """
    Specifies in which hardware ProvidedMemorySegment the softwareMemorySection is located.
    """

    # MemorySectionLocation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.19, p.162
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getProvidedMemoryRef         [x] impl  [x] docstring  [x] test
    # [x] setProvidedMemoryRef         [x] impl  [x] docstring  [x] test
    # [x] getSoftwareMemorySectionRef  [x] impl  [x] docstring  [x] test
    # [x] setSoftwareMemorySectionRef  [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the MemorySectionLocation.
        """
        super().__init__()

        # Reference to the hardware ProvidedMemorySegment. [constr_10318] The reference
        # in the role providedMemory shall exist at the time when the configuration of
        # the BSW module is finished.
        self.providedMemoryRef: Optional[RefType] = None

        # Reference to the MemorySection which is mapped on a certain hardware memory
        # segment. [constr_10319] The reference in the role softwareMemorySection shall
        # exist at the time when the configuration of the BSW module is finished.
        self.softwareMemorySectionRef: Optional[RefType] = None

    def getProvidedMemoryRef(self) -> Optional[RefType]:
        """
        Gets the reference to the hardware ProvidedMemorySegment.

        Returns:
            RefType referencing the provided memory segment, or None if not set
        """
        return self.providedMemoryRef

    def setProvidedMemoryRef(self, value: Optional[RefType]) -> "MemorySectionLocation":
        """
        Sets the reference to the hardware ProvidedMemorySegment.

        Args:
            value: The provided memory reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.providedMemoryRef = value
        return self

    def getSoftwareMemorySectionRef(self) -> Optional[RefType]:
        """
        Gets the reference to the MemorySection which is mapped on a certain hardware memory segment.

        Returns:
            RefType referencing the software memory section, or None if not set
        """
        return self.softwareMemorySectionRef

    def setSoftwareMemorySectionRef(self, value: Optional[RefType]) -> "MemorySectionLocation":
        """
        Sets the reference to the MemorySection which is mapped on a certain hardware memory segment.

        Args:
            value: The software memory section reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.softwareMemorySectionRef = value
        return self


class AnalyzedExecutionTime(ExecutionTime):
    """
    AnalyzedExecutionTime provides an analytic method for specifying the best and
    worst case execution time.
    [constr_4031] The attribute values of AnalyzedExecutionTime shall fulfill:
    bestCaseExecutionTime <= worstCaseExecutionTime.
    """

    # AnalyzedExecutionTime method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.21, p.164
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getBestCaseExecutionTime     [x] impl  [x] docstring  [x] test
    # [x] setBestCaseExecutionTime     [x] impl  [x] docstring  [x] test
    # [x] getWorstCaseExecutionTime    [x] impl  [x] docstring  [x] test
    # [x] setWorstCaseExecutionTime    [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the AnalyzedExecutionTime with a parent and short name.

        Args:
            parent: The parent ARObject that contains this analyzed execution time
            short_name: The unique short name of this analyzed execution time
        """
        super().__init__(parent, short_name)

        # The best case execution time (BCET) defines the minimum amount of time the
        # related executable entity requires for its execution. [constr_10323] The
        # attribute shall exist at the time when the configuration of the BSW module is
        # finished.
        self.bestCaseExecutionTime: Optional[MultidimensionalTime] = None

        # The worst case execution time (WCET) defines the maximum amount of time the
        # related executable entity requires for its execution. [constr_10324] The
        # attribute shall exist at the time when the configuration of the BSW module is
        # finished.
        self.worstCaseExecutionTime: Optional[MultidimensionalTime] = None

    def getBestCaseExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the best case execution time (BCET).

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.bestCaseExecutionTime

    def setBestCaseExecutionTime(self, value: Optional[MultidimensionalTime]) -> "AnalyzedExecutionTime":
        """
        Sets the best case execution time (BCET).

        Args:
            value: The best case execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bestCaseExecutionTime = value
        return self

    def getWorstCaseExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the worst case execution time (WCET).

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.worstCaseExecutionTime

    def setWorstCaseExecutionTime(self, value: Optional[MultidimensionalTime]) -> "AnalyzedExecutionTime":
        """
        Sets the worst case execution time (WCET).

        Args:
            value: The worst case execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.worstCaseExecutionTime = value
        return self


class MeasuredExecutionTime(ExecutionTime):
    """
    Specifies the ExecutionTime which has been gathered using measurement means.
    [constr_4032] The attribute values of MeasuredExecutionTime shall fulfill:
    minimumExecutionTime <= nominalExecutionTime <= maximumExecutionTime.
    """

    # MeasuredExecutionTime method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.23, p.166
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getMaximumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] setMaximumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] getMinimumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] setMinimumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] getNominalExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] setNominalExecutionTime      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the MeasuredExecutionTime with a parent and short name.

        Args:
            parent: The parent ARObject that contains this measured execution time
            short_name: The unique short name of this measured execution time
        """
        super().__init__(parent, short_name)

        # The maximum measured execution time. [constr_10325] The attribute shall exist
        # at the time when the configuration of the BSW module is finished.
        self.maximumExecutionTime: Optional[MultidimensionalTime] = None

        # The minimum measured execution time. [constr_10326] The attribute shall exist
        # at the time when the configuration of the BSW module is finished.
        self.minimumExecutionTime: Optional[MultidimensionalTime] = None

        # The nominal measured execution time. [constr_10327] The attribute shall exist
        # at the time when the configuration of the BSW module is finished.
        self.nominalExecutionTime: Optional[MultidimensionalTime] = None

    def getMaximumExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the maximum measured execution time.

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.maximumExecutionTime

    def setMaximumExecutionTime(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTime":
        """
        Sets the maximum measured execution time.

        Args:
            value: The maximum execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maximumExecutionTime = value
        return self

    def getMinimumExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the minimum measured execution time.

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.minimumExecutionTime

    def setMinimumExecutionTime(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTime":
        """
        Sets the minimum measured execution time.

        Args:
            value: The minimum execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minimumExecutionTime = value
        return self

    def getNominalExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the nominal measured execution time.

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.nominalExecutionTime

    def setNominalExecutionTime(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTime":
        """
        Sets the nominal measured execution time.

        Args:
            value: The nominal execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nominalExecutionTime = value
        return self


class SimulatedExecutionTime(ExecutionTime):
    """
    Specifies the ExecutionTime which has been gathered using simulation means.
    [constr_4033] The attribute values of SimulatedExecutionTime shall fulfill:
    minimumExecutionTime <= nominalExecutionTime <= maximumExecutionTime.
    """

    # SimulatedExecutionTime method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.24, p.167
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getMaximumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] setMaximumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] getMinimumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] setMinimumExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] getNominalExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] setNominalExecutionTime      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SimulatedExecutionTime with a parent and short name.

        Args:
            parent: The parent ARObject that contains this simulated execution time
            short_name: The unique short name of this simulated execution time
        """
        super().__init__(parent, short_name)

        # The maximum simulated execution time. [constr_10331] The attribute shall exist
        # at the time when the configuration of the BSW module is finished.
        self.maximumExecutionTime: Optional[MultidimensionalTime] = None

        # The minimum simulated execution time. [constr_10332] The attribute shall exist
        # at the time when the configuration of the BSW module is finished.
        self.minimumExecutionTime: Optional[MultidimensionalTime] = None

        # The nominal simulated execution time. [constr_10333] The attribute shall exist
        # at the time when the configuration of the BSW module is finished.
        self.nominalExecutionTime: Optional[MultidimensionalTime] = None

    def getMaximumExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the maximum simulated execution time.

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.maximumExecutionTime

    def setMaximumExecutionTime(self, value: Optional[MultidimensionalTime]) -> "SimulatedExecutionTime":
        """
        Sets the maximum simulated execution time.

        Args:
            value: The maximum execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maximumExecutionTime = value
        return self

    def getMinimumExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the minimum simulated execution time.

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.minimumExecutionTime

    def setMinimumExecutionTime(self, value: Optional[MultidimensionalTime]) -> "SimulatedExecutionTime":
        """
        Sets the minimum simulated execution time.

        Args:
            value: The minimum execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minimumExecutionTime = value
        return self

    def getNominalExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the nominal simulated execution time.

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.nominalExecutionTime

    def setNominalExecutionTime(self, value: Optional[MultidimensionalTime]) -> "SimulatedExecutionTime":
        """
        Sets the nominal simulated execution time.

        Args:
            value: The nominal execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nominalExecutionTime = value
        return self


class RoughEstimateOfExecutionTime(ExecutionTime):
    """
    Provides a description of a rough estimate on the ExecutionTime.
    """

    # RoughEstimateOfExecutionTime method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.25, p.167
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAdditionalInformation     [x] impl  [x] docstring  [x] test
    # [x] setAdditionalInformation     [x] impl  [x] docstring  [x] test
    # [x] getEstimatedExecutionTime    [x] impl  [x] docstring  [x] test
    # [x] setEstimatedExecutionTime    [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RoughEstimateOfExecutionTime with a parent and short name.

        Args:
            parent: The parent ARObject that contains this rough estimate of execution time
            short_name: The unique short name of this rough estimate of execution time
        """
        super().__init__(parent, short_name)

        # Provides description on the rough estimate of the ExecutionTime. [constr_10334]
        # The attribute shall exist at the time when the configuration of the BSW module
        # is finished.
        self.additionalInformation: Optional[String] = None

        # The estimated execution time. [constr_10335] The attribute shall exist at the
        # time when the configuration of the BSW module is finished.
        self.estimatedExecutionTime: Optional[MultidimensionalTime] = None

    def getAdditionalInformation(self) -> Optional[String]:
        """
        Gets the description on the rough estimate of the execution time.

        Returns:
            String containing additional information, or None if not set
        """
        return self.additionalInformation

    def setAdditionalInformation(self, value: Optional[String]) -> "RoughEstimateOfExecutionTime":
        """
        Sets the description on the rough estimate of the execution time.

        Args:
            value: The additional information to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.additionalInformation = value
        return self

    def getEstimatedExecutionTime(self) -> Optional[MultidimensionalTime]:
        """
        Gets the estimated execution time.

        Returns:
            MultidimensionalTime instance, or None if not set
        """
        return self.estimatedExecutionTime

    def setEstimatedExecutionTime(self, value: Optional[MultidimensionalTime]) -> "RoughEstimateOfExecutionTime":
        """
        Sets the estimated execution time.

        Args:
            value: The estimated execution time to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.estimatedExecutionTime = value
        return self
