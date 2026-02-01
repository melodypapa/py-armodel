"""
This module defines additional mode declaration classes in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, AREnum


class ModeTransition(ARObject):
    """
    Represents a mode transition in AUTOSAR.
    This class defines transitions between different mode declarations.
    """

    def __init__(self):
        """
        Initializes the ModeTransition with default values.
        """
        super().__init__()
        self.sourceModeRef: RefType = None
        self.targetModeRef: RefType = None

    def getSourceModeRef(self):
        return self.sourceModeRef

    def setSourceModeRef(self, value):
        self.sourceModeRef = value
        return self

    def getTargetModeRef(self):
        return self.targetModeRef

    def setTargetModeRef(self, value):
        self.targetModeRef = value
        return self


class ModeErrorBehavior(ARObject):
    """
    Represents mode error behavior in AUTOSAR.
    This class defines the behavior when a mode error occurs.
    """

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

    KEEP_MODE = "keep-mode"
    TRANSITION_TO_DEFAULT_MODE = "transition-to-default-mode"
    TRANSITION_TO_SAFE_MODE = "transition-to-safe-mode"

    def __init__(self):
        super().__init__((
            ModeErrorReactionPolicyEnum.KEEP_MODE,
            ModeErrorReactionPolicyEnum.TRANSITION_TO_DEFAULT_MODE,
            ModeErrorReactionPolicyEnum.TRANSITION_TO_SAFE_MODE,
        ))