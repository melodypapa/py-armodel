from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    AtomicSwComponentType,
    HwDescriptionEntity,
)


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """
    The ECUAbstraction is a special AtomicSwComponentType that resides between a
    software-component that wants to access ECU periphery and the
    Microcontroller Abstraction. The EcuAbstractionSw ComponentType introduces
    the possibility to link from the software representation to its hardware
    description provided by the ECU Resource Template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::EcuAbstractionSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 313, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 647, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2020, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 222, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference from the EcuAbstractionComponentType to the of the used HwElements.
        self._hardware: List["HwDescriptionEntity"] = []

    @property
    def hardware(self) -> List["HwDescriptionEntity"]:
        """Get hardware (Pythonic accessor)."""
        return self._hardware

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHardware(self) -> List["HwDescriptionEntity"]:
        """
        AUTOSAR-compliant getter for hardware.

        Returns:
            The hardware value

        Note:
            Delegates to hardware property (CODING_RULE_V2_00017)
        """
        return self.hardware  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
