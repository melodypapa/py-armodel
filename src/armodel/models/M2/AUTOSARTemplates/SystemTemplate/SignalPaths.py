from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import OperationInSystemInstanceRef, VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class SwcToSwcOperationArgumentsDirectionEnum(AREnum):
    """
    Direction addressed by this element.
    """

    # SwcToSwcOperationArgumentsDirectionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.39, p.254
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on SwcToSwcOperationArguments.direction
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # IN (all IN and INOUT arguments) Tags: atp.EnumerationLiteralIndex=0
    IN = "IN"

    # OUT (all OUT and INOUT arguments) . Tags: atp.EnumerationLiteralIndex=1
    OUT = "OUT"

    def __init__(self):
        super().__init__(
            (
                SwcToSwcOperationArgumentsDirectionEnum.IN,
                SwcToSwcOperationArgumentsDirectionEnum.OUT,
            )
        )


class SignalPathConstraint(ARObject, VariationPointCapable, ABC):
    """
    Additional guidelines for the System Generator, which specific way a signal between two Software Components should take in the network without defining in which frame and with which timing it is transmitted.
    """

    # SignalPathConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.114, p.NN/A (R23-11 markdown appendix; page not extractable from the R23-11 PDF)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIntroduction    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)

    def __init__(self):
        if type(self) is SignalPathConstraint:
            raise TypeError("SignalPathConstraint is an abstract class.")

        super().__init__()

        # This represents introductory documentation about the signal path constraint.
        self.introduction: Optional[DocumentationBlock] = None

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents introductory documentation about the signal path constraint.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> SignalPathConstraint:
        """
        This represents introductory documentation about the signal path constraint.

        A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self


class SwcToSwcSignal(ARObject):
    """
    The SwcToSwcSignal describes the information (data element) that is exchanged between two SW Components. On the SWC Level it is possible that a SW Component sends one data element from one P-Port to two different SW Components (1:n Communication). The SwcToSwcSignal describes exactly the information which is exchanged between one P-Port of a SW Component and one R-Port of another SW Component.
    """

    # SwcToSwcSignal method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.37, p.253
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDataElementIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElementIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to a data element on the PPortPrototype and to the same data element on the RPortPrototype. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        self.dataElementIRefs: List[VariableDataPrototypeInSystemInstanceRef] = []

    def addDataElementIRef(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]) -> SwcToSwcSignal:
        """
        Reference to a data element on the PPortPrototype and to the same data element on the RPortPrototype. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.dataElementIRefs.append(value)
        return self

    def getDataElementIRefs(self) -> List[VariableDataPrototypeInSystemInstanceRef]:
        """
        Reference to a data element on the PPortPrototype and to the same data element on the RPortPrototype. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        """
        return self.dataElementIRefs


class CommonSignalPath(SignalPathConstraint):
    """
    The CommonSignalPath describes that two or more SwcToSwcSignals and/or SwcToSwcOperationArguments shall take the same way (Signal Path) in the topology.
    """

    # CommonSignalPath method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.36, p.253
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addOperation    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOperations   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSignal       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignals      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # The arguments sent in one direction (either from client to server or server to client) of the operations that shall take the same signal path.
        self.operations: List[SwcToSwcOperationArguments] = []

        # The SwcToSwcSignals that shall take the same way (Signal Path) in the topology.
        self.signals: List[SwcToSwcSignal] = []

    def addOperation(self, value: Optional[SwcToSwcOperationArguments]) -> CommonSignalPath:
        """
        The arguments sent in one direction (either from client to server or server to client) of the operations that shall take the same signal path.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.operations.append(value)
        return self

    def getOperations(self) -> List[SwcToSwcOperationArguments]:
        """
        The arguments sent in one direction (either from client to server or server to client) of the operations that shall take the same signal path.
        """
        return self.operations

    def addSignal(self, value: Optional[SwcToSwcSignal]) -> CommonSignalPath:
        """
        The SwcToSwcSignals that shall take the same way (Signal Path) in the topology.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.signals.append(value)
        return self

    def getSignals(self) -> List[SwcToSwcSignal]:
        """
        The SwcToSwcSignals that shall take the same way (Signal Path) in the topology.
        """
        return self.signals


class SwcToSwcOperationArguments(ARObject):
    """
    The SwcToSwcOperationArguments describes the information (client server operation arguments, plus the operation identification, if required) that are exchanged between two SW Components from exactly one client to one server, or from one server back to one client. The direction attribute defines which direction is described. If direction == IN, all arguments sent from the client to the server are described by the SwcToSwcOperationArguments, in direction == OUT, it's the arguments sent back from server to client.
    """

    # SwcToSwcOperationArguments method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.38, p.254
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDirection         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDirection         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addOperationIRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOperationIRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Direction addressed by this SwcToSwcClientServerOperation element.
        self.direction: Optional[SwcToSwcOperationArgumentsDirectionEnum] = None

        # Reference to the operation at the client and at the server side whose arguments are described by SwcToSwcOperationArguments. The two ports referenced shall be connected by a connector in the software component description. InstanceRef implemented by: OperationInSystemInstanceRef
        self.operationIRefs: List[OperationInSystemInstanceRef] = []

    def getDirection(self) -> Optional[SwcToSwcOperationArgumentsDirectionEnum]:
        """
        Direction addressed by this SwcToSwcClientServerOperation element.
        """
        return self.direction

    def setDirection(self, value: Optional[SwcToSwcOperationArgumentsDirectionEnum]) -> SwcToSwcOperationArguments:
        """
        Direction addressed by this SwcToSwcClientServerOperation element.

        A None value is a no-op and does not overwrite an existing direction.
        """
        if value is not None:
            self.direction = value
        return self

    def addOperationIRef(self, value: Optional[OperationInSystemInstanceRef]) -> SwcToSwcOperationArguments:
        """
        Reference to the operation at the client and at the server side whose arguments are described by SwcToSwcOperationArguments. The two ports referenced shall be connected by a connector in the software component description. InstanceRef implemented by: OperationInSystemInstanceRef

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.operationIRefs.append(value)
        return self

    def getOperationIRefs(self) -> List[OperationInSystemInstanceRef]:
        """
        Reference to the operation at the client and at the server side whose arguments are described by SwcToSwcOperationArguments. The two ports referenced shall be connected by a connector in the software component description. InstanceRef implemented by: OperationInSystemInstanceRef
        """
        return self.operationIRefs


class ForbiddenSignalPath(SignalPathConstraint):
    """
    The ForbiddenSignalPath describes the physical channels which an element shall not take in the topology. Such a signal path can be a constraint for the communication matrix, because such a path has an effect on the frame generation and the frame path.
    """

    # ForbiddenSignalPath method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.40, p.255
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addOperation              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOperations             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPhysicalChannelRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPhysicalChannelRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSignal                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignals                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the operation arguments of one operation which shall not take the predefined way in the topology.
        self.operations: List[SwcToSwcOperationArguments] = []

        # The SwcToSwcSignal shall not be transmitted on one of these physical channels.
        self.physicalChannelRefs: List[RefType] = []

        # The data element which shall not take the predefined way in the topology.
        self.signals: List[SwcToSwcSignal] = []

    def addOperation(self, value: Optional[SwcToSwcOperationArguments]) -> ForbiddenSignalPath:
        """
        Reference to the operation arguments of one operation which shall not take the predefined way in the topology.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.operations.append(value)
        return self

    def getOperations(self) -> List[SwcToSwcOperationArguments]:
        """
        Reference to the operation arguments of one operation which shall not take the predefined way in the topology.
        """
        return self.operations

    def addPhysicalChannelRef(self, value: Optional[RefType]) -> ForbiddenSignalPath:
        """
        The SwcToSwcSignal shall not be transmitted on one of these physical channels.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.physicalChannelRefs.append(value)
        return self

    def getPhysicalChannelRefs(self) -> List[RefType]:
        """
        The SwcToSwcSignal shall not be transmitted on one of these physical channels.
        """
        return self.physicalChannelRefs

    def addSignal(self, value: Optional[SwcToSwcSignal]) -> ForbiddenSignalPath:
        """
        The data element which shall not take the predefined way in the topology.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.signals.append(value)
        return self

    def getSignals(self) -> List[SwcToSwcSignal]:
        """
        The data element which shall not take the predefined way in the topology.
        """
        return self.signals


class PermissibleSignalPath(SignalPathConstraint):
    """
    The PermissibleSignalPath describes the way a data element shall take in the topology. The path is described by ordered references to PhysicalChannels. If more than one PermissibleSignalPath is defined for the same signal/operation attributes, any of them can be chosen. Such a signal path can be a constraint for the communication matrix . This path describes that one data element should take path A (e.g. 1. CAN channel, 2. LIN channel) and not path B (1. CAN channel, FlexRay channel A). This has an effect on the frame generation and the frame path.
    """

    # PermissibleSignalPath method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.41, p.256
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addOperation              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOperations             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPhysicalChannelRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPhysicalChannelRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSignal                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignals                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # The arguments of an operation that can take the predefined way in the topology.
        self.operations: List[SwcToSwcOperationArguments] = []

        # The SwcToSwcSignal can be transmitted on one of these physical channels.
        self.physicalChannelRefs: List[RefType] = []

        # The data element which can take the predefined way in the topology.
        self.signals: List[SwcToSwcSignal] = []

    def addOperation(self, value: Optional[SwcToSwcOperationArguments]) -> PermissibleSignalPath:
        """
        The arguments of an operation that can take the predefined way in the topology.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.operations.append(value)
        return self

    def getOperations(self) -> List[SwcToSwcOperationArguments]:
        """
        The arguments of an operation that can take the predefined way in the topology.
        """
        return self.operations

    def addPhysicalChannelRef(self, value: Optional[RefType]) -> PermissibleSignalPath:
        """
        The SwcToSwcSignal can be transmitted on one of these physical channels.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.physicalChannelRefs.append(value)
        return self

    def getPhysicalChannelRefs(self) -> List[RefType]:
        """
        The SwcToSwcSignal can be transmitted on one of these physical channels.
        """
        return self.physicalChannelRefs

    def addSignal(self, value: Optional[SwcToSwcSignal]) -> PermissibleSignalPath:
        """
        The data element which can take the predefined way in the topology.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.signals.append(value)
        return self

    def getSignals(self) -> List[SwcToSwcSignal]:
        """
        The data element which can take the predefined way in the topology.
        """
        return self.signals
