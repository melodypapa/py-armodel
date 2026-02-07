from abc import ABC
from typing import Optional


class EcucAbstractInternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """
    Common abstract class to gather attributes for internal references (where
    the destination is located in the Ecu Configuration Description). (cid:53)
    71 of 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration Specification of
    ECU Configuration AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractInternalReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractInternalReferenceDef:
            raise TypeError("EcucAbstractInternalReferenceDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If this attribute is set to true the implementation of the is done using a
        # Symbolic Name defined by the container according to TPS_ECUC_02108.
        self._requires: Optional["Boolean"] = None

    @property
    def requires(self) -> Optional["Boolean"]:
        """Get requires (Pythonic accessor)."""
        return self._requires

    @requires.setter
    def requires(self, value: Optional["Boolean"]) -> None:
        """
        Set requires with validation.

        Args:
            value: The requires to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requires = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"requires must be Boolean or None, got {type(value).__name__}"
            )
        self._requires = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequires(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for requires.

        Returns:
            The requires value

        Note:
            Delegates to requires property (CODING_RULE_V2_00017)
        """
        return self.requires  # Delegates to property

    def setRequires(self, value: "Boolean") -> "EcucAbstractInternalReferenceDef":
        """
        AUTOSAR-compliant setter for requires with method chaining.

        Args:
            value: The requires to set

        Returns:
            self for method chaining

        Note:
            Delegates to requires property setter (gets validation automatically)
        """
        self.requires = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_requires(self, value: Optional["Boolean"]) -> "EcucAbstractInternalReferenceDef":
        """
        Set requires and return self for chaining.

        Args:
            value: The requires to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requires("value")
        """
        self.requires = value  # Use property setter (gets validation)
        return self
