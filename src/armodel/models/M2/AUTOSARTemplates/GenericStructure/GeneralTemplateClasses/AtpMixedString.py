from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class AtpMixedString(ARObject):
    """
    This is a mixed content model with intermixed text. This is applied to metaclasses only.
    """

    # AtpMixedString — implementation support base for the <<atpMixedString>> stereotype.
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.md, [TPS_GST_00025], section 2.3.1 (R23-11)
    # Serialization: R23-11/AUTOSAR_FO_TPS_XMLSchemaProductionRules.md, [TPS_XMLSPR_00047], section 3.2.4.2 (R23-11)
    # No spec table: stereotype-inherent accessors have no attribute rows ("no spec row" convention).
    # Columns: impl / docstring / test   ([—] = no spec row)
    # [x] __init__          [x] impl  [x] docstring  [x] test
    # [x] getMixedString    [x] impl  [x] docstring  [x] test
    # [x] setMixedString    [x] impl  [x] docstring  [x] test

    def __init__(self):
        if type(self) is AtpMixedString:
            raise TypeError("AtpMixedString is an abstract class.")
        super().__init__()

        # The unqualified text content mixed into the element (<<atpMixedString>>).
        # Whitespace is preserved verbatim (no strip/normalize).
        self.mixedString: Optional[str] = None

    def getMixedString(self) -> Optional[str]:
        """The unqualified text content mixed into the element (<<atpMixedString>>)."""
        return self.mixedString

    def setMixedString(self, value: Optional[str]) -> "AtpMixedString":
        """
        The unqualified text content mixed into the element (<<atpMixedString>>).
        A None value is a no-op and does not clear previously set text.
        """
        if value is not None:
            self.mixedString = value
        return self
