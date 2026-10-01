from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, RefType


class DiagnosticLogicalOperatorEnum(AREnum):
    """Logical AND and OR operation (&&, ||)"""

    # DiagnosticLogicalOperatorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.37, p.80
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DiagnosticEnvConditionFormula.op
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Logical AND Tags: atp.EnumerationLiteralIndex=0
    LOGICAL_AND = "LOGICAL-AND"

    # Logical OR Tags: atp.EnumerationLiteralIndex=1
    LOGICAL_OR = "LOGICAL-OR"

    def __init__(self):
        super().__init__(
            (
                DiagnosticLogicalOperatorEnum.LOGICAL_AND,
                DiagnosticLogicalOperatorEnum.LOGICAL_OR,
            )
        )


class DiagnosticCompareTypeEnum(AREnum):
    """Enumeration for the type of a comparison of values usually expressed by the following operators: ==, !=, <, <=, >, >="""

    # DiagnosticCompareTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.40, p.83
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DiagnosticEnvCompareCondition.compareType
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # equal Tags: atp.EnumerationLiteralIndex=0
    IS_EQUAL = "isEqual"

    # greater than or equal Tags: atp.EnumerationLiteralIndex=5
    IS_GREATER_OR_EQUAL = "isGreaterOrEqual"

    # greater than Tags: atp.EnumerationLiteralIndex=4
    IS_GREATER_THAN = "isGreaterThan"

    # less than or equal Tags: atp.EnumerationLiteralIndex=3
    IS_LESS_OR_EQUAL = "isLessOrEqual"

    # less than Tags: atp.EnumerationLiteralIndex=2
    IS_LESS_THAN = "isLessThan"

    # not equal Tags: atp.EnumerationLiteralIndex=1
    IS_NOT_EQUAL = "isNotEqual"

    def __init__(self):
        super().__init__(
            (
                DiagnosticCompareTypeEnum.IS_EQUAL,
                DiagnosticCompareTypeEnum.IS_GREATER_OR_EQUAL,
                DiagnosticCompareTypeEnum.IS_GREATER_THAN,
                DiagnosticCompareTypeEnum.IS_LESS_OR_EQUAL,
                DiagnosticCompareTypeEnum.IS_LESS_THAN,
                DiagnosticCompareTypeEnum.IS_NOT_EQUAL,
            )
        )


class DiagnosticEnvConditionFormulaPart(ARObject, ABC):
    """A DiagnosticEnvConditionFormulaPart can either be a atomic condition, e.g. a DiagnosticEnvCompareCondition, or a DiagnosticEnvConditionFormula, again, which allows arbitrary nesting."""

    # DiagnosticEnvConditionFormulaPart method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.38, p.81
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is DiagnosticEnvConditionFormulaPart:
            raise TypeError("DiagnosticEnvConditionFormulaPart is an abstract class.")
        super().__init__()


class DiagnosticEnvCompareCondition(DiagnosticEnvConditionFormulaPart, ABC):
    """
    DiagnosticCompareConditions are atomic conditions. They are based on the idea of a comparison at runtime of some variable data with something constant. The type of the comparison (==, !=, <, <=, ...) is specified in DiagnosticCompareCondition.compareType.
    """

    # DiagnosticEnvCompareCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.39, p.82
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompareType    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompareType    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is DiagnosticEnvCompareCondition:
            raise TypeError("DiagnosticEnvCompareCondition is an abstract class.")

        super().__init__()

        # This attributes represents the concrete type of the comparison.
        self.compareType: Optional[DiagnosticCompareTypeEnum] = None

    def getCompareType(self) -> Optional[DiagnosticCompareTypeEnum]:
        """
        This attributes represents the concrete type of the comparison.
        """
        return self.compareType

    def setCompareType(self, value: Optional[DiagnosticCompareTypeEnum]) -> DiagnosticEnvCompareCondition:
        """
        This attributes represents the concrete type of the comparison.
        A None value is a no-op and does not overwrite an existing compareType.
        """
        if value is not None:
            self.compareType = value
        return self


class DiagnosticEnvConditionFormula(DiagnosticEnvConditionFormulaPart):
    """A DiagnosticEnvConditionFormula embodies the computation instruction that is to be evaluated at runtime to determine if the DiagnosticEnvironmentalCondition is currently present (i.e. the formula is evaluated to true) or not (otherwise). The formula itself consists of parts which are combined by the logical operations specified by DiagnosticEnvConditionFormula.op. If a diagnostic functionality cannot be executed because an environmental condition fails then the diagnostic stack shall send a negative response code (NRC) back to the client. The value of the NRC is directly related to the specific formula and is therefore formalized in the attribute DiagnosticEnvConditionFormula.nrcValue."""

    # DiagnosticEnvConditionFormula method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.36, p.80
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNrcValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNrcValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOp           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOp           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParts        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPart         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute represents the concrete NRC value that shall be returned if the condition fails.
        self.nrcValue: Optional[PositiveInteger] = None

        # This attribute represents the concrete operator (supported operators: and, or) of the condition formula.
        self.op: Optional[DiagnosticLogicalOperatorEnum] = None

        # This aggregation represents the collection of formula parts that can be combined by logical operators.
        self.parts: List[DiagnosticEnvConditionFormulaPart] = []

    def getNrcValue(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the concrete NRC value that shall be returned if the condition fails.
        """
        return self.nrcValue

    def setNrcValue(self, value: Optional[PositiveInteger]) -> DiagnosticEnvConditionFormula:
        """
        This attribute represents the concrete NRC value that shall be returned if the condition fails.

        A None value is a no-op and does not overwrite an existing nrcValue.
        """
        if value is not None:
            self.nrcValue = value
        return self

    def getOp(self) -> Optional[DiagnosticLogicalOperatorEnum]:
        """
        This attribute represents the concrete operator (supported operators: and, or) of the condition formula.
        """
        return self.op

    def setOp(self, value: Optional[DiagnosticLogicalOperatorEnum]) -> DiagnosticEnvConditionFormula:
        """
        This attribute represents the concrete operator (supported operators: and, or) of the condition formula.

        A None value is a no-op and does not overwrite an existing op.
        """
        if value is not None:
            self.op = value
        return self

    def getParts(self) -> List[DiagnosticEnvConditionFormulaPart]:
        """
        This aggregation represents the collection of formula parts that can be combined by logical operators.
        """
        return self.parts

    def addPart(self, part: Optional[DiagnosticEnvConditionFormulaPart]) -> DiagnosticEnvConditionFormula:
        """
        This aggregation represents the collection of formula parts that can be combined by logical operators.

        A None value is a no-op and does not extend the parts list.
        """
        if part is not None:
            self.parts.append(part)
        return self


class DiagnosticEnvModeElement(Referrable, ABC):
    """All ModeDeclarations that are referenced in a DiagnosticEnvModeCondition shall be defined as a DiagnosticEnvModeElement of this DiagnosticEnvironmentalCondition. This concept keeps the ARXML clean: It avoids that the DiagnosticEnvConditionFormula is cluttered by lengthy InstanceRef definitions. Furthermore, it allows that an InstanceRef only needs to be defined once and can be used multiple times in the different DiagnosticEnvModeConditions."""

    # DiagnosticEnvModeElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.44, p.89
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticEnvModeElement:
            raise TypeError("DiagnosticEnvModeElement is an abstract class.")
        super().__init__(parent, short_name)


class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """The meta-class DiagnosticEnvironmentalCondition formalizes the idea of a condition which is evaluated during runtime of the ECU by looking at "environmental" states (e.g. one such condition is that the vehicle is not driving, i.e. vehicle speed == 0). Tags: atp.recommendedPackage=DiagnosticEnvironmentalConditions"""

    # DiagnosticEnvironmentalCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.35, p.79
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFormula        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFormula        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeElements   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11  (XSD MODE-ELEMENTS choice alternatives are the concrete subclasses — not in src, Pending 16.4)
    # [x] addModeElement    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11  (ditto)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the formula part of the DiagnosticEnvironmentalCondition.
        self.formula: Optional[DiagnosticEnvConditionFormula] = None

        # This aggregation contains a representation of ModeDeclarations in the context of a DiagnosticEnvironmentalCondition.
        self.modeElements: List[DiagnosticEnvModeElement] = []

    def getFormula(self) -> Optional[DiagnosticEnvConditionFormula]:
        """
        This attribute represents the formula part of the DiagnosticEnvironmentalCondition.
        """
        return self.formula

    def setFormula(self, value: Optional[DiagnosticEnvConditionFormula]):
        """
        This attribute represents the formula part of the DiagnosticEnvironmentalCondition.

        A None value is a no-op and does not overwrite an existing formula.
        """
        if value is not None:
            self.formula = value
        return self

    def getModeElements(self) -> List[DiagnosticEnvModeElement]:
        """
        This aggregation contains a representation of ModeDeclarations in the context of a DiagnosticEnvironmentalCondition.
        """
        return self.modeElements

    def addModeElement(self, mode_element: Optional[DiagnosticEnvModeElement]):
        """
        This aggregation contains a representation of ModeDeclarations in the context of a DiagnosticEnvironmentalCondition.

        A None value is a no-op and does not extend the modeElements list.
        """
        if mode_element is not None:
            self.modeElements.append(mode_element)
        return self


class DiagnosticEnvBswModeElement(DiagnosticEnvModeElement):
    pass


class DiagnosticEnvDataCondition(DiagnosticEnvCompareCondition):
    """
    A DiagnosticEnvDataCondition is an atomic condition that compares the current value of the referenced DiagnosticDataElement with a constant value defined by the ValueSpecification. All compareTypes are supported.

    [constr_1802] Existence of DiagnosticEnvDataCondition.compareValue: For each DiagnosticEnvDataCondition, that attribute compareValue shall exist at the time when the DEXT is complete.

    [constr_1803] Existence of DiagnosticEnvDataCondition.dataElement: For each DiagnosticEnvDataCondition, that attribute dataElement shall exist at the time when the DEXT is complete.
    """

    # DiagnosticEnvDataCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.41, p.84
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompareValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompareValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElementRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute represents a fixed compare value taken to evaluate the compare condition.
        self.compareValue: Optional[ValueSpecification] = None

        # This reference represents the related diagnostic data element.
        self.dataElementRef: Optional[RefType] = None

    def getCompareValue(self) -> Optional[ValueSpecification]:
        """
        This attribute represents a fixed compare value taken to evaluate the compare condition.
        """
        return self.compareValue

    def setCompareValue(self, value: Optional[ValueSpecification]):
        """
        This attribute represents a fixed compare value taken to evaluate the compare condition.

        A None value is a no-op and does not overwrite an existing compareValue.
        """
        if value is not None:
            self.compareValue = value
        return self

    def getDataElementRef(self) -> Optional[RefType]:
        """
        This reference represents the related diagnostic data element.
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]):
        """
        This reference represents the related diagnostic data element.

        A None value is a no-op and does not overwrite an existing dataElementRef.
        """
        if value is not None:
            self.dataElementRef = value
        return self


class DiagnosticEnvDataElementCondition(DiagnosticEnvCompareCondition):
    pass


class DiagnosticEnvSwcModeElement(DiagnosticEnvModeElement):
    pass


from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification  # noqa: E402
