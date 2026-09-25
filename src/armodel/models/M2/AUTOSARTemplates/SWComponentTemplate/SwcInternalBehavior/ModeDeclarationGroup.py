"""
This module contains classes for representing AUTOSAR mode declaration groups
in software component internal behavior templates.
"""

from __future__ import annotations

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import ModeAccessPointIdent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ModeGroupInAtomicSwcInstanceRef, PModeGroupInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class ModeAccessPoint(ARObject, VariationPointCapable):
    """
    A ModeAccessPoint is required by a RunnableEntity owned by a Mode Manager or Mode User. Its semantics implies the ability to access the current mode (provided by the RTE) of a ModeDeclarationGroupPrototype's ModeDeclarationGroup.
    """

    # ModeAccessPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 9.5, p.634
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createIdent      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIdent         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getModeGroupIRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModeGroupIRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The aggregation in the role ident provides the ability to make the ModeAccessPoint identifiable. From the semantical point of view, the ModeAccessPoint is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let ModeAccessPoint directly inherit from Identifiable).
        self.ident: Optional[ModeAccessPointIdent] = None

        # The mode declaration group that is accessed by this runnable.
        self.modeGroupIRef: Optional[ModeGroupInAtomicSwcInstanceRef] = None

    def createIdent(self, short_name: str) -> ModeAccessPointIdent:
        """
        The aggregation in the role ident provides the ability to make the ModeAccessPoint identifiable. From the semantical point of view, the ModeAccessPoint is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let ModeAccessPoint directly inherit from Identifiable).
        """
        if self.ident is None:
            self.ident = ModeAccessPointIdent(self, short_name)
        return self.ident

    def getIdent(self) -> Optional[ModeAccessPointIdent]:
        """
        The aggregation in the role ident provides the ability to make the ModeAccessPoint identifiable. From the semantical point of view, the ModeAccessPoint is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let ModeAccessPoint directly inherit from Identifiable).
        """
        return self.ident

    def getModeGroupIRef(self) -> Optional[ModeGroupInAtomicSwcInstanceRef]:
        """
        The mode declaration group that is accessed by this runnable.
        """
        return self.modeGroupIRef

    def setModeGroupIRef(self, value: Optional[ModeGroupInAtomicSwcInstanceRef]) -> ModeAccessPoint:
        """
        The mode declaration group that is accessed by this runnable.
        A None value is a no-op and does not overwrite an existing modeGroupIRef.
        """
        if value is not None:
            self.modeGroupIRef = value
        return self


class ModeSwitchPoint(AbstractAccessPoint, VariationPointCapable):
    """
    A ModeSwitchPoint is required by a RunnableEntity owned a Mode Manager. Its semantics implies the ability to initiate a mode switch.

    [constr_1778] Value of attribute modeSwitchPoint.returnValueProvision: All RunnableEntity.modeSwitchPoint that refer to the same modeGroup shall define the identical value of attribute returnValueProvision at the time when the contract phase generation is executed.
    """

    # ModeSwitchPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 9.4, p.633
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getModeGroupIRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModeGroupIRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The mode declaration group that is switched by this runnable. InstanceRef implemented by: PModeGroupInAtomicSwcInstanceRef
        self.modeGroupIRef: Optional[PModeGroupInAtomicSwcInstanceRef] = None

    def getModeGroupIRef(self) -> Optional[PModeGroupInAtomicSwcInstanceRef]:
        """
        The mode declaration group that is switched by this runnable. InstanceRef implemented by: PModeGroupInAtomicSwcInstanceRef
        """
        return self.modeGroupIRef

    def setModeGroupIRef(self, value: Optional[PModeGroupInAtomicSwcInstanceRef]) -> ModeSwitchPoint:
        """
        The mode declaration group that is switched by this runnable. InstanceRef implemented by: PModeGroupInAtomicSwcInstanceRef
        A None value is a no-op and does not overwrite an existing modeGroupIRef.
        """
        if value is not None:
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

    def addModeDeclarationGroupRef(self, value: RefType) -> IncludedModeDeclarationGroupSet:
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

    def setPrefix(self, value: Optional[Identifier]) -> IncludedModeDeclarationGroupSet:
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
