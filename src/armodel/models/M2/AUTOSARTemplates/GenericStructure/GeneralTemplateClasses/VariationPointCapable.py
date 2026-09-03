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
