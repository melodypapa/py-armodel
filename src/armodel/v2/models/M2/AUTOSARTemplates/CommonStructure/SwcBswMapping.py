"""
This module contains classes for representing AUTOSAR SWC-BSW mapping structures
in the CommonStructure module. SWC-BSW mapping defines relationships between
software component entities and basic software module entities for integration purposes.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwcBswRunnableMapping(ARObject):
    """
    Represents a mapping between BSW module entities and SWC runnable entities in AUTOSAR models.
    Maps a BswModuleEntity to a RunnableEntity if it is implemented as part of a BSW
    module (in the case of an AUTOSAR Service, a Complex Driver or an ECU
    Abstraction). The mapping can be used by a tool to find relevant information on the
    behavior, e.g. whether the bswEntity shall be running in interrupt context.
    """


    def __init__(self) -> None:
        """
        Initializes the SwcBswRunnableMapping with default values.
        """
        super().__init__()

        # Reference to the BSW module entity in this mapping
        self.bswEntityRef: Union[Union[RefType, None] , None] = None
        # Reference to the SWC runnable entity in this mapping
        self.swcRunnableRef: Union[Union[RefType, None] , None] = None

    def getBswEntityRef(self):
        """
        Gets the reference to the BSW module entity in this mapping.

        Returns:
            RefType: The BSW entity reference
        """
        return self.bswEntityRef

    def setBswEntityRef(self, value):
        """
        Sets the reference to the BSW module entity in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The BSW entity reference to set

        Returns:
            self for method chaining
        """
        self.bswEntityRef = value
        return self

    def getSwcRunnableRef(self):
        """
        Gets the reference to the SWC runnable entity in this mapping.

        Returns:
            RefType: The SWC runnable reference
        """
        return self.swcRunnableRef

    def setSwcRunnableRef(self, value):
        """
        Sets the reference to the SWC runnable entity in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The SWC runnable reference to set

        Returns:
            self for method chaining
        """
        self.swcRunnableRef = value
        return self

class SwcBswMapping(AtpStructureElement):
    """
    Represents SWC-BSW mapping in AUTOSAR models.
    This class defines mappings between software component (SWC) behavior and basic software (BSW) behavior.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the SwcBswMapping with a parent and short name.

        Args:
            parent: The parent ARObject that contains this SWC-BSW mapping
            short_name: The unique short name of this SWC-BSW mapping
        """
        super().__init__(parent, short_name)

        # Reference to the BSW behavior in this mapping
        self.bswBehaviorRef: Union[Union[RefType, None] , None] = None
        # List of runnable mappings in this SWC-BSW mapping
        self.runnableMappings: List[SwcBswRunnableMapping] = []
        # Reference to the SWC behavior in this mapping
        self.swcBehaviorRef: Union[Union[RefType, None] , None] = None
        # List of synchronized mode groups in this mapping
        self.synchronizedModeGroups = []
        # List of synchronized triggers in this mapping
        self.synchronizedTriggers = []

    def getBswBehaviorRef(self):
        """
        Gets the reference to the BSW behavior in this mapping.

        Returns:
            RefType: The BSW behavior reference
        """
        return self.bswBehaviorRef

    def setBswBehaviorRef(self, value):
        """
        Sets the reference to the BSW behavior in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The BSW behavior reference to set

        Returns:
            self for method chaining
        """
        self.bswBehaviorRef = value
        return self

    def getRunnableMappings(self):
        """
        Gets the list of runnable mappings in this SWC-BSW mapping.

        Returns:
            List of SwcBswRunnableMapping instances
        """
        return self.runnableMappings

    def addRunnableMapping(self, value):
        """
        Adds a runnable mapping to this SWC-BSW mapping.

        Args:
            value: The runnable mapping to add

        Returns:
            self for method chaining
        """
        self.runnableMappings.append(value)
        return self

    def getSwcBehaviorRef(self):
        """
        Gets the reference to the SWC behavior in this mapping.

        Returns:
            RefType: The SWC behavior reference
        """
        return self.swcBehaviorRef

    def setSwcBehaviorRef(self, value):
        """
        Sets the reference to the SWC behavior in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The SWC behavior reference to set

        Returns:
            self for method chaining
        """
        self.swcBehaviorRef = value
        return self

    def getSynchronizedModeGroups(self):
        """
        Gets the list of synchronized mode groups in this mapping.

        Returns:
            List of synchronized mode group objects
        """
        return self.synchronizedModeGroups

    def setSynchronizedModeGroups(self, value):
        """
        Sets the list of synchronized mode groups in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The synchronized mode groups list to set

        Returns:
            self for method chaining
        """
        self.synchronizedModeGroups = value
        return self

    def getSynchronizedTriggers(self):
        """
        Gets the list of synchronized triggers in this mapping.

        Returns:
            List of synchronized trigger objects
        """
        return self.synchronizedTriggers

    def setSynchronizedTriggers(self, value):
        """
        Sets the list of synchronized triggers in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The synchronized triggers list to set

        Returns:
            self for method chaining
        """
        self.synchronizedTriggers = value
        return self


class SwcBswSynchronizedModeGroupPrototype(ARObject):
    """
    Represents a SWC-BSW synchronized mode group prototype in AUTOSAR.
    Defines a synchronized mode group prototype for SWC-BSW mapping.
    """


    def __init__(self) -> None:
        """
        Initializes the SwcBswSynchronizedModeGroupPrototype with default values.
        """
        super().__init__()
        self.modeGroupRef: Union[Union[RefType, None] , None] = None

    def getModeGroupRef(self) -> Union[RefType, None]:
        """
        Gets the mode group reference.

        Returns:
            Reference to the mode group
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value: RefType) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        Sets the mode group reference.

        Args:
            value: The mode group reference to set

        Returns:
            self for method chaining
        """
        self.modeGroupRef = value
        return self


class SwcBswSynchronizedTrigger(ARObject):
    """
    Represents a SWC-BSW synchronized trigger in AUTOSAR.
    Defines a synchronized trigger for SWC-BSW mapping.
    """


    def __init__(self) -> None:
        """
        Initializes the SwcBswSynchronizedTrigger with default values.
        """
        super().__init__()
        self.triggerRef: Union[Union[RefType, None] , None] = None

    def getTriggerRef(self) -> Union[RefType, None]:
        """
        Gets the trigger reference.

        Returns:
            Reference to the trigger
        """
        return self.triggerRef

    def setTriggerRef(self, value: RefType) -> "SwcBswSynchronizedTrigger":
        """
        Sets the trigger reference.

        Args:
            value: The trigger reference to set

        Returns:
            self for method chaining
        """
        self.triggerRef = value
        return self
