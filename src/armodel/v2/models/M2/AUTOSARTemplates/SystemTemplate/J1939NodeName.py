from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class J1939NodeName(ARObject):
    """
    This element contains attributes to configure the J1939NmNode NAME.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 691, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Arbitrary Address Capable field of the NAME of this node.
        self._arbitrary: Optional["Boolean"] = None

    @property
    def arbitrary(self) -> Optional["Boolean"]:
        """Get arbitrary (Pythonic accessor)."""
        return self._arbitrary

    @arbitrary.setter
    def arbitrary(self, value: Optional["Boolean"]) -> None:
        """
        Set arbitrary with validation.

        Args:
            value: The arbitrary to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arbitrary = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"arbitrary must be Boolean or None, got {type(value).__name__}"
            )
        self._arbitrary = value
        # ECU Instance field of the NAME of this node.
        self._ecuInstance: Optional["Integer"] = None

    @property
    def ecu_instance(self) -> Optional["Integer"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["Integer"]) -> None:
        """
        Set ecuInstance with validation.

        Args:
            value: The ecuInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"ecuInstance must be Integer or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # Function field of the NAME of this node.
        self._function: Optional["Integer"] = None

    @property
    def function(self) -> Optional["Integer"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["Integer"]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"function must be Integer or None, got {type(value).__name__}"
            )
        self._function = value
        # Function Instance field of the NAME of this node.
        self._functionInstance: Optional["Integer"] = None

    @property
    def function_instance(self) -> Optional["Integer"]:
        """Get functionInstance (Pythonic accessor)."""
        return self._functionInstance

    @function_instance.setter
    def function_instance(self, value: Optional["Integer"]) -> None:
        """
        Set functionInstance with validation.

        Args:
            value: The functionInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionInstance = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"functionInstance must be Integer or None, got {type(value).__name__}"
            )
        self._functionInstance = value
        # Identity Number field of the NAME of this node.
        self._identitiyNumber: Optional["Integer"] = None

    @property
    def identitiy_number(self) -> Optional["Integer"]:
        """Get identitiyNumber (Pythonic accessor)."""
        return self._identitiyNumber

    @identitiy_number.setter
    def identitiy_number(self, value: Optional["Integer"]) -> None:
        """
        Set identitiyNumber with validation.

        Args:
            value: The identitiyNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identitiyNumber = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"identitiyNumber must be Integer or None, got {type(value).__name__}"
            )
        self._identitiyNumber = value
        # Industry Group field of the NAME of this node.
        self._industryGroup: Optional["Integer"] = None

    @property
    def industry_group(self) -> Optional["Integer"]:
        """Get industryGroup (Pythonic accessor)."""
        return self._industryGroup

    @industry_group.setter
    def industry_group(self, value: Optional["Integer"]) -> None:
        """
        Set industryGroup with validation.

        Args:
            value: The industryGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._industryGroup = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"industryGroup must be Integer or None, got {type(value).__name__}"
            )
        self._industryGroup = value
        # Manufacturer Code field of the NAME of this node.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._manufacturerCode: Optional["Integer"] = None

    @property
    def manufacturer_code(self) -> Optional["Integer"]:
        """Get manufacturerCode (Pythonic accessor)."""
        return self._manufacturerCode

    @manufacturer_code.setter
    def manufacturer_code(self, value: Optional["Integer"]) -> None:
        """
        Set manufacturerCode with validation.

        Args:
            value: The manufacturerCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._manufacturerCode = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"manufacturerCode must be Integer or None, got {type(value).__name__}"
            )
        self._manufacturerCode = value
        # Vehicle System Instance field of the NAME of this node.
        self._vehicleSystem: Optional["Integer"] = None

    @property
    def vehicle_system(self) -> Optional["Integer"]:
        """Get vehicleSystem (Pythonic accessor)."""
        return self._vehicleSystem

    @vehicle_system.setter
    def vehicle_system(self, value: Optional["Integer"]) -> None:
        """
        Set vehicleSystem with validation.

        Args:
            value: The vehicleSystem to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vehicleSystem = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"vehicleSystem must be Integer or None, got {type(value).__name__}"
            )
        self._vehicleSystem = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArbitrary(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for arbitrary.

        Returns:
            The arbitrary value

        Note:
            Delegates to arbitrary property (CODING_RULE_V2_00017)
        """
        return self.arbitrary  # Delegates to property

    def setArbitrary(self, value: "Boolean") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for arbitrary with method chaining.

        Args:
            value: The arbitrary to set

        Returns:
            self for method chaining

        Note:
            Delegates to arbitrary property setter (gets validation automatically)
        """
        self.arbitrary = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> "Integer":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "Integer") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getFunction(self) -> "Integer":
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: "Integer") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    def getFunctionInstance(self) -> "Integer":
        """
        AUTOSAR-compliant getter for functionInstance.

        Returns:
            The functionInstance value

        Note:
            Delegates to function_instance property (CODING_RULE_V2_00017)
        """
        return self.function_instance  # Delegates to property

    def setFunctionInstance(self, value: "Integer") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for functionInstance with method chaining.

        Args:
            value: The functionInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_instance property setter (gets validation automatically)
        """
        self.function_instance = value  # Delegates to property setter
        return self

    def getIdentitiyNumber(self) -> "Integer":
        """
        AUTOSAR-compliant getter for identitiyNumber.

        Returns:
            The identitiyNumber value

        Note:
            Delegates to identitiy_number property (CODING_RULE_V2_00017)
        """
        return self.identitiy_number  # Delegates to property

    def setIdentitiyNumber(self, value: "Integer") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for identitiyNumber with method chaining.

        Args:
            value: The identitiyNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to identitiy_number property setter (gets validation automatically)
        """
        self.identitiy_number = value  # Delegates to property setter
        return self

    def getIndustryGroup(self) -> "Integer":
        """
        AUTOSAR-compliant getter for industryGroup.

        Returns:
            The industryGroup value

        Note:
            Delegates to industry_group property (CODING_RULE_V2_00017)
        """
        return self.industry_group  # Delegates to property

    def setIndustryGroup(self, value: "Integer") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for industryGroup with method chaining.

        Args:
            value: The industryGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to industry_group property setter (gets validation automatically)
        """
        self.industry_group = value  # Delegates to property setter
        return self

    def getManufacturerCode(self) -> "Integer":
        """
        AUTOSAR-compliant getter for manufacturerCode.

        Returns:
            The manufacturerCode value

        Note:
            Delegates to manufacturer_code property (CODING_RULE_V2_00017)
        """
        return self.manufacturer_code  # Delegates to property

    def setManufacturerCode(self, value: "Integer") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for manufacturerCode with method chaining.

        Args:
            value: The manufacturerCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to manufacturer_code property setter (gets validation automatically)
        """
        self.manufacturer_code = value  # Delegates to property setter
        return self

    def getVehicleSystem(self) -> "Integer":
        """
        AUTOSAR-compliant getter for vehicleSystem.

        Returns:
            The vehicleSystem value

        Note:
            Delegates to vehicle_system property (CODING_RULE_V2_00017)
        """
        return self.vehicle_system  # Delegates to property

    def setVehicleSystem(self, value: "Integer") -> "J1939NodeName":
        """
        AUTOSAR-compliant setter for vehicleSystem with method chaining.

        Args:
            value: The vehicleSystem to set

        Returns:
            self for method chaining

        Note:
            Delegates to vehicle_system property setter (gets validation automatically)
        """
        self.vehicle_system = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_arbitrary(self, value: Optional["Boolean"]) -> "J1939NodeName":
        """
        Set arbitrary and return self for chaining.

        Args:
            value: The arbitrary to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arbitrary("value")
        """
        self.arbitrary = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["Integer"]) -> "J1939NodeName":
        """
        Set ecuInstance and return self for chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_function(self, value: Optional["Integer"]) -> "J1939NodeName":
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

    def with_function_instance(self, value: Optional["Integer"]) -> "J1939NodeName":
        """
        Set functionInstance and return self for chaining.

        Args:
            value: The functionInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_instance("value")
        """
        self.function_instance = value  # Use property setter (gets validation)
        return self

    def with_identitiy_number(self, value: Optional["Integer"]) -> "J1939NodeName":
        """
        Set identitiyNumber and return self for chaining.

        Args:
            value: The identitiyNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identitiy_number("value")
        """
        self.identitiy_number = value  # Use property setter (gets validation)
        return self

    def with_industry_group(self, value: Optional["Integer"]) -> "J1939NodeName":
        """
        Set industryGroup and return self for chaining.

        Args:
            value: The industryGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_industry_group("value")
        """
        self.industry_group = value  # Use property setter (gets validation)
        return self

    def with_manufacturer_code(self, value: Optional["Integer"]) -> "J1939NodeName":
        """
        Set manufacturerCode and return self for chaining.

        Args:
            value: The manufacturerCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_manufacturer_code("value")
        """
        self.manufacturer_code = value  # Use property setter (gets validation)
        return self

    def with_vehicle_system(self, value: Optional["Integer"]) -> "J1939NodeName":
        """
        Set vehicleSystem and return self for chaining.

        Args:
            value: The vehicleSystem to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vehicle_system("value")
        """
        self.vehicle_system = value  # Use property setter (gets validation)
        return self
