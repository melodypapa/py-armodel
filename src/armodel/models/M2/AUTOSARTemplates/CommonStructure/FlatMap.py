"""
This module contains classes for representing AUTOSAR flat map structures
in the CommonStructure module. Flat maps are used to describe instance
hierarchies in a flat manner, typically used for code generation purposes.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class FlatInstanceDescriptor(Identifiable, VariationPointCapable):
    """
    Represents exactly one node (e.g. a component instance or data element) of the instance tree of a software system. The purpose of this element is to map the various nested representations of this instance to a flat representation and assign a unique name (shortName) to it. Use cases: • Specify unique names of measurable data to be used by MCD tools • Specify unique names of calibration data to be used by MCD tool • Specify a unique name for an instance of a component prototype in the ECU extract of the system description Note that in addition it is possible to assign alias names via AliasNameAssignment.
    """

    # FlatInstanceDescriptor method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 14.2, p.967
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEcuExtractReferenceIRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuExtractReferenceIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRole                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRtePluginProps            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRtePluginProps            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwDataDefProps            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwDataDefProps            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUpstreamReferenceIRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUpstreamReferenceIRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Refers to the instance in the ECU extract. This is valid only, if the FlatMap is used in the context of an ECU extract. The reference shall be such that it uniquely defines the object instance. For example, if a data prototype is declared as a role within an SwcInternalBehavior, it is not enough to state the SwcInternalBehavior as context and the aggregated data prototype as target. In addition, the reference shall also include the complete path identifying instance of the component prototype and the AtomicSoftwareComponentType, which is refered by the particular SwcInternalBehavior. InstanceRef implemented by: AnyInstanceRef
        self.ecuExtractReferenceIRef: Optional[AnyInstanceRef] = None

        # The role denotes the particular role of the downstream memory location described by this FlatInstanceDescriptor. It applies to use case where one upstream object results in multiple downstream objects, e.g. ModeDeclarationGroupPrototypes which are measurable. In this case the RTE will provide locations for current mode, previous mode and next mode.
        self.role: Optional[Identifier] = None

        # The properties of a communication graph with respect to the utilization of RTE Implementation Plug-in.
        self.rtePluginProps: Optional["RtePluginProps"] = None

        # The properties of this FlatInstanceDescriptor.
        self.swDataDefProps: Optional[SwDataDefProps] = None

        # Refers to the instance in the context of an "upstream" description, which could be: the SYSTEM_DESCRIPTION, or SYSTEM_EXTRACT, or ECU_SYSTEM_DESCRIPTION, or SW_CLUSTER_SYSTEM_DESCRIPTION, or the basic software module description (in this case only the target reference of the AnyInstanceRef is needed), or (if a flat map is used in preliminary context) a description of an atomic component or composition. This reference is optional in case the flat map is used in ECU context. The reference shall be such that it uniquely defines the object instance in the given context. For example, if a data prototype is declared as a role within an SwcInternalBehavior, it is not enough to state the SwcInternalBehavior as context and the aggregated data prototype as target. In addition, the reference shall also include the complete path identifying the instance of the component prototype that contains the particular instance of SwcInternalBehavior. InstanceRef implemented by: AnyInstanceRef
        self.upstreamReferenceIRef: Optional[AnyInstanceRef] = None

    def getEcuExtractReferenceIRef(self) -> Optional[AnyInstanceRef]:
        """
        Refers to the instance in the ECU extract. This is valid only, if the FlatMap is used in the context of an ECU extract. The reference shall be such that it uniquely defines the object instance. For example, if a data prototype is declared as a role within an SwcInternalBehavior, it is not enough to state the SwcInternalBehavior as context and the aggregated data prototype as target. In addition, the reference shall also include the complete path identifying instance of the component prototype and the AtomicSoftwareComponentType, which is refered by the particular SwcInternalBehavior. InstanceRef implemented by: AnyInstanceRef
        """
        return self.ecuExtractReferenceIRef

    def setEcuExtractReferenceIRef(self, value: Optional[AnyInstanceRef]) -> "FlatInstanceDescriptor":
        """
        Refers to the instance in the ECU extract. This is valid only, if the FlatMap is used in the context of an ECU extract. The reference shall be such that it uniquely defines the object instance. For example, if a data prototype is declared as a role within an SwcInternalBehavior, it is not enough to state the SwcInternalBehavior as context and the aggregated data prototype as target. In addition, the reference shall also include the complete path identifying instance of the component prototype and the AtomicSoftwareComponentType, which is refered by the particular SwcInternalBehavior. InstanceRef implemented by: AnyInstanceRef

        A None value is a no-op and does not overwrite an existing ecuExtractReferenceIRef.
        """
        if value is not None:
            self.ecuExtractReferenceIRef = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        The role denotes the particular role of the downstream memory location described by this FlatInstanceDescriptor. It applies to use case where one upstream object results in multiple downstream objects, e.g. ModeDeclarationGroupPrototypes which are measurable. In this case the RTE will provide locations for current mode, previous mode and next mode.
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "FlatInstanceDescriptor":
        """
        The role denotes the particular role of the downstream memory location described by this FlatInstanceDescriptor. It applies to use case where one upstream object results in multiple downstream objects, e.g. ModeDeclarationGroupPrototypes which are measurable. In this case the RTE will provide locations for current mode, previous mode and next mode.

        A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self

    def getRtePluginProps(self) -> Optional["RtePluginProps"]:
        """
        The properties of a communication graph with respect to the utilization of RTE Implementation Plug-in.
        """
        return self.rtePluginProps

    def setRtePluginProps(self, value: Optional["RtePluginProps"]) -> "FlatInstanceDescriptor":
        """
        The properties of a communication graph with respect to the utilization of RTE Implementation Plug-in.

        A None value is a no-op and does not overwrite an existing rtePluginProps.
        """
        if value is not None:
            self.rtePluginProps = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        The properties of this FlatInstanceDescriptor.
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "FlatInstanceDescriptor":
        """
        The properties of this FlatInstanceDescriptor.

        A None value is a no-op and does not overwrite an existing swDataDefProps.
        """
        if value is not None:
            self.swDataDefProps = value
        return self

    def getUpstreamReferenceIRef(self) -> Optional[AnyInstanceRef]:
        """
        Refers to the instance in the context of an "upstream" description, which could be: the SYSTEM_DESCRIPTION, or SYSTEM_EXTRACT, or ECU_SYSTEM_DESCRIPTION, or SW_CLUSTER_SYSTEM_DESCRIPTION, or the basic software module description (in this case only the target reference of the AnyInstanceRef is needed), or (if a flat map is used in preliminary context) a description of an atomic component or composition. This reference is optional in case the flat map is used in ECU context. The reference shall be such that it uniquely defines the object instance in the given context. For example, if a data prototype is declared as a role within an SwcInternalBehavior, it is not enough to state the SwcInternalBehavior as context and the aggregated data prototype as target. In addition, the reference shall also include the complete path identifying the instance of the component prototype that contains the particular instance of SwcInternalBehavior. InstanceRef implemented by: AnyInstanceRef
        """
        return self.upstreamReferenceIRef

    def setUpstreamReferenceIRef(self, value: Optional[AnyInstanceRef]) -> "FlatInstanceDescriptor":
        """
        Refers to the instance in the context of an "upstream" description, which could be: the SYSTEM_DESCRIPTION, or SYSTEM_EXTRACT, or ECU_SYSTEM_DESCRIPTION, or SW_CLUSTER_SYSTEM_DESCRIPTION, or the basic software module description (in this case only the target reference of the AnyInstanceRef is needed), or (if a flat map is used in preliminary context) a description of an atomic component or composition. This reference is optional in case the flat map is used in ECU context. The reference shall be such that it uniquely defines the object instance in the given context. For example, if a data prototype is declared as a role within an SwcInternalBehavior, it is not enough to state the SwcInternalBehavior as context and the aggregated data prototype as target. In addition, the reference shall also include the complete path identifying the instance of the component prototype that contains the particular instance of SwcInternalBehavior. InstanceRef implemented by: AnyInstanceRef

        A None value is a no-op and does not overwrite an existing upstreamReferenceIRef.
        """
        if value is not None:
            self.upstreamReferenceIRef = value
        return self


class FlatMap(ARElement):
    """
    Contains a flat list of references to software objects. This list is used to identify instances and to resolve name conflicts. The scope is given by the RootSwCompositionPrototype for which it is used, i.e. it can be applied to a system, system extract or ECU-extract. An instance of FlatMap may also be used in a preliminary context, e.g. in the scope of a software component before integration into a system. In this case it is not referred by a RootSwCompositionPrototype.
    """

    # FlatMap method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 14.1, p.966
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createFlatInstanceDescriptor [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInstances                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # A descriptor instance aggregated in the flat map. The variation point accounts for the fact, that the system in scope can be subject to variability, and thus the existence of some instances is variable. The aggregation has been made splitable because the content might be contributed by different stakeholders at different times in the workflow. Plus, the overall size might be so big that eventually it becomes more manageable if it is distributed over several files.
        self.instances: List[FlatInstanceDescriptor] = []

    def createFlatInstanceDescriptor(self, short_name: str) -> FlatInstanceDescriptor:
        """
        A descriptor instance aggregated in the flat map. The variation point accounts for the fact, that the system in scope can be subject to variability, and thus the existence of some instances is variable. The aggregation has been made splitable because the content might be contributed by different stakeholders at different times in the workflow. Plus, the overall size might be so big that eventually it becomes more manageable if it is distributed over several files.
        """
        if not self.IsElementExists(short_name, FlatInstanceDescriptor):
            element = FlatInstanceDescriptor(self, short_name)
            self.addElement(element)
            self.instances.append(element)
        return self.getElement(short_name, FlatInstanceDescriptor)

    def getInstances(self) -> List[FlatInstanceDescriptor]:
        """
        A descriptor instance aggregated in the flat map. The variation point accounts for the fact, that the system in scope can be subject to variability, and thus the existence of some instances is variable. The aggregation has been made splitable because the content might be contributed by different stakeholders at different times in the workflow. Plus, the overall size might be so big that eventually it becomes more manageable if it is distributed over several files.
        """
        return self.instances


class AliasNameAssignment(ARObject, VariationPointCapable):
    """
    This meta-class represents the ability to associate an alternative name to a flat representations or an Identifiable. The usage of this name is defined outside of AUTOSAR. For example this name can be used by MCD tools or as a name for component instances in the ECU extract. Note that flatInstance and identifiable are mutually exclusive.

    [constr_10363] Existence of attribute AliasNameAssignment.shortLabel: For each AliasNameAssignment, the attribute shortLabel shall exist at the time when the configuration of the BSW module is finished.
    """

    # AliasNameAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.3, p.175
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getFlatInstanceRef           [x] impl  [x] docstring  [x] test
    # [x] setFlatInstanceRef           [x] impl  [x] docstring  [x] test
    # [x] getIdentifiableRef           [x] impl  [x] docstring  [x] test
    # [x] setIdentifiableRef           [x] impl  [x] docstring  [x] test
    # [x] getLabel                     [x] impl  [x] docstring  [x] test
    # [x] setLabel                     [x] impl  [x] docstring  [x] test
    # [x] getShortLabel                [x] impl  [x] docstring  [x] test
    # [x] setShortLabel                [x] impl  [x] docstring  [x] test

    def __init__(self):
        super().__init__()

        # Assignment of a unique name to a flat representation.
        self.flatInstanceRef: Optional[RefType] = None

        # Assignment of a unique name to an Identifiable.
        self.identifiableRef: Optional[RefType] = None

        # This represents an "Alias LongName".
        self.label: Optional[MultilanguageLongName] = None

        # This attribute represents the alias name. It is modeled as string because the alias name is used outside of AUTOSAR and therefore no naming conventions can be applied within AUTOSAR.
        self.shortLabel: Optional[String] = None

    def getFlatInstanceRef(self) -> Optional[RefType]:
        """
        Gets the reference assigning a unique name to a flat representation (DEST: FlatInstanceDescriptor subtypes). Mutually exclusive with identifiableRef.

        Returns:
            RefType instance, or None if not set
        """
        return self.flatInstanceRef

    def setFlatInstanceRef(self, value: Optional[RefType]) -> "AliasNameAssignment":
        """
        Sets the reference assigning a unique name to a flat representation (DEST: FlatInstanceDescriptor subtypes). Mutually exclusive with identifiableRef.

        A None value is a no-op and does not overwrite an existing flatInstanceRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.flatInstanceRef = value
        return self

    def getIdentifiableRef(self) -> Optional[RefType]:
        """
        Gets the reference assigning a unique name to an Identifiable (DEST: Identifiable subtypes). Mutually exclusive with flatInstanceRef.

        Returns:
            RefType instance, or None if not set
        """
        return self.identifiableRef

    def setIdentifiableRef(self, value: Optional[RefType]) -> "AliasNameAssignment":
        """
        Sets the reference assigning a unique name to an Identifiable (DEST: Identifiable subtypes). Mutually exclusive with flatInstanceRef.

        A None value is a no-op and does not overwrite an existing identifiableRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.identifiableRef = value
        return self

    def getLabel(self) -> Optional[MultilanguageLongName]:
        """
        Gets the "Alias LongName" (multi-language long name).

        Returns:
            MultilanguageLongName instance, or None if not set
        """
        return self.label

    def setLabel(self, value: Optional[MultilanguageLongName]) -> "AliasNameAssignment":
        """
        Sets the "Alias LongName" (multi-language long name).

        A None value is a no-op and does not overwrite an existing label.

        Args:
            value: The MultilanguageLongName instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.label = value
        return self

    def getShortLabel(self) -> Optional[String]:
        """
        Gets the alias name (modeled as String because it is used outside of AUTOSAR).

        Returns:
            String instance holding the alias name, or None if not set
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[String]) -> "AliasNameAssignment":
        """
        Sets the alias name (modeled as String because it is used outside of AUTOSAR). [constr_10363] shortLabel shall exist at the time when the configuration of the BSW module is finished.

        A None value is a no-op and does not overwrite an existing shortLabel.

        Args:
            value: The String instance holding the alias name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortLabel = value
        return self


class AliasNameSet(ARElement):
    """
    This meta-class represents a set of AliasNames. The AliasNameSet can for example be an input to the A2L-Generator.

    [constr_10362] Existence of attribute AliasNameSet.aliasName: For each AliasNameSet, the attribute aliasName shall exist at least once at the time when the configuration of the BSW module is finished.
    """

    # AliasNameSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.2, p.174
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] addAliasName                 [x] impl  [x] docstring  [x] test
    # [x] getAliasNames                [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the AliasNameSet with a parent and short name.

        Args:
            parent: The parent ARObject that contains this alias name set
            short_name: The unique short name of this alias name set
        """
        super().__init__(parent, short_name)

        # AliasNames contained in the AliasNameSet.
        self.aliasNames: List[AliasNameAssignment] = []

    def addAliasName(self, value: Optional[AliasNameAssignment]) -> "AliasNameSet":
        """
        Appends an AliasNameAssignment to this set.

        A None value is a no-op and does not append to the list.

        Args:
            value: The AliasNameAssignment to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.aliasNames.append(value)
        return self

    def getAliasNames(self) -> List[AliasNameAssignment]:
        """
        Gets the AliasNameAssignments contained in this set.

        Returns:
            List of AliasNameAssignment instances (empty by default)
        """
        return self.aliasNames


class RtePluginProps(ARObject):
    """
    Represents RTE plugin properties in AUTOSAR.
    This class defines properties for RTE plugins.
    """

    # RtePluginProps method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getPluginName                [x] impl  [ ] docstring  [ ] test
    # [ ] setPluginName                [x] impl  [ ] docstring  [ ] test
    # [ ] getPluginVersion             [x] impl  [ ] docstring  [ ] test
    # [ ] setPluginVersion             [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        """
        Initializes the RtePluginProps with default values.
        """
        super().__init__()
        self.pluginName: str = None
        self.pluginVersion: str = None

    def getPluginName(self):
        return self.pluginName

    def setPluginName(self, value):
        self.pluginName = value
        return self

    def getPluginVersion(self):
        return self.pluginVersion

    def setPluginVersion(self, value):
        self.pluginVersion = value
        return self
