from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

__all__ = ["BlueprintGenerator"]


class BlueprintGenerator(ARObject):
    """This class express the Extended Language to generate blueprint derivates in complex descriptions."""

    # BlueprintGenerator method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.12, pp.424-425 (R23-11)
    # (appendix E caption-shift: the table body renders ABOVE the caption — main
    # fragment incl. the expression row on p.424, introduction continuation + caption
    # on p.425; no numeric main table exists in R23-11 and the R4.3.1 corpus has no
    # table for this class. XSD 00052 group BLUEPRINT-GENERATOR line 9083: sequence
    # INTRODUCTION (offset 10) -> EXPRESSION (offset 20); complexType line 9105
    # composes AR-OBJECT group + own group. Reader: readBlueprintGenerator dispatched
    # from readVariationPoint via FORMAL-BLUEPRINT-GENERATOR; writer: the matching
    # writeBlueprintGenerator from writeVariationPoint.)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getExpression     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExpression     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIntroduction   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents a formal term in the expression based on the extended language.
        self.expression: Optional[VerbatimString] = None

        # This represents a description that documents how the blueprint generator shall be resolved when deriving objects from blueprints.
        self.introduction: Optional[DocumentationBlock] = None

    def getExpression(self) -> Optional[VerbatimString]:
        """This represents a formal term in the expression based on the extended language."""
        return self.expression

    def setExpression(self, value: Optional[VerbatimString]) -> "BlueprintGenerator":
        """This represents a formal term in the expression based on the extended language. A None value is a no-op and does not overwrite an existing expression."""
        if value is not None:
            self.expression = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """This represents a description that documents how the blueprint generator shall be resolved when deriving objects from blueprints."""
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> "BlueprintGenerator":
        """This represents a description that documents how the blueprint generator shall be resolved when deriving objects from blueprints. A None value is a no-op and does not overwrite an existing introduction."""
        if value is not None:
            self.introduction = value
        return self
