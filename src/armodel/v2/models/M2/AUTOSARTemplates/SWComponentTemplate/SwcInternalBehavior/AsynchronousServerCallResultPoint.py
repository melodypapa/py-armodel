from typing import Optional


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    """
    If a RunnableEntity owns a AsynchronousServerCallResultPoint it is entitled
    to get the result of the referenced AsynchronousServerCallPoint. If it is
    associated with AsynchronousServerCallReturnsEvent, this RTEEvent notifies
    the completion of the required ClientServerOperation or a timeout. The
    occurrence of this event can either unblock a WaitPoint or can lead to the
    invocation of a RunnableEntity.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall::AsynchronousServerCallResultPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 304, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 581, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced Asynchronous Server Call Point defines the asynchronous server
        # call from which the results are.
        self._asynchronous: Optional["AsynchronousServer"] = None

    @property
    def asynchronous(self) -> Optional["AsynchronousServer"]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, value: Optional["AsynchronousServer"]) -> None:
        """
        Set asynchronous with validation.

        Args:
            value: The asynchronous to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._asynchronous = None
            return

        if not isinstance(value, AsynchronousServer):
            raise TypeError(
                f"asynchronous must be AsynchronousServer or None, got {type(value).__name__}"
            )
        self._asynchronous = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAsynchronous(self) -> "AsynchronousServer":
        """
        AUTOSAR-compliant getter for asynchronous.

        Returns:
            The asynchronous value

        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def setAsynchronous(self, value: "AsynchronousServer") -> "AsynchronousServerCallResultPoint":
        """
        AUTOSAR-compliant setter for asynchronous with method chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Note:
            Delegates to asynchronous property setter (gets validation automatically)
        """
        self.asynchronous = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_asynchronous(self, value: Optional["AsynchronousServer"]) -> "AsynchronousServerCallResultPoint":
        """
        Set asynchronous and return self for chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_asynchronous("value")
        """
        self.asynchronous = value  # Use property setter (gets validation)
        return self
