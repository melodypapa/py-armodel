
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    Paginateable,
)


class ListEnum(AREnum):

    NUMBER = 'number'
    UNNUMBER = 'unnumber'

    def __init__(self,) -> None:
        super().__init__((
            ListEnum.NUMBER,
            ListEnum.UNNUMBER
        ))


class Item(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.itemContents = None

    def getItemContents(self):
        return self.itemContents

    def setItemContents(self, value):
        self.itemContents = value
        return self


class ARList(Paginateable):
    '''
        This meta-class represents the ability to express a list. The kind of list is specified in the attribute.
        In AUTOSAR standard class name shall be List, but it is conflict with Python List and renamed to ARList
    '''
    def __init__(self) -> None:
        super().__init__()

        self.items = []                         # type: List[Item]
        self.type: Union[ListEnum, None] = None

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


class DefItem(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.term: Union[String, None] = None
        self.definition: Union[String, None] = None

    def getTerm(self) -> Union[String, None]:
        return self.term

    def setTerm(self, value: String) -> "DefItem":
        self.term = value
        return self

    def getDefinition(self) -> Union[String, None]:
        return self.definition

    def setDefinition(self, value: String) -> "DefItem":
        self.definition = value
        return self


class DefList(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.defItems: List[DefItem] = []

    def getDefItems(self) -> List[DefItem]:
        return self.defItems

    def addDefItem(self, value: DefItem):
        self.defItems.append(value)
        return self


class LabeledItem(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.label: Union[String, None] = None
        self.content: Union[String, None] = None

    def getLabel(self) -> Union[String, None]:
        return self.label

    def setLabel(self, value: String) -> "LabeledItem":
        self.label = value
        return self

    def getContent(self) -> Union[String, None]:
        return self.content

    def setContent(self, value: String) -> "LabeledItem":
        self.content = value
        return self


class LabeledList(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.indentSample: Union[String, None] = None
        self.labeledItems: List[LabeledItem] = []

    def getIndentSample(self) -> Union[String, None]:
        return self.indentSample

    def setIndentSample(self, value: String) -> "LabeledList":
        self.indentSample = value
        return self

    def getLabeledItems(self) -> List[LabeledItem]:
        return self.labeledItems

    def addLabeledItem(self, value: LabeledItem):
        self.labeledItems.append(value)
        return self


__all__ = [
    'ListEnum',
    'Item',
    'ARList',
    'DefItem',
    'DefList',
    'LabeledItem',
    'LabeledList',
]
