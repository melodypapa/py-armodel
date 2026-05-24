"""
This module contains classes for representing AUTOSAR mode declaration groups
in software component internal behavior templates.
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import ModeAccessPointIdent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ModeAccessPoint(ARObject):
    """
    A mode access point used by a runnable entity to read the current mode
    of a mode declaration group.
    """

    def __init__(self):
        super().__init__()

        self.ident: 'ModeAccessPointIdent' = None
        self.modeGroupIRef: 'RModeGroupInAtomicSWCInstanceRef' = None

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

class ModeSwitchPoint(AbstractAccessPoint):
    """
    A mode switch point used by a runnable entity to switch the mode
    of a mode declaration group.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.modeGroupIRef: 'PModeGroupInAtomicSwcInstanceRef' = None

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
    A set of mode declaration group references included in the scope
    of a software component internal behavior.
    """

    def __init__(self):
        super().__init__()

        self.mode_declaration_group_refs: List['RefType'] = []
        self.prefix: 'Identifier' = None

    def addModeDeclarationGroupRef(self, ref: RefType):
        """
        Adds a mode declaration group reference.

        Args:
            ref: The mode declaration group reference to add

        Returns:
            self for method chaining
        """
        self.mode_declaration_group_refs.append(ref)
        return self

    def getModeDeclarationGroupRefs(self) -> List[RefType]:
        """
        Gets the list of mode declaration group references.

        Returns:
            List[RefType]: The list of mode declaration group references
        """
        return self.mode_declaration_group_refs

    def setPrefix(self, prefix: str):
        """
        Sets the prefix for mode declaration group references.

        Args:
            prefix: The prefix to set

        Returns:
            self for method chaining
        """
        self.prefix = prefix
        return self

    def getPrefix(self) -> ARLiteral:
        """
        Gets the prefix for mode declaration group references.

        Returns:
            ARLiteral: The prefix
        """
        return self.prefix
