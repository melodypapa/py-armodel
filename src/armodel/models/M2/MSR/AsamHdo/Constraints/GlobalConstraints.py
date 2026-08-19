from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARNumerical,
    Identifier,
    Limit,
    MonotonyEnum,
    Numerical,
    RefType,
)


class InternalConstrs(ARObject):
    """
    Represents internal constraints for data values.
    Base: ARObject
    """

    # InternalConstrs method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.lower_limit: Limit = None
        self.upper_limit: Limit = None


class ScaleConstrValidityEnum(AREnum):
    """
    Specifies if the values defined by the scales are considered to be valid.
    """

    # ScaleConstrValidityEnum method parity checklist:
    # Source: docs/requirements/xsd/AUTOSAR_00046.xsd (ScaleConstrValidityEnum) — no markdown/PDF table
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [ ] __init__            [x] impl  [ ] docstring  [ ] test  [—] reader  [—] writer
    # [ ] NOT_AVAILABLE       [x] impl  [ ] docstring  [ ] test  [—] reader  [—] writer
    # [ ] NOT_DEFINED         [x] impl  [ ] docstring  [ ] test  [—] reader  [—] writer
    # [ ] NOT_VALID           [x] impl  [ ] docstring  [ ] test  [—] reader  [—] writer
    # [ ] VALID               [x] impl  [ ] docstring  [ ] test  [—] reader  [—] writer

    # atp.EnumerationValue=0
    NOT_AVAILABLE = "notAvailable"

    # atp.EnumerationValue=1
    NOT_DEFINED = "notDefined"

    # atp.EnumerationValue=2
    NOT_VALID = "notValid"

    # atp.EnumerationValue=3
    VALID = "valid"

    def __init__(self):
        super().__init__(
            [
                ScaleConstrValidityEnum.NOT_AVAILABLE,
                ScaleConstrValidityEnum.NOT_DEFINED,
                ScaleConstrValidityEnum.NOT_VALID,
                ScaleConstrValidityEnum.VALID,
            ]
        )


class ScaleConstr(ARObject):
    """
    One particular scale which contributes to the data constraints. This meta-class is marked obsolete in the AUTOSAR template (atp.Status=obsolete).
    """

    # ScaleConstr method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.40
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setShortLabel       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getShortLabel       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperLimit       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getUpperLimit       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValidity         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getValidity         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This element specifies a short name for the scaleConstr. This can for example be used to create more specific messages of a constraint checker. The constraints cannot be associated in the meta-model, therefore shortLabel is somehow a substitute for shortName.
        self.shortLabel: Optional[Identifier] = None

        # This specifies the upper limit of a the scale.
        self.upperLimit: Optional[Limit] = None

        # Specifies if the values defined by the scales are considered to be valid. If the attribute is missing then the default value is "VALID".
        self.validity: Optional[ScaleConstrValidityEnum] = None

    def setShortLabel(self, value: Optional[Identifier]) -> "ScaleConstr":
        """
        This element specifies a short name for the scaleConstr. This can for example be used to create more specific messages of a constraint checker. The constraints cannot be associated in the meta-model, therefore shortLabel is somehow a substitute for shortName.

        A None value is a no-op and does not overwrite an existing shortLabel.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortLabel = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This element specifies a short name for the scaleConstr. This can for example be used to create more specific messages of a constraint checker. The constraints cannot be associated in the meta-model, therefore shortLabel is somehow a substitute for shortName.

        Returns:
            The short label, or None if not set
        """
        return self.shortLabel

    def setUpperLimit(self, value: Optional[Limit]) -> "ScaleConstr":
        """
        This specifies the upper limit of a the scale.

        A None value is a no-op and does not overwrite an existing upperLimit.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.upperLimit = value
        return self

    def getUpperLimit(self) -> Optional[Limit]:
        """
        This specifies the upper limit of a the scale.

        Returns:
            The upper limit, or None if not set
        """
        return self.upperLimit

    def setValidity(self, value: Optional[ScaleConstrValidityEnum]) -> "ScaleConstr":
        """
        Specifies if the values defined by the scales are considered to be valid. If the attribute is missing then the default value is "VALID".

        A None value is a no-op and does not overwrite an existing validity.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.validity = value
        return self

    def getValidity(self) -> Optional[ScaleConstrValidityEnum]:
        """
        Specifies if the values defined by the scales are considered to be valid. If the attribute is missing then the default value is "VALID".

        Returns:
            The validity, or None if not set
        """
        return self.validity


class PhysConstrs(ARObject):
    """
    This meta-class represents the ability to express physical constraints. Therefore it has (in opposite to InternalConstrs) a reference to a Unit.

    Base: ARObject
    """

    # PhysConstrs method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.84, p.406
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setLowerLimit             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getLowerLimit             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxDiff                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getMaxDiff                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxGradient            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getMaxGradient            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMonotony               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getMonotony               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addScaleConstr            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getScaleConstrs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnitRef                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getUnitRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperLimit             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getUpperLimit             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This specifies the lower limit of the constraint.
        self.lowerLimit: Optional[Limit] = None

        # Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis.
        self.maxDiff: Optional[Numerical] = None

        # This element specifies the maximum slope that may be used in curves and maps.
        self.maxGradient: Optional[Numerical] = None

        # This specifies the monotony constraints on the data object. Note that this applies only to curves and maps.
        self.monotony: Optional[MonotonyEnum] = None

        # This is one particular scale which contributes to the data constraints.
        self.scaleConstrs: List[ScaleConstr] = []

        # This is the unit to which the physical constraints relate to. In particular, it is the physical unit of the specified limits.
        self.unitRef: Optional[RefType] = None

        # This specifies the upper limit of the constraint.
        self.upperLimit: Optional[Limit] = None

    def setLowerLimit(self, value: Optional[Limit]) -> "PhysConstrs":
        """
        This specifies the lower limit of the constraint.

        A None value is a no-op and does not overwrite an existing lowerLimit.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.lowerLimit = value
        return self

    def getLowerLimit(self) -> Optional[Limit]:
        """
        This specifies the lower limit of the constraint.

        Returns:
            The lower limit, or None if not set
        """
        return self.lowerLimit

    def setMaxDiff(self, value: Optional[Numerical]) -> "PhysConstrs":
        """
        Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis.

        A None value is a no-op and does not overwrite an existing maxDiff.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxDiff = value
        return self

    def getMaxDiff(self) -> Optional[Numerical]:
        """
        Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis.

        Returns:
            The max difference, or None if not set
        """
        return self.maxDiff

    def setMaxGradient(self, value: Optional[Numerical]) -> "PhysConstrs":
        """
        This element specifies the maximum slope that may be used in curves and maps.

        A None value is a no-op and does not overwrite an existing maxGradient.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxGradient = value
        return self

    def getMaxGradient(self) -> Optional[Numerical]:
        """
        This element specifies the maximum slope that may be used in curves and maps.

        Returns:
            The max gradient, or None if not set
        """
        return self.maxGradient

    def setMonotony(self, value: Optional[MonotonyEnum]) -> "PhysConstrs":
        """
        This specifies the monotony constraints on the data object. Note that this applies only to curves and maps.

        A None value is a no-op and does not overwrite an existing monotony.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.monotony = value
        return self

    def getMonotony(self) -> Optional[MonotonyEnum]:
        """
        This specifies the monotony constraints on the data object. Note that this applies only to curves and maps.

        Returns:
            The monotony, or None if not set
        """
        return self.monotony

    def addScaleConstr(self, value: Optional[ScaleConstr]) -> "PhysConstrs":
        """
        This is one particular scale which contributes to the data constraints.

        A None value is a no-op and does not add a scaleConstr.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.scaleConstrs.append(value)
        return self

    def getScaleConstrs(self) -> List[ScaleConstr]:
        """
        This is one particular scale which contributes to the data constraints.

        Returns:
            The ordered list of scale constraints
        """
        return self.scaleConstrs

    def setUnitRef(self, value: Optional[RefType]) -> "PhysConstrs":
        """
        This is the unit to which the physical constraints relate to. In particular, it is the physical unit of the specified limits.

        A None value is a no-op and does not overwrite an existing unitRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.unitRef = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """
        This is the unit to which the physical constraints relate to. In particular, it is the physical unit of the specified limits.

        Returns:
            The unit reference, or None if not set
        """
        return self.unitRef

    def setUpperLimit(self, value: Optional[Limit]) -> "PhysConstrs":
        """
        This specifies the upper limit of the constraint.

        A None value is a no-op and does not overwrite an existing upperLimit.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.upperLimit = value
        return self

    def getUpperLimit(self) -> Optional[Limit]:
        """
        This specifies the upper limit of the constraint.

        Returns:
            The upper limit, or None if not set
        """
        return self.upperLimit


class DataConstrRule(ARObject):
    """
    Represents a single data constraint rule with internal and physical constraints.
    Base: ARObject
    """

    # DataConstrRule method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.constrLevel: ARNumerical = None
        self.internalConstrs: InternalConstrs = None
        self.physConstrs: PhysConstrs = None


class DataConstr(AtpBlueprintable):
    """
    Represents data constraints with multiple rules.
    Base: AtpBlueprintable
    """

    # DataConstr method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addDataConstrRule            [x] impl  [ ] docstring  [ ] test
    # [ ] getDataConstrRules           [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.data_constr_rule: List[DataConstrRule] = []

    def addDataConstrRule(self, rule: DataConstrRule):
        self.data_constr_rule.append(rule)

    def getDataConstrRules(self) -> List[DataConstrRule]:
        return self.data_constr_rule
