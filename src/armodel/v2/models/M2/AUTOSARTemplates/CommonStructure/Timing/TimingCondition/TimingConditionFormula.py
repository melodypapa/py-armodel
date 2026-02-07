from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TimingConditionFormula(ARObject):
    """
    Represents a timing condition formula in AUTOSAR.
    Defines a formula for evaluating timing conditions.
    """


    def __init__(self) -> None:
        """
        Initializes the TimingConditionFormula with default values.
        """
        super().__init__()
        self.expression: Union[str, None] = None

    def getExpression(self) -> Union[str, None]:
        """
        Gets the formula expression.

        Returns:
            String representing the expression
        """
        return self.expression

    def setExpression(self, value: str) -> "TimingConditionFormula":
        """
        Sets the formula expression.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.expression = value
        return self
