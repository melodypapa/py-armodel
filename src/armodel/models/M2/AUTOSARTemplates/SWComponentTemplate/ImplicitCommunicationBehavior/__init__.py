"""
This module contains the classes of the ImplicitCommunicationBehavior
sub-package of the SWComponentTemplate module, together with its
InstanceRefs sub-module.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import *  # noqa: F401,F403
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)


class DataPrototypeGroup(AtpStructureElement):
    """
    This meta-class represents the ability to define a collection of
    DataPrototypes that are subject to the formal definition of implicit
    communication behavior. The definition of the collection can be nested.
    """

    # DataPrototypeGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.101, p.223
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addDataPrototypeGroupIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataPrototypeGroupIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addImplicitDataAccessIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplicitDataAccessIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DataPrototypeGroup with default values.
        """
        super().__init__(parent, short_name)

        # This represents the ability to define nested groups of
        # VariableDataPrototypes.
        self.dataPrototypeGroupIRefs: List[InnerDataPrototypeGroupInCompositionInstanceRef] = []

        # This represents a collection of VariableDataPrototypes that belong to
        # the enclosing DataPrototypeGroup
        self.implicitDataAccessIRefs: List[VariableDataPrototypeInCompositionInstanceRef] = []

    def addDataPrototypeGroupIRef(self, value: Optional[InnerDataPrototypeGroupInCompositionInstanceRef]) -> "DataPrototypeGroup":
        """
        This represents the ability to define nested groups of
        VariableDataPrototypes. A None value is a no-op and does not append to
        dataPrototypeGroupIRefs.

        Args:
            value: The InnerDataPrototypeGroupInCompositionInstanceRef to add

        Returns:
            DataPrototypeGroup: self for method chaining
        """
        if value is not None:
            self.dataPrototypeGroupIRefs.append(value)
        return self

    def getDataPrototypeGroupIRefs(self) -> List[InnerDataPrototypeGroupInCompositionInstanceRef]:
        """
        This represents the ability to define nested groups of
        VariableDataPrototypes.

        Returns:
            List[InnerDataPrototypeGroupInCompositionInstanceRef]: The list of
            dataPrototypeGroup instance references
        """
        return self.dataPrototypeGroupIRefs

    def addImplicitDataAccessIRef(self, value: Optional[VariableDataPrototypeInCompositionInstanceRef]) -> "DataPrototypeGroup":
        """
        This represents a collection of VariableDataPrototypes that belong to
        the enclosing DataPrototypeGroup A None value is a no-op and does not
        append to implicitDataAccessIRefs.

        Args:
            value: The VariableDataPrototypeInCompositionInstanceRef to add

        Returns:
            DataPrototypeGroup: self for method chaining
        """
        if value is not None:
            self.implicitDataAccessIRefs.append(value)
        return self

    def getImplicitDataAccessIRefs(self) -> List[VariableDataPrototypeInCompositionInstanceRef]:
        """
        This represents a collection of VariableDataPrototypes that belong to
        the enclosing DataPrototypeGroup

        Returns:
            List[VariableDataPrototypeInCompositionInstanceRef]: The list of
            implicitDataAccess instance references
        """
        return self.implicitDataAccessIRefs


class RunnableEntityGroup(AtpStructureElement):
    """
    This meta-class represents the ability to define a collection of
    RunnableEntities. The collection can be nested.
    """

    # RunnableEntityGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.100, p.223
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addRunnableEntityIRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRunnableEntityIRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addRunnableEntityGroupIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRunnableEntityGroupIRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RunnableEntityGroup with default values.
        """
        super().__init__(parent, short_name)

        # This represents a collection of RunnableEntitys that belong to the
        # enclosing RunnableEntityGroup.
        self.runnableEntityIRefs: List[RunnableEntityInCompositionInstanceRef] = []

        # This represents the ability to define nested groups of RunnableEntitys.
        self.runnableEntityGroupIRefs: List[InnerRunnableEntityGroupInCompositionInstanceRef] = []

    def addRunnableEntityIRef(self, value: Optional[RunnableEntityInCompositionInstanceRef]) -> "RunnableEntityGroup":
        """
        This represents a collection of RunnableEntitys that belong to the
        enclosing RunnableEntityGroup. A None value is a no-op and does not
        append to runnableEntityIRefs.

        Args:
            value: The RunnableEntityInCompositionInstanceRef to add

        Returns:
            RunnableEntityGroup: self for method chaining
        """
        if value is not None:
            self.runnableEntityIRefs.append(value)
        return self

    def getRunnableEntityIRefs(self) -> List[RunnableEntityInCompositionInstanceRef]:
        """
        This represents a collection of RunnableEntitys that belong to the
        enclosing RunnableEntityGroup.

        Returns:
            List[RunnableEntityInCompositionInstanceRef]: The list of
            runnableEntity instance references
        """
        return self.runnableEntityIRefs

    def addRunnableEntityGroupIRef(self, value: Optional[InnerRunnableEntityGroupInCompositionInstanceRef]) -> "RunnableEntityGroup":
        """
        This represents the ability to define nested groups of
        RunnableEntitys. A None value is a no-op and does not append to
        runnableEntityGroupIRefs.

        Args:
            value: The InnerRunnableEntityGroupInCompositionInstanceRef to add

        Returns:
            RunnableEntityGroup: self for method chaining
        """
        if value is not None:
            self.runnableEntityGroupIRefs.append(value)
        return self

    def getRunnableEntityGroupIRefs(self) -> List[InnerRunnableEntityGroupInCompositionInstanceRef]:
        """
        This represents the ability to define nested groups of
        RunnableEntitys.

        Returns:
            List[InnerRunnableEntityGroupInCompositionInstanceRef]: The list of
            runnableEntityGroup instance references
        """
        return self.runnableEntityGroupIRefs


class ConsistencyNeeds(AtpBlueprintable):
    """
    This meta-class represents the ability to define requirements on the
    implicit communication behavior.
    """

    # ConsistencyNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.99, p.222
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createDpgDoesNotRequireCoherency   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDpgDoesNotRequireCoherencys     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createDpgRequiresCoherency         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDpgRequiresCoherencys           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createRegDoesNotRequireStability   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRegDoesNotRequireStabilitys     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createRegRequiresStability         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRegRequiresStabilitys           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ConsistencyNeeds with default values.
        """
        super().__init__(parent, short_name)

        # This group of VariableDataPrototypes does not require coherency with
        # respect to the implicit communication behavior.
        self.dpgDoesNotRequireCoherency: List[DataPrototypeGroup] = []

        # This group of VariableDataPrototypes requires coherency with respect
        # to the implicit communication behavior, i.e. all read and write
        # access to VariableDataPrototypes in the DataPrototypeGroup by the
        # RunnableEntitys of the RunnableEntityGroup need to be handled in a
        # coherent manner.
        self.dpgRequiresCoherency: List[DataPrototypeGroup] = []

        # This group of RunnableEntities does not require stability with
        # respect to the implicit communication behavior.
        self.regDoesNotRequireStability: List[RunnableEntityGroup] = []

        # This group of RunnableEntities requires stability with respect to the
        # implicit communication behavior, i.e. all read and write access to
        # VariableDataPrototypes in the DataPrototypeGroup by the
        # RunnableEntitys of the RunnableEntityGroup need to be handled in a
        # stable manner.
        self.regRequiresStability: List[RunnableEntityGroup] = []

    def createDpgDoesNotRequireCoherency(self, short_name: str) -> DataPrototypeGroup:
        """
        This group of VariableDataPrototypes does not require coherency with
        respect to the implicit communication behavior.
        Returns the existing DataPrototypeGroup when the short name already
        exists.

        Args:
            short_name: The short name of the DataPrototypeGroup

        Returns:
            DataPrototypeGroup: The created or existing DataPrototypeGroup
        """
        if not self.IsElementExists(short_name, DataPrototypeGroup):
            data_group = DataPrototypeGroup(self, short_name)
            self.addElement(data_group)
            self.dpgDoesNotRequireCoherency.append(data_group)
        return self.getElement(short_name, DataPrototypeGroup)

    def getDpgDoesNotRequireCoherencys(self) -> List[DataPrototypeGroup]:
        """
        This group of VariableDataPrototypes does not require coherency with
        respect to the implicit communication behavior.

        Returns:
            List[DataPrototypeGroup]: The list of DataPrototypeGroups
        """
        return self.dpgDoesNotRequireCoherency

    def createDpgRequiresCoherency(self, short_name: str) -> DataPrototypeGroup:
        """
        This group of VariableDataPrototypes requires coherency with respect
        to the implicit communication behavior, i.e. all read and write access
        to VariableDataPrototypes in the DataPrototypeGroup by the
        RunnableEntitys of the RunnableEntityGroup need to be handled in a
        coherent manner.
        Returns the existing DataPrototypeGroup when the short name already
        exists.

        Args:
            short_name: The short name of the DataPrototypeGroup

        Returns:
            DataPrototypeGroup: The created or existing DataPrototypeGroup
        """
        if not self.IsElementExists(short_name, DataPrototypeGroup):
            data_group = DataPrototypeGroup(self, short_name)
            self.addElement(data_group)
            self.dpgRequiresCoherency.append(data_group)
        return self.getElement(short_name, DataPrototypeGroup)

    def getDpgRequiresCoherencys(self) -> List[DataPrototypeGroup]:
        """
        This group of VariableDataPrototypes requires coherency with respect
        to the implicit communication behavior, i.e. all read and write access
        to VariableDataPrototypes in the DataPrototypeGroup by the
        RunnableEntitys of the RunnableEntityGroup need to be handled in a
        coherent manner.

        Returns:
            List[DataPrototypeGroup]: The list of DataPrototypeGroups
        """
        return self.dpgRequiresCoherency

    def createRegDoesNotRequireStability(self, short_name: str) -> RunnableEntityGroup:
        """
        This group of RunnableEntities does not require stability with respect
        to the implicit communication behavior.
        Returns the existing RunnableEntityGroup when the short name already
        exists.

        Args:
            short_name: The short name of the RunnableEntityGroup

        Returns:
            RunnableEntityGroup: The created or existing RunnableEntityGroup
        """
        if not self.IsElementExists(short_name, RunnableEntityGroup):
            runnable_group = RunnableEntityGroup(self, short_name)
            self.addElement(runnable_group)
            self.regDoesNotRequireStability.append(runnable_group)
        return self.getElement(short_name, RunnableEntityGroup)

    def getRegDoesNotRequireStabilitys(self) -> List[RunnableEntityGroup]:
        """
        This group of RunnableEntities does not require stability with respect
        to the implicit communication behavior.

        Returns:
            List[RunnableEntityGroup]: The list of RunnableEntityGroups
        """
        return self.regDoesNotRequireStability

    def createRegRequiresStability(self, short_name: str) -> RunnableEntityGroup:
        """
        This group of RunnableEntities requires stability with respect to the
        implicit communication behavior, i.e. all read and write access to
        VariableDataPrototypes in the DataPrototypeGroup by the
        RunnableEntitys of the RunnableEntityGroup need to be handled in a
        stable manner.
        Returns the existing RunnableEntityGroup when the short name already
        exists.

        Args:
            short_name: The short name of the RunnableEntityGroup

        Returns:
            RunnableEntityGroup: The created or existing RunnableEntityGroup
        """
        if not self.IsElementExists(short_name, RunnableEntityGroup):
            runnable_group = RunnableEntityGroup(self, short_name)
            self.addElement(runnable_group)
            self.regRequiresStability.append(runnable_group)
        return self.getElement(short_name, RunnableEntityGroup)

    def getRegRequiresStabilitys(self) -> List[RunnableEntityGroup]:
        """
        This group of RunnableEntities requires stability with respect to the
        implicit communication behavior, i.e. all read and write access to
        VariableDataPrototypes in the DataPrototypeGroup by the
        RunnableEntitys of the RunnableEntityGroup need to be handled in a
        stable manner.

        Returns:
            List[RunnableEntityGroup]: The list of RunnableEntityGroups
        """
        return self.regRequiresStability
