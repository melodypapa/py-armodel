from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PortPrototype,
)


class AbstractRequiredPortPrototype(PortPrototype, ABC):
    """
    This abstract class provides the ability to become a required PortPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 67, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 204, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 422, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractRequiredPortPrototype:
            raise TypeError("AbstractRequiredPortPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Required communication attributes, one for each element.
        self._requiredCom: List["RPortComSpec"] = []

    @property
    def required_com(self) -> List["RPortComSpec"]:
        """Get requiredCom (Pythonic accessor)."""
        return self._requiredCom

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequiredCom(self) -> List["RPortComSpec"]:
        """
        AUTOSAR-compliant getter for requiredCom.

        Returns:
            The requiredCom value

        Note:
            Delegates to required_com property (CODING_RULE_V2_00017)
        """
        return self.required_com  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
