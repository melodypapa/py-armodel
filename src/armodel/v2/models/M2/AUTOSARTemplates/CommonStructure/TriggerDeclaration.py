"""
This module contains classes for representing AUTOSAR trigger declaration structures
in the CommonStructure module. Triggers define events that can initiate specific
behaviors or actions in AUTOSAR components and systems.
"""

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class Trigger(AtpStructureElement):
    """
    Represents a trigger in AUTOSAR models.
    Triggers define events that can initiate specific behaviors or actions in AUTOSAR components and systems.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the Trigger with a parent and short name.

        Args:
            parent: The parent ARObject that contains this trigger
            short_name: The unique short name of this trigger
        """
        super().__init__(parent, short_name)

        # Software implementation policy for this trigger
        self.swImplPolicy: SwImplPolicyEnum = None
        # Period for this trigger (MultidimensionalTime type)
        self.triggerPeriod = None

    def getSwImplPolicy(self):
        """
        Gets the software implementation policy for this trigger.

        Returns:
            SwImplPolicyEnum: The software implementation policy
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value):
        """
        Sets the software implementation policy for this trigger.
        Only sets the value if it is not None.

        Args:
            value: The software implementation policy to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swImplPolicy = value
        return self

    def getTriggerPeriod(self):
        """
        Gets the period for this trigger.

        Returns:
            MultidimensionalTime: The trigger period
        """
        return self.triggerPeriod

    def setTriggerPeriod(self, value):
        """
        Sets the period for this trigger.
        Only sets the value if it is not None.

        Args:
            value: The trigger period to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerPeriod = value
        return self


class TriggerMapping(ARObject):
    """
    Represents a mapping between triggers in AUTOSAR models.
    This class defines relationships between different triggers across system boundaries or components.
    """

    def __init__(self):
        """
        Initializes the TriggerMapping with default values.
        """
        super().__init__()

        # Reference to the first trigger in the mapping
        self.firstTriggerRef: RefType = None
        # Reference to the second trigger in the mapping
        self.secondTriggerRef: RefType = None

    def getFirstTriggerRef(self):
        """
        Gets the reference to the first trigger in the mapping.

        Returns:
            RefType: The first trigger reference
        """
        return self.firstTriggerRef

    def setFirstTriggerRef(self, value):
        """
        Sets the reference to the first trigger in the mapping.
        Only sets the value if it is not None.

        Args:
            value: The first trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.firstTriggerRef = value
        return self

    def getSecondTriggerRef(self):
        """
        Gets the reference to the second trigger in the mapping.

        Returns:
            RefType: The second trigger reference
        """
        return self.secondTriggerRef

    def setSecondTriggerRef(self, value):
        """
        Sets the reference to the second trigger in the mapping.
        Only sets the value if it is not None.

        Args:
            value: The second trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.secondTriggerRef = value
        return self
