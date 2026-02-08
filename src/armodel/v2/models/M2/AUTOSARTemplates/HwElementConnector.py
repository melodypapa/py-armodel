from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable

    RefType,
)


class HwElementConnector(Describable):
    """
    This meta-class represents the ability to connect two hardware elements. The
    details of the connection can be refined by hwPinGroupConnection.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 21, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association connects two hardware elements.
        self._hwElement: List["HwElement"] = []

    @property
    def hw_element(self) -> List["HwElement"]:
        """Get hwElement (Pythonic accessor)."""
        return self._hwElement
        # This represents one particular connection between two pins.
        # This connection shall be used if to be described but no description
                # connection between the hierarchical composition of HwPinGroupConnector) is
                # required.
        # atpVariation.
        self._hwPin: List["HwPinConnector"] = []

    @property
    def hw_pin(self) -> List["HwPinConnector"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin
        # This represents one particular connection between two pin groups.
        # atpVariation.
        self._hwPinGroup: List[RefType] = []

    @property
    def hw_pin_group(self) -> List[RefType]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwElement(self) -> List["HwElement"]:
        """
        AUTOSAR-compliant getter for hwElement.

        Returns:
            The hwElement value

        Note:
            Delegates to hw_element property (CODING_RULE_V2_00017)
        """
        return self.hw_element  # Delegates to property

    def getHwPin(self) -> List["HwPinConnector"]:
        """
        AUTOSAR-compliant getter for hwPin.

        Returns:
            The hwPin value

        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    def getHwPinGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for hwPinGroup.

        Returns:
            The hwPinGroup value

        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
