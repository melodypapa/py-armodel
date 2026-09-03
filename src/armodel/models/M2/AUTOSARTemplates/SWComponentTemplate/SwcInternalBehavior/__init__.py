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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntity import RunnableEntityArgument
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
    The SwcInternalBehavior of an AtomicSwComponentType describes the
    relevant aspects of the software-component with respect to the RTE, i.e.
    the RunnableEntities and the RTEEvents they respond to.
    """

    # SwcInternalBehavior method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.2, p.518
    # [x] __init__                                   [x] impl  [x] docstring  [x] test
    # [x] getArTypedPerInstanceMemories              [x] impl  [x] docstring  [x] test
    # [x] createArTypedPerInstanceMemory             [x] impl  [x] docstring  [x] test
    # [x] addExclusiveAreaPolicy                     [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaPolicies                   [x] impl  [x] docstring  [x] test
    # [x] getExplicitInterRunnableVariables          [x] impl  [x] docstring  [x] test
    # [x] createExplicitInterRunnableVariable        [x] impl  [x] docstring  [x] test
    # [x] getHandleTerminationAndRestart             [x] impl  [x] docstring  [x] test
    # [x] setHandleTerminationAndRestart             [x] impl  [x] docstring  [x] test
    # [x] getImplicitInterRunnableVariables          [x] impl  [x] docstring  [x] test
    # [x] createImplicitInterRunnableVariable        [x] impl  [x] docstring  [x] test
    # [x] getPerInstanceMemories                     [x] impl  [x] docstring  [x] test
    # [x] createPerInstanceMemory                    [x] impl  [x] docstring  [x] test
    # [x] getPerInstanceParameters                   [x] impl  [x] docstring  [x] test
    # [x] createPerInstanceParameter                 [x] impl  [x] docstring  [x] test
    # [x] getSharedParameters                        [x] impl  [x] docstring  [x] test
    # [x] createSharedParameter                      [x] impl  [x] docstring  [x] test
    # [x] addPortAPIOption                           [x] impl  [x] docstring  [x] test
    # [x] getPortAPIOptions                          [x] impl  [x] docstring  [x] test
    # [x] addIncludedDataTypeSet                     [x] impl  [x] docstring  [x] test
    # [x] getIncludedDataTypeSets                    [x] impl  [x] docstring  [x] test
    # [x] addIncludedModeDeclarationGroupSet         [x] impl  [x] docstring  [x] test
    # [x] getIncludedModeDeclarationGroupSets        [x] impl  [x] docstring  [x] test
    # [x] createOperationInvokedEvent                [x] impl  [x] docstring  [x] test
    # [x] createTimingEvent                          [x] impl  [x] docstring  [x] test
    # [x] createInitEvent                            [x] impl  [x] docstring  [x] test
    # [x] createAsynchronousServerCallReturnsEvent   [x] impl  [x] docstring  [x] test
    # [x] createDataReceivedEvent                    [x] impl  [x] docstring  [x] test
    # [x] createSwcModeSwitchEvent                   [x] impl  [x] docstring  [x] test
    # [x] createInternalTriggerOccurredEvent         [x] impl  [x] docstring  [x] test
    # [x] createModeSwitchedAckEvent                 [x] impl  [x] docstring  [x] test
    # [x] createBackgroundEvent                      [x] impl  [x] docstring  [x] test
    # [x] createDataSendCompletedEvent               [x] impl  [x] docstring  [x] test
    # [x] getRteEvents                               [x] impl  [x] docstring  [x] test
    # [x] getOperationInvokedEvents                  [x] impl  [x] docstring  [x] test
    # [x] getInitEvents                              [x] impl  [x] docstring  [x] test
    # [x] getTimingEvents                            [x] impl  [x] docstring  [x] test
    # [x] getDataReceivedEvents                      [x] impl  [x] docstring  [x] test
    # [x] getSwcModeSwitchEvents                     [x] impl  [x] docstring  [x] test
    # [x] getInternalTriggerOccurredEvents           [x] impl  [x] docstring  [x] test
    # [x] getModeSwitchedAckEvents                   [x] impl  [x] docstring  [x] test
    # [x] getBackgroundEvents                        [x] impl  [x] docstring  [x] test
    # [x] getDataSendCompletedEvents                 [x] impl  [x] docstring  [x] test
    # [x] getEvent                                   [x] impl  [x] docstring  [x] test
    # [x] createSwcServiceDependency                 [x] impl  [x] docstring  [x] test
    # [x] getSwcServiceDependencies                  [x] impl  [x] docstring  [x] test
    # [x] getVariableDataPrototypes                  [x] impl  [x] docstring  [x] test
    # [x] createRunnableEntity                       [x] impl  [x] docstring  [x] test
    # [x] getRunnableEntities                        [x] impl  [x] docstring  [x] test
    # [x] getRunnableEntity                          [x] impl  [x] docstring  [x] test
    # [x] getSupportsMultipleInstantiation           [x] impl  [x] docstring  [x] test
    # [x] setSupportsMultipleInstantiation           [x] impl  [x] docstring  [x] test
    # [x] addInstantiationDataDefProps               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInstantiationDataDefPropss              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addVariationPointProxy                     [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer
    # [x] getVariationPointProxies                   [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines an AUTOSAR typed memory-block that needs to be available for
        # each instance of the SW-component.
        self.arTypedPerInstanceMemories: List[VariableDataPrototype] = []

        # This is a RTEEvent specified for the particular Swc InternalBehavior.
        # RTEEvents are registered through the create*Event factories and are
        # retrieved from the elements registry via getRteEvents / getEvent.
        self.events: List[RTEEvent] = []

        # Options how to generate the ExclusiveArea related APIs.
        self.exclusiveAreaPolicies: List[SwcExclusiveAreaPolicy] = []

        # Implement state message semantics for establishing communication
        # among runnables of the same component.
        self.explicitInterRunnableVariables: List[VariableDataPrototype] = []

        # Controls the behavior with respect to stopping and restarting; the
        # corresponding AtomicSwComponentType may either not support stop and
        # restart, or support only stop, or support both. (Present in the XSD,
        # absent from the PDF table rendering; PDF enum
        # HandleTerminationAndRestartEnum not modeled, carried as ARLiteral.)
        self.handleTerminationAndRestart: Optional[ARLiteral] = None

        # Implement state message semantics for establishing communication
        # among runnables of the same component.
        self.implicitInterRunnableVariables: List[VariableDataPrototype] = []

        # The includedDataTypeSet is used by a software component for its
        # implementation.
        self.includedDataTypeSets: List[IncludedDataTypeSet] = []

        # This aggregation represents the included Mode DeclarationGroups.
        self.includedModeDeclarationGroupSets: List[IncludedModeDeclarationGroupSet] = []

        # Within the context of a given SwComponentType some data def
        # properties of individual instantiations can be modified.
        self.instantiationDataDefProps: List[InstantiationDataDefProps] = []

        # Defines a per-instance memory object needed by this software
        # component.
        self.perInstanceMemories: List[PerInstanceMemory] = []

        # Defines parameter(s) or characteristic value(s) that needs to be
        # available for each instance of the software-component.
        self.perInstanceParameters: List[ParameterDataPrototype] = []

        # Options for generating the signature of port-related calls from a
        # runnable to the RTE and vice versa.
        self.portAPIOptions: List[PortAPIOption] = []

        # This is a RunnableEntity specified for the particular Swc
        # InternalBehavior.
        self.runnables: List[RunnableEntity] = []

        # Defines the requirements on AUTOSAR Services for a particular item.
        self.serviceDependencies: List[SwcServiceDependency] = []

        # Defines parameter(s) or characteristic value(s) shared between
        # SwComponentPrototypes of the same SwComponentType.
        self.sharedParameters: List[ParameterDataPrototype] = []

        # Indicate whether the corresponding software-component can be multiply
        # instantiated on one ECU. [constr_1935]
        self.supportsMultipleInstantiation: Optional[Boolean] = None

        # Proxy of a variation points in the C/C++ implementation.
        self.variationPointProxies: List[VariationPointProxy] = []

    def getArTypedPerInstanceMemories(self) -> List[VariableDataPrototype]:
        """Gets the AUTOSAR typed per-instance memory blocks owned by this behavior."""
        return self.arTypedPerInstanceMemories

    def createArTypedPerInstanceMemory(self, short_name: str) -> VariableDataPrototype:
        """Creates (or returns an existing) arTypedPerInstanceMemory registered to this behavior."""
        if not self.IsElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.arTypedPerInstanceMemories.append(prototype)
        return self.getElement(short_name, VariableDataPrototype)

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        """Gets the explicitInterRunnableVariables owned by this behavior."""
        return self.explicitInterRunnableVariables

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        """Creates (or returns an existing) explicitInterRunnableVariable registered to this behavior."""
        if not self.IsElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.explicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name, VariableDataPrototype)

    def getHandleTerminationAndRestart(self) -> Optional[ARLiteral]:
        """Gets handleTerminationAndRestart (stop/restart support of the AtomicSwComponentType)."""
        return self.handleTerminationAndRestart

    def setHandleTerminationAndRestart(self, value: Optional[ARLiteral]) -> "SwcInternalBehavior":
        """
        Sets handleTerminationAndRestart (stop/restart support of the
        AtomicSwComponentType). A None value is a no-op and does not overwrite
        an existing handleTerminationAndRestart.
        """
        if value is not None:
            self.handleTerminationAndRestart = value
        return self

    def getImplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        """Gets the implicitInterRunnableVariables owned by this behavior."""
        return self.implicitInterRunnableVariables

    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        """Creates (or returns an existing) implicitInterRunnableVariable registered to this behavior."""
        if not self.IsElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.implicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name, VariableDataPrototype)

    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        """Gets the perInstanceMemory objects owned by this behavior."""
        return self.perInstanceMemories

    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        """Creates (or returns an existing) perInstanceMemory registered to this behavior."""
        if not self.IsElementExists(short_name, PerInstanceMemory):
            memory = PerInstanceMemory(self, short_name)
            self.addElement(memory)
            self.perInstanceMemories.append(memory)
        return self.getElement(short_name, PerInstanceMemory)

    def getPerInstanceParameters(self) -> List[ParameterDataPrototype]:
        """Gets the perInstanceParameter objects owned by this behavior."""
        return self.perInstanceParameters

    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        """Creates (or returns an existing) perInstanceParameter registered to this behavior."""
        if not self.IsElementExists(short_name, ParameterDataPrototype):
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.perInstanceParameters.append(prototype)
        return self.getElement(short_name, ParameterDataPrototype)

    def getSharedParameters(self) -> List[ParameterDataPrototype]:
        """Gets the sharedParameter objects owned by this behavior."""
        return self.sharedParameters

    def createSharedParameter(self, short_name: str) -> ParameterDataPrototype:
        """Creates (or returns an existing) sharedParameter registered to this behavior."""
        if not self.IsElementExists(short_name, ParameterDataPrototype):
            memory = ParameterDataPrototype(self, short_name)
            self.addElement(memory)
            self.sharedParameters.append(memory)
        return self.getElement(short_name, ParameterDataPrototype)

    def addPortAPIOption(self, value: Optional[PortAPIOption]) -> "SwcInternalBehavior":
        """
        Adds a portAPIOption (options for generating port-related call signatures).
        A None value is a no-op and does not append to portAPIOptions.
        """
        if value is not None:
            self.portAPIOptions.append(value)
        return self

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        """Gets the portAPIOption objects owned by this behavior."""
        return self.portAPIOptions

    def addIncludedDataTypeSet(self, value: Optional[IncludedDataTypeSet]) -> "SwcInternalBehavior":
        """
        Adds an includedDataTypeSet used by the software component for its
        implementation. A None value is a no-op and does not append to
        includedDataTypeSets.
        """
        if value is not None:
            self.includedDataTypeSets.append(value)
        return self

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        """Gets the includedDataTypeSet objects owned by this behavior."""
        return self.includedDataTypeSets

    def addIncludedModeDeclarationGroupSet(self, value: Optional[IncludedModeDeclarationGroupSet]) -> "SwcInternalBehavior":
        """
        Adds an includedModeDeclarationGroupSet representing the included Mode
        DeclarationGroups. A None value is a no-op and does not append to
        includedModeDeclarationGroupSets.
        """
        if value is not None:
            self.includedModeDeclarationGroupSets.append(value)
        return self

    def getIncludedModeDeclarationGroupSets(self) -> List[IncludedModeDeclarationGroupSet]:
        """Gets the includedModeDeclarationGroupSet objects owned by this behavior."""
        return self.includedModeDeclarationGroupSets

    def addExclusiveAreaPolicy(self, value: Optional[SwcExclusiveAreaPolicy]) -> "SwcInternalBehavior":
        """
        Adds an exclusiveAreaPolicy (options how to generate the ExclusiveArea
        related APIs). A None value is a no-op and does not append to
        exclusiveAreaPolicies.
        """
        if value is not None:
            self.exclusiveAreaPolicies.append(value)
        return self

    def getExclusiveAreaPolicies(self) -> List[SwcExclusiveAreaPolicy]:
        """Gets the exclusiveAreaPolicy objects owned by this behavior."""
        return self.exclusiveAreaPolicies

    def createOperationInvokedEvent(self, short_name: str) -> OperationInvokedEvent:
        """Creates (or returns an existing) OperationInvokedEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, OperationInvokedEvent):
            event = OperationInvokedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, OperationInvokedEvent)

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        """Creates (or returns an existing) TimingEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, TimingEvent):
            event = TimingEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, TimingEvent)

    def createInitEvent(self, short_name: str) -> InitEvent:
        """Creates (or returns an existing) InitEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, InitEvent):
            event = InitEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, InitEvent)

    def createAsynchronousServerCallReturnsEvent(self, short_name: str) -> AsynchronousServerCallReturnsEvent:
        """Creates (or returns an existing) AsynchronousServerCallReturnsEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, AsynchronousServerCallReturnsEvent):
            event = AsynchronousServerCallReturnsEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, AsynchronousServerCallReturnsEvent)

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        """Creates (or returns an existing) DataReceivedEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, DataReceivedEvent):
            event = DataReceivedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, DataReceivedEvent)

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        """Creates (or returns an existing) SwcModeSwitchEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, SwcModeSwitchEvent):
            event = SwcModeSwitchEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, SwcModeSwitchEvent)

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        """Creates (or returns an existing) InternalTriggerOccurredEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, InternalTriggerOccurredEvent):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, InternalTriggerOccurredEvent)

    def createModeSwitchedAckEvent(self, short_name: str) -> ModeSwitchedAckEvent:
        """Creates (or returns an existing) ModeSwitchedAckEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, ModeSwitchedAckEvent):
            event = ModeSwitchedAckEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, ModeSwitchedAckEvent)

    def createBackgroundEvent(self, short_name: str) -> BackgroundEvent:
        """Creates (or returns an existing) BackgroundEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, BackgroundEvent):
            event = BackgroundEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, BackgroundEvent)

    def createDataSendCompletedEvent(self, short_name: str) -> DataSendCompletedEvent:
        """Creates (or returns an existing) DataSendCompletedEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name, DataSendCompletedEvent):
            event = DataSendCompletedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, DataSendCompletedEvent)

    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        """Creates (or returns an existing) SwcServiceDependency defining AUTOSAR Service requirements."""
        if not self.IsElementExists(short_name, SwcServiceDependency):
            event = SwcServiceDependency(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, SwcServiceDependency)

    def getRteEvents(self) -> List[RTEEvent]:
        """Gets all RTEEvents specified for this SwcInternalBehavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, RTEEvent), self.elements), key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        """Gets the OperationInvokedEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, OperationInvokedEvent), self.elements), key=lambda e: e.short_name)

    def getInitEvents(self) -> List[InitEvent]:
        """Gets the InitEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, InitEvent), self.elements), key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        """Gets the TimingEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, TimingEvent), self.elements), key=lambda e: e.short_name)

    def getDataReceivedEvents(self) -> List[DataReceivedEvent]:
        """Gets the DataReceivedEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, DataReceivedEvent), self.elements), key=lambda e: e.short_name)

    def getSwcModeSwitchEvents(self) -> List[SwcModeSwitchEvent]:
        """Gets the SwcModeSwitchEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, SwcModeSwitchEvent), self.elements), key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        """Gets the InternalTriggerOccurredEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, InternalTriggerOccurredEvent), self.elements), key=lambda e: e.short_name)

    def getModeSwitchedAckEvents(self) -> List[ModeSwitchedAckEvent]:
        """Gets the ModeSwitchedAckEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, ModeSwitchedAckEvent), self.elements), key=lambda e: e.short_name)

    def getBackgroundEvents(self) -> List[BackgroundEvent]:
        """Gets the BackgroundEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, BackgroundEvent), self.elements), key=lambda e: e.short_name)

    def getDataSendCompletedEvents(self) -> List[DataSendCompletedEvent]:
        """Gets the DataSendCompletedEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, DataSendCompletedEvent), self.elements), key=lambda e: e.short_name)

    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        """Gets the SwcServiceDependency objects defining AUTOSAR Service requirements, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, SwcServiceDependency), self.elements), key=lambda e: e.short_name)

    def getEvent(self, short_name: str) -> RTEEvent:
        """Gets the RTEEvent with the given short name from this behavior."""
        return self.getElement(short_name, RTEEvent)

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        """Gets all VariableDataPrototype instances owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements), key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        """Creates (or returns an existing) RunnableEntity specified for this SwcInternalBehavior."""
        if not self.IsElementExists(short_name, RunnableEntity):
            runnable = RunnableEntity(self, short_name)
            self.addElement(runnable)
        return self.getElement(short_name, RunnableEntity)

    def getRunnableEntities(self) -> List[RunnableEntity]:
        """Gets the RunnableEntity objects owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, RunnableEntity), self.elements), key=lambda r: r.short_name)

    def getRunnableEntity(self, short_name: str) -> RunnableEntity:
        """Gets the RunnableEntity with the given short name from this behavior."""
        return self.getElement(short_name, RunnableEntity)

    def getSupportsMultipleInstantiation(self) -> Optional[Boolean]:
        """
        Indicates whether the corresponding software-component can be multiply
        instantiated on one ECU.
        """
        return self.supportsMultipleInstantiation

    def setSupportsMultipleInstantiation(self, value: Optional[Boolean]) -> "SwcInternalBehavior":
        """
        Indicates whether the corresponding software-component can be multiply
        instantiated on one ECU. A None value is a no-op and does not overwrite
        an existing supportsMultipleInstantiation.
        """
        if value is not None:
            self.supportsMultipleInstantiation = value
        return self

    def addInstantiationDataDefProps(self, value: Optional[InstantiationDataDefProps]) -> "SwcInternalBehavior":
        """
        Adds an InstantiationDataDefProps applying additional SwDataDefProps to
        a particular instantiation. A None value is a no-op and does not append
        to instantiationDataDefProps.
        """
        if value is not None:
            self.instantiationDataDefProps.append(value)
        return self

    def getInstantiationDataDefPropss(self) -> List[InstantiationDataDefProps]:
        """Gets the InstantiationDataDefProps objects owned by this behavior."""
        return self.instantiationDataDefProps

    def addVariationPointProxy(self, value: Optional[VariationPointProxy]) -> "SwcInternalBehavior":
        """
        Adds a VariationPointProxy (proxy of a variation point in the C/C++
        implementation). A None value is a no-op and does not append to
        variationPointProxies.
        """
        if value is not None:
            self.variationPointProxies.append(value)
        return self

    def getVariationPointProxies(self) -> List[VariationPointProxy]:
        """Gets the VariationPointProxy objects owned by this behavior."""
        return self.variationPointProxies
