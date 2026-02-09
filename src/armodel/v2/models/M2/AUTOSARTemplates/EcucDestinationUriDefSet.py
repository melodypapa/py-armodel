from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class EcucDestinationUriDefSet(ARElement):
    """
    This class represents a list of EcucDestinationUriDefs.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

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

    def with_destination_uri_def(self, value):
        """
        Set destination_uri_def and return self for chaining.

        Args:
            value: The destination_uri_def to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_uri_def("value")
        """
        self.destination_uri_def = value  # Use property setter (gets validation)
        return self

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
