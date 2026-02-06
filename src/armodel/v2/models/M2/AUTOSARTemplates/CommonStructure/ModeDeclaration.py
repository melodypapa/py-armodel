"""
This module contains classes for representing AUTOSAR mode declaration structures
in the CommonStructure module. Mode declarations define different operational states
that software components or BSW modules can be in, along with transitions between states.
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpPrototype,
    AtpStructureElement,
    AtpType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARNumerical,
    PositiveInteger,
    RefType,
    TRefType,
)


class ModeActivationKind(AREnum):
    """
    Enumeration for mode activation kind values.
    Defines the kind of mode switch condition used for activation of an event.
    """
    # On entering the referred mode
    ON_ENTRY = "onEntry"
    # On exiting the referred mode
    ON_EXIT = "onExit"
    # On transition of the 1st referred mode to the 2nd referred mode
    ON_TRANSITION = "onTransition"

    def __init__(self):
        super().__init__((
            ModeActivationKind.ON_ENTRY,
            ModeActivationKind.ON_EXIT,
            ModeActivationKind.ON_TRANSITION,
        ))


class ModeDeclarationGroupPrototypeMapping(ARObject):
    """
    Represents a mapping between mode declaration group prototypes in AUTOSAR models.
    This class defines relationships between different mode declaration group prototypes across system boundaries.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        """
        Initializes the ModeDeclarationGroupPrototypeMapping with default values.
        """
        super().__init__()

        # Reference to the first mode group in the mapping
        self.firstModeGroupRef: RefType = None
        # Reference to the mode declaration mapping set
        self.modeDeclarationMappingSetRef: RefType = None
        # Reference to the second mode group in the mapping
        self.secondModeGroupRef: RefType = None

    def getFirstModeGroupRef(self):
        """
        Gets the reference to the first mode group in the mapping.

        Returns:
            RefType: The first mode group reference
        """
        return self.firstModeGroupRef

    def setFirstModeGroupRef(self, value):
        """
        Sets the reference to the first mode group in the mapping.
        Only sets the value if it is not None.

        Args:
            value: The first mode group reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.firstModeGroupRef = value
        return self

    def getModeDeclarationMappingSetRef(self):
        """
        Gets the reference to the mode declaration mapping set.

        Returns:
            RefType: The mode declaration mapping set reference
        """
        return self.modeDeclarationMappingSetRef

    def setModeDeclarationMappingSetRef(self, value):
        """
        Sets the reference to the mode declaration mapping set.
        Only sets the value if it is not None.

        Args:
            value: The mode declaration mapping set reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeDeclarationMappingSetRef = value
        return self

    def getSecondModeGroupRef(self):
        """
        Gets the reference to the second mode group in the mapping.

        Returns:
            RefType: The second mode group reference
        """
        return self.secondModeGroupRef

    def setSecondModeGroupRef(self, value):
        """
        Sets the reference to the second mode group in the mapping.
        Only sets the value if it is not None.

        Args:
            value: The second mode group reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.secondModeGroupRef = value
        return self


class ModeDeclaration(AtpStructureElement):
    """
    Represents a mode declaration in AUTOSAR models.
    Mode declarations define specific operational states that components can be in, with associated values.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ModeDeclaration with a parent and short name.

        Args:
            parent: The parent ARObject that contains this mode declaration
            short_name: The unique short name of this mode declaration
        """
        super().__init__(parent, short_name)

        # Value associated with this mode declaration
        self.value: ARNumerical = None

    def setValue(self, value):
        """
        Sets the value associated with this mode declaration.
        Only sets the value if it is not None.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        self.value = value
        return self

    def getValue(self) -> ARNumerical:
        """
        Gets the value associated with this mode declaration.

        Returns:
            ARNumerical: The mode value
        """
        return self.value


class ModeRequestTypeMap(ARObject):
    """
    Represents a mapping between mode requests and implementation data types in AUTOSAR models.
    This class defines how mode requests are mapped to specific implementation data types.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        """
        Initializes the ModeRequestTypeMap with default values.
        """
        super().__init__()

        # Reference to the implementation data type for mode requests
        self.implementationDataTypeRef: RefType = None
        # Reference to the mode group for this mapping
        self.modeGroupRef: RefType = None

    def getImplementationDataTypeRef(self):
        """
        Gets the reference to the implementation data type for mode requests.

        Returns:
            RefType: The implementation data type reference
        """
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value):
        """
        Sets the reference to the implementation data type for mode requests.
        Only sets the value if it is not None.

        Args:
            value: The implementation data type reference to set

        Returns:
            self for method chaining
        """
        self.implementationDataTypeRef = value
        return self

    def getModeGroupRef(self):
        """
        Gets the reference to the mode group for this mapping.

        Returns:
            RefType: The mode group reference
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        """
        Sets the reference to the mode group for this mapping.
        Only sets the value if it is not None.

        Args:
            value: The mode group reference to set

        Returns:
            self for method chaining
        """
        self.modeGroupRef = value
        return self


class ModeDeclarationGroup(AtpType):
    """
    Represents a mode declaration group in AUTOSAR models.
    Mode declaration groups define collections of related mode declarations and their initial state.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ModeDeclarationGroup with a parent and short name.

        Args:
            parent: The parent ARObject that contains this mode declaration group
            short_name: The unique short name of this mode declaration group
        """
        super().__init__(parent, short_name)

        # Reference to the initial mode of this group
        self.initialModeRef: RefType = None
        # List of mode declarations in this group
        self.modeDeclarations: List['ModeDeclaration'] = []
        # Error behavior for the mode manager
        self.modeManagerErrorBehavior = None
        # Mode transition behavior for this group
        self.modeTransition = None
        # Error behavior for the mode user
        self.modeUserErrorBehavior = None
        # Value used on mode transitions
        self.onTransitionValue: PositiveInteger = None

    def createModeDeclaration(self, short_name: str) -> 'ModeDeclaration':
        """
        Creates and adds a ModeDeclaration to this mode declaration group.

        Args:
            short_name: The short name for the new mode declaration

        Returns:
            The created ModeDeclaration instance
        """
        if not self.IsElementExists(short_name):
            spec = ModeDeclaration(self, short_name)
            self.addElement(spec)
        return self.getElement(short_name, ModeDeclaration)

    def getModeDeclarations(self) -> List['ModeDeclaration']:
        """
        Gets all mode declarations from the elements list, sorted by short name.

        Returns:
            List of ModeDeclaration instances sorted by short name
        """
        return sorted(filter(lambda a: isinstance(a, ModeDeclaration), self.elements), key=lambda o: o.short_name)

    def setInitialModeRef(self, ref: RefType):
        """
        Sets the reference to the initial mode of this group.
        Only sets the value if it is not None.

        Args:
            ref: The initial mode reference to set

        Returns:
            self for method chaining
        """
        self.initialModeRef = ref
        return self

    def getInitialModeRef(self) -> RefType:
        """
        Gets the reference to the initial mode of this group.

        Returns:
            RefType: The initial mode reference
        """
        return self.initialModeRef

    def setOnTransitionValue(self, value):
        """
        Sets the value used on mode transitions.
        If value is an integer, creates an ARNumerical instance with that value.

        Args:
            value: The value to set for transitions

        Returns:
            self for method chaining
        """
        if isinstance(value, int):
            original_value = value
            value = ARNumerical()
            value.setValue(original_value)
        self.onTransitionValue = value
        return self

    def getOnTransitionValue(self) -> ARNumerical:
        """
        Gets the value used on mode transitions.

        Returns:
            ARNumerical: The transition value
        """
        return self.onTransitionValue


class ModeDeclarationGroupPrototype(AtpPrototype):
    """
    Represents a mode declaration group prototype in AUTOSAR models.
    The ModeDeclarationGroupPrototype specifies a set of Modes (ModeDeclarationGroup) which is provided or required in the given context.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ModeDeclarationGroupPrototype with a parent and short name.

        Args:
            parent: The parent ARObject that contains this mode declaration group prototype
            short_name: The unique short name of this mode declaration group prototype
        """
        super().__init__(parent, short_name)

        # Private storage for software calibration access setting
        self._swCalibrationAccess: str = None
        # Type reference to the mode declaration group
        self.typeTRef: TRefType = None

    @property
    def sw_calibration_access(self):
        """
        Gets the software calibration access setting for this mode declaration group prototype.
        This property controls access permissions for calibration parameters.

        Returns:
            str: The software calibration access setting
        """
        return self._swCalibrationAccess

    @sw_calibration_access.setter
    def sw_calibration_access(self, value):
        """
        Sets the software calibration access setting for this mode declaration group prototype.
        Valid values are "notAccessible", "readOnly", or "readWrite".
        Raises ValueError if an invalid value is provided.

        Args:
            value: The software calibration access setting to set
        """
        if (value not in ("notAccessible", "readOnly", "readWrite")):
            raise ValueError("Invalid SwCalibrationAccess <%s> of ModeDeclarationGroupPrototype <%s>" % (value, self.short_name))
        self._swCalibrationAccess = value

    def getSwCalibrationAccess(self):
        """
        Gets the software calibration access setting for this mode declaration group prototype.
        This is a convenience method that returns the same value as the property.

        Returns:
            str: The software calibration access setting
        """
        return self.sw_calibration_access

    def setSwCalibrationAccess(self, value):
        """
        Sets the software calibration access setting for this mode declaration group prototype.
        This is a convenience method that sets the same value as the property.
        Only sets the value if it is not None.

        Args:
            value: The software calibration access setting to set

        Returns:
            self for method chaining
        """
        self.sw_calibration_access = value
        return self

    def getTypeTRef(self):
        """
        Gets the type reference to the mode declaration group for this prototype.

        Returns:
            TRefType: The type reference
        """
        return self.typeTRef

    def setTypeTRef(self, value):
        """
        Sets the type reference to the mode declaration group for this prototype.
        Only sets the value if it is not None.

        Args:
            value: The type reference to set

        Returns:
            self for method chaining
        """
        self.typeTRef = value
        return self


class ModeErrorBehavior(ARObject):
    """
    Represents mode error behavior in AUTOSAR.
    This class defines the behavior when a mode error occurs.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

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


class ModeTransition(ARObject):
    """
    Represents a mode transition in AUTOSAR.
    This class defines transitions between different mode declarations.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

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
