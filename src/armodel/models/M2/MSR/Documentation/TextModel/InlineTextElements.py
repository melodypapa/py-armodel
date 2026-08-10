from __future__ import annotations

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, NameToken, String


class Superscript(ARLiteral):
    """
    This is text which is rendered superscript or subscript depending on the role.
    """

    # Superscript method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.38, p.318
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class Tt(ARObject):
    """
    This meta-class represents the ability to express specific technical terms. The kind of term is denoted in the attribute "type".
    """

    # Tt method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.39, p.319
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTexRender [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTexRender [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getType      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setType      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is the term itself.
        self.value: String = None

        # This attribute holds information how the content (represented by attribute "term") of the particular technical term is rendered using LaTeX. This allows to inject specific LaTeX commands such as \sep{}. An example is to render "MyClass" as "My\sep{}Class". Default is the value of the attribute "term".
        self.texRender: Optional[String] = None

        # This attribute specifies the type of the technical term. Values are such as "VARIABLE" "CALPRM". It is no longer an enum in order to support process specific extensions.
        self.type: Optional[NameToken] = None

    def getValue(self) -> String:
        """
        This is the term itself.

        Returns:
            The term itself
        """
        return self.value

    def setValue(self, value: String) -> "Tt":
        """
        This is the term itself. A None value is a no-op and does not overwrite an existing value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self

    def getTexRender(self) -> Optional[String]:
        r"""
        This attribute holds information how the content (represented by attribute "term") of the particular technical term is rendered using LaTeX. This allows to inject specific LaTeX commands such as \sep{}. An example is to render "MyClass" as "My\sep{}Class". Default is the value of the attribute "term".

        Returns:
            The LaTeX rendering information
        """
        return self.texRender

    def setTexRender(self, value: Optional[String]) -> "Tt":
        r"""
        This attribute holds information how the content (represented by attribute "term") of the particular technical term is rendered using LaTeX. This allows to inject specific LaTeX commands such as \sep{}. An example is to render "MyClass" as "My\sep{}Class". Default is the value of the attribute "term". A None value is a no-op and does not overwrite an existing texRender.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.texRender = value
        return self

    def getType(self) -> Optional[NameToken]:
        """
        This attribute specifies the type of the technical term. Values are such as "VARIABLE" "CALPRM". It is no longer an enum in order to support process specific extensions.

        Returns:
            The type of the technical term
        """
        return self.type

    def setType(self, value: Optional[NameToken]) -> "Tt":
        """
        This attribute specifies the type of the technical term. Values are such as "VARIABLE" "CALPRM". It is no longer an enum in order to support process specific extensions. A None value is a no-op and does not overwrite an existing type.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.type = value
        return self


class IndexEntry(ARObject):
    """
    This class represents an index entry.
    """

    # IndexEntry method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.36, p.317
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The text content of the index entry.
        self.value: String = None

        # This is subscript text.
        self.sub: Optional[Superscript] = None

        # This is superscript text.
        self.sup: Optional[Superscript] = None

    def getValue(self) -> String:
        """
        Gets the text content of the index entry.

        Returns:
            The text content of the index entry
        """
        return self.value

    def setValue(self, value: String) -> "IndexEntry":
        """
        Sets the text content of the index entry. A None value is a no-op and does not overwrite an existing value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        This is subscript text.

        Returns:
            The subscript text
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> "IndexEntry":
        """
        This is subscript text. A None value is a no-op and does not overwrite an existing sub.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text.

        Returns:
            The superscript text
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> "IndexEntry":
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sup.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sup = value
        return self


class EmphasisText(ARObject):
    """
    This is an emphasized text. As a compromise it contains some rendering oriented attributes such as color and font.
    """

    # EmphasisText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.34, p.317
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getColor     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setColor     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFont      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFont      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTt        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTt        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getType      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setType      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The text content of the emphasized text.
        self.value: String = None

        # This allows to recommend a color of the emphasis. It is specified bases on 6 digits RGB hex-code.
        self.color: Optional[String] = None

        # This specifies the font style in which the emphasized text shall be rendered.
        self.font: Optional[ARLiteral] = None

        # this is subscript text
        self.sub: Optional[Superscript] = None

        # This is superscript text
        self.sup: Optional[Superscript] = None

        # This is a technical term.
        self.tt: Optional[Tt] = None

        # Indicates how the text may be emphasized. Note that this is only a proposal which can be overridden or ignored by particular formatting engines. Default is BOLD.
        self.type: Optional[ARLiteral] = None

    def getValue(self) -> String:
        """
        Gets the text content of the emphasized text.

        Returns:
            The text content of the emphasized text
        """
        return self.value

    def setValue(self, value: String) -> "EmphasisText":
        """
        Sets the text content of the emphasized text. A None value is a no-op and does not overwrite an existing value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self

    def getColor(self) -> Optional[String]:
        """
        This allows to recommend a color of the emphasis. It is specified bases on 6 digits RGB hex-code.

        Returns:
            The recommended color of the emphasis
        """
        return self.color

    def setColor(self, value: Optional[String]) -> "EmphasisText":
        """
        This allows to recommend a color of the emphasis. It is specified bases on 6 digits RGB hex-code. A None value is a no-op and does not overwrite an existing color.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.color = value
        return self

    def getFont(self) -> Optional[ARLiteral]:
        """
        This specifies the font style in which the emphasized text shall be rendered.

        Returns:
            The font style in which the emphasized text shall be rendered
        """
        return self.font

    def setFont(self, value: Optional[ARLiteral]) -> "EmphasisText":
        """
        This specifies the font style in which the emphasized text shall be rendered. A None value is a no-op and does not overwrite an existing font.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.font = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        this is subscript text

        Returns:
            The subscript text
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> "EmphasisText":
        """
        this is subscript text. A None value is a no-op and does not overwrite an existing sub.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text

        Returns:
            The superscript text
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> "EmphasisText":
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sup.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sup = value
        return self

    def getTt(self) -> Optional[Tt]:
        """
        This is a technical term.

        Returns:
            The technical term
        """
        return self.tt

    def setTt(self, value: Optional[Tt]) -> "EmphasisText":
        """
        This is a technical term. A None value is a no-op and does not overwrite an existing tt.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.tt = value
        return self

    def getType(self) -> Optional[ARLiteral]:
        """
        Indicates how the text may be emphasized. Note that this is only a proposal which can be overridden or ignored by particular formatting engines. Default is BOLD.

        Returns:
            How the text may be emphasized
        """
        return self.type

    def setType(self, value: Optional[ARLiteral]) -> "EmphasisText":
        """
        Indicates how the text may be emphasized. Note that this is only a proposal which can be overridden or ignored by particular formatting engines. Default is BOLD. A None value is a no-op and does not overwrite an existing type.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.type = value
        return self
