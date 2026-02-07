from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwitchStreamFilterEntry(Identifiable):
    """
    Defines a Stream Filter Entry.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamFilterEntry
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 141, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the Asynchronous Traffic Shaper (ATS).
        # Tags: atp.
        # Status=candidate Shaper.
        self._asynchronous: Optional["CouplingPort"] = None

    @property
    def asynchronous(self) -> Optional["CouplingPort"]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, value: Optional["CouplingPort"]) -> None:
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

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"asynchronous must be CouplingPort or None, got {type(value).__name__}"
            )
        self._asynchronous = value
        # Defines the Priority of this Stream Filter Entry.
        self._filterPriority: Optional["PositiveInteger"] = None

    @property
    def filter_priority(self) -> Optional["PositiveInteger"]:
        """Get filterPriority (Pythonic accessor)."""
        return self._filterPriority

    @filter_priority.setter
    def filter_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set filterPriority with validation.
        
        Args:
            value: The filterPriority to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"filterPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._filterPriority = value
        # Reference to a Flow Metering Entry.
        # atp.
        # Status=candidate.
        self._flowMetering: Optional["SwitchFlowMetering"] = None

    @property
    def flow_metering(self) -> Optional["SwitchFlowMetering"]:
        """Get flowMetering (Pythonic accessor)."""
        return self._flowMetering

    @flow_metering.setter
    def flow_metering(self, value: Optional["SwitchFlowMetering"]) -> None:
        """
        Set flowMetering with validation.
        
        Args:
            value: The flowMetering to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flowMetering = None
            return

        if not isinstance(value, SwitchFlowMetering):
            raise TypeError(
                f"flowMetering must be SwitchFlowMetering or None, got {type(value).__name__}"
            )
        self._flowMetering = value
        # Defines the maximum SDU size (size of an Ethernet is acceptable to be
        # processed by the.
        self._maxSduSize: Optional["PositiveInteger"] = None

    @property
    def max_sdu_size(self) -> Optional["PositiveInteger"]:
        """Get maxSduSize (Pythonic accessor)."""
        return self._maxSduSize

    @max_sdu_size.setter
    def max_sdu_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSduSize with validation.
        
        Args:
            value: The maxSduSize to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSduSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxSduSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxSduSize = value
        # Reference to a Stream Gate Entry.
        self._streamGate: Optional["SwitchStreamGateEntry"] = None

    @property
    def stream_gate(self) -> Optional["SwitchStreamGateEntry"]:
        """Get streamGate (Pythonic accessor)."""
        return self._streamGate

    @stream_gate.setter
    def stream_gate(self, value: Optional["SwitchStreamGateEntry"]) -> None:
        """
        Set streamGate with validation.
        
        Args:
            value: The streamGate to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamGate = None
            return

        if not isinstance(value, SwitchStreamGateEntry):
            raise TypeError(
                f"streamGate must be SwitchStreamGateEntry or None, got {type(value).__name__}"
            )
        self._streamGate = value
        # Defines whether this Stream Filter Entry includes the for
                # SwitchStreamIdentification.
        # atp.
        # Status=candidate.
        self._stream: Optional["Boolean"] = None

    @property
    def stream(self) -> Optional["Boolean"]:
        """Get stream (Pythonic accessor)."""
        return self._stream

    @stream.setter
    def stream(self, value: Optional["Boolean"]) -> None:
        """
        Set stream with validation.
        
        Args:
            value: The stream to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stream = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"stream must be Boolean or None, got {type(value).__name__}"
            )
        self._stream = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAsynchronous(self) -> "CouplingPort":
        """
        AUTOSAR-compliant getter for asynchronous.
        
        Returns:
            The asynchronous value
        
        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def setAsynchronous(self, value: "CouplingPort") -> "SwitchStreamFilterEntry":
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

    def getFilterPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for filterPriority.
        
        Returns:
            The filterPriority value
        
        Note:
            Delegates to filter_priority property (CODING_RULE_V2_00017)
        """
        return self.filter_priority  # Delegates to property

    def setFilterPriority(self, value: "PositiveInteger") -> "SwitchStreamFilterEntry":
        """
        AUTOSAR-compliant setter for filterPriority with method chaining.
        
        Args:
            value: The filterPriority to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to filter_priority property setter (gets validation automatically)
        """
        self.filter_priority = value  # Delegates to property setter
        return self

    def getFlowMetering(self) -> "SwitchFlowMetering":
        """
        AUTOSAR-compliant getter for flowMetering.
        
        Returns:
            The flowMetering value
        
        Note:
            Delegates to flow_metering property (CODING_RULE_V2_00017)
        """
        return self.flow_metering  # Delegates to property

    def setFlowMetering(self, value: "SwitchFlowMetering") -> "SwitchStreamFilterEntry":
        """
        AUTOSAR-compliant setter for flowMetering with method chaining.
        
        Args:
            value: The flowMetering to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to flow_metering property setter (gets validation automatically)
        """
        self.flow_metering = value  # Delegates to property setter
        return self

    def getMaxSduSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSduSize.
        
        Returns:
            The maxSduSize value
        
        Note:
            Delegates to max_sdu_size property (CODING_RULE_V2_00017)
        """
        return self.max_sdu_size  # Delegates to property

    def setMaxSduSize(self, value: "PositiveInteger") -> "SwitchStreamFilterEntry":
        """
        AUTOSAR-compliant setter for maxSduSize with method chaining.
        
        Args:
            value: The maxSduSize to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_sdu_size property setter (gets validation automatically)
        """
        self.max_sdu_size = value  # Delegates to property setter
        return self

    def getStreamGate(self) -> "SwitchStreamGateEntry":
        """
        AUTOSAR-compliant getter for streamGate.
        
        Returns:
            The streamGate value
        
        Note:
            Delegates to stream_gate property (CODING_RULE_V2_00017)
        """
        return self.stream_gate  # Delegates to property

    def setStreamGate(self, value: "SwitchStreamGateEntry") -> "SwitchStreamFilterEntry":
        """
        AUTOSAR-compliant setter for streamGate with method chaining.
        
        Args:
            value: The streamGate to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to stream_gate property setter (gets validation automatically)
        """
        self.stream_gate = value  # Delegates to property setter
        return self

    def getStream(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for stream.
        
        Returns:
            The stream value
        
        Note:
            Delegates to stream property (CODING_RULE_V2_00017)
        """
        return self.stream  # Delegates to property

    def setStream(self, value: "Boolean") -> "SwitchStreamFilterEntry":
        """
        AUTOSAR-compliant setter for stream with method chaining.
        
        Args:
            value: The stream to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to stream property setter (gets validation automatically)
        """
        self.stream = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_asynchronous(self, value: Optional["CouplingPort"]) -> "SwitchStreamFilterEntry":
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

    def with_filter_priority(self, value: Optional["PositiveInteger"]) -> "SwitchStreamFilterEntry":
        """
        Set filterPriority and return self for chaining.
        
        Args:
            value: The filterPriority to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_filter_priority("value")
        """
        self.filter_priority = value  # Use property setter (gets validation)
        return self

    def with_flow_metering(self, value: Optional["SwitchFlowMetering"]) -> "SwitchStreamFilterEntry":
        """
        Set flowMetering and return self for chaining.
        
        Args:
            value: The flowMetering to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_flow_metering("value")
        """
        self.flow_metering = value  # Use property setter (gets validation)
        return self

    def with_max_sdu_size(self, value: Optional["PositiveInteger"]) -> "SwitchStreamFilterEntry":
        """
        Set maxSduSize and return self for chaining.
        
        Args:
            value: The maxSduSize to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_sdu_size("value")
        """
        self.max_sdu_size = value  # Use property setter (gets validation)
        return self

    def with_stream_gate(self, value: Optional["SwitchStreamGateEntry"]) -> "SwitchStreamFilterEntry":
        """
        Set streamGate and return self for chaining.
        
        Args:
            value: The streamGate to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_stream_gate("value")
        """
        self.stream_gate = value  # Use property setter (gets validation)
        return self

    def with_stream(self, value: Optional["Boolean"]) -> "SwitchStreamFilterEntry":
        """
        Set stream and return self for chaining.
        
        Args:
            value: The stream to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_stream("value")
        """
        self.stream = value  # Use property setter (gets validation)
        return self