from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

__all__ = ["BlueprintMappingSet", "BlueprintMapping"]


class BlueprintMapping(AtpBlueprintMapping):
    """
    This meta-class represents the ability to map two an object and its blueprint.
    """

    # BlueprintMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.17, p.163 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBlueprintRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBlueprintRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDerivedObjectRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDerivedObjectRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Table C.17 is an appendix-letter table with the one-caption-early extraction shift:
    # the actual BlueprintMapping body renders ABOVE the "Table C.17" caption (FO_TPS_
    # StandardizationTemplate L4977-4985); the rows under the caption are BlueprintPolicy
    # (row-identified). No numeric main table exists in R23-11; the R4.3.1 reproduction is
    # Table D.13 (AUTOSAR_TPS_StandardizationTemplate, identical Note/Base/Attributes).
    # The appendix table omits Mul./Kind columns: kinds and multiplicities come from XSD
    # 00052 group BLUEPRINT-MAPPING (L9118) — BLUEPRINT-REF (0..1, DEST
    # ATP-BLUEPRINT--SUBTYPES-ENUM) then DERIVED-OBJECT-REF (0..1, DEST
    # ATP-BLUEPRINTABLE--SUBTYPES-ENUM); the attribute docstrings are the XSD element
    # documentations (the table carries no per-attribute Notes). Base row
    # "ARObject , AtpBlueprintMapping" -> most-derived AtpBlueprintMapping (abstract base,
    # R23-11 Table C.13); the base group ATP-BLUEPRINT-MAPPING (L6888) skips both
    # atpDerived associations, so the base models them (atpBlueprintRef /
    # atpBlueprintedElementRef) while only this class's BLUEPRINT-REF/DERIVED-OBJECT-REF
    # serialize. Reader readBlueprintMapping is dispatched from readBlueprintMappingSet's
    # BLUEPRINT-MAPPING branch; writer writeBlueprintMapping from writeBlueprintMappingSet's
    # else-branch (XSD element order BLUEPRINT-REF -> DERIVED-OBJECT-REF).

    def __init__(self):
        super().__init__()

        # This represents the mapped blueprint.
        self.blueprintRef: Optional[RefType] = None

        # This represents the object which was derived from the blueprint.
        self.derivedObjectRef: Optional[RefType] = None

    def getBlueprintRef(self) -> Optional[RefType]:
        """This represents the mapped blueprint."""
        return self.blueprintRef

    def setBlueprintRef(self, value: Optional[RefType]) -> "BlueprintMapping":
        """This represents the mapped blueprint. A None value is a no-op and is not set."""
        if value is not None:
            self.blueprintRef = value
        return self

    def getDerivedObjectRef(self) -> Optional[RefType]:
        """This represents the object which was derived from the blueprint."""
        return self.derivedObjectRef

    def setDerivedObjectRef(self, value: Optional[RefType]) -> "BlueprintMapping":
        """This represents the object which was derived from the blueprint. A None value is a no-op and is not set."""
        if value is not None:
            self.derivedObjectRef = value
        return self


class BlueprintMappingSet(ARElement):
    """
    This represents a container of mappings between "actual" model elements and the "blueprint" that has been taken for their creation.
    """

    # BlueprintMappingSet method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 3.1, p.48 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addBlueprintMap      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBlueprintMaps     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents a particular blueprint map in the set.
        self.blueprintMaps: List[AtpBlueprintMapping] = []

    def addBlueprintMap(self, value: Optional[AtpBlueprintMapping]) -> "BlueprintMappingSet":
        """
        This represents a particular blueprint map in the set. A None value is a no-op and is not added.
        """
        if value is not None:
            self.blueprintMaps.append(value)
        return self

    def getBlueprintMaps(self) -> List[AtpBlueprintMapping]:
        """
        This represents a particular blueprint map in the set.
        """
        return self.blueprintMaps
