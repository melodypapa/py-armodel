from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class McDataInstance(Identifiable):
    """
    Describes the specific properties of one data instance in order to support
    measurement and/or calibration of this data instance. The most important
    attributes are: • Its shortName is copied from the ECU Flat map (if
    applicable) and will be used as identifier and for display by the MC system.
    • The category is copied from the corresponding data type
    (ApplicationDataType if defined, otherwise ImplementationDataType) as far as
    applicable. • The symbol is the one used in the programming language. It
    will be used to find out the actual memory address by the final generation
    tool with the help of linker generated information. It is assumed that in
    the M1 model this part and all the aggregated and referred elements (with
    the exception of the Flat Map and the references from
    ImplementationElementInParameterInstanceRef and McAccessDetails) are
    completely generated from "upstream" information. This means, that even if
    an element like e.g. a CompuMethod is only used via reference here, it will
    be copied into the M1 artifact which holds the complete McSupportData for a
    given Implementation.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 177, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 997, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The existence of this attribute turns the data instance into of data.
        # The attribute determines the size of the terms of number of elements.
        self._arraySize: Optional["PositiveInteger"] = None

    @property
    def array_size(self) -> Optional["PositiveInteger"]:
        """Get arraySize (Pythonic accessor)."""
        return self._arraySize

    @array_size.setter
    def array_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set arraySize with validation.

        Args:
            value: The arraySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arraySize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"arraySize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._arraySize = value
        # An optional attribute to be used to set the ASAM ASAP2.
        self._displayIdentifier: Optional["McdIdentifier"] = None

    @property
    def display_identifier(self) -> Optional["McdIdentifier"]:
        """Get displayIdentifier (Pythonic accessor)."""
        return self._displayIdentifier

    @display_identifier.setter
    def display_identifier(self, value: Optional["McdIdentifier"]) -> None:
        """
        Set displayIdentifier with validation.

        Args:
            value: The displayIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._displayIdentifier = None
            return

        if not isinstance(value, McdIdentifier):
            raise TypeError(
                f"displayIdentifier must be McdIdentifier or None, got {type(value).__name__}"
            )
        self._displayIdentifier = value
        # Reference to the corresponding entry in the ECU Flat allows to trace back to
                # the original specification generated data instance.
        # This link shall be added RTE generator mainly for documentation purposes.
        # is optional because McDataInstance may represent an array or struct only the
                # subElements correspond to FlatMap McDataInstance may represent a task local
                # buffer prototyping access which is different from the used for measurement
                # access.
        self._flatMapEntry: Optional["FlatInstanceDescriptor"] = None

    @property
    def flat_map_entry(self) -> Optional["FlatInstanceDescriptor"]:
        """Get flatMapEntry (Pythonic accessor)."""
        return self._flatMapEntry

    @flat_map_entry.setter
    def flat_map_entry(self, value: Optional["FlatInstanceDescriptor"]) -> None:
        """
        Set flatMapEntry with validation.

        Args:
            value: The flatMapEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flatMapEntry = None
            return

        if not isinstance(value, FlatInstanceDescriptor):
            raise TypeError(
                f"flatMapEntry must be FlatInstanceDescriptor or None, got {type(value).__name__}"
            )
        self._flatMapEntry = value
        # Reference to the corresponding data instance in the description of
                # calibration data structures published by the generator.
        # This is used to support emulation the ECU, it is not required for A2L.
        self._instanceIn: Optional["ImplementationElement"] = None

    @property
    def instance_in(self) -> Optional["ImplementationElement"]:
        """Get instanceIn (Pythonic accessor)."""
        return self._instanceIn

    @instance_in.setter
    def instance_in(self, value: Optional["ImplementationElement"]) -> None:
        """
        Set instanceIn with validation.

        Args:
            value: The instanceIn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._instanceIn = None
            return

        if not isinstance(value, ImplementationElement):
            raise TypeError(
                f"instanceIn must be ImplementationElement or None, got {type(value).__name__}"
            )
        self._instanceIn = value
        # Refers to "upstream" information on how the RTE uses data instance.
        # Use Case: Rapid Prototyping.
        self._mcDataAccess: Optional["McDataAccessDetails"] = None

    @property
    def mc_data_access(self) -> Optional["McDataAccessDetails"]:
        """Get mcDataAccess (Pythonic accessor)."""
        return self._mcDataAccess

    @mc_data_access.setter
    def mc_data_access(self, value: Optional["McDataAccessDetails"]) -> None:
        """
        Set mcDataAccess with validation.

        Args:
            value: The mcDataAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mcDataAccess = None
            return

        if not isinstance(value, McDataAccessDetails):
            raise TypeError(
                f"mcDataAccess must be McDataAccessDetails or None, got {type(value).__name__}"
            )
        self._mcDataAccess = value
        # An assignment between McDataInstances.
        # This supports the indication of related McDataElement implementing "RP global
                # buffer", "RP global measurement enabler flag".
        self._mcData: List["RoleBasedMcData"] = []

    @property
    def mc_data(self) -> List["RoleBasedMcData"]:
        """Get mcData (Pythonic accessor)."""
        return self._mcData
        # These are the generated properties resulting from taken by the RTE generator
                # for the actually instance.
        # Only those properties are which are needed for the measurement system.
        self._resulting: Optional["SwDataDefProps"] = None

    @property
    def resulting(self) -> Optional["SwDataDefProps"]:
        """Get resulting (Pythonic accessor)."""
        return self._resulting

    @resulting.setter
    def resulting(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set resulting with validation.

        Args:
            value: The resulting to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resulting = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"resulting must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._resulting = value
        # Describes the implemented accessibility of data and modes by the rapid
                # prototyping tooling.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._resultingRptSw: Optional["RptSwPrototyping"] = None

    @property
    def resulting_rpt_sw(self) -> Optional["RptSwPrototyping"]:
        """Get resultingRptSw (Pythonic accessor)."""
        return self._resultingRptSw

    @resulting_rpt_sw.setter
    def resulting_rpt_sw(self, value: Optional["RptSwPrototyping"]) -> None:
        """
        Set resultingRptSw with validation.

        Args:
            value: The resultingRptSw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resultingRptSw = None
            return

        if not isinstance(value, RptSwPrototyping):
            raise TypeError(
                f"resultingRptSw must be RptSwPrototyping or None, got {type(value).__name__}"
            )
        self._resultingRptSw = value
        # An optional attribute to be used for additional information role of this data
        # instance, for example in the rapid prototyping.
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
        # Describes the implemented code preparation for rapid data accesses for a hook
        # based bypassing.
        self._rptImplPolicy: Optional["RptImplPolicy"] = None

    @property
    def rpt_impl_policy(self) -> Optional["RptImplPolicy"]:
        """Get rptImplPolicy (Pythonic accessor)."""
        return self._rptImplPolicy

    @rpt_impl_policy.setter
    def rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> None:
        """
        Set rptImplPolicy with validation.

        Args:
            value: The rptImplPolicy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptImplPolicy = None
            return

        if not isinstance(value, RptImplPolicy):
            raise TypeError(
                f"rptImplPolicy must be RptImplPolicy or None, got {type(value).__name__}"
            )
        self._rptImplPolicy = value
        # This relation indicates, that the target element is part of a which is given
                # by the source element.
        # This be used by the final generator to set up addressing scheme.
        # atpVariation.
        self._subElement: List["McDataInstance"] = []

    @property
    def sub_element(self) -> List["McDataInstance"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement
        # This String is used to determine the memory address generation of the MC
                # configuration data (e.
        # g.
        # It shall be the name of the element in the such that it can be identified in
                # information.
        # the McDataInstance is part of composite data in language, the symbol String
                # may denoting the element context, unless the given by the symbol attribute of
                # an enclosing means in particular for the C the ".
        # " character shall be used as a the name of a "struct" variable the one of its
                # elements.
        # can differ from the shortName in case of data declarations.
        # an optional attribute since it may be missing in case represents an element
                # (e.
        # g.
        # a single array has no name in the linker map.
        self._symbol: Optional["SymbolString"] = None

    @property
    def symbol(self) -> Optional["SymbolString"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["SymbolString"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, SymbolString):
            raise TypeError(
                f"symbol must be SymbolString or None, got {type(value).__name__}"
            )
        self._symbol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArraySize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: "PositiveInteger") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for arraySize with method chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to array_size property setter (gets validation automatically)
        """
        self.array_size = value  # Delegates to property setter
        return self

    def getDisplayIdentifier(self) -> "McdIdentifier":
        """
        AUTOSAR-compliant getter for displayIdentifier.

        Returns:
            The displayIdentifier value

        Note:
            Delegates to display_identifier property (CODING_RULE_V2_00017)
        """
        return self.display_identifier  # Delegates to property

    def setDisplayIdentifier(self, value: "McdIdentifier") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for displayIdentifier with method chaining.

        Args:
            value: The displayIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to display_identifier property setter (gets validation automatically)
        """
        self.display_identifier = value  # Delegates to property setter
        return self

    def getFlatMapEntry(self) -> "FlatInstanceDescriptor":
        """
        AUTOSAR-compliant getter for flatMapEntry.

        Returns:
            The flatMapEntry value

        Note:
            Delegates to flat_map_entry property (CODING_RULE_V2_00017)
        """
        return self.flat_map_entry  # Delegates to property

    def setFlatMapEntry(self, value: "FlatInstanceDescriptor") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for flatMapEntry with method chaining.

        Args:
            value: The flatMapEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to flat_map_entry property setter (gets validation automatically)
        """
        self.flat_map_entry = value  # Delegates to property setter
        return self

    def getInstanceIn(self) -> "ImplementationElement":
        """
        AUTOSAR-compliant getter for instanceIn.

        Returns:
            The instanceIn value

        Note:
            Delegates to instance_in property (CODING_RULE_V2_00017)
        """
        return self.instance_in  # Delegates to property

    def setInstanceIn(self, value: "ImplementationElement") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for instanceIn with method chaining.

        Args:
            value: The instanceIn to set

        Returns:
            self for method chaining

        Note:
            Delegates to instance_in property setter (gets validation automatically)
        """
        self.instance_in = value  # Delegates to property setter
        return self

    def getMcDataAccess(self) -> "McDataAccessDetails":
        """
        AUTOSAR-compliant getter for mcDataAccess.

        Returns:
            The mcDataAccess value

        Note:
            Delegates to mc_data_access property (CODING_RULE_V2_00017)
        """
        return self.mc_data_access  # Delegates to property

    def setMcDataAccess(self, value: "McDataAccessDetails") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for mcDataAccess with method chaining.

        Args:
            value: The mcDataAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to mc_data_access property setter (gets validation automatically)
        """
        self.mc_data_access = value  # Delegates to property setter
        return self

    def getMcData(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for mcData.

        Returns:
            The mcData value

        Note:
            Delegates to mc_data property (CODING_RULE_V2_00017)
        """
        return self.mc_data  # Delegates to property

    def getResulting(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for resulting.

        Returns:
            The resulting value

        Note:
            Delegates to resulting property (CODING_RULE_V2_00017)
        """
        return self.resulting  # Delegates to property

    def setResulting(self, value: "SwDataDefProps") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for resulting with method chaining.

        Args:
            value: The resulting to set

        Returns:
            self for method chaining

        Note:
            Delegates to resulting property setter (gets validation automatically)
        """
        self.resulting = value  # Delegates to property setter
        return self

    def getResultingRptSw(self) -> "RptSwPrototyping":
        """
        AUTOSAR-compliant getter for resultingRptSw.

        Returns:
            The resultingRptSw value

        Note:
            Delegates to resulting_rpt_sw property (CODING_RULE_V2_00017)
        """
        return self.resulting_rpt_sw  # Delegates to property

    def setResultingRptSw(self, value: "RptSwPrototyping") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for resultingRptSw with method chaining.

        Args:
            value: The resultingRptSw to set

        Returns:
            self for method chaining

        Note:
            Delegates to resulting_rpt_sw property setter (gets validation automatically)
        """
        self.resulting_rpt_sw = value  # Delegates to property setter
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

    def setRole(self, value: "Identifier") -> "McDataInstance":
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

    def getRptImplPolicy(self) -> "RptImplPolicy":
        """
        AUTOSAR-compliant getter for rptImplPolicy.

        Returns:
            The rptImplPolicy value

        Note:
            Delegates to rpt_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.rpt_impl_policy  # Delegates to property

    def setRptImplPolicy(self, value: "RptImplPolicy") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for rptImplPolicy with method chaining.

        Args:
            value: The rptImplPolicy to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_impl_policy property setter (gets validation automatically)
        """
        self.rpt_impl_policy = value  # Delegates to property setter
        return self

    def getSubElement(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    def getSymbol(self) -> "SymbolString":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "SymbolString") -> "McDataInstance":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["PositiveInteger"]) -> "McDataInstance":
        """
        Set arraySize and return self for chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_size("value")
        """
        self.array_size = value  # Use property setter (gets validation)
        return self

    def with_display_identifier(self, value: Optional["McdIdentifier"]) -> "McDataInstance":
        """
        Set displayIdentifier and return self for chaining.

        Args:
            value: The displayIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_display_identifier("value")
        """
        self.display_identifier = value  # Use property setter (gets validation)
        return self

    def with_flat_map_entry(self, value: Optional["FlatInstanceDescriptor"]) -> "McDataInstance":
        """
        Set flatMapEntry and return self for chaining.

        Args:
            value: The flatMapEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flat_map_entry("value")
        """
        self.flat_map_entry = value  # Use property setter (gets validation)
        return self

    def with_instance_in(self, value: Optional["ImplementationElement"]) -> "McDataInstance":
        """
        Set instanceIn and return self for chaining.

        Args:
            value: The instanceIn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_instance_in("value")
        """
        self.instance_in = value  # Use property setter (gets validation)
        return self

    def with_mc_data_access(self, value: Optional["McDataAccessDetails"]) -> "McDataInstance":
        """
        Set mcDataAccess and return self for chaining.

        Args:
            value: The mcDataAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_data_access("value")
        """
        self.mc_data_access = value  # Use property setter (gets validation)
        return self

    def with_resulting(self, value: Optional["SwDataDefProps"]) -> "McDataInstance":
        """
        Set resulting and return self for chaining.

        Args:
            value: The resulting to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resulting("value")
        """
        self.resulting = value  # Use property setter (gets validation)
        return self

    def with_resulting_rpt_sw(self, value: Optional["RptSwPrototyping"]) -> "McDataInstance":
        """
        Set resultingRptSw and return self for chaining.

        Args:
            value: The resultingRptSw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resulting_rpt_sw("value")
        """
        self.resulting_rpt_sw = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["Identifier"]) -> "McDataInstance":
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

    def with_rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> "McDataInstance":
        """
        Set rptImplPolicy and return self for chaining.

        Args:
            value: The rptImplPolicy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_impl_policy("value")
        """
        self.rpt_impl_policy = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["SymbolString"]) -> "McDataInstance":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self
