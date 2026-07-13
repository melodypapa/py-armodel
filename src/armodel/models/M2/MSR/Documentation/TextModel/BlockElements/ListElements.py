
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class ListEnum(AREnum):
    """
    Enumeration for list numbering types: number or unnumber.
    """
    # ListEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    NUMBER = 'number'
    UNNUMBER = 'unnumber'

    def __init__(self,):
        super().__init__((
            ListEnum.NUMBER,
            ListEnum.UNNUMBER
        ))


class Item(Paginateable):
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
    '''
        This meta-class represents the ability to express a list. The kind of list is specified in the attribute.
        In AUTOSAR standard class name shall be List, but it is conflict with Python List and renamed to ARList
    '''
    # ARList method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getItems                     [x] impl  [ ] docstring  [ ] test
    # [ ] addItem                      [x] impl  [ ] docstring  [ ] test
    # [ ] getType                      [x] impl  [ ] docstring  [ ] test
    # [ ] setType                      [x] impl  [ ] docstring  [ ] test

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
