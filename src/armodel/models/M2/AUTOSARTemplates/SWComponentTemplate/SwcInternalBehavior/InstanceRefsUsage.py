"""
This module contains classes for representing AUTOSAR instance reference usages
in software component internal behavior templates.
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef

class ArVariableInImplementationDataInstanceRef(ARObject):
    """
    A reference to an AUTOSAR variable in the context of an implementation
    data type instance.
    """
    # ArVariableInImplementationDataInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextDataPrototypeRefs  [x] impl  [x] docstring  [ ] test
    # [ ] setContextDataPrototypeRefs  [x] impl  [x] docstring  [ ] test
    # [ ] getPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] setPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] getRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] setRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] getTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test
    # [ ] setTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.contextDataPrototypeRefs: List['RefType'] = []
        self.portPrototypeRef: 'RefType' = None
        self.rootVariableDataPrototypeRef: 'RefType' = None
        self.targetDataPrototypeRef: 'RefType' = None

    def getContextDataPrototypeRefs(self):
        """
        Gets the list of context data prototype references.

        Returns:
            List[RefType]: The list of context data prototype references
        """
        return self.contextDataPrototypeRefs

    def setContextDataPrototypeRefs(self, value):
        """
        Sets the list of context data prototype references.

        Args:
            value: The list of context data prototype references to set

        Returns:
            self for method chaining
        """
        self.contextDataPrototypeRefs = value
        return self

    def getPortPrototypeRef(self):
        """
        Gets the port prototype reference.

        Returns:
            RefType: The port prototype reference
        """
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        """
        Sets the port prototype reference.

        Args:
            value: The port prototype reference to set

        Returns:
            self for method chaining
        """
        self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self):
        """
        Gets the root variable data prototype reference.

        Returns:
            RefType: The root variable data prototype reference
        """
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value):
        """
        Sets the root variable data prototype reference.

        Args:
            value: The root variable data prototype reference to set

        Returns:
            self for method chaining
        """
        self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        """
        Gets the target data prototype reference.

        Returns:
            RefType: The target data prototype reference
        """
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        """
        Sets the target data prototype reference.

        Args:
            value: The target data prototype reference to set

        Returns:
            self for method chaining
        """
        self.targetDataPrototypeRef = value
        return self

class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    """
    A reference to a variable data prototype in the context of an atomic
    software component type instance.
    """
    # VariableInAtomicSWCTypeInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [x] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [x] docstring  [ ] test
    # [ ] getContextDataPrototypeRefs  [x] impl  [x] docstring  [ ] test
    # [ ] addContextDataPrototypeRef   [x] impl  [x] docstring  [ ] test
    # [ ] getPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] setPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] getRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] setRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] getTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test
    # [ ] setTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.baseRef: 'RefType' = None
        self.contextDataPrototypeRefs: List['RefType'] = []
        self.portPrototypeRef: 'RefType' = None
        self.rootVariableDataPrototypeRef: 'RefType' = None
        self.targetDataPrototypeRef: 'RefType' = None

    def getBaseRef(self):
        """
        Gets the base reference.

        Returns:
            RefType: The base reference
        """
        return self.baseRef

    def setBaseRef(self, value):
        """
        Sets the base reference.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        self.baseRef = value
        return self

    def getContextDataPrototypeRefs(self):
        """
        Gets the list of context data prototype references.

        Returns:
            List[RefType]: The list of context data prototype references
        """
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value):
        """
        Adds a context data prototype reference.

        Args:
            value: The context data prototype reference to add

        Returns:
            self for method chaining
        """
        self.contextDataPrototypeRefs.append(value)
        return self

    def getPortPrototypeRef(self):
        """
        Gets the port prototype reference.

        Returns:
            RefType: The port prototype reference
        """
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        """
        Sets the port prototype reference.

        Args:
            value: The port prototype reference to set

        Returns:
            self for method chaining
        """
        self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self):
        """
        Gets the root variable data prototype reference.

        Returns:
            RefType: The root variable data prototype reference
        """
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value):
        """
        Sets the root variable data prototype reference.

        Args:
            value: The root variable data prototype reference to set

        Returns:
            self for method chaining
        """
        self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        """
        Gets the target data prototype reference.

        Returns:
            RefType: The target data prototype reference
        """
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        """
        Sets the target data prototype reference.

        Args:
            value: The target data prototype reference to set

        Returns:
            self for method chaining
        """
        self.targetDataPrototypeRef = value
        return self
    

class ParameterInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    """
    A reference to a parameter data prototype in the context of an atomic
    software component type instance.
    """
    # ParameterInAtomicSWCTypeInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [x] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [x] docstring  [ ] test
    # [ ] getContextDataPrototypeRef   [x] impl  [x] docstring  [ ] test
    # [ ] setContextDataPrototypeRef   [x] impl  [x] docstring  [ ] test
    # [ ] getPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] setPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] getRootParameterDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] setRootParameterDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] getTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test
    # [ ] setTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.baseRef: 'RefType' = None
        self.contextDataPrototypeRef: 'RefType' = None
        self.portPrototypeRef: 'RefType' = None
        self.rootParameterDataPrototypeRef: 'RefType' = None
        self.targetDataPrototypeRef: 'RefType' = None

    def getBaseRef(self):
        """
        Gets the base reference.

        Returns:
            RefType: The base reference
        """
        return self.baseRef

    def setBaseRef(self, value):
        """
        Sets the base reference.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        self.baseRef = value
        return self

    def getContextDataPrototypeRef(self):
        """
        Gets the context data prototype reference.

        Returns:
            RefType: The context data prototype reference
        """
        return self.contextDataPrototypeRef

    def setContextDataPrototypeRef(self, value):
        """
        Sets the context data prototype reference.

        Args:
            value: The context data prototype reference to set

        Returns:
            self for method chaining
        """
        self.contextDataPrototypeRef = value
        return self

    def getPortPrototypeRef(self):
        """
        Gets the port prototype reference.

        Returns:
            RefType: The port prototype reference
        """
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        """
        Sets the port prototype reference.

        Args:
            value: The port prototype reference to set

        Returns:
            self for method chaining
        """
        self.portPrototypeRef = value
        return self

    def getRootParameterDataPrototypeRef(self):
        """
        Gets the root parameter data prototype reference.

        Returns:
            RefType: The root parameter data prototype reference
        """
        return self.rootParameterDataPrototypeRef

    def setRootParameterDataPrototypeRef(self, value):
        """
        Sets the root parameter data prototype reference.

        Args:
            value: The root parameter data prototype reference to set

        Returns:
            self for method chaining
        """
        self.rootParameterDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        """
        Gets the target data prototype reference.

        Returns:
            RefType: The target data prototype reference
        """
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        """
        Sets the target data prototype reference.

        Args:
            value: The target data prototype reference to set

        Returns:
            self for method chaining
        """
        self.targetDataPrototypeRef = value
        return self


class AutosarParameterRef(ARObject):
    """
    A reference to an AUTOSAR parameter.
    """
    # AutosarParameterRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAutosarParameterIRef      [x] impl  [x] docstring  [ ] test
    # [ ] setAutosarParameterIRef      [x] impl  [x] docstring  [ ] test
    # [ ] getLocalParameterRef         [x] impl  [x] docstring  [ ] test
    # [ ] setLocalParameterRef         [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.autosarParameterIRef: 'ParameterInAtomicSWCTypeInstanceRef' = None
        self.localParameterRef: 'RefType' = None

    def getAutosarParameterIRef(self):
        """
        Gets the AUTOSAR parameter instance reference.

        Returns:
            ParameterInAtomicSWCTypeInstanceRef: The AUTOSAR parameter instance
                reference
        """
        return self.autosarParameterIRef

    def setAutosarParameterIRef(self, value):
        """
        Sets the AUTOSAR parameter instance reference.

        Args:
            value: The AUTOSAR parameter instance reference to set

        Returns:
            self for method chaining
        """
        self.autosarParameterIRef = value
        return self

    def getLocalParameterRef(self):
        """
        Gets the local parameter reference.

        Returns:
            RefType: The local parameter reference
        """
        return self.localParameterRef

    def setLocalParameterRef(self, value):
        """
        Sets the local parameter reference.

        Args:
            value: The local parameter reference to set

        Returns:
            self for method chaining
        """
        self.localParameterRef = value
        return self
