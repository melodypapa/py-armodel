"""
This module defines classes for execution order constraint entities in AUTOSAR timing specifications.

The execution order constraint mechanism allows defining the execution sequence of runnables
within AUTOSAR software components. It defines abstract and concrete classes for representing
executable entity references and their ordering constraints.

Classes:
    EOCExecutableEntityRefAbstract: Abstract base class for executable entity references
    EOCExecutableEntityRef: Concrete implementation of executable entity reference
    ExecutionOrderConstraint: Constraint defining the execution order of entities
"""

from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """
    Abstract base class for execution order constraint executable entity references.
    This class cannot be instantiated directly and serves as the base for concrete implementations.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is EOCExecutableEntityRefAbstract:
            raise TypeError("EOCExecutableEntityRefAbstract is an abstract class.")

        super().__init__(parent, short_name)


class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """
    Concrete implementation of executable entity reference for execution order constraints.
    Represents a specific runnable or executable entity in an execution order constraint.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.successor_refs: List[RefType] = []

    def addSuccessorRef(self, ref: RefType):
        """
        Adds a reference to a successor executable entity.

        Args:
            ref: Reference to the successor entity
        """
        self.successor_refs.append(ref)

    def getSuccessorRefs(self) -> List[RefType]:
        """
        Returns the list of successor references for this entity.

        Returns:
            List of successor entity references
        """
        return self.successor_refs


class ExecutionOrderConstraint(TimingConstraint):
    """
    Execution order constraint defining the execution sequence of executable entities.
    This constraint specifies the order in which runnables or other executable entities
    should be executed within a software component.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.ordered_elements: List[EOCExecutableEntityRefAbstract] = []

    def createEOCExecutableEntityRef(self, short_name: str)-> EOCExecutableEntityRef:
        """
        Creates a new executable entity reference with the specified short name.

        Args:
            short_name: Short name for the new entity reference

        Returns:
            The created EOCExecutableEntityRef instance
        """
        if not self.IsElementExists(short_name):
            entity_ref = EOCExecutableEntityRef(self, short_name)
            self.addElement(entity_ref)
            self.ordered_elements.append(entity_ref)
        return self.getElement(short_name, EOCExecutableEntityRef)

    def getOrderedElements(self) -> List[EOCExecutableEntityRefAbstract]:
        """
        Returns the list of ordered executable entity references.

        Returns:
            List of ordered executable entity references
        """
        return self.ordered_elements


class EOCEventRef(ARObject):
    """
    Represents an event reference in execution order constraints.
    Defines a reference to an event used in execution order specifications.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the EOCEventRef with default values.
        """
        super().__init__()
        self.eventRef: Union[Union[RefType, None] , None] = None

    def getEventRef(self) -> RefType:
        """
        Gets the event reference.

        Returns:
            Reference to the event
        """
        return self.eventRef

    def setEventRef(self, value: RefType):
        """
        Sets the event reference.

        Args:
            value: The event reference to set

        Returns:
            self for method chaining
        """
        self.eventRef = value
        return self


class EOCExecutableEntityRefGroup(ARObject):
    """
    Represents a group of executable entity references in execution order constraints.
    Defines a collection of executable entity references that can be ordered as a group.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the EOCExecutableEntityRefGroup with default values.
        """
        super().__init__()
        self.entityRefs: List[RefType] = []

    def addEntityRef(self, ref: RefType):
        """
        Adds an executable entity reference to this group.

        Args:
            ref: The executable entity reference to add

        Returns:
            self for method chaining
        """
        self.entityRefs.append(ref)
        return self

    def getEntityRefs(self) -> List[RefType]:
        """
        Gets the list of executable entity references.

        Returns:
            List of executable entity references
        """
        return self.entityRefs


class ExecutionOrderConstraintTypeEnum:
    """
    Enumeration for execution order constraint types in AUTOSAR.
    Defines different types of execution order constraints.
    """

    ENUM_BEFORE = "before"
    ENUM_AFTER = "after"
    ENUM_IMMEDIATE = "immediate"
    ENUM_CONCURRENT = "concurrent"


class LetDataExchangeParadigmEnum:
    """
    Enumeration for LET (Logical Execution Time) data exchange paradigms in AUTOSAR.
    Defines different paradigms for data exchange in LET timing.
    """

    ENUM_BUFFERED = "buffered"
    ENUM_UNBUFFERED = "unbuffered"
    ENUM_EVENT_TRIGGERED = "event-triggered"
