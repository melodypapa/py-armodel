from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwRecordLayoutGroup(ARObject):
    """
    that depending on the arraySizeSemantics of Sw TextProps the iteration ends
    at the value specified in sw MaxTextSize. Table 5.99: SwRecordLayoutGroup
    
    Package: M2::MSR::DataDictionary::RecordLayout::SwRecordLayoutGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 422, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2066, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute denotes the semantics in particular in terms the corresponding
                # A2L-Keyword.
        # This is to support the the more general record layouts in AUTOSAR/ the
                # specific A2l keywords.
        # possible to express the specific semantics of A2l in swRecordlayoutGroup but
                # not versa.
        # Therefore the mapping is provided in attribute.
        self._category: Optional["AsamRecordLayout"] = None

    @property
    def category(self) -> Optional["AsamRecordLayout"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["AsamRecordLayout"]) -> None:
        """
        Set category with validation.
        
        Args:
            value: The category to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, AsamRecordLayout):
            raise TypeError(
                f"category must be AsamRecordLayout or None, got {type(value).__name__}"
            )
        self._category = value
        # This aggregation allows a brief description about the record layout group
        # which can help to identify In-depth documentation should be added to the the
        # surrounding record layout.
        self._desc: Optional["MultiLanguageOverview"] = None

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.
        
        Args:
            value: The desc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"desc must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._desc = value
        # This attribute specifies a name which can be used e.
        # g.
        # code is generated from the record layout.
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
        # This association allows to specify record layout groups to iterate over
                # generic axis parameters.
        # For example, if the parameter is an array, the record layout iterate over
                # this array.
        # axis referred to by swRecordLayoutGroup be a generic axis in which the
                # referenced Sw aggregated.
        self._swGenericAxis: Optional["SwGenericAxisParam"] = None

    @property
    def sw_generic_axis(self) -> Optional["SwGenericAxisParam"]:
        """Get swGenericAxis (Pythonic accessor)."""
        return self._swGenericAxis

    @sw_generic_axis.setter
    def sw_generic_axis(self, value: Optional["SwGenericAxisParam"]) -> None:
        """
        Set swGenericAxis with validation.
        
        Args:
            value: The swGenericAxis to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swGenericAxis = None
            return

        if not isinstance(value, SwGenericAxisParam):
            raise TypeError(
                f"swGenericAxis must be SwGenericAxisParam or None, got {type(value).__name__}"
            )
        self._swGenericAxis = value
        # This attribute specifies the end point for the iteration.
        # Negative values are also possible, i.
        # e.
        # the value -4 counts the fourth value from the end.
        # If this property is not iteration ends at "-1" which is the last element.
        self._swRecord: Optional["RecordLayoutIterator"] = None

    @property
    def sw_record(self) -> Optional["RecordLayoutIterator"]:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: Optional["RecordLayoutIterator"]) -> None:
        """
        Set swRecord with validation.
        
        Args:
            value: The swRecord to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swRecord = None
            return

        if not isinstance(value, RecordLayoutIterator):
            raise TypeError(
                f"swRecord must be RecordLayoutIterator or None, got {type(value).__name__}"
            )
        self._swRecord = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "AsamRecordLayout":
        """
        AUTOSAR-compliant getter for category.
        
        Returns:
            The category value
        
        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "AsamRecordLayout") -> "SwRecordLayoutGroup":
        """
        AUTOSAR-compliant setter for category with method chaining.
        
        Args:
            value: The category to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.
        
        Returns:
            The desc value
        
        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> "SwRecordLayoutGroup":
        """
        AUTOSAR-compliant setter for desc with method chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
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

    def setShortLabel(self, value: "Identifier") -> "SwRecordLayoutGroup":
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

    def getSwGenericAxis(self) -> "SwGenericAxisParam":
        """
        AUTOSAR-compliant getter for swGenericAxis.
        
        Returns:
            The swGenericAxis value
        
        Note:
            Delegates to sw_generic_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_generic_axis  # Delegates to property

    def setSwGenericAxis(self, value: "SwGenericAxisParam") -> "SwRecordLayoutGroup":
        """
        AUTOSAR-compliant setter for swGenericAxis with method chaining.
        
        Args:
            value: The swGenericAxis to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_generic_axis property setter (gets validation automatically)
        """
        self.sw_generic_axis = value  # Delegates to property setter
        return self

    def getSwRecord(self) -> "RecordLayoutIterator":
        """
        AUTOSAR-compliant getter for swRecord.
        
        Returns:
            The swRecord value
        
        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: "RecordLayoutIterator") -> "SwRecordLayoutGroup":
        """
        AUTOSAR-compliant setter for swRecord with method chaining.
        
        Args:
            value: The swRecord to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_record property setter (gets validation automatically)
        """
        self.sw_record = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional["AsamRecordLayout"]) -> "SwRecordLayoutGroup":
        """
        Set category and return self for chaining.
        
        Args:
            value: The category to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "SwRecordLayoutGroup":
        """
        Set desc and return self for chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "SwRecordLayoutGroup":
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

    def with_sw_generic_axis(self, value: Optional["SwGenericAxisParam"]) -> "SwRecordLayoutGroup":
        """
        Set swGenericAxis and return self for chaining.
        
        Args:
            value: The swGenericAxis to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_generic_axis("value")
        """
        self.sw_generic_axis = value  # Use property setter (gets validation)
        return self

    def with_sw_record(self, value: Optional["RecordLayoutIterator"]) -> "SwRecordLayoutGroup":
        """
        Set swRecord and return self for chaining.
        
        Args:
            value: The swRecord to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_record("value")
        """
        self.sw_record = value  # Use property setter (gets validation)
        return self