from __future__ import annotations

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.Documentation.Chapters import PredefinedChapter


class Documentation(ARElement):
    """
    This meta-class represents the ability to handle a so called standalone documentation. Standalone means, that such a documentation is not embedded in another ARElement or identifiable object. The standalone documentation is an entity of its own which denotes its context by reference to other objects and instances.
    """

    # Documentation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.28, p.439
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addContext                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContexts                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDocumentationContent     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDocumentationContent     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is the context of the particular documentation.
        self.contexts: List[DocumentationContext] = []

        # This is the content of the documentation related to the specified contexts.
        self.documentationContent: Optional[PredefinedChapter] = None

    def addContext(self, value: DocumentationContext) -> "Documentation":
        """
        This is the context of the particular documentation.

        A None value is a no-op and does not append an existing context.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contexts.append(value)
        return self

    def getContexts(self) -> List[DocumentationContext]:
        """
        This is the context of the particular documentation.

        Returns:
            The contexts of the particular documentation
        """
        return self.contexts

    def setDocumentationContent(self, value: Optional[PredefinedChapter]) -> "Documentation":
        """
        This is the content of the documentation related to the specified contexts.

        A None value is a no-op and does not overwrite an existing documentationContent.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.documentationContent = value
        return self

    def getDocumentationContent(self) -> Optional[PredefinedChapter]:
        """
        This is the content of the documentation related to the specified contexts.

        Returns:
            The content of the documentation related to the specified contexts
        """
        return self.documentationContent


class DocumentationContext(MultilanguageReferrable):
    """
    This class represents the ability to denote a context of a so called standalone documentation. Note that this is an <<atpMixed>>. The contents needs to be considered as ordered.
    """

    # DocumentationContext method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.56, p.327
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setFeatureIRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFeatureIRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIdentifiableRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIdentifiableRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This refers to a particular feature (instance in the M0 model) to which is the context of the documentation.
        self.featureIRef: Optional[AnyInstanceRef] = None

        # This is an identifiable object which is part of the context of the documentation.
        self.identifiableRef: Optional[RefType] = None

    def setFeatureIRef(self, value: Optional[AnyInstanceRef]) -> "DocumentationContext":
        """
        This refers to a particular feature (instance in the M0 model) to which is the context of the documentation.

        A None value is a no-op and does not overwrite an existing featureIRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.featureIRef = value
        return self

    def getFeatureIRef(self) -> Optional[AnyInstanceRef]:
        """
        This refers to a particular feature (instance in the M0 model) to which is the context of the documentation.

        Returns:
            The feature (instance in the M0 model) to which is the context of the documentation
        """
        return self.featureIRef

    def setIdentifiableRef(self, value: Optional[RefType]) -> "DocumentationContext":
        """
        This is an identifiable object which is part of the context of the documentation.

        A None value is a no-op and does not overwrite an existing identifiableRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.identifiableRef = value
        return self

    def getIdentifiableRef(self) -> Optional[RefType]:
        """
        This is an identifiable object which is part of the context of the documentation.

        Returns:
            The identifiable object which is part of the context of the documentation
        """
        return self.identifiableRef
