"""
AUTOSAR Package - ComputationMethod

Package: M2::MSR::AsamHdo::ComputationMethod
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class CompuMethod(ARElement):
    """
    that this is still independent of the technical implementation in data
    types. It only specifies the formula how the internal value corresponds to
    its physical pendant.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuMethod

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 310, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 308, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 380, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2010, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 436, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 30, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 176, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the computation from internal values to values.
        self._compuInternal: Optional["Compu"] = None

    @property
    def compu_internal(self) -> Optional["Compu"]:
        """Get compuInternal (Pythonic accessor)."""
        return self._compuInternal

    @compu_internal.setter
    def compu_internal(self, value: Optional["Compu"]) -> None:
        """
        Set compuInternal with validation.

        Args:
            value: The compuInternal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuInternal = None
            return

        if not isinstance(value, Compu):
            raise TypeError(
                f"compuInternal must be Compu or None, got {type(value).__name__}"
            )
        self._compuInternal = value
        self._compuPhysTo: Optional["Compu"] = None

    @property
    def compu_phys_to(self) -> Optional["Compu"]:
        """Get compuPhysTo (Pythonic accessor)."""
        return self._compuPhysTo

    @compu_phys_to.setter
    def compu_phys_to(self, value: Optional["Compu"]) -> None:
        """
        Set compuPhysTo with validation.

        Args:
            value: The compuPhysTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuPhysTo = None
            return

        if not isinstance(value, Compu):
            raise TypeError(
                f"compuPhysTo must be Compu or None, got {type(value).__name__}"
            )
        self._compuPhysTo = value
        # measurement and.
        self._displayFormat: Optional["DisplayFormatString"] = None

    @property
    def display_format(self) -> Optional["DisplayFormatString"]:
        """Get displayFormat (Pythonic accessor)."""
        return self._displayFormat

    @display_format.setter
    def display_format(self, value: Optional["DisplayFormatString"]) -> None:
        """
        Set displayFormat with validation.

        Args:
            value: The displayFormat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._displayFormat = None
            return

        if not isinstance(value, DisplayFormatString):
            raise TypeError(
                f"displayFormat must be DisplayFormatString or None, got {type(value).__name__}"
            )
        self._displayFormat = value
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.

        Args:
            value: The unit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuInternal(self) -> "Compu":
        """
        AUTOSAR-compliant getter for compuInternal.

        Returns:
            The compuInternal value

        Note:
            Delegates to compu_internal property (CODING_RULE_V2_00017)
        """
        return self.compu_internal  # Delegates to property

    def setCompuInternal(self, value: "Compu") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for compuInternal with method chaining.

        Args:
            value: The compuInternal to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_internal property setter (gets validation automatically)
        """
        self.compu_internal = value  # Delegates to property setter
        return self

    def getCompuPhysTo(self) -> "Compu":
        """
        AUTOSAR-compliant getter for compuPhysTo.

        Returns:
            The compuPhysTo value

        Note:
            Delegates to compu_phys_to property (CODING_RULE_V2_00017)
        """
        return self.compu_phys_to  # Delegates to property

    def setCompuPhysTo(self, value: "Compu") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for compuPhysTo with method chaining.

        Args:
            value: The compuPhysTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_phys_to property setter (gets validation automatically)
        """
        self.compu_phys_to = value  # Delegates to property setter
        return self

    def getDisplayFormat(self) -> "DisplayFormatString":
        """
        AUTOSAR-compliant getter for displayFormat.

        Returns:
            The displayFormat value

        Note:
            Delegates to display_format property (CODING_RULE_V2_00017)
        """
        return self.display_format  # Delegates to property

    def setDisplayFormat(self, value: "DisplayFormatString") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for displayFormat with method chaining.

        Args:
            value: The displayFormat to set

        Returns:
            self for method chaining

        Note:
            Delegates to display_format property setter (gets validation automatically)
        """
        self.display_format = value  # Delegates to property setter
        return self

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for unit with method chaining.

        Args:
            value: The unit to set

        Returns:
            self for method chaining

        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_internal(self, value: Optional["Compu"]) -> "CompuMethod":
        """
        Set compuInternal and return self for chaining.

        Args:
            value: The compuInternal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_internal("value")
        """
        self.compu_internal = value  # Use property setter (gets validation)
        return self

    def with_compu_phys_to(self, value: Optional["Compu"]) -> "CompuMethod":
        """
        Set compuPhysTo and return self for chaining.

        Args:
            value: The compuPhysTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_phys_to("value")
        """
        self.compu_phys_to = value  # Use property setter (gets validation)
        return self

    def with_display_format(self, value: Optional["DisplayFormatString"]) -> "CompuMethod":
        """
        Set displayFormat and return self for chaining.

        Args:
            value: The displayFormat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_display_format("value")
        """
        self.display_format = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "CompuMethod":
        """
        Set unit and return self for chaining.

        Args:
            value: The unit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self



class CompuGenericMath(ARObject):
    """
    This meta-class represents the ability to specify a generic formula
    expression.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuGenericMath

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 374, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Placeholder to describe an indicator of a language level mathematics e.
        # g.
        # INFORMAL, ASAMHDO.
        # May be particular use-cases.
        self._level: Optional["PrimitiveIdentifier"] = None

    @property
    def level(self) -> Optional["PrimitiveIdentifier"]:
        """Get level (Pythonic accessor)."""
        return self._level

    @level.setter
    def level(self, value: Optional["PrimitiveIdentifier"]) -> None:
        """
        Set level with validation.

        Args:
            value: The level to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._level = None
            return

        if not isinstance(value, PrimitiveIdentifier):
            raise TypeError(
                f"level must be PrimitiveIdentifier or None, got {type(value).__name__}"
            )
        self._level = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLevel(self) -> "PrimitiveIdentifier":
        """
        AUTOSAR-compliant getter for level.

        Returns:
            The level value

        Note:
            Delegates to level property (CODING_RULE_V2_00017)
        """
        return self.level  # Delegates to property

    def setLevel(self, value: "PrimitiveIdentifier") -> "CompuGenericMath":
        """
        AUTOSAR-compliant setter for level with method chaining.

        Args:
            value: The level to set

        Returns:
            self for method chaining

        Note:
            Delegates to level property setter (gets validation automatically)
        """
        self.level = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_level(self, value: Optional["PrimitiveIdentifier"]) -> "CompuGenericMath":
        """
        Set level and return self for chaining.

        Args:
            value: The level to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_level("value")
        """
        self.level = value  # Use property setter (gets validation)
        return self



class Compu(ARObject):
    """
    This meta-class represents the ability to express one particular
    computation.

    Package: M2::MSR::AsamHdo::ComputationMethod::Compu

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 386, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the details of the computation.
        self._compuContent: Optional["CompuContent"] = None

    @property
    def compu_content(self) -> Optional["CompuContent"]:
        """Get compuContent (Pythonic accessor)."""
        return self._compuContent

    @compu_content.setter
    def compu_content(self, value: Optional["CompuContent"]) -> None:
        """
        Set compuContent with validation.

        Args:
            value: The compuContent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuContent = None
            return

        if not isinstance(value, CompuContent):
            raise TypeError(
                f"compuContent must be CompuContent or None, got {type(value).__name__}"
            )
        self._compuContent = value
                # value to be converted lies plausibility limit.
        # Although this is possible for formulae, it is especially valid for variables
                # conversion formulae.
        self._compuDefault: Optional["CompuConst"] = None

    @property
    def compu_default(self) -> Optional["CompuConst"]:
        """Get compuDefault (Pythonic accessor)."""
        return self._compuDefault

    @compu_default.setter
    def compu_default(self, value: Optional["CompuConst"]) -> None:
        """
        Set compuDefault with validation.

        Args:
            value: The compuDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuDefault = None
            return

        if not isinstance(value, CompuConst):
            raise TypeError(
                f"compuDefault must be CompuConst or None, got {type(value).__name__}"
            )
        self._compuDefault = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuContent(self) -> "CompuContent":
        """
        AUTOSAR-compliant getter for compuContent.

        Returns:
            The compuContent value

        Note:
            Delegates to compu_content property (CODING_RULE_V2_00017)
        """
        return self.compu_content  # Delegates to property

    def setCompuContent(self, value: "CompuContent") -> "Compu":
        """
        AUTOSAR-compliant setter for compuContent with method chaining.

        Args:
            value: The compuContent to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_content property setter (gets validation automatically)
        """
        self.compu_content = value  # Delegates to property setter
        return self

    def getCompuDefault(self) -> "CompuConst":
        """
        AUTOSAR-compliant getter for compuDefault.

        Returns:
            The compuDefault value

        Note:
            Delegates to compu_default property (CODING_RULE_V2_00017)
        """
        return self.compu_default  # Delegates to property

    def setCompuDefault(self, value: "CompuConst") -> "Compu":
        """
        AUTOSAR-compliant setter for compuDefault with method chaining.

        Args:
            value: The compuDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_default property setter (gets validation automatically)
        """
        self.compu_default = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_content(self, value: Optional["CompuContent"]) -> "Compu":
        """
        Set compuContent and return self for chaining.

        Args:
            value: The compuContent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_content("value")
        """
        self.compu_content = value  # Use property setter (gets validation)
        return self

    def with_compu_default(self, value: Optional["CompuConst"]) -> "Compu":
        """
        Set compuDefault and return self for chaining.

        Args:
            value: The compuDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_default("value")
        """
        self.compu_default = value  # Use property setter (gets validation)
        return self



class CompuContent(ARObject, ABC):
    """
    This abstract meta-class represents the various definition means of a
    computation method.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuContent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 386, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompuContent:
            raise TypeError("CompuContent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CompuScale(ARObject):
    """
    This meta-class represents the ability to specify one segment of a segmented
    computation method.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuScale

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 387, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2011, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 177, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value of this attribute shall be taken for generating text (specifically
        # the OutVal) within the the enclosing CompuMethod in A2L.
        self._a2lDisplayText: Optional["String"] = None

    @property
    def a2l_display_text(self) -> Optional["String"]:
        """Get a2lDisplayText (Pythonic accessor)."""
        return self._a2lDisplayText

    @a2l_display_text.setter
    def a2l_display_text(self, value: Optional["String"]) -> None:
        """
        Set a2lDisplayText with validation.

        Args:
            value: The a2lDisplayText to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._a2lDisplayText = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"a2lDisplayText must be String or str or None, got {type(value).__name__}"
            )
        self._a2lDisplayText = value
        # This is the inverse value of the constraint.
        # This supports case that the scale is not reversible per se.
        self._compuInverse: Optional["CompuConst"] = None

    @property
    def compu_inverse(self) -> Optional["CompuConst"]:
        """Get compuInverse (Pythonic accessor)."""
        return self._compuInverse

    @compu_inverse.setter
    def compu_inverse(self, value: Optional["CompuConst"]) -> None:
        """
        Set compuInverse with validation.

        Args:
            value: The compuInverse to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuInverse = None
            return

        if not isinstance(value, CompuConst):
            raise TypeError(
                f"compuInverse must be CompuConst or None, got {type(value).__name__}"
            )
        self._compuInverse = value
        self._compuScale: Optional["CompuScaleContents"] = None

    @property
    def compu_scale(self) -> Optional["CompuScaleContents"]:
        """Get compuScale (Pythonic accessor)."""
        return self._compuScale

    @compu_scale.setter
    def compu_scale(self, value: Optional["CompuScaleContents"]) -> None:
        """
        Set compuScale with validation.

        Args:
            value: The compuScale to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuScale = None
            return

        if not isinstance(value, CompuScaleContents):
            raise TypeError(
                f"compuScale must be CompuScaleContents or None, got {type(value).__name__}"
            )
        self._compuScale = value
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
        self._lowerLimit: Optional["Limit"] = None

    @property
    def lower_limit(self) -> Optional["Limit"]:
        """Get lowerLimit (Pythonic accessor)."""
        return self._lowerLimit

    @lower_limit.setter
    def lower_limit(self, value: Optional["Limit"]) -> None:
        """
        Set lowerLimit with validation.

        Args:
            value: The lowerLimit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"lowerLimit must be Limit or None, got {type(value).__name__}"
            )
        self._lowerLimit = value
                # including the bit MASK.
        # is allowed for this type of COMPU-METHOD, overlap.
        # the string reverse to a value, the string has to and the according value for
                # each substring has to up.
        # The sum is finally transmitted.
        # has to be done in order of the.
        self._mask: Optional["PositiveUnlimitedInteger"] = None

    @property
    def mask(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get mask (Pythonic accessor)."""
        return self._mask

    @mask.setter
    def mask(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set mask with validation.

        Args:
            value: The mask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mask = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"mask must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._mask = value
        # be used to derive a identifier.
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
                # CompuScale.
        # The name will be used for the code generation, therefore it needs to be the
                # generation context.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._symbol: Optional["CIdentifier"] = None

    @property
    def symbol(self) -> Optional["CIdentifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["CIdentifier"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"symbol must be CIdentifier or None, got {type(value).__name__}"
            )
        self._symbol = value
        self._upperLimit: Optional["Limit"] = None

    @property
    def upper_limit(self) -> Optional["Limit"]:
        """Get upperLimit (Pythonic accessor)."""
        return self._upperLimit

    @upper_limit.setter
    def upper_limit(self, value: Optional["Limit"]) -> None:
        """
        Set upperLimit with validation.

        Args:
            value: The upperLimit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"upperLimit must be Limit or None, got {type(value).__name__}"
            )
        self._upperLimit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getA2lDisplayText(self) -> "String":
        """
        AUTOSAR-compliant getter for a2lDisplayText.

        Returns:
            The a2lDisplayText value

        Note:
            Delegates to a2l_display_text property (CODING_RULE_V2_00017)
        """
        return self.a2l_display_text  # Delegates to property

    def setA2lDisplayText(self, value: "String") -> "CompuScale":
        """
        AUTOSAR-compliant setter for a2lDisplayText with method chaining.

        Args:
            value: The a2lDisplayText to set

        Returns:
            self for method chaining

        Note:
            Delegates to a2l_display_text property setter (gets validation automatically)
        """
        self.a2l_display_text = value  # Delegates to property setter
        return self

    def getCompuInverse(self) -> "CompuConst":
        """
        AUTOSAR-compliant getter for compuInverse.

        Returns:
            The compuInverse value

        Note:
            Delegates to compu_inverse property (CODING_RULE_V2_00017)
        """
        return self.compu_inverse  # Delegates to property

    def setCompuInverse(self, value: "CompuConst") -> "CompuScale":
        """
        AUTOSAR-compliant setter for compuInverse with method chaining.

        Args:
            value: The compuInverse to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_inverse property setter (gets validation automatically)
        """
        self.compu_inverse = value  # Delegates to property setter
        return self

    def getCompuScale(self) -> "CompuScaleContents":
        """
        AUTOSAR-compliant getter for compuScale.

        Returns:
            The compuScale value

        Note:
            Delegates to compu_scale property (CODING_RULE_V2_00017)
        """
        return self.compu_scale  # Delegates to property

    def setCompuScale(self, value: "CompuScaleContents") -> "CompuScale":
        """
        AUTOSAR-compliant setter for compuScale with method chaining.

        Args:
            value: The compuScale to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_scale property setter (gets validation automatically)
        """
        self.compu_scale = value  # Delegates to property setter
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

    def setDesc(self, value: "MultiLanguageOverview") -> "CompuScale":
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

    def getLowerLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for lowerLimit.

        Returns:
            The lowerLimit value

        Note:
            Delegates to lower_limit property (CODING_RULE_V2_00017)
        """
        return self.lower_limit  # Delegates to property

    def setLowerLimit(self, value: "Limit") -> "CompuScale":
        """
        AUTOSAR-compliant setter for lowerLimit with method chaining.

        Args:
            value: The lowerLimit to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_limit property setter (gets validation automatically)
        """
        self.lower_limit = value  # Delegates to property setter
        return self

    def getMask(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for mask.

        Returns:
            The mask value

        Note:
            Delegates to mask property (CODING_RULE_V2_00017)
        """
        return self.mask  # Delegates to property

    def setMask(self, value: "PositiveUnlimitedInteger") -> "CompuScale":
        """
        AUTOSAR-compliant setter for mask with method chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Note:
            Delegates to mask property setter (gets validation automatically)
        """
        self.mask = value  # Delegates to property setter
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

    def setShortLabel(self, value: "Identifier") -> "CompuScale":
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

    def getSymbol(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "CIdentifier") -> "CompuScale":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    def getUpperLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for upperLimit.

        Returns:
            The upperLimit value

        Note:
            Delegates to upper_limit property (CODING_RULE_V2_00017)
        """
        return self.upper_limit  # Delegates to property

    def setUpperLimit(self, value: "Limit") -> "CompuScale":
        """
        AUTOSAR-compliant setter for upperLimit with method chaining.

        Args:
            value: The upperLimit to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_limit property setter (gets validation automatically)
        """
        self.upper_limit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_a2l_display_text(self, value: Optional["String"]) -> "CompuScale":
        """
        Set a2lDisplayText and return self for chaining.

        Args:
            value: The a2lDisplayText to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_a2l_display_text("value")
        """
        self.a2l_display_text = value  # Use property setter (gets validation)
        return self

    def with_compu_inverse(self, value: Optional["CompuConst"]) -> "CompuScale":
        """
        Set compuInverse and return self for chaining.

        Args:
            value: The compuInverse to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_inverse("value")
        """
        self.compu_inverse = value  # Use property setter (gets validation)
        return self

    def with_compu_scale(self, value: Optional["CompuScaleContents"]) -> "CompuScale":
        """
        Set compuScale and return self for chaining.

        Args:
            value: The compuScale to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_scale("value")
        """
        self.compu_scale = value  # Use property setter (gets validation)
        return self

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "CompuScale":
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

    def with_lower_limit(self, value: Optional["Limit"]) -> "CompuScale":
        """
        Set lowerLimit and return self for chaining.

        Args:
            value: The lowerLimit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_limit("value")
        """
        self.lower_limit = value  # Use property setter (gets validation)
        return self

    def with_mask(self, value: Optional["PositiveUnlimitedInteger"]) -> "CompuScale":
        """
        Set mask and return self for chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mask("value")
        """
        self.mask = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "CompuScale":
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

    def with_symbol(self, value: Optional["CIdentifier"]) -> "CompuScale":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self

    def with_upper_limit(self, value: Optional["Limit"]) -> "CompuScale":
        """
        Set upperLimit and return self for chaining.

        Args:
            value: The upperLimit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_limit("value")
        """
        self.upper_limit = value  # Use property setter (gets validation)
        return self



class CompuScaleContents(ARObject, ABC):
    """
    This abstract meta-class represents the content of one particular scale.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuScaleContents

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 388, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompuScaleContents:
            raise TypeError("CompuScaleContents is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CompuRationalCoeffs(ARObject):
    """
    This meta-class represents the ability to express a rational function by
    specifying the coefficients of nominator and denominator.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuRationalCoeffs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 389, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the numerator of the rational expression.
        # Tags: xml.
        # sequenceOffset=20.
        self._compu: Optional["CompuNominator"] = None

    @property
    def compu(self) -> Optional["CompuNominator"]:
        """Get compu (Pythonic accessor)."""
        return self._compu

    @compu.setter
    def compu(self, value: Optional["CompuNominator"]) -> None:
        """
        Set compu with validation.

        Args:
            value: The compu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compu = None
            return

        if not isinstance(value, CompuNominator):
            raise TypeError(
                f"compu must be CompuNominator or None, got {type(value).__name__}"
            )
        self._compu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompu(self) -> "CompuNominator":
        """
        AUTOSAR-compliant getter for compu.

        Returns:
            The compu value

        Note:
            Delegates to compu property (CODING_RULE_V2_00017)
        """
        return self.compu  # Delegates to property

    def setCompu(self, value: "CompuNominator") -> "CompuRationalCoeffs":
        """
        AUTOSAR-compliant setter for compu with method chaining.

        Args:
            value: The compu to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu property setter (gets validation automatically)
        """
        self.compu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu(self, value: Optional["CompuNominator"]) -> "CompuRationalCoeffs":
        """
        Set compu and return self for chaining.

        Args:
            value: The compu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu("value")
        """
        self.compu = value  # Use property setter (gets validation)
        return self



class CompuConst(ARObject):
    """
    This meta-class represents the fact that the value of a computation method
    scale is constant.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuConst

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the actual content of the constant compu method.
        self._compuConst: Optional["CompuConstContent"] = None

    @property
    def compu_const(self) -> Optional["CompuConstContent"]:
        """Get compuConst (Pythonic accessor)."""
        return self._compuConst

    @compu_const.setter
    def compu_const(self, value: Optional["CompuConstContent"]) -> None:
        """
        Set compuConst with validation.

        Args:
            value: The compuConst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuConst = None
            return

        if not isinstance(value, CompuConstContent):
            raise TypeError(
                f"compuConst must be CompuConstContent or None, got {type(value).__name__}"
            )
        self._compuConst = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuConst(self) -> "CompuConstContent":
        """
        AUTOSAR-compliant getter for compuConst.

        Returns:
            The compuConst value

        Note:
            Delegates to compu_const property (CODING_RULE_V2_00017)
        """
        return self.compu_const  # Delegates to property

    def setCompuConst(self, value: "CompuConstContent") -> "CompuConst":
        """
        AUTOSAR-compliant setter for compuConst with method chaining.

        Args:
            value: The compuConst to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_const property setter (gets validation automatically)
        """
        self.compu_const = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_const(self, value: Optional["CompuConstContent"]) -> "CompuConst":
        """
        Set compuConst and return self for chaining.

        Args:
            value: The compuConst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_const("value")
        """
        self.compu_const = value  # Use property setter (gets validation)
        return self



class CompuConstContent(ARObject, ABC):
    """
    This meta-class represents the fact that the constant value of the
    computation method can be numerical or textual.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuConstContent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompuConstContent:
            raise TypeError("CompuConstContent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CompuNominatorDenominator(ARObject):
    """
    This class represents the ability to express a polynomial either as
    Nominator or as Denominator.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuNominatorDenominator

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 391, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CompuScales(CompuContent):
    """
    This meta-class represents the ability to stepwise express a computation
    method.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuScales

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 388, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents one scale within the compu method.
        # Note it contains a Variationpoint in order to support enumerations.
        # atpVariation.
        self._compuScale: List["CompuScale"] = []

    @property
    def compu_scale(self) -> List["CompuScale"]:
        """Get compuScale (Pythonic accessor)."""
        return self._compuScale

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuScale(self) -> List["CompuScale"]:
        """
        AUTOSAR-compliant getter for compuScale.

        Returns:
            The compuScale value

        Note:
            Delegates to compu_scale property (CODING_RULE_V2_00017)
        """
        return self.compu_scale  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CompuScaleRationalFormula(CompuScaleContents):
    """
    This meta-class represents the fact that the computation in this scale is
    represented as rational term.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuScaleRationalFormula

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the coefficients of the rational formula.
        # xml.
        # sequenceOffset=110.
        self._compuRational: Optional["CompuRationalCoeffs"] = None

    @property
    def compu_rational(self) -> Optional["CompuRationalCoeffs"]:
        """Get compuRational (Pythonic accessor)."""
        return self._compuRational

    @compu_rational.setter
    def compu_rational(self, value: Optional["CompuRationalCoeffs"]) -> None:
        """
        Set compuRational with validation.

        Args:
            value: The compuRational to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuRational = None
            return

        if not isinstance(value, CompuRationalCoeffs):
            raise TypeError(
                f"compuRational must be CompuRationalCoeffs or None, got {type(value).__name__}"
            )
        self._compuRational = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuRational(self) -> "CompuRationalCoeffs":
        """
        AUTOSAR-compliant getter for compuRational.

        Returns:
            The compuRational value

        Note:
            Delegates to compu_rational property (CODING_RULE_V2_00017)
        """
        return self.compu_rational  # Delegates to property

    def setCompuRational(self, value: "CompuRationalCoeffs") -> "CompuScaleRationalFormula":
        """
        AUTOSAR-compliant setter for compuRational with method chaining.

        Args:
            value: The compuRational to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_rational property setter (gets validation automatically)
        """
        self.compu_rational = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_rational(self, value: Optional["CompuRationalCoeffs"]) -> "CompuScaleRationalFormula":
        """
        Set compuRational and return self for chaining.

        Args:
            value: The compuRational to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_rational("value")
        """
        self.compu_rational = value  # Use property setter (gets validation)
        return self



class CompuScaleConstantContents(CompuScaleContents):
    """
    This meta-class represents the fact that a particular scale of the
    computation method is constant.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuScaleConstantContents

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the fact that the scale is a constant.
        # The is mainly a non interpolated scale.
        # It is a the fact that a constant scale can also be rational function of order
                # 0.
        self._compuConst: Optional["CompuConst"] = None

    @property
    def compu_const(self) -> Optional["CompuConst"]:
        """Get compuConst (Pythonic accessor)."""
        return self._compuConst

    @compu_const.setter
    def compu_const(self, value: Optional["CompuConst"]) -> None:
        """
        Set compuConst with validation.

        Args:
            value: The compuConst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuConst = None
            return

        if not isinstance(value, CompuConst):
            raise TypeError(
                f"compuConst must be CompuConst or None, got {type(value).__name__}"
            )
        self._compuConst = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuConst(self) -> "CompuConst":
        """
        AUTOSAR-compliant getter for compuConst.

        Returns:
            The compuConst value

        Note:
            Delegates to compu_const property (CODING_RULE_V2_00017)
        """
        return self.compu_const  # Delegates to property

    def setCompuConst(self, value: "CompuConst") -> "CompuScaleConstantContents":
        """
        AUTOSAR-compliant setter for compuConst with method chaining.

        Args:
            value: The compuConst to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_const property setter (gets validation automatically)
        """
        self.compu_const = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_const(self, value: Optional["CompuConst"]) -> "CompuScaleConstantContents":
        """
        Set compuConst and return self for chaining.

        Args:
            value: The compuConst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_const("value")
        """
        self.compu_const = value  # Use property setter (gets validation)
        return self



class CompuConstTextContent(CompuConstContent):
    """
    This meta-class represents the textual content of a scale.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuConstTextContent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 388, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2010, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a textual constant in the computation.
        self._vt: Optional["VerbatimString"] = None

    @property
    def vt(self) -> Optional["VerbatimString"]:
        """Get vt (Pythonic accessor)."""
        return self._vt

    @vt.setter
    def vt(self, value: Optional["VerbatimString"]) -> None:
        """
        Set vt with validation.

        Args:
            value: The vt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vt = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"vt must be VerbatimString or None, got {type(value).__name__}"
            )
        self._vt = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVt(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for vt.

        Returns:
            The vt value

        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: "VerbatimString") -> "CompuConstTextContent":
        """
        AUTOSAR-compliant setter for vt with method chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Note:
            Delegates to vt property setter (gets validation automatically)
        """
        self.vt = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vt(self, value: Optional["VerbatimString"]) -> "CompuConstTextContent":
        """
        Set vt and return self for chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vt("value")
        """
        self.vt = value  # Use property setter (gets validation)
        return self



class CompuConstNumericContent(CompuConstContent):
    """
    This meta-class represents the fact that the constant value of the
    computation method is a numerical value. It is separated from
    CompuConstFormulaContent to support compatibility with ASAM HDO.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuConstNumericContent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 389, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the numerical value.
        self._v: Optional["Numerical"] = None

    @property
    def v(self) -> Optional["Numerical"]:
        """Get v (Pythonic accessor)."""
        return self._v

    @v.setter
    def v(self, value: Optional["Numerical"]) -> None:
        """
        Set v with validation.

        Args:
            value: The v to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._v = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"v must be Numerical or None, got {type(value).__name__}"
            )
        self._v = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getV(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for v.

        Returns:
            The v value

        Note:
            Delegates to v property (CODING_RULE_V2_00017)
        """
        return self.v  # Delegates to property

    def setV(self, value: "Numerical") -> "CompuConstNumericContent":
        """
        AUTOSAR-compliant setter for v with method chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Note:
            Delegates to v property setter (gets validation automatically)
        """
        self.v = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_v(self, value: Optional["Numerical"]) -> "CompuConstNumericContent":
        """
        Set v and return self for chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_v("value")
        """
        self.v = value  # Use property setter (gets validation)
        return self



class CompuConstFormulaContent(CompuConstContent):
    """
    This meta-class represents the fact that the constant value of the
    computation method is represented by a variation point. This difference is
    due to compatibility with ASAM HDO.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuConstFormulaContent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 900, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Value calculated via a system constant.
        # This element is every case where parameters should be numerical values during
                # compile time (not example, the influence of the cylinder number on can be
                # introduced in a repeatable.
        self._vf: "Numerical" = None

    @property
    def vf(self) -> "Numerical":
        """Get vf (Pythonic accessor)."""
        return self._vf

    @vf.setter
    def vf(self, value: "Numerical") -> None:
        """
        Set vf with validation.

        Args:
            value: The vf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Numerical):
            raise TypeError(
                f"vf must be Numerical, got {type(value).__name__}"
            )
        self._vf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVf(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for vf.

        Returns:
            The vf value

        Note:
            Delegates to vf property (CODING_RULE_V2_00017)
        """
        return self.vf  # Delegates to property

    def setVf(self, value: "Numerical") -> "CompuConstFormulaContent":
        """
        AUTOSAR-compliant setter for vf with method chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Note:
            Delegates to vf property setter (gets validation automatically)
        """
        self.vf = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vf(self, value: "Numerical") -> "CompuConstFormulaContent":
        """
        Set vf and return self for chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vf("value")
        """
        self.vf = value  # Use property setter (gets validation)
        return self
