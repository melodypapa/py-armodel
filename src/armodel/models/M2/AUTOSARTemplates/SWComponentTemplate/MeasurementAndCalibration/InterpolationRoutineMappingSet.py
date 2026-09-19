"""
InterpolationRoutineMappingSet module for AUTOSAR M2 models.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, RefType

__all__ = [
    "InterpolationRoutine",
    "InterpolationRoutineMapping",
]


class InterpolationRoutine(ARObject):
    """
    This represents an interpolation routine taken to evaluate the contents of a curve or map against a specific input value.

    [constr_5114] Semantics of InterpolationRoutine.isDefault: For each SwRecordLayout that is referenced by one or more InterpolationRoutineMappings that are aggregated by InterpolationRoutineMappingSets that are referenced from a System in the role interpolationRoutineMappingSet, only one of the collection of aggregated InterpolationRoutines shall have attribute isDefault set to True.
    """

    # InterpolationRoutine method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 2.6, pp.46-47 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInterpolationRoutineRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInterpolationRoutineRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIsDefault               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIsDefault               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortLabel              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortLabel              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This specifies a BswModuleEntry which implements the current interpolation method for the given record layout. Tags: xml.sequenceOffset=30
        self.interpolationRoutineRef: Optional[RefType] = None

        # This attribute specifies whether the enclosing InterpolationRoutine is considered the default in the context (defined by the System Template) of a given collection InterpolationRoutineMapping that owns the enclosing InterpolationRoutine. Tags: xml.sequenceOffset=20
        self.isDefault: Optional[Boolean] = None

        # This is the name of the interpolation method which is implemented by the referenced bswModuleEntry. It corresponds to swInterpolationMethod in SwDataDefProps. Tags: xml.sequenceOffset=10
        self.shortLabel: Optional[Identifier] = None

    def getInterpolationRoutineRef(self) -> Optional[RefType]:
        """
        This specifies a BswModuleEntry which implements the current interpolation method for the given record layout. Tags: xml.sequenceOffset=30
        """
        return self.interpolationRoutineRef

    def setInterpolationRoutineRef(self, value: Optional[RefType]) -> "InterpolationRoutine":
        """
        This specifies a BswModuleEntry which implements the current interpolation method for the given record layout. Tags: xml.sequenceOffset=30

        A None value is a no-op and does not set interpolationRoutineRef.
        """
        if value is not None:
            self.interpolationRoutineRef = value
        return self

    def getIsDefault(self) -> Optional[Boolean]:
        """
        This attribute specifies whether the enclosing InterpolationRoutine is considered the default in the context (defined by the System Template) of a given collection InterpolationRoutineMapping that owns the enclosing InterpolationRoutine. Tags: xml.sequenceOffset=20
        """
        return self.isDefault

    def setIsDefault(self, value: Optional[Boolean]) -> "InterpolationRoutine":
        """
        This attribute specifies whether the enclosing InterpolationRoutine is considered the default in the context (defined by the System Template) of a given collection InterpolationRoutineMapping that owns the enclosing InterpolationRoutine. Tags: xml.sequenceOffset=20

        A None value is a no-op and does not set isDefault.
        """
        if value is not None:
            self.isDefault = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This is the name of the interpolation method which is implemented by the referenced bswModuleEntry. It corresponds to swInterpolationMethod in SwDataDefProps. Tags: xml.sequenceOffset=10
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "InterpolationRoutine":
        """
        This is the name of the interpolation method which is implemented by the referenced bswModuleEntry. It corresponds to swInterpolationMethod in SwDataDefProps. Tags: xml.sequenceOffset=10

        A None value is a no-op and does not set shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self


class InterpolationRoutineMapping(ARObject):
    """
    This meta-class provides a mapping between one record layout and its matching interpolation routines. This allows to formally specify the semantics of the interpolation routines.

    The use case is such that the curves/Maps define an interpolation method. This mapping table specifies which interpolation routine implements methods for a particular record layout. Using this information, the implementer of a software-component can select the appropriate interpolation routine.
    """

    # InterpolationRoutineMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 2.5, p.46 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInterpolationRoutines    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addInterpolationRoutine     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createInterpolationRoutine  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is one particular interpolation routine which is mapped to the record layout.
        self.interpolationRoutines: List[InterpolationRoutine] = []

        # This refers to the record layout which is mapped to interpolation routines.
        self.swRecordLayoutRef: Optional[RefType] = None

    def getInterpolationRoutines(self) -> List[InterpolationRoutine]:
        """
        This is one particular interpolation routine which is mapped to the record layout.
        """
        return self.interpolationRoutines

    def addInterpolationRoutine(self, value: InterpolationRoutine) -> "InterpolationRoutineMapping":
        """
        This is one particular interpolation routine which is mapped to the record layout.
        """
        self.interpolationRoutines.append(value)
        return self

    def createInterpolationRoutine(self) -> InterpolationRoutine:
        """
        This is one particular interpolation routine which is mapped to the record layout.
        """
        routine = InterpolationRoutine()
        self.interpolationRoutines.append(routine)
        return routine

    def getSwRecordLayoutRef(self) -> Optional[RefType]:
        """
        This refers to the record layout which is mapped to interpolation routines.
        """
        return self.swRecordLayoutRef

    def setSwRecordLayoutRef(self, value: Optional[RefType]) -> "InterpolationRoutineMapping":
        """
        This refers to the record layout which is mapped to interpolation routines.

        A None value is a no-op and does not set swRecordLayoutRef.
        """
        if value is not None:
            self.swRecordLayoutRef = value
        return self
