from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class RunnableEntityArgument(ARObject):
    # RunnableEntityArgument method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSymbol                    [x] impl  [ ] docstring  [ ] test
    # [ ] setSymbol                    [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.symbol = None  # type: ARLiteral

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self
