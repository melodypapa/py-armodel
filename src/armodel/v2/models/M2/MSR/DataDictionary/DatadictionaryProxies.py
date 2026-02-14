"""
AUTOSAR Package - DatadictionaryProxies

Package: M2::MSR::DataDictionary::DatadictionaryProxies
"""


from __future__ import annotations

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import (
    McDataInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwCalprmRefProxy(ARObject):
    """
    Wrapper class for different kinds of references to a calibration parameter.

    Package: M2::MSR::DataDictionary::DatadictionaryProxies::SwCalprmRefProxy

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 370, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a Parameter within AUTOSAR.
        # Note that of the referenced ParameterDataPrototype an ApplicationDataType of
                # category VALUE.
        self._arParameter: Optional[RefType] = None

    @property
    def ar_parameter(self) -> Optional[RefType]:
        """Get arParameter (Pythonic accessor)."""
        return self._arParameter

    @ar_parameter.setter
    def ar_parameter(self, value: Optional[RefType]) -> None:
        """
        Set arParameter with validation.

        Args:
            value: The arParameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arParameter = None
            return

        self._arParameter = value
                # axis etc.
        # It is not allowed to use of an McDataInstance.
        # mcDataInstance shall be originated from.
        self._mcDataInstance: Optional[McDataInstance] = None

    @property
    def mc_data_instance(self) -> Optional[McDataInstance]:
        """Get mcDataInstance (Pythonic accessor)."""
        return self._mcDataInstance

    @mc_data_instance.setter
    def mc_data_instance(self, value: Optional[McDataInstance]) -> None:
        """
        Set mcDataInstance with validation.

        Args:
            value: The mcDataInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mcDataInstance = None
            return

        if not isinstance(value, McDataInstance):
            raise TypeError(
                f"mcDataInstance must be McDataInstance or None, got {type(value).__name__}"
            )
        self._mcDataInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArParameter(self) -> RefType:
        """
        AUTOSAR-compliant getter for arParameter.

        Returns:
            The arParameter value

        Note:
            Delegates to ar_parameter property (CODING_RULE_V2_00017)
        """
        return self.ar_parameter  # Delegates to property

    def setArParameter(self, value: RefType) -> SwCalprmRefProxy:
        """
        AUTOSAR-compliant setter for arParameter with method chaining.

        Args:
            value: The arParameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to ar_parameter property setter (gets validation automatically)
        """
        self.ar_parameter = value  # Delegates to property setter
        return self

    def getMcDataInstance(self) -> McDataInstance:
        """
        AUTOSAR-compliant getter for mcDataInstance.

        Returns:
            The mcDataInstance value

        Note:
            Delegates to mc_data_instance property (CODING_RULE_V2_00017)
        """
        return self.mc_data_instance  # Delegates to property

    def setMcDataInstance(self, value: McDataInstance) -> SwCalprmRefProxy:
        """
        AUTOSAR-compliant setter for mcDataInstance with method chaining.

        Args:
            value: The mcDataInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to mc_data_instance property setter (gets validation automatically)
        """
        self.mc_data_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ar_parameter(self, value: Optional[RefType]) -> SwCalprmRefProxy:
        """
        Set arParameter and return self for chaining.

        Args:
            value: The arParameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ar_parameter("value")
        """
        self.ar_parameter = value  # Use property setter (gets validation)
        return self

    def with_mc_data_instance(self, value: Optional[McDataInstance]) -> SwCalprmRefProxy:
        """
        Set mcDataInstance and return self for chaining.

        Args:
            value: The mcDataInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_data_instance("value")
        """
        self.mc_data_instance = value  # Use property setter (gets validation)
        return self



class SwVariableRefProxy(ARObject):
    """
    Proxy class for several kinds of references to a variable.

    Package: M2::MSR::DataDictionary::DatadictionaryProxies::SwVariableRefProxy

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 370, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the reference to a Variable in an Autosar that the target of
        # the reference within be typed by a primitive data type.
        self._autosarVariable: Optional[RefType] = None

    @property
    def autosar_variable(self) -> Optional[RefType]:
        """Get autosarVariable (Pythonic accessor)."""
        return self._autosarVariable

    @autosar_variable.setter
    def autosar_variable(self, value: Optional[RefType]) -> None:
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

        self._autosarVariable = value
                # input values etc.
        # It is not allowed to outside of an McDataInstance.
        # mcDataInstance shall be originated from.
        self._mcDataInstance: Optional[McDataInstance] = None

    @property
    def mc_data_instance(self) -> Optional[McDataInstance]:
        """Get mcDataInstance (Pythonic accessor)."""
        return self._mcDataInstance

    @mc_data_instance.setter
    def mc_data_instance(self, value: Optional[McDataInstance]) -> None:
        """
        Set mcDataInstance with validation.

        Args:
            value: The mcDataInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mcDataInstance = None
            return

        if not isinstance(value, McDataInstance):
            raise TypeError(
                f"mcDataInstance must be McDataInstance or None, got {type(value).__name__}"
            )
        self._mcDataInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutosarVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for autosarVariable.

        Returns:
            The autosarVariable value

        Note:
            Delegates to autosar_variable property (CODING_RULE_V2_00017)
        """
        return self.autosar_variable  # Delegates to property

    def setAutosarVariable(self, value: RefType) -> SwVariableRefProxy:
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

    def getMcDataInstance(self) -> McDataInstance:
        """
        AUTOSAR-compliant getter for mcDataInstance.

        Returns:
            The mcDataInstance value

        Note:
            Delegates to mc_data_instance property (CODING_RULE_V2_00017)
        """
        return self.mc_data_instance  # Delegates to property

    def setMcDataInstance(self, value: McDataInstance) -> SwVariableRefProxy:
        """
        AUTOSAR-compliant setter for mcDataInstance with method chaining.

        Args:
            value: The mcDataInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to mc_data_instance property setter (gets validation automatically)
        """
        self.mc_data_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_autosar_variable(self, value: Optional[RefType]) -> SwVariableRefProxy:
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

    def with_mc_data_instance(self, value: Optional[McDataInstance]) -> SwVariableRefProxy:
        """
        Set mcDataInstance and return self for chaining.

        Args:
            value: The mcDataInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_data_instance("value")
        """
        self.mc_data_instance = value  # Use property setter (gets validation)
        return self
