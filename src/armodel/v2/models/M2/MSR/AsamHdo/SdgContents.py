from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SdgContents(ARObject):
    """
    This meta-class represents the possible contents of a special data group. It
    can be an arbitrary mix of references, of primitive special data and nested
    special data groups.

    Package: M2::MSR::AsamHdo::SpecialData

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 90, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular special data element.
        self._sd: Optional["Sd"] = None

    @property
    def sd(self) -> Optional["Sd"]:
        """Get sd (Pythonic accessor)."""
        return self._sd

    @sd.setter
    def sd(self, value: Optional["Sd"]) -> None:
        """
        Set sd with validation.

        Args:
            value: The sd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sd = None
            return

        if not isinstance(value, Sd):
            raise TypeError(
                f"sd must be Sd or None, got {type(value).__name__}"
            )
        self._sd = value
        self._sdf: Optional["Sdf"] = None

    @property
    def sdf(self) -> Optional["Sdf"]:
        """Get sdf (Pythonic accessor)."""
        return self._sdf

    @sdf.setter
    def sdf(self, value: Optional["Sdf"]) -> None:
        """
        Set sdf with validation.

        Args:
            value: The sdf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdf = None
            return

        if not isinstance(value, Sdf):
            raise TypeError(
                f"sdf must be Sdf or None, got {type(value).__name__}"
            )
        self._sdf = value
        # can be represented in atpVariation.
        self._sdg: Optional["Sdg"] = None

    @property
    def sdg(self) -> Optional["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    @sdg.setter
    def sdg(self, value: Optional["Sdg"]) -> None:
        """
        Set sdg with validation.

        Args:
            value: The sdg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdg = None
            return

        if not isinstance(value, Sdg):
            raise TypeError(
                f"sdg must be Sdg or None, got {type(value).__name__}"
            )
        self._sdg = value
        # This allows to use to establish arbitrary relationships.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._sdx: RefType = None

    @property
    def sdx(self) -> RefType:
        """Get sdx (Pythonic accessor)."""
        return self._sdx

    @sdx.setter
    def sdx(self, value: RefType) -> None:
        """
        Set sdx with validation.

        Args:
            value: The sdx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdx = None
            return

        self._sdx = value
        # atpVariation.
        self._sdxf: RefType = None

    @property
    def sdxf(self) -> RefType:
        """Get sdxf (Pythonic accessor)."""
        return self._sdxf

    @sdxf.setter
    def sdxf(self, value: RefType) -> None:
        """
        Set sdxf with validation.

        Args:
            value: The sdxf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdxf = None
            return

        self._sdxf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSd(self) -> "Sd":
        """
        AUTOSAR-compliant getter for sd.

        Returns:
            The sd value

        Note:
            Delegates to sd property (CODING_RULE_V2_00017)
        """
        return self.sd  # Delegates to property

    def setSd(self, value: "Sd") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sd with method chaining.

        Args:
            value: The sd to set

        Returns:
            self for method chaining

        Note:
            Delegates to sd property setter (gets validation automatically)
        """
        self.sd = value  # Delegates to property setter
        return self

    def getSdf(self) -> "Sdf":
        """
        AUTOSAR-compliant getter for sdf.

        Returns:
            The sdf value

        Note:
            Delegates to sdf property (CODING_RULE_V2_00017)
        """
        return self.sdf  # Delegates to property

    def setSdf(self, value: "Sdf") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdf with method chaining.

        Args:
            value: The sdf to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdf property setter (gets validation automatically)
        """
        self.sdf = value  # Delegates to property setter
        return self

    def getSdg(self) -> "Sdg":
        """
        AUTOSAR-compliant getter for sdg.

        Returns:
            The sdg value

        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    def setSdg(self, value: "Sdg") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdg with method chaining.

        Args:
            value: The sdg to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdg property setter (gets validation automatically)
        """
        self.sdg = value  # Delegates to property setter
        return self

    def getSdx(self) -> RefType:
        """
        AUTOSAR-compliant getter for sdx.

        Returns:
            The sdx value

        Note:
            Delegates to sdx property (CODING_RULE_V2_00017)
        """
        return self.sdx  # Delegates to property

    def setSdx(self, value: RefType) -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdx with method chaining.

        Args:
            value: The sdx to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdx property setter (gets validation automatically)
        """
        self.sdx = value  # Delegates to property setter
        return self

    def getSdxf(self) -> RefType:
        """
        AUTOSAR-compliant getter for sdxf.

        Returns:
            The sdxf value

        Note:
            Delegates to sdxf property (CODING_RULE_V2_00017)
        """
        return self.sdxf  # Delegates to property

    def setSdxf(self, value: RefType) -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdxf with method chaining.

        Args:
            value: The sdxf to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdxf property setter (gets validation automatically)
        """
        self.sdxf = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sd(self, value: Optional["Sd"]) -> "SdgContents":
        """
        Set sd and return self for chaining.

        Args:
            value: The sd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sd("value")
        """
        self.sd = value  # Use property setter (gets validation)
        return self

    def with_sdf(self, value: Optional["Sdf"]) -> "SdgContents":
        """
        Set sdf and return self for chaining.

        Args:
            value: The sdf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdf("value")
        """
        self.sdf = value  # Use property setter (gets validation)
        return self

    def with_sdg(self, value: Optional["Sdg"]) -> "SdgContents":
        """
        Set sdg and return self for chaining.

        Args:
            value: The sdg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg("value")
        """
        self.sdg = value  # Use property setter (gets validation)
        return self

    def with_sdx(self, value: Optional[RefType]) -> "SdgContents":
        """
        Set sdx and return self for chaining.

        Args:
            value: The sdx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdx("value")
        """
        self.sdx = value  # Use property setter (gets validation)
        return self

    def with_sdxf(self, value: Optional[RefType]) -> "SdgContents":
        """
        Set sdxf and return self for chaining.

        Args:
            value: The sdxf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdxf("value")
        """
        self.sdxf = value  # Use property setter (gets validation)
        return self
