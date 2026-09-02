"""
This module contains classes for representing AUTOSAR element collections
in the GenericStructure module.
"""

from __future__ import annotations

from abc import ABC
from typing import List, Optional, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Identifier, NameToken, RefType

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef


class AutoCollectEnum(AREnum):
    """
    This enumerator defines the possible approaches to determine the final set of elements in a collection.
    """

    # AutoCollectEnum method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 13.2, p.399 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Collection.autoCollect
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # Spec verified: R23-11

    # All objects being referenced (recursively) from the objects mentioned directly in the collection are also considered as part of the collection. Tags: atp.EnumerationLiteralIndex=0
    REF_ALL = "refAll"
    # This indicates that only those objects mentioned directly in the collection are part of the collection. No other objects are considered further. Tags: atp.EnumerationLiteralIndex=1
    REF_NONE = "refNone"
    # This indicates that non standard objects ([TPS_GST_00088]) referenced (recursively) by the objects mentioned directly in the collection are also considered to be part of the collection. Tags: atp.EnumerationLiteralIndex=2
    REF_NON_STANDARD = "refNonStandard"

    def __init__(self):
        super().__init__((AutoCollectEnum.REF_ALL, AutoCollectEnum.REF_NONE, AutoCollectEnum.REF_NON_STANDARD))


class CollectableElement(Identifiable, ABC):
    """
    This meta-class specifies the ability to be part of a specific AUTOSAR collection of ARPackages or ARElements. The scope of collection has been extended beyond CollectableElement with Revision 4.0.3. For compatibility reasons the name of this meta Class was not changed.
    """

    # CollectableElement method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 13.3, p.399 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")

        super().__init__(parent, short_name)


# Table 13.1 Base closure names ARElement as the most-derived direct base, but ARElement is
# defined in ARPackage.py which imports this module for CollectableElement before ARElement
# exists — the declared base below is a placeholder; ARPackage.py re-binds
# Collection.__bases__ = (ARElement,) once its module is fully defined.
class Collection(Identifiable):
    """
    This meta-class specifies a collection of elements. A collection can be utilized to express additional aspects for a set of elements. Note that Collection is an ARElement. Therefore it is applicable e.g. for EvaluatedVariant, even if this is not obvious. Usually the category of a Collection is "SET". On the other hand, a Collection can also express an arbitrary relationship between elements. This is denoted by the category "RELATION" (see also [TPS_GST_00347]). In this case the collection represents an association from "sourceElement" to "targetElement" in the role "role".
    """

    # Collection method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 13.1, p.399 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAutoCollect             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAutoCollect             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCollectedInstanceIRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addCollectedInstanceIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCollectionSemantics     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCollectionSemantics     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getElementRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addElementRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getElementRole             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setElementRole             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceElementRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSourceElementRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceInstanceIRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSourceInstanceIRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # Spec verified: R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This attribute reflects how far the referenced objects are part of the collection.
        self.autoCollect: Optional[AutoCollectEnum] = None

        # This instance ref supports the use case that a particular instance is part of the collection.
        self.collectedInstanceIRefs: List[AnyInstanceRef] = []

        # Provides the ability to express the semantics of a Collection depending on the intended use case. The collectionSemantics is specified as a NameToken which must be agreed by all stakeholders.
        self.collectionSemantics: Optional[NameToken] = None

        # This is an element in the collection. Note that Collection itself is collectable. Therefore collections can be nested. In case of category="RELATION" this represents the target end of the relation.
        self.elementRefs: List[RefType] = []

        # This attribute allows to denote a particular role of the collection. Note that the applicable semantics shall be mutually agreed between the two parties. In particular it denotes the role of element in the context of sourceElement.
        self.elementRole: Optional[Identifier] = None

        # Only if Category = "RELATION". This represents the source of a relation.
        self.sourceElementRefs: List[RefType] = []

        # Only if Category = "RELATION". This represents the source instance of a relation.
        self.sourceInstanceIRefs: List[AnyInstanceRef] = []

    def getAutoCollect(self) -> Optional[AutoCollectEnum]:
        """
        This attribute reflects how far the referenced objects are part of the collection.
        """
        return self.autoCollect

    def setAutoCollect(self, value: Optional[AutoCollectEnum]) -> "Collection":
        """
        This attribute reflects how far the referenced objects are part of the collection.
        A None value is a no-op and is not set.
        """
        if value is not None:
            self.autoCollect = value
        return self

    def getCollectedInstanceIRefs(self) -> List[AnyInstanceRef]:
        """
        This instance ref supports the use case that a particular instance is part of the collection.
        """
        return self.collectedInstanceIRefs

    def addCollectedInstanceIRef(self, value: Optional[AnyInstanceRef]) -> "Collection":
        """
        This instance ref supports the use case that a particular instance is part of the collection.
        A None value is a no-op and is not set.
        """
        if value is not None:
            self.collectedInstanceIRefs.append(value)
        return self

    def getCollectionSemantics(self) -> Optional[NameToken]:
        """
        Provides the ability to express the semantics of a Collection depending on the intended use case. The collectionSemantics is specified as a NameToken which must be agreed by all stakeholders.
        """
        return self.collectionSemantics

    def setCollectionSemantics(self, value: Optional[NameToken]) -> "Collection":
        """
        Provides the ability to express the semantics of a Collection depending on the intended use case. The collectionSemantics is specified as a NameToken which must be agreed by all stakeholders.
        A None value is a no-op and is not set.
        """
        if value is not None:
            self.collectionSemantics = value
        return self

    def getElementRefs(self) -> List[RefType]:
        """
        This is an element in the collection. Note that Collection itself is collectable. Therefore collections can be nested. In case of category="RELATION" this represents the target end of the relation.
        """
        return self.elementRefs

    def addElementRef(self, value: Optional[RefType]) -> "Collection":
        """
        This is an element in the collection. Note that Collection itself is collectable. Therefore collections can be nested. In case of category="RELATION" this represents the target end of the relation.
        A None value is a no-op and is not set.
        """
        if value is not None:
            self.elementRefs.append(value)
        return self

    def getElementRole(self) -> Optional[Identifier]:
        """
        This attribute allows to denote a particular role of the collection. Note that the applicable semantics shall be mutually agreed between the two parties. In particular it denotes the role of element in the context of sourceElement.
        """
        return self.elementRole

    def setElementRole(self, value: Optional[Identifier]) -> "Collection":
        """
        This attribute allows to denote a particular role of the collection. Note that the applicable semantics shall be mutually agreed between the two parties. In particular it denotes the role of element in the context of sourceElement.
        A None value is a no-op and is not set.
        """
        if value is not None:
            self.elementRole = value
        return self

    def getSourceElementRefs(self) -> List[RefType]:
        """
        Only if Category = "RELATION". This represents the source of a relation.
        """
        return self.sourceElementRefs

    def addSourceElementRef(self, value: Optional[RefType]) -> "Collection":
        """
        Only if Category = "RELATION". This represents the source of a relation.
        A None value is a no-op and is not set.
        """
        if value is not None:
            self.sourceElementRefs.append(value)
        return self

    def getSourceInstanceIRefs(self) -> List[AnyInstanceRef]:
        """
        Only if Category = "RELATION". This represents the source instance of a relation.
        """
        return self.sourceInstanceIRefs

    def addSourceInstanceIRef(self, value: Optional[AnyInstanceRef]) -> "Collection":
        """
        Only if Category = "RELATION". This represents the source instance of a relation.
        A None value is a no-op and is not set.
        """
        if value is not None:
            self.sourceInstanceIRefs.append(value)
        return self
