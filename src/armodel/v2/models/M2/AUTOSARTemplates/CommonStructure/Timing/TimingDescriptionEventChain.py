from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescription,
)


class TimingDescriptionEventChain(TimingDescription):
    """
    An event chain describes the causal order for a set of functionally
    dependent timing events. Each event chain has a well defined stimulus and
    response, which describe its start and end point. Furthermore, it can be
    hierarchically decomposed into an arbitrary number of sub-chains, so called
    event chain segments.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 40, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # States whether the scheduled entities in an LET interval use pipelined
                # execution or not i.
        # e.
        # "permitted If TRUE, then the scheduled entities pipelining.
        # If FALSE or undefined, no.
        self._isPipelining: Optional["Boolean"] = None

    @property
    def is_pipelining(self) -> Optional["Boolean"]:
        """Get isPipelining (Pythonic accessor)."""
        return self._isPipelining

    @is_pipelining.setter
    def is_pipelining(self, value: Optional["Boolean"]) -> None:
        """
        Set isPipelining with validation.

        Args:
            value: The isPipelining to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isPipelining = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isPipelining must be Boolean or None, got {type(value).__name__}"
            )
        self._isPipelining = value
        # The response event representing the point in time where chain is terminated.
        self._response: Optional["TimingDescriptionEvent"] = None

    @property
    def response(self) -> Optional["TimingDescriptionEvent"]:
        """Get response (Pythonic accessor)."""
        return self._response

    @response.setter
    def response(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set response with validation.

        Args:
            value: The response to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._response = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"response must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._response = value
        # A composed event chain consists of an arbitrary number sub-chains.
        self._segment: List["TimingDescriptionEvent"] = []

    @property
    def segment(self) -> List["TimingDescriptionEvent"]:
        """Get segment (Pythonic accessor)."""
        return self._segment
        # The stimulus event representing the point in time where chain is activated.
        self._stimulus: Optional["TimingDescriptionEvent"] = None

    @property
    def stimulus(self) -> Optional["TimingDescriptionEvent"]:
        """Get stimulus (Pythonic accessor)."""
        return self._stimulus

    @stimulus.setter
    def stimulus(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set stimulus with validation.

        Args:
            value: The stimulus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stimulus = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"stimulus must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._stimulus = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIsPipelining(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isPipelining.

        Returns:
            The isPipelining value

        Note:
            Delegates to is_pipelining property (CODING_RULE_V2_00017)
        """
        return self.is_pipelining  # Delegates to property

    def setIsPipelining(self, value: "Boolean") -> "TimingDescriptionEventChain":
        """
        AUTOSAR-compliant setter for isPipelining with method chaining.

        Args:
            value: The isPipelining to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_pipelining property setter (gets validation automatically)
        """
        self.is_pipelining = value  # Delegates to property setter
        return self

    def getResponse(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for response.

        Returns:
            The response value

        Note:
            Delegates to response property (CODING_RULE_V2_00017)
        """
        return self.response  # Delegates to property

    def setResponse(self, value: "TimingDescriptionEvent") -> "TimingDescriptionEventChain":
        """
        AUTOSAR-compliant setter for response with method chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Note:
            Delegates to response property setter (gets validation automatically)
        """
        self.response = value  # Delegates to property setter
        return self

    def getSegment(self) -> List["TimingDescriptionEvent"]:
        """
        AUTOSAR-compliant getter for segment.

        Returns:
            The segment value

        Note:
            Delegates to segment property (CODING_RULE_V2_00017)
        """
        return self.segment  # Delegates to property

    def getStimulus(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for stimulus.

        Returns:
            The stimulus value

        Note:
            Delegates to stimulus property (CODING_RULE_V2_00017)
        """
        return self.stimulus  # Delegates to property

    def setStimulus(self, value: "TimingDescriptionEvent") -> "TimingDescriptionEventChain":
        """
        AUTOSAR-compliant setter for stimulus with method chaining.

        Args:
            value: The stimulus to set

        Returns:
            self for method chaining

        Note:
            Delegates to stimulus property setter (gets validation automatically)
        """
        self.stimulus = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_pipelining(self, value: Optional["Boolean"]) -> "TimingDescriptionEventChain":
        """
        Set isPipelining and return self for chaining.

        Args:
            value: The isPipelining to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_pipelining("value")
        """
        self.is_pipelining = value  # Use property setter (gets validation)
        return self

    def with_response(self, value: Optional["TimingDescriptionEvent"]) -> "TimingDescriptionEventChain":
        """
        Set response and return self for chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response("value")
        """
        self.response = value  # Use property setter (gets validation)
        return self

    def with_stimulus(self, value: Optional["TimingDescriptionEvent"]) -> "TimingDescriptionEventChain":
        """
        Set stimulus and return self for chaining.

        Args:
            value: The stimulus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stimulus("value")
        """
        self.stimulus = value  # Use property setter (gets validation)
        return self
