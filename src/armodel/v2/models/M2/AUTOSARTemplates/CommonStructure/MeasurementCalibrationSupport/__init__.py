from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class McSupportData(ARObject):
    """
    Root element for all measurement and calibration support data related to one
    Implementation artifact on an ECU. There shall be one such element related
    to the RTE implementation (if it owns MC data) and a separate one for each
    module or component, which owns private MC data.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport

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
        self._mcParameter: List["McDataInstance"] = []

    @property
    def mc_parameter(self) -> List["McDataInstance"]:
        """Get mcParameter (Pythonic accessor)."""
        return self._mcParameter
        # A data instance to be used for measurement.
        # atpSplitable; atpVariation.
        self._mcVariable: List["McDataInstance"] = []

    @property
    def mc_variable(self) -> List["McDataInstance"]:
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

    def getMcParameter(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for mcParameter.

        Returns:
            The mcParameter value

        Note:
            Delegates to mc_parameter property (CODING_RULE_V2_00017)
        """
        return self.mc_parameter  # Delegates to property

    def getMcVariable(self) -> List["McDataInstance"]:
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

    def setRptSupportData(self, value: "RptSupportData") -> "McSupportData":
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

    def with_rpt_support_data(self, value: Optional["RptSupportData"]) -> "McSupportData":
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

from typing import (
    List,
    Union,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class McDataInstance(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport
    Represents an MC (Measurement and Calibration) data instance in AUTOSAR.
    Defines an instance of MC data that can be accessed or modified.
    """


    def __init__(self) -> None:
        """
        Initializes the McDataInstance with default values.
        """
        super().__init__()
        self.dataAccessDetails: List[RefType] = []
        self.dataRef: Union[Union[RefType, None] , None] = None

    def addDataAccessDetail(self, ref: RefType) -> "McDataInstance":
        """
        Adds a data access detail reference.

        Args:
            ref: The data access detail reference to add

        Returns:
            self for method chaining
        """
        self.dataAccessDetails.append(ref)
        return self

    def getDataAccessDetails(self) -> List[RefType]:
        """
        Gets the list of data access detail references.

        Returns:
            List of data access detail references
        """
        return self.dataAccessDetails

    def getDataRef(self) -> Union[RefType, None]:
        """
        Gets the data reference.

        Returns:
            Reference to the data
        """
        return self.dataRef

    def setDataRef(self, value: RefType) -> "McDataInstance":
        """
        Sets the data reference.

        Args:
            value: The data reference to set

        Returns:
            self for method chaining
        """
        self.dataRef = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class McSwEmulationMethodSupport(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport
    Represents MC (Measurement and Calibration) software emulation method support in AUTOSAR.
    Defines support for software emulation methods in measurement and calibration.
    """


    def __init__(self) -> None:
        """
        Initializes the McSwEmulationMethodSupport with default values.
        """
        super().__init__()
        self.emulationMethodName: Union[str, None] = None

    def getEmulationMethodName(self) -> Union[str, None]:
        """
        Gets the emulation method name.

        Returns:
            String representing the emulation method name
        """
        return self.emulationMethodName

    def setEmulationMethodName(self, value: str) -> "McSwEmulationMethodSupport":
        """
        Sets the emulation method name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.emulationMethodName = value
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class McParameterElementGroup(ARObject):
    """
    Denotes a group of calibration parameters which are handled by the RTE as
    one data structure.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 181, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to the RAM location of this parameter group.
        # To be the init-RAM method.
        self._ramLocation: RefType = None

    @property
    def ram_location(self) -> RefType:
        """Get ramLocation (Pythonic accessor)."""
        return self._ramLocation

    @ram_location.setter
    def ram_location(self, value: RefType) -> None:
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
        # Refers to the ROM location of this parameter group.
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
        # Assigns a name to this element.
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

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
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

    def setRamLocation(self, value: RefType) -> "McParameterElementGroup":
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

    def setRomLocation(self, value: "ParameterData") -> "McParameterElementGroup":
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

    def setShortLabel(self, value: "Identifier") -> "McParameterElementGroup":
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

    def with_ram_location(self, value: Optional[RefType]) -> "McParameterElementGroup":
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

    def with_rom_location(self, value: Optional["ParameterData"]) -> "McParameterElementGroup":
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

    def with_short_label(self, value: Optional["Identifier"]) -> "McParameterElementGroup":
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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ImplementationElementInParameterInstanceRef(ARObject):
    """
    that this class follows the pattern of an InstanceRef but is not implemented
    based on the abstract classes because the ImplementationDataType isn’t
    either, especially because ImplementationDataType Element isn’t derived from
    AtpPrototype.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport

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
        # The referred data element.
        # xml.
        # sequenceOffset=30.
        self._target: Optional["AbstractImplementation"] = None

    @property
    def target(self) -> Optional["AbstractImplementation"]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional["AbstractImplementation"]) -> None:
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

    def setContext(self, value: "ParameterData") -> "ImplementationElementInParameterInstanceRef":
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

    def getTarget(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "AbstractImplementation") -> "ImplementationElementInParameterInstanceRef":
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

    def with_context(self, value: Optional["ParameterData"]) -> "ImplementationElementInParameterInstanceRef":
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

    def with_target(self, value: Optional["AbstractImplementation"]) -> "ImplementationElementInParameterInstanceRef":
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

from typing import (
    List,
    Union,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class McFunction(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport
    Represents an MC (Measurement and Calibration) function in AUTOSAR.
    Defines a function that can be used for measurement and calibration purposes.
    """


    def __init__(self) -> None:
        """
        Initializes the McFunction with default values.
        """
        super().__init__()
        self.dataRefs: List[RefType] = []
        self.functionName: Union[str, None] = None

    def addDataRef(self, ref: RefType):
        """
        Adds a data reference to this MC function.

        Args:
            ref: The data reference to add

        Returns:
            self for method chaining
        """
        self.dataRefs.append(ref)
        return self

    def getDataRefs(self) -> List[RefType]:
        """
        Gets the list of data references.

        Returns:
            List of data references
        """
        return self.dataRefs

    def getFunctionName(self) -> Union[str, None]:
        """
        Gets the function name.

        Returns:
            String representing the function name
        """
        return self.functionName

    def setFunctionName(self, value: str) -> "McFunction":
        """
        Sets the function name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.functionName = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class McDataAccessDetails(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport
    Represents MC (Measurement and Calibration) data access details in AUTOSAR.
    Defines details about how MC data can be accessed.
    """


    def __init__(self) -> None:
        """
        Initializes the McDataAccessDetails with default values.
        """
        super().__init__()
        self.accessType: Union[str, None] = None
        self.address: Union[str, None] = None

    def getAccessType(self) -> Union[str, None]:
        """
        Gets the access type.

        Returns:
            String representing the access type
        """
        return self.accessType

    def setAccessType(self, value: str) -> "McDataAccessDetails":
        """
        Sets the access type.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.accessType = value
        return self

    def getAddress(self) -> Union[str, None]:
        """
        Gets the address.

        Returns:
            String representing the address
        """
        return self.address

    def setAddress(self, value: str) -> "McDataAccessDetails":
        """
        Sets the address.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.address = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RoleBasedMcDataAssignment(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport
    Represents a role-based MC (Measurement and Calibration) data assignment in AUTOSAR.
    Defines assignment of MC data based on roles.
    """


    def __init__(self) -> None:
        """
        Initializes the RoleBasedMcDataAssignment with default values.
        """
        super().__init__()
        self.dataRef: Union[Union[RefType, None] , None] = None
        self.role: Union[str, None] = None

    def getDataRef(self) -> Union[RefType, None]:
        """
        Gets the data reference.

        Returns:
            Reference to the data
        """
        return self.dataRef

    def setDataRef(self, value: RefType) -> "RoleBasedMcDataAssignment":
        """
        Sets the data reference.

        Args:
            value: The data reference to set

        Returns:
            self for method chaining
        """
        self.dataRef = value
        return self

    def getRole(self) -> Union[str, None]:
        """
        Gets the role.

        Returns:
            String representing the role
        """
        return self.role

    def setRole(self, value: str) -> "RoleBasedMcDataAssignment":
        """
        Sets the role.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.role = value
        return self


__all__ = [
    "McSupportData",
    "McDataInstance",
    "McSwEmulationMethodSupport",
    "McParameterElementGroup",
    "ImplementationElementInParameterInstanceRef",
    "McFunction",
    "McDataAccessDetails",
    "RoleBasedMcDataAssignment",
]
