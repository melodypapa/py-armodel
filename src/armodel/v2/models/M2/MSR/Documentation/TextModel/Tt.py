from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


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
        if not isinstance(value, String):
            raise TypeError(
                f"term must be String, got {type(value).__name__}"
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

        if not isinstance(value, String):
            raise TypeError(
                f"texRender must be String or None, got {type(value).__name__}"
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
        if not isinstance(value, NameToken):
            raise TypeError(
                f"type must be NameToken, got {type(value).__name__}"
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
