from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AutosarDataPrototype


class Field(AutosarDataPrototype, VariationPointCapable):
    """
    This meta-class represents the ability to define a piece of data that can be accessed with read and/or write semantics. It is also possible to generate a notification if the value of the data changes.
    """

    # Field method parity checklist:
    # Spec: AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf, Table B.9, pp.44-45 (R23-11; body renders above the caption line, caption on p.45)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getHasGetter    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHasGetter    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHasNotifier  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHasNotifier  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHasSetter    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHasSetter    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute controls whether read access is foreseen to this field.
        self.hasGetter: Optional[Boolean] = None

        # This attribute controls whether a notification semantics is foreseen to this field.
        self.hasNotifier: Optional[Boolean] = None

        # This attribute controls whether write access is foreseen to this field.
        self.hasSetter: Optional[Boolean] = None

    def getHasGetter(self) -> Optional[Boolean]:
        """
        This attribute controls whether read access is foreseen to this field.
        """
        return self.hasGetter

    def setHasGetter(self, value: Optional[Boolean]) -> "Field":
        """
        This attribute controls whether read access is foreseen to this field. A None value is a no-op and does not overwrite an existing hasGetter.
        """
        if value is not None:
            self.hasGetter = value
        return self

    def getHasNotifier(self) -> Optional[Boolean]:
        """
        This attribute controls whether a notification semantics is foreseen to this field.
        """
        return self.hasNotifier

    def setHasNotifier(self, value: Optional[Boolean]) -> "Field":
        """
        This attribute controls whether a notification semantics is foreseen to this field. A None value is a no-op and does not overwrite an existing hasNotifier.
        """
        if value is not None:
            self.hasNotifier = value
        return self

    def getHasSetter(self) -> Optional[Boolean]:
        """
        This attribute controls whether write access is foreseen to this field.
        """
        return self.hasSetter

    def setHasSetter(self, value: Optional[Boolean]) -> "Field":
        """
        This attribute controls whether write access is foreseen to this field. A None value is a no-op and does not overwrite an existing hasSetter.
        """
        if value is not None:
            self.hasSetter = value
        return self
