"""
This module contains classes for representing AUTOSAR measurement and calibration
support data (MC support data) in software component and BSW module templates.
"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, McdIdentifier, PositiveInteger, RefType, SymbolString
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptSupportData, RptSwPrototypingAccess
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptImplPolicy


class McDataAccessDetails(ARObject):
    """
    Represents MC (Measurement and Calibration) data access details in AUTOSAR.
    Defines details about how MC data can be accessed.
    """

    # McDataAccessDetails method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getAccessType                [x] impl  [x] docstring  [ ] test
    # [ ] setAccessType                [x] impl  [x] docstring  [ ] test
    # [ ] getAddress                   [x] impl  [x] docstring  [ ] test
    # [ ] setAddress                   [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the McDataAccessDetails with default values.
        """
        super().__init__()
        self.accessType: str = None
        self.address: str = None

    def getAccessType(self) -> str:
        """
        Gets the access type.

        Returns:
            String representing the access type
        """
        return self.accessType

    def setAccessType(self, value: str):
        """
        Sets the access type.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.accessType = value
        return self

    def getAddress(self) -> str:
        """
        Gets the address.

        Returns:
            String representing the address
        """
        return self.address

    def setAddress(self, value: str):
        """
        Sets the address.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.address = value
        return self


class McParameterElementGroup(ARObject):
    """
    Represents an MC (Measurement and Calibration) parameter element group in AUTOSAR.
    Defines a group of parameter elements for measurement and calibration purposes.
    """

    # McParameterElementGroup method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] addParameterRef              [x] impl  [x] docstring  [ ] test
    # [ ] getParameterRefs             [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the McParameterElementGroup with default values.
        """
        super().__init__()
        self.parameterRefs: List[RefType] = []

    def addParameterRef(self, ref: RefType):
        """
        Adds a parameter reference to this MC parameter element group.

        Args:
            ref: The parameter reference to add

        Returns:
            self for method chaining
        """
        self.parameterRefs.append(ref)
        return self

    def getParameterRefs(self) -> List[RefType]:
        """
        Gets the list of parameter references.

        Returns:
            List of parameter references
        """
        return self.parameterRefs


class McSwEmulationMethodSupport(ARObject):
    """
    Represents MC (Measurement and Calibration) software emulation method support in AUTOSAR.
    Defines support for software emulation methods in measurement and calibration.
    """

    # McSwEmulationMethodSupport method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getEmulationMethodName       [x] impl  [x] docstring  [ ] test
    # [ ] setEmulationMethodName       [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the McSwEmulationMethodSupport with default values.
        """
        super().__init__()
        self.emulationMethodName: str = None

    def getEmulationMethodName(self) -> str:
        """
        Gets the emulation method name.

        Returns:
            String representing the emulation method name
        """
        return self.emulationMethodName

    def setEmulationMethodName(self, value: str):
        """
        Sets the emulation method name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.emulationMethodName = value
        return self


class ImplementationElementInParameterInstanceRef(RefType):
    """
    Represents a reference to an implementation element in a parameter instance.
    Used for referencing implementation elements within parameter instances in AUTOSAR models.
    """

    # ImplementationElementInParameterInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the ImplementationElementInParameterInstanceRef with default values.
        """
        super().__init__()


class McFunction(ARObject):
    """
    Represents an MC (Measurement and Calibration) function in AUTOSAR.
    Defines a function that can be used for measurement and calibration purposes.
    """

    # McFunction method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] addDataRef                   [x] impl  [x] docstring  [ ] test
    # [ ] getDataRefs                  [x] impl  [x] docstring  [ ] test
    # [ ] getFunctionName              [x] impl  [x] docstring  [ ] test
    # [ ] setFunctionName              [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the McFunction with default values.
        """
        super().__init__()
        self.dataRefs: List[RefType] = []
        self.functionName: str = None

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

    def getFunctionName(self) -> str:
        """
        Gets the function name.

        Returns:
            String representing the function name
        """
        return self.functionName

    def setFunctionName(self, value: str):
        """
        Sets the function name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.functionName = value
        return self


class RoleBasedMcDataAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular McDataInstance, enabling the reuse of data in different contexts of rapid prototyping.
    """

    # RoleBasedMcDataAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.55, p.195
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getExecutionContextRef       [x] impl  [x] docstring  [x] test
    # [x] setExecutionContextRef       [x] impl  [x] docstring  [x] test
    # [x] getMcDataInstanceRef         [x] impl  [x] docstring  [x] test
    # [x] setMcDataInstanceRef         [x] impl  [x] docstring  [x] test
    # [x] getRole                      [x] impl  [x] docstring  [x] test
    # [x] setRole                      [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the RoleBasedMcDataAssignment.
        """
        super().__init__()

        # Reference to the execution context the assigned data instance is used in.
        self.executionContextRef: Optional[RefType] = None

        # Reference to the McDataInstance the role is assigned to.
        self.mcDataInstanceRef: Optional[RefType] = None

        # Shall be used to specify the role of the assigned data instance in relation to the instance that owns the assignment.
        self.role: Optional[Identifier] = None

    def getExecutionContextRef(self) -> Optional[RefType]:
        """
        Gets the reference to the execution context the assigned data instance is used in.

        Returns:
            RefType referencing the execution context, or None if not set
        """
        return self.executionContextRef

    def setExecutionContextRef(self, value: Optional[RefType]) -> "RoleBasedMcDataAssignment":
        """
        Sets the reference to the execution context the assigned data instance is used in.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The execution context reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.executionContextRef = value
        return self

    def getMcDataInstanceRef(self) -> Optional[RefType]:
        """
        Gets the reference to the McDataInstance the role is assigned to.

        Returns:
            RefType referencing the McDataInstance, or None if not set
        """
        return self.mcDataInstanceRef

    def setMcDataInstanceRef(self, value: Optional[RefType]) -> "RoleBasedMcDataAssignment":
        """
        Sets the reference to the McDataInstance the role is assigned to.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The McDataInstance reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataInstanceRef = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        Gets the role of the assigned data instance in relation to the instance that owns the assignment.

        Returns:
            Identifier representing the role, or None if not set
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "RoleBasedMcDataAssignment":
        """
        Sets the role of the assigned data instance in relation to the instance that owns the assignment.
        A None value is a no-op and does not overwrite an existing role.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self


class McDataInstance(Identifiable):
    """
    Describes the specific properties of one data instance in order to support measurement and/or calibration of this data instance. The most important attributes are: • Its shortName is copied from the ECU Flat map (if applicable) and will be used as identifier and for display by the MC system. • The category is copied from the corresponding data type (ApplicationDataType if defined, otherwise ImplementationDataType) as far as applicable. • The symbol is the one used in the programming language. It will be used to find out the actual memory address by the final generation tool with the help of linker generated information. It is assumed that in the M1 model this part and all the aggregated and referred elements (with the exception of the Flat Map and the references from ImplementationElementInParameterInstanceRef and McAccessDetails) are completely generated from "upstream" information. This means, that even if an element like e.g. a CompuMethod is only used via reference here, it will be copied into the M1 artifact which holds the complete McSupportData for a given Implementation.
    """

    # McDataInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.4, p.177
    # Spec verified: R23-11
    # [x] __init__                        [x] impl  [x] docstring  [x] test
    # [x] getArraySize                    [x] impl  [x] docstring  [x] test
    # [x] setArraySize                    [x] impl  [x] docstring  [x] test
    # [x] getDisplayIdentifier            [x] impl  [x] docstring  [x] test
    # [x] setDisplayIdentifier            [x] impl  [x] docstring  [x] test
    # [x] getFlatMapEntryRef              [x] impl  [x] docstring  [x] test
    # [x] setFlatMapEntryRef              [x] impl  [x] docstring  [x] test
    # [x] getInstanceInMemory             [x] impl  [x] docstring  [x] test
    # [x] setInstanceInMemory             [x] impl  [x] docstring  [x] test
    # [x] getMcDataAccessDetails          [x] impl  [x] docstring  [x] test
    # [x] setMcDataAccessDetails          [x] impl  [x] docstring  [x] test
    # [x] addMcDataAssignment             [x] impl  [x] docstring  [x] test
    # [x] getMcDataAssignments            [x] impl  [x] docstring  [x] test
    # [x] getResultingProperties          [x] impl  [x] docstring  [x] test
    # [x] setResultingProperties          [x] impl  [x] docstring  [x] test
    # [x] getResultingRptSwPrototypingAccess [x] impl [x] docstring  [x] test
    # [x] setResultingRptSwPrototypingAccess [x] impl [x] docstring  [x] test
    # [x] getRole                         [x] impl  [x] docstring  [x] test
    # [x] setRole                         [x] impl  [x] docstring  [x] test
    # [x] getRptImplPolicy                [x] impl  [x] docstring  [x] test
    # [x] setRptImplPolicy                [x] impl  [x] docstring  [x] test
    # [x] createSubElement                [x] impl  [x] docstring  [x] test
    # [x] getSubElements                  [x] impl  [x] docstring  [x] test
    # [x] getSymbol                       [x] impl  [x] docstring  [x] test
    # [x] setSymbol                       [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the McDataInstance with a parent and short name.

        Args:
            parent: The parent ARObject that contains this data instance
            short_name: The unique short name of this data instance
        """
        super().__init__(parent, short_name)

        # Array size, if this McDataInstance represents an array.
        self.arraySize: Optional[PositiveInteger] = None

        # Optional identifier to be used by an MCD system to identify this data instance.
        self.displayIdentifier: Optional[McdIdentifier] = None

        # Reference to the FlatInstanceDescriptor the data instance is linked to.
        self.flatMapEntryRef: Optional[RefType] = None

        # Reference to the implementation element in parameter instance representing the data instance in memory.
        self.instanceInMemory: Optional[ImplementationElementInParameterInstanceRef] = None

        # Details of the access to the data instance.
        self.mcDataAccessDetails: Optional[McDataAccessDetails] = None

        # Role-based assignments of MC data to this data instance.
        self.mcDataAssignments: List[RoleBasedMcDataAssignment] = []

        # Resulting properties of the data instance.
        self.resultingProperties: Optional[SwDataDefProps] = None

        # Resulting rapid prototyping access of the data instance.
        self.resultingRptSwPrototypingAccess: Optional[RptSwPrototypingAccess] = None

        # An optional attribute to be used for additional information on the role of this data instance, for example in the context of rapid prototyping.
        self.role: Optional[Identifier] = None

        # Describes the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.
        self.rptImplPolicy: Optional[RptImplPolicy] = None

        # This relation indicates, that the target element is part of a "struct" which is given by the source element. This information will be used by the final generator to set up the correct addressing scheme.
        self.subElements: List[McDataInstance] = []

        # This String is used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file) . It shall be the name of the element in the programming language such that it can be identified in linker generated information. In case the McDataInstance is part of composite data in the programming language, the symbol String may include parts denoting the element context, unless the context is given by the symbol attribute of an enclosing McDataInstance. This means in particular for the C language that the "." character shall be used as a separator between the name of a "struct" variable the name of one of its elements. The symbol can differ from the shortName in case of generated C data declarations. It is an optional attribute since it may be missing in case the instance represents an element (e.g. a single array element) which has no name in the linker map.
        self.symbol: Optional[SymbolString] = None

    def getArraySize(self) -> Optional[PositiveInteger]:
        """
        Gets the array size of this data instance.

        Returns:
            PositiveInteger representing the array size, or None if not set
        """
        return self.arraySize

    def setArraySize(self, value: Optional[PositiveInteger]) -> "McDataInstance":
        """
        Sets the array size of this data instance.
        A None value is a no-op and does not overwrite an existing size.

        Args:
            value: The array size to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arraySize = value
        return self

    def getDisplayIdentifier(self) -> Optional[McdIdentifier]:
        """
        Gets the optional identifier to be used by an MCD system to identify this data instance.

        Returns:
            McdIdentifier to be used by the MCD system, or None if not set
        """
        return self.displayIdentifier

    def setDisplayIdentifier(self, value: Optional[McdIdentifier]) -> "McDataInstance":
        """
        Sets the optional identifier to be used by an MCD system to identify this data instance.
        A None value is a no-op and does not overwrite an existing identifier.

        Args:
            value: The McdIdentifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.displayIdentifier = value
        return self

    def getFlatMapEntryRef(self) -> Optional[RefType]:
        """
        Gets the reference to the FlatInstanceDescriptor the data instance is linked to.

        Returns:
            RefType referencing the flat map entry, or None if not set
        """
        return self.flatMapEntryRef

    def setFlatMapEntryRef(self, value: Optional[RefType]) -> "McDataInstance":
        """
        Sets the reference to the FlatInstanceDescriptor the data instance is linked to.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The flat map entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.flatMapEntryRef = value
        return self

    def getInstanceInMemory(self) -> Optional[ImplementationElementInParameterInstanceRef]:
        """
        Gets the reference to the implementation element in parameter instance representing the data instance in memory.

        Returns:
            ImplementationElementInParameterInstanceRef referencing the data instance in memory, or None if not set
        """
        return self.instanceInMemory

    def setInstanceInMemory(self, value: Optional[ImplementationElementInParameterInstanceRef]) -> "McDataInstance":
        """
        Sets the reference to the implementation element in parameter instance representing the data instance in memory.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The instance in memory reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.instanceInMemory = value
        return self

    def getMcDataAccessDetails(self) -> Optional[McDataAccessDetails]:
        """
        Gets the details of the access to the data instance.

        Returns:
            McDataAccessDetails instance, or None if not set
        """
        return self.mcDataAccessDetails

    def setMcDataAccessDetails(self, value: Optional[McDataAccessDetails]) -> "McDataInstance":
        """
        Sets the details of the access to the data instance.
        A None value is a no-op and does not overwrite existing access details.

        Args:
            value: The McDataAccessDetails to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataAccessDetails = value
        return self

    def addMcDataAssignment(self, value: Optional[RoleBasedMcDataAssignment]) -> "McDataInstance":
        """
        Adds a role-based MC data assignment to this data instance.
        A None value is a no-op and does not append anything.

        Args:
            value: The role-based MC data assignment to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataAssignments.append(value)
        return self

    def getMcDataAssignments(self) -> List[RoleBasedMcDataAssignment]:
        """
        Gets the role-based MC data assignments aggregated by this data instance.

        Returns:
            List of RoleBasedMcDataAssignment instances
        """
        return self.mcDataAssignments

    def getResultingProperties(self) -> Optional[SwDataDefProps]:
        """
        Gets the resulting properties of the data instance.

        Returns:
            SwDataDefProps instance, or None if not set
        """
        return self.resultingProperties

    def setResultingProperties(self, value: Optional[SwDataDefProps]) -> "McDataInstance":
        """
        Sets the resulting properties of the data instance.
        A None value is a no-op and does not overwrite existing properties.

        Args:
            value: The SwDataDefProps to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.resultingProperties = value
        return self

    def getResultingRptSwPrototypingAccess(self) -> Optional[RptSwPrototypingAccess]:
        """
        Gets the resulting rapid prototyping access of the data instance.

        Returns:
            RptSwPrototypingAccess instance, or None if not set
        """
        return self.resultingRptSwPrototypingAccess

    def setResultingRptSwPrototypingAccess(self, value: Optional[RptSwPrototypingAccess]) -> "McDataInstance":
        """
        Sets the resulting rapid prototyping access of the data instance.
        A None value is a no-op and does not overwrite existing access.

        Args:
            value: The RptSwPrototypingAccess to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.resultingRptSwPrototypingAccess = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        Gets the additional information on the role of this data instance, for example in the context of rapid prototyping.

        Returns:
            Identifier representing the role, or None if not set
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "McDataInstance":
        """
        Sets the additional information on the role of this data instance, for example in the context of rapid prototyping.
        A None value is a no-op and does not overwrite an existing role.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self

    def getRptImplPolicy(self) -> Optional[RptImplPolicy]:
        """
        Gets the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.

        Returns:
            RptImplPolicy instance, or None if not set
        """
        return self.rptImplPolicy

    def setRptImplPolicy(self, value: Optional[RptImplPolicy]) -> "McDataInstance":
        """
        Sets the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.
        A None value is a no-op and does not overwrite an existing policy.

        Args:
            value: The RptImplPolicy to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptImplPolicy = value
        return self

    def createSubElement(self, short_name: str) -> "McDataInstance":
        """
        Creates a McDataInstance sub element and adds it to this data instance.
        If a sub element with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new sub element

        Returns:
            The created (or existing) McDataInstance
        """
        for sub_element in self.subElements:
            if sub_element.short_name == short_name:
                return sub_element
        sub_element = McDataInstance(self, short_name)
        self.subElements.append(sub_element)
        return sub_element

    def getSubElements(self) -> List["McDataInstance"]:
        """
        Gets the sub elements aggregated by this data instance.

        Returns:
            List of McDataInstance sub elements
        """
        return self.subElements

    def getSymbol(self) -> Optional[SymbolString]:
        """
        Gets the symbol used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file).

        Returns:
            SymbolString representing the symbol, or None if not set
        """
        return self.symbol

    def setSymbol(self, value: Optional[SymbolString]) -> "McDataInstance":
        """
        Sets the symbol used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file).
        A None value is a no-op and does not overwrite an existing symbol.

        Args:
            value: The SymbolString to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbol = value
        return self


class McSupportData(ARObject):
    """
    Root element for all measurement and calibration support data related to one Implementation artifact on an ECU. There shall be one such element related to the RTE implementation (if it owns MC data) and a separate one for each module or component, which owns private MC data.
    """

    # McSupportData method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.1, p.172
    # Spec verified: R23-11
    # [x] __init__                              [x] impl  [x] docstring  [x] test
    # [x] addEmulationSupport                   [x] impl  [x] docstring  [x] test
    # [x] getEmulationSupports                  [x] impl  [x] docstring  [x] test
    # [x] createMcParameterInstance             [x] impl  [x] docstring  [x] test
    # [x] getMcParameterInstances               [x] impl  [x] docstring  [x] test
    # [x] createMcVariableInstance              [x] impl  [x] docstring  [x] test
    # [x] getMcVariableInstances                [x] impl  [x] docstring  [x] test
    # [x] addMeasurableSystemConstantValuesRef  [x] impl  [x] docstring  [x] test
    # [x] getMeasurableSystemConstantValuesRefs [x] impl  [x] docstring  [x] test
    # [x] getRptSupportData                     [x] impl  [x] docstring  [x] test
    # [x] setRptSupportData                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the McSupportData with default values.
        """
        super().__init__()

        # Describes the calibration method used by the RTE. This information is not needed for A2L generation, but to setup software emulation in the ECU.
        self.emulationSupports: List[McSwEmulationMethodSupport] = []

        # A data instance to be used for calibration.
        self.mcParameterInstances: List[McDataInstance] = []

        # A data instance to be used for measurement.
        self.mcVariableInstances: List[McDataInstance] = []

        # Sets of system constant values to be transferred to the MCD system, because the system constants have been specified with "swCalibrationAccess" = readonly.
        self.measurableSystemConstantValuesRefs: List[RefType] = []

        # The rapid prototyping support data belonging to this implementation. The aggregtion is <<atpSplitable>> because in case of an already exisiting BSW Implementation model, this description will be added later in the process, namely at code generation time.
        self.rptSupportData: Optional[RptSupportData] = None

    def addEmulationSupport(self, value: Optional[McSwEmulationMethodSupport]) -> "McSupportData":
        """
        Adds an emulation support to this MC support data.
        A None value is a no-op and does not append anything.

        Args:
            value: The emulation support to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.emulationSupports.append(value)
        return self

    def getEmulationSupports(self) -> List[McSwEmulationMethodSupport]:
        """
        Gets the emulation supports aggregated by this MC support data.

        Returns:
            List of McSwEmulationMethodSupport instances
        """
        return self.emulationSupports

    def createMcParameterInstance(self, short_name: str) -> McDataInstance:
        """
        Creates a McDataInstance for calibration and adds it to this MC support data.
        If a data instance with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new calibration data instance

        Returns:
            The created (or existing) McDataInstance
        """
        for instance in self.mcParameterInstances:
            if instance.short_name == short_name:
                return instance
        instance = McDataInstance(self, short_name)
        self.mcParameterInstances.append(instance)
        return instance

    def getMcParameterInstances(self) -> List[McDataInstance]:
        """
        Gets the calibration data instances aggregated by this MC support data.

        Returns:
            List of McDataInstance instances used for calibration
        """
        return self.mcParameterInstances

    def createMcVariableInstance(self, short_name: str) -> McDataInstance:
        """
        Creates a McDataInstance for measurement and adds it to this MC support data.
        If a data instance with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new measurement data instance

        Returns:
            The created (or existing) McDataInstance
        """
        for instance in self.mcVariableInstances:
            if instance.short_name == short_name:
                return instance
        instance = McDataInstance(self, short_name)
        self.mcVariableInstances.append(instance)
        return instance

    def getMcVariableInstances(self) -> List[McDataInstance]:
        """
        Gets the measurement data instances aggregated by this MC support data.

        Returns:
            List of McDataInstance instances used for measurement
        """
        return self.mcVariableInstances

    def addMeasurableSystemConstantValuesRef(self, value: Optional[RefType]) -> "McSupportData":
        """
        Adds a reference to a set of system constant values to be transferred to the MCD system.
        A None value is a no-op and does not append anything.

        Args:
            value: The reference to a SwSystemconstantValueSet

        Returns:
            self for method chaining
        """
        if value is not None:
            self.measurableSystemConstantValuesRefs.append(value)
        return self

    def getMeasurableSystemConstantValuesRefs(self) -> List[RefType]:
        """
        Gets the references to sets of system constant values to be transferred to the MCD system.

        Returns:
            List of RefType instances referencing SwSystemconstantValueSet elements
        """
        return self.measurableSystemConstantValuesRefs

    def getRptSupportData(self) -> Optional[RptSupportData]:
        """
        Gets the rapid prototyping support data belonging to this implementation.

        Returns:
            RptSupportData instance, or None if not set
        """
        return self.rptSupportData

    def setRptSupportData(self, value: Optional[RptSupportData]) -> "McSupportData":
        """
        Sets the rapid prototyping support data belonging to this implementation.
        A None value is a no-op and does not overwrite existing support data.

        Args:
            value: The rapid prototyping support data to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptSupportData = value
        return self


__all__ = [
    "ImplementationElementInParameterInstanceRef",
    "McDataAccessDetails",
    "McDataInstance",
    "McFunction",
    "McParameterElementGroup",
    "McSupportData",
    "McSwEmulationMethodSupport",
    "RoleBasedMcDataAssignment",
]
