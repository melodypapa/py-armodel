from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger


class DiagnosticLogicalOperatorEnum(AREnum):
    """Logical AND and OR operation (&&, ||)"""

    # DiagnosticLogicalOperatorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.37, p.81
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

    def setNrcValue(self, value: Optional[PositiveInteger]):
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

    def setOp(self, value: Optional[DiagnosticLogicalOperatorEnum]):
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

    def addPart(self, part: Optional[DiagnosticEnvConditionFormulaPart]):
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
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.44, p.83
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
