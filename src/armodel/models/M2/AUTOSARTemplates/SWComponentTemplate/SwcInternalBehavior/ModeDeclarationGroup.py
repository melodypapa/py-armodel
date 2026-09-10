"""
This module contains classes for representing AUTOSAR mode declaration groups
in software component internal behavior templates.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import ModeAccessPointIdent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class ModeAccessPoint(ARObject, VariationPointCapable):
    """
    A mode access point used by a runnable entity to read the current mode
    of a mode declaration group.
    """

    # ModeAccessPoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIdent                     [x] impl  [x] docstring  [ ] test
    # [ ] setIdent                     [x] impl  [x] docstring  [ ] test
    # [ ] getModeGroupIRef             [x] impl  [x] docstring  [ ] test
    # [ ] setModeGroupIRef             [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.ident: "ModeAccessPointIdent" = None
        self.modeGroupIRef: "RModeGroupInAtomicSWCInstanceRef" = None

    def createIdent(self, short_name: str) -> "ModeAccessPointIdent":
        """
        Creates the identification of this mode access point.

        Returns:
            ModeAccessPointIdent: The identification
        """
        if self.ident is None:
            self.ident = ModeAccessPointIdent(self, short_name)
        return self.ident

    def getIdent(self):
        """
        Gets the identification of this mode access point.

        Returns:
            ModeAccessPointIdent: The identification
        """
        return self.ident

    def setIdent(self, value):
        """
        Sets the identification of this mode access point.

        Args:
            value: The identification to set

        Returns:
            self for method chaining
        """
        self.ident = value
        return self

    def getModeGroupIRef(self):
        """
        Gets the mode group instance reference.

        Returns:
            RModeGroupInAtomicSWCInstanceRef: The mode group instance reference
        """
        return self.modeGroupIRef

    def setModeGroupIRef(self, value):
        """
        Sets the mode group instance reference.

        Args:
            value: The mode group instance reference to set

        Returns:
            self for method chaining
        """
        self.modeGroupIRef = value
        return self


class ModeSwitchPoint(AbstractAccessPoint, VariationPointCapable):
    """
    A mode switch point used by a runnable entity to switch the mode
    of a mode declaration group.
    """

    # ModeSwitchPoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getModeGroupIRef             [x] impl  [x] docstring  [ ] test
    # [ ] setModeGroupIRef             [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.modeGroupIRef: "PModeGroupInAtomicSwcInstanceRef" = None

    def getModeGroupIRef(self):
        """
        Gets the mode group instance reference.

        Returns:
            PModeGroupInAtomicSwcInstanceRef: The mode group instance reference
        """
        return self.modeGroupIRef

    def setModeGroupIRef(self, value):
        """
        Sets the mode group instance reference.

        Args:
            value: The mode group instance reference to set

        Returns:
            self for method chaining
        """
        self.modeGroupIRef = value
        return self


class IncludedModeDeclarationGroupSet(ARObject):
    """
    An IncludedModeDeclarationGroupSet declares that a set of ModeDeclarationGroups used by the software component for its implementation and consequently these ModeDeclarationGroups become part of the contract.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.51, p.601 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addModeDeclarationGroupRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeDeclarationGroupRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrefix                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrefix                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the referenced ModeDeclarationGroup.
        self.modeDeclarationGroupRefs: List[RefType] = []

        # The prefix shall be used by the RTE generator as a prefix for the creation of symbols related to the referenced ModeDeclarationGroups, e.g RTE_TRANSITION_<Mode DeclarationGroup>.
        self.prefix: Optional[Identifier] = None

    def addModeDeclarationGroupRef(self, value: RefType) -> "IncludedModeDeclarationGroupSet":
        """
        This represents the referenced ModeDeclarationGroup.

        A None value is a no-op and does not append anything.

        Args:
            value: The mode declaration group reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeDeclarationGroupRefs.append(value)
        return self

    def getModeDeclarationGroupRefs(self) -> List[RefType]:
        """
        This represents the referenced ModeDeclarationGroup.

        Returns:
            List[RefType]: The list of mode declaration group references
        """
        return self.modeDeclarationGroupRefs

    def setPrefix(self, value: Optional[Identifier]) -> "IncludedModeDeclarationGroupSet":
        """
        The prefix shall be used by the RTE generator as a prefix for the creation of symbols related to the referenced ModeDeclarationGroups, e.g RTE_TRANSITION_<Mode DeclarationGroup>.

        A None value is a no-op and does not overwrite an existing prefix.

        Args:
            value: The prefix to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.prefix = value
        return self

    def getPrefix(self) -> Optional[Identifier]:
        """
        The prefix shall be used by the RTE generator as a prefix for the creation of symbols related to the referenced ModeDeclarationGroups, e.g RTE_TRANSITION_<Mode DeclarationGroup>.

        Returns:
            Optional[Identifier]: The prefix
        """
        return self.prefix
