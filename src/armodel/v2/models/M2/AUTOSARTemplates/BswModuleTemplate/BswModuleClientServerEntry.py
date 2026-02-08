from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class BswModuleClientServerEntry(Referrable):
    """
    This meta-class represents a single API entry into the BSW module or cluster
    that has the ability to be called in client-server fashion via the BSW
    Scheduler. In this regard it is more special than BswModuleEntry and can be
    seen as a wrapper around the Bsw ModuleEntry to which it refers (property
    encapsulatedEntry).

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswModuleClientServerEntry

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 53, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The underlying BswModuleEntry.
        # xml.
        # sequenceOffset=5.
        self._encapsulated: Optional["BswModuleEntry"] = None

    @property
    def encapsulated(self) -> Optional["BswModuleEntry"]:
        """Get encapsulated (Pythonic accessor)."""
        return self._encapsulated

    @encapsulated.setter
    def encapsulated(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set encapsulated with validation.

        Args:
            value: The encapsulated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._encapsulated = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"encapsulated must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._encapsulated = value
        # Reentrancy from the viewpoint of clients invoking the the BSW Scheduler:
                # Enables the service to be invoked again, before has finished.
        # It is prohibited to invoke the service again before finished.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._isReentrant: Optional["Boolean"] = None

    @property
    def is_reentrant(self) -> Optional["Boolean"]:
        """Get isReentrant (Pythonic accessor)."""
        return self._isReentrant

    @is_reentrant.setter
    def is_reentrant(self, value: Optional["Boolean"]) -> None:
        """
        Set isReentrant with validation.

        Args:
            value: The isReentrant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isReentrant = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isReentrant must be Boolean or None, got {type(value).__name__}"
            )
        self._isReentrant = value
        # Synchronicity from the viewpoint of clients invoking the the BSW Scheduler:
                # This calls a synchronous service, i.
        # e.
        # the service when the call returns.
        # The service (on semantical level) may not be the call returns.
        self._isSynchronous: Optional["Boolean"] = None

    @property
    def is_synchronous(self) -> Optional["Boolean"]:
        """Get isSynchronous (Pythonic accessor)."""
        return self._isSynchronous

    @is_synchronous.setter
    def is_synchronous(self, value: Optional["Boolean"]) -> None:
        """
        Set isSynchronous with validation.

        Args:
            value: The isSynchronous to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isSynchronous = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isSynchronous must be Boolean or None, got {type(value).__name__}"
            )
        self._isSynchronous = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEncapsulated(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for encapsulated.

        Returns:
            The encapsulated value

        Note:
            Delegates to encapsulated property (CODING_RULE_V2_00017)
        """
        return self.encapsulated  # Delegates to property

    def setEncapsulated(self, value: "BswModuleEntry") -> "BswModuleClientServerEntry":
        """
        AUTOSAR-compliant setter for encapsulated with method chaining.

        Args:
            value: The encapsulated to set

        Returns:
            self for method chaining

        Note:
            Delegates to encapsulated property setter (gets validation automatically)
        """
        self.encapsulated = value  # Delegates to property setter
        return self

    def getIsReentrant(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isReentrant.

        Returns:
            The isReentrant value

        Note:
            Delegates to is_reentrant property (CODING_RULE_V2_00017)
        """
        return self.is_reentrant  # Delegates to property

    def setIsReentrant(self, value: "Boolean") -> "BswModuleClientServerEntry":
        """
        AUTOSAR-compliant setter for isReentrant with method chaining.

        Args:
            value: The isReentrant to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_reentrant property setter (gets validation automatically)
        """
        self.is_reentrant = value  # Delegates to property setter
        return self

    def getIsSynchronous(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isSynchronous.

        Returns:
            The isSynchronous value

        Note:
            Delegates to is_synchronous property (CODING_RULE_V2_00017)
        """
        return self.is_synchronous  # Delegates to property

    def setIsSynchronous(self, value: "Boolean") -> "BswModuleClientServerEntry":
        """
        AUTOSAR-compliant setter for isSynchronous with method chaining.

        Args:
            value: The isSynchronous to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_synchronous property setter (gets validation automatically)
        """
        self.is_synchronous = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_encapsulated(self, value: Optional["BswModuleEntry"]) -> "BswModuleClientServerEntry":
        """
        Set encapsulated and return self for chaining.

        Args:
            value: The encapsulated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_encapsulated("value")
        """
        self.encapsulated = value  # Use property setter (gets validation)
        return self

    def with_is_reentrant(self, value: Optional["Boolean"]) -> "BswModuleClientServerEntry":
        """
        Set isReentrant and return self for chaining.

        Args:
            value: The isReentrant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_reentrant("value")
        """
        self.is_reentrant = value  # Use property setter (gets validation)
        return self

    def with_is_synchronous(self, value: Optional["Boolean"]) -> "BswModuleClientServerEntry":
        """
        Set isSynchronous and return self for chaining.

        Args:
            value: The isSynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_synchronous("value")
        """
        self.is_synchronous = value  # Use property setter (gets validation)
        return self
