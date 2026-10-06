"""
This module contains the classes of the ImplicitCommunicationBehavior
sub-package of the SWComponentTemplate module, together with its
InstanceRefs sub-module.
"""

from __future__ import annotations

from typing import List, Optional, cast
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import *  # noqa: F401,F403
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)


class DataPrototypeGroup(AtpStructureElement, VariationPointCapable):
    """
    This meta-class represents the ability to define a collection of DataPrototypes that are subject to the formal definition of implicit communication behavior. The definition of the collection can be nested.
    """

    # DataPrototypeGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.101, p.223
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDataPrototypeGroupIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataPrototypeGroupIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addImplicitDataAccessIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImplicitDataAccessIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent; VARIATION-POINT anchored in XSD group DATA-PROTOTYPE-GROUP, sequenceOffset 10000)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the ability to define nested groups of VariableDataPrototypes.
        self.dataPrototypeGroupIRefs: List[InnerDataPrototypeGroupInCompositionInstanceRef] = []

        # This represents a collection of VariableDataPrototypes that belong to the enclosing DataPrototypeGroup
        self.implicitDataAccessIRefs: List[VariableDataPrototypeInCompositionInstanceRef] = []

    def addDataPrototypeGroupIRef(self, value: Optional[InnerDataPrototypeGroupInCompositionInstanceRef]) -> DataPrototypeGroup:
        """
        This represents the ability to define nested groups of VariableDataPrototypes.
        A None value is a no-op and does not append to dataPrototypeGroupIRefs.
        """
        if value is not None:
            self.dataPrototypeGroupIRefs.append(value)
        return self

    def getDataPrototypeGroupIRefs(self) -> List[InnerDataPrototypeGroupInCompositionInstanceRef]:
        """
        This represents the ability to define nested groups of VariableDataPrototypes.
        """
        return self.dataPrototypeGroupIRefs

    def addImplicitDataAccessIRef(self, value: Optional[VariableDataPrototypeInCompositionInstanceRef]) -> DataPrototypeGroup:
        """
        This represents a collection of VariableDataPrototypes that belong to the enclosing DataPrototypeGroup
        A None value is a no-op and does not append to implicitDataAccessIRefs.
        """
        if value is not None:
            self.implicitDataAccessIRefs.append(value)
        return self

    def getImplicitDataAccessIRefs(self) -> List[VariableDataPrototypeInCompositionInstanceRef]:
        """
        This represents a collection of VariableDataPrototypes that belong to the enclosing DataPrototypeGroup
        """
        return self.implicitDataAccessIRefs


class RunnableEntityGroup(AtpStructureElement, VariationPointCapable):
    """
    This meta-class represents the ability to define a collection of RunnableEntities. The collection can be nested.
    """

    # RunnableEntityGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.100, p.223
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRunnableEntityIRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRunnableEntityIRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addRunnableEntityGroupIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRunnableEntityGroupIRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent; VARIATION-POINT anchored in XSD group RUNNABLE-ENTITY-GROUP, sequenceOffset 10000)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents a collection of RunnableEntitys that belong to the enclosing RunnableEntityGroup.
        self.runnableEntityIRefs: List[RunnableEntityInCompositionInstanceRef] = []

        # This represents the ability to define nested groups of RunnableEntitys.
        self.runnableEntityGroupIRefs: List[InnerRunnableEntityGroupInCompositionInstanceRef] = []

    def addRunnableEntityIRef(self, value: Optional[RunnableEntityInCompositionInstanceRef]) -> RunnableEntityGroup:
        """
        This represents a collection of RunnableEntitys that belong to the enclosing RunnableEntityGroup.
        A None value is a no-op and does not append to runnableEntityIRefs.
        """
        if value is not None:
            self.runnableEntityIRefs.append(value)
        return self

    def getRunnableEntityIRefs(self) -> List[RunnableEntityInCompositionInstanceRef]:
        """
        This represents a collection of RunnableEntitys that belong to the enclosing RunnableEntityGroup.
        """
        return self.runnableEntityIRefs

    def addRunnableEntityGroupIRef(self, value: Optional[InnerRunnableEntityGroupInCompositionInstanceRef]) -> RunnableEntityGroup:
        """
        This represents the ability to define nested groups of RunnableEntitys.
        A None value is a no-op and does not append to runnableEntityGroupIRefs.
        """
        if value is not None:
            self.runnableEntityGroupIRefs.append(value)
        return self

    def getRunnableEntityGroupIRefs(self) -> List[InnerRunnableEntityGroupInCompositionInstanceRef]:
        """
        This represents the ability to define nested groups of RunnableEntitys.
        """
        return self.runnableEntityGroupIRefs


class ConsistencyNeeds(AtpBlueprint, VariationPointCapable):
    """
    This meta-class represents the ability to define requirements on the implicit communication behavior.
    """

    # ConsistencyNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.99, p.222
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createDpgDoesNotRequireCoherency   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDpgDoesNotRequireCoherencys     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDpgRequiresCoherency         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDpgRequiresCoherencys           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRegDoesNotRequireStability   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRegDoesNotRequireStabilitys     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRegRequiresStability         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRegRequiresStabilitys           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent; VARIATION-POINT anchored in XSD group CONSISTENCY-NEEDS, sequenceOffset 10000)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This group of VariableDataPrototypes does not require coherency with respect to the implicit communication behavior.
        self.dpgDoesNotRequireCoherencys: List[DataPrototypeGroup] = []

        # This group of VariableDataPrototypes requires coherency with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a coherent manner.
        self.dpgRequiresCoherencys: List[DataPrototypeGroup] = []

        # This group of RunnableEntities does not require stability with respect to the implicit communication behavior.
        self.regDoesNotRequireStabilitys: List[RunnableEntityGroup] = []

        # This group of RunnableEntities requires stability with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a stable manner.
        self.regRequiresStabilitys: List[RunnableEntityGroup] = []

    def createDpgDoesNotRequireCoherency(self, short_name: str) -> DataPrototypeGroup:
        """
        This group of VariableDataPrototypes does not require coherency with respect to the implicit communication behavior.
        """
        if not self.IsReferrableElementExists(short_name, DataPrototypeGroup):
            data_group = DataPrototypeGroup(self, short_name)
            self.addReferrableElement(data_group)
            self.dpgDoesNotRequireCoherencys.append(data_group)
        return cast(DataPrototypeGroup, self.getReferrableElement(short_name, DataPrototypeGroup))

    def getDpgDoesNotRequireCoherencys(self) -> List[DataPrototypeGroup]:
        """
        This group of VariableDataPrototypes does not require coherency with respect to the implicit communication behavior.
        """
        return self.dpgDoesNotRequireCoherencys

    def createDpgRequiresCoherency(self, short_name: str) -> DataPrototypeGroup:
        """
        This group of VariableDataPrototypes requires coherency with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a coherent manner.
        """
        if not self.IsReferrableElementExists(short_name, DataPrototypeGroup):
            data_group = DataPrototypeGroup(self, short_name)
            self.addReferrableElement(data_group)
            self.dpgRequiresCoherencys.append(data_group)
        return cast(DataPrototypeGroup, self.getReferrableElement(short_name, DataPrototypeGroup))

    def getDpgRequiresCoherencys(self) -> List[DataPrototypeGroup]:
        """
        This group of VariableDataPrototypes requires coherency with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a coherent manner.
        """
        return self.dpgRequiresCoherencys

    def createRegDoesNotRequireStability(self, short_name: str) -> RunnableEntityGroup:
        """
        This group of RunnableEntities does not require stability with respect to the implicit communication behavior.
        """
        if not self.IsReferrableElementExists(short_name, RunnableEntityGroup):
            runnable_group = RunnableEntityGroup(self, short_name)
            self.addReferrableElement(runnable_group)
            self.regDoesNotRequireStabilitys.append(runnable_group)
        return cast(RunnableEntityGroup, self.getReferrableElement(short_name, RunnableEntityGroup))

    def getRegDoesNotRequireStabilitys(self) -> List[RunnableEntityGroup]:
        """
        This group of RunnableEntities does not require stability with respect to the implicit communication behavior.
        """
        return self.regDoesNotRequireStabilitys

    def createRegRequiresStability(self, short_name: str) -> RunnableEntityGroup:
        """
        This group of RunnableEntities requires stability with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a stable manner.
        """
        if not self.IsReferrableElementExists(short_name, RunnableEntityGroup):
            runnable_group = RunnableEntityGroup(self, short_name)
            self.addReferrableElement(runnable_group)
            self.regRequiresStabilitys.append(runnable_group)
        return cast(RunnableEntityGroup, self.getReferrableElement(short_name, RunnableEntityGroup))

    def getRegRequiresStabilitys(self) -> List[RunnableEntityGroup]:
        """
        This group of RunnableEntities requires stability with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a stable manner.
        """
        return self.regRequiresStabilitys
