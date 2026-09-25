from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString


class FormulaExpression(ARObject, AtpMixedString, ABC):
    """
    This class represents the syntax of the formula language. The class is modeled as an abstract class in order to be specialized into particular use cases. For each use case the referable objects might be specified in the specialization.
    """

    # FormulaExpression method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table C.5, pp.73-74 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element; getMixedString/setMixedString inherited from the AtpMixedString mixin — no spec rows)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAtpReferences         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAtpReference          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAtpStringReferences   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAtpStringReference    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is FormulaExpression:
            raise TypeError("FormulaExpression is an abstract class.")

        super().__init__()

        # The referable object shall yield a numerical / boolean value. Stereotypes: atpAbstract
        self.atpReferences: List[Referrable] = []

        # The referable object shall yield a string value. Stereotypes: atpAbstract
        self.atpStringReferences: List[Referrable] = []

    def getAtpReferences(self) -> List[Referrable]:
        """The referable object shall yield a numerical / boolean value."""
        return self.atpReferences

    def addAtpReference(self, value: Optional[Referrable]) -> "FormulaExpression":
        """The referable object shall yield a numerical / boolean value. A None value is a no-op and does not append anything."""
        if value is not None:
            self.atpReferences.append(value)
        return self

    def getAtpStringReferences(self) -> List[Referrable]:
        """The referable object shall yield a string value."""
        return self.atpStringReferences

    def addAtpStringReference(self, value: Optional[Referrable]) -> "FormulaExpression":
        """The referable object shall yield a string value. A None value is a no-op and does not append anything."""
        if value is not None:
            self.atpStringReferences.append(value)
        return self
