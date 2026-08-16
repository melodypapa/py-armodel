"""
This module contains classes for representing AUTOSAR mode declaration structures
in the CommonStructure module. Mode declarations define different operational states
that software components or BSW modules can be in, along with transitions between states.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpType, AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType, TRefType, AREnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum


class ModeActivationKind(AREnum):
    """
    Kind of mode switch condition used for activation of an event,
    as further described for each enumeration field.
    """

    # ModeActivationKind method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.34, p.96
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # On entering the referred mode. Tags: atp.EnumerationLiteralIndex=0
    ON_ENTRY = "onEntry"

    # On exiting the referred mode. Tags: atp.EnumerationLiteralIndex=1
    ON_EXIT = "onExit"

    # On transition of the 1st referred mode to the 2nd referred mode.
    # Tags: atp.EnumerationLiteralIndex=2
    ON_TRANSITION = "onTransition"

    def __init__(self):
        """
        Initializes the ModeActivationKind with valid values.
        """
        super().__init__(
            (
                ModeActivationKind.ON_ENTRY,
                ModeActivationKind.ON_EXIT,
                ModeActivationKind.ON_TRANSITION,
            )
        )


class ModeDeclarationGroupPrototypeMapping(ARObject):
    """
    Represents a mapping between mode declaration group prototypes in AUTOSAR models.
    This class defines relationships between different mode declaration group prototypes across system boundaries.
    """

    # ModeDeclarationGroupPrototypeMapping method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getFirstModeGroupRef         [x] impl  [x] docstring  [x] test
    # [x] setFirstModeGroupRef         [x] impl  [x] docstring  [x] test
    # [x] getModeDeclarationMappingSetRef [x] impl  [x] docstring  [x] test
    # [x] setModeDeclarationMappingSetRef [x] impl  [x] docstring  [x] test
    # [x] getSecondModeGroupRef        [x] impl  [x] docstring  [x] test
    # [x] setSecondModeGroupRef        [x] impl  [x] docstring  [x] test

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

    # ModeDeclaration method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] setValue                     [x] impl  [x] docstring  [x] test
    # [x] getValue                     [x] impl  [x] docstring  [x] test

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

    # ModeRequestTypeMap method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getImplementationDataTypeRef [x] impl  [x] docstring  [x] test
    # [x] setImplementationDataTypeRef [x] impl  [x] docstring  [x] test
    # [x] getModeGroupRef              [x] impl  [x] docstring  [x] test
    # [x] setModeGroupRef              [x] impl  [x] docstring  [x] test

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
    A collection of Mode Declarations. Also, the initial mode is explicitly identified.
    """

    # ModeDeclarationGroup method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] createModeDeclaration        [x] impl  [x] docstring  [x] test
    # [x] getModeDeclarations          [x] impl  [x] docstring  [x] test
    # [x] setInitialModeRef            [x] impl  [x] docstring  [x] test
    # [x] getInitialModeRef            [x] impl  [x] docstring  [x] test
    # [x] setOnTransitionValue         [x] impl  [x] docstring  [x] test
    # [x] getOnTransitionValue         [x] impl  [x] docstring  [x] test
    # [x] createModeTransition         [x] impl  [x] docstring  [x] test
    # [x] getModeTransitions           [x] impl  [x] docstring  [x] test
    # [x] getModeManagerErrorBehavior  [x] impl  [x] docstring  [x] test
    # [x] setModeManagerErrorBehavior  [x] impl  [x] docstring  [x] test
    # [x] getModeUserErrorBehavior     [x] impl  [x] docstring  [x] test
    # [x] setModeUserErrorBehavior     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ModeDeclarationGroup with a parent and short name.

        Args:
            parent: The parent ARObject that contains this mode declaration group
            short_name: The unique short name of this mode declaration group
        """
        super().__init__(parent, short_name)

        # The initial mode of the ModeDeclarationGroup. This mode is active before any
        # mode switches occurred.
        self.initialModeRef: RefType = None

        # The ModeDeclarations collected in this ModeDeclarationGroup.
        self.modeDeclarations: List["ModeDeclaration"] = []

        # This represents the ability to define the error behavior expected by the mode
        # manager in case of errors on the mode user side (e.g. terminated mode user).
        self.modeManagerErrorBehavior: "ModeErrorBehavior" = None

        # This represents the available ModeTransitions of the ModeDeclarationGroup.
        self.modeTransitions: List["ModeTransition"] = []

        # This represents the definition of the error behavior expected by the mode
        # user in case of errors on the mode manager side (e.g. terminated mode
        # manager).
        self.modeUserErrorBehavior: "ModeErrorBehavior" = None

        # The value of this attribute shall be taken into account by the RTE generator
        # for programmatically representing a value used for the transition between two
        # statuses.
        self.onTransitionValue: ARNumerical = None

    def createModeDeclaration(self, short_name: str) -> "ModeDeclaration":
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

    def getModeDeclarations(self) -> List["ModeDeclaration"]:
        """
        Gets all mode declarations from the elements list, sorted by short name.

        Returns:
            List of ModeDeclaration instances sorted by short name
        """
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclaration), self.elements), key=lambda o: o.short_name))

    def setInitialModeRef(self, ref: RefType) -> "ModeDeclarationGroup":
        """
        Sets the reference to the initial mode of this group.
        Only sets the value if it is not None.

        Args:
            ref: The initial mode reference to set

        Returns:
            self for method chaining
        """
        if ref is not None:
            self.initialModeRef = ref
        return self

    def getInitialModeRef(self) -> Optional[RefType]:
        """
        Gets the reference to the initial mode of this group.

        Returns:
            Optional[RefType]: The initial mode reference
        """
        return self.initialModeRef

    def setOnTransitionValue(self, value: ARNumerical) -> "ModeDeclarationGroup":
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

    def getOnTransitionValue(self) -> Optional[ARNumerical]:
        """
        Gets the value used on mode transitions.

        Returns:
            Optional[ARNumerical]: The transition value
        """
        return self.onTransitionValue

    def createModeTransition(self, short_name: str) -> "ModeTransition":
        """
        Creates and adds a ModeTransition to this mode declaration group.

        Args:
            short_name: The short name for the new mode transition

        Returns:
            The created ModeTransition instance
        """
        if not self.IsElementExists(short_name):
            spec = ModeTransition(self, short_name)
            self.addElement(spec)
            self.modeTransitions.append(spec)
        return self.getElement(short_name, ModeTransition)

    def getModeTransitions(self) -> List["ModeTransition"]:
        """
        Gets all mode transitions of this mode declaration group.

        Returns:
            List of ModeTransition instances
        """
        return self.modeTransitions

    def getModeManagerErrorBehavior(self) -> Optional["ModeErrorBehavior"]:
        """
        Gets the error behavior expected by the mode manager in case of errors on the
        mode user side (e.g. terminated mode user).

        Returns:
            Optional["ModeErrorBehavior"]: The mode manager error behavior
        """
        return self.modeManagerErrorBehavior

    def setModeManagerErrorBehavior(self, value: "ModeErrorBehavior") -> "ModeDeclarationGroup":
        """
        Sets the error behavior expected by the mode manager in case of errors on the
        mode user side (e.g. terminated mode user).
        Only sets the value if it is not None.

        Args:
            value: The mode manager error behavior to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeManagerErrorBehavior = value
        return self

    def getModeUserErrorBehavior(self) -> Optional["ModeErrorBehavior"]:
        """
        Gets the error behavior expected by the mode user in case of errors on the mode
        manager side (e.g. terminated mode manager).

        Returns:
            Optional["ModeErrorBehavior"]: The mode user error behavior
        """
        return self.modeUserErrorBehavior

    def setModeUserErrorBehavior(self, value: "ModeErrorBehavior") -> "ModeDeclarationGroup":
        """
        Sets the error behavior expected by the mode user in case of errors on the mode
        manager side (e.g. terminated mode manager).
        Only sets the value if it is not None.

        Args:
            value: The mode user error behavior to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeUserErrorBehavior = value
        return self


class ModeDeclarationGroupPrototype(AtpPrototype):
    """
    The ModeDeclarationGroupPrototype specifies a set of Modes (ModeDeclarationGroup) which is provided or required in the given context.
    """

    # ModeDeclarationGroupPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.17, p.113
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSwCalibrationAccess   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwCalibrationAccess   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTypeTRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTypeTRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This allows for specifying whether or not the enclosing ModeDeclarationGroupPrototype can be measured at run-time.
        self.swCalibrationAccess: Optional[SwCalibrationAccessEnum] = None

        # The "collection of ModeDeclarations" ( = ModeDeclarationGroup) supported by a component Stereotypes: isOfType
        self.typeTRef: Optional[TRefType] = None

    def getSwCalibrationAccess(self) -> Optional["SwCalibrationAccessEnum"]:
        """
        Gets whether or not the enclosing ModeDeclarationGroupPrototype can be measured at run-time.

        This allows for specifying whether or not the enclosing ModeDeclarationGroupPrototype can be measured at run-time.

        Returns:
            SwCalibrationAccessEnum representing the calibration access, or None if not set
        """
        return self.swCalibrationAccess

    def setSwCalibrationAccess(self, value: Optional["SwCalibrationAccessEnum"]) -> "ModeDeclarationGroupPrototype":
        """
        Sets whether or not the enclosing ModeDeclarationGroupPrototype can be measured at run-time.
        A None value is a no-op and does not overwrite an existing calibration access.

        This allows for specifying whether or not the enclosing ModeDeclarationGroupPrototype can be measured at run-time.

        Args:
            value: The SwCalibrationAccessEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swCalibrationAccess = value
        return self

    def getTypeTRef(self) -> Optional[TRefType]:
        """
        Gets the "collection of ModeDeclarations" ( = ModeDeclarationGroup) supported by a component.

        The "collection of ModeDeclarations" ( = ModeDeclarationGroup) supported by a component Stereotypes: isOfType

        Returns:
            TRefType referencing the ModeDeclarationGroup, or None if not set
        """
        return self.typeTRef

    def setTypeTRef(self, value: Optional[TRefType]) -> "ModeDeclarationGroupPrototype":
        """
        Sets the "collection of ModeDeclarations" ( = ModeDeclarationGroup) supported by a component.
        A None value is a no-op and does not overwrite an existing type reference.

        The "collection of ModeDeclarations" ( = ModeDeclarationGroup) supported by a component Stereotypes: isOfType

        Args:
            value: The ModeDeclarationGroup type reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.typeTRef = value
        return self


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

    def setEnteredModeRef(self, value: RefType) -> "ModeTransition":
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

    def setExitedModeRef(self, value: RefType) -> "ModeTransition":
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
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getDefaultModeRef            [x] impl  [x] docstring  [x] test
    # [x] setDefaultModeRef            [x] impl  [x] docstring  [x] test
    # [x] getErrorReactionPolicy       [x] impl  [x] docstring  [x] test
    # [x] setErrorReactionPolicy       [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the ModeErrorBehavior with default values.
        """
        super().__init__()

        # The ModeDeclaration that is considered the error mode.
        self.defaultModeRef: Optional[RefType] = None

        # The policy defining which default mode shall apply in case of error.
        self.errorReactionPolicy: Optional[str] = None

    def getDefaultModeRef(self) -> Optional[RefType]:
        """
        Gets the reference to the error mode declaration.

        Returns:
            Optional[RefType]: The error mode reference
        """
        return self.defaultModeRef

    def setDefaultModeRef(self, value: RefType) -> "ModeErrorBehavior":
        """
        Sets the reference to the error mode declaration.
        Only sets the value if it is not None.

        Args:
            value: The error mode reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defaultModeRef = value
        return self

    def getErrorReactionPolicy(self) -> Optional[str]:
        """
        Gets the error reaction policy defining behavior on mode error.

        Returns:
            Optional[str]: The error reaction policy
        """
        return self.errorReactionPolicy

    def setErrorReactionPolicy(self, value: str) -> "ModeErrorBehavior":
        """
        Sets the error reaction policy.
        Only sets the value if it is not None.

        Args:
            value: The error reaction policy to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.errorReactionPolicy = value
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
        super().__init__(
            (
                ModeErrorReactionPolicyEnum.KEEP_MODE,
                ModeErrorReactionPolicyEnum.TRANSITION_TO_DEFAULT_MODE,
                ModeErrorReactionPolicyEnum.TRANSITION_TO_SAFE_MODE,
            )
        )
