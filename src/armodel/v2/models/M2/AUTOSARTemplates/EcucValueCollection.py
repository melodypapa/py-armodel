from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class EcucValueCollection(ARElement):
    """
    This represents the anchor point of the ECU configuration description.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucValueCollection

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 108, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2022, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 222, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # References to the configuration of individual software that are present on
                # this ECU.
        # atpVariation.
        self._ecucValue: List["EcucModule"] = []

    @property
    def ecuc_value(self) -> List["EcucModule"]:
        """Get ecucValue (Pythonic accessor)."""
        return self._ecucValue
        # Represents the extract of the System Configuration that is the ECU configured
        # with that ECU.
        self._ecuExtract: Optional["System"] = None

    @property
    def ecu_extract(self) -> Optional["System"]:
        """Get ecuExtract (Pythonic accessor)."""
        return self._ecuExtract

    @ecu_extract.setter
    def ecu_extract(self, value: Optional["System"]) -> None:
        """
        Set ecuExtract with validation.

        Args:
            value: The ecuExtract to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuExtract = None
            return

        if not isinstance(value, System):
            raise TypeError(
                f"ecuExtract must be System or None, got {type(value).__name__}"
            )
        self._ecuExtract = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucValue(self) -> List["EcucModule"]:
        """
        AUTOSAR-compliant getter for ecucValue.

        Returns:
            The ecucValue value

        Note:
            Delegates to ecuc_value property (CODING_RULE_V2_00017)
        """
        return self.ecuc_value  # Delegates to property

    def getEcuExtract(self) -> "System":
        """
        AUTOSAR-compliant getter for ecuExtract.

        Returns:
            The ecuExtract value

        Note:
            Delegates to ecu_extract property (CODING_RULE_V2_00017)
        """
        return self.ecu_extract  # Delegates to property

    def setEcuExtract(self, value: "System") -> "EcucValueCollection":
        """
        AUTOSAR-compliant setter for ecuExtract with method chaining.

        Args:
            value: The ecuExtract to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_extract property setter (gets validation automatically)
        """
        self.ecu_extract = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_extract(self, value: Optional["System"]) -> "EcucValueCollection":
        """
        Set ecuExtract and return self for chaining.

        Args:
            value: The ecuExtract to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_extract("value")
        """
        self.ecu_extract = value  # Use property setter (gets validation)
        return self
