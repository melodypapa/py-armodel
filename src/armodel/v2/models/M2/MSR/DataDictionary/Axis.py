"""
AUTOSAR Package - Axis

Package: M2::MSR::DataDictionary::Axis
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
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
from armodel.v2.models.M2.MSR.DataDictionary.CalibrationParameter import (
    SwCalprmAxisTypeProps,
)


class SwAxisIndividual(SwCalprmAxisTypeProps):
    """
    This meta-class describes an axis integrated into a parameter (field etc.).
    The integration makes this individual to each parameter. The so-called
    grouped axis represents the counterpart to this. It is conceived as an
    independent parameter (see class SwAxisGrouped).
    
    Package: M2::MSR::DataDictionary::Axis::SwAxisIndividual
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 354, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the compuMethod which is expected for the axis.
        # It in early stages if the particular input-value is not.
        self._compuMethod: Optional["CompuMethod"] = None

    @property
    def compu_method(self) -> Optional["CompuMethod"]:
        """Get compuMethod (Pythonic accessor)."""
        return self._compuMethod

    @compu_method.setter
    def compu_method(self, value: Optional["CompuMethod"]) -> None:
        """
        Set compuMethod with validation.
        
        Args:
            value: The compuMethod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuMethod = None
            return

        if not isinstance(value, CompuMethod):
            raise TypeError(
                f"compuMethod must be CompuMethod or None, got {type(value).__name__}"
            )
        self._compuMethod = value
        # Refers to constraints, e.
        # g.
        # for plausibility checks.
        self._dataConstr: Optional["DataConstr"] = None

    @property
    def data_constr(self) -> Optional["DataConstr"]:
        """Get dataConstr (Pythonic accessor)."""
        return self._dataConstr

    @data_constr.setter
    def data_constr(self, value: Optional["DataConstr"]) -> None:
        """
        Set dataConstr with validation.
        
        Args:
            value: The dataConstr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataConstr = None
            return

        if not isinstance(value, DataConstr):
            raise TypeError(
                f"dataConstr must be DataConstr or None, got {type(value).__name__}"
            )
        self._dataConstr = value
        # This is the datatype of the input value for the axis.
        # This allows to define e.
        # g.
        # a type of curve, where the input finalized at the access point.
        self._inputVariable: Optional["ApplicationPrimitive"] = None

    @property
    def input_variable(self) -> Optional["ApplicationPrimitive"]:
        """Get inputVariable (Pythonic accessor)."""
        return self._inputVariable

    @input_variable.setter
    def input_variable(self, value: Optional["ApplicationPrimitive"]) -> None:
        """
        Set inputVariable with validation.
        
        Args:
            value: The inputVariable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inputVariable = None
            return

        if not isinstance(value, ApplicationPrimitive):
            raise TypeError(
                f"inputVariable must be ApplicationPrimitive or None, got {type(value).__name__}"
            )
        self._inputVariable = value
        # this specifies the properties of a generic axis if applicable.
        self._swAxisGeneric: Optional["SwAxisGeneric"] = None

    @property
    def sw_axis_generic(self) -> Optional["SwAxisGeneric"]:
        """Get swAxisGeneric (Pythonic accessor)."""
        return self._swAxisGeneric

    @sw_axis_generic.setter
    def sw_axis_generic(self, value: Optional["SwAxisGeneric"]) -> None:
        """
        Set swAxisGeneric with validation.
        
        Args:
            value: The swAxisGeneric to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAxisGeneric = None
            return

        if not isinstance(value, SwAxisGeneric):
            raise TypeError(
                f"swAxisGeneric must be SwAxisGeneric or None, got {type(value).__name__}"
            )
        self._swAxisGeneric = value
        # Maximum number of base points contained in the axis of map or curve.
        self._swMaxAxis: Optional["Integer"] = None

    @property
    def sw_max_axis(self) -> Optional["Integer"]:
        """Get swMaxAxis (Pythonic accessor)."""
        return self._swMaxAxis

    @sw_max_axis.setter
    def sw_max_axis(self, value: Optional["Integer"]) -> None:
        """
        Set swMaxAxis with validation.
        
        Args:
            value: The swMaxAxis to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swMaxAxis = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"swMaxAxis must be Integer or int or None, got {type(value).__name__}"
            )
        self._swMaxAxis = value
        # Minimum number of base points contained in the axis of a or curve.
        self._swMinAxis: Optional["Integer"] = None

    @property
    def sw_min_axis(self) -> Optional["Integer"]:
        """Get swMinAxis (Pythonic accessor)."""
        return self._swMinAxis

    @sw_min_axis.setter
    def sw_min_axis(self, value: Optional["Integer"]) -> None:
        """
        Set swMinAxis with validation.
        
        Args:
            value: The swMinAxis to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swMinAxis = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"swMinAxis must be Integer or int or None, got {type(value).__name__}"
            )
        self._swMinAxis = value
        # Refers to input variables of the axis.
        # It is possible to more than one variable.
        # Here the following is variable with the highest priority shall be given
                # first.
        # used in the generation of the code and is also in the application system.
        # variables referenced shall be of the same physical is usually detected in
                # that the conversion refer back to the same SI-units.
        # this ensured by the constraint, that the variables shall use a type
                # compatible to multiple referencing allows a base point more than one input
                # variable to be used.
        # of this are the temperature curves which both on the induction air
                # temperature and temperature.
        # can be displayed simultaneously by MCD systems), enabling operating points
                # shown in the curves.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._swVariableRef: List["RefType"] = []

    @property
    def sw_variable_ref(self) -> List["RefType"]:
        """Get swVariableRef (Pythonic accessor)."""
        return self._swVariableRef
        # This represents the physical unit of the input value of the is provided to
        # support the case that the particular is not yet known.
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.
        
        Args:
            value: The unit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value

    def with_sw_variable_ref(self, value):
        """
        Set sw_variable_ref and return self for chaining.

        Args:
            value: The sw_variable_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_variable_ref("value")
        """
        self.sw_variable_ref = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuMethod(self) -> "CompuMethod":
        """
        AUTOSAR-compliant getter for compuMethod.
        
        Returns:
            The compuMethod value
        
        Note:
            Delegates to compu_method property (CODING_RULE_V2_00017)
        """
        return self.compu_method  # Delegates to property

    def setCompuMethod(self, value: "CompuMethod") -> "SwAxisIndividual":
        """
        AUTOSAR-compliant setter for compuMethod with method chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compu_method property setter (gets validation automatically)
        """
        self.compu_method = value  # Delegates to property setter
        return self

    def getDataConstr(self) -> "DataConstr":
        """
        AUTOSAR-compliant getter for dataConstr.
        
        Returns:
            The dataConstr value
        
        Note:
            Delegates to data_constr property (CODING_RULE_V2_00017)
        """
        return self.data_constr  # Delegates to property

    def setDataConstr(self, value: "DataConstr") -> "SwAxisIndividual":
        """
        AUTOSAR-compliant setter for dataConstr with method chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_constr property setter (gets validation automatically)
        """
        self.data_constr = value  # Delegates to property setter
        return self

    def getInputVariable(self) -> "ApplicationPrimitive":
        """
        AUTOSAR-compliant getter for inputVariable.
        
        Returns:
            The inputVariable value
        
        Note:
            Delegates to input_variable property (CODING_RULE_V2_00017)
        """
        return self.input_variable  # Delegates to property

    def setInputVariable(self, value: "ApplicationPrimitive") -> "SwAxisIndividual":
        """
        AUTOSAR-compliant setter for inputVariable with method chaining.
        
        Args:
            value: The inputVariable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to input_variable property setter (gets validation automatically)
        """
        self.input_variable = value  # Delegates to property setter
        return self

    def getSwAxisGeneric(self) -> "SwAxisGeneric":
        """
        AUTOSAR-compliant getter for swAxisGeneric.
        
        Returns:
            The swAxisGeneric value
        
        Note:
            Delegates to sw_axis_generic property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_generic  # Delegates to property

    def setSwAxisGeneric(self, value: "SwAxisGeneric") -> "SwAxisIndividual":
        """
        AUTOSAR-compliant setter for swAxisGeneric with method chaining.
        
        Args:
            value: The swAxisGeneric to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_axis_generic property setter (gets validation automatically)
        """
        self.sw_axis_generic = value  # Delegates to property setter
        return self

    def getSwMaxAxis(self) -> "Integer":
        """
        AUTOSAR-compliant getter for swMaxAxis.
        
        Returns:
            The swMaxAxis value
        
        Note:
            Delegates to sw_max_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_max_axis  # Delegates to property

    def setSwMaxAxis(self, value: "Integer") -> "SwAxisIndividual":
        """
        AUTOSAR-compliant setter for swMaxAxis with method chaining.
        
        Args:
            value: The swMaxAxis to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_max_axis property setter (gets validation automatically)
        """
        self.sw_max_axis = value  # Delegates to property setter
        return self

    def getSwMinAxis(self) -> "Integer":
        """
        AUTOSAR-compliant getter for swMinAxis.
        
        Returns:
            The swMinAxis value
        
        Note:
            Delegates to sw_min_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_min_axis  # Delegates to property

    def setSwMinAxis(self, value: "Integer") -> "SwAxisIndividual":
        """
        AUTOSAR-compliant setter for swMinAxis with method chaining.
        
        Args:
            value: The swMinAxis to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_min_axis property setter (gets validation automatically)
        """
        self.sw_min_axis = value  # Delegates to property setter
        return self

    def getSwVariableRef(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for swVariableRef.
        
        Returns:
            The swVariableRef value
        
        Note:
            Delegates to sw_variable_ref property (CODING_RULE_V2_00017)
        """
        return self.sw_variable_ref  # Delegates to property

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.
        
        Returns:
            The unit value
        
        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "SwAxisIndividual":
        """
        AUTOSAR-compliant setter for unit with method chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_method(self, value: Optional["CompuMethod"]) -> "SwAxisIndividual":
        """
        Set compuMethod and return self for chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compu_method("value")
        """
        self.compu_method = value  # Use property setter (gets validation)
        return self

    def with_data_constr(self, value: Optional["DataConstr"]) -> "SwAxisIndividual":
        """
        Set dataConstr and return self for chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_constr("value")
        """
        self.data_constr = value  # Use property setter (gets validation)
        return self

    def with_input_variable(self, value: Optional["ApplicationPrimitive"]) -> "SwAxisIndividual":
        """
        Set inputVariable and return self for chaining.
        
        Args:
            value: The inputVariable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_input_variable("value")
        """
        self.input_variable = value  # Use property setter (gets validation)
        return self

    def with_sw_axis_generic(self, value: Optional["SwAxisGeneric"]) -> "SwAxisIndividual":
        """
        Set swAxisGeneric and return self for chaining.
        
        Args:
            value: The swAxisGeneric to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_axis_generic("value")
        """
        self.sw_axis_generic = value  # Use property setter (gets validation)
        return self

    def with_sw_max_axis(self, value: Optional["Integer"]) -> "SwAxisIndividual":
        """
        Set swMaxAxis and return self for chaining.
        
        Args:
            value: The swMaxAxis to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_max_axis("value")
        """
        self.sw_max_axis = value  # Use property setter (gets validation)
        return self

    def with_sw_min_axis(self, value: Optional["Integer"]) -> "SwAxisIndividual":
        """
        Set swMinAxis and return self for chaining.
        
        Args:
            value: The swMinAxis to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_min_axis("value")
        """
        self.sw_min_axis = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "SwAxisIndividual":
        """
        Set unit and return self for chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self



class SwAxisGeneric(ARObject):
    """
    This meta-class defines a generic axis. In a generic axis the axispoints
    points are calculated in the ECU. The ECU is equipped with a fixed
    calculation algorithm. Parameters for the algorithm can be stored in the
    data component of the ECU. Therefore these parameters are specified in the
    data declaration, not in the calibration data.
    
    Package: M2::MSR::DataDictionary::Axis::SwAxisGeneric
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 355, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Associated axis calculation strategy.
        self._swAxisType: Optional["SwAxisType"] = None

    @property
    def sw_axis_type(self) -> Optional["SwAxisType"]:
        """Get swAxisType (Pythonic accessor)."""
        return self._swAxisType

    @sw_axis_type.setter
    def sw_axis_type(self, value: Optional["SwAxisType"]) -> None:
        """
        Set swAxisType with validation.
        
        Args:
            value: The swAxisType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAxisType = None
            return

        if not isinstance(value, SwAxisType):
            raise TypeError(
                f"swAxisType must be SwAxisType or None, got {type(value).__name__}"
            )
        self._swAxisType = value
        # Specific parameter of a generic axis.
        self._swGenericAxis: List["SwGenericAxisParam"] = []

    @property
    def sw_generic_axis(self) -> List["SwGenericAxisParam"]:
        """Get swGenericAxis (Pythonic accessor)."""
        return self._swGenericAxis

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwAxisType(self) -> "SwAxisType":
        """
        AUTOSAR-compliant getter for swAxisType.
        
        Returns:
            The swAxisType value
        
        Note:
            Delegates to sw_axis_type property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_type  # Delegates to property

    def setSwAxisType(self, value: "SwAxisType") -> "SwAxisGeneric":
        """
        AUTOSAR-compliant setter for swAxisType with method chaining.
        
        Args:
            value: The swAxisType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_axis_type property setter (gets validation automatically)
        """
        self.sw_axis_type = value  # Delegates to property setter
        return self

    def getSwGenericAxis(self) -> List["SwGenericAxisParam"]:
        """
        AUTOSAR-compliant getter for swGenericAxis.
        
        Returns:
            The swGenericAxis value
        
        Note:
            Delegates to sw_generic_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_generic_axis  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_axis_type(self, value: Optional["SwAxisType"]) -> "SwAxisGeneric":
        """
        Set swAxisType and return self for chaining.
        
        Args:
            value: The swAxisType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_axis_type("value")
        """
        self.sw_axis_type = value  # Use property setter (gets validation)
        return self



class SwAxisType(ARElement):
    """
    This meta-class represents a specific axis calculation strategy. No formal
    specification is given, due to the fact that it is possible to use arbitrary
    algorithms for calculating axis-points. Instead, the algorithm is described
    verbally but the parameters are specified formally with respect to their
    names and constraints. As a result, SwAxisType mainly reserves appropriate
    keywords.
    
    Package: M2::MSR::DataDictionary::Axis::SwAxisType
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 355, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Parameters for this calculation algorithm.
        # Tags:.
        self._swGenericAxis: List["SwGenericAxisParam"] = []

    @property
    def sw_generic_axis(self) -> List["SwGenericAxisParam"]:
        """Get swGenericAxis (Pythonic accessor)."""
        return self._swGenericAxis

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwGenericAxis(self) -> List["SwGenericAxisParam"]:
        """
        AUTOSAR-compliant getter for swGenericAxis.
        
        Returns:
            The swGenericAxis value
        
        Note:
            Delegates to sw_generic_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_generic_axis  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwGenericAxisParam(ARObject):
    """
    This meta-class describes a specific parameter of a generic axis. The name
    of the parameter is defined through a reference to a parameter type defined
    on a corresponding axis type. The value of the parameter is given here in
    case that it is not changeable during calibration. Example is shift / offset
    in a fixed axis.
    
    Package: M2::MSR::DataDictionary::Axis::SwGenericAxisParam
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 356, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Parameter type defined on a corresponding axis type.
        # References can only be made to axis parameters types defined within the
                # referenced axis type.
        # Numerical * attr This attribute represents the value of the generic axis.
        self._swGenericAxis: Optional["SwGenericAxisParam"] = None

    @property
    def sw_generic_axis(self) -> Optional["SwGenericAxisParam"]:
        """Get swGenericAxis (Pythonic accessor)."""
        return self._swGenericAxis

    @sw_generic_axis.setter
    def sw_generic_axis(self, value: Optional["SwGenericAxisParam"]) -> None:
        """
        Set swGenericAxis with validation.
        
        Args:
            value: The swGenericAxis to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swGenericAxis = None
            return

        if not isinstance(value, SwGenericAxisParam):
            raise TypeError(
                f"swGenericAxis must be SwGenericAxisParam or None, got {type(value).__name__}"
            )
        self._swGenericAxis = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwGenericAxis(self) -> "SwGenericAxisParam":
        """
        AUTOSAR-compliant getter for swGenericAxis.
        
        Returns:
            The swGenericAxis value
        
        Note:
            Delegates to sw_generic_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_generic_axis  # Delegates to property

    def setSwGenericAxis(self, value: "SwGenericAxisParam") -> "SwGenericAxisParam":
        """
        AUTOSAR-compliant setter for swGenericAxis with method chaining.
        
        Args:
            value: The swGenericAxis to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_generic_axis property setter (gets validation automatically)
        """
        self.sw_generic_axis = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_generic_axis(self, value: Optional["SwGenericAxisParam"]) -> "SwGenericAxisParam":
        """
        Set swGenericAxis and return self for chaining.
        
        Args:
            value: The swGenericAxis to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_generic_axis("value")
        """
        self.sw_generic_axis = value  # Use property setter (gets validation)
        return self



class SwGenericAxisParamType(Identifiable):
    """
    This meta-class describes a generic axis parameter type, namely: •
    Plausibility checks can be specified via dataConstr. • Textual description
    (desc), as a formal description is not of any use, due to the large variety
    of possibilities. • If this parameter contains structures, these can be
    simulated through the recursive use of SwGeneric AxisParamTypes.
    
    Package: M2::MSR::DataDictionary::Axis::SwGenericAxisParamType
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 356, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference denoted data constraints applicable to the parameter.
        self._dataConstr: Optional["DataConstr"] = None

    @property
    def data_constr(self) -> Optional["DataConstr"]:
        """Get dataConstr (Pythonic accessor)."""
        return self._dataConstr

    @data_constr.setter
    def data_constr(self, value: Optional["DataConstr"]) -> None:
        """
        Set dataConstr with validation.
        
        Args:
            value: The dataConstr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataConstr = None
            return

        if not isinstance(value, DataConstr):
            raise TypeError(
                f"dataConstr must be DataConstr or None, got {type(value).__name__}"
            )
        self._dataConstr = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataConstr(self) -> "DataConstr":
        """
        AUTOSAR-compliant getter for dataConstr.
        
        Returns:
            The dataConstr value
        
        Note:
            Delegates to data_constr property (CODING_RULE_V2_00017)
        """
        return self.data_constr  # Delegates to property

    def setDataConstr(self, value: "DataConstr") -> "SwGenericAxisParamType":
        """
        AUTOSAR-compliant setter for dataConstr with method chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_constr property setter (gets validation automatically)
        """
        self.data_constr = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_constr(self, value: Optional["DataConstr"]) -> "SwGenericAxisParamType":
        """
        Set dataConstr and return self for chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_constr("value")
        """
        self.data_constr = value  # Use property setter (gets validation)
        return self



class SwAxisGrouped(SwCalprmAxisTypeProps):
    """
    An SwAxisGrouped is an axis which is shared between multiple calibration
    parameters.
    
    Package: M2::MSR::DataDictionary::Axis::SwAxisGrouped
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 357, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the datatype of the calibration parameter providing shared axis.
        self._sharedAxisType: Optional["ApplicationPrimitive"] = None

    @property
    def shared_axis_type(self) -> Optional["ApplicationPrimitive"]:
        """Get sharedAxisType (Pythonic accessor)."""
        return self._sharedAxisType

    @shared_axis_type.setter
    def shared_axis_type(self, value: Optional["ApplicationPrimitive"]) -> None:
        """
        Set sharedAxisType with validation.
        
        Args:
            value: The sharedAxisType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sharedAxisType = None
            return

        if not isinstance(value, ApplicationPrimitive):
            raise TypeError(
                f"sharedAxisType must be ApplicationPrimitive or None, got {type(value).__name__}"
            )
        self._sharedAxisType = value
        # Describes which axis of the referenced calibration the values for the group
                # axis.
        # The the following convention: = value axis.
        # in this case, the interpolation result of parameter is used as a base point
                # index should only be specified if the parameter contains more than one axis.
        # It is for the axis index of parameters with one axis, to be set to 1, if data
                # has not been swAxisIndex.
        self._swAxisIndex: Optional["AxisIndexType"] = None

    @property
    def sw_axis_index(self) -> Optional["AxisIndexType"]:
        """Get swAxisIndex (Pythonic accessor)."""
        return self._swAxisIndex

    @sw_axis_index.setter
    def sw_axis_index(self, value: Optional["AxisIndexType"]) -> None:
        """
        Set swAxisIndex with validation.
        
        Args:
            value: The swAxisIndex to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAxisIndex = None
            return

        if not isinstance(value, AxisIndexType):
            raise TypeError(
                f"swAxisIndex must be AxisIndexType or None, got {type(value).__name__}"
            )
        self._swAxisIndex = value
        # This property specifies the calibration parameter which the input axis.
        # In AUTOSAR, the type of the parameter shall be compatible to specified by
                # sharedAxisType.
        # that the multiplicity of this aggregation cannot to 0.
        # 1 based on the non-mainstream schema defined at the aggregation.
        # multiplicity has to be factually considered a SwAxisGrouped that does not
                # aggregate the is still valid according to the XML on the use case documented
                # in.
        self._swCalprmRef: "RefType" = None

    @property
    def sw_calprm_ref(self) -> "RefType":
        """Get swCalprmRef (Pythonic accessor)."""
        return self._swCalprmRef

    @sw_calprm_ref.setter
    def sw_calprm_ref(self, value: "RefType") -> None:
        """
        Set swCalprmRef with validation.
        
        Args:
            value: The swCalprmRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._swCalprmRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSharedAxisType(self) -> "ApplicationPrimitive":
        """
        AUTOSAR-compliant getter for sharedAxisType.
        
        Returns:
            The sharedAxisType value
        
        Note:
            Delegates to shared_axis_type property (CODING_RULE_V2_00017)
        """
        return self.shared_axis_type  # Delegates to property

    def setSharedAxisType(self, value: "ApplicationPrimitive") -> "SwAxisGrouped":
        """
        AUTOSAR-compliant setter for sharedAxisType with method chaining.
        
        Args:
            value: The sharedAxisType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to shared_axis_type property setter (gets validation automatically)
        """
        self.shared_axis_type = value  # Delegates to property setter
        return self

    def getSwAxisIndex(self) -> "AxisIndexType":
        """
        AUTOSAR-compliant getter for swAxisIndex.
        
        Returns:
            The swAxisIndex value
        
        Note:
            Delegates to sw_axis_index property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_index  # Delegates to property

    def setSwAxisIndex(self, value: "AxisIndexType") -> "SwAxisGrouped":
        """
        AUTOSAR-compliant setter for swAxisIndex with method chaining.
        
        Args:
            value: The swAxisIndex to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_axis_index property setter (gets validation automatically)
        """
        self.sw_axis_index = value  # Delegates to property setter
        return self

    def getSwCalprmRef(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swCalprmRef.
        
        Returns:
            The swCalprmRef value
        
        Note:
            Delegates to sw_calprm_ref property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_ref  # Delegates to property

    def setSwCalprmRef(self, value: "RefType") -> "SwAxisGrouped":
        """
        AUTOSAR-compliant setter for swCalprmRef with method chaining.
        
        Args:
            value: The swCalprmRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_calprm_ref property setter (gets validation automatically)
        """
        self.sw_calprm_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_shared_axis_type(self, value: Optional["ApplicationPrimitive"]) -> "SwAxisGrouped":
        """
        Set sharedAxisType and return self for chaining.
        
        Args:
            value: The sharedAxisType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_shared_axis_type("value")
        """
        self.shared_axis_type = value  # Use property setter (gets validation)
        return self

    def with_sw_axis_index(self, value: Optional["AxisIndexType"]) -> "SwAxisGrouped":
        """
        Set swAxisIndex and return self for chaining.
        
        Args:
            value: The swAxisIndex to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_axis_index("value")
        """
        self.sw_axis_index = value  # Use property setter (gets validation)
        return self

    def with_sw_calprm_ref(self, value: RefType) -> "SwAxisGrouped":
        """
        Set swCalprmRef and return self for chaining.
        
        Args:
            value: The swCalprmRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_calprm_ref("value")
        """
        self.sw_calprm_ref = value  # Use property setter (gets validation)
        return self
