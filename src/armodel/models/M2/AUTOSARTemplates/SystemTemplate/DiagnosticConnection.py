# This module contains AUTOSAR System Template classes for diagnostic connections
# It defines connections for diagnostic services and communication between diagnostic entities

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TpConnectionIdent(Referrable):
    """
    This meta-class is created to add the ability to become the target of a reference to the non-Referrable Tp Connection.
    """

    # TpConnectionIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.273, p.633
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
    Represents a diagnostic connection in the AUTOSAR system, defining the relationship
    between diagnostic services and their communication endpoints. This class connects
    functional requests, physical requests, and responses within the diagnostic communication
    infrastructure of the system.
    """

    # DiagnosticConnection method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFunctionalRequestRefs     [x] impl  [ ] docstring  [ ] test
    # [ ] addFunctionalRequestRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getPeriodicResponseUudtRefs  [x] impl  [ ] docstring  [ ] test
    # [ ] addPeriodicResponseUudtRef   [x] impl  [ ] docstring  [ ] test
    # [ ] getPhysicalRequestRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setPhysicalRequestRef        [x] impl  [ ] docstring  [ ] test
    # [ ] getResponseRef               [x] impl  [ ] docstring  [ ] test
    # [ ] setResponseRef               [x] impl  [ ] docstring  [ ] test
    # [ ] getResponseOnEventRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setResponseOnEventRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.functionalRequestRefs: List[RefType] = []
        self.periodicResponseUudtRefs: List[RefType] = []
        self.physicalRequestRef: RefType = None
        self.responseRef: RefType = None
        self.responseOnEventRef: RefType = None

    def getFunctionalRequestRefs(self):
        return self.functionalRequestRefs

    def addFunctionalRequestRef(self, value):
        if value is not None:
            self.functionalRequestRefs.append(value)
        return self

    def getPeriodicResponseUudtRefs(self):
        return self.periodicResponseUudtRefs

    def addPeriodicResponseUudtRef(self, value):
        if value is not None:
            self.periodicResponseUudtRefs.append(value)
        return self

    def getPhysicalRequestRef(self):
        return self.physicalRequestRef

    def setPhysicalRequestRef(self, value):
        if value is not None:
            self.physicalRequestRef = value
        return self

    def getResponseRef(self):
        return self.responseRef

    def setResponseRef(self, value):
        if value is not None:
            self.responseRef = value
        return self

    def getResponseOnEventRef(self):
        return self.responseOnEventRef

    def setResponseOnEventRef(self, value):
        if value is not None:
            self.responseOnEventRef = value
        return self
