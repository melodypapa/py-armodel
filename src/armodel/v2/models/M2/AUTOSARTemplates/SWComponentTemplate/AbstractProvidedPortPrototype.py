from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortPrototype import (
    PortPrototype,
)


class AbstractProvidedPortPrototype(PortPrototype, ABC):
    """
    This abstract class provides the ability to become a provided PortPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::AbstractProvidedPortPrototype

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 67, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractProvidedPortPrototype:
            raise TypeError("AbstractProvidedPortPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Provided communication attributes per interface element element or
        # operation).
        self._providedCom: List["PPortComSpec"] = []

    @property
    def provided_com(self) -> List["PPortComSpec"]:
        """Get providedCom (Pythonic accessor)."""
        return self._providedCom

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvidedCom(self) -> List["PPortComSpec"]:
        """
        AUTOSAR-compliant getter for providedCom.

        Returns:
            The providedCom value

        Note:
            Delegates to provided_com property (CODING_RULE_V2_00017)
        """
        return self.provided_com  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
