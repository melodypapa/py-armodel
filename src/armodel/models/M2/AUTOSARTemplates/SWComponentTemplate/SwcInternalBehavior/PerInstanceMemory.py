from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, String
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class PerInstanceMemory(AtpStructureElement, VariationPointCapable):
    "Defines a 'C' typed memory-block that needs to be available for each instance of the SW-component. This is typically only useful if supportsMultipleInstantiation is set to \"true\" or if the software-component defines NVRAM access via permanent blocks."

    # PerInstanceMemory method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.49, p.597 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInitValue      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInitValue      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwDataDefProps [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwDataDefProps [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getType          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setType          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTypeDefinition [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTypeDefinition [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies initial value(s) of the PerInstanceMemory
        self.initValue: Optional[String] = None

        # This represents the ability to to allocate RAM at specific memory sections, for example, to support the RAM Block recovery strategy by mapping to uninitialized RAM.
        self.swDataDefProps: Optional[SwDataDefProps] = None

        # The name of the "C"-type
        self.type: Optional[CIdentifier] = None

        # A definition of the type with the syntax of a 'C' typedef.
        self.typeDefinition: Optional[String] = None

    def getInitValue(self) -> Optional[String]:
        """Specifies initial value(s) of the PerInstanceMemory"""
        return self.initValue

    def setInitValue(self, value: Optional[String]) -> "PerInstanceMemory":
        """Specifies initial value(s) of the PerInstanceMemory. None values are ignored."""
        if value is not None:
            self.initValue = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """This represents the ability to to allocate RAM at specific memory sections, for example, to support the RAM Block recovery strategy by mapping to uninitialized RAM."""
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "PerInstanceMemory":
        """This represents the ability to to allocate RAM at specific memory sections, for example, to support the RAM Block recovery strategy by mapping to uninitialized RAM. None values are ignored."""
        if value is not None:
            self.swDataDefProps = value
        return self

    def getType(self) -> Optional[CIdentifier]:
        """The name of the \"C\"-type"""
        return self.type

    def setType(self, value: Optional[CIdentifier]) -> "PerInstanceMemory":
        """The name of the \"C\"-type. None values are ignored."""
        if value is not None:
            self.type = value
        return self

    def getTypeDefinition(self) -> Optional[String]:
        """A definition of the type with the syntax of a 'C' typedef."""
        return self.typeDefinition

    def setTypeDefinition(self, value: Optional[String]) -> "PerInstanceMemory":
        """A definition of the type with the syntax of a 'C' typedef. None values are ignored."""
        if value is not None:
            self.typeDefinition = value
        return self
