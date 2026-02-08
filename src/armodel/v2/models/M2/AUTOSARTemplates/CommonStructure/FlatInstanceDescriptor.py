from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AtpFeature,
    Identifier,
    RtePluginProps,
    SwDataDefProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


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
        # The role denotes the particular role of the downstream described by this
                # FlatInstanceDescriptor.
        # to use case where one upstream object results downstream objects, e.
        # g.
        # ModeDeclaration are measurable.
        # In this case the provide locations for current mode, previous next mode.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
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

        if not isinstance(value, Identifier):
            raise TypeError(
                f"role must be Identifier or None, got {type(value).__name__}"
            )
        self._role = value
        # The properties of a communication graph with respect to of RTE Implementation
        # Plug-in.
        self._rtePluginProps: Optional["RtePluginProps"] = None

    @property
    def rte_plugin_props(self) -> Optional["RtePluginProps"]:
        """Get rtePluginProps (Pythonic accessor)."""
        return self._rtePluginProps

    @rte_plugin_props.setter
    def rte_plugin_props(self, value: Optional["RtePluginProps"]) -> None:
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
        # The properties of this FlatInstanceDescriptor.
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
        # which could be: the SYSTEM_ SYSTEM_EXTRACT, or ECU_ SW_CLUSTER_SYSTEM_ the
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

    def setEcuExtract(self, value: "AtpFeature") -> "FlatInstanceDescriptor":
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

    def setRole(self, value: "Identifier") -> "FlatInstanceDescriptor":
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

    def getRtePluginProps(self) -> "RtePluginProps":
        """
        AUTOSAR-compliant getter for rtePluginProps.

        Returns:
            The rtePluginProps value

        Note:
            Delegates to rte_plugin_props property (CODING_RULE_V2_00017)
        """
        return self.rte_plugin_props  # Delegates to property

    def setRtePluginProps(self, value: "RtePluginProps") -> "FlatInstanceDescriptor":
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

    def setSwDataDef(self, value: "SwDataDefProps") -> "FlatInstanceDescriptor":
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

    def setUpstream(self, value: "AtpFeature") -> "FlatInstanceDescriptor":
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

    def with_ecu_extract(self, value: Optional["AtpFeature"]) -> "FlatInstanceDescriptor":
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

    def with_role(self, value: Optional["Identifier"]) -> "FlatInstanceDescriptor":
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

    def with_rte_plugin_props(self, value: Optional["RtePluginProps"]) -> "FlatInstanceDescriptor":
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

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "FlatInstanceDescriptor":
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

    def with_upstream(self, value: Optional["AtpFeature"]) -> "FlatInstanceDescriptor":
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
