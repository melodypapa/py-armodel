from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, String
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable

if TYPE_CHECKING:
    from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName


class PrmCharContents(ARObject, ABC):
    """
    This is the contents of the parameter.
    """

    # PrmCharContents method parity checklist:
    # Spec: AUTOSAR_00052.xsd, group PRM-CHAR-CONTENTS l.93805 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is PrmCharContents:
            raise TypeError("PrmCharContents is an abstract class and cannot be instantiated directly")
        super().__init__()


class PrmCharNumericalValue(ARObject, ABC):
    """
    This metaclass represents a numercial parameter characteristics.
    """

    # PrmCharNumericalValue method parity checklist:
    # Spec: AUTOSAR_00052.xsd, group PRM-CHAR-NUMERICAL-VALUE l.93890 (XSD-only; group-only in both XSDs — no complexType; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is PrmCharNumericalValue:
            raise TypeError("PrmCharNumericalValue is an abstract class and cannot be instantiated directly")
        super().__init__()


class PrmCharAbsTol(PrmCharNumericalValue):
    """
    The parameter is specified as ablolute value with a tolerance.
    """

    # PrmCharAbsTol method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType PRM-CHAR-ABS-TOL l.93791, group l.93769 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAbs    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAbs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTol    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTol    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represnts the absolute value of the parameter.
        self.abs: Optional[Numerical] = None

        # This represnts the tolerance of the parameter in the same units as the paramter: E.g. Tmperature= 50 +- 0.5 grad.
        self.tol: Optional[Numerical] = None

    def setAbs(self, value: Optional[Numerical]) -> PrmCharAbsTol:
        """
        This represnts the absolute value of the parameter.

        A None value is a no-op and does not overwrite an existing abs.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.abs = value
        return self

    def getAbs(self) -> Optional[Numerical]:
        """
        This represnts the absolute value of the parameter.

        Returns:
            The absolute value of the parameter
        """
        return self.abs

    def setTol(self, value: Optional[Numerical]) -> PrmCharAbsTol:
        """
        This represnts the tolerance of the parameter in the same units as the paramter: E.g. Tmperature= 50 +- 0.5 grad.

        A None value is a no-op and does not overwrite an existing tol.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.tol = value
        return self

    def getTol(self) -> Optional[Numerical]:
        """
        This represnts the tolerance of the parameter in the same units as the paramter: E.g. Tmperature= 50 +- 0.5 grad.

        Returns:
            The tolerance of the parameter in the same units as the paramter
        """
        return self.tol


class PrmCharMinTypMax(PrmCharNumericalValue):
    """
    This metaclass represents the characteristics of a parameter as minimal, typical maximum value.
    """

    # PrmCharMinTypMax method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType PRM-CHAR-MIN-TYP-MAX l.93842, group l.93814 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setMin    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMin    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTyp    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTyp    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMax    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMax    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represnts the minimum value of the parameter.
        self.min: Optional[Numerical] = None

        # This represnts the typical value of the parameter.
        self.typ: Optional[Numerical] = None

        # This represnts the maximum value of the parameter.
        self.max: Optional[Numerical] = None

    def setMin(self, value: Optional[Numerical]) -> PrmCharMinTypMax:
        """
        This represnts the minimum value of the parameter.

        A None value is a no-op and does not overwrite an existing min.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.min = value
        return self

    def getMin(self) -> Optional[Numerical]:
        """
        This represnts the minimum value of the parameter.

        Returns:
            The minimum value of the parameter
        """
        return self.min

    def setTyp(self, value: Optional[Numerical]) -> PrmCharMinTypMax:
        """
        This represnts the typical value of the parameter.

        A None value is a no-op and does not overwrite an existing typ.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.typ = value
        return self

    def getTyp(self) -> Optional[Numerical]:
        """
        This represnts the typical value of the parameter.

        Returns:
            The typical value of the parameter
        """
        return self.typ

    def setMax(self, value: Optional[Numerical]) -> PrmCharMinTypMax:
        """
        This represnts the maximum value of the parameter.

        A None value is a no-op and does not overwrite an existing max.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.max = value
        return self

    def getMax(self) -> Optional[Numerical]:
        """
        This represnts the maximum value of the parameter.

        Returns:
            The maximum value of the parameter
        """
        return self.max


class PrmCharNumericalContents(PrmCharContents):
    """
    This metaclass represents the fact that it is a numerical parameter.
    """

    # PrmCharNumericalContents method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType PRM-CHAR-NUMERICAL-CONTENTS l.93876, group l.93856 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAbsTol       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAbsTol       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinTypMax    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinTypMax    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrmUnit      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrmUnit      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This metaclass represents the fact that it is a numerical parameter. (choice member: ABS-TOL | MIN-TYP-MAX)
        self.absTol: Optional[PrmCharAbsTol] = None

        # This metaclass represents the fact that it is a numerical parameter. (choice member: ABS-TOL | MIN-TYP-MAX)
        self.minTypMax: Optional[PrmCharMinTypMax] = None

        # This is the measurement unit. Note that due to the fact that Prm is also available outside of MSRSW / AUTOSAR, this is not a formal reference  to a unit.
        self.prmUnit: Optional[SingleLanguageUnitNames] = None

    def setAbsTol(self, value: Optional[PrmCharAbsTol]) -> PrmCharNumericalContents:
        """
        This metaclass represents the fact that it is a numerical parameter.

        A None value is a no-op and does not overwrite an existing absTol.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.absTol = value
        return self

    def getAbsTol(self) -> Optional[PrmCharAbsTol]:
        """
        This metaclass represents the fact that it is a numerical parameter.

        Returns:
            The fact that it is a numerical parameter
        """
        return self.absTol

    def setMinTypMax(self, value: Optional[PrmCharMinTypMax]) -> PrmCharNumericalContents:
        """
        This metaclass represents the fact that it is a numerical parameter.

        A None value is a no-op and does not overwrite an existing minTypMax.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minTypMax = value
        return self

    def getMinTypMax(self) -> Optional[PrmCharMinTypMax]:
        """
        This metaclass represents the fact that it is a numerical parameter.

        Returns:
            The fact that it is a numerical parameter
        """
        return self.minTypMax

    def setPrmUnit(self, value: Optional[SingleLanguageUnitNames]) -> PrmCharNumericalContents:
        """
        This is the measurement unit. Note that due to the fact that Prm is also available outside of MSRSW / AUTOSAR, this is not a formal reference  to a unit.

        A None value is a no-op and does not overwrite an existing prmUnit.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.prmUnit = value
        return self

    def getPrmUnit(self) -> Optional[SingleLanguageUnitNames]:
        """
        This is the measurement unit. Note that due to the fact that Prm is also available outside of MSRSW / AUTOSAR, this is not a formal reference  to a unit.

        Returns:
            The measurement unit
        """
        return self.prmUnit


class PrmCharTextualContents(PrmCharContents):
    """
    This metaclass represents the fact that it is a textual parameter.
    """

    # PrmCharTextualContents method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType PRM-CHAR-TEXTUAL-CONTENTS l.93915, group l.93899 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setText   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getText   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the value of a textual parameter
        self.text: Optional[String] = None

    def setText(self, value: Optional[String]) -> PrmCharTextualContents:
        """
        This is the value of a textual parameter

        A None value is a no-op and does not overwrite an existing text.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.text = value
        return self

    def getText(self) -> Optional[String]:
        """
        This is the value of a textual parameter

        Returns:
            The value of a textual parameter
        """
        return self.text


class PrmChar(ARObject):
    """
    This metaclass represents the ability to express the characteristics of one particular parameter. It can be exressed as numerical or as text parameter (provided as subclasses of PrmCharContents)
    """

    # PrmChar method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType PRM-CHAR l.93756, group l.93730 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setCond                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCond                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNumericalContents   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNumericalContents   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTextualContents     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTextualContents     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemark              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRemark              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the particular conditions under which the parameter characteristic is valid.
        self.cond: Optional[DocumentationBlock] = None

        # This metaclass represents the fact that it is a numerical parameter. (choice member: PRM-CHAR-NUMERICAL-CONTENTS | PRM-CHAR-TEXTUAL-CONTENTS)
        self.numericalContents: Optional[PrmCharNumericalContents] = None

        # This metaclass represents the fact that it is a textual parameter. (choice member: PRM-CHAR-NUMERICAL-CONTENTS | PRM-CHAR-TEXTUAL-CONTENTS)
        self.textualContents: Optional[PrmCharTextualContents] = None

        # This represents further remarks about the particular parameter characteristics.
        self.remark: Optional[DocumentationBlock] = None

    def setCond(self, value: Optional[DocumentationBlock]) -> PrmChar:
        """
        This represents the particular conditions under which the parameter characteristic is valid.

        A None value is a no-op and does not overwrite an existing cond.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.cond = value
        return self

    def getCond(self) -> Optional[DocumentationBlock]:
        """
        This represents the particular conditions under which the parameter characteristic is valid.

        Returns:
            The particular conditions under which the parameter characteristic is valid
        """
        return self.cond

    def setNumericalContents(self, value: Optional[PrmCharNumericalContents]) -> PrmChar:
        """
        This metaclass represents the fact that it is a numerical parameter.

        A None value is a no-op and does not overwrite an existing numericalContents.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.numericalContents = value
        return self

    def getNumericalContents(self) -> Optional[PrmCharNumericalContents]:
        """
        This metaclass represents the fact that it is a numerical parameter.

        Returns:
            The fact that it is a numerical parameter
        """
        return self.numericalContents

    def setTextualContents(self, value: Optional[PrmCharTextualContents]) -> PrmChar:
        """
        This metaclass represents the fact that it is a textual parameter.

        A None value is a no-op and does not overwrite an existing textualContents.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.textualContents = value
        return self

    def getTextualContents(self) -> Optional[PrmCharTextualContents]:
        """
        This metaclass represents the fact that it is a textual parameter.

        Returns:
            The fact that it is a textual parameter
        """
        return self.textualContents

    def setRemark(self, value: Optional[DocumentationBlock]) -> PrmChar:
        """
        This represents further remarks about the particular parameter characteristics.

        A None value is a no-op and does not overwrite an existing remark.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.remark = value
        return self

    def getRemark(self) -> Optional[DocumentationBlock]:
        """
        This represents further remarks about the particular parameter characteristics.

        Returns:
            The further remarks about the particular parameter characteristics
        """
        return self.remark


class GeneralParameter(Identifiable):
    """
    This represents a parameter in general e.g. an entry in a data sheet.
    """

    # GeneralParameter method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType GENERAL-PARAMETER l.63790, group l.63774 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd (2026-09-28, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addPrmChar      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrmChars     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the characteristics of one parameter under one particular condition.
        self.prmChar: List[PrmChar] = []

    def addPrmChar(self, value: Optional[PrmChar]) -> GeneralParameter:
        """
        This represents the characteristics of one parameter under one particular condition.

        A None value is a no-op and does not append anything.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.prmChar.append(value)
        return self

    def getPrmChars(self) -> List[PrmChar]:
        """
        This represents the characteristics of one parameter under one particular condition.

        Returns:
            The characteristics of one parameter under one particular condition
        """
        return self.prmChar


class Prms(Paginateable):
    """
    This metaclass represents the ability to specify a parameter table. It can be used e.g. to specify parameter tables in a data sheet.
    """

    # Prms method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.74, p.339 (R23-11; markdown render loses the meta rows —
    #       Note/Base/label verified against the R4.3.1 reproduction Table 8.75, p.305, row-identical)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setLabel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLabel     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createPrm    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPrm       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrms      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the caption of the parameter table.
        self.label: Optional[MultilanguageLongName] = None

        # This represents one particular parameter in the table.
        self.prm: List[GeneralParameter] = []

    def setLabel(self, value: Optional[MultilanguageLongName]) -> Prms:
        """
        This represents the caption of the parameter table.

        A None value is a no-op and does not overwrite an existing label.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.label = value
        return self

    def getLabel(self) -> Optional[MultilanguageLongName]:
        """
        This represents the caption of the parameter table.

        Returns:
            The caption of the parameter table
        """
        return self.label

    def createPrm(self, short_name: str) -> GeneralParameter:
        """
        This represents one particular parameter in the table.

        Returns:
            The created particular parameter in the table
        """
        prm = GeneralParameter(self, short_name)
        self.addPrm(prm)
        return prm

    def addPrm(self, value: Optional[GeneralParameter]) -> Prms:
        """
        This represents one particular parameter in the table.

        A None value is a no-op and does not append anything.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.prm.append(value)
        return self

    def getPrms(self) -> List[GeneralParameter]:
        """
        This represents one particular parameter in the table.

        Returns:
            The particular parameters in the table
        """
        return self.prm
