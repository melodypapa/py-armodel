from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String


class MlFormula(ARObject):
    """
    Represents a MathML formula in the AUTOSAR model.

    This class is used to define mathematical formulas using MathML notation
    for documentation purposes.

    Attributes:
        formula (String): The MathML formula expression.
    """
    # MlFormula method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFormula                   [x] impl  [ ] docstring  [ ] test
    # [ ] setFormula                   [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.formula: String = None

    def getFormula(self) -> String:
        return self.formula

    def setFormula(self, value: String):
        if value is not None:
            self.formula = value
        return self
