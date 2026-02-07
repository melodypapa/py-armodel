from typing import Optional


class IEEE1722TpRvfConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp RVF connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv::IEEE1722TpRvfConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 649, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the RVF stream active_pixels.
        self._rvfActivePixels: Optional["PositiveInteger"] = None

    @property
    def rvf_active_pixels(self) -> Optional["PositiveInteger"]:
        """Get rvfActivePixels (Pythonic accessor)."""
        return self._rvfActivePixels

    @rvf_active_pixels.setter
    def rvf_active_pixels(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set rvfActivePixels with validation.

        Args:
            value: The rvfActivePixels to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfActivePixels = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"rvfActivePixels must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._rvfActivePixels = value
        # Definition of the RVF stream colorspace.
        # atp.
        # Status=candidate 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._rvfColorSpace: Optional["IEEE1722TpRvfColor"] = None

    @property
    def rvf_color_space(self) -> Optional["IEEE1722TpRvfColor"]:
        """Get rvfColorSpace (Pythonic accessor)."""
        return self._rvfColorSpace

    @rvf_color_space.setter
    def rvf_color_space(self, value: Optional["IEEE1722TpRvfColor"]) -> None:
        """
        Set rvfColorSpace with validation.

        Args:
            value: The rvfColorSpace to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfColorSpace = None
            return

        if not isinstance(value, IEEE1722TpRvfColor):
            raise TypeError(
                f"rvfColorSpace must be IEEE1722TpRvfColor or None, got {type(value).__name__}"
            )
        self._rvfColorSpace = value
        # Definition of the RVF stream event (evt) default value.
        self._rvfEventDefault: Optional["PositiveInteger"] = None

    @property
    def rvf_event_default(self) -> Optional["PositiveInteger"]:
        """Get rvfEventDefault (Pythonic accessor)."""
        return self._rvfEventDefault

    @rvf_event_default.setter
    def rvf_event_default(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set rvfEventDefault with validation.

        Args:
            value: The rvfEventDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfEventDefault = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"rvfEventDefault must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._rvfEventDefault = value
        # Definition of the RVF stream frame_rate.
        # atp.
        # Status=candidate.
        self._rvfFrameRate: Optional["IEEE1722TpRvfFrame"] = None

    @property
    def rvf_frame_rate(self) -> Optional["IEEE1722TpRvfFrame"]:
        """Get rvfFrameRate (Pythonic accessor)."""
        return self._rvfFrameRate

    @rvf_frame_rate.setter
    def rvf_frame_rate(self, value: Optional["IEEE1722TpRvfFrame"]) -> None:
        """
        Set rvfFrameRate with validation.

        Args:
            value: The rvfFrameRate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfFrameRate = None
            return

        if not isinstance(value, IEEE1722TpRvfFrame):
            raise TypeError(
                f"rvfFrameRate must be IEEE1722TpRvfFrame or None, got {type(value).__name__}"
            )
        self._rvfFrameRate = value
        # Defines the RVF stream interlaced (i).
        self._rvfInterlaced: Optional["Boolean"] = None

    @property
    def rvf_interlaced(self) -> Optional["Boolean"]:
        """Get rvfInterlaced (Pythonic accessor)."""
        return self._rvfInterlaced

    @rvf_interlaced.setter
    def rvf_interlaced(self, value: Optional["Boolean"]) -> None:
        """
        Set rvfInterlaced with validation.

        Args:
            value: The rvfInterlaced to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfInterlaced = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"rvfInterlaced must be Boolean or None, got {type(value).__name__}"
            )
        self._rvfInterlaced = value
        # Definition of the RVF stream pixel_depth.
        # atp.
        # Status=candidate.
        self._rvfPixelDepth: Optional["IEEE1722TpRvfPixel"] = None

    @property
    def rvf_pixel_depth(self) -> Optional["IEEE1722TpRvfPixel"]:
        """Get rvfPixelDepth (Pythonic accessor)."""
        return self._rvfPixelDepth

    @rvf_pixel_depth.setter
    def rvf_pixel_depth(self, value: Optional["IEEE1722TpRvfPixel"]) -> None:
        """
        Set rvfPixelDepth with validation.

        Args:
            value: The rvfPixelDepth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfPixelDepth = None
            return

        if not isinstance(value, IEEE1722TpRvfPixel):
            raise TypeError(
                f"rvfPixelDepth must be IEEE1722TpRvfPixel or None, got {type(value).__name__}"
            )
        self._rvfPixelDepth = value
        # Definition of the RVF stream pixel_format.
        # atp.
        # Status=candidate.
        self._rvfPixelFormat: Optional["IEEE1722TpRvfPixel"] = None

    @property
    def rvf_pixel_format(self) -> Optional["IEEE1722TpRvfPixel"]:
        """Get rvfPixelFormat (Pythonic accessor)."""
        return self._rvfPixelFormat

    @rvf_pixel_format.setter
    def rvf_pixel_format(self, value: Optional["IEEE1722TpRvfPixel"]) -> None:
        """
        Set rvfPixelFormat with validation.

        Args:
            value: The rvfPixelFormat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfPixelFormat = None
            return

        if not isinstance(value, IEEE1722TpRvfPixel):
            raise TypeError(
                f"rvfPixelFormat must be IEEE1722TpRvfPixel or None, got {type(value).__name__}"
            )
        self._rvfPixelFormat = value
        # Definition of the RVF stream total_lines.
        self._rvfTotalLines: Optional["PositiveInteger"] = None

    @property
    def rvf_total_lines(self) -> Optional["PositiveInteger"]:
        """Get rvfTotalLines (Pythonic accessor)."""
        return self._rvfTotalLines

    @rvf_total_lines.setter
    def rvf_total_lines(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set rvfTotalLines with validation.

        Args:
            value: The rvfTotalLines to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rvfTotalLines = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"rvfTotalLines must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._rvfTotalLines = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRvfActivePixels(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rvfActivePixels.

        Returns:
            The rvfActivePixels value

        Note:
            Delegates to rvf_active_pixels property (CODING_RULE_V2_00017)
        """
        return self.rvf_active_pixels  # Delegates to property

    def setRvfActivePixels(self, value: "PositiveInteger") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfActivePixels with method chaining.

        Args:
            value: The rvfActivePixels to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_active_pixels property setter (gets validation automatically)
        """
        self.rvf_active_pixels = value  # Delegates to property setter
        return self

    def getRvfColorSpace(self) -> "IEEE1722TpRvfColor":
        """
        AUTOSAR-compliant getter for rvfColorSpace.

        Returns:
            The rvfColorSpace value

        Note:
            Delegates to rvf_color_space property (CODING_RULE_V2_00017)
        """
        return self.rvf_color_space  # Delegates to property

    def setRvfColorSpace(self, value: "IEEE1722TpRvfColor") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfColorSpace with method chaining.

        Args:
            value: The rvfColorSpace to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_color_space property setter (gets validation automatically)
        """
        self.rvf_color_space = value  # Delegates to property setter
        return self

    def getRvfEventDefault(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rvfEventDefault.

        Returns:
            The rvfEventDefault value

        Note:
            Delegates to rvf_event_default property (CODING_RULE_V2_00017)
        """
        return self.rvf_event_default  # Delegates to property

    def setRvfEventDefault(self, value: "PositiveInteger") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfEventDefault with method chaining.

        Args:
            value: The rvfEventDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_event_default property setter (gets validation automatically)
        """
        self.rvf_event_default = value  # Delegates to property setter
        return self

    def getRvfFrameRate(self) -> "IEEE1722TpRvfFrame":
        """
        AUTOSAR-compliant getter for rvfFrameRate.

        Returns:
            The rvfFrameRate value

        Note:
            Delegates to rvf_frame_rate property (CODING_RULE_V2_00017)
        """
        return self.rvf_frame_rate  # Delegates to property

    def setRvfFrameRate(self, value: "IEEE1722TpRvfFrame") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfFrameRate with method chaining.

        Args:
            value: The rvfFrameRate to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_frame_rate property setter (gets validation automatically)
        """
        self.rvf_frame_rate = value  # Delegates to property setter
        return self

    def getRvfInterlaced(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for rvfInterlaced.

        Returns:
            The rvfInterlaced value

        Note:
            Delegates to rvf_interlaced property (CODING_RULE_V2_00017)
        """
        return self.rvf_interlaced  # Delegates to property

    def setRvfInterlaced(self, value: "Boolean") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfInterlaced with method chaining.

        Args:
            value: The rvfInterlaced to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_interlaced property setter (gets validation automatically)
        """
        self.rvf_interlaced = value  # Delegates to property setter
        return self

    def getRvfPixelDepth(self) -> "IEEE1722TpRvfPixel":
        """
        AUTOSAR-compliant getter for rvfPixelDepth.

        Returns:
            The rvfPixelDepth value

        Note:
            Delegates to rvf_pixel_depth property (CODING_RULE_V2_00017)
        """
        return self.rvf_pixel_depth  # Delegates to property

    def setRvfPixelDepth(self, value: "IEEE1722TpRvfPixel") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfPixelDepth with method chaining.

        Args:
            value: The rvfPixelDepth to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_pixel_depth property setter (gets validation automatically)
        """
        self.rvf_pixel_depth = value  # Delegates to property setter
        return self

    def getRvfPixelFormat(self) -> "IEEE1722TpRvfPixel":
        """
        AUTOSAR-compliant getter for rvfPixelFormat.

        Returns:
            The rvfPixelFormat value

        Note:
            Delegates to rvf_pixel_format property (CODING_RULE_V2_00017)
        """
        return self.rvf_pixel_format  # Delegates to property

    def setRvfPixelFormat(self, value: "IEEE1722TpRvfPixel") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfPixelFormat with method chaining.

        Args:
            value: The rvfPixelFormat to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_pixel_format property setter (gets validation automatically)
        """
        self.rvf_pixel_format = value  # Delegates to property setter
        return self

    def getRvfTotalLines(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rvfTotalLines.

        Returns:
            The rvfTotalLines value

        Note:
            Delegates to rvf_total_lines property (CODING_RULE_V2_00017)
        """
        return self.rvf_total_lines  # Delegates to property

    def setRvfTotalLines(self, value: "PositiveInteger") -> "IEEE1722TpRvfConnection":
        """
        AUTOSAR-compliant setter for rvfTotalLines with method chaining.

        Args:
            value: The rvfTotalLines to set

        Returns:
            self for method chaining

        Note:
            Delegates to rvf_total_lines property setter (gets validation automatically)
        """
        self.rvf_total_lines = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rvf_active_pixels(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfActivePixels and return self for chaining.

        Args:
            value: The rvfActivePixels to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_active_pixels("value")
        """
        self.rvf_active_pixels = value  # Use property setter (gets validation)
        return self

    def with_rvf_color_space(self, value: Optional["IEEE1722TpRvfColor"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfColorSpace and return self for chaining.

        Args:
            value: The rvfColorSpace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_color_space("value")
        """
        self.rvf_color_space = value  # Use property setter (gets validation)
        return self

    def with_rvf_event_default(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfEventDefault and return self for chaining.

        Args:
            value: The rvfEventDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_event_default("value")
        """
        self.rvf_event_default = value  # Use property setter (gets validation)
        return self

    def with_rvf_frame_rate(self, value: Optional["IEEE1722TpRvfFrame"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfFrameRate and return self for chaining.

        Args:
            value: The rvfFrameRate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_frame_rate("value")
        """
        self.rvf_frame_rate = value  # Use property setter (gets validation)
        return self

    def with_rvf_interlaced(self, value: Optional["Boolean"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfInterlaced and return self for chaining.

        Args:
            value: The rvfInterlaced to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_interlaced("value")
        """
        self.rvf_interlaced = value  # Use property setter (gets validation)
        return self

    def with_rvf_pixel_depth(self, value: Optional["IEEE1722TpRvfPixel"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfPixelDepth and return self for chaining.

        Args:
            value: The rvfPixelDepth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_pixel_depth("value")
        """
        self.rvf_pixel_depth = value  # Use property setter (gets validation)
        return self

    def with_rvf_pixel_format(self, value: Optional["IEEE1722TpRvfPixel"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfPixelFormat and return self for chaining.

        Args:
            value: The rvfPixelFormat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_pixel_format("value")
        """
        self.rvf_pixel_format = value  # Use property setter (gets validation)
        return self

    def with_rvf_total_lines(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpRvfConnection":
        """
        Set rvfTotalLines and return self for chaining.

        Args:
            value: The rvfTotalLines to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rvf_total_lines("value")
        """
        self.rvf_total_lines = value  # Use property setter (gets validation)
        return self
