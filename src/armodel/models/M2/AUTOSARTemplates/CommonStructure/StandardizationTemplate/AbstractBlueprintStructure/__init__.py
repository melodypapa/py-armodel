"""
This module contains the AbstractBlueprintStructure package classes for AUTOSAR models.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AtpBlueprintable(Identifiable, ABC):
    """This meta-class represents the ability to be derived from a Blueprint. As this class is an abstract one, particular blueprintable meta-classes inherit from this one."""

    # AtpBlueprintable method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.14, p.162 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # Source corpus corrected R4.3.1 -> R23-11: the class exists in R23-11 (StandardizationTemplate
    # Table C.14, p.162; its R23-11 markdown body is misaligned under "Table C.13: AtpBlueprintMapping").
    # The Phase-0 todo cited R4.3.1 (Table 4.3, p.45) because the pdf_page.py helper regex matches only
    # unprefixed table ids (R4.3.1 "4.3") and skips R23-11 "C.14"; R23-11 is authoritative (target release,
    # identical content: Base = ARObject, Identifiable, MultilanguageReferrable, Referrable; no attributes).
    # Heritage fix: re-parented (PackageableElement) -> (Identifiable). PackageableElement/CollectableElement
    # are empty markers (no fields/methods); the `element` aggregation lives on Identifiable, so the 13
    # subclasses (CompuMethod, DataConstr, SwAddrMethod, PortPrototype, ModeDeclaration, ...) keep it.

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpBlueprintable:
            raise TypeError("AtpBlueprintable is an abstract class.")
        super().__init__(parent, short_name)


class BlueprintPolicy(ARObject, ABC):
    """This meta-class represents the ability to indicate whether blueprintable elements will be modifiable or not modifiable."""

    # BlueprintPolicy method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.18, p.164 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAttributeName     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAttributeName     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is BlueprintPolicy:
            raise TypeError("BlueprintPolicy is an abstract class.")
        super().__init__()

        # This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used.
        self.attributeName: Optional[String] = None

    def getAttributeName(self) -> Optional[String]:
        """This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used."""
        return self.attributeName

    def setAttributeName(self, attributeName: Optional[String]) -> "BlueprintPolicy":
        """This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used. A None value is a no-op and is not set."""
        if attributeName is not None:
            self.attributeName = attributeName
        return self


class AtpBlueprint(Identifiable, ABC):
    """This meta-class represents the ability to act as a Blueprint. As this class is an abstract one, particular blueprint meta-classes inherit from this one."""

    # AtpBlueprint method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.11, p.305 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addBlueprintPolicy  [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer  R23-11
    # [x] getBlueprintPolicys [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer  R23-11
    # Table D.11 is the aligned AtpBlueprint table (caption+body); the row-identical
    # bodies also render under the extraction-shifted captions C.12 (FO_TPS_
    # StandardizationTemplate, caption p.161) and E.10 (FO_TPS_GenericStructureTemplate,
    # caption p.424) one caption early. XSD 00052: AtpBlueprint is group-only
    # (ATP-BLUEPRINT, L6652) = abstract verified; its SHORT-NAME-PATTERN member carries
    # atp.Status="removed" and is absent from the PDF table (not modeled, Rule 0015).
    # Marker withheld: the blueprintPolicy aggregation's reader/writer rows stay [ ]
    # because the concrete XML-bearing BlueprintPolicy subclasses (BlueprintPolicyList,
    # BlueprintPolicyNotModifiable, BlueprintPolicySingle) are not yet synced AND not
    # queued — they own the BLUEPRINT-POLICY-LIST/-NOT-MODIFIABLE/-SINGLE elements (and
    # thus the attributeName coverage); no readAtpBlueprint/writeAtpBlueprint helper
    # exists for the same reason. BlueprintPolicy itself is implemented (R23-11 Table
    # C.18); only the subtypes' sync unblocks these rows and the stamp.

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpBlueprint:
            raise TypeError("AtpBlueprint is an abstract class.")
        super().__init__(parent, short_name)

        # This role indicates whether the blueprintable element will be modifiable or not modifiable.
        # Spec type: BlueprintPolicy (abstract, R23-11 Table C.18); the concrete XML-bearing
        # subtypes (BlueprintPolicyList/-NotModifiable/-Single) own the BLUEPRINT-POLICY-* elements.
        self.blueprintPolicys: List[BlueprintPolicy] = []

    def addBlueprintPolicy(self, value: Optional[BlueprintPolicy]) -> "AtpBlueprint":
        """This role indicates whether the blueprintable element will be modifiable or not modifiable. A None value is a no-op and does not append to blueprintPolicys."""
        if value is not None:
            self.blueprintPolicys.append(value)
        return self

    def getBlueprintPolicys(self) -> List[BlueprintPolicy]:
        """This role indicates whether the blueprintable element will be modifiable or not modifiable."""
        return self.blueprintPolicys


class AtpBlueprintMapping(ARObject, ABC):
    """This meta-class represents the ability to express a particular mapping between a blueprint and an element derived from this blueprint. Particular mappings are defined by specializations of this meta-class."""

    # AtpBlueprintMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.13, p.162 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAtpBlueprintRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAtpBlueprintRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAtpBlueprintedElementRef [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAtpBlueprintedElementRef [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # atpBlueprint / atpBlueprintedElement are abstract derived association ends (Stereotypes: atpAbstract,
    # Table C.13); the XSD serializes them only on the concrete BlueprintMapping subclass as BLUEPRINT-REF /
    # DERIVED-OBJECT-REF, so the abstract class carries no own XML element (reader/writer [—] here; the
    # coverage belongs to the BlueprintMapping sync).

    def __init__(self):
        if type(self) is AtpBlueprintMapping:
            raise TypeError("AtpBlueprintMapping is an abstract class.")
        super().__init__()
        # atpBlueprint: AtpBlueprint, 1, ref
        # This represents the blueprint.
        self.atpBlueprintRef: Optional[RefType] = None

        # atpBlueprintedElement: AtpBlueprintable, 1, ref
        # This represents the bluprinted elements which shall be mapped to the blueprint.
        self.atpBlueprintedElementRef: Optional[RefType] = None

    def getAtpBlueprintRef(self) -> Optional[RefType]:
        """This represents the blueprint."""
        return self.atpBlueprintRef

    def setAtpBlueprintRef(self, value: Optional[RefType]) -> "AtpBlueprintMapping":
        """This represents the blueprint. A None value is a no-op and is not set."""
        if value is not None:
            self.atpBlueprintRef = value
        return self

    def getAtpBlueprintedElementRef(self) -> Optional[RefType]:
        """This represents the bluprinted elements which shall be mapped to the blueprint."""
        return self.atpBlueprintedElementRef

    def setAtpBlueprintedElementRef(self, value: Optional[RefType]) -> "AtpBlueprintMapping":
        """This represents the bluprinted elements which shall be mapped to the blueprint. A None value is a no-op and is not set."""
        if value is not None:
            self.atpBlueprintedElementRef = value
        return self


__all__ = ["AtpBlueprintable", "AtpBlueprint", "AtpBlueprintMapping", "BlueprintPolicy"]
