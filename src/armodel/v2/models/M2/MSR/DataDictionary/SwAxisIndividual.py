from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwAxisIndividual(SwCalprmAxisTypeProps):
    """
    This meta-class describes an axis integrated into a parameter (field etc.).
    The integration makes this individual to each parameter. The so-called
    grouped axis represents the counterpart to this. It is conceived as an
    independent parameter (see class SwAxisGrouped).

    Package: M2::MSR::DataDictionary::Axis

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

        if not isinstance(value, Integer):
            raise TypeError(
                f"swMaxAxis must be Integer or None, got {type(value).__name__}"
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"swMinAxis must be Integer or None, got {type(value).__name__}"
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
        self._swVariableRef: List[RefType] = []

    @property
    def sw_variable_ref(self) -> List[RefType]:
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

    def getSwVariableRef(self) -> List[RefType]:
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
