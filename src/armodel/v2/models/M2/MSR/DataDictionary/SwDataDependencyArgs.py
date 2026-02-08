from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwDataDependencyArgs(ARObject):
    """
    This element specifies the elements used in a SwDataDependency.

    Package: M2::MSR::DataDictionary::DataDefProperties::SwDataDependencyArgs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 374, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies a calibration parameter as an input argument to.
        self._swCalprmRef: RefType = None

    @property
    def sw_calprm_ref(self) -> RefType:
        """Get swCalprmRef (Pythonic accessor)."""
        return self._swCalprmRef

    @sw_calprm_ref.setter
    def sw_calprm_ref(self, value: RefType) -> None:
        """
        Set swCalprmRef with validation.

        Args:
            value: The swCalprmRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalprmRef = None
            return

        self._swCalprmRef = value
        # Specifies a variable as an input argument to the.
        self._swVariable: RefType = None

    @property
    def sw_variable(self) -> RefType:
        """Get swVariable (Pythonic accessor)."""
        return self._swVariable

    @sw_variable.setter
    def sw_variable(self, value: RefType) -> None:
        """
        Set swVariable with validation.

        Args:
            value: The swVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swVariable = None
            return

        self._swVariable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwCalprmRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for swCalprmRef.

        Returns:
            The swCalprmRef value

        Note:
            Delegates to sw_calprm_ref property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_ref  # Delegates to property

    def setSwCalprmRef(self, value: RefType) -> "SwDataDependencyArgs":
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

    def getSwVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for swVariable.

        Returns:
            The swVariable value

        Note:
            Delegates to sw_variable property (CODING_RULE_V2_00017)
        """
        return self.sw_variable  # Delegates to property

    def setSwVariable(self, value: RefType) -> "SwDataDependencyArgs":
        """
        AUTOSAR-compliant setter for swVariable with method chaining.

        Args:
            value: The swVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_variable property setter (gets validation automatically)
        """
        self.sw_variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_calprm_ref(self, value: Optional[RefType]) -> "SwDataDependencyArgs":
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

    def with_sw_variable(self, value: Optional[RefType]) -> "SwDataDependencyArgs":
        """
        Set swVariable and return self for chaining.

        Args:
            value: The swVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_variable("value")
        """
        self.sw_variable = value  # Use property setter (gets validation)
        return self
