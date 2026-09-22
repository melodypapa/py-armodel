from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier


class RunnableEntityArgument(ARObject):
    """
    This meta-class represents the ability to provide specific information regarding the arguments to a RunnableEntity.
    """

    # RunnableEntityArgument method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.5, p.536 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSymbol [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSymbol [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the symbol to be generated into the actual signature on the level of the C programming language.
        self.symbol: Optional[CIdentifier] = None

    def getSymbol(self) -> Optional[CIdentifier]:
        """
        This represents the symbol to be generated into the actual signature on the level of the C programming language.
        """
        return self.symbol

    def setSymbol(self, value: Optional[CIdentifier]) -> "RunnableEntityArgument":
        """
        This represents the symbol to be generated into the actual signature on the level of the C programming language.
        A None value is a no-op and does not overwrite an existing symbol.
        """
        if value is not None:
            self.symbol = value
        return self
