from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeInPortInterfaceRef, DataPrototypeReference


class DataPrototypeInSenderReceiverInterfaceInstanceRef(AtpInstanceRef, DataPrototypeInPortInterfaceRef):
    """
    Instance reference to a DataPrototype in the context of a SenderReceiverInterface.
    """

    # DataPrototypeInSenderReceiverInterfaceInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.20, p.788
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getBaseRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeInSrRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeInSrRefs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootDataPrototypeInSrRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootDataPrototypeInSrRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeInSrRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeInSrRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        self.contextDataPrototypeInSrRefs: List[RefType] = []

        # Tags: xml.sequenceOffset=10
        self.rootDataPrototypeInSrRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetDataPrototypeInSrRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Stereotypes: atpDerived
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextDataPrototypeInSrRefs(self) -> List[RefType]:
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        """
        return self.contextDataPrototypeInSrRefs

    def addContextDataPrototypeInSrRefs(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not add to contextDataPrototypeInSrRefs.
        """
        if value is not None:
            self.contextDataPrototypeInSrRefs.append(value)
        return self

    def getRootDataPrototypeInSrRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=10
        """
        return self.rootDataPrototypeInSrRef

    def setRootDataPrototypeInSrRef(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing rootDataPrototypeInSrRef.
        """
        if value is not None:
            self.rootDataPrototypeInSrRef = value
        return self

    def getTargetDataPrototypeInSrRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetDataPrototypeInSrRef

    def setTargetDataPrototypeInSrRef(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetDataPrototypeInSrRef.
        """
        if value is not None:
            self.targetDataPrototypeInSrRef = value
        return self


class DataPrototypeInClientServerInterfaceInstanceRef(AtpInstanceRef, DataPrototypeInPortInterfaceRef):
    """
    Instance reference to a DataPrototype in the context of a ClientServerInterface.
    """

    # DataPrototypeInClientServerInterfaceInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.21, p.788
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getBaseRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeInCsRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeInCsRefs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootDataPrototypeInCsRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootDataPrototypeInCsRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeInCsRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeInCsRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        self.contextDataPrototypeInCsRefs: List[RefType] = []

        # Tags: xml.sequenceOffset=10
        self.rootDataPrototypeInCsRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetDataPrototypeInCsRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Stereotypes: atpDerived
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextDataPrototypeInCsRefs(self) -> List[RefType]:
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        """
        return self.contextDataPrototypeInCsRefs

    def addContextDataPrototypeInCsRefs(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not add to contextDataPrototypeInCsRefs.
        """
        if value is not None:
            self.contextDataPrototypeInCsRefs.append(value)
        return self

    def getRootDataPrototypeInCsRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=10
        """
        return self.rootDataPrototypeInCsRef

    def setRootDataPrototypeInCsRef(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing rootDataPrototypeInCsRef.
        """
        if value is not None:
            self.rootDataPrototypeInCsRef = value
        return self

    def getTargetDataPrototypeInCsRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetDataPrototypeInCsRef

    def setTargetDataPrototypeInCsRef(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetDataPrototypeInCsRef.
        """
        if value is not None:
            self.targetDataPrototypeInCsRef = value
        return self


class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """
    This meta-class represents the ability to refer to the internal structure of an AutosarDataPrototype which is typed by an ImplementationDatatype in the context of a PortInterface. In other words, this meta-class shall not be used to model a reference to the AutosarDataPrototype as a target itself, even if the AutosarDataPrototype is typed by an ImplementationDataType and even if that ImplementationDataType represents a composite data type.
    """

    # ImplementationDataTypeElementInPortInterfaceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.22, p.789
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getContextImplementationDataElementRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextImplementationDataElementRefs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootDataPrototypeRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootDataPrototypeRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetImplementationDataTypeElementRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetImplementationDataTypeElementRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        self.contextImplementationDataElementRefs: List[RefType] = []

        # This refers to the AutosarDataPrototype which is typed by the ImplementationDatatype. The targetDataPrototype and all defined contextDataPrototypes can be found within this rootDataPrototype. Tags: xml.sequenceOffset=10
        self.rootDataPrototypeRef: Optional[RefType] = None

        # This is a target ImplementationDataTypeElement in case that the rootDataPrototype is composite and the target is a subElement of the rootDataPrototype. Tags: xml.sequenceOffset=30
        self.targetImplementationDataTypeElementRef: Optional[RefType] = None

    def getContextImplementationDataElementRefs(self) -> List[RefType]:
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        """
        return self.contextImplementationDataElementRefs

    def addContextImplementationDataElementRefs(self, value: Optional[RefType]) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not add to contextImplementationDataElementRefs.
        """
        if value is not None:
            self.contextImplementationDataElementRefs.append(value)
        return self

    def getRootDataPrototypeRef(self) -> Optional[RefType]:
        """
        This refers to the AutosarDataPrototype which is typed by the ImplementationDatatype. The targetDataPrototype and all defined contextDataPrototypes can be found within this rootDataPrototype. Tags: xml.sequenceOffset=10
        """
        return self.rootDataPrototypeRef

    def setRootDataPrototypeRef(self, value: Optional[RefType]) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        This refers to the AutosarDataPrototype which is typed by the ImplementationDatatype. The targetDataPrototype and all defined contextDataPrototypes can be found within this rootDataPrototype. Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing rootDataPrototypeRef.
        """
        if value is not None:
            self.rootDataPrototypeRef = value
        return self

    def getTargetImplementationDataTypeElementRef(self) -> Optional[RefType]:
        """
        This is a target ImplementationDataTypeElement in case that the rootDataPrototype is composite and the target is a subElement of the rootDataPrototype. Tags: xml.sequenceOffset=30
        """
        return self.targetImplementationDataTypeElementRef

    def setTargetImplementationDataTypeElementRef(self, value: Optional[RefType]) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        This is a target ImplementationDataTypeElement in case that the rootDataPrototype is composite and the target is a subElement of the rootDataPrototype. Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetImplementationDataTypeElementRef.
        """
        if value is not None:
            self.targetImplementationDataTypeElementRef = value
        return self
