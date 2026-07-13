"""
This module contains classes for representing AUTOSAR variable references
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import ArVariableInImplementationDataInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef


class AutosarVariableRef(ARObject):
    """
    A reference to a variable used in the context of AUTOSAR software component
    internal behavior.
    """
    # AutosarVariableRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAutosarVariableIRef       [x] impl  [x] docstring  [ ] test
    # [ ] setAutosarVariableIRef       [x] impl  [x] docstring  [ ] test
    # [ ] getAutosarVariableInImplDatatype [x] impl  [x] docstring  [ ] test
    # [ ] setAutosarVariableInImplDatatype [x] impl  [ ] docstring  [ ] test
    # [ ] getLocalVariableRef          [x] impl  [x] docstring  [ ] test
    # [ ] setLocalVariableRef          [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.autosarVariableIRef: VariableInAtomicSWCTypeInstanceRef = None
        self.autosarVariableInImplDatatype: ArVariableInImplementationDataInstanceRef = None
        self.localVariableRef: 'VariableInAtomicSWCTypeInstanceRef' = None

    def getAutosarVariableIRef(self) -> VariableInAtomicSWCTypeInstanceRef:
        """
        Gets the AUTOSAR variable instance reference.

        Returns:
            VariableInAtomicSWCTypeInstanceRef: The AUTOSAR variable instance reference
        """
        return self.autosarVariableIRef

    def setAutosarVariableIRef(self, value):
        """
        Sets the AUTOSAR variable instance reference.

        Args:
            value: The AUTOSAR variable instance reference to set

        Returns:
            self for method chaining
        """
        self.autosarVariableIRef = value
        return self

    def getAutosarVariableInImplDatatype(self) -> ArVariableInImplementationDataInstanceRef:
        """Get the autosarVariableInImplDatatype attribute."""
        return self.autosarVariableInImplDatatype

    def setAutosarVariableInImplDatatype(self, value):
        self.autosarVariableInImplDatatype = value
        return self

    def getLocalVariableRef(self):
        """
        Gets the local variable reference.

        Returns:
            The local variable reference
        """
        return self.localVariableRef

    def setLocalVariableRef(self, value):
        """
        Sets the local variable reference.

        Args:
            value: The local variable reference to set

        Returns:
            self for method chaining
        """
        self.localVariableRef = value
        return self
