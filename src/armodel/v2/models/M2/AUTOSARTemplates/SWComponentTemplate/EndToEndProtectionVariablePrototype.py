from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EndToEndProtectionVariablePrototype(ARObject):
    """
    It is possible to protect the data exchanged between software components.
    For this purpose, for each communication to be protected, the user defines a
    separate EndToEndProtection (specifying a set of protection settings) and
    refers to a variableDataPrototype in the role of sender and to one or many
    variableDataPrototypes in the role of receiver. For details, see EndToEnd
    Library. Caveat: The E2E wrapper approach involves technologies that are not
    subjected to the AUTOSAR standard and is superseded by the superior E2E
    transformer approach (which is fully standardized by AUTOSAR). Hence, new
    projects (without legacy constraints due to carry-over parts) shall use the
    fully standardized E2E transformer approach.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 215, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2022, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # supported for this use case.
        # by: VariableDataPrototypeIn.
        self._receiver: List[RefType] = []

    @property
    def receiver(self) -> List[RefType]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # optional if an ecu extract is provided and the part of the extract.
        # by: VariableDataPrototypeIn.
        self._sender: RefType = None

    @property
    def sender(self) -> RefType:
        """Get sender (Pythonic accessor)."""
        return self._sender

    @sender.setter
    def sender(self, value: RefType) -> None:
        """
        Set sender with validation.

        Args:
            value: The sender to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sender = None
            return

        self._sender = value
        # This serves as part of the split key in case of more than is aggregated bound
        # model.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    def with_receiver(self, value):
        """
        Set receiver and return self for chaining.

        Args:
            value: The receiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receiver("value")
        """
        self.receiver = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReceiver(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getSender(self) -> RefType:
        """
        AUTOSAR-compliant getter for sender.

        Returns:
            The sender value

        Note:
            Delegates to sender property (CODING_RULE_V2_00017)
        """
        return self.sender  # Delegates to property

    def setSender(self, value: RefType) -> "EndToEndProtectionVariablePrototype":
        """
        AUTOSAR-compliant setter for sender with method chaining.

        Args:
            value: The sender to set

        Returns:
            self for method chaining

        Note:
            Delegates to sender property setter (gets validation automatically)
        """
        self.sender = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "EndToEndProtectionVariablePrototype":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sender(self, value: Optional[RefType]) -> "EndToEndProtectionVariablePrototype":
        """
        Set sender and return self for chaining.

        Args:
            value: The sender to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sender("value")
        """
        self.sender = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "EndToEndProtectionVariablePrototype":
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self
