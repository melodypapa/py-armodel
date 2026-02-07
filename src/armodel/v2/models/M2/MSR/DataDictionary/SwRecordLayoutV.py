from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


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

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
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

        if not isinstance(value, NameToken):
            raise TypeError(
                f"swRecord must be NameToken or None, got {type(value).__name__}"
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
