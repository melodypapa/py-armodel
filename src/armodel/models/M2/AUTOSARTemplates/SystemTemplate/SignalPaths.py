from __future__ import annotations

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import OperationInSystemInstanceRef, VariableDataPrototypeInSystemInstanceRef


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
