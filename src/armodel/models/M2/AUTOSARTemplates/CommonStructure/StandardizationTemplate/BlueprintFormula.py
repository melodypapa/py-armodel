from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import SwSystemconstDependentFormula
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim

__all__ = ["BlueprintFormula"]


class BlueprintFormula(SwSystemconstDependentFormula):
    """This class express the extension of the Formula Language to provide formalized blueprint-Value resp. blueprintCondition."""

    # BlueprintFormula method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.16, p.163 (R23-11)
    # (appendix C caption-shift: the table body renders ABOVE the caption on the same
    # page; R4.3.1 reproduction Table D.12 has the same rows. XSD 00052 group
    # BLUEPRINT-FORMULA line 9023: choice ECUC-QUERY-REF (atp.Status="removed" — not
    # modeled, Rule 0015 the PDF wins) / ECUC-REF / VERBATIM; complexType line 9068
    # composes AR-OBJECT + FORMULA-EXPRESSION + SW-SYSTEMCONST-DEPENDENT-FORMULA +
    # own group, mixed="true" (text via the AtpMixedString mixin). The sole consuming
    # element VariationPoint.formalBlueprintCondition (FORMAL-BLUEPRINT-CONDITION, XSD
    # line 130040) is atp.Status="removed" in R23-11 and is deliberately not dispatched
    # by readVariationPoint/writeVariationPoint — reader/writer coverage is the class's
    # own helper pair, pinned at element level (PostBuildVariantCriterionValue precedent).)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEcucRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcucRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVerbatim    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVerbatim    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getMixedString / setMixedString provided by the AtpMixedString mixin (via FormulaExpression) — no spec row (stereotype-inherent)
    # syscRef / syscStringRef accessors inherited from SwSystemconstDependentFormula — covered by that class's checklist

    def __init__(self):
        super().__init__()

        # The EcucDefinitionElement serves as a argument for the formular.
        self.ecucRef: Optional[RefType] = None

        # This represents an informal term in the expression as verbatim text. Note that the result of this is same as formula keyword "undefined".
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def getEcucRef(self) -> Optional[RefType]:
        """The EcucDefinitionElement serves as a argument for the formular."""
        return self.ecucRef

    def setEcucRef(self, value: Optional[RefType]) -> "BlueprintFormula":
        """The EcucDefinitionElement serves as a argument for the formular. A None value is a no-op and does not overwrite an existing ecucRef."""
        if value is not None:
            self.ecucRef = value
        return self

    def getVerbatim(self) -> Optional[MultiLanguageVerbatim]:
        """This represents an informal term in the expression as verbatim text. Note that the result of this is same as formula keyword "undefined"."""
        return self.verbatim

    def setVerbatim(self, value: Optional[MultiLanguageVerbatim]) -> "BlueprintFormula":
        """This represents an informal term in the expression as verbatim text. Note that the result of this is same as formula keyword "undefined". A None value is a no-op and does not overwrite an existing verbatim."""
        if value is not None:
            self.verbatim = value
        return self
