from __future__ import annotations

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
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class InternalConstrs(ARObject):
    """
    This meta-class represents the ability to express internal constraints.
    """

    # InternalConstrs method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.85, p.407
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLowerLimit           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLowerLimit           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxDiff              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxDiff              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxGradient          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxGradient          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMonotony             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMonotony             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addScaleConstr          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getScaleConstrs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getUpperLimit           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperLimit           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This specifies the lower limit of the constraint.
        self.lowerLimit: Optional[Limit] = None

        # Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis.
        self.maxDiff: Optional[Numerical] = None

        # This element specifies the maximum slope that may be used in maps and curves.
        self.maxGradient: Optional[Numerical] = None

        # This element specifies the monotony characteristics of the current internal or physical limits. The following table shows the monotony characteristics which are to be filled through the corresponding values. If the element has no contents or if it is omitted, "no Monotony" is the default content.
        self.monotony: Optional[MonotonyEnum] = None

        # This is one particular scale which contributes to the data constraints.
        self.scaleConstrs: List[ScaleConstr] = []

        # This specifies the upper limit defined by the constraint.
        self.upperLimit: Optional[Limit] = None

    def getLowerLimit(self) -> Optional[Limit]:
        """
        This specifies the lower limit of the constraint.
        """
        return self.lowerLimit

    def setLowerLimit(self, value: Optional[Limit]) -> "InternalConstrs":
        """
        This specifies the lower limit of the constraint. A None value is a no-op and does not overwrite an existing lowerLimit.
        """
        if value is not None:
            self.lowerLimit = value
        return self

    def getMaxDiff(self) -> Optional[Numerical]:
        """
        Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis.
        """
        return self.maxDiff

    def setMaxDiff(self, value: Optional[Numerical]) -> "InternalConstrs":
        """
        Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis. A None value is a no-op and does not overwrite an existing maxDiff.
        """
        if value is not None:
            self.maxDiff = value
        return self

    def getMaxGradient(self) -> Optional[Numerical]:
        """
        This element specifies the maximum slope that may be used in maps and curves.
        """
        return self.maxGradient

    def setMaxGradient(self, value: Optional[Numerical]) -> "InternalConstrs":
        """
        This element specifies the maximum slope that may be used in maps and curves. A None value is a no-op and does not overwrite an existing maxGradient.
        """
        if value is not None:
            self.maxGradient = value
        return self

    def getMonotony(self) -> Optional[MonotonyEnum]:
        """
        This element specifies the monotony characteristics of the current internal or physical limits. The following table shows the monotony characteristics which are to be filled through the corresponding values. If the element has no contents or if it is omitted, "no Monotony" is the default content.
        """
        return self.monotony

    def setMonotony(self, value: Optional[MonotonyEnum]) -> "InternalConstrs":
        """
        This element specifies the monotony characteristics of the current internal or physical limits. The following table shows the monotony characteristics which are to be filled through the corresponding values. If the element has no contents or if it is omitted, "no Monotony" is the default content. A None value is a no-op and does not overwrite an existing monotony.
        """
        if value is not None:
            self.monotony = value
        return self

    def addScaleConstr(self, value: Optional[ScaleConstr]) -> "InternalConstrs":
        """
        This is one particular scale which contributes to the data constraints. A None value is a no-op and does not add a scaleConstr.
        """
        if value is not None:
            self.scaleConstrs.append(value)
        return self

    def getScaleConstrs(self) -> List[ScaleConstr]:
        """
        This is one particular scale which contributes to the data constraints.
        """
        return self.scaleConstrs

    def getUpperLimit(self) -> Optional[Limit]:
        """
        This specifies the upper limit defined by the constraint.
        """
        return self.upperLimit

    def setUpperLimit(self, value: Optional[Limit]) -> "InternalConstrs":
        """
        This specifies the upper limit defined by the constraint. A None value is a no-op and does not overwrite an existing upperLimit.
        """
        if value is not None:
            self.upperLimit = value
        return self


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
    This meta-class represents the ability to specify constraints as a list of intervals (called scales).
    """

    # ScaleConstr method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.39/E.40, p.1003
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDesc             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLowerLimit       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLowerLimit       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShortLabel       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setShortLabel       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpperLimit       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperLimit       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValidity         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValidity         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # <desc> represents a general but brief description of the object in question.
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

        # This specifies the lower limit of the scale.
        self.lowerLimit: Optional[Limit] = None

        # This element specifies a short name for the scaleConstr. This can for example be used to create more specific messages of a constraint checker. The constraints cannot be associated in the meta-model, therefore shortLabel is somehow a substitute for shortName.
        self.shortLabel: Optional[Identifier] = None

        # This specifies the upper limit of a the scale.
        self.upperLimit: Optional[Limit] = None

        # Specifies if the values defined by the scales are considered to be valid. If the attribute is missing then the default value is "VALID".
        self.validity: Optional[ScaleConstrValidityEnum] = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        <desc> represents a general but brief description of the object in question.
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "ScaleConstr":
        """
        <desc> represents a general but brief description of the object in question. A None value is a no-op and does not overwrite an existing desc.
        """
        if value is not None:
            self.desc = value
        return self

    def getLowerLimit(self) -> Optional[Limit]:
        """
        This specifies the lower limit of the scale.
        """
        return self.lowerLimit

    def setLowerLimit(self, value: Optional[Limit]) -> "ScaleConstr":
        """
        This specifies the lower limit of the scale. A None value is a no-op and does not overwrite an existing lowerLimit.
        """
        if value is not None:
            self.lowerLimit = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This element specifies a short name for the scaleConstr. This can for example be used to create more specific messages of a constraint checker. The constraints cannot be associated in the meta-model, therefore shortLabel is somehow a substitute for shortName.
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "ScaleConstr":
        """
        This element specifies a short name for the scaleConstr. This can for example be used to create more specific messages of a constraint checker. The constraints cannot be associated in the meta-model, therefore shortLabel is somehow a substitute for shortName. A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self

    def getUpperLimit(self) -> Optional[Limit]:
        """
        This specifies the upper limit of a the scale.
        """
        return self.upperLimit

    def setUpperLimit(self, value: Optional[Limit]) -> "ScaleConstr":
        """
        This specifies the upper limit of a the scale. A None value is a no-op and does not overwrite an existing upperLimit.
        """
        if value is not None:
            self.upperLimit = value
        return self

    def getValidity(self) -> Optional[ScaleConstrValidityEnum]:
        """
        Specifies if the values defined by the scales are considered to be valid. If the attribute is missing then the default value is "VALID".
        """
        return self.validity

    def setValidity(self, value: Optional[ScaleConstrValidityEnum]) -> "ScaleConstr":
        """
        Specifies if the values defined by the scales are considered to be valid. If the attribute is missing then the default value is "VALID". A None value is a no-op and does not overwrite an existing validity.
        """
        if value is not None:
            self.validity = value
        return self


class PhysConstrs(ARObject):
    """
    This meta-class represents the ability to express physical constraints. Therefore it has (in opposite to InternalConstrs) a reference to a Unit.
    """

    # PhysConstrs method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.84, p.406
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLowerLimit             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLowerLimit             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxDiff                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxDiff                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxGradient            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxGradient            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMonotony               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMonotony               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addScaleConstr            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getScaleConstrs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getUnitRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnitRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpperLimit             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperLimit             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

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

    def getLowerLimit(self) -> Optional[Limit]:
        """
        This specifies the lower limit of the constraint.
        """
        return self.lowerLimit

    def setLowerLimit(self, value: Optional[Limit]) -> "PhysConstrs":
        """
        This specifies the lower limit of the constraint. A None value is a no-op and does not overwrite an existing lowerLimit.
        """
        if value is not None:
            self.lowerLimit = value
        return self

    def getMaxDiff(self) -> Optional[Numerical]:
        """
        Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis.
        """
        return self.maxDiff

    def setMaxDiff(self, value: Optional[Numerical]) -> "PhysConstrs":
        """
        Maximum difference that is permitted between two consecutive values if the constraint is applied to an axis. A None value is a no-op and does not overwrite an existing maxDiff.
        """
        if value is not None:
            self.maxDiff = value
        return self

    def getMaxGradient(self) -> Optional[Numerical]:
        """
        This element specifies the maximum slope that may be used in curves and maps.
        """
        return self.maxGradient

    def setMaxGradient(self, value: Optional[Numerical]) -> "PhysConstrs":
        """
        This element specifies the maximum slope that may be used in curves and maps. A None value is a no-op and does not overwrite an existing maxGradient.
        """
        if value is not None:
            self.maxGradient = value
        return self

    def getMonotony(self) -> Optional[MonotonyEnum]:
        """
        This specifies the monotony constraints on the data object. Note that this applies only to curves and maps.
        """
        return self.monotony

    def setMonotony(self, value: Optional[MonotonyEnum]) -> "PhysConstrs":
        """
        This specifies the monotony constraints on the data object. Note that this applies only to curves and maps. A None value is a no-op and does not overwrite an existing monotony.
        """
        if value is not None:
            self.monotony = value
        return self

    def addScaleConstr(self, value: Optional[ScaleConstr]) -> "PhysConstrs":
        """
        This is one particular scale which contributes to the data constraints. A None value is a no-op and does not add a scaleConstr.
        """
        if value is not None:
            self.scaleConstrs.append(value)
        return self

    def getScaleConstrs(self) -> List[ScaleConstr]:
        """
        This is one particular scale which contributes to the data constraints.
        """
        return self.scaleConstrs

    def getUnitRef(self) -> Optional[RefType]:
        """
        This is the unit to which the physical constraints relate to. In particular, it is the physical unit of the specified limits.
        """
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]) -> "PhysConstrs":
        """
        This is the unit to which the physical constraints relate to. In particular, it is the physical unit of the specified limits. A None value is a no-op and does not overwrite an existing unitRef.
        """
        if value is not None:
            self.unitRef = value
        return self

    def getUpperLimit(self) -> Optional[Limit]:
        """
        This specifies the upper limit of the constraint.
        """
        return self.upperLimit

    def setUpperLimit(self, value: Optional[Limit]) -> "PhysConstrs":
        """
        This specifies the upper limit of the constraint. A None value is a no-op and does not overwrite an existing upperLimit.
        """
        if value is not None:
            self.upperLimit = value
        return self


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
