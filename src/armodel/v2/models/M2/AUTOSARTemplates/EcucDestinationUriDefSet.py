from typing import List


class EcucDestinationUriDefSet(ARElement):
    """
    This class represents a list of EcucDestinationUriDefs.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDestinationUriDefSet

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 82, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular EcucDestinationUriDef.
        self._destinationUriDef: List["EcucDestinationUriDef"] = []

    @property
    def destination_uri_def(self) -> List["EcucDestinationUriDef"]:
        """Get destinationUriDef (Pythonic accessor)."""
        return self._destinationUriDef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationUriDef(self) -> List["EcucDestinationUriDef"]:
        """
        AUTOSAR-compliant getter for destinationUriDef.

        Returns:
            The destinationUriDef value

        Note:
            Delegates to destination_uri_def property (CODING_RULE_V2_00017)
        """
        return self.destination_uri_def  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
