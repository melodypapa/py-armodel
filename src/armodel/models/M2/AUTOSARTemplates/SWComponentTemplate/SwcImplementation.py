"""
This module contains classes for representing AUTOSAR software component implementation
elements in software component templates.
"""

from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import PerInstanceMemorySize


class SwcImplementation(Implementation):
    """This meta-class represents a specialization of the general Implementation meta-class with respect to the usage in application software. Tags: atp.recommendedPackage=SwcImplementations"""

    # SwcImplementation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.7, p.623
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBehaviorRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBehaviorRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPerInstanceMemorySizes   [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer  R23-11
    # [x] addPerInstanceMemorySize    [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer  R23-11
    # [x] getRequiredRTEVendor        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequiredRTEVendor        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        # The internal behavior implemented by this Implementation. [constr_1969]
        self.behaviorRef: Optional[RefType] = None

        # Allows a definition of the size of the per-instance memory for this implementation. The aggregation of PerInstanceMemorySize is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects, in this case PerInstanceMemory.
        # (PerInstanceMemorySize class is not yet implemented - Rule 0001.10 placeholder)
        self.perInstanceMemorySizes: List["PerInstanceMemorySize"] = []

        # Identify a specific RTE vendor. This information is potentially important at the time of integrating (in particular: linking) the application code with the RTE. The semantics is that (if the association exists) the corresponding code has been created to fit to the vendor-mode RTE provided by this specific vendor. Attempting to integrate the code with another RTE generated in vendor mode is in general not possible.
        self.requiredRTEVendor: Optional[String] = None

    def getBehaviorRef(self) -> Optional[RefType]:
        """The internal behavior implemented by this Implementation. [constr_1969]"""
        return self.behaviorRef

    def setBehaviorRef(self, value: Optional[RefType]) -> SwcImplementation:
        """The internal behavior implemented by this Implementation. [constr_1969] A None value is a no-op and does not overwrite an existing behaviorRef."""
        if value is not None:
            self.behaviorRef = value
        return self

    def getPerInstanceMemorySizes(self) -> List["PerInstanceMemorySize"]:
        """Allows a definition of the size of the per-instance memory for this implementation. The aggregation of PerInstanceMemorySize is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects, in this case PerInstanceMemory."""
        return self.perInstanceMemorySizes

    def addPerInstanceMemorySize(self, value: Optional["PerInstanceMemorySize"]) -> SwcImplementation:
        """Allows a definition of the size of the per-instance memory for this implementation. The aggregation of PerInstanceMemorySize is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects, in this case PerInstanceMemory. A None value is a no-op and does not append anything."""
        if value is not None:
            self.perInstanceMemorySizes.append(value)
        return self

    def getRequiredRTEVendor(self) -> Optional[String]:
        """Identify a specific RTE vendor. This information is potentially important at the time of integrating (in particular: linking) the application code with the RTE. The semantics is that (if the association exists) the corresponding code has been created to fit to the vendor-mode RTE provided by this specific vendor. Attempting to integrate the code with another RTE generated in vendor mode is in general not possible."""
        return self.requiredRTEVendor

    def setRequiredRTEVendor(self, value: Optional[String]) -> SwcImplementation:
        """Identify a specific RTE vendor. This information is potentially important at the time of integrating (in particular: linking) the application code with the RTE. The semantics is that (if the association exists) the corresponding code has been created to fit to the vendor-mode RTE provided by this specific vendor. Attempting to integrate the code with another RTE generated in vendor mode is in general not possible. A None value is a no-op and does not overwrite an existing requiredRTEVendor."""
        if value is not None:
            self.requiredRTEVendor = value
        return self
