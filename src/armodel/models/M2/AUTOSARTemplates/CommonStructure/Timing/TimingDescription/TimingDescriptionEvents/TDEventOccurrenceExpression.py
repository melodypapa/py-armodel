from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TDEventOccurrenceExpressionFormula(Referrable):
    """
    This is an extension of the FormulaExpression for the AUTOSAR Timing Extensions. A TDEventOccurrenceExpressionFormula provides the means to express the temporal characteristics of timing event occurrences in correlation with specific variable and argument values. The formal definition of the extended functions (ExtUnaryFunctions) is described in detail in the AUTOSAR Timing Extensions.
    """

    # TDEventOccurrenceExpressionFormula method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.51, p.84
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getText            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setText            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getArgumentRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArgumentRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEventRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModeRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVariableRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVariableRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This is one particular argument value used in the expression formula.
        self.argumentRef: Optional[RefType] = None

        # This is one particular timing description event used in the expression formula.
        self.eventRef: Optional[RefType] = None

        # This is one particular mode used in the expression formula.
        self.modeRef: Optional[RefType] = None

        # This is one particular variable value used in the expression formula.
        self.variableRef: Optional[RefType] = None

        self._text: Optional[str] = None

    def getText(self) -> Optional[str]:
        """Returns the mixed string content (the occurrence expression) of this <<atpMixedString>> TDEventOccurrenceExpressionFormula."""
        return self._text

    def setText(self, value: Optional[str]) -> "TDEventOccurrenceExpressionFormula":
        """Sets the mixed string content (the occurrence expression) of this <<atpMixedString>> TDEventOccurrenceExpressionFormula. A None value is a no-op and does not overwrite an existing value."""
        if value is not None:
            self._text = value
        return self

    def getArgumentRef(self) -> Optional[RefType]:
        """This is one particular argument value used in the expression formula."""
        return self.argumentRef

    def setArgumentRef(self, value: Optional[RefType]) -> "TDEventOccurrenceExpressionFormula":
        """This is one particular argument value used in the expression formula. A None value is a no-op and does not overwrite an existing argumentRef."""
        if value is not None:
            self.argumentRef = value
        return self

    def getEventRef(self) -> Optional[RefType]:
        """This is one particular timing description event used in the expression formula."""
        return self.eventRef

    def setEventRef(self, value: Optional[RefType]) -> "TDEventOccurrenceExpressionFormula":
        """This is one particular timing description event used in the expression formula. A None value is a no-op and does not overwrite an existing eventRef."""
        if value is not None:
            self.eventRef = value
        return self

    def getModeRef(self) -> Optional[RefType]:
        """This is one particular mode used in the expression formula."""
        return self.modeRef

    def setModeRef(self, value: Optional[RefType]) -> "TDEventOccurrenceExpressionFormula":
        """This is one particular mode used in the expression formula. A None value is a no-op and does not overwrite an existing modeRef."""
        if value is not None:
            self.modeRef = value
        return self

    def getVariableRef(self) -> Optional[RefType]:
        """This is one particular variable value used in the expression formula."""
        return self.variableRef

    def setVariableRef(self, value: Optional[RefType]) -> "TDEventOccurrenceExpressionFormula":
        """This is one particular variable value used in the expression formula. A None value is a no-op and does not overwrite an existing variableRef."""
        if value is not None:
            self.variableRef = value
        return self


class OperationArgumentInComponentInstanceRef(AtpInstanceRef):
    """
    Instance reference to be capable of referencing an argument of an operation in the context of a component.
    """

    # OperationArgumentInComponentInstanceRef method parity checklist:
    # Spec: (XSD-only - AUTOSAR_00052.xsd OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF group; no own AUTOSAR table)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextComponentRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextComponentRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextPortPrototypeRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextPortPrototypeRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextOperationRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextOperationRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootArgumentDataPrototypeRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootArgumentDataPrototypeRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the SW component prototype representing the context.
        self.contextComponentRefs: List[RefType] = []

        # Specifies the port prototype representing the context.
        self.contextPortPrototypeRef: Optional[RefType] = None

        # Specifies the client server operation representing the context.
        self.contextOperationRef: Optional[RefType] = None

        # Specifies the root argument data prototype representing the context.
        self.rootArgumentDataPrototypeRef: Optional[RefType] = None

        # Specifies the application composite element data prototype representing the context.
        self.contextDataPrototypeRefs: List[RefType] = []

        # Specifies the target data prototype (the argument instance target).
        self.targetDataPrototypeRef: Optional[RefType] = None

    def getContextComponentRefs(self) -> List[RefType]:
        """Specifies the SW component prototype representing the context."""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the SW component prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextPortPrototypeRef(self) -> Optional[RefType]:
        """Specifies the port prototype representing the context."""
        return self.contextPortPrototypeRef

    def setContextPortPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the port prototype representing the context. A None value is a no-op and does not overwrite an existing contextPortPrototypeRef."""
        if value is not None:
            self.contextPortPrototypeRef = value
        return self

    def getContextOperationRef(self) -> Optional[RefType]:
        """Specifies the client server operation representing the context."""
        return self.contextOperationRef

    def setContextOperationRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the client server operation representing the context. A None value is a no-op and does not overwrite an existing contextOperationRef."""
        if value is not None:
            self.contextOperationRef = value
        return self

    def getRootArgumentDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the root argument data prototype representing the context."""
        return self.rootArgumentDataPrototypeRef

    def setRootArgumentDataPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the root argument data prototype representing the context. A None value is a no-op and does not overwrite an existing rootArgumentDataPrototypeRef."""
        if value is not None:
            self.rootArgumentDataPrototypeRef = value
        return self

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """Specifies the application composite element data prototype representing the context."""
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the application composite element data prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the target data prototype (the argument instance target)."""
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the target data prototype (the argument instance target). A None value is a no-op and does not overwrite an existing targetDataPrototypeRef."""
        if value is not None:
            self.targetDataPrototypeRef = value
        return self


class AutosarOperationArgumentInstance(Identifiable):
    """
    This class represents a reference to an argument instance. This way it is possible to reference an argument instance in the occurrence expression formula. The argument instance can target to one of the following arguments: • a whole argument used in an operation of a PortPrototype with ClientServerInterface • an element inside of a composite argument used in an operation of a PortPrototype with ClientServer Interface
    """

    # AutosarOperationArgumentInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.53, p.85
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # operationArgumentInstanceIRef is an InstanceRef (OperationArgumentInComponentInstanceRef), read/written via its own reader/writer.
    # [x] __init__                               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getOperationArgumentInstanceIRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setOperationArgumentInstanceIRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef
        self.operationArgumentInstanceIRef: Optional[OperationArgumentInComponentInstanceRef] = None

    def getOperationArgumentInstanceIRef(self) -> Optional[OperationArgumentInComponentInstanceRef]:
        """This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef."""
        return self.operationArgumentInstanceIRef

    def setOperationArgumentInstanceIRef(self, value: Optional[OperationArgumentInComponentInstanceRef]) -> "AutosarOperationArgumentInstance":
        """This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef. A None value is a no-op and does not overwrite an existing operationArgumentInstanceIRef."""
        if value is not None:
            self.operationArgumentInstanceIRef = value
        return self


class VariableInComponentInstanceRef(AtpInstanceRef):
    """
    Instance reference to be capable of referencing a variable of a software component in the context of a component.
    """

    # VariableInComponentInstanceRef method parity checklist:
    # Spec: (XSD-only - AUTOSAR_00052.xsd VARIABLE-IN-COMPONENT-INSTANCE-REF group; no own AUTOSAR table)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextComponentRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextComponentRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextPortPrototypeRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextPortPrototypeRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootVariableDataPrototypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootVariableDataPrototypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the SW component prototype representing the context.
        self.contextComponentRefs: List[RefType] = []

        # Specifies the port prototype representing the context.
        self.contextPortPrototypeRef: Optional[RefType] = None

        # Specifies the root variable data prototype representing the context.
        self.rootVariableDataPrototypeRef: Optional[RefType] = None

        # Specifies the application composite element data prototype representing the context.
        self.contextDataPrototypeRefs: List[RefType] = []

        # Specifies the target data prototype (the variable instance target).
        self.targetDataPrototypeRef: Optional[RefType] = None

    def getContextComponentRefs(self) -> List[RefType]:
        """Specifies the SW component prototype representing the context."""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the SW component prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextPortPrototypeRef(self) -> Optional[RefType]:
        """Specifies the port prototype representing the context."""
        return self.contextPortPrototypeRef

    def setContextPortPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the port prototype representing the context. A None value is a no-op and does not overwrite an existing contextPortPrototypeRef."""
        if value is not None:
            self.contextPortPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the root variable data prototype representing the context."""
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the root variable data prototype representing the context. A None value is a no-op and does not overwrite an existing rootVariableDataPrototypeRef."""
        if value is not None:
            self.rootVariableDataPrototypeRef = value
        return self

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """Specifies the application composite element data prototype representing the context."""
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the application composite element data prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the target data prototype (the variable instance target)."""
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the target data prototype (the variable instance target). A None value is a no-op and does not overwrite an existing targetDataPrototypeRef."""
        if value is not None:
            self.targetDataPrototypeRef = value
        return self


class AutosarVariableInstance(Identifiable):
    """
    This class represents a reference to a variable instance within AUTOSAR. This way it is possible to reference a variable instance in the occurrence expression formula. The variable instance can target to one of the following variables: • a variable provided via a PortPrototype as whole • an element inside of a composite variable provided via a PortPrototype
    """

    # AutosarVariableInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.52, p.85
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # variableInstanceIRef is an InstanceRef (VariableInComponentInstanceRef), read/written via its own reader/writer.
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getVariableInstanceIRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setVariableInstanceIRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef
        self.variableInstanceIRef: Optional[VariableInComponentInstanceRef] = None

    def getVariableInstanceIRef(self) -> Optional[VariableInComponentInstanceRef]:
        """This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef."""
        return self.variableInstanceIRef

    def setVariableInstanceIRef(self, value: Optional[VariableInComponentInstanceRef]) -> "AutosarVariableInstance":
        """This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef. A None value is a no-op and does not overwrite an existing variableInstanceIRef."""
        if value is not None:
            self.variableInstanceIRef = value
        return self
