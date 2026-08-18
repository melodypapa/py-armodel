"""
This module contains classes for representing AUTOSAR mode declaration structures
in the CommonStructure module. Mode declarations define different operational states
that software components or BSW modules can be in, along with transitions between states.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpType, AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TRefType, AREnum
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
    Declaration of one Mode. The name and semantics of a specific mode is not defined in the meta-model.
    """

    # ModeDeclaration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.11, p.43
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The RTE shall take the value of this attribute for generating the source code representation of this Mode Declaration.
        self.value: Optional[PositiveInteger] = None

    def getValue(self) -> Optional[PositiveInteger]:
        """
        The RTE shall take the value of this attribute for generating the source code representation of this Mode Declaration.

        Returns:
            Optional[PositiveInteger]: The mode value
        """
        return self.value

    def setValue(self, value: Optional[PositiveInteger]) -> "ModeDeclaration":
        """
        The RTE shall take the value of this attribute for generating the source code representation of this Mode Declaration.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


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
    A collection of Mode Declarations. Also, the initial mode is explicitly identified. Tags: atp.recommendedPackage=ModeDeclarationGroups
    """

    # ModeDeclarationGroup method parity checklist:
    # Spec: AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.68, p.197
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createModeDeclaration        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeDeclarations          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInitialModeRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInitialModeRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOnTransitionValue         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOnTransitionValue         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createModeTransition         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeTransitions           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getModeManagerErrorBehavior  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModeManagerErrorBehavior  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeUserErrorBehavior     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModeUserErrorBehavior     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The initial mode of the ModeDeclarationGroup. This mode is active before any mode switches occurred.
        self.initialModeRef: Optional[RefType] = None

        # The ModeDeclarations collected in this ModeDeclaration Group. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeDeclaration.shortName, mode Declaration.variationPoint.shortLabel vh.latestBindingTime=blueprintDerivationTime
        self.modeDeclarations: List[ModeDeclaration] = []

        # This represents the ability to define the error behavior expected by the mode manager in case of errors on the mode user side (e.g. terminated mode user).
        self.modeManagerErrorBehavior: Optional[ModeErrorBehavior] = None

        # This represents the avaliable ModeTransitions of the ModeDeclarationGroup
        self.modeTransitions: List[ModeTransition] = []

        # This represents the definition of the error behavior expected by the mode user in case of errors on the mode manager side (e.g. terminated mode manager).
        self.modeUserErrorBehavior: Optional[ModeErrorBehavior] = None

        # The value of this attribute shall be taken into account by the RTE generator for programmatically representing a value used for the transition between two statuses.
        self.onTransitionValue: Optional[PositiveInteger] = None

    def createModeDeclaration(self, short_name: str) -> ModeDeclaration:
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

    def getModeDeclarations(self) -> List[ModeDeclaration]:
        """
        The ModeDeclarations collected in this ModeDeclaration Group.

        Returns:
            List of ModeDeclaration instances
        """
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclaration), self.elements), key=lambda o: o.short_name))

    def setInitialModeRef(self, ref: Optional[RefType]) -> "ModeDeclarationGroup":
        """
        The initial mode of the ModeDeclarationGroup. This mode is active before any mode switches occurred.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            ref: The value to set

        Returns:
            self for method chaining
        """
        if ref is not None:
            self.initialModeRef = ref
        return self

    def getInitialModeRef(self) -> Optional[RefType]:
        """
        The initial mode of the ModeDeclarationGroup. This mode is active before any mode switches occurred.

        Returns:
            Optional[RefType]: The initial mode reference
        """
        return self.initialModeRef

    def setOnTransitionValue(self, value: Optional[PositiveInteger]) -> "ModeDeclarationGroup":
        """
        The value of this attribute shall be taken into account by the RTE generator for programmatically representing a value used for the transition between two statuses.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onTransitionValue = value
        return self

    def getOnTransitionValue(self) -> Optional[PositiveInteger]:
        """
        The value of this attribute shall be taken into account by the RTE generator for programmatically representing a value used for the transition between two statuses.

        Returns:
            Optional[PositiveInteger]: The transition value
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
        This represents the avaliable ModeTransitions of the ModeDeclarationGroup

        Returns:
            List of ModeTransition instances
        """
        return self.modeTransitions

    def getModeManagerErrorBehavior(self) -> Optional["ModeErrorBehavior"]:
        """
        This represents the ability to define the error behavior expected by the mode manager in case of errors on the mode user side (e.g. terminated mode user).

        Returns:
            Optional["ModeErrorBehavior"]: The mode manager error behavior
        """
        return self.modeManagerErrorBehavior

    def setModeManagerErrorBehavior(self, value: Optional["ModeErrorBehavior"]) -> "ModeDeclarationGroup":
        """
        This represents the ability to define the error behavior expected by the mode manager in case of errors on the mode user side (e.g. terminated mode user).
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeManagerErrorBehavior = value
        return self

    def getModeUserErrorBehavior(self) -> Optional["ModeErrorBehavior"]:
        """
        This represents the definition of the error behavior expected by the mode user in case of errors on the mode manager side (e.g. terminated mode manager).

        Returns:
            Optional["ModeErrorBehavior"]: The mode user error behavior
        """
        return self.modeUserErrorBehavior

    def setModeUserErrorBehavior(self, value: Optional["ModeErrorBehavior"]) -> "ModeDeclarationGroup":
        """
        This represents the definition of the error behavior expected by the mode user in case of errors on the mode manager side (e.g. terminated mode manager).
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

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
    This meta-class represents the ability to describe possible ModeTransitions in the context of a Mode DeclarationGroup.
    """

    # ModeTransition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.12, p.43
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEnteredModeRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEnteredModeRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExitedModeRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExitedModeRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the entered model of the ModeTransition.
        self.enteredModeRef: Optional[RefType] = None

        # This represents the exited mode of the ModeTransition
        self.exitedModeRef: Optional[RefType] = None

    def getEnteredModeRef(self) -> Optional[RefType]:
        """
        This represents the entered model of the ModeTransition.

        Returns:
            Optional[RefType]: The entered mode reference
        """
        return self.enteredModeRef

    def setEnteredModeRef(self, value: Optional[RefType]) -> "ModeTransition":
        """
        This represents the entered model of the ModeTransition.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.enteredModeRef = value
        return self

    def getExitedModeRef(self) -> Optional[RefType]:
        """
        This represents the exited mode of the ModeTransition

        Returns:
            Optional[RefType]: The exited mode reference
        """
        return self.exitedModeRef

    def setExitedModeRef(self, value: Optional[RefType]) -> "ModeTransition":
        """
        This represents the exited mode of the ModeTransition
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exitedModeRef = value
        return self


class ModeErrorBehavior(ARObject):
    """
    This represents the ability to define the error behavior in the context of mode handling.
    """

    # ModeErrorBehavior method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.13, p.44
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefaultModeRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultModeRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getErrorReactionPolicy      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setErrorReactionPolicy      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the ModeDeclaration that is considered the error mode in the context of the enclosing ModeDeclarationGroup.
        self.defaultModeRef: Optional[RefType] = None

        # This represents the ability to define the policy in terms of which default model shall apply in case an error occurs.
        self.errorReactionPolicy: Optional["ModeErrorReactionPolicyEnum"] = None

    def getDefaultModeRef(self) -> Optional[RefType]:
        """
        This represents the ModeDeclaration that is considered the error mode in the context of the enclosing ModeDeclarationGroup.

        Returns:
            Optional[RefType]: The default mode reference
        """
        return self.defaultModeRef

    def setDefaultModeRef(self, value: Optional[RefType]) -> "ModeErrorBehavior":
        """
        This represents the ModeDeclaration that is considered the error mode in the context of the enclosing ModeDeclarationGroup.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defaultModeRef = value
        return self

    def getErrorReactionPolicy(self) -> Optional["ModeErrorReactionPolicyEnum"]:
        """
        This represents the ability to define the policy in terms of which default model shall apply in case an error occurs.

        Returns:
            Optional[ModeErrorReactionPolicyEnum]: The error reaction policy
        """
        return self.errorReactionPolicy

    def setErrorReactionPolicy(self, value: Optional["ModeErrorReactionPolicyEnum"]) -> "ModeErrorBehavior":
        """
        This represents the ability to define the policy in terms of which default model shall apply in case an error occurs.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.errorReactionPolicy = value
        return self


class ModeErrorReactionPolicyEnum(AREnum):
    """
    This represents the ability to specify the reaction on a mode error.
    """

    # ModeErrorReactionPolicyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.14, p.44
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on ModeErrorBehavior.errorReactionPolicy
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # This represents the ability to switch to the defaultMode in case of a mode error. Tags: atp.EnumerationLiteralIndex=0
    DEFAULT_MODE = "defaultMode"

    # This represents the ability to keep the last mode in case of a mode error. Tags: atp.EnumerationLiteralIndex=1
    LAST_MODE = "lastMode"

    def __init__(self):
        super().__init__(
            [
                ModeErrorReactionPolicyEnum.DEFAULT_MODE,
                ModeErrorReactionPolicyEnum.LAST_MODE,
            ]
        )
