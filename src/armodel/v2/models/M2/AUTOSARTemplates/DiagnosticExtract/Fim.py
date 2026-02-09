"""
AUTOSAR Package - Fim

Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim
"""

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import (
    DiagnosticAbstractAliasEvent,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticFimAliasEvent(DiagnosticAbstractAliasEvent):
    """
    This meta-class is used to represent a given event semantics. However, the
    name of the actual events used in a specific project is sometimes not
    defined yet, not known or not in the responsibility of the author.
    Therefore, the DiagnosticFimAliasEvent has a reference to the actual
    DiagnosticEvent and by this the final connection is created.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFimAliasEvent
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 214, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_inhibit_source(self, value):
        """
        Set inhibit_source and return self for chaining.

        Args:
            value: The inhibit_source to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inhibit_source("value")
        """
        self.inhibit_source = value  # Use property setter (gets validation)
        return self

    def with_grouped_alias(self, value):
        """
        Set grouped_alias and return self for chaining.

        Args:
            value: The grouped_alias to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_grouped_alias("value")
        """
        self.grouped_alias = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticFunctionIdentifier(DiagnosticCommonElement):
    """
    This meta-class represents a diagnostic function identifier (a.k.a. FID).
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFunctionIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 215, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define the inhibition of a
    specific function identifier within the Fim configuration.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFunctionIdentifierInhibit
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 215, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the corresponding function identifier.
        self._function: Optional["DiagnosticFunction"] = None

    @property
    def function(self) -> Optional["DiagnosticFunction"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set function with validation.
        
        Args:
            value: The function to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"function must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._function = value
        # This represents the value of the inhibition mask behavior.
        self._inhibitionMask: Optional["DiagnosticInhibition"] = None

    @property
    def inhibition_mask(self) -> Optional["DiagnosticInhibition"]:
        """Get inhibitionMask (Pythonic accessor)."""
        return self._inhibitionMask

    @inhibition_mask.setter
    def inhibition_mask(self, value: Optional["DiagnosticInhibition"]) -> None:
        """
        Set inhibitionMask with validation.
        
        Args:
            value: The inhibitionMask to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inhibitionMask = None
            return

        if not isinstance(value, DiagnosticInhibition):
            raise TypeError(
                f"inhibitionMask must be DiagnosticInhibition or None, got {type(value).__name__}"
            )
        self._inhibitionMask = value
        # This represents a collection of DiagnosticFunctionInhibit that contribute to
        # the configuration of the.
        self._inhibitSource: List["DiagnosticFunction"] = []

    @property
    def inhibit_source(self) -> List["DiagnosticFunction"]:
        """Get inhibitSource (Pythonic accessor)."""
        return self._inhibitSource

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunction(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for function.
        
        Returns:
            The function value
        
        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: "DiagnosticFunction") -> "DiagnosticFunctionIdentifierInhibit":
        """
        AUTOSAR-compliant setter for function with method chaining.
        
        Args:
            value: The function to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    def getInhibitionMask(self) -> "DiagnosticInhibition":
        """
        AUTOSAR-compliant getter for inhibitionMask.
        
        Returns:
            The inhibitionMask value
        
        Note:
            Delegates to inhibition_mask property (CODING_RULE_V2_00017)
        """
        return self.inhibition_mask  # Delegates to property

    def setInhibitionMask(self, value: "DiagnosticInhibition") -> "DiagnosticFunctionIdentifierInhibit":
        """
        AUTOSAR-compliant setter for inhibitionMask with method chaining.
        
        Args:
            value: The inhibitionMask to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to inhibition_mask property setter (gets validation automatically)
        """
        self.inhibition_mask = value  # Delegates to property setter
        return self

    def getInhibitSource(self) -> List["DiagnosticFunction"]:
        """
        AUTOSAR-compliant getter for inhibitSource.
        
        Returns:
            The inhibitSource value
        
        Note:
            Delegates to inhibit_source property (CODING_RULE_V2_00017)
        """
        return self.inhibit_source  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function(self, value: Optional["DiagnosticFunction"]) -> "DiagnosticFunctionIdentifierInhibit":
        """
        Set function and return self for chaining.
        
        Args:
            value: The function to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

    def with_inhibition_mask(self, value: Optional["DiagnosticInhibition"]) -> "DiagnosticFunctionIdentifierInhibit":
        """
        Set inhibitionMask and return self for chaining.
        
        Args:
            value: The inhibitionMask to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_inhibition_mask("value")
        """
        self.inhibition_mask = value  # Use property setter (gets validation)
        return self



class DiagnosticFunctionInhibitSource(Identifiable):
    """
    This meta-class represents the ability to define an inhibition source in the
    context of the Fim configuration.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFunctionInhibitSource
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 216, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the alias event applicable for the inhibition source.
        self._event: Optional["DiagnosticFimAlias"] = None

    @property
    def event(self) -> Optional["DiagnosticFimAlias"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["DiagnosticFimAlias"]) -> None:
        """
        Set event with validation.
        
        Args:
            value: The event to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, DiagnosticFimAlias):
            raise TypeError(
                f"event must be DiagnosticFimAlias or None, got {type(value).__name__}"
            )
        self._event = value
        # This represents the event group applicable for the inhibition source.
        self._eventGroup: Optional["DiagnosticFimAlias"] = None

    @property
    def event_group(self) -> Optional["DiagnosticFimAlias"]:
        """Get eventGroup (Pythonic accessor)."""
        return self._eventGroup

    @event_group.setter
    def event_group(self, value: Optional["DiagnosticFimAlias"]) -> None:
        """
        Set eventGroup with validation.
        
        Args:
            value: The eventGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventGroup = None
            return

        if not isinstance(value, DiagnosticFimAlias):
            raise TypeError(
                f"eventGroup must be DiagnosticFimAlias or None, got {type(value).__name__}"
            )
        self._eventGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> "DiagnosticFimAlias":
        """
        AUTOSAR-compliant getter for event.
        
        Returns:
            The event value
        
        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "DiagnosticFimAlias") -> "DiagnosticFunctionInhibitSource":
        """
        AUTOSAR-compliant setter for event with method chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getEventGroup(self) -> "DiagnosticFimAlias":
        """
        AUTOSAR-compliant getter for eventGroup.
        
        Returns:
            The eventGroup value
        
        Note:
            Delegates to event_group property (CODING_RULE_V2_00017)
        """
        return self.event_group  # Delegates to property

    def setEventGroup(self, value: "DiagnosticFimAlias") -> "DiagnosticFunctionInhibitSource":
        """
        AUTOSAR-compliant setter for eventGroup with method chaining.
        
        Args:
            value: The eventGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_group property setter (gets validation automatically)
        """
        self.event_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event(self, value: Optional["DiagnosticFimAlias"]) -> "DiagnosticFunctionInhibitSource":
        """
        Set event and return self for chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_event_group(self, value: Optional["DiagnosticFimAlias"]) -> "DiagnosticFunctionInhibitSource":
        """
        Set eventGroup and return self for chaining.
        
        Args:
            value: The eventGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_group("value")
        """
        self.event_group = value  # Use property setter (gets validation)
        return self



class DiagnosticFimEventGroup(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a Fim event group, also
    known as a summary event in Fim terminology. This represents a group of
    single diagnostic events.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFimEventGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 217, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the way of grouping diagnostic a summary event in
        # the context of the Fim.
        self._event: List["DiagnosticEvent"] = []

    @property
    def event(self) -> List["DiagnosticEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> List["DiagnosticEvent"]:
        """
        AUTOSAR-compliant getter for event.
        
        Returns:
            The event value
        
        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """
    This meta-class represents the ability to define an alias for a Fim
    summarized event. This alias can be used in early phases of the
    configuration process until a further refinement is possible.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFimAliasEventGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 263, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # By means of this reference the grouping of Diagnostic AliasEvents within the
        # DiagnosticFimSummaryEvent can.
        self._groupedAlias: List["DiagnosticFimAlias"] = []

    @property
    def grouped_alias(self) -> List["DiagnosticFimAlias"]:
        """Get groupedAlias (Pythonic accessor)."""
        return self._groupedAlias

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGroupedAlias(self) -> List["DiagnosticFimAlias"]:
        """
        AUTOSAR-compliant getter for groupedAlias.
        
        Returns:
            The groupedAlias value
        
        Note:
            Delegates to grouped_alias property (CODING_RULE_V2_00017)
        """
        return self.grouped_alias  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class DiagnosticInhibitionMaskEnum(AREnum):
    """
    DiagnosticInhibitionMaskEnum enumeration

This meta-class represents the ability to define different kinds of inhibition mask behavior. Aggregated by DiagnosticFunctionIdentifierInhibit.inhibitionMask

Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim
    """
    # This represents the inhibition mask behavior "last failed".
    lastFailed = "0"

    # This represents the inhibition mask behavior "not tested".
    notTested = "1"

    # This represents the inhibition mask behavior "tested".
    tested = "3"

    # This represents the inhibition mask behavior "tested and failed".
    testedAndFailed = "2"
