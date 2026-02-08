from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AtomicSwComponentType,
)


class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    """
    The ComplexDeviceDriverSwComponentType is a special AtomicSwComponentType
    that has direct access to hardware on an ECU and which is therefore linked
    to a specific ECU or specific hardware. The
    ComplexDeviceDriverSwComponentType introduces the possibility to link from
    the software representation to its hardware description provided by the ECU
    Resource Template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 310, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 648, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2010, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 218, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference from the ComplexDeviceDriverSwComponent to the description of the
        # used HwElements.
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
