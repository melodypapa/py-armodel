from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TimingCondition(ARObject):
    """
    Represents a timing condition in AUTOSAR timing specifications.
    Defines conditions that affect timing behavior.
    """

    def __init__(self):
        """
        Initializes the TimingCondition with default values.
        """
        super().__init__()
        self.conditionFormula: str = None
        self.modeInstances: List[str] = []

    def getConditionFormula(self) -> str:
        """
        Gets the condition formula.

        Returns:
            String representing the condition formula
        """
        return self.conditionFormula

    def setConditionFormula(self, value: str):
        """
        Sets the condition formula.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.conditionFormula = value
        return self

    def addModeInstance(self, instance: str):
        """
        Adds a mode instance to this timing condition.

        Args:
            instance: The mode instance to add

        Returns:
            self for method chaining
        """
        self.modeInstances.append(instance)
        return self

    def getModeInstances(self) -> List[str]:
        """
        Gets the list of mode instances.

        Returns:
            List of mode instances
        """
        return self.modeInstances
