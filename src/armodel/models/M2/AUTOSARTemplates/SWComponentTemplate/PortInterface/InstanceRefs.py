"""
This module contains classes for representing AUTOSAR instance references
in port interface contexts. These classes are used for referencing data
elements within port interfaces and compositions.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class ApplicationCompositeElementInPortInterfaceInstanceRef(AtpInstanceRef):

    # ApplicationCompositeElementInPortInterfaceInstanceRef method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.17, p.953 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBaseRef                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextDataPrototypeRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextDataPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRootDataPrototypeRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRootDataPrototypeRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetDataPrototypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetDataPrototypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the SenderReceiverInterface that acts as the base in this InstanceRef definition
        self.baseRef: Optional[RefType] = None

        # This represents a context ApplicationCompositeDataPrototype
        self.contextDataPrototypeRefs: List[RefType] = []

        # This refers to the dataPrototype which is typed by the ApplicationDatatype in which which the target can be found.
        self.rootDataPrototypeRef: Optional[RefType] = None

        # This represents the referenced ApplicationCompositeDataPrototype.
        self.targetDataPrototypeRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        This represents the SenderReceiverInterface that acts as the base in this InstanceRef definition
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        This represents the SenderReceiverInterface that acts as the base in this InstanceRef definition. A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """
        This represents a context ApplicationCompositeDataPrototype
        """
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        This represents a context ApplicationCompositeDataPrototype. A None value is a no-op and does not add a contextDataPrototypeRef.
        """
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getRootDataPrototypeRef(self) -> Optional[RefType]:
        """
        This refers to the dataPrototype which is typed by the ApplicationDatatype in which which the target can be found.
        """
        return self.rootDataPrototypeRef

    def setRootDataPrototypeRef(self, value: Optional[RefType]) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        This refers to the dataPrototype which is typed by the ApplicationDatatype in which which the target can be found. A None value is a no-op and does not overwrite an existing rootDataPrototypeRef.
        """
        if value is not None:
            self.rootDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """
        This represents the referenced ApplicationCompositeDataPrototype.
        """
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """
        This represents the referenced ApplicationCompositeDataPrototype. A None value is a no-op and does not overwrite an existing targetDataPrototypeRef.
        """
        if value is not None:
            self.targetDataPrototypeRef = value
        return self
