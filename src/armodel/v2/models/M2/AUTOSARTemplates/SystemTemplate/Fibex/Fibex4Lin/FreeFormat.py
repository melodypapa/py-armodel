from typing import List


class FreeFormat(FreeFormatEntry):
    """
    Representing freely defined data.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::FreeFormat

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 439, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The integer Value of a freely defined data byte.
        self._byteValue: List["Integer"] = []

    @property
    def byte_value(self) -> List["Integer"]:
        """Get byteValue (Pythonic accessor)."""
        return self._byteValue

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getByteValue(self) -> List["Integer"]:
        """
        AUTOSAR-compliant getter for byteValue.

        Returns:
            The byteValue value

        Note:
            Delegates to byte_value property (CODING_RULE_V2_00017)
        """
        return self.byte_value  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
