"""
AUTOSAR Package - RecordLayout

Package: M2::MSR::DataDictionary::RecordLayout
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class SwRecordLayout(ARElement):
    """
    Defines how the data objects (variables, calibration parameters etc.) are to
    be stored in the ECU memory. As an example, this definition specifies the
    sequence of axis points in the ECU memory. Iterations through axis values
    are stored within the sub-elements swRecordLayoutGroup.
    
    Package: M2::MSR::DataDictionary::RecordLayout::SwRecordLayout
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 421, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2066, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the top level record layout group.
        self._swRecord: Optional["RefType"] = None

    @property
    def sw_record(self) -> Optional["RefType"]:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: Optional["RefType"]) -> None:
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

        self._swRecord = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwRecord(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swRecord.
        
        Returns:
            The swRecord value
        
        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: "RefType") -> "SwRecordLayout":
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

    def with_sw_record(self, value: Optional[RefType]) -> "SwRecordLayout":
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



class SwRecordLayoutV(ARObject):
    """
    This element specifies which values are stored for the current
    SwRecordLayoutGroup. If no baseType is present, the SwBaseType referenced
    initially in the parent SwRecordLayoutGroup is valid. The specification of
    swRecordLayoutVAxis gives the axis of the values which shall be stored in
    accordance with the current record layout SwRecordLayoutGroup. In
    swRecordLayoutVProp one can specify the information which shall be stored.
    
    Package: M2::MSR::DataDictionary::RecordLayout::SwRecordLayoutV
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 421, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association allows to refer to a base type in case a is intended.
        # If no base type is referred, type referenced initially in the corresponding
                # to be used.
        self._baseType: Optional["SwBaseType"] = None

    @property
    def base_type(self) -> Optional["SwBaseType"]:
        """Get baseType (Pythonic accessor)."""
        return self._baseType

    @base_type.setter
    def base_type(self, value: Optional["SwBaseType"]) -> None:
        """
        Set baseType with validation.
        
        Args:
            value: The baseType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseType = None
            return

        if not isinstance(value, SwBaseType):
            raise TypeError(
                f"baseType must be SwBaseType or None, got {type(value).__name__}"
            )
        self._baseType = value
        # This aggregation allows for a brief description about the record layout value
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value
        # This association supports the case that a value from a generic axis
                # definition shall be stored.
        # This value is a particular generic axis parameter type.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
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
        # This attribute describes the kind of values to be stored.
        # details see below.
        # The standardized values this attribute are defined in.
        self._swRecord: Optional["NameToken"] = None

    @property
    def sw_record(self) -> Optional["NameToken"]:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: Optional["NameToken"]) -> None:
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

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"swRecord must be NameToken or str or None, got {type(value).__name__}"
            )
        self._swRecord = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseType(self) -> "SwBaseType":
        """
        AUTOSAR-compliant getter for baseType.
        
        Returns:
            The baseType value
        
        Note:
            Delegates to base_type property (CODING_RULE_V2_00017)
        """
        return self.base_type  # Delegates to property

    def setBaseType(self, value: "SwBaseType") -> "SwRecordLayoutV":
        """
        AUTOSAR-compliant setter for baseType with method chaining.
        
        Args:
            value: The baseType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base_type property setter (gets validation automatically)
        """
        self.base_type = value  # Delegates to property setter
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

    def setDesc(self, value: "MultiLanguageOverview") -> "SwRecordLayoutV":
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

    def setShortLabel(self, value: "Identifier") -> "SwRecordLayoutV":
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

    def setSwGenericAxis(self, value: "SwGenericAxisParam") -> "SwRecordLayoutV":
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

    def getSwRecord(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for swRecord.
        
        Returns:
            The swRecord value
        
        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: "NameToken") -> "SwRecordLayoutV":
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

    def with_base_type(self, value: Optional["SwBaseType"]) -> "SwRecordLayoutV":
        """
        Set baseType and return self for chaining.
        
        Args:
            value: The baseType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base_type("value")
        """
        self.base_type = value  # Use property setter (gets validation)
        return self

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "SwRecordLayoutV":
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

    def with_short_label(self, value: Optional["Identifier"]) -> "SwRecordLayoutV":
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

    def with_sw_generic_axis(self, value: Optional["SwGenericAxisParam"]) -> "SwRecordLayoutV":
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

    def with_sw_record(self, value: Optional["NameToken"]) -> "SwRecordLayoutV":
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
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



class SwRecordLayoutGroupContent(ARObject):
    """
    This is the contents of a RecordLayout which is inserted for every
    iteration. Note that since this is atp Mixed, multiple properties can be
    inserted for each iteration.
    
    Package: M2::MSR::DataDictionary::RecordLayout::SwRecordLayoutGroupContent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 424, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Particular Value specification for this record layout group.
        # xml.
        # sequenceOffset=120.
        self._swRecord: Optional["SwRecordLayoutV"] = None

    @property
    def sw_record(self) -> Optional["SwRecordLayoutV"]:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: Optional["SwRecordLayoutV"]) -> None:
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

        if not isinstance(value, SwRecordLayoutV):
            raise TypeError(
                f"swRecord must be SwRecordLayoutV or None, got {type(value).__name__}"
            )
        self._swRecord = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwRecord(self) -> "SwRecordLayoutV":
        """
        AUTOSAR-compliant getter for swRecord.
        
        Returns:
            The swRecord value
        
        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: "SwRecordLayoutV") -> "SwRecordLayoutGroupContent":
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

    def with_sw_record(self, value: Optional["SwRecordLayoutV"]) -> "SwRecordLayoutGroupContent":
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


class AxisIndexType(ARLiteral):
    """
    AxisIndexType primitive type

This meta-class specifies an axis in a curve/map data object. The index satisfies the following convention: • 0 output "axis" • 1 input axis 1 (X input axis e.g. of a CURVE) • 2 input axis 2 (Y input axis e.g. of a MAP) • 3 input axis 3 (Z input axis e.g. of a CUBOID) • 4 input axis 3 (Z4 input axis e.g. of a CUBE_4) • 5 input axis 3 (Z5 input axis e.g. of a CUBE_5) • 6..9 etc. The output "axis" provides access to the output value of the parameter. Note that this access is usually performed via an index according to the input axis. In addition to this, the Values STRING and ARRAY support specific iterations. Tags: xml.xsd.customType=AXIS-INDEX-TYPE xml.xsd.pattern=[0-9]+|STRING|ARRAY xml.xsd.type=string Table 5.101: AxisIndexType

Package: M2::MSR::DataDictionary::RecordLayout
    """
    pass





class RecordLayoutIteratorPoint(ARLiteral):
    """
    RecordLayoutIteratorPoint primitive type

This meta-class denotes a start / endpoint for the iteration of a SwRecordLayoutGroup. It can be an integer or one of the keywords MAX-TEXT-SIZE|ARRAY-SIZE. Note that negative numbers are counted backwards. Therefore e.g. -1 refers to the last value. Tags: xml.xsd.customType=RECORD-LAYOUT-ITERATOR-POINT xml.xsd.pattern=-?([0-9]+|MAX-TEXT-SIZE|ARRAY-SIZE) xml.xsd.type=string Table 5.102: RecordLayoutIteratorPoint [TPS_SWCT_01489] Description of standardized values of SwRecordLayoutV. swRecordLayoutVProp (cid:100) Property Description The value of the axis for the current iterator point. This is e.g. the particular point on an input-axis, but VALUE also the particular character in a string. COUNT The amount of values of the axis. LEFTDIFF The difference to the previous axis point. RIGHTDIFF The difference to the next axis point. DIST The distance value of this axis in case of a fixed axis with distance specification. SHIFT The shift value of this axis in case of a fixed axis with shift/offset. OFFSET The offset value of this axis in case of a fixed axis with shift/offset. FILL Fill with the hex value specified as contents of swRecordLayoutVFixValue. RESERVED Position shall be ignored by MCD tools. IDENTIFIER An “identifier” is deposited at the position. FIXLEFTDIFF Difference between this and a fixed left-hand value specified in swRecordLayoutVFixValue. FIXRIGHTDIFF Difference between this and a fixed right-hand value specified in swRecordLayoutVFixValue. (cid:99)(RS_SWCT_03215) 425 of 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR CP R23-11 Figure 5.54 and Figure 5.55 illustrate most of these properties. Current point 0 VALUE LLEEFFTTDDIIFFFF RRIIGGHHTTDDIIFFFF FFIIXXLLEEFFTTDDIIFFFF FFIIXXRRIIGGHHTTDDIIFFFF 111 222 333 444 CCOOUUNNTT == 44 Figure 5.54: Values for swRecordLayoutVProp for individual axis VVaalluuee == OOFFFFSSEETT ++ nn ** 22^^SSHHIIFFTT 00 VVaalluuee == OOFFFFSSEETT ++ nn ** DDIISSTT OOFFFFSSEETT DDIISSTT DDIISSTT 22^^SSHHIIFFTT Figure 5.55: Values for swRecordLayoutVProp for fixed axis [TPS_SWCT_01296] Different approaches of ASAM MCD-2MC and AUTOSAR with respect to SwRecordLayout (cid:100)ASAM MCD-2D specification (also known as A2L, or ASAP) uses keywords in record layouts where MSR/AUTOSAR uses the more generic approach specified here. It may happen that this generic approach cannot always be safely mapped to the A2L keywords. Therefore, SwRecordLayoutGroup.category can assist the conversion to the current A2L format.(cid:99)(RS_SWCT_03215) 426 of 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR CP R23-11

Package: M2::MSR::DataDictionary::RecordLayout
    """
    pass





class AsamRecordLayoutSemantics(ARLiteral):
    """
    AsamRecordLayoutSemantics primitive type

This meta-class is used to denote the semantics in particular in terms of the corresponding A2L-Keyword. This is to support the mapping of the more general record layouts in AUTOSAR/MSR to the specific A2L keywords. It is possible to express the specific semantics of A2l RecordLayout keywords in SwRecordlayoutGroup but not always vice versa. Therefore the mapping is provided in this optional attribute. It is specified as NMTOKEN to reduce the direct dependency of ASAM an AUTOSAR standards. Tags: xml.xsd.customType=ASAM-RECORD-LAYOUT-SEMANTICS xml.xsd.type=NMTOKEN Table 5.103: AsamRecordLayoutSemantics The values of SwRecordLayoutGroup.category can, for example, be taken from the ASAM MCD 2D specification provided in [15]. Examples are: • INDEX_INCR • INDEX_DECR • COLUMN_DIR • ROW_DIR • ALTERNATE_WITH_X • ALTERNATE_WITH_Y • ALTERNATE_CURVES

Package: M2::MSR::DataDictionary::RecordLayout
    """
    pass


