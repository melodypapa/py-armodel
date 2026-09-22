# This module contains AUTOSAR System Template classes for diagnostic connections
# It defines connections for diagnostic services and communication between diagnostic entities

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TpConnectionIdent(Referrable):
    """
    This meta-class is created to add the ability to become the target of a reference to the non-Referrable Tp Connection.
    """

    # TpConnectionIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.273, p.633
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # (no own attributes; Base = ARObject, Referrable)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class TpConnection(ARObject, ABC):
    """
    TpConnection Base Class.
    """

    # TpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.272, p.633
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIdent                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createTpConnectionIdent   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self):
        if type(self) is TpConnection:
            raise TypeError("TpConnection is an abstract class.")

        super().__init__()

        # This adds the ability to become referrable to Tp Connection.
        self.ident: Optional[TpConnectionIdent] = None

    def getIdent(self) -> Optional[TpConnectionIdent]:
        """This adds the ability to become referrable to Tp Connection."""
        return self.ident

    def createTpConnectionIdent(self, short_name: str) -> TpConnectionIdent:
        """This adds the ability to become referrable to Tp Connection."""
        if self.getIdent() is not None:
            return self.getIdent()
        ident = TpConnectionIdent(self, short_name)
        self.ident = ident
        return ident


class DiagnosticConnection(ARElement):
    """
    DiagnosticConncection that is used to describe the relationship between several TP connections.
    """

    # DiagnosticConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.17, p.61 (sibling copy AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.271, p.633)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFunctionalRequestRefs          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addFunctionalRequestRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPeriodicResponseUudtRefs       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addPeriodicResponseUudtRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPhysicalRequestRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPhysicalRequestRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponseRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponseOnEventRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseOnEventRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to functional request messages.
        self.functionalRequestRefs: List[RefType] = []

        # Reference to UUDT responses.
        self.periodicResponseUudtRefs: List[RefType] = []

        # Reference to a physical request message.
        self.physicalRequestRef: RefType = None

        # In the vast majority of cases a response is required. However, there are also cases where providing the response is not possible and/or not allowed.
        self.responseRef: RefType = None

        # Reference to a ROE message.
        self.responseOnEventRef: RefType = None

    def getFunctionalRequestRefs(self):
        """
        Reference to functional request messages.

        Returns:
            List of RefType instances
        """
        return self.functionalRequestRefs

    def addFunctionalRequestRef(self, value):
        """
        Reference to functional request messages.
        Only appends the value if it is not None.

        Args:
            value: The functional request reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.functionalRequestRefs.append(value)
        return self

    def getPeriodicResponseUudtRefs(self):
        """
        Reference to UUDT responses.

        Returns:
            List of RefType instances
        """
        return self.periodicResponseUudtRefs

    def addPeriodicResponseUudtRef(self, value):
        """
        Reference to UUDT responses.
        Only appends the value if it is not None.

        Args:
            value: The UUDT response reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.periodicResponseUudtRefs.append(value)
        return self

    def getPhysicalRequestRef(self):
        """
        Reference to a physical request message.

        Returns:
            The RefType instance
        """
        return self.physicalRequestRef

    def setPhysicalRequestRef(self, value):
        """
        Reference to a physical request message.
        Only sets the value if it is not None.

        Args:
            value: The physical request reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.physicalRequestRef = value
        return self

    def getResponseRef(self):
        """
        In the vast majority of cases a response is required. However, there are also cases where providing the response is not possible and/or not allowed.

        Returns:
            The RefType instance
        """
        return self.responseRef

    def setResponseRef(self, value):
        """
        In the vast majority of cases a response is required. However, there are also cases where providing the response is not possible and/or not allowed.
        Only sets the value if it is not None.

        Args:
            value: The response reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.responseRef = value
        return self

    def getResponseOnEventRef(self):
        """
        Reference to a ROE message.

        Returns:
            The RefType instance
        """
        return self.responseOnEventRef

    def setResponseOnEventRef(self, value):
        """
        Reference to a ROE message.
        Only sets the value if it is not None.

        Args:
            value: The ROE message reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.responseOnEventRef = value
        return self
