"""
This module defines additional mode declaration classes in AUTOSAR.
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, AREnum


class ModeTransition(AtpStructureElement):
    """
    This meta-class represents the ability to describe possible ModeTransitions in
    the context of a ModeDeclarationGroup.
    """
    # ModeTransition method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getEnteredModeRef            [x] impl  [x] docstring  [x] test
    # [x] setEnteredModeRef            [x] impl  [x] docstring  [x] test
    # [x] getExitedModeRef             [x] impl  [x] docstring  [x] test
    # [x] setExitedModeRef             [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ModeTransition with a parent and short name.

        Args:
            parent: The parent ARObject that contains this mode transition
            short_name: The unique short name of this mode transition
        """
        super().__init__(parent, short_name)

        # This represents the entered mode of the ModeTransition.
        self.enteredModeRef: RefType = None

        # This represents the exited mode of the ModeTransition.
        self.exitedModeRef: RefType = None

    def getEnteredModeRef(self) -> Optional[RefType]:
        """
        Gets the mode that is entered by this transition.

        Returns:
            Optional[RefType]: The entered mode reference
        """
        return self.enteredModeRef

    def setEnteredModeRef(self, value: RefType) -> 'ModeTransition':
        """
        Sets the mode that is entered by this transition.
        Only sets the value if it is not None.

        Args:
            value: The entered mode reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.enteredModeRef = value
        return self

    def getExitedModeRef(self) -> Optional[RefType]:
        """
        Gets the mode that is exited by this transition.

        Returns:
            Optional[RefType]: The exited mode reference
        """
        return self.exitedModeRef

    def setExitedModeRef(self, value: RefType) -> 'ModeTransition':
        """
        Sets the mode that is exited by this transition.
        Only sets the value if it is not None.

        Args:
            value: The exited mode reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exitedModeRef = value
        return self


class ModeErrorBehavior(ARObject):
    """
    Represents mode error behavior in AUTOSAR.
    This class defines the behavior when a mode error occurs.
    """
    # ModeErrorBehavior method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getErrorPolicy               [x] impl  [ ] docstring  [ ] test
    # [ ] setErrorPolicy               [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        """
        Initializes the ModeErrorBehavior with default values.
        """
        super().__init__()
        self.errorPolicy: str = None

    def getErrorPolicy(self):
        return self.errorPolicy

    def setErrorPolicy(self, value):
        self.errorPolicy = value
        return self


class ModeErrorReactionPolicyEnum(AREnum):
    """
    Enumeration for mode error reaction policy.
    """
    # ModeErrorReactionPolicyEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    KEEP_MODE = "keep-mode"
    TRANSITION_TO_DEFAULT_MODE = "transition-to-default-mode"
    TRANSITION_TO_SAFE_MODE = "transition-to-safe-mode"

    def __init__(self):
        super().__init__((
            ModeErrorReactionPolicyEnum.KEEP_MODE,
            ModeErrorReactionPolicyEnum.TRANSITION_TO_DEFAULT_MODE,
            ModeErrorReactionPolicyEnum.TRANSITION_TO_SAFE_MODE,
        ))
