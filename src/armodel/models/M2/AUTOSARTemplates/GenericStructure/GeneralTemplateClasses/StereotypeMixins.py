from abc import ABC
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint


class VariationPointCapable(ABC):
    variationPoint: Optional["VariationPoint"] = None

    def getVariationPoint(self) -> Optional["VariationPoint"]:
        return self.variationPoint

    def setVariationPoint(self, value: Optional["VariationPoint"]) -> "VariationPointCapable":
        if value is not None:
            self.variationPoint = value
        return self


class AtpMixedString(ABC):
    """
    This is a mixed content model with intermixed text. This is applied to metaclasses only.
    """

    # AtpMixedString — interface-level mixin for the <<atpMixedString>> stereotype.
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.md, [TPS_GST_00025], section 2.3.1 (R23-11)
    # Serialization: R23-11/AUTOSAR_FO_TPS_XMLSchemaProductionRules.md, [TPS_XMLSPR_00047], section 3.2.4.2 (R23-11)
    # No spec table: stereotype-inherent accessors have no attribute rows ("no spec row" convention).
    # Columns: impl / docstring / test   ([—] = no spec row)
    # [x] getMixedString    [x] impl  [x] docstring  [x] test
    # [x] setMixedString    [x] impl  [x] docstring  [x] test

    # Class-level default — the ONLY initialization. The repo's Referrable.__init__
    # calls ARObject.__init__ directly (bypassing super()), so a mixin __init__ may
    # never run under combined inheritance (e.g. TimingConditionFormula). This mixin
    # has no __init__ at all; reads fall back to this class attribute until
    # setMixedString assigns the instance attribute. Do not remove it.
    mixedString: Optional[str] = None

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
