from abc import ABC
from typing import Optional


class AutosarDataPrototype(DataPrototype, ABC):
    """
    Base class for prototypical roles of an AutosarDataType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::AutosarDataPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 305, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 301, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 306, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2001, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AutosarDataPrototype:
            raise TypeError("AutosarDataPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._type: Optional["AutosarDataType"] = None

    @property
    def type(self) -> Optional["AutosarDataType"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["AutosarDataType"]) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        if not isinstance(value, AutosarDataType):
            raise TypeError(
                f"type must be AutosarDataType or None, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getType(self) -> "AutosarDataType":
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "AutosarDataType") -> "AutosarDataPrototype":
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type(self, value: Optional["AutosarDataType"]) -> "AutosarDataPrototype":
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self
