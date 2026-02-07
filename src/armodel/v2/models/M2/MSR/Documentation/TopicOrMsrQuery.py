from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TopicOrMsrQuery(ARObject):
    """
    This class provides the alternative of a Topic with an MsrQuery which
    delivers a topic.
    
    Package: M2::MSR::Documentation::Chapters::TopicOrMsrQuery
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 342, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents automatically contributed topics provided an msrquery.
        self._msrQuery: "MsrQueryTopic1" = None

    @property
    def msr_query(self) -> "MsrQueryTopic1":
        """Get msrQuery (Pythonic accessor)."""
        return self._msrQuery

    @msr_query.setter
    def msr_query(self, value: "MsrQueryTopic1") -> None:
        """
        Set msrQuery with validation.
        
        Args:
            value: The msrQuery to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryTopic1):
            raise TypeError(
                f"msrQuery must be MsrQueryTopic1, got {type(value).__name__}"
            )
        self._msrQuery = value
        # This is used to create particular topics within a chapter.
        # A similar to a subchapter, but cannot be nested and appear in the table of
                # contents of the document.
        # atpVariation.
        self._topic1: "Topic1" = None

    @property
    def topic1(self) -> "Topic1":
        """Get topic1 (Pythonic accessor)."""
        return self._topic1

    @topic1.setter
    def topic1(self, value: "Topic1") -> None:
        """
        Set topic1 with validation.
        
        Args:
            value: The topic1 to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Topic1):
            raise TypeError(
                f"topic1 must be Topic1, got {type(value).__name__}"
            )
        self._topic1 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMsrQuery(self) -> "MsrQueryTopic1":
        """
        AUTOSAR-compliant getter for msrQuery.
        
        Returns:
            The msrQuery value
        
        Note:
            Delegates to msr_query property (CODING_RULE_V2_00017)
        """
        return self.msr_query  # Delegates to property

    def setMsrQuery(self, value: "MsrQueryTopic1") -> "TopicOrMsrQuery":
        """
        AUTOSAR-compliant setter for msrQuery with method chaining.
        
        Args:
            value: The msrQuery to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to msr_query property setter (gets validation automatically)
        """
        self.msr_query = value  # Delegates to property setter
        return self

    def getTopic1(self) -> "Topic1":
        """
        AUTOSAR-compliant getter for topic1.
        
        Returns:
            The topic1 value
        
        Note:
            Delegates to topic1 property (CODING_RULE_V2_00017)
        """
        return self.topic1  # Delegates to property

    def setTopic1(self, value: "Topic1") -> "TopicOrMsrQuery":
        """
        AUTOSAR-compliant setter for topic1 with method chaining.
        
        Args:
            value: The topic1 to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to topic1 property setter (gets validation automatically)
        """
        self.topic1 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_msr_query(self, value: "MsrQueryTopic1") -> "TopicOrMsrQuery":
        """
        Set msrQuery and return self for chaining.
        
        Args:
            value: The msrQuery to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_msr_query("value")
        """
        self.msr_query = value  # Use property setter (gets validation)
        return self

    def with_topic1(self, value: "Topic1") -> "TopicOrMsrQuery":
        """
        Set topic1 and return self for chaining.
        
        Args:
            value: The topic1 to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_topic1("value")
        """
        self.topic1 = value  # Use property setter (gets validation)
        return self