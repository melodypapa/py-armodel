from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
        self._defCalprmSet: RefType = None

    @property
    def def_calprm_set(self) -> RefType:
        """Get defCalprmSet (Pythonic accessor)."""
        return self._defCalprmSet

    @def_calprm_set.setter
    def def_calprm_set(self, value: RefType) -> None:
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
        # Refers to the set of measurable input data for this.
        self._inMeasurement: RefType = None

    @property
    def in_measurement(self) -> RefType:
        """Get inMeasurement (Pythonic accessor)."""
        return self._inMeasurement

    @in_measurement.setter
    def in_measurement(self, value: RefType) -> None:
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
        # Refers to the set of measurable local data in this function.
        # atpSplitable Set Tags:.
        self._loc: RefType = None

    @property
    def loc(self) -> RefType:
        """Get loc (Pythonic accessor)."""
        return self._loc

    @loc.setter
    def loc(self, value: RefType) -> None:
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
        # Refers to the set of measurable output data from this atpSplitable.
        self._out: RefType = None

    @property
    def out(self) -> RefType:
        """Get out (Pythonic accessor)."""
        return self._out

    @out.setter
    def out(self, value: RefType) -> None:
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
        # Refers to the set of adjustable data (= calibration by this function.
        self._refCalprmSet: RefType = None

    @property
    def ref_calprm_set(self) -> RefType:
        """Get refCalprmSet (Pythonic accessor)."""
        return self._refCalprmSet

    @ref_calprm_set.setter
    def ref_calprm_set(self, value: RefType) -> None:
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
        # A sub-function that is seen as part of the enclosing.
        self._subFunction: List["McFunction"] = []

    @property
    def sub_function(self) -> List["McFunction"]:
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

    def setDefCalprmSet(self, value: RefType) -> "McFunction":
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

    def setInMeasurement(self, value: RefType) -> "McFunction":
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

    def setLoc(self, value: RefType) -> "McFunction":
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

    def setOut(self, value: RefType) -> "McFunction":
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

    def setRefCalprmSet(self, value: RefType) -> "McFunction":
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

    def getSubFunction(self) -> List["McFunction"]:
        """
        AUTOSAR-compliant getter for subFunction.

        Returns:
            The subFunction value

        Note:
            Delegates to sub_function property (CODING_RULE_V2_00017)
        """
        return self.sub_function  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_def_calprm_set(self, value: Optional[RefType]) -> "McFunction":
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

    def with_in_measurement(self, value: Optional[RefType]) -> "McFunction":
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

    def with_loc(self, value: Optional[RefType]) -> "McFunction":
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

    def with_out(self, value: Optional[RefType]) -> "McFunction":
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

    def with_ref_calprm_set(self, value: Optional[RefType]) -> "McFunction":
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
