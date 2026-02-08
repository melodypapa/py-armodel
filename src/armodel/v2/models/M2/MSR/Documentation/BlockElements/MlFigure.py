from typing import (
    List,
    Optional,
)


class MlFigure(Paginateable):
    """
    This metaclass represents the ability to embed a figure.

    Package: M2::MSR::Documentation::BlockElements::Figure

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 307, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element specifies the title of an illustration.
        self._figureCaption: Optional["Caption"] = None

    @property
    def figure_caption(self) -> Optional["Caption"]:
        """Get figureCaption (Pythonic accessor)."""
        return self._figureCaption

    @figure_caption.setter
    def figure_caption(self, value: Optional["Caption"]) -> None:
        """
        Set figureCaption with validation.

        Args:
            value: The figureCaption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._figureCaption = None
            return

        if not isinstance(value, Caption):
            raise TypeError(
                f"figureCaption must be Caption or None, got {type(value).__name__}"
            )
        self._figureCaption = value
        # Used to defined the frame line around a figure.
        # It can following values: - Border at the top of the figure - Border at the
                # bottom of the figure - Borders at the top and bottom of the figure - Borders
                # all around the figure - Borders at the sides of the figure - No borders
                # around the figure.
        self._frame: Optional["FrameEnum"] = None

    @property
    def frame(self) -> Optional["FrameEnum"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["FrameEnum"]) -> None:
        """
        Set frame with validation.

        Args:
            value: The frame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, FrameEnum):
            raise TypeError(
                f"frame must be FrameEnum or None, got {type(value).__name__}"
            )
        self._frame = value
        # This specifies an entry point in an online help system to with the parent
                # class.
        # The syntax shall be the applied help system respectively help.
        self._helpEntry: Optional["String"] = None

    @property
    def help_entry(self) -> Optional["String"]:
        """Get helpEntry (Pythonic accessor)."""
        return self._helpEntry

    @help_entry.setter
    def help_entry(self, value: Optional["String"]) -> None:
        """
        Set helpEntry with validation.

        Args:
            value: The helpEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._helpEntry = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"helpEntry must be String or None, got {type(value).__name__}"
            )
        self._helpEntry = value
        # Container of the graphic (or diagram) and optional map of in a given
        # language.
        self._lGraphic: List["LGraphic"] = []

    @property
    def l_graphic(self) -> List["LGraphic"]:
        """Get lGraphic (Pythonic accessor)."""
        return self._lGraphic
        # Used to indicate wether the figure should take the width (value = "pgwide")
        # or not (value =.
        self._pgwide: Optional["PgwideEnum"] = None

    @property
    def pgwide(self) -> Optional["PgwideEnum"]:
        """Get pgwide (Pythonic accessor)."""
        return self._pgwide

    @pgwide.setter
    def pgwide(self, value: Optional["PgwideEnum"]) -> None:
        """
        Set pgwide with validation.

        Args:
            value: The pgwide to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pgwide = None
            return

        if not isinstance(value, PgwideEnum):
            raise TypeError(
                f"pgwide must be PgwideEnum or None, got {type(value).__name__}"
            )
        self._pgwide = value
        # <verbatim> is a paragraph in which white-space (in and line feeds) is obeyed.
        # This enables to be carried out, which can even be simple devices.
        # Behavior is the same as HTML.
        self._verbatim: Optional["MultiLanguageVerbatim"] = None

    @property
    def verbatim(self) -> Optional["MultiLanguageVerbatim"]:
        """Get verbatim (Pythonic accessor)."""
        return self._verbatim

    @verbatim.setter
    def verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> None:
        """
        Set verbatim with validation.

        Args:
            value: The verbatim to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._verbatim = None
            return

        if not isinstance(value, MultiLanguageVerbatim):
            raise TypeError(
                f"verbatim must be MultiLanguageVerbatim or None, got {type(value).__name__}"
            )
        self._verbatim = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFigureCaption(self) -> "Caption":
        """
        AUTOSAR-compliant getter for figureCaption.

        Returns:
            The figureCaption value

        Note:
            Delegates to figure_caption property (CODING_RULE_V2_00017)
        """
        return self.figure_caption  # Delegates to property

    def setFigureCaption(self, value: "Caption") -> "MlFigure":
        """
        AUTOSAR-compliant setter for figureCaption with method chaining.

        Args:
            value: The figureCaption to set

        Returns:
            self for method chaining

        Note:
            Delegates to figure_caption property setter (gets validation automatically)
        """
        self.figure_caption = value  # Delegates to property setter
        return self

    def getFrame(self) -> "FrameEnum":
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "FrameEnum") -> "MlFigure":
        """
        AUTOSAR-compliant setter for frame with method chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
        return self

    def getHelpEntry(self) -> "String":
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: "String") -> "MlFigure":
        """
        AUTOSAR-compliant setter for helpEntry with method chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to help_entry property setter (gets validation automatically)
        """
        self.help_entry = value  # Delegates to property setter
        return self

    def getLGraphic(self) -> List["LGraphic"]:
        """
        AUTOSAR-compliant getter for lGraphic.

        Returns:
            The lGraphic value

        Note:
            Delegates to l_graphic property (CODING_RULE_V2_00017)
        """
        return self.l_graphic  # Delegates to property

    def getPgwide(self) -> "PgwideEnum":
        """
        AUTOSAR-compliant getter for pgwide.

        Returns:
            The pgwide value

        Note:
            Delegates to pgwide property (CODING_RULE_V2_00017)
        """
        return self.pgwide  # Delegates to property

    def setPgwide(self, value: "PgwideEnum") -> "MlFigure":
        """
        AUTOSAR-compliant setter for pgwide with method chaining.

        Args:
            value: The pgwide to set

        Returns:
            self for method chaining

        Note:
            Delegates to pgwide property setter (gets validation automatically)
        """
        self.pgwide = value  # Delegates to property setter
        return self

    def getVerbatim(self) -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant getter for verbatim.

        Returns:
            The verbatim value

        Note:
            Delegates to verbatim property (CODING_RULE_V2_00017)
        """
        return self.verbatim  # Delegates to property

    def setVerbatim(self, value: "MultiLanguageVerbatim") -> "MlFigure":
        """
        AUTOSAR-compliant setter for verbatim with method chaining.

        Args:
            value: The verbatim to set

        Returns:
            self for method chaining

        Note:
            Delegates to verbatim property setter (gets validation automatically)
        """
        self.verbatim = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_figure_caption(self, value: Optional["Caption"]) -> "MlFigure":
        """
        Set figureCaption and return self for chaining.

        Args:
            value: The figureCaption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_figure_caption("value")
        """
        self.figure_caption = value  # Use property setter (gets validation)
        return self

    def with_frame(self, value: Optional["FrameEnum"]) -> "MlFigure":
        """
        Set frame and return self for chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self

    def with_help_entry(self, value: Optional["String"]) -> "MlFigure":
        """
        Set helpEntry and return self for chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_help_entry("value")
        """
        self.help_entry = value  # Use property setter (gets validation)
        return self

    def with_pgwide(self, value: Optional["PgwideEnum"]) -> "MlFigure":
        """
        Set pgwide and return self for chaining.

        Args:
            value: The pgwide to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pgwide("value")
        """
        self.pgwide = value  # Use property setter (gets validation)
        return self

    def with_verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> "MlFigure":
        """
        Set verbatim and return self for chaining.

        Args:
            value: The verbatim to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_verbatim("value")
        """
        self.verbatim = value  # Use property setter (gets validation)
        return self
