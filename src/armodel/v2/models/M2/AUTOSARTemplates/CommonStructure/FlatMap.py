"""
AUTOSAR Package - FlatMap

Package: M2::AUTOSARTemplates::CommonStructure::FlatMap
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    String,
)


class AliasNameSet(ARElement):
    """
    This meta-class represents a set of AliasNames. The AliasNameSet can for
    example be an input to the A2L-Generator.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::AliasNameSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 174, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 968, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 160, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AliasNames contained in the AliasNameSet.
        # atpVariation.
        self._aliasName: List[AliasNameAssignment] = []

    @property
    def alias_name(self) -> List[AliasNameAssignment]:
        """Get aliasName (Pythonic accessor)."""
        return self._aliasName

    def with_alias_name(self, value):
        """
        Set alias_name and return self for chaining.

        Args:
            value: The alias_name to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alias_name("value")
        """
        self.alias_name = value  # Use property setter (gets validation)
        return self

    def with_instance(self, value):
        """
        Set instance and return self for chaining.

        Args:
            value: The instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_instance("value")
        """
        self.instance = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAliasName(self) -> List[AliasNameAssignment]:
        """
        AUTOSAR-compliant getter for aliasName.

        Returns:
            The aliasName value

        Note:
            Delegates to alias_name property (CODING_RULE_V2_00017)
        """
        return self.alias_name  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AliasNameAssignment(ARObject):
    """
    that flatInstance and identifiable are mutually exclusive.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::AliasNameAssignment

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 175, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 968, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Assignment of a unique name to a flat representation.
        self._flatInstance: Optional[FlatInstanceDescriptor] = None

    @property
    def flat_instance(self) -> Optional[FlatInstanceDescriptor]:
        """Get flatInstance (Pythonic accessor)."""
        return self._flatInstance

    @flat_instance.setter
    def flat_instance(self, value: Optional[FlatInstanceDescriptor]) -> None:
        """
        Set flatInstance with validation.

        Args:
            value: The flatInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flatInstance = None
            return

        if not isinstance(value, FlatInstanceDescriptor):
            raise TypeError(
                f"flatInstance must be FlatInstanceDescriptor or None, got {type(value).__name__}"
            )
        self._flatInstance = value
        self._identifiable: Optional[Identifiable] = None

    @property
    def identifiable(self) -> Optional[Identifiable]:
        """Get identifiable (Pythonic accessor)."""
        return self._identifiable

    @identifiable.setter
    def identifiable(self, value: Optional[Identifiable]) -> None:
        """
        Set identifiable with validation.

        Args:
            value: The identifiable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identifiable = None
            return

        if not isinstance(value, Identifiable):
            raise TypeError(
                f"identifiable must be Identifiable or None, got {type(value).__name__}"
            )
        self._identifiable = value
        # xml.
        # sequenceOffset=20.
        self._label: Optional["MultilanguageLong"] = None

    @property
    def label(self) -> Optional["MultilanguageLong"]:
        """Get label (Pythonic accessor)."""
        return self._label

    @label.setter
    def label(self, value: Optional["MultilanguageLong"]) -> None:
        """
        Set label with validation.

        Args:
            value: The label to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._label = None
            return

        if not isinstance(value, MultilanguageLong):
            raise TypeError(
                f"label must be MultilanguageLong or None, got {type(value).__name__}"
            )
        self._label = value
        # It is modeled as the alias name is used outside of therefore no naming
                # conventions can be AUTOSAR.
        self._shortLabel: Optional[String] = None

    @property
    def short_label(self) -> Optional[String]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional[String]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"shortLabel must be String or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFlatInstance(self) -> FlatInstanceDescriptor:
        """
        AUTOSAR-compliant getter for flatInstance.

        Returns:
            The flatInstance value

        Note:
            Delegates to flat_instance property (CODING_RULE_V2_00017)
        """
        return self.flat_instance  # Delegates to property

    def setFlatInstance(self, value: FlatInstanceDescriptor) -> AliasNameAssignment:
        """
        AUTOSAR-compliant setter for flatInstance with method chaining.

        Args:
            value: The flatInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to flat_instance property setter (gets validation automatically)
        """
        self.flat_instance = value  # Delegates to property setter
        return self

    def getIdentifiable(self) -> Identifiable:
        """
        AUTOSAR-compliant getter for identifiable.

        Returns:
            The identifiable value

        Note:
            Delegates to identifiable property (CODING_RULE_V2_00017)
        """
        return self.identifiable  # Delegates to property

    def setIdentifiable(self, value: Identifiable) -> AliasNameAssignment:
        """
        AUTOSAR-compliant setter for identifiable with method chaining.

        Args:
            value: The identifiable to set

        Returns:
            self for method chaining

        Note:
            Delegates to identifiable property setter (gets validation automatically)
        """
        self.identifiable = value  # Delegates to property setter
        return self

    def getLabel(self) -> "MultilanguageLong":
        """
        AUTOSAR-compliant getter for label.

        Returns:
            The label value

        Note:
            Delegates to label property (CODING_RULE_V2_00017)
        """
        return self.label  # Delegates to property

    def setLabel(self, value: "MultilanguageLong") -> AliasNameAssignment:
        """
        AUTOSAR-compliant setter for label with method chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Note:
            Delegates to label property setter (gets validation automatically)
        """
        self.label = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> String:
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: String) -> AliasNameAssignment:
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_flat_instance(self, value: Optional[FlatInstanceDescriptor]) -> AliasNameAssignment:
        """
        Set flatInstance and return self for chaining.

        Args:
            value: The flatInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flat_instance("value")
        """
        self.flat_instance = value  # Use property setter (gets validation)
        return self

    def with_identifiable(self, value: Optional[Identifiable]) -> AliasNameAssignment:
        """
        Set identifiable and return self for chaining.

        Args:
            value: The identifiable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identifiable("value")
        """
        self.identifiable = value  # Use property setter (gets validation)
        return self

    def with_label(self, value: Optional["MultilanguageLong"]) -> AliasNameAssignment:
        """
        Set label and return self for chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_label("value")
        """
        self.label = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional[String]) -> AliasNameAssignment:
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self



class FlatInstanceDescriptor(Identifiable):
    """
    that in addition it is possible to assign alias names via
    AliasNameAssignment.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::FlatInstanceDescriptor

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 316, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 989, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 966, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # if the FlatMap is used in the context of an ECU shall be such that it
                # uniquely defines the For example, if a data prototype is a role within an
                # SwcInternalBehavior, it is not state the SwcInternalBehavior as context and
                # data prototype as target.
        # In addition, the also include the complete path identifying the component
                # prototype and the Atomic is refered by the by: AnyInstanceRef 381 Document ID
                # 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._ecuExtract: Optional["AtpFeature"] = None

    @property
    def ecu_extract(self) -> Optional["AtpFeature"]:
        """Get ecuExtract (Pythonic accessor)."""
        return self._ecuExtract

    @ecu_extract.setter
    def ecu_extract(self, value: Optional["AtpFeature"]) -> None:
        """
        Set ecuExtract with validation.

        Args:
            value: The ecuExtract to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuExtract = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"ecuExtract must be AtpFeature or None, got {type(value).__name__}"
            )
        self._ecuExtract = value
                # FlatInstanceDescriptor.
        # to use case where one upstream object results downstream objects, e.
        # g.
        # ModeDeclaration are measurable.
        # In this case the provide locations for current mode, previous next mode.
        self._role: Optional[Identifier] = None

    @property
    def role(self) -> Optional[Identifier]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional[Identifier]) -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value
        # Plug-in.
        self._rtePluginProps: Optional[RtePluginProps] = None

    @property
    def rte_plugin_props(self) -> Optional[RtePluginProps]:
        """Get rtePluginProps (Pythonic accessor)."""
        return self._rtePluginProps

    @rte_plugin_props.setter
    def rte_plugin_props(self, value: Optional[RtePluginProps]) -> None:
        """
        Set rtePluginProps with validation.

        Args:
            value: The rtePluginProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rtePluginProps = None
            return

        if not isinstance(value, RtePluginProps):
            raise TypeError(
                f"rtePluginProps must be RtePluginProps or None, got {type(value).__name__}"
            )
        self._rtePluginProps = value
        # atpSplitable.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.

        Args:
            value: The swDataDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value
                # basic software module description case only the target reference of the
                # AnyInstance needed), or (if a flat map is used in preliminary description of
                # an atomic component or is optional in case the flat map is used in The
                # reference shall be such that it uniquely object instance in the given
                # context.
        # For a data prototype is declared as a role within Behavior, it is not enough
                # to state the Swc as context and the aggregated data target.
        # In addition, the reference shall also complete path identifying the instance
                # of the that contains the particular instance InternalBehavior.
        # by: AnyInstanceRef.
        self._upstream: Optional["AtpFeature"] = None

    @property
    def upstream(self) -> Optional["AtpFeature"]:
        """Get upstream (Pythonic accessor)."""
        return self._upstream

    @upstream.setter
    def upstream(self, value: Optional["AtpFeature"]) -> None:
        """
        Set upstream with validation.

        Args:
            value: The upstream to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upstream = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"upstream must be AtpFeature or None, got {type(value).__name__}"
            )
        self._upstream = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuExtract(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for ecuExtract.

        Returns:
            The ecuExtract value

        Note:
            Delegates to ecu_extract property (CODING_RULE_V2_00017)
        """
        return self.ecu_extract  # Delegates to property

    def setEcuExtract(self, value: "AtpFeature") -> FlatInstanceDescriptor:
        """
        AUTOSAR-compliant setter for ecuExtract with method chaining.

        Args:
            value: The ecuExtract to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_extract property setter (gets validation automatically)
        """
        self.ecu_extract = value  # Delegates to property setter
        return self

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> FlatInstanceDescriptor:
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getRtePluginProps(self) -> RtePluginProps:
        """
        AUTOSAR-compliant getter for rtePluginProps.

        Returns:
            The rtePluginProps value

        Note:
            Delegates to rte_plugin_props property (CODING_RULE_V2_00017)
        """
        return self.rte_plugin_props  # Delegates to property

    def setRtePluginProps(self, value: RtePluginProps) -> FlatInstanceDescriptor:
        """
        AUTOSAR-compliant setter for rtePluginProps with method chaining.

        Args:
            value: The rtePluginProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to rte_plugin_props property setter (gets validation automatically)
        """
        self.rte_plugin_props = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> FlatInstanceDescriptor:
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    def getUpstream(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for upstream.

        Returns:
            The upstream value

        Note:
            Delegates to upstream property (CODING_RULE_V2_00017)
        """
        return self.upstream  # Delegates to property

    def setUpstream(self, value: "AtpFeature") -> FlatInstanceDescriptor:
        """
        AUTOSAR-compliant setter for upstream with method chaining.

        Args:
            value: The upstream to set

        Returns:
            self for method chaining

        Note:
            Delegates to upstream property setter (gets validation automatically)
        """
        self.upstream = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_extract(self, value: Optional["AtpFeature"]) -> FlatInstanceDescriptor:
        """
        Set ecuExtract and return self for chaining.

        Args:
            value: The ecuExtract to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_extract("value")
        """
        self.ecu_extract = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional[Identifier]) -> FlatInstanceDescriptor:
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self

    def with_rte_plugin_props(self, value: Optional[RtePluginProps]) -> FlatInstanceDescriptor:
        """
        Set rtePluginProps and return self for chaining.

        Args:
            value: The rtePluginProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rte_plugin_props("value")
        """
        self.rte_plugin_props = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> FlatInstanceDescriptor:
        """
        Set swDataDef and return self for chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self

    def with_upstream(self, value: Optional["AtpFeature"]) -> FlatInstanceDescriptor:
        """
        Set upstream and return self for chaining.

        Args:
            value: The upstream to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upstream("value")
        """
        self.upstream = value  # Use property setter (gets validation)
        return self



class FlatMap(ARElement):
    """
    Contains a flat list of references to software objects. This list is used to
    identify instances and to resolve name conflicts. The scope is given by the
    RootSwCompositionPrototype for which it is used, i.e. it can be applied to a
    system, system extract or ECU-extract. An instance of FlatMap may also be
    used in a preliminary context, e.g. in the scope of a software component
    before integration into a system. In this case it is not referred by a
    RootSwComposition Prototype.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::FlatMap

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 317, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 965, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 445, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 190, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A descriptor instance aggregated in the flat map.
        # point accounts for the fact, that the system can be subject to variability,
                # and thus the some instances is variable.
        # has been made splitable because the be contributed by different stakeholders
                # at in the workflow.
        # Plus, the overall size might big that eventually it becomes more manageable
                # if distributed over several files.
        # atpVariation.
        self._instance: List[FlatInstanceDescriptor] = []

    @property
    def instance(self) -> List[FlatInstanceDescriptor]:
        """Get instance (Pythonic accessor)."""
        return self._instance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInstance(self) -> List[FlatInstanceDescriptor]:
        """
        AUTOSAR-compliant getter for instance.

        Returns:
            The instance value

        Note:
            Delegates to instance property (CODING_RULE_V2_00017)
        """
        return self.instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RtePluginProps(ARObject):
    """
    The properties of a communication graph with respect to the utilization of
    RTE Implementation Plug-in.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::RtePluginProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 971, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This associates a communication graph to a specific RTE Plug-in handling
        # cross Software Cluster.
        self._associated: Optional["EcucContainerValue"] = None

    @property
    def associated(self) -> Optional["EcucContainerValue"]:
        """Get associated (Pythonic accessor)."""
        return self._associated

    @associated.setter
    def associated(self, value: Optional["EcucContainerValue"]) -> None:
        """
        Set associated with validation.

        Args:
            value: The associated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._associated = None
            return

        if not isinstance(value, EcucContainerValue):
            raise TypeError(
                f"associated must be EcucContainerValue or None, got {type(value).__name__}"
            )
        self._associated = value
        # local Software Cluster communication in a non-cluster ECU.
        self._associatedRte: Optional["EcucContainerValue"] = None

    @property
    def associated_rte(self) -> Optional["EcucContainerValue"]:
        """Get associatedRte (Pythonic accessor)."""
        return self._associatedRte

    @associated_rte.setter
    def associated_rte(self, value: Optional["EcucContainerValue"]) -> None:
        """
        Set associatedRte with validation.

        Args:
            value: The associatedRte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._associatedRte = None
            return

        if not isinstance(value, EcucContainerValue):
            raise TypeError(
                f"associatedRte must be EcucContainerValue or None, got {type(value).__name__}"
            )
        self._associatedRte = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssociated(self) -> "EcucContainerValue":
        """
        AUTOSAR-compliant getter for associated.

        Returns:
            The associated value

        Note:
            Delegates to associated property (CODING_RULE_V2_00017)
        """
        return self.associated  # Delegates to property

    def setAssociated(self, value: "EcucContainerValue") -> RtePluginProps:
        """
        AUTOSAR-compliant setter for associated with method chaining.

        Args:
            value: The associated to set

        Returns:
            self for method chaining

        Note:
            Delegates to associated property setter (gets validation automatically)
        """
        self.associated = value  # Delegates to property setter
        return self

    def getAssociatedRte(self) -> "EcucContainerValue":
        """
        AUTOSAR-compliant getter for associatedRte.

        Returns:
            The associatedRte value

        Note:
            Delegates to associated_rte property (CODING_RULE_V2_00017)
        """
        return self.associated_rte  # Delegates to property

    def setAssociatedRte(self, value: "EcucContainerValue") -> RtePluginProps:
        """
        AUTOSAR-compliant setter for associatedRte with method chaining.

        Args:
            value: The associatedRte to set

        Returns:
            self for method chaining

        Note:
            Delegates to associated_rte property setter (gets validation automatically)
        """
        self.associated_rte = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_associated(self, value: Optional["EcucContainerValue"]) -> RtePluginProps:
        """
        Set associated and return self for chaining.

        Args:
            value: The associated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_associated("value")
        """
        self.associated = value  # Use property setter (gets validation)
        return self

    def with_associated_rte(self, value: Optional["EcucContainerValue"]) -> RtePluginProps:
        """
        Set associatedRte and return self for chaining.

        Args:
            value: The associatedRte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_associated_rte("value")
        """
        self.associated_rte = value  # Use property setter (gets validation)
        return self
