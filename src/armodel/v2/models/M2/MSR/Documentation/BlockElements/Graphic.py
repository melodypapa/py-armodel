from typing import Optional


class Graphic(EngineeringObject):
    """
    This class represents an artifact containing the image to be inserted in the
    document

    Package: M2::MSR::Documentation::BlockElements::Figure

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 302, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies how the graphic shall be displayed in an editor.
        # attribute is missing,.
        self._editfit: Optional["GraphicFitEnum"] = None

    @property
    def editfit(self) -> Optional["GraphicFitEnum"]:
        """Get editfit (Pythonic accessor)."""
        return self._editfit

    @editfit.setter
    def editfit(self, value: Optional["GraphicFitEnum"]) -> None:
        """
        Set editfit with validation.

        Args:
            value: The editfit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editfit = None
            return

        if not isinstance(value, GraphicFitEnum):
            raise TypeError(
                f"editfit must be GraphicFitEnum or None, got {type(value).__name__}"
            )
        self._editfit = value
        # Specifies the height of the graphic when it is displayed in The unit can be
                # added to the number in the units are: cm, mm, px, pt.
        # The default unit.
        self._editHeight: Optional["String"] = None

    @property
    def edit_height(self) -> Optional["String"]:
        """Get editHeight (Pythonic accessor)."""
        return self._editHeight

    @edit_height.setter
    def edit_height(self, value: Optional["String"]) -> None:
        """
        Set editHeight with validation.

        Args:
            value: The editHeight to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editHeight = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"editHeight must be String or None, got {type(value).__name__}"
            )
        self._editHeight = value
        # Set the proportional scale when displayed in an editor.
        self._editscale: Optional["String"] = None

    @property
    def editscale(self) -> Optional["String"]:
        """Get editscale (Pythonic accessor)."""
        return self._editscale

    @editscale.setter
    def editscale(self, value: Optional["String"]) -> None:
        """
        Set editscale with validation.

        Args:
            value: The editscale to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editscale = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"editscale must be String or None, got {type(value).__name__}"
            )
        self._editscale = value
        # Specifies the width of the graphic when it is displayed in The unit can be
                # added to the number in the units are: cm, mm, px, pt.
        # The default unit.
        self._editWidth: Optional["String"] = None

    @property
    def edit_width(self) -> Optional["String"]:
        """Get editWidth (Pythonic accessor)."""
        return self._editWidth

    @edit_width.setter
    def edit_width(self, value: Optional["String"]) -> None:
        """
        Set editWidth with validation.

        Args:
            value: The editWidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editWidth = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"editWidth must be String or None, got {type(value).__name__}"
            )
        self._editWidth = value
        # Name of the file that should be displayed.
        # This attribute is ASAM FSX and kept in AUTOSAR in order cut and paste.
        self._filename: Optional["String"] = None

    @property
    def filename(self) -> Optional["String"]:
        """Get filename (Pythonic accessor)."""
        return self._filename

    @filename.setter
    def filename(self, value: Optional["String"]) -> None:
        """
        Set filename with validation.

        Args:
            value: The filename to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filename = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"filename must be String or None, got {type(value).__name__}"
            )
        self._filename = value
        # It determines the way in which the graphic should be attribute value "AS-IS"
                # , to insert a graphic in its is adapted, if it is too big for the space for
                # was intended.
        # Default is "AS-IS" 535 Document ID 202:
                # AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._fit: Optional["GraphicFitEnum"] = None

    @property
    def fit(self) -> Optional["GraphicFitEnum"]:
        """Get fit (Pythonic accessor)."""
        return self._fit

    @fit.setter
    def fit(self, value: Optional["GraphicFitEnum"]) -> None:
        """
        Set fit with validation.

        Args:
            value: The fit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fit = None
            return

        if not isinstance(value, GraphicFitEnum):
            raise TypeError(
                f"fit must be GraphicFitEnum or None, got {type(value).__name__}"
            )
        self._fit = value
        # This attribute specifies the generator which is used to image.
        # is that when editing a documentation, a figure delivered by the modeling
                # tool) is inserted by the as reference (this is the role of graphic).
        # real figure maybe injected during document be able to recognize this
                # situation, this be applied.
        self._generator: Optional["NameToken"] = None

    @property
    def generator(self) -> Optional["NameToken"]:
        """Get generator (Pythonic accessor)."""
        return self._generator

    @generator.setter
    def generator(self, value: Optional["NameToken"]) -> None:
        """
        Set generator with validation.

        Args:
            value: The generator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._generator = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"generator must be NameToken or None, got {type(value).__name__}"
            )
        self._generator = value
        # Define the displayed height of the figure.
        # The unit can be the number in the string.
        # Possible units are: cm, pt.
        # The default unit is px.
        self._height: Optional["String"] = None

    @property
    def height(self) -> Optional["String"]:
        """Get height (Pythonic accessor)."""
        return self._height

    @height.setter
    def height(self, value: Optional["String"]) -> None:
        """
        Set height with validation.

        Args:
            value: The height to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._height = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"height must be String or None, got {type(value).__name__}"
            )
        self._height = value
        # How to fit the graphic in an online media.
        # Default is AS-IS.
        self._htmlFit: Optional["GraphicFitEnum"] = None

    @property
    def html_fit(self) -> Optional["GraphicFitEnum"]:
        """Get htmlFit (Pythonic accessor)."""
        return self._htmlFit

    @html_fit.setter
    def html_fit(self, value: Optional["GraphicFitEnum"]) -> None:
        """
        Set htmlFit with validation.

        Args:
            value: The htmlFit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlFit = None
            return

        if not isinstance(value, GraphicFitEnum):
            raise TypeError(
                f"htmlFit must be GraphicFitEnum or None, got {type(value).__name__}"
            )
        self._htmlFit = value
        # Specifies the height of the graphic when it is displayed unit can be added to
                # the number in the string.
        # are: cm, mm, px, pt.
        # The default unit is px.
        self._htmlHeight: Optional["String"] = None

    @property
    def html_height(self) -> Optional["String"]:
        """Get htmlHeight (Pythonic accessor)."""
        return self._htmlHeight

    @html_height.setter
    def html_height(self, value: Optional["String"]) -> None:
        """
        Set htmlHeight with validation.

        Args:
            value: The htmlHeight to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlHeight = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"htmlHeight must be String or None, got {type(value).__name__}"
            )
        self._htmlHeight = value
        # Set the proportional scale when displayed online.
        self._htmlScale: Optional["String"] = None

    @property
    def html_scale(self) -> Optional["String"]:
        """Get htmlScale (Pythonic accessor)."""
        return self._htmlScale

    @html_scale.setter
    def html_scale(self, value: Optional["String"]) -> None:
        """
        Set htmlScale with validation.

        Args:
            value: The htmlScale to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlScale = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"htmlScale must be String or None, got {type(value).__name__}"
            )
        self._htmlScale = value
        # Specifies the width of the graphic when it is displayed unit can be added to
                # the number in the string.
        # are: cm, mm, px, pt.
        # The default unit is px.
        self._htmlWidth: Optional["String"] = None

    @property
    def html_width(self) -> Optional["String"]:
        """Get htmlWidth (Pythonic accessor)."""
        return self._htmlWidth

    @html_width.setter
    def html_width(self, value: Optional["String"]) -> None:
        """
        Set htmlWidth with validation.

        Args:
            value: The htmlWidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlWidth = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"htmlWidth must be String or None, got {type(value).__name__}"
            )
        self._htmlWidth = value
        # This attribute captures the format used to represent the.
        self._notation: Optional["GraphicNotationEnum"] = None

    @property
    def notation(self) -> Optional["GraphicNotationEnum"]:
        """Get notation (Pythonic accessor)."""
        return self._notation

    @notation.setter
    def notation(self, value: Optional["GraphicNotationEnum"]) -> None:
        """
        Set notation with validation.

        Args:
            value: The notation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._notation = None
            return

        if not isinstance(value, GraphicNotationEnum):
            raise TypeError(
                f"notation must be GraphicNotationEnum or None, got {type(value).__name__}"
            )
        self._notation = value
        # In this element the dimensions of the graphic can be.
        self._scale: Optional["String"] = None

    @property
    def scale(self) -> Optional["String"]:
        """Get scale (Pythonic accessor)."""
        return self._scale

    @scale.setter
    def scale(self, value: Optional["String"]) -> None:
        """
        Set scale with validation.

        Args:
            value: The scale to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scale = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"scale must be String or None, got {type(value).__name__}"
            )
        self._scale = value
        # Define the displayed width of the figure.
        # The unit can be the number in the string.
        # Possible units are: cm, pt.
        # The default unit is px.
        self._width: Optional["String"] = None

    @property
    def width(self) -> Optional["String"]:
        """Get width (Pythonic accessor)."""
        return self._width

    @width.setter
    def width(self, value: Optional["String"]) -> None:
        """
        Set width with validation.

        Args:
            value: The width to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._width = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"width must be String or None, got {type(value).__name__}"
            )
        self._width = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEditfit(self) -> "GraphicFitEnum":
        """
        AUTOSAR-compliant getter for editfit.

        Returns:
            The editfit value

        Note:
            Delegates to editfit property (CODING_RULE_V2_00017)
        """
        return self.editfit  # Delegates to property

    def setEditfit(self, value: "GraphicFitEnum") -> "Graphic":
        """
        AUTOSAR-compliant setter for editfit with method chaining.

        Args:
            value: The editfit to set

        Returns:
            self for method chaining

        Note:
            Delegates to editfit property setter (gets validation automatically)
        """
        self.editfit = value  # Delegates to property setter
        return self

    def getEditHeight(self) -> "String":
        """
        AUTOSAR-compliant getter for editHeight.

        Returns:
            The editHeight value

        Note:
            Delegates to edit_height property (CODING_RULE_V2_00017)
        """
        return self.edit_height  # Delegates to property

    def setEditHeight(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for editHeight with method chaining.

        Args:
            value: The editHeight to set

        Returns:
            self for method chaining

        Note:
            Delegates to edit_height property setter (gets validation automatically)
        """
        self.edit_height = value  # Delegates to property setter
        return self

    def getEditscale(self) -> "String":
        """
        AUTOSAR-compliant getter for editscale.

        Returns:
            The editscale value

        Note:
            Delegates to editscale property (CODING_RULE_V2_00017)
        """
        return self.editscale  # Delegates to property

    def setEditscale(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for editscale with method chaining.

        Args:
            value: The editscale to set

        Returns:
            self for method chaining

        Note:
            Delegates to editscale property setter (gets validation automatically)
        """
        self.editscale = value  # Delegates to property setter
        return self

    def getEditWidth(self) -> "String":
        """
        AUTOSAR-compliant getter for editWidth.

        Returns:
            The editWidth value

        Note:
            Delegates to edit_width property (CODING_RULE_V2_00017)
        """
        return self.edit_width  # Delegates to property

    def setEditWidth(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for editWidth with method chaining.

        Args:
            value: The editWidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to edit_width property setter (gets validation automatically)
        """
        self.edit_width = value  # Delegates to property setter
        return self

    def getFilename(self) -> "String":
        """
        AUTOSAR-compliant getter for filename.

        Returns:
            The filename value

        Note:
            Delegates to filename property (CODING_RULE_V2_00017)
        """
        return self.filename  # Delegates to property

    def setFilename(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for filename with method chaining.

        Args:
            value: The filename to set

        Returns:
            self for method chaining

        Note:
            Delegates to filename property setter (gets validation automatically)
        """
        self.filename = value  # Delegates to property setter
        return self

    def getFit(self) -> "GraphicFitEnum":
        """
        AUTOSAR-compliant getter for fit.

        Returns:
            The fit value

        Note:
            Delegates to fit property (CODING_RULE_V2_00017)
        """
        return self.fit  # Delegates to property

    def setFit(self, value: "GraphicFitEnum") -> "Graphic":
        """
        AUTOSAR-compliant setter for fit with method chaining.

        Args:
            value: The fit to set

        Returns:
            self for method chaining

        Note:
            Delegates to fit property setter (gets validation automatically)
        """
        self.fit = value  # Delegates to property setter
        return self

    def getGenerator(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for generator.

        Returns:
            The generator value

        Note:
            Delegates to generator property (CODING_RULE_V2_00017)
        """
        return self.generator  # Delegates to property

    def setGenerator(self, value: "NameToken") -> "Graphic":
        """
        AUTOSAR-compliant setter for generator with method chaining.

        Args:
            value: The generator to set

        Returns:
            self for method chaining

        Note:
            Delegates to generator property setter (gets validation automatically)
        """
        self.generator = value  # Delegates to property setter
        return self

    def getHeight(self) -> "String":
        """
        AUTOSAR-compliant getter for height.

        Returns:
            The height value

        Note:
            Delegates to height property (CODING_RULE_V2_00017)
        """
        return self.height  # Delegates to property

    def setHeight(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for height with method chaining.

        Args:
            value: The height to set

        Returns:
            self for method chaining

        Note:
            Delegates to height property setter (gets validation automatically)
        """
        self.height = value  # Delegates to property setter
        return self

    def getHtmlFit(self) -> "GraphicFitEnum":
        """
        AUTOSAR-compliant getter for htmlFit.

        Returns:
            The htmlFit value

        Note:
            Delegates to html_fit property (CODING_RULE_V2_00017)
        """
        return self.html_fit  # Delegates to property

    def setHtmlFit(self, value: "GraphicFitEnum") -> "Graphic":
        """
        AUTOSAR-compliant setter for htmlFit with method chaining.

        Args:
            value: The htmlFit to set

        Returns:
            self for method chaining

        Note:
            Delegates to html_fit property setter (gets validation automatically)
        """
        self.html_fit = value  # Delegates to property setter
        return self

    def getHtmlHeight(self) -> "String":
        """
        AUTOSAR-compliant getter for htmlHeight.

        Returns:
            The htmlHeight value

        Note:
            Delegates to html_height property (CODING_RULE_V2_00017)
        """
        return self.html_height  # Delegates to property

    def setHtmlHeight(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for htmlHeight with method chaining.

        Args:
            value: The htmlHeight to set

        Returns:
            self for method chaining

        Note:
            Delegates to html_height property setter (gets validation automatically)
        """
        self.html_height = value  # Delegates to property setter
        return self

    def getHtmlScale(self) -> "String":
        """
        AUTOSAR-compliant getter for htmlScale.

        Returns:
            The htmlScale value

        Note:
            Delegates to html_scale property (CODING_RULE_V2_00017)
        """
        return self.html_scale  # Delegates to property

    def setHtmlScale(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for htmlScale with method chaining.

        Args:
            value: The htmlScale to set

        Returns:
            self for method chaining

        Note:
            Delegates to html_scale property setter (gets validation automatically)
        """
        self.html_scale = value  # Delegates to property setter
        return self

    def getHtmlWidth(self) -> "String":
        """
        AUTOSAR-compliant getter for htmlWidth.

        Returns:
            The htmlWidth value

        Note:
            Delegates to html_width property (CODING_RULE_V2_00017)
        """
        return self.html_width  # Delegates to property

    def setHtmlWidth(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for htmlWidth with method chaining.

        Args:
            value: The htmlWidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to html_width property setter (gets validation automatically)
        """
        self.html_width = value  # Delegates to property setter
        return self

    def getNotation(self) -> "GraphicNotationEnum":
        """
        AUTOSAR-compliant getter for notation.

        Returns:
            The notation value

        Note:
            Delegates to notation property (CODING_RULE_V2_00017)
        """
        return self.notation  # Delegates to property

    def setNotation(self, value: "GraphicNotationEnum") -> "Graphic":
        """
        AUTOSAR-compliant setter for notation with method chaining.

        Args:
            value: The notation to set

        Returns:
            self for method chaining

        Note:
            Delegates to notation property setter (gets validation automatically)
        """
        self.notation = value  # Delegates to property setter
        return self

    def getScale(self) -> "String":
        """
        AUTOSAR-compliant getter for scale.

        Returns:
            The scale value

        Note:
            Delegates to scale property (CODING_RULE_V2_00017)
        """
        return self.scale  # Delegates to property

    def setScale(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for scale with method chaining.

        Args:
            value: The scale to set

        Returns:
            self for method chaining

        Note:
            Delegates to scale property setter (gets validation automatically)
        """
        self.scale = value  # Delegates to property setter
        return self

    def getWidth(self) -> "String":
        """
        AUTOSAR-compliant getter for width.

        Returns:
            The width value

        Note:
            Delegates to width property (CODING_RULE_V2_00017)
        """
        return self.width  # Delegates to property

    def setWidth(self, value: "String") -> "Graphic":
        """
        AUTOSAR-compliant setter for width with method chaining.

        Args:
            value: The width to set

        Returns:
            self for method chaining

        Note:
            Delegates to width property setter (gets validation automatically)
        """
        self.width = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_editfit(self, value: Optional["GraphicFitEnum"]) -> "Graphic":
        """
        Set editfit and return self for chaining.

        Args:
            value: The editfit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_editfit("value")
        """
        self.editfit = value  # Use property setter (gets validation)
        return self

    def with_edit_height(self, value: Optional["String"]) -> "Graphic":
        """
        Set editHeight and return self for chaining.

        Args:
            value: The editHeight to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_edit_height("value")
        """
        self.edit_height = value  # Use property setter (gets validation)
        return self

    def with_editscale(self, value: Optional["String"]) -> "Graphic":
        """
        Set editscale and return self for chaining.

        Args:
            value: The editscale to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_editscale("value")
        """
        self.editscale = value  # Use property setter (gets validation)
        return self

    def with_edit_width(self, value: Optional["String"]) -> "Graphic":
        """
        Set editWidth and return self for chaining.

        Args:
            value: The editWidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_edit_width("value")
        """
        self.edit_width = value  # Use property setter (gets validation)
        return self

    def with_filename(self, value: Optional["String"]) -> "Graphic":
        """
        Set filename and return self for chaining.

        Args:
            value: The filename to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filename("value")
        """
        self.filename = value  # Use property setter (gets validation)
        return self

    def with_fit(self, value: Optional["GraphicFitEnum"]) -> "Graphic":
        """
        Set fit and return self for chaining.

        Args:
            value: The fit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fit("value")
        """
        self.fit = value  # Use property setter (gets validation)
        return self

    def with_generator(self, value: Optional["NameToken"]) -> "Graphic":
        """
        Set generator and return self for chaining.

        Args:
            value: The generator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_generator("value")
        """
        self.generator = value  # Use property setter (gets validation)
        return self

    def with_height(self, value: Optional["String"]) -> "Graphic":
        """
        Set height and return self for chaining.

        Args:
            value: The height to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_height("value")
        """
        self.height = value  # Use property setter (gets validation)
        return self

    def with_html_fit(self, value: Optional["GraphicFitEnum"]) -> "Graphic":
        """
        Set htmlFit and return self for chaining.

        Args:
            value: The htmlFit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_html_fit("value")
        """
        self.html_fit = value  # Use property setter (gets validation)
        return self

    def with_html_height(self, value: Optional["String"]) -> "Graphic":
        """
        Set htmlHeight and return self for chaining.

        Args:
            value: The htmlHeight to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_html_height("value")
        """
        self.html_height = value  # Use property setter (gets validation)
        return self

    def with_html_scale(self, value: Optional["String"]) -> "Graphic":
        """
        Set htmlScale and return self for chaining.

        Args:
            value: The htmlScale to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_html_scale("value")
        """
        self.html_scale = value  # Use property setter (gets validation)
        return self

    def with_html_width(self, value: Optional["String"]) -> "Graphic":
        """
        Set htmlWidth and return self for chaining.

        Args:
            value: The htmlWidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_html_width("value")
        """
        self.html_width = value  # Use property setter (gets validation)
        return self

    def with_notation(self, value: Optional["GraphicNotationEnum"]) -> "Graphic":
        """
        Set notation and return self for chaining.

        Args:
            value: The notation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_notation("value")
        """
        self.notation = value  # Use property setter (gets validation)
        return self

    def with_scale(self, value: Optional["String"]) -> "Graphic":
        """
        Set scale and return self for chaining.

        Args:
            value: The scale to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scale("value")
        """
        self.scale = value  # Use property setter (gets validation)
        return self

    def with_width(self, value: Optional["String"]) -> "Graphic":
        """
        Set width and return self for chaining.

        Args:
            value: The width to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_width("value")
        """
        self.width = value  # Use property setter (gets validation)
        return self
