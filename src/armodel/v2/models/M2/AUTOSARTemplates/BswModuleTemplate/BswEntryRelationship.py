from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BswEntryRelationship(ARObject):
    """
    Describes a relationship between two BswModuleEntrys and the type of
    relationship.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswEntryRelationship

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 51, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 52, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Denotes the type of the relationship.
        # Tags: xml.
        # sequenceOffset=5 Type.
        self._bswEntry: Optional["BswEntryRelationship"] = None

    @property
    def bsw_entry(self) -> Optional["BswEntryRelationship"]:
        """Get bswEntry (Pythonic accessor)."""
        return self._bswEntry

    @bsw_entry.setter
    def bsw_entry(self, value: Optional["BswEntryRelationship"]) -> None:
        """
        Set bswEntry with validation.

        Args:
            value: The bswEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswEntry = None
            return

        if not isinstance(value, BswEntryRelationship):
            raise TypeError(
                f"bswEntry must be BswEntryRelationship or None, got {type(value).__name__}"
            )
        self._bswEntry = value
        # Type of relationship that refers to the abstract BswModule notice that in
        # this case the bswEntry be set to drivedFrom.
        self._from: Optional["BswModuleEntry"] = None

    @property
    def from(self) -> Optional["BswModuleEntry"]:
        """Get from (Pythonic accessor)."""
        return self._from

    @from.setter
    def from(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set from with validation.

        Args:
            value: The from to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._from = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"from must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._from = value
        # Type of relationship that refers to the concrete Bsw.
        self._to: Optional["BswModuleEntry"] = None

    @property
    def to(self) -> Optional["BswModuleEntry"]:
        """Get to (Pythonic accessor)."""
        return self._to

    @to.setter
    def to(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set to with validation.

        Args:
            value: The to to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._to = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"to must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._to = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswEntry(self) -> "BswEntryRelationship":
        """
        AUTOSAR-compliant getter for bswEntry.

        Returns:
            The bswEntry value

        Note:
            Delegates to bsw_entry property (CODING_RULE_V2_00017)
        """
        return self.bsw_entry  # Delegates to property

    def setBswEntry(self, value: "BswEntryRelationship") -> "BswEntryRelationship":
        """
        AUTOSAR-compliant setter for bswEntry with method chaining.

        Args:
            value: The bswEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_entry property setter (gets validation automatically)
        """
        self.bsw_entry = value  # Delegates to property setter
        return self

    def getFrom(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for from.

        Returns:
            The from value

        Note:
            Delegates to from property (CODING_RULE_V2_00017)
        """
        return self.from  # Delegates to property

    def setFrom(self, value: "BswModuleEntry") -> "BswEntryRelationship":
        """
        AUTOSAR-compliant setter for from with method chaining.

        Args:
            value: The from to set

        Returns:
            self for method chaining

        Note:
            Delegates to from property setter (gets validation automatically)
        """
        self.from = value  # Delegates to property setter
        return self

    def getTo(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for to.

        Returns:
            The to value

        Note:
            Delegates to to property (CODING_RULE_V2_00017)
        """
        return self.to  # Delegates to property

    def setTo(self, value: "BswModuleEntry") -> "BswEntryRelationship":
        """
        AUTOSAR-compliant setter for to with method chaining.

        Args:
            value: The to to set

        Returns:
            self for method chaining

        Note:
            Delegates to to property setter (gets validation automatically)
        """
        self.to = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_entry(self, value: Optional["BswEntryRelationship"]) -> "BswEntryRelationship":
        """
        Set bswEntry and return self for chaining.

        Args:
            value: The bswEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_entry("value")
        """
        self.bsw_entry = value  # Use property setter (gets validation)
        return self

    def with_from(self, value: Optional["BswModuleEntry"]) -> "BswEntryRelationship":
        """
        Set from and return self for chaining.

        Args:
            value: The from to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_from("value")
        """
        self.from = value  # Use property setter (gets validation)
        return self

    def with_to(self, value: Optional["BswModuleEntry"]) -> "BswEntryRelationship":
        """
        Set to and return self for chaining.

        Args:
            value: The to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_to("value")
        """
        self.to = value  # Use property setter (gets validation)
        return self
