
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.models_v2.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    Paginateable,
)


class ListEnum(AREnum):

    NUMBER = 'number'
    UNNUMBER = 'unnumber'

    def __init__(self,):
        super().__init__((
            ListEnum.NUMBER,
            ListEnum.UNNUMBER
        ))


class Item(Paginateable):
    def __init__(self):
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
    def __init__(self):
        super().__init__()

        self.items = []                         # type: List[Item]
        self.type = None                        # type: ListEnum

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
