"""
AUTOSAR Package - MeasurementCalibrationSupport

Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class McSupportData(ARObject):
    """
    Root element for all measurement and calibration support data related to one
    Implementation artifact on an ECU. There shall be one such element related
    to the RTE implementation (if it owns MC data) and a separate one for each
    module or component, which owns private MC data.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McSupportData

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 172, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 999, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes the calibration method used by the RTE.
        # This information is not needed for A2L generation, but to setup in the ECU.
        # atpVariation.
        self._emulation: List["McSwEmulationMethod"] = []

    @property
    def emulation(self) -> List["McSwEmulationMethod"]:
        """Get emulation (Pythonic accessor)."""
        return self._emulation
        # A data instance to be used for calibration.
        # atpSplitable; atpVariation.
        self._mcParameter: List[McDataInstance] = []

    @property
    def mc_parameter(self) -> List[McDataInstance]:
        """Get mcParameter (Pythonic accessor)."""
        return self._mcParameter
        # A data instance to be used for measurement.
        # atpSplitable; atpVariation.
        self._mcVariable: List[McDataInstance] = []

    @property
    def mc_variable(self) -> List[McDataInstance]:
        """Get mcVariable (Pythonic accessor)."""
        return self._mcVariable
        # Sets of system constant values to be transferred to the MCD system, because
        # the system constants have been with "swCalibrationAccess" = readonly.
        self._measurable: List["SwSystemconstant"] = []

    @property
    def measurable(self) -> List["SwSystemconstant"]:
        """Get measurable (Pythonic accessor)."""
        return self._measurable
        # The rapid prototyping support data belonging to this aggregtion is
        # <<atpSplitable>> case of an already exisiting BSW this description will be
        # added later process, namely at code generation time.
        self._rptSupportData: Optional["RptSupportData"] = None

    @property
    def rpt_support_data(self) -> Optional["RptSupportData"]:
        """Get rptSupportData (Pythonic accessor)."""
        return self._rptSupportData

    @rpt_support_data.setter
    def rpt_support_data(self, value: Optional["RptSupportData"]) -> None:
        """
        Set rptSupportData with validation.

        Args:
            value: The rptSupportData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptSupportData = None
            return

        if not isinstance(value, RptSupportData):
            raise TypeError(
                f"rptSupportData must be RptSupportData or None, got {type(value).__name__}"
            )
        self._rptSupportData = value

    def with_emulation(self, value):
        """
        Set emulation and return self for chaining.

        Args:
            value: The emulation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_emulation("value")
        """
        self.emulation = value  # Use property setter (gets validation)
        return self

    def with_mc_parameter(self, value):
        """
        Set mc_parameter and return self for chaining.

        Args:
            value: The mc_parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_parameter("value")
        """
        self.mc_parameter = value  # Use property setter (gets validation)
        return self

    def with_mc_variable(self, value):
        """
        Set mc_variable and return self for chaining.

        Args:
            value: The mc_variable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_variable("value")
        """
        self.mc_variable = value  # Use property setter (gets validation)
        return self

    def with_measurable(self, value):
        """
        Set measurable and return self for chaining.

        Args:
            value: The measurable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_measurable("value")
        """
        self.measurable = value  # Use property setter (gets validation)
        return self

    def with_mc_data(self, value):
        """
        Set mc_data and return self for chaining.

        Args:
            value: The mc_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_data("value")
        """
        self.mc_data = value  # Use property setter (gets validation)
        return self

    def with_sub_element(self, value):
        """
        Set sub_element and return self for chaining.

        Args:
            value: The sub_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_element("value")
        """
        self.sub_element = value  # Use property setter (gets validation)
        return self

    def with_element_group(self, value):
        """
        Set element_group and return self for chaining.

        Args:
            value: The element_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element_group("value")
        """
        self.element_group = value  # Use property setter (gets validation)
        return self

    def with_sub_function(self, value):
        """
        Set sub_function and return self for chaining.

        Args:
            value: The sub_function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_function("value")
        """
        self.sub_function = value  # Use property setter (gets validation)
        return self

    def with_rte_event_ref(self, value):
        """
        Set rte_event_ref and return self for chaining.

        Args:
            value: The rte_event_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rte_event_ref("value")
        """
        self.rte_event_ref = value  # Use property setter (gets validation)
        return self

    def with_variable_access_instance_ref(self, value):
        """
        Set variable_access_instance_ref and return self for chaining.

        Args:
            value: The variable_access_instance_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_access_instance_ref("value")
        """
        self.variable_access_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_execution(self, value):
        """
        Set execution and return self for chaining.

        Args:
            value: The execution to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_execution("value")
        """
        self.execution = value  # Use property setter (gets validation)
        return self

    def with_mc_data_instance(self, value):
        """
        Set mc_data_instance and return self for chaining.

        Args:
            value: The mc_data_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_data_instance("value")
        """
        self.mc_data_instance = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEmulation(self) -> List["McSwEmulationMethod"]:
        """
        AUTOSAR-compliant getter for emulation.

        Returns:
            The emulation value

        Note:
            Delegates to emulation property (CODING_RULE_V2_00017)
        """
        return self.emulation  # Delegates to property

    def getMcParameter(self) -> List[McDataInstance]:
        """
        AUTOSAR-compliant getter for mcParameter.

        Returns:
            The mcParameter value

        Note:
            Delegates to mc_parameter property (CODING_RULE_V2_00017)
        """
        return self.mc_parameter  # Delegates to property

    def getMcVariable(self) -> List[McDataInstance]:
        """
        AUTOSAR-compliant getter for mcVariable.

        Returns:
            The mcVariable value

        Note:
            Delegates to mc_variable property (CODING_RULE_V2_00017)
        """
        return self.mc_variable  # Delegates to property

    def getMeasurable(self) -> List["SwSystemconstant"]:
        """
        AUTOSAR-compliant getter for measurable.

        Returns:
            The measurable value

        Note:
            Delegates to measurable property (CODING_RULE_V2_00017)
        """
        return self.measurable  # Delegates to property

    def getRptSupportData(self) -> "RptSupportData":
        """
        AUTOSAR-compliant getter for rptSupportData.

        Returns:
            The rptSupportData value

        Note:
            Delegates to rpt_support_data property (CODING_RULE_V2_00017)
        """
        return self.rpt_support_data  # Delegates to property

    def setRptSupportData(self, value: "RptSupportData") -> McSupportData:
        """
        AUTOSAR-compliant setter for rptSupportData with method chaining.

        Args:
            value: The rptSupportData to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_support_data property setter (gets validation automatically)
        """
        self.rpt_support_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_support_data(self, value: Optional["RptSupportData"]) -> McSupportData:
        """
        Set rptSupportData and return self for chaining.

        Args:
            value: The rptSupportData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_support_data("value")
        """
        self.rpt_support_data = value  # Use property setter (gets validation)
        return self



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

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McDataInstance

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
        self._arraySize: Optional[PositiveInteger] = None

    @property
    def array_size(self) -> Optional[PositiveInteger]:
        """Get arraySize (Pythonic accessor)."""
        return self._arraySize

    @array_size.setter
    def array_size(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"arraySize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._arraySize = value
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
        # Use Case: Rapid Prototyping.
        self._mcDataAccess: Optional[McDataAccessDetails] = None

    @property
    def mc_data_access(self) -> Optional[McDataAccessDetails]:
        """Get mcDataAccess (Pythonic accessor)."""
        return self._mcDataAccess

    @mc_data_access.setter
    def mc_data_access(self, value: Optional[McDataAccessDetails]) -> None:
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
        self._resulting: Optional[SwDataDefProps] = None

    @property
    def resulting(self) -> Optional[SwDataDefProps]:
        """Get resulting (Pythonic accessor)."""
        return self._resulting

    @resulting.setter
    def resulting(self, value: Optional[SwDataDefProps]) -> None:
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value
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
                # by the source element.
        # This be used by the final generator to set up addressing scheme.
        # atpVariation.
        self._subElement: List[McDataInstance] = []

    @property
    def sub_element(self) -> List[McDataInstance]:
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

    def getArraySize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: PositiveInteger) -> McDataInstance:
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

    def setDisplayIdentifier(self, value: "McdIdentifier") -> McDataInstance:
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

    def setFlatMapEntry(self, value: "FlatInstanceDescriptor") -> McDataInstance:
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

    def setInstanceIn(self, value: "ImplementationElement") -> McDataInstance:
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

    def getMcDataAccess(self) -> McDataAccessDetails:
        """
        AUTOSAR-compliant getter for mcDataAccess.

        Returns:
            The mcDataAccess value

        Note:
            Delegates to mc_data_access property (CODING_RULE_V2_00017)
        """
        return self.mc_data_access  # Delegates to property

    def setMcDataAccess(self, value: McDataAccessDetails) -> McDataInstance:
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

    def getResulting(self) -> SwDataDefProps:
        """
        AUTOSAR-compliant getter for resulting.

        Returns:
            The resulting value

        Note:
            Delegates to resulting property (CODING_RULE_V2_00017)
        """
        return self.resulting  # Delegates to property

    def setResulting(self, value: SwDataDefProps) -> McDataInstance:
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

    def setResultingRptSw(self, value: "RptSwPrototyping") -> McDataInstance:
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

    def setRole(self, value: "Identifier") -> McDataInstance:
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

    def setRptImplPolicy(self, value: "RptImplPolicy") -> McDataInstance:
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

    def getSubElement(self) -> List[McDataInstance]:
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

    def setSymbol(self, value: "SymbolString") -> McDataInstance:
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

    def with_array_size(self, value: Optional[PositiveInteger]) -> McDataInstance:
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

    def with_display_identifier(self, value: Optional["McdIdentifier"]) -> McDataInstance:
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

    def with_flat_map_entry(self, value: Optional["FlatInstanceDescriptor"]) -> McDataInstance:
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

    def with_instance_in(self, value: Optional["ImplementationElement"]) -> McDataInstance:
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

    def with_mc_data_access(self, value: Optional[McDataAccessDetails]) -> McDataInstance:
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

    def with_resulting(self, value: Optional[SwDataDefProps]) -> McDataInstance:
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

    def with_resulting_rpt_sw(self, value: Optional["RptSwPrototyping"]) -> McDataInstance:
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

    def with_role(self, value: Optional["Identifier"]) -> McDataInstance:
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

    def with_rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> McDataInstance:
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

    def with_symbol(self, value: Optional["SymbolString"]) -> McDataInstance:
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



class McSwEmulationMethodSupport(ARObject):
    """
    This denotes the method used by the RTE to handle the calibration data. It
    is published by the RTE generator and can be used e.g. to generate the
    corresponding emulation method in a Complex Driver. According to the actual
    method given by the category attribute, not all attributes are always
    needed: • double pointered method: only baseReference is mandatory • single
    pointered method: only referenceTable is mandatory • initRam method: only
    elementGroup(s) are mandatory Note: For single/double pointered method the
    group locations are implicitly accessed via the reference table and their
    location can be found from the initial values in the M1 model of the
    respective pointers. Therefore, the description of elementGroups is not
    needed in these cases. Likewise, for double pointered method the reference
    table description can be accessed via the M1 model under baseReference.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McSwEmulationMethodSupport

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 180, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to the base pointer in case of the double-pointered.
        self._baseReference: Optional[RefType] = None

    @property
    def base_reference(self) -> Optional[RefType]:
        """Get baseReference (Pythonic accessor)."""
        return self._baseReference

    @base_reference.setter
    def base_reference(self, value: Optional[RefType]) -> None:
        """
        Set baseReference with validation.

        Args:
            value: The baseReference to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseReference = None
            return

        self._baseReference = value
        # The possible names shall the symbols of the ECU configuration the calibration
                # method of the RTE, and can specific methods.
        self._category: Optional["Identifier"] = None

    @property
    def category(self) -> Optional["Identifier"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["Identifier"]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"category must be Identifier or str or None, got {type(value).__name__}"
            )
        self._category = value
        # Depending on the category, this required to set up the emulation code.
        self._elementGroup: List["McParameterElement"] = []

    @property
    def element_group(self) -> List["McParameterElement"]:
        """Get elementGroup (Pythonic accessor)."""
        return self._elementGroup
        # Refers to the pointer table in case of the single-pointered.
        self._referenceTable: Optional[RefType] = None

    @property
    def reference_table(self) -> Optional[RefType]:
        """Get referenceTable (Pythonic accessor)."""
        return self._referenceTable

    @reference_table.setter
    def reference_table(self, value: Optional[RefType]) -> None:
        """
        Set referenceTable with validation.

        Args:
            value: The referenceTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referenceTable = None
            return

        self._referenceTable = value
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseReference(self) -> RefType:
        """
        AUTOSAR-compliant getter for baseReference.

        Returns:
            The baseReference value

        Note:
            Delegates to base_reference property (CODING_RULE_V2_00017)
        """
        return self.base_reference  # Delegates to property

    def setBaseReference(self, value: RefType) -> McSwEmulationMethodSupport:
        """
        AUTOSAR-compliant setter for baseReference with method chaining.

        Args:
            value: The baseReference to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_reference property setter (gets validation automatically)
        """
        self.base_reference = value  # Delegates to property setter
        return self

    def getCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "Identifier") -> McSwEmulationMethodSupport:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getElementGroup(self) -> List["McParameterElement"]:
        """
        AUTOSAR-compliant getter for elementGroup.

        Returns:
            The elementGroup value

        Note:
            Delegates to element_group property (CODING_RULE_V2_00017)
        """
        return self.element_group  # Delegates to property

    def getReferenceTable(self) -> RefType:
        """
        AUTOSAR-compliant getter for referenceTable.

        Returns:
            The referenceTable value

        Note:
            Delegates to reference_table property (CODING_RULE_V2_00017)
        """
        return self.reference_table  # Delegates to property

    def setReferenceTable(self, value: RefType) -> McSwEmulationMethodSupport:
        """
        AUTOSAR-compliant setter for referenceTable with method chaining.

        Args:
            value: The referenceTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to reference_table property setter (gets validation automatically)
        """
        self.reference_table = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> McSwEmulationMethodSupport:
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

    def with_base_reference(self, value: Optional[RefType]) -> McSwEmulationMethodSupport:
        """
        Set baseReference and return self for chaining.

        Args:
            value: The baseReference to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_reference("value")
        """
        self.base_reference = value  # Use property setter (gets validation)
        return self

    def with_category(self, value: Optional["Identifier"]) -> McSwEmulationMethodSupport:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_reference_table(self, value: Optional[RefType]) -> McSwEmulationMethodSupport:
        """
        Set referenceTable and return self for chaining.

        Args:
            value: The referenceTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reference_table("value")
        """
        self.reference_table = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> McSwEmulationMethodSupport:
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



class McParameterElementGroup(ARObject):
    """
    Denotes a group of calibration parameters which are handled by the RTE as
    one data structure.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McParameterElementGroup

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 181, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to the RAM location of this parameter group.
        # To be the init-RAM method.
        self._ramLocation: Optional[RefType] = None

    @property
    def ram_location(self) -> Optional[RefType]:
        """Get ramLocation (Pythonic accessor)."""
        return self._ramLocation

    @ram_location.setter
    def ram_location(self, value: Optional[RefType]) -> None:
        """
        Set ramLocation with validation.

        Args:
            value: The ramLocation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ramLocation = None
            return

        self._ramLocation = value
        # To used for the init-RAM method.
        self._romLocation: Optional["ParameterData"] = None

    @property
    def rom_location(self) -> Optional["ParameterData"]:
        """Get romLocation (Pythonic accessor)."""
        return self._romLocation

    @rom_location.setter
    def rom_location(self, value: Optional["ParameterData"]) -> None:
        """
        Set romLocation with validation.

        Args:
            value: The romLocation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._romLocation = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"romLocation must be ParameterData or None, got {type(value).__name__}"
            )
        self._romLocation = value
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRamLocation(self) -> RefType:
        """
        AUTOSAR-compliant getter for ramLocation.

        Returns:
            The ramLocation value

        Note:
            Delegates to ram_location property (CODING_RULE_V2_00017)
        """
        return self.ram_location  # Delegates to property

    def setRamLocation(self, value: RefType) -> McParameterElementGroup:
        """
        AUTOSAR-compliant setter for ramLocation with method chaining.

        Args:
            value: The ramLocation to set

        Returns:
            self for method chaining

        Note:
            Delegates to ram_location property setter (gets validation automatically)
        """
        self.ram_location = value  # Delegates to property setter
        return self

    def getRomLocation(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for romLocation.

        Returns:
            The romLocation value

        Note:
            Delegates to rom_location property (CODING_RULE_V2_00017)
        """
        return self.rom_location  # Delegates to property

    def setRomLocation(self, value: "ParameterData") -> McParameterElementGroup:
        """
        AUTOSAR-compliant setter for romLocation with method chaining.

        Args:
            value: The romLocation to set

        Returns:
            self for method chaining

        Note:
            Delegates to rom_location property setter (gets validation automatically)
        """
        self.rom_location = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> McParameterElementGroup:
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

    def with_ram_location(self, value: Optional[RefType]) -> McParameterElementGroup:
        """
        Set ramLocation and return self for chaining.

        Args:
            value: The ramLocation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ram_location("value")
        """
        self.ram_location = value  # Use property setter (gets validation)
        return self

    def with_rom_location(self, value: Optional["ParameterData"]) -> McParameterElementGroup:
        """
        Set romLocation and return self for chaining.

        Args:
            value: The romLocation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rom_location("value")
        """
        self.rom_location = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> McParameterElementGroup:
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



class ImplementationElementInParameterInstanceRef(ARObject):
    """
    that this class follows the pattern of an InstanceRef but is not implemented
    based on the abstract classes because the ImplementationDataType isn’t
    either, especially because ImplementationDataType Element isn’t derived from
    AtpPrototype.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::ImplementationElementInParameterInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 184, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The context for the referred element.
        # xml.
        # sequenceOffset=20.
        self._context: Optional["ParameterData"] = None

    @property
    def context(self) -> Optional["ParameterData"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["ParameterData"]) -> None:
        """
        Set context with validation.

        Args:
            value: The context to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"context must be ParameterData or None, got {type(value).__name__}"
            )
        self._context = value
        # xml.
        # sequenceOffset=30.
        self._target: Optional[AbstractImplementation] = None

    @property
    def target(self) -> Optional[AbstractImplementation]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional[AbstractImplementation]) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"target must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "ParameterData") -> ImplementationElementInParameterInstanceRef:
        """
        AUTOSAR-compliant setter for context with method chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getTarget(self) -> AbstractImplementation:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: AbstractImplementation) -> ImplementationElementInParameterInstanceRef:
        """
        AUTOSAR-compliant setter for target with method chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context(self, value: Optional["ParameterData"]) -> ImplementationElementInParameterInstanceRef:
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: Optional[AbstractImplementation]) -> ImplementationElementInParameterInstanceRef:
        """
        Set target and return self for chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self



class McFunction(ARElement):
    """
    Represents a functional element to be used as input to support measurement
    and calibration. It is used to • assign calibration parameters to a logical
    function • assign measurement variables to a logical function • structure
    functions hierarchically

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McFunction

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 186, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to the set of adjustable data (= calibration in this function.
        self._defCalprmSet: Optional[RefType] = None

    @property
    def def_calprm_set(self) -> Optional[RefType]:
        """Get defCalprmSet (Pythonic accessor)."""
        return self._defCalprmSet

    @def_calprm_set.setter
    def def_calprm_set(self, value: Optional[RefType]) -> None:
        """
        Set defCalprmSet with validation.

        Args:
            value: The defCalprmSet to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defCalprmSet = None
            return

        self._defCalprmSet = value
        self._inMeasurement: Optional[RefType] = None

    @property
    def in_measurement(self) -> Optional[RefType]:
        """Get inMeasurement (Pythonic accessor)."""
        return self._inMeasurement

    @in_measurement.setter
    def in_measurement(self, value: Optional[RefType]) -> None:
        """
        Set inMeasurement with validation.

        Args:
            value: The inMeasurement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inMeasurement = None
            return

        self._inMeasurement = value
        # atpSplitable Set Tags:.
        self._loc: Optional[RefType] = None

    @property
    def loc(self) -> Optional[RefType]:
        """Get loc (Pythonic accessor)."""
        return self._loc

    @loc.setter
    def loc(self, value: Optional[RefType]) -> None:
        """
        Set loc with validation.

        Args:
            value: The loc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._loc = None
            return

        self._loc = value
        self._out: Optional[RefType] = None

    @property
    def out(self) -> Optional[RefType]:
        """Get out (Pythonic accessor)."""
        return self._out

    @out.setter
    def out(self, value: Optional[RefType]) -> None:
        """
        Set out with validation.

        Args:
            value: The out to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._out = None
            return

        self._out = value
        self._refCalprmSet: Optional[RefType] = None

    @property
    def ref_calprm_set(self) -> Optional[RefType]:
        """Get refCalprmSet (Pythonic accessor)."""
        return self._refCalprmSet

    @ref_calprm_set.setter
    def ref_calprm_set(self, value: Optional[RefType]) -> None:
        """
        Set refCalprmSet with validation.

        Args:
            value: The refCalprmSet to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._refCalprmSet = None
            return

        self._refCalprmSet = value
        self._subFunction: List[McFunction] = []

    @property
    def sub_function(self) -> List[McFunction]:
        """Get subFunction (Pythonic accessor)."""
        return self._subFunction

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefCalprmSet(self) -> RefType:
        """
        AUTOSAR-compliant getter for defCalprmSet.

        Returns:
            The defCalprmSet value

        Note:
            Delegates to def_calprm_set property (CODING_RULE_V2_00017)
        """
        return self.def_calprm_set  # Delegates to property

    def setDefCalprmSet(self, value: RefType) -> McFunction:
        """
        AUTOSAR-compliant setter for defCalprmSet with method chaining.

        Args:
            value: The defCalprmSet to set

        Returns:
            self for method chaining

        Note:
            Delegates to def_calprm_set property setter (gets validation automatically)
        """
        self.def_calprm_set = value  # Delegates to property setter
        return self

    def getInMeasurement(self) -> RefType:
        """
        AUTOSAR-compliant getter for inMeasurement.

        Returns:
            The inMeasurement value

        Note:
            Delegates to in_measurement property (CODING_RULE_V2_00017)
        """
        return self.in_measurement  # Delegates to property

    def setInMeasurement(self, value: RefType) -> McFunction:
        """
        AUTOSAR-compliant setter for inMeasurement with method chaining.

        Args:
            value: The inMeasurement to set

        Returns:
            self for method chaining

        Note:
            Delegates to in_measurement property setter (gets validation automatically)
        """
        self.in_measurement = value  # Delegates to property setter
        return self

    def getLoc(self) -> RefType:
        """
        AUTOSAR-compliant getter for loc.

        Returns:
            The loc value

        Note:
            Delegates to loc property (CODING_RULE_V2_00017)
        """
        return self.loc  # Delegates to property

    def setLoc(self, value: RefType) -> McFunction:
        """
        AUTOSAR-compliant setter for loc with method chaining.

        Args:
            value: The loc to set

        Returns:
            self for method chaining

        Note:
            Delegates to loc property setter (gets validation automatically)
        """
        self.loc = value  # Delegates to property setter
        return self

    def getOut(self) -> RefType:
        """
        AUTOSAR-compliant getter for out.

        Returns:
            The out value

        Note:
            Delegates to out property (CODING_RULE_V2_00017)
        """
        return self.out  # Delegates to property

    def setOut(self, value: RefType) -> McFunction:
        """
        AUTOSAR-compliant setter for out with method chaining.

        Args:
            value: The out to set

        Returns:
            self for method chaining

        Note:
            Delegates to out property setter (gets validation automatically)
        """
        self.out = value  # Delegates to property setter
        return self

    def getRefCalprmSet(self) -> RefType:
        """
        AUTOSAR-compliant getter for refCalprmSet.

        Returns:
            The refCalprmSet value

        Note:
            Delegates to ref_calprm_set property (CODING_RULE_V2_00017)
        """
        return self.ref_calprm_set  # Delegates to property

    def setRefCalprmSet(self, value: RefType) -> McFunction:
        """
        AUTOSAR-compliant setter for refCalprmSet with method chaining.

        Args:
            value: The refCalprmSet to set

        Returns:
            self for method chaining

        Note:
            Delegates to ref_calprm_set property setter (gets validation automatically)
        """
        self.ref_calprm_set = value  # Delegates to property setter
        return self

    def getSubFunction(self) -> List[McFunction]:
        """
        AUTOSAR-compliant getter for subFunction.

        Returns:
            The subFunction value

        Note:
            Delegates to sub_function property (CODING_RULE_V2_00017)
        """
        return self.sub_function  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_def_calprm_set(self, value: Optional[RefType]) -> McFunction:
        """
        Set defCalprmSet and return self for chaining.

        Args:
            value: The defCalprmSet to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_def_calprm_set("value")
        """
        self.def_calprm_set = value  # Use property setter (gets validation)
        return self

    def with_in_measurement(self, value: Optional[RefType]) -> McFunction:
        """
        Set inMeasurement and return self for chaining.

        Args:
            value: The inMeasurement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_in_measurement("value")
        """
        self.in_measurement = value  # Use property setter (gets validation)
        return self

    def with_loc(self, value: Optional[RefType]) -> McFunction:
        """
        Set loc and return self for chaining.

        Args:
            value: The loc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_loc("value")
        """
        self.loc = value  # Use property setter (gets validation)
        return self

    def with_out(self, value: Optional[RefType]) -> McFunction:
        """
        Set out and return self for chaining.

        Args:
            value: The out to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_out("value")
        """
        self.out = value  # Use property setter (gets validation)
        return self

    def with_ref_calprm_set(self, value: Optional[RefType]) -> McFunction:
        """
        Set refCalprmSet and return self for chaining.

        Args:
            value: The refCalprmSet to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ref_calprm_set("value")
        """
        self.ref_calprm_set = value  # Use property setter (gets validation)
        return self



class McDataAccessDetails(ARObject):
    """
    that the SwComponentPrototype, the RunnableEntity and the
    VariableDataPrototype are implicitly given be the referred instances of
    RTEEvent and VariableAccess.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McDataAccessDetails

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 195, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: RteEventInEcuInstance.
        self._rteEventRef: List["RTEEvent"] = []

    @property
    def rte_event_ref(self) -> List["RTEEvent"]:
        """Get rteEventRef (Pythonic accessor)."""
        return self._rteEventRef
        # by: VariableAccessInEcu.
        self._variableAccessInstanceRef: List["VariableAccess"] = []

    @property
    def variable_access_instance_ref(self) -> List["VariableAccess"]:
        """Get variableAccessInstanceRef (Pythonic accessor)."""
        return self._variableAccessInstanceRef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRteEventRef(self) -> List["RTEEvent"]:
        """
        AUTOSAR-compliant getter for rteEventRef.

        Returns:
            The rteEventRef value

        Note:
            Delegates to rte_event_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_ref  # Delegates to property

    def getVariableAccessInstanceRef(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for variableAccessInstanceRef.

        Returns:
            The variableAccessInstanceRef value

        Note:
            Delegates to variable_access_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.variable_access_instance_ref  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RoleBasedMcDataAssignment(ARObject):
    """
    This meta-class allows to define links that specify logical relationships
    between single McDataInstances. The details on the existence and semantics
    of such links are not standardized. Possible Use Case: Rapid Prototyping
    solutions in which additional communication buffers and switches are
    implemented in the RTE that allow to switch between the usage of the
    original and the bypass buffers. The different buffers and the switch can be
    represented by McDataInstances (in order to be accessed by MC tools) which
    have relationships to each other.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RoleBasedMcDataAssignment

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 329, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Determines the executionContext in which the McData describing a local (e.
        # g Task-Local) buffer of a is valid.
        self._execution: List["RptExecutionContext"] = []

    @property
    def execution(self) -> List["RptExecutionContext"]:
        """Get execution (Pythonic accessor)."""
        return self._execution
        # The target of the assignment.
        self._mcDataInstance: List[McDataInstance] = []

    @property
    def mc_data_instance(self) -> List[McDataInstance]:
        """Get mcDataInstance (Pythonic accessor)."""
        return self._mcDataInstance
        # Shall be used to specify the role of the assigned data relation to the
        # instance that owns the roles of the RoleBasedMcData are:.
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecution(self) -> List["RptExecutionContext"]:
        """
        AUTOSAR-compliant getter for execution.

        Returns:
            The execution value

        Note:
            Delegates to execution property (CODING_RULE_V2_00017)
        """
        return self.execution  # Delegates to property

    def getMcDataInstance(self) -> List[McDataInstance]:
        """
        AUTOSAR-compliant getter for mcDataInstance.

        Returns:
            The mcDataInstance value

        Note:
            Delegates to mc_data_instance property (CODING_RULE_V2_00017)
        """
        return self.mc_data_instance  # Delegates to property

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> RoleBasedMcDataAssignment:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional["Identifier"]) -> RoleBasedMcDataAssignment:
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
