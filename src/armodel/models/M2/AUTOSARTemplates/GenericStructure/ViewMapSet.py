"""
ViewMapSet module for AUTOSAR M2 models.

Spec package: AUTOSAR Templates::GenericStructure::ViewMapSet (ViewMap + ViewMapSet).
ViewMapSet is declared on the import-safe Identifiable base; ARPackage rebinds its
__bases__ to ARElement after its own definition (late-bind pattern, see
BuildActionManifest / Collection).
"""

from __future__ import annotations
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType

__all__ = ["ViewMap", "ViewMapSet"]


class ViewMap(Identifiable):
    """
    The ViewMap allows to relate any number of elements on the "first" side to any number of elements on the "second" side. Since the ViewMap does not address a specific mapping use-case the roles "first" and "second" shall imply this generality. This mapping allows to trace transformations of artifacts within the AUTOSAR environment. The references to the mapped elements can be plain references and/or InstanceRefs.
    """

    # ViewMap method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 14.2, p.401
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstElementRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addFirstElementRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirstElementIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addFirstElementIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRole                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondElementRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSecondElementRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondElementIRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSecondElementIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to identifiable elements on the first "side".
        self.firstElementRefs: List[RefType] = []

        # InstanceRefs to elements on the first "side".
        self.firstElementIRefs: List[AnyInstanceRef] = []

        # This attribute is used to describe specific mapping scenarios, e.g. the mappings: • AR_AbstractSystemDescription_SystemDescription • AR_SystemDescription_SystemExtract
        self.role: Optional[Identifier] = None

        # Reference to identifiable elements on the second "side".
        self.secondElementRefs: List[RefType] = []

        # InstanceRefs to elements on the second "side".
        self.secondElementIRefs: List[AnyInstanceRef] = []

    def getFirstElementRefs(self) -> List[RefType]:
        """
        Reference to identifiable elements on the first "side".
        """
        return self.firstElementRefs

    def addFirstElementRef(self, value: Optional[RefType]) -> ViewMap:
        """
        Reference to identifiable elements on the first "side".
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.firstElementRefs.append(value)
        return self

    def getFirstElementIRefs(self) -> List[AnyInstanceRef]:
        """
        InstanceRefs to elements on the first "side".
        """
        return self.firstElementIRefs

    def addFirstElementIRef(self, value: Optional[AnyInstanceRef]) -> ViewMap:
        """
        InstanceRefs to elements on the first "side".
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.firstElementIRefs.append(value)
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        This attribute is used to describe specific mapping scenarios, e.g. the mappings: • AR_AbstractSystemDescription_SystemDescription • AR_SystemDescription_SystemExtract
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> ViewMap:
        """
        This attribute is used to describe specific mapping scenarios, e.g. the mappings: • AR_AbstractSystemDescription_SystemDescription • AR_SystemDescription_SystemExtract
        A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self

    def getSecondElementRefs(self) -> List[RefType]:
        """
        Reference to identifiable elements on the second "side".
        """
        return self.secondElementRefs

    def addSecondElementRef(self, value: Optional[RefType]) -> ViewMap:
        """
        Reference to identifiable elements on the second "side".
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.secondElementRefs.append(value)
        return self

    def getSecondElementIRefs(self) -> List[AnyInstanceRef]:
        """
        InstanceRefs to elements on the second "side".
        """
        return self.secondElementIRefs

    def addSecondElementIRef(self, value: Optional[AnyInstanceRef]) -> ViewMap:
        """
        InstanceRefs to elements on the second "side".
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.secondElementIRefs.append(value)
        return self


class ViewMapSet(Identifiable):
    """
    Collection of ViewMaps that are used to establish relationships between different AUTOSAR artifacts. Tags: atp.recommendedPackage=ViewMapSets
    """

    # ViewMapSet method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 14.1, p.401
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createViewMap    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getViewMaps      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # ViewMaps that are collected by the ViewMapSet.
        self.viewMaps: List[ViewMap] = []

    def createViewMap(self, short_name: str) -> ViewMap:
        """
        Creates a ViewMap of this ViewMapSet with the given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new ViewMap

        Returns:
            The created (or existing) ViewMap
        """
        if not self.IsReferrableElementExists(short_name, ViewMap):
            view_map = ViewMap(self, short_name)
            self.addReferrableElement(view_map)
            self.viewMaps.append(view_map)
        return self.getReferrableElement(short_name, ViewMap)

    def getViewMaps(self) -> List[ViewMap]:
        """
        ViewMaps that are collected by the ViewMapSet.
        """
        return self.viewMaps
