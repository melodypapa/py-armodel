from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, String
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class ListEnum(AREnum):
    """
    Enumeration for list numbering types: number or unnumber.
    """

    # ListEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    NUMBER = "number"
    UNNUMBER = "unnumber"

    def __init__(
        self,
    ):
        super().__init__((ListEnum.NUMBER, ListEnum.UNNUMBER))


class Item(Paginateable, VariationPointCapable):
    """
    An item within a list with content defined by itemContents.
    """

    # Item method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getItemContents              [x] impl  [ ] docstring  [ ] test
    # [ ] setItemContents              [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.itemContents = None

    def getItemContents(self):
        return self.itemContents

    def setItemContents(self, value):
        self.itemContents = value
        return self


class ARList(Paginateable):
    """
    This meta-class represents the ability to express a list. The kind of list is specified in the attribute.
    In AUTOSAR standard class name shall be List, but it is conflict with Python List and renamed to ARList
    """

    # ARList method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getItems                     [x] impl  [ ] docstring  [ ] test
    # [ ] addItem                      [x] impl  [ ] docstring  [ ] test
    # [ ] getType                      [x] impl  [ ] docstring  [ ] test
    # [ ] setType                      [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.items = []  # type: List[Item]
        self.type = None  # type: ListEnum

    def getItems(self):
        return self.items

    def addItem(self, value: Item):
        self.items.append(value)
        return self

    def getType(self):
        return self.type

    def setType(self, value):
        self.type = value
        return self


class ItemLabelPosEnum(AREnum):
    """
    This enumerator specifies, how the label of a labeled list shall be rendered.
    """

    # ItemLabelPosEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.14, p.297
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on IndentSample.itemLabelPos
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The label is renders in a new line. Tags: atp.EnumerationLiteralIndex=0
    NEWLINE = "newline"
    # The label is rendered in a new line if it is longer than the indentation. Tags: atp.EnumerationLiteralIndex=1
    NEWLINE_IF_NECESSARY = "newlineIfNecessary"
    # The label is rendered in one line with the item even if it is longer than the indentation. Tags: atp.EnumerationLiteralIndex=2
    NO_NEWLINE = "noNewline"

    def __init__(self):
        super().__init__(
            (
                ItemLabelPosEnum.NEWLINE,
                ItemLabelPosEnum.NEWLINE_IF_NECESSARY,
                ItemLabelPosEnum.NO_NEWLINE,
            )
        )


class IndentSample(ARObject):
    """
    This represents the ability to specify indentation of a labeled list by providing a sample content. This content can be measured by the rendering system in order to determine the width of indentation.
    """

    # IndentSample method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.13, p.297
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getItemLabelPos  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setItemLabelPos  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addL2            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getL2s           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # The position of the label in case the label is too long. The default is "NO-NEWLINE"
        self.itemLabelPos: Optional[ItemLabelPosEnum] = None

        # This represents the indent sample in one particular language.
        self.l2s: List[LOverviewParagraph] = []

    def getItemLabelPos(self) -> Optional[ItemLabelPosEnum]:
        """
        The position of the label in case the label is too long. The default is "NO-NEWLINE"

        Returns:
            The position of the label
        """
        return self.itemLabelPos

    def setItemLabelPos(self, value: Optional[ItemLabelPosEnum]) -> "IndentSample":
        """
        The position of the label in case the label is too long. The default is "NO-NEWLINE". A None value is a no-op and does not overwrite an existing itemLabelPos.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.itemLabelPos = value
        return self

    def addL2(self, value: Optional[LOverviewParagraph]) -> "IndentSample":
        """
        This represents the indent sample in one particular language. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.l2s.append(value)
        return self

    def getL2s(self) -> List[LOverviewParagraph]:
        """
        This represents the indent sample in one particular language.

        Returns:
            The indent samples in particular languages
        """
        return self.l2s


class LabeledItem(ARObject, VariationPointCapable):
    """
    this represents an item of a labeled list.
    """

    # LabeledItem method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.12, p.296
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHelpEntry        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHelpEntry        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getItemContents     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setItemContents     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getItemLabel        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setItemLabel        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.
        self.helpEntry: Optional[String] = None

        # This represents the actual content of the item. It is composed of a DocumentationBlock. This way it is possible to use simple paragraphs to nested lists, formula, figures or notes.
        self.itemContents: Optional["DocumentationBlock"] = None

        # This is the label of the item.
        self.itemLabel: Optional[MultiLanguageOverviewParagraph] = None

    def getHelpEntry(self) -> Optional[String]:
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.

        Returns:
            The entry point in an online help system
        """
        return self.helpEntry

    def setHelpEntry(self, value: Optional[String]) -> "LabeledItem":
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. A None value is a no-op and does not overwrite an existing helpEntry.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.helpEntry = value
        return self

    def getItemContents(self) -> Optional["DocumentationBlock"]:
        """
        This represents the actual content of the item. It is composed of a DocumentationBlock. This way it is possible to use simple paragraphs to nested lists, formula, figures or notes.

        Returns:
            The actual content of the item
        """
        return self.itemContents

    def setItemContents(self, value: Optional["DocumentationBlock"]) -> "LabeledItem":
        """
        This represents the actual content of the item. It is composed of a DocumentationBlock. This way it is possible to use simple paragraphs to nested lists, formula, figures or notes. A None value is a no-op and does not overwrite an existing itemContents.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.itemContents = value
        return self

    def getItemLabel(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This is the label of the item.

        Returns:
            The label of the item
        """
        return self.itemLabel

    def setItemLabel(self, value: Optional[MultiLanguageOverviewParagraph]) -> "LabeledItem":
        """
        This is the label of the item. A None value is a no-op and does not overwrite an existing itemLabel.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.itemLabel = value
        return self


class LabeledList(ARObject, VariationPointCapable):
    """
    This meta-class represents a labeled list, in which items have a label and a content. The policy how to render such items is specified in the labeled list.
    """

    # LabeledList method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.11, p.296
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIndentSample     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIndentSample     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addLabeledItem      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLabeledItems     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This is a sample item. This sample is used by a rendering system to measure out the width of indentation. Since this depends on the particular fontsize etc. the indentation cannot be specified e.g. in mm.
        self.indentSample: Optional[IndentSample] = None

        # This represents one particular item in the labeled list.
        self.labeledItems: List[LabeledItem] = []

    def getIndentSample(self) -> Optional[IndentSample]:
        """
        This is a sample item. This sample is used by a rendering system to measure out the width of indentation. Since this depends on the particular fontsize etc. the indentation cannot be specified e.g. in mm.

        Returns:
            The sample item
        """
        return self.indentSample

    def setIndentSample(self, value: Optional[IndentSample]) -> "LabeledList":
        """
        This is a sample item. This sample is used by a rendering system to measure out the width of indentation. Since this depends on the particular fontsize etc. the indentation cannot be specified e.g. in mm. A None value is a no-op and does not overwrite an existing indentSample.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.indentSample = value
        return self

    def addLabeledItem(self, value: Optional[LabeledItem]) -> "LabeledList":
        """
        This represents one particular item in the labeled list. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.labeledItems.append(value)
        return self

    def getLabeledItems(self) -> List[LabeledItem]:
        """
        This represents one particular item in the labeled list.

        Returns:
            The items in the labeled list
        """
        return self.labeledItems


class DefItem(ARObject, VariationPointCapable):
    """
    This represents an entry in a definition list. The defined item is specified using shortName and longName.
    """

    # DefItem method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.16, p.298
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHelpEntry    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHelpEntry    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the definition part of the DefItem.
        self.def_doc: Optional["DocumentationBlock"] = None

        # This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.
        self.helpEntry: Optional[String] = None

    def getDef(self) -> Optional["DocumentationBlock"]:
        """
        This represents the definition part of the DefItem.
        """
        return self.def_doc

    def setDef(self, value: Optional["DocumentationBlock"]) -> "DefItem":
        """
        This represents the definition part of the DefItem. A None value is a no-op and does not overwrite an existing def.
        """
        if value is not None:
            self.def_doc = value
        return self

    def getHelpEntry(self) -> Optional[String]:
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.
        """
        return self.helpEntry

    def setHelpEntry(self, value: Optional[String]) -> "DefItem":
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. A None value is a no-op and does not overwrite an existing helpEntry.
        """
        if value is not None:
            self.helpEntry = value
        return self


class DefList(ARObject, VariationPointCapable):
    """
    This meta-class represents the ability to express a list of definitions. Note that a definition list might rendered similar to a labeled list but has a particular semantics to denote definitions.
    """

    # DefList method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.15, p.298
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addDefItem     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefItems    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This is one entry in the definition list.
        self.defItems: List[DefItem] = []

    def addDefItem(self, value: Optional[DefItem]) -> "DefList":
        """
        This is one entry in the definition list. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defItems.append(value)
        return self

    def getDefItems(self) -> List[DefItem]:
        """
        This is one entry in the definition list.

        Returns:
            The entries in the definition list
        """
        return self.defItems
