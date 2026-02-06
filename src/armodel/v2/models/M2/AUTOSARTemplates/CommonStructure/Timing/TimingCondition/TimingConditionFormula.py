from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TimingConditionFormula(ARObject):
    """
    Represents a timing condition formula in AUTOSAR.
    Defines a formula for evaluating timing conditions.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the TimingConditionFormula with default values.
        """
        super().__init__()
        self.expression: Union[str, None] = None

    def getExpression(self) -> str:
        """
        Gets the formula expression.

        Returns:
            String representing the expression
        """
        return self.expression

    def setExpression(self, value: str):
        """
        Sets the formula expression.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.expression = value
        return self
