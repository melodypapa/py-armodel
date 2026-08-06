"""
This module contains classes for representing AUTOSAR flat map structures
in the CommonStructure module. Flat maps are used to describe instance
hierarchies in a flat manner, typically used for code generation purposes.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable


class FlatInstanceDescriptor(Identifiable):
    """
    Represents a flat instance descriptor in AUTOSAR models.
    This class describes a single instance in a flattened instance hierarchy, typically used for code generation.
    """

    # FlatInstanceDescriptor method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getEcuExtractReferenceIRef   [x] impl  [x] docstring  [x] test
    # [x] setEcuExtractReferenceIRef   [x] impl  [x] docstring  [x] test
    # [x] getRole                      [x] impl  [x] docstring  [x] test
    # [x] setRole                      [x] impl  [x] docstring  [x] test
    # [x] getRtePluginProps            [x] impl  [x] docstring  [x] test
    # [x] setRtePluginProps            [x] impl  [x] docstring  [x] test
    # [x] getSwDataDefProps            [x] impl  [x] docstring  [x] test
    # [x] setSwDataDefProps            [x] impl  [x] docstring  [x] test
    # [x] getUpstreamReferenceIRef     [x] impl  [x] docstring  [x] test
    # [x] setUpstreamReferenceIRef     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FlatInstanceDescriptor with a parent and short name.

        Args:
            parent: The parent ARObject that contains this instance descriptor
            short_name: The unique short name of this instance descriptor
        """
        super().__init__(parent, short_name)

        # Instance reference to ECU extract reference
        self.ecuExtractReferenceIRef: AnyInstanceRef = None
        # Role identifier for this instance descriptor
        self.role: Identifier = None
        # RTE plugin properties for this instance (forward reference)
        self.rtePluginProps = None
        # Software data definition properties for this instance
        self.swDataDefProps: SwDataDefProps = None
        # Upstream instance reference for this instance descriptor
        self.upstreamReferenceIRef: AnyInstanceRef = None

    def getEcuExtractReferenceIRef(self):
        """
        Gets the instance reference to ECU extract reference.

        Returns:
            AnyInstanceRef: The ECU extract reference instance reference
        """
        return self.ecuExtractReferenceIRef

    def setEcuExtractReferenceIRef(self, value):
        """
        Sets the instance reference to ECU extract reference.

        Args:
            value: The ECU extract reference instance reference to set

        Returns:
            self for method chaining
        """
        self.ecuExtractReferenceIRef = value
        return self

    def getRole(self):
        """
        Gets the role identifier for this instance descriptor.

        Returns:
            Identifier: The role identifier
        """
        return self.role

    def setRole(self, value):
        """
        Sets the role identifier for this instance descriptor.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        self.role = value
        return self

    def getRtePluginProps(self):
        """
        Gets the RTE plugin properties for this instance.

        Returns:
            RtePluginProps: The RTE plugin properties
        """
        return self.rtePluginProps

    def setRtePluginProps(self, value):
        """
        Sets the RTE plugin properties for this instance.

        Args:
            value: The RTE plugin properties to set

        Returns:
            self for method chaining
        """
        self.rtePluginProps = value
        return self

    def getSwDataDefProps(self):
        """
        Gets the software data definition properties for this instance.

        Returns:
            SwDataDefProps: The software data definition properties
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        """
        Sets the software data definition properties for this instance.

        Args:
            value: The software data definition properties to set

        Returns:
            self for method chaining
        """
        self.swDataDefProps = value
        return self

    def getUpstreamReferenceIRef(self):
        """
        Gets the upstream instance reference for this instance descriptor.

        Returns:
            AnyInstanceRef: The upstream reference instance reference
        """
        return self.upstreamReferenceIRef

    def setUpstreamReferenceIRef(self, value):
        """
        Sets the upstream instance reference for this instance descriptor.

        Args:
            value: The upstream reference instance reference to set

        Returns:
            self for method chaining
        """
        self.upstreamReferenceIRef = value
        return self


class FlatMap(AtpBlueprintable):
    """
    Represents a flat map in AUTOSAR models.
    This class contains a collection of flat instance descriptors that define a flattened view of instance hierarchies.
    """

    # FlatMap method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getInstances                 [x] impl  [x] docstring  [x] test
    # [x] createFlatInstanceDescriptor [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FlatMap with a parent and short name.

        Args:
            parent: The parent ARObject that contains this flat map
            short_name: The unique short name of this flat map
        """
        super().__init__(parent, short_name)

        # List of flat instance descriptors in this flat map
        self.instances: List["FlatInstanceDescriptor"] = []

    def getInstances(self):
        """
        Gets all flat instance descriptors from the elements list, sorted by short name.

        Returns:
            List of FlatInstanceDescriptor instances sorted by short name
        """
        return list(sorted(filter(lambda a: isinstance(a, FlatInstanceDescriptor), self.elements), key=lambda o: o.short_name))

    def createFlatInstanceDescriptor(self, short_name: str):
        """
        Creates and adds a FlatInstanceDescriptor to this flat map.

        Args:
            short_name: The short name for the new instance descriptor

        Returns:
            The created FlatInstanceDescriptor instance
        """
        if short_name not in self.elements:
            element = FlatInstanceDescriptor(self, short_name)
            self.addElement(element)
            self.instances.append(element)
        return self.getElement(short_name)


class AliasNameAssignment(ARObject):
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
