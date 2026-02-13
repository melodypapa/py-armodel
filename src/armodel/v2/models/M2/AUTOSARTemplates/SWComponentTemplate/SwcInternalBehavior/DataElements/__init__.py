"""
AUTOSAR Package - DataElements

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)


class AutosarParameterRef(ARObject):
    """
    This class represents a reference to a parameter within AUTOSAR which can be
    one of the following use cases: localParameter: • localParameter which is
    used as whole (e.g. sharedAxis for curve) autosarVariable: • a parameter
    provided via PortPrototype which is used as whole (e.g. parameterAccess) •
    an element inside of a composite local parameter typed by
    ApplicationDatatype (e.g. sharedAxis for a curve) • an element inside of a
    composite parameter provided via Port and typed by ApplicationDatatype (e.g.
    sharedAxis for a curve) autosarParameterInImplDatatype: • an element inside
    of a composite local parameter typed by ImplementationDatatype • an element
    inside of a composite parameter provided via PortPrototype and typed by
    Implementation Datatype

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::AutosarParameterRef

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 306, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 317, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # is either imported via a port or is part of a structure.
        # by: ParameterInAtomicSWC 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._autosar: Optional[RefType] = None

    @property
    def autosar(self) -> Optional[RefType]:
        """Get autosar (Pythonic accessor)."""
        return self._autosar

    @autosar.setter
    def autosar(self, value: Optional[RefType]) -> None:
        """
        Set autosar with validation.

        Args:
            value: The autosar to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autosar = None
            return

        self._autosar = value
        # In the majority of cases this reference goes to Parameter than
                # VariableDataPrototypes.
        # reference to a VariableDataPrototype is special use cases, e.
        # g.
        # if the AutosarParameter used in the context of an SwAxisGrouped.
        # is used if the arParameter is local to the it would technically also be
                # feasible to use an this case.
        # However, the InstanceRef have a contextElement (because the current the
                # context).
        # local instance is a special case which may optimization.
        # Therefore an explicit provided for this case.
        self._localParameter: Optional[RefType] = None

    @property
    def local_parameter(self) -> Optional[RefType]:
        """Get localParameter (Pythonic accessor)."""
        return self._localParameter

    @local_parameter.setter
    def local_parameter(self, value: Optional[RefType]) -> None:
        """
        Set localParameter with validation.

        Args:
            value: The localParameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localParameter = None
            return

        self._localParameter = value

    def with_context_data(self, value):
        """
        Set context_data and return self for chaining.

        Args:
            value: The context_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    def with_context_data(self, value):
        """
        Set context_data and return self for chaining.

        Args:
            value: The context_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutosar(self) -> RefType:
        """
        AUTOSAR-compliant getter for autosar.

        Returns:
            The autosar value

        Note:
            Delegates to autosar property (CODING_RULE_V2_00017)
        """
        return self.autosar  # Delegates to property

    def setAutosar(self, value: RefType) -> AutosarParameterRef:
        """
        AUTOSAR-compliant setter for autosar with method chaining.

        Args:
            value: The autosar to set

        Returns:
            self for method chaining

        Note:
            Delegates to autosar property setter (gets validation automatically)
        """
        self.autosar = value  # Delegates to property setter
        return self

    def getLocalParameter(self) -> RefType:
        """
        AUTOSAR-compliant getter for localParameter.

        Returns:
            The localParameter value

        Note:
            Delegates to local_parameter property (CODING_RULE_V2_00017)
        """
        return self.local_parameter  # Delegates to property

    def setLocalParameter(self, value: RefType) -> AutosarParameterRef:
        """
        AUTOSAR-compliant setter for localParameter with method chaining.

        Args:
            value: The localParameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_parameter property setter (gets validation automatically)
        """
        self.local_parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_autosar(self, value: Optional[RefType]) -> AutosarParameterRef:
        """
        Set autosar and return self for chaining.

        Args:
            value: The autosar to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_autosar("value")
        """
        self.autosar = value  # Use property setter (gets validation)
        return self

    def with_local_parameter(self, value: Optional[RefType]) -> AutosarParameterRef:
        """
        Set localParameter and return self for chaining.

        Args:
            value: The localParameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_parameter("value")
        """
        self.local_parameter = value  # Use property setter (gets validation)
        return self



class AutosarVariableRef(ARObject):
    """
    This class represents a reference to a variable within AUTOSAR which can be
    one of the following use cases: localVariable: • localVariable which is used
    as whole (e.g. InterRunnableVariable, inputValue for curve) autosarVariable:
    • a variable provided via Port which is used as whole (e.g.
    dataAccesspoints) • an element inside of a composite local variable typed by
    ApplicationDatatype (e.g. inputValue for a curve) • an element inside of a
    composite variable provided via Port and typed by ApplicationDatatype (e.g.
    inputValue for a curve) autosarVariableInImplDatatype: • an element inside
    of a composite local variable typed by ImplementationDatatype (e.g.
    nvramData mapping) • an element inside of a composite variable provided via
    Port and typed by ImplementationDatatype (e.g. inputValue for a curve)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::AutosarVariableRef

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 307, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 315, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is used if the target variable is inside of variableData Prototype typed
                # by an ImplementationDataType.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._autosarVariable: Optional[ArVariableIn] = None

    @property
    def autosar_variable(self) -> Optional[ArVariableIn]:
        """Get autosarVariable (Pythonic accessor)."""
        return self._autosarVariable

    @autosar_variable.setter
    def autosar_variable(self, value: Optional[ArVariableIn]) -> None:
        """
        Set autosarVariable with validation.

        Args:
            value: The autosarVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autosarVariable = None
            return

        if not isinstance(value, ArVariableIn):
            raise TypeError(
                f"autosarVariable must be ArVariableIn or None, got {type(value).__name__}"
            )
        self._autosarVariable = value
        # This reference is used if the variable is local to the current would also be
                # possible to use the instance Such an instance ref would not have a the
                # current instance is the context.
        # local instance is a special case which may provide Therefore an explicit
                # reference is this case.
        self._localVariable: Optional[RefType] = None

    @property
    def local_variable(self) -> Optional[RefType]:
        """Get localVariable (Pythonic accessor)."""
        return self._localVariable

    @local_variable.setter
    def local_variable(self, value: Optional[RefType]) -> None:
        """
        Set localVariable with validation.

        Args:
            value: The localVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localVariable = None
            return

        self._localVariable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutosarVariable(self) -> ArVariableIn:
        """
        AUTOSAR-compliant getter for autosarVariable.

        Returns:
            The autosarVariable value

        Note:
            Delegates to autosar_variable property (CODING_RULE_V2_00017)
        """
        return self.autosar_variable  # Delegates to property

    def setAutosarVariable(self, value: ArVariableIn) -> AutosarVariableRef:
        """
        AUTOSAR-compliant setter for autosarVariable with method chaining.

        Args:
            value: The autosarVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to autosar_variable property setter (gets validation automatically)
        """
        self.autosar_variable = value  # Delegates to property setter
        return self

    def getLocalVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for localVariable.

        Returns:
            The localVariable value

        Note:
            Delegates to local_variable property (CODING_RULE_V2_00017)
        """
        return self.local_variable  # Delegates to property

    def setLocalVariable(self, value: RefType) -> AutosarVariableRef:
        """
        AUTOSAR-compliant setter for localVariable with method chaining.

        Args:
            value: The localVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_variable property setter (gets validation automatically)
        """
        self.local_variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_autosar_variable(self, value: Optional[ArVariableIn]) -> AutosarVariableRef:
        """
        Set autosarVariable and return self for chaining.

        Args:
            value: The autosarVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_autosar_variable("value")
        """
        self.autosar_variable = value  # Use property setter (gets validation)
        return self

    def with_local_variable(self, value: Optional[RefType]) -> AutosarVariableRef:
        """
        Set localVariable and return self for chaining.

        Args:
            value: The localVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_variable("value")
        """
        self.local_variable = value  # Use property setter (gets validation)
        return self



class ParameterAccess(AbstractAccessPoint):
    """
    The presence of a ParameterAccess implies that a RunnableEntity needs access
    to a ParameterData Prototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::ParameterAccess

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 325, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 586, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the accessed calibration parameter.
        self._accessedParameter: Optional[RefType] = None

    @property
    def accessed_parameter(self) -> Optional[RefType]:
        """Get accessedParameter (Pythonic accessor)."""
        return self._accessedParameter

    @accessed_parameter.setter
    def accessed_parameter(self, value: Optional[RefType]) -> None:
        """
        Set accessedParameter with validation.

        Args:
            value: The accessedParameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessedParameter = None
            return

        self._accessedParameter = value
        # This allows denote instance and access specific mainly input values and
        # common axis.
        self._swDataDef: Optional[SwDataDefProps] = None

    @property
    def sw_data_def(self) -> Optional[SwDataDefProps]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional[SwDataDefProps]) -> None:
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedParameter(self) -> RefType:
        """
        AUTOSAR-compliant getter for accessedParameter.

        Returns:
            The accessedParameter value

        Note:
            Delegates to accessed_parameter property (CODING_RULE_V2_00017)
        """
        return self.accessed_parameter  # Delegates to property

    def setAccessedParameter(self, value: RefType) -> ParameterAccess:
        """
        AUTOSAR-compliant setter for accessedParameter with method chaining.

        Args:
            value: The accessedParameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to accessed_parameter property setter (gets validation automatically)
        """
        self.accessed_parameter = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> SwDataDefProps:
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: SwDataDefProps) -> ParameterAccess:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accessed_parameter(self, value: Optional[RefType]) -> ParameterAccess:
        """
        Set accessedParameter and return self for chaining.

        Args:
            value: The accessedParameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accessed_parameter("value")
        """
        self.accessed_parameter = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional[SwDataDefProps]) -> ParameterAccess:
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



class VariableAccess(AbstractAccessPoint):
    """
    The presence of a VariableAccess implies that a RunnableEntity needs access
    to a VariableData Prototype. The kind of access is specified by the role in
    which the class is used.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::VariableAccess

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 351, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 567, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2077, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 256, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the accessed variable.
        self._accessedVariable: Optional[RefType] = None

    @property
    def accessed_variable(self) -> Optional[RefType]:
        """Get accessedVariable (Pythonic accessor)."""
        return self._accessedVariable

    @accessed_variable.setter
    def accessed_variable(self, value: Optional[RefType]) -> None:
        """
        Set accessedVariable with validation.

        Args:
            value: The accessedVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessedVariable = None
            return

        self._accessedVariable = value
        # This attribute allows for constraining the scope of the communication.
        # For example, it possible to the communication is intended to cross of an ECU
                # or whether it is intended not to boundary of a single partition.
        self._scope: Optional["VariableAccessScope"] = None

    @property
    def scope(self) -> Optional["VariableAccessScope"]:
        """Get scope (Pythonic accessor)."""
        return self._scope

    @scope.setter
    def scope(self, value: Optional["VariableAccessScope"]) -> None:
        """
        Set scope with validation.

        Args:
            value: The scope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scope = None
            return

        if not isinstance(value, VariableAccessScope):
            raise TypeError(
                f"scope must be VariableAccessScope or None, got {type(value).__name__}"
            )
        self._scope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for accessedVariable.

        Returns:
            The accessedVariable value

        Note:
            Delegates to accessed_variable property (CODING_RULE_V2_00017)
        """
        return self.accessed_variable  # Delegates to property

    def setAccessedVariable(self, value: RefType) -> VariableAccess:
        """
        AUTOSAR-compliant setter for accessedVariable with method chaining.

        Args:
            value: The accessedVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to accessed_variable property setter (gets validation automatically)
        """
        self.accessed_variable = value  # Delegates to property setter
        return self

    def getScope(self) -> "VariableAccessScope":
        """
        AUTOSAR-compliant getter for scope.

        Returns:
            The scope value

        Note:
            Delegates to scope property (CODING_RULE_V2_00017)
        """
        return self.scope  # Delegates to property

    def setScope(self, value: "VariableAccessScope") -> VariableAccess:
        """
        AUTOSAR-compliant setter for scope with method chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Note:
            Delegates to scope property setter (gets validation automatically)
        """
        self.scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accessed_variable(self, value: Optional[RefType]) -> VariableAccess:
        """
        Set accessedVariable and return self for chaining.

        Args:
            value: The accessedVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accessed_variable("value")
        """
        self.accessed_variable = value  # Use property setter (gets validation)
        return self

    def with_scope(self, value: Optional["VariableAccessScope"]) -> VariableAccess:
        """
        Set scope and return self for chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scope("value")
        """
        self.scope = value  # Use property setter (gets validation)
        return self



class ArVariableInImplementationDataInstanceRef(ARObject):
    """
    that this class follows the pattern of an InstanceRef but is not implemented
    based on the abstract classes because the ImplementationDataType isn’t
    either, especially because ImplementationDataType Element isn’t derived from
    AtpPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::ArVariableInImplementationDataInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 322, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a context in case there are subelements with explicit types.
        # The reference has to be ordered to reflect the nested structure.
        self._contextData: List[AbstractImplementation] = []

    @property
    def context_data(self) -> List[AbstractImplementation]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # This is the port providing/receiving the root of the variable.
        self._portPrototype: Optional[RefType] = None

    @property
    def port_prototype(self) -> Optional[RefType]:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: Optional[RefType]) -> None:
        """
        Set portPrototype with validation.

        Args:
            value: The portPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portPrototype = None
            return

        self._portPrototype = value
        # This refers to the VariableDataPrototype typed by the in which the target can
        # be found.
        self._rootVariable: Optional[RefType] = None

    @property
    def root_variable(self) -> Optional[RefType]:
        """Get rootVariable (Pythonic accessor)."""
        return self._rootVariable

    @root_variable.setter
    def root_variable(self, value: Optional[RefType]) -> None:
        """
        Set rootVariable with validation.

        Args:
            value: The rootVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootVariable = None
            return

        self._rootVariable = value
        # This reference points to the target ImplementationData TypeElement.
        self._targetData: Optional[AbstractImplementation] = None

    @property
    def target_data(self) -> Optional[AbstractImplementation]:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: Optional[AbstractImplementation]) -> None:
        """
        Set targetData with validation.

        Args:
            value: The targetData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetData = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"targetData must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextData(self) -> List[AbstractImplementation]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getPortPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: RefType) -> ArVariableInImplementationDataInstanceRef:
        """
        AUTOSAR-compliant setter for portPrototype with method chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_prototype property setter (gets validation automatically)
        """
        self.port_prototype = value  # Delegates to property setter
        return self

    def getRootVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootVariable.

        Returns:
            The rootVariable value

        Note:
            Delegates to root_variable property (CODING_RULE_V2_00017)
        """
        return self.root_variable  # Delegates to property

    def setRootVariable(self, value: RefType) -> ArVariableInImplementationDataInstanceRef:
        """
        AUTOSAR-compliant setter for rootVariable with method chaining.

        Args:
            value: The rootVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_variable property setter (gets validation automatically)
        """
        self.root_variable = value  # Delegates to property setter
        return self

    def getTargetData(self) -> AbstractImplementation:
        """
        AUTOSAR-compliant getter for targetData.

        Returns:
            The targetData value

        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: AbstractImplementation) -> ArVariableInImplementationDataInstanceRef:
        """
        AUTOSAR-compliant setter for targetData with method chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data property setter (gets validation automatically)
        """
        self.target_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_port_prototype(self, value: Optional[RefType]) -> ArVariableInImplementationDataInstanceRef:
        """
        Set portPrototype and return self for chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_prototype("value")
        """
        self.port_prototype = value  # Use property setter (gets validation)
        return self

    def with_root_variable(self, value: Optional[RefType]) -> ArVariableInImplementationDataInstanceRef:
        """
        Set rootVariable and return self for chaining.

        Args:
            value: The rootVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_variable("value")
        """
        self.root_variable = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional[AbstractImplementation]) -> ArVariableInImplementationDataInstanceRef:
        """
        Set targetData and return self for chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data("value")
        """
        self.target_data = value  # Use property setter (gets validation)
        return self



class ArParameterInImplementationDataInstanceRef(ARObject):
    """
    that this class follows the pattern of an InstanceRef but is not implemented
    based on the abstract classes because the ImplementationDataType isn’t
    either, especially because ImplementationDataType Element (intentionally)
    isn’t derived from AtpPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::ArParameterInImplementationDataInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 324, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a context in case there are subelements with explicit types.
        # The reference has to be ordered to reflect the nested structure.
        self._contextData: List[AbstractImplementation] = []

    @property
    def context_data(self) -> List[AbstractImplementation]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # This reference points to the PortPrototype providing/ root of the parameter.
        self._portPrototype: Optional[RefType] = None

    @property
    def port_prototype(self) -> Optional[RefType]:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: Optional[RefType]) -> None:
        """
        Set portPrototype with validation.

        Args:
            value: The portPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portPrototype = None
            return

        self._portPrototype = value
        # This refers to the ParameterDataPrototype typed by the implementationDataType
        # in which the target can be.
        self._rootParameter: Optional["ParameterData"] = None

    @property
    def root_parameter(self) -> Optional["ParameterData"]:
        """Get rootParameter (Pythonic accessor)."""
        return self._rootParameter

    @root_parameter.setter
    def root_parameter(self, value: Optional["ParameterData"]) -> None:
        """
        Set rootParameter with validation.

        Args:
            value: The rootParameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootParameter = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"rootParameter must be ParameterData or None, got {type(value).__name__}"
            )
        self._rootParameter = value
        # This reference points to the target ImplementationData TypeElement.
        self._targetData: Optional[AbstractImplementation] = None

    @property
    def target_data(self) -> Optional[AbstractImplementation]:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: Optional[AbstractImplementation]) -> None:
        """
        Set targetData with validation.

        Args:
            value: The targetData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetData = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"targetData must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextData(self) -> List[AbstractImplementation]:
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getPortPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: RefType) -> ArParameterInImplementationDataInstanceRef:
        """
        AUTOSAR-compliant setter for portPrototype with method chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_prototype property setter (gets validation automatically)
        """
        self.port_prototype = value  # Delegates to property setter
        return self

    def getRootParameter(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for rootParameter.

        Returns:
            The rootParameter value

        Note:
            Delegates to root_parameter property (CODING_RULE_V2_00017)
        """
        return self.root_parameter  # Delegates to property

    def setRootParameter(self, value: "ParameterData") -> ArParameterInImplementationDataInstanceRef:
        """
        AUTOSAR-compliant setter for rootParameter with method chaining.

        Args:
            value: The rootParameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to root_parameter property setter (gets validation automatically)
        """
        self.root_parameter = value  # Delegates to property setter
        return self

    def getTargetData(self) -> AbstractImplementation:
        """
        AUTOSAR-compliant getter for targetData.

        Returns:
            The targetData value

        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: AbstractImplementation) -> ArParameterInImplementationDataInstanceRef:
        """
        AUTOSAR-compliant setter for targetData with method chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data property setter (gets validation automatically)
        """
        self.target_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_port_prototype(self, value: Optional[RefType]) -> ArParameterInImplementationDataInstanceRef:
        """
        Set portPrototype and return self for chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_prototype("value")
        """
        self.port_prototype = value  # Use property setter (gets validation)
        return self

    def with_root_parameter(self, value: Optional["ParameterData"]) -> ArParameterInImplementationDataInstanceRef:
        """
        Set rootParameter and return self for chaining.

        Args:
            value: The rootParameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root_parameter("value")
        """
        self.root_parameter = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional[AbstractImplementation]) -> ArParameterInImplementationDataInstanceRef:
        """
        Set targetData and return self for chaining.

        Args:
            value: The targetData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data("value")
        """
        self.target_data = value  # Use property setter (gets validation)
        return self


class VariableAccessScopeEnum(AREnum):
    """
    VariableAccessScopeEnum enumeration

This enumeration defines scopes for communication. Aggregated by VariableAccess.scope

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements
    """
    # This case is foreseen to express that the corresponding communication shall be considered Ecu inter-ECU, i.e. it will cross the ECU boundary. This is considered the default case.
    communicationInter = "0"

    # This case is foreseen to express that the corresponding communication shall not cross the boundary Partition of a partition.
    communicationIntra = "1"

    # In this case the communication shall cross the boundaries of partitions within one ECU but it shall not Ecu cross the boundaries of the ECU itself.
    interPartitionIntra = "2"


__all__ = [
    AutosarParameterRef,
    AutosarVariableRef,
    ParameterAccess,
    VariableAccess,
    ArVariableInImplementationDataInstanceRef,
    ArParameterInImplementationDataInstanceRef,
    VariableAccessScopeEnum,
]
