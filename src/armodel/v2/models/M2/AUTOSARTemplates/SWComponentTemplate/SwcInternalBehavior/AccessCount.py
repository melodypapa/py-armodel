"""
AUTOSAR Package - AccessCount

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class AccessCountSet(ARObject):
    """
    This meta-class provides a set of count values evaluated according to the
    rules of a specific countProfile.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount::AccessCountSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 57, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Count value for a AbstractAccessPoint.
        # atpVariation.
        self._accessCount: List["AccessCount"] = []

    @property
    def access_count(self) -> List["AccessCount"]:
        """Get accessCount (Pythonic accessor)."""
        return self._accessCount
        # This attribute defines the name of the count profile used the AccessCount.
        # value numbers.
        self._countProfile: Optional["NameToken"] = None

    @property
    def count_profile(self) -> Optional["NameToken"]:
        """Get countProfile (Pythonic accessor)."""
        return self._countProfile

    @count_profile.setter
    def count_profile(self, value: Optional["NameToken"]) -> None:
        """
        Set countProfile with validation.

        Args:
            value: The countProfile to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._countProfile = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"countProfile must be NameToken or str or None, got {type(value).__name__}"
            )
        self._countProfile = value

    def with_access_count(self, value):
        """
        Set access_count and return self for chaining.

        Args:
            value: The access_count to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access_count("value")
        """
        self.access_count = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessCount(self) -> List["AccessCount"]:
        """
        AUTOSAR-compliant getter for accessCount.

        Returns:
            The accessCount value

        Note:
            Delegates to access_count property (CODING_RULE_V2_00017)
        """
        return self.access_count  # Delegates to property

    def getCountProfile(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for countProfile.

        Returns:
            The countProfile value

        Note:
            Delegates to count_profile property (CODING_RULE_V2_00017)
        """
        return self.count_profile  # Delegates to property

    def setCountProfile(self, value: "NameToken") -> "AccessCountSet":
        """
        AUTOSAR-compliant setter for countProfile with method chaining.

        Args:
            value: The countProfile to set

        Returns:
            self for method chaining

        Note:
            Delegates to count_profile property setter (gets validation automatically)
        """
        self.count_profile = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_count_profile(self, value: Optional["NameToken"]) -> "AccessCountSet":
        """
        Set countProfile and return self for chaining.

        Args:
            value: The countProfile to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_count_profile("value")
        """
        self.count_profile = value  # Use property setter (gets validation)
        return self



class AccessCount(ARObject):
    """
    This meta-class provides one count value for a AbstractAccessPoint.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount::AccessCount

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 57, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AbstractAccessPoint for which the count value is.
        self._accessPoint: Optional["AbstractAccessPoint"] = None

    @property
    def access_point(self) -> Optional["AbstractAccessPoint"]:
        """Get accessPoint (Pythonic accessor)."""
        return self._accessPoint

    @access_point.setter
    def access_point(self, value: Optional["AbstractAccessPoint"]) -> None:
        """
        Set accessPoint with validation.

        Args:
            value: The accessPoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessPoint = None
            return

        if not isinstance(value, AbstractAccessPoint):
            raise TypeError(
                f"accessPoint must be AbstractAccessPoint or None, got {type(value).__name__}"
            )
        self._accessPoint = value
        self._value: Optional["PositiveInteger"] = None

    @property
    def value(self) -> Optional["PositiveInteger"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"value must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessPoint(self) -> "AbstractAccessPoint":
        """
        AUTOSAR-compliant getter for accessPoint.

        Returns:
            The accessPoint value

        Note:
            Delegates to access_point property (CODING_RULE_V2_00017)
        """
        return self.access_point  # Delegates to property

    def setAccessPoint(self, value: "AbstractAccessPoint") -> "AccessCount":
        """
        AUTOSAR-compliant setter for accessPoint with method chaining.

        Args:
            value: The accessPoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to access_point property setter (gets validation automatically)
        """
        self.access_point = value  # Delegates to property setter
        return self

    def getValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "PositiveInteger") -> "AccessCount":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access_point(self, value: Optional["AbstractAccessPoint"]) -> "AccessCount":
        """
        Set accessPoint and return self for chaining.

        Args:
            value: The accessPoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access_point("value")
        """
        self.access_point = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["PositiveInteger"]) -> "AccessCount":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class AbstractAccessPoint(Identifiable, ABC):
    """
    Abstract class indicating an access point from an ExecutableEntity.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount::AbstractAccessPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 57, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 562, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractAccessPoint:
            raise TypeError("AbstractAccessPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the provision of return values for RTE APIs that
        # correspond to the enclosing access point.
        self._returnValue: Optional["RteApiReturnValue"] = None

    @property
    def return_value(self) -> Optional["RteApiReturnValue"]:
        """Get returnValue (Pythonic accessor)."""
        return self._returnValue

    @return_value.setter
    def return_value(self, value: Optional["RteApiReturnValue"]) -> None:
        """
        Set returnValue with validation.

        Args:
            value: The returnValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._returnValue = None
            return

        if not isinstance(value, RteApiReturnValue):
            raise TypeError(
                f"returnValue must be RteApiReturnValue or None, got {type(value).__name__}"
            )
        self._returnValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReturnValue(self) -> "RteApiReturnValue":
        """
        AUTOSAR-compliant getter for returnValue.

        Returns:
            The returnValue value

        Note:
            Delegates to return_value property (CODING_RULE_V2_00017)
        """
        return self.return_value  # Delegates to property

    def setReturnValue(self, value: "RteApiReturnValue") -> "AbstractAccessPoint":
        """
        AUTOSAR-compliant setter for returnValue with method chaining.

        Args:
            value: The returnValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to return_value property setter (gets validation automatically)
        """
        self.return_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_return_value(self, value: Optional["RteApiReturnValue"]) -> "AbstractAccessPoint":
        """
        Set returnValue and return self for chaining.

        Args:
            value: The returnValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_return_value("value")
        """
        self.return_value = value  # Use property setter (gets validation)
        return self


class RteApiReturnValueProvisionEnum(AREnum):
    """
    RteApiReturnValueProvisionEnum enumeration

This meta-class provides values to control how return values from RTE APIs are provided. Aggregated by AbstractAccessPoint.returnValueProvision

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount
    """
    # The RTE API shall not provide a return value.
    noReturnValueProvided = "1"

    # The RTE API shall provide a return value.
    returnValueProvided = "0"
