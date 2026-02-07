from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class NumericalValueVariationPoint(ARObject):
    """
    Represents a numerical value variation point in the AUTOSAR model.

    This class is used to define variation points for numerical values,
    allowing for different values based on variant conditions.

    Attributes:
        defaultValue (Float): The default value.
        variantValue (Float): The variant value.
    """

    def __init__(self) -> None:
        super().__init__()

        self.defaultValue: Union[Union[Float, None] , None] = None
        self.variantValue: Union[Union[Float, None] , None] = None

    def getDefaultValue(self) -> Union[Float, None]:
        return self.defaultValue

    def setDefaultValue(self, value: Float) -> "NumericalValueVariationPoint":
        if value is not None:
            self.defaultValue = value
        return self

    def getVariantValue(self) -> Union[Float, None]:
        return self.variantValue

    def setVariantValue(self, value: Float) -> "NumericalValueVariationPoint":
        if value is not None:
            self.variantValue = value
        return self


__all__ = []
