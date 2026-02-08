from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucCommonAttributes,
)


class EcucAbstractReferenceDef(EcucCommonAttributes, ABC):
    """
    Common class to gather the attributes for the definition of references.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractReferenceDef:
            raise TypeError("EcucAbstractReferenceDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies whether it shall be allowed on the value side to reference value as
                # "AUTO".
        # is "true" it shall be possible to set the "isAuto of the respective reference
                # to "true".
        # This the actual value will not be considered during but will be
                # (re-)calculated by the code stored in the value attribute afterwards.
        # updated values might require a other modules which reference these is "false"
                # it shall not be possible to set the "is of the respective reference to
                # "true".
        # is not present the default is "false".
        self._withAuto: Optional["Boolean"] = None

    @property
    def with_auto(self) -> Optional["Boolean"]:
        """Get withAuto (Pythonic accessor)."""
        return self._withAuto

    @with_auto.setter
    def with_auto(self, value: Optional["Boolean"]) -> None:
        """
        Set withAuto with validation.

        Args:
            value: The withAuto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._withAuto = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"withAuto must be Boolean or None, got {type(value).__name__}"
            )
        self._withAuto = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getWithAuto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for withAuto.

        Returns:
            The withAuto value

        Note:
            Delegates to with_auto property (CODING_RULE_V2_00017)
        """
        return self.with_auto  # Delegates to property

    def setWithAuto(self, value: "Boolean") -> "EcucAbstractReferenceDef":
        """
        AUTOSAR-compliant setter for withAuto with method chaining.

        Args:
            value: The withAuto to set

        Returns:
            self for method chaining

        Note:
            Delegates to with_auto property setter (gets validation automatically)
        """
        self.with_auto = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_with_auto(self, value: Optional["Boolean"]) -> "EcucAbstractReferenceDef":
        """
        Set withAuto and return self for chaining.

        Args:
            value: The withAuto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_with_auto("value")
        """
        self.with_auto = value  # Use property setter (gets validation)
        return self
