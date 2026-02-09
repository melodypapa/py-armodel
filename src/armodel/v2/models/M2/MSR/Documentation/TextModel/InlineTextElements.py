"""
AUTOSAR Package - InlineTextElements

Package: M2::MSR::Documentation::TextModel::InlineTextElements
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    SingleLanguageReferrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class Br(ARObject):
    """
    This element is the same as function here as in a HTML document i.e. it
    forces a line break.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::Br
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 316, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EmphasisText(ARObject):
    """
    This is an emphasized text. As a compromise it contains some rendering
    oriented attributes such as color and font.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::EmphasisText
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 316, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This allows to recommend a color of the emphasis.
        # It is on 6 digits RGB hex-code.
        self._color: Optional["String"] = None

    @property
    def color(self) -> Optional["String"]:
        """Get color (Pythonic accessor)."""
        return self._color

    @color.setter
    def color(self, value: Optional["String"]) -> None:
        """
        Set color with validation.
        
        Args:
            value: The color to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._color = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"color must be String or str or None, got {type(value).__name__}"
            )
        self._color = value
        # This specifies the font style in which the emphasized text rendered.
        self._font: Optional["EEnumFont"] = None

    @property
    def font(self) -> Optional["EEnumFont"]:
        """Get font (Pythonic accessor)."""
        return self._font

    @font.setter
    def font(self, value: Optional["EEnumFont"]) -> None:
        """
        Set font with validation.
        
        Args:
            value: The font to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._font = None
            return

        if not isinstance(value, EEnumFont):
            raise TypeError(
                f"font must be EEnumFont or None, got {type(value).__name__}"
            )
        self._font = value
        # this is subscript text.
        self._sub: "Superscript" = None

    @property
    def sub(self) -> "Superscript":
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: "Superscript") -> None:
        """
        Set sub with validation.
        
        Args:
            value: The sub to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        # This is superscript text.
        self._sup: "Superscript" = None

    @property
    def sup(self) -> "Superscript":
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: "Superscript") -> None:
        """
        Set sup with validation.
        
        Args:
            value: The sup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value
        # This is a technical term.
        self._tt: Optional["Tt"] = None

    @property
    def tt(self) -> Optional["Tt"]:
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: Optional["Tt"]) -> None:
        """
        Set tt with validation.
        
        Args:
            value: The tt to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tt = None
            return

        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt or None, got {type(value).__name__}"
            )
        self._tt = value
        # Indicates how the text may be emphasized.
        # Note that this a proposal which can be overridden or ignored by engines.
        # Default is BOLD.
        self._type: Optional["EEnum"] = None

    @property
    def type(self) -> Optional["EEnum"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["EEnum"]) -> None:
        """
        Set type with validation.
        
        Args:
            value: The type to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        if not isinstance(value, EEnum):
            raise TypeError(
                f"type must be EEnum or None, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getColor(self) -> "String":
        """
        AUTOSAR-compliant getter for color.
        
        Returns:
            The color value
        
        Note:
            Delegates to color property (CODING_RULE_V2_00017)
        """
        return self.color  # Delegates to property

    def setColor(self, value: "String") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for color with method chaining.
        
        Args:
            value: The color to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to color property setter (gets validation automatically)
        """
        self.color = value  # Delegates to property setter
        return self

    def getFont(self) -> "EEnumFont":
        """
        AUTOSAR-compliant getter for font.
        
        Returns:
            The font value
        
        Note:
            Delegates to font property (CODING_RULE_V2_00017)
        """
        return self.font  # Delegates to property

    def setFont(self, value: "EEnumFont") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for font with method chaining.
        
        Args:
            value: The font to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to font property setter (gets validation automatically)
        """
        self.font = value  # Delegates to property setter
        return self

    def getSub(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sub.
        
        Returns:
            The sub value
        
        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: "Superscript") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for sub with method chaining.
        
        Args:
            value: The sub to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sub property setter (gets validation automatically)
        """
        self.sub = value  # Delegates to property setter
        return self

    def getSup(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sup.
        
        Returns:
            The sup value
        
        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: "Superscript") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for sup with method chaining.
        
        Args:
            value: The sup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sup property setter (gets validation automatically)
        """
        self.sup = value  # Delegates to property setter
        return self

    def getTt(self) -> "Tt":
        """
        AUTOSAR-compliant getter for tt.
        
        Returns:
            The tt value
        
        Note:
            Delegates to tt property (CODING_RULE_V2_00017)
        """
        return self.tt  # Delegates to property

    def setTt(self, value: "Tt") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for tt with method chaining.
        
        Args:
            value: The tt to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tt property setter (gets validation automatically)
        """
        self.tt = value  # Delegates to property setter
        return self

    def getType(self) -> "EEnum":
        """
        AUTOSAR-compliant getter for type.
        
        Returns:
            The type value
        
        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "EEnum") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for type with method chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_color(self, value: Optional["String"]) -> "EmphasisText":
        """
        Set color and return self for chaining.
        
        Args:
            value: The color to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_color("value")
        """
        self.color = value  # Use property setter (gets validation)
        return self

    def with_font(self, value: Optional["EEnumFont"]) -> "EmphasisText":
        """
        Set font and return self for chaining.
        
        Args:
            value: The font to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_font("value")
        """
        self.font = value  # Use property setter (gets validation)
        return self

    def with_sub(self, value: "Superscript") -> "EmphasisText":
        """
        Set sub and return self for chaining.
        
        Args:
            value: The sub to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sub("value")
        """
        self.sub = value  # Use property setter (gets validation)
        return self

    def with_sup(self, value: "Superscript") -> "EmphasisText":
        """
        Set sup and return self for chaining.
        
        Args:
            value: The sup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sup("value")
        """
        self.sup = value  # Use property setter (gets validation)
        return self

    def with_tt(self, value: Optional["Tt"]) -> "EmphasisText":
        """
        Set tt and return self for chaining.
        
        Args:
            value: The tt to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tt("value")
        """
        self.tt = value  # Use property setter (gets validation)
        return self

    def with_type(self, value: Optional["EEnum"]) -> "EmphasisText":
        """
        Set type and return self for chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self



class IndexEntry(ARObject):
    """
    This class represents an index entry.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::IndexEntry
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 317, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is subscript text.
        self._sub: "Superscript" = None

    @property
    def sub(self) -> "Superscript":
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: "Superscript") -> None:
        """
        Set sub with validation.
        
        Args:
            value: The sub to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        # This is superscript text.
        self._sup: "Superscript" = None

    @property
    def sup(self) -> "Superscript":
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: "Superscript") -> None:
        """
        Set sup with validation.
        
        Args:
            value: The sup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSub(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sub.
        
        Returns:
            The sub value
        
        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: "Superscript") -> "IndexEntry":
        """
        AUTOSAR-compliant setter for sub with method chaining.
        
        Args:
            value: The sub to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sub property setter (gets validation automatically)
        """
        self.sub = value  # Delegates to property setter
        return self

    def getSup(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sup.
        
        Returns:
            The sup value
        
        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: "Superscript") -> "IndexEntry":
        """
        AUTOSAR-compliant setter for sup with method chaining.
        
        Args:
            value: The sup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sup property setter (gets validation automatically)
        """
        self.sup = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sub(self, value: "Superscript") -> "IndexEntry":
        """
        Set sub and return self for chaining.
        
        Args:
            value: The sub to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sub("value")
        """
        self.sub = value  # Use property setter (gets validation)
        return self

    def with_sup(self, value: "Superscript") -> "IndexEntry":
        """
        Set sup and return self for chaining.
        
        Args:
            value: The sup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sup("value")
        """
        self.sup = value  # Use property setter (gets validation)
        return self



class Std(SingleLanguageReferrable):
    """
    This represents a reference to external standards.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::Std
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 318, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element specifies the release date of the external applicable.
        self._date: Optional["DateTime"] = None

    @property
    def date(self) -> Optional["DateTime"]:
        """Get date (Pythonic accessor)."""
        return self._date

    @date.setter
    def date(self, value: Optional["DateTime"]) -> None:
        """
        Set date with validation.
        
        Args:
            value: The date to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._date = None
            return

        if not isinstance(value, DateTime):
            raise TypeError(
                f"date must be DateTime or None, got {type(value).__name__}"
            )
        self._date = value
        # This represents the reference to the relevant positions of Kept as a string.
        self._position: Optional["String"] = None

    @property
    def position(self) -> Optional["String"]:
        """Get position (Pythonic accessor)."""
        return self._position

    @position.setter
    def position(self, value: Optional["String"]) -> None:
        """
        Set position with validation.
        
        Args:
            value: The position to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._position = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"position must be String or str or None, got {type(value).__name__}"
            )
        self._position = value
        # This represents version and state of a standard.
        # Kept as.
        self._state: Optional["String"] = None

    @property
    def state(self) -> Optional["String"]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional["String"]) -> None:
        """
        Set state with validation.
        
        Args:
            value: The state to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"state must be String or str or None, got {type(value).__name__}"
            )
        self._state = value
        # This represents the subtitle of the standard.
        self._subtitle: Optional["String"] = None

    @property
    def subtitle(self) -> Optional["String"]:
        """Get subtitle (Pythonic accessor)."""
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value: Optional["String"]) -> None:
        """
        Set subtitle with validation.
        
        Args:
            value: The subtitle to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subtitle = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"subtitle must be String or str or None, got {type(value).__name__}"
            )
        self._subtitle = value
        # This represents the URL of the standard.
        self._url: Optional["Url"] = None

    @property
    def url(self) -> Optional["Url"]:
        """Get url (Pythonic accessor)."""
        return self._url

    @url.setter
    def url(self, value: Optional["Url"]) -> None:
        """
        Set url with validation.
        
        Args:
            value: The url to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._url = None
            return

        if not isinstance(value, Url):
            raise TypeError(
                f"url must be Url or None, got {type(value).__name__}"
            )
        self._url = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDate(self) -> "DateTime":
        """
        AUTOSAR-compliant getter for date.
        
        Returns:
            The date value
        
        Note:
            Delegates to date property (CODING_RULE_V2_00017)
        """
        return self.date  # Delegates to property

    def setDate(self, value: "DateTime") -> "Std":
        """
        AUTOSAR-compliant setter for date with method chaining.
        
        Args:
            value: The date to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to date property setter (gets validation automatically)
        """
        self.date = value  # Delegates to property setter
        return self

    def getPosition(self) -> "String":
        """
        AUTOSAR-compliant getter for position.
        
        Returns:
            The position value
        
        Note:
            Delegates to position property (CODING_RULE_V2_00017)
        """
        return self.position  # Delegates to property

    def setPosition(self, value: "String") -> "Std":
        """
        AUTOSAR-compliant setter for position with method chaining.
        
        Args:
            value: The position to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to position property setter (gets validation automatically)
        """
        self.position = value  # Delegates to property setter
        return self

    def getState(self) -> "String":
        """
        AUTOSAR-compliant getter for state.
        
        Returns:
            The state value
        
        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: "String") -> "Std":
        """
        AUTOSAR-compliant setter for state with method chaining.
        
        Args:
            value: The state to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    def getSubtitle(self) -> "String":
        """
        AUTOSAR-compliant getter for subtitle.
        
        Returns:
            The subtitle value
        
        Note:
            Delegates to subtitle property (CODING_RULE_V2_00017)
        """
        return self.subtitle  # Delegates to property

    def setSubtitle(self, value: "String") -> "Std":
        """
        AUTOSAR-compliant setter for subtitle with method chaining.
        
        Args:
            value: The subtitle to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to subtitle property setter (gets validation automatically)
        """
        self.subtitle = value  # Delegates to property setter
        return self

    def getUrl(self) -> "Url":
        """
        AUTOSAR-compliant getter for url.
        
        Returns:
            The url value
        
        Note:
            Delegates to url property (CODING_RULE_V2_00017)
        """
        return self.url  # Delegates to property

    def setUrl(self, value: "Url") -> "Std":
        """
        AUTOSAR-compliant setter for url with method chaining.
        
        Args:
            value: The url to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to url property setter (gets validation automatically)
        """
        self.url = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_date(self, value: Optional["DateTime"]) -> "Std":
        """
        Set date and return self for chaining.
        
        Args:
            value: The date to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_date("value")
        """
        self.date = value  # Use property setter (gets validation)
        return self

    def with_position(self, value: Optional["String"]) -> "Std":
        """
        Set position and return self for chaining.
        
        Args:
            value: The position to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_position("value")
        """
        self.position = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional["String"]) -> "Std":
        """
        Set state and return self for chaining.
        
        Args:
            value: The state to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self

    def with_subtitle(self, value: Optional["String"]) -> "Std":
        """
        Set subtitle and return self for chaining.
        
        Args:
            value: The subtitle to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_subtitle("value")
        """
        self.subtitle = value  # Use property setter (gets validation)
        return self

    def with_url(self, value: Optional["Url"]) -> "Std":
        """
        Set url and return self for chaining.
        
        Args:
            value: The url to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_url("value")
        """
        self.url = value  # Use property setter (gets validation)
        return self



class Tt(ARObject):
    """
    This meta-class represents the ability to express specific technical terms.
    The kind of term is denoted in the attribute "type".
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::Tt
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 318, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the term itself.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._term: "String" = None

    @property
    def term(self) -> "String":
        """Get term (Pythonic accessor)."""
        return self._term

    @term.setter
    def term(self, value: "String") -> None:
        """
        Set term with validation.
        
        Args:
            value: The term to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"term must be String or str, got {type(value).__name__}"
            )
        self._term = value
        # This attribute holds information how the content attribute "term") of the
                # particular is rendered using LaTeX.
        # This allows to LaTeX commands such as \sep{}.
        # An to render "MyClass" as "My\sep{}Class".
        # the value of the attribute "term".
        self._texRender: Optional["String"] = None

    @property
    def tex_render(self) -> Optional["String"]:
        """Get texRender (Pythonic accessor)."""
        return self._texRender

    @tex_render.setter
    def tex_render(self, value: Optional["String"]) -> None:
        """
        Set texRender with validation.
        
        Args:
            value: The texRender to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._texRender = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"texRender must be String or str or None, got {type(value).__name__}"
            )
        self._texRender = value
        # This attribute specifies the type of the technical term.
        # such as "VARIABLE" "CALPRM".
        # It is no enum in order to support process specific.
        self._type: "NameToken" = None

    @property
    def type(self) -> "NameToken":
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: "NameToken") -> None:
        """
        Set type with validation.
        
        Args:
            value: The type to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"type must be NameToken or str, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTerm(self) -> "String":
        """
        AUTOSAR-compliant getter for term.
        
        Returns:
            The term value
        
        Note:
            Delegates to term property (CODING_RULE_V2_00017)
        """
        return self.term  # Delegates to property

    def setTerm(self, value: "String") -> "Tt":
        """
        AUTOSAR-compliant setter for term with method chaining.
        
        Args:
            value: The term to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to term property setter (gets validation automatically)
        """
        self.term = value  # Delegates to property setter
        return self

    def getTexRender(self) -> "String":
        """
        AUTOSAR-compliant getter for texRender.
        
        Returns:
            The texRender value
        
        Note:
            Delegates to tex_render property (CODING_RULE_V2_00017)
        """
        return self.tex_render  # Delegates to property

    def setTexRender(self, value: "String") -> "Tt":
        """
        AUTOSAR-compliant setter for texRender with method chaining.
        
        Args:
            value: The texRender to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tex_render property setter (gets validation automatically)
        """
        self.tex_render = value  # Delegates to property setter
        return self

    def getType(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for type.
        
        Returns:
            The type value
        
        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "NameToken") -> "Tt":
        """
        AUTOSAR-compliant setter for type with method chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_term(self, value: "String") -> "Tt":
        """
        Set term and return self for chaining.
        
        Args:
            value: The term to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_term("value")
        """
        self.term = value  # Use property setter (gets validation)
        return self

    def with_tex_render(self, value: Optional["String"]) -> "Tt":
        """
        Set texRender and return self for chaining.
        
        Args:
            value: The texRender to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tex_render("value")
        """
        self.tex_render = value  # Use property setter (gets validation)
        return self

    def with_type(self, value: "NameToken") -> "Tt":
        """
        Set type and return self for chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self



class Xdoc(SingleLanguageReferrable):
    """
    This meta-class represents the ability to refer to an external document
    which can be rendered as printed matter.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::Xdoc
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 319, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element specifies the release date of the external applicable.
        self._date: Optional["DateTime"] = None

    @property
    def date(self) -> Optional["DateTime"]:
        """Get date (Pythonic accessor)."""
        return self._date

    @date.setter
    def date(self, value: Optional["DateTime"]) -> None:
        """
        Set date with validation.
        
        Args:
            value: The date to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._date = None
            return

        if not isinstance(value, DateTime):
            raise TypeError(
                f"date must be DateTime or None, got {type(value).__name__}"
            )
        self._date = value
        # This represents document number of an external is referenced.
        # Kept as a string.
        self._number: Optional["String"] = None

    @property
    def number(self) -> Optional["String"]:
        """Get number (Pythonic accessor)."""
        return self._number

    @number.setter
    def number(self, value: Optional["String"]) -> None:
        """
        Set number with validation.
        
        Args:
            value: The number to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._number = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"number must be String or str or None, got {type(value).__name__}"
            )
        self._number = value
        # This represents the reference to the relevant positions of Kept as a string.
        self._position: Optional["String"] = None

    @property
    def position(self) -> Optional["String"]:
        """Get position (Pythonic accessor)."""
        return self._position

    @position.setter
    def position(self, value: Optional["String"]) -> None:
        """
        Set position with validation.
        
        Args:
            value: The position to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._position = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"position must be String or str or None, got {type(value).__name__}"
            )
        self._position = value
        # This represents the publisher of an external document being referenced.
        # Kept as a string.
        self._publisher: Optional["String"] = None

    @property
    def publisher(self) -> Optional["String"]:
        """Get publisher (Pythonic accessor)."""
        return self._publisher

    @publisher.setter
    def publisher(self, value: Optional["String"]) -> None:
        """
        Set publisher with validation.
        
        Args:
            value: The publisher to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._publisher = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"publisher must be String or str or None, got {type(value).__name__}"
            )
        self._publisher = value
        # This represents version and state of the external as a string.
        self._state: Optional["String"] = None

    @property
    def state(self) -> Optional["String"]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional["String"]) -> None:
        """
        Set state with validation.
        
        Args:
            value: The state to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"state must be String or str or None, got {type(value).__name__}"
            )
        self._state = value
        # This specifies the URL of the external document.
        self._url: Optional["Url"] = None

    @property
    def url(self) -> Optional["Url"]:
        """Get url (Pythonic accessor)."""
        return self._url

    @url.setter
    def url(self, value: Optional["Url"]) -> None:
        """
        Set url with validation.
        
        Args:
            value: The url to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._url = None
            return

        if not isinstance(value, Url):
            raise TypeError(
                f"url must be Url or None, got {type(value).__name__}"
            )
        self._url = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDate(self) -> "DateTime":
        """
        AUTOSAR-compliant getter for date.
        
        Returns:
            The date value
        
        Note:
            Delegates to date property (CODING_RULE_V2_00017)
        """
        return self.date  # Delegates to property

    def setDate(self, value: "DateTime") -> "Xdoc":
        """
        AUTOSAR-compliant setter for date with method chaining.
        
        Args:
            value: The date to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to date property setter (gets validation automatically)
        """
        self.date = value  # Delegates to property setter
        return self

    def getNumber(self) -> "String":
        """
        AUTOSAR-compliant getter for number.
        
        Returns:
            The number value
        
        Note:
            Delegates to number property (CODING_RULE_V2_00017)
        """
        return self.number  # Delegates to property

    def setNumber(self, value: "String") -> "Xdoc":
        """
        AUTOSAR-compliant setter for number with method chaining.
        
        Args:
            value: The number to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to number property setter (gets validation automatically)
        """
        self.number = value  # Delegates to property setter
        return self

    def getPosition(self) -> "String":
        """
        AUTOSAR-compliant getter for position.
        
        Returns:
            The position value
        
        Note:
            Delegates to position property (CODING_RULE_V2_00017)
        """
        return self.position  # Delegates to property

    def setPosition(self, value: "String") -> "Xdoc":
        """
        AUTOSAR-compliant setter for position with method chaining.
        
        Args:
            value: The position to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to position property setter (gets validation automatically)
        """
        self.position = value  # Delegates to property setter
        return self

    def getPublisher(self) -> "String":
        """
        AUTOSAR-compliant getter for publisher.
        
        Returns:
            The publisher value
        
        Note:
            Delegates to publisher property (CODING_RULE_V2_00017)
        """
        return self.publisher  # Delegates to property

    def setPublisher(self, value: "String") -> "Xdoc":
        """
        AUTOSAR-compliant setter for publisher with method chaining.
        
        Args:
            value: The publisher to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to publisher property setter (gets validation automatically)
        """
        self.publisher = value  # Delegates to property setter
        return self

    def getState(self) -> "String":
        """
        AUTOSAR-compliant getter for state.
        
        Returns:
            The state value
        
        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: "String") -> "Xdoc":
        """
        AUTOSAR-compliant setter for state with method chaining.
        
        Args:
            value: The state to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    def getUrl(self) -> "Url":
        """
        AUTOSAR-compliant getter for url.
        
        Returns:
            The url value
        
        Note:
            Delegates to url property (CODING_RULE_V2_00017)
        """
        return self.url  # Delegates to property

    def setUrl(self, value: "Url") -> "Xdoc":
        """
        AUTOSAR-compliant setter for url with method chaining.
        
        Args:
            value: The url to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to url property setter (gets validation automatically)
        """
        self.url = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_date(self, value: Optional["DateTime"]) -> "Xdoc":
        """
        Set date and return self for chaining.
        
        Args:
            value: The date to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_date("value")
        """
        self.date = value  # Use property setter (gets validation)
        return self

    def with_number(self, value: Optional["String"]) -> "Xdoc":
        """
        Set number and return self for chaining.
        
        Args:
            value: The number to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_number("value")
        """
        self.number = value  # Use property setter (gets validation)
        return self

    def with_position(self, value: Optional["String"]) -> "Xdoc":
        """
        Set position and return self for chaining.
        
        Args:
            value: The position to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_position("value")
        """
        self.position = value  # Use property setter (gets validation)
        return self

    def with_publisher(self, value: Optional["String"]) -> "Xdoc":
        """
        Set publisher and return self for chaining.
        
        Args:
            value: The publisher to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_publisher("value")
        """
        self.publisher = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional["String"]) -> "Xdoc":
        """
        Set state and return self for chaining.
        
        Args:
            value: The state to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self

    def with_url(self, value: Optional["Url"]) -> "Xdoc":
        """
        Set url and return self for chaining.
        
        Args:
            value: The url to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_url("value")
        """
        self.url = value  # Use property setter (gets validation)
        return self



class Xfile(SingleLanguageReferrable):
    """
    This represents to reference an external file within a documentation.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::Xfile
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 319, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element describes the tool which was used to corresponding Xfile.
        # Kept as a string since syntax can be provided to denote a tool.
        self._tool: Optional["String"] = None

    @property
    def tool(self) -> Optional["String"]:
        """Get tool (Pythonic accessor)."""
        return self._tool

    @tool.setter
    def tool(self, value: Optional["String"]) -> None:
        """
        Set tool with validation.
        
        Args:
            value: The tool to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tool = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"tool must be String or str or None, got {type(value).__name__}"
            )
        self._tool = value
        # This element describes the tool version which was used the corresponding
                # xfile.
        # Kept as a string, specific syntax can be specified.
        self._toolVersion: Optional["String"] = None

    @property
    def tool_version(self) -> Optional["String"]:
        """Get toolVersion (Pythonic accessor)."""
        return self._toolVersion

    @tool_version.setter
    def tool_version(self, value: Optional["String"]) -> None:
        """
        Set toolVersion with validation.
        
        Args:
            value: The toolVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._toolVersion = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"toolVersion must be String or str or None, got {type(value).__name__}"
            )
        self._toolVersion = value
        # This represents the URL of the external file.
        self._url: Optional["Url"] = None

    @property
    def url(self) -> Optional["Url"]:
        """Get url (Pythonic accessor)."""
        return self._url

    @url.setter
    def url(self, value: Optional["Url"]) -> None:
        """
        Set url with validation.
        
        Args:
            value: The url to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._url = None
            return

        if not isinstance(value, Url):
            raise TypeError(
                f"url must be Url or None, got {type(value).__name__}"
            )
        self._url = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTool(self) -> "String":
        """
        AUTOSAR-compliant getter for tool.
        
        Returns:
            The tool value
        
        Note:
            Delegates to tool property (CODING_RULE_V2_00017)
        """
        return self.tool  # Delegates to property

    def setTool(self, value: "String") -> "Xfile":
        """
        AUTOSAR-compliant setter for tool with method chaining.
        
        Args:
            value: The tool to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tool property setter (gets validation automatically)
        """
        self.tool = value  # Delegates to property setter
        return self

    def getToolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for toolVersion.
        
        Returns:
            The toolVersion value
        
        Note:
            Delegates to tool_version property (CODING_RULE_V2_00017)
        """
        return self.tool_version  # Delegates to property

    def setToolVersion(self, value: "String") -> "Xfile":
        """
        AUTOSAR-compliant setter for toolVersion with method chaining.
        
        Args:
            value: The toolVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tool_version property setter (gets validation automatically)
        """
        self.tool_version = value  # Delegates to property setter
        return self

    def getUrl(self) -> "Url":
        """
        AUTOSAR-compliant getter for url.
        
        Returns:
            The url value
        
        Note:
            Delegates to url property (CODING_RULE_V2_00017)
        """
        return self.url  # Delegates to property

    def setUrl(self, value: "Url") -> "Xfile":
        """
        AUTOSAR-compliant setter for url with method chaining.
        
        Args:
            value: The url to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to url property setter (gets validation automatically)
        """
        self.url = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tool(self, value: Optional["String"]) -> "Xfile":
        """
        Set tool and return self for chaining.
        
        Args:
            value: The tool to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tool("value")
        """
        self.tool = value  # Use property setter (gets validation)
        return self

    def with_tool_version(self, value: Optional["String"]) -> "Xfile":
        """
        Set toolVersion and return self for chaining.
        
        Args:
            value: The toolVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tool_version("value")
        """
        self.tool_version = value  # Use property setter (gets validation)
        return self

    def with_url(self, value: Optional["Url"]) -> "Xfile":
        """
        Set url and return self for chaining.
        
        Args:
            value: The url to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_url("value")
        """
        self.url = value  # Use property setter (gets validation)
        return self



class Xref(ARObject):
    """
    This represents a cross-reference within documentation.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::Xref
    
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
        self._referrable: Optional["RefType"] = None

    @property
    def referrable(self) -> Optional["RefType"]:
        """Get referrable (Pythonic accessor)."""
        return self._referrable

    @referrable.setter
    def referrable(self, value: Optional["RefType"]) -> None:
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
        # Indicates if the content of the xref element follow a policy.
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
        # Indicates if the content of the xref element shall be default is
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
        # Indicates if the type of the referenced Resource shall be shown.
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
        # Indicates if the word "see " shall be shown before the is "NO-SHOW-SEE".
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

    def getReferrable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for referrable.
        
        Returns:
            The referrable value
        
        Note:
            Delegates to referrable property (CODING_RULE_V2_00017)
        """
        return self.referrable  # Delegates to property

    def setReferrable(self, value: "RefType") -> "Xref":
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



class XrefTarget(SingleLanguageReferrable):
    """
    This element specifies a reference target which can be scattered throughout
    the text.
    
    Package: M2::MSR::Documentation::TextModel::InlineTextElements::XrefTarget
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 321, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class Superscript(ARLiteral):
    """
    Superscript primitive type

This is text which is rendered superscript or subscript depending on the role. Tags: xml.xsd.customType=SUPSCRIPT xml.xsd.type=string Table 9.38: Superscript

Package: M2::MSR::Documentation::TextModel::InlineTextElements
    """
    pass


