from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class Xref(ARObject):
    """
    This represents a cross-reference within documentation.

    Package: M2::MSR::Documentation::TextModel::InlineTextElements

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 320, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This allows to specify a replacement text which shall be if showContent is
        # selected.
        self._label1: Optional["SingleLanguageLong"] = None

    @property
    def label1(self) -> Optional["SingleLanguageLong"]:
        """Get label1 (Pythonic accessor)."""
        return self._label1

    @label1.setter
    def label1(self, value: Optional["SingleLanguageLong"]) -> None:
        """
        Set label1 with validation.

        Args:
            value: The label1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._label1 = None
            return

        if not isinstance(value, SingleLanguageLong):
            raise TypeError(
                f"label1 must be SingleLanguageLong or None, got {type(value).__name__}"
            )
        self._label1 = value
        # This establishes the reference in Autosar style.
        self._referrable: RefType = None

    @property
    def referrable(self) -> RefType:
        """Get referrable (Pythonic accessor)."""
        return self._referrable

    @referrable.setter
    def referrable(self, value: RefType) -> None:
        """
        Set referrable with validation.

        Args:
            value: The referrable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referrable = None
            return

        self._referrable = value
        # The default is "NO-SLOPPY".
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._resolutionPolicy: Optional["ResolutionPolicyEnum"] = None

    @property
    def resolution_policy(self) -> Optional["ResolutionPolicyEnum"]:
        """Get resolutionPolicy (Pythonic accessor)."""
        return self._resolutionPolicy

    @resolution_policy.setter
    def resolution_policy(self, value: Optional["ResolutionPolicyEnum"]) -> None:
        """
        Set resolutionPolicy with validation.

        Args:
            value: The resolutionPolicy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resolutionPolicy = None
            return

        if not isinstance(value, ResolutionPolicyEnum):
            raise TypeError(
                f"resolutionPolicy must be ResolutionPolicyEnum or None, got {type(value).__name__}"
            )
        self._resolutionPolicy = value
        # "NO-SHOW-CONTENT".
        self._showContent: Optional["ShowContentEnum"] = None

    @property
    def show_content(self) -> Optional["ShowContentEnum"]:
        """Get showContent (Pythonic accessor)."""
        return self._showContent

    @show_content.setter
    def show_content(self, value: Optional["ShowContentEnum"]) -> None:
        """
        Set showContent with validation.

        Args:
            value: The showContent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._showContent = None
            return

        if not isinstance(value, ShowContentEnum):
            raise TypeError(
                f"showContent must be ShowContentEnum or None, got {type(value).__name__}"
            )
        self._showContent = value
        # Default is "SHOW-TYPE".
        self._showResource: Optional["ShowResourceType"] = None

    @property
    def show_resource(self) -> Optional["ShowResourceType"]:
        """Get showResource (Pythonic accessor)."""
        return self._showResource

    @show_resource.setter
    def show_resource(self, value: Optional["ShowResourceType"]) -> None:
        """
        Set showResource with validation.

        Args:
            value: The showResource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._showResource = None
            return

        if not isinstance(value, ShowResourceType):
            raise TypeError(
                f"showResource must be ShowResourceType or None, got {type(value).__name__}"
            )
        self._showResource = value
        # Note that this is compatibility reasons only.
        self._showSee: Optional["ShowSeeEnum"] = None

    @property
    def show_see(self) -> Optional["ShowSeeEnum"]:
        """Get showSee (Pythonic accessor)."""
        return self._showSee

    @show_see.setter
    def show_see(self, value: Optional["ShowSeeEnum"]) -> None:
        """
        Set showSee with validation.

        Args:
            value: The showSee to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._showSee = None
            return

        if not isinstance(value, ShowSeeEnum):
            raise TypeError(
                f"showSee must be ShowSeeEnum or None, got {type(value).__name__}"
            )
        self._showSee = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLabel1(self) -> "SingleLanguageLong":
        """
        AUTOSAR-compliant getter for label1.

        Returns:
            The label1 value

        Note:
            Delegates to label1 property (CODING_RULE_V2_00017)
        """
        return self.label1  # Delegates to property

    def setLabel1(self, value: "SingleLanguageLong") -> "Xref":
        """
        AUTOSAR-compliant setter for label1 with method chaining.

        Args:
            value: The label1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to label1 property setter (gets validation automatically)
        """
        self.label1 = value  # Delegates to property setter
        return self

    def getReferrable(self) -> RefType:
        """
        AUTOSAR-compliant getter for referrable.

        Returns:
            The referrable value

        Note:
            Delegates to referrable property (CODING_RULE_V2_00017)
        """
        return self.referrable  # Delegates to property

    def setReferrable(self, value: RefType) -> "Xref":
        """
        AUTOSAR-compliant setter for referrable with method chaining.

        Args:
            value: The referrable to set

        Returns:
            self for method chaining

        Note:
            Delegates to referrable property setter (gets validation automatically)
        """
        self.referrable = value  # Delegates to property setter
        return self

    def getResolutionPolicy(self) -> "ResolutionPolicyEnum":
        """
        AUTOSAR-compliant getter for resolutionPolicy.

        Returns:
            The resolutionPolicy value

        Note:
            Delegates to resolution_policy property (CODING_RULE_V2_00017)
        """
        return self.resolution_policy  # Delegates to property

    def setResolutionPolicy(self, value: "ResolutionPolicyEnum") -> "Xref":
        """
        AUTOSAR-compliant setter for resolutionPolicy with method chaining.

        Args:
            value: The resolutionPolicy to set

        Returns:
            self for method chaining

        Note:
            Delegates to resolution_policy property setter (gets validation automatically)
        """
        self.resolution_policy = value  # Delegates to property setter
        return self

    def getShowContent(self) -> "ShowContentEnum":
        """
        AUTOSAR-compliant getter for showContent.

        Returns:
            The showContent value

        Note:
            Delegates to show_content property (CODING_RULE_V2_00017)
        """
        return self.show_content  # Delegates to property

    def setShowContent(self, value: "ShowContentEnum") -> "Xref":
        """
        AUTOSAR-compliant setter for showContent with method chaining.

        Args:
            value: The showContent to set

        Returns:
            self for method chaining

        Note:
            Delegates to show_content property setter (gets validation automatically)
        """
        self.show_content = value  # Delegates to property setter
        return self

    def getShowResource(self) -> "ShowResourceType":
        """
        AUTOSAR-compliant getter for showResource.

        Returns:
            The showResource value

        Note:
            Delegates to show_resource property (CODING_RULE_V2_00017)
        """
        return self.show_resource  # Delegates to property

    def setShowResource(self, value: "ShowResourceType") -> "Xref":
        """
        AUTOSAR-compliant setter for showResource with method chaining.

        Args:
            value: The showResource to set

        Returns:
            self for method chaining

        Note:
            Delegates to show_resource property setter (gets validation automatically)
        """
        self.show_resource = value  # Delegates to property setter
        return self

    def getShowSee(self) -> "ShowSeeEnum":
        """
        AUTOSAR-compliant getter for showSee.

        Returns:
            The showSee value

        Note:
            Delegates to show_see property (CODING_RULE_V2_00017)
        """
        return self.show_see  # Delegates to property

    def setShowSee(self, value: "ShowSeeEnum") -> "Xref":
        """
        AUTOSAR-compliant setter for showSee with method chaining.

        Args:
            value: The showSee to set

        Returns:
            self for method chaining

        Note:
            Delegates to show_see property setter (gets validation automatically)
        """
        self.show_see = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_label1(self, value: Optional["SingleLanguageLong"]) -> "Xref":
        """
        Set label1 and return self for chaining.

        Args:
            value: The label1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_label1("value")
        """
        self.label1 = value  # Use property setter (gets validation)
        return self

    def with_referrable(self, value: Optional[RefType]) -> "Xref":
        """
        Set referrable and return self for chaining.

        Args:
            value: The referrable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_referrable("value")
        """
        self.referrable = value  # Use property setter (gets validation)
        return self

    def with_resolution_policy(self, value: Optional["ResolutionPolicyEnum"]) -> "Xref":
        """
        Set resolutionPolicy and return self for chaining.

        Args:
            value: The resolutionPolicy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resolution_policy("value")
        """
        self.resolution_policy = value  # Use property setter (gets validation)
        return self

    def with_show_content(self, value: Optional["ShowContentEnum"]) -> "Xref":
        """
        Set showContent and return self for chaining.

        Args:
            value: The showContent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_show_content("value")
        """
        self.show_content = value  # Use property setter (gets validation)
        return self

    def with_show_resource(self, value: Optional["ShowResourceType"]) -> "Xref":
        """
        Set showResource and return self for chaining.

        Args:
            value: The showResource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_show_resource("value")
        """
        self.show_resource = value  # Use property setter (gets validation)
        return self

    def with_show_see(self, value: Optional["ShowSeeEnum"]) -> "Xref":
        """
        Set showSee and return self for chaining.

        Args:
            value: The showSee to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_show_see("value")
        """
        self.show_see = value  # Use property setter (gets validation)
        return self
