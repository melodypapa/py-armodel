from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
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
    def __init__(self):
        super().__init__()

        self.defaultValue: Float = None
        self.variantValue: Float = None

    def getDefaultValue(self) -> Float:
        return self.defaultValue

    def setDefaultValue(self, value: Float):
        if value is not None:
            self.defaultValue = value
        return self

    def getVariantValue(self) -> Float:
        return self.variantValue

    def setVariantValue(self, value: Float):
        if value is not None:
            self.variantValue = value
        return self


__all__ = []
