from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

__all__ = ["BlueprintGenerator"]


class BlueprintGenerator(ARObject):
    """
    This class express the Extended Language to generate blueprint derivates in complex
    descriptions.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintGenerator
    Base: ARObject

    Attributes:
        expression (VerbatimString): This represents a formal term in the expression
            based on the extended language. (Multiplicity: 0..1)
        introduction (DocumentationBlock): This represents a description that documents
            how the blueprint generator shall be resolved when deriving objects from
            blueprints. (Multiplicity: 0..1)
    """

    # BlueprintGenerator method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.12, p.424
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getExpression     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExpression     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIntroduction   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIntroduction   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents a formal term in the expression based on the extended language.
        self.expression: Optional[VerbatimString] = None

        # This represents a description that documents how the blueprint generator shall be resolved when deriving objects from blueprints.
        self.introduction: Optional[DocumentationBlock] = None

    def getExpression(self) -> Optional[VerbatimString]:
        """
        This represents a formal term in the expression based on the extended language.
        """
        return self.expression

    def setExpression(self, value: Optional[VerbatimString]) -> "BlueprintGenerator":
        """
        This represents a formal term in the expression based on the extended language. A
        None value is a no-op and does not overwrite an existing expression.
        """
        if value is not None:
            self.expression = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents a description that documents how the blueprint generator shall be
        resolved when deriving objects from blueprints.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> "BlueprintGenerator":
        """
        This represents a description that documents how the blueprint generator shall be
        resolved when deriving objects from blueprints. A None value is a no-op and does
        not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self
