from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class SwServiceArg(Identifiable):
    """
    Service argument with direction, array size, and data definition
    properties.
    """
    # SwServiceArg method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDirection                 [x] impl  [ ] docstring  [ ] test
    # [ ] setDirection                 [x] impl  [ ] docstring  [ ] test
    # [ ] getSwArraysize               [x] impl  [ ] docstring  [ ] test
    # [ ] setSwArraysize               [x] impl  [ ] docstring  [ ] test
    # [ ] getSwDataDefProps            [x] impl  [ ] docstring  [ ] test
    # [ ] setSwDataDefProps            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.direction = None                   # type: ArgumentDirectionEnum
        self.swArraysize = None                 # type: ValueList
        self.swDataDefProps = None              # type: SwDataDefProps

    def getDirection(self):
        return self.direction

    def setDirection(self, value):
        self.direction = value
        return self

    def getSwArraysize(self):
        return self.swArraysize

    def setSwArraysize(self, value):
        self.swArraysize = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self
