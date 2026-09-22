from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ApiPrincipleEnum, InternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import PerInstanceMemory
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import AsynchronousServerCallReturnsEvent, BackgroundEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataSendCompletedEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataReceivedEvent, InitEvent, InternalTriggerOccurredEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import ModeSwitchedAckEvent, OperationInvokedEvent, RTEEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import SwcModeSwitchEvent, TimingEvent, WaitPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    RefType,
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess, VariableAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    AsynchronousServerCallPoint,
    AsynchronousServerCallResultPoint,
    ServerCallPoint,
    SynchronousServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntityArgument import RunnableEntityArgument
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    IncludedModeDeclarationGroupSet as IncludedModeDeclarationGroupSet,
    ModeAccessPoint,
    ModeSwitchPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import (
    ExternalTriggeringPoint,
    InternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity


class RunnableEntity(ExecutableEntity, VariationPointCapable):
    """
    A RunnableEntity represents the smallest code-fragment that is provided by an AtomicSwComponentType and are executed under control of the RTE. RunnableEntities are for instance set up to respond to data reception or operation invocation on a server.
    """

    # RunnableEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.3, p.525
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] _createVariableAccess        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArguments                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addArgument                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanBeInvokedConcurrently  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanBeInvokedConcurrently  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createDataReadAccess         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataReadAccesses          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createDataWriteAccess        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataWriteAccesses         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createDataReceivePointByArgument [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataReceivePointByArguments [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createDataReceivePointByValue [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataReceivePointByValues  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createDataSendPoint          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataSendPoints            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createReadLocalVariable      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReadLocalVariables        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createWrittenLocalVariable   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWrittenLocalVariables     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getParameterAccesses         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createParameterAccess        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createSynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createAsynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createAsynchronousServerCallResultPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getAsynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getAsynchronousServerCallResultPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getServerCallPoints          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createInternalTriggeringPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInternalTriggeringPoints  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getExternalTriggeringPoints  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addExternalTriggeringPoint   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeAccessPoints          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addModeAccessPoint           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeSwitchPoints          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createModeSwitchPoint        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSymbol                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSymbol                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createWaitPoint              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWaitPoints                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the formal definition of a an argument to a RunnableEntity.
        self.arguments: List[RunnableEntityArgument] = []

        # The server call result point admits a runnable to fetch the result of an asynchronous server call.
        # The aggregation of AsynchronousServerCallResultPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes and the variant existence of server call result points in the implementation.
        self.asynchronousServerCallResultPoints: List[AsynchronousServerCallResultPoint] = []

        # If the value of this attribute is set to "true" the enclosing RunnableEntity can be invoked concurrently (even for one instance of the corresponding AtomicSwComponentType).
        # This implies that it is the responsibility of the implementation of the RunnableEntity to take care of this form of concurrency.
        self.canBeInvokedConcurrently: Boolean = None

        # RunnableEntity has implicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        # The aggregation of dataReadAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataReadAccess in the implementation.
        self.dataReadAccesses: List[VariableAccess] = []

        # RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        # The result is passed back to the application by means of an argument in the function signature.
        # The aggregation of dataReceivePointByArgument is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data receive points in the implementation.
        self.dataReceivePointByArguments: List[VariableAccess] = []

        # RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        # The result is passed back to the application by means of the return value.
        # The aggregation of dataReceivePointByValue is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of data receive points in the implementation.
        self.dataReceivePointByValues: List[VariableAccess] = []

        # RunnableEntity has explicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        # The aggregation of dataSendPoint is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data send points in the implementation.
        self.dataSendPoints: List[VariableAccess] = []

        # RunnableEntity has implicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        # The aggregation of dataWriteAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataWriteAccess in the implementation.
        self.dataWriteAccesses: List[VariableAccess] = []

        # The aggregation of ExternalTriggeringPoint is subject to variability with the purpose to support the conditional existence of trigger ports or the variant existence of external triggering points in the implementation.
        self.externalTriggeringPoints: List[ExternalTriggeringPoint] = []

        # The aggregation of InternalTriggeringPoint is subject to variability with the purpose to support the variant existence of internal triggering points in the implementation.
        self.internalTriggeringPoints: List[InternalTriggeringPoint] = []

        # The runnable has a mode access point.
        # The aggregation of ModeAccessPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode access points in the implementation.
        self.modeAccessPoints: List[ModeAccessPoint] = []

        # The runnable has a mode switch point.
        # The aggregation of ModeSwitchPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode switch points in the implementation.
        self.modeSwitchPoints: List[ModeSwitchPoint] = []

        # The presence of a ParameterAccess implies that a RunnableEntity needs read only access to a ParameterDataPrototype which may either be local or within a PortPrototype.
        # The aggregation of ParameterAccess is subject to variability with the purpose to support the conditional existence of parameter ports and component local parameters as well as the variant existence of ParameterAccess (points) in the implementation.
        self.parameterAccesses: List[ParameterAccess] = []

        # The presence of a readLocalVariable implies that a RunnableEntity needs read access to a VariableDataPrototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable.
        # The aggregation of readLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicitInterRunnableVariable or the variant existence of readLocalVariable (points) in the implementation.
        self.readLocalVariables: List[VariableAccess] = []

        # The RunnableEntity has a ServerCallPoint.
        # The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation.
        self.serverCallPoints: List[ServerCallPoint] = []

        # The symbol describing this RunnableEntity's entry point. This is considered the API of the RunnableEntity and is required during the RTE contract phase.
        self.symbol: ARLiteral = None

        # The WaitPoint associated with the RunnableEntity.
        self.waitPoints: List[WaitPoint] = []

        # The presence of a writtenLocalVariable implies that a RunnableEntity needs write access to a VariableDataPrototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable.
        # The aggregation of writtenLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicitInterRunnableVariable or the variant existence of writtenLocalVariable (points) in the implementation.
        self.writtenLocalVariables: List[VariableAccess] = []

    def _createVariableAccess(self, short_name, variable_accesses: List[VariableAccess]):
        if not self.IsElementExists(short_name, VariableAccess):
            variable_access = VariableAccess(self, short_name)
            self.addElement(variable_access)
            variable_accesses.append(variable_access)
        return self.getElement(short_name, VariableAccess)

    def getArguments(self) -> List[RunnableEntityArgument]:
        """
        This represents the formal definition of a an argument to a RunnableEntity.

        Returns:
            List[RunnableEntityArgument]: The list of arguments
        """
        return self.arguments

    def addArgument(self, value: Optional[RunnableEntityArgument]) -> "RunnableEntity":
        """
        This represents the formal definition of a an argument to a RunnableEntity.
        A None value is a no-op and does not append to arguments.

        Args:
            value: The argument to add

        Returns:
            RunnableEntity: self for method chaining
        """
        if value is not None:
            self.arguments.append(value)
        return self

    def getCanBeInvokedConcurrently(self) -> Optional[Boolean]:
        """
        If the value of this attribute is set to "true" the enclosing RunnableEntity can be invoked concurrently (even for one instance of the corresponding AtomicSwComponentType).
        This implies that it is the responsibility of the implementation of the RunnableEntity to take care of this form of concurrency.

        Returns:
            Optional[Boolean]: The concurrency flag, or None if not set
        """
        return self.canBeInvokedConcurrently

    def setCanBeInvokedConcurrently(self, value: Optional[Boolean]) -> "RunnableEntity":
        """
        If the value of this attribute is set to "true" the enclosing RunnableEntity can be invoked concurrently (even for one instance of the corresponding AtomicSwComponentType).
        This implies that it is the responsibility of the implementation of the RunnableEntity to take care of this form of concurrency.
        A None value is a no-op and does not overwrite an existing canBeInvokedConcurrently.

        Args:
            value: The concurrency flag to set

        Returns:
            RunnableEntity: self for method chaining
        """
        if value is not None:
            self.canBeInvokedConcurrently = value
        return self

    def createDataReadAccess(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has implicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The aggregation of dataReadAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataReadAccess in the implementation.

        Args:
            short_name: The short name of the data read access

        Returns:
            VariableAccess: the created or existing VariableAccess
        """
        return self._createVariableAccess(short_name, self.dataReadAccesses)

    def getDataReadAccesses(self) -> List[VariableAccess]:
        """
        RunnableEntity has implicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The aggregation of dataReadAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataReadAccess in the implementation.

        Returns:
            List[VariableAccess]: The list of data read accesses
        """
        return sorted(self.dataReadAccesses, key=lambda v: v.short_name)

    def createDataWriteAccess(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has implicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The aggregation of dataWriteAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataWriteAccess in the implementation.

        Args:
            short_name: The short name of the data write access

        Returns:
            VariableAccess: the created or existing VariableAccess
        """
        return self._createVariableAccess(short_name, self.dataWriteAccesses)

    def getDataWriteAccesses(self) -> List[VariableAccess]:
        """
        RunnableEntity has implicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The aggregation of dataWriteAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataWriteAccess in the implementation.

        Returns:
            List[VariableAccess]: The list of data write accesses
        """
        return sorted(self.dataWriteAccesses, key=lambda v: v.short_name)

    def createDataReceivePointByArgument(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The result is passed back to the application by means of an argument in the function signature.
        The aggregation of dataReceivePointByArgument is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data receive points in the implementation.

        Args:
            short_name: The short name of the data receive point

        Returns:
            VariableAccess: the created or existing VariableAccess
        """
        return self._createVariableAccess(short_name, self.dataReceivePointByArguments)

    def getDataReceivePointByArguments(self) -> List[VariableAccess]:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The result is passed back to the application by means of an argument in the function signature.
        The aggregation of dataReceivePointByArgument is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data receive points in the implementation.

        Returns:
            List[VariableAccess]: The list of data receive points by argument
        """
        return sorted(self.dataReceivePointByArguments, key=lambda v: v.short_name)

    def createDataReceivePointByValue(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The result is passed back to the application by means of the return value.
        The aggregation of dataReceivePointByValue is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of data receive points in the implementation.

        Args:
            short_name: The short name of the data receive point

        Returns:
            VariableAccess: the created or existing VariableAccess
        """
        return self._createVariableAccess(short_name, self.dataReceivePointByValues)

    def getDataReceivePointByValues(self) -> List[VariableAccess]:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The result is passed back to the application by means of the return value.
        The aggregation of dataReceivePointByValue is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of data receive points in the implementation.

        Returns:
            List[VariableAccess]: The list of data receive points by value
        """
        return sorted(self.dataReceivePointByValues, key=lambda v: v.short_name)

    def createDataSendPoint(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has explicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The aggregation of dataSendPoint is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data send points in the implementation.

        Args:
            short_name: The short name of the data send point

        Returns:
            VariableAccess: the created or existing VariableAccess
        """
        return self._createVariableAccess(short_name, self.dataSendPoints)

    def getDataSendPoints(self) -> List[VariableAccess]:
        """
        RunnableEntity has explicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype.
        The aggregation of dataSendPoint is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data send points in the implementation.

        Returns:
            List[VariableAccess]: The list of data send points
        """
        return self.dataSendPoints

    def createReadLocalVariable(self, short_name: str) -> VariableAccess:
        """
        The presence of a readLocalVariable implies that a RunnableEntity needs read access to a VariableDataPrototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable.
        The aggregation of readLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicitInterRunnableVariable or the variant existence of readLocalVariable (points) in the implementation.

        Args:
            short_name: The short name of the read local variable

        Returns:
            VariableAccess: the created or existing VariableAccess
        """
        return self._createVariableAccess(short_name, self.readLocalVariables)

    def getReadLocalVariables(self) -> List[VariableAccess]:
        """
        The presence of a readLocalVariable implies that a RunnableEntity needs read access to a VariableDataPrototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable.
        The aggregation of readLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicitInterRunnableVariable or the variant existence of readLocalVariable (points) in the implementation.

        Returns:
            List[VariableAccess]: The list of read local variables
        """
        return self.readLocalVariables

    def createWrittenLocalVariable(self, short_name: str) -> VariableAccess:
        """
        The presence of a writtenLocalVariable implies that a RunnableEntity needs write access to a VariableDataPrototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable.
        The aggregation of writtenLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicitInterRunnableVariable or the variant existence of writtenLocalVariable (points) in the implementation.

        Args:
            short_name: The short name of the written local variable

        Returns:
            VariableAccess: the created or existing VariableAccess
        """
        return self._createVariableAccess(short_name, self.writtenLocalVariables)

    def getWrittenLocalVariables(self) -> List[VariableAccess]:
        """
        The presence of a writtenLocalVariable implies that a RunnableEntity needs write access to a VariableDataPrototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable.
        The aggregation of writtenLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicitInterRunnableVariable or the variant existence of writtenLocalVariable (points) in the implementation.

        Returns:
            List[VariableAccess]: The list of written local variables
        """
        return self.writtenLocalVariables

    def getParameterAccesses(self) -> List[ParameterAccess]:
        """
        The presence of a ParameterAccess implies that a RunnableEntity needs read only access to a ParameterDataPrototype which may either be local or within a PortPrototype.
        The aggregation of ParameterAccess is subject to variability with the purpose to support the conditional existence of parameter ports and component local parameters as well as the variant existence of ParameterAccess (points) in the implementation.

        Returns:
            List[ParameterAccess]: The list of parameter accesses
        """
        return list(sorted(filter(lambda a: isinstance(a, ParameterAccess), self.elements), key=lambda o: o.short_name))

    def createParameterAccess(self, short_name: str) -> ParameterAccess:
        """
        The presence of a ParameterAccess implies that a RunnableEntity needs read only access to a ParameterDataPrototype which may either be local or within a PortPrototype.
        The aggregation of ParameterAccess is subject to variability with the purpose to support the conditional existence of parameter ports and component local parameters as well as the variant existence of ParameterAccess (points) in the implementation.

        Args:
            short_name: The short name of the parameter access

        Returns:
            ParameterAccess: the created or existing ParameterAccess
        """
        if not self.IsElementExists(short_name, ParameterAccess):
            access = ParameterAccess(self, short_name)
            self.addElement(access)
        return self.getElement(short_name, ParameterAccess)

    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        """
        The RunnableEntity has a ServerCallPoint.
        The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation.

        Args:
            short_name: The short name of the synchronous server call point

        Returns:
            SynchronousServerCallPoint: the created or existing SynchronousServerCallPoint
        """
        if short_name not in self.serverCallPoints:
            point = SynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        """
        The RunnableEntity has a ServerCallPoint.
        The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation.

        Args:
            short_name: The short name of the asynchronous server call point

        Returns:
            AsynchronousServerCallPoint: the created or existing AsynchronousServerCallPoint
        """
        if short_name not in self.serverCallPoints:
            point = AsynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name, AsynchronousServerCallPoint)

    def createAsynchronousServerCallResultPoint(self, short_name: str) -> AsynchronousServerCallResultPoint:
        """
        The server call result point admits a runnable to fetch the result of an asynchronous server call.
        The aggregation of AsynchronousServerCallResultPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes and the variant existence of server call result points in the implementation.

        Args:
            short_name: The short name of the asynchronous server call result point

        Returns:
            AsynchronousServerCallResultPoint: the created or existing AsynchronousServerCallResultPoint
        """
        if short_name not in self.serverCallPoints:
            point = AsynchronousServerCallResultPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)

    def getSynchronousServerCallPoint(self) -> List[SynchronousServerCallPoint]:
        """
        The RunnableEntity has a ServerCallPoint.
        The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation.

        Returns:
            List[SynchronousServerCallPoint]: The list of synchronous server call points
        """
        return list(sorted(filter(lambda a: isinstance(a, SynchronousServerCallPoint), self.elements), key=lambda o: o.getShortName()))

    def getAsynchronousServerCallPoint(self) -> List[AsynchronousServerCallPoint]:
        """
        The RunnableEntity has a ServerCallPoint.
        The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation.

        Returns:
            List[AsynchronousServerCallPoint]: The list of asynchronous server call points
        """
        return list(sorted(filter(lambda a: isinstance(a, AsynchronousServerCallPoint), self.elements), key=lambda o: o.getShortName()))

    def getAsynchronousServerCallResultPoints(self) -> List[AsynchronousServerCallResultPoint]:
        """
        The server call result point admits a runnable to fetch the result of an asynchronous server call.
        The aggregation of AsynchronousServerCallResultPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes and the variant existence of server call result points in the implementation.

        Returns:
            List[AsynchronousServerCallResultPoint]: The list of asynchronous server call result points
        """
        return list(sorted(filter(lambda a: isinstance(a, AsynchronousServerCallResultPoint), self.elements), key=lambda o: o.getShortName()))  # noqa E501

    def getServerCallPoints(self) -> List[ServerCallPoint]:
        """
        The RunnableEntity has a ServerCallPoint.
        The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation.

        Returns:
            List[ServerCallPoint]: The list of server call points
        """
        return list(sorted(filter(lambda a: isinstance(a, ServerCallPoint), self.elements), key=lambda o: o.getShortName()))

    def createInternalTriggeringPoint(self, short_name: str) -> InternalTriggeringPoint:
        """
        The aggregation of InternalTriggeringPoint is subject to variability with the purpose to support the variant existence of internal triggering points in the implementation.

        Args:
            short_name: The short name of the internal triggering point

        Returns:
            InternalTriggeringPoint: the created or existing InternalTriggeringPoint
        """
        if not self.IsElementExists(short_name, InternalTriggeringPoint):
            point = InternalTriggeringPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name, InternalTriggeringPoint)

    def getInternalTriggeringPoints(self) -> List[InternalTriggeringPoint]:
        """
        The aggregation of InternalTriggeringPoint is subject to variability with the purpose to support the variant existence of internal triggering points in the implementation.

        Returns:
            List[InternalTriggeringPoint]: The list of internal triggering points
        """
        return filter(lambda o: isinstance(o, InternalTriggeringPoint), self.elements)

    def getExternalTriggeringPoints(self) -> List[ExternalTriggeringPoint]:
        """
        The aggregation of ExternalTriggeringPoint is subject to variability with the purpose to support the conditional existence of trigger ports or the variant existence of external triggering points in the implementation.

        Returns:
            List[ExternalTriggeringPoint]: The list of external triggering points
        """
        return self.externalTriggeringPoints

    def addExternalTriggeringPoint(self, value: Optional[ExternalTriggeringPoint]) -> "RunnableEntity":
        """
        The aggregation of ExternalTriggeringPoint is subject to variability with the purpose to support the conditional existence of trigger ports or the variant existence of external triggering points in the implementation.
        A None value is a no-op and does not append to externalTriggeringPoints.

        Args:
            value: The external triggering point to add

        Returns:
            RunnableEntity: self for method chaining
        """
        if value is not None:
            self.externalTriggeringPoints.append(value)
        return self

    def getModeAccessPoints(self) -> List[ModeAccessPoint]:
        """
        The runnable has a mode access point.
        The aggregation of ModeAccessPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode access points in the implementation.

        Returns:
            List[ModeAccessPoint]: The list of mode access points
        """
        return self.modeAccessPoints

    def addModeAccessPoint(self, value: Optional[ModeAccessPoint]) -> "RunnableEntity":
        """
        The runnable has a mode access point.
        The aggregation of ModeAccessPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode access points in the implementation.
        A None value is a no-op and does not append to modeAccessPoints.

        Args:
            value: The mode access point to add

        Returns:
            RunnableEntity: self for method chaining
        """
        if value is not None:
            self.modeAccessPoints.append(value)
        return self

    def getModeSwitchPoints(self) -> List[ModeSwitchPoint]:
        """
        The runnable has a mode switch point.
        The aggregation of ModeSwitchPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode switch points in the implementation.

        Returns:
            List[ModeSwitchPoint]: The list of mode switch points
        """
        return list(sorted(filter(lambda a: isinstance(a, ModeSwitchPoint), self.elements), key=lambda o: o.short_name))

    def createModeSwitchPoint(self, short_name: str) -> ModeSwitchPoint:
        """
        The runnable has a mode switch point.
        The aggregation of ModeSwitchPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode switch points in the implementation.

        Args:
            short_name: The short name of the mode switch point

        Returns:
            ModeSwitchPoint: the created or existing ModeSwitchPoint
        """
        if not self.IsElementExists(short_name, ModeSwitchPoint):
            access = ModeSwitchPoint(self, short_name)
            self.addElement(access)
            self.modeSwitchPoints.append(access)
        return self.getElement(short_name, ModeSwitchPoint)

    def getSymbol(self) -> Optional[ARLiteral]:
        """
        The symbol describing this RunnableEntity's entry point. This is considered the API of the RunnableEntity and is required during the RTE contract phase.

        Returns:
            Optional[ARLiteral]: The symbol, or None if not set
        """
        return self.symbol

    def setSymbol(self, value: Optional[ARLiteral]) -> "RunnableEntity":
        """
        The symbol describing this RunnableEntity's entry point. This is considered the API of the RunnableEntity and is required during the RTE contract phase.
        A None value is a no-op and does not overwrite an existing symbol.

        Args:
            value: The symbol to set

        Returns:
            RunnableEntity: self for method chaining
        """
        if value is not None:
            self.symbol = value
        return self

    def createWaitPoint(self, short_name: str) -> WaitPoint:
        """
        The WaitPoint associated with the RunnableEntity.

        Args:
            short_name: The short name of the WaitPoint

        Returns:
            WaitPoint: the created or existing WaitPoint
        """
        if not self.IsElementExists(short_name, WaitPoint):
            point = WaitPoint(self, short_name)
            self.addElement(point)
            self.waitPoints.append(point)
        return self.getElement(short_name, WaitPoint)

    def getWaitPoints(self) -> List[WaitPoint]:
        """
        The WaitPoint associated with the RunnableEntity.

        Returns:
            List[WaitPoint]: The list of wait points
        """
        return self.waitPoints


class SwcExclusiveAreaPolicy(ARObject, VariationPointCapable):
    """
    Options how to generate the ExclusiveArea related APIs. If no
    SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values
    apply.
    """

    # SwcExclusiveAreaPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.28, p.556
    # Spec verified: R23-11
    # [x] __init__             [x] impl  [x] docstring  [x] test
    # [x] getApiPrinciple      [x] impl  [x] docstring  [x] test
    # [x] setApiPrinciple      [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaRef  [x] impl  [x] docstring  [x] test
    # [x] setExclusiveAreaRef  [x] impl  [x] docstring  [x] test

    def __init__(self):
        super().__init__()

        # Specifies for this ExclusiveArea if either one common set of Enter
        # and Exit APIs for the whole software component is requested from the
        # Rte or if the set of Enter and Exit APIs is expected per
        # RunnableEntity. The default value is "common".
        self.apiPrinciple: Optional[ApiPrincipleEnum] = None

        # This reference represents the ExclusiveArea for which the policy
        # applies.
        self.exclusiveAreaRef: Optional[RefType] = None

    def getApiPrinciple(self) -> Optional[ApiPrincipleEnum]:
        """Gets the apiPrinciple (common vs per-RunnableEntity API generation) for this policy."""
        return self.apiPrinciple

    def setApiPrinciple(self, value: Optional[ApiPrincipleEnum]) -> "SwcExclusiveAreaPolicy":
        """
        Sets the apiPrinciple (common vs per-RunnableEntity API generation) for
        this policy. A None value is a no-op and does not overwrite an existing
        apiPrinciple.
        """
        if value is not None:
            self.apiPrinciple = value
        return self

    def getExclusiveAreaRef(self) -> Optional[RefType]:
        """Gets the reference to the ExclusiveArea for which this policy applies."""
        return self.exclusiveAreaRef

    def setExclusiveAreaRef(self, value: Optional[RefType]) -> "SwcExclusiveAreaPolicy":
        """
        Sets the reference to the ExclusiveArea for which this policy applies.
        A None value is a no-op and does not overwrite an existing
        exclusiveAreaRef.
        """
        if value is not None:
            self.exclusiveAreaRef = value
        return self


class SwcInternalBehavior(InternalBehavior, VariationPointCapable):
    """
    The SwcInternalBehavior of an AtomicSwComponentType describes the relevant aspects of the software-component with respect to the RTE, i.e. the RunnableEntities and the RTEEvents they respond to.
    """

    # SwcInternalBehavior method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.2, p.521 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf, Table 7.3, p.536 (R4.3.1)
    # Spec verified: R23-11
    # Deviations:
    #   legacy handleTerminationAndRestart (R4.3.1 Table 7.3, p.536); removed in R23-11 (XSD atp.Status="removed").
    #   Absent from the R23-11 Table 7.2 attribute rows; kept as an optional legacy member with full
    #   reader/writer coverage (Rule 0019 combine case). Accepted at Step 9b.
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # Legacy: handleTerminationAndRestart is absent from the R23-11 table (XSD atp.Status="removed");
    #          its value domain is the R4.3.1 HandleTerminationAndRestartEnum, so those rows cite R4.3.1.
    # [x] __init__                                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArTypedPerInstanceMemories                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createArTypedPerInstanceMemory               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExplicitInterRunnableVariables            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createExplicitInterRunnableVariable          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHandleTerminationAndRestart               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setHandleTerminationAndRestart               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getImplicitInterRunnableVariables            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createImplicitInterRunnableVariable          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPerInstanceMemories                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createPerInstanceMemory                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPerInstanceParameters                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createPerInstanceParameter                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSharedParameters                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSharedParameter                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPortAPIOption                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortAPIOptions                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addIncludedDataTypeSet                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIncludedDataTypeSets                      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addIncludedModeDeclarationGroupSet           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIncludedModeDeclarationGroupSets          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addExclusiveAreaPolicy                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExclusiveAreaPolicies                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createOperationInvokedEvent                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createTimingEvent                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createInitEvent                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createAsynchronousServerCallReturnsEvent     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDataReceivedEvent                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSwcModeSwitchEvent                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createInternalTriggerOccurredEvent           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createModeSwitchedAckEvent                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createBackgroundEvent                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDataSendCompletedEvent                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSwcServiceDependency                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRteEvents                                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getOperationInvokedEvents                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInitEvents                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTimingEvents                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataReceivedEvents                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwcModeSwitchEvents                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInternalTriggerOccurredEvents             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getModeSwitchedAckEvents                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBackgroundEvents                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataSendCompletedEvents                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwcServiceDependencies                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEvent                                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getVariableDataPrototypes                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createRunnableEntity                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRunnableEntities                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRunnableEntity                            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getSupportsMultipleInstantiation             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportsMultipleInstantiation             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addInstantiationDataDefProps                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInstantiationDataDefPropss                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addVariationPointProxy                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVariationPointProxies                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines an AUTOSAR typed memory-block that needs to be available for each instance of the SW-component. This is typically only useful if supportsMultipleInstantiation is set to "true" or if the component defines NVRAM access via permanent blocks. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the software component's implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=arTypedPerInstanceMemory.shortName, ar TypedPerInstanceMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.arTypedPerInstanceMemories: List[VariableDataPrototype] = []

        # This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        self.events: List[RTEEvent] = []

        # Options how to generate the ExclusiveArea related APIs. When no SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values apply. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveAreaPolicy, exclusiveArea Policy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.exclusiveAreaPolicies: List[SwcExclusiveAreaPolicy] = []

        # Implement state message semantics for establishing communication among runnables of the same component. The aggregation of explicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=explicitInterRunnableVariable.shortName, explicitInterRunnableVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.explicitInterRunnableVariables: List[VariableDataPrototype] = []

        # This attribute controls the behavior with respect to stopping and restarting. The corresponding AtomicSwComponentType may either not support stop and restart, or support only stop, or support both stop and restart.
        self.handleTerminationAndRestart: Optional[ARLiteral] = None

        # Implement state message semantics for establishing communication among runnables of the same component. The aggregation of implicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=implicitInterRunnableVariable.shortName, implicitInterRunnableVariable.variationPoint.shortLabel
        self.implicitInterRunnableVariables: List[VariableDataPrototype] = []

        # The includedDataTypeSet is used by a software component for its implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=includedDataTypeSet
        self.includedDataTypeSets: List[IncludedDataTypeSet] = []

        # This aggregation represents the included Mode DeclarationGroups Stereotypes: atpSplitable Tags: atp.Splitkey=includedModeDeclarationGroupSet
        self.includedModeDeclarationGroupSets: List[IncludedModeDeclarationGroupSet] = []

        # The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of Port Prototypes and component local memories like "per InstanceParameter" or "arTypedPerInstanceMemory". Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instantiationDataDefProps, instantiationData DefProps.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.instantiationDataDefProps: List[InstantiationDataDefProps] = []

        # Defines a per-instance memory object needed by this software component. The aggregation of PerInstance Memory is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceMemory.shortName, perInstance Memory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.perInstanceMemories: List[PerInstanceMemory] = []

        # Defines parameter(s) or characteristic value(s) that needs to be available for each instance of the software-component. This is typically only useful if supportsMultipleInstantiation is set to "true". The aggregation of perInstanceParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceParameter.shortName, per InstanceParameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.perInstanceParameters: List[ParameterDataPrototype] = []

        # Options for generating the signature of port-related calls from a runnable to the RTE and vice versa. The aggregation of PortPrototypes is subject to variability with the purpose to support the conditional existence of ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portAPIOption, portAPIOption.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.portAPIOptions: List[PortAPIOption] = []

        # This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.runnables: List[RunnableEntity] = []

        # Defines the requirements on AUTOSAR Services for a particular item. The aggregation of SwcServiceDependency is subject to variability with the purpose to support the conditional existence of ports as well as the conditional existence of ServiceNeeds. The SwcServiceDependency owned by an SwcInternal Behavior can be located in a different physical file in order to support that SwcServiceDependency might be provided in later development steps or even by different expert domain (e.g OBD expert for Obd related Service Needs) tools. Therefore the aggregation is <<atp Splitable>>. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serviceDependency.shortName, service Dependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.serviceDependencies: List[SwcServiceDependency] = []

        # Defines parameter(s) or characteristic value(s) shared between SwComponentPrototypes of the same Sw ComponentType The aggregation of sharedParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sharedParameter.shortName, shared Parameter.variationPoint.shortLabel
        self.sharedParameters: List[ParameterDataPrototype] = []

        # Indicate whether the corresponding software-component can be multiply instantiated on one ECU. In this case the attribute will result in an appropriate component API on programming language level (with or without instance handle).
        self.supportsMultipleInstantiation: Optional[Boolean] = None

        # Proxy of a variation points in the C/C++ implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=variationPointProxy.shortName
        self.variationPointProxies: List[VariationPointProxy] = []

    def getArTypedPerInstanceMemories(self) -> List[VariableDataPrototype]:
        """
        Defines an AUTOSAR typed memory-block that needs to be available for each instance of the SW-component. This is typically only useful if supportsMultipleInstantiation is set to "true" or if the component defines NVRAM access via permanent blocks. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the software component's implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=arTypedPerInstanceMemory.shortName, ar TypedPerInstanceMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.arTypedPerInstanceMemories

    def createArTypedPerInstanceMemory(self, short_name: str) -> VariableDataPrototype:
        """
        Defines an AUTOSAR typed memory-block that needs to be available for each instance of the SW-component. This is typically only useful if supportsMultipleInstantiation is set to "true" or if the component defines NVRAM access via permanent blocks. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the software component's implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=arTypedPerInstanceMemory.shortName, ar TypedPerInstanceMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.arTypedPerInstanceMemories.append(prototype)
        return self.getElement(short_name, VariableDataPrototype)

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        """
        Implement state message semantics for establishing communication among runnables of the same component. The aggregation of explicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=explicitInterRunnableVariable.shortName, explicitInterRunnableVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.explicitInterRunnableVariables

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        """
        Implement state message semantics for establishing communication among runnables of the same component. The aggregation of explicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=explicitInterRunnableVariable.shortName, explicitInterRunnableVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.explicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name, VariableDataPrototype)

    def getHandleTerminationAndRestart(self) -> Optional[ARLiteral]:
        """
        This attribute controls the behavior with respect to stopping and restarting. The corresponding AtomicSwComponentType may either not support stop and restart, or support only stop, or support both stop and restart.
        """
        return self.handleTerminationAndRestart

    def setHandleTerminationAndRestart(self, value: Optional[ARLiteral]) -> "SwcInternalBehavior":
        """
        This attribute controls the behavior with respect to stopping and restarting. The corresponding AtomicSwComponentType may either not support stop and restart, or support only stop, or support both stop and restart. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.handleTerminationAndRestart = value
        return self

    def getImplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        """
        Implement state message semantics for establishing communication among runnables of the same component. The aggregation of implicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=implicitInterRunnableVariable.shortName, implicitInterRunnableVariable.variationPoint.shortLabel
        """
        return self.implicitInterRunnableVariables

    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        """
        Implement state message semantics for establishing communication among runnables of the same component. The aggregation of implicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=implicitInterRunnableVariable.shortName, implicitInterRunnableVariable.variationPoint.shortLabel
        """
        if not self.IsElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.implicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name, VariableDataPrototype)

    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        """
        Defines a per-instance memory object needed by this software component. The aggregation of PerInstance Memory is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceMemory.shortName, perInstance Memory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.perInstanceMemories

    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        """
        Defines a per-instance memory object needed by this software component. The aggregation of PerInstance Memory is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceMemory.shortName, perInstance Memory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, PerInstanceMemory):
            memory = PerInstanceMemory(self, short_name)
            self.addElement(memory)
            self.perInstanceMemories.append(memory)
        return self.getElement(short_name, PerInstanceMemory)

    def getPerInstanceParameters(self) -> List[ParameterDataPrototype]:
        """
        Defines parameter(s) or characteristic value(s) that needs to be available for each instance of the software-component. This is typically only useful if supportsMultipleInstantiation is set to "true". The aggregation of perInstanceParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceParameter.shortName, per InstanceParameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.perInstanceParameters

    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        """
        Defines parameter(s) or characteristic value(s) that needs to be available for each instance of the software-component. This is typically only useful if supportsMultipleInstantiation is set to "true". The aggregation of perInstanceParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceParameter.shortName, per InstanceParameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, ParameterDataPrototype):
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.perInstanceParameters.append(prototype)
        return self.getElement(short_name, ParameterDataPrototype)

    def getSharedParameters(self) -> List[ParameterDataPrototype]:
        """
        Defines parameter(s) or characteristic value(s) shared between SwComponentPrototypes of the same Sw ComponentType The aggregation of sharedParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sharedParameter.shortName, shared Parameter.variationPoint.shortLabel
        """
        return self.sharedParameters

    def createSharedParameter(self, short_name: str) -> ParameterDataPrototype:
        """
        Defines parameter(s) or characteristic value(s) shared between SwComponentPrototypes of the same Sw ComponentType The aggregation of sharedParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sharedParameter.shortName, shared Parameter.variationPoint.shortLabel
        """
        if not self.IsElementExists(short_name, ParameterDataPrototype):
            memory = ParameterDataPrototype(self, short_name)
            self.addElement(memory)
            self.sharedParameters.append(memory)
        return self.getElement(short_name, ParameterDataPrototype)

    def addPortAPIOption(self, value: Optional[PortAPIOption]) -> "SwcInternalBehavior":
        """
        Options for generating the signature of port-related calls from a runnable to the RTE and vice versa. The aggregation of PortPrototypes is subject to variability with the purpose to support the conditional existence of ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portAPIOption, portAPIOption.variation Point.shortLabel vh.latestBindingTime=preCompileTime A None value is a no-op and does not append to portAPIOptions.
        """
        if value is not None:
            self.portAPIOptions.append(value)
        return self

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        """
        Options for generating the signature of port-related calls from a runnable to the RTE and vice versa. The aggregation of PortPrototypes is subject to variability with the purpose to support the conditional existence of ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portAPIOption, portAPIOption.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.portAPIOptions

    def addIncludedDataTypeSet(self, value: Optional[IncludedDataTypeSet]) -> "SwcInternalBehavior":
        """
        The includedDataTypeSet is used by a software component for its implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=includedDataTypeSet A None value is a no-op and does not append to includedDataTypeSets.
        """
        if value is not None:
            self.includedDataTypeSets.append(value)
        return self

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        """
        The includedDataTypeSet is used by a software component for its implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=includedDataTypeSet
        """
        return self.includedDataTypeSets

    def addIncludedModeDeclarationGroupSet(self, value: Optional[IncludedModeDeclarationGroupSet]) -> "SwcInternalBehavior":
        """
        This aggregation represents the included Mode DeclarationGroups Stereotypes: atpSplitable Tags: atp.Splitkey=includedModeDeclarationGroupSet A None value is a no-op and does not append to includedModeDeclarationGroupSets.
        """
        if value is not None:
            self.includedModeDeclarationGroupSets.append(value)
        return self

    def getIncludedModeDeclarationGroupSets(self) -> List[IncludedModeDeclarationGroupSet]:
        """
        This aggregation represents the included Mode DeclarationGroups Stereotypes: atpSplitable Tags: atp.Splitkey=includedModeDeclarationGroupSet
        """
        return self.includedModeDeclarationGroupSets

    def addExclusiveAreaPolicy(self, value: Optional[SwcExclusiveAreaPolicy]) -> "SwcInternalBehavior":
        """
        Options how to generate the ExclusiveArea related APIs. When no SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values apply. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveAreaPolicy, exclusiveArea Policy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime A None value is a no-op and does not append to exclusiveAreaPolicies.
        """
        if value is not None:
            self.exclusiveAreaPolicies.append(value)
        return self

    def getExclusiveAreaPolicies(self) -> List[SwcExclusiveAreaPolicy]:
        """
        Options how to generate the ExclusiveArea related APIs. When no SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values apply. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveAreaPolicy, exclusiveArea Policy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.exclusiveAreaPolicies

    def createOperationInvokedEvent(self, short_name: str) -> OperationInvokedEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, OperationInvokedEvent):
            event = OperationInvokedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, OperationInvokedEvent)

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, TimingEvent):
            event = TimingEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, TimingEvent)

    def createInitEvent(self, short_name: str) -> InitEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, InitEvent):
            event = InitEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, InitEvent)

    def createAsynchronousServerCallReturnsEvent(self, short_name: str) -> AsynchronousServerCallReturnsEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, AsynchronousServerCallReturnsEvent):
            event = AsynchronousServerCallReturnsEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, AsynchronousServerCallReturnsEvent)

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, DataReceivedEvent):
            event = DataReceivedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, DataReceivedEvent)

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, SwcModeSwitchEvent):
            event = SwcModeSwitchEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, SwcModeSwitchEvent)

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, InternalTriggerOccurredEvent):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, InternalTriggerOccurredEvent)

    def createModeSwitchedAckEvent(self, short_name: str) -> ModeSwitchedAckEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, ModeSwitchedAckEvent):
            event = ModeSwitchedAckEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, ModeSwitchedAckEvent)

    def createBackgroundEvent(self, short_name: str) -> BackgroundEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, BackgroundEvent):
            event = BackgroundEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BackgroundEvent)

    def createDataSendCompletedEvent(self, short_name: str) -> DataSendCompletedEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, DataSendCompletedEvent):
            event = DataSendCompletedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, DataSendCompletedEvent)

    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        """
        Defines the requirements on AUTOSAR Services for a particular item. The aggregation of SwcServiceDependency is subject to variability with the purpose to support the conditional existence of ports as well as the conditional existence of ServiceNeeds. The SwcServiceDependency owned by an SwcInternal Behavior can be located in a different physical file in order to support that SwcServiceDependency might be provided in later development steps or even by different expert domain (e.g OBD expert for Obd related Service Needs) tools. Therefore the aggregation is <<atp Splitable>>. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serviceDependency.shortName, service Dependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, SwcServiceDependency):
            event = SwcServiceDependency(self, short_name)
            self.addElement(event)
            self.serviceDependencies.append(event)
        return self.getElement(short_name, SwcServiceDependency)

    def getRteEvents(self) -> List[RTEEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(self.events, key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, OperationInvokedEvent), self.events), key=lambda e: e.short_name)

    def getInitEvents(self) -> List[InitEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, InitEvent), self.events), key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, TimingEvent), self.events), key=lambda e: e.short_name)

    def getDataReceivedEvents(self) -> List[DataReceivedEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, DataReceivedEvent), self.events), key=lambda e: e.short_name)

    def getSwcModeSwitchEvents(self) -> List[SwcModeSwitchEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, SwcModeSwitchEvent), self.events), key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, InternalTriggerOccurredEvent), self.events), key=lambda e: e.short_name)

    def getModeSwitchedAckEvents(self) -> List[ModeSwitchedAckEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, ModeSwitchedAckEvent), self.events), key=lambda e: e.short_name)

    def getBackgroundEvents(self) -> List[BackgroundEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, BackgroundEvent), self.events), key=lambda e: e.short_name)

    def getDataSendCompletedEvents(self) -> List[DataSendCompletedEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(filter(lambda c: isinstance(c, DataSendCompletedEvent), self.events), key=lambda e: e.short_name)

    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        """
        Defines the requirements on AUTOSAR Services for a particular item. The aggregation of SwcServiceDependency is subject to variability with the purpose to support the conditional existence of ports as well as the conditional existence of ServiceNeeds. The SwcServiceDependency owned by an SwcInternal Behavior can be located in a different physical file in order to support that SwcServiceDependency might be provided in later development steps or even by different expert domain (e.g OBD expert for Obd related Service Needs) tools. Therefore the aggregation is <<atp Splitable>>. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serviceDependency.shortName, service Dependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return sorted(self.serviceDependencies, key=lambda e: e.short_name)

    def getEvent(self, short_name: str) -> RTEEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return self.getElement(short_name, RTEEvent)

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        """Gets all VariableDataPrototype instances owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements), key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        """
        This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsElementExists(short_name, RunnableEntity):
            runnable = RunnableEntity(self, short_name)
            self.addElement(runnable)
            self.runnables.append(runnable)
        return self.getElement(short_name, RunnableEntity)

    def getRunnableEntities(self) -> List[RunnableEntity]:
        """
        This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """
        return sorted(self.runnables, key=lambda r: r.short_name)

    def getRunnableEntity(self, short_name: str) -> RunnableEntity:
        """
        This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.getElement(short_name, RunnableEntity)

    def getSupportsMultipleInstantiation(self) -> Optional[Boolean]:
        """
        Indicate whether the corresponding software-component can be multiply instantiated on one ECU. In this case the attribute will result in an appropriate component API on programming language level (with or without instance handle).
        """
        return self.supportsMultipleInstantiation

    def setSupportsMultipleInstantiation(self, value: Optional[Boolean]) -> "SwcInternalBehavior":
        """
        Indicate whether the corresponding software-component can be multiply instantiated on one ECU. In this case the attribute will result in an appropriate component API on programming language level (with or without instance handle). A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.supportsMultipleInstantiation = value
        return self

    def addInstantiationDataDefProps(self, value: Optional[InstantiationDataDefProps]) -> "SwcInternalBehavior":
        """
        The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of Port Prototypes and component local memories like "per InstanceParameter" or "arTypedPerInstanceMemory". Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instantiationDataDefProps, instantiationData DefProps.variationPoint.shortLabel vh.latestBindingTime=preCompileTime A None value is a no-op and does not append to instantiationDataDefProps.
        """
        if value is not None:
            self.instantiationDataDefProps.append(value)
        return self

    def getInstantiationDataDefPropss(self) -> List[InstantiationDataDefProps]:
        """
        The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of Port Prototypes and component local memories like "per InstanceParameter" or "arTypedPerInstanceMemory". Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instantiationDataDefProps, instantiationData DefProps.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.instantiationDataDefProps

    def addVariationPointProxy(self, value: Optional[VariationPointProxy]) -> "SwcInternalBehavior":
        """
        Proxy of a variation points in the C/C++ implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=variationPointProxy.shortName A None value is a no-op and does not append to variationPointProxies.
        """
        if value is not None:
            self.variationPointProxies.append(value)
        return self

    def getVariationPointProxies(self) -> List[VariationPointProxy]:
        """
        Proxy of a variation points in the C/C++ implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=variationPointProxy.shortName
        """
        return self.variationPointProxies
