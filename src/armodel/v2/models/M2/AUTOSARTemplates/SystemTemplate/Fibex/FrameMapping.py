from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DocumentationBlock
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class FrameMapping(ARObject):
    """
    The entire source frame is mapped as it is onto the target frame (what in
    general is only possible inside of a common platform). In this case source
    and target frame should be the identical object. Each pair consists in a
    SOURCE and a TARGET referencing to a FrameTriggering. The Frame Mapping is
    not supported by the Autosar BSW. The existence is optional and has been
    incorporated into the System Template mainly for compatibility in order to
    allow interchange between FIBEX and AUTOSAR descriptions.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::FrameMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 838, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value
        # Source destination of the referencing mapping.
        self._sourceFrame: RefType = None

    @property
    def source_frame(self) -> RefType:
        """Get sourceFrame (Pythonic accessor)."""
        return self._sourceFrame

    @source_frame.setter
    def source_frame(self, value: RefType) -> None:
        """
        Set sourceFrame with validation.

        Args:
            value: The sourceFrame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceFrame = None
            return

        self._sourceFrame = value
        # Target destination of the referencing mapping.
        self._targetFrame: RefType = None

    @property
    def target_frame(self) -> RefType:
        """Get targetFrame (Pythonic accessor)."""
        return self._targetFrame

    @target_frame.setter
    def target_frame(self, value: RefType) -> None:
        """
        Set targetFrame with validation.

        Args:
            value: The targetFrame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetFrame = None
            return

        self._targetFrame = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "FrameMapping":
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    def getSourceFrame(self) -> RefType:
        """
        AUTOSAR-compliant getter for sourceFrame.

        Returns:
            The sourceFrame value

        Note:
            Delegates to source_frame property (CODING_RULE_V2_00017)
        """
        return self.source_frame  # Delegates to property

    def setSourceFrame(self, value: RefType) -> "FrameMapping":
        """
        AUTOSAR-compliant setter for sourceFrame with method chaining.

        Args:
            value: The sourceFrame to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_frame property setter (gets validation automatically)
        """
        self.source_frame = value  # Delegates to property setter
        return self

    def getTargetFrame(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetFrame.

        Returns:
            The targetFrame value

        Note:
            Delegates to target_frame property (CODING_RULE_V2_00017)
        """
        return self.target_frame  # Delegates to property

    def setTargetFrame(self, value: RefType) -> "FrameMapping":
        """
        AUTOSAR-compliant setter for targetFrame with method chaining.

        Args:
            value: The targetFrame to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_frame property setter (gets validation automatically)
        """
        self.target_frame = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "FrameMapping":
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self

    def with_source_frame(self, value: Optional[RefType]) -> "FrameMapping":
        """
        Set sourceFrame and return self for chaining.

        Args:
            value: The sourceFrame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_frame("value")
        """
        self.source_frame = value  # Use property setter (gets validation)
        return self

    def with_target_frame(self, value: Optional[RefType]) -> "FrameMapping":
        """
        Set targetFrame and return self for chaining.

        Args:
            value: The targetFrame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_frame("value")
        """
        self.target_frame = value  # Use property setter (gets validation)
        return self
